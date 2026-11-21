#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""market_calendar.py — 台股交易日曆(TWSE 開休市表 + TWSE/TPEx 實際成交日核對)。

rank_change 自動選週用它區分「週五休市」與「週五資料漏抓」;只讀 config/market_calendar.json,
不連網。日期狀態:
  * closed:週末、開休市表列為無交易,或已核對月份中 TWSE 與 TPEx 都沒有該日成交。
  * trading:已核對月份中 TWSE 與 TPEx 都有該日成交(realized),
    或尚未核對、但開休市表涵蓋該年且未列為休市(scheduled;臨時休市要 --refresh 才知道)。
  * unknown:開休市表與成交核對都沒涵蓋 → 無法確認,呼叫端必須明示。

用法(repo 根目錄):
  python scripts/market_calendar.py --check 2026-10-23            # 離線讀 config,列出狀態與來源
  python scripts/market_calendar.py --verify-online 2026-10-23    # 連交易所官方 API 重查該日
  python scripts/market_calendar.py --refresh                     # 重抓官方資料並改寫 config(手動)
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CALENDAR = os.path.join(ROOT, "config", "market_calendar.json")
TAIPEI_TZ = dt.timezone(dt.timedelta(hours=8))
FIRST_MONTH = "2026-03"          # fetch_daily.HISTORY_FLOOR 所在月份
URL_HOLIDAY = "https://www.twse.com.tw/rwd/zh/holidaySchedule/holidaySchedule?date={y}0101&response=json"
URL_TWSE = "https://www.twse.com.tw/rwd/zh/afterTrading/FMTQIK?date={y}{m:02d}01&response=json"
URL_TPEX = "https://www.tpex.org.tw/www/zh-tw/afterTrading/tradingIndex?date={y}%2F{m:02d}%2F01&response=json"
OPEN_WORDS = ("開始交易", "最後交易")     # 開休市表中這兩類列是「有交易」的提示,不是休市


class CalendarError(RuntimeError):
    pass


def _roc(text):
    y, m, d = (int(x) for x in text.strip().split("/"))
    return str(dt.date(y + 1911, m, d))


class MarketCalendar:
    def __init__(self, data):
        self.data = data
        self.closures = {}
        for year, entry in data.get("announced", {}).items():
            for c in entry["closed"]:
                self.closures[c["date"]] = (f"{c['name']}(TWSE {year} 開休市表)", entry["source"])
        for c in data.get("closures", []):
            self.closures[c["date"]] = (c["reason"], c["source"])
        self.realized = {m: (e["covered_through"], set(e["trading_days"]), e)
                         for m, e in data.get("realized", {}).items()}

    def coverage(self):
        months = sorted(self.realized)
        thru = self.realized[months[-1]][0] if months else None
        return (f"成交核對 {months[0]}~{thru}" if months else "無成交核對") + \
            f";開休市表 {','.join(sorted(self.data.get('announced', {}))) or '無'}"

    def status(self, day):
        """{'state': trading|closed|unknown, 'basis': realized|scheduled|weekend|None, 'reason', 'source'}"""
        d = dt.date.fromisoformat(day)
        if d.weekday() >= 5:
            return {"state": "closed", "basis": "weekend", "reason": "週末", "source": None}
        real = self.realized.get(day[:7])
        if real and day <= real[0]:
            if day in real[1]:
                return {"state": "trading", "basis": "realized", "reason": "TWSE、TPEx 當日皆有成交",
                        "source": real[2]["sources"]}
            reason, source = self.closures.get(day, ("TWSE、TPEx 當月成交資料皆無此日", real[2]["sources"]))
            return {"state": "closed", "basis": "realized", "reason": reason, "source": source}
        if day in self.closures:
            reason, source = self.closures[day]
            return {"state": "closed", "basis": "scheduled", "reason": reason, "source": source}
        if day[:4] in self.data.get("announced", {}):
            return {"state": "trading", "basis": "scheduled",
                    "reason": "開休市表未列休市(尚未以實際成交核對)",
                    "source": self.data["announced"][day[:4]]["source"]}
        return {"state": "unknown", "basis": None, "reason": f"交易日曆未涵蓋({self.coverage()})", "source": None}


def load(path=CALENDAR):
    with open(path, encoding="utf-8") as fh:
        return MarketCalendar(json.load(fh))


# ── 官方資料抓取(只在 --refresh / --verify-online 用) ─────────────────
def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        raw = resp.read()
    return json.loads(raw.decode("utf-8")), hashlib.sha256(raw).hexdigest()


def fetch_holidays(year):
    url = URL_HOLIDAY.format(y=year)
    body, sha = _get(url)
    if str(body.get("stat", "")).lower() != "ok":
        raise CalendarError(f"{url} stat={body.get('stat')}")
    closed = [{"date": r[0], "name": r[1]} for r in body["data"]
              if dt.date.fromisoformat(r[0]).weekday() < 5 and not any(w in r[1] for w in OPEN_WORDS)]
    return {"title": body.get("title"), "source": url, "sha256": sha, "closed": closed}


