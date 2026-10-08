"""Independent numerical checks and adversarial short-cycle experiment contracts."""
import copy
import datetime as dt
import json
import math
from pathlib import Path
import random
import sqlite3
import statistics
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import experiment_lab as lab


def rows_fixture(days=15):
    rows = []
    for d in range(days):
        for i in range(9):
            rows.append({"date": f"2026-08-{d+1:02d}", "stock_id": str(i), "grp": "G",
                "rs20": i * .01, "down_rs20": (8-i) * .003, "vol_ratio60": 1.5,
                "turnover_pct": 2.0, "fpct_chg20": (i-4) * .5,
                "trust5_pct": ((i+d) % 9-4)*.05, "dipbuy20": 0.0,
                "ret20": (i-4) * .01, "ret1": (4-i)*.001,
                "dist_hi20": -i*.01, "dist_hi60": -.1, "margin_util_pct": 2.0,
                "margin_chg10": -.01, "margin_chg5": -.01})
    return rows


def independent_correlation(x, y):
    # Does not call rank, spearman, evaluate, or stats_ci helpers.
    def ranks(v):
        return [1 + sum(z < a for z in v) + (sum(z == a for z in v)-1)/2 for a in v]
    a, b = ranks(x), ranks(y)
    ma, mb = sum(a)/len(a), sum(b)/len(b)
    numerator = sum((u-ma)*(v-mb) for u, v in zip(a,b))
    denom = math.sqrt(sum((u-ma)**2 for u in a)*sum((v-mb)**2 for v in b))
    return numerator/denom if denom else None


