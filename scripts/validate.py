#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate.py — 週度驗證報告。讀 db 不寫 db,輸出 reports/validate_<資料迄日>.md + console 摘要。
零第三方依賴。報酬一律用還原收盤(daily_metrics.close_adj)。

驗什麼:
  ① 元素 IC:族群內(=汰弱留強的正確量尺)與混池,分 全期/OOS/修正/多頭
  ② tier 前瞻超額(vs 族群中位)與 tier「轉移」事件(升層/降層才是交易訊號)
  ③ 蓄勢濾網 cohort(含 v1/v2 對照於 ①②)
  ④ 族群層:med_dip 最高者領漲命中率、各 state 的族群前瞻超額
  ⑤ 市值公平性監測(影子因子 + tier 佔用 by 市值三分位)
  ⑥ 觀察因子(Phase 4a:TDCC 大戶/借券賣出餘額——未計分,IC 追蹤等 OOS 裁決歸宿)

判讀紀律:
  * IS_CUTOFF(2026-07-05)前屬 in-sample —— v2.1 權重在該窗校準,數字必然好看;
    真正的評判是 OOS 欄(2026-07-06 起累積,需 2~4 週才有意義)。
  * 前瞻視窗重疊 → 顯著性高估;30 檔小樣本 → 每次檢視最多調 1~2 個旋鈕。

用法:
  uv run --no-project python scripts/validate.py           # 預設 10 日前瞻
  uv run --no-project python scripts/validate.py --fwd 5
