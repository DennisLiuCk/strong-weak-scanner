"""Keep evidence scopes, event dates and original monitor predicates distinct."""
import csv
import hashlib
import json
from collections import Counter
from decimal import Decimal
import unittest

from test_research_cycle_20261012 import ROOT, records
from test_research_cycle_20261019 import keyed

DAY = '2026-11-18'
CAPEX = 'notes/research_topics/2026-08-01_ai_capex_cash_conversion.md'
HELIOS = 'notes/research_topics/2026-08-02_amd_helios_deployment_ladder.md'
RUBIN = 'notes/research_topics/2026-07-21_nvidia_vera_rubin_production.md'


class ResearchCycleNovember18EveningTest(unittest.TestCase):
    def reviews(self):
        with (ROOT/'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf8', newline='') as f:
            return [r for r in csv.DictReader(f) if r['review_id'].startswith('MR-2026-11-18-EVENING-')]

    def test_due_cohort_is_complete_and_early_event_separate(self):
        rows=self.reviews()
        self.assertEqual(len(rows),12)
        self.assertEqual(len({(r['topic_id'],r['monitor_id']) for r in rows}),12)
        due=[r for r in rows if '-RUBIN-' not in r['review_id']]
        self.assertEqual(len(due),11)
        cohort='\n'.join(sorted(r['topic_id']+'#'+r['monitor_id'] for r in due))
        self.assertEqual(hashlib.sha256(cohort.encode()).hexdigest(),
                         '9a701e986cb2a24600fa9377a9c2bf3e5541b7e048580768a535e03447c56f34')
        self.assertEqual(Counter(r['result'] for r in due),{'not_yet_testable':10,'no_new_evidence':1})
        for r in rows:
            self.assertEqual(r['checked_at'],DAY)
            self.assertGreater(r['next_check'],DAY)
            self.assertLessEqual(r['next_check'],'2026-11-25')
            self.assertIn('原有效期限',r['notes'])
        early=next(r for r in rows if '-RUBIN-' in r['review_id'])
        self.assertEqual((early['result'],early['evidence_source_ids'],early['next_check']),
                         ('new_support','S30|S31|S32','2026-11-24'))
        self.assertIn('不屬11項凍結',early['notes'])

    def test_side_claim_does_not_weaken_payment_event_predicate(self):
        row=next(r for r in self.reviews() if r['topic_id'].endswith('AI-CAPEX-CASH-CONVERSION'))
        self.assertEqual((row['result'],row['claim_action'],row['evidence_source_ids']),
                         ('not_yet_testable','none',''))
        m=keyed(CAPEX,'monitoring_item','monitor_id')
        self.assertIn('或具體ready-for-service',m['T5']['trigger'])
        self.assertIn('NVIDIA付款與OpenAI reimbursement',m['T5']['trigger'])
        self.assertEqual(m['T5']['next_check'],'2026-09-04')
        self.assertEqual(m['T7']['next_check'],'2026-11-25')
        c=keyed(CAPEX,'research_claim','claim_id')
        self.assertIn('尚未支付',c['C37']['claim'])
        self.assertIn('不是銀行獨立確認',c['C37']['boundary'])
        self.assertEqual(c['C39']['label'],'unverified')

    def test_commitment_table_and_contingent_exposure_are_not_current_cash(self):
        table=[[69,203,92,10,8,8],[2,7,7,6,4,2],[0,1,2,4,4,63],
               [5,11,2,2,0,0],[6,0,0,0,0,0]]
        self.assertEqual([sum(r) for r in table],[390,28,74,20,6])
        self.assertEqual([sum(c) for c in zip(*table)],[82,222,103,22,16,73])
        self.assertEqual(sum(map(sum,table)),518)
        self.assertEqual(sum([0,6,7,6,5,8]),32)
        self.assertEqual(sum(map(Decimal,('3.5','105.0','9.5'))),Decimal('118.0'))
        c=keyed(CAPEX,'research_claim','claim_id')
        self.assertIn('105再次加進118',c['C38']['claim'])
        self.assertIn('同一欄',c['C38']['basis'])
        source=keyed(CAPEX,'research_source','source_id')['S30']
        self.assertIn('2026-10-25',source['locator'])
        self.assertIn('不是10-Q',source['limitation'])

    def test_helios_procedure_is_not_same_configuration_acceptance(self):
        c=keyed(HELIOS,'research_claim','claim_id')
        self.assertIn('程序',c['C34']['claim'])
        self.assertIn('不是具名場站已通過',c['C34']['boundary'])
        for term in ('HDv2','MI300X','MI455X'):
            self.assertIn(term,c['C35']['claim'])
        edge=keyed('notes/knowledge_graph/amd_helios.md','knowledge_edge','edge_id')['KG-HEL-C02']
        self.assertEqual(edge['commercial_stage'],'validation')

    def test_operator_event_publication_and_capture_dates_are_distinct(self):
        c=keyed(RUBIN,'research_claim','claim_id')
        self.assertIn('計畫',c['C32']['claim'])
        self.assertIn('10月22日',c['C33']['claim'])
        self.assertEqual(c['C33']['as_of'],'2026-11-06')
        self.assertIn('a5x-highgpu-4g-metal',c['C34']['claim'])
        self.assertIn('預留容量',c['C34']['claim'])
        s=keyed(RUBIN,'research_source','source_id')
        self.assertEqual(s['S31']['published_at'],'2026-10-22')
        self.assertEqual(s['S31']['captured_at'],DAY)
        self.assertIn('10/21',s['S31']['limitation'])
        self.assertEqual(s['S31']['independence_group'],s['S32']['independence_group'])

    def test_unavailable_page_is_not_unchanged_product_state(self):
        row=next(r for r in self.reviews() if r['topic_id'].endswith('LIQUID-COOLING-QUALIFICATION-LADDER'))
        self.assertEqual(row['result'],'not_yet_testable')
        self.assertIn('timeout',row['notes'])
        self.assertIn('不能代表平台刪除',row['notes'])
        self.assertEqual((row['evidence_source_ids'],row['claim_action']),('','none'))

    def test_partial_scan_does_not_hide_missing_day(self):
        with (ROOT/'notes/research_topics/scan_log.csv').open(encoding='utf8',newline='') as f:
            row=next(r for r in csv.DictReader(f) if r['scan_id']=='scan-2026-11-18-commitments-and-service-gates')
        self.assertEqual((row['window_start'],row['window_end'],row['scope']),('2026-11-17',DAY,'partial'))
        for term in ('13列6公司','只覆蓋兩市場11/17','6213','5234','正式簽核'):
            self.assertIn(term,row['coverage_note'])

    def test_append_only_snapshot_retains_old_staleness(self):
        old=json.loads((ROOT/'notes/research_method_reviews/2026-11-18_01.json').read_text(encoding='utf8'))
        new=json.loads((ROOT/'notes/research_method_reviews/2026-11-18_02.json').read_text(encoding='utf8'))
        self.assertEqual(old['corrections']['monitorReviewEvents'],1273)
        self.assertEqual(new['corrections']['monitorReviewEvents'],1285)
        self.assertEqual(new['freshness']['staleTopics'],42)
        self.assertEqual(new['freshness']['staleEdges'],870)
        for path in (CAPEX,HELIOS,RUBIN):
            meta=records(path,'research_topic')[0]
            self.assertLess(meta['last_reviewed_at'],DAY)
            self.assertLess(meta['review_due'],DAY)
            self.assertTrue(any(t['date']==DAY for t in records(path,'transition')))


if __name__=='__main__':
    unittest.main()
