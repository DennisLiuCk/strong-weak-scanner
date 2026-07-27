#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
財報四表(月營收/損益表/資產負債表/現金流量表)→ SQLite 落地。
零第三方依賴,重用 fetch_daily 的抓取層(token/retry/限流退避一致,同 screen.py 的做法)。

月/季頻資料,不掛每日管線——獨立排程(.github/workflows/fetch-financials.yml):
  月營收:每月抓一次(公司約月初 10 日內公布上月數字)
  損益表/資產負債表/現金流量表:季頻,季後 45 天內公布(Q4 為年報,隔年 3/31 截止)

損益表/資產負債表/現金流量表三個 dataset 是 FinMind 原生「type/value」窄表(long
format)——各期揭露項目數量不固定(EPS 偶爾缺、資產負債表單期可達 ~90 個 type),
用寬表存就要跟著 FinMind schema 變動維護欄位,故照原樣存 EAV 結構,
PRIMARY KEY(date, stock_id, type)。

⚠ 這批是基本面資料,**不進 daily_metrics/daily_scores 評分管線**,供 Universe 治理
(R1 業務歸屬)等質化查證用——同 tdcc_holding/sbl 屬「觀察層」,見 CLAUDE.md。

用法:
  python scripts/fetch_financials.py                       # 全部四個 dataset
  python scripts/fetch_financials.py --datasets TaiwanStockMonthRevenue
  python scripts/fetch_financials.py --stocks 6525,8131 --start 2023-01-01
  python scripts/fetch_financials.py --official-month-revenue-only --stocks 3016,3680
"""
import argparse, csv, json, os, sqlite3, sys, time
import urllib.request
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_daily import api_get, get_token, REF_IDS   # 重用抓取層(retry/限流退避一致)

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
UNIVERSE = os.path.join(ROOT, "config", "universe.csv")
TWSE_MONTH_REVENUE_URL = "https://openapi.twse.com.tw/v1/opendata/t187ap05_L"
TPEX_MONTH_REVENUE_URL = "https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap05_O"

SCHEMA = """
CREATE TABLE IF NOT EXISTS month_revenue(date TEXT, stock_id TEXT, revenue INTEGER,
  revenue_month INTEGER, revenue_year INTEGER, PRIMARY KEY(date, stock_id));
CREATE TABLE IF NOT EXISTS financials(date TEXT, stock_id TEXT, type TEXT, value REAL,
  origin_name TEXT, PRIMARY KEY(date, stock_id, type));
CREATE TABLE IF NOT EXISTS balance_sheet(date TEXT, stock_id TEXT, type TEXT, value REAL,
  origin_name TEXT, PRIMARY KEY(date, stock_id, type));
CREATE TABLE IF NOT EXISTS cash_flow(date TEXT, stock_id TEXT, type TEXT, value REAL,
  origin_name TEXT, PRIMARY KEY(date, stock_id, type));
