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
  # 只回補單一 dataset(名稱保留 FinMind 相容性,實際由交易所批次取得)
  uv run --no-project python scripts/fetch_daily.py --datasets TaiwanDailyShortSaleBalances --start 2026-03-01
  # schema 新增欄位回補：只掃既有交易日與 NULL 欄位，可中斷續跑，且只落 raw checkpoint
  uv run --no-project python scripts/fetch_daily.py --backfill-expanded-fields --start 2026-03-02 --end 2026-07-17
  # 18:00 早場 checkpoint:只抓價格/法人,不重算衍生表
  uv run --no-project python scripts/fetch_daily.py --datasets TaiwanStockPrice,TaiwanStockInstitutionalInvestorsBuySell --raw-only
  # 定向補缺:只抓指定股票(省 API 額度;可與 --datasets 疊加)
  uv run --no-project python scripts/fetch_daily.py --stocks 6510,6515 --start 2026-03-02

Token 讀取順序:環境變數 FINMIND_TOKEN/FINMIND_TOKEN2/FINMIND_TOKEN3
→ 專案根目錄 .mcp.json。
五張原始表皆由 TWSE/TPEx 官方全市場日報各抓一次；FinMind 僅留除權息、分割、
加權報酬指數與參考個股等事件／觀察序列。
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

