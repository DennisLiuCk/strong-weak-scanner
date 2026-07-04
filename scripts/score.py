#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
score.py — v2 族群內橫斷面排名評分 + tier,寫入 daily_scores。
零第三方依賴。每次用「當前規則」重算全部歷史(調規則後重跑即一致)。
舊絕對門檻制(v1)最後結果凍結於 daily_scores_v1(2026-07-05),供 validate 對照。

v2 核心改變(依 2026-07-05 方法論 review 實證):
  * 排名制:各元素在「族群內」按分位數給 −2..+2 —— 解決絕對門檻的個股結構偏誤
    (日月光永遠拿不到外資+2、小型股躺著滿分)。
  * ⑤融資改「價×融資」交互;②量改「相對自身 60 日中位」量比。
  * 蓄勢加質量濾網:修正日抗跌(down_rs20)不得輸族群 —— 排除華泰式假佈局。
  * 遲滯:composite 取 3 日平滑;tier 需連 2 日同 raw 才轉層(v1 日均 7.2/30 檔換層)。

v2.1 權重再校準(族群內 IC 診斷,2026-07-05):
  * 族群內選股靠「價格相對」:rs20 相對強弱(族群內 IC +0.155)、down_rs20 抗跌(+0.119)
    → s_price 改排名 rs20、新元素 s_resil 排名 down_rs20,兩者權重最高。
  * 籌碼(fpct_chg20 −0.007、dipbuy20 −0.096)在「族群內」沒有選股力 —— 它們是
    「族群層」訊號(v1 混池 IC +0.07 全來自跨族群選對族群)。故 s_foreign 降權、
    s_dip 權重 0(只用於蓄勢 tier 條件與儀表板顯示);族群層籌碼聚合屬 Phase 2。
  * 此為 in-sample 校準 + 因子先驗(橫斷面動能/低下行 beta 是最強健的已知因子);
    正式評判交給 validate.py 的 out-of-sample 累積。

