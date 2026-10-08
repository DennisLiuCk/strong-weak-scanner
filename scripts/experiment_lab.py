#!/usr/bin/env python3
"""Short-cycle, read-only strategy experiments. Historical replay is NOT OOS.

No formal weights, tiers, database, or archive are written. All candidates and
looks remain visible. Source changes require a new registration before forward
results can be called prospective. Pure stdlib; reports are UTF-8 with LF.
"""
import argparse
from collections import Counter, defaultdict, deque
from contextlib import closing
import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import statistics as st
import sys

import db_ro
import evidence_status
import score
import stats_ci as sci
from signal_structure import spearman

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config/experiment_lab.json"
REGISTRY_DIR = ROOT / "config/experiment_registry"
SOURCE_FILES = ("scripts/experiment_lab.py", "scripts/score.py",
                "scripts/signal_structure.py", "scripts/stats_ci.py",
                "scripts/evidence_status.py", "scripts/db_ro.py")
FACTORS = ("price", "resil", "vol", "foreign", "trust", "dip", "margin")
REQUIRED = ("rs20", "down_rs20", "vol_ratio60", "fpct_chg20", "trust5_pct",
            "ret20", "ret1", "dist_hi20", "margin_util_pct")
DATASET_LABELS = {"replay": "歷史重播（現行母體與修訂後資料）",
                  "frozen_replay": "舊快照重播（當時輸入，新設計策略）",
                  "forward": "登錄後前瞻實驗"}


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
                       separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def load_config(path=CONFIG_PATH):
    cfg = json.loads(Path(path).read_text(encoding="utf-8"))
    ids = [s["id"] for s in cfg["strategies"]]
    if not ids or ids[0] != "BASE" or len(ids) != len(set(ids)):
        raise ValueError("strategies must start with unique BASE")
    if cfg["primary_horizon"] not in cfg["horizons"] or min(cfg["horizons"]) < 1:
        raise ValueError("invalid horizons")
    if cfg["gap_days"] < max(cfg["horizons"]) + 1:
        raise ValueError("gap must exclude all next-open outcome windows")
    for s in cfg["strategies"]:
        if s["smooth"] < 1 or ("weights" in s) == ("raw_rank" in s):
            raise ValueError("each strategy needs positive smoothing and exactly one rule")
        if any(k not in FACTORS for k in s.get("weights", {})):
            raise ValueError("unknown factor")
    registered = dt.datetime.fromisoformat(cfg["registered_at"])
    if registered.tzinfo is None:
        raise ValueError("registration must include timezone")
    return cfg


def source_fingerprint(cfg):
    sources = {name: hashlib.sha256((ROOT / name).read_text(encoding="utf-8")
                                   .replace("\r\n", "\n").encode("utf-8")).hexdigest()
               for name in SOURCE_FILES}
    return {"config_sha256": digest(cfg), "sources": sources,
            "spec_sha256": digest({"config": cfg, "sources": sources})}


def check_registration(cfg, registry_dir=REGISTRY_DIR):
    expected = source_fingerprint(cfg)
    path = Path(registry_dir) / (cfg["protocol"] + ".json")
    stored = json.loads(path.read_text(encoding="utf-8"))
    if stored != {"protocol": cfg["protocol"], "registered_at": cfg["registered_at"], "config": cfg, **expected}:
        raise ValueError("lab registration/source drift; register a NEW protocol, keep old evidence")
    return expected


