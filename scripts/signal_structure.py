#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""signal_structure.py — 訊號結構診斷(唯讀、純計算,零第三方依賴)。

**為什麼要獨立成一個模組**:WEEKLY_REVIEW §4-7 的「rs20 單因子濃度風險」原本只是文字
備忘。它問的是「訊號有多集中」,而那是**當日橫斷面的確定性事實**——不需要前瞻報酬、
沒有取樣誤差、沒有 look-ahead。因此它可以每日監控,和 §①②(需要成熟前瞻報酬、單日讀數
是純雜訊、必須走連 N 週規則)在方法學上完全不同類。

  結構指標(本模組)→ 每日可讀,`daily_brief.py`
  績效指標(IC/超額)→ 只能週度,`validate.py` §①~⑥

權重一律由 `score.WEIGHTS` 取得,不在此處寫死——否則調了旋鈕而監控沒跟上,會量錯對象。
"""
import statistics

from score import WEIGHTS   # 單一真相來源:個股層權重旋鈕

# score.WEIGHTS 的鍵是 price/resil/...;db 欄位是 s_price/s_resil/...
ELEMENT_COLS = {k: f"s_{k}" for k in WEIGHTS}
STRONG_TOP_N = 2      # 真強閘門:族群內 comp_s 前 2 名(score.py tier 條件)

# 單柱警戒線(僅為監看提示,不是行動門檻——行動一律走 WEEKLY_REVIEW 的 OOS 規則)
RHO_ALERT = 0.80      # composite 與最大貢獻元素的排名相關
EFF_ALERT = 2.5       # 有效因子數


def rankdata(x):
    """平均秩(與 validate.py 同定義,tie 取中點)。"""
    idx = sorted(range(len(x)), key=lambda i: x[i])
    rk, i = [0.0] * len(x), 0
    while i < len(idx):
        j = i
        while j + 1 < len(idx) and x[idx[j + 1]] == x[idx[i]]:
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


def _get(row, col):
    """同時支援 dict 與 sqlite3.Row —— 後者沒有 .get(),且缺欄拋 IndexError。

    daily_brief 走 dict(r),validate 直接存 sqlite3.Row;兩邊都要能餵進來。
    """
    try:
        v = row[col]
    except (KeyError, IndexError):
        return 0
    return 0 if v is None else v


def composite_of(row, weights=None):
    """由元素重算 composite;缺值以 0 計(同 score.py 對無訊號元素的處理)。"""
    weights = WEIGHTS if weights is None else weights
    return sum(w * _get(row, ELEMENT_COLS[k]) for k, w in weights.items())


def variance_shares(groups, weights=None):
    """各元素對 composite 橫斷面變異的貢獻份額,逐族群計算後取平均(合計 = 1)。

    分解式:Var(comp) = Σᵢ wᵢ·Cov(sᵢ, comp) → shareᵢ = wᵢ·Cov(sᵢ, comp) / Var(comp)。
    份額可為負(該元素與 composite 反向),故不做非負假設。
    """
    weights = WEIGHTS if weights is None else weights
    acc = {k: [] for k in weights}
    for rows in groups:
        if len(rows) < 3:
            continue
        comp = [composite_of(r, weights) for r in rows]
        var = statistics.pvariance(comp)
        if not var:
            continue
        mc = statistics.mean(comp)
        for k in weights:
            v = [_get(r, ELEMENT_COLS[k]) for r in rows]
            mv = statistics.mean(v)
            cov = sum((a - mv) * (b - mc) for a, b in zip(v, comp)) / len(v)
            acc[k].append(weights[k] * cov / var)
    return {k: statistics.mean(v) for k, v in acc.items() if v}


def effective_factors(shares):
    """有效因子數(變異貢獻的倒 Herfindahl)。1 = 完全單柱,n = n 個等貢獻因子。"""
    s2 = sum(v * v for v in shares.values())
    return (1.0 / s2) if s2 else None


def rank_rho(groups, element, weights=None):
    """composite 排名 vs 單一元素排名的族群內 spearman,回傳各族群中位數。

    這個數字回答「最終輸出的名次,實質上是不是就是該元素的名次」。
    """
    col = ELEMENT_COLS[element]
    v = []
    for rows in groups:
        r = spearman([composite_of(r, weights) for r in rows],
                     [_get(x, col) for x in rows])
        if r is not None:
            v.append(r)
    return statistics.median(v) if v else None


def top_n_churn(groups, element, weights=None, n=STRONG_TOP_N):
    """把某元素權重歸零後,族群內 comp 前 n 名(真強閘門)有幾個席次易主。

    這是「拿掉它會不會改變分層決策」的下限估計:只看前 n 名進出,不重跑完整 tier 邏輯
    (避免與 score.py 的條件鏈重複實作而漂移)。
    """
    weights = WEIGHTS if weights is None else weights
    dropped = {k: (0.0 if k == element else w) for k, w in weights.items()}
    churn = 0
    for rows in groups:
        if len(rows) <= n:
            continue
        def topn(wt):
            ranked = sorted(rows, key=lambda r: composite_of(r, wt), reverse=True)
            return {r["stock_id"] for r in ranked[:n]}
        churn += len(topn(dropped) - topn(weights))
    return churn


def summarize(groups, weights=None):
    """一次算齊每日監控要的全部結構指標。"""
    weights = WEIGHTS if weights is None else weights
    shares = variance_shares(groups, weights)
    if not shares:
        return None
    lead = max(shares, key=lambda k: shares[k])
    return {
        "shares": shares,
        "lead": lead,
        "lead_rho": rank_rho(groups, lead, weights),
        "eff_factors": effective_factors(shares),
        "churn": {k: top_n_churn(groups, k, weights)
                  for k, w in weights.items() if w},
        "alert": _alert(shares, lead, rank_rho(groups, lead, weights)),
    }


def _alert(shares, lead, lead_rho):
    eff = effective_factors(shares)
    hits = []
    if lead_rho is not None and lead_rho > RHO_ALERT:
        hits.append(f"ρ({lead})>{RHO_ALERT}")
    if eff is not None and eff < EFF_ALERT:
        hits.append(f"有效因子數<{EFF_ALERT}")
    return hits


# ── tier 持續性(結構指標第二組:訊號活多久,而非訊號多集中)──────────────
#
# 「每日幾檔變層」是錯的指標——數量分不出「來回震盪(純摩擦成本)」與「單向遷移(真訊號)」。
# 這裡量三件事:停留天數、震盪率、名單換手。三者同樣不需前瞻報酬,故可每日讀。
#
# 最關鍵的產出是 dwell_vs_horizon():若可交易 tier 的中位停留 < 超額被量測的前瞻窗,
# 則「照 tier 進出」抓不到報告 §② 宣稱的那個優勢——量測窗與可用訊號長度不一致。
EVAL_HORIZON_DAYS = 10    # 對齊 validate.py --fwd 預設;呼叫端可覆寫為實際使用的 F
TRADABLE_TIERS = ("真強", "蓄勢·外資佈局", "強但過熱", "真弱")
ROUND_TRIP_WINDOW = 5     # 幾個交易日內變回原 tier 才算「震盪」


def tier_sequences(con, *, since=None):
    """stock_id -> [(date, tier), ...](升冪)。用 daily_scores(最新規則重算歷史)。"""
    sql = "SELECT date, stock_id, tier FROM daily_scores"
    args = ()
    if since:
        sql += " WHERE date>=?"
        args = (since,)
    seqs = {}
    for r in con.execute(sql + " ORDER BY stock_id, date", args):
        seqs.setdefault(r["stock_id"], []).append((r["date"], r["tier"]))
    return seqs


def _runs_of(seq, all_dates):
    """把一檔的 (date, tier) 序列切成區段;日期不連續視為斷點。

    回傳 [(tier, 長度, 是否右截尾)];最後一段必然截尾(我們還沒看到它結束)。
    """
    idx = {d: i for i, d in enumerate(all_dates)}
    out, cur, n = [], None, 0
    prev_i = None
    for d, t in seq:
        i = idx.get(d)
        if i is None:
            continue
        broken = prev_i is not None and i != prev_i + 1
        if cur is None or t != cur or broken:
            if cur is not None:
                out.append((cur, n, False))
            cur, n = t, 1
        else:
            n += 1
        prev_i = i
    if cur is not None:
        out.append((cur, n, True))     # 尾段截尾
    return out


def dwell_runs(seqs, all_dates, *, include_censored=False):
    """tier -> [完整區段長度]。預設排除右截尾的尾段:把只看到一半的區段當成完整的
    會低估停留天數。排除本身也略偏低(被排除的多是長區段),兩種偏誤都往短的方向。"""
    acc = {}
    for seq in seqs.values():
        for t, n, censored in _runs_of(seq, all_dates):
            if censored and not include_censored:
                continue
            acc.setdefault(t, []).append(n)
    return acc


def round_trip_rate(seqs, all_dates, within=ROUND_TRIP_WINDOW):
    """變動後 `within` 個交易日內又變回原 tier 的比例。回傳 (次數, 總變動數, 比例)。"""
    idx = {d: i for i, d in enumerate(all_dates)}
    back = total = 0
    for seq in seqs.values():
        s = [(idx[d], t) for d, t in seq if d in idx]
        s.sort()
        for k in range(1, len(s)):
            if s[k][0] != s[k - 1][0] + 1 or s[k][1] == s[k - 1][1]:
                continue
            total += 1
            prev = s[k - 1][1]
            if any(s[j][1] == prev for j in range(k + 1, len(s))
                   if s[j][0] <= s[k][0] + within):
                back += 1
    return back, total, (back / total if total else None)


def membership_turnover(seqs, all_dates, tier):
    """名單進出:平均檔數、每日新進/退出、全量換手需時(交易日)、年化換手次數。"""
    by_date = {d: set() for d in all_dates}
    for sid, seq in seqs.items():
        for d, t in seq:
            if t == tier and d in by_date:
                by_date[d].add(sid)
    ins, outs, sizes = [], [], []
    for i in range(1, len(all_dates)):
        a, b = by_date[all_dates[i - 1]], by_date[all_dates[i]]
        ins.append(len(b - a))
        outs.append(len(a - b))
        sizes.append(len(b))
    if not sizes or not statistics.mean(sizes):
        return None
    avg_n, avg_in = statistics.mean(sizes), statistics.mean(ins)
    days = (avg_n / avg_in) if avg_in else None
    return {"avg_n": avg_n, "avg_in": avg_in, "avg_out": statistics.mean(outs),
            "full_turn_days": days, "turns_per_year": (250 / days) if days else None}


def dwell_vs_horizon(seqs, all_dates, *, horizon=EVAL_HORIZON_DAYS,
                     tiers=TRADABLE_TIERS):
    """列出中位停留 < 前瞻量測窗的可交易 tier —— 照訊號進出抓不到被量測的優勢。"""
    runs = dwell_runs(seqs, all_dates)
    short = []
    for t in tiers:
        v = runs.get(t)
        if v:
            med = statistics.median(v)
            if med < horizon:
                short.append((t, med))
    return short


def churn_summary(seqs, all_dates, *, horizon=EVAL_HORIZON_DAYS):
    """一次算齊 tier 持續性要的全部數字。"""
    runs = dwell_runs(seqs, all_dates)
    if not runs:
        return None
    back, total, rate = round_trip_rate(seqs, all_dates)
    return {
        "dwell": {t: statistics.median(v) for t, v in runs.items()},
        "dwell_n": {t: len(v) for t, v in runs.items()},
        "round_trip": (back, total, rate),
        "turnover": {t: membership_turnover(seqs, all_dates, t) for t in TRADABLE_TIERS},
        "short_vs_horizon": dwell_vs_horizon(seqs, all_dates, horizon=horizon),
        "horizon": horizon,
    }


# ── 兩個視角的分歧(結構指標第三組)────────────────────────────────────
#
# 「價格」與「籌碼」是兩個近乎正交的視角(實測族群內排名相關 ρ≈0.27~0.52),而分歧本身
# 就是資訊:動能強而籌碼弱 = 漲了但沒人接;籌碼強而動能弱 = 有人在買但價格還沒動。
# 實測 ρ(動能,籌碼) 在 2026 年 1 月是 0.66,到 7 月修正時降到全期最低 0.37
# ——**市場轉折時兩個視角分歧最大**。
#
# 這組同樣不需要前瞻報酬 → 可每日讀。但**它是描述,不是訊號**:它有沒有預測力,
# 正由事先登錄的假設 H1 檢定中(見 hypotheses.py 與週報 §⑪),目前尚無結論。
#
# 百分位一律用**平均秩**:s_* 是 −2..+2 的整數,用排序切片會大量平手,結果隨餵入順序
# 而變(2026-07-26 的實測:93% 的格在邊界平手,換順序讓統計量從 t=1.4 掉到 t=0.2)。
# 平均秩給平手相同的秩,與任何順序無關。
DIVERGE_NOTABLE = 40.0     # |分歧| ≥ 此值(百分位點)才列為值得一看


def lens_pct(values):
    """把一組分數轉成族群內百分位(0~100),平手取平均秩 → 與餵入順序無關。"""
    n = len(values)
    if n < 2:
        return [50.0] * n
    return [(r - 1) / (n - 1) * 100 for r in rankdata(list(values))]


def divergence(rows, chip_weights, momentum_col="s_price"):
    """回傳 (每檔的分歧明細, 該組的視角相關 ρ)。

    分歧 = 動能百分位 − 籌碼百分位(百分位點)。正 = 漲了但沒人接;負 = 有人接但沒漲。
    """
    if len(rows) < 2:
        return [], None
    mom = [_get(r, momentum_col) for r in rows]
    chip = [sum(w * _get(r, k) for k, w in chip_weights.items()) for r in rows]
    mp, cp = lens_pct(mom), lens_pct(chip)
    out = [{"stock_id": r["stock_id"], "mom_pct": round(mp[i], 1),
            "chip_pct": round(cp[i], 1), "gap": round(mp[i] - cp[i], 1),
            "mom_score": _get(r, momentum_col), "chip_score": round(chip[i], 2)}
           for i, r in enumerate(rows)]
    return out, spearman(mom, chip)


def divergence_summary(groups, chip_weights, momentum_col="s_price"):
    """跨族群彙總:每檔明細 + 各族群 ρ 的中位(= 當日兩視角的一致程度)。"""
    detail, rhos = [], []
    for rows in groups:
        d, rho = divergence(rows, chip_weights, momentum_col)
        for x in d:
            x["grp"] = rows[0]["grp"] if "grp" in rows[0].keys() else None
        detail.extend(d)
        if rho is not None:
            rhos.append(rho)
    if not detail:
        return None
    return {
        "detail": detail,
        "rho_median": statistics.median(rhos) if rhos else None,
        "n_groups": len(rhos),
        "price_ahead": sorted((x for x in detail if x["gap"] >= DIVERGE_NOTABLE),
                              key=lambda x: -x["gap"]),
        "chips_ahead": sorted((x for x in detail if x["gap"] <= -DIVERGE_NOTABLE),
                              key=lambda x: x["gap"]),
    }


# ── 時間尺度視角(結構指標第四組)──────────────────────────────────────
#
# 前面所有東西都活在同一個時間尺度上:五元素裡的價格軸是 rs20,族群層的動能也是
# 20 日。也就是說整個系統只有一個週期的視野,而「這檔強不強」在不同週期可以是
# 完全不同的答案——2026-07-24 的南電 tier=真強、波段與趨勢都在族群內 100 分位,
# 短期卻只有 9 分位(剛開始回檔);健策則相反,波段 100 而趨勢 0(剛從長期低檔翻上來)。
#
# 三個視角都是**絕對價格事實**,再各自做族群內平均秩百分位——這樣三欄才可比:
#   短期 close_adj/ma5   最近 5 日相對自身均線
#   波段 ret20           20 日報酬(族群內排名 ⇔ 排 rs20,兩者只差一個族群常數)
#   趨勢 ma20/ma60       中期均線相對長期均線
#
# 冗餘門檻沿用分歧視角那次的規矩 |ρ| ≥ 0.8 不採用。2026-07-26 實測,窗口為
# 2026-05-27..07-24 共 41 個交易日(ma60 需 60 日暖身,更早的算不出來):
#   逐日 ρ 取中位(**這是部署中實際執行的門檻**,build_lenses 逐日重算再取中位):
#     短↔趨 +0.04、短↔波 +0.32、波↔趨 +0.49
#   pooled 4961 stock-days(另一種統計量,結論相同):+0.02 / +0.34 / +0.49
#   ρ(波段, rs20) = +1.00,且每一天都是 —— 這是恆等式不是發現:
#     rs20 = ret20 − 族群中位,族群內做保序平移,排名必然相同。波段欄即現行視角。
# 最初的趨勢定義 close_adj/ma60 已否決,但**要說清楚是憑什麼否決的**:它在逐日中位
# 下是 +0.789(對波段)與 +0.799(對 ma20/ma60)——**低於 0.8,門檻擋不住它**。
# 否決是判斷:它同時像另外兩欄(兩邊都 ≈0.79),等於把第三欄花在重複的資訊上;
# 而且以 41 天、日 ρ 一階自相關 +0.59~0.76 推算約 5~11 個有效獨立觀測,0.789 與
# 0.80 本來就分不開。門檻只是篩子,不是判準。
#
# 窗口本身不是單一走勢:大盤 05-27 起先漲 8.2% 到 06-22 的期間高,再回 7.9%
# (曾誤寫成「幾乎全在同一段修正裡」,實測後更正)。但 41 天仍短,ρ 在其他行情
# 下未必相同。ρ 低也不等於獨立——波段與趨勢共用同一段 20 日價格,機械相關的底線
# 尚未拆解(ANALYSIS_DISCIPLINE 檢查表 §1.6 的打散重算還沒做)。
# 這裡只把 ρ 當冗餘篩,不當假設檢定,故不附標準誤與 t。
#
# 與分歧視角一樣:**這是描述,不是訊號**,未計分、未進 tier、無前瞻報酬主張。
LENS_SPREAD_NOTABLE = 50.0   # 三視角百分位極差 ≥ 此值才列為「週期看法不一致」

TIME_LENSES = (
    ("short", "短期", "close_adj", "ma5"),
    ("swing", "波段", None, None),          # 直接用 ret20
    ("trend", "趨勢", "ma20", "ma60"),
)


def _raw(row, col):
    """取原值,缺值回 None —— **不可用 `_get`**:它把 None 當 0(那是給 s_* 分數
    「無訊號=中性」用的)。均線與報酬沒有這種語意:ret20 缺值變 0 會被當成「持平」
    排進名次,close_adj 缺值變 0 會算出 −100% 的短期視角。兩者都是憑空捏造的位置。"""
    try:
        return row[col]
    except (KeyError, IndexError):
        return None


def _lens_raw(row, key, num, den):
    if key == "swing":
        return _raw(row, "ret20")
    a, b = _raw(row, num), _raw(row, den)
    if a is None or b is None or not b:
        return None
    return a / b - 1


def time_lenses(rows):
    """回傳該族群每檔在三個時間尺度上的族群內百分位與極差。

    任一視角缺值(暖身不足)就整檔略過——只排得出兩欄的極差不可與三欄的比較。
    """
    ok = []
    for r in rows:
        vals = {k: _lens_raw(r, k, n, d) for k, _, n, d in TIME_LENSES}
        if all(v is not None for v in vals.values()):
            ok.append((r, vals))
    if len(ok) < 2:
        return []
    pct = {k: lens_pct([v[k] for _, v in ok]) for k, _, _, _ in TIME_LENSES}
    out = []
    for i, (r, vals) in enumerate(ok):
        p = {k: round(pct[k][i], 1) for k, _, _, _ in TIME_LENSES}
        out.append({"stock_id": r["stock_id"], "pct": p,
                    "raw": {k: round(vals[k] * 100, 2) for k in vals},
                    "spread": round(max(p.values()) - min(p.values()), 1)})
    return out


def time_lens_summary(groups):
    """跨族群彙總 + 三視角兩兩相關(pooled,用來證明它們不是同一件事講三遍)。"""
    detail, series = [], {k: [] for k, _, _, _ in TIME_LENSES}
    for rows in groups:
        d = time_lenses(rows)
        g = rows[0]["grp"] if rows and "grp" in rows[0].keys() else None
        for x in d:
            x["grp"] = g
            for k in series:
                series[k].append(x["pct"][k])
        detail.extend(d)
    if not detail:
        return None
    keys = [k for k, _, _, _ in TIME_LENSES]
    rho = {}
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            rho[f"{a}-{b}"] = spearman(series[a], series[b])
    return {
        "detail": detail,
        "rho": rho,
        "spread_median": round(statistics.median(x["spread"] for x in detail), 1),
        "notable": sorted((x for x in detail if x["spread"] >= LENS_SPREAD_NOTABLE),
                          key=lambda x: -x["spread"]),
    }


def group_rows(con, date, *, snapshot_id=None):
    """把某資料日的評分列依族群分組。snapshot_id 給定時讀 as-seen 快照(自帶當日族群)。"""
    if snapshot_id:
        rows = [dict(r) for r in con.execute(
            "SELECT * FROM oos_signal_snapshots WHERE snapshot_id=?", (snapshot_id,))]
    else:
        rows = [dict(r) for r in con.execute(
            """SELECT s.*, u.grp FROM daily_scores s JOIN universe u USING(stock_id)
               WHERE s.date=?""", (date,))]
    by = {}
    for r in rows:
        by.setdefault(r["grp"], []).append(r)
    return list(by.values())


def group_metric_rows(con, date):
    """同上,但取原始 daily_metrics —— 時間尺度視角要的是均線與報酬,不是
    daily_scores 的 −2..+2 分數。

    不支援 snapshot_id,但**理由不是快照表缺欄**:`oos_signal_snapshots` 有 65 欄,
    ma5/ma20/ma60/ret20/close_adj/grp 全都在,且 1118/1118 列都有值(2026-07-26 實查;
    一度誤寫成「快照表沒有均線欄」)。純粹是目前沒有消費端需要 as-seen 的時間尺度
    歷史;要接的話資料是齊的。"""
    rows = [dict(r) for r in con.execute(
        """SELECT m.*, u.grp FROM daily_metrics m JOIN universe u USING(stock_id)
           WHERE m.date=?""", (date,))]
    by = {}
    for r in rows:
        by.setdefault(r["grp"], []).append(r)
    return list(by.values())
