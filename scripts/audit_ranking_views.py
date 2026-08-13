#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""唯讀稽核 A/B/C/D 平行視角的結構健康與正式快照進度。

這支工具刻意不計算前瞻績效、不替視角排勝負，也不寫 SQLite。它把兩類問題分開：

1. 目前橫斷面的精確庫存：覆蓋、同分、Pareto 篩選力、peer sensitivity、component 覆蓋。
2. append-only OOS 的操作進度：目前 spec 有幾個完整正式日、幾日已成熟、是否混入舊 spec。

`--require-current-snapshot` 供每日 final pipeline 使用，只把缺表、漏列、JSON 損壞或
當日尚未正式凍結視為 hard error。高 tie／高 Pareto 等是觀察警告，不會阻斷每日資料。
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import statistics
import sys

import db_ro
import ranking_views as rv
import stats_ci


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
VIEW_KEYS = ("champion_pct", "lens_a", "lens_b", "lens_c", "lens_d")
LENS_KEYS = ("lens_a", "lens_b", "lens_c", "lens_d")
COMPONENT_KEYS = {
    "lens_a": ("short", "swing", "trend"),
    "lens_b": ("resilience", "leverage_safety", "heat_safety"),
    "lens_c": ("core", "tdcc", "sbl_relief"),
    "lens_d": ("revenue_3m_yoy", "revenue_accel", "operating_margin",
               "operating_margin_yoy_delta"),
}
COMPONENT_FIELDS = {
    "lens_a": "a_components",
    "lens_b": "b_components",
    "lens_c": "c_components",
    "lens_d": "d_components",
}
PEER_SENSITIVITY_WATCH = 25.0
PARETO_LOW_SELECTIVITY = 0.50
TIE_WATCH_RATE = 0.40


def _table_exists(con, name):
    return bool(con.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)
    ).fetchone())


def _group(row):
    return row.get("grp") or row.get("g")


def _median(values):
    values = [value for value in values if value is not None]
    return round(statistics.median(values), 4) if values else None


def _summary(values):
    values = [value for value in values if value is not None]
    if not values:
        return {"days": 0, "latest": None, "median": None, "min": None, "max": None}
    return {
        "days": len(values),
        "latest": round(values[-1], 4),
        "median": round(statistics.median(values), 4),
        "min": round(min(values), 4),
        "max": round(max(values), 4),
    }


def _correlation(xs, ys):
    """平均秩百分位的 Pearson correlation；在單一族群內等同 tie-aware rank corr。"""
    pairs = [(float(x), float(y)) for x, y in zip(xs, ys)
             if x is not None and y is not None]
    if len(pairs) < 3:
        return None
    x_values, y_values = zip(*pairs)
    x_mean = statistics.mean(x_values)
    y_mean = statistics.mean(y_values)
    x_var = sum((value - x_mean) ** 2 for value in x_values)
    y_var = sum((value - y_mean) ** 2 for value in y_values)
    if x_var == 0 or y_var == 0:
        return None
    covariance = sum(
        (x_value - x_mean) * (y_value - y_mean)
        for x_value, y_value in pairs
    )
    return covariance / (x_var * y_var) ** 0.5


def _jaccard(left, right):
    union = set(left) | set(right)
    return len(set(left) & set(right)) / len(union) if union else None


def _pair_keys():
    for index, left in enumerate(LENS_KEYS):
        for right in LENS_KEYS[index + 1:]:
            yield left, right, f"{left}__{right}"


