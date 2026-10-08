import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import validation_progress as vp


class ProgressProtocolTest(unittest.TestCase):
    def test_fixed_review_ignores_future_observations_and_waits_for_sample(self):
        calendar = list(range(350))
        series = {d: (d % 7) / 100 for d in range(99)}
        self.assertEqual(vp.fixed_review_summaries(series, calendar), {})
        series[99] = .1
        at_first = vp.fixed_review_summaries(series, calendar)
        self.assertEqual(set(at_first), {100})
        series.update({d: 10000 for d in range(100, 205)})
        later = vp.fixed_review_summaries(series, calendar)
        self.assertEqual(set(later), {100, 200})
        self.assertEqual(later[100], at_first[100])

    def test_missing_days_delay_the_fixed_review(self):
        calendar = list(range(150))
        values = {d: .01 * (d % 5) for d in range(110) if d % 10}
        self.assertEqual(len(values), 99)
        self.assertEqual(vp.fixed_review_summaries(values, calendar), {})


class FixedReviewLedgerTest(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.output = Path(self.folder.name)
        self.calendar = list(range(350))
        self.context = {
            "series_id": "shadow_vol0", "score_spec_sha": "score-a",
            "ranking_spec_sha": "ranking-a", "protocol_version": "protocol-a",
            "source_sha": "evaluator-a", "snapshot_ids": {d: f"first-{d}" for d in self.calendar},
        }
        self.series = {d: (d % 7) / 100 for d in range(100)}

    def record(self, series=None, calendar=None, context=None):
        return vp.fixed_review_records(
            self.series if series is None else series,
            self.calendar if calendar is None else calendar,
            10, self.context if context is None else context, self.output)

    def test_first_look_is_exclusive_utf8_lf_and_later_append_preserves_it(self):
        self.assertEqual(self.record({d: self.series[d] for d in range(99)}), {})
        first = self.record()[100]
        self.assertTrue(first["created"])
        self.assertFalse(first["drift"])
        self.assertTrue(first["integrity_ok"])
        path = Path(first["path"])
        receipt = path.with_suffix(".sha256")
        frozen, frozen_receipt = path.read_bytes(), receipt.read_bytes()
        self.assertNotIn(b"\r\n", frozen)
        payload = json.loads(frozen)
        sample = payload["record"]
        self.assertEqual(sample["days"], list(range(100)))
        self.assertEqual(sample["calendar_positions"], list(range(100)))
        self.assertEqual(sample["return_end_dates"], list(range(10, 110)))
        self.assertEqual(sample["calendar"], list(range(110)))
        self.assertEqual(sample["snapshot_ids"], [f"first-{d}" for d in range(100)])
        self.assertEqual(payload["integrity_sha256"],
                         hashlib.sha256(vp._canonical_bytes(sample)).hexdigest())
        grown = {**self.series, **{d: 10000 for d in range(100, 205)}}
        later = self.record(grown)
        self.assertEqual(set(later), {100, 200})
        self.assertEqual(later[100]["summary"], first["summary"])
        self.assertFalse(later[100]["created"])
        self.assertFalse(later[100]["drift"])
        self.assertEqual(path.read_bytes(), frozen)
        self.assertEqual(receipt.read_bytes(), frozen_receipt)

    def test_earlier_missing_day_backfill_flags_drift_without_reselecting(self):
        sparse = {d: d / 100 for d in range(1, 101)}
        first = self.record(sparse)[100]
        path = Path(first["path"])
        original_bytes = path.read_bytes()
        updated = self.record({0: -999, **sparse})[100]
        self.assertTrue(updated["drift"])
        self.assertIn("first_N_paired_days_changed_by_backfill_or_removal", updated["drift_reasons"])
        self.assertEqual(updated["summary"], first["summary"])
        self.assertEqual(updated["first_date"], 1)
        self.assertEqual(path.read_bytes(), original_bytes)

    def test_revised_price_values_are_explicit_drift_and_never_overwritten(self):
        first = self.record()[100]
        path = Path(first["path"])
        original = path.read_bytes()
        updated = self.record({**self.series, 20: 99})[100]
        self.assertTrue(updated["integrity_ok"])
        self.assertTrue(updated["drift"])
        self.assertIn("paired_values_changed_or_price_history_restated", updated["drift_reasons"])
        self.assertEqual(updated["summary"], first["summary"])
        self.assertEqual(path.read_bytes(), original)

    def test_snapshot_or_context_changes_are_detected(self):
        self.record()
        ids = {**self.context["snapshot_ids"], 15: "corrected-not-first"}
        changed_id = self.record(context={**self.context, "snapshot_ids": ids})[100]
        self.assertIn("first_official_snapshot_ids_changed_or_missing", changed_id["drift_reasons"])
        for key in ("score_spec_sha", "ranking_spec_sha", "source_sha", "protocol_version"):
            with self.subTest(key=key):
                changed = self.record(context={**self.context, key: "changed"})[100]
                self.assertIn("spec_protocol_or_source_context_changed", changed["drift_reasons"])

    def test_calendar_revision_is_detected_but_later_calendar_extension_is_not(self):
        first = self.record()[100]
        altered = self.record(calendar=[-1] + self.calendar)[100]
        self.assertIn("historical_trading_calendar_changed", altered["drift_reasons"])
        self.assertIn("sample_calendar_positions_changed", altered["drift_reasons"])
        self.assertEqual(altered["summary"], first["summary"])
        appended = self.record(calendar=list(range(500)))[100]
        self.assertFalse(appended["drift"])

    def test_missing_observations_keep_existing_look_and_flag_drift(self):
        first = self.record()[100]
        changed = self.record({d: v for d, v in self.series.items() if d != 50})[100]
        self.assertTrue(changed["drift"])
        self.assertIn("fewer_than_frozen_N_observed_paired_days", changed["drift_reasons"])
        self.assertEqual(changed["summary"], first["summary"])

    def test_tampered_record_is_red_even_if_inner_digest_is_recomputed(self):
        first = self.record()[100]
        path = Path(first["path"])
        envelope = json.loads(path.read_bytes())
        envelope["record"]["daily_values"][0] = 999
        envelope["integrity_sha256"] = hashlib.sha256(vp._canonical_bytes(envelope["record"])).hexdigest()
        tampered = (json.dumps(envelope) + "\n").encode("utf8")
        path.write_bytes(tampered)
        changed = self.record()[100]
        self.assertTrue(changed["drift"])
        self.assertFalse(changed["integrity_ok"])
        self.assertIsNone(changed["summary"])
        self.assertIn("ledger_receipt_sha256_mismatch", changed["drift_reasons"])
        self.assertEqual(path.read_bytes(), tampered)

    def test_missing_receipt_is_not_silently_repaired(self):
        first = self.record()[100]
        receipt = Path(first["path"]).with_suffix(".sha256")
        receipt.unlink()
        changed = self.record()[100]
        self.assertFalse(changed["integrity_ok"])
        self.assertTrue(changed["drift"])
        self.assertFalse(receipt.exists())

    def test_crlf_git_checkout_does_not_change_content_identity(self):
        first = self.record()[100]
        path = Path(first["path"])
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
        later = self.record()[100]
        self.assertTrue(later["integrity_ok"])
        self.assertFalse(later["drift"])
        self.assertEqual(later["summary"], first["summary"])

    def test_multidigit_lag_keys_keep_the_same_digest_after_json_roundtrip(self):
        first = vp.fixed_review_records(self.series, self.calendar, 20, self.context, self.output)[100]
        self.assertTrue(first["integrity_ok"])
        self.assertFalse(first["drift"])
        self.assertEqual(set(first["summary"]["observed_lag_pairs"]), {str(i) for i in range(20)})
        again = vp.fixed_review_records(self.series, self.calendar, 20, self.context, self.output)[100]
        self.assertTrue(again["integrity_ok"])
        self.assertFalse(again["drift"])
        self.assertEqual(again["summary"], first["summary"])

    def test_unmature_values_and_none_do_not_trigger_a_look(self):
        self.assertEqual(self.record(calendar=list(range(109))), {})  # Only 99 mature dates.
        with_none = {**self.series, 50: None}
        self.assertEqual(self.record(with_none), {})
        shifted = {**self.context, "entry_offset": 1}
        self.assertEqual(self.record(calendar=list(range(110)), context=shifted), {})

    def test_missing_identity_is_rejected_before_creating_an_archive(self):
        ids = {d: value for d, value in self.context["snapshot_ids"].items() if d != 50}
        with self.assertRaises(ValueError):
            self.record(context={**self.context, "snapshot_ids": ids})
        self.assertFalse((self.output / self.context["series_id"]).exists())

    def test_invalid_date_alignment_cannot_be_hidden_below_first_look(self):
        with self.assertRaises(ValueError):
            self.record({999: 1})
        with self.assertRaises(ValueError):
            self.record({1: 1}, calendar=[1, 0, 2])
        with self.assertRaises(ValueError):
            self.record(context={**self.context, "series_id": "../escape"})
