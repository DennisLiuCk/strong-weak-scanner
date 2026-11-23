"""Design artifacts do not silently advance product acceptance or evidence clocks."""
import csv
import hashlib
import json
import unittest

from test_research_cycle_20261012 import ROOT, records
from test_research_cycle_20261019 import keyed

DAY = '2026-11-23'
MEMORY = 'notes/research_topics/2026-08-02_ai_memory_hierarchy.md'
HELIOS = 'notes/research_topics/2026-08-02_amd_helios_deployment_ladder.md'
COOLING = 'notes/research_topics/2026-08-02_liquid_cooling_qualification_ladder.md'
CUSTOM = 'notes/research_topics/2026-08-03_custom_hbm_scope_ladder.md'


class ResearchCycleNovember23Test(unittest.TestCase):
    def reviews(self):
        with (ROOT/'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf8', newline='') as stream:
            return [r for r in csv.DictReader(stream) if r['review_id'].startswith('MR-2026-11-23-')]

    def test_frozen_due_cohort_preserves_all_23_and_boundaries(self):
        rows = self.reviews()
        self.assertEqual(len(rows), 23)
        pairs = [r['topic_id']+'#'+r['monitor_id'] for r in rows]
        self.assertEqual(len(set(pairs)), 23)
        self.assertEqual(hashlib.sha256('\n'.join(sorted(pairs)).encode()).hexdigest(),
                         '5f2c954a8a61afb3ca1ad9cd2cff24890c5408bdaa97529c25a6dc5ba5bf6e68')
        for row in rows:
            self.assertEqual(row['checked_at'], DAY)
            self.assertEqual((row['result'], row['claim_action'], row['evidence_source_ids']),
                             ('not_yet_testable', 'none', ''))
            self.assertGreater(row['next_check'], DAY)
            self.assertIn('原有效期限', row['notes'])
            self.assertIn('來源：', row['notes'])

    def test_reference_design_capacity_and_product_availability_are_separate(self):
        claims = keyed(COOLING, 'research_claim', 'claim_id')
        self.assertIn('60MW IT負載', claims['C49']['claim'])
        self.assertIn('不是單台CDU容量', claims['C49']['boundary'])
        self.assertIn('仍在開發', claims['C50']['claim'])
        self.assertIn('2027年下半年', claims['C50']['claim'])
        self.assertIn('不延伸到同稿其他設備', claims['C50']['boundary'])
        sources = keyed(COOLING, 'research_source', 'source_id')
        self.assertEqual(sources['S39']['published_at'], '2026-11-11')
        self.assertIn('11/10', sources['S39']['locator'])

    def test_static_kvcr_example_is_not_runtime_proof(self):
        claims = keyed(MEMORY, 'research_claim', 'claim_id')
        self.assertIn('靜態測試不宣稱', claims['C45']['claim'])
        self.assertIn('不是具名operator', claims['C45']['boundary'])
        sources = keyed(MEMORY, 'research_source', 'source_id')
        self.assertIn('/v1.6.0/', sources['S33']['url'])
        self.assertIn('CodeRabbit', sources['S34']['locator'])
        self.assertEqual(sources['S33']['independence_group'], sources['S34']['independence_group'])

    def test_adjacent_cxl_validation_cannot_be_borrowed_by_custom_hbm(self):
        claim = keyed(CUSTOM, 'research_claim', 'claim_id')['C20']
        self.assertIn('產品模型', claim['claim'])
        self.assertIn('預期', claim['claim'])
        self.assertIn('不是實體樣品交付', claim['boundary'])
        self.assertIn('CXL卸載', keyed(CUSTOM, 'research_source', 'source_id')['S18']['limitation'])
        self.assertEqual(keyed(MEMORY, 'research_source', 'source_id')['S35']['url'],
                         keyed(CUSTOM, 'research_source', 'source_id')['S18']['url'])

    def test_helios_scope_difference_does_not_refute_unmatched_customer_claim(self):
        claims = keyed(HELIOS, 'research_claim', 'claim_id')
        self.assertEqual(claims['C38']['as_of'], '2026-11-10')
        self.assertIn('尚未production', claims['C38']['claim'])
        self.assertIn('不refute', claims['C38']['boundary'])
        self.assertEqual(claims['C38']['contrary_source_ids'], '')
        self.assertEqual(claims['C31']['status'], 'active')
        self.assertIn('資訊截點', keyed(HELIOS, 'monitoring_item', 'monitor_id')['T16']['trigger'])

    def test_scanning_tool_is_not_new_auditor(self):
        row = next(r for r in self.reviews() if r['topic_id'].endswith('AI-RACK-TRUST-ROOT') and r['monitor_id'] == 'T2')
        self.assertIn('AI掃描harness', row['notes'])
        self.assertIn('沒有新增稽核機構', row['notes'])
        self.assertEqual(row['result'], 'not_yet_testable')

    def test_candidates_keep_frozen_rank_and_wait_for_evidence(self):
        path = 'notes/research_candidates/2026-09-13_verification_gaps.md'
        candidates = keyed(path, 'research_candidate', 'candidate_id')
        for cid, rank in [('RC-800V-SSCB-FAULT-ISOLATION', '1'), ('RC-HBFSIM-MODEL-VALIDATION', '2'), ('RC-GLASS-CORE-CUSTOMER-RELEASE', '3')]:
            self.assertEqual((candidates[cid]['rank'], candidates[cid]['status']), (rank, 'watch'))
        self.assertGreaterEqual(candidates['RC-HBFSIM-MODEL-VALIDATION']['next_check'], '2026-12-07')
        self.assertEqual(records(path, 'research_radar')[0]['selection_cycle_id'], 'RS-2026-09-13-01')

    def test_partial_scan_and_new_snapshot_do_not_erase_history(self):
        with (ROOT/'notes/research_topics/scan_log.csv').open(encoding='utf8', newline='') as stream:
            scan = next(r for r in csv.DictReader(stream) if r['scan_id'] == 'scan-2026-11-23-design-and-validation-boundaries')
        self.assertEqual(scan['scope'], 'partial')
        for term in ('上市11/22', '上櫃11/21', '0列0公司', '不得互補', '沒有新MOPS'):
            self.assertIn(term, scan['coverage_note'])
        old = json.loads((ROOT/'notes/research_method_reviews/2026-11-21_01.json').read_text(encoding='utf8'))
        new = json.loads((ROOT/'notes/research_method_reviews/2026-11-23_01.json').read_text(encoding='utf8'))
        self.assertEqual(old['corrections']['monitorReviewEvents'], 1289)
        self.assertEqual(new['corrections']['monitorReviewEvents'], 1312)
        self.assertEqual(new['corrections']['resultCounts']['new_support'], old['corrections']['resultCounts']['new_support'])
        self.assertEqual(new['freshness']['staleTopics'], 42)
        self.assertEqual(new['monitors']['dueOrOverdue'], 0)


if __name__ == '__main__':
    unittest.main()
