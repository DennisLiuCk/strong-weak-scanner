"""Pure validation calculations: paired populations and executable-price cohorts.

No database access. A caller must supply first eligible official signals when
claiming OOS. Daily outputs retain calendar keys; no missing observation is zero.
"""
import statistics

from signal_structure import spearman


def paired_rank_ics(champion, challenger, returns):
    """Return both rank ICs on one identical stock set, or None for both.

    A constant leg invalidates the pair; it must not change the comparison's
    group population by being dropped on only one side.
    """
    ids = sorted(s for s, r in returns.items() if r is not None
                 and champion.get(s) is not None and challenger.get(s) is not None)
    target = [returns[s] for s in ids]
    left = spearman([champion[s] for s in ids], target)
    right = spearman([challenger[s] for s in ids], target)
    return (left, right) if left is not None and right is not None else None


def leader_hit(signal, future):
    """Equal allocation across tied signal leaders; random baseline respects ties."""
    if not signal or set(signal) != set(future):
        return None
    if any(v is None for v in (*signal.values(), *future.values())):
        return None
    leaders = [g for g, v in signal.items() if v == max(signal.values())]
    winners = {g for g, v in future.items() if v == max(future.values())}
    return len(set(leaders) & winners) / len(leaders), len(winners) / len(future)


def fixed_hold_net_series(scores, calendar, adjusted_open, grp_of, tier, hold,
                          cost_pct):
    """Daily stock-equal cohort excess, open(d+1) to open(d+1+hold).

    Benchmark is gross leave-one-out group median, at least five peers. This
    is not a funded portfolio or a tier-exit strategy. Missing entry/exit prices
    are excluded, with coverage counts returned for every mature signal day.
    """
    if hold <= 0:
        raise ValueError("hold must be positive")
    index = {d: i for i, d in enumerate(calendar)}
    daily, coverage = {}, {}
    for day, rows in sorted(scores.items()):
        pos = index.get(day)
        if pos is None or pos + 1 + hold >= len(calendar):
            continue
        entry, end = calendar[pos + 1], calendar[pos + 1 + hold]
        grouped = {}
        for sid in rows:
            a, b = adjusted_open.get((entry, sid)), adjusted_open.get((end, sid))
            if a and b and a > 0 and b > 0:
                grouped.setdefault(grp_of(day, sid), {})[sid] = b / a - 1
        selected = [s for s, row in rows.items() if row["tier"] == tier]
        values = []
        for sid in selected:
            returns = grouped.get(grp_of(day, sid), {})
            peers = [v for s, v in returns.items() if s != sid]
            if sid in returns and len(peers) >= 5:
                values.append(100 * (returns[sid] - statistics.median(peers)) - cost_pct)
        coverage[day] = {"selected": len(selected), "evaluated": len(values),
                         "excluded": len(selected) - len(values)}
        if values:
            daily[day] = statistics.mean(values)
    return daily, coverage


def subset_series(series, predicate):
    return {day: value for day, value in series.items() if predicate(day)}
