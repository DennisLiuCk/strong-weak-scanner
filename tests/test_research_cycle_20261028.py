"""Preserve speaker, period and denominator when adding a company update."""
import csv
import json
import unittest
from test_research_cycle_20261012 import ROOT, bd, records
from test_research_cycle_20261019 import keyed

TOPIC='notes/research_topics/2026-08-02_ai_memory_hierarchy.md'
GRAPH='notes/knowledge_graph/ai_memory_hierarchy.md'

class ResearchCycleOctober28Test(unittest.TestCase):
    def test_frozen_due_cohort_is_reviewed_without_clock_refresh(self):
        with (ROOT/'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf-8',newline='') as f:
            rows=[r for r in csv.DictReader(f) if r['checked_at']=='2026-10-28']
        self.assertEqual(len(rows),11)
        self.assertEqual(len({(r['topic_id'],r['monitor_id']) for r in rows}),11)
        for r in rows:
            self.assertEqual((r['result'],r['claim_action'],r['evidence_source_ids']),('not_yet_testable','none',''))
            for marker in ['原有效期限2026-10-28','未完成／邊界','來源：','下一工作']:
                self.assertIn(marker,r['notes'])
            self.assertGreater(r['next_check'],r['checked_at'])
        self.assertGreater(len({r['next_check'] for r in rows}),3)

    def test_source_and_claims_keep_attribution_tense_and_denominator(self):
        s=keyed(TOPIC,'research_source','source_id')
        self.assertEqual(s['S30']['independence_group'],s['S22']['independence_group'])
        self.assertEqual(s['S31']['source_kind'],'living_index')
        self.assertIn('417d1b8e3350c1908632e780891a4b3811cf0e638051965fd154f3890592d777',s['S30']['locator'])
        self.assertIn('preliminary',s['S30']['limitation'])
        c=keyed(TOPIC,'research_claim','claim_id')
        self.assertEqual([c[k]['label'] for k in ['C39','C40','C41','C42']],['verified','verified','verified','inference'])
        self.assertIn('公司已作此陳述',c['C39']['boundary'])
        self.assertIn('而非結果已實現',c['C40']['boundary'])
        self.assertIn('總產能',c['C41']['claim'])
        self.assertIn('不是',s['S30']['limitation'])
        self.assertIn('非跨公司可比',c['C41']['boundary'])

    def test_new_monitors_and_graph_do_not_upgrade_company_exposure(self):
        m=keyed(TOPIC,'monitoring_item','monitor_id')
        for mid in ['T10','T11']:
            self.assertEqual(m[mid]['watch_source_ids'],'S30,S31')
            self.assertEqual(m[mid]['next_check'],'2026-11-25')
            self.assertTrue(m[mid]['invalidation'])
        edge=keyed(GRAPH,'knowledge_edge','edge_id')['KG-MEM-I26']
        self.assertEqual((edge['evidence_state'],edge['commercial_stage'],edge['materiality']),('inference','concept','adjacent'))
        self.assertEqual(edge['exclusivity'],'unknown')
        self.assertIn('台灣公司曝險',edge['boundary'])

    def test_revision_is_visible_without_refreshing_old_thesis(self):
        meta=records(TOPIC,'research_topic')[0]
        self.assertEqual(tuple(meta[k] for k in ['thesis_claim_id','last_reviewed_at','review_due']),('C8','2026-08-12','2026-08-17'))
        transitions=records(TOPIC,'transition')
        self.assertTrue(any(r['date']=='2026-10-28' and r['evidence']=='sources:S30' for r in transitions))
        transitions=[r for r in transitions if r['date']<='2026-10-28']
        topic=dict(topic_id=meta['topic_id'],title=meta['topic_id'],relpath=TOPIC,meta=meta,transitions=transitions)
        recent=bd.build_recent_articles('2026-10-28',{},{},topics=[topic])
        self.assertEqual(recent['items'][0]['date'],'2026-10-28')
        body=(ROOT/TOPIC).read_text(encoding='utf-8')
        for marker in ['讀財報新聞的四本帳','句子的主詞是哪個產品','LTA（長期供應協議）']:
            self.assertIn(marker,body)

    def test_partial_scan_preserves_unattempted_and_quoted_media_boundaries(self):
        with (ROOT/'notes/research_topics/scan_log.csv').open(encoding='utf-8',newline='') as f:
            r=next(r for r in csv.DictReader(f) if r['scan_id']=='scan-2026-10-28-speaker-period-and-capacity')
        self.assertEqual(r['scope'],'partial')
        for marker in ['缺10/26及10/28','另6公司未請求','媒體引述不當公司背書','本輪未核本批PDF','新季附件不代舊季分解']:
            self.assertIn(marker,r['coverage_note'])
        method=(ROOT/'MARKET_RESEARCH_METHOD.md').read_text(encoding='utf-8')
        self.assertIn('句子的主張者',method)
        self.assertIn('海外事件另記原時區',method)

    def test_snapshot_and_unmatured_candidates_remain_honest(self):
        snap=json.loads((ROOT/'notes/research_method_reviews/2026-10-28_01.json').read_text(encoding='utf-8'))
        self.assertEqual(snap['claims']['active'],917)
        self.assertEqual(snap['monitors']['active'],168)
        self.assertEqual(snap['monitors']['dueOrOverdue'],0)
        self.assertEqual(snap['corrections']['monitorReviewEvents'],963)
        self.assertEqual(snap['freshness'],{'staleTopics':40,'staleEdges':842})
        candidates=records('notes/research_candidates/2026-09-13_verification_gaps.md','research_candidate')
        self.assertEqual([(r['rank'],r['status']) for r in candidates],[('1','watch'),('2','watch'),('3','watch')])

if __name__=='__main__':
    unittest.main()
