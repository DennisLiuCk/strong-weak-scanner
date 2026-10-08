"""Adversarial numerical contracts, independent of report wording."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validation_metrics as vm
import signal_structure as sig


class ValidationMetricsTest(unittest.TestCase):
    def test_pairs_use_identical_stocks_and_reject_constant_leg(self):
        returns = {str(i): i for i in range(7)}
        champion = {str(i): i for i in range(7)}
        challenger = {str(i): -i for i in range(6)}
        self.assertEqual(vm.paired_rank_ics(champion, challenger, returns), (1.0, -1.0))
        self.assertIsNone(vm.paired_rank_ics(champion, {s: 0 for s in returns}, returns))
        self.assertIsNone(vm.paired_rank_ics(champion, {str(i): i for i in range(5)}, returns))

    def test_leader_ties_are_order_invariant_and_baseline_counts_ties(self):
        signal = {"a": 3, "b": 3, "c": 1}
        future = {"a": 2, "b": 1, "c": 2}
        self.assertEqual(vm.leader_hit(signal, future), (0.5, 2 / 3))
        self.assertEqual(vm.leader_hit(dict(reversed(list(signal.items()))), future), (0.5, 2 / 3))

    def test_cost_uses_next_open_fixed_duration_excludes_self_and_charges_cost(self):
        days = list(range(6))
        rows = {str(i): {"tier": "strong" if i == 0 else "other"} for i in range(6)}
        prices = {(d, s): 100.0 for d in days for s in rows}
        prices[0, "0"] = 1.0  # Buying the signal close would give an absurd return.
        prices[3, "0"] = 999.0  # Must not shorten H=3 to exit day 3.
        for i, value in enumerate((110, 101, 102, 103, 104, 105)):
            prices[4, str(i)] = value
        daily, coverage = vm.fixed_hold_net_series({0: rows}, days, prices,
                                                    lambda d, s: "g", "strong", 3, 0.585)
        self.assertAlmostEqual(daily[0], 10 - 3 - 0.585)
        self.assertEqual(coverage[0], {"selected": 1, "evaluated": 1, "excluded": 0})
        prices.pop((4, "0"))
        daily, coverage = vm.fixed_hold_net_series({0: rows}, days, prices,
                                                    lambda d, s: "g", "strong", 3, 0.585)
        self.assertEqual(daily, {})
        self.assertEqual(coverage[0]["excluded"], 1)

    def test_immature_cost_day_is_not_a_zero_return(self):
        daily, coverage = vm.fixed_hold_net_series({0: {"a": {"tier": "s"}}}, [0, 1, 2],
                                                    {}, lambda d, s: "g", "s", 3, .585)
        self.assertEqual((daily, coverage), ({}, {}))

    def test_composite_rounding_preserves_mathematical_ties(self):
        a = {"s_price": 1, "s_trust": 1, "s_margin": 1}
        b = {"s_price": 2, "s_margin": -1, "s_foreign": .4}
        self.assertEqual(sig.composite_of(a), 2.6)
        self.assertEqual(sig.composite_of(b), 2.6)

    def test_top_boundary_churn_does_not_depend_on_input_order(self):
        rows = [{"stock_id": str(i), "s_price": 1, "s_resil": i % 2} for i in range(6)]
        self.assertEqual(sig.top_n_churn([rows], "resil"),
                         sig.top_n_churn([list(reversed(rows))], "resil"))


if __name__ == "__main__":
    unittest.main()
