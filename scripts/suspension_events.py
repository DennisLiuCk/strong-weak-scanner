"""官方減資停牌證據：只豁免有明確起訖的整日停牌，不補造價格。

按缺價日取件；只保存該日、該股票的證據，不把公告或舊查核外推到未來。
每次讀取離線重算原文 SHA 並重解析日期。SHA 是完整性檢查，不是簽章或 ACL。
一般臨時停牌／無復牌日仍維持硬停，不能拿本契約無條件豁免。
"""
import hashlib
import json
import re
import time
import urllib.request
from datetime import date, datetime, timedelta, timezone


SOURCE = "official_capital_reduction"
URLS = {
    "TWSE": "https://www.twse.com.tw/rwd/zh/reducation/TWTAVU?response=json",
    "TPEx": "https://www.tpex.org.tw/www/zh-tw/bulletin/decap?response=json",
}
TAIPEI = timezone(timedelta(hours=8))
SCHEMA = """
CREATE TABLE IF NOT EXISTS suspension_evidence(
  date TEXT NOT NULL, stock_id TEXT NOT NULL, market TEXT NOT NULL,
  source_url TEXT NOT NULL, fetched_at TEXT NOT NULL,
  payload_json TEXT NOT NULL, payload_sha256 TEXT NOT NULL,
  PRIMARY KEY(date,stock_id)
);
"""


def _date(value):
    value = str(value).strip()
    if re.fullmatch(r"\d{3}/\d{2}/\d{2}", value):
        year, month, day = map(int, value.split("/"))
        return date(year + 1911, month, day).isoformat()
    if re.fullmatch(r"\d{7}", value):
        return date(int(value[:3]) + 1911, int(value[3:5]), int(value[5:])).isoformat()
    if re.fullmatch(r"\d{8}", value):
        return date(int(value[:4]), int(value[4:6]), int(value[6:])).isoformat()
    raise ValueError(f"停牌公告日期格式不明:{value!r}")


def parse_notices(market, payload):
    """按官方欄名解析，拒絕 schema 漂移、日期缺漏或同股衝突。"""
    if market not in URLS or not isinstance(payload, dict):
        raise ValueError("停牌公告來源／payload 不合法")
    if str(payload.get("stat", "")).lower() != "ok":
        raise ValueError("停牌公告 stat 非 OK（不能視為無公告）")
    tables = payload.get("tables") if market == "TPEx" else [payload]
    code_field = "代號" if market == "TPEx" else "股票代號"
    required = (code_field, "停止買賣日期", "恢復買賣日期", "減資原因")
    matches = [t for t in (tables or []) if isinstance(t, dict)
               and all(f in t.get("fields", []) for f in required)]
    if len(matches) != 1:
        raise ValueError("停牌公告缺唯一減資日期表")
    table = matches[0]
    fields, rows = table["fields"], table.get("data")
    if not isinstance(rows, list) or len(fields) != len(set(fields)):
        raise ValueError("停牌公告欄位／列格式錯誤")
    if "totalCount" in table and int(table["totalCount"]) != len(rows):
        raise ValueError("停牌公告列數不完整")
    notices = {}
    for values in rows:
        if not isinstance(values, list) or len(values) != len(fields):
            raise ValueError("停牌公告列與欄位不符")
        row = dict(zip(fields, values))
        sid = str(row[code_field]).strip()
        start, resume = _date(row["停止買賣日期"]), _date(row["恢復買賣日期"])
        reason = str(row["減資原因"]).strip()
        if not re.fullmatch(r"\d{4,6}", sid) or start >= resume or not reason:
            raise ValueError(f"停牌公告代號／起訖／原因不合法:{sid}")
        item = (start, resume, reason)
        if sid in notices and notices[sid] != item:
            raise ValueError(f"停牌公告同股衝突:{sid}")
        notices[sid] = item
    return notices