from observation_metrics import build_observation_metrics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
UNIVERSE = os.path.join(ROOT, "config", "universe.csv")
GROUPS_CSV = os.path.join(ROOT, "config", "groups.csv")
API = "https://api.finmindtrade.com/api/v4/data"
TWSE_PRICE_URL = "https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX"
TPEX_PRICE_URL = "https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyQuotes"
PRICE_SOURCES = ("TWSE", "TPEx")
TWSE_INST_URL = "https://www.twse.com.tw/rwd/zh/fund/T86"
TPEX_INST_URL = "https://www.tpex.org.tw/www/zh-tw/insti/dailyTrade"
TWSE_MARGIN_URL = "https://www.twse.com.tw/exchangeReport/MI_MARGN"
TPEX_MARGIN_URL = "https://www.tpex.org.tw/www/zh-tw/margin/balance"
TWSE_HOLDING_URL = "https://www.twse.com.tw/rwd/zh/fund/MI_QFIIS"
TPEX_HOLDING_URL = "https://www.tpex.org.tw/www/zh-tw/insti/qfii"
TWSE_SBL_URL = "https://www.twse.com.tw/exchangeReport/TWT93U"
TPEX_SBL_URL = "https://www.tpex.org.tw/www/zh-tw/margin/sbl"
TPEX_MARKET_INDEX_URL = "https://www.tpex.org.tw/openapi/v1/tpex_reward_index"

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
EXCHANGE_RAW_DATASETS = tuple(DATASETS[1:])

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
  close REAL, volume INTEGER, amount REAL, trades INTEGER, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS inst(date TEXT, stock_id TEXT, foreign_net INTEGER, trust_net INTEGER,
  dealer_net INTEGER, foreign_buy INTEGER, foreign_sell INTEGER, trust_buy INTEGER,
  trust_sell INTEGER, dealer_self_buy INTEGER, dealer_self_sell INTEGER,
  dealer_self_net INTEGER, dealer_hedge_buy INTEGER, dealer_hedge_sell INTEGER,
  dealer_hedge_net INTEGER, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS margin(date TEXT, stock_id TEXT, margin_bal INTEGER, short_bal INTEGER,
  margin_buy INTEGER, margin_sell INTEGER, margin_cash_repay INTEGER, margin_limit INTEGER,
  short_sell INTEGER, short_buyback INTEGER, short_stock_repay INTEGER, short_limit INTEGER,
  offset_volume INTEGER, margin_prev_bal INTEGER, short_prev_bal INTEGER,
  PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS holding(date TEXT, stock_id TEXT, foreign_pct REAL, shares_issued INTEGER,
  foreign_shares INTEGER, foreign_available_shares INTEGER, foreign_available_pct REAL,
  foreign_limit_pct REAL,
  PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS sbl(date TEXT, stock_id TEXT, sbl_bal INTEGER,
  sbl_prev_bal INTEGER, sbl_sell INTEGER, sbl_return INTEGER, sbl_adjustment INTEGER,
  sbl_next_limit INTEGER,
  PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS risk_flags(date TEXT, stock_id TEXT, kind TEXT, reason TEXT, period TEXT,
  PRIMARY KEY(date,stock_id,kind));
CREATE TABLE IF NOT EXISTS dividend_result(date TEXT, stock_id TEXT, before_price REAL,
  reference_price REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS split_event(date TEXT, stock_id TEXT, before_price REAL,
  after_price REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS market(date TEXT PRIMARY KEY, taiex REAL);
CREATE TABLE IF NOT EXISTS market_index(date TEXT, market TEXT, index_key TEXT, index_name TEXT,
  index_type TEXT, close REAL, PRIMARY KEY(date,market,index_key));
CREATE INDEX IF NOT EXISTS idx_market_index_date_type ON market_index(date,index_type);
CREATE TABLE IF NOT EXISTS security_market(stock_id TEXT PRIMARY KEY, market TEXT,
  observed_date TEXT);
CREATE TABLE IF NOT EXISTS ref_price(date TEXT, stock_id TEXT, close REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS ref_holding(date TEXT, stock_id TEXT, foreign_pct REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS price_adj(date TEXT, stock_id TEXT, close REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS fetch_log(ts TEXT, start TEXT, "end" TEXT, rows INTEGER);
CREATE TABLE IF NOT EXISTS fetch_coverage(dataset TEXT, data_id TEXT, covered_through TEXT,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(dataset,data_id));
"""

# SQLite 的 CREATE TABLE IF NOT EXISTS 不會替既有表補欄；欄位順序刻意沿用「舊欄在前、
# 新欄附加在後」，讓 repo 內既有 data/findmind.db 可原地升級且不需整表搬移。
RAW_COLUMN_MIGRATIONS = {
    "price": (("trades", "INTEGER"),),
    "inst": (
        ("foreign_buy", "INTEGER"), ("foreign_sell", "INTEGER"),
        ("trust_buy", "INTEGER"), ("trust_sell", "INTEGER"),
        ("dealer_self_buy", "INTEGER"), ("dealer_self_sell", "INTEGER"),
        ("dealer_self_net", "INTEGER"), ("dealer_hedge_buy", "INTEGER"),
        ("dealer_hedge_sell", "INTEGER"), ("dealer_hedge_net", "INTEGER"),
    ),
    "margin": (
        ("margin_buy", "INTEGER"), ("margin_sell", "INTEGER"),
        ("margin_cash_repay", "INTEGER"), ("margin_limit", "INTEGER"),
        ("short_sell", "INTEGER"), ("short_buyback", "INTEGER"),
        ("short_stock_repay", "INTEGER"), ("short_limit", "INTEGER"),
        ("offset_volume", "INTEGER"),
        ("margin_prev_bal", "INTEGER"), ("short_prev_bal", "INTEGER"),
    ),
    "holding": (
        ("foreign_shares", "INTEGER"), ("foreign_available_shares", "INTEGER"),
        ("foreign_available_pct", "REAL"), ("foreign_limit_pct", "REAL"),
    ),
    "sbl": (
        ("sbl_prev_bal", "INTEGER"), ("sbl_sell", "INTEGER"),
        ("sbl_return", "INTEGER"), ("sbl_adjustment", "INTEGER"),
        ("sbl_next_limit", "INTEGER"),
    ),
}

# 原始表完整度契約：core 是策略既有欄位；expanded 由 schema migration 唯一來源自動衍生。
# audit_raw_data.py 會同時檢查兩者；--backfill-expanded-fields 只以 expanded 欄位的 NULL
# 當作缺口，避免一般智慧補缺因「整列已存在」而跳過舊 DB 新增欄位。
RAW_CORE_COLUMNS = {
    "price": ("open", "high", "low", "close", "volume", "amount"),
    "inst": ("foreign_net", "trust_net", "dealer_net"),
    "margin": ("margin_bal", "short_bal"),
    "holding": ("foreign_pct", "shares_issued"),
    "sbl": ("sbl_bal",),
}
RAW_EXPANDED_COLUMNS = {
    table: tuple(name for name, _ in columns)
    for table, columns in RAW_COLUMN_MIGRATIONS.items()
}
RAW_AUDIT_COLUMNS = {
    table: RAW_CORE_COLUMNS[table] + RAW_EXPANDED_COLUMNS[table]
    for table in RAW_CORE_COLUMNS
}


def ensure_schema(con):
    """建立新資料庫或就地升級舊 DB；可重複執行。"""
    con.executescript(SCHEMA)
    for table, columns in RAW_COLUMN_MIGRATIONS.items():
        existing = {row[1] for row in con.execute(f"PRAGMA table_info({table})")}
        for name, sql_type in columns:
            if name not in existing:
                con.execute(f"ALTER TABLE {table} ADD COLUMN {name} {sql_type}")
    con.commit()

_TOKENS = []   # get_tokens() 快取
_TOK_I = 0     # 輪替黏性指標:換到新 token 後,行程內後續呼叫直接沿用
_TOK_DISABLED = set()  # 本次 process 已熔斷的 token index;不再回頭使用
TOKEN_ENV_KEYS = ("FINMIND_TOKEN", "FINMIND_TOKEN2", "FINMIND_TOKEN3")
TOKEN_FATAL_HTTP_CODES = {401, 402, 403}


class TokenPoolExhausted(RuntimeError):
    """所有 FinMind token 都已在本次 process 熔斷。"""


class ExchangePriceFetchError(RuntimeError):
    """TWSE/TPEx 官方價格批次失敗或最新交易日不完整。"""


class ExchangeRawFetchError(RuntimeError):
    """TWSE/TPEx 官方原始表批次失敗或交易日不完整。"""


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


def _price_row(day, sid, open_, high, low, close, volume, amount, trades):
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
        "Trading_turnover": _market_number(trades, integer=True),
    }


def parse_twse_price(payload, day, wanted_ids=None):
    """解析 TWSE MI_INDEX 的「每日收盤行情(全部)」；回傳(rows,市場是否有資料)。"""
    stat = str(payload.get("stat") or "")
    if "沒有符合條件的資料" in stat:
        return [], False
    ymd = day.replace("-", "")
    if stat != "OK" or payload.get("date") != ymd:
        raise ValueError(f"TWSE MI_INDEX 回應異常:stat={stat},date={payload.get('date')}")
    required = {"證券代號", "成交股數", "成交筆數", "成交金額", "開盤價", "最高價",
                "最低價", "收盤價"}
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
                raw[pos["收盤價"]], raw[pos["成交股數"]], raw[pos["成交金額"]],
                raw[pos["成交筆數"]]))
    return rows, market_rows > 0


def parse_tpex_price(payload, day, wanted_ids=None):
    """解析 TPEx dailyQuotes；兩張同 schema 表都納入，避免管理股票等分表漏列。"""
    ymd = day.replace("-", "")
    if str(payload.get("stat") or "").lower() != "ok" or payload.get("date") != ymd:
        raise ValueError(f"TPEx dailyQuotes 回應異常:stat={payload.get('stat')},date={payload.get('date')}")
    required = {"代號", "收盤", "開盤", "最高", "最低", "成交股數", "成交金額(元)",
                "成交筆數"}
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
                raw[pos["收盤"]], raw[pos["成交股數"]], raw[pos["成交金額(元)"]],
                raw[pos["成交筆數"]]))
    return rows, market_rows > 0


TWSE_TOTAL_RETURN_KEY = "發行量加權股價報酬指數"
TPEX_TOTAL_RETURN_KEY = "櫃買報酬指數"


def parse_twse_market_indices(payload, day):
    """從價格已使用的 MI_INDEX payload 順手保留全部報酬指數，零額外請求。"""
    stat = str(payload.get("stat") or "")
    if "沒有符合條件的資料" in stat:
        return []
    ymd = day.replace("-", "")
    if stat != "OK" or payload.get("date") != ymd:
        raise ValueError(f"TWSE MI_INDEX 回應異常:stat={stat},date={payload.get('date')}")
    rows = []
    for table in payload.get("tables", []):
        fields = table.get("fields", [])
        if not fields or fields[0] != "報酬指數" or "收盤指數" not in fields:
            continue
        close_at = fields.index("收盤指數")
        for raw in table.get("data", []):
            name = str(raw[0]).strip()
            close = _market_number(raw[close_at])
            if name and close is not None:
                rows.append({
                    "date": day, "market": "TWSE", "index_key": name,
                    "index_name": name, "index_type": "total_return", "close": close,
                })
    if not rows:
        raise ValueError("TWSE MI_INDEX 找不到報酬指數欄位")
    return rows


def _roc_ymd_to_iso(value):
    text = str(value).strip()
    if len(text) < 6 or not text.isdigit():
        raise ValueError(f"民國日期格式錯誤:{value}")
    year = int(text[:-4]) + 1911
    month, day = int(text[-4:-2]), int(text[-2:])
    return date(year, month, day).isoformat()


def parse_tpex_market_indices(payload):
    """TPEx OpenAPI 當月櫃買指數；P0 僅落地含息報酬指數。"""
    if not isinstance(payload, list):
        raise ValueError("TPEx tpex_reward_index 回應不是陣列")
    rows = []
    for raw in payload:
        if not {"Date", "TPExTotalReturnIndex"}.issubset(raw):
            raise ValueError("TPEx tpex_reward_index 欄位不完整")
        close = _market_number(raw["TPExTotalReturnIndex"])
        if close is None:
            continue
        rows.append({
            "date": _roc_ymd_to_iso(raw["Date"]), "market": "TPEx",
            "index_key": TPEX_TOTAL_RETURN_KEY, "index_name": TPEX_TOTAL_RETURN_KEY,
            "index_type": "total_return", "close": close,
        })
    if not rows:
        raise ValueError("TPEx tpex_reward_index 無有效報酬指數")
    return rows


def fetch_exchange_price_source(source, day, wanted_ids=None, retries=3):
    """抓單一交易所單日全市場價格；失敗重試後拋錯，交給 Action 保存 checkpoint。"""
    for attempt in range(retries):
        try:
            if source == "TWSE":
                url = (f"{TWSE_PRICE_URL}?date={day.replace('-', '')}"
                       "&type=ALLBUT0999&response=json")
                payload = _request_json(url)
                rows, available = parse_twse_price(payload, day, wanted_ids)
                indices = []
                if available:
                    try:
                        indices = parse_twse_market_indices(payload, day)
                    except Exception as exc:
                        # 指數是非阻斷觀察層；不可因子表格式／發布延遲拖垮價格 checkpoint。
                        print(f"  ! TWSE {day} market_index 順手解析失敗:{exc}", file=sys.stderr)
                return rows, available, indices
            if source == "TPEx":
                rows, available = parse_tpex_price(_request_json(
                    TPEX_PRICE_URL,
                    {"date": day.replace("-", "/"), "response": "json"}), day, wanted_ids)
                return rows, available, []
            raise ValueError(f"未知價格來源:{source}")
        except Exception as exc:
            if attempt == retries - 1:
                raise ExchangePriceFetchError(f"{source} {day} 官方價格批次失敗:{exc}") from exc
            time.sleep(2 * (attempt + 1))


def _market_percent(value):
    """交易所百分比欄正規化；資料缺值保留 None。"""
    if value is None:
        return None
    text = str(value).strip().replace(",", "").rstrip("%")
    if not text or not any(ch.isdigit() for ch in text):
        return None
    try:
        return float(text)
    except ValueError:
        return None


def _validate_exchange_day(payload, day, source, report):
    """驗證官方回應確實是要求的資料日；無資料(休市/尚未發布)回傳 False。"""
    stat = str(payload.get("stat") or "")
    if "沒有符合條件的資料" in stat or "查無資料" in stat:
        return False
    expected = day.replace("-", "")
    ok = stat == "OK" if source == "TWSE" else stat.lower() == "ok"
    if not ok or payload.get("date") != expected:
        raise ValueError(
            f"{source} {report} 回應異常:stat={stat},date={payload.get('date')}")
    return True


def _inst_record(day, sid, name, buy, sell, net=None):
    """保留法人買／賣／淨額；缺官方淨額時才由買減賣計算。"""
    buy = _market_number(buy, integer=True) or 0
    sell = _market_number(sell, integer=True) or 0
    parsed_net = _market_number(net, integer=True) if net is not None else None
    return {
        "date": day, "stock_id": sid, "name": name,
        "buy": buy, "sell": sell, "net": buy - sell if parsed_net is None else parsed_net,
    }


def parse_twse_inst(payload, day, wanted_ids=None):
    if not _validate_exchange_day(payload, day, "TWSE", "T86"):
        return [], False
    fields = payload.get("fields", [])
    required = {
        "證券代號",
        "外陸資買進股數(不含外資自營商)", "外陸資賣出股數(不含外資自營商)",
        "外陸資買賣超股數(不含外資自營商)",
        "投信買進股數", "投信賣出股數", "投信買賣超股數",
        "自營商買賣超股數",
        "自營商買進股數(自行買賣)", "自營商賣出股數(自行買賣)",
        "自營商買賣超股數(自行買賣)",
        "自營商買進股數(避險)", "自營商賣出股數(避險)",
        "自營商買賣超股數(避險)",
    }
    if not required.issubset(fields):
        raise ValueError("TWSE T86 找不到三大法人欄位")
    pos = {name: i for i, name in enumerate(fields)}
    wanted = set(wanted_ids) if wanted_ids is not None else None
    out, raw_rows = [], payload.get("data", [])
    for raw in raw_rows:
        sid = str(raw[pos["證券代號"]]).strip()
        if wanted is not None and sid not in wanted:
            continue
        out.extend((
            _inst_record(day, sid, "Foreign_Investor",
                         raw[pos["外陸資買進股數(不含外資自營商)"]],
                         raw[pos["外陸資賣出股數(不含外資自營商)"]],
                         raw[pos["外陸資買賣超股數(不含外資自營商)"]]),
            _inst_record(day, sid, "Investment_Trust",
                         raw[pos["投信買進股數"]], raw[pos["投信賣出股數"]],
                         raw[pos["投信買賣超股數"]]),
            _inst_record(day, sid, "Dealer_self",
                         raw[pos["自營商買進股數(自行買賣)"]],
                         raw[pos["自營商賣出股數(自行買賣)"]],
                         raw[pos["自營商買賣超股數(自行買賣)"]]),
            _inst_record(day, sid, "Dealer_Hedging",
                         raw[pos["自營商買進股數(避險)"]],
                         raw[pos["自營商賣出股數(避險)"]],
                         raw[pos["自營商買賣超股數(避險)"]]),
            _inst_record(day, sid, "Dealer_Total", 0, 0,
                         raw[pos["自營商買賣超股數"]]),
        ))
    return out, bool(raw_rows)


def parse_tpex_inst(payload, day, wanted_ids=None):
    if not _validate_exchange_day(payload, day, "TPEx", "dailyTrade"):
        return [], False
    triplet = ["買進股數", "賣出股數", "買賣超股數"]
    tables = [t for t in payload.get("tables", [])
              if len(t.get("fields", [])) == 24 and t["fields"][:2] == ["代號", "名稱"]
              and all(t["fields"][i:i + 3] == triplet for i in (2, 5, 8, 11, 14, 17, 20))
              and t["fields"][23] == "三大法人買賣超股數合計"]
    if not tables:
        raise ValueError("TPEx dailyTrade 找不到三大法人欄位")
    wanted = set(wanted_ids) if wanted_ids is not None else None
    out, market_rows = [], 0
    for table in tables:
        market_rows += len(table.get("data", []))
        for raw in table.get("data", []):
            if len(raw) < 24:
                raise ValueError("TPEx dailyTrade 資料欄數不足")
            sid = str(raw[0]).strip()
            if wanted is not None and sid not in wanted:
                continue
            # 官方重複欄名依群組位置固定：2–4 外陸資(不含外資自營商)、5–7 外資
            # 自營商、8–10 外資合計、11–13 投信、14–16 自營自行、17–19 避險、
            # 20–22 自營合計。既有 foreign_net 口徑維持「不含外資自營商」。
            out.extend((
                _inst_record(day, sid, "Foreign_Investor", raw[2], raw[3], raw[4]),
                _inst_record(day, sid, "Investment_Trust", raw[11], raw[12], raw[13]),
                _inst_record(day, sid, "Dealer_self", raw[14], raw[15], raw[16]),
                _inst_record(day, sid, "Dealer_Hedging", raw[17], raw[18], raw[19]),
                _inst_record(day, sid, "Dealer_Total", raw[20], raw[21], raw[22]),
            ))
    return out, market_rows > 0


def parse_twse_margin(payload, day, wanted_ids=None):
    if not _validate_exchange_day(payload, day, "TWSE", "MI_MARGN"):
        return [], False
    tables = [t for t in payload.get("tables", [])
              if len(t.get("fields", [])) >= 13 and t["fields"][0] == "代號"
              and t["fields"][6] == "今日餘額" and t["fields"][12] == "今日餘額"]
    if not tables:
        raise ValueError("TWSE MI_MARGN 找不到個股融資融券欄位")
    wanted = set(wanted_ids) if wanted_ids is not None else None
    out, market_rows = [], 0
    for table in tables:
        market_rows += len(table.get("data", []))
        for raw in table.get("data", []):
            sid = str(raw[0]).strip()
            if wanted is not None and sid not in wanted:
                continue
            out.append({
                "date": day, "stock_id": sid,
                "MarginPurchasePreviousDayBalance": _market_number(raw[5], integer=True),
                "MarginPurchaseTodayBalance": _market_number(raw[6], integer=True),
                "ShortSalePreviousDayBalance": _market_number(raw[11], integer=True),
                "ShortSaleTodayBalance": _market_number(raw[12], integer=True),
                "MarginPurchaseBuy": _market_number(raw[2], integer=True),
                "MarginPurchaseSell": _market_number(raw[3], integer=True),
                "MarginPurchaseCashRepayment": _market_number(raw[4], integer=True),
                "MarginPurchaseLimit": _market_number(raw[7], integer=True),
                # 融券欄的「賣出」是新借券賣出；「買進」是買回。
                "ShortSaleSell": _market_number(raw[9], integer=True),
                "ShortSaleBuyback": _market_number(raw[8], integer=True),
                "ShortSaleStockRepayment": _market_number(raw[10], integer=True),
                "ShortSaleLimit": _market_number(raw[13], integer=True),
                "MarginShortOffset": _market_number(raw[14], integer=True),
            })
    return out, market_rows > 0


def parse_tpex_margin(payload, day, wanted_ids=None):
    if not _validate_exchange_day(payload, day, "TPEx", "margin/balance"):
        return [], False
    required = {"代號", "前資餘額(張)", "資買", "資賣", "現償", "資餘額", "資限額",
                "前券餘額(張)", "券賣", "券買", "券償", "券餘額", "券限額",
                "資券相抵(張)"}
    tables = [t for t in payload.get("tables", []) if required.issubset(t.get("fields", []))]
    if not tables:
        raise ValueError("TPEx margin/balance 找不到個股融資融券欄位")
    wanted = set(wanted_ids) if wanted_ids is not None else None
    out, market_rows = [], 0
    for table in tables:
        pos = {name: i for i, name in enumerate(table["fields"])}
        market_rows += len(table.get("data", []))
        for raw in table.get("data", []):
            sid = str(raw[pos["代號"]]).strip()
            if wanted is not None and sid not in wanted:
                continue
            out.append({
                "date": day, "stock_id": sid,
                "MarginPurchasePreviousDayBalance": _market_number(
                    raw[pos["前資餘額(張)"]], integer=True),
                "MarginPurchaseTodayBalance": _market_number(raw[pos["資餘額"]], integer=True),
                "ShortSalePreviousDayBalance": _market_number(
                    raw[pos["前券餘額(張)"]], integer=True),
                "ShortSaleTodayBalance": _market_number(raw[pos["券餘額"]], integer=True),
                "MarginPurchaseBuy": _market_number(raw[pos["資買"]], integer=True),
                "MarginPurchaseSell": _market_number(raw[pos["資賣"]], integer=True),
                "MarginPurchaseCashRepayment": _market_number(raw[pos["現償"]], integer=True),
                "MarginPurchaseLimit": _market_number(raw[pos["資限額"]], integer=True),
                "ShortSaleSell": _market_number(raw[pos["券賣"]], integer=True),
                "ShortSaleBuyback": _market_number(raw[pos["券買"]], integer=True),
                "ShortSaleStockRepayment": _market_number(raw[pos["券償"]], integer=True),
                "ShortSaleLimit": _market_number(raw[pos["券限額"]], integer=True),
                "MarginShortOffset": _market_number(raw[pos["資券相抵(張)"]], integer=True),
            })
    return out, market_rows > 0


def parse_twse_holding(payload, day, wanted_ids=None):
    if not _validate_exchange_day(payload, day, "TWSE", "MI_QFIIS"):
        return [], False
    fields = payload.get("fields", [])
    required = {"證券代號", "發行股數", "外資及陸資尚可投資股數",
                "全體外資及陸資持有股數", "外資及陸資尚可投資比率",
                "全體外資及陸資持股比率", "外資及陸資共用法令投資上限比率"}
    if not required.issubset(fields):
        raise ValueError("TWSE MI_QFIIS 找不到外資持股欄位")
    pos = {name: i for i, name in enumerate(fields)}
    wanted = set(wanted_ids) if wanted_ids is not None else None
    out, raw_rows = [], payload.get("data", [])
    for raw in raw_rows:
        sid = str(raw[pos["證券代號"]]).strip()
        if wanted is not None and sid not in wanted:
            continue
        out.append({
            "date": day, "stock_id": sid,
            "ForeignInvestmentSharesRatio": _market_percent(raw[pos["全體外資及陸資持股比率"]]),
            "NumberOfSharesIssued": _market_number(raw[pos["發行股數"]], integer=True),
            "ForeignInvestmentShares": _market_number(
                raw[pos["全體外資及陸資持有股數"]], integer=True),
            "ForeignInvestmentAvailableShares": _market_number(
                raw[pos["外資及陸資尚可投資股數"]], integer=True),
            "ForeignInvestmentAvailableRatio": _market_percent(
                raw[pos["外資及陸資尚可投資比率"]]),
            "ForeignInvestmentLimitRatio": _market_percent(
                raw[pos["外資及陸資共用法令投資上限比率"]]),
        })
    return out, bool(raw_rows)


def parse_tpex_holding(payload, day, wanted_ids=None):
    if not _validate_exchange_day(payload, day, "TPEx", "insti/qfii"):
        return [], False
    required = {"代號", "發行股數(A)", "僑外資及陸資尚可投資股數B=A*F-C",
                "僑外資及陸資持有股數(C)", "僑外資及陸資尚可投資比率(D=B/A)",
                "僑外資及陸資持股比率(E=C/A)", "法令投資上限比率(F)"}
    tables = [t for t in payload.get("tables", []) if required.issubset(t.get("fields", []))]
    if not tables:
        raise ValueError("TPEx insti/qfii 找不到外資持股欄位")
    wanted = set(wanted_ids) if wanted_ids is not None else None
    out, market_rows = [], 0
    for table in tables:
        pos = {name: i for i, name in enumerate(table["fields"])}
        market_rows += len(table.get("data", []))
        for raw in table.get("data", []):
            sid = str(raw[pos["代號"]]).strip()
            if wanted is not None and sid not in wanted:
                continue
            out.append({
                "date": day, "stock_id": sid,
                "ForeignInvestmentSharesRatio": _market_percent(
                    raw[pos["僑外資及陸資持股比率(E=C/A)"]]),
                "NumberOfSharesIssued": _market_number(raw[pos["發行股數(A)"]], integer=True),
                "ForeignInvestmentShares": _market_number(
                    raw[pos["僑外資及陸資持有股數(C)"]], integer=True),
                "ForeignInvestmentAvailableShares": _market_number(
                    raw[pos["僑外資及陸資尚可投資股數B=A*F-C"]], integer=True),
                "ForeignInvestmentAvailableRatio": _market_percent(
                    raw[pos["僑外資及陸資尚可投資比率(D=B/A)"]]),
                "ForeignInvestmentLimitRatio": _market_percent(
                    raw[pos["法令投資上限比率(F)"]]),
            })
    return out, market_rows > 0


def _parse_sbl(payload, day, source, report):
    if not _validate_exchange_day(payload, day, source, report):
        return [], False
    if source == "TWSE":
        fields, raw_rows = payload.get("fields", []), payload.get("data", [])
        tables = [{"fields": fields, "data": raw_rows}]
    else:
        tables = payload.get("tables", [])
    tables = [t for t in tables if len(t.get("fields", [])) >= 14
              and t["fields"][0] in {"代號", "股票代號"}
              and "當日餘額" in t["fields"][12]]
    if not tables:
        raise ValueError(f"{source} {report} 找不到借券賣出餘額欄位")
    out, market_rows = [], 0
    for table in tables:
        market_rows += len(table.get("data", []))
        for raw in table.get("data", []):
            if len(raw) < 14:
                raise ValueError(f"{source} {report} 資料欄數不足")
            out.append({
                "date": day, "stock_id": str(raw[0]).strip(),
                "SBLShortSalesCurrentDayBalance": _market_number(raw[12], integer=True),
                "SBLShortSalesPreviousDayBalance": _market_number(raw[8], integer=True),
                "SBLShortSalesCurrentDaySell": _market_number(raw[9], integer=True),
                "SBLShortSalesCurrentDayReturn": _market_number(raw[10], integer=True),
                "SBLShortSalesCurrentDayAdjustment": _market_number(raw[11], integer=True),
                "SBLShortSalesNextDayLimit": _market_number(raw[13], integer=True),
            })
    return out, market_rows > 0


def parse_twse_sbl(payload, day, wanted_ids=None):
    rows, available = _parse_sbl(payload, day, "TWSE", "TWT93U")
    wanted = set(wanted_ids) if wanted_ids is not None else None
    return [row for row in rows if wanted is None or row["stock_id"] in wanted], available


def parse_tpex_sbl(payload, day, wanted_ids=None):
    rows, available = _parse_sbl(payload, day, "TPEx", "margin/sbl")
    wanted = set(wanted_ids) if wanted_ids is not None else None
    return [row for row in rows if wanted is None or row["stock_id"] in wanted], available


EXCHANGE_RAW_PARSERS = {
    ("TaiwanStockInstitutionalInvestorsBuySell", "TWSE"): parse_twse_inst,
    ("TaiwanStockInstitutionalInvestorsBuySell", "TPEx"): parse_tpex_inst,
    ("TaiwanStockMarginPurchaseShortSale", "TWSE"): parse_twse_margin,
    ("TaiwanStockMarginPurchaseShortSale", "TPEx"): parse_tpex_margin,
    ("TaiwanStockShareholding", "TWSE"): parse_twse_holding,
    ("TaiwanStockShareholding", "TPEx"): parse_tpex_holding,
    ("TaiwanDailyShortSaleBalances", "TWSE"): parse_twse_sbl,
    ("TaiwanDailyShortSaleBalances", "TPEx"): parse_tpex_sbl,
}


def _exchange_raw_url(dataset, source, day):
    ymd, slash = day.replace("-", ""), day.replace("-", "/")
    if (dataset, source) == ("TaiwanStockInstitutionalInvestorsBuySell", "TWSE"):
        return f"{TWSE_INST_URL}?" + urllib.parse.urlencode(
            {"date": ymd, "selectType": "ALL", "response": "json"})
    if (dataset, source) == ("TaiwanStockInstitutionalInvestorsBuySell", "TPEx"):
        return f"{TPEX_INST_URL}?" + urllib.parse.urlencode(
            {"type": "Daily", "cate": "EW", "date": slash, "response": "json"})
    if (dataset, source) == ("TaiwanStockMarginPurchaseShortSale", "TWSE"):
        return f"{TWSE_MARGIN_URL}?" + urllib.parse.urlencode(
            {"date": ymd, "selectType": "ALL", "response": "json"})
    if (dataset, source) == ("TaiwanStockMarginPurchaseShortSale", "TPEx"):
        return f"{TPEX_MARGIN_URL}?" + urllib.parse.urlencode(
            {"date": slash, "response": "json"})
    if (dataset, source) == ("TaiwanStockShareholding", "TWSE"):
        return f"{TWSE_HOLDING_URL}?" + urllib.parse.urlencode(
            {"date": ymd, "selectType": "ALLBUT0999", "response": "json"})
    if (dataset, source) == ("TaiwanStockShareholding", "TPEx"):
        return f"{TPEX_HOLDING_URL}?" + urllib.parse.urlencode(
            {"date": slash, "response": "json"})
    if (dataset, source) == ("TaiwanDailyShortSaleBalances", "TWSE"):
        return f"{TWSE_SBL_URL}?" + urllib.parse.urlencode(
            {"date": ymd, "response": "json"})
    if (dataset, source) == ("TaiwanDailyShortSaleBalances", "TPEx"):
        return f"{TPEX_SBL_URL}?" + urllib.parse.urlencode(
            {"date": slash, "response": "json"})
    raise ValueError(f"未知官方原始表:{dataset}/{source}")


def fetch_exchange_raw_source(dataset, source, day, wanted_ids=None, retries=3):
    """抓單一交易所的一張單日原始表；失敗重試後交由 Action checkpoint。"""
    parser = EXCHANGE_RAW_PARSERS.get((dataset, source))
    if parser is None:
        raise ValueError(f"未知官方原始表:{dataset}/{source}")
    for attempt in range(retries):
        try:
            payload = _request_json(_exchange_raw_url(dataset, source, day))
            return parser(payload, day, wanted_ids)
        except Exception as exc:
            if attempt == retries - 1:
                raise ExchangeRawFetchError(
                    f"{source} {day} {dataset} 官方批次失敗:{exc}") from exc
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
             d.get("close"), d.get("Trading_Volume"), d.get("Trading_money"),
             d.get("Trading_turnover")) for d in data]
    con.executemany(
        """INSERT OR REPLACE INTO price
           (date,stock_id,open,high,low,close,volume,amount,trades)
           VALUES(?,?,?,?,?,?,?,?,?)""", rows)
    return len(rows)


def up_security_market(con, market, data):
    """保存價格批次已確認的上市／上櫃別，供官方指數基準配對。

    交易所別不是評分因子；只用來讓上市股扣 TWSE、上櫃股扣 TPEx 含息指數。
    """
    rows = [(d["stock_id"], market, d["date"]) for d in data]
    con.executemany(
        """INSERT INTO security_market(stock_id,market,observed_date) VALUES(?,?,?)
           ON CONFLICT(stock_id) DO UPDATE SET
             market=excluded.market,
             observed_date=CASE WHEN excluded.observed_date>=security_market.observed_date
                                THEN excluded.observed_date ELSE security_market.observed_date END""",
        rows)
    return len(rows)

def up_inst(con, data):
    # 把官方分項匯總成每檔一列；舊的三個 net 欄口徑保持不變。
    agg = {}
    for d in data:
        key = (d["date"], d["stock_id"])
        a = agg.setdefault(key, {
            "f_buy": 0, "f_sell": 0, "f_net": 0,
            "t_buy": 0, "t_sell": 0, "t_net": 0,
            "ds_buy": 0, "ds_sell": 0, "ds_net": 0,
            "dh_buy": 0, "dh_sell": 0, "dh_net": 0,
            "dealer_total": 0, "has_dealer_total": False,
        })
        buy, sell = d.get("buy") or 0, d.get("sell") or 0
        net = d.get("net")
        net = buy - sell if net is None else net
        nm = d.get("name", "")
        if nm == "Foreign_Investor":
            a["f_buy"] += buy
            a["f_sell"] += sell
            a["f_net"] += net
        elif nm == "Investment_Trust":
            a["t_buy"] += buy
            a["t_sell"] += sell
            a["t_net"] += net
        elif nm == "Dealer_self":
            a["ds_buy"] += buy
            a["ds_sell"] += sell
            a["ds_net"] += net
        elif nm == "Dealer_Hedging":
            a["dh_buy"] += buy
            a["dh_sell"] += sell
            a["dh_net"] += net
        elif nm == "Dealer_Total":
            a["dealer_total"] += net
            a["has_dealer_total"] = True
    rows = []
    for key, value in agg.items():
        dealer_net = (value["dealer_total"] if value["has_dealer_total"]
                      else value["ds_net"] + value["dh_net"])
        rows.append((
            key[0], key[1], value["f_net"], value["t_net"], dealer_net,
            value["f_buy"], value["f_sell"], value["t_buy"], value["t_sell"],
            value["ds_buy"], value["ds_sell"], value["ds_net"],
            value["dh_buy"], value["dh_sell"], value["dh_net"],
        ))
    con.executemany(
        """INSERT OR REPLACE INTO inst
           (date,stock_id,foreign_net,trust_net,dealer_net,foreign_buy,foreign_sell,
            trust_buy,trust_sell,dealer_self_buy,dealer_self_sell,dealer_self_net,
            dealer_hedge_buy,dealer_hedge_sell,dealer_hedge_net)
           VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", rows)
    return len(rows)

def up_margin(con, data):
    rows = [(d["date"], d["stock_id"], d.get("MarginPurchaseTodayBalance"),
             d.get("ShortSaleTodayBalance"), d.get("MarginPurchaseBuy"),
             d.get("MarginPurchaseSell"), d.get("MarginPurchaseCashRepayment"),
             d.get("MarginPurchaseLimit"), d.get("ShortSaleSell"),
             d.get("ShortSaleBuyback"), d.get("ShortSaleStockRepayment"),
             d.get("ShortSaleLimit"), d.get("MarginShortOffset"),
             d.get("MarginPurchasePreviousDayBalance"),
             d.get("ShortSalePreviousDayBalance")) for d in data]
    con.executemany(
        """INSERT OR REPLACE INTO margin
           (date,stock_id,margin_bal,short_bal,margin_buy,margin_sell,margin_cash_repay,
            margin_limit,short_sell,short_buyback,short_stock_repay,short_limit,offset_volume,
            margin_prev_bal,short_prev_bal)
           VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", rows)
    return len(rows)

def up_holding(con, data):
    rows = [(d["date"], d["stock_id"], d.get("ForeignInvestmentSharesRatio"),
             d.get("NumberOfSharesIssued"), d.get("ForeignInvestmentShares"),
             d.get("ForeignInvestmentAvailableShares"),
             d.get("ForeignInvestmentAvailableRatio"),
             d.get("ForeignInvestmentLimitRatio")) for d in data]
    con.executemany(
        """INSERT OR REPLACE INTO holding
           (date,stock_id,foreign_pct,shares_issued,foreign_shares,foreign_available_shares,
            foreign_available_pct,foreign_limit_pct) VALUES(?,?,?,?,?,?,?,?)""", rows)
    return len(rows)

def up_sbl(con, data):
    # 借券賣出餘額(觀察層)。⚠ 單位是「股」、不是張——margin_bal 才是張,算比例時勿照抄 ×1000
    rows = [(d["date"], d["stock_id"], d.get("SBLShortSalesCurrentDayBalance"),
             d.get("SBLShortSalesPreviousDayBalance"),
             d.get("SBLShortSalesCurrentDaySell"), d.get("SBLShortSalesCurrentDayReturn"),
             d.get("SBLShortSalesCurrentDayAdjustment"),
             d.get("SBLShortSalesNextDayLimit")) for d in data]
    con.executemany(
        """INSERT OR REPLACE INTO sbl
           (date,stock_id,sbl_bal,sbl_prev_bal,sbl_sell,sbl_return,sbl_adjustment,sbl_next_limit)
           VALUES(?,?,?,?,?,?,?,?)""", rows)
    return len(rows)


def up_market_index(con, data):
    rows = [(d["date"], d["market"], d["index_key"], d["index_name"],
             d["index_type"], d.get("close")) for d in data]
    con.executemany(
        """INSERT OR REPLACE INTO market_index
           (date,market,index_key,index_name,index_type,close) VALUES(?,?,?,?,?,?)""", rows)
    return len(rows)


def fetch_twse_market_indices(day, retries=3):
    """獨立補 TWSE market_index；正常新日由價格呼叫順手寫入，不會走到這裡。"""
    url = (f"{TWSE_PRICE_URL}?date={day.replace('-', '')}"
           "&type=ALLBUT0999&response=json")
    for attempt in range(retries):
        try:
            return parse_twse_market_indices(_request_json(url), day)
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2 * (attempt + 1))


def fetch_tpex_market_indices(retries=3):
    """TPEx OpenAPI 一次回傳當月櫃買價格／報酬指數；P0 只保留後者。"""
    for attempt in range(retries):
        try:
            return parse_tpex_market_indices(_request_json(TPEX_MARKET_INDEX_URL))
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2 * (attempt + 1))


def fetch_missing_market_indices(con, dates, force=False, twse_fetcher=None,
                                 tpex_fetcher=None):
    """補觀察層報酬指數，不作為五表完整性或 dashboard 發布門檻。

    正常新交易日的 TWSE 指數已隨 MI_INDEX 價格批次落地，因此這裡通常只需 TPEx
    OpenAPI 1 次。舊 DB 首次 migration 若最新日尚無 TWSE 指數，僅補最新交易日，
    避免部署當下突然回打整個歷史視窗；需要歷史 TWSE 時可用 --force 隨價格回補。
    """
    dates = set(dates)
    if not dates:
        return {"rows": 0, "requests": 0, "errors": []}
    twse_fetcher = twse_fetcher or fetch_twse_market_indices
    tpex_fetcher = tpex_fetcher or fetch_tpex_market_indices
    latest = max(dates)
    rows = requests = 0
    errors = []

    if force:
        twse_dates = {day for day in dates if not con.execute(
            "SELECT 1 FROM market_index WHERE date=? AND market='TWSE' AND index_key=?",
            (day, TWSE_TOTAL_RETURN_KEY)).fetchone()}
    else:
        has_latest_twse = con.execute(
            "SELECT 1 FROM market_index WHERE date=? AND market='TWSE' AND index_key=?",
            (latest, TWSE_TOTAL_RETURN_KEY)).fetchone()
        twse_dates = {latest} if not has_latest_twse else set()
    for day in sorted(twse_dates):
        requests += 1
        try:
            batch = twse_fetcher(day)
            rows += up_market_index(con, batch)
            con.commit()
            if day == latest and not any(
                    d["index_key"] == TWSE_TOTAL_RETURN_KEY for d in batch):
                errors.append(f"TWSE {day}:缺 {TWSE_TOTAL_RETURN_KEY}")
        except Exception as exc:
            errors.append(f"TWSE {day}:{exc}")

    has_latest_tpex = con.execute(
        "SELECT 1 FROM market_index WHERE date=? AND market='TPEx' AND index_key=?",
        (latest, TPEX_TOTAL_RETURN_KEY)).fetchone()
    if force or not has_latest_tpex:
        requests += 1
        try:
            batch = []
            for row in tpex_fetcher():
                if row["date"] not in dates:
                    continue
                exists = con.execute(
                    "SELECT 1 FROM market_index WHERE date=? AND market=? AND index_key=?",
                    (row["date"], row["market"], row["index_key"])).fetchone()
                if force or not exists:
                    batch.append(row)
            rows += up_market_index(con, batch)
            con.commit()
            if not any(row["date"] == latest for row in batch):
                errors.append(f"TPEx {latest}:當月 OpenAPI 尚無 {TPEX_TOTAL_RETURN_KEY}")
        except Exception as exc:
            errors.append(f"TPEx {latest}:{exc}")

    return {"rows": rows, "requests": requests, "errors": errors}

UPSERT = {"TaiwanStockPrice": up_price, "TaiwanStockInstitutionalInvestorsBuySell": up_inst,
          "TaiwanStockMarginPurchaseShortSale": up_margin, "TaiwanStockShareholding": up_holding,
          "TaiwanDailyShortSaleBalances": up_sbl}


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


def _nonnull_sql(required_columns):
    """內部固定欄名的非 NULL 條件；呼叫端只能傳 RAW_*_COLUMNS 契約。"""
    return "".join(f' AND "{column}" IS NOT NULL' for column in required_columns or ())


def _missing_dataset_dates(con, table, ids, dates, required_columns=()):
    """找出指定股票集合缺列，或指定必備欄仍為 NULL 的交易日。"""
    dates = set(dates)
    if not ids or not dates:
        return set()
    marks = ",".join("?" for _ in ids)
    nonnull = _nonnull_sql(required_columns)
    counts = dict(con.execute(
        f"""SELECT date,COUNT(*) FROM {table}
            WHERE stock_id IN ({marks}) AND date BETWEEN ? AND ?{nonnull} GROUP BY date""",
        (*ids, min(dates), max(dates))).fetchall())
    return {day for day in dates if counts.get(day, 0) != len(ids)}


def _missing_dataset_ids(con, table, ids, day, required_columns=()):
    """同日精準到股票的缺列／缺欄集合，供欄位回補中斷後續跑。"""
    wanted = set(ids)
    if not wanted:
        return set()
    marks = ",".join("?" for _ in wanted)
    nonnull = _nonnull_sql(required_columns)
    complete = {row[0] for row in con.execute(
        f"""SELECT stock_id FROM {table}
            WHERE date=? AND stock_id IN ({marks}){nonnull}""",
        (day, *sorted(wanted))).fetchall()}
    return wanted - complete


def _missing_price_dates(con, ids, dates):
    """價格表相容 wrapper；批次價格按日補，不再逐檔請求。"""
    return _missing_dataset_dates(con, "price", ids, dates)


def fetch_exchange_prices(con, ids, dates, write=True, fetcher=None, required_columns=()):
    """TWSE+TPEx 各日全市場批次。

    任一來源失敗時仍先 commit 另一來源已取得的 rows，讓 GitHub Action checkpoint
    可以保存；但隨後拋錯阻止未完成資料進入評分/發布。兩邊都空代表休市或尚未發布。
    """
    fetcher = fetcher or fetch_exchange_price_source
    wanted = set(ids)
    total_rows = market_index_rows = requests = 0
    found_dates, written_dates = set(), set()
    for day in sorted(set(dates)):
        availability, errors = {}, []
        for source in PRICE_SOURCES:
            requests += 1
            try:
                result = fetcher(source, day, wanted)
                batch, has_market_data = result[:2]
                index_batch = result[2] if len(result) >= 3 else []
            except Exception as exc:
                errors.append(f"{source}:{exc}")
                continue
            availability[source] = has_market_data
            if write and (batch or index_batch):
                if batch:
                    total_rows += up_price(con, batch)
                    up_security_market(con, source, batch)
                    written_dates.add(day)
                if index_batch:
                    market_index_rows += up_market_index(con, index_batch)
                con.commit()  # source-by-source checkpoint；下一來源失敗時仍可保存。
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
                missing_ids = _missing_dataset_ids(
                    con, "price", wanted, day, required_columns=required_columns)
                if missing_ids:
                    raise ExchangePriceFetchError(
                        f"拒絕完成價格不完整資料日／欄位 {day}:"
                        f"price={len(wanted) - len(missing_ids)}/{len(wanted)};"
                        f"缺 {','.join(sorted(missing_ids))}")
    return {
        "rows": total_rows,
        "market_index_rows": market_index_rows,
        "requests": requests,
        "found_dates": found_dates,
        "written_dates": written_dates,
    }


def fetch_exchange_raw_dataset(con, ids, dataset, dates, overwrite_dates=None, fetcher=None,
                               required_columns=()):
    """單一原始表的 TWSE+TPEx 單日全市場批次，逐來源 checkpoint。

    一般補缺只寫入當日尚缺股票；`overwrite_dates` 用於明確的最終版刷新。任一來源失敗
    仍保留另一來源已 commit 的 rows，但拒絕把不完整資料日交給評分／發布。
    """
    if dataset not in EXCHANGE_RAW_DATASETS:
        raise ValueError(f"非官方批次原始表:{dataset}")
    fetcher = fetcher or fetch_exchange_raw_source
    wanted = set(ids)
    overwrite_dates = set(overwrite_dates or ())
    table = DATASET_TABLE[dataset]
    total_rows = requests = 0
    found_dates, written_dates = set(), set()
    for day in sorted(set(dates)):
        day_wanted = wanted if day in overwrite_dates else _missing_dataset_ids(
            con, table, wanted, day, required_columns=required_columns)
        if not day_wanted:
            continue
        availability, errors = {}, []
        for source in PRICE_SOURCES:
            requests += 1
            try:
                batch, has_market_data = fetcher(dataset, source, day, day_wanted)
            except Exception as exc:
                errors.append(f"{source}:{exc}")
                continue
            availability[source] = has_market_data
            if batch:
                total_rows += UPSERT[dataset](con, batch)
                con.commit()  # source-by-source checkpoint；下一來源失敗時仍可保存。
                written_dates.add(day)
        if errors:
            raise ExchangeRawFetchError(
                f"{day} {dataset} 官方批次未完成({'; '.join(errors)})")
        flags = [availability.get(source, False) for source in PRICE_SOURCES]
        if not all(flags):
            missing_sources = [source for source in PRICE_SOURCES
                               if not availability.get(source, False)]
            raise ExchangeRawFetchError(
                f"{day} 已是交易日但 {','.join(missing_sources)} {dataset} 回傳空白")
        missing_ids = _missing_dataset_ids(
            con, table, wanted, day, required_columns=required_columns)
        if missing_ids:
            raise ExchangeRawFetchError(
                f"拒絕完成不完整資料日／欄位 {day}:{table}="
                f"{len(wanted) - len(missing_ids)}/{len(wanted)};缺 {','.join(sorted(missing_ids))}")
        found_dates.add(day)
    return {
        "rows": total_rows,
        "requests": requests,
        "found_dates": found_dates,
        "written_dates": written_dates,
    }


def fetch_missing_raw(con, ids, ds_list, start, end, token, sleep=0.25,
                      force=False, fetcher=None, price_fetcher=None, final_pass=False,
                      backfill_expanded_fields=False):
    """五張原始表皆走交易所按日批次，只補 SQLite 尚缺的 dataset×日期。

    交易日以 price∪market 為準。未知尾端逐日用 TWSE+TPEx 批次探測；找到新交易日後，
    其餘四張表才各以 TWSE+TPEx 全市場報表補齊。`final_pass` 會把最新 holding 重新抓取
    一次，避免 18:00 初版阻止 22:00 最終版覆寫；完成日另記 coverage，重跑保持冪等。
    `backfill_expanded_fields` 只掃既有交易日，把 RAW_COLUMN_MIGRATIONS 中任一 NULL 視為
    缺口；每個來源完成即 commit，同一命令中斷後可只續補剩餘股票／日期。
    """
    if force and backfill_expanded_fields:
        raise ValueError("force 與 backfill_expanded_fields 不可同時使用")
    if final_pass and backfill_expanded_fields:
        raise ValueError("final_pass 與 backfill_expanded_fields 不可同時使用")
    known_before = _trading_dates(con, start, end)
    expected = set(known_before)
    exchange_requests = probe_requests = skipped = rows = market_index_rows = 0
    want_price = "TaiwanStockPrice" in ds_list
    exchange_ds = [ds for ds in ds_list if ds != "TaiwanStockPrice"]
    probe_start = None
    probe_dates = set()

    if not force and not backfill_expanded_fields:
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
        if force:
            price_gap_dates = set(_calendar_dates(start, end))
        elif backfill_expanded_fields:
            price_gap_dates = _missing_dataset_dates(
                con, "price", ids, expected,
                required_columns=RAW_EXPANDED_COLUMNS["price"])
        else:
            price_gap_dates = _missing_price_dates(con, ids, expected)
    else:
        price_gap_dates = set()
    price_fetch_dates = probe_dates | price_gap_dates
    price_dates_written = set()
    if price_fetch_dates:
        price_stats = fetch_exchange_prices(
            con, ids, price_fetch_dates, write=want_price, fetcher=price_fetcher,
            required_columns=(RAW_EXPANDED_COLUMNS["price"]
                              if backfill_expanded_fields else ()))
        rows += price_stats["rows"]
        market_index_rows += price_stats["market_index_rows"]
        exchange_requests += price_stats["requests"]
        probe_requests += len(PRICE_SOURCES) * len(probe_dates & price_fetch_dates)
        expected.update(price_stats["found_dates"])
        price_dates_written.update(price_stats["written_dates"])

    final_holding_day = None
    for ds in exchange_ds:
        table = DATASET_TABLE[ds]
        required_columns = (RAW_EXPANDED_COLUMNS[table]
                            if backfill_expanded_fields else ())
        if force:
            fetch_dates = set(expected)
        else:
            fetch_dates = _missing_dataset_dates(
                con, table, ids, expected, required_columns=required_columns)
        overwrite_dates = set(expected) if force else set()
        if final_pass and ds == "TaiwanStockShareholding" and expected:
            latest = max(expected)
            final_covered = _coverage_get(con, "exchange_final", ds)
            if not final_covered or final_covered < latest:
                fetch_dates.add(latest)
                overwrite_dates.add(latest)
                final_holding_day = latest
        if not fetch_dates:
            skipped += 1
            continue
        raw_stats = fetch_exchange_raw_dataset(
            con, ids, ds, fetch_dates, overwrite_dates=overwrite_dates, fetcher=fetcher,
            required_columns=required_columns)
        rows += raw_stats["rows"]
        exchange_requests += raw_stats["requests"]
        print(f"{table}: {raw_stats['rows']} rows · {raw_stats['requests']} 官方 requests"
              f" · {len(fetch_dates)} dates")

    # 延至所有指定原始表都成功後才標示 holding 最終版；若後續 margin/sbl 失敗，
    # 19:00 重跑仍會再次刷新 holding，不會讓早場版本被誤認為完成。
    if final_holding_day:
        _coverage_set(con, "exchange_final", "TaiwanStockShareholding", final_holding_day)
        con.commit()

    expected.update(_trading_dates(con, start, end))
    if want_price and expected and ids:
        latest = max(expected)
        missing_latest = _missing_dataset_dates(
            con, "price", ids, {latest},
            required_columns=(RAW_EXPANDED_COLUMNS["price"]
                              if backfill_expanded_fields else ()))
        if missing_latest:
            have = len(ids) - sum(1 for sid in ids if not con.execute(
                "SELECT 1 FROM price WHERE date=? AND stock_id=?", (latest, sid)).fetchone())
            raise ExchangePriceFetchError(
                f"拒絕完成價格不完整資料日 {latest}:price={have}/{len(ids)}")
    return {
        "rows": rows,
        "market_index_rows": market_index_rows,
        "requests": exchange_requests,
        "finmind_requests": 0,
        "exchange_requests": exchange_requests,
        "probe_requests": probe_requests,
        "skipped_batches": skipped,
        "skipped_pairs": skipped,  # 舊日誌／外部呼叫相容 alias
        "known_dates": known_before,
        "expected_dates": expected,
        "new_dates": expected - known_before,
        "price_dates_written": price_dates_written,
        "probe_start": probe_start,
        "backfill_expanded_fields": backfill_expanded_fields,
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
    ap.add_argument("--datasets", help="逗號分隔,只抓指定官方原始表(沿用 FinMind dataset 名稱);過濾時跳過事件段")
    ap.add_argument("--stocks", help="逗號分隔,只抓指定股票(定向補缺用,省 API 額度);事件段同步過濾,指數照抓")
    ap.add_argument("--raw-only", action="store_true",
                    help="只落地原始表 checkpoint,不抓事件、不重算 metrics(18:00 早場用)")
    ap.add_argument("--final-pass", action="store_true",
                    help="完整場:最新 holding 強制刷新一次，指定原始表完整才記 final coverage")
    fetch_mode = ap.add_mutually_exclusive_group()
    fetch_mode.add_argument("--force", action="store_true",
                            help="忽略缺口規劃,強制重抓指定日期範圍(來源修正/人工稽核才用)")
    fetch_mode.add_argument(
        "--backfill-expanded-fields", action="store_true",
        help="只在既有交易日補 RAW_COLUMN_MIGRATIONS 的 NULL 欄位;可續跑且自動 raw-only")
    args = ap.parse_args()

    if args.backfill_expanded_fields and not args.start:
        ap.error("--backfill-expanded-fields 必須明確指定 --start，避免意外回打過大範圍")
    if args.backfill_expanded_fields and args.final_pass:
        ap.error("--backfill-expanded-fields 不可與 --final-pass 同時使用")

    if args.metrics_only:
        con = sqlite3.connect(DB)
        ensure_schema(con)
        load_universe(con)
        con.commit()
        print("只重算 price_adj + daily_metrics + 觀察指標 + 族群/大盤層(不抓取)…")
        build_price_adj(con)
        build_metrics(con)
        obs = build_observation_metrics(
            con, TWSE_TOTAL_RETURN_KEY, TPEX_TOTAL_RETURN_KEY, GRP_MIN_N)
        build_group_market(con)
        n = con.execute("SELECT COUNT(*) FROM daily_metrics").fetchone()[0]
        con.close()
        print(f"完成 — daily_metrics {n} rows;觀察層 {obs['stock_rows']} stock rows / "
              f"{obs['group_rows']} group rows")
        return

    end = args.end or date.today().isoformat()
    start = args.start or (date.today() - timedelta(days=args.days)).isoformat()
    ds_list = [s.strip() for s in args.datasets.split(",") if s.strip()] if args.datasets else DATASETS
    bad = [s for s in ds_list if s not in UPSERT]
    if bad:
        sys.exit(f"未知 dataset:{bad}(可用:{sorted(UPSERT)})")

    # 指定原始表、raw-only、欄位回補全程不碰 FinMind；正式晚場才需 token 補事件／觀察序列。
    effective_raw_only = args.raw_only or args.backfill_expanded_fields
    token = None if (args.datasets or effective_raw_only) else get_token()
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    con = sqlite3.connect(DB)
    ensure_schema(con)
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
    mode = ("強制重抓" if args.force else
            "新增欄位可續跑回補" if args.backfill_expanded_fields else "智慧補缺")
    print(f"{mode} {start} .. {end} · {len(ids)} 檔 · {len(ds_list)} datasets")
    stats = fetch_missing_raw(
        con, ids, ds_list, start, end, token, args.sleep, force=args.force,
        final_pass=args.final_pass,
        backfill_expanded_fields=args.backfill_expanded_fields)
    total = stats["rows"]
    market_index_rows = stats.get("market_index_rows", 0)
    index_stats = {"rows": 0, "requests": 0, "errors": []}
    if "TaiwanStockPrice" in ds_list and stats["expected_dates"]:
        index_stats = fetch_missing_market_indices(
            con, stats["expected_dates"], force=args.force)
        market_index_rows += index_stats["rows"]
        for error in index_stats["errors"]:
            print(f"  ! market_index 非阻斷補缺失敗:{error}", file=sys.stderr)
    print(f"原始資料規劃:FinMind {stats['finmind_requests']} 次;"
          f"TWSE/TPEx 官方批次 {stats['exchange_requests']} 次"
          f"(新交易日探針 {stats['probe_requests']}),"
          f"跳過已完整 dataset-day {stats['skipped_batches']} 組")
    print(f"market_index:upsert {market_index_rows} rows · "
          f"額外官方 requests {index_stats['requests']}"
          f" · errors {len(index_stats['errors'])}")
    if total:
        con.execute('INSERT INTO fetch_log VALUES(datetime("now"),?,?,?)', (start, end, total))
        con.commit()

    data_changed = total > 0
    expected_dates = stats["expected_dates"]
    target_date = max(expected_dates) if expected_dates else None
    if effective_raw_only:
        n = con.execute("SELECT COUNT(*) FROM daily_metrics").fetchone()[0] if con.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='daily_metrics'").fetchone() else 0
        con.close()
        label = "欄位回補" if args.backfill_expanded_fields else "raw-only"
        print(f"{label} 完成 — 原始 {total} rows + market_index {market_index_rows} rows "
              f"checkpoint,daily_metrics 未重算({n} rows)")
        return
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
    if target_date and not args.datasets:
        risk_through = None if args.force else _coverage_get(con, "risk_flags", "*")
        if not risk_through or risk_through < target_date:
            _, risk_ok = fetch_risk_flags(con, target_date)
            if risk_ok:
                _coverage_set(con, "risk_flags", "*", target_date)
                con.commit()

    metric_last = con.execute("SELECT MAX(date) FROM daily_metrics").fetchone()[0] if con.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='daily_metrics'").fetchone() else None
    observation_last = con.execute(
        "SELECT MAX(date) FROM observation_metrics").fetchone()[0] if con.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='observation_metrics'").fetchone() else None
    price_last = con.execute("SELECT MAX(date) FROM price").fetchone()[0]
    if data_changed or metric_last != price_last:
        build_price_adj(con)
        print("重算 daily_metrics + 觀察指標 + 族群/大盤層 …")
        build_metrics(con)
        build_observation_metrics(
            con, TWSE_TOTAL_RETURN_KEY, TPEX_TOTAL_RETURN_KEY, GRP_MIN_N)
        build_group_market(con)
    elif market_index_rows or observation_last != price_last:
        print("官方指數／觀察層有更新，重算 observation_metrics …")
        build_observation_metrics(
            con, TWSE_TOTAL_RETURN_KEY, TPEX_TOTAL_RETURN_KEY, GRP_MIN_N)
    else:
        print("原始/事件資料無變更且 metrics/observation 已同步,略過衍生表重建")
    n = con.execute("SELECT COUNT(*) FROM daily_metrics").fetchone()[0]
    con.close()
    print(f"完成 — 原始 {total} rows 落地,daily_metrics {n} rows → {DB}")

if __name__ == "__main__":
    main()
