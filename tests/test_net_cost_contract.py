"""Report integration contract; numerical execution tests live in test_validation_metrics."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate


class NetCostContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src = (ROOT / "scripts" / "validate.py").read_text(encoding="utf-8")
        start = cls.src.index("# ── ⑩ 淨成本下限")
        cls.sec = cls.src[start:cls.src.index('w("## 判讀警語")', start)]

    def test_cost_model_is_taiwan_round_trip(self):
        """手續費 0.1425%×2 + 證交稅 0.3%(賣出)= 0.585%。"""
        self.assertAlmostEqual(validate.COST_ROUND_TRIP, 0.585, places=6)
        self.assertAlmostEqual(validate.COST_DISCOUNTED, 0.471, places=6)
        self.assertLess(validate.COST_DISCOUNTED, validate.COST_ROUND_TRIP)

    def test_hold_horizons_include_short_and_primary_sensitivity(self):
        """Fixed windows are not a claim about actual tier-exit dwell."""
        self.assertIn(3, validate.NET_HOLD_DAYS)
        self.assertIn(10, validate.NET_HOLD_DAYS, "要保留與 §② 量測窗相同的對照")
        self.assertEqual(sorted(validate.NET_HOLD_DAYS), list(validate.NET_HOLD_DAYS))

    def test_section_uses_next_day_open_not_same_day_close(self):
        """進出一律隔日開盤。訊號 18:07 才產出,用 close(d) 等於假設買到不可能的價格。"""
        self.assertIn("shift(d, 1)", self.sec, "進場必須是隔日")
        self.assertIn("adj_o", self.sec, "必須用還原開盤")
        self.assertIn("原始開盤 × 還原收盤/原始收盤", self.sec,
                      "還原開盤的推導方式要寫在報告裡供稽核")

    def test_section_uses_the_numerically_tested_cohort_engine(self):
        self.assertIn("vm.fixed_hold_net_series(v2, dates, adj_o, grp_of,", self.sec)
        self.assertIn("tier_name, H, COST_ROUND_TRIP)", self.sec)

    def test_section_refuses_to_claim_effectiveness(self):
        self.assertIn("單一 t 門檻不證明可交易獲利", self.sec)
        self.assertIn("進出各延一天不會縮短持有期", self.sec)
        self.assertIn("本表也不是 NAV", self.sec)
        self.assertNotIn("證明有效", self.sec)


if __name__ == "__main__":
    unittest.main()
