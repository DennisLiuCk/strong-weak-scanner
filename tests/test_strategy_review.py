"""Guard the evidence boundary and aggregation used by the read-only review."""
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import db_ro
import ranking_views as rv
import strategy_review as review
import score


class ReviewMathTest(unittest.TestCase):
    def test_challenger_uses_same_stock_set_with_missing_components(self):
        returns = {str(i): i for i in range(7)}
        champion = {str(i): i for i in range(7)}
        challenger = {str(i): -i for i in range(7)}
        champion['6'] = -1000  # Would distort an unmatched Champion IC.
        challenger['6'] = None
        self.assertAlmostEqual(review.paired_rank_delta(champion, challenger, returns), -2)
        challenger['5'] = None
        self.assertIsNone(review.paired_rank_delta(champion, challenger, returns))

    def test_random_hit_baseline_handles_joint_winners(self):
        self.assertAlmostEqual(review.random_leader_hit_rate({'a': 1, 'b': 1, 'c': 0}), 2 / 3)

    def test_pairing_excludes_unmatched_market_days(self):
        self.assertEqual(review.paired_difference({'d1': 10, 'd2': 2}, {'d2': 1, 'd3': -10}),
                         {'d2': 1})

    def test_benchmark_excludes_self_only_when_requested(self):
        returns = {'a': -1, 'b': 1, 'c': 3, 'd': 4}
        self.assertEqual(review.peer_excess(returns, 'a'), -3)
        self.assertEqual(review.peer_excess(returns, 'a', exclude_self=True), -4)

    def test_summary_keeps_gaps_and_blocks_small_sample_se(self):
        result = review.summary({'d1': 0.1, 'd3': 0.3}, 10, ['d1', 'd2', 'd3'], 'rank_ic')
        self.assertEqual(result['n_days'], 2)
        self.assertEqual(result['episodes'], 2)
        self.assertIsNone(result['se'])
        self.assertAlmostEqual(result['mean'], 0.2)

    def test_calendar_hac_equals_repo_for_contiguous_days_but_not_across_gaps(self):
        xs = [-3, -2, -1, 1, 2, 3]
        contiguous = {f'd{i}': x for i, x in enumerate(xs)}
        self.assertAlmostEqual(review.calendar_hac_se(contiguous, 2, list(contiguous)),
                               review.sci.nw_se(xs, 1))
        gapped = dict(zip(['d0', 'd1', 'd2', 'd6', 'd7', 'd8'], xs))
        gap_se = review.calendar_hac_se(gapped, 2, [f'd{i}' for i in range(9)])
        # Across-gap pair (-1,+1) has no covariance weight. Diagonal 28,
        # adjacent within-segment products 6+2+2+6, divided by n^2.
        self.assertAlmostEqual(gap_se, (44 / 36) ** 0.5)
        self.assertGreater(gap_se, review.sci.nw_se(xs, 1))


class SnapshotBoundaryTest(unittest.TestCase):
    def test_late_first_release_cannot_be_replaced_and_current_universe_is_not_used(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'fixture.db'
            # Only fixture creation is writable. The reviewed connection is db_ro.
            con = sqlite3.connect(path)
            con.executescript('''
                CREATE TABLE daily_metrics(date, stock_id, close_adj);
                CREATE TABLE oos_snapshot_runs(snapshot_id, data_date, captured_at,
                                                is_official, quality_json);
                CREATE TABLE oos_signal_snapshots(snapshot_id, stock_id, grp);
                CREATE TABLE oos_group_snapshots(snapshot_id, grp);
                CREATE TABLE oos_ranking_view_snapshots(snapshot_id, stock_id, spec_sha);
                CREATE TABLE price(date, stock_id, open, close);
                CREATE TABLE price_adj(date, stock_id, close);
            ''')
            for day in ('2026-10-12', '2026-10-13', '2026-10-14'):
                con.execute('INSERT INTO daily_metrics VALUES(?,?,?)', (day, 'old_member', 100))
            for snap, day, captured, eligible in (
                ('late', '2026-10-12', '01', False),
                ('replacement', '2026-10-12', '02', True),
                ('original', '2026-10-13', '01', True),
                ('revision', '2026-10-13', '02', True),
                ('future', '2026-10-14', '01', True),
            ):
                con.execute('INSERT INTO oos_snapshot_runs VALUES(?,?,?,?,?)',
                            (snap, day, captured, 1, json.dumps({'oos_eligible': eligible,
                                                               'score_spec_sha': score.score_spec_digest()})))
                con.execute('INSERT INTO oos_signal_snapshots VALUES(?,?,?)',
                            (snap, 'old_member', snap + '_group'))
                con.execute('INSERT INTO oos_group_snapshots VALUES(?,?)', (snap, snap + '_group'))
                con.execute('INSERT INTO oos_ranking_view_snapshots VALUES(?,?,?)',
                            (snap, 'old_member', 'old-spec' if snap == 'original' else rv.SPEC_SHA))
            con.commit()
            con.close()
            con = db_ro.connect(path)
            try:
                cal, runs, signals, groups, rankings, close, opening = review.load_inputs(con, '2026-10-13')
                self.assertEqual(cal, ['2026-10-12', '2026-10-13'])
                self.assertEqual(list(runs), ['2026-10-13'])
                self.assertEqual(runs['2026-10-13']['snapshot_id'], 'original')
                self.assertEqual(signals['2026-10-13']['old_member']['grp'], 'original_group')
                self.assertEqual(rankings['2026-10-13'], {})
                with self.assertRaises(sqlite3.OperationalError):
                    con.execute('DELETE FROM oos_snapshot_runs')
            finally:
                con.close()


if __name__ == '__main__':
    unittest.main()