def fetch_month(year, month):
    """回傳 (TWSE 成交日, TPEx 成交日, 來源);兩邊都是官方當月逐日成交彙總。"""
    tw, tw_sha = _get(URL_TWSE.format(y=year, m=month))
    if str(tw.get("stat", "")).lower() != "ok":
        raise CalendarError(f"TWSE FMTQIK {year}-{month:02d} stat={tw.get('stat')}")
    tp, tp_sha = _get(URL_TPEX.format(y=year, m=month))
    tables = tp.get("tables") or []
    if not tables or "data" not in tables[0]:
        raise CalendarError(f"TPEx tradingIndex {year}-{month:02d} 無資料表")
    twse = sorted(_roc(r[0]) for r in tw.get("data", []))
    tpex = sorted(_roc(r[0]) for r in tables[0]["data"])
    return twse, tpex, [{"url": URL_TWSE.format(y=year, m=month), "sha256": tw_sha},
                        {"url": URL_TPEX.format(y=year, m=month), "sha256": tp_sha}]


def _months(first, last):
    y, m = (int(x) for x in first.split("-"))
    while (y, m) <= last:
        yield y, m
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def refresh(path=CALENDAR, now=None):
    now = now or dt.datetime.now(TAIPEI_TZ)
    old = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
    today = now.date()
    announced = {}
    for y in range(int(FIRST_MONTH[:4]), today.year + 2):
        try:
            h = fetch_holidays(y)
        except CalendarError:
            continue
        if h["closed"] or y <= today.year:
            announced[str(y)] = h
    realized = {}
    for y, m in _months(FIRST_MONTH, (today.year, today.month)):
        twse, tpex, sources = fetch_month(y, m)
        if twse != tpex:
            raise CalendarError(f"{y}-{m:02d} TWSE 與 TPEx 成交日不一致:只在 TWSE {sorted(set(twse) - set(tpex))}、"
                                f"只在 TPEx {sorted(set(tpex) - set(twse))}")
        end = (dt.date(y + (m == 12), m % 12 + 1, 1) - dt.timedelta(days=1))
        thru = min(end, today - dt.timedelta(days=1))
        realized[f"{y}-{m:02d}"] = {"covered_through": str(thru), "trading_days": [d for d in twse if d <= str(thru)],
                                    "sources": sources}
    data = {"schema": 1, "fetched_at": now.isoformat(timespec="seconds"),
            "note": "TWSE 開休市表 + TWSE FMTQIK/TPEx tradingIndex 實際成交日;由 market_calendar.py --refresh 產生",
            "announced": announced, "closures": old.get("closures", []), "realized": realized}
    with open(path, "wb") as fh:
        fh.write((json.dumps(data, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))
    return data


def verify_online(day):
    d = dt.date.fromisoformat(day)
    twse, tpex, sources = fetch_month(d.year, d.month)
    h = fetch_holidays(d.year)
    listed = [c["name"] for c in h["closed"] if c["date"] == day]
    lines = [f"{day}(週{'一二三四五六日'[d.weekday()]})",
             f"  TWSE {d.year}-{d.month:02d} 成交日 {len(twse)} 天,含 {day}:{day in twse}",
             f"  TPEx {d.year}-{d.month:02d} 成交日 {len(tpex)} 天,含 {day}:{day in tpex}",
             f"  TWSE 開休市表({h['title']})列為休市:{listed or '否'}"]
    for c in load().data.get("closures", []):
        if c["date"] == day and "newsDetail" in c.get("source", ""):
            body, sha = _get(c["source"])
            title = ((body.get("tables") or [{}])[0]).get("title")
            lines.append(f"  TWSE 公告({body.get('date')}):{title}")
            sources.append({"url": c["source"], "sha256": sha})
    lines += [f"  來源 {s['url']} sha256={s['sha256']}" for s in sources]
    lines.append(f"  來源 {h['source']} sha256={h['sha256']}")
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", nargs="+", metavar="日期")
    ap.add_argument("--verify-online", metavar="日期")
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--path", default=CALENDAR)
    a = ap.parse_args(argv)
    out = []
    if a.refresh:
        data = refresh(a.path)
        out.append(f"已更新 {a.path}:{MarketCalendar(data).coverage()}")
    if a.verify_online:
        out.append(verify_online(a.verify_online))
    if a.check:
        cal = load(a.path)
        for day in a.check:
            st = cal.status(day)
            out.append(f"{day} {st['state']}({st['basis']}):{st['reason']}")
            src = st["source"]
            for s in (src if isinstance(src, list) else [src] if src else []):
                out.append(f"  來源 {s['url'] if isinstance(s, dict) else s}")
    if not out:
        ap.error("請給 --check、--verify-online 或 --refresh")
    sys.stdout.buffer.write(("\n".join(out) + "\n").encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
