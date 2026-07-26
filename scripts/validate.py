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
  * IS_CUTOFF(2026-07-05)前屬 in-sample —— v2.1 權重在該窗校準,數字必然好看。
  * OOS 只認 `oos_*_snapshots` 的 as-seen 首次正式發布快照；cutoff 後但沒有快照的
    restated history 不得進 OOS。前瞻成熟仍需 2~4 週累積。
  * 前瞻視窗重疊 → 顯著性高估;30 檔小樣本 → 每次檢視最多調 1~2 個旋鈕。

用法:
  python scripts/validate.py           # 預設 10 日前瞻
  python scripts/validate.py --fwd 5
"""
import argparse, json, os, sqlite3, statistics, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import signal_structure as sig   # §⑦:元素邊際貢獻與結構指標(共用 score.WEIGHTS)
import stats_ci as sci           # §⑨:NW 標準誤 / 有效獨立觀測 / episode 計數

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
REPORTS = os.path.join(ROOT, "reports")
IS_CUTOFF = "2026-07-05"      # v2.1 權重校準日:此日(含)之前 = in-sample

# ── §⑩ 淨成本下限的市場參數(不是策略旋鈕,是台股交易事實)────────────────
# 訊號在台北 18:07 之後才算出來 → close(d) 買不到。可成交的最早進場是隔日開盤。
COST_ROUND_TRIP = 0.1425 * 2 + 0.3    # 手續費 0.1425%×2 + 證交稅 0.3%(賣出)= 0.585%
COST_DISCOUNTED = 0.1425 * 0.6 * 2 + 0.3   # 手續費 6 折 = 0.471%
NET_HOLD_DAYS = (3, 5, 10, 20)        # 固定持有期對照(3 日 ≈ 照 tier 進出的實際持有)
NET_TIERS = ("真強", "蓄勢·外資佈局")   # 只算「可能被當進場訊號」的層
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
    ap.add_argument("--db", default=DB, help="SQLite 路徑(測試/診斷用;預設 production db)")
    ap.add_argument("--reports", default=REPORTS, help="報告輸出目錄")
    args = ap.parse_args()
    F = args.fwd

    con = sqlite3.connect(args.db)
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

    # ── OOS as-seen 快照 ──────────────────────────────────────
    # daily_scores / daily_metrics 仍保留「最新規則重算歷史」供 IS 研究；只有每日正式管線
    # append-only 留下的最早正式快照才可覆蓋進 OOS。觸發來源可為 GitHub Actions 或本地；
    # 後續同日修正版保留稽核，
    # 但不會改寫當天第一次實際發布、使用者可能已據以決策的訊號。
    snap_runs, snap_grp, snap_grps, snap_quality = {}, defaultdict(dict), {}, {}
    loaded_snap_dates = set()
    try:
        for r in con.execute("""SELECT * FROM oos_snapshot_runs
                                WHERE is_official=1
                                ORDER BY data_date, captured_at, snapshot_id"""):
            if r["data_date"] not in snap_runs:
                snap_runs[r["data_date"]] = r["snapshot_id"]
                snap_quality[r["data_date"]] = r["quality_json"]
        for d, run_id in snap_runs.items():
            sr = list(con.execute("SELECT * FROM oos_signal_snapshots WHERE snapshot_id=?", (run_id,)))
            if not sr:
                continue
            loaded_snap_dates.add(d)
            v2[d] = {r["stock_id"]: r for r in sr}
            met[d] = {r["stock_id"]: r for r in sr}
            if obs is not None:
                obs[d] = {r["stock_id"]: r for r in sr}
            snap_grp[d] = {r["stock_id"]: r["grp"] for r in sr}
            gs = list(con.execute("""SELECT * FROM oos_group_snapshots WHERE snapshot_id=?
                                     ORDER BY COALESCE(ord, 999), grp""", (run_id,)))
            if gs:
                gm[d] = {r["grp"]: r for r in gs}
                snap_grps[d] = tuple(r["grp"] for r in gs)
            mr = con.execute("SELECT * FROM oos_market_snapshots WHERE snapshot_id=?", (run_id,)).fetchone()
            if mr:
                regime[d] = mr["regime"]
    except sqlite3.OperationalError:
        snap_runs = {}
    snap_dates = loaded_snap_dates

    def grp_of(d, sid):
        return snap_grp.get(d, {}).get(sid, uni.get(sid))

    def grps_on(d):
        return snap_grps.get(d, GRPS)

    all_sids = sorted(set(uni) | {s for bys in v2.values() for s in bys})
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
        bs = ["全期"]
        if d <= IS_CUTOFF:
            bs.append("IS")
        elif d in snap_dates:
            bs.append("OOS")
        else:
            bs.append("重算")   # cutoff 後但非 as-seen；只供背景，絕不可冒充 OOS
        r = regime.get(d)
        if r == 1:
            bs.append("修正")
        elif r == 0:
            bs.append("多頭")
        return bs

    # ── ① 元素 IC ──────────────────────────────────────────────
    wg = defaultdict(lambda: defaultdict(list))    # factor -> bucket -> [ic per date×group]
    pool = defaultdict(lambda: defaultdict(list))  # factor -> bucket -> [ic per date]
    # §⑨ 判讀強度用:同一份 IC 但**保留日期**。格數(date×group)不是獨立樣本——
    # 前瞻窗重疊使日 IC 自相關(實測 lag-1 ≈ +0.7),必須先收斂成「每日一個數」
    # 才能算 Newey-West 標準誤。
    wg_by_date = defaultdict(lambda: defaultdict(dict))   # factor -> bucket -> {date: [ic]}
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
        for g in grps_on(d):
            sids = [s for s in v2[d] if grp_of(d, s) == g and fwd(d, s) is not None]
            f = [fwd(d, s) for s in sids]
            for el in cols:
                ic = spearman([v2[d][s][el] for s in sids], f)
                if ic is not None:
                    for b in bs:
                        wg[el][b].append(ic)
                        wg_by_date[el][b].setdefault(d, []).append(ic)
            if d in v1:
                ic = spearman([v1[d][s]["composite"] for s in sids if s in v1[d]],
                              [fwd(d, s) for s in sids if s in v1[d]])
                if ic is not None:
                    for b in bs:
                        wg["v1_composite"][b].append(ic)

    # ── ② tier 前瞻超額 + 轉移事件 ─────────────────────────────
    def grp_med_fwd(d, g):
        v = [fwd(d, s) for s in v2.get(d, {}) if grp_of(d, s) == g]
        v = [x for x in v if x is not None]
        return statistics.median(v) if v else None

    tier_x = defaultdict(lambda: defaultdict(list))   # tier -> bucket -> [excess]
    for d in dates:
        if d not in v2:
            continue
        bs = bucket(d)
        gmed = {g: grp_med_fwd(d, g) for g in grps_on(d)}
        for sid, r in v2[d].items():
            f, gv = fwd(d, sid), gmed.get(grp_of(d, sid))
            if f is None or gv is None:
                continue
            for b in bs:
                tier_x[r["tier"]][b].append(f - gv)

    trans = defaultdict(lambda: defaultdict(list))   # (from,to) -> bucket -> [excess]
    for sid in all_sids:
        prev, prev_date = None, None
        for d in dates:
            r = v2[d].get(sid)
            if r is None:
                continue
            if prev is not None and r["tier"] != prev:
                f, gv = fwd(d, sid), grp_med_fwd(d, grp_of(d, sid))
                if f is not None and gv is not None:
                    for b in bucket(d):
                        # 轉移需要前後兩天的「實際發布」tier；第一份快照不能拿前一日
                        # restated tier 冒充 OOS 起點,快照中斷時也同理。
                        if b == "OOS" and (prev_date not in snap_dates or didx.get(prev_date, -2) + 1 != didx[d]):
                            continue
                        trans[(prev, r["tier"])][b].append(f - gv)
            prev, prev_date = r["tier"], d

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
            f, gv = fwd(d, sid), grp_med_fwd(d, grp_of(d, sid))
            if f is None or gv is None:
                continue
            key = ("抗跌≥0(放行)" if m["down_rs20"] >= 0 else "領跌<0(擋下)") \
                if m["down_rs20"] is not None else "抗跌缺值"
            for b in bs:
                cohort[key][b].append(f - gv)

    # ── ④ 族群層 ──────────────────────────────────────────────
    dip_hit = defaultdict(list)   # bucket -> [1/0]
    dip_base = defaultdict(list)  # bucket -> [隨當日族群數變動的隨機基準]
    state_x = defaultdict(lambda: defaultdict(list))  # state -> bucket -> [group excess]
    for d in dates:
        if d not in gm:
            continue
        bs = bucket(d)
        gf = {}
        day_grps = grps_on(d)
        for g in day_grps:
            v = grp_med_fwd(d, g)
            if v is not None:
                gf[g] = v
        if day_grps and len(gf) == len(day_grps):
            uv = statistics.median(gf.values())
            dips = {g: gm[d][g]["med_dip"] for g in day_grps
                    if g in gm[d] and gm[d][g]["med_dip"] is not None}
            if len(dips) == len(day_grps):
                leader = max(dips, key=dips.get)
                hit = 1 if gf[leader] == max(gf.values()) else 0
                for b in bs:
                    dip_hit[b].append(hit)
                    dip_base[b].append(1 / len(day_grps))
            for g in day_grps:
                if g in gm[d]:
                    for b in bs:
                        state_x[gm[d][g]["state"]][b].append(gf[g] - uv)

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
        for g in grps_on(d):
            sids = [s for s in met[d] if grp_of(d, s) == g]
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
                for g in grps_on(d):
                    sids = [s for s in obs[d] if grp_of(d, s) == g and fwd(d, s) is not None]
                    ic = spearman([obs[d][s][el] for s in sids], [fwd(d, s) for s in sids])
                    if ic is None:
                        continue
                    for b in bs:
                        ow[el][b].append(ic)
                    if el.startswith("tdcc_") and eff.get(d):
                        for b in bs:
                            ow_wk[el][b].append(ic)
            for el in ("tdcc_big400_chg", "sbl_chg10"):   # 共線性:族群內為主、混池補充
                for g in grps_on(d):
                    sids = [s for s in obs[d] if grp_of(d, s) == g]
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
    oos_dates = sorted(d for d in snap_dates if d > IS_CUTOFF and d in didx)
    mature_oos_dates = [d for d in oos_dates if didx[d] + F < len(dates)]
    restated_post_dates = [d for d in dates if d > IS_CUTOFF and d not in snap_dates]
    n_oos, n_oos_mature = len(oos_dates), len(mature_oos_dates)
    snapshot_quality_issues = []
    for d in oos_dates:
        try:
            q = json.loads(snap_quality[d])
            for table in ("price", "inst", "margin", "holding", "sbl"):
                if q.get(table, 0) < q.get("universe", 0):
                    snapshot_quality_issues.append(
                        f"{d} {table}={q.get(table, 0)}/{q.get('universe', 0)}")
            if q.get("market_date") != d:
                snapshot_quality_issues.append(f"{d} market 僅至 {q.get('market_date')}")
        except (KeyError, TypeError, ValueError):
            snapshot_quality_issues.append(f"{d} quality_json 無法解析")
    L = []
    w = L.append
    w(f"# 驗證報告 · 資料至 {last}(前瞻 {F} 日,還原價)")
    w("")
    w(f"- 覆蓋:{dates[0]} ~ {last},共 {len(dates)} 交易日;"
      f"修正 regime {sum(1 for v in regime.values() if v == 1)} 日、"
      f"多頭 {sum(1 for v in regime.values() if v == 0)} 日、冷啟動 {sum(1 for v in regime.values() if v is None)} 日")
    w(f"- **IS/OOS 分界 {IS_CUTOFF}**(v2.1 權重校準日);正式 as-seen OOS 快照 "
      f"{n_oos} 日、其中前瞻 {F} 日已成熟 {n_oos_mature} 日"
      + ("——**尚不足以下結論,勿據此調旋鈕**" if n_oos_mature < 10 else ""))
    if restated_post_dates:
        w(f"- cutoff 後另有 {len(restated_post_dates)} 日僅存最新規則重算歷史"
          f"({restated_post_dates[0]}~{restated_post_dates[-1]}),**不計入 OOS**。")
    w("- 同資料日若有多次正式發布,驗證固定採最早正式快照(不分 Actions/local);後續修正版只供稽核。")
    if snapshot_quality_issues:
        w("- ⚠ OOS 快照資料品質:" + ";".join(snapshot_quality_issues))
    w("")
    w("## ① 元素 rank-IC(族群內 = 汰弱留強的正確量尺)")
    w("")
    w("> 下表只有點估計與格數。**格數不是獨立樣本**——證據強度(標準誤、有效獨立觀測、連續區段)見 §⑨,t<2 時大小順序沒有意義。")
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
    w("### tier 轉移事件(轉移日起算的前瞻超額;全期 n≥5 才列)")
    w("")
    w("| 轉移 | n·全期 | 超額·全期 | n·OOS | 超額·OOS |")
    w("|---|---|---|---|---|")
    for (a, b), buckets in sorted(
            trans.items(), key=lambda kv: -(mean(kv[1].get("全期")) or -9)):
        av, ov = buckets.get("全期", []), buckets.get("OOS", [])
        if len(av) >= 5:
            w(f"| {a} → {b} | {len(av)} | {pctf(mean(av))} | {len(ov)} | {pctf(mean(ov))} |")
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
    base = round(100 * mean(dip_base.get("全期", []))) if dip_base.get("全期") else 0
    w(f"- **med_dip 最高者領漲**命中率:全期 "
      + (f"{100*statistics.mean(hit_all):.0f}%(n={len(hit_all)},基準 {base}%)" if hit_all else "–")
      + ";OOS " + (f"{100*statistics.mean(hit_oos):.0f}%(n={len(hit_oos)})" if hit_oos else "–"))
    w("- 各 state 的族群前瞻超額(vs 全體中位):")
    w("")
    w("| state | n·全期 | 超額·全期 | n·OOS | 超額·OOS |")
    w("|---|---|---|---|---|")
    for s, buckets in sorted(
            state_x.items(), key=lambda kv: -(mean(kv[1].get("全期")) or -9)):
        av, ov = buckets.get("全期", []), buckets.get("OOS", [])
        w(f"| {s} | {len(av)} | {pctf(mean(av))} | {len(ov)} | {pctf(mean(ov))} |")
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
        w("來源:TDCC 股權分散(週頻,自 2026-07-03 起累積)、借券賣出餘額"
          "(日頻,有回補歷史)。兩者只有落在正式 as-seen 訊號快照的日期才計入 OOS。"
          "預期方向:大戶 chg 為正、people_chg 與 "
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
    # ── ⑦ 元素邊際貢獻與訊號集中度(WEEKLY_REVIEW §4-7 單柱風險)────────
    # §① 給的是「每個元素單獨有多準」,回答不了「它在 composite 裡有沒有加值」。
    # 一個元素可以單獨 IC 為正,卻因為與其他元素近乎獨立又無訊號,在加權和裡稀釋掉
    # 唯一的訊號。這節用「移除後重算」量測邊際貢獻,並附不需前瞻報酬的結構指標。
    w("## ⑦ 元素邊際貢獻與訊號集中度(§4-7 單柱風險)")
    w("")
    w("移除某元素後重算 composite 的 IC —— 「該元素在加權和裡有沒有加值」,"
      "與 §① 的「單獨有多準」是不同問題。同一組格對照,故可直接相減。")
    w("")
    lo_shares = sig.variance_shares([[v2[d][s] for s in v2[d] if grp_of(d, s) == g]
                                     for d in dates if d in v2 for g in grps_on(d)]) or {}

    def comp_ic(weights, bucket_name):
        acc = []
        for d in dates:
            if d not in v2 or bucket_name not in bucket(d):
                continue
            for g in grps_on(d):
                sids = [s for s in v2[d] if grp_of(d, s) == g and fwd(d, s) is not None]
                ic = spearman([sig.composite_of(v2[d][s], weights) for s in sids],
                              [fwd(d, s) for s in sids])
                if ic is not None:
                    acc.append(ic)
        return (mean(acc), len(acc))

    base = {b: comp_ic(sig.WEIGHTS, b) for b in ("全期", "OOS")}
    w("| 移除的元素 | 權重 | 變異貢獻·全期 | IC·全期 | Δ | IC·OOS | Δ |")
    w("|---|---|---|---|---|---|---|")
    w(f"| (現行 {len([k for k, v in sig.WEIGHTS.items() if v])} 個計分元素) | – | – | "
      f"{fmt_ic(base['全期'][0], base['全期'][1])} | — | "
      f"{fmt_ic(base['OOS'][0], base['OOS'][1])} | — |")
    for el, wt in sorted(sig.WEIGHTS.items(), key=lambda kv: -kv[1]):
        if not wt:
            continue
        dropped = {k: (0.0 if k == el else v) for k, v in sig.WEIGHTS.items()}
        cells = []
        for b in ("全期", "OOS"):
            v, n = comp_ic(dropped, b)
            cells.append(fmt_ic(v, n))
            cells.append(f"{v - base[b][0]:+.3f}" if (v is not None and base[b][0] is not None) else "–")
        share = lo_shares.get(el)
        w(f"| s_{el} | {wt:.1f} | " + (f"{share:.0%}" if share is not None else "–")
          + " | " + " | ".join(cells) + " |")
    w("")
    w("> Δ 為正 = 移除該元素後 composite 變準,即它在加權和裡是淨負貢獻。"
      "全期欄大部分落在 IS 窗,只能當假說;動權重一律等 OOS 欄達 §① 的連 N 週門檻。")
    w("")
    lead = max(lo_shares, key=lambda k: lo_shares[k]) if lo_shares else None
    if lead:
        w(f"### 結構指標(不需前瞻報酬 → 每日可由 `daily_brief.py` 監控)")
        w("")
        eff = sig.effective_factors(lo_shares)
        for label, only_snap in (("全期", False), ("OOS(as-seen 快照日)", True)):
            gs = [[v2[d][s] for s in v2[d] if grp_of(d, s) == g]
                  for d in dates if d in v2 and (not only_snap or d in snap_dates)
                  for g in grps_on(d)]
            r = sig.rank_rho(gs, lead)
            sh = sig.variance_shares(gs)
            e = sig.effective_factors(sh) if sh else None
            n_scored = len([k for k, v in sig.WEIGHTS.items() if v])
            w(f"- {label}:composite 排名 vs s_{lead} 排名 ρ 中位 "
              + (f"**{r:+.3f}**" if r is not None else "–")
              + ";有效因子數 " + (f"**{e:.2f}** / {n_scored}" if e is not None else "–"))
        w("")
        w(f"> 有效因子數 = 變異貢獻的倒 Herfindahl(1 = 完全單柱)。"
          f"警戒線 ρ>{sig.RHO_ALERT}、有效因子數<{sig.EFF_ALERT};"
          "越線只代表脆弱,不構成調旋鈕的理由。")
    w("")
    # ── ⑧ tier 持續性(結構指標第二組)────────────────────────────
    # §② 量的是「tier 對不對」,量不到「tier 撐多久」。若可交易 tier 的中位停留短於
    # 前瞻窗,照訊號進出就抓不到 §② 那個超額——量測窗與可用訊號長度不一致。
    w("## ⑧ tier 持續性與名單換手(結構指標,不需前瞻報酬)")
    w("")
    w("「每日幾檔變層」分不出震盪與單向遷移,故量停留天數、震盪率、名單換手。"
      f"基礎為 daily_scores(最新規則重算歷史)——as-seen 快照目前僅 {n_oos} 日,"
      "不足以測停留;累積足夠後應改以 as-seen 為準。")
    w("")
    ch = sig.churn_summary(sig.tier_sequences(con), dates, horizon=F)
    if not ch:
        w("- 資料不足。")
    else:
        w("| tier | 完整區段數 | 中位停留 | 名單平均檔數 | 全量換手需時 | 年化換手 |")
        w("|---|---|---|---|---|---|")
        for t in sorted(ch["dwell"], key=lambda k: -ch["dwell_n"].get(k, 0)):
            tv = ch["turnover"].get(t)
            cells = (f"{tv['avg_n']:.1f} | {tv['full_turn_days']:.1f} 交易日 | "
                     f"{tv['turns_per_year']:.0f} 次/年"
                     if tv and tv["full_turn_days"] else "– | – | –")
            w(f"| {t} | {ch['dwell_n'][t]} | {ch['dwell'][t]:.0f} 日 | {cells} |")
        w("")
        back, total, rate = ch["round_trip"]
        w(f"- **震盪率**:{total} 次變動中,{sig.ROUND_TRIP_WINDOW} 個交易日內又變回原 tier 的有 "
          + (f"**{back} 次({rate:.0%})**" if rate is not None else "–")
          + ";其餘為單向遷移。")
        if ch["short_vs_horizon"]:
            names = "、".join(f"{t} {m:.0f} 日" for t, m in ch["short_vs_horizon"])
            w(f"- ⚠ **停留短於量測窗**:{names},皆 < 前瞻 {F} 日。"
              "照 tier 進出的實際持有期比 §② 的量測視窗短,兩者不是同一件事"
              "(見 WEEKLY_REVIEW §4-10)。")
        w("")
        w("> 中位停留排除右截尾的尾段(只看到一半的區段當成完整會低估);"
          "排除本身也略偏短,兩種偏誤同向,故此值宜視為停留天數的下限。")
    w("")
    # ── ⑨ 判讀強度 ────────────────────────────────────────────────
    # 2026-07-26 對抗性審查的結論:在此之前報告只有點估計與 n=格數,沒有任何誤差量。
    # 補算後三個候選策略的全期 IC(+0.021/+0.034/+0.040)t 值全部 <2——先前那些
    # 「哪個比較好」的比較,比的是三個統計上等於零的數字。
    w("## ⑨ 判讀強度(標準誤 / 獨立觀測 / episode)")
    w("")
    w(f"格數(date×group)**不是**獨立樣本:前瞻 {F} 日的窗互相重疊,日 IC 高度自相關。"
      f"下表先把同一天各族群的 IC 收斂成「每日一個數」,再用 Newey-West"
      f"(lag={sci.overlap_lag(F)})估標準誤。")
    w("")
    w("| 因子 | 桶 | 日均 IC ±NW SE (t) | 交易日 | 有效獨立觀測 | 連續區段 | 判讀 |")
    w("|---|---|---|---|---|---|---|")
    for el in ("composite_s", "s_price", "s_resil", "s_foreign", "s_dip", "s_trust", "s_margin"):
        for b in ("全期", "OOS", "修正", "多頭"):
            by_d = wg_by_date[el].get(b) or {}
            if not by_d:
                continue
            ds = sorted(by_d)
            s = sci.summarize([mean(by_d[d]) for d in ds], F, ds, dates)
            if not s:
                continue
            w(f"| {el} | {b} | {sci.fmt(s)} | {s['n_days']} | **{s['eff_obs']:.1f}** | "
              f"{s['episodes']} | {sci.verdict(s)} |")
    ac = sci.autocorr1([mean(v) for _, v in sorted((wg_by_date['composite_s'].get('全期') or {}).items())])
    if ac is not None:
        w("")
        w(f"- 日 IC 序列 lag-1 自相關 = **{ac:+.2f}**——這就是不能用一般標準誤的原因。")
    w(f"- 有效獨立觀測 = 交易日數 ÷ {F}。{n_oos_mature} 個成熟 OOS 日 ≈ "
      f"**{sci.effective_obs(n_oos_mature, F):.1f} 個獨立觀測**。")
    w("- 連續區段 = 該桶的交易日切成幾段連續期間。修正桶若只來自少數幾段大跌,"
      "「修正期有效」講的是那幾個事件,不是規律。")
    w("")
    w("> **規矩**:沒有標準誤與區段數的數字,不得作為調旋鈕的依據——"
      "點估計的大小順序在 t<2 時沒有意義。§①②③ 的點估計請一律回到本節查證據強度。")
    w("")
    # ── ⑩ 淨成本下限 ──────────────────────────────────────────────
    # §①~⑨ 量的全是「毛」訊號品質,且用 close(d) → close(d+F)。但訊號在台北 18:07
    # 之後才算出來,**close(d) 買不到**;而 §⑧ 顯示真強中位停留只有 4~5 日,
    # 照 tier 進出的年化換手上百次。這節把兩件事都算進去:進出各延一天到隔日開盤,
    # 再扣來回成本,看還剩什麼。
    w("## ⑩ 淨成本下限(可成交價 + 交易成本)")
    w("")
    w(f"訊號 18:07 後才產出 → **close(d) 買不到**,以下一律用**隔日開盤**進出"
      f"(還原開盤 = 原始開盤 × 還原收盤/原始收盤)。"
      f"來回成本 **{COST_ROUND_TRIP:.3f}%**(手續費 0.1425%×2 + 證交稅 0.3%);"
      f"6 折手續費為 {COST_DISCOUNTED:.3f}%。")
    w("")
    # 還原開盤(price_adj 只存 close,係數逐日逐股相同)
    adj_o = {}
    for r in con.execute("""SELECT p.date, p.stock_id, p.open, p.close, a.close AS ac
                            FROM price p JOIN price_adj a
                              ON a.date=p.date AND a.stock_id=p.stock_id"""):
        if r["open"] and r["close"] and r["ac"]:
            adj_o[(r["date"], r["stock_id"])] = r["open"] * (r["ac"] / r["close"])

    def shift(d, n):
        i = didx.get(d)
        return dates[i + n] if (i is not None and 0 <= i + n < len(dates)) else None

    def oret(s, d0, d1):
        a, b = adj_o.get((d0, s)), adj_o.get((d1, s))
        return (b / a - 1) if (a and b) else None

    # (A) 執行時差:同一個 composite_s,只換報酬定義
    w("### A 執行時差:換成可成交的報酬定義後,毛 IC 變多少")
    w("")
    w("| 報酬定義 | 日均 IC ±NW SE (t) | 交易日 | 有效獨立觀測 |")
    w("|---|---|---|---|")
    for label, n0, n1, use_open in (
            (f"close(d) → close(d+{F})  §① 現行定義(**買不到**)", 0, F, False),
            (f"open(d+1) → open(d+1+{F})  隔日開盤進出(可成交)", 1, 1 + F, True)):
        by_d = {}
        for d in dates:
            if d not in v2:
                continue
            d0, d1 = shift(d, n0), shift(d, n1)
            if not d0 or not d1:
                continue
            v = []
            for g in grps_on(d):
                sids = [s for s in v2[d] if grp_of(d, s) == g]
                rr = {s: (oret(s, d0, d1) if use_open
                          else ((cadj.get((d1, s)) / cadj[(d0, s)] - 1)
                                if cadj.get((d1, s)) and cadj.get((d0, s)) else None))
                      for s in sids}
                ok = [s for s in sids if rr[s] is not None]
                if len(ok) < 6:
                    continue
                ic = spearman([v2[d][s]["composite_s"] for s in ok], [rr[s] for s in ok])
                if ic is not None:
                    v.append(ic)
            if v:
                by_d[d] = mean(v)
        ds = sorted(by_d)
        s = sci.summarize([by_d[d] for d in ds], F, ds, dates)
        if s:
            w(f"| {label} | {sci.fmt(s)} | {s['n_days']} | {s['eff_obs']:.1f} |")
    w("")

    # (B) 優勢是否藏在買不到的隔夜跳空
    gp = {}
    for d in dates:
        if d not in v2:
            continue
        d1 = shift(d, 1)
        if not d1:
            continue
        v = []
        for g in grps_on(d):
            sids = [s for s in v2[d] if grp_of(d, s) == g
                    and cadj.get((d, s)) and adj_o.get((d1, s))]
            if len(sids) < 6:
                continue
            ic = spearman([v2[d][s]["composite_s"] for s in sids],
                          [adj_o[(d1, s)] / cadj[(d, s)] - 1 for s in sids])
            if ic is not None:
                v.append(ic)
        if v:
            gp[d] = mean(v)
    ds = sorted(gp)
    sg = sci.summarize([gp[d] for d in ds], 1, ds, dates)   # 跳空不重疊 → lag 0
    if sg:
        w(f"- **B 隔夜跳空**:composite_s 對「當日收盤 → 隔日開盤」的族群內 IC "
          f"**{sci.fmt(sg)}**——若接近 0,代表優勢不是集中在買不到的那一刻。")
        w("")

    # (C) 固定持有期的淨超額(先按日聚合再 NW,避免同股連續日重複計入)
    w(f"### C 固定持有期的淨超額(vs 族群中位,已扣 {COST_ROUND_TRIP:.3f}%)")
    w("")
    w("| 進場層 | 固定持有 | 交易日 | 有效獨立觀測 | 淨超額 ±NW SE (t) | 判讀 |")
    w("|---|---|---|---|---|---|")
    for tier_name in NET_TIERS:
        for H in NET_HOLD_DAYS:
            daily = {}
            for d in dates:
                if d not in v2:
                    continue
                d0, d1 = shift(d, 1), shift(d, 1 + H)
                if not d0 or not d1:
                    continue
                # 每個族群的報酬只算一次
                gret = {}
                for g in grps_on(d):
                    gr = {s: oret(s, d0, d1) for s in v2[d] if grp_of(d, s) == g}
                    gr = {k: x for k, x in gr.items() if x is not None}
                    if len(gr) >= 6:
                        gret[g] = gr
                vals = []
                for s, row in v2[d].items():
                    if row["tier"] != tier_name:
                        continue
                    g = grp_of(d, s)
                    gr = gret.get(g)
                    if not gr or s not in gr:
                        continue
                    peers = [x for k, x in gr.items() if k != s]
                    if len(peers) < 5:
                        continue
                    vals.append((gr[s] - statistics.median(peers)) * 100 - COST_ROUND_TRIP)
                if vals:
                    daily[d] = mean(vals)
            ds = sorted(daily)
            s = sci.summarize([daily[d] for d in ds], H, ds, dates)
            if s:
                w(f"| {tier_name} | {H} 日 | {s['n_days']} | **{s['eff_obs']:.1f}** | "
                  f"{sci.fmt(s)} | {sci.verdict(s)} |")
    w("")
    w(f"> **怎麼讀**:`{NET_HOLD_DAYS[0]} 日`約等於「照 tier 進出」的實際持有"
      f"(§⑧ 顯示真強中位停留 4~5 日,進出各延一天後約 3 日)。持有期越長,"
      f"固定成本被攤薄、點估計越好——但有效獨立觀測同時變少,長持有反而更難判讀。"
      f"**沒有一格達到 |t|>2 之前,不可宣稱這套訊號在扣成本後仍有效。**")
    w("")
    w("## 判讀警語")
    w("")
    w(f"- {IS_CUTOFF} 前屬 in-sample;cutoff 後若沒有正式快照也只是 restated history。"
      "評判只看 as-seen OOS 欄。")
    w("- 前瞻視窗重疊 → 顯著性高估;每次檢視最多調 1~2 個旋鈕,調完記錄於 commit。")
    w("- 警告類 tier(強但過熱/陷阱)需經歷完整漲跌循環才可信(主升段樣本中曾為反指標)。")

    os.makedirs(args.reports, exist_ok=True)
    path = os.path.join(args.reports, f"validate_{last}.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")

    # console 摘要
    print(f"報告已寫入 {path}\n")
    print(f"覆蓋 {dates[0]}~{last}({len(dates)}日);as-seen OOS {n_oos} 日,成熟 {n_oos_mature} 日")
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
