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
價格類指標(ret1/距高)用還原股價 price_adj。FinMind 的 TaiwanStockPriceAdj 免費層不可用
(需 Sponsor),所以改抓 TaiwanStockDividendResult + TaiwanStockSplitPrice(皆免費),
本地以倒推法重算還原價(事件日前的歷史價 × 係數連乘,最新區段==原始價)。
減資參考價 dataset 需付費、未涵蓋——由「無事件大跳空」偵測示警兜底。
price_adj 每次整表重建、冪等;原始 price 表維持 append-only 不動。
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
CREATE TABLE IF NOT EXISTS dividend_result(date TEXT, stock_id TEXT, before_price REAL,
  reference_price REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS split_event(date TEXT, stock_id TEXT, before_price REAL,
  after_price REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS price_adj(date TEXT, stock_id TEXT, close REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS fetch_log(ts TEXT, start TEXT, "end" TEXT, rows INTEGER);
"""

def get_token():
    t = os.environ.get("FINMIND_TOKEN")
    if t:
        return t
    with open(os.path.join(ROOT, ".mcp.json"), encoding="utf-8") as f:
        return json.load(f)["mcpServers"]["finmind"]["env"]["FINMIND_TOKEN"]

def api_get(dataset, data_id, start, end, token, retries=3):
    p = {"dataset": dataset, "start_date": start, "end_date": end}
    if data_id:
        p["data_id"] = data_id          # 部分 dataset(如 TaiwanStockSplitPrice)全市場一次回傳
    q = urllib.parse.urlencode(p)
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
    con.execute("DELETE FROM universe")   # 從 csv 整表重建:移除的股票不再殭屍重算
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

def fetch_dividends(con, ids, token, start, end, sleep):
    """除權息結果 → dividend_result(upsert)。事件稀疏,整段視窗抓也便宜(payload 極小,
    抓全視窗才能保證「price 涵蓋範圍內的事件都在庫」,回補舊價也不會留缺口)。"""
    n = 0
    for sid in ids:
        data = api_get("TaiwanStockDividendResult", sid, start, end, token)
        rows = [(d["date"], d["stock_id"], d.get("before_price"), d.get("reference_price"))
                for d in data if d.get("before_price") and d.get("reference_price")]
        if rows:
            con.executemany("INSERT OR REPLACE INTO dividend_result VALUES(?,?,?,?)", rows)
            n += len(rows)
        con.commit()
        time.sleep(sleep)
    return n

def fetch_splits(con, ids, token, start, end, sleep):
    """股票分割/反分割參考價 → split_event(upsert)。此 dataset 免 data_id、全市場一次回傳,
    只留 universe 內的股票。"""
    data = api_get("TaiwanStockSplitPrice", None, start, end, token)
    keep = set(ids)
    rows = [(d["date"], d["stock_id"], d.get("before_price"), d.get("after_price"))
            for d in data if d.get("stock_id") in keep and d.get("before_price") and d.get("after_price")]
    if rows:
        con.executemany("INSERT OR REPLACE INTO split_event VALUES(?,?,?,?)", rows)
        con.commit()
    time.sleep(sleep)
    return len(rows)

def build_price_adj(con):
    """由 price × 事件係數重算還原價(倒推法:事件日「之前」的價 × 係數連乘,最新區段==原始價)。
    事件來源:dividend_result(date=除息「交易日」、before_price=前一交易日收盤——已對 10 筆實際
    事件逐一驗證;係數 reference/before 必然 <=1)+ split_event(分割/反分割,係數 after/before
    可 >1)。減資參考價 dataset 需付費、未涵蓋 → 靠下方「無事件大跳空」偵測示警。
    整表重建、冪等;無事件時 price_adj == price。異常事件一律 stderr 示警、不靜默。"""
    con.execute("DELETE FROM price_adj")
    for (sid,) in con.execute("SELECT stock_id FROM universe").fetchall():
        evs = []   # (事件日, 係數, 事件前收盤)
        for d, bp, rp in con.execute("SELECT date, before_price, reference_price FROM dividend_result "
                                     "WHERE stock_id=?", (sid,)).fetchall():
            f = (rp / bp) if (bp and rp) else None
            if f is None or not (0 < f <= 1.02):
                print(f"  ! {sid} {d} 除權息係數異常 ({bp}->{rp}),略過該事件", file=sys.stderr)
                continue
            evs.append((d, f, bp))
        for d, bp, ap in con.execute("SELECT date, before_price, after_price FROM split_event "
                                     "WHERE stock_id=?", (sid,)).fetchall():
            f = (ap / bp) if (bp and ap) else None
            if f is None or not (0.05 <= f <= 20):
                print(f"  ! {sid} {d} 分割係數異常 ({bp}->{ap}),略過該事件", file=sys.stderr)
                continue
            evs.append((d, f, bp))
        rows = con.execute("SELECT date, close FROM price WHERE stock_id=? ORDER BY date", (sid,)).fetchall()
        for ed, _f, bp in evs:   # 對帳:事件 before_price 應==前一交易日收盤,不符=日期語義漂移
            prev = next((c for d2, c in reversed(rows) if d2 < ed and c is not None), None)
            if prev and bp and abs(prev - bp) / bp > 0.01:
                print(f"  ! {sid} {ed} before_price {bp} != 前日收盤 {prev},請查事件日期語義", file=sys.stderr)
        ev_dates = {e[0] for e in evs}
        out, prev_c = [], None
        for d, c in rows:
            if c is None:
                continue
            if prev_c and abs(c / prev_c - 1) > 0.15 and d not in ev_dates:   # 台股漲跌幅 ±10%
                print(f"  ! {sid} {d} 原始價跳空 {c/prev_c-1:+.0%} 且無已知事件——疑似減資/缺事件,"
                      f"還原價未修正", file=sys.stderr)
            prev_c = c
            f = 1.0
            for ed, ef, _bp in evs:
                if ed > d:
                    f *= ef
            out.append((d, sid, round(c * f, 4)))
        con.executemany("INSERT OR REPLACE INTO price_adj VALUES(?,?,?)", out)
    miss = con.execute("""SELECT COUNT(*) FROM price p JOIN universe u USING(stock_id)
                          LEFT JOIN price_adj a ON a.date=p.date AND a.stock_id=p.stock_id
                          WHERE p.close IS NOT NULL AND a.close IS NULL""").fetchone()[0]
    if miss:
        print(f"  ! price_adj 缺 {miss} 列(metrics 將以原始價替代——不應發生,請檢查)", file=sys.stderr)
    con.commit()

def build_metrics(con):
    """由原始表重算五元素衍生指標(純 Python 滾動,穩健)。整表重建,可重複執行。
    價格類(ret1/距高)用還原價;股本取「當日」值(forward-fill),避免用最新股本回填歷史造成前視。"""
    con.execute("DROP TABLE IF EXISTS daily_metrics")
    con.execute("""CREATE TABLE daily_metrics(
        date TEXT, stock_id TEXT, close REAL, close_adj REAL, ret1 REAL,
        turnover_pct REAL,            -- ②量:周轉率 = 量/當日發行股數
        dist_hi20 REAL, dist_hi60 REAL, -- ①價:距 20/60 日高(還原價)
        foreign_pct REAL, fpct_chg5 REAL, fpct_chg20 REAL,  -- ③外資:持股% 與變化(pp)
        trust5 INTEGER, trust5_pct REAL, foreign5 INTEGER,  -- ④投信/外資:近5日淨額(張;投信另存佔股本%)
        margin_bal INTEGER, margin_util_pct REAL,
        margin_chg5 REAL, margin_chg10 REAL, margin_chg20 REAL,  -- ⑤散戶:水位 + 5/10/20 日融資變化
        short_margin_ratio REAL,                            -- ⑤券資比(%)
        PRIMARY KEY(date, stock_id))""")
    ids = [r[0] for r in con.execute("SELECT stock_id FROM universe")]
    for sid in ids:
        rows = con.execute("""SELECT p.date, p.close, p.volume, h.foreign_pct, m.margin_bal, m.short_bal,
                                     i.trust_net, i.foreign_net, h.shares_issued, pa.close
                              FROM price p
                              LEFT JOIN holding h ON h.date=p.date AND h.stock_id=p.stock_id
                              LEFT JOIN margin  m ON m.date=p.date AND m.stock_id=p.stock_id
                              LEFT JOIN inst    i ON i.date=p.date AND i.stock_id=p.stock_id
                              LEFT JOIN price_adj pa ON pa.date=p.date AND pa.stock_id=p.stock_id
                              WHERE p.stock_id=? ORDER BY p.date""", (sid,)).fetchall()
        adj = [(r[9] if r[9] is not None else r[1]) for r in rows]  # 還原價;缺值退回原始價
        fpct = [r[3] for r in rows]
        mbal = [r[4] for r in rows]
        trust = [r[6] or 0 for r in rows]
        fnet = [r[7] or 0 for r in rows]
        sh = [r[8] for r in rows]   # 股本逐日 forward-fill,0/None 都視為缺值;
        prev = next((x for x in sh if x), None)   # 種子=第一筆已知 → 最前段以其回填(輕微前視,僅及 holding 起點前)
        for k in range(len(sh)):
            if sh[k]:
                prev = sh[k]
            else:
                sh[k] = prev
        out = []
        for k, r in enumerate(rows):
            d, close, vol, fp, mb, sb = r[0], r[1], r[2], r[3], r[4], r[5]
            shares, ca = sh[k], adj[k]
            ret1 = (ca / adj[k-1] - 1) if (k > 0 and adj[k-1] and ca) else None
            win20 = [c for c in adj[max(0, k-19):k+1] if c is not None]
            win60 = [c for c in adj[max(0, k-59):k+1] if c is not None]
            hi20 = max(win20) if len(win20) >= 10 else None    # 冷啟動保護:視窗樣本不足時
            hi60 = max(win60) if len(win60) >= 30 else None    # 不給「距高」,避免上市/新增股假新高
            turnover = (vol / shares * 100) if (vol is not None and shares) else None  # vol=0 → 0%(量縮),非缺值
            fchg5 = (fp - fpct[k-5]) if (k >= 5 and fp is not None and fpct[k-5] is not None) else None
            fchg20 = (fp - fpct[k-20]) if (k >= 20 and fp is not None and fpct[k-20] is not None) else None
            t5 = sum(trust[max(0, k-4):k+1])
            trust5 = round(t5 / 1000)                             # 張
            trust5_pct = (t5 / shares * 100) if shares else None  # 佔股本 %
            foreign5 = round(sum(fnet[max(0, k-4):k+1]) / 1000)   # 張
            mutil = (mb * 1000 / shares * 100) if (mb and shares) else None
            mchg5 = (mb / mbal[k-5] - 1) if (mb is not None and k >= 5 and mbal[k-5]) else None
            mchg10 = (mb / mbal[k-10] - 1) if (mb is not None and k >= 10 and mbal[k-10]) else None
            mchg20 = (mb / mbal[k-20] - 1) if (mb is not None and k >= 20 and mbal[k-20]) else None
            smr = (sb / mb * 100) if (sb is not None and mb) else None
            out.append((d, sid, close, ca, ret1, turnover,
                        (ca/hi20 - 1) if (hi20 and ca) else None, (ca/hi60 - 1) if (hi60 and ca) else None,
                        fp, fchg5, fchg20, trust5, trust5_pct, foreign5, mb, mutil, mchg5, mchg10, mchg20, smr))
        con.executemany("INSERT OR REPLACE INTO daily_metrics VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", out)
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
        print("只重算 price_adj + daily_metrics(不抓取)…")
        build_price_adj(con)
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
    # 事件視窗:price 的完整涵蓋範圍 .. 今天(與 --end 無關:回補舊價時才不會留事件缺口)
    adj_start = con.execute("SELECT MIN(date) FROM price").fetchone()[0] or start
    today = date.today().isoformat()
    print(f"除權息/分割事件 {adj_start} .. {today} …")
    nd = fetch_dividends(con, ids, token, adj_start, today, args.sleep)
    ns = fetch_splits(con, ids, token, adj_start, today, args.sleep)
    build_price_adj(con)
    print(f"dividend_result upsert {nd};split_event upsert {ns};price_adj 已重算")
    print("重算 daily_metrics …")
    build_metrics(con)
    n = con.execute("SELECT COUNT(*) FROM daily_metrics").fetchone()[0]
    con.close()
    print(f"完成 — 原始 {total} rows 落地,daily_metrics {n} rows → {DB}")

if __name__ == "__main__":
    main()