★ 策略優化調下面 CONFIG;validate.py(Phase 3)會告訴你哪個元素/權重最準。
"""
import argparse, os, sqlite3, statistics, sys
from collections import defaultdict, deque

try:                       # 讓輸出在任何 console(含 Windows cp950)都不會因中文/⚠ 崩潰
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")

# ══════════════════════════════════════════════════════════════════
# CONFIG ── 策略旋鈕(調這裡)
# ══════════════════════════════════════════════════════════════════
# 族群內百分位 → 分數(0=最弱,1=最強);低於最後一檔門檻給 -2
RANK_MAP = [(0.8, 2), (0.6, 1), (0.4, 0), (0.2, -1)]

# 雜訊死區:|原始值| 低於此,不論排名一律 0 分(全族群無訊號時,排名只會放大雜訊)
DZ_FOREIGN = 0.3     # fpct_chg20(pp)
DZ_TRUST   = 0.03    # trust5_pct(佔股本 %)
DZ_DIP     = 0.03    # dipbuy20(佔股本 %)

# ②量:量比(相對自身 60 日中位)
VOLR_ACTIVE   = (1.2, 3.0)   # 健康活絡 → +1
VOLR_DRY      = 0.5          # 低於 → -1(無人氣)
VOL_OVERHEAT  = 20.0         # 周轉率絕對過熱旗標(%)
VOLR_OVERHEAT = 5.0          # 量比過熱旗標

# ⑤融資:價(ret20)×融資(margin_chg10)交互
MARGIN_DOWN_BIG = -0.05      # 融資 10 日大減
MARGIN_UP_MID   = 0.06       # 融資 10 日明顯增
MARGIN_UP_BIG   = 0.20       # 融資 10 日暴增
MARGIN_UTIL_HOT = 9.0        # 散戶水位(%)≥ → 封頂 -1 並示警
MARGIN_UTIL_MID = 6.0        # ≥ → 封頂 +1

# 綜合權重(v2.1:族群內選股以價格相對因子為主,籌碼降權/歸零 —— 見檔頭說明)
WEIGHTS = {"price": 1.4, "resil": 1.0, "vol": 0.3, "foreign": 0.5, "trust": 0.8,
           "dip": 0.0, "margin": 0.4}

# 蓄勢 tier 的「價未動」定義:距 60 日高至少落後此幅度
STEALTH_OFF_HIGH = -0.03

SMOOTH_N    = 3      # composite 平滑天數
STRONG_MIN  = 2.5    # 真強:族群 comp_s 前 2 名 且 comp_s ≥ 此值(避免「爛族群裡的最好」)
WEAK_ABS    = -3.5   # 真弱絕對線(或族群倒數 2 名且 comp_s < 0)
STEALTH_MIN = 1.5    # 蓄勢最低 comp_s
# ══════════════════════════════════════════════════════════════════


def rank_scores(vals, deadzone=None):
    """族群內橫斷面:原始值 list → −2..+2 分數 list(五分位)。
    None 不參與排名、給 0;參與檔數 <4 全給 0;死區內強制 0。"""
    out = [0] * len(vals)
    idx = [i for i, v in enumerate(vals) if v is not None]
    m = len(idx)
    if m < 4:
        return out
    order = sorted(idx, key=lambda i: vals[i])
    for pos, i in enumerate(order):
        pct = pos / (m - 1)
        s = -2
        for thr, sc in RANK_MAP:
            if pct >= thr:
                s = sc
                break
        out[i] = s
    if deadzone is not None:
        for i in idx:
            if abs(vals[i]) < deadzone:
                out[i] = 0
    return out


def score_vol(m):
    """量比制。回傳 (分數, 過熱旗標)。"""
    vr, t = m["vol_ratio60"], m["turnover_pct"]
    warn = (t is not None and t >= VOL_OVERHEAT) or (vr is not None and vr >= VOLR_OVERHEAT)
    if vr is None:
        return 0, warn
    if VOLR_ACTIVE[0] <= vr <= VOLR_ACTIVE[1]:
        return 1, warn
    if vr < VOLR_DRY:
        return -1, warn
    return 0, warn


def score_margin(m):
    """價(ret20)×融資(chg10,不足退 chg5)交互 + 散戶水位封頂。回傳 (分數, 水位旗標)。"""
    chg = m["margin_chg10"] if m["margin_chg10"] is not None else m["margin_chg5"]
    r20 = m["ret20"]
    down = r20 is not None and r20 < 0
    if chg is None:
        base = 0
    elif chg <= MARGIN_DOWN_BIG:
        base = 2 if down else 1          # 價跌融資減=洗盤(最佳);價漲融資減=健康換手
    elif chg >= MARGIN_UP_BIG:
        base = -2                        # 融資暴增:無論價格方向都是散戶湧入
    elif chg >= MARGIN_UP_MID:
        base = -2 if down else -1        # 價跌融資增=散戶接刀(最凶);價漲融資增=追高
    else:
        base = 0
    u = m["margin_util_pct"]
    warn = False
    if u is not None and u >= MARGIN_UTIL_HOT:
        base = min(base, -1)
        warn = True
    elif u is not None and u >= MARGIN_UTIL_MID:
        base = min(base, 1)
    return base, warn


def main():
    argparse.ArgumentParser(description="v2 排名制評分(永遠重算全歷史)").parse_args()
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    con.execute("DROP TABLE IF EXISTS daily_scores")
    con.execute("""CREATE TABLE daily_scores(
        date TEXT, stock_id TEXT,
        s_price INT, s_resil INT, s_vol INT, s_foreign INT, s_trust INT, s_dip INT, s_margin INT,
        composite REAL, composite_s REAL, tier_raw TEXT, tier TEXT, warn INT,
        pending TEXT,   -- 蓄勢候補:籌碼條件已符、尚差哪些蓄勢條件(顯示用,不影響 tier)
        PRIMARY KEY(date, stock_id))""")

    rows = con.execute("""SELECT m.*, u.grp FROM daily_metrics m
                          JOIN universe u USING(stock_id) ORDER BY m.date""").fetchall()
    by_date = defaultdict(lambda: defaultdict(list))   # date -> grp -> [row]
    for r in rows:
        by_date[r["date"]][r["grp"]].append(r)

    comp_hist = defaultdict(lambda: deque(maxlen=SMOOTH_N))   # 平滑用
    prev_raw, prev_tier = {}, {}                              # 遲滯用
    out = []
    for d in sorted(by_date):
        for grp, ms in by_date[d].items():
            s_price = rank_scores([m["rs20"] for m in ms])          # 20日相對強弱(族群內最強因子)
            s_resil = rank_scores([m["down_rs20"] for m in ms])     # 修正日抗跌
            s_foreign = rank_scores([m["fpct_chg20"] for m in ms], DZ_FOREIGN)
            s_trust = rank_scores([m["trust5_pct"] for m in ms], DZ_TRUST)
            s_dip = rank_scores([m["dipbuy20"] for m in ms], DZ_DIP)
            scored = []
            for i, m in enumerate(ms):
                sv, vwarn = score_vol(m)
                sm, mwarn = score_margin(m)
                s = {"price": s_price[i], "resil": s_resil[i], "vol": sv, "foreign": s_foreign[i],
                     "trust": s_trust[i], "dip": s_dip[i], "margin": sm}
                comp = round(sum(WEIGHTS[k] * s[k] for k in WEIGHTS), 2)
                comp_hist[m["stock_id"]].append(comp)
                comp_s = round(sum(comp_hist[m["stock_id"]]) / len(comp_hist[m["stock_id"]]), 2)
                scored.append((m, s, vwarn, mwarn, comp, comp_s))
            # 族群內以平滑綜合分排名(1=最強)
            grank = {id(t): rk + 1 for rk, t in
                     enumerate(sorted(scored, key=lambda t: -t[5]))}
            n = len(scored)
            for t in scored:
                m, s, vwarn, mwarn, comp, comp_s = t
                sid = m["stock_id"]
                overheat = vwarn or mwarn
                trap = (s["foreign"] <= -1 and s["margin"] <= -1
                        and m["rs20"] is not None and m["rs20"] < 0)
                stealth = ((s["foreign"] >= 2 or s["dip"] >= 2)
                           and m["dist_hi60"] is not None and m["dist_hi60"] <= STEALTH_OFF_HIGH
                           and m["down_rs20"] is not None and m["down_rs20"] >= 0
                           and comp_s >= STEALTH_MIN)          # 籌碼吃貨+價未動+修正日不輸族群
                if trap:
                    tier_raw = "真弱·陷阱"
                elif s["price"] >= 1 and overheat:
                    tier_raw = "強但過熱"
                elif stealth:
                    tier_raw = "蓄勢·外資佈局"
                elif (grank[id(t)] <= 2 and comp_s >= STRONG_MIN and s["price"] >= 1
                      and (s["foreign"] >= 1 or s["trust"] >= 1 or s["dip"] >= 1)):
                    tier_raw = "真強"
                elif comp_s <= WEAK_ABS or (grank[id(t)] >= n - 1 and comp_s < 0):
                    tier_raw = "真弱"
                else:
                    tier_raw = "潛在/中性"
                # 遲滯:連 2 日同 raw tier 才轉層,否則沿用昨日已確認 tier
                if prev_tier.get(sid) is None or prev_raw.get(sid) == tier_raw:
                    tier = tier_raw
                else:
                    tier = prev_tier[sid]
                prev_raw[sid], prev_tier[sid] = tier_raw, tier
                warn = 1 if (trap or overheat) else 0
                # 蓄勢候補:籌碼吃貨但還沒到蓄勢 —— 標出差哪幾項(cohort 實證:差「抗跌」者
                # 10日仍落後族群,但20日多會補上 → 是「等時機」名單,不是弱股)
                pending = None
                if (s["foreign"] >= 2 or s["dip"] >= 2) and tier_raw == "潛在/中性":
                    miss = []
                    if not (m["dist_hi60"] is not None and m["dist_hi60"] <= STEALTH_OFF_HIGH):
                        miss.append("價未動")
                    if not (m["down_rs20"] is not None and m["down_rs20"] >= 0):
                        miss.append("抗跌")
                    if comp_s < STEALTH_MIN:
                        miss.append("綜合分")
                    if miss:
                        pending = "蓄勢候補·差:" + "、".join(miss)
                out.append((d, sid, s["price"], s["resil"], s["vol"], s["foreign"], s["trust"],
                            s["dip"], s["margin"], comp, comp_s, tier_raw, tier, warn, pending))
    con.executemany("INSERT OR REPLACE INTO daily_scores VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", out)
    con.commit()

    # ── 印最新日的 tier 排行 ──
    last = con.execute("SELECT MAX(date) FROM daily_scores").fetchone()[0]
    print(f"daily_scores(v2 排名制)已更新 {len(out)} 列。最新日 {last}:\n")
    def fnum(v, fmt):
        return fmt.format(v) if v is not None else "-"
    have = {r[0] for r in con.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name IN ('market_daily','group_metrics')")}
    if {"market_daily", "group_metrics"} <= have:   # 舊 db 無族群/大盤表 → 略過(跑一次 fetch_daily 即補齊)
        # 指數資料可能落後個股一日 → 取 ≤last 的最近一筆
        mk = con.execute("""SELECT * FROM market_daily WHERE date<=? AND dd20 IS NOT NULL
                            ORDER BY date DESC LIMIT 1""", (last,)).fetchone()
        if mk:
            lag = "" if mk["date"] == last else f"(指數至 {mk['date']})"
            print(f"市場:報酬指數(含息){mk['taiex']:,.0f},距20日高 {mk['dd20']*100:+.1f}%{lag} → "
                  f"{'⚠ 修正 regime(抗跌/投信因子最有效的環境)' if mk['regime'] else '多頭/中性 regime'}")
        print("族群雷達(修正日中位淨買=候選主訊號,OOS 驗證中):")
        for g in con.execute("SELECT * FROM group_metrics WHERE date=? ORDER BY grp", (last,)):
            print(f"   {g['grp']:<9} {g['state']:<7} 修正日淨買{fnum(g['med_dip'], '{:+.2f}%')} "
                  f"廣度{fnum(g['breadth_f'], '{:.0%}')} 動能vs全體{fnum(g['rel20'], '{:+.1%}')} "
                  f"距60日高{fnum(g['med_dist60'], '{:+.1%}')}")
        print()
    q = """SELECT sc.*, u.name, u.grp FROM daily_scores sc JOIN universe u USING(stock_id)
           WHERE sc.date=? ORDER BY sc.composite_s DESC"""
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
            pend = "" if r["tier_raw"] == r["tier"] else f" →{r['tier_raw']}?"
            cand = f" ◇{r['pending']}" if r["pending"] else ""
            elem = (f"價{r['s_price']:+d} 抗{r['s_resil']:+d} 量{r['s_vol']:+d} 外{r['s_foreign']:+d} "
                    f"投{r['s_trust']:+d} 逆{r['s_dip']:+d} 融{r['s_margin']:+d}")
            print(f"   {r['stock_id']} {r['name']:<5} [{r['grp']:<8}] 綜{r['composite_s']:>5.1f}  {elem}{flag}{pend}{cand}")
        print()
    con.close()


if __name__ == "__main__":
    main()
