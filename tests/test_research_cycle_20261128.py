"""Receipt, architecture and classification must not stand in for acceptance."""
import csv
import hashlib
import json
import unittest
from test_research_cycle_20261012 import ROOT, records
from test_research_cycle_20261019 import keyed

HELIOS = 'notes/research_topics/2026-08-02_amd_helios_deployment_ladder.md'
STORAGE = 'notes/research_topics/2026-08-09_ai_storage_data_plane.md'
PENDING = {
    'MI-2026-07-29-PRIORITY-Q2-DISCLOSURES#T9',
    'MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL#T5',
    'MI-2026-07-31-MISSED-PRIORITY-Q2#T11',
}


class ResearchCycleNovember28Test(unittest.TestCase):
    def test_due_cohort_and_unfinished_full_reviews_are_not_snoozed(self):
        with (ROOT/'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf8', newline='') as stream:
            rows = [r for r in csv.DictReader(stream) if r['review_id'].startswith('MR-2026-11-28-')]
        pairs = {r['topic_id']+'#'+r['monitor_id'] for r in rows}
        self.assertEqual((len(rows),len(pairs)),(3,3))
        self.assertFalse(pairs & PENDING)
        self.assertEqual(hashlib.sha256('\n'.join(sorted(pairs | PENDING)).encode()).hexdigest(),
                         'f2b4cf229c5ba539549404801963b40c10634721df9a5f87fed3807ece03b4cc')
        for row in rows:
            self.assertEqual((row['result'],row['claim_action'],row['evidence_source_ids']),('not_yet_testable','none',''))
            self.assertIn('原有效期限',row['notes'])

    def test_amd_reported_receipt_is_not_independent_acceptance(self):
        source = keyed(HELIOS,'research_source','source_id')['S35']
        self.assertEqual((source['publisher'],source['independence_group']),('AMD','amd'))
        claim = keyed(HELIOS,'research_claim','claim_id')['C39']
        self.assertIn('收到首台Helios',claim['claim'])
        self.assertIn('不計為獨立客戶驗收',claim['boundary'])
        self.assertIn('不證明Azure正式開放',claim['boundary'])
        edge = keyed('notes/knowledge_graph/amd_helios.md','knowledge_edge','edge_id')['KG-HEL-C02']
        self.assertEqual(edge['commercial_stage'],'validation')
        self.assertIn('#C39',edge['claim_refs'])

    def test_storage_announcement_and_research_framework_have_different_labels(self):
        claims = keyed(STORAGE,'research_claim','claim_id')
        self.assertEqual((claims['C33']['label'],claims['C34']['label']),('verified','inference'))
        self.assertIn('仍開發中',claims['C33']['claim'])
        self.assertIn('不推論所有功能都未完成',claims['C33']['boundary'])
        self.assertIn('T2與T4原AND條件不改',claims['C34']['boundary'])
        source = keyed(STORAGE,'research_source','source_id')['S28']
        self.assertIn('不是原HTML',source['locator'])
        self.assertIn('工具文字快照',source['locator'])
        self.assertEqual(source['independence_group'],'phison-issuer')

    def test_original_storage_company_edge_is_not_refreshed(self):
        edge = keyed('notes/knowledge_graph/ai_storage_data_plane.md','knowledge_edge','edge_id')['KG-ASD-C01']
        self.assertLess(edge['as_of'],'2026-11-28')
        self.assertNotIn('#C33',edge['claim_refs'])
        self.assertNotIn('#C34',edge['claim_refs'])

    def test_partial_event_coverage_preserves_unknown_index_targets(self):
        with (ROOT/'notes/research_topics/scan_log.csv').open(encoding='utf8', newline='') as stream:
            row = next(r for r in csv.DictReader(stream) if r['scan_id']=='scan-2026-11-28-receipt-design-and-classification')
        self.assertEqual(row['scope'],'partial')
        for marker in ('21列15公司','12found','8155限流即停','8210/8996未查','保留原11/25到期','missing0不當全部成功'):
            self.assertIn(marker,row['coverage_note'])

    def test_not_due_radar_does_not_reselect_frozen_candidates(self):
        path = 'notes/research_candidates/2026-09-13_verification_gaps.md'
        self.assertEqual(records(path,'research_radar')[0]['selection_cycle_id'],'RS-2026-09-13-01')
        candidates = keyed(path,'research_candidate','candidate_id')
        for rank, ident in enumerate(('RC-800V-SSCB-FAULT-ISOLATION','RC-HBFSIM-MODEL-VALIDATION','RC-GLASS-CORE-CUSTOMER-RELEASE'),1):
            self.assertEqual((candidates[ident]['rank'],candidates[ident]['status']),(str(rank),'watch'))

    def test_yageo_arithmetic_keeps_classification_unresolved(self):
        from decimal import Decimal
        amounts = [11745798,11052916,10307980,7401238,5254184,3769421]
        self.assertEqual(sum(amounts),49531537)
        self.assertEqual([str((Decimal(n)*100/49531537).quantize(Decimal('.01'))) for n in amounts],
                         ['23.71','22.31','20.81','14.94','10.61','7.61'])
        claims = keyed('notes/research_topics/2026-07-30_yageo_q2_earnings_call.md','research_claim','claim_id')
        self.assertEqual([claims[c]['label'] for c in ('C20','C21','C22')],['verified','inference','unverified'])
        self.assertIn('不證明誤植',claims['C21']['boundary'])
        self.assertIn('不解除C16',claims['C22']['boundary'])
        self.assertIn('49531537',claims['C20']['claim'])
        monitor = keyed('notes/research_topics/2026-07-30_yageo_q2_earnings_call.md','monitoring_item','monitor_id')['T7']
        self.assertEqual(monitor['source_ids'],'S6,S7')
        self.assertIn('差額調節',monitor['trigger'])
        self.assertIn('沒有說明不判造假',monitor['invalidation'])

    def test_snapshot_has_no_supported_thesis_from_side_updates(self):
        before = json.loads((ROOT/'notes/research_method_reviews/2026-11-25_01.json').read_text(encoding='utf8'))
        after = json.loads((ROOT/'notes/research_method_reviews/2026-11-28_02.json').read_text(encoding='utf8'))
        self.assertEqual(after['corrections']['monitorReviewEvents']-before['corrections']['monitorReviewEvents'],3)
        for result in ('new_support','new_contrary','no_new_evidence'):
            self.assertEqual(after['corrections']['resultCounts'][result],before['corrections']['resultCounts'][result])
        self.assertEqual(after['monitors']['dueOrOverdue'],3)
        self.assertEqual(after['freshness']['staleTopics'],42)


if __name__ == '__main__':
    unittest.main()