def register(cfg, config_path=CONFIG_PATH, registry_dir=REGISTRY_DIR):
    """Explicit new-round operation. Always timestamp NOW, never backdate OOS."""
    target = Path(registry_dir) / (cfg["protocol"] + ".json")
    if target.exists():
        raise ValueError("protocol already registered; choose a new ID and preserve its old record")
    cfg = {**cfg, "registered_at": dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).isoformat(timespec="seconds")}
    receipt = {"protocol": cfg["protocol"], "registered_at": cfg["registered_at"], "config": cfg,
               **source_fingerprint(cfg)}
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("xb") as stream:
        stream.write(canonical(receipt))
    Path(config_path).write_bytes((json.dumps(cfg, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    return receipt


def finite(value):
    return value is not None and math.isfinite(value)


def load_inputs(con, as_of=None):
    calendar = [r[0] for r in con.execute("SELECT date FROM market ORDER BY date")
                if as_of is None or r[0] <= as_of]
    cutoff = calendar[-1] if calendar else ""
    rows = [dict(r) for r in con.execute("""SELECT m.*, u.grp FROM daily_metrics m
               JOIN universe u USING(stock_id) WHERE m.date<=? ORDER BY m.date,m.stock_id""", (cutoff,))]
    first_runs = evidence_status.first_official_runs(con)
    frozen, runs, rejected = [], {}, {}
    for day, run in first_runs.items():
        if day not in calendar:
            continue
        if not evidence_status.oos_eligible(run):
            rejected[day] = "first_official_ineligible"
            continue
        items = [dict(r) for r in con.execute(
            "SELECT * FROM oos_signal_snapshots WHERE snapshot_id=? ORDER BY stock_id",
            (run["snapshot_id"],))]
        if not items or len(items) != run["stock_count"]:
            rejected[day] = "empty_or_incomplete_first_official"
            continue
        frozen.extend(items)
        runs[day] = dict(run)
    opening = {}
    for r in con.execute("""SELECT p.date,p.stock_id,p.open,p.close,a.close AS adjusted
                FROM price p JOIN price_adj a USING(date,stock_id) WHERE p.date<=?""", (cutoff,)):
        if all(finite(r[k]) and r[k] > 0 for k in ("open", "close", "adjusted")):
            opening[r["date"], r["stock_id"]] = r["open"] * r["adjusted"] / r["close"]
    return calendar, rows, frozen, runs, rejected, opening


def build_signals(rows, cfg, calendar=None):
    """Chronological prefix-only scores. Rank scope matches formal scorer.

    A shared complete-feature population makes candidate comparisons fair.
    Incomplete current or smoothing-window features are excluded, never zeroed
    into an apparently valid experiment. BASE itself equals formal composite_s.
    """
    rows = sorted(rows, key=lambda r: (r["date"], r["stock_id"]))
    positions = {d: i for i, d in enumerate(calendar or sorted({r["date"] for r in rows}))}
    if len({(r["date"], r["stock_id"]) for r in rows}) != len(rows):
        raise ValueError("duplicate stock/date")
    calculated = {(r[0], r[1]): r for r in score.calculate_scores(rows)}
    grouped = defaultdict(list)
    for row in rows:
        grouped[row["date"], row["grp"]].append(row)
    history = defaultdict(deque)
    validity = defaultdict(lambda: deque(maxlen=max(s["smooth"] for s in cfg["strategies"])))
    previous = {}
    signals, excluded = {}, Counter()
    for (day, grp), items in sorted(grouped.items()):
        raw_ranks = {}
        for field in {s["raw_rank"] for s in cfg["strategies"] if "raw_rank" in s}:
            valid = [r for r in items if finite(r.get(field))]
            rr = score.average_ranks([r[field] for r in valid])
            raw_ranks[field] = {r["stock_id"]: (2 * (rank - 1) / (len(valid) - 1) - 1)
                                for r, rank in zip(valid, rr)} if len(valid) > 1 else {}
        for row in items:
            sid = row["stock_id"]
            if sid in previous and positions[day] != previous[sid] + 1:
                validity[sid].clear()
            previous[sid] = positions[day]
            complete = all(finite(row.get(k)) for k in REQUIRED) and (
                finite(row.get("margin_chg10")) or finite(row.get("margin_chg5")))
            validity[sid].append(complete)
            factors = dict(zip(FACTORS, calculated[day, sid][2:9]))
            values = {}
            for spec in cfg["strategies"]:
                if "weights" in spec:
                    raw = round(sum(w * factors[k] for k, w in spec["weights"].items()), 2)
                else:
                    raw = raw_ranks[spec["raw_rank"]].get(sid)
                    if raw is not None:
                        raw *= spec["direction"]
                hist = history[sid, spec["id"]]
                hist.append(raw)
                while len(hist) > spec["smooth"]:
                    hist.popleft()
                values[spec["id"]] = (round(st.mean(hist), 2) if hist and all(finite(x) for x in hist)
                                      else None)
            valid_history = len(validity[sid]) == validity[sid].maxlen and all(validity[sid])
            if not valid_history or not all(finite(v) for v in values.values()):
                excluded["missing_feature_or_smoothing_warmup"] += 1
                continue
            if values["BASE"] != calculated[day, sid][10]:
                raise ValueError("BASE differs from formal scorer; update protocol")
            signals.setdefault(day, {}).setdefault(grp, {})[sid] = values
    return signals, dict(excluded)


def tails(values):
    """Quarter tails by midrank, never tie-break with stock IDs."""
    ids = sorted(values)
    if len(ids) < 2 or len(set(values.values())) < 2:
        return set(), set()
    ranks = score.average_ranks([values[s] for s in ids])
    top = {s for s, rank in zip(ids, ranks) if (rank - 1) / (len(ids) - 1) >= .75}
    bottom = {s for s, rank in zip(ids, ranks) if (rank - 1) / (len(ids) - 1) <= .25}
    return top, bottom


def pack(series, horizon, calendar):
    days = sorted(series)
    result = sci.summarize([series[d] for d in days], horizon, days, calendar)
    if result is None:
        return None
    result.update(first=days[0], last=days[-1])
    # A minimum lag 5 also probes persistence for F1; F1 is not automatically iid.
    result["lag_sensitivity"] = {}
    for lag in sorted({horizon - 1, max(5, 2 * horizon - 1), max(10, 3 * horizon - 1)}):
        se = sci.nw_se([series[d] for d in days], lag, dates_used=days, all_dates=calendar) if len(days) >= 3 * (lag + 1) else None
        result["lag_sensitivity"][str(lag)] = {"se": se, "t": result["mean"] / se if se else None}
    return result


def structural_report(signals, calendar, cfg, allowed):
    """Outcome-free list differences; Jaccard distance is NOT portfolio turnover."""
    positions = {d: i for i, d in enumerate(calendar)}
    prior = {}
    series = {s['id']: defaultdict(dict) for s in cfg['strategies']}
    for day in sorted(set(allowed) & signals.keys()):
        values = {s['id']: defaultdict(list) for s in cfg['strategies']}
        for group, population in signals[day].items():
            if len(population) < cfg['min_group']:
                continue
            base_top, _ = tails({s: r['BASE'] for s, r in population.items()})
            for spec in cfg['strategies']:
                candidate=spec['id']
                ranks={s: r[candidate] for s, r in population.items()}
                top, _ = tails(ranks)
                values[candidate]['tie_fraction'].append(1-len(set(ranks.values()))/len(ranks))
                if top and base_top:
                    values[candidate]['top_jaccard'].append(len(top & base_top)/len(top | base_top))
                previous=prior.get((candidate,group))
                if previous and previous[0]+1==positions[day] and top and previous[1]:
                    old=previous[1]
                    values[candidate]['list_change'].append(1-len(top & old)/len(top | old))
                prior[candidate,group]=(positions[day],top)
        for candidate, metrics in values.items():
            for metric, items in metrics.items():
                if items:
                    series[candidate][metric][day]=st.mean(items)
    return {candidate:{'summary':{k:pack(v,1,calendar) for k,v in metrics.items()},
                       'daily':dict(metrics)} for candidate,metrics in series.items()}


def evaluate(signals, calendar, opening, cfg, horizon, eligible_days=None):
    allowed = set(signals if eligible_days is None else eligible_days)
    position = {d: i for i, d in enumerate(calendar)}
    ids = [s["id"] for s in cfg["strategies"]]
    cell = {sid: defaultdict(dict) for sid in ids}
    coverage = {sid: Counter() for sid in ids}
    for day in sorted(signals):
        if day not in allowed or day not in position:
            continue
        pos = position[day]
        if pos + 1 + horizon >= len(calendar):
            continue
        entry, exit_day = calendar[pos + 1], calendar[pos + 1 + horizon]
        for grp, population in sorted(signals[day].items()):
            stocks = sorted(population)
            reason = None
            if len(stocks) < cfg["min_group"]:
                reason = "small_group"
            rr = {}
            for stock in stocks:
                a, b = opening.get((entry, stock)), opening.get((exit_day, stock))
                if finite(a) and finite(b) and a > 0 and b > 0:
                    rr[stock] = b / a - 1
            if len(rr) != len(stocks):
                reason = "missing_entry_or_exit_entire_group_excluded"
            for candidate in ids:
                coverage[candidate]["attempted_group_days"] += 1
                if reason:
                    coverage[candidate][reason] += 1
                    continue
                base = {s: population[s]["BASE"] for s in stocks}
                alternative = {s: population[s][candidate] for s in stocks}
                future = [rr[s] for s in stocks]
                a = spearman(list(base.values()), future)
                b = spearman(list(alternative.values()), future)
                if a is None or b is None:
                    coverage[candidate]["constant_leg_or_outcome"] += 1
                    continue
                top, bottom = tails(alternative)
                base_top, _ = tails(base)
                row = {"ic": b, "base_ic": a, "delta_ic": b - a,
                       "n_stocks": len(stocks)}
                if top and bottom:
                    row["spread_pp"] = 100 * (st.mean(rr[s] for s in top) - st.mean(rr[s] for s in bottom))
                    row["top_excess_gross_pp"] = 100 * (st.mean(rr[s] for s in top) - st.mean(rr.values()))
                    row["top_excess_cost_pp"] = row["top_excess_gross_pp"] - cfg["cost_pp"]
                if top and base_top:
                    row["top_jaccard"] = len(top & base_top) / len(top | base_top)
                cell[candidate][day][grp] = row
                coverage[candidate]["paired_group_days"] += 1
                coverage[candidate]["stock_days_coverage_only"] += len(stocks)
    results = {}
    for candidate in ids:
        series = defaultdict(dict)
        for day, groups in cell[candidate].items():
            for metric in {k for r in groups.values() for k in r if k != "n_stocks"}:
                v = [r[metric] for r in groups.values() if metric in r]
                if v:
                    series[metric][day] = st.mean(v)
        delta = series["delta_ic"]
        leave_group_out = {}
        for excluded in sorted({g for groups in cell[candidate].values() for g in groups}):
            daily = {d: st.mean(r["delta_ic"] for g, r in groups.items() if g != excluded)
                     for d, groups in cell[candidate].items() if any(g != excluded for g in groups)}
            leave_group_out[excluded] = pack(daily, horizon, calendar)
        offsets = {str(offset): pack({d: v for d, v in delta.items()
                    if position[d] % horizon == offset}, 1, calendar) for offset in range(horizon)}
        results[candidate] = {"summary": {k: pack(v, horizon, calendar) for k, v in series.items()},
            "daily": dict(series), "coverage": dict(coverage[candidate]),
            "leave_one_group_out": leave_group_out, "nonoverlap_offsets": offsets,
            "cells": dict(cell[candidate])}
    return results


def walk_forward(results, calendar, cfg):
    """Purged expanding training window; fixed candidate set, no random splitting.

    This is a replay of a selection process, not genuinely untouched market OOS.
    Training labels must have ended before each test block's first signal.
    """
    start = cfg["warmup_days"] + cfg["train_days"] + cfg["gap_days"]
    horizon = cfg["primary_horizon"]
    folds = []
    combined = {}
    for i in range(start, len(calendar) - horizon - 1, cfg["test_days"]):
        test_days = calendar[i:i + cfg["test_days"]]
        if len(test_days) < cfg["test_days"] or i + cfg["test_days"] + horizon >= len(calendar):
            break
        train_days = calendar[cfg["warmup_days"]:i - cfg["gap_days"]]
        means, train_summary = {}, {}
        for candidate, result in results.items():
            delta = result["daily"].get("delta_ic", {})
            vals = {d: delta[d] for d in train_days if d in delta}
            train_summary[candidate] = pack(vals, horizon, calendar)
            if len(vals) >= cfg["train_days"]:
                means[candidate] = st.mean(vals.values())
        # A tie chooses BASE first, then stable protocol order; never look at test outcomes.
        selected = max(means, key=lambda k: (means[k], k == "BASE", -list(results).index(k))) if means else None
        fold_results = {c: pack({d: v for d, v in r["daily"].get("delta_ic", {}).items()
                               if d in test_days}, horizon, calendar) for c, r in results.items()}
        if selected:
            combined.update({d: v for d, v in results[selected]["daily"]["delta_ic"].items() if d in test_days})
        folds.append({"train_first": train_days[0], "train_last": train_days[-1],
                      "train_last_outcome": calendar[i - cfg["gap_days"] - 1 + horizon + 1],
                      "test_first": test_days[0], "test_last": test_days[-1],
                      "gap_days": cfg["gap_days"], "selected": selected,
                      "train": train_summary, "all_test_candidates": fold_results})
    return {"folds": folds, "selected_process_delta": pack(combined, horizon, calendar),
            "label": "歷史選擇流程重播；策略設計已看過歷史，非真正未見 OOS"}


def negative_controls(signals, calendar, opening, cfg, allowed):
    """Fixed per-group ticker permutations across time, diagnostic, not p-values."""
    members = defaultdict(set)
    for day in signals.values():
        for grp, stocks in day.items():
            members[grp].update(stocks)
    output = []
    small_cfg = {**cfg, "strategies": [cfg["strategies"][0], {"id": "SHUFFLE"}]}
    for seed in cfg["shuffle_seeds"]:
        mapping = {}
        for grp, stocks in sorted(members.items()):
            ordered = sorted(stocks)
            shuffled = sorted(stocks, key=lambda s: hashlib.sha256(f"{seed}|{grp}|{s}".encode()).digest())
            mapping[grp] = dict(zip(ordered, shuffled))
        fake = {}
        for day, groups in signals.items():
            if day not in allowed:
                continue
            for grp, stocks in groups.items():
                # Membership changes cannot silently substitute a different permutation.
                if not all(mapping[grp][s] in stocks for s in stocks):
                    continue
                fake.setdefault(day, {})[grp] = {s: {"BASE": row["BASE"],
                    "SHUFFLE": stocks[mapping[grp][s]]["BASE"]} for s, row in stocks.items()}
        result = evaluate(fake, calendar, opening, small_cfg, cfg["primary_horizon"], allowed)["SHUFFLE"]
        output.append({"seed": seed, "ic": result["summary"].get("ic"),
                       "coverage": result["coverage"]})
    return {"kind": "固定族群內 ticker 置換；保留分數時間路徑，非交換性保證或多重檢定 p 值",
            "runs": output}


def lab_action(series, cfg):
    """Resource-allocation heuristic for experiments; not a significance test."""
    days = sorted(series)
    if len(days) < 5:
        return "collect", "尚未達 5 個成熟日；先累積"
    if len(days) < 10:
        return "inspect", "先看缺值、名單差異與程式；不分勝負"
    first = [series[d] for d in days[:min(20, len(days))]]
    if st.mean(first) <= cfg["redesign_delta_ic"]:
        return "redesign", "探索差異偏負；下一輪優先改機制或停止此候選"
    if len(days) >= 20 and st.mean(first) >= cfg["practical_delta_ic"] and all(
            st.mean(first[i:i + 10]) > 0 for i in (0, 10)):
        return "retain", "保留到下一輪實驗；不是證明有效或正式升格"
    return "simplify_or_extend", "未見預設的實用差異；可簡化、換機制或另開一輪"


def fixed_looks(result, calendar, cfg):
    series = result["daily"].get("delta_ic", {})
    days = sorted(series)
    output = []
    for n in cfg["looks"]:
        subset = {d: series[d] for d in days[:n]}
        ready = len(days) >= n
        action, reason = lab_action(subset, cfg) if ready else ("pending", "尚未成熟")
        output.append({"n": n, "ready": ready, "remaining": max(0, n - len(days)),
                       "summary": pack(subset, cfg["primary_horizon"], calendar) if ready else None,
                       "daily": subset if ready else {}, "action": action, "reason": reason})
    return output


def freeze_reviews(path, report, calendar):
    """First-N forward inputs/outcomes are immutable; changed history hard-fails."""
    folder = Path(path) / report["protocol"]
    active = set()
    for candidate, looks in report["forward_looks"].items():
        if candidate == "BASE":
            continue
        for look in looks:
            if not look["ready"]:
                continue
            dates = sorted(look["daily"])
            last_pos = calendar.index(dates[-1]) + report["config"]["primary_horizon"] + 1
            body = {"protocol": report["protocol"], "spec": report["fingerprint"],
                    "candidate": candidate, "look": look,
                    "calendar": calendar[:last_pos + 1],
                    "input_snapshots": {d: r for d, r in report["snapshot_receipts"].items() if d <= dates[-1]},
                    "paired_cells": {d: report["datasets"]["forward"]["horizons"][str(report["config"]["primary_horizon"])]
                                     [candidate]["cells"][d] for d in dates}}
            payload = {"body": body, "sha256": digest(body)}
            file = folder / f"{candidate}-{look['n']:03d}.json"
            active.add(file.name)
            if file.exists():
                if json.loads(file.read_text(encoding="utf-8")) != json.loads(canonical(payload)):
                    raise ValueError(f"fixed lab review drift: {file.name}; do not overwrite")
            else:
                folder.mkdir(parents=True, exist_ok=True)
                with file.open("xb") as stream:
                    stream.write(canonical(payload))
    if folder.exists() and {p.name for p in folder.glob("*.json")} - active:
        raise ValueError("previously mature lab review disappeared")


def forward_dates(runs, cfg):
    registration = dt.datetime.fromisoformat(cfg["registered_at"])
    selected = []
    for day, run in runs.items():
        captured = dt.datetime.fromisoformat(run["captured_at"])
        quality = json.loads(run["quality_json"])
        # New captures must explicitly attest timeliness, never rely on legacy defaults.
        if (day >= registration.date().isoformat() and captured >= registration
                and quality.get("oos_eligible") is True):
            selected.append(day)
    return sorted(selected)


def analyze(con, cfg, fingerprint, as_of=None):
    calendar, rows, frozen, runs, rejected, opening = load_inputs(con, as_of)
    restated, restated_excluded = build_signals(rows, cfg, calendar)
    observed, observed_excluded = build_signals(frozen, cfg, calendar)
    forward = forward_dates(runs, cfg)
    replay_days = calendar[cfg["warmup_days"]:]
    registration_day = dt.datetime.fromisoformat(cfg["registered_at"]).date().isoformat()
    datasets = {}
    definitions = (("replay", restated, replay_days),
                   ("frozen_replay", observed, [d for d in observed if d < registration_day]),
                   ("forward", observed, forward))
    for name, signals, allowed in definitions:
        datasets[name] = {"label": DATASET_LABELS[name], "eligible_signal_dates": sorted(allowed),
            "structure": structural_report(signals, calendar, cfg, allowed),
            "horizons": {str(h): evaluate(signals, calendar, opening, cfg, h, allowed) for h in cfg["horizons"]}}
    primary = str(cfg["primary_horizon"])
    report = {"protocol": cfg["protocol"], "as_of": calendar[-1] if calendar else None,
              "config": cfg, "fingerprint": fingerprint, "calendar": calendar,
              "db_query_only": con.execute("PRAGMA query_only").fetchone()[0],
              "datasets": datasets, "input_exclusions": {"replay": restated_excluded,
              "frozen": observed_excluded, "first_official": rejected},
              "walk_forward": walk_forward(datasets["replay"]["horizons"][primary], calendar, cfg),
              "negative_controls": negative_controls(restated, calendar, opening, cfg, set(replay_days)),
              "forward_looks": {c: fixed_looks(r, calendar, cfg) for c, r in datasets["forward"]["horizons"][primary].items()},
              "snapshot_receipts": {d: {"snapshot_id": r["snapshot_id"], "captured_at": r["captured_at"],
                  "content_hash": r["content_hash"], "actual_rows_sha256": digest([x for x in frozen if x["date"] == d])}
                  for d, r in sorted(runs.items())},
              "automatic_production_change": False,
              "limitations": ["Short horizons test a different question; not a shortcut to proving F10 alpha.",
                "Current-universe/current-vintage replay has survivorship, revision and design-selection bias.",
                "Old as-seen inputs replayed with new designs are not new-strategy OOS.",
                "n/F is a heuristic overlap scale, not measured independent observations.",
                "Daily group-equal cohorts overlap; no portfolio NAV, turnover costs, fills, slippage or capacity model.",
                "Missing future price excludes the entire group; exclusions can still be informative selection.",
                "Five/ten/twenty-day actions allocate experiment time, not significance or trading permission."]}
    return report


def public_report(report, *, browser=False):
    """Keep daily audit data in JSON, avoid duplicating large cells in artifacts."""
    trimmed = {k: v for k, v in report.items() if k not in ("snapshot_receipts",)}
    trimmed["snapshot_receipts"] = report["snapshot_receipts"] if not browser else {}
    trimmed["datasets"] = {}
    for name, dataset in report["datasets"].items():
        trimmed["datasets"][name] = {**dataset, "horizons": {
            h: {s: {k: v for k, v in result.items()
                    if k != "cells" and (not browser or k != "daily")}
                for s, result in candidates.items()}
            for h, candidates in dataset["horizons"].items()}}
    return trimmed


def render_html(report):
    payload = json.dumps(public_report(report, browser=True), ensure_ascii=False,
                         allow_nan=False).replace("<", "\\u003c")
    return """<!doctype html><html lang="zh-Hant"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>短週期策略實驗室</title>
<style>body{font:16px/1.65 system-ui,sans-serif;background:#f4f6fa;color:#16243b;margin:0}main{max-width:1180px;margin:auto;padding:32px 22px}h1{font-size:32px;margin:8px 0}h2{margin-top:32px}a{color:#07599f}section,.card{background:white;border:1px solid #dce3ed;border-radius:12px;padding:20px;margin:18px 0}.muted{color:#526477}.badge{display:inline-block;background:#e4eef9;padding:3px 10px;border-radius:30px;font-size:13px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(205px,1fr));gap:14px}.grid .card{margin:0}label{display:inline-flex;gap:10px;align-items:center;margin:8px 22px 8px 0}select{font:inherit;padding:8px;border:1px solid #9aabc0;border-radius:6px}.scroll{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:14px}th,td{text-align:left;border-bottom:1px solid #e0e6ef;padding:12px 10px;vertical-align:top}th{background:#edf2f9;white-space:nowrap}.number{white-space:nowrap;font-variant-numeric:tabular-nums}.good{color:#136542}.warn{color:#943d13}summary{cursor:pointer;font-weight:600}code{font-size:13px}footer{margin:25px 0;color:#526477}button{font:inherit}small{font-size:12px}</style>
<main><a href="../index.html">← 汰弱留強</a><p class="badge">研究用實驗 · 可快速迭代</p>
<h1>先得到回饋，再決定下一輪</h1><p>現在可用歷史重播找出值得繼續研究的方向；前瞻實驗在 5／10／20 個成熟日檢視。主要目標是學習與簡化，不用等到 2027 年才動手。</p>
<p id="meta" class="muted"></p><div class="grid"><div class="card"><b>立即：歷史重播</b><br>共同母體比較九個版本，保留全部結果。</div><div class="card"><b>約兩週：第一輪短期回饋</b><br>3 日結果 × 5 個成熟日，先查邏輯與缺值。</div><div class="card"><b>約三至五週：迭代候選</b><br>10／20 日按固定規則保留、重設或簡化。</div></div>
<section><h2>策略比較</h2><label>資料<select id="dataset"><option value="replay">歷史重播</option><option value="frozen_replay">舊快照重播</option><option value="forward">登錄後前瞻</option></select></label><label>持有視窗<select id="horizon"><option value="1">1 日（敏感度）</option><option value="3" selected>3 日（主要）</option><option value="5">5 日（敏感度）</option></select></label>
<p id="context" class="muted"></p><div class="scroll"><table><thead><tr><th>版本／研究問題</th><th>相對基準 ΔIC ±SE</th><th>候選 IC ±SE</th><th>前四分位－後四分位</th><th>覆蓋／排除</th></tr></thead><tbody id="rows"></tbody></table></div><p class="muted">訊號日 d → d+1 開盤 → d+1+H 開盤。每日先等權聚合族群，HAC 保留完整交易日距離。n/H 只代表重疊尺度；短窗仍可能有自相關。SE 尚不可估會明示，沒有把未成熟結果補成 0。</p></section>
<section><h2>不等報酬：名單是否真的不同？</h2><div id="structure" class="scroll"></div><p class="muted">同分比例＝1−不同分數數量／股票數；相似度＝與基準前四分位名單的 Jaccard；日變動＝相鄰市場日前四分位名單的 Jaccard 距離。這些是名單結構，日變動不是投組換手率。單位為比例，附跨日 SE。</p></section>
<section><h2>如何快一點，而且知道自己在測什麼</h2><div class="scroll"><table><tr><th>方法</th><th>能回答</th><th>下一個動作</th></tr><tr><td>歷史／舊快照重播</td><td>策略是否有變異？哪個元素看起來冗餘？</td><td>立即設計下一輪；不稱為新策略 OOS。</td></tr><tr><td>時間分段走動驗證</td><td>前段選中的版本，後段是否崩壞？</td><td>固定 30 日起始訓練、6 日隔離、15 日測試。</td></tr><tr><td>短期前瞻 1／3／5 日</td><td>名單能否辨認短期強弱？</td><td>固定 3 日為主，不事後挑最好視窗。</td></tr><tr><td>移除族群／不重疊起點／置換</td><td>結果是否依賴一個族群、一個起點或任意配對？</td><td>優先淘汰脆弱設計；這些不是額外獨立樣本。</td></tr></table></div></section>
<section><h2>固定短期檢視</h2><p>5 日查計算與差異；10 日明顯偏負可重設；20 日 ΔIC ≥0.02 且前後兩段方向皆正，保留到下一輪。這是實驗資源分配規則，未校準顯著性，也不自動改主頁策略。</p><div id="looks"></div></section>
<section><details><summary>時間分段重播、壓力測試與完整證據</summary><div id="folds"></div><div id="sensitivity"></div><p>成本觀察：前四分位相對全組等權毛報酬，再扣固定 0.585 個百分點；只是 cohort 敏感度，沒有資金投組，也不當成實驗准入門檻。</p><p><a href="experiment_lab.json">下載全部日序列、樣本、缺失與規格 JSON</a> · <a href="../EXPERIMENT_LAB.md">實驗規格</a></p><ul id="limits"></ul></details></section>
<footer>日期估計假設資料及時完整；缺值、休市或零變異會延後。所有策略都保留於表中，不只展示勝者。</footer></main>
<script>const R=__PAYLOAD__;const $=id=>document.getElementById(id);const esc=x=>String(x).replace(/[&<>\"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}[c]));
const f=(v,n=3)=>v==null?'—':v.toFixed(n);function stat(s){if(!s)return '尚無成熟配對';return `${f(s.mean)} ± ${s.se==null?'尚不可估':f(s.se)}<br><small>t=${f(s.t,2)}；n=${s.n_days}；n/H=${f(s.eff_obs,1)}；${s.episodes} 區段</small>`;}
$('meta').textContent=`資料截至 ${R.as_of} · ${R.protocol} · DB 唯讀 · 九個版本 · 主視窗 3 日`;
function draw(){let ds=$('dataset').value,h=$('horizon').value,data=R.datasets[ds].horizons[h];$('context').textContent=R.datasets[ds].label+(ds==='forward'?'：只認登錄後及時的首次正式快照。':'：探索與設計用，結果不是新策略的前瞻證明。');$('rows').innerHTML=R.config.strategies.map(s=>{let r=data[s.id],c=r.coverage;return `<tr><td><b>${esc(s.name)}</b><br><small>${esc(s.question)}</small></td><td class="number">${stat(r.summary.delta_ic)}</td><td class="number">${stat(r.summary.ic)}</td><td class="number">${stat(r.summary.spread_pp)}<small>單位：百分點</small></td><td>${c.paired_group_days||0} 組日<br><small>${(c.attempted_group_days||0)-(c.paired_group_days||0)} 組日未納入；組日不是獨立樣本</small></td></tr>`}).join('');$('sensitivity').innerHTML='<h3>目前選定視窗的穩健性</h3>'+R.config.strategies.filter(s=>s.id!=='BASE').map(s=>{let r=data[s.id];return `<p><b>${esc(s.name)}</b>：移除一族群後 ΔIC ${Object.entries(r.leave_one_group_out).map(([g,v])=>`${esc(g)} ${v?f(v.mean):'—'}`).join('；')}<br><small>不重疊起點：${Object.entries(r.nonoverlap_offsets).map(([k,v])=>`${k}: ${v?f(v.mean)+' (n='+v.n_days+')':'—'}`).join('；')}。完整 SE／t、帶寬與成本讀 JSON。</small></p>`}).join('');}
function drawStructure(){let data=R.datasets[$('dataset').value].structure;$('structure').innerHTML='<table><thead><tr><th>版本</th><th>同分比例</th><th>與基準名單相似度</th><th>名單日變動</th></tr></thead><tbody>'+R.config.strategies.map(s=>{let r=data[s.id].summary;return `<tr><td>${esc(s.name)}</td><td>${stat(r.tie_fraction)}</td><td>${stat(r.top_jaccard)}</td><td>${stat(r.list_change)}</td></tr>`}).join('')+'</tbody></table>';}
$('dataset').onchange=()=>{draw();drawStructure();};$('horizon').onchange=draw;draw();drawStructure();$('looks').innerHTML=R.config.strategies.filter(s=>s.id!=='BASE').map(s=>`<p><b>${esc(s.name)}</b>：${R.forward_looks[s.id].map(l=>`${l.n}日 ${l.ready?esc(l.reason):'還需 '+l.remaining+' 個成熟日'}`).join(' ／ ')}</p>`).join('');$('folds').innerHTML='<h3>歷史分段結果</h3>'+R.walk_forward.folds.map(fold=>`<p>訓練截至 ${fold.train_last}（最後標籤 ${fold.train_last_outcome}），測試 ${fold.test_first}～${fold.test_last}，選中 ${esc(fold.selected||'無足夠資料')}：${stat(fold.selected?fold.all_test_candidates[fold.selected]:null)}</p>`).join('')+'<p>置換對照使用 16 個固定 seed；完整個別 IC ±SE 見 JSON，不將置換分布當成通過門檻。</p>';$('limits').innerHTML=R.limitations.map(x=>`<li>${esc(x)}</li>`).join('');</script></html>""".replace("__PAYLOAD__", payload)


def validate_output_paths(db, output_dir, review_dir):
    for directory in (output_dir, review_dir):
        resolved = Path(directory).resolve()
        if any((ROOT / name).resolve() in (resolved, *resolved.parents) for name in ("data", "archive", "config", "scripts")):
            raise ValueError("outputs cannot target formal data, archive, config, or source")
    for filename in ("experiment_lab.json", "experiment_lab.html"):
        target = (Path(output_dir) / filename).resolve()
        if target == Path(db).resolve() or any((ROOT / name).resolve() in (target, *target.parents)
                                             for name in ("data", "archive", "config", "scripts")):
            raise ValueError("output must not overwrite database")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=ROOT / "data/findmind.db")
    ap.add_argument("--as-of", help="Outcome cutoff only; does not recreate an old DB vintage")
    ap.add_argument("--out-dir", type=Path, default=ROOT / "reports")
    ap.add_argument("--registry-dir", type=Path, default=REGISTRY_DIR)
    ap.add_argument("--reviews-dir", type=Path, default=ROOT / "reports/experiment_reviews")
    ap.add_argument("--register", action="store_true", help="Register a NEW protocol at current time; no backdating or overwrite")
    args = ap.parse_args()
    cfg = load_config()
    if args.register:
        receipt = register(cfg, registry_dir=args.registry_dir)
        print(f"registered {receipt['protocol']} at {receipt['registered_at']}")
        return
    fingerprint = check_registration(cfg, args.registry_dir)
    validate_output_paths(args.db, args.out_dir, args.reviews_dir)
    before = hashlib.sha256(args.db.read_bytes()).hexdigest()
    with closing(db_ro.connect(args.db)) as con:
        report = analyze(con, cfg, fingerprint, args.as_of)
    if hashlib.sha256(args.db.read_bytes()).hexdigest() != before:
        raise RuntimeError("database changed during experiment")
    report["db_sha256"] = before
    report["environment"] = {"python": sys.version, "platform": platform.platform(),
        "utf8_mode": sys.flags.utf8_mode, "PYTHONUTF8": os.environ.get("PYTHONUTF8"),
        "PYTHONIOENCODING": os.environ.get("PYTHONIOENCODING")}
    freeze_reviews(args.reviews_dir, report, report["calendar"])
    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "experiment_lab.json").write_bytes(canonical(public_report(report)))
    (args.out_dir / "experiment_lab.html").write_bytes(render_html(report).encode("utf-8"))
    print(f"{cfg['protocol']}: as_of={report['as_of']}, variants={len(cfg['strategies'])}, "
          f"forward_signals={len(report['datasets']['forward']['eligible_signal_dates'])}; DB unchanged")


if __name__ == "__main__":
    main()
