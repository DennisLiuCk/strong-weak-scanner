"""事先登錄假設的契約(§⑪)。

核心是**不可事後修改**:`spec_sha` 同時覆蓋規格欄位與評估函式原始碼。任何人動了操作
定義又想引用既有資料,這裡就會標紅——他必須改成登錄一個新假設、OOS 時鐘重新起算。

為什麼登錄假設而不是登錄策略名單:2026-07-26 的檢定力估算顯示,要分辨兩個正交策略的
真實 IC 差 0.02 需約 2.3 年;能快速分勝負的配對恰好是冗餘的(ρ≈0.86)。與其比一組
分不出高下的名次,不如驗一個方向、門檻、放棄條件都事先寫死的假設。
"""
import datetime
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import hypotheses as hyp


class HypothesisRegistryTest(unittest.TestCase):
    def test_spec_sha_matches_spec_and_evaluator_source(self):
        """規格或評估函式一被改動,雜湊就不符——這是整套紀律的執行機制。"""
        for h in hyp.REGISTRY:
            self.assertEqual(
                h["spec_sha"], hyp.spec_digest(h),
                f"{h['id']} 的規格或評估函式已被改動。要修操作定義請登錄新假設"
                f"(新 id、新 registered 日期),不可原地改寫後繼續引用既有資料。")

    def test_ids_unique_and_dates_well_formed(self):
        ids = [h["id"] for h in hyp.REGISTRY]
        self.assertEqual(len(ids), len(set(ids)), "假設 id 不可重複")
        for h in hyp.REGISTRY:
            self.assertRegex(h["registered"], r"^\d{4}-\d{2}-\d{2}$")
            datetime.date.fromisoformat(h["registered"])   # 必須是合法日期

    def test_every_hypothesis_declares_direction_thresholds_and_abandonment(self):
        """方向、門檻、放棄條件缺一個,就不是可證偽的假設。"""
        for h in hyp.REGISTRY:
            self.assertIn(h["direction"], ("positive", "negative"),
                          f"{h['id']} 必須事先宣告方向")
            self.assertGreater(h["min_eff_obs"], 0, f"{h['id']} 必須宣告最短評估窗")
            self.assertTrue(h["success"].strip(), f"{h['id']} 必須宣告成功條件")
            self.assertTrue(h["abandon"].strip(), f"{h['id']} 必須宣告放棄條件")
            self.assertIn(h["evaluator"], hyp.EVALUATORS)
            self.assertTrue(h["plain"].strip(), f"{h['id']} 要有白話說明")

    def test_prior_is_value_is_labelled_as_not_evidence(self):
        """登錄時的 in-sample 值只記錄出身;文件必須明寫它不得再被當證據。"""
        for h in hyp.REGISTRY:
            note = h["prior_is"]["note"]
            self.assertIn("不得", note, f"{h['id']} 的 prior_is 必須標明不可當證據")
            self.assertIn("in-sample", note.lower() + note)

    def test_status_never_declares_success_before_min_window(self):
        """有效獨立觀測不足時,即使 t 很大也只能是「累積中」。"""
        h = hyp.REGISTRY[0]
        early = {"t": 9.9, "se": 0.1, "mean": 1.0, "eff_obs": 1.0, "se_blocked": False}
        self.assertIn("累積中", hyp.status(h, early))
        blocked = {"t": None, "se": None, "mean": 1.0, "eff_obs": 1.0, "se_blocked": True}
        self.assertIn("累積中", hyp.status(h, blocked))
        self.assertEqual(hyp.status(h, None), "尚無資料")

    def test_status_honours_declared_direction(self):
        """宣告方向為正時,強烈的反向結果必須判成「依宣告放棄」,不能改口說也算成功。"""
        h = dict(hyp.REGISTRY[0])
        ok = {"t": 2.5, "se": 0.1, "mean": 0.25, "eff_obs": 12.0, "se_blocked": False}
        bad = {"t": -2.5, "se": 0.1, "mean": -0.25, "eff_obs": 12.0, "se_blocked": False}
        self.assertIn("達成", hyp.status(h, ok))
        self.assertIn("放棄", hyp.status(h, bad))
        h["direction"] = "negative"
        self.assertIn("放棄", hyp.status(h, ok))
        self.assertIn("達成", hyp.status(h, bad))

    def test_no_signal_after_long_window_triggers_abandonment(self):
        h = hyp.REGISTRY[0]
        flat = {"t": 0.3, "se": 0.1, "mean": 0.03, "eff_obs": 31.0, "se_blocked": False}
        self.assertIn("放棄", hyp.status(h, flat))

    def test_chip_weights_exclude_price_and_are_frozen(self):
        """籌碼分數不得含價格因子(否則假設就不是「價 vs 籌碼」了),
        且不得綁 score.WEIGHTS——策略旋鈕一動,假設的操作定義就漂移了。"""
        self.assertNotIn("s_price", hyp.CHIP_WEIGHTS)
        self.assertNotIn("s_resil", hyp.CHIP_WEIGHTS)
        src = (ROOT / "scripts" / "hypotheses.py").read_text(encoding="utf-8")
        self.assertNotIn("from score import", src)
        self.assertNotIn("import score", src)

    def test_report_section_exists_and_is_wired(self):
        v = (ROOT / "scripts" / "validate.py").read_text(encoding="utf-8")
        self.assertIn("import hypotheses as hyp", v)
        self.assertIn("## ⑪ 事先登錄的假設", v)
        self.assertIn("hyp.spec_digest(h)", v, "報告必須每次重算雜湊並在漂移時標紅")
        self.assertIn("規格已被改動", v)


if __name__ == "__main__":
    unittest.main()
