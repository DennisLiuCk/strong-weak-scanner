"""October follow-up: version scope, incomplete evidence and publication clocks."""
import csv
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build_dashboard as bd

TOPIC = 'notes/research_topics/2026-08-12_chiplet_design_handoff_contracts.md'


def records(path, kind):
    text = (ROOT / path).read_text(encoding='utf8')
    return [dict((k.strip(), v.strip()) for k, v in
                 (line.split(':', 1) for line in body.splitlines() if ':' in line))
            for body in re.findall(r'<!-- ' + kind + r'\s*\n(.*?)-->', text, re.S)]


class OctoberVersionFollowupTest(unittest.TestCase):
    def test_rc_branch_preserves_thesis_clock_and_candidate_suffix(self):
        meta = records(TOPIC, 'research_topic')[0]
        self.assertEqual(meta['thesis_claim_id'], 'C7')
        self.assertEqual(meta['last_reviewed_at'], '2026-08-12')
        self.assertEqual(meta['review_due'], '2026-08-24')
        claims = {r['claim_id']: r for r in records(TOPIC, 'research_claim')}
        for key in ('C26', 'C27', 'C28'):
            self.assertEqual(claims[key]['supporting_source_ids'], 'S17')
            self.assertEqual(claims[key]['label'], 'verified')
            self.assertTrue(claims[key]['boundary'])
        sources = {r['source_id']: r for r in records(TOPIC, 'research_source')}
        self.assertIn('RC0', sources['S17']['title'])
        self.assertIn('403', sources['S18']['limitation'])
        self.assertIn('索引', sources['S18']['limitation'])
        self.assertEqual(sources['S17']['independence_group'], sources['S18']['independence_group'])

    def test_successor_preserves_decision_contract_not_a_second_sample(self):
        monitors = {r['monitor_id']: r for r in records(TOPIC, 'monitoring_item')}
        self.assertEqual(monitors['T3']['status'], 'retired')
        for field in ('metric', 'trigger', 'invalidation', 'frequency', 'frequency_detail', 'next_check'):
            self.assertEqual(monitors['T3'][field], monitors['T5'][field])
        self.assertEqual(monitors['T5']['watch_source_ids'], 'S18')
        with (ROOT / 'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf8', newline='') as f:
            rows = [r for r in csv.DictReader(f) if r['checked_at'] == '2026-10-08'
                    and not r['review_id'].startswith('MR-2026-10-08-EVENING-')]
        self.assertEqual(len(rows), 7)
        for row in rows:
            self.assertEqual(row['result'], 'not_yet_testable')
            self.assertEqual(row['evidence_source_ids'], '')
            self.assertEqual(row['claim_action'], 'none')
        self.assertTrue({'MR-2026-10-08-FCSA-T3', 'MR-2026-10-08-FCSA-T5'} <=
                        {r['review_id'] for r in rows})

    def test_new_edges_are_design_requirements_not_company_exposure(self):
        edges = {r['edge_id']: r for r in records(
            'notes/knowledge_graph/chiplet_design_handoff_contracts.md', 'knowledge_edge')}
        for key in ('KG-CDH-I18', 'KG-CDH-I19'):
            self.assertEqual(edges[key]['view'], 'industry')
            self.assertEqual(edges[key]['commercial_stage'], 'capability')
            self.assertEqual(edges[key]['materiality'], 'unknown')
            self.assertEqual(edges[key]['exclusivity'], 'unknown')
            self.assertEqual(edges[key]['as_of'], '2026-10-08')

    def test_revision_reaches_homepage_without_main_evidence_refresh(self):
        meta = records(TOPIC, 'research_topic')[0]
        transitions = [r for r in records(TOPIC, 'transition') if r['date'] == '2026-10-08']
        self.assertEqual(len(transitions), 1)
        topic = {'topic_id': meta['topic_id'], 'title': meta['topic_id'], 'relpath': TOPIC,
                 'meta': meta, 'transitions': transitions}
        recent = bd.build_recent_articles('2026-10-08', {}, {}, topics=[topic])
        self.assertIn('topic-' + meta['topic_id'], {r['researchId'] for r in recent['items']})

    def test_scan_retains_partial_coverage_and_unreviewed_work(self):
        with (ROOT / 'notes/research_topics/scan_log.csv').open(encoding='utf8', newline='') as f:
            row = next(r for r in csv.DictReader(f)
                       if r['scan_id'] == 'scan-2026-10-08-version-and-paired-evidence')
        self.assertEqual(row['scope'], 'partial')
        self.assertIn('63個原到期項未查仍逾期', row['coverage_note'])
        self.assertIn('玻璃核心本輪未查', row['coverage_note'])
        self.assertEqual(row['result_topic_ids'], records(TOPIC, 'research_topic')[0]['topic_id'])


if __name__ == '__main__':
    unittest.main()