def formal_structure(day_payloads):
    """正式快照的 exact descriptive history；不提供 SE/t 或績效推論。"""
    days = sorted((date, [dict(row) for row in rows])
                  for date, rows in day_payloads.items())
    rank_corr = collections.defaultdict(list)
    top20_jaccard = collections.defaultdict(list)
    unique_top20 = collections.defaultdict(list)
    tie_rate = collections.defaultdict(list)
    pareto_rate = []
    retention = collections.defaultdict(list)
    previous_top = None

    for _date, rows in days:
        grouped = collections.defaultdict(list)
        for row in rows:
            grouped[_group(row)].append(row)
        top = {
            key: {row.get("stock_id") or row.get("id") for row in rows
                  if row.get(key) is not None and row[key] >= rv.TOP_PCT}
            for key in LENS_KEYS
        }
        for left, right, pair_key in _pair_keys():
            group_correlations = []
            for members in grouped.values():
                correlation = _correlation(
                    [row.get(left) for row in members],
                    [row.get(right) for row in members],
                )
                if correlation is not None:
                    group_correlations.append(correlation)
            rank_corr[pair_key].append(
                statistics.mean(group_correlations) if group_correlations else None
            )
            top20_jaccard[pair_key].append(_jaccard(top[left], top[right]))
        for key in LENS_KEYS:
            other = set().union(*(top[other_key] for other_key in LENS_KEYS
                                  if other_key != key))
            unique_top20[key].append(len(top[key] - other))
            if previous_top is not None:
                retention[key].append(_jaccard(previous_top[key], top[key]))
        health = analyze_rows(rows)
        for key in LENS_KEYS:
            tie_rate[key].append(health["tie_rate"][key])
        pareto_rate.append(health["pareto_rate"])
        previous_top = top

    return {
        "basis": "exact_formal_snapshot_census_no_inference",
        "performance_claim": False,
        "days": len(days),
        "first_date": days[0][0] if days else None,
        "latest_date": days[-1][0] if days else None,
        "pairwise_rank_correlation_equal_group_weight": {
            key: _summary(values) for key, values in sorted(rank_corr.items())
        },
        "pairwise_top20_jaccard": {
            key: _summary(values) for key, values in sorted(top20_jaccard.items())
        },
        "unique_top20_count": {
            key: _summary(values) for key, values in sorted(unique_top20.items())
        },
        "adjacent_snapshot_top20_retention": {
            key: _summary(values) for key, values in sorted(retention.items())
        },
        "tie_rate": {
            key: _summary(values) for key, values in sorted(tie_rate.items())
        },
        "pareto_rate": _summary(pareto_rate),
    }


def analyze_rows(rows):
    """分析一個 payload 的精確橫斷面；所有 tie 都只在正式族群內計算。"""
    rows = [dict(row) for row in rows]
    grouped = collections.defaultdict(list)
    for row in rows:
        grouped[_group(row)].append(row)

    duplicate_ids = sorted(
        stock_id for stock_id, count in collections.Counter(
            row.get("stock_id") or row.get("id") for row in rows
        ).items() if count > 1
    )
    coverage = {key: sum(row.get(key) is not None for row in rows) for key in VIEW_KEYS}
    component_coverage = {}
    for lens, keys in COMPONENT_KEYS.items():
        field = COMPONENT_FIELDS[lens]
        component_coverage[lens] = {
            key: sum((row.get(field) or {}).get(key) is not None for row in rows)
            for key in keys
        }

    tie_exposed = {key: 0 for key in VIEW_KEYS}
    unique_shares = {key: [] for key in VIEW_KEYS}
    group_rows = []
    for grp, members in sorted(grouped.items(), key=lambda item: str(item[0])):
        group_ties = {}
        group_unique = {}
        for key in VIEW_KEYS:
            counts = collections.Counter(
                row.get(key) for row in members if row.get(key) is not None
            )
            tied = sum(count for count in counts.values() if count > 1)
            usable = sum(counts.values())
            share = len(counts) / usable if usable else None
            tie_exposed[key] += tied
            unique_shares[key].append(share)
            group_ties[key] = tied
            group_unique[key] = round(share, 4) if share is not None else None
        group_rows.append({
            "grp": grp,
            "stocks": len(members),
            "coverage": {
                key: sum(row.get(key) is not None for row in members) for key in VIEW_KEYS
            },
            "tie_exposed": group_ties,
            "unique_share": group_unique,
            "consensus2": sum((row.get("consensus_count") or 0) >= 2 for row in members),
            "pareto": sum(row.get("pareto") is True for row in members),
            "peer_sensitivity_ge_25": sum(
                row.get("peer_sensitivity") is not None
                and row["peer_sensitivity"] >= PEER_SENSITIVITY_WATCH
                for row in members
            ),
        })

    stock_count = len(rows)
    pareto = sum(row.get("pareto") is True for row in rows)
    consensus2 = sum((row.get("consensus_count") or 0) >= 2 for row in rows)
    peer_watch = sum(
        row.get("peer_sensitivity") is not None
        and row["peer_sensitivity"] >= PEER_SENSITIVITY_WATCH
        for row in rows
    )
    return {
        "stocks": stock_count,
        "groups": len(grouped),
        "duplicate_stock_ids": duplicate_ids,
        "coverage": coverage,
        "component_coverage": component_coverage,
        "role_rank_coverage": sum(row.get("role_pct") is not None for row in rows),
        "tie_exposed": tie_exposed,
        "tie_rate": {
            key: round(tie_exposed[key] / stock_count, 4) if stock_count else None
            for key in VIEW_KEYS
        },
        "median_unique_share_by_group": {
            key: _median(unique_shares[key]) for key in VIEW_KEYS
        },
        "top_20": {
            key: sum(row.get(key) is not None and row[key] >= rv.TOP_PCT for row in rows)
            for key in VIEW_KEYS
        },
        "consensus2": consensus2,
        "consensus2_rate": round(consensus2 / stock_count, 4) if stock_count else None,
        "pareto": pareto,
        "pareto_rate": round(pareto / stock_count, 4) if stock_count else None,
        "peer_sensitivity_ge_25": peer_watch,
        "peer_sensitivity_ge_25_rate": (
            round(peer_watch / stock_count, 4) if stock_count else None
        ),
        "group_detail": group_rows,
    }