class ExperimentLabTests(unittest.TestCase):
    def setUp(self):
        self.cfg = lab.load_config()

    def test_registered_roster_has_distinct_mechanisms_and_primary_three_days(self):
        self.assertEqual(self.cfg["primary_horizon"], 3)
        self.assertEqual(self.cfg["horizons"], [1,3,5])
        self.assertEqual(self.cfg["looks"], [5,10,20])
        self.assertEqual(len(self.cfg["strategies"]), 9)
        self.assertEqual(self.cfg["strategies"][0]["weights"], lab.score.WEIGHTS)

    def test_baseline_equals_formal_score_and_order_is_irrelevant(self):
        rows = rows_fixture()
        signals, _ = lab.build_signals(rows, self.cfg)
        expected = {(r[0], r[1]): r[10] for r in lab.score.calculate_scores(rows)}
        for d, groups in signals.items():
            for stocks in groups.values():
                for stock, values in stocks.items():
                    self.assertEqual(values["BASE"], expected[d, stock])
        random.Random(12).shuffle(rows)
        self.assertEqual(lab.build_signals(rows, self.cfg)[0], signals)

    def test_future_features_never_change_past_signals(self):
        rows = rows_fixture()
        full, _ = lab.build_signals(rows, self.cfg)
        cutoff = "2026-08-09"
        prefix, _ = lab.build_signals([r for r in rows if r["date"]<=cutoff], self.cfg)
        self.assertEqual(prefix, {d: v for d,v in full.items() if d<=cutoff})
        for row in rows:
            if row["date"]>cutoff:
                row["rs20"] = row["down_rs20"] = 999
        changed, _ = lab.build_signals(rows, self.cfg)
        self.assertEqual(prefix, {d:v for d,v in changed.items() if d<=cutoff})

    def test_missing_feature_requires_full_smoothing_recovery(self):
        rows = rows_fixture()
        rows[9*4]["rs20"] = None
        signals, excluded = lab.build_signals(rows, self.cfg)
        for day in (5,6,7):
            self.assertNotIn("0", signals[f"2026-08-{day:02d}"]["G"])
        self.assertIn("0", signals["2026-08-08"]["G"])
        self.assertGreater(excluded["missing_feature_or_smoothing_warmup"], 0)

    def test_missing_snapshot_day_does_not_shorten_three_day_smoothing(self):
        rows=rows_fixture()
        calendar=sorted({r['date'] for r in rows})
        rows=[r for r in rows if r['date']!='2026-08-05']
        signals,_=lab.build_signals(rows,self.cfg,calendar)
        self.assertNotIn('2026-08-06',signals)
        self.assertNotIn('2026-08-07',signals)
        self.assertIn('2026-08-08',signals)

    def test_tail_boundary_ties_cannot_pick_arbitrary_stock(self):
        values = dict(zip("abcdefgh", [0,1,2,3,4,5,5,5]))
        top, bottom = lab.tails(values)
        self.assertEqual(top, set("fgh"))
        self.assertEqual(bottom, set("ab"))
        self.assertEqual(lab.tails(dict(reversed(list(values.items())))), (top,bottom))
        self.assertEqual(lab.tails({k:0 for k in values}), (set(),set()))

    def market_fixture(self):
        days = [f"2026-09-{d+1:02d}" for d in range(9)]
        stocks = {str(i): {s["id"]: (i if s["id"]!="REV1" else -i)
                            for s in self.cfg["strategies"]} for i in range(8)}
        signals = {days[0]: {"G": stocks}}
        prices = {(d,s):100.0 for d in days for s in stocks}
        for s in stocks:
            prices[days[0], s] = 1.0
            prices[days[3], s] = 900.0
            prices[days[4], s] = 100 + 2*int(s)
        return days, signals, prices

    def test_next_open_horizon_cost_and_paired_ic_by_independent_oracle(self):
        days, signals, prices = self.market_fixture()
        result = lab.evaluate(signals, days, prices, self.cfg, 3)
        reverse = result["REV1"]["cells"][days[0]]["G"]
        target = [i*.02 for i in range(8)]
        self.assertAlmostEqual(reverse["ic"], independent_correlation(list(range(0,-8,-1)), target))
        self.assertAlmostEqual(reverse["base_ic"], 1)
        self.assertAlmostEqual(reverse["delta_ic"], -2)
        self.assertAlmostEqual(reverse["spread_pp"], -12)
        self.assertAlmostEqual(reverse["top_excess_gross_pp"], -6)
        self.assertAlmostEqual(reverse["top_excess_cost_pp"], -6-.585)
        self.assertEqual(result["REV1"]["summary"]["delta_ic"]["n_days"], 1)
        self.assertIsNone(result["REV1"]["summary"]["delta_ic"]["se"])

    def test_missing_future_price_excludes_group_before_ranking(self):
        days, signals, prices = self.market_fixture()
        del prices[days[4], "7"]
        result = lab.evaluate(signals, days, prices, self.cfg, 3)
        for candidate in result.values():
            self.assertEqual(candidate["daily"]["delta_ic"], {})
            self.assertEqual(candidate["coverage"]["missing_entry_or_exit_entire_group_excluded"], 1)

    def test_constant_candidate_excludes_both_legs_only_for_that_pair(self):
        days, signals, prices = self.market_fixture()
        for values in signals[days[0]]["G"].values():
            values["REV1"] = 0
        result = lab.evaluate(signals, days, prices, self.cfg, 3)
        self.assertIsNone(result["REV1"]["summary"].get("delta_ic"))
        self.assertEqual(result["REV1"]["coverage"]["constant_leg_or_outcome"], 1)
        self.assertEqual(result["BASE"]["summary"]["ic"]["n_days"], 1)

    def test_immature_days_cannot_become_zero_or_shorter_horizon(self):
        days, signals, prices = self.market_fixture()
        result = lab.evaluate(signals, days[:4], prices, self.cfg, 3)
        self.assertEqual(result["BASE"]["daily"]["delta_ic"], {})

    def test_hac_matches_full_calendar_quadratic_form_with_gaps(self):
        calendar = list(range(50))
        series = {d: math.sin(d*.4) for d in calendar if d%7!=0}
        result = lab.pack(series, 3, calendar)
        center = statistics.mean(series.values())
        total = sum((a-center)*(b-center)*max(0,1-abs(i-j)/3)
                    for i,a in series.items() for j,b in series.items())
        expected = math.sqrt(max(0,total))/len(series)
        self.assertAlmostEqual(result["se"], expected, places=13)
        self.assertGreater(result["episodes"], 1)

    def test_walk_forward_selector_cannot_see_future_outcomes(self):
        cal = list(range(170))
        result = {s["id"]: {"daily": {"delta_ic": {d: 0.0 for d in cal}}} for s in self.cfg["strategies"]}
        result["MOM20"]["daily"]["delta_ic"] = {d: .01 if d<96 else -1 for d in cal}
        initial = lab.walk_forward(result, cal, self.cfg)
        self.assertEqual(initial["folds"][0]["selected"], "MOM20")
        for fold in initial["folds"]:
            self.assertLess(fold["train_last_outcome"], fold["test_first"])
        for d in range(96,len(cal)):
            result["REV1"]["daily"]["delta_ic"][d] = 1
        changed = lab.walk_forward(result, cal, self.cfg)
        self.assertEqual(changed["folds"][0]["selected"], "MOM20")
        self.assertEqual(initial["folds"][0]["train"], changed["folds"][0]["train"])

    def test_actions_are_fixed_first_n_not_repeated_weekly_successes(self):
        series = {i: .03 for i in range(20)}
        result = {"daily": {"delta_ic": series}}
        first = lab.fixed_looks(result, list(range(40)), self.cfg)
        self.assertEqual([l["action"] for l in first], ["inspect", "simplify_or_extend", "retain"])
        series.update({i:-100 for i in range(20,40)})
        self.assertEqual(first, lab.fixed_looks(result, list(range(40)), self.cfg))
        self.assertEqual(lab.lab_action({i:-.06 for i in range(10)}, self.cfg)[0], "redesign")

    def test_forward_requires_after_registration_and_explicit_timeliness(self):
        reg = dt.datetime.fromisoformat(self.cfg["registered_at"])
        run = {"captured_at": (reg+dt.timedelta(days=1)).isoformat(),
               "quality_json": '{"oos_eligible":true}'}
        days = {(reg.date()+dt.timedelta(days=i)).isoformat():copy.deepcopy(run) for i in (-1,0,1,2)}
        day0,day1,day2 = [(reg.date()+dt.timedelta(days=i)).isoformat() for i in (0,1,2)]
        days[day1]["quality_json"] = '{}'
        days[day2]["quality_json"] = '{"oos_eligible":false}'
        self.assertEqual(lab.forward_dates(days,self.cfg), [day0])

    def test_registration_detects_configuration_and_helper_drift(self):
        cfg = copy.deepcopy(self.cfg)
        with tempfile.TemporaryDirectory() as directory:
            file=Path(directory)/(cfg["protocol"]+'.json')
            file.write_bytes(lab.canonical({"protocol":cfg["protocol"],"registered_at":cfg["registered_at"],"config":cfg,
                                           **lab.source_fingerprint(cfg)}))
            lab.check_registration(cfg, directory)
            cfg["practical_delta_ic"] = .001
            with self.assertRaisesRegex(ValueError, 'drift'):
                lab.check_registration(cfg,directory)
            with mock.patch.object(lab, 'source_fingerprint', return_value={}):
                with self.assertRaisesRegex(ValueError,'drift'):
                    lab.check_registration(self.cfg,directory)

    def test_registration_cannot_backdate_or_overwrite_an_existing_round(self):
        cfg=copy.deepcopy(self.cfg)
        cfg['registered_at']='2000-01-01T00:00:00+08:00'
        with tempfile.TemporaryDirectory() as folder:
            config_path=Path(folder)/'config.json'
            receipt=lab.register(cfg,config_path,folder)
            actual=json.loads(config_path.read_text(encoding='utf-8'))
            self.assertNotEqual(actual['registered_at'],cfg['registered_at'])
            self.assertEqual(receipt['registered_at'],actual['registered_at'])
            lab.check_registration(actual,folder)
            with self.assertRaisesRegex(ValueError,'already registered'):
                lab.register(actual,config_path,folder)

    def test_output_guards_cover_nested_and_case_normalized_protected_paths(self):
        for name in ('data/subfolder', 'archive/experiment', 'config/experiment', 'scripts/report'):
            with self.assertRaises(ValueError):
                lab.validate_output_paths(lab.ROOT/'data/findmind.db',lab.ROOT/name,lab.ROOT/'tmp/reviews')
        with self.assertRaises(ValueError):
            lab.validate_output_paths(lab.ROOT/'tmp/experiment_lab.json',lab.ROOT/'tmp',lab.ROOT/'tmp/reviews')
        lab.validate_output_paths(lab.ROOT/'data/findmind.db',lab.ROOT/'reports',lab.ROOT/'tmp/reviews')

    def test_first_official_selection_does_not_replace_late_first_with_correction(self):
        rows = [dict(data_date='2026-10-12', quality_json='{"oos_eligible":false}', snapshot_id='first'),
                dict(data_date='2026-10-12', quality_json='{"oos_eligible":true}', snapshot_id='later')]
        con=mock.Mock()
        con.execute.return_value=rows
        self.assertEqual(lab.evidence_status.first_official_runs(con,eligible_only=True),{})

    def test_freeze_reviews_rejects_tampering_and_disappearing_look(self):
        cal=list(range(30))
        candidate={"daily":{"delta_ic":{i:.03 for i in range(20)}},
                   "cells":{i:{"g":{"delta_ic":.03}} for i in range(20)}}
        report={"protocol":"fixture", "fingerprint":{"spec":"v1"}, "config":self.cfg,
                "forward_looks":{"MOM20":lab.fixed_looks(candidate,cal,self.cfg)},
                "snapshot_receipts":{i:{"snapshot_id":str(i)} for i in range(20)},
                "datasets":{"forward":{"horizons":{"3":{"MOM20":candidate}}}}}
        with tempfile.TemporaryDirectory() as folder:
            lab.freeze_reviews(folder,report,cal)
            lab.freeze_reviews(folder,report,cal)
            file=Path(folder)/'fixture/MOM20-005.json'
            content=json.loads(file.read_text(encoding='utf-8'))
            content['body']['look']['daily']['0']=100
            file.write_bytes(lab.canonical(content))
            with self.assertRaisesRegex(ValueError,'drift'):
                lab.freeze_reviews(folder,report,cal)
            file.unlink()
            lab.freeze_reviews(folder,report,cal)
            report['forward_looks']['MOM20'][0]['ready']=False
            with self.assertRaisesRegex(ValueError,'disappeared'):
                lab.freeze_reviews(folder,report,cal)

    def test_negative_control_is_deterministic_under_input_permutation(self):
        days, signals, prices = self.market_fixture()
        cfg={**self.cfg,'shuffle_seeds':[1,2]}
        a=lab.negative_controls(signals,days,prices,cfg,set(days))
        for groups in signals.values():
            for group,values in groups.items():
                groups[group]=dict(reversed(list(values.items())))
        self.assertEqual(a,lab.negative_controls(signals,days,prices,cfg,set(days)))
        self.assertEqual(len(a['runs']),2)
        self.assertTrue(all(r['ic'] is not None for r in a['runs']))

    def test_structure_needs_no_future_and_preserves_gaps(self):
        days, signals, _=self.market_fixture()
        signals[days[1]]=copy.deepcopy(signals[days[0]])
        signals[days[3]]=copy.deepcopy(signals[days[0]])
        for row in signals[days[1]]['G'].values():
            row['BASE']=-row['BASE']
        r=lab.structural_report(signals,days,self.cfg,days)['BASE']
        self.assertEqual(r['daily']['list_change'],{days[1]:1.0})
        self.assertEqual(r['daily']['top_jaccard'],{d:1.0 for d in signals})
        self.assertEqual(r['daily']['tie_fraction'],{d:0.0 for d in signals})

    def test_full_forward_path_on_fixture_db_freezes_all_three_looks_read_only(self):
        cfg={**self.cfg,'registered_at':'2026-08-01T00:00:00+08:00','warmup_days':0,'shuffle_seeds':[]}
        rows=rows_fixture(30)
        with tempfile.TemporaryDirectory() as folder:
            db=Path(folder)/'fixture.db'
            # Only the test fixture is writable; the analysis always opens db_ro.
            with sqlite3.connect(db) as writer:
                cols=[k for k in rows[0] if k!='grp']
                declaration=','.join('"'+k+'" '+('TEXT' if k in ('date','stock_id') else 'REAL') for k in cols)
                writer.execute('CREATE TABLE daily_metrics ('+declaration+')')
                writer.executemany('INSERT INTO daily_metrics VALUES('+','.join('?' for _ in cols)+')',
                                   [tuple(r[k] for k in cols) for r in rows])
                writer.execute('CREATE TABLE universe(stock_id TEXT,grp TEXT)')
                writer.executemany('INSERT INTO universe VALUES (?,?)',[(str(i),'G') for i in range(9)])
                writer.execute('CREATE TABLE market(date TEXT)')
                days=sorted({r['date'] for r in rows})
                writer.executemany('INSERT INTO market VALUES (?)',[(d,) for d in days])
                writer.execute('CREATE TABLE price(date TEXT,stock_id TEXT,open REAL,close REAL)')
                writer.execute('CREATE TABLE price_adj(date TEXT,stock_id TEXT,close REAL)')
                for i,d in enumerate(days):
                    for s in range(9):
                        value=100+s*i*.1+math.sin(i+s)
                        writer.execute('INSERT INTO price VALUES (?,?,?,?)',(d,str(s),value,value))
                        writer.execute('INSERT INTO price_adj VALUES (?,?,?)',(d,str(s),value))
                writer.execute('CREATE TABLE oos_snapshot_runs(snapshot_id TEXT,data_date TEXT,captured_at TEXT,'
                               'is_official INT,stock_count INT,quality_json TEXT,content_hash TEXT)')
                writer.execute('CREATE TABLE oos_signal_snapshots AS SELECT *,CAST(NULL AS TEXT) AS grp,'
                               'CAST(NULL AS TEXT) AS snapshot_id FROM daily_metrics WHERE 0')
                for d in days:
                    writer.execute('INSERT INTO oos_snapshot_runs VALUES (?,?,?,?,?,?,?)',
                                   (d,d,d+'T23:50:00+08:00',1,9,'{"oos_eligible":true}',d))
                    writer.execute('INSERT INTO oos_signal_snapshots SELECT *,?,? FROM daily_metrics WHERE date=?',
                                   ('G',d,d))
            writer.close()
            original=db.read_bytes()
            with lab.db_ro.connect(db) as con:
                report=lab.analyze(con,cfg,{'fixture':True})
            con.close()
            self.assertEqual(original,db.read_bytes())
            self.assertEqual(report['db_query_only'],1)
            self.assertEqual(report['datasets']['forward']['eligible_signal_dates'],days)
            for candidate,looks in report['forward_looks'].items():
                self.assertTrue(all(look['ready'] for look in looks),candidate)
            lab.freeze_reviews(Path(folder)/'reviews',report,days)
            lab.freeze_reviews(Path(folder)/'reviews',report,days)
            files=list((Path(folder)/'reviews'/cfg['protocol']).glob('*.json'))
            self.assertEqual(len(files),8*3)


if __name__ == '__main__':
    unittest.main()
