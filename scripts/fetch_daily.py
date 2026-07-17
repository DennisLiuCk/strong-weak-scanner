#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
台股五元素每日抓取 → SQLite 落地。
零第三方依賴(只用 Python 標準庫),方便本機排程或雲端 routine 搬運。

用法:
  # 增量(預設抓最近 15 天,補當日缺口)
  uv run --no-project python scripts/fetch_daily.py
  # 回補歷史(建立滾動視窗需要的基期)
  uv run --no-project python scripts/fetch_daily.py --start 2026-03-01 --end 2026-07-03
  # 只回補單一 dataset(新表補歷史用;跳過事件段、仍重算 metrics)
  uv run --no-project python scripts/fetch_daily.py --datasets TaiwanDailyShortSaleBalances --start 2026-03-01
  # 定向補缺:只抓指定股票(省 API 額度;可與 --datasets 疊加)
  uv run --no-project python scripts/fetch_daily.py --stocks 6510,6515 --start 2026-03-02

Token 讀取順序:環境變數 FINMIND_TOKEN/FINMIND_TOKEN2/FINMIND_TOKEN3
→ 專案根目錄 .mcp.json。
日 OHLCV 改由 TWSE/TPEx 官方全市場日報各抓一次；其餘四張個股原始表仍走 FinMind。
抓完會自動重算 daily_metrics(五元素衍生指標表)。
價格類指標(ret1/距高)用還原股價 price_adj。FinMind 的 TaiwanStockPriceAdj 免費層不可用
(需 Sponsor),所以改抓 TaiwanStockDividendResult + TaiwanStockSplitPrice(皆免費),
本地以倒推法重算還原價(事件日前的歷史價 × 係數連乘,最新區段==原始價)。
減資參考價 dataset 需付費、未涵蓋——由「無事件大跳空」偵測示警兜底。
price_adj 每次整表重建、冪等;原始 price 表維持 append-only 不動。
"""
import argparse, bisect, csv, json, os, sqlite3, statistics, sys, time
import urllib.parse, urllib.request
from datetime import date, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
UNIVERSE = os.path.join(ROOT, "config", "universe.csv")
GROUPS_CSV = os.path.join(ROOT, "config", "groups.csv")
API = "https://api.finmindtrade.com/api/v4/data"
TWSE_PRICE_URL = "https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX"
TPEX_PRICE_URL = "https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyQuotes"
PRICE_SOURCES = ("TWSE", "TPEx")

DATASETS = ["TaiwanStockPrice", "TaiwanStockInstitutionalInvestorsBuySell",
            "TaiwanStockMarginPurchaseShortSale", "TaiwanStockShareholding",
            "TaiwanDailyShortSaleBalances"]
DATASET_TABLE = {
    "TaiwanStockPrice": "price",
    "TaiwanStockInstitutionalInvestorsBuySell": "inst",
    "TaiwanStockMarginPurchaseShortSale": "margin",
    "TaiwanStockShareholding": "holding",
    "TaiwanDailyShortSaleBalances": "sbl",
}

# ── 觀察層參考個股(上游錨定,如台積電):收盤/外資持股進 ref_* 隔離表,
#    絕不進 universe/daily_metrics/daily_scores/tier;僅供儀表板台積電專區顯示 ──
REF_IDS = ["2330"]

# ── 族群/大盤層策略旋鈕(個股層旋鈕在 score.py CONFIG)──
REGIME_DD      = -0.03   # 報酬指數距20日高 ≤ 此值 → 修正 regime
DD_MIN_OBS     = 10      # dd20 最少樣本數(冷啟動保護,同 dist_hi 慣例)
GRP_MIN_N      = 6       # 族群聚合最少有效檔數(避免 1 檔代表全族群)
GS_OFF_HIGH    = -0.05   # 族群狀態:「價未回高」門檻(中位距60日高)
GS_BREADTH_LOW = 0.4     # 族群狀態:「佈局廣度低」門檻
TDCC_LAG_DAYS  = 3       # 資料層假設:TDCC 週快照(週五結算、週六公布)自次週一生效(T−3 日曆日)

SCHEMA = """
CREATE TABLE IF NOT EXISTS universe(stock_id TEXT PRIMARY KEY, name TEXT, grp TEXT, biz TEXT);
CREATE TABLE IF NOT EXISTS price(date TEXT, stock_id TEXT, open REAL, high REAL, low REAL,
  close REAL, volume INTEGER, amount REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS inst(date TEXT, stock_id TEXT, foreign_net INTEGER, trust_net INTEGER,
  dealer_net INTEGER, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS margin(date TEXT, stock_id TEXT, margin_bal INTEGER, short_bal INTEGER,
  PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS holding(date TEXT, stock_id TEXT, foreign_pct REAL, shares_issued INTEGER,
  PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS sbl(date TEXT, stock_id TEXT, sbl_bal INTEGER,
  PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS risk_flags(date TEXT, stock_id TEXT, kind TEXT, reason TEXT, period TEXT,
  PRIMARY KEY(date,stock_id,kind));
CREATE TABLE IF NOT EXISTS dividend_result(date TEXT, stock_id TEXT, before_price REAL,
  reference_price REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS split_event(date TEXT, stock_id TEXT, before_price REAL,
  after_price REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS market(date TEXT PRIMARY KEY, taiex REAL);
CREATE TABLE IF NOT EXISTS ref_price(date TEXT, stock_id TEXT, close REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS ref_holding(date TEXT, stock_id TEXT, foreign_pct REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS price_adj(date TEXT, stock_id TEXT, close REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS fetch_log(ts TEXT, start TEXT, "end" TEXT, rows INTEGER);
CREATE TABLE IF NOT EXISTS fetch_coverage(dataset TEXT, data_id TEXT, covered_through TEXT,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(dataset,data_id));
"""

_TOKENS = []   # get_tokens() 快取
_TOK_I = 0     # 輪替黏性指標:換到新 token 後,行程內後續呼叫直接沿用
_TOK_DISABLED = set()  # 本次 process 已熔斷的 token index;不再回頭使用
TOKEN_ENV_KEYS = ("FINMIND_TOKEN", "FINMIND_TOKEN2", "FINMIND_TOKEN3")
TOKEN_FATAL_HTTP_CODES = {401, 402, 403}


class TokenPoolExhausted(RuntimeError):
    """所有 FinMind token 都已在本次 process 熔斷。"""


class ExchangePriceFetchError(RuntimeError):
    """TWSE/TPEx 官方價格批次失敗或最新交易日不完整。"""


def get_tokens():
    """可用 token 清單:環境變數 FINMIND_TOKEN{,2,3} → .mcp.json 同名欄位。
    多組 token = 時額(600/hr)輪替池;401/402/403 時熔斷該把並換下一組。"""
    global _TOKENS
    if _TOKENS:
        return _TOKENS
    ts = [os.environ[k] for k in TOKEN_ENV_KEYS if os.environ.get(k)]
    if not ts:
        with open(os.path.join(ROOT, ".mcp.json"), encoding="utf-8") as f:
            env = json.load(f)["mcpServers"]["finmind"]["env"]
        ts = [env[k] for k in TOKEN_ENV_KEYS if env.get(k)]
    # GitHub secret 貼上時可能夾帶 BOM(例如來源檔案存成「UTF-8 with BOM」)——
    # 混進 Authorization header 會讓 latin-1 編碼直接炸掉,且 api_get 逐檔 catch 例外,
    # 會變成「全部靜默失敗、job 卻顯示成功」(2026-07-06 事故:GH Actions 兩次 run 皆 0 rows)。
    # 同一支 token 若誤填到多個 secret,輪替沒有意義且會重複消耗 retry。
    _TOKENS = list(dict.fromkeys(t.strip().lstrip("﻿") for t in ts if t.strip().lstrip("﻿")))
    return _TOKENS

def get_token():
    return get_tokens()[0]


def _active_token_index(tokens):
    """從目前位置找下一把未熔斷 token；找不到就立即停止主管線。"""
    global _TOK_I
    for offset in range(len(tokens)):
        idx = (_TOK_I + offset) % len(tokens)
        if idx not in _TOK_DISABLED:
            _TOK_I = idx
            return idx
    raise TokenPoolExhausted("所有 FinMind token 均已失敗,停止本次 action")


def api_get(dataset, data_id, start, end, token, retries=3, return_status=False):
    global _TOK_I
    tokens = get_tokens() or [token]
    p = {"dataset": dataset, "start_date": start, "end_date": end}
    if data_id:
        p["data_id"] = data_id          # 部分 dataset(如 TaiwanStockSplitPrice)全市場一次回傳
    q = urllib.parse.urlencode(p)
    url = API + "?" + q
    for i in range(retries):
        token_i = _active_token_index(tokens)
        try:
            req = urllib.request.Request(url, headers={
                "Authorization": "Bearer " + tokens[token_i]})
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.load(resp).get("data", [])
                return (data, True) if return_status else data
        except Exception as e:
            code = getattr(e, "code", None)
            if code in TOKEN_FATAL_HTTP_CODES:
                _TOK_DISABLED.add(token_i)
                print(f"  ! HTTP {code}:token #{token_i + 1} 本次 action 停用", file=sys.stderr)
                if len(_TOK_DISABLED) >= len(tokens):
                    raise TokenPoolExhausted(
                        f"所有 {len(tokens)} 把 FinMind token 均已失敗,停止本次 action") from e
                _TOK_I = (token_i + 1) % len(tokens)
                continue
            if i == retries - 1:
                print(f"  ! {dataset} {data_id} 失敗: {e}", file=sys.stderr)
                return ([], False) if return_status else []
            time.sleep(2 * (i + 1))  # 遇限流退避重試
    return ([], False) if return_status else []


def _request_json(url, form=None):
    """交易所公開 JSON；form=None 用 GET，否則以 x-www-form-urlencoded POST。"""
    body = urllib.parse.urlencode(form).encode() if form is not None else None
    req = urllib.request.Request(
        url, data=body, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        data = json.load(resp)
    time.sleep(0.5)  # 官方未公布限流數字；市場批次每日僅各一請求，保留禮貌間隔。
    return data


def _market_number(value, integer=False):
    """交易所數字欄正規化；`--`/空字串代表當日無成交，保留為 None。"""
    if value is None:
        return None
    text = str(value).strip().replace(",", "")
    if not text or not any(ch.isdigit() for ch in text):
        return None
    try:
        number = float(text)
        return int(number) if integer else number
    except ValueError:
        return None


def _price_row(day, sid, open_, high, low, close, volume, amount):
    """轉成既有 up_price() 接受的 FinMind-compatible 欄位名稱。"""
    return {
        "date": day,
        "stock_id": str(sid).strip(),
        "open": _market_number(open_),
        "max": _market_number(high),
        "min": _market_number(low),
        "close": _market_number(close),
        "Trading_Volume": _market_number(volume, integer=True),
        "Trading_money": _market_number(amount),
    }


def parse_twse_price(payload, day, wanted_ids=None):
    """解析 TWSE MI_INDEX 的「每日收盤行情(全部)」；回傳(rows,市場是否有資料)。"""
    stat = str(payload.get("stat") or "")
    if "沒有符合條件的資料" in stat:
        return [], False
    ymd = day.replace("-", "")
    if stat != "OK" or payload.get("date") != ymd:
        raise ValueError(f"TWSE MI_INDEX 回應異常:stat={stat},date={payload.get('date')}")
    required = {"證券代號", "成交股數", "成交金額", "開盤價", "最高價", "最低價", "收盤價"}
    tables = [t for t in payload.get("tables", []) if required.issubset(t.get("fields", []))]
    if not tables:
        raise ValueError("TWSE MI_INDEX 找不到每日收盤行情欄位")
    wanted = set(wanted_ids) if wanted_ids is not None else None
    rows, market_rows = [], 0
    for table in tables:
        pos = {name: i for i, name in enumerate(table["fields"])}
        market_rows += len(table.get("data", []))
        for raw in table.get("data", []):
            sid = str(raw[pos["證券代號"]]).strip()
            if wanted is not None and sid not in wanted:
                continue
            rows.append(_price_row(
                day, sid, raw[pos["開盤價"]], raw[pos["最高價"]], raw[pos["最低價"]],
                raw[pos["收盤價"]], raw[pos["成交股數"]], raw[pos["成交金額"]]))
    return rows, market_rows > 0


def parse_tpex_price(payload, day, wanted_ids=None):
    """解析 TPEx dailyQuotes；兩張同 schema 表都納入，避免管理股票等分表漏列。"""
    ymd = day.replace("-", "")
    if str(payload.get("stat") or "").lower() != "ok" or payload.get("date") != ymd:
        raise ValueError(f"TPEx dailyQuotes 回應異常:stat={payload.get('stat')},date={payload.get('date')}")
    required = {"代號", "收盤", "開盤", "最高", "最低", "成交股數", "成交金額(元)"}
    tables = [t for t in payload.get("tables", []) if required.issubset(t.get("fields", []))]
    if not tables:
        raise ValueError("TPEx dailyQuotes 找不到每日收盤行情欄位")
    wanted = set(wanted_ids) if wanted_ids is not None else None
    rows, market_rows = [], 0
    for table in tables:
        pos = {name: i for i, name in enumerate(table["fields"])}
        market_rows += len(table.get("data", []))
        for raw in table.get("data", []):
            sid = str(raw[pos["代號"]]).strip()
            if wanted is not None and sid not in wanted:
                continue
            rows.append(_price_row(
                day, sid, raw[pos["開盤"]], raw[pos["最高"]], raw[pos["最低"]],
                raw[pos["收盤"]], raw[pos["成交股數"]], raw[pos["成交金額(元)"]]))
    return rows, market_rows > 0


def fetch_exchange_price_source(source, day, wanted_ids=None, retries=3):
    """抓單一交易所單日全市場價格；失敗重試後拋錯，交給 Action 保存 checkpoint。"""
    for attempt in range(retries):
        try:
            if source == "TWSE":
                url = (f"{TWSE_PRICE_URL}?date={day.replace('-', '')}"
                       "&type=ALLBUT0999&response=json")
                return parse_twse_price(_request_json(url), day, wanted_ids)
            if source == "TPEx":
                return parse_tpex_price(_request_json(
                    TPEX_PRICE_URL,
                    {"date": day.replace("-", "/"), "response": "json"}), day, wanted_ids)
            raise ValueError(f"未知價格來源:{source}")
        except Exception as exc:
            if attempt == retries - 1:
                raise ExchangePriceFetchError(f"{source} {day} 官方價格批次失敗:{exc}") from exc
            time.sleep(2 * (attempt + 1))


def load_universe(con):
    rows = []
    with open(UNIVERSE, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append((r["stock_id"].strip(), r["name"].strip(), r["group"].strip(),
                         (r.get("biz") or "").strip()))
    con.execute("DROP TABLE IF EXISTS universe")   # 從 csv 整表重建(含 schema 演進、移除股不殭屍)
    con.execute("CREATE TABLE universe(stock_id TEXT PRIMARY KEY, name TEXT, grp TEXT, biz TEXT)")
    con.executemany("INSERT INTO universe VALUES(?,?,?,?)", rows)
    # 族群定義(名稱/標籤/排序)一併配置化:加族群 = groups.csv + universe.csv 各加一行
    grows = []
    with open(GROUPS_CSV, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            grows.append((r["group"].strip(), r["name"].strip(),
                          (r.get("tag") or "").strip(), int(r.get("ord") or 0)))
    con.execute("DROP TABLE IF EXISTS groups")
    con.execute("CREATE TABLE groups(grp TEXT PRIMARY KEY, name TEXT, tag TEXT, ord INT)")
    con.executemany("INSERT INTO groups VALUES(?,?,?,?)", grows)
    missing = [g for (g,) in con.execute(
        "SELECT DISTINCT grp FROM universe WHERE grp NOT IN (SELECT grp FROM groups)")]
    if missing:
        print(f"  ! universe 含未定義族群 {missing}——請補 config/groups.csv", file=sys.stderr)
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

def up_sbl(con, data):
    # 借券賣出餘額(觀察層)。⚠ 單位是「股」、不是張——margin_bal 才是張,算比例時勿照抄 ×1000
    rows = [(d["date"], d["stock_id"], d.get("SBLShortSalesCurrentDayBalance")) for d in data]
    con.executemany("INSERT OR REPLACE INTO sbl VALUES(?,?,?)", rows)
    return len(rows)

UPSERT = {"TaiwanStockPrice": up_price, "TaiwanStockInstitutionalInvestorsBuySell": up_inst,
          "TaiwanStockMarginPurchaseShortSale": up_margin, "TaiwanStockShareholding": up_holding,
          "TaiwanDailyShortSaleBalances": up_sbl}


def _dates_in_table(con, table, stock_id, start, end):
    return {r[0] for r in con.execute(
        f"SELECT date FROM {table} WHERE stock_id=? AND date BETWEEN ? AND ?",
        (stock_id, start, end))}


def _trading_dates(con, start, end):
    # price 與大盤任一方曾落地都視為交易日；可抓出「全 universe price 同日整批漏掉」
    # 的歷史洞。兩者都沒有的尾端，仍由 TWSE/TPEx 每日全市場批次探針發現。
    return {r[0] for r in con.execute(
        """SELECT date FROM price WHERE date BETWEEN ? AND ?
           UNION SELECT date FROM market WHERE date BETWEEN ? AND ?""",
        (start, end, start, end))}


def _next_date(iso_date):
    return (date.fromisoformat(iso_date) + timedelta(days=1)).isoformat()


def _calendar_dates(start, end):
    current, last = date.fromisoformat(start), date.fromisoformat(end)
    out = []
    while current <= last:
        out.append(current.isoformat())
        current += timedelta(days=1)
    return out


def _missing_price_dates(con, ids, dates):
    """找出指定股票集合未全數落地的交易日；批次價格按日補，不再逐檔請求。"""
    dates = set(dates)
    if not ids or not dates:
        return set()
    marks = ",".join("?" for _ in ids)
    counts = dict(con.execute(
        f"""SELECT date,COUNT(*) FROM price
            WHERE stock_id IN ({marks}) AND date BETWEEN ? AND ? GROUP BY date""",
        (*ids, min(dates), max(dates))).fetchall())
    return {day for day in dates if counts.get(day, 0) != len(ids)}


def fetch_exchange_prices(con, ids, dates, write=True, fetcher=None):
    """TWSE+TPEx 各日全市場批次。

    任一來源失敗時仍先 commit 另一來源已取得的 rows，讓 GitHub Action checkpoint
    可以保存；但隨後拋錯阻止未完成資料進入評分/發布。兩邊都空代表休市或尚未發布。
    """
    fetcher = fetcher or fetch_exchange_price_source
    wanted = set(ids)
    total_rows = requests = 0
    found_dates, written_dates = set(), set()
    for day in sorted(set(dates)):
        availability, errors = {}, []
        for source in PRICE_SOURCES:
            requests += 1
            try:
                batch, has_market_data = fetcher(source, day, wanted)
            except Exception as exc:
                errors.append(f"{source}:{exc}")
                continue
            availability[source] = has_market_data
            if write and batch:
                total_rows += up_price(con, batch)
                con.commit()  # source-by-source checkpoint；下一來源失敗時仍可保存。
                written_dates.add(day)
        if errors:
            raise ExchangePriceFetchError(
                f"{day} 官方價格批次未完成({'; '.join(errors)})")
        flags = [availability.get(source, False) for source in PRICE_SOURCES]
        if any(flags) and not all(flags):
            missing_sources = [source for source in PRICE_SOURCES
                               if not availability.get(source, False)]
            raise ExchangePriceFetchError(
                f"{day} 已是交易日但 {','.join(missing_sources)} 價格回傳空白")
        if all(flags):
            found_dates.add(day)
            if write:
                missing_ids = {sid for sid in wanted if not con.execute(
                    "SELECT 1 FROM price WHERE date=? AND stock_id=?", (day, sid)).fetchone()}
                if missing_ids:
                    raise ExchangePriceFetchError(
                        f"拒絕完成價格不完整資料日 {day}:"
                        f"price={len(wanted) - len(missing_ids)}/{len(wanted)};"
                        f"缺 {','.join(sorted(missing_ids))}")
    return {
        "rows": total_rows,
        "requests": requests,
        "found_dates": found_dates,
        "written_dates": written_dates,
    }


def fetch_missing_raw(con, ids, ds_list, start, end, token, sleep=0.25,
                      force=False, fetcher=api_get, price_fetcher=None):
    """價格走交易所按日批次，其餘 FinMind dataset 只抓 SQLite 尚缺的股票×日期。

    交易日以 price∪market 為準。未知尾端逐日用 TWSE+TPEx 批次探測；找到新交易日後，
    其餘四張 FinMind 表才按股票×dataset 缺口展開。
    """
    known_before = _trading_dates(con, start, end)
    expected = set(known_before)
    finmind_requests = exchange_requests = probe_requests = skipped = rows = 0
    want_price = "TaiwanStockPrice" in ds_list
    finmind_ds = [ds for ds in ds_list if ds != "TaiwanStockPrice"]
    probe_start = None
    probe_dates = set()

    if not force:
        if not expected:
            probe_start = start
        else:
            lo, hi = min(expected), max(expected)
            if start < lo:
                probe_start = start
            elif hi < end:
                probe_start = _next_date(hi)
        if probe_start and probe_start <= end:
            probe_dates = set(_calendar_dates(probe_start, end)) - expected

    if want_price:
        price_gap_dates = (set(_calendar_dates(start, end)) if force
                           else _missing_price_dates(con, ids, expected))
    else:
        price_gap_dates = set()
    price_fetch_dates = probe_dates | price_gap_dates
    price_dates_written = set()
    if price_fetch_dates:
        price_stats = fetch_exchange_prices(
            con, ids, price_fetch_dates, write=want_price, fetcher=price_fetcher)
        rows += price_stats["rows"]
        exchange_requests += price_stats["requests"]
        probe_requests += len(PRICE_SOURCES) * len(probe_dates & price_fetch_dates)
        expected.update(price_stats["found_dates"])
        price_dates_written.update(price_stats["written_dates"])

    for i, sid in enumerate(ids, 1):
        got = calls = 0
        for ds in finmind_ds:
            table = DATASET_TABLE[ds]
            if force:
                req_start, req_end = start, end
            else:
                have = _dates_in_table(con, table, sid, start, end)
                missing = expected - have
                if not missing:
                    skipped += 1
                    continue
                req_start, req_end = min(missing), max(missing)
            data = fetcher(ds, sid, req_start, req_end, token)
            finmind_requests += 1
            calls += 1
            if data:
                n = UPSERT[ds](con, data)
                got += n
                rows += n
            if sleep:
                time.sleep(sleep)
        con.commit()
        if calls:
            print(f"[{i:>2}/{len(ids)}] {sid} · {got} rows · {calls} requests")

    expected.update(_trading_dates(con, start, end))
    if want_price and expected and ids:
        latest = max(expected)
        missing_latest = _missing_price_dates(con, ids, {latest})
        if missing_latest:
            have = len(ids) - sum(1 for sid in ids if not con.execute(
                "SELECT 1 FROM price WHERE date=? AND stock_id=?", (latest, sid)).fetchone())
            raise ExchangePriceFetchError(
                f"拒絕完成價格不完整資料日 {latest}:price={have}/{len(ids)}")
    return {
        "rows": rows,
        "requests": finmind_requests + exchange_requests,
        "finmind_requests": finmind_requests,
        "exchange_requests": exchange_requests,
        "probe_requests": probe_requests,
        "skipped_pairs": skipped,
        "known_dates": known_before,
        "expected_dates": expected,
        "new_dates": expected - known_before,
        "price_dates_written": price_dates_written,
        "probe_start": probe_start,
    }


def _coverage_get(con, dataset, data_id):
    row = con.execute(
        "SELECT covered_through FROM fetch_coverage WHERE dataset=? AND data_id=?",
        (dataset, data_id)).fetchone()
    return row[0] if row else None


def _coverage_set(con, dataset, data_id, covered_through):
    con.execute(
        """INSERT INTO fetch_coverage(dataset,data_id,covered_through,updated_at)
           VALUES(?,?,?,CURRENT_TIMESTAMP)
           ON CONFLICT(dataset,data_id) DO UPDATE SET
             covered_through=excluded.covered_through,updated_at=CURRENT_TIMESTAMP""",
        (dataset, data_id, covered_through))


def initialize_fetch_coverage(con, ids, baseline):
    """舊版每日流程曾逐檔重抓完整事件視窗；首次升級時把已知最新日設為基線。

    只在整張 coverage 表為空時 seed。之後新增 universe 成員沒有 coverage，會自然從
    該股票最早 price 日補抓事件，不會錯把新成員視為已檢查。
    """
    if not baseline or con.execute("SELECT 1 FROM fetch_coverage LIMIT 1").fetchone():
        return
    con.executemany(
        "INSERT INTO fetch_coverage(dataset,data_id,covered_through) VALUES(?,?,?)",
        [("TaiwanStockDividendResult", sid, baseline) for sid in ids])
    con.execute("INSERT INTO fetch_coverage VALUES(?,?,?,CURRENT_TIMESTAMP)",
                ("TaiwanStockSplitPrice", "*", baseline))
    # risk_flags 舊表的 0 rows 無法區分「當天無列管」與「四端點曾失敗」；不 seed，
    # 升級後第一次 daily 必須重新確認四端點成功，之後才可依 coverage 跳過。
    con.commit()

def fetch_dividends(con, ids, token, start, end, sleep, force=False):
    """除權息結果 → dividend_result；coverage 讓無事件日也不必重複請求。"""
    n = requests = 0
    for sid in ids:
        covered = None if force else _coverage_get(con, "TaiwanStockDividendResult", sid)
        req_start = start if not covered else max(start, _next_date(covered))
        if req_start > end:
            continue
        data, ok = api_get("TaiwanStockDividendResult", sid, req_start, end, token,
                           return_status=True)
        requests += 1
        rows = [(d["date"], d["stock_id"], d.get("before_price"), d.get("reference_price"))
                for d in data if d.get("before_price") and d.get("reference_price")]
        if rows:
            con.executemany("INSERT OR REPLACE INTO dividend_result VALUES(?,?,?,?)", rows)
            n += len(rows)
        if ok:
            _coverage_set(con, "TaiwanStockDividendResult", sid, end)
        con.commit()
        if sleep:
            time.sleep(sleep)
    return n, requests

def fetch_splits(con, ids, token, start, end, sleep, force=False):
    """股票分割/反分割參考價 → split_event(upsert)。此 dataset 免 data_id、全市場一次回傳,
    只留 universe 內的股票。"""
    covered = None if force else _coverage_get(con, "TaiwanStockSplitPrice", "*")
    req_start = start if not covered else max(start, _next_date(covered))
    if req_start > end:
        return 0, 0
    data, ok = api_get("TaiwanStockSplitPrice", None, req_start, end, token,
                       return_status=True)
    keep = set(ids)
    rows = [(d["date"], d["stock_id"], d.get("before_price"), d.get("after_price"))
            for d in data if d.get("stock_id") in keep and d.get("before_price") and d.get("after_price")]
    if rows:
        con.executemany("INSERT OR REPLACE INTO split_event VALUES(?,?,?,?)", rows)
    if ok:
        _coverage_set(con, "TaiwanStockSplitPrice", "*", end)
    con.commit()
    if sleep:
        time.sleep(sleep)
    return len(rows), 1

def fetch_index(con, token, start, end, sleep, expected_dates=None, force=False):
    """加權報酬指數(TAIEX,含息)→ market(upsert)。大盤 regime 旗標的原料。"""
    if not force and expected_dates:
        have = {r[0] for r in con.execute(
            "SELECT date FROM market WHERE date BETWEEN ? AND ?", (start, end))}
        missing = set(expected_dates) - have
        if not missing:
            return 0, 0
        start, end = min(missing), max(missing)
    data = api_get("TaiwanStockTotalReturnIndex", "TAIEX", start, end, token)
    rows = [(d["date"], d.get("price")) for d in data
            if d.get("stock_id") == "TAIEX" and d.get("price")]   # 防呆:只收 TAIEX 序列
    if rows:
        con.executemany("INSERT OR REPLACE INTO market VALUES(?,?)", rows)
        con.commit()
    else:
        print("  ! TAIEX 指數抓取為空——市場 regime 將沿用舊資料", file=sys.stderr)
    if sleep:
        time.sleep(sleep)
    return len(rows), 1

def fetch_ref_series(con, token, start, end, sleep, expected_dates=None, force=False):
    """觀察層參考個股(REF_IDS)收盤/外資持股 → ref_price/ref_holding(upsert)。
    隔離表:不進 universe/daily_metrics/daily_scores,只供儀表板專區顯示;
    缺口守門同 fetch_index。Shareholding 約 21:00 發布,排程時段常缺當日,隔日自補。"""
    total = requests = 0
    for sid in REF_IDS:
        for dataset, table, field in (
                ("TaiwanStockPrice", "ref_price", "close"),
                ("TaiwanStockShareholding", "ref_holding", "ForeignInvestmentSharesRatio")):
            s, e = start, end
            if not force and expected_dates:
                have = {r[0] for r in con.execute(
                    f"SELECT date FROM {table} WHERE stock_id=? AND date BETWEEN ? AND ?",
                    (sid, s, e))}
                missing = set(expected_dates) - have
                if not missing:
                    continue
                s, e = min(missing), max(missing)
            data = api_get(dataset, sid, s, e, token)
            requests += 1
            rows = [(d["date"], d["stock_id"], d.get(field)) for d in data
                    if d.get("stock_id") == sid and d.get(field) is not None]
            if rows:
                con.executemany(f"INSERT OR REPLACE INTO {table} VALUES(?,?,?)", rows)
                con.commit()
            total += len(rows)
            if sleep:
                time.sleep(sleep)
    return total, requests

# FinMind TaiwanStockShareholding 對個別股票偶有發布延遲(2026-07-06 事故:19 檔當天缺值,
# 隔天仍缺,但 TWSE/TPEx 官方當天就有——見 reports/data_gap_2026-07-06.md)。
# 兩者皆免token、免登入,合計涵蓋全市場(上市+上櫃),與 fetch_tdcc.py 同一原則:
# 直接打交易所官方 opendata,失敗不擋主管線。
TWSE_QFIIS_URL = "https://www.twse.com.tw/rwd/zh/fund/MI_QFIIS"
TPEX_QFII_URL = "https://www.tpex.org.tw/openapi/v1/tpex_3insti_qfii"

def _roc_date(iso_date):
    """2026-07-06 → 民國 1150706(TPEx Date 欄位格式)。"""
    y, m, d = iso_date.split("-")
    return f"{int(y) - 1911}{m}{d}"

def backfill_holding_from_exchange(con, target_date):
    """FinMind holding(外資持股)在 target_date 缺值時的備援:直接查 TWSE(上市)/
    TPEx(上櫃)當天官方數字回補,只補缺、不覆寫既有資料。任一來源格式跑掉或連不上,
    印警告後跳過,不擋主管線(建置/評分沿用既有的 None→中性0 兜底)。"""
    missing = {r[0] for r in con.execute(
        """SELECT u.stock_id FROM universe u
           LEFT JOIN holding h ON h.stock_id = u.stock_id AND h.date = ?
           WHERE h.stock_id IS NULL""", (target_date,))}
    if not missing:
        return 0
    ymd = target_date.replace("-", "")
    found = {}
    try:
        d = _get_json(f"{TWSE_QFIIS_URL}?date={ymd}&selectType=ALLBUT0999&response=json")
        if d.get("stat") == "OK" and d.get("date") == ymd:
            for row in d["data"]:
                sid = row[0]
                if sid in missing:
                    found[sid] = (float(row[7]), int(str(row[3]).replace(",", "")))
    except Exception as e:
        print(f"  ! TWSE MI_QFIIS 備援失敗:{e}", file=sys.stderr)
    still_missing = missing - found.keys()
    if still_missing:
        try:
            rows = _get_json(TPEX_QFII_URL)
            roc = _roc_date(target_date)
            if rows and rows[0].get("Date") == roc:
                for row in rows:
                    sid = row.get("SecuritiesCompanyCode")
                    if sid in still_missing:
                        pct = float(row["PercentageOfSharesOC/FMIHeld"].rstrip("%"))
                        shares = int(row["NumberOfSharesIssued"])
                        found[sid] = (pct, shares)
        except Exception as e:
            print(f"  ! TPEx qfii 備援失敗:{e}", file=sys.stderr)
    for sid, (pct, shares) in found.items():
        con.execute("INSERT OR REPLACE INTO holding VALUES(?,?,?,?)", (target_date, sid, pct, shares))
    con.commit()
    if found:
        print(f"  外資持股備援(TWSE/TPEx)補上 {len(found)}/{len(missing)} 檔:{','.join(sorted(found))}")
    still = missing - found.keys()
    if still:
        print(f"  ! 外資持股仍缺 {len(still)} 檔(TWSE/TPEx 當天也沒有):{','.join(sorted(still))}",
              file=sys.stderr)
    return len(found)

# 處置/注意股票(觀察層、不計分):交易所對異常價量的官方認證,五元素分數看不到這塊
# ——2026-07-07 驗證發現「真強」評級個股同時被列注意股票(90日漲幅163%)的實例。
# TWSE(上市)+TPEx(上櫃)各自的處置/注意端點,免token,合計涵蓋全市場;當天名單
# 即代表當下正被列管,不必自行判斷起訖。任一端點失敗印警告後跳過,不擋主管線。
TWSE_PUNISH_URL = "https://openapi.twse.com.tw/v1/announcement/punish"
TWSE_NOTICE_URL = "https://openapi.twse.com.tw/v1/announcement/notice"
TPEX_DISPOSAL_URL = "https://www.tpex.org.tw/openapi/v1/tpex_disposal_information"
TPEX_WARNING_URL = "https://www.tpex.org.tw/openapi/v1/tpex_trading_warning_information"

def _get_json(url):
    return _request_json(url)

def fetch_risk_flags(con, target_date):
    """抓當天 TWSE/TPEx 處置+注意名單,篩出 universe 內的檔位存進 risk_flags(整表重建,
    冪等)。同一檔同一天可能有多筆理由(TPEx 注意常見),合併成一筆用「;」串接。"""
    uni = {r[0] for r in con.execute("SELECT stock_id FROM universe")}
    picked = {}   # (stock_id, kind) -> {"reasons": [...], "period": str|None}
    successful_sources = 0

    def add(sid, kind, reason, period=None):
        if sid not in uni:
            return
        e = picked.setdefault((sid, kind), {"reasons": [], "period": period})
        if reason and reason not in e["reasons"]:
            e["reasons"].append(reason)
        if period and not e["period"]:
            e["period"] = period

    try:
        for r in _get_json(TWSE_PUNISH_URL):
            add(r.get("Code"), "處置", r.get("ReasonsOfDisposition"), r.get("DispositionPeriod"))
        successful_sources += 1
    except Exception as e:
        print(f"  ! TWSE 處置股票抓取失敗:{e}", file=sys.stderr)
    try:
        for r in _get_json(TWSE_NOTICE_URL):
            if r.get("Code"):   # 當天無注意股票時回傳單筆全空值 placeholder row
                add(r["Code"], "注意", r.get("TradingInfoForAttention"))
        successful_sources += 1
    except Exception as e:
        print(f"  ! TWSE 注意股票抓取失敗:{e}", file=sys.stderr)
    try:
        for r in _get_json(TPEX_DISPOSAL_URL):
            add(r.get("SecuritiesCompanyCode"), "處置", r.get("DispositionReasons"), r.get("DispositionPeriod"))
        successful_sources += 1
    except Exception as e:
        print(f"  ! TPEx 處置股票抓取失敗:{e}", file=sys.stderr)
    try:
        for r in _get_json(TPEX_WARNING_URL):
            if r.get("SecuritiesCompanyCode"):
                add(r["SecuritiesCompanyCode"], "注意", r.get("TradingInformation"))
        successful_sources += 1
    except Exception as e:
        print(f"  ! TPEx 注意股票抓取失敗:{e}", file=sys.stderr)

    con.execute("DELETE FROM risk_flags WHERE date=?", (target_date,))
    rows = [(target_date, sid, kind, "；".join(e["reasons"]), e["period"])
            for (sid, kind), e in picked.items()]
    if rows:
        con.executemany("INSERT OR REPLACE INTO risk_flags VALUES(?,?,?,?,?)", rows)
    con.commit()
    if rows:
        print(f"  處置/注意股票(觀察層):{len(picked)} 檔次,{','.join(sorted({s for s, _ in picked}))}")
    return len(rows), successful_sources == 4

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

def _window_mean(values, k, window):
    """含當日的完整交易日視窗平均；樣本不足或中間缺值時不產生指標。"""
    if k + 1 < window:
        return None
    sample = values[k-window+1:k+1]
    if any(v is None for v in sample):
        return None
    return sum(sample) / window


def _wilder_rsi(values, period=14):
    """Wilder RSI；首值使用 period 個漲跌的簡單平均，之後採 Wilder 平滑。"""
    out = [None] * len(values)
    gains, losses = [], []
    avg_gain = avg_loss = None

    def value(gain, loss):
        if loss == 0:
            return 50.0 if gain == 0 else 100.0
        return 100.0 - 100.0 / (1.0 + gain / loss)

    for k in range(1, len(values)):
        prev, cur = values[k-1], values[k]
        if prev is None or cur is None:
            gains, losses = [], []
            avg_gain = avg_loss = None
            continue
        delta = cur - prev
        gain, loss = max(delta, 0.0), max(-delta, 0.0)
        if avg_gain is None:
            gains.append(gain)
            losses.append(loss)
            if len(gains) < period:
                continue
            if len(gains) > period:
                gains.pop(0)
                losses.pop(0)
            avg_gain = sum(gains) / period
            avg_loss = sum(losses) / period
        else:
            avg_gain = (avg_gain * (period - 1) + gain) / period
            avg_loss = (avg_loss * (period - 1) + loss) / period
        out[k] = value(avg_gain, avg_loss)
    return out


def build_metrics(con):
    """由原始表重算五元素衍生指標(純 Python 滾動,穩健)。整表重建,可重複執行。
    價格類(ret1/ret20/距高)用還原價;股本取「當日」值(forward-fill)。
    兩段式:先算每檔基礎序列 → 族群逐日中位數 → 再合成「族群相對」指標:
    rs20(20日相對強弱)、down_rs20(族群下跌日抗跌)、dipbuy20(逆勢買超)。"""
    con.execute("DROP TABLE IF EXISTS daily_metrics")
    con.execute("""CREATE TABLE daily_metrics(
        date TEXT, stock_id TEXT, close REAL, close_adj REAL,
        ma5 REAL, ma20 REAL, ma60 REAL, rsi14 REAL,
        volume INTEGER, vol_ma5 REAL, vol_ma20 REAL, vol_ma60 REAL, vol_ratio20 REAL,
        ret1 REAL, ret20 REAL,
        turnover_pct REAL, vol_ratio60 REAL,   -- ②量:周轉率 + 量比(相對自身60日中位)
        dist_hi20 REAL, dist_hi60 REAL,        -- ①價:距 20/60 日高(還原價)
        rs20 REAL, down_rs20 REAL,             -- ①價(相對):20日報酬-族群中位;族群下跌日平均相對表現
        foreign_pct REAL, fpct_chg5 REAL, fpct_chg20 REAL,   -- ③外資:持股% 與變化(pp)
        dipbuy20 REAL, dipbuy20_t REAL,        -- ③④逆勢買超:族群下跌日外資/投信淨買20日累計佔股本%
        trust5 INTEGER, trust5_pct REAL, foreign5 INTEGER,   -- ④投信/外資:近5日淨額(張;投信另存佔股本%)
        margin_bal INTEGER, margin_util_pct REAL,
        margin_chg5 REAL, margin_chg10 REAL, margin_chg20 REAL,  -- ⑤散戶:水位 + 5/10/20 日融資變化
        short_margin_ratio REAL,               -- ⑤券資比(%)
        tdcc_date TEXT, tdcc_big400_pct REAL, tdcc_big400_chg REAL,   -- 觀察:TDCC 大戶>400張(生效快照日/集保庫存%水位/對前週 pp)
        tdcc_big1000_pct REAL, tdcc_big1000_chg REAL,                 -- 觀察:>1000張
        tdcc_people_chg REAL,                                         -- 觀察:總股東人數週變化(比率;負=籌碼集中)
        sbl_pct REAL, sbl_chg5 REAL, sbl_chg10 REAL, sbl_chg20 REAL,  -- 觀察:借券賣出餘額佔股本% + 5/10/20日變化(pp)
        PRIMARY KEY(date, stock_id))""")
    # ── TDCC 週快照預載(觀察層;表可能不存在=fetch_tdcc 尚未跑過,全欄留 None)──
    tdcc = {}
    if con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tdcc_holding'").fetchone():
        acc = {}
        for d, sid, lv, people, pct in con.execute(
                "SELECT date, stock_id, level, people, pct FROM tdcc_holding ORDER BY date"):
            w = acc.setdefault(sid, {}).setdefault(d, [0.0, 0.0, None])   # [big400, big1000, people]
            if 12 <= lv <= 15:
                w[0] += pct or 0.0
            if lv == 15:
                w[1] = pct or 0.0
            if lv == 17:
                w[2] = people   # 合計列人數=總股東數(含差異調整,誤差可忽略)
        for sid, byd in acc.items():
            tdcc[sid] = sorted((d, v[0], v[1], v[2]) for d, v in byd.items())
    # ── 第一趟:每檔基礎序列 ──
    S = {}
    for sid, grp in con.execute("SELECT stock_id, grp FROM universe").fetchall():
        rows = con.execute("""SELECT p.date, p.close, p.volume, h.foreign_pct, m.margin_bal, m.short_bal,
                                     i.trust_net, i.foreign_net, h.shares_issued, pa.close, s.sbl_bal
                              FROM price p
                              LEFT JOIN holding h ON h.date=p.date AND h.stock_id=p.stock_id
                              LEFT JOIN margin  m ON m.date=p.date AND m.stock_id=p.stock_id
                              LEFT JOIN inst    i ON i.date=p.date AND i.stock_id=p.stock_id
                              LEFT JOIN price_adj pa ON pa.date=p.date AND pa.stock_id=p.stock_id
                              LEFT JOIN sbl     s ON s.date=p.date AND s.stock_id=p.stock_id
                              WHERE p.stock_id=? ORDER BY p.date""", (sid,)).fetchall()
        n = len(rows)
        adj = [(r[9] if r[9] is not None else r[1]) for r in rows]  # 還原價;缺值退回原始價
        sh = [r[8] for r in rows]   # 股本逐日 forward-fill,0/None 都視為缺值
        prev = next((x for x in sh if x), None)   # 種子=第一筆已知 → 最前段以其回填(輕微前視,僅及 holding 起點前)
        for k in range(n):
            if sh[k]:
                prev = sh[k]
            else:
                sh[k] = prev
        turn = [(rows[k][2] / sh[k] * 100) if (rows[k][2] is not None and sh[k]) else None for k in range(n)]
        volumes = [r[2] for r in rows]
        ma5s = [_window_mean(adj, k, 5) for k in range(n)]
        ma20s = [_window_mean(adj, k, 20) for k in range(n)]
        ma60s = [_window_mean(adj, k, 60) for k in range(n)]
        rsi14s = _wilder_rsi(adj, 14)
        vol_ma5s = [_window_mean(volumes, k, 5) for k in range(n)]
        vol_ma20s = [_window_mean(volumes, k, 20) for k in range(n)]
        vol_ma60s = [_window_mean(volumes, k, 60) for k in range(n)]
        vol_ratio20s = [(volumes[k] / vol_ma20s[k]) if (volumes[k] is not None and vol_ma20s[k]) else None
                        for k in range(n)]
        ret1s = [(adj[k] / adj[k-1] - 1) if (k > 0 and adj[k-1] and adj[k]) else None for k in range(n)]
        ret20s = [(adj[k] / adj[k-20] - 1) if (k >= 20 and adj[k-20] and adj[k]) else None for k in range(n)]
        S[sid] = dict(grp=grp, rows=rows, adj=adj, sh=sh, turn=turn,
                      ma5=ma5s, ma20=ma20s, ma60=ma60s, rsi14=rsi14s,
                      vol_ma5=vol_ma5s, vol_ma20=vol_ma20s, vol_ma60=vol_ma60s,
                      vol_ratio20=vol_ratio20s, ret1=ret1s, ret20=ret20s)
    # ── 族群逐日中位數(等權,供相對指標)──
    g1, g20 = {}, {}
    for sid, st in S.items():
        for k, r in enumerate(st["rows"]):
            key = (r[0], st["grp"])
            if st["ret1"][k] is not None:
                g1.setdefault(key, []).append(st["ret1"][k])
            if st["ret20"][k] is not None:
                g20.setdefault(key, []).append(st["ret20"][k])
    gmed1 = {k: statistics.median(v) for k, v in g1.items()}
    gmed20 = {k: statistics.median(v) for k, v in g20.items()}
    # ── 第二趟:合成 ──
    for sid, st in S.items():
        rows, adj, sh, turn = st["rows"], st["adj"], st["sh"], st["turn"]
        ret1s, ret20s, grp = st["ret1"], st["ret20"], st["grp"]
        fpct = [r[3] for r in rows]
        mbal = [r[4] for r in rows]
        trust = [r[6] or 0 for r in rows]
        fnet = [r[7] or 0 for r in rows]
        gd = [gmed1.get((r[0], grp)) for r in rows]   # 族群當日中位報酬
        # 觀察層序列:借券賣出餘額佔股本%(sbl_bal 單位=股,直接除股本;margin_bal 才是張)
        sblp = [(rows[k][10] / sh[k] * 100) if (rows[k][10] is not None and sh[k]) else None
                for k in range(len(rows))]
        snaps = tdcc.get(sid, [])
        snap_dates = [x[0] for x in snaps]
        out = []
        for k, r in enumerate(rows):
            d, close, vol, fp, mb, sb = r[0], r[1], r[2], r[3], r[4], r[5]
            shares, ca = sh[k], adj[k]
            ret1, ret20 = ret1s[k], ret20s[k]
            win20 = [c for c in adj[max(0, k-19):k+1] if c is not None]
            win60 = [c for c in adj[max(0, k-59):k+1] if c is not None]
            hi20 = max(win20) if len(win20) >= 10 else None    # 冷啟動保護:視窗樣本不足時
            hi60 = max(win60) if len(win60) >= 30 else None    # 不給「距高」,避免上市/新增股假新高
            turnover = turn[k]
            volwin = [t for t in turn[max(0, k-59):k+1] if t is not None]
            vmed = statistics.median(volwin) if len(volwin) >= 20 else None
            vratio = (turnover / vmed) if (turnover is not None and vmed) else None
            gm20 = gmed20.get((d, grp))
            rs20 = (ret20 - gm20) if (ret20 is not None and gm20 is not None) else None
            downs = [j for j in range(max(0, k-19), k+1) if gd[j] is not None and gd[j] < 0]
            rels = [ret1s[j] - gd[j] for j in downs if ret1s[j] is not None]
            down_rs20 = (sum(rels) / len(rels)) if len(rels) >= 3 else None   # 至少3個下跌日才有意義
            dipbuy20 = (sum(fnet[j] for j in downs) / shares * 100) if (shares and downs) else None
            dipbuy20_t = (sum(trust[j] for j in downs) / shares * 100) if (shares and downs) else None
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
            # 觀察層:TDCC 週快照以 T−TDCC_LAG_DAYS(日曆日)生效——週五結算、週六才公布,防前視
            td = b4 = b4c = b10 = b10c = ppc = None
            if snaps:
                cut = (date.fromisoformat(d) - timedelta(days=TDCC_LAG_DAYS)).isoformat()
                j = bisect.bisect_right(snap_dates, cut) - 1
                if j >= 0:
                    td, b4, b10, pp = snaps[j]
                    if j >= 1:
                        b4c = b4 - snaps[j-1][1]
                        b10c = b10 - snaps[j-1][2]
                        ppc = (pp / snaps[j-1][3] - 1) if (pp and snaps[j-1][3]) else None
            sblv = sblp[k]
            sblc5 = (sblv - sblp[k-5]) if (sblv is not None and k >= 5 and sblp[k-5] is not None) else None
            sblc10 = (sblv - sblp[k-10]) if (sblv is not None and k >= 10 and sblp[k-10] is not None) else None
            sblc20 = (sblv - sblp[k-20]) if (sblv is not None and k >= 20 and sblp[k-20] is not None) else None
            out.append((d, sid, close, ca,
                        st["ma5"][k], st["ma20"][k], st["ma60"][k], st["rsi14"][k],
                        vol, st["vol_ma5"][k], st["vol_ma20"][k], st["vol_ma60"][k],
                        st["vol_ratio20"][k], ret1, ret20, turnover, vratio,
                        (ca/hi20 - 1) if (hi20 and ca) else None, (ca/hi60 - 1) if (hi60 and ca) else None,
                        rs20, down_rs20, fp, fchg5, fchg20, dipbuy20, dipbuy20_t,
                        trust5, trust5_pct, foreign5, mb, mutil, mchg5, mchg10, mchg20, smr,
                        td, b4, b4c, b10, b10c, ppc, sblv, sblc5, sblc10, sblc20))
        con.executemany("INSERT OR REPLACE INTO daily_metrics VALUES(" + ",".join("?" * 45) + ")", out)
    con.commit()

def _gstate(breadth, dist, dip, rel):
    """族群狀態分類。策略規則放資料層(而非儀表板),validate.py 之後直接讀 state 欄。
    med_dip(修正日中位淨買)為選族群「候選」主訊號(OOS 驗證中,見週報④);門檻見 GS_* 旋鈕。"""
    if breadth is None or dist is None:
        return "資料不足", "族群指標樣本不足"
    if dip is not None and dip > 0 and dist <= GS_OFF_HIGH:
        return "蓄勢·被佈局", "修正日有人接、價未回高——佈局特徵"
    if rel is not None and rel > 0 and dist > GS_OFF_HIGH:
        note = "動能領先全體、價近波段高"
        if dip is not None and dip > 0:
            note += ";修正日仍獲買超"
        return "發動·領漲", note
    if dip is not None and dip < 0 and breadth <= GS_BREADTH_LOW:
        return "籌碼退潮", "修正日遭調節、佈局廣度低"
    return "中性觀察", "族群訊號分歧"

def build_group_market(con):
    """族群層聚合 + 大盤 regime(整表重建,冪等)。
    Phase 1 實證:籌碼(外資pp/逆勢買超)是「族群層」訊號、族群內無選股力 →
    佈局廣度與中位籌碼在此聚合,回答「哪個族群正在被佈局」;個股層交給 score.py 排名。
    註:regime 刻意用「報酬指數(含息)」——除息季價格指數會機械性下跌,含息指數
    只反映經濟性修正,與個股層用還原價是同一個邏輯。"""
    con.execute("DROP TABLE IF EXISTS market_daily")
    con.execute("CREATE TABLE market_daily(date TEXT PRIMARY KEY, taiex REAL, dd20 REAL, regime INT)")
    rows = con.execute("SELECT date, taiex FROM market ORDER BY date").fetchall()
    closes = [r[1] for r in rows]
    mk = []
    for k, (d, c) in enumerate(rows):
        win = [x for x in closes[max(0, k-19):k+1] if x]
        dd = (c / max(win) - 1) if (c and len(win) >= DD_MIN_OBS) else None   # 冷啟動保護
        mk.append((d, c, dd, None if dd is None else (1 if dd <= REGIME_DD else 0)))
    con.executemany("INSERT INTO market_daily VALUES(?,?,?,?)", mk)
    pmax = con.execute("SELECT MAX(date) FROM price").fetchone()[0]
    mmax = rows[-1][0] if rows else None
    if pmax and (mmax is None or mmax < pmax):
        print(f"  ! TAIEX 指數最新日 {mmax} 落後個股資料 {pmax}——市場 regime 沿用較舊值", file=sys.stderr)
    con.execute("DROP TABLE IF EXISTS group_metrics")
    con.execute("""CREATE TABLE group_metrics(
        date TEXT, grp TEXT,
        breadth_f REAL,                        -- 佈局廣度:fpct_chg20>0 檔數比例
        med_dist60 REAL, rel20 REAL,           -- 中位距60日高 / 20日動能相對全體
        med_dip REAL, breadth_t REAL,          -- 中位逆勢買超 / 投信買超廣度(5日淨買>0 檔數比例)
        state TEXT, note TEXT,                 -- 族群狀態(規則見 _gstate)
        PRIMARY KEY(date, grp))""")
    agg, uni_ret = {}, {}
    for d, grp, f20, dist60, ret20, dip, tpct in con.execute(
            """SELECT m.date, u.grp, m.fpct_chg20, m.dist_hi60, m.ret20, m.dipbuy20, m.trust5_pct
               FROM daily_metrics m JOIN universe u USING(stock_id)"""):
        a = agg.setdefault((d, grp), {"f20": [], "dist": [], "ret": [], "dip": [], "t": []})
        if f20 is not None:
            a["f20"].append(f20)
        if dist60 is not None:
            a["dist"].append(dist60)
        if ret20 is not None:
            a["ret"].append(ret20)
            uni_ret.setdefault(d, []).append(ret20)
        if dip is not None:
            a["dip"].append(dip)
        if tpct is not None:
            a["t"].append(tpct)
    def med(v):
        return statistics.median(v) if (v and len(v) >= GRP_MIN_N) else None   # 樣本不足不給值
    out = []
    for (d, grp), a in agg.items():
        breadth = (sum(1 for x in a["f20"] if x > 0) / len(a["f20"])) if len(a["f20"]) >= GRP_MIN_N else None
        breadth_t = (sum(1 for x in a["t"] if x > 0) / len(a["t"])) if len(a["t"]) >= GRP_MIN_N else None
        m20 = med(a["ret"])
        u20 = statistics.median(uni_ret[d]) if uni_ret.get(d) else None
        rel20 = (m20 - u20) if (m20 is not None and u20 is not None) else None
        dist, dip = med(a["dist"]), med(a["dip"])
        state, note = _gstate(breadth, dist, dip, rel20)
        out.append((d, grp, breadth, dist, rel20, dip, breadth_t, state, note))
    con.executemany("INSERT OR REPLACE INTO group_metrics VALUES(?,?,?,?,?,?,?,?,?)", out)
    con.commit()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", help="YYYY-MM-DD;省略則抓最近 --days 天")
    ap.add_argument("--end", help="YYYY-MM-DD;預設今天")
    ap.add_argument("--days", type=int, default=15)
    ap.add_argument("--sleep", type=float, default=0.25, help="每次 API 間隔秒數(避免限流)")
    ap.add_argument("--metrics-only", action="store_true", help="不抓取,只用現有原始表重算 daily_metrics")
    ap.add_argument("--datasets", help="逗號分隔,只抓指定 dataset(回補新表用);過濾時跳過除權息/分割/指數事件段")
    ap.add_argument("--stocks", help="逗號分隔,只抓指定股票(定向補缺用,省 API 額度);事件段同步過濾,指數照抓")
    ap.add_argument("--force", action="store_true",
                    help="忽略缺口規劃,強制重抓指定日期範圍(來源修正/人工稽核才用)")
    args = ap.parse_args()

    if args.metrics_only:
        con = sqlite3.connect(DB)
        con.executescript(SCHEMA)
        load_universe(con)
        con.commit()
        print("只重算 price_adj + daily_metrics + 族群/大盤層(不抓取)…")
        build_price_adj(con)
        build_metrics(con)
        build_group_market(con)
        n = con.execute("SELECT COUNT(*) FROM daily_metrics").fetchone()[0]
        con.close()
        print(f"完成 — daily_metrics {n} rows")
        return

    end = args.end or date.today().isoformat()
    start = args.start or (date.today() - timedelta(days=args.days)).isoformat()
    ds_list = [s.strip() for s in args.datasets.split(",") if s.strip()] if args.datasets else DATASETS
    bad = [s for s in ds_list if s not in UPSERT]
    if bad:
        sys.exit(f"未知 dataset:{bad}(可用:{sorted(UPSERT)})")

    token = get_token()
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    con = sqlite3.connect(DB)
    con.executescript(SCHEMA)
    ids = load_universe(con)
    con.commit()
    baseline = con.execute("SELECT MAX(date) FROM price").fetchone()[0]
    initialize_fetch_coverage(con, ids, baseline)
    if args.stocks:
        want = {s.strip() for s in args.stocks.split(",") if s.strip()}
        missing = want - set(ids)
        if missing:
            sys.exit(f"--stocks 含 universe 外代號:{sorted(missing)}")
        ids = [s for s in ids if s in want]
    mode = "強制重抓" if args.force else "智慧補缺"
    print(f"{mode} {start} .. {end} · {len(ids)} 檔 · {len(ds_list)} datasets")
    stats = fetch_missing_raw(
        con, ids, ds_list, start, end, token, args.sleep, force=args.force)
    total = stats["rows"]
    print(f"原始資料規劃:FinMind {stats['finmind_requests']} 次;"
          f"TWSE/TPEx 價格批次 {stats['exchange_requests']} 次"
          f"(新交易日探針 {stats['probe_requests']}),"
          f"跳過已完整 FinMind pair {stats['skipped_pairs']} 個")
    if total or stats["finmind_requests"]:
        con.execute('INSERT INTO fetch_log VALUES(datetime("now"),?,?,?)', (start, end, total))
        con.commit()

    data_changed = total > 0
    expected_dates = stats["expected_dates"]
    target_date = max(expected_dates) if expected_dates else None
    # 事件 coverage 能區分「已查但當天沒有事件」與「尚未查」；新交易日只補新增區間，
    # 中斷後重跑也會從未完成的 coverage 接續，不會再掃完整歷史。
    if args.datasets:
        print("(--datasets 過濾:跳過除權息/分割/指數/參考個股事件抓取,仍重算 price_adj 與 metrics)")
    elif target_date:
        adj_start = con.execute("SELECT MIN(date) FROM price").fetchone()[0] or start
        print(f"除權息/分割/指數補缺 {adj_start} .. {target_date} …")
        nd, rd = fetch_dividends(con, ids, token, adj_start, target_date, args.sleep, args.force)
        ns, rs = fetch_splits(con, ids, token, adj_start, target_date, args.sleep, args.force)
        ni, ri = fetch_index(con, token, adj_start, target_date, args.sleep,
                             expected_dates=expected_dates, force=args.force)
        nr, rr = fetch_ref_series(con, token, adj_start, target_date, args.sleep,
                                  expected_dates=expected_dates, force=args.force)
        # ref_* 是觀察層隔離表、不餵任何衍生表 → 刻意不併入 data_changed(避免無謂 metrics 重建)
        data_changed = data_changed or bool(nd or ns or ni)
        print(f"事件 API {rd + rs + ri + rr} 次:dividend_result upsert {nd};"
              f"split_event upsert {ns};TAIEX {ni};參考個股 {nr}")
    if target_date and "TaiwanStockShareholding" in ds_list:
        n_bf = backfill_holding_from_exchange(con, target_date)
        if n_bf:
            print(f"外資持股 TWSE/TPEx 備援:補上 {n_bf} 檔")
            data_changed = True
    if target_date and not args.datasets:
        risk_through = None if args.force else _coverage_get(con, "risk_flags", "*")
        if not risk_through or risk_through < target_date:
            _, risk_ok = fetch_risk_flags(con, target_date)
            if risk_ok:
                _coverage_set(con, "risk_flags", "*", target_date)
                con.commit()

    metric_last = con.execute("SELECT MAX(date) FROM daily_metrics").fetchone()[0] if con.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='daily_metrics'").fetchone() else None
    price_last = con.execute("SELECT MAX(date) FROM price").fetchone()[0]
    if data_changed or metric_last != price_last:
        build_price_adj(con)
        print("重算 daily_metrics + 族群/大盤層 …")
        build_metrics(con)
        build_group_market(con)
    else:
        print("原始/事件資料無變更且 metrics 已同步,略過衍生表重建")
    n = con.execute("SELECT COUNT(*) FROM daily_metrics").fetchone()[0]
    con.close()
    print(f"完成 — 原始 {total} rows 落地,daily_metrics {n} rows → {DB}")

if __name__ == "__main__":
    main()
