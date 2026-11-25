"""Publication progress never substitutes for task completion or product evidence."""
import csv
import hashlib
import json
import unittest
from collections import Counter

from test_research_cycle_20261012 import ROOT, records
from test_research_cycle_20261019 import keyed

DAY = '2026-11-25'
MEMORY = 'notes/research_topics/2026-08-02_ai_memory_hierarchy.md'
CPO = 'notes/research_topics/2026-08-01_cpo_pluggable_coexistence.md'
PENDING = {
    'MI-2026-07-29-PRIORITY-Q2-DISCLOSURES#T9',
    'MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL#T5',
    'MI-2026-07-31-MISSED-PRIORITY-Q2#T11',
}


class ResearchCycleNovember25Test(unittest.TestCase):
    def reviews(self):
        with (ROOT/'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf8', newline='') as stream:
            return [r for r in csv.DictReader(stream) if r['review_id'].startswith('MR-2026-11-25-')]

    def test_frozen_74_keeps_three_unstarted_tasks_due(self):
        rows = self.reviews()
        pairs = {r['topic_id']+'#'+r['monitor_id'] for r in rows}
        self.assertEqual(len(rows), 71)
        self.assertEqual(len(pairs), 71)
        self.assertFalse(pairs & PENDING)
        self.assertEqual(hashlib.sha256('\n'.join(sorted(pairs | PENDING)).encode()).hexdigest(),
                         '4861ca259425686ba2102d9bd8179cabc498e38e47d1ecb6de860e1f9078cd17')
        self.assertEqual(Counter(r['result'] for r in rows), {'not_yet_testable':68, 'no_new_evidence':3})
        for row in rows:
            self.assertEqual(row['checked_at'], DAY)
            self.assertEqual((row['claim_action'],row['evidence_source_ids']), ('none',''))
            self.assertIn('原有效期限', row['notes'])

    def test_hp_revenue_units_and_accounting_do_not_prove_memory_causality(self):
        claims = keyed(MEMORY, 'research_claim', 'claim_id')
        for marker in ('14%', '29%', '3.0%', 'non-GAAP', '股票薪酬'):
            self.assertIn(marker, claims['C47']['claim'])
        self.assertIn('不由營收除台數', claims['C47']['boundary'])
        self.assertEqual(claims['C48']['label'], 'inference')
        source = keyed(MEMORY, 'research_source', 'source_id')['S36']
        self.assertEqual((source['published_at'], source['accepted_at']), ('2026-11-24', DAY))
        self.assertIn('不是伺服器或HBM', source['limitation'])

    def test_cpo_same_deployment_is_one_chain_with_per_switch_denominator(self):
        sources = keyed(CPO, 'research_source', 'source_id')
        self.assertEqual(sources['S26']['independence_group'], sources['S27']['independence_group'])
        claim = keyed(CPO, 'research_claim', 'claim_id')['C30']
        self.assertIn('每台交換器', claim['claim'])
        self.assertIn('GPU數不是switch或link分母', claim['boundary'])
        self.assertIn('不刷新C9', claim['boundary'])

    def test_product_label_does_not_solve_cabling_conflict(self):
        claims = keyed(CPO, 'research_claim', 'claim_id')
        self.assertIn('Prototype', claims['C23']['claim'])
        self.assertEqual(claims['C31']['as_of'], '2026-11-24')
        self.assertIn('P-Rel', claims['C31']['claim'])
        for marker in ('144 MPO', '兩個ports', '總144 ports', '72nd'):
            self.assertIn(marker, claims['C31']['basis'])
        self.assertIn('不將P-Rel自行展開', claims['C31']['boundary'])
        self.assertIn('沒有新附件不等於部署失敗', keyed(CPO, 'monitoring_item', 'monitor_id')['T8']['invalidation'])

    def test_radar_frozen_choices_and_partial_census_are_preserved(self):
        radar = 'notes/research_candidates/2026-09-13_verification_gaps.md'
        candidates = keyed(radar, 'research_candidate', 'candidate_id')
        glass = candidates['RC-GLASS-CORE-CUSTOMER-RELEASE']
        self.assertEqual((glass['rank'],glass['status']), ('3','watch'))
        self.assertGreaterEqual(glass['next_check'], '2026-12-09')
        self.assertEqual(records(radar, 'research_radar')[0]['selection_cycle_id'], 'RS-2026-09-13-01')
        with (ROOT/'notes/research_topics/scan_log.csv').open(encoding='utf8', newline='') as stream:
            scan = next(r for r in csv.DictReader(stream) if r['scan_id']=='scan-2026-11-25-product-state-and-denominators')
        self.assertEqual(scan['scope'], 'partial')
        for marker in ('15列10公司','均缺11/23與11/25','不等六份季報已驗','3項不產review'):
            self.assertIn(marker, scan['coverage_note'])

    def test_snapshot_does_not_turn_side_claims_into_supported_theses(self):
        old = json.loads((ROOT/'notes/research_method_reviews/2026-11-23_01.json').read_text(encoding='utf8'))
        new = json.loads((ROOT/'notes/research_method_reviews/2026-11-25_01.json').read_text(encoding='utf8'))
        self.assertEqual(new['corrections']['monitorReviewEvents']-old['corrections']['monitorReviewEvents'], 71)
        self.assertEqual(new['corrections']['resultCounts']['new_support'], old['corrections']['resultCounts']['new_support'])
        self.assertEqual(new['monitors']['dueOrOverdue'], 3)
        self.assertEqual(new['freshness']['staleTopics'], 42)


if __name__ == '__main__':
    unittest.main()
