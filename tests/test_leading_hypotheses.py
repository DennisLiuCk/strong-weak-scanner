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
report_version: 1
status: active_monitoring
last_updated: 2026-07-12
content_as_of: 2026-07-12
next_review: 2026-08-31
formal_note_content_sha256: {digest}
-->

## H1｜可驗證主張

- **市場主張：** 某產品可能在下季量產。
- **首次捕捉：** 2026-07-01。
- **來源層級：** 具名媒體轉述。
- **目前狀態：** `plausible_lead`。
- **正式資料基準：** 正式筆記只確認研發。
- **可證偽條件：** 下季仍未量產。
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
                         "`plausible_lead`。")

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

    def test_default_today_uses_taiwan_research_date(self):
        with mock.patch.object(lh, "_today", return_value=date(2026, 7, 12)):
            info = lh.analyse_report("1234_測試.md", report_text(), notes=self.notes)
        self.assertFalse(info["quality_invalid"], info["quality_errors"])

    def test_three_batches_have_thirty_valid_reports_and_sixty_hypotheses(self):
        reports = lh.load_reports()
        self.assertEqual(len(reports), 30)
        self.assertEqual(sum(report["hypothesis_count"] for report in reports.values()), 60)
        self.assertFalse([report["quality_errors"] for report in reports.values()
                          if report["quality_invalid"]])


if __name__ == "__main__":
    unittest.main()
