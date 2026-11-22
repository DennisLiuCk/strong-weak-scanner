from contextlib import closing
import hashlib
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import audit_experiment_lab as audit
import db_ro
import experiment_lab as lab
import fetch_daily


class IntervalReturnsTest(unittest.TestCase):
    def fixture(self, path):
        days = ['2026-10-15', '2026-10-16', '2026-10-19', '2026-10-20', '2026-10-21', '2026-10-22', '2026-11-18']
        with closing(sqlite3.connect(path)) as con, con:
            con.executescript('''CREATE TABLE market(date TEXT);
                CREATE TABLE universe(stock_id TEXT, grp TEXT);
                CREATE TABLE daily_metrics(date TEXT, stock_id TEXT);
                CREATE TABLE price(date TEXT,stock_id TEXT,open REAL,close REAL);
                CREATE TABLE price_adj(date TEXT,stock_id TEXT,close REAL);
                CREATE TABLE dividend_result(date TEXT,stock_id TEXT,before_price REAL,reference_price REAL);
                CREATE TABLE split_event(date TEXT,stock_id TEXT,before_price REAL,after_price REAL);
                CREATE TABLE oos_snapshot_runs(snapshot_id TEXT,data_date TEXT,captured_at TEXT,
                    is_official INT,stock_count INT,quality_json TEXT,content_hash TEXT);''')
            con.executemany('INSERT INTO market VALUES (?)', [(d,) for d in days])
            con.executemany('INSERT INTO universe VALUES (?,?)', [(s, 'G') for s in ('2344', '5351', 'A', 'B', 'C', 'D')])
            for d in days:
                for sid in ('2344', '5351', 'A', 'B', 'C', 'D'):
                    opening = 157.5 if sid == '2344' else 100.0
                    if d == days[4] and sid in ('A', 'B'):
                        opening += 10 if sid == 'A' else -10
                    if d == days[4] and sid in ('C', 'D'):
                        opening += 20 if sid == 'C' else -20
                    close = (161.5 if d == days[1] else 159.5) if sid == '2344' else opening
                    if d >= days[5] and sid == '2344':
                        close = 110.5
                    con.execute('INSERT INTO price VALUES (?,?,?,?)', (d, sid, opening, close))
            fetch_daily.build_price_adj(con)
        return days

    def result(self, path, days):
        with closing(db_ro.connect(path)) as con:
            loaded = lab.load_inputs(con)
        stocks = {s: {'BASE': i, 'ALT': 5-i} for i, s in enumerate(('2344', '5351', 'A', 'B', 'C', 'D'))}
        cfg = {'strategies': [{'id': 'BASE'}, {'id': 'ALT'}], 'min_group': 2, 'cost_pp': .585}
        kwargs = {'events': loaded[6]} if len(loaded) > 6 else {}
        result = lab.evaluate({days[0]: {'G': stocks}}, days, loaded[5], cfg, 3, **kwargs)
        if len(loaded) > 6:
            self.assertEqual(lab.interval_return(loaded[5], loaded[6], days[1], days[4], '2344'), 0)
            self.assertEqual(lab.interval_return(loaded[5], loaded[6], days[1], days[4], '5351'), 0)
        return result

    def test_later_dividend_preserves_forward_returns_ic_and_tie(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'fixture.db'
            days = self.fixture(path)
            before = self.result(path, days)
            with closing(sqlite3.connect(path)) as con, con:
                con.execute('INSERT INTO dividend_result VALUES (?,?,?,?)', ('2026-11-18', '2344', 110.5, 108.5))
                fetch_daily.build_price_adj(con)
            self.assertEqual(before, self.result(path, days))

    def test_interval_boundaries_split_dividend_and_invalid_events(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'fixture.db'
            days = self.fixture(path)
            with closing(sqlite3.connect(path)) as con, con:
                con.executemany('INSERT INTO dividend_result VALUES (?,?,?,?)', [
                    (days[1], 'A', 100, 50), (days[2], 'A', 100, 90),
                    (days[4], 'A', 100, 80), (days[5], 'A', 100, 50),
                    (days[3], 'A', 100, 200), (days[3], 'B', 0, 50)])
                con.executemany('INSERT INTO split_event VALUES (?,?,?,?)', [
                    (days[3], 'A', 100, 50), (days[2], 'B', 100, 1)])
            with closing(db_ro.connect(path)) as con:
                loaded = lab.load_inputs(con)
            opening, events = loaded[5:]
            self.assertAlmostEqual(lab.interval_return(opening, events, days[1], days[4], 'A'), 1.1 / (.9 * .5 * .8) - 1)
            self.assertAlmostEqual(lab.interval_return(opening, events, days[1], days[4], 'B'), -.1)
            self.assertIsNone(lab.interval_return({}, events, days[1], days[4], 'A'))
            self.assertEqual(lab.interval_return(opening, {}, days[1], days[4], '2344'), 0)

    def test_audit_matches_without_lab_return_helper(self):
        cfg = {**lab.load_config(), 'warmup_days': 0, 'shuffle_seeds': []}
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'fixture.db'
            days = self.fixture(path)
            stocks = {s: {spec['id']: i for spec in cfg['strategies']}
                      for i, s in enumerate(('2344', '5351', 'A', 'B', 'C', 'D'))}
            cfg['min_group'] = 2
            signals = {days[0]: {'G': stocks}}
            with closing(sqlite3.connect(path)) as con, con:
                con.execute('INSERT INTO dividend_result VALUES (?,?,?,?)', (days[3], 'A', 100, 90))
                con.execute('INSERT INTO split_event VALUES (?,?,?,?)', (days[4], 'B', 100, 50))
            with closing(db_ro.connect(path)) as con, mock.patch.object(lab, 'build_signals', return_value=(signals, {})):
                report = lab.analyze(con, cfg, {})
                with mock.patch.object(lab, 'interval_return', side_effect=AssertionError('audit must be independent')):
                    result = audit.audit(con, report)
            self.assertTrue(result['ok'])
            self.assertLessEqual(result['max_absolute_error'], 1e-10)

    def test_v2_archive_and_original_reviews_match_manifest(self):
        folder = lab.ROOT / 'reports/experiment_rounds/fast-lab-v2-20261009'
        manifest = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
        report = json.loads((folder / 'experiment_lab.json').read_text(encoding='utf-8'))
        acceptance = json.loads((folder / 'experiment_lab_acceptance.json').read_text(encoding='utf-8'))
        self.assertEqual(manifest['db_sha256'], report['db_sha256'])
        self.assertEqual(manifest['db_sha256'], acceptance['db_sha256'])
        self.assertEqual(acceptance['report_sha256'], hashlib.sha256((folder / 'experiment_lab.json').read_bytes()).hexdigest())
        for name, receipt in manifest['files'].items():
            self.assertEqual(hashlib.sha256((folder / name).read_bytes()).hexdigest(), receipt['sha256'], name)
            if name.startswith('experiment_reviews/'):
                self.assertEqual(hashlib.sha256((lab.ROOT / receipt['original']).read_bytes()).hexdigest(), receipt['sha256'])