def canonical_official_runs(con):
    """與 validate.py 相同：每個資料日只認 captured_at 最早的正式發布。"""
    if not _table_exists(con, "oos_snapshot_runs"):
        return []
    out = {}
    for row in con.execute(
        """SELECT snapshot_id,data_date,captured_at,stock_count
           FROM oos_snapshot_runs WHERE is_official=1
           ORDER BY data_date,captured_at,snapshot_id"""
    ):
        out.setdefault(row["data_date"], dict(row))
    return [out[date] for date in sorted(out)]


def formal_progress(con, spec_sha, *, fwd=10):
    runs = canonical_official_runs(con)
    have_views = _table_exists(con, "oos_ranking_view_snapshots")
    specs_seen = set()
    current_dates = []
    historical_other_spec_days = 0
    invalid_runs = []
    parsed_rows = 0
    latest_snapshot_health = None
    current_payloads_by_date = {}

    if have_views:
        for run in runs:
            rows = list(con.execute(
                """SELECT spec_sha,payload_json FROM oos_ranking_view_snapshots
                   WHERE snapshot_id=? ORDER BY stock_id""", (run["snapshot_id"],)
            ))
            specs = {row["spec_sha"] for row in rows}
            specs_seen.update(specs)
            payloads = []
            json_error = False
            for row in rows:
                try:
                    payloads.append(json.loads(row["payload_json"]))
                except (TypeError, json.JSONDecodeError):
                    json_error = True
            structurally_complete = (
                len(rows) == run["stock_count"]
                and len(specs) == 1
                and not json_error
                and len(payloads) == len(rows)
            )
            if structurally_complete and specs == {spec_sha}:
                current_dates.append(run["data_date"])
                parsed_rows += len(payloads)
                latest_snapshot_health = analyze_rows(payloads)
                current_payloads_by_date[run["data_date"]] = payloads
            elif structurally_complete:
                historical_other_spec_days += 1
            elif rows:
                invalid_runs.append({
                    "date": run["data_date"],
                    "snapshot_id": run["snapshot_id"],
                    "expected_rows": run["stock_count"],
                    "actual_rows": len(rows),
                    "specs": sorted(specs),
                    "json_error": json_error,
                })

    price_dates = [row[0] for row in con.execute(
        "SELECT DISTINCT date FROM price_adj ORDER BY date"
    )] if _table_exists(con, "price_adj") else []
    date_index = {date: index for index, date in enumerate(price_dates)}
    mature_dates = [
        date for date in current_dates
        if date in date_index and date_index[date] + fwd < len(price_dates)
    ]
    eff_obs = stats_ci.effective_obs(len(mature_dates), fwd)
    if not current_dates:
        phase = "await_first_snapshot"
    elif len(current_dates) < 10:
        phase = "collecting_operational_history"
    elif not mature_dates:
        phase = "structural_review_only"
    elif eff_obs < 10:
        phase = "outcome_diagnostics_accumulating"
    else:
        phase = "challenger_gate_readable_in_validate"
    return {
        "ranking_snapshot_table": have_views,
        "canonical_official_days": len(runs),
        "current_spec_days": len(current_dates),
        "current_spec_first_date": current_dates[0] if current_dates else None,
        "current_spec_latest_date": current_dates[-1] if current_dates else None,
        "mature_10d_days": len(mature_dates),
        "effective_independent_obs_approx": round(eff_obs, 2),
        "phase": phase,
        "specs_seen": sorted(specs_seen),
        "historical_other_spec_days": historical_other_spec_days,
        "invalid_runs": invalid_runs,
        "parsed_rows": parsed_rows,
        "latest_snapshot_health": latest_snapshot_health,
        "structural_history": formal_structure(current_payloads_by_date),
    }


