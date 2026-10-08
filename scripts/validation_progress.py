#!/usr/bin/env python3
"""Read-only progress for the prospective validation protocol; never promotes a model."""
import argparse
import hashlib
import json
from pathlib import Path
import re

import audit_ranking_views as audit
import db_ro
import evidence_status
import ranking_views as rv
import score
import stats_ci as sci

ROOT = Path(__file__).resolve().parents[1]
REGISTERED = "2026-10-09"
HORIZON = 10
STRUCTURAL_LOOKS = (10, 20, 40)
OUTCOME_LOOKS = (100, 200, 300)
PROTOCOL_VERSION = "validation-v2-20261009"


def fixed_review_summaries(series, calendar, horizon=HORIZON):
    """Calculate a first-N slice; use fixed_review_records for durable reviews.

    This pure helper alone cannot detect earlier backfills or revised prices.
    """
    days = sorted(series)
    return {n: sci.summarize([series[d] for d in days[:n]], horizon, days[:n], calendar)
            for n in OUTCOME_LOOKS if len(days) >= n}


def _canonical_bytes(value):
    # JSON object keys are strings. Normalize first so an in-memory int-keyed
    # lag-count map (0..19) has the same identity after a disk round trip.
    normalized = json.loads(json.dumps(value, ensure_ascii=False, allow_nan=False))
    return json.dumps(normalized, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
                      allow_nan=False).encode("utf-8")


def _review_body(series, calendar, horizon, context, days, n):
    positions = {day: i for i, day in enumerate(calendar)}
    sample_days = days[:n]
    values = [series[day] for day in sample_days]
    entry_offset = context.get("entry_offset", 0)
    end_positions = [positions[day] + entry_offset + horizon for day in sample_days]
    frozen_calendar = calendar[:end_positions[-1] + 1]
    return {
        "ledger_version": 1,
        "sample_n": n,
        "horizon": horizon,
        "context": {key: value for key, value in context.items() if key != "snapshot_ids"},
        "days": sample_days,
        "daily_values": values,
        "calendar": frozen_calendar,
        "calendar_positions": [positions[day] for day in sample_days],
        "return_end_dates": [calendar[position] for position in end_positions],
        "snapshot_ids": [context["snapshot_ids"].get(day) for day in sample_days],
        "summary": sci.summarize(values, horizon, sample_days, frozen_calendar),
        "automatic_promotion": False,
    }


def _load_review_record(path, receipt):
    """Verify content against its separately written receipt; never repair it.

    LF normalization allows Git CRLF checkouts. Digests detect changed evidence,
    not a security boundary against an actor rewriting both file and receipt.
    Git history remains the external provenance anchor.
    """
    if not path.exists() or not receipt.exists():
        return None, ["incomplete_ledger_or_missing_digest_receipt"]
    try:
        blob = path.read_bytes().replace(b"\r\n", b"\n")
        expected = receipt.read_text(encoding="ascii").strip()
        if not re.fullmatch(r"[0-9a-f]{64}", expected):
            return None, ["invalid_digest_receipt"]
        if hashlib.sha256(blob).hexdigest() != expected:
            return None, ["ledger_receipt_sha256_mismatch"]
        envelope = json.loads(blob)
        body = envelope["record"]
        digest = hashlib.sha256(_canonical_bytes(body)).hexdigest()
        if envelope["integrity_sha256"] != digest:
            return None, ["ledger_content_digest_mismatch"]
        if body["ledger_version"] != 1:
            return None, ["unsupported_ledger_version"]
        n = body["sample_n"]
        if not isinstance(n, int) or n <= 0 or not isinstance(body["summary"], dict):
            return None, ["malformed_frozen_sample"]
        if any(len(body[key]) != n for key in (
                "days", "daily_values", "calendar_positions", "snapshot_ids", "return_end_dates")):
            return None, ["malformed_frozen_sample"]
        if not body["calendar"] or any(key not in body["summary"] for key in ("mean", "se", "t", "n_days")):
            return None, ["malformed_frozen_sample"]
        return body, []
    except (OSError, UnicodeError, ValueError, TypeError, KeyError):
        return None, ["unreadable_or_malformed_ledger"]


