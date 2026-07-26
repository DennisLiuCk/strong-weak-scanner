#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""stats_ci.py — 判讀強度:標準誤、有效獨立觀測、episode 計數(純計算,零第三方依賴)。

**為什麼需要這支模組**(2026-07-26 對抗性審查的結論):
在此之前,報告裡每個 IC 與超額都只有點估計與 `n=格數`,沒有任何誤差量。實際重算後
發現三個候選策略的全期 IC 分別是 +0.021 / +0.034 / +0.040,配上 Newey-West 標準誤
之後 **t 值全部 < 2**——也就是在比較三個統計上等於零的數字的小數點。

兩個會讓人系統性高估證據強度的陷阱,這裡各給一個對策:

1. **前瞻窗重疊 → 日 IC 高度自相關**(實測 lag-1 = +0.70)。普通標準誤假設獨立,
   會嚴重低估不確定性。→ `nw_se()` 用 Newey-West 修正,lag 預設 = 前瞻窗 − 1。
2. **`n=格數` 讓樣本看起來很大**。10 個交易日 × 11 族群 = 110 格,但那 10 天的前瞻窗
   幾乎完全重疊,實際上接近**一個**獨立觀測。→ `effective_obs()` 與 `episodes()`
   report 真正的獨立程度。
"""
import statistics


def overlap_lag(fwd):
    """重疊前瞻窗的 Newey-West lag:窗長 F 的重疊延伸到 F−1 期。"""
    return max(int(fwd) - 1, 0)


def nw_se(series, lag):
    """Newey-West 標準誤(Bartlett kernel)。series = 每個交易日一個數。

    lag=0 時退化為一般標準誤。回傳 None 表示樣本不足以估計。
    """
    x = [v for v in series if v is not None]
    n = len(x)
    if n < 3:
        return None
    m = statistics.mean(x)
    e = [v - m for v in x]
    s = sum(v * v for v in e) / n                      # gamma_0
    for L in range(1, min(int(lag), n - 1) + 1):
        g = sum(e[i] * e[i - L] for i in range(L, n)) / n
        s += 2 * (1 - L / (lag + 1)) * g               # Bartlett 權重
    return (max(s, 0.0) / n) ** 0.5


def autocorr1(series):
    """lag-1 自相關;用來說明「為什麼要用 NW」而不是憑空宣稱。"""
    x = [v for v in series if v is not None]
    if len(x) < 3:
        return None
    m = statistics.mean(x)
    den = sum((v - m) ** 2 for v in x)
    if not den:
        return None
    return sum((x[i] - m) * (x[i - 1] - m) for i in range(1, len(x))) / den


def episodes(dates, all_dates):
    """把一組交易日切成「連續區段」數。

    regime 桶的 451 個格可能只來自 5 段連續修正——段數才是有效事件數,格數不是。
    """
    idx = {d: i for i, d in enumerate(all_dates)}
    pos = sorted(idx[d] for d in dates if d in idx)
    if not pos:
        return 0
    return 1 + sum(1 for i in range(1, len(pos)) if pos[i] != pos[i - 1] + 1)


def effective_obs(n_days, fwd):
    """重疊前瞻窗下的近似獨立觀測數 = 交易日數 / 窗長(至少 0)。

    10 個成熟日配 10 日前瞻窗 ≈ **1 個**獨立觀測——這個數字比 n=110 誠實得多。
    """
    if not n_days or not fwd:
        return 0.0
    return n_days / float(fwd)


# NW 估計需要 n 遠大於 lag。實測反例:5 個成熟日配 lag=4 時,5 個高度重疊的日 IC
# 幾乎相同 → 變異數塌陷 → 吐出 ±0.008、t=−23.3。**那個區塊本來就是要防止過度解讀的,
# 卻會在 OOS 剛成熟(正好 5~10 日)時印出假精確的 t 值。**
# 門檻用「有效獨立觀測」而非天數,語意才一致:前瞻 F 日窗下 n 天 ≈ n/F 個獨立觀測。
MIN_EFF_OBS = 3.0


def summarize(daily, fwd, dates_used=None, all_dates=None):
    """一次算齊判讀強度。daily = 每個交易日一個數(例:當日各族群 IC 的平均)。

    有效獨立觀測不足時**刻意不回報 SE 與 t**——寧可顯示「樣本不足」,
    也不要給一個會被當成證據的假數字。
    """
    x = [v for v in daily if v is not None]
    if not x:
        return None
    lag = overlap_lag(fwd)
    eff = effective_obs(len(x), fwd)
    m = statistics.mean(x)
    se = nw_se(x, lag) if eff >= MIN_EFF_OBS else None
    return {
        "mean": m, "se": se, "t": (m / se) if se else None,
        "n_days": len(x), "lag": lag, "eff_obs": eff,
        "se_blocked": eff < MIN_EFF_OBS,
        "ac1": autocorr1(x),
        "episodes": (episodes(dates_used, all_dates)
                     if dates_used is not None and all_dates is not None else None),
    }


def fmt(s, digits=3):
    """排成一格。SE 不可估時仍顯示點估計,但明確標示不可估——不要讓它看起來像有誤差棒。"""
    if not s:
        return "–"
    if s.get("se") is None:
        if s.get("se_blocked"):
            return f"{s['mean']:+.{digits}f} (SE 不可估)"
        return "–"
    return f"{s['mean']:+.{digits}f} ±{s['se']:.{digits}f} (t={s['t']:+.1f})"


# ── t 門檻必須隨有效獨立觀測分級 ────────────────────────────────────────
# 1.96 是「大樣本、獨立」下的 5% 臨界值,在這裡完全不適用。用 repo 自己的 nw_se 跑
# Monte Carlo(null 為真、4000 reps、AR(1) φ=0.63 貼合實測日 IC 自相關 +0.63):
#
#   有效獨立觀測   null 下 |t| 的 q95   用 1.96 的實際誤判率
#        3.0             4.02                 24.3%
#        5.0             3.15                 17.9%
#        8.9             2.62                 13.0%
#       15.0             2.46                 11.4%
#       30.0             2.36                 10.1%
#
# 也就是說,原本用 1.96 判「可分辨於 0」時,誤判率是 10~24% 而不是 5%。
# 下表取上述 q95 並向上取整,故各級都偏保守。改用純 MA(F) null(自相關更強)門檻會更高,
# 真實序列介於兩者之間 → 取較寬鬆的 AR 版當門檻已是下限。
T_THRESHOLD = ((6.0, 4.0), (12.0, 3.0), (30.0, 2.5))   # (eff_obs 上界, 門檻)
T_THRESHOLD_LARGE = 2.4


def t_threshold(eff_obs):
    """依有效獨立觀測回傳該用的 |t| 門檻(MC 校準,見上表)。"""
    for upper, thr in T_THRESHOLD:
        if eff_obs < upper:
            return thr
    return T_THRESHOLD_LARGE


def verdict(s, t_strong=None):
    """一句話判讀。刻意不說「有效/無效」,只說證據夠不夠分辨。

    門檻預設隨 `eff_obs` 分級;傳 t_strong 可覆寫(僅供測試/診斷)。
    """
    if not s:
        return "樣本不足"
    if s.get("se_blocked"):
        return f"**獨立觀測 <{MIN_EFF_OBS:.0f},不判讀**"
    if s.get("t") is None:
        return "樣本不足"
    thr = t_strong if t_strong is not None else t_threshold(s.get("eff_obs") or 0.0)
    if abs(s["t"]) >= thr:
        return f"可分辨於 0(門檻 {thr:.1f})"
    return f"**與 0 無法分辨**(門檻 {thr:.1f})"
