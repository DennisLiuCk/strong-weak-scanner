#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TDCC 集保戶股權分散表(週頻)→ SQLite 落地(tdcc_holding,append-only 跨週累積)。
零第三方依賴。資料源:TDCC opendata(免 token,非 FinMind)。

⚠ opendata 只提供「最新一週」快照(週五結算、週六公布),歷史不可回補——每缺一週
   = 永久洞。因此本腳本掛在每日管線 fetch_daily 之前(週一~五各重抓一次 = 5 次保險),
   任何失敗只 stderr 示警、exit 0,不擋後續 FinMind 抓取。
儲存範圍 = universe.csv ∪ candidates.csv(候選股先累積歷史,季度納入後才有回溯資料)。
級距語義:1~15 = 持股分級(12~15 = 400 張以上、15 = 1000 張以上)、16 = 差異數調整、
17 = 合計;pct 分母是「集保庫存」、非發行股本(與 foreign_pct 不同尺)。
衍生欄位(tdcc_big400_pct 等)由 fetch_daily.build_metrics 以 T−TDCC_LAG_DAYS 生效規則計算。
"""
import csv, io, os, sqlite3, sys, time, urllib.request

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
UNIVERSE = os.path.join(ROOT, "config", "universe.csv")
CANDIDATES = os.path.join(ROOT, "config", "candidates.csv")
TDCC_URL = "https://opendata.tdcc.com.tw/getOD.ashx?id=1-5"
LEVELS_FULL = 17   # 每檔每週應有的級距列數(1~15 + 16 差異調整 + 17 合計)

SCHEMA = """CREATE TABLE IF NOT EXISTS tdcc_holding(
    date TEXT, stock_id TEXT, level INTEGER, people INTEGER, shares INTEGER, pct REAL,
    PRIMARY KEY(date, stock_id, level))"""


def read_ids(path):
    """讀 csv 的 stock_id 欄;檔案不存在或只有表頭(候選池常態為空)都回空集合。"""
    ids = set()
    if not os.path.exists(path):
        return ids
    with open(path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            sid = (r.get("stock_id") or "").strip()
            if sid:
                ids.add(sid)
    return ids


def download(retries=2):
    for i in range(retries):
        try:
            req = urllib.request.Request(TDCC_URL, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=120) as resp:
                return resp.read().decode("utf-8-sig")
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(5)


def main():
    try:
        text = download()
    except Exception as e:
        print(f"  ! TDCC opendata 下載失敗:{e}——本次略過(同週每日 run 會再試)", file=sys.stderr)
        sys.exit(0)

    uni = read_ids(UNIVERSE)
    keep = uni | read_ids(CANDIDATES)
    rows, lv_count = [], {}
    try:
        for r in csv.DictReader(io.StringIO(text)):
            sid = r["證券代號"].strip()
            if sid not in keep:
                continue
            raw = r["資料日期"].strip()
            d = f"{raw[:4]}-{raw[4:6]}-{raw[6:]}"   # 20260703 → 2026-07-03
            rows.append((d, sid, int(r["持股分級"]), int(r["人數"]), int(r["股數"]),
                         float(r["占集保庫存數比例%"])))
            lv_count[(d, sid)] = lv_count.get((d, sid), 0) + 1
    except Exception as e:
        print(f"  ! TDCC CSV 解析失敗(格式變更?):{e}——本次略過", file=sys.stderr)
        sys.exit(0)
    if not rows:
        print("  ! TDCC CSV 無 universe/候選股資料——請人工檢查欄位或代號格式", file=sys.stderr)
        sys.exit(0)

    got = {sid for (_, sid) in lv_count}
    for sid in sorted(uni - got):   # 只對 universe 成員缺席示警(候選股缺席可能屬正常)
        print(f"  ! TDCC 快照缺 universe 成員 {sid}", file=sys.stderr)
    for (d, sid), n in sorted(lv_count.items()):
        if n != LEVELS_FULL:
            print(f"  ! TDCC {sid} {d} 級距不全({n}/{LEVELS_FULL} 列)", file=sys.stderr)

    con = sqlite3.connect(DB)
    con.execute(SCHEMA)
    con.executemany("INSERT OR REPLACE INTO tdcc_holding VALUES(?,?,?,?,?,?)", rows)
    con.commit()
    weeks = con.execute("SELECT COUNT(DISTINCT date) FROM tdcc_holding").fetchone()[0]
    con.close()
    dates = sorted({d for (d, _) in lv_count})
    print(f"TDCC 股權分散:快照 {'、'.join(dates)} · {len(got)} 檔 {len(rows)} 列 · 表內累積 {weeks} 週")


if __name__ == "__main__":
    main()
