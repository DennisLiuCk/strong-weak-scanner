"""首頁與週報共用的 OOS 樣本狀態；不判定任何因子或策略有效。"""
import stats_ci as sci


def first_official_runs(con):
    """同資料日採首次正式發布；空快照不得用後來修正版冒充。"""
    runs = {}
    for row in con.execute("""SELECT * FROM oos_snapshot_runs WHERE is_official=1
                              ORDER BY data_date, captured_at, snapshot_id"""):
        runs.setdefault(row["data_date"], row)
    return runs


def maturity(snapshot_dates, trading_dates, cutoff, fwd):
    """交易日成熟度是樣本上限；各指標仍須依自己的有效日數估 SE / t。"""
    if fwd <= 0:
        raise ValueError("前瞻交易日數必須大於 0")
    dates = sorted(set(trading_dates))
    positions = {d: i for i, d in enumerate(dates)}
    oos = sorted(d for d in set(snapshot_dates)
                 if cutoff and d > cutoff and d in positions)
    mature = [d for d in oos if positions[d] + fwd < len(dates)]
    eff = sci.effective_obs(len(mature), fwd)
    blocked = eff < sci.MIN_EFF_OBS
    label = "獨立觀測不足，暫不判讀" if blocked else "逐指標檢查證據，尚非策略通過"
    reason = (f"有效獨立觀測未達 {sci.MIN_EFF_OBS:g}，SE／t 暫不可估；不據此調整策略。"
              if blocked else
              "僅達估計 SE 的最低樣本要求；各指標須通過週報 §⑨ 的分級 t 門檻，"
              "再依 WEEKLY_REVIEW 的連續週數與成本條件判斷。")
    return {"oos_days": len(oos), "oos_mature": len(mature), "fwd": fwd,
            "eff_obs": eff, "episodes": sci.episodes(mature, dates),
            "min_eff_obs": sci.MIN_EFF_OBS, "se_blocked": blocked,
            "status": "insufficient_independent_observations" if blocked else "per_metric_review_required",
            "label": label, "reason": reason}