"""


def up_month_revenue(con, data):
    rows = [(d["date"], d["stock_id"], d.get("revenue"), d.get("revenue_month"),
             d.get("revenue_year")) for d in data]
    con.executemany("INSERT OR REPLACE INTO month_revenue VALUES(?,?,?,?,?)", rows)
    return len(rows)


def _up_eav(table):
    def _up(con, data):
        rows = [(d["date"], d["stock_id"], d["type"], d.get("value"), d.get("origin_name"))
                for d in data]
        con.executemany(f"INSERT OR REPLACE INTO {table} VALUES(?,?,?,?,?)", rows)
        return len(rows)
    return _up


UPSERT = {
    "TaiwanStockMonthRevenue": up_month_revenue,
    "TaiwanStockFinancialStatements": _up_eav("financials"),
    "TaiwanStockBalanceSheet": _up_eav("balance_sheet"),
    "TaiwanStockCashFlowsStatement": _up_eav("cash_flow"),
}


def read_universe_ids():
    ids = []
    with open(UNIVERSE, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            sid = r["stock_id"].strip()
            if sid:
                ids.append(sid)
    return ids


def _previous_calendar_month(value):
    first = value.replace(day=1)
    return first - timedelta(days=1)


def _month_storage_date(year, month):
    """FinMind month_revenue 用次月 1 日代表 revenue_year/revenue_month。"""
    if month == 12:
        return f"{year + 1}-01-01"
    return f"{year}-{month + 1:02d}-01"


def _integer(value):
    raw = str(value or "").replace(",", "").strip()
    if not raw or raw == "-":
        return None
    return int(float(raw))


def official_month_revenue_rows(stock_ids, year, month, opener=urllib.request.urlopen):
    """從 TWSE/TPEx 當期 OpenAPI 取得月營收；官方單位千元，DB 單位元。"""
    wanted = set(stock_ids)
    roc_period = f"{year - 1911:03d}{month:02d}"
    rows = {}
    for url in (TWSE_MONTH_REVENUE_URL, TPEX_MONTH_REVENUE_URL):
        req = urllib.request.Request(
            url, headers={"User-Agent": "strong-weak-scanner/financial-coverage"})
        with opener(req, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8-sig"))
        for item in payload:
            sid = str(item.get("公司代號") or "").strip()
            if sid not in wanted or str(item.get("資料年月") or "").strip() != roc_period:
                continue
            revenue_thousand = _integer(item.get("營業收入-當月營收"))
            if revenue_thousand is None:
                continue
            rows[sid] = {
                "date": _month_storage_date(year, month),
                "stock_id": sid,
                "revenue": revenue_thousand * 1000,
                "revenue_month": month,
                "revenue_year": year,
            }
    return rows


def missing_month_revenue(con, stock_ids, year, month):
    if not stock_ids:
        return []
    placeholders = ",".join("?" for _ in stock_ids)
    present = {
        row[0] for row in con.execute(
            f"SELECT stock_id FROM month_revenue "
            f"WHERE revenue_year=? AND revenue_month=? AND revenue IS NOT NULL "
            f"AND stock_id IN ({placeholders})",
            (year, month, *stock_ids),
        )
    }
    return [sid for sid in stock_ids if sid not in present]


def fill_official_month_revenue(con, stock_ids, year, month,
                                fetcher=official_month_revenue_rows):
    """只補 FinMind 尚缺的股票，不覆寫既有列。"""
    before = missing_month_revenue(con, stock_ids, year, month)
    if not before:
        return before, [], []
    official = fetcher(before, year, month)
    rows = [official[sid] for sid in before if sid in official]
    if rows:
        up_month_revenue(con, rows)
    after = missing_month_revenue(con, stock_ids, year, month)
    return before, [row["stock_id"] for row in rows], after


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", help="YYYY-MM-DD;省略則抓近 1095 天(約 3 年,涵蓋 12 季)")
    ap.add_argument("--end", help="YYYY-MM-DD;預設今天")
    ap.add_argument("--datasets", help="逗號分隔,只抓指定 dataset")
    ap.add_argument("--stocks", help="逗號分隔,只抓指定股票(定向補缺用,省 API 額度)")
    ap.add_argument("--sleep", type=float, default=0.25, help="每次 API 間隔秒數(避免限流)")
    ap.add_argument(
        "--official-month-revenue-only", action="store_true",
        help="不呼叫 FinMind，只用 TWSE/TPEx OpenAPI 補最新月營收缺口")
    ap.add_argument(
        "--no-official-month-revenue-fallback", action="store_true",
        help="停用月營收的 TWSE/TPEx 官方缺口補援")
    ap.add_argument(
        "--require-latest-month-complete", action="store_true",
        help="最新應公布月份仍有缺口時 exit 1（建議用於每月 17 日重試）")
    args = ap.parse_args()

    end = args.end or date.today().isoformat()
    start = args.start or (date.today() - timedelta(days=1095)).isoformat()
    ds_list = [s.strip() for s in args.datasets.split(",") if s.strip()] if args.datasets else list(UPSERT)
    if args.official_month_revenue_only:
        if args.datasets and ds_list != ["TaiwanStockMonthRevenue"]:
            sys.exit("--official-month-revenue-only 只能搭配 TaiwanStockMonthRevenue")
        ds_list = ["TaiwanStockMonthRevenue"]
    bad = [s for s in ds_list if s not in UPSERT]
    if bad:
        sys.exit(f"未知 dataset:{bad}(可用:{sorted(UPSERT)})")

    ids = read_universe_ids()
    ids += [s for s in REF_IDS if s not in ids]   # 觀察層參考個股(2330):月營收/財報供台積電專區
    if args.stocks:
        want = {s.strip() for s in args.stocks.split(",") if s.strip()}
        missing = want - set(ids)
        if missing:
            sys.exit(f"--stocks 含 universe 外代號:{sorted(missing)}")
        ids = [s for s in ids if s in want]

    token = None if args.official_month_revenue_only else get_token()
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    con = sqlite3.connect(DB)
    con.executescript(SCHEMA)
    print(f"抓取財報 {start} .. {end} · {len(ids)} 檔 · {len(ds_list)} datasets")
    total = 0
    if not args.official_month_revenue_only:
        for i, sid in enumerate(ids, 1):
            got = 0
            for ds in ds_list:
                data = api_get(ds, sid, start, end, token)
                if data:
                    got += UPSERT[ds](con, data)
                time.sleep(args.sleep)
            total += got
            con.commit()
            print(f"[{i:>3}/{len(ids)}] {sid} · {got} rows")

    remaining = []
    if "TaiwanStockMonthRevenue" in ds_list:
        end_date = date.fromisoformat(end)
        target = _previous_calendar_month(end_date)
        if args.no_official_month_revenue_fallback:
            remaining = missing_month_revenue(
                con, ids, target.year, target.month)
            print(
                f"月營收覆蓋 {target.year}-{target.month:02d}："
                f"{len(ids) - len(remaining)}/{len(ids)}")
        else:
            try:
                before, filled, remaining = fill_official_month_revenue(
                    con, ids, target.year, target.month)
                con.commit()
                total += len(filled)
                print(
                    f"官方月營收補援 {target.year}-{target.month:02d}："
                    f"原缺 {len(before)}，補 {len(filled)}，仍缺 {len(remaining)}")
                if filled:
                    print("官方補入：" + ",".join(filled))
            except Exception as exc:
                remaining = missing_month_revenue(
                    con, ids, target.year, target.month)
                print(
                    f"WARN 官方月營收補援失敗：{type(exc).__name__}: {exc}",
                    file=sys.stderr)
                if args.require_latest_month_complete:
                    con.close()
                    sys.exit(1)
    print(f"完成 — 共 {total} rows 落地 {DB}")
    con.close()
    if args.require_latest_month_complete and remaining:
        print("ERROR 最新月營收仍缺：" + ",".join(remaining), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
