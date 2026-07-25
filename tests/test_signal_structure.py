"""signal_structure 的數學契約:用合成資料釘住定義,避免日後重構把指標算歪。

這些指標會出現在每日簡報與週報 §⑦,是判讀 §4-7 單柱風險的依據——算錯比沒有更糟。
"""
import sqlite3
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import signal_structure as sig


def rows(*specs):
    """specs = [(stock_id, s_price, s_resil, s_vol, s_foreign, s_trust, s_dip, s_margin), ...]"""
    keys = ["s_price", "s_resil", "s_vol", "s_foreign", "s_trust", "s_dip", "s_margin"]
    return [dict(zip(["stock_id"] + keys, s)) for s in specs]


class SignalStructureTest(unittest.TestCase):
    def test_variance_shares_sum_to_one(self):
        g = rows(("A", 2, 1, 0, -1, 2, 0, 1), ("B", -2, 0, 1, 2, -1, 1, 0),
                 ("C", 1, -2, -1, 0, 0, -2, 2), ("D", 0, 2, 2, 1, 1, 2, -1),
                 ("E", -1, -1, 0, -2, 2, 1, 0), ("F", 2, 0, -2, 1, -2, 0, 1))
        shares = sig.variance_shares([g])
        self.assertAlmostEqual(sum(shares.values()), 1.0, places=9,
                               msg="變異貢獻分解必須完全加總為 1")

    def test_single_weight_gives_one_effective_factor(self):
        """只有一個元素有權重 → 有效因子數 = 1、composite 排名 = 該元素排名。"""
        g = rows(("A", 2, 1, 0, -1, 2, 0, 1), ("B", -2, 0, 1, 2, -1, 1, 0),
                 ("C", 1, -2, -1, 0, 0, -2, 2), ("D", 0, 2, 2, 1, 1, 2, -1),
                 ("E", -1, -1, 0, -2, 2, 1, 0), ("F", 2, 0, -2, 1, -2, 0, 1))
        only = {k: (1.0 if k == "price" else 0.0) for k in sig.WEIGHTS}
        shares = sig.variance_shares([g], only)
        self.assertAlmostEqual(sig.effective_factors(shares), 1.0, places=6)
        self.assertAlmostEqual(sig.rank_rho([g], "price", only), 1.0, places=6)

    def test_equal_weights_give_more_effective_factors_than_current(self):
        """等權(7 個)的有效因子數應高於現行(集中在 price/resil)。"""
        g = rows(("A", 2, 1, 0, -1, 2, 0, 1), ("B", -2, 0, 1, 2, -1, 1, 0),
                 ("C", 1, -2, -1, 0, 0, -2, 2), ("D", 0, 2, 2, 1, 1, 2, -1),
                 ("E", -1, -1, 0, -2, 2, 1, 0), ("F", 2, 0, -2, 1, -2, 0, 1))
        eq = {k: 1.0 for k in sig.WEIGHTS}
        self.assertGreater(sig.effective_factors(sig.variance_shares([g], eq)),
                           sig.effective_factors(sig.variance_shares([g], sig.WEIGHTS)))

    def test_dropping_zero_weight_element_changes_nothing(self):
        """權重為 0 的元素移除後,前 N 名不可能易主——否則 composite_of 有 bug。"""
        g = rows(("A", 2, 1, 0, -1, 2, 2, 1), ("B", -2, 0, 1, 2, -1, -2, 0),
                 ("C", 1, -2, -1, 0, 0, 2, 2), ("D", 0, 2, 2, 1, 1, -2, -1))
        zero = [k for k, v in sig.WEIGHTS.items() if not v]
        for k in zero:
            self.assertEqual(sig.top_n_churn([g], k), 0, f"s_{k} 權重為 0 卻改變了名次")

    def test_get_accepts_sqlite_row_and_missing_column(self):
        """validate.py 餵 sqlite3.Row(無 .get);缺欄與 NULL 都要當 0。"""
        con = sqlite3.connect(":memory:")
        con.row_factory = sqlite3.Row
        con.execute("CREATE TABLE t(stock_id TEXT, s_price INT, s_resil INT)")
        con.execute("INSERT INTO t VALUES('A', 2, NULL)")
        r = con.execute("SELECT * FROM t").fetchone()
        self.assertEqual(sig._get(r, "s_price"), 2)
        self.assertEqual(sig._get(r, "s_resil"), 0, "NULL 應視為 0")
        self.assertEqual(sig._get(r, "s_vol"), 0, "缺欄應視為 0,不得拋錯")
        self.assertEqual(sig._get({"s_price": 2}, "s_trust"), 0)
        con.close()

    def test_weights_come_from_score_config(self):
        """權重必須取自 score.WEIGHTS,不得在 signal_structure 另立一份。"""
        import score
        self.assertIs(sig.WEIGHTS, score.WEIGHTS)
        self.assertEqual(set(sig.ELEMENT_COLS.values()),
                         {f"s_{k}" for k in score.WEIGHTS})


if __name__ == "__main__":
    unittest.main()
