"""Product predicates, contract scope and research clocks remain separate."""
import csv
import hashlib
import json
import unittest
from collections import Counter

from test_research_cycle_20261012 import ROOT, records
from test_research_cycle_20261019 import keyed

DAY = '2026-11-21'
HELIOS = 'notes/research_topics/2026-08-02_amd_helios_deployment_ladder.md'
RADAR = 'notes/research_candidates/2026-09-13_verification_gaps.md'


class ResearchCycleNovember21Test(unittest.TestCase):
    def reviews(self):
        with (ROOT/'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf8', newline='') as stream:
            return [r for r in csv.DictReader(stream) if r['review_id'].startswith('MR-2026-11-21-')]

    def test_due_cohort_has_four_bounded_reviews(self):
        rows = self.reviews()
        self.assertEqual(len(rows), 4)
        cohort = '\n'.join(sorted(r['topic_id']+'#'+r['monitor_id'] for r in rows))
        self.assertEqual(hashlib.sha256(cohort.encode()).hexdigest(),
                         '8a3fdcd4065c66b82e9318903a2e94e66c08a7c67bdcd18ce5930a2a119707fa')
        self.assertEqual(Counter(r['result'] for r in rows), {'not_yet_testable': 3, 'new_support': 1})
        for row in rows:
            self.assertEqual(row['checked_at'], DAY)
            self.assertGreater(row['next_check'], DAY)
            if row['result'] == 'not_yet_testable':
                self.assertEqual((row['claim_action'], row['evidence_source_ids']), ('none', ''))
            else:
                self.assertTrue(row['topic_id'].endswith('AI-RACK-TRUST-ROOT'))
                self.assertEqual(row['monitor_id'], 'T3')
                self.assertEqual(row['claim_action'], 'new_claim')
                self.assertTrue(row['evidence_source_ids'])
            self.assertIn('原有效期限', row['notes'])
            self.assertIn('來源：', row['notes'])

    def test_brand_and_other_product_shipping_do_not_complete_helios(self):
        claims = keyed(HELIOS, 'research_claim', 'claim_id')
        self.assertIn('PowerRack', claims['C36']['claim'])
        self.assertIn('H15', claims['C37']['claim'])
        self.assertEqual(claims['C36']['supporting_source_ids'], 'S32')
        self.assertEqual(claims['C37']['supporting_source_ids'], 'S33')
        self.assertIn('不等已交付', claims['C36']['boundary'])
        self.assertIn('不證明Helios未出貨', claims['C37']['boundary'])
        monitors = keyed(HELIOS, 'monitoring_item', 'monitor_id')
        self.assertIn('並確認已出貨', monitors['T6']['trigger'])
        self.assertIn('場站、日期及驗收範圍', monitors['T14']['trigger'])
        for monitor in ('T6', 'T14'):
            row = next(r for r in self.reviews() if r['topic_id'].endswith('AMD-HELIOS-DEPLOYMENT-LADDER') and r['monitor_id'] == monitor)
            self.assertEqual(row['result'], 'not_yet_testable')

    def test_candidate_recheck_does_not_reselect_or_promote(self):
        candidates = keyed(RADAR, 'research_candidate', 'candidate_id')
        expected = [('RC-800V-SSCB-FAULT-ISOLATION', '1', '2026-12-05'),
                    ('RC-HBFSIM-MODEL-VALIDATION', '2', '2026-11-23'),
                    ('RC-GLASS-CORE-CUSTOMER-RELEASE', '3', '2026-11-24')]
        for candidate_id, rank, next_check in expected:
            item = candidates[candidate_id]
            self.assertEqual((item['rank'], item['status']), (rank, 'watch'))
            # Future cycles may move work dates, but never before this bounded review.
            self.assertGreaterEqual(item['next_check'], next_check)
        self.assertEqual(records(RADAR, 'research_radar')[0]['selection_cycle_id'], 'RS-2026-09-13-01')

    def test_supply_contract_sums_keep_historical_source_mapping(self):
        path = 'notes/research_topics/2026-08-01_us_advanced_packaging_regionalization.md'
        claims = keyed(path, 'research_claim', 'claim_id')
        self.assertEqual(claims['C22']['supporting_source_ids'], 'S1,S2,S16,S17')
        self.assertIn('不是公司30億的精確合約調節', claims['C22']['boundary'])
        self.assertIn('不把10月總額再加到7月金額', claims['C22']['boundary'])
        self.assertEqual(claims['C26']['label'], 'unverified')
        self.assertEqual(records(path, 'research_topic')[0]['last_reviewed_at'], '2026-10-04')

    def test_customer_configuration_or_branch_does_not_verify_financial_claim(self):
        path = 'notes/research_topics/2026-08-08_ai_rack_trust_root.md'
        claims = keyed(path, 'research_claim', 'claim_id')
        self.assertEqual(claims['C24']['label'], 'verified')
        for product in ('H15SPHM', 'R265-DG3-AS1', 'AST2700'):
            self.assertIn(product, claims['C24']['claim'])
        self.assertEqual(claims['C10']['label'], 'unverified')
        self.assertEqual(claims['C7']['as_of'], '2026-08-08')
        monitors = keyed(path, 'monitoring_item', 'monitor_id')
        self.assertIn('或客戶端出現具名採用文件', monitors['T3']['trigger'])

    def test_supply_selection_is_separate_from_original_watch_cycle(self):
        with (ROOT/'notes/research_candidates/selection_log.csv').open(encoding='utf8', newline='') as stream:
            rows = [r for r in csv.DictReader(stream) if r['cycle_id'] == 'RS-2026-11-21-01']
        self.assertEqual(len(rows), 1)
        self.assertEqual((rows[0]['rank'], rows[0]['selection_decision']), ('1', 'advance'))
        self.assertEqual(rows[0]['selected_at'], '2026-11-21T13:45:42+08:00')
        self.assertIn('不新增台股財務受惠線', rows[0]['first_rejection'])

    def test_markets_cannot_fill_each_others_missing_dates(self):
        with (ROOT/'notes/research_topics/scan_log.csv').open(encoding='utf8', newline='') as stream:
            row = next(r for r in csv.DictReader(stream) if r['scan_id'] == 'scan-2026-11-21-product-and-contract-scope')
        self.assertEqual((row['window_start'], row['window_end'], row['scope']), ('2026-11-19', DAY, 'partial'))
        for term in ('25列22公司', '上市11/20', '上櫃11/19', '不得互補', '仟元', '5274'):
            self.assertIn(term, row['coverage_note'])

    def test_snapshot_is_appended_and_stale_theses_remain_visible(self):
        old = json.loads((ROOT/'notes/research_method_reviews/2026-11-18_02.json').read_text(encoding='utf8'))
        new = json.loads((ROOT/'notes/research_method_reviews/2026-11-21_01.json').read_text(encoding='utf8'))
        self.assertEqual(old['corrections']['monitorReviewEvents'], 1285)
        self.assertEqual(new['corrections']['monitorReviewEvents'], 1289)
        self.assertEqual(new['freshness']['staleTopics'], 42)
        self.assertEqual(new['monitors']['dueOrOverdue'], 0)
        self.assertEqual(new['corrections']['supersededOrRefutedClaims'], old['corrections']['supersededOrRefutedClaims'])
        meta = records(HELIOS, 'research_topic')[0]
        self.assertEqual((meta['last_reviewed_at'], meta['review_due']), ('2026-08-12', '2026-08-15'))


if __name__ == '__main__':
    unittest.main()
