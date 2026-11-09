"""Same dates and official documents do not erase accounting/version boundaries."""
import csv
from decimal import Decimal
import unittest

from test_research_cycle_20261012 import ROOT, records
from test_research_cycle_20261019 import keyed

CASH = 'notes/research_topics/2026-08-01_ai_capex_cash_conversion.md'
YAGEO = 'notes/research_topics/2026-07-30_yageo_q2_earnings_call.md'
DAY = '2026-11-09'


class ResearchCycleNovember9Test(unittest.TestCase):
    def test_company_cash_formulas_recalculate_without_ranking(self):
        values = [58000-39367, 32786-33942-964, 42422-77259+1381]
        decimal_values = [Decimal('58000')-Decimal('39367'),
                          Decimal('32786')-Decimal('33942')-Decimal('964'),
                          Decimal('42422')-Decimal('77259')+Decimal('1381')]
        obs = [r for r in records(CASH, 'metric_comparison') if r['comparison_id'] == 'M4']
        self.assertEqual(len(obs), 3)
        self.assertEqual([Decimal(r['reported_value']) for r in obs], decimal_values)
        self.assertEqual(values, [18633, -2120, -33456])
        for row in obs:
            self.assertEqual((row['period_start'], row['period_end'], row['unit'], row['comparability']),
                             ('2026-07-01', '2026-09-30', 'USD million', 'not_comparable'))

    def test_lease_conflict_does_not_become_an_invented_adjustment(self):
        claims = keyed(CASH, 'research_claim', 'claim_id')
        self.assertEqual(claims['C35']['label'], 'unverified')
        for value in ('45.2', '7.4', '39.4', '5.192', '1.000', '364.6'):
            self.assertIn(value, claims['C34']['claim'])
        self.assertIn('不擅稱錯誤或重編', claims['C34']['boundary'])
        self.assertIn('調整項', claims['C35']['boundary'])

    def test_new_comparative_cash_keeps_old_version(self):
        claim = keyed(YAGEO, 'research_claim', 'claim_id')['C16']
        self.assertEqual(Decimal('200718')-Decimal('200078'), Decimal('640'))
        self.assertEqual(claim['label'], 'unverified')
        self.assertIn('200078', claim['basis'])
        self.assertIn('200718', claim['basis'])
        self.assertIn('不覆寫', claim['boundary'])
        self.assertEqual(claim['supporting_source_ids'], 'S2,S6')

    def test_updated_articles_keep_thesis_clocks(self):
        for path in [CASH, YAGEO,
                     'notes/research_topics/2026-08-02_ai_memory_hierarchy.md',
                     'notes/research_topics/2026-08-12_chiplet_design_handoff_contracts.md']:
            with self.subTest(path=path):
                meta = records(path, 'research_topic')[0]
                self.assertLess(meta['last_reviewed_at'], DAY)
                self.assertLess(meta['review_due'], DAY)
                self.assertTrue(any(r['date']==DAY for r in records(path, 'transition')))

    def test_complete_frozen_due_cohort_with_no_duplicate_pairs(self):
        with (ROOT/'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf8', newline='') as f:
            rows = [r for r in csv.DictReader(f) if r['checked_at'] == DAY]
        self.assertEqual(len(rows), 52)
        self.assertEqual(len({(r['topic_id'], r['monitor_id']) for r in rows}), 52)
        self.assertTrue(all(r['next_check'] > DAY for r in rows))
        for row in rows:
            if row['result'] not in ('new_support', 'new_contrary'):
                self.assertEqual((row['evidence_source_ids'], row['claim_action']), ('', 'none'))
        finance = [r for r in rows if r['topic_id'].endswith('AI-CAPEX-CASH-CONVERSION')]
        self.assertEqual({r['monitor_id'] for r in finance}, {'T1','T6'})
        self.assertTrue(all(r['result']=='not_yet_testable' for r in finance))

    def test_graph_keeps_company_scope_not_taiwan_financial_benefit(self):
        edges = keyed('notes/knowledge_graph/ai_capex_cash_conversion.md', 'knowledge_edge', 'edge_id')
        for key in ['KG-ACC-C01','KG-ACC-C02','KG-ACC-C03']:
            self.assertEqual(edges[key]['materiality'], 'adjacent')
            self.assertIn('#C32', edges[key]['claim_refs'])
        edge = keyed('notes/knowledge_graph/yageo_q2_financial_materiality.md', 'knowledge_edge', 'edge_id')['KG-YQ2-I04']
        self.assertEqual(edge['evidence_state'], 'unverified')
        self.assertIn('640', edge['boundary'])

    def test_method_requires_actual_replacement_content(self):
        text = (ROOT/'MARKET_RESEARCH_METHOD.md').read_text(encoding='utf8')
        for phrase in ('比較欄與補更正的雙版本檢查', '替換原件未取得', '不靠相似欄名'):
            self.assertIn(phrase, text)
