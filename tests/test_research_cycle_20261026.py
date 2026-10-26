"""Calling an API, observing a path, and measuring benefit are separate evidence."""
from collections import Counter
import csv
import json
import unittest

from test_research_cycle_20261012 import ROOT, bd, records
from test_research_cycle_20261019 import keyed

TOPIC = 'notes/research_topics/2026-08-09_ai_storage_data_plane.md'
GRAPH = 'notes/knowledge_graph/ai_storage_data_plane.md'
RADAR = 'notes/research_candidates/2026-09-13_verification_gaps.md'


class ResearchCycleOctober26Test(unittest.TestCase):
    def test_due_attempts_preserve_clocks_and_event_specific_dates(self):
        with (ROOT/'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf-8', newline='') as f:
            rows = [r for r in csv.DictReader(f) if r['checked_at'] == '2026-10-26']
        self.assertEqual(len(rows), 120)
        self.assertEqual(len({(r['topic_id'], r['monitor_id']) for r in rows}), 120)
        self.assertEqual(Counter(r['result'] for r in rows), {'not_yet_testable': 118, 'no_new_evidence': 2})
        self.assertGreater(len({r['next_check'] for r in rows}), 1)
        for row in rows:
            self.assertEqual(row['claim_action'], 'none')
            self.assertFalse(row['evidence_source_ids'])
            for marker in ['原有效期限2026-10-26', '未完成／邊界', '來源：', '下一工作']:
                self.assertIn(marker, row['notes'])
            self.assertGreater(row['next_check'], row['checked_at'])

    def test_gds_document_date_source_chain_and_counter_boundaries(self):
        sources = keyed(TOPIC, 'research_source', 'source_id')
        source = sources['S26']
        self.assertEqual((source['published_at'], source['captured_at']), ('2026-10-22', '2026-10-26'))
        self.assertEqual(source['independence_group'], sources['S3']['independence_group'])
        self.assertIn('790bc78011b593d3cafed11f11613664c661caa5df9a1f80ea3324cac1b6ef23', source['locator'])
        claims = keyed(TOPIC, 'research_claim', 'claim_id')
        self.assertEqual([claims[k]['label'] for k in ['C29', 'C30', 'C31']], ['verified', 'verified', 'inference'])
        self.assertIn('兩層', claims['C29']['claim'])
        self.assertIn('不由 cuFile 記錄', claims['C30']['claim'])
        self.assertIn('操作數', claims['C30']['boundary'])
        self.assertIn('零拷貝', claims['C30']['boundary'])
        self.assertIn('未重跑教材', claims['C31']['boundary'])

    def test_monitor_and_graph_do_not_upgrade_commercial_exposure(self):
        monitor = keyed(TOPIC, 'monitoring_item', 'monitor_id')['T5']
        self.assertEqual(monitor['claim_ids'], 'C29,C30,C31')
        self.assertEqual(monitor['next_check'], '2026-11-02')
        self.assertIn('不確定度', monitor['trigger'])
        self.assertIn('不回寫 C5', monitor['invalidation'])
        edge = keyed(GRAPH, 'knowledge_edge', 'edge_id')['KG-ASD-I19']
        self.assertEqual(edge['to_id'], 'process:gds-path-observation-contract')
        self.assertEqual((edge['evidence_state'], edge['commercial_stage'], edge['materiality']), ('inference', 'concept', 'adjacent'))
        self.assertEqual(edge['exclusivity'], 'unknown')

    def test_homepage_revision_does_not_refresh_old_thesis(self):
        meta = records(TOPIC, 'research_topic')[0]
        self.assertEqual(tuple(meta[k] for k in ['thesis_claim_id', 'last_reviewed_at', 'review_due']), ('C5', '2026-08-12', '2026-08-28'))
        self.assertEqual(keyed(TOPIC, 'research_claim', 'claim_id')['C5']['as_of'], '2026-08-09')
        transitions = records(TOPIC, 'transition')
        self.assertTrue(any(t['date'] == '2026-10-26' and t['evidence'] == 'sources:S26' for t in transitions))
        topic = dict(topic_id=meta['topic_id'], title=meta['topic_id'], relpath=TOPIC, meta=meta, transitions=transitions)
        recent = bd.build_recent_articles('2026-10-26', {}, {}, topics=[topic])
        self.assertEqual(recent['items'][0]['researchId'], 'topic-'+meta['topic_id'])
        self.assertEqual(recent['items'][0]['date'], '2026-10-26')

    def test_partial_scan_preserves_request_and_denominator_limits(self):
        with (ROOT/'notes/research_topics/scan_log.csv').open(encoding='utf-8', newline='') as f:
            row = next(r for r in csv.DictReader(f) if r['scan_id'] == 'scan-2026-10-26-path-evidence-and-event-cadence')
        self.assertEqual(row['scope'], 'partial')
        for marker in ['缺10/24及10/26', '每股下降不等總額減少', '共22次對21公司', '2327兩次時點結果不同', '本輪未核本批PDF']:
            self.assertIn(marker, row['coverage_note'])

    def test_snapshot_and_candidate_ranks_preserve_unresolved_evidence(self):
        snap = json.loads((ROOT/'notes/research_method_reviews/2026-10-26_01.json').read_text(encoding='utf-8'))
        self.assertEqual(snap['freshness'], {'staleTopics': 40, 'staleEdges': 840})
        self.assertEqual(snap['corrections']['monitorReviewEvents'], 952)
        self.assertEqual(snap['claims']['active'], 913)
        self.assertEqual(snap['monitors']['active'], 166)
        self.assertEqual(snap['monitors']['dueOrOverdue'], 0)
        candidates = records(RADAR, 'research_candidate')
        self.assertEqual([(r['rank'], r['status']) for r in candidates], [('1', 'watch'), ('2', 'watch'), ('3', 'watch')])


if __name__ == '__main__':
    unittest.main()