"""
import argparse, os, sqlite3, statistics, sys
from collections import defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
REPORTS = os.path.join(ROOT, "reports")
IS_CUTOFF = "2026-07-05"      # v2.1 權重校準日:此日(含)之前 = in-sample
ELEMENTS = ["s_price", "s_resil", "s_vol", "s_foreign", "s_trust", "s_dip", "s_margin",
            "composite", "composite_s"]


def rankdata(x):
    idx = sorted(range(len(x)), key=lambda i: x[i])
    rk, i = [0.0] * len(x), 0
    while i < len(idx):
        j = i
        while j + 1 < len(idx) and x[idx[j+1]] == x[idx[i]]:
            j += 1
        r = (i + j) / 2 + 1
        for k in range(i, j + 1):
            rk[idx[k]] = r
        i = j + 1
    return rk


def spearman(a, b, minn=6):
    p = [(x, y) for x, y in zip(a, b) if x is not None and y is not None]
    if len(p) < minn:
        return None
    xa, yb = rankdata([q[0] for q in p]), rankdata([q[1] for q in p])
    mx, my = statistics.mean(xa), statistics.mean(yb)
    num = sum((x - mx) * (y - my) for x, y in zip(xa, yb))
    dx = sum((x - mx) ** 2 for x in xa) ** 0.5
    dy = sum((y - my) ** 2 for y in yb) ** 0.5
    return num / (dx * dy) if dx and dy else None


def mean(v):
    return statistics.mean(v) if v else None


def fmt_ic(v, n=None):
    if v is None:
        return "–"
    s = f"{v:+.3f}"
    return f"{s} (n={n})" if n is not None else s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fwd", type=int, default=10, help="前瞻交易日數")
    F = ap.parse_args().fwd

    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    uni = {r["stock_id"]: r["grp"] for r in con.execute("SELECT stock_id, grp FROM universe")}
    try:   # 族群清單配置化(groups 表);舊 db 退回 universe 去重
        GRPS = tuple(r[0] for r in con.execute("SELECT grp FROM groups ORDER BY ord"))
    except sqlite3.OperationalError:
        GRPS = ()
    if not GRPS:
        GRPS = tuple(sorted(set(uni.values())))
    dates = [r[0] for r in con.execute("SELECT DISTINCT date FROM daily_metrics ORDER BY date")]
    didx = {d: i for i, d in enumerate(dates)}
    cadj = {(r["date"], r["stock_id"]): r["close_adj"]
            for r in con.execute("SELECT date, stock_id, close_adj FROM daily_metrics")}
    regime = {r["date"]: r["regime"] for r in con.execute("SELECT date, regime FROM market_daily")}
    v2 = defaultdict(dict)
    for r in con.execute("SELECT * FROM daily_scores"):
        v2[r["date"]][r["stock_id"]] = r
    v1 = defaultdict(dict)
    try:
        for r in con.execute("SELECT * FROM daily_scores_v1"):
            v1[r["date"]][r["stock_id"]] = r
    except sqlite3.OperationalError:
        pass
    gm = defaultdict(dict)
    for r in con.execute("SELECT * FROM group_metrics"):
        gm[r["date"]][r["grp"]] = r
    met = defaultdict(dict)
    for r in con.execute("SELECT date, stock_id, dist_hi60, down_rs20, rs20, ret1, close FROM daily_metrics"):
        met[r["date"]][r["stock_id"]] = r
    obs = defaultdict(dict)   # §⑥ 觀察因子;舊 db 無欄位 → None,整節略過
    try:
        for r in con.execute("SELECT date, stock_id, tdcc_date, tdcc_big400_chg, tdcc_big1000_chg, "
                             "tdcc_people_chg, sbl_chg10, fpct_chg20 FROM daily_metrics"):
            obs[r["date"]][r["stock_id"]] = r
    except sqlite3.OperationalError:
        obs = None
    sh_latest = {}
    for r in con.execute("SELECT stock_id, shares_issued FROM holding "
                         "WHERE shares_issued IS NOT NULL ORDER BY date"):
        sh_latest[r["stock_id"]] = r["shares_issued"]   # 升冪覆寫 → 留最新

    def fwd(d, sid):
        i = didx.get(d)
        if i is None or i + F >= len(dates):
            return None
        a, b = cadj.get((d, sid)), cadj.get((dates[i + F], sid))
        return (b / a - 1) if (a and b) else None

    def bucket(d):
        """一天可同屬多個統計桶。"""
        bs = ["全期", "OOS" if d > IS_CUTOFF else "IS"]
        r = regime.get(d)
        if r == 1:
            bs.append("修正")
        elif r == 0:
            bs.append("多頭")
        return bs

    # ── ① 元素 IC ──────────────────────────────────────────────
    wg = defaultdict(lambda: defaultdict(list))    # factor -> bucket -> [ic per date×group]
    pool = defaultdict(lambda: defaultdict(list))  # factor -> bucket -> [ic per date]
    for d in dates:
        if d not in v2:
            continue
        bs = bucket(d)
        sids_all = [s for s in v2[d] if fwd(d, s) is not None]
        f_all = [fwd(d, s) for s in sids_all]
        cols = list(ELEMENTS)
        for el in cols:
            ic = spearman([v2[d][s][el] for s in sids_all], f_all, minn=15)
            if ic is not None:
                for b in bs:
                    pool[el][b].append(ic)
        if d in v1:
            ic = spearman([v1[d][s]["composite"] for s in sids_all if s in v1[d]],
                          [fwd(d, s) for s in sids_all if s in v1[d]], minn=15)
            if ic is not None:
                for b in bs:
                    pool["v1_composite"][b].append(ic)
        for g in GRPS:
            sids = [s for s in v2[d] if uni.get(s) == g and fwd(d, s) is not None]
            f = [fwd(d, s) for s in sids]
            for el in cols:
                ic = spearman([v2[d][s][el] for s in sids], f)
                if ic is not None:
                    for b in bs:
                        wg[el][b].append(ic)
            if d in v1:
                ic = spearman([v1[d][s]["composite"] for s in sids if s in v1[d]],
                              [fwd(d, s) for s in sids if s in v1[d]])
                if ic is not None:
                    for b in bs:
                        wg["v1_composite"][b].append(ic)

    # ── ② tier 前瞻超額 + 轉移事件 ─────────────────────────────
    def grp_med_fwd(d, g):
        v = [fwd(d, s) for s in uni if uni[s] == g]
        v = [x for x in v if x is not None]
        return statistics.median(v) if v else None

    tier_x = defaultdict(lambda: defaultdict(list))   # tier -> bucket -> [excess]
    for d in dates:
        if d not in v2:
            continue
        bs = bucket(d)
        gmed = {g: grp_med_fwd(d, g) for g in GRPS}
        for sid, r in v2[d].items():
            f, gv = fwd(d, sid), gmed.get(uni.get(sid))
            if f is None or gv is None:
                continue
            for b in bs:
                tier_x[r["tier"]][b].append(f - gv)

    trans = defaultdict(list)   # (from,to) -> [excess at transition day]
    for sid in uni:
        prev = None
        for d in dates:
            r = v2[d].get(sid)
            if r is None:
                continue
            if prev is not None and r["tier"] != prev:
                f, gv = fwd(d, sid), grp_med_fwd(d, uni[sid])
                if f is not None and gv is not None:
                    trans[(prev, r["tier"])].append(f - gv)
            prev = r["tier"]

    # ── ③ 蓄勢濾網 cohort:籌碼吃貨+價未動,按修正日抗跌分組 ──
    # 濾網存在理由:抗跌<0 組 10 日仍落後族群(v1 無濾網時蓄勢事件 −0.92%)。
    # 若 OOS 顯示該組不再落後(20 日視窗本就會收斂)→ 考慮放寬 STEALTH 的抗跌條件。
    OFF_HIGH = -0.03   # 同 score.py STEALTH_OFF_HIGH
    cohort = defaultdict(lambda: defaultdict(list))   # 分組 -> bucket -> [excess]
    for d in dates:
        if d not in v2:
            continue
        bs = bucket(d)
        for sid, sc in v2[d].items():
            m = met[d].get(sid)
            if m is None or not (sc["s_foreign"] >= 2 or sc["s_dip"] >= 2):
                continue
            if not (m["dist_hi60"] is not None and m["dist_hi60"] <= OFF_HIGH):
                continue
            f, gv = fwd(d, sid), grp_med_fwd(d, uni.get(sid))
            if f is None or gv is None:
                continue
            key = ("抗跌≥0(放行)" if m["down_rs20"] >= 0 else "領跌<0(擋下)") \
                if m["down_rs20"] is not None else "抗跌缺值"
            for b in bs:
                cohort[key][b].append(f - gv)

    # ── ④ 族群層 ──────────────────────────────────────────────
    dip_hit = defaultdict(list)   # bucket -> [1/0]
    state_x = defaultdict(list)   # state -> [group excess vs universe]
    for d in dates:
        if d not in gm:
            continue
        bs = bucket(d)
        gf = {}
        for g in GRPS:
            v = grp_med_fwd(d, g)
            if v is not None:
                gf[g] = v
        if len(gf) == len(GRPS):
            uv = statistics.median(gf.values())
            dips = {g: gm[d][g]["med_dip"] for g in GRPS
                    if g in gm[d] and gm[d][g]["med_dip"] is not None}
            if len(dips) == len(GRPS):
                leader = max(dips, key=dips.get)
                hit = 1 if gf[leader] == max(gf.values()) else 0
                for b in bs:
                    dip_hit[b].append(hit)
            for g in GRPS:
                if g in gm[d]:
                    state_x[gm[d][g]["state"]].append(gf[g] - uv)

    # ── ⑤ 市值公平性監測 ────────────────────────────────────────
    # (a) 影子因子:風險調整 rs20/σ20 vs 原始 rs20——「同一把尺」的兩種定義,
    #     若 OOS 持續分歧(尤其小型股行情期)才考慮換尺,現行評分不動。
    sigma, hist = {}, defaultdict(list)
    for d in dates:
        for sid, m in met[d].items():
            if m["ret1"] is not None:
                h = hist[sid]
                h.append(m["ret1"])
                if len(h) >= 20:
                    sigma[(d, sid)] = statistics.pstdev(h[-20:])
    ic_sz = defaultdict(lambda: defaultdict(list))
    for d in dates:
        if d not in met:
            continue
        bs = bucket(d)
        for g in GRPS:
            sids = [s for s in met[d] if uni.get(s) == g]
            f = [fwd(d, s) for s in sids]
            raw = [met[d][s]["rs20"] for s in sids]
            adj = [(met[d][s]["rs20"] / sigma[(d, s)])
                   if (met[d][s]["rs20"] is not None and sigma.get((d, s))) else None
                   for s in sids]
            for key, vals in (("rs20(原始)", raw), ("rs20/σ20(風險調整)", adj)):
                ic = spearman(vals, f)
                if ic is not None:
                    for b in bs:
                        ic_sz[key][b].append(ic)
    # (b) tier 佔用 by 族群內市值三分位(期末市值;監測同尺是否發展出持續傾斜)
    lastd = dates[-1]
    cap = {}
    for sid in uni:
        m = met.get(lastd, {}).get(sid)
        if m and m["close"] and sh_latest.get(sid):
            cap[sid] = m["close"] * sh_latest[sid]
    terc = {}
    for g in GRPS:
        sids = sorted([s for s in uni if uni[s] == g and s in cap], key=lambda s: cap[s])
        k = len(sids) // 3
        for i, s in enumerate(sids):
            terc[s] = "小" if i < k else ("大" if i >= len(sids) - k else "中")
    tsz = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    tszN = defaultdict(lambda: defaultdict(int))
    for d in dates:
        if d not in v2:
            continue
        bs = bucket(d)
        for sid, r in v2[d].items():
            tc = terc.get(sid)
            if not tc:
                continue
            for b in bs:
                tsz[b][r["tier"]][tc] += 1
                tszN[b][tc] += 1

    # ── ⑥ 觀察因子(Phase 4a:未計分,IC 追蹤等 OOS 裁決歸宿)────
    OBS_FACTORS = ["tdcc_big400_chg", "tdcc_big1000_chg", "tdcc_people_chg", "sbl_chg10"]
    ow = defaultdict(lambda: defaultdict(list))     # factor -> bucket -> [族群內 ic](日頻)
    ow_wk = defaultdict(lambda: defaultdict(list))  # 同上,只在 TDCC 快照生效日取樣(每週一點,獨立樣本)
    ocol_in, ocol_pool = defaultdict(list), defaultdict(list)  # 與 fpct_chg20 的橫斷面相關
    if obs is not None:
        prev_td, eff = {}, {}   # eff[d]=True ⇔ 當日任一檔的生效快照日前進(=新一週 TDCC 資料上線)
        for d in dates:
            cur = {s: obs[d][s]["tdcc_date"] for s in obs.get(d, {})}
            eff[d] = any(v and v != prev_td.get(s) for s, v in cur.items())
            prev_td.update({s: v for s, v in cur.items() if v})
        for d in dates:
            if d not in obs:
                continue
            bs = bucket(d)
            for el in OBS_FACTORS:
                for g in GRPS:
                    sids = [s for s in obs[d] if uni.get(s) == g and fwd(d, s) is not None]
                    ic = spearman([obs[d][s][el] for s in sids], [fwd(d, s) for s in sids])
                    if ic is None:
                        continue
                    for b in bs:
                        ow[el][b].append(ic)
                    if el.startswith("tdcc_") and eff.get(d):
                        for b in bs:
                            ow_wk[el][b].append(ic)
            for el in ("tdcc_big400_chg", "sbl_chg10"):   # 共線性:族群內為主、混池補充
                for g in GRPS:
                    sids = [s for s in obs[d] if uni.get(s) == g]
                    ic = spearman([obs[d][s][el] for s in sids],
                                  [obs[d][s]["fpct_chg20"] for s in sids])
                    if ic is not None:
                        ocol_in[el].append(ic)
                sids = list(obs[d])
                ic = spearman([obs[d][s][el] for s in sids],
                              [obs[d][s]["fpct_chg20"] for s in sids], minn=15)
                if ic is not None:
                    ocol_pool[el].append(ic)

    # ── 輸出 ──────────────────────────────────────────────────
    last = dates[-1]
    n_oos = sum(1 for d in dates if d > IS_CUTOFF)
    L = []
    w = L.append
    w(f"# 驗證報告 · 資料至 {last}(前瞻 {F} 日,還原價)")
    w("")
    w(f"- 覆蓋:{dates[0]} ~ {last},共 {len(dates)} 交易日;"
      f"修正 regime {sum(1 for v in regime.values() if v == 1)} 日、"
      f"多頭 {sum(1 for v in regime.values() if v == 0)} 日、冷啟動 {sum(1 for v in regime.values() if v is None)} 日")
    w(f"- **IS/OOS 分界 {IS_CUTOFF}**(v2.1 權重校準日);OOS 累積 {n_oos} 交易日"
      + ("——**尚不足以下結論,勿據此調旋鈕**" if n_oos < 10 else ""))
    w("")
    w("## ① 元素 rank-IC(族群內 = 汰弱留強的正確量尺)")
    w("")
    w("| 因子 | 族群內·全期 | 族群內·OOS | 族群內·修正 | 族群內·多頭 | 混池·全期 |")
    w("|---|---|---|---|---|---|")
    order = ["composite_s", "composite", "v1_composite", "s_price", "s_resil", "s_trust",
             "s_foreign", "s_dip", "s_vol", "s_margin"]
    for el in order:
        if el == "v1_composite" and not v1:
            continue
        cells = [fmt_ic(mean(wg[el].get(b)), len(wg[el].get(b, []))) for b in ("全期", "OOS", "修正", "多頭")]
        w(f"| {el} | " + " | ".join(cells) + f" | {fmt_ic(mean(pool[el].get('全期')))} |")
    w("")
    w("## ② tier 前瞻超額(vs 族群中位;確認後 tier)")
    w("")
    w("| tier | n·全期 | 超額·全期 | 勝率 | n·OOS | 超額·OOS |")
    w("|---|---|---|---|---|---|")
    def pctf(v):
        return f"{v*100:+.2f}%" if v is not None else "–"
    for t in sorted(tier_x, key=lambda t: -(mean(tier_x[t].get("全期")) or -9)):
        a = tier_x[t].get("全期", [])
        o = tier_x[t].get("OOS", [])
        hit = f"{100*sum(1 for x in a if x > 0)/len(a):.0f}%" if a else "–"
        w(f"| {t} | {len(a)} | {pctf(mean(a))} | {hit} | {len(o)} | {pctf(mean(o))} |")
    w("")
    w("### tier 轉移事件(轉移日起算的前瞻超額;n≥5 才列)")
    w("")
    w("| 轉移 | n | 平均超額 |")
    w("|---|---|---|")
    for (a, b), v in sorted(trans.items(), key=lambda kv: -mean(kv[1])):
        if len(v) >= 5:
            w(f"| {a} → {b} | {len(v)} | {mean(v)*100:+.2f}% |")
    w("")
    w("## ③ 蓄勢濾網 cohort(籌碼吃貨+價未動,按修正日抗跌分組)")
    w("")
    w("| 分組 | n·全期 | 超額·全期 | 勝率 | n·OOS | 超額·OOS |")
    w("|---|---|---|---|---|---|")
    for k in ("抗跌≥0(放行)", "領跌<0(擋下)", "抗跌缺值"):
        a, o = cohort[k].get("全期", []), cohort[k].get("OOS", [])
        if not a:
            continue
        hit = f"{100*sum(1 for x in a if x > 0)/len(a):.0f}%"
        w(f"| {k} | {len(a)} | {mean(a)*100:+.2f}% | {hit} | {len(o)} | "
          + (f"{mean(o)*100:+.2f}%" if o else "–") + " |")
    w("")
    w("> 放寬濾網的條件:OOS 累積 ≥15 筆且「領跌<0」組超額不再顯著落後「抗跌≥0」組。")
    w("")
    w("## ④ 族群層")
    w("")
    hit_all, hit_oos = dip_hit.get("全期", []), dip_hit.get("OOS", [])
    base = round(100 / len(GRPS)) if GRPS else 0
    w(f"- **med_dip 最高者領漲**命中率:全期 "
      + (f"{100*statistics.mean(hit_all):.0f}%(n={len(hit_all)},基準 {base}%)" if hit_all else "–")
      + ";OOS " + (f"{100*statistics.mean(hit_oos):.0f}%(n={len(hit_oos)})" if hit_oos else "–"))
    w("- 各 state 的族群前瞻超額(vs 全體中位):")
    w("")
    w("| state | n | 平均超額 |")
    w("|---|---|---|")
    for s, v in sorted(state_x.items(), key=lambda kv: -mean(kv[1])):
        w(f"| {s} | {len(v)} | {mean(v)*100:+.2f}% |")
    w("")
    w("## ⑤ 市值公平性監測(同尺檢核)")
    w("")
    w("### 影子因子:原始 rs20 vs 風險調整 rs20/σ20(族群內 IC)")
    w("")
    w("| 因子 | 全期 | OOS | 修正 |")
    w("|---|---|---|---|")
    for key in ("rs20(原始)", "rs20/σ20(風險調整)"):
        cells = [fmt_ic(mean(ic_sz[key].get(b)), len(ic_sz[key].get(b, [])))
                 for b in ("全期", "OOS", "修正")]
        w(f"| {key} | " + " | ".join(cells) + " |")
    w("")
    w("> 換尺條件:風險調整版在 OOS **持續**優於原始版(尤其小型股行情期)才改評分;現行不動。")
    w("")
    w("### tier 佔用率 by 族群內市值三分位")
    w("")
    w("| tier | 小·全期 | 中·全期 | 大·全期 | 小·OOS | 大·OOS |")
    w("|---|---|---|---|---|---|")
    def _occ(b, t_, tc):
        n = tszN[b].get(tc, 0)
        return f"{100*tsz[b][t_][tc]/n:.1f}%" if n else "–"
    for t_ in ("真強", "蓄勢·外資佈局", "真弱", "真弱·陷阱"):
        w(f"| {t_} | {_occ('全期', t_, '小')} | {_occ('全期', t_, '中')} | {_occ('全期', t_, '大')} | "
          f"{_occ('OOS', t_, '小')} | {_occ('OOS', t_, '大')} |")
    w("")
    w("> 真強的大/小佔用差若「持續」單邊擴大、且與當期領漲結構不符 → 檢查評分尺的市值傾斜。")
    w("")
    w("## ⑥ 觀察因子(Phase 4a:未計分,等 OOS 裁決歸宿)")
    w("")
    if obs is None or not any(ow[el] for el in OBS_FACTORS):
        w("- 尚無觀察因子資料(TDCC 需兩個週快照才有變化值;sbl 需先回補)。")
    else:
        w("來源:TDCC 股權分散(週頻,自 2026-07-03 起累積=天然全 OOS)、借券賣出餘額"
          "(日頻,有回補歷史——IS 段僅供參考)。預期方向:大戶 chg 為正、people_chg 與 "
          "sbl_chg 為負;歸宿裁決條件見 WEEKLY_REVIEW §4-8。")
        w("")
        w("| 因子 | 族群內·全期 | 族群內·OOS | 族群內·修正 | 族群內·多頭 |")
        w("|---|---|---|---|---|")
        for el in OBS_FACTORS:
            cells = [fmt_ic(mean(ow[el].get(b)), len(ow[el].get(b, []))) for b in ("全期", "OOS", "修正", "多頭")]
            w(f"| {el} | " + " | ".join(cells) + " |")
            if el.startswith("tdcc_"):
                cells = [fmt_ic(mean(ow_wk[el].get(b)), len(ow_wk[el].get(b, [])))
                         for b in ("全期", "OOS", "修正", "多頭")]
                w("| ↳ 快照取樣版(裁決用) | " + " | ".join(cells) + " |")
        w("")
        w("- 與 fpct_chg20 共線性(逐日橫斷面 spearman 取中位;|ρ|≥0.7 = 疑為 s_foreign 慢版):")
        for el in ("tdcc_big400_chg", "sbl_chg10"):
            mi = statistics.median(ocol_in[el]) if ocol_in[el] else None
            mp = statistics.median(ocol_pool[el]) if ocol_pool[el] else None
            w(f"  - {el}:族群內 {fmt_ic(mi, len(ocol_in[el]))};混池 {fmt_ic(mp, len(ocol_pool[el]))}")
        w("")
        w("> TDCC 週頻 forward-fill 使日頻 IC 的 n 虛胖約 5 倍(同一快照重複取樣)——8 週後的歸宿裁決以「快照取樣版」為準。")
    w("")
    w("## 判讀警語")
    w("")
    w(f"- {IS_CUTOFF} 前屬 in-sample(權重該窗校準,數字必然偏好看);評判看 OOS 欄。")
    w("- 前瞻視窗重疊 → 顯著性高估;每次檢視最多調 1~2 個旋鈕,調完記錄於 commit。")
    w("- 警告類 tier(強但過熱/陷阱)需經歷完整漲跌循環才可信(主升段樣本中曾為反指標)。")

    os.makedirs(REPORTS, exist_ok=True)
    path = os.path.join(REPORTS, f"validate_{last}.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")

    # console 摘要
    print(f"報告已寫入 {path}\n")
    print(f"覆蓋 {dates[0]}~{last}({len(dates)}日);OOS {n_oos} 日")
    print(f"composite_s 族群內 IC:全期 {fmt_ic(mean(wg['composite_s'].get('全期')))}"
          f",OOS {fmt_ic(mean(wg['composite_s'].get('OOS')))}")
    if v1:
        print(f"v1 composite 族群內 IC:全期 {fmt_ic(mean(wg['v1_composite'].get('全期')))}")
    if hit_all:
        print(f"med_dip 領漲命中:全期 {100*statistics.mean(hit_all):.0f}%(基準{base}%)")
    ca, cb = cohort["抗跌≥0(放行)"].get("全期", []), cohort["領跌<0(擋下)"].get("全期", [])
    if ca and cb:
        print(f"蓄勢濾網 cohort:放行 {mean(ca)*100:+.2f}%(n={len(ca)}) vs 擋下 {mean(cb)*100:+.2f}%(n={len(cb)})")
    print(f"影子因子:rs20 {fmt_ic(mean(ic_sz['rs20(原始)'].get('全期')))} vs "
          f"rs20/σ20 {fmt_ic(mean(ic_sz['rs20/σ20(風險調整)'].get('全期')))}")
    n_all = tszN["全期"]
    if n_all.get("小") and n_all.get("大"):
        print(f"真強佔用(小/大):{100*tsz['全期']['真強']['小']/n_all['小']:.1f}% / "
              f"{100*tsz['全期']['真強']['大']/n_all['大']:.1f}%")
    if obs is not None and any(ow[el] for el in OBS_FACTORS):
        print(f"觀察因子(§⑥):sbl_chg10 族群內全期 {fmt_ic(mean(ow['sbl_chg10'].get('全期')))};"
              f"tdcc_big400_chg 取樣版 OOS {fmt_ic(mean(ow_wk['tdcc_big400_chg'].get('OOS')))}")
    con.close()


if __name__ == "__main__":
    main()