def build_audit(con, *, date=None, fwd=10, require_current_snapshot=False):
    date = date or con.execute("SELECT MAX(date) FROM daily_scores").fetchone()[0]
    hard_errors = []
    warnings = []
    payload = rv.build_from_db(
        con, date, roles_path=rv.ROLES_CONFIG, strict_roles=True
    ) if date else None
    if not payload:
        hard_errors.append("current_payload_missing")
        current = analyze_rows([])
    else:
        current = analyze_rows(payload["rows"])

    expected = con.execute(
        """SELECT COUNT(*) FROM daily_scores s
           JOIN daily_metrics m USING(date,stock_id)
           JOIN universe u USING(stock_id) WHERE s.date=?""", (date,)
    ).fetchone()[0] if date else 0
    if current["stocks"] != expected:
        hard_errors.append(
            f"current_row_count_mismatch:{current['stocks']}!={expected}"
        )
    if current["duplicate_stock_ids"]:
        hard_errors.append("duplicate_stock_ids")
    if con.execute("PRAGMA query_only").fetchone()[0] != 1:
        hard_errors.append("query_only_not_enforced")

    progress = formal_progress(con, rv.SPEC_SHA, fwd=fwd)
    if require_current_snapshot and progress["current_spec_latest_date"] != date:
        hard_errors.append(
            "current_formal_snapshot_missing:"
            f"data_date={date},latest={progress['current_spec_latest_date']}"
        )
    if progress["invalid_runs"]:
        hard_errors.append("invalid_or_mixed_spec_snapshot")

    stock_count = current["stocks"] or 1
    for key in ("lens_a", "lens_b", "lens_c", "lens_d"):
        if current["coverage"].get(key, 0) < current["stocks"]:
            warnings.append(
                f"partial_coverage:{key}={current['coverage'].get(key, 0)}/{current['stocks']}"
            )
        if (current["tie_rate"].get(key) or 0) >= TIE_WATCH_RATE:
            warnings.append(
                f"high_tie_current_census:{key}={current['tie_exposed'][key]}/{current['stocks']}"
            )
    if (current["pareto_rate"] or 0) >= PARETO_LOW_SELECTIVITY:
        warnings.append(
            f"pareto_low_selectivity_current_census:{current['pareto']}/{current['stocks']}"
        )
    if current["peer_sensitivity_ge_25"] / stock_count >= 1 / 3:
        warnings.append(
            "peer_sensitivity_watch_current_census:"
            f"{current['peer_sensitivity_ge_25']}/{current['stocks']}"
        )

    return {
        "status": "fail" if hard_errors else "ok",
        "basis": "current_restated_census_plus_append_only_progress",
        "performance_claim": False,
        "date": date,
        "spec_sha": rv.SPEC_SHA,
        "expected_stocks": expected,
        "current": current,
        "fundamental": payload.get("fundamental") if payload else None,
        "formal_progress": progress,
        "hard_errors": hard_errors,
        "warnings": warnings,
    }


def compact(audit):
    current = audit["current"]
    progress = audit["formal_progress"]
    return {
        "status": audit["status"],
        "date": audit["date"],
        "spec_sha": audit["spec_sha"],
        "stocks": current["stocks"],
        "coverage": current["coverage"],
        "tie_exposed": current["tie_exposed"],
        "consensus2": current["consensus2"],
        "pareto": current["pareto"],
        "peer_sensitivity_ge_25": current["peer_sensitivity_ge_25"],
        "formal_days": progress["current_spec_days"],
        "structural_days": progress["structural_history"]["days"],
        "mature_10d_days": progress["mature_10d_days"],
        "phase": progress["phase"],
        "hard_errors": audit["hard_errors"],
        "warnings": audit["warnings"],
    }


def write_json(path, payload):
    raw = (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )
    if path:
        with open(path, "wb") as handle:
            handle.write(raw)
    else:
        sys.stdout.buffer.write(raw)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="唯讀稽核平行視角的結構健康與 append-only 進度"
    )
    parser.add_argument("--db", default=DB)
    parser.add_argument("--date", help="預設 daily_scores 最新資料日")
    parser.add_argument("--fwd", type=int, default=10)
    parser.add_argument("--require-current-snapshot", action="store_true")
    parser.add_argument("--compact", action="store_true")
    parser.add_argument("--json-out", help="直接以 UTF-8 LF 寫檔；勿用 shell 重導向")
    args = parser.parse_args(argv)
    if args.fwd <= 0:
        parser.error("--fwd 必須為正整數")
    con = db_ro.connect(args.db)
    try:
        audit = build_audit(
            con, date=args.date, fwd=args.fwd,
            require_current_snapshot=args.require_current_snapshot,
        )
    finally:
        con.close()
    write_json(args.json_out, compact(audit) if args.compact else audit)
    return 1 if audit["hard_errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
