import tempfile
import unittest
from datetime import date
from pathlib import Path
import sys
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import leading_hypotheses as lh


def report_text(digest="a" * 64):
    return f"""# 1234 測試 — 領先假說報告

<!-- meta
stock_id: 1234
report_version: 2
status: active_monitoring
last_updated: 2026-07-12
content_as_of: 2026-07-12
next_review: 2026-08-31
formal_note_content_sha256: {digest}
-->

## H1｜可驗證主張

<!-- hypothesis_meta
source_published_at: 2026-07-01
research_captured_at: 2026-07-12
capture_mode: prospective
lifecycle: open
evidence_strength: weak
evidence_flags: none
source_type: media_report
source_publishers: example.com
source_accessed_at: 2026-07-12
source_chain_ids: 1234-H1-C1
independent_chain_count: 1
review_due: 2026-08-31
-->
<!-- transition
date: 2026-07-12
from: initial
to: open
reason: initial_capture
evidence: source_chain:1234-H1-C1
evidence_published_at: 2026-07-01
review_due: 2026-08-31
-->

- **市場主張：** 某產品可能在下季量產。
- **消息日期：** 2026-07-01。
- **研究收錄：** 2026-07-12（前瞻捕捉）。
- **來源層級：** 具名媒體轉述。
- **目前狀態：** 合理線索・證據不足（`plausible_lead`）。
- **正式資料基準：** 正式筆記只確認研發。
- **可證偽條件：** 下季仍未量產。
- **驗證期限：** 2026-08-31。
- **下次驗證：** 下一季財報。
- **研究判讀：** 量產與研發必須分開。
- **來源：** [來源](https://example.com/report)。
"""


