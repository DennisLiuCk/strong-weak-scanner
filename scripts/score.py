#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
score.py — 五元素數值 → 分數(−2..+2)+ 綜合 + tier,寫入 daily_scores。
零第三方依賴。預設用「當前規則」重算全部歷史(調規則後要重跑才會一致)。

用法:
  uv run --no-project python scripts/score.py            # 重算全部並印最新日 tier
  uv run --no-project python scripts/score.py --date 2026-07-03

★ 策略優化就是調下面 CONFIG 的門檻與權重;改完重跑即可,validate.py 會告訴你哪個元素最準。
"""
import argparse, os, sqlite3, sys
from collections import defaultdict

try:                       # 讓輸出在任何 console(含 Windows cp950)都不會因中文/⚠ 崩潰
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")

# ══════════════════════════════════════════════════════════════════
# CONFIG ── 策略旋鈕(調這裡)
# ══════════════════════════════════════════════════════════════════
# 各元素門檻:list 由高到低,x >= 門檻 就給該分數;都不符合給 default。
TH_PRICE   = [(-0.03, 2), (-0.08, 1), (-0.15, 0), (-0.25, -1)]   # ①價:距60日高(近高=強)
TH_FOREIGN = [(3.0, 2), (1.0, 1), (-1.0, 0), (-3.0, -1)]          # ③外資:20日持股變化(pp)
TH_TRUST   = [(0.5, 2), (0.1, 1), (-0.1, 0), (-0.5, -1)]          # ④投信:近5日淨額(佔股本%)
DEFAULT_LOW = -2

# ②量:周轉率(雙面刃)—— 極高=過熱churn、太低=量縮無人氣、中間健康
VOL_OVERHEAT = 20.0   # 周轉率 >= 此值 → 過熱旗標
VOL_HEALTHY  = (3.0, 12.0)   # 此區間 → +1;>上界=0;1~下界=0;<1=-1

# ⑤融資券:以「融資10日變化」定方向(貼近我們手工的~2週視窗;不足10日退回5日),「散戶水位」加罰
# 備註:daily_metrics 另存了 margin_chg5/20,validate.py 可比較哪個窗預測力最好再改這裡。
TH_MARGIN_CHG = [(-0.08, 2), (-0.03, 1), (0.06, 0), (0.15, -1)]  # 融資大減=洗清(強)/暴增=追高(弱)
MARGIN_UTIL_HOT = 9.0   # 散戶水位 >= 此值 → 封頂 -1 並示警
MARGIN_UTIL_MID = 6.0   # >= 此值 → 分數封頂 +1

# 綜合權重(籌碼權重刻意高於價量)
WEIGHTS = {"price": 1.0, "vol": 0.6, "foreign": 1.6, "trust": 1.2, "margin": 1.3}

# tier 分界
STRONG_CUT = 4.0     # composite >= → 真強
WEAK_CUT   = -3.0    # composite <= → 真弱
STEALTH_MIN = 2.0    # 蓄勢需綜合仍為正(籌碼真的強、只是價未動)
# ══════════════════════════════════════════════════════════════════


def _ladder(x, table):
    """越高越好:table 由高到低,x >= 門檻 給該分。"""
    if x is None:
        return 0
    for thr, sc in table:
        if x >= thr:
            return sc
    return DEFAULT_LOW


def _ladder_low(x, table):
    """越低越好(⑤融資:融資減=強):table 由低到高,x <= 門檻 給該分。"""
    if x is None:
        return 0
    for thr, sc in table:
        if x <= thr:
            return sc
    return DEFAULT_LOW


def score_price(m):
    return _ladder(m["dist_hi60"], TH_PRICE)


def score_foreign(m):
    return _ladder(m["fpct_chg20"], TH_FOREIGN)


def score_trust(m):
    return _ladder(m["trust5_pct"], TH_TRUST)   # 近5日投信淨額佔股本 %(metrics 已用當日股本算好)


def score_vol(m):
    """回傳 (分數, 過熱旗標)。"""
    t = m["turnover_pct"]
    if t is None:
        return 0, False
    if t >= VOL_OVERHEAT:
        return -1, True                 # 爆量churn/過熱
    lo, hi = VOL_HEALTHY
    if t >= hi:
        return 0, False
    if t >= lo:
        return 1, False                 # 健康活量
    if t >= 1.0:
        return 0, False
    return -1, False                    # 量縮無人問津


def score_margin(m):
    """回傳 (分數, 水位過滿旗標)。方向用 10 日融資變化(貼近手工的~2週視窗),不足 10 日退回 5 日。"""
    chg = m["margin_chg10"] if m["margin_chg10"] is not None else m["margin_chg5"]
    base = _ladder_low(chg, TH_MARGIN_CHG)
    u = m["margin_util_pct"]
    warn = False
    if u is not None and u >= MARGIN_UTIL_HOT:
        base = min(base, -1)            # 散戶槓桿滿載 = 未來賣壓
        warn = True
    elif u is not None and u >= MARGIN_UTIL_MID and base > 1:
        base = 1
    return base, warn


def classify(s):
    comp = round(sum(WEIGHTS[k] * s[k] for k in WEIGHTS), 2)
    overheat = s["vol_warn"] or s["margin_warn"] or s["margin"] <= -2
    trap = s["foreign"] <= -1 and s["margin"] <= -1          # 外資出 + 散戶接 = 陷阱
    stealth = s["foreign"] >= 2 and s["price"] <= 1          # 籌碼強、價未動 = 蓄勢

    if trap:
        tier = "真弱·陷阱"
    elif s["price"] >= 1 and overheat:
        tier = "強但過熱"
    elif stealth and comp >= STEALTH_MIN:
        tier = "蓄勢·外資佈局"
    elif comp >= STRONG_CUT and s["price"] >= 1 and (s["foreign"] >= 1 or s["trust"] >= 1):
        tier = "真強"                                        # 真強:價在高檔 + 至少一種法人挺(不能只靠融資)
    elif comp <= WEAK_CUT:
        tier = "真弱"
    else:
        tier = "潛在/中性"
    warn = 1 if (trap or overheat) else 0
    return comp, tier, warn


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="只算單日;省略=重算全部歷史")
    args = ap.parse_args()

    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    con.execute("""CREATE TABLE IF NOT EXISTS daily_scores(
        date TEXT, stock_id TEXT, s_price INT, s_vol INT, s_foreign INT, s_trust INT, s_margin INT,
        composite REAL, tier TEXT, warn INT, PRIMARY KEY(date, stock_id))""")

    where = "WHERE date = ?" if args.date else ""
    params = (args.date,) if args.date else ()
    rows = con.execute(f"SELECT * FROM daily_metrics {where}", params).fetchall()

    out = []
    for m in rows:
        sp = score_price(m)
        sv, vwarn = score_vol(m)
        sf = score_foreign(m)
        st = score_trust(m)
        sm, mwarn = score_margin(m)
        s = {"price": sp, "vol": sv, "foreign": sf, "trust": st, "margin": sm,
             "vol_warn": vwarn, "margin_warn": mwarn}
        comp, tier, warn = classify(s)
        out.append((m["date"], m["stock_id"], sp, sv, sf, st, sm, comp, tier, warn))

    con.executemany("""INSERT OR REPLACE INTO daily_scores
        (date,stock_id,s_price,s_vol,s_foreign,s_trust,s_margin,composite,tier,warn)
        VALUES(?,?,?,?,?,?,?,?,?,?)""", out)
    con.commit()

    # ── 印最新日的 tier 排行 ──
    last = con.execute("SELECT MAX(date) FROM daily_scores").fetchone()[0]
    print(f"daily_scores 已更新 {len(out)} 列。最新日 {last} 的 tier:\n")
    q = """SELECT sc.stock_id,u.name,u.grp,sc.composite,sc.tier,sc.warn,
                  sc.s_price,sc.s_vol,sc.s_foreign,sc.s_trust,sc.s_margin
           FROM daily_scores sc JOIN universe u USING(stock_id)
           WHERE sc.date=? ORDER BY sc.composite DESC"""
    ORDER = ["真強", "蓄勢·外資佈局", "強但過熱", "潛在/中性", "真弱", "真弱·陷阱"]
    by_tier = defaultdict(list)
    for r in con.execute(q, (last,)):
        by_tier[r["tier"]].append(r)
    for tier in ORDER:
        rs = by_tier.get(tier, [])
        if not rs:
            continue
        print(f"■ {tier}  ({len(rs)})")
        for r in rs:
            flag = " ⚠" if r["warn"] else ""
            elem = f"價{r['s_price']:+d} 量{r['s_vol']:+d} 外{r['s_foreign']:+d} 投{r['s_trust']:+d} 融{r['s_margin']:+d}"
            print(f"   {r['stock_id']} {r['name']:<5} [{r['grp']:<8}] 綜{r['composite']:>5.1f}  {elem}{flag}")
        print()
    con.close()


if __name__ == "__main__":
    main()
