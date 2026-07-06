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
  # 只回補單一 dataset(新表補歷史用;跳過事件段、仍重算 metrics)
  uv run --no-project python scripts/fetch_daily.py --datasets TaiwanDailyShortSaleBalances --start 2026-03-01
  # 定向補缺:只抓指定股票(省 API 額度;可與 --datasets 疊加)
  uv run --no-project python scripts/fetch_daily.py --stocks 6510,6515 --start 2026-03-02

Token 讀取順序:環境變數 FINMIND_TOKEN → 專案根目錄 .mcp.json。
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

DATASETS = ["TaiwanStockPrice", "TaiwanStockInstitutionalInvestorsBuySell",
            "TaiwanStockMarginPurchaseShortSale", "TaiwanStockShareholding",
            "TaiwanDailyShortSaleBalances"]

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
CREATE TABLE IF NOT EXISTS dividend_result(date TEXT, stock_id TEXT, before_price REAL,
  reference_price REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS split_event(date TEXT, stock_id TEXT, before_price REAL,
  after_price REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS market(date TEXT PRIMARY KEY, taiex REAL);
CREATE TABLE IF NOT EXISTS price_adj(date TEXT, stock_id TEXT, close REAL, PRIMARY KEY(date,stock_id));
CREATE TABLE IF NOT EXISTS fetch_log(ts TEXT, start TEXT, "end" TEXT, rows INTEGER);
"""

_TOKENS = []   # get_tokens() 快取
_TOK_I = 0     # 402 輪替黏性指標:換到新 token 後,行程內後續呼叫直接沿用

def get_tokens():
    """可用 token 清單:環境變數 FINMIND_TOKEN/FINMIND_TOKEN2 → .mcp.json 同名欄位。
    多組 token = 時額(600/hr)輪替池;402 時 api_get 自動換下一組。"""
    global _TOKENS
    if _TOKENS:
        return _TOKENS
    ts = [os.environ[k] for k in ("FINMIND_TOKEN", "FINMIND_TOKEN2") if os.environ.get(k)]
    if not ts:
        with open(os.path.join(ROOT, ".mcp.json"), encoding="utf-8") as f:
            env = json.load(f)["mcpServers"]["finmind"]["env"]
        ts = [env[k] for k in ("FINMIND_TOKEN", "FINMIND_TOKEN2") if env.get(k)]
    # GitHub secret 貼上時可能夾帶 BOM(例如來源檔案存成「UTF-8 with BOM」)——
    # 混進 Authorization header 會讓 latin-1 編碼直接炸掉,且 api_get 逐檔 catch 例外,
    # 會變成「全部靜默失敗、job 卻顯示成功」(2026-07-06 事故:GH Actions 兩次 run 皆 0 rows)。
    _TOKENS = [t.strip().lstrip("﻿") for t in ts]
    return _TOKENS

def get_token():
    return get_tokens()[0]

def api_get(dataset, data_id, start, end, token, retries=3):
    global _TOK_I
    tokens = get_tokens() or [token]
    p = {"dataset": dataset, "start_date": start, "end_date": end}
    if data_id:
        p["data_id"] = data_id          # 部分 dataset(如 TaiwanStockSplitPrice)全市場一次回傳
    q = urllib.parse.urlencode(p)
    url = API + "?" + q
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                "Authorization": "Bearer " + tokens[_TOK_I % len(tokens)]})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp).get("data", [])
        except Exception as e:
            if getattr(e, "code", None) == 402 and len(tokens) > 1 and i < retries - 1:
                _TOK_I += 1              # 額度用盡 → 輪替下一組立即重試(不退避)
                print(f"  ! 402 額度用盡,輪替 token → #{_TOK_I % len(tokens) + 1}", file=sys.stderr)
                continue
            if i == retries - 1:
                print(f"  ! {dataset} {data_id} 失敗: {e}", file=sys.stderr)
                return []
            time.sleep(2 * (i + 1))  # 遇限流退避重試
    return []

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

def fetch_index(con, token, start, end, sleep):
    """加權報酬指數(TAIEX,含息)→ market(upsert)。大盤 regime 旗標的原料。"""
    data = api_get("TaiwanStockTotalReturnIndex", "TAIEX", start, end, token)
    rows = [(d["date"], d.get("price")) for d in data
            if d.get("stock_id") == "TAIEX" and d.get("price")]   # 防呆:只收 TAIEX 序列
    if rows:
        con.executemany("INSERT OR REPLACE INTO market VALUES(?,?)", rows)
        con.commit()
    else:
        print("  ! TAIEX 指數抓取為空——市場 regime 將沿用舊資料", file=sys.stderr)
    time.sleep(sleep)
    return len(rows)

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
        req = urllib.request.Request(
            f"{TWSE_QFIIS_URL}?date={ymd}&selectType=ALLBUT0999&response=json",
            headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            d = json.load(resp)
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
            req = urllib.request.Request(TPEX_QFII_URL, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                rows = json.load(resp)
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
    價格類(ret1/ret20/距高)用還原價;股本取「當日」值(forward-fill)。
    兩段式:先算每檔基礎序列 → 族群逐日中位數 → 再合成「族群相對」指標:
    rs20(20日相對強弱)、down_rs20(族群下跌日抗跌)、dipbuy20(逆勢買超)。"""
    con.execute("DROP TABLE IF EXISTS daily_metrics")
    con.execute("""CREATE TABLE daily_metrics(
        date TEXT, stock_id TEXT, close REAL, close_adj REAL, ret1 REAL, ret20 REAL,
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
        ret1s = [(adj[k] / adj[k-1] - 1) if (k > 0 and adj[k-1] and adj[k]) else None for k in range(n)]
        ret20s = [(adj[k] / adj[k-20] - 1) if (k >= 20 and adj[k-20] and adj[k]) else None for k in range(n)]
        S[sid] = dict(grp=grp, rows=rows, adj=adj, sh=sh, turn=turn, ret1=ret1s, ret20=ret20s)
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
            out.append((d, sid, close, ca, ret1, ret20, turnover, vratio,
                        (ca/hi20 - 1) if (hi20 and ca) else None, (ca/hi60 - 1) if (hi60 and ca) else None,
                        rs20, down_rs20, fp, fchg5, fchg20, dipbuy20, dipbuy20_t,
                        trust5, trust5_pct, foreign5, mb, mutil, mchg5, mchg10, mchg20, smr,
                        td, b4, b4c, b10, b10c, ppc, sblv, sblc5, sblc10, sblc20))
        con.executemany("INSERT OR REPLACE INTO daily_metrics VALUES(" + ",".join("?" * 36) + ")", out)
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
    if args.stocks:
        want = {s.strip() for s in args.stocks.split(",") if s.strip()}
        missing = want - set(ids)
        if missing:
            sys.exit(f"--stocks 含 universe 外代號:{sorted(missing)}")
        ids = [s for s in ids if s in want]
    print(f"抓取 {start} .. {end} · {len(ids)} 檔 · {len(ds_list)} datasets")
    total = 0
    for i, sid in enumerate(ids, 1):
        got = 0
        for ds in ds_list:
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
    if args.datasets:
        print("(--datasets 過濾:跳過除權息/分割/指數事件抓取,仍重算 price_adj 與 metrics)")
    else:
        adj_start = con.execute("SELECT MIN(date) FROM price").fetchone()[0] or start
        today = date.today().isoformat()
        print(f"除權息/分割事件 {adj_start} .. {today} …")
        nd = fetch_dividends(con, ids, token, adj_start, today, args.sleep)
        ns = fetch_splits(con, ids, token, adj_start, today, args.sleep)
        ni = fetch_index(con, token, adj_start, today, args.sleep)
        print(f"dividend_result upsert {nd};split_event upsert {ns};TAIEX {ni}")
    if "TaiwanStockShareholding" in ds_list:
        n_bf = backfill_holding_from_exchange(con, end)
        if n_bf:
            print(f"外資持股 TWSE/TPEx 備援:補上 {n_bf} 檔")
    build_price_adj(con)
    print("重算 daily_metrics + 族群/大盤層 …")
    build_metrics(con)
    build_group_market(con)
    n = con.execute("SELECT COUNT(*) FROM daily_metrics").fetchone()[0]
    con.close()
    print(f"完成 — 原始 {total} rows 落地,daily_metrics {n} rows → {DB}")

if __name__ == "__main__":
    main()
