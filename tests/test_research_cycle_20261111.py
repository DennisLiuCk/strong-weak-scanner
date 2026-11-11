"""Acquisition success is not product acceptance or comparable revenue."""
import csv
from decimal import Decimal
import unittest

from test_research_cycle_20261012 import ROOT, records
from test_research_cycle_20261019 import keyed

DAY = '2026-11-11'
POWER = 'notes/research_topics/2026-08-01_800vdc_execution_readiness.md'
PROCESS = 'notes/research_topics/2026-08-02_ai_process_control_intensity.md'


class ResearchCycleNovember11Test(unittest.TestCase):
    def test_frozen_cohort_is_reviewed_once_without_claiming_support(self):
        expected = {
            'MI-2026-07-23-US-SECTION301-TAIWAN': {'T2'},
            'MI-2026-07-29-PRIORITY-Q2-DISCLOSURES': {'T9'},
            'MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL': {'T5'},
            'MI-2026-07-31-MISSED-PRIORITY-Q2': {'T11', 'T12'},
            'MI-2026-08-01-800VDC-EXECUTION-READINESS': {'T2', 'T4', 'T5'},
            'MI-2026-08-01-AI-CAPEX-CASH-CONVERSION': {'T5'},
            'MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY': {'T2', 'T6', 'T9'},
            'MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER': {'T6', 'T14', 'T15'},
            'MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER': {'T4'},
            'MI-2026-08-02-OPEN-AI-FABRICS': {'T2'},
            'MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY': {'T2'},
            'MI-2026-09-10-DC-PHASE-DELIVERY': {'T2'},
        }
        with (ROOT/'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf8', newline='') as f:
            rows = [r for r in csv.DictReader(f) if r['checked_at'] == DAY]
        pairs = {(r['topic_id'], r['monitor_id']) for r in rows}
        self.assertEqual(len(rows), 19)
        self.assertEqual(pairs, {(t, m) for t, ms in expected.items() for m in ms})
        for row in rows:
            self.assertIn(row['result'], ('not_yet_testable', 'no_new_evidence'))
            self.assertEqual((row['evidence_source_ids'], row['claim_action']), ('', 'none'))
            self.assertGreater(row['next_check'], DAY)
            self.assertIn('原有效期限', row['notes'])

    def test_sidebranch_updates_do_not_refresh_thesis_clocks(self):
        for path in (POWER, PROCESS):
            meta = records(path, 'research_topic')[0]
            self.assertLess(meta['last_reviewed_at'], DAY)
            self.assertLess(meta['review_due'], DAY)
            self.assertTrue(any(r['date'] == DAY for r in records(path, 'transition')))

    def test_ercot_acquisition_limit_and_same_producer_are_explicit(self):
        sources = keyed(POWER, 'research_source', 'source_id')
        for sid in ('S24', 'S25'):
            self.assertEqual(sources[sid]['independence_group'], 'ercot')
            self.assertIn('403', sources[sid]['limitation'])
            self.assertIn('原件SHA', sources[sid]['limitation'])
        self.assertIn('不採統計圖表數字', sources['S25']['limitation'])

    def test_rfi_process_has_separate_monitor_and_no_project_acceptance(self):
        monitors = keyed(POWER, 'monitoring_item', 'monitor_id')
        self.assertEqual(monitors['T7']['next_check'], '2026-12-11')
        self.assertIn('不同', keyed(POWER, 'research_claim', 'claim_id')['C31']['boundary'])
        edge = keyed('notes/knowledge_graph/800vdc_execution_readiness.md', 'knowledge_edge', 'edge_id')['KG-8ER-I21']
        self.assertEqual(edge['claim_refs'], 'MI-2026-08-01-800VDC-EXECUTION-READINESS#C30')
        self.assertEqual(edge['materiality'], 'adjacent')
        self.assertIn('不等於', edge['boundary'])

    def test_record_forecast_and_actual_do_not_become_comparable(self):
        claims = keyed(PROCESS, 'research_claim', 'claim_id')
        self.assertIn('公告沒有該類別／產品收入表', claims['C45']['basis'])
        self.assertIn('全年預測', claims['C46']['claim'])
        self.assertIn('不能反推精確基期', claims['C46']['boundary'])
        self.assertEqual(claims['C47']['label'], 'inference')
        self.assertIn('not_comparable', claims['C47']['claim'])
        edges = records('notes/knowledge_graph/hbm.md', 'knowledge_edge')
        edge = next(r for r in edges if '#C45' in r.get('claim_refs', ''))
        self.assertEqual((edge['evidence_state'], edge['materiality']), ('inference', 'adjacent'))

    def test_scan_retains_partial_coverage_and_unattempted_items(self):
        with (ROOT/'notes/research_topics/scan_log.csv').open(encoding='utf8', newline='') as f:
            row = next(r for r in csv.DictReader(f) if r['scan_id'] == 'scan-2026-11-11-acquisition-and-acceptance')
        self.assertEqual(row['scope'], 'partial')
        for term in ('74', '69', '56', '限流', '11/10'):
            self.assertIn(term, row['coverage_note'])

    def test_matching_arithmetic_does_not_resolve_official_definition(self):
        total = sum(map(Decimal, ('147495485', '31079294', '22143004')))
        self.assertEqual(total/1000, Decimal('200717.783'))
        claim = keyed('notes/research_topics/2026-07-30_yageo_q2_earnings_call.md', 'research_claim', 'claim_id')['C16']
        self.assertEqual(claim['label'], 'unverified')
        self.assertIn('200078', claim['basis'])
        self.assertIn('200718', claim['basis'])

    def test_method_does_not_treat_text_hash_as_pdf_hash(self):
        text = (ROOT/'MARKET_RESEARCH_METHOD.md').read_text(encoding='utf8')
        for term in ('取得管道與可重驗範圍', '節錄雜湊', '不得冒稱原始PDF雜湊', '不回改舊收據'):
            self.assertIn(term, text)

    def test_watch_candidates_keep_frozen_order_and_conditions(self):
        candidates = records('notes/research_candidates/2026-09-13_verification_gaps.md', 'research_candidate')
        self.assertEqual([r['rank'] for r in candidates], ['1', '2', '3'])
        for row in candidates:
            self.assertEqual(row['status'], 'watch')
            self.assertTrue(row['first_rejection'])
            self.assertTrue(row['next_evidence'])
