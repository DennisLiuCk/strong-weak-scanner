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
(R1 業務歸屬)等質化查證與 D 基本面觀察排名用——同 tdcc_holding/sbl 屬「觀察層」,
見 CLAUDE.md。

用法:
  python scripts/fetch_financials.py                       # 全部四個 dataset
  python scripts/fetch_financials.py --datasets TaiwanStockMonthRevenue
  python scripts/fetch_financials.py --stocks 6525,8131 --start 2023-01-01
  python scripts/fetch_financials.py --official-month-revenue-only --stocks 3016,3680
  python scripts/fetch_financials.py --initialize-availability-only
"""
import argparse, csv, datetime as dt, json, os, sqlite3, sys, time
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
CREATE TABLE IF NOT EXISTS fundamental_availability(
  dataset TEXT NOT NULL,
  data_date TEXT NOT NULL,
  stock_id TEXT NOT NULL,
  source_published_at TEXT,
  first_seen_at TEXT NOT NULL,
  source TEXT NOT NULL,
  PRIMARY KEY(dataset, data_date, stock_id));
"""


def utc_now():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def record_availability(con, dataset, data, *, first_seen_at=None, source=None,
                        source_published_at=None):
    """以第一次看到的時間建立 point-in-time ledger；重跑不得覆寫。

    ``date`` 是財報期間／月營收 storage date，不等於發布日。FinMind／官方 OpenAPI
    目前沒有逐列穩定發布 timestamp，故 ``source_published_at`` 保留 NULL，而以
    ``first_seen_at`` 作保守可用時間下界。之後若來源補發布日可原欄填入，不能倒填成
    早於 first-seen 後拿去宣稱過去已知。
    """
    first_seen_at = first_seen_at or utc_now()
    source = source or "unknown"
    rows = sorted({(dataset, str(item["date"]), str(item["stock_id"]),
                    source_published_at, first_seen_at, source)
                   for item in data if item.get("date") and item.get("stock_id")})
    con.executemany(
        """INSERT OR IGNORE INTO fundamental_availability(
             dataset,data_date,stock_id,source_published_at,first_seen_at,source)
           VALUES(?,?,?,?,?,?)""", rows)
    return len(rows)


def initialize_existing_availability(con, *, first_seen_at=None):
    """將既有 restated rows 只宣告為「從 migration 當下起已知」，不回填歷史發布日。"""
    first_seen_at = first_seen_at or utc_now()
    mapping = {
        "TaiwanStockMonthRevenue": "month_revenue",
        "TaiwanStockFinancialStatements": "financials",
        "TaiwanStockBalanceSheet": "balance_sheet",
        "TaiwanStockCashFlowsStatement": "cash_flow",
    }
    inserted = 0
    for dataset, table in mapping.items():
        before = con.total_changes
        con.execute(
            f"""INSERT OR IGNORE INTO fundamental_availability(
                   dataset,data_date,stock_id,source_published_at,first_seen_at,source)
                 SELECT ?,date,stock_id,NULL,?,'migration_existing_rows'
                 FROM {table} GROUP BY date,stock_id""",
            (dataset, first_seen_at),
        )
        inserted += con.total_changes - before
    return inserted


def ensure_schema(con, *, initialize_existing=False, first_seen_at=None):
    """建立財務 schema；只有正式抓取入口才初始化既有 rows 的 first-seen ledger。"""
    con.executescript(SCHEMA)
    if initialize_existing:
        return initialize_existing_availability(con, first_seen_at=first_seen_at)
    return 0


def initialize_availability_ledger(db=DB, *, first_seen_at=None):
    """離線建立 first-seen 帳本；不抓網路、不更動既有財報列。"""
    os.makedirs(os.path.dirname(os.path.abspath(db)), exist_ok=True)
    con = sqlite3.connect(db)
    try:
        initialized = ensure_schema(
            con, initialize_existing=True, first_seen_at=first_seen_at)
        con.commit()
        return initialized
    finally:
        con.close()


def up_month_revenue(con, data, *, first_seen_at=None, source="FinMind"):
    rows = [(d["date"], d["stock_id"], d.get("revenue"), d.get("revenue_month"),
             d.get("revenue_year")) for d in data]
    con.executemany("INSERT OR REPLACE INTO month_revenue VALUES(?,?,?,?,?)", rows)
    record_availability(
        con, "TaiwanStockMonthRevenue", data,
        first_seen_at=first_seen_at, source=source)
    return len(rows)


def _up_eav(table, dataset):
    def _up(con, data, *, first_seen_at=None, source="FinMind"):
        rows = [(d["date"], d["stock_id"], d["type"], d.get("value"), d.get("origin_name"))
                for d in data]
        con.executemany(f"INSERT OR REPLACE INTO {table} VALUES(?,?,?,?,?)", rows)
        record_availability(
            con, dataset, data, first_seen_at=first_seen_at, source=source)
        return len(rows)
    return _up


UPSERT = {
    "TaiwanStockMonthRevenue": up_month_revenue,
    "TaiwanStockFinancialStatements": _up_eav(
        "financials", "TaiwanStockFinancialStatements"),
    "TaiwanStockBalanceSheet": _up_eav(
        "balance_sheet", "TaiwanStockBalanceSheet"),
    "TaiwanStockCashFlowsStatement": _up_eav(
        "cash_flow", "TaiwanStockCashFlowsStatement"),
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
        up_month_revenue(con, rows, source="TWSE_TPEx_official_openapi")
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
    ap.add_argument(
        "--initialize-availability-only", action="store_true",
        help="只建立 point-in-time ledger 並把既有列標成此刻才首次可知；不連網")
    args = ap.parse_args()

    if args.initialize_availability_only:
        conflicting = (
            args.start or args.end or args.datasets or args.stocks
            or args.official_month_revenue_only
            or args.no_official_month_revenue_fallback
            or args.require_latest_month_complete
        )
        if conflicting:
            sys.exit("--initialize-availability-only 不可與抓取／補援參數併用")
        initialized = initialize_availability_ledger(DB)
        print(
            f"point-in-time ledger 初始化 {initialized} 組既有期間；"
            "未抓網路，舊資料僅自本次 first-seen 起可用")
        return

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
    initialized = ensure_schema(con, initialize_existing=True)
    if initialized:
        con.commit()
        print(f"point-in-time ledger 初始化 {initialized} 組既有期間；僅自本次 first-seen 起可用")
    print(f"抓取財報 {start} .. {end} · {len(ids)} 檔 · {len(ds_list)} datasets")
    total = 0
    if not args.official_month_revenue_only:
        for i, sid in enumerate(ids, 1):
            got = 0
            for ds in ds_list:
                data = api_get(ds, sid, start, end, token)
                if data:
                    got += UPSERT[ds](con, data, source="FinMind")
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
