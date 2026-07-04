#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FinMind 五元素每日抓取 → SQLite 落地。
零第三方依賴(只用 Python 標準庫),方便本機排程或雲端 routine 搬運。

用法:
  # 增量(預設抓最近 15 天,補當日缺口)
  uv run --no-project python scripts/fetch_daily.py
  # 回補歷史(建立滾動視窗需要的基期)
  uv run --no-project python scripts/fetch_daily.py --start 2026-03-01 --end 2026-07-03

Token 讀取順序:環境變數 FINMIND_TOKEN → 專案根目錄 .mcp.json。
抓完會自動重算 daily_metrics(五元素衍生指標表)。
"""
import argparse, csv, json, os, sqlite3, sys, time
import urllib.parse, urllib.request
from datetime import date, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
UNIVERSE = os.path.join(ROOT, "config", "universe.csv")
API = "https://api.finmindtrade.com/api/v4/data"

DATASETS = ["TaiwanStockPrice", "TaiwanStockInstitutionalInvestorsBuySell",
            "TaiwanStockMarginPurchaseShortSale", "TaiwanStockShareholding"]

SCHEMA = """
CREATE TABLE IF NOT EXISTS universe(stock_id TEXT PRIMARY KEY, name TEXT, grp TEXT);
CREATE TABLE IF NOT EXISTS price(date TEXT, stock_id TEXT, open REAL, high REAL, low REAL,
  close REAL, volume INTEGER, amount REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS inst(date TEXT, stock_id TEXT, foreign_net INTEGER, trust_net INTEGER,
  dealer_net INTEGER, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS margin(date TEXT, stock_id TEXT, margin_bal INTEGER, short_bal INTEGER,
  PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS holding(date TEXT, stock_id TEXT, foreign_pct REAL, shares_issued INTEGER,
  PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS fetch_log(ts TEXT, start TEXT, "end" TEXT, rows INTEGER);
"""

def get_token():
    t = os.environ.get("FINMIND_TOKEN")
    if t:
        return t
    with open(os.path.join(ROOT, ".mcp.json"), encoding="utf-8") as f:
        return json.load(f)["mcpServers"]["finmind"]["env"]["FINMIND_TOKEN"]

def api_get(dataset, data_id, start, end, token, retries=3):
    q = urllib.parse.urlencode({"dataset": dataset, "data_id": data_id,
                                "start_date": start, "end_date": end})
    url = API + "?" + q
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"Authorization": "Bearer " + token})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp).get("data", [])
        except Exception as e:
            if i == retries - 1:
                print(f"  ! {dataset} {data_id} 失敗: {e}", file=sys.stderr)
                return []
            time.sleep(2 * (i + 1))  # 遇限流退避重試
    return []

def load_universe(con):
    rows = []
    with open(UNIVERSE, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append((r["stock_id"].strip(), r["name"].strip(), r["group"].strip()))
    con.executemany("INSERT OR REPLACE INTO universe VALUES(?,?,?)", rows)
    return [r[0] for r in rows]

def up_price(con, data):
    rows = [(d["date"], d["stock_id"], d.get("open"), d.get("max"), d.get("min"),
             d.get("close"), d.get("Trading_Volume"), d.get("Trading_money")) for d in data]
    con.executemany("INSERT OR REPLACE INTO price VALUES(?,?,?,?,?,?,?,?)", rows)
    return len(rows)

def up_inst(con, data):
    # 把三大法人各分項的 buy-sell 匯總成 外資 / 投信 / 自營 淨額(股數)
    agg = {}
    for d in data:
        key = (d["date"], d["stock_id"])
        a = agg.setdefault(key, {"f": 0, "t": 0, "dl": 0})
        net = (d.get("buy") or 0) - (d.get("sell") or 0)
        nm = d.get("name", "")
        if nm == "Foreign_Investor":
            a["f"] += net
        elif nm == "Investment_Trust":
            a["t"] += net
        elif nm in ("Dealer_self", "Dealer_Hedging"):
            a["dl"] += net
    rows = [(k[0], k[1], v["f"], v["t"], v["dl"]) for k, v in agg.items()]
    con.executemany("INSERT OR REPLACE INTO inst VALUES(?,?,?,?,?)", rows)
    return len(rows)

def up_margin(con, data):
    rows = [(d["date"], d["stock_id"], d.get("MarginPurchaseTodayBalance"),
             d.get("ShortSaleTodayBalance")) for d in data]
    con.executemany("INSERT OR REPLACE INTO margin VALUES(?,?,?,?)", rows)
    return len(rows)

def up_holding(con, data):
    rows = [(d["date"], d["stock_id"], d.get("ForeignInvestmentSharesRatio"),
             d.get("NumberOfSharesIssued")) for d in data]
    con.executemany("INSERT OR REPLACE INTO holding VALUES(?,?,?,?)", rows)
    return len(rows)

UPSERT = {"TaiwanStockPrice": up_price, "TaiwanStockInstitutionalInvestorsBuySell": up_inst,
          "TaiwanStockMarginPurchaseShortSale": up_margin, "TaiwanStockShareholding": up_holding}

def build_metrics(con):
    """由原始表重算五元素衍生指標(純 Python 滾動,穩健)。整表重建,可重複執行。"""
    con.execute("DROP TABLE IF EXISTS daily_metrics")
    con.execute("""CREATE TABLE daily_metrics(
        date TEXT, stock_id TEXT, close REAL, ret1 REAL,
        turnover_pct REAL,            -- ②量:周轉率 = 量/發行股數
        dist_hi20 REAL, dist_hi60 REAL, -- ①價:距 20/60 日高
        foreign_pct REAL, fpct_chg5 REAL, fpct_chg20 REAL,  -- ③外資:持股% 與變化(pp)
        trust5 INTEGER, foreign5 INTEGER,                   -- ④投信/外資:近5日淨額(張)
        margin_bal INTEGER, margin_util_pct REAL,
        margin_chg5 REAL, margin_chg10 REAL, margin_chg20 REAL,  -- ⑤散戶:水位 + 5/10/20 日融資變化
        short_margin_ratio REAL,                            -- ⑤券資比(%)
        PRIMARY KEY(date, stock_id))""")
    ids = [r[0] for r in con.execute("SELECT stock_id FROM universe")]
    for sid in ids:
        si = con.execute("SELECT shares_issued FROM holding WHERE stock_id=? AND shares_issued IS NOT NULL "
                         "ORDER BY date DESC LIMIT 1", (sid,)).fetchone()
        shares = si[0] if si else None
        rows = con.execute("""SELECT p.date, p.close, p.volume, h.foreign_pct, m.margin_bal, m.short_bal,
                                     i.trust_net, i.foreign_net
                              FROM price p
                              LEFT JOIN holding h ON h.date=p.date AND h.stock_id=p.stock_id
                              LEFT JOIN margin  m ON m.date=p.date AND m.stock_id=p.stock_id
                              LEFT JOIN inst    i ON i.date=p.date AND i.stock_id=p.stock_id
                              WHERE p.stock_id=? ORDER BY p.date""", (sid,)).fetchall()
        closes = [r[1] for r in rows]
        fpct = [r[3] for r in rows]
        mbal = [r[4] for r in rows]
        trust = [r[6] or 0 for r in rows]
        fnet = [r[7] or 0 for r in rows]
        out = []
        for k, r in enumerate(rows):
            d, close, vol, fp, mb, sb, _tn, _fn = r
            ret1 = (close / closes[k-1] - 1) if k > 0 and closes[k-1] else None
            win20 = [c for c in closes[max(0, k-19):k+1] if c is not None]
            win60 = [c for c in closes[max(0, k-59):k+1] if c is not None]
            hi20 = max(win20) if win20 else None
            hi60 = max(win60) if win60 else None
            turnover = (vol / shares * 100) if (vol and shares) else None
            fchg5 = (fp - fpct[k-5]) if (k >= 5 and fp is not None and fpct[k-5] is not None) else None
            fchg20 = (fp - fpct[k-20]) if (k >= 20 and fp is not None and fpct[k-20] is not None) else None
            trust5 = round(sum(trust[max(0, k-4):k+1]) / 1000)   # 張
            foreign5 = round(sum(fnet[max(0, k-4):k+1]) / 1000)  # 張
            mutil = (mb * 1000 / shares * 100) if (mb and shares) else None
            mchg5 = (mb / mbal[k-5] - 1) if (k >= 5 and mbal[k-5]) else None
            mchg10 = (mb / mbal[k-10] - 1) if (k >= 10 and mbal[k-10]) else None
            mchg20 = (mb / mbal[k-20] - 1) if (k >= 20 and mbal[k-20]) else None
            smr = (sb / mb * 100) if (sb is not None and mb) else None
            out.append((d, sid, close, ret1, turnover,
                        (close/hi20 - 1) if hi20 else None, (close/hi60 - 1) if hi60 else None,
                        fp, fchg5, fchg20, trust5, foreign5, mb, mutil, mchg5, mchg10, mchg20, smr))
        con.executemany("INSERT OR REPLACE INTO daily_metrics VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", out)
    con.commit()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", help="YYYY-MM-DD;省略則抓最近 --days 天")
    ap.add_argument("--end", help="YYYY-MM-DD;預設今天")
    ap.add_argument("--days", type=int, default=15)
    ap.add_argument("--sleep", type=float, default=0.25, help="每次 API 間隔秒數(避免限流)")
    ap.add_argument("--metrics-only", action="store_true", help="不抓取,只用現有原始表重算 daily_metrics")
    args = ap.parse_args()

    if args.metrics_only:
        con = sqlite3.connect(DB)
        con.executescript(SCHEMA)
        load_universe(con)
        con.commit()
        print("只重算 daily_metrics(不抓取)…")
        build_metrics(con)
        n = con.execute("SELECT COUNT(*) FROM daily_metrics").fetchone()[0]
        con.close()
        print(f"完成 — daily_metrics {n} rows")
        return

    end = args.end or date.today().isoformat()
    start = args.start or (date.today() - timedelta(days=args.days)).isoformat()

    token = get_token()
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    con = sqlite3.connect(DB)
    con.executescript(SCHEMA)
    ids = load_universe(con)
    con.commit()
    print(f"抓取 {start} .. {end} · {len(ids)} 檔 · 4 datasets")
    total = 0
    for i, sid in enumerate(ids, 1):
        got = 0
        for ds in DATASETS:
            data = api_get(ds, sid, start, end, token)
            if data:
                got += UPSERT[ds](con, data)
            time.sleep(args.sleep)
        total += got
        con.commit()
        print(f"[{i:>2}/{len(ids)}] {sid} · {got} rows")
    con.execute('INSERT INTO fetch_log VALUES(datetime("now"),?,?,?)', (start, end, total))
    con.commit()
    print("重算 daily_metrics …")
    build_metrics(con)
    n = con.execute("SELECT COUNT(*) FROM daily_metrics").fetchone()[0]
    con.close()
    print(f"完成 — 原始 {total} rows 落地,daily_metrics {n} rows → {DB}")

if __name__ == "__main__":
    main()
