#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Read-only strategy diagnostics; never changes scores or registers a strategy.

Only the first eligible official snapshot supplies signals and group membership.
Returns use the current adjusted-price history. Daily clusters, rather than
stock-days, supply HAC uncertainty. Ablations are retrospective diagnostics,
not prospective OOS evidence for a newly selected strategy. Output is UTF-8/LF.
"""
import argparse
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path
import platform
import statistics as st
import sys

import db_ro
import evidence_status
import ranking_views as rv
from score import WEIGHTS, STEALTH_OFF_HIGH
import stats_ci as sci
import validation_metrics as vm
from validate import COST_ROUND_TRIP, IS_CUTOFF, ELEMENTS, spearman

ROOT = Path(__file__).resolve().parents[1]


def calendar_hac_se(series, horizon, calendar):
    """Sensitivity: Bartlett weights use actual trading-day distance across gaps.

    Keeps the repository's daily sample size and finite-sample governance rules.
    This is an audit sensitivity, not a replacement for stats_ci or its gate.
    """
    if len(series) / horizon < sci.MIN_EFF_OBS:
        return None
    positions = {day: i for i, day in enumerate(calendar)}
    center = st.mean(series.values())
    residuals = [(positions[day], value - center) for day, value in sorted(series.items())]
    variance_sum = sum(e * e for _, e in residuals)
    for i, (position, error) in enumerate(residuals):
        for prior_position, prior_error in residuals[:i]:
            gap = position - prior_position
            if 0 < gap < horizon:
                variance_sum += 2 * (1 - gap / horizon) * error * prior_error
    return max(variance_sum, 0) ** 0.5 / len(series)


def summary(series, horizon, calendar, units):
    days = sorted(series)
    result = sci.summarize([series[d] for d in days], horizon, days, calendar)
    if result is None:
        return None
    result.update(first=days[0], last=days[-1], units=units,
                  threshold=sci.t_threshold(result['eff_obs']), daily=series)
    sensitivity_se = calendar_hac_se(series, horizon, calendar)
    result['calendar_gap_hac_sensitivity'] = {
        'se': sensitivity_se,
        't': result['mean'] / sensitivity_se if sensitivity_se else None}
    return result


def paired_difference(left, right):
    return {d: left[d] - right[d] for d in sorted(left.keys() & right.keys())}


def paired_rank_delta(champion, challenger, returns):
    """Compare IC on exactly the same group and stock set, including missingness."""
    ids = sorted(s for s in returns if champion.get(s) is not None
                 and challenger.get(s) is not None and returns[s] is not None)
    target = [returns[s] for s in ids]
    original = spearman([champion[s] for s in ids], target)
    alternative = spearman([challenger[s] for s in ids], target)
    return alternative - original if original is not None and alternative is not None else None


def random_leader_hit_rate(group_returns):
    best = max(group_returns.values())
    return sum(value == best for value in group_returns.values()) / len(group_returns)


def peer_excess(returns, sid, *, exclude_self=False):
    peers = [v for s, v in returns.items() if not exclude_self or s != sid]
    return returns[sid] - st.median(peers) if peers else None


def load_inputs(con, as_of=None):
    calendar = [r[0] for r in con.execute(
        'SELECT DISTINCT date FROM daily_metrics ORDER BY date')
        if as_of is None or r[0] <= as_of]
    signals, groups, rankings, runs = {}, {}, {}, {}
    for day, run in evidence_status.current_score_runs(con, IS_CUTOFF).items():
        if day <= IS_CUTOFF or day not in calendar:
            continue
        rows = [dict(r) for r in con.execute(
            'SELECT * FROM oos_signal_snapshots WHERE snapshot_id=?', (run['snapshot_id'],))]
        if not rows:
            continue
        runs[day] = dict(run)
        signals[day] = {r['stock_id']: r for r in rows}
        groups[day] = {r['grp']: dict(r) for r in con.execute(
            'SELECT * FROM oos_group_snapshots WHERE snapshot_id=?', (run['snapshot_id'],))}
        rankings[day] = {r['stock_id']: dict(r) for r in con.execute(
            'SELECT * FROM oos_ranking_view_snapshots WHERE snapshot_id=? AND spec_sha=?',
            (run['snapshot_id'], rv.SPEC_SHA))}
    close = {(r['date'], r['stock_id']): r['close_adj'] for r in con.execute(
        'SELECT date, stock_id, close_adj FROM daily_metrics')}
    opening = {}
    for r in con.execute('''SELECT p.date,p.stock_id,p.open,p.close,a.close AS adjusted
                           FROM price p JOIN price_adj a USING(date,stock_id)'''):
        if r['open'] and r['close'] and r['adjusted']:
            opening[r['date'], r['stock_id']] = r['open'] * r['adjusted'] / r['close']
    return calendar, runs, signals, groups, rankings, close, opening


def analyze(con, as_of=None):
    calendar, runs, signals, groups, rankings, close, opening = load_inputs(con, as_of)
    positions = {d: i for i, d in enumerate(calendar)}

    def returns(day, horizon, next_open=False):
        start = positions[day] + int(next_open)
        end = start + horizon
        if end >= len(calendar):
            return {}
        prices = opening if next_open else close
        result = defaultdict(dict)
        for sid, row in signals[day].items():
            a, b = prices.get((calendar[start], sid)), prices.get((calendar[end], sid))
            if a and b:
                result[row['grp']][sid] = b / a - 1
        return result

    factor, tier, cohort, drops = (defaultdict(dict) for _ in range(4))
    cells = defaultdict(int)
    hit, base, group_ic, group_ties = {}, {}, {}, []
    ablation_paired_cells = defaultdict(int)
    for day in sorted(signals):
        by_group = returns(day, 10)
        if not by_group:
            continue
        factor_cells, tier_values, cohort_values, drop_cells = (defaultdict(list) for _ in range(4))
        group_returns = {}
        for group, rr in by_group.items():
            group_returns[group] = st.median(rr.values())
            ids = sorted(rr)
            future = [rr[sid] for sid in ids]
            for name in ELEMENTS:
                ic = spearman([signals[day][sid][name] for sid in ids], future)
                if ic is not None:
                    factor_cells[name].append(ic)
                    cells[name] += 1
            # Round both sides just as production composite does. Neither side
            # reclassifies tiers or applies 3-day smoothing: a marginal diagnostic.
            original = [round(sum(w * signals[day][sid]['s_' + k]
                                  for k, w in WEIGHTS.items()), 2) for sid in ids]
            original_ic = spearman(original, future)
            for name, weight in WEIGHTS.items():
                if weight == 0 or original_ic is None:
                    continue
                reduced = [round(value - weight * signals[day][sid]['s_' + name], 2)
                           for sid, value in zip(ids, original)]
                alternative_ic = spearman(reduced, future)
                if alternative_ic is not None:
                    drop_cells[name].append(alternative_ic - original_ic)
                    ablation_paired_cells[name] += 1
            for sid in ids:
                row = signals[day][sid]
                excess_pp = peer_excess(rr, sid) * 100
                tier_values[row['tier']].append(excess_pp)
                if ((row['s_foreign'] >= 2 or row['s_dip'] >= 2)
                        and row['dist_hi60'] is not None
                        and row['dist_hi60'] <= STEALTH_OFF_HIGH
                        and row['down_rs20'] is not None):
                    label = 'pass' if row['down_rs20'] >= 0 else 'blocked'
                    cohort_values[label].append(excess_pp)
        for source, target in ((factor_cells, factor), (tier_values, tier),
                               (cohort_values, cohort), (drop_cells, drops)):
            for key, values in source.items():
                target[key][day] = st.mean(values)
        gm = groups[day]
        if gm and set(gm) == set(group_returns) and all(r['med_dip'] is not None for r in gm.values()):
            leaders = [g for g in gm if gm[g]['med_dip'] == max(r['med_dip'] for r in gm.values())]
            if len(leaders) != 1:
                group_ties.append(day)
            hit[day], base[day] = vm.leader_hit({g: gm[g]['med_dip'] for g in gm}, group_returns)
            ic = spearman([gm[g]['med_dip'] for g in sorted(gm)],
                          [group_returns[g] for g in sorted(gm)])
            if ic is not None:
                group_ic[day] = ic

    net = {}
    for horizon in (3, 5, 10):
        daily = defaultdict(dict)
        for day in sorted(signals):
            values = defaultdict(list)
            for group, rr in returns(day, horizon, next_open=True).items():
                if len(rr) < 6:
                    continue
                for sid in rr:
                    label = signals[day][sid]['tier']
                    if label in ('真強', '蓄勢·外資佈局'):
                        values[label].append(peer_excess(rr, sid, exclude_self=True) * 100 - COST_ROUND_TRIP)
            for label, xs in values.items():
                daily[label][day] = st.mean(xs)
        net[str(horizon)] = {key: summary(value, horizon, calendar, 'percentage_points')
                             for key, value in daily.items()}

    rank_delta = defaultdict(dict)
    for day, rows in sorted(rankings.items()):
        for field in ('shadow_vol0', 'shadow_price10'):
            deltas = []
            for rr in returns(day, 10).values():
                delta = paired_rank_delta(
                    {s: rows[s]['champion_pct'] for s in rr if s in rows},
                    {s: rows[s][field] for s in rr if s in rows}, rr)
                if delta is not None:
                    deltas.append(delta)
            if deltas:
                rank_delta[field][day] = st.mean(deltas)

    def pack(data, units='rank_ic', horizon=10):
        return {key: summary(value, horizon, calendar, units) for key, value in data.items()}

    return {
        'scope': {'data_start': calendar[0], 'data_end': calendar[-1],
                  'calendar_days': len(calendar), 'cutoff': IS_CUTOFF,
                  'eligible_signal_days': len(signals),
                  'maturity': evidence_status.maturity(signals, calendar, IS_CUTOFF, 10),
                  'eligible_dates': sorted(signals), 'ranking_spec': rv.SPEC_SHA,
                  'ranking_eligible_dates': sorted(d for d, rows in rankings.items() if rows),
                  'read_only_query_only': con.execute('PRAGMA query_only').fetchone()[0]},
        'method': {'factor_aggregation': 'equal-weight group IC then equal-weight dates',
                   'tier_aggregation': 'equal-weight stocks within date then equal-weight dates',
                   'net_benchmark': 'leave-one-out group median, before benchmark costs',
                   'net_cost_pp': COST_ROUND_TRIP,
                   'net_caveat': 'hypothetical overlapping fixed-horizon cohorts, no slippage/capacity/portfolio accounting',
                   'ablation': 'retrospective paired date/group unsmoothed rounded composite; not new-strategy OOS',
                   'effective_observations': 'repo heuristic n_days/horizon, not empirically measured independence',
                   'returns': 'current adjusted outcomes; signals and membership are frozen as-seen'},
        'factors': pack(factor), 'factor_group_day_cells': dict(cells),
        'tiers_close_10d': pack(tier, 'percentage_points'),
        'strong_minus_weak': summary(paired_difference(tier['真強'], tier['真弱']), 10, calendar, 'percentage_points'),
        'cohorts_close_10d': pack(cohort, 'percentage_points'),
        'cohort_blocked_minus_pass': summary(paired_difference(cohort['blocked'], cohort['pass']), 10, calendar, 'percentage_points'),
        'ablation_paired': pack(drops), 'ablation_paired_group_day_cells': dict(ablation_paired_cells),
        'med_dip': {'hit': summary(hit, 10, calendar, 'fraction'),
                    'random_baseline': summary(base, 10, calendar, 'fraction'),
                    'hit_minus_baseline': summary(paired_difference(hit, base), 10, calendar, 'fraction'),
                    'cross_group_ic': summary(group_ic, 10, calendar, 'rank_ic'),
                    'excluded_top_tie_dates': group_ties},
        'net_open': net,
        'challenger_paired': pack(rank_delta),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--db', type=Path, default=ROOT / 'data/findmind.db')
    ap.add_argument('--as-of', help='Latest outcome date; does not recreate an older database vintage')
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.resolve() == args.db.resolve():
        ap.error('--out must not overwrite the database')
    with args.db.open('rb') as handle:
        db_sha = hashlib.file_digest(handle, 'sha256').hexdigest()
    con = db_ro.connect(args.db)
    try:
        result = analyze(con, args.as_of)
    finally:
        con.close()
    with args.db.open('rb') as handle:
        after_sha = hashlib.file_digest(handle, 'sha256').hexdigest()
    if after_sha != db_sha:
        raise RuntimeError('Database changed during review; rerun on a stable input')
    result['environment'] = {'python': sys.version, 'platform': platform.platform(),
                             'PYTHONUTF8': os.getenv('PYTHONUTF8'),
                             'PYTHONIOENCODING': os.getenv('PYTHONIOENCODING'),
                             'utf8_mode': sys.flags.utf8_mode,
                             'db_sha256': db_sha, 'db_sha256_unchanged': True}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes((json.dumps(result, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
    print(json.dumps({'written': str(args.out), 'scope': result['scope']}, ensure_ascii=True))


if __name__ == '__main__':
    main()
