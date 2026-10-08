#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""stats_ci.py — 判讀強度:HAC 標準誤、重疊窗樣本尺度、episode 計數。

**為什麼需要這支模組**(2026-07-26 對抗性審查的結論):
在此之前,報告裡每個 IC 與超額都只有點估計與 `n=格數`,沒有任何誤差量。實際重算後
發現三個候選策略的全期 IC 分別是 +0.021 / +0.034 / +0.040,配上 Newey-West 標準誤
之後 **t 值全部 < 2**——也就是在比較三個統計上等於零的數字的小數點。

兩個會讓人系統性高估證據強度的陷阱,這裡各給一個對策:

1. **前瞻窗重疊 → 日 IC 高度自相關**(實測 lag-1 = +0.70)。普通標準誤假設獨立,
   會嚴重低估不確定性。→ `nw_se()` 用 Newey-West 修正,lag 預設 = 前瞻窗 − 1。
2. **`n=格數` 讓樣本看起來很大**。先按交易日聚合,再列出 n/F 與連續區段。
   n/F 是重疊窗有效樣本尺度(啟發式,非量得獨立性),並非真實有效樣本數或必然上界;
   長記憶、缺日與市場區段都會改變資訊量。

HAC 的 lag 是完整交易日距離。None 保留原位置,缺少的交易日也不會被壓縮成相鄰日。
這修正時間對齊,不代表既有分級門檻已對所有自相關或多重比較完成校準。
"""
import math
import statistics


EFFECTIVE_OBS_METHOD = "重疊窗有效樣本尺度(n/F;啟發式,非量得獨立性)"


def _calendar_positions(all_dates):
    """Validate the complete chronological calendar without silently sorting it."""
    calendar = list(all_dates)
    if len(set(calendar)) != len(calendar):
        raise ValueError("all_dates must contain unique trading dates")
    if calendar != sorted(calendar):
        raise ValueError("all_dates must be in chronological order")
    return {date: position for position, date in enumerate(calendar)}


def _aligned_values(series, dates_used=None, all_dates=None):
    """Return finite observations with their original trading-calendar positions.

    None is an explicit missing observation. Non-finite numeric values are data
    errors, not an instruction to change the sample. Date/value alignment must
    be supplied as a pair and is never repaired by independently sorting dates.
    """
    values = list(series)
    if (dates_used is None) != (all_dates is None):
        raise ValueError("dates_used and all_dates must be provided together")
    if dates_used is None:
        positions = list(range(len(values)))
        used = None
    else:
        used = list(dates_used)
        if len(used) != len(values):
            raise ValueError("dates_used must align one-to-one with series")
        calendar_pos = _calendar_positions(all_dates)
        if len(set(used)) != len(used):
            raise ValueError("dates_used must contain unique trading dates")
        if any(date not in calendar_pos for date in used):
            raise ValueError("dates_used contains a date absent from all_dates")
        positions = [calendar_pos[date] for date in used]
        if positions != sorted(positions):
            raise ValueError("dates_used must follow all_dates order; do not shuffle alignment")
    observed = []
    observed_dates = []
    for index, (position, value) in enumerate(zip(positions, values)):
        if value is None:
            continue
        try:
            finite = math.isfinite(value)
        except TypeError as exc:
            raise ValueError("series values must be finite numbers or None") from exc
        if not finite:
            raise ValueError("series values must be finite numbers or None")
        observed.append((position, value))
        if used is not None:
            observed_dates.append(used[index])
    return observed, observed_dates if used is not None else None


def _lag_products(observed, lag):
    """Centered covariance numerators and observed pair counts at real lags."""
    center = statistics.mean(value for _, value in observed)
    errors = {position: value - center for position, value in observed}
    products = {0: sum(error * error for error in errors.values())}
    counts = {0: len(errors)}
    for distance in range(1, lag + 1):
        pairs = [(error, errors[position - distance]) for position, error in errors.items()
                 if position - distance in errors]
        products[distance] = sum(current * previous for current, previous in pairs)
        counts[distance] = len(pairs)
    return products, counts


def overlap_lag(fwd):
    """重疊前瞻窗的 Newey-West lag:窗長 F 的重疊延伸到 F−1 期。"""
    return max(int(fwd) - 1, 0)


def nw_se(series, lag, *, dates_used=None, all_dates=None):
    """Newey-West 標準誤(Bartlett kernel)。series = 每個交易日一個數。

    lag=0 時退化為 population SD / sqrt(n)。回傳 None 表示觀測少於 3 筆。
    若提供 dates_used/all_dates,lag 依完整交易日距離;否則依 series 的原位置。
    缺值不補零、不壓縮;分母 n 只計非 None 觀測。日期對齊錯誤明確拒絕。
    """
    if int(lag) != lag or lag < 0:
        raise ValueError("lag must be a non-negative integer")
    lag = int(lag)
    observed, _ = _aligned_values(series, dates_used, all_dates)
    n = len(observed)
    if n < 3:
        return None
    products, _ = _lag_products(observed, lag)
    s = products[0] / n
    for distance in range(1, lag + 1):
        s += 2 * (1 - distance / (lag + 1)) * products[distance] / n
    return (max(s, 0.0) / n) ** 0.5


def autocorr1(series, *, dates_used=None, all_dates=None):
    """One-trading-day covariance ratio; absent adjacent pairs give None."""
    observed, _ = _aligned_values(series, dates_used, all_dates)
    if len(observed) < 3:
        return None
    products, counts = _lag_products(observed, 1)
    if not products[0] or not counts[1]:
        return None
    return products[1] / products[0]


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
    """n/F:重疊窗有效樣本尺度(啟發式,非量得獨立性)。

    沿用作為既有治理 gate 的尺度,不是估計的獨立樣本數、也不是保證的上界。
    真實有效樣本會受長記憶與缺口影響;不可用此值宣稱已觀察到 n/F 個獨立事件。
    """
    if not n_days or not fwd:
        return 0.0
    return n_days / float(fwd)


# NW 估計需要 n 遠大於 lag。實測反例:5 個成熟日配 lag=4 時,5 個高度重疊的日 IC
# 幾乎相同 → 變異數塌陷 → 吐出 ±0.008、t=−23.3。**那個區塊本來就是要防止過度解讀的,
# 卻會在 OOS 剛成熟(正好 5~10 日)時印出假精確的 t 值。**
# 沿用 n/F 的治理下限,不把這個啟發式尺度冒充量得的獨立性。
MIN_EFF_OBS = 3.0


def summarize(daily, fwd, dates_used=None, all_dates=None):
    """一次算齊判讀強度。daily = 每個交易日一個數(例:當日各族群 IC 的平均)。

    n/F 未達治理下限時不回報 SE 與 t。None 保留日距離;日期與數值不可各自排序。
    dates_used/all_dates 若有提供,必須成對、無重複、長度相符且有序。
    """
    if int(fwd) != fwd or fwd <= 0:
        raise ValueError("fwd must be a positive integer")
    values = list(daily)
    used = list(dates_used) if dates_used is not None else None
    calendar = list(all_dates) if all_dates is not None else None
    observed, observed_dates = _aligned_values(values, used, calendar)
    x = [value for _, value in observed]
    if not x:
        return None
    lag = overlap_lag(fwd)
    eff = effective_obs(len(x), fwd)
    m = statistics.mean(x)
    se = nw_se(values, lag, dates_used=used, all_dates=calendar) if eff >= MIN_EFF_OBS else None
    _, lag_counts = _lag_products(observed, lag)
    return {
        "mean": m, "se": se, "t": (m / se) if se else None,
        "n_days": len(x), "lag": lag, "eff_obs": eff,
        "se_blocked": eff < MIN_EFF_OBS,
        "ac1": autocorr1(values, dates_used=used, all_dates=calendar),
        "episodes": episodes(observed_dates, calendar) if observed_dates is not None else None,
        "eff_obs_method": EFFECTIVE_OBS_METHOD,
        "calendar_span_days": observed[-1][0] - observed[0][0] + 1,
        "observed_lag_pairs": lag_counts,
        "zero_se": se == 0.0,
    }


def paired_daily_difference(left_by_date, right_by_date, *, all_dates):
    """Return left minus right only on common observed trading dates.

    Input map insertion order is irrelevant. Unknown dates or non-finite values
    are rejected, including on unpaired dates, so an invalid input cannot hide
    behind the intersection. None is missing and excluded symmetrically.
    """
    calendar = list(all_dates)
    positions = _calendar_positions(calendar)
    for source in (left_by_date, right_by_date):
        if any(date not in positions for date in source):
            raise ValueError("paired series contains a date absent from all_dates")
        used = sorted(source, key=positions.get)
        _aligned_values([source[date] for date in used], used, calendar)
    return {date: left_by_date[date] - right_by_date[date] for date in calendar
            if date in left_by_date and date in right_by_date
            and left_by_date[date] is not None and right_by_date[date] is not None}


def fmt(s, digits=3):
    """排成一格。SE 不可估時仍顯示點估計,但明確標示不可估——不要讓它看起來像有誤差棒。"""
    if not s:
        return "–"
    if s.get("se") is None:
        if s.get("se_blocked"):
            return f"{s['mean']:+.{digits}f} (SE 不可估)"
        return "–"
    if s.get("t") is None:
        return f"{s['mean']:+.{digits}f} ±{s['se']:.{digits}f} (t 不可估)"
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
# 下表保留原治理門檻。上述是特定 AR(1) 與連續取樣的模擬背景,並非一般型態的保證;
# 本次改正缺日對齊沒有重設門檻,也沒有校準反覆週檢視或多重比較的家庭錯誤率。
T_THRESHOLD = ((6.0, 4.0), (12.0, 3.0), (30.0, 2.5))   # (eff_obs 上界, 門檻)
T_THRESHOLD_LARGE = 2.4


def t_threshold(eff_obs):
    """依 n/F 啟發式尺度回傳既有治理門檻;不是通用顯著水準保證。"""
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
        return f"**n/F 樣本尺度 <{MIN_EFF_OBS:.0f},不判讀**"
    if s.get("t") is None:
        if s.get("se") == 0.0:
            return "**SE 為 0，t 不可估，不判讀**"
        return "樣本不足"
    thr = t_strong if t_strong is not None else t_threshold(s.get("eff_obs") or 0.0)
    if abs(s["t"]) >= thr:
        return f"可分辨於 0(門檻 {thr:.1f})"
    return f"**與 0 無法分辨**(門檻 {thr:.1f})"