def fixed_review_records(series, calendar, horizon, context, output_dir):
    """Persist each first-N review once and flag any later evidence drift.

    Context requires series_id, score_spec_sha, ranking_spec_sha,
    protocol_version, source_sha, and snapshot_ids (date -> first official ID).
    Other context fields must also be immutable; source_sha describes evaluator
    sources, not the repository's changing daily-data commit.

    The path is fixed per series and N. Protocol/evaluator changes flag drift;
    an explicitly newly registered protocol must use its own output directory.
    Existing records remain visible if the current sample falls below N.
    Return {N: {summary, drift, integrity_ok, drift_reasons, created, path,
                first_date, last_date}}. Invalid/tampered evidence has no usable
    summary. Changed inputs return the original summary with drift=True.
    Only dates whose full horizon has matured in calendar can enter a look;
    entry_offset (default 0; next-open cohorts use 1) is part of the context.
    """
    required = ("series_id", "score_spec_sha", "ranking_spec_sha", "protocol_version", "source_sha")
    if any(not isinstance(context.get(key), str) or not context[key] for key in required):
        raise ValueError("fixed review context requires nonempty identity/spec/source strings")
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,100}", context["series_id"]):
        raise ValueError("series_id must be a safe ASCII identifier")
    if not isinstance(context.get("snapshot_ids"), dict):
        raise ValueError("fixed review context requires snapshot_ids by date")
    entry_offset = context.get("entry_offset", 0)
    if not isinstance(entry_offset, int) or entry_offset < 0:
        raise ValueError("entry_offset must be a nonnegative integer")
    calendar = list(calendar)
    all_days = sorted(series)
    # Validate all input alignment, even before the first review can mature.
    sci.summarize([series[day] for day in all_days], horizon, all_days, calendar)
    positions = {day: index for index, day in enumerate(calendar)}
    days = [day for day in all_days if series[day] is not None
            and positions[day] + entry_offset + horizon < len(calendar)]
    directory = Path(output_dir) / context["series_id"]
    results = {}
    for n in OUTCOME_LOOKS:
        path = directory / f"first_{n}.json"
        receipt = directory / f"first_{n}.sha256"
        exists = path.exists() or receipt.exists()
        if not exists and len(days) < n:
            continue
        created = False
        candidate = _review_body(series, calendar, horizon, context, days, n) if len(days) >= n else None
        if not exists:
            if any(not isinstance(value, str) or not value for value in candidate["snapshot_ids"]):
                raise ValueError("every first-N paired day needs its first official snapshot ID")
            digest = hashlib.sha256(_canonical_bytes(candidate)).hexdigest()
            envelope = {"record": candidate, "integrity_sha256": digest}
            blob = (json.dumps(envelope, ensure_ascii=False, sort_keys=True, indent=2,
                               allow_nan=False) + "\n").encode("utf-8")
            directory.mkdir(parents=True, exist_ok=True)
            try:
                with path.open("xb") as handle:
                    handle.write(blob)
                with receipt.open("xb") as handle:
                    handle.write((hashlib.sha256(blob).hexdigest() + "\n").encode("ascii"))
                created = True
            except FileExistsError:
                # Another writer or a partial prior write owns this review.
                # Re-read it; never overwrite or silently regenerate a receipt.
                pass
        stored, problems = _load_review_record(path, receipt)
        integrity_ok = stored is not None
        if stored is not None:
            try:
                if stored["sample_n"] != n or stored["context"]["series_id"] != context["series_id"]:
                    raise ValueError("ledger identity does not match its path")
                static_context = {key: value for key, value in context.items() if key != "snapshot_ids"}
                if _canonical_bytes(stored["context"]) != _canonical_bytes(static_context):
                    problems.append("spec_protocol_or_source_context_changed")
                if stored["horizon"] != horizon:
                    problems.append("horizon_changed")
                if candidate is None:
                    problems.append("fewer_than_frozen_N_observed_paired_days")
                else:
                    for key, reason in (
                        ("days", "first_N_paired_days_changed_by_backfill_or_removal"),
                        ("daily_values", "paired_values_changed_or_price_history_restated"),
                        ("calendar", "historical_trading_calendar_changed"),
                        ("calendar_positions", "sample_calendar_positions_changed"),
                        ("return_end_dates", "forward_return_end_dates_changed"),
                        ("snapshot_ids", "first_official_snapshot_ids_changed_or_missing"),
                        ("summary", "summary_or_evaluator_result_changed"),
                    ):
                        if _canonical_bytes(stored[key]) != _canonical_bytes(candidate[key]):
                            problems.append(reason)
            except (TypeError, ValueError, KeyError):
                stored = None
                integrity_ok = False
                problems.append("malformed_frozen_sample")
        results[n] = {
            "summary": stored["summary"] if stored else None,
            "drift": bool(problems),
            "integrity_ok": integrity_ok,
            "drift_reasons": problems,
            "created": created,
            "path": str(path),
            "first_date": stored["days"][0] if stored else None,
            "last_date": stored["days"][-1] if stored else None,
        }
    return results


def build_progress(con):
    calendar = [r[0] for r in con.execute("SELECT DISTINCT date FROM price_adj ORDER BY date")]
    runs = evidence_status.current_score_runs(con, REGISTERED)
    days = [d for d, run in runs.items() if con.execute(
        "SELECT 1 FROM oos_signal_snapshots WHERE snapshot_id=? LIMIT 1", (run['snapshot_id'],)
    ).fetchone()]
    ranking = audit.formal_progress(con, rv.SPEC_SHA, fwd=HORIZON)
    maturity = evidence_status.maturity(days, calendar, REGISTERED, HORIZON)
    mature = ranking['mature_10d_days']
    return {
        "protocol": PROTOCOL_VERSION, "registered": REGISTERED,
        "as_of": calendar[-1] if calendar else None,
        "score_version": score.SCORE_VERSION, "score_spec_sha": score.score_spec_digest(),
        "ranking_spec_sha": rv.SPEC_SHA, "score_evidence": maturity,
        "ranking": ranking,
        "structural_reviews": [{"formal_days": n,
            "remaining": max(0, n - ranking['current_spec_days'])} for n in STRUCTURAL_LOOKS],
        "outcome_reviews": [{"paired_mature_days": n,
            "remaining_at_least": max(0, n - mature)} for n in OUTCOME_LOOKS],
        "limitations": [
            "Ranking maturity is an upper bound; each challenger needs N valid paired days.",
            "n/F is a heuristic overlap scale, not measured independence.",
            "Weekly reports are monitoring; only fixed first-N samples trigger research review.",
            "Multiple-testing/sequential calibration and prospective tier/cost study are required before adoption."],
        "automatic_promotion": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=ROOT / 'data/findmind.db')
    parser.add_argument('--out', type=Path, default=ROOT / 'reports/validation_progress.json')
    args = parser.parse_args()
    if args.out.resolve() == args.db.resolve():
        parser.error('output must not overwrite the database')
    with db_ro.connect(args.db) as con:
        result = build_progress(con)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes((json.dumps(result, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
    print(f"{PROTOCOL_VERSION}: score OOS={result['score_evidence']['oos_days']}, "
          f"ranking mature={result['ranking']['mature_10d_days']}; automatic_promotion=false")


if __name__ == '__main__':
    main()
