"""Economic ties must not depend on SQL insertion order or stock identifiers."""
import itertools
from pathlib import Path
import random
import sys
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import score


def rows_for(values, *, day="2026-10-12", chips=True, resilience=True):
    return [{
        "date": day, "stock_id": f"S{i}", "grp": "g", "rs20": value,
        "down_rs20": value if resilience else None,
        "fpct_chg20": value * 10 if chips else 0,
        "trust5_pct": value * 10 if chips else 0, "dipbuy20": 0,
        "vol_ratio60": 1.0, "turnover_pct": 1.0,
        "margin_chg10": 0, "margin_chg5": 0, "margin_util_pct": 1,
        "ret20": .01, "dist_hi60": 0,
    } for i, value in enumerate(values)]


class MidrankScoreTest(unittest.TestCase):
    def test_exact_factor_ties_share_average_position(self):
        self.assertEqual(score.rank_scores([.5] * 5, score.DZ_FOREIGN), [0] * 5)
        values = [1, 2, 2, 3, 4, None]
        expected = score.rank_scores(values)
        self.assertEqual(expected[1], expected[2])
        self.assertEqual(expected[-1], 0)
        for indices in itertools.permutations(range(len(values))):
            actual = score.rank_scores([values[i] for i in indices])
            self.assertEqual(dict(zip(indices, actual)), dict(enumerate(expected)))
        self.assertEqual(score.rank_scores([None, 1, 2, 3]), [0] * 4)
        self.assertEqual(score.rank_scores([0, .001, -.001, .002], .03), [0] * 4)

    def test_top_two_boundary_tie_excludes_both_middle_ranks(self):
        result = score.calculate_scores(rows_for([.4, .3, .3, .2, .1, 0]))
        raw = {row[1]: row[11] for row in result}
        self.assertEqual(raw["S0"], "真強")
        self.assertEqual(raw["S1"], "潛在/中性")
        self.assertEqual(raw["S2"], "潛在/中性")
        self.assertEqual(result[1][10], result[2][10])

    def test_three_way_top_tie_has_midrank_two_and_equal_eligibility(self):
        result = score.calculate_scores(rows_for([.3, .3, .3, .2, .1, 0]))
        self.assertTrue(all(row[11] == "真強" for row in result[:3]))

    def test_bottom_boundary_tie_is_symmetric(self):
        rows = rows_for([.6, .5, .4, .1, .1, 0], chips=False, resilience=False)
        result = score.calculate_scores(rows)
        self.assertEqual([row[11] for row in result[-3:]], ["潛在/中性", "潛在/中性", "真弱"])

    def test_full_scores_smoothing_and_hysteresis_are_permutation_invariant(self):
        rows = []
        for day, values in (("2026-10-12", [.4, .3, .3, .2, .1, 0]),
                            ("2026-10-13", [.3, .3, .3, .2, .1, 0]),
                            ("2026-10-14", [.1, .1, .4, .3, .2, 0]),
                            ("2026-10-15", [.4, .3, .3, .2, .1, 0])):
            rows.extend(rows_for(values, day=day))
        expected = score.calculate_scores(rows)
        for seed in range(12):
            permuted = rows[:]
            random.Random(seed).shuffle(permuted)
            self.assertEqual(score.calculate_scores(permuted), expected)

    def test_score_version_fingerprint_covers_helpers_and_runtime_config(self):
        baseline = score.score_spec_digest()
        self.assertEqual(score.SCORE_EFFECTIVE_FROM, "2026-10-09")
        with mock.patch.object(score, "average_ranks", lambda values: list(range(len(values)))):
            self.assertNotEqual(score.score_spec_digest(), baseline)
        with mock.patch.dict(score.WEIGHTS, {"resil": .5}):
            self.assertNotEqual(score.score_spec_digest(), baseline)
        self.assertEqual(score.score_spec_digest(), baseline)


if __name__ == "__main__":
    unittest.main()
