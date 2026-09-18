"""Publication recovery and source-boundary regressions for the September cycle."""
import csv
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build_dashboard as bd


def records(path, kind):
    text = (ROOT / path).read_text(encoding='utf8')
    result = []
    for body in re.findall(r'<!-- ' + kind + r'\s*\n(.*?)-->', text, re.S):
        result.append(dict((k.strip(), v.strip()) for k, v in
                           (line.split(':', 1) for line in body.splitlines() if ':' in line)))
    return result


class SeptemberRecoveryTest(unittest.TestCase):
    def test_pfas_correction_keeps_history_and_original_schedule(self):
        path = 'notes/research_topics/2026-08-12_semiconductor_pfas_exposure.md'
        claims = {r['claim_id']: r for r in records(path, 'research_claim')}
        monitors = {r['monitor_id']: r for r in records(path, 'monitoring_item')}
        self.assertEqual(claims['C5']['status'], 'superseded')
        self.assertEqual(claims['C5']['corrected_by_claim_id'], 'C23')
        self.assertIn('2027-01-31', claims['C23']['claim'])
        self.assertIn('取較早', claims['C23']['claim'])
        for field in ('metric', 'trigger', 'invalidation', 'frequency', 'next_check'):
            self.assertEqual(monitors['T2'][field], monitors['T4'][field])
        meta = records(path, 'research_topic')[0]
        self.assertEqual(meta['last_reviewed_at'], '2026-08-12')
        self.assertEqual(meta['review_due'], '2026-09-15')

    def test_high_na_total_is_not_a_qualified_production_denominator(self):
        path = 'notes/research_topics/2026-08-02_high_na_euv_insertion_ladder.md'
        claims = {r['claim_id']: r for r in records(path, 'research_claim')}
        self.assertIn('設備認證測試', claims['C21']['claim'])
        self.assertIn('研發', claims['C21']['claim'])
        self.assertIn('部分產品特定層量產', claims['C21']['claim'])
        self.assertEqual(claims['C22']['label'], 'inference')
        self.assertIn('不能直接', claims['C22']['claim'])

    def test_policy_successor_preserves_contract_and_covers_authorities(self):
        path = 'notes/research_topics/2026-07-23_us_section_301_taiwan.md'
        monitors = {r['monitor_id']: r for r in records(path, 'monitoring_item')}
        self.assertEqual(monitors['T4']['status'], 'retired')
        for field in ('metric', 'trigger', 'invalidation', 'frequency', 'next_check'):
            self.assertEqual(monitors['T4'][field], monitors['T5'][field])
        watch = set(monitors['T5']['watch_source_ids'].split(','))
        self.assertTrue({'S7', 'S8', 'S9', 'S17', 'S18'} <= watch)

    def test_tonghsing_scope_extension_is_not_a_new_independent_source(self):
        path = 'notes/research_topics/2026-07-29_priority_q2_disclosures.md'
        sources = {r['source_id']: r for r in records(path, 'research_source')}
        claims = {r['claim_id']: r for r in records(path, 'research_claim')}
        self.assertEqual(sources['S35']['url'], sources['S36']['url'])
        self.assertEqual(sources['S35']['status'], 'superseded')
        self.assertEqual(claims['C33']['corrected_by_claim_id'], 'C34')
        self.assertIn('不是認定原附件事件錯誤', claims['C34']['basis'])
        self.assertIn('898165', claims['C35']['claim'])
        self.assertIn('H1而非Q2', claims['C35']['claim'])
        self.assertIn('新台幣仟元', claims['C35']['claim'])
        self.assertEqual(3208504 - 55540, 3152964)
        self.assertEqual(6051570 - 79369, 5972201)
        self.assertEqual(945932 + 81854 - 34916 - 94705, 898165)

    def test_procedural_edges_do_not_imply_company_revenue(self):
        for path, edge_id in (
            ('section301_taiwan_exposure.md', 'KG-S301-I19'),
            ('800vdc_execution_readiness.md', 'KG-8ER-I19'),
            ('pcie6_compliance_ladder.md', 'KG-PCIE6-I29'),
        ):
            edge = next(r for r in records('notes/knowledge_graph/' + path, 'knowledge_edge')
                        if r['edge_id'] == edge_id)
            self.assertEqual(edge['view'], 'industry')
            self.assertEqual(edge['materiality'], 'adjacent')
            self.assertNotEqual(edge['commercial_stage'], 'scaled_revenue')

    def test_recovered_revisions_reach_homepage_without_thesis_refresh(self):
        topics = []
        for filename, clock, due in (
            ('2026-07-23_us_section_301_taiwan.md', '2026-08-12', '2026-08-15'),
            ('2026-07-29_priority_q2_disclosures.md', '2026-08-12', '2026-08-15'),
            ('2026-08-01_800vdc_execution_readiness.md', '2026-08-12', '2026-09-12'),
            ('2026-08-02_open_ai_fabrics.md', '2026-08-12', '2026-08-17'),
            ('2026-08-03_pcie6_compliance_ladder.md', '2026-08-24', '2026-08-31'),
        ):
            path = 'notes/research_topics/' + filename
            meta = records(path, 'research_topic')[0]
            self.assertEqual(meta['last_reviewed_at'], clock)
            self.assertEqual(meta['review_due'], due)
            transitions = [r for r in records(path, 'transition') if r['date'] == '2026-09-13']
            self.assertTrue(transitions)
            topics.append({'topic_id': meta['topic_id'], 'title': meta['topic_id'],
                           'relpath': path, 'meta': meta, 'transitions': transitions})
        recent = bd.build_recent_articles('2026-09-18', {}, {}, topics=topics)
        self.assertTrue({'topic-' + t['topic_id'] for t in topics} <=
                        {item['researchId'] for item in recent['items']})

    def test_prior_checks_keep_original_dates_and_not_double_counted(self):
        with (ROOT / 'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf8', newline='') as f:
            rows = list(csv.DictReader(f))
        prior = [r for r in rows if r['checked_at'] == '2026-09-13']
        self.assertEqual(len(prior), 21)
        self.assertEqual(sum(r['result'] == 'new_support' for r in prior), 2)
        successor = next(r for r in prior if r['review_id'] == 'MR-2026-09-13-SECTION301-T5')
        self.assertEqual(successor['evidence_source_ids'], '')
        self.assertEqual(successor['claim_action'], 'none')


if __name__ == '__main__':
    unittest.main()
