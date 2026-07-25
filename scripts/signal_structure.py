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
