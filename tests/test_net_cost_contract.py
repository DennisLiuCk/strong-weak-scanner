"""§⑩ 淨成本下限的契約。

存在理由(2026-07-26 實測):§①~⑨ 量的全是「毛」訊號品質,而且用 `close(d)` 計價——
但訊號在台北 18:07 之後才產出,**close(d) 買不到**;§⑧ 又顯示真強中位停留只有 4~5 日,
照 tier 進出的年化換手上百次。實測結論:真強在固定持有 3 日(≈ 照 tier 進出)時,
扣掉 0.585% 來回成本後淨超額 −0.094%(t=−0.2);拉到 10 日是 +1.408%(t=+1.4)。
**沒有一格達到 |t|>2**,所以「這套訊號扣成本後仍有效」目前不可宣稱。

這組斷言防的是「哪天有人把 §⑩ 改成用 close(d) 計價、或忘了扣成本」——那會讓一個
本來誠實的區塊變成過度樂觀的區塊。
"""
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

    def test_hold_horizons_include_the_observed_dwell(self):
        """必須含一個接近實際停留(§⑧ 真強中位 4~5 日、進出各延一天後約 3 日)的短持有,
        否則只呈現長持有會系統性低估成本衝擊。"""
        self.assertIn(3, validate.NET_HOLD_DAYS)
        self.assertIn(10, validate.NET_HOLD_DAYS, "要保留與 §② 量測窗相同的對照")
        self.assertEqual(sorted(validate.NET_HOLD_DAYS), list(validate.NET_HOLD_DAYS))

    def test_section_uses_next_day_open_not_same_day_close(self):
        """進出一律隔日開盤。訊號 18:07 才產出,用 close(d) 等於假設買到不可能的價格。"""
        self.assertIn("shift(d, 1)", self.sec, "進場必須是隔日")
        self.assertIn("adj_o", self.sec, "必須用還原開盤")
        self.assertIn("原始開盤 × 還原收盤/原始收盤", self.sec,
                      "還原開盤的推導方式要寫在報告裡供稽核")

    def test_section_actually_subtracts_the_cost(self):
        self.assertIn("- COST_ROUND_TRIP", self.sec, "淨超額必須真的扣掉來回成本")

    def test_section_clusters_by_date_before_standard_error(self):
        """同一檔連續多日為真強會被重複計入;必須先按日聚合再估 SE。
        未聚合時實測 t 由 +1.4 虛胖到 +3.3。"""
        self.assertIn("sci.summarize", self.sec)
        self.assertIn("daily[d] = mean(vals)", self.sec,
                      "必須先把當日各檔收斂成一個數,才能按日聚類")

    def test_section_refuses_to_claim_effectiveness(self):
        self.assertIn("|t|>2", self.sec, "必須明示未達門檻前不可宣稱有效")
        self.assertNotIn("證明有效", self.sec)


if __name__ == "__main__":
    unittest.main()
