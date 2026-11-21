"""Round-two mechanism, paired stability and selection leakage checks."""
import copy
import hashlib
import json
from pathlib import Path
import random
import statistics as st
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
import experiment_lab as lab
from tests import test_experiment_lab as first_round

rows_fixture = first_round.rows_fixture


class RoundTwoTests(unittest.TestCase):
    def setUp(self):
        self.cfg = lab.load_config()

    test_full_forward_path = first_round.ExperimentLabTests.test_full_forward_path_on_fixture_db_freezes_all_three_looks_read_only

    def result(self, delta=-.01, reduction=.2, ic=.05, days=170):
        return {'daily': {'delta_ic': {d:delta for d in range(days)},
                         'joint_delta_ic': {d:delta for d in range(days)},
                         'joint_ic': {d:ic for d in range(days)},
                         'list_change_reduction': {d:reduction for d in range(days)}}}

    def test_roster_is_two_by_two_with_three_controls(self):
        self.assertEqual(len(self.cfg['strategies']),7)
        self.assertEqual(self.cfg['comparison_reference'],'REV1')
        self.assertEqual(self.cfg['selection_candidates'],['REV1','REV1_S2','REV1_TREND25','REV1_S2_TREND25'])
        self.assertEqual(self.cfg['strategies'][0]['weights'],lab.score.WEIGHTS)
        self.assertEqual(self.cfg['stability_objective']['ic_loss_tolerance'],.02)
        self.assertEqual(self.cfg['stability_objective']['min_list_change_reduction'],.1)

    def test_mix_then_smooth_matches_manual_midrank_and_prefix(self):
        rows=rows_fixture()
        for r in rows:
            r['ret1']=(int(r['stock_id'])+int(r['date'][-2:]))%9
        signals,_=lab.build_signals(rows,self.cfg)
        history={}
        for day in sorted({r['date'] for r in rows}):
            group=[r for r in rows if r['date']==day]
            for r in group:
                sid=r['stock_id']
                ranks={key: sum(x[key]<r[key] for x in group)+(sum(x[key]==r[key] for x in group)-1)/2
                       for key in ('ret1','rs20')}
                raw=-.75*(2*ranks['ret1']/8-1)+.25*(2*ranks['rs20']/8-1)
                history.setdefault(sid,[]).append(raw)
                if day in signals:
                    self.assertEqual(signals[day]['G'][sid]['REV1_TREND25'],round(raw,2))
                    self.assertEqual(signals[day]['G'][sid]['REV1_S2_TREND25'],round(st.mean(history[sid][-2:]),2))
        prefix=[r for r in rows if r['date']<='2026-08-08']
        self.assertEqual(lab.build_signals(prefix,self.cfg)[0],{d:g for d,g in signals.items() if d<='2026-08-08'})
        random.Random(9).shuffle(rows)
        self.assertEqual(lab.build_signals(rows,self.cfg)[0],signals)

    def test_reference_is_reversal_and_constant_reference_excludes_every_pair(self):
        cal=list(range(6))
        signals={0:{'G':{str(i):{s['id']:(-i if s['id']=='REV1' else i)
                                  for s in self.cfg['strategies']} for i in range(8)}}}
        prices={(d,str(i)):100+(i if d==4 else 0) for d in cal for i in range(8)}
        results=lab.evaluate(signals,cal,prices,self.cfg,3)
        self.assertAlmostEqual(results['BASE']['daily']['delta_ic'][0],2)
        self.assertEqual(results['REV1']['daily']['delta_ic'][0],0)
        for row in signals[0]['G'].values():
            row['REV1']=0
        results=lab.evaluate(signals,cal,prices,self.cfg,3)
        self.assertTrue(all(not r['daily']['delta_ic'] for r in results.values()))

    def test_stability_is_group_paired_and_missing_reference_not_zero_filled(self):
        cal=list(range(7))
        population={str(i):{s['id']:i for s in self.cfg['strategies']} for i in range(8)}
        signals={d:{'G':copy.deepcopy(population),'H':copy.deepcopy(population)} for d in (0,1,3)}
        for row in signals[1]['G'].values():
            row['REV1']=-row['REV1']
        for row in signals[0]['H'].values():
            row['REV1']=0
        structure=lab.structural_report(signals,cal,self.cfg,cal)
        self.assertEqual(structure['REV1_S2']['daily']['list_change_reduction'],{1:1.0})
        self.assertNotIn('list_change_reduction',structure['REV1_S2']['cells'][1]['H'])
        prices={(d,str(i)):100+i*d for d in cal for i in range(8)}
        result=lab.evaluate(signals,cal,prices,self.cfg,3,structure=structure)['REV1_S2']
        self.assertEqual(result['daily']['list_change_reduction'],{1:1.0})
        self.assertAlmostEqual(result['daily']['joint_delta_ic'][1],2)
        self.assertAlmostEqual(result['daily']['delta_ic'][1],1)

    def test_selector_uses_both_tradeoffs_and_excludes_controls(self):
        cal=list(range(170))
        results={s['id']:self.result(delta=-.1) for s in self.cfg['strategies']}
        results['REV1']=self.result(delta=0,reduction=0)
        results['BASE']=self.result(delta=1,reduction=1)
        results['REV1_S2']=self.result()
        result=lab.walk_forward(results,cal,self.cfg)
        self.assertEqual(result['folds'][0]['selected'],'REV1_S2')
        for d in range(96,170):
            for metric in results['REV1_TREND25']['daily'].values():
                metric[d]=1
        changed=lab.walk_forward(results,cal,self.cfg)
        self.assertEqual(changed['folds'][0]['selected'],'REV1_S2')
        self.assertEqual(result['folds'][0]['train_tradeoff'],changed['folds'][0]['train_tradeoff'])
        for fold in changed['folds']:
            self.assertLess(fold['train_last_outcome'],fold['test_first'])
        results['REV1_S2']=self.result(delta=-.021)
        self.assertEqual(lab.walk_forward(results,cal,self.cfg)['folds'][0]['selected'],'REV1')

    def test_iteration_requires_both_replays_and_no_threshold_rewrite(self):
        cal=list(range(30))
        results={s['id']:self.result(days=30) for s in self.cfg['strategies']}
        datasets={name:{'horizons':{'3':copy.deepcopy(results)}} for name in ('replay','frozen_replay')}
        self.assertEqual(lab.iteration_decision(datasets,self.cfg,cal)['selected'],'REV1_S2')
        for c in self.cfg['selection_candidates'][1:]:
            datasets['frozen_replay']['horizons']['3'][c]=self.result(reduction=.09,days=30)
        self.assertEqual(lab.iteration_decision(datasets,self.cfg,cal)['selected'],'REV1')

    def test_fixed_looks_use_joint_samples_and_both_halves(self):
        cal=list(range(40))
        result=self.result(days=20)
        initial=lab.fixed_looks(result,cal,self.cfg)
        self.assertEqual(initial[2]['action'],'retain')
        for values in result['daily'].values():
            values.update({i:-100 for i in range(20,40)})
        self.assertEqual(initial,lab.fixed_looks(result,cal,self.cfg))
        for i in range(10,20):
            result['daily']['joint_delta_ic'][i]=-.025
        self.assertEqual(lab.fixed_looks(result,cal,self.cfg)[2]['action'],'simplify_or_extend')
        del result['daily']['joint_delta_ic'][0]
        # All decision summaries must restrict the other legs to the same dates.
        assessment=lab.assess_tradeoff(result,self.cfg,cal,min_days=1)
        self.assertTrue(all(s['n_days']==39 for s in assessment['summary'].values()))

    def test_ledger_locks_structure_as_well_as_ic(self):
        cal=list(range(30))
        result=self.result(days=20)
        result['cells']={d:{'G':{'list_change_reduction':.2,'joint_delta_ic':-.01}} for d in range(20)}
        report={'protocol':'test-v2','fingerprint':{},'config':self.cfg,'snapshot_receipts':{},
                'forward_looks':{'REV1_S2':lab.fixed_looks(result,cal,self.cfg)},
                'datasets':{'forward':{'horizons':{'3':{'REV1_S2':result}}}}}
        with tempfile.TemporaryDirectory() as folder:
            lab.freeze_reviews(folder,report,cal)
            result['daily']['list_change_reduction'][0]=.9
            report['forward_looks']['REV1_S2']=lab.fixed_looks(result,cal,self.cfg)
            with self.assertRaisesRegex(ValueError,'drift'):
                lab.freeze_reviews(folder,report,cal)

    def test_archive_manifest_matches_every_preserved_byte(self):
        folder=lab.ROOT/'reports/experiment_rounds/fast-lab-v1-20261009'
        manifest=json.loads((folder/'manifest.json').read_text(encoding='utf-8'))
        for name,receipt in manifest['files'].items():
            self.assertEqual(hashlib.sha256((folder/name).read_bytes()).hexdigest(),receipt['sha256'],name)

    def test_empty_or_misscaled_mix_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            file=Path(folder)/'cfg.json'
            for terms in ([],[{'field':'ret1','direction':-1,'weight':.75}]):
                cfg=copy.deepcopy(self.cfg)
                cfg['strategies'][-1]['raw_mix']=terms
                file.write_bytes(lab.canonical(cfg))
                with self.assertRaises(ValueError):
                    lab.load_config(file)


if __name__=='__main__':
    unittest.main()