class LeadingHypothesesTest(unittest.TestCase):
    def setUp(self):
        self.notes = {"1234": {
            "verification": "independently_verified",
            "reviewed_content_sha256": "a" * 64,
        }}

    def test_valid_report_is_anchored_and_falsifiable(self):
        info = lh.analyse_report("1234_測試.md", report_text(), notes=self.notes,
                                 today="2026-07-12")
        self.assertFalse(info["quality_invalid"], info["quality_errors"])
        self.assertEqual(info["hypothesis_count"], 1)
        self.assertEqual(info["hypotheses"][0]["fields"]["目前狀態"],
                         "合理線索・證據不足（`plausible_lead`）。")
        self.assertEqual(info["hypotheses"][0]["meta"]["capture_mode"], "prospective")
        self.assertEqual(info["hypotheses"][0]["transitions"][-1]["to"], "open")

    def test_status_catalog_has_reader_labels_and_terminal_states(self):
        self.assertEqual(lh.HYPOTHESIS_STATUS_INFO["management_quoted"]["label"],
                         "管理層說法・待驗證")
        self.assertEqual(lh.HYPOTHESIS_STATUS_INFO["attribution_error"]["stage"],
                         "證據警示")
        self.assertFalse(lh.HYPOTHESIS_STATUS_INFO["plausible_lead"]["terminal"])
        self.assertTrue(lh.HYPOTHESIS_STATUS_INFO["resolved"]["terminal"])
        self.assertTrue(lh.HYPOTHESIS_STATUS_INFO["contradicted"]["terminal"])
        self.assertTrue(lh.HYPOTHESIS_STATUS_INFO["expired_unresolved"]["terminal"])

    def test_formal_note_change_invalidates_anchor(self):
        info = lh.analyse_report("1234_測試.md", report_text("b" * 64),
                                 notes=self.notes, today="2026-07-12")
        self.assertTrue(info["quality_invalid"])
        self.assertTrue(any("重新對照" in error for error in info["quality_errors"]))

    def test_missing_falsifier_fails(self):
        text = report_text().replace("- **可證偽條件：** 下季仍未量產。\n", "")
        info = lh.analyse_report("1234_測試.md", text, notes=self.notes,
                                 today="2026-07-12")
        self.assertTrue(any("可證偽條件" in error for error in info["quality_errors"]))

    def test_published_date_cannot_be_after_research_capture(self):
        text = report_text().replace("source_published_at: 2026-07-01",
                                     "source_published_at: 2026-07-13")
        text = text.replace("- **消息日期：** 2026-07-01。", "- **消息日期：** 2026-07-13。")
        info = lh.analyse_report("1234_測試.md", text, notes=self.notes, today="2026-07-13")
        self.assertTrue(any("不可晚於 research_captured_at" in error
                            for error in info["quality_errors"]))

    def test_lifecycle_must_match_reader_status(self):
        text = report_text().replace("lifecycle: open", "lifecycle: confirmed", 1)
        text = text.replace("to: open", "to: confirmed", 1)
        text = text.replace("review_due: 2026-08-31", "review_due: none", 1)
        text = text.replace("- **驗證期限：** 2026-08-31。", "- **驗證期限：** none。")
        info = lh.analyse_report("1234_測試.md", text, notes=self.notes, today="2026-07-12")
        self.assertTrue(any("lifecycle 與目前狀態不一致" in error
                            for error in info["quality_errors"]))

    def test_transition_history_must_connect(self):
        addition = """\n<!-- transition
date: 2026-07-13
from: wrong_state
to: open
reason: new_evidence
evidence: source_chain:1234-H1-C1
evidence_published_at: 2026-07-13
review_due: 2026-08-31
-->"""
        text = report_text().replace("- **市場主張：**", addition + "\n- **市場主張：**")
        info = lh.analyse_report("1234_測試.md", text, notes=self.notes, today="2026-07-13")
        self.assertTrue(any("未銜接上一狀態" in error for error in info["quality_errors"]))

    def test_source_chain_count_must_match_ids(self):
        text = report_text().replace("independent_chain_count: 1", "independent_chain_count: 2")
        info = lh.analyse_report("1234_測試.md", text, notes=self.notes, today="2026-07-12")
        self.assertTrue(any("source_chain_ids" in error for error in info["quality_errors"]))

    def test_v1_migration_preserves_claim_and_marks_retrospective(self):
        v1 = report_text().replace("report_version: 2", "report_version: 1")
        v1 = lh.HYP_META_RE.sub("", v1)
        v1 = lh.TRANSITION_RE.sub("", v1)
        v1 = v1.replace("- **消息日期：**", "- **首次捕捉：**")
        v1 = v1.replace("- **研究收錄：** 2026-07-12（前瞻捕捉）。\n", "")
        v1 = v1.replace("- **驗證期限：** 2026-08-31。\n", "")
        migrated = lh.migrate_report_text_v2(v1)
        self.assertIn("report_version: 2", migrated)
        self.assertIn("capture_mode: retrospective", migrated)
        self.assertIn("研究收錄：** 2026-07-12（回溯建檔）", migrated)
        self.assertIn("某產品可能在下季量產", migrated)

    def test_due_queue_is_hypothesis_level(self):
        info = lh.analyse_report("1234_測試.md", report_text(), notes=self.notes,
                                 today="2026-07-12")
        reports = {"1234": info}
        self.assertEqual(lh.due_hypotheses(reports, "2026-08-30"), [])
        self.assertEqual(lh.due_hypotheses(reports, "2026-08-31")[0][1:3],
                         ("1234", "H1"))

    def test_due_queue_reconstructs_history_after_terminal_transition(self):
        reports = {"1234": {"hypotheses": [{
            "id": "H1", "title": "歷史期限", "meta": {"lifecycle": "confirmed"},
            "transitions": [
                {"date": "2026-07-12", "to": "open", "review_due": "2026-08-31"},
                {"date": "2026-09-05", "to": "confirmed", "review_due": "none"},
            ],
        }]}}
        self.assertEqual(len(lh.due_hypotheses(reports, "2026-08-31")), 1)
        self.assertEqual(lh.due_hypotheses(reports, "2026-09-05"), [])

    def test_metrics_include_only_prospective_samples(self):
        prospective = lh.analyse_report("1234_測試.md", report_text(), notes=self.notes,
                                        today="2026-07-12")
        metrics = lh.prospective_metrics({"1234": prospective}, "2026-08-31")
        self.assertEqual(metrics["cohort"], 1)
        self.assertEqual(metrics["windows"][30], {"eligible": 1, "terminal": 0})

        retrospective_text = report_text().replace("capture_mode: prospective",
                                                   "capture_mode: retrospective")
        retrospective_text = retrospective_text.replace("（前瞻捕捉）", "（回溯建檔）")
        retrospective = lh.analyse_report("1234_測試.md", retrospective_text,
                                          notes=self.notes, today="2026-07-12")
        metrics = lh.prospective_metrics({"1234": retrospective}, "2026-08-31")
        self.assertEqual(metrics["cohort"], 0)

    def test_new_content_after_baseline_cannot_be_retrospective(self):
        text = report_text().replace("capture_mode: prospective", "capture_mode: retrospective")
        text = text.replace("research_captured_at: 2026-07-12", "research_captured_at: 2026-07-13")
        text = text.replace("source_accessed_at: 2026-07-12", "source_accessed_at: 2026-07-13")
        text = text.replace("date: 2026-07-12", "date: 2026-07-13")
        text = text.replace("（前瞻捕捉）", "（回溯建檔）")
        text = text.replace("- **研究收錄：** 2026-07-12", "- **研究收錄：** 2026-07-13")
        info = lh.analyse_report("1234_測試.md", text, notes=self.notes, today="2026-07-13")
        self.assertTrue(any("之後新增內容必須使用 prospective" in error
                            for error in info["quality_errors"]))

    def test_default_today_uses_taiwan_research_date(self):
        with mock.patch.object(lh, "_today", return_value=date(2026, 7, 12)):
            info = lh.analyse_report("1234_測試.md", report_text(), notes=self.notes)
        self.assertFalse(info["quality_invalid"], info["quality_errors"])

    def test_all_verified_notes_have_valid_reports_and_hypotheses(self):
        reports = lh.load_reports()
        self.assertEqual(len(reports), 118)
        self.assertEqual(sum(report["hypothesis_count"] for report in reports.values()), 219)
        self.assertFalse([report["quality_errors"] for report in reports.values()
                          if report["quality_invalid"]])
        hypotheses = [item for report in reports.values() for item in report["hypotheses"]]
        self.assertTrue(all(report["report_version"] == 2 for report in reports.values()))
        modes = [item["meta"]["capture_mode"] for item in hypotheses]
        self.assertEqual(modes.count("retrospective"), 196)
        self.assertEqual(modes.count("prospective"), 23)
        self.assertEqual(sum(int(item["meta"]["independent_chain_count"])
                             for item in hypotheses), 239)
        self.assertTrue(all(item["transitions"] for item in hypotheses))


if __name__ == "__main__":
    unittest.main()
