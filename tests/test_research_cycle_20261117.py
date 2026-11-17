"""Evidence advances one declared branch, not an entire investment thesis."""
import csv
import hashlib
from collections import Counter
from decimal import Decimal
import unittest

from test_research_cycle_20261012 import ROOT, records
from test_research_cycle_20261019 import keyed

DAY = '2026-11-17'
YAGEO = 'notes/research_topics/2026-07-30_yageo_q2_earnings_call.md'
RUBIN = 'notes/research_topics/2026-07-21_nvidia_vera_rubin_production.md'
UCIE = 'notes/research_topics/2026-08-02_ucie_interoperability_ladder.md'
LIQUID = 'notes/research_topics/2026-08-02_liquid_cooling_qualification_ladder.md'
STORAGE = 'notes/research_topics/2026-08-09_ai_storage_data_plane.md'
GALLIUM = 'notes/research_topics/2026-09-10_gallium_permit_delivery.md'


class ResearchCycleNovember17Test(unittest.TestCase):
    def review_rows(self):
        with (ROOT/'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf8', newline='') as f:
            return [r for r in csv.DictReader(f) if r['review_id'].startswith('MR-2026-11-17-')]

    def test_reviews_keep_outcomes_sources_and_actual_date(self):
        rows=self.review_rows()
        self.assertEqual(len(rows),84)
        self.assertEqual(len({(r['topic_id'],r['monitor_id']) for r in rows}),84)
        self.assertEqual(Counter(r['result'] for r in rows),{'new_support':4,'not_yet_testable':79,'no_new_evidence':1})
        with (ROOT/'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf8',newline='') as f:
            carry=next(r for r in csv.DictReader(f) if r['review_id']=='MR-2026-11-18-SPHBM4-001')
        self.assertEqual((carry['checked_at'],carry['result'],carry['next_check']),
                         ('2026-11-18','not_yet_testable','2026-11-25'))
        cohort='\n'.join(sorted(r['topic_id']+'#'+r['monitor_id'] for r in rows+[carry]))
        self.assertEqual(hashlib.sha256(cohort.encode()).hexdigest(),
                         'aa8230d39b388d8d845948ad72cbedf8b68171458ea9fffa29e6d615c3c8f728')
        for r in rows:
            self.assertEqual(r['checked_at'],DAY)
            self.assertGreater(r['next_check'],DAY)
            self.assertIn('原有效期限',r['notes'])
            if r['result']=='new_support':
                self.assertTrue(r['evidence_source_ids'])
                self.assertEqual(r['claim_action'],'new_claim')
            else:
                self.assertEqual((r['evidence_source_ids'],r['claim_action']),('','none'))

    def test_new_branches_do_not_refresh_original_topic_clocks(self):
        for path in (YAGEO,RUBIN,UCIE,LIQUID,STORAGE,GALLIUM):
            meta=records(path,'research_topic')[0]
            self.assertLess(meta['last_reviewed_at'],DAY)
            self.assertLess(meta['review_due'],DAY)
            self.assertTrue(any(r['date']==DAY for r in records(path,'transition')))

    def test_quarter_cash_flow_is_cumulative_difference_and_reconciles_stock(self):
        nine=list(map(Decimal,('27891320','5119877','-36085641','8627481','416902')))
        half=list(map(Decimal,('16478788','2943267','-45074871','94040886','577198')))
        q=[a-b for a,b in zip(nine,half)]
        self.assertEqual(q[0]-q[1],Decimal('9235922'))
        self.assertEqual(sum((q[0],q[2],q[3],q[4])),Decimal('82323546')-Decimal('147495485'))
        self.assertEqual(sum(map(Decimal,('82323546','6908595','35815046'))),Decimal('125047187'))
        self.assertEqual(Decimal('125047187')-Decimal('200717783'),Decimal('-75670596'))
        c=keyed(YAGEO,'research_claim','claim_id')
        self.assertEqual(c['C18']['label'],'inference')
        self.assertEqual(c['C16']['label'],'unverified')
        self.assertIn('640',c['C19']['claim'])

    def test_original_or_monitor_keeps_open_definition_question(self):
        m=keyed(YAGEO,'monitoring_item','monitor_id')['T6']
        self.assertEqual(m['status'],'active')
        self.assertIn('或下一季文件',m['trigger'])
        row=next(r for r in self.review_rows() if r['topic_id'].endswith('YAGEO-Q2-EARNINGS-CALL') and r['monitor_id']=='T6')
        self.assertEqual(row['result'],'new_support')
        self.assertIn('OR第二分支',row['notes'])
        self.assertIn('640',row['notes'])

    def test_gallium_two_monitors_remain_one_source_chain(self):
        rows=[r for r in self.review_rows() if r['topic_id'].endswith('GALLIUM-PERMIT-DELIVERY')]
        self.assertEqual(len(rows),2)
        self.assertEqual({r['evidence_source_ids'] for r in rows},{'S5'})
        s=keyed(GALLIUM,'research_source','source_id')['S5']
        self.assertIn('403',s['limitation'])
        text=(ROOT/GALLIUM).read_text(encoding='utf8')
        self.assertIn('兩張表不能直接交叉相乘',text)
        self.assertIn('11月17日更新另採S5',text)

    def test_ucie_new_standard_is_not_silicon_acceptance(self):
        c=keyed(UCIE,'research_claim','claim_id')
        self.assertEqual(c['C15']['label'],'verified')
        self.assertIn('規格',c['C15']['claim'])
        self.assertIn('silicon',c['C15']['boundary'])
        self.assertEqual(keyed(UCIE,'monitoring_item','monitor_id')['T4']['next_check'],'2026-11-24')
        edges=keyed('notes/knowledge_graph/ucie_interoperability.md','knowledge_edge','edge_id')
        self.assertIn('KG-UCI-I15',edges)

    def test_liquid_cooling_shipment_does_not_merge_different_models(self):
        c=keyed(LIQUID,'research_claim','claim_id')
        self.assertIn('250億元',c['C46']['claim'])
        self.assertIn('全年',c['C46']['claim'])
        self.assertIn('380kW',c['C47']['boundary'])
        self.assertEqual(c['C48']['label'],'inference')
        edge=keyed('notes/knowledge_graph/liquid_cooling.md','knowledge_edge','edge_id')['KG-LC-C11']
        self.assertEqual(edge['commercial_stage'],'shipment')
        self.assertEqual(edge['exclusivity'],'unknown')

    def test_rubin_supply_statement_does_not_verify_benchmark_rerun(self):
        c=keyed(RUBIN,'research_claim','claim_id')
        self.assertIn('Available',c['C29']['claim'])
        self.assertIn('未經MLCommons',c['C30']['claim'])
        self.assertIn('不刷新C11',c['C31']['boundary'])
        self.assertIn('不是對每家',c['C31']['boundary'])

    def test_phison_mix_keeps_broad_denominator_and_previous_quarter(self):
        c=keyed(STORAGE,'research_claim','claim_id')
        self.assertIn('57%',c['C32']['claim'])
        self.assertIn('38%',c['C32']['basis'])
        self.assertIn('Pascari',c['C32']['boundary'])
        self.assertIn('C27',c)

    def test_partial_scan_and_method_limits_are_preserved(self):
        with (ROOT/'notes/research_topics/scan_log.csv').open(encoding='utf8',newline='') as f:
            row=next(r for r in csv.DictReader(f) if r['scan_id']=='scan-2026-11-17-evidence-stage-and-cash-bridge')
        self.assertEqual(row['scope'],'partial')
        for term in ('85','21列16公司','12found','11/16','SPHBM4'):
            self.assertIn(term,row['coverage_note'])
        text=(ROOT/'MARKET_RESEARCH_METHOD.md').read_text(encoding='utf8')
        for term in ('累計轉單季','邊際表','事後增加門檻','未執行寫成查無新證據'):
            self.assertIn(term,text)


if __name__=='__main__':
    unittest.main()
