#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""market_calendar.py — 台股交易日曆(TWSE 開休市表 + 臨時休市公告 + TWSE/TPEx 實際成交日)。

rank_change 自動選週用它區分「週五休市」與「週五資料漏抓」;只讀 config/market_calendar.json,
不連網。status(day, as_of) 依序判定(給 as_of 時只用當時已知的資訊):
  * closed/weekend:週六、日。
  * trading/realized:as-of 前已取得(fetched_at)的 TWSE 與 TPEx 月成交資料都列有該日。
  * closed/announced:臨時休市公告(closures,announced_at ≤ as-of)。
  * closed/scheduled:TWSE 年度開休市表列為無交易。
  * closed/realized:兩所已取得的成交資料都略過該日、且其後已有共同成交日(該日落在
    已發布區間中間)。只到前一日的成交資料不能證明該日休市——只代表兩所列出相同日期。
  * trading/scheduled:開休市表涵蓋該年、未列休市、也沒有公告(尚未以實際成交核對)。
  * unknown:以上都沒涵蓋 → 無法確認,呼叫端必須明示。
年度開休市表沒有可比較的發布時間,視為該年開始前已公告;臨時休市一律要有 announced_at。

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


def _when(text):
    t = dt.datetime.fromisoformat(text)
    if t.tzinfo is None:
        raise CalendarError(f"時間必須帶時區:{text}")
    return t


class MarketCalendar:
    def __init__(self, data):
        self.data = data
        self.scheduled = {}
        for year, entry in data.get("announced", {}).items():
            for c in entry["closed"]:
                self.scheduled[c["date"]] = (f"{c['name']}(TWSE {year} 開休市表)", entry["source"])
        self.closures = {}
        for c in data.get("closures", []):
            if not c.get("announced_at"):
                raise CalendarError(f"臨時休市 {c['date']} 缺 announced_at,無法做 as-of 判斷")
            self.closures[c["date"]] = (_when(c["announced_at"]), c["reason"], c["source"])
        default = data.get("fetched_at")
        self.realized = []
        for month, e in sorted(data.get("realized", {}).items()):
            fetched = e.get("fetched_at") or default
            if not fetched:
                raise CalendarError(f"成交核對 {month} 缺 fetched_at,無法做 as-of 判斷")
            self.realized.append((month, _when(fetched), set(e["trading_days"]), e["sources"]))

    def coverage(self, as_of=None):
        seen = [r for r in self.realized if as_of is None or r[1] <= as_of]
        days = sorted(set().union(*(r[2] for r in seen))) if seen else []
        return (f"成交核對至 {days[-1]}" if days else "無成交核對") + \
            f";開休市表 {','.join(sorted(self.data.get('announced', {}))) or '無'}"

    def status(self, day, as_of=None):
        """{'state': trading|closed|unknown, 'basis': realized|announced|scheduled|weekend|None,
        'reason', 'source'};as_of(帶時區)只看當時已公告/已取得的資料。"""
        d = dt.date.fromisoformat(day)
        if d.weekday() >= 5:
            return {"state": "closed", "basis": "weekend", "reason": "週末", "source": None}
        seen = [r for r in self.realized if as_of is None or r[1] <= as_of]
        for month, _, days, sources in seen:
            if day in days:
                return {"state": "trading", "basis": "realized", "reason": "TWSE、TPEx 當日皆有成交",
                        "source": sources}
        c = self.closures.get(day)
        if c and (as_of is None or c[0] <= as_of):
            return {"state": "closed", "basis": "announced",
                    "reason": f"{c[1]};公告 {c[0].isoformat()}", "source": c[2]}
        if day in self.scheduled:
            reason, source = self.scheduled[day]
            return {"state": "closed", "basis": "scheduled", "reason": reason, "source": source}
        own = [r for r in seen if r[0] == day[:7]]
        later = sorted(x for r in seen for x in r[2] if x > day)
        if own and later:
            return {"state": "closed", "basis": "realized",
                    "reason": f"TWSE、TPEx 成交資料都略過此日(其後 {later[0]} 已有成交),無休市公告",
                    "source": own[0][3]}
        if day[:4] in self.data.get("announced", {}):
            note = "開休市表未列休市、無臨時休市公告(尚未以實際成交核對)"
            if own:
                note += f";兩所已取得的成交資料只到 {max(x for r in seen for x in r[2])},不能證明此日休市"
            return {"state": "trading", "basis": "scheduled", "reason": note,
                    "source": self.data["announced"][day[:4]]["source"]}
        return {"state": "unknown", "basis": None,
                "reason": f"交易日曆未涵蓋({self.coverage(as_of)})", "source": None}


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
    """重抓官方資料並改寫 config;每月記錄實際取得時間(fetched_at),臨時休市 closures 原樣保留。"""
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
        realized[f"{y}-{m:02d}"] = {"fetched_at": now.isoformat(timespec="seconds"),
                                    "trading_days": [d for d in twse if d < str(today)], "sources": sources}
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
    ap.add_argument("--as-of", help="帶時區 ISO 時間;--check 只用當時已公告/已取得的資料")
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
        as_of = _when(a.as_of) if a.as_of else None
        if as_of:
            out.append(f"as-of {as_of.isoformat()}")
        for day in a.check:
            st = cal.status(day, as_of)
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
