"""Design requirements, product test results, and economic event states differ."""
import csv
import json
import unittest

from test_research_cycle_20261012 import ROOT, bd, records
from test_research_cycle_20261019 import keyed

RUBIN='notes/research_topics/2026-07-21_nvidia_vera_rubin_production.md'
BUFFER='notes/research_topics/2026-08-03_ai_power_buffering_hierarchy.md'


class ResearchCycleOctober21Test(unittest.TestCase):
    def test_due_cohort_is_attempts_not_product_support(self):
        with (ROOT/'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf-8',newline='') as stream:
            rows=[r for r in csv.DictReader(stream) if r['checked_at']=='2026-10-21']
        self.assertEqual(len(rows),77)
        self.assertEqual(len({(r['topic_id'],r['monitor_id']) for r in rows}),77)
        for r in rows:
            self.assertEqual(r['result'],'not_yet_testable')
            self.assertEqual(r['claim_action'],'none')
            self.assertFalse(r['evidence_source_ids'])
            self.assertIn('未完成／邊界',r['notes'])
            self.assertIn('來源：',r['notes'])
            self.assertGreater(r['next_check'],r['checked_at'])
        chip=next(r for r in rows if r['topic_id'].endswith('CHIPLET-DESIGN-HANDOFF-CONTRACTS') and r['monitor_id']=='T1')
        self.assertIn('原有效期限2026-10-20',chip['notes'])

    def test_dsx_reference_design_has_no_nvl72_acceptance_upgrade(self):
        src=keyed(RUBIN,'research_source','source_id')['S27']
        claims=keyed(RUBIN,'research_claim','claim_id')
        self.assertIn('40fff1e11beb9fb33e38726d5b6b476409a65ecc7e88efbdb3db13e040520513',src['locator'])
        self.assertEqual(src['published_at'],'2026-10-21')
        self.assertIn('validation plan can cover',claims['C27']['basis'])
        self.assertEqual(claims['C28']['label'],'inference')
        edge=keyed('notes/knowledge_graph/vera_rubin_delivery_contract.md','knowledge_edge','edge_id')['KG-VRD-I21']
        self.assertIn('未指名NVL72',edge['boundary'])
        self.assertEqual((edge['commercial_stage'],edge['materiality']),('concept','adjacent'))

    def test_mt_diablo_is_conditional_requirement_not_device_measurement(self):
        src=keyed(BUFFER,'research_source','source_id')['S10']
        claims=keyed(BUFFER,'research_claim','claim_id')
        self.assertEqual(src['published_at'],'2026-10-08')
        self.assertEqual(src['captured_at'],'2026-10-21')
        self.assertIn('87aa3f2df88ca7b3e01bc6a9a499779970662e5c9f7b0f18a19a9e95b0bea2a4',src['locator'])
        self.assertIn('不應觸發BBU',claims['C18']['claim'])
        for text in ('選用BBU','100%負載','45至90秒','輸出端'):
            self.assertIn(text,claims['C19']['claim'])
        self.assertIn('不是產品測試結果',src['limitation'])
        edge=keyed('notes/knowledge_graph/ai_power_buffering.md','knowledge_edge','edge_id')['KG-APB-I19']
        self.assertEqual((edge['commercial_stage'],edge['materiality']),('concept','adjacent'))

    def test_revisions_reach_homepage_without_main_clock_change(self):
        topics=[]
        for path,clock in [(RUBIN,('C11','2026-08-12','2026-08-15')),
                           (BUFFER,('C4','2026-08-03','2026-09-01'))]:
            meta=records(path,'research_topic')[0]
            self.assertEqual(tuple(meta[k] for k in ('thesis_claim_id','last_reviewed_at','review_due')),clock)
            transitions=records(path,'transition')
            self.assertTrue(any(t['date']=='2026-10-21' and t['evidence'].startswith('sources:') for t in transitions))
            topics.append(dict(topic_id=meta['topic_id'],title=meta['topic_id'],relpath=path,meta=meta,transitions=transitions))
        recent=bd.build_recent_articles('2026-10-21',{},{},topics=topics)
        self.assertEqual({r['researchId'] for r in recent['items']},{'topic-'+t['topic_id'] for t in topics})
        self.assertTrue(all(r['date']=='2026-10-21' for r in recent['items']))

    def test_scan_keeps_missing_dates_rate_limit_and_event_units(self):
        with (ROOT/'notes/research_topics/scan_log.csv').open(encoding='utf-8',newline='') as stream:
            row=next(r for r in csv.DictReader(stream) if r['scan_id']=='scan-2026-10-21-design-tests-and-event-state')
        self.assertEqual(row['scope'],'partial')
        for text in ('缺10/19及10/21','4批設備不等4台','查詢過量','未核本批PDF'):
            self.assertIn(text,row['coverage_note'])

    def test_snapshot_keeps_stale_evidence_and_frozen_watchlist(self):
        snap=json.loads((ROOT/'notes/research_method_reviews/2026-10-21_01.json').read_text(encoding='utf-8'))
        self.assertEqual(snap['freshness']['staleTopics'],40)
        self.assertEqual(snap['corrections']['monitorReviewEvents'],754)
        self.assertEqual(snap['monitors']['dueOrOverdue'],0)
        self.assertEqual(snap['claims']['active'],905)
        candidates=records('notes/research_candidates/2026-09-13_verification_gaps.md','research_candidate')
        self.assertEqual([(r['rank'],r['status']) for r in candidates],[('1','watch'),('2','watch'),('3','watch')])


if __name__=='__main__':
    unittest.main()
