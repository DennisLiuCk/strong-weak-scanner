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