def fetch_notice(market):
    """固定官方來源；暫時性網路錯誤重試，不能把錯誤轉成空公告。"""
    for attempt in range(3):
        try:
            req = urllib.request.Request(URLS[market], headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as response:
                return response.read().decode("utf-8-sig")
        except OSError:
            if attempt == 2:
                raise
            time.sleep(attempt + 1)


def record_evidence(con, day, stock_ids, market, raw, fetched_at):
    """保留完整 API 回應，僅授權已到期資料日與有公告的缺價股。"""
    day = date.fromisoformat(day).isoformat()
    observed = datetime.fromisoformat(fetched_at)
    if observed.tzinfo is None or day > observed.astimezone(TAIPEI).date().isoformat():
        raise ValueError("停牌證據不能預先授權未來資料日")
    payload = json.loads(raw)
    notices = parse_notices(market, payload)
    if market == "TPEx" and not day <= _date(payload.get("date", "")) <= observed.astimezone(TAIPEI).date().isoformat():
        raise ValueError("櫃買減資預告回應日期落後資料日")
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    con.executescript(SCHEMA)
    accepted = []
    for sid in sorted(set(stock_ids)):
        notice = notices.get(sid)
        if not notice or not notice[0] <= day < notice[1]:
            continue
        if con.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='security_market'").fetchone():
            known = con.execute("SELECT market FROM security_market WHERE stock_id=?", (sid,)).fetchone()
            if known and known[0] != market:
                raise ValueError(f"停牌公告與股票市場衝突:{sid}/{market}")
        # 減資公告不准覆蓋已存在的價格；零交易原始列走原來的契約。
        if con.execute("SELECT 1 FROM price WHERE date=? AND stock_id=?", (day, sid)).fetchone():
            continue
        con.execute("INSERT OR REPLACE INTO suspension_evidence VALUES(?,?,?,?,?,?,?)",
                    (day, sid, market, URLS[market], fetched_at, raw, digest))
        accepted.append(sid)
    con.commit()
    return accepted


def resolve_missing_prices(con, day, stock_ids, fetcher=None):
    """缺價才查兩市場公告；未知缺漏仍交由價格完整性閘門標紅。"""
    fetcher = fetcher or fetch_notice
    requests, errors, accepted = 0, [], []
    for market in URLS:
        requests += 1
        try:
            raw = fetcher(market)
            accepted.extend(record_evidence(
                con, day, stock_ids, market, raw,
                datetime.now(TAIPEI).isoformat(timespec="seconds")))
        except (OSError, ValueError, TypeError) as exc:
            errors.append(f"{market}:{exc}")
    print(f"停牌公告 {day}:官方 requests {requests}；有證據 {','.join(accepted) or '無'}")
    for error in errors:
        print(f"  ! 停牌公告查核失敗:{error}")
    return {"requests": requests, "accepted": accepted, "errors": errors}


def verified(con, day, stock_ids=None):
    """唯讀重算證據，不信任人工 status 標記；回傳 (sid,status,source,reason)。"""
    if not con.execute("SELECT 1 FROM sqlite_master WHERE type='table' "
                       "AND name='suspension_evidence'").fetchone():
        return []
    wanted = None if stock_ids is None else set(stock_ids)
    result = []
    for row in con.execute("SELECT stock_id,market,source_url,fetched_at,payload_json,payload_sha256 "
                           "FROM suspension_evidence WHERE date=?", (day,)):
        sid, market, url, fetched, raw, digest = row
        if wanted is not None and sid not in wanted:
            continue
        if url != URLS.get(market) or hashlib.sha256(raw.encode("utf-8")).hexdigest() != digest:
            raise ValueError(f"停牌證據來源／SHA 不符:{day}/{sid}")
        payload = json.loads(raw)
        notice = parse_notices(market, payload).get(sid)
        observed = datetime.fromisoformat(fetched)
        if (not notice or not notice[0] <= day < notice[1] or observed.tzinfo is None
                or day > observed.astimezone(TAIPEI).date().isoformat()
                or (market == "TPEx" and not day <= _date(payload.get("date", ""))
                    <= observed.astimezone(TAIPEI).date().isoformat())):
            raise ValueError(f"停牌證據日期不符:{day}/{sid}")
        price = con.execute("SELECT open,high,low,close,volume,amount,trades FROM price "
                            "WHERE date=? AND stock_id=?", (day, sid)).fetchone()
        if price:
            if tuple(price) != (None, None, None, None, 0, 0, 0):
                raise ValueError(f"停牌公告與實際價格衝突:{day}/{sid}")
            continue  # 官方零交易列使用 price 契約，價格本身仍需稽核。
        start, resume, reason = notice
        result.append((sid, "no_trade", SOURCE,
                       f"{market} {reason}；{start} 起停止買賣，{resume} 恢復；"
                       f"原文 SHA256={digest}；{url}"))
    return result
