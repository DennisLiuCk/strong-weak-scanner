#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""交易狀態的單一資料契約。

交易所日成交表會為暫停交易等「當日沒有形成交易」的股票保留一列：OHLC 空白，
成交量、成交金額與成交筆數皆為 0。這種列不是價格漏抓；而法人日報通常不會列出該股。

本模組只承認上述可由官方 price 原始列重算的嚴格條件。`trading_status` 是衍生的
稽核索引，不取代或補造任何原始表資料；若條件不完整，股票仍視為應有完整資料。
"""

NO_TRADE = "no_trade"
OFFICIAL_PRICE_SOURCE = "official_price_zero_trade"
NO_TRADE_REASON = "官方價格列 OHLC 空白且成交量／金額／筆數皆為 0"

SCHEMA = """
CREATE TABLE IF NOT EXISTS trading_status(
  date TEXT,
  stock_id TEXT,
  status TEXT NOT NULL,
  source TEXT NOT NULL,
  reason TEXT,
  PRIMARY KEY(date,stock_id)
);
CREATE INDEX IF NOT EXISTS idx_trading_status_date_status
  ON trading_status(date,status);
"""


def table_exists(con, table):
    return con.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)
    ).fetchone() is not None


def ensure_schema(con):
    con.executescript(SCHEMA)


def _marks(values):
    return ",".join("?" for _ in values)


def refresh_from_prices(con, dates, stock_ids=None):
    """以官方 price 列同步指定日期的 no-trade 狀態，回傳狀態筆數。

    僅刪除本模組產生的 source；未來若加入交易所停復牌公告來源，不會被此步驟抹除。
    呼叫者負責 commit，方便與 price checkpoint 放在同一交易邊界。
    """
    ensure_schema(con)
    dates = sorted(set(dates or ()))
    ids = sorted(set(stock_ids or ()))
    if not dates:
        return 0

    date_marks = _marks(dates)
    select_params = list(dates)
    select_ids = ""
    if ids:
        select_ids = f" AND p.stock_id IN ({_marks(ids)})"
        select_params.extend(ids)
    desired = {tuple(row) for row in con.execute(
        f"""SELECT p.date,p.stock_id
            FROM price p
            WHERE p.date IN ({date_marks}){select_ids}
              AND p.open IS NULL AND p.high IS NULL AND p.low IS NULL AND p.close IS NULL
              AND p.volume=0 AND p.amount=0 AND p.trades=0
            ORDER BY p.date,p.stock_id""",
        select_params,
    ).fetchall()}

    existing_params = [OFFICIAL_PRICE_SOURCE, *dates]
    existing_ids = ""
    if ids:
        existing_ids = f" AND stock_id IN ({_marks(ids)})"
        existing_params.extend(ids)
    existing = {tuple(row) for row in con.execute(
        f"""SELECT date,stock_id FROM trading_status
            WHERE source=? AND date IN ({date_marks}){existing_ids}""",
        existing_params,
    ).fetchall()}
    con.executemany(
        "DELETE FROM trading_status WHERE date=? AND stock_id=? AND source=?",
        [(day, sid, OFFICIAL_PRICE_SOURCE) for day, sid in sorted(existing - desired)],
    )
    con.executemany(
        "INSERT OR IGNORE INTO trading_status VALUES(?,?,?,?,?)",
        [(day, sid, NO_TRADE, OFFICIAL_PRICE_SOURCE, NO_TRADE_REASON)
         for day, sid in sorted(desired - existing)],
    )
    return len(desired)


def verified_exclusions(con, day, stock_ids=None):
    """回傳可由原始 price 嚴格驗證的非交易狀態列。

    即使 trading_status 被人工誤寫，只要 price 不符合零交易契約，就不會取得豁免。
    """
    if not table_exists(con, "trading_status") or not table_exists(con, "price"):
        return []
    ids = sorted(set(stock_ids or ()))
    where_ids = ""
    params = [day, NO_TRADE, OFFICIAL_PRICE_SOURCE]
    if ids:
        where_ids = f" AND t.stock_id IN ({_marks(ids)})"
        params.extend(ids)
    return con.execute(
        f"""SELECT t.stock_id,t.status,t.source,t.reason
            FROM trading_status t
            JOIN price p ON p.date=t.date AND p.stock_id=t.stock_id
            WHERE t.date=? AND t.status=? AND t.source=?{where_ids}
              AND p.open IS NULL AND p.high IS NULL AND p.low IS NULL AND p.close IS NULL
              AND p.volume=0 AND p.amount=0 AND p.trades=0
            ORDER BY t.stock_id""",
        params,
    ).fetchall()


def verified_exclusion_ids(con, day, stock_ids=None):
    return {row[0] for row in verified_exclusions(con, day, stock_ids)}


def expected_ids(con, table, stock_ids, day):
    """各原始表當日應出現的股票。

    僅法人日報可排除官方零交易股票；價格、融資券、外資持股、借券仍要求完整 universe。
    """
    wanted = set(stock_ids)
    if table == "inst":
        wanted -= verified_exclusion_ids(con, day, wanted)
    return wanted
