import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_dashboard as bd


class ChipDisplayTest(unittest.TestCase):
    def test_inverse_signs_are_explained_as_diagnostic_direction(self):
        metrics = {
            "fpct_chg20": 0.5,
            "trust5_pct": -0.05,
            "margin_util_pct": 3.0,
            "margin_chg10": -0.10,
            "tdcc_big400_chg": 0.2,
            "tdcc_people_chg": -0.08,
            "sbl_chg10": -0.3,
        }
        rows, n_health, n_warn = bd.build_chip_rows(metrics, False)
        by_label = {r[0]: r for r in rows}

        margin = by_label["融資10日變化(↓去槓桿)"]
        self.assertTrue(margin[1].startswith("-"))
        self.assertIn("融資下降(去槓桿) → 本欄判讀為健康訊號", margin[2])

        people = by_label["股東人數週變化(↓集中·觀察)"]
        self.assertTrue(people[1].startswith("-"))
        self.assertIn("股東人數下降(籌碼集中) → 本欄判讀為健康訊號", people[2])
        self.assertIn("方向尚未用規則定案後的新資料驗證", people[2])

        sbl = by_label["借券餘額10日變化(↓減壓·觀察)"]
        self.assertTrue(sbl[1].startswith("-"))
        self.assertIn("壓力減輕", sbl[2])
        self.assertEqual((n_health, n_warn), (6, 1))

    def test_missing_and_official_risk_are_explicit(self):
        metrics = {k: None for k in (
            "fpct_chg20", "trust5_pct", "margin_util_pct", "margin_chg10",
            "tdcc_big400_chg", "tdcc_people_chg", "sbl_chg10")}
        rows, n_health, n_warn = bd.build_chip_rows(metrics, True)
        self.assertEqual((n_health, n_warn), (0, 0))
        self.assertIn("資料不足 → 中性", rows[0][2])
        self.assertEqual(rows[-1][1], "有列管")
        self.assertIn("一票否決", rows[-1][2])

    def test_tiny_observation_keeps_its_sign_after_formatting(self):
        metrics = {
            "fpct_chg20": None, "trust5_pct": None, "margin_util_pct": None,
            "margin_chg10": None, "tdcc_big400_chg": 0.0001,
            "tdcc_people_chg": None, "sbl_chg10": -0.00001,
        }
        rows, _, _ = bd.build_chip_rows(metrics, False)
        self.assertEqual(rows[4][1], "+0.0001pp")
        self.assertEqual(rows[6][1], "-<0.0001pp")
        self.assertIn("集中度上升", rows[4][2])
        self.assertIn("壓力減輕", rows[6][2])

    def test_template_does_not_present_chip_health_as_a_rank(self):
        template = (ROOT / "scripts" / "dashboard_template.html").read_text(encoding="utf-8")
        self.assertNotIn("row.chip.rank", template)
        self.assertNotIn("族群內第\"+row.chip", template)
        self.assertIn("純描述性,不是選股排名", template)


if __name__ == "__main__":
    unittest.main()
