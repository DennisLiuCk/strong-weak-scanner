"""Versions, raw evidence, and financial measures must not be conflated."""
import csv
import json
import unittest

from test_research_cycle_20261012 import ROOT, bd, records
from test_research_cycle_20261019 import keyed

MEMORY='notes/research_topics/2026-08-02_ai_memory_hierarchy.md'
POWER='notes/research_topics/2026-08-02_800v_power_semiconductor_partition.md'


class ResearchCycleOctober24Test(unittest.TestCase):
    def test_frozen_due_attempts_do_not_refresh_evidence(self):
        with (ROOT/'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf-8',newline='') as f:
            rows=[r for r in csv.DictReader(f) if r['checked_at']=='2026-10-24']
        self.assertEqual(len(rows),78)
        self.assertEqual(len({(r['topic_id'],r['monitor_id']) for r in rows}),78)
        for r in rows:
            self.assertEqual(r['result'],'not_yet_testable')
            self.assertEqual(r['claim_action'],'none')
            self.assertFalse(r['evidence_source_ids'])
            self.assertIn('原有效期限2026-10-23',r['notes'])
            self.assertIn('未完成／邊界',r['notes'])
            self.assertIn('來源：',r['notes'])
            self.assertGreater(r['next_check'],r['checked_at'])

    def test_dynamo_dev_capture_is_not_runtime_or_stable_release(self):
        sources=keyed(MEMORY,'research_source','source_id')
        for sid in ['S28','S29']:
            self.assertEqual(sources[sid]['source_kind'],'living_index')
            self.assertEqual(sources[sid]['captured_at'],'2026-10-24')
            self.assertFalse(sources[sid]['published_at'])
            self.assertEqual(sources[sid]['independence_group'],sources['S14']['independence_group'])
            self.assertNotIn('Beta',sources[sid]['locator'])
        self.assertIn('9929eadfcc0b2dd92e99b77df7b05f079979264a1ace21aaddb5447abc2a8805',sources['S28']['locator'])
        claims=keyed(MEMORY,'research_claim','claim_id')
        self.assertIn('替代實作',claims['C36']['claim'])
        self.assertIn('不是本輪實驗',claims['C37']['boundary'])
        self.assertEqual(claims['C38']['label'],'inference')

    def test_power_vendor_positioning_does_not_prove_operating_point(self):
        source=keyed(POWER,'research_source','source_id')['S15']
        self.assertEqual(source['published_at'],'2026-10-21')
        self.assertEqual(source['captured_at'],'2026-10-24')
        self.assertIn('be55cd376bcf784ab82ccd374af303ba543c3522de977acca8e4ce1315a30995',source['locator'])
        claims=keyed(POWER,'research_claim','claim_id')
        self.assertIn('只確認公司如此揭露',claims['C19']['boundary'])
        self.assertIn('最高1MHz',claims['C19']['claim'])
        self.assertEqual(claims['C20']['label'],'inference')
        for file,eid in [('notes/knowledge_graph/ai_memory_hierarchy.md','KG-MEM-I25'),('notes/knowledge_graph/800v_power_tree.md','KG-8VP-I22')]:
            edge=keyed(file,'knowledge_edge','edge_id')[eid]
            self.assertEqual((edge['commercial_stage'],edge['materiality']),('concept','adjacent'))
            self.assertEqual(edge['exclusivity'],'unknown')

    def test_revision_reaches_homepage_without_changing_thesis_clock(self):
        topics=[]
        for path,clock in [(MEMORY,('C8','2026-08-12','2026-08-17')),(POWER,('C7','2026-08-12','2026-08-19'))]:
            meta=records(path,'research_topic')[0]
            self.assertEqual(tuple(meta[k] for k in ('thesis_claim_id','last_reviewed_at','review_due')),clock)
            transitions=records(path,'transition')
            self.assertTrue(any(t['date']=='2026-10-24' and t['evidence'].startswith('sources:') for t in transitions))
            topics.append(dict(topic_id=meta['topic_id'],title=meta['topic_id'],relpath=path,meta=meta,transitions=transitions))
        recent=bd.build_recent_articles('2026-10-24',{},{},topics=topics)
        self.assertEqual({r['researchId'] for r in recent['items']},{'topic-'+t['topic_id'] for t in topics})
        self.assertTrue(all(r['date']=='2026-10-24' for r in recent['items']))

    def test_partial_scan_and_raw_evidence_boundaries_remain_explicit(self):
        with (ROOT/'notes/research_topics/scan_log.csv').open(encoding='utf-8',newline='') as f:
            row=next(r for r in csv.DictReader(f) if r['scan_id']=='scan-2026-10-24-versions-and-economic-measures')
        self.assertEqual(row['scope'],'partial')
        for text in ['缺10/21、10/22及10/24','5299另查115Q3','面額不等募資所得','未核本批PDF','raw留作者處']:
            self.assertIn(text,row['coverage_note'])
        radar=(ROOT/'notes/research_candidates/2026-09-13_verification_gaps.md').read_text(encoding='utf-8')
        self.assertIn('ed6f5559673767bd620eb8174fdf61bdc7aa3639',radar)
        self.assertIn('完整raw logs與ACK原件留在作者處',radar)

    def test_snapshot_keeps_stale_evidence_and_original_candidate_ranks(self):
        snap=json.loads((ROOT/'notes/research_method_reviews/2026-10-24_01.json').read_text(encoding='utf-8'))
        self.assertEqual(snap['freshness']['staleTopics'],40)
        self.assertEqual(snap['corrections']['monitorReviewEvents'],832)
        self.assertEqual(snap['monitors']['dueOrOverdue'],0)
        self.assertEqual(snap['claims']['active'],910)
        candidates=records('notes/research_candidates/2026-09-13_verification_gaps.md','research_candidate')
        self.assertEqual([(r['rank'],r['status']) for r in candidates],[('1','watch'),('2','watch'),('3','watch')])


if __name__=='__main__':
    unittest.main()
