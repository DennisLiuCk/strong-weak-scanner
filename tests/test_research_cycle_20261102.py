"""Monthly review separates work completion, evidence, and economic provenance."""
import csv
import json
import unittest
from test_research_cycle_20261012 import ROOT, bd, records
from test_research_cycle_20261019 import keyed

CPO='notes/research_topics/2026-08-01_cpo_pluggable_coexistence.md'
TAM='notes/research_topics/2026-08-01_inference_compute_tester_tam.md'
OFAC='notes/research_topics/2026-07-23_us_section_301_taiwan.md'
YAGEO='notes/research_topics/2026-07-30_yageo_q2_earnings_call.md'

class ResearchCycleNovember2Test(unittest.TestCase):
    def test_frozen_due_cohort_results_and_non_evidence_clocks(self):
        with (ROOT/'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf8',newline='') as f:
            rows=[r for r in csv.DictReader(f) if r['checked_at']=='2026-11-02']
        self.assertEqual(len(rows),49)
        self.assertEqual(len({(r['topic_id'],r['monitor_id']) for r in rows}),49)
        supported={(r['topic_id'],r['monitor_id']) for r in rows if r['result']=='new_support'}
        self.assertEqual(supported,{('MI-2026-07-23-US-SECTION301-TAIWAN','T5'),('MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM','T3')})
        self.assertEqual(sum(r['result']=='not_yet_testable' for r in rows),45)
        self.assertEqual(sum(r['result']=='no_new_evidence' for r in rows),2)
        for r in rows:
            self.assertGreater(r['next_check'],r['checked_at'])
            self.assertIn('原有效期限',r['notes'])
            self.assertIn('未完成／邊界',r['notes'])
            if r['result']!='new_support':
                self.assertEqual((r['claim_action'],r['evidence_source_ids']),('none',''))

    def test_tam_unchanged_capacity_is_not_shipment(self):
        c=keyed(TAM,'research_claim','claim_id')
        for marker in ['維持七月','10.5–11.5','2.5–3.0','13.0–14.5']:
            self.assertIn(marker,c['C24']['claim'])
        self.assertIn('年產能不是',c['C25']['boundary'])
        self.assertIn('實際產量',c['C25']['boundary'])
        self.assertEqual(c['C26']['label'],'inference')
        self.assertIn('2027年一月',c['C27']['claim'])

    def test_cpo_overlap_and_event_denominators(self):
        sources=keyed(CPO,'research_source','source_id')
        for sid in ['S21','S22','S23']:
            self.assertEqual(sources[sid]['independence_group'],sources['S12']['independence_group'])
        claims=keyed(CPO,'research_claim','claim_id')
        self.assertIn('不同溫度',claims['C27']['claim'])
        self.assertIn('零不可維修故障替代零中斷',claims['C27']['claim'])
        self.assertIn('T7',keyed(CPO,'monitoring_item','monitor_id'))

    def test_ofac_current_guidance_not_new_obligation_or_authorization(self):
        c=keyed(OFAC,'research_claim','claim_id')
        self.assertEqual([c[k]['label'] for k in ['C18','C19','C20','C21']],['verified','verified','verified','inference'])
        self.assertIn('十個工作日',c['C20']['claim'])
        self.assertIn('報告不等於授權',c['C20']['boundary'])
        self.assertIn('未對照舊版',c['C18']['boundary'])
        self.assertIn('T6',keyed(OFAC,'monitoring_item','monitor_id'))

    def test_revision_dates_do_not_require_thesis_clock_refresh(self):
        for path in [CPO,TAM,OFAC,YAGEO]:
            meta=records(path,'research_topic')[0]
            self.assertLess(meta['last_reviewed_at'],'2026-11-02')
            transitions=[r for r in records(path,'transition') if r['date']<='2026-11-02']
            topic=dict(topic_id=meta['topic_id'],title=meta['topic_id'],relpath=path,meta=meta,transitions=transitions)
            recent=bd.build_recent_articles('2026-11-02',{},{},topics=[topic])
            self.assertEqual(recent['items'][0]['date'],'2026-11-02')

    def test_monthly_snapshot_exposes_unresolved_work_and_source_limit(self):
        snap=json.loads((ROOT/'notes/research_method_reviews/2026-11-02_01.json').read_text(encoding='utf8'))
        self.assertEqual(snap['monitors']['dueOrOverdue'],0)
        self.assertEqual(snap['freshness']['staleTopics'],42)
        counts=snap['reviewProgress']['latestOutcomeCounts']
        self.assertEqual(sum(counts.values()),175)
        self.assertEqual(counts['not_yet_testable'],140)
        self.assertEqual(counts['never_reviewed'],16)
        self.assertIn('結構檢查',snap['sources']['boundary'])
        gate=next(g for g in snap['gates'] if g['id']=='cross_check_depth')
        self.assertEqual(gate['label'],'來源群組結構')
        self.assertIn('不是兩條獨立經濟驗證',records(YAGEO,'research_topic')[0]['confidence_basis'])
        self.assertNotIn('兩條獨立官方來源',keyed('notes/knowledge_graph/yageo_q2_financial_materiality.md','knowledge_edge','edge_id')['KG-YQ2-C01']['boundary'])

if __name__=='__main__':
    unittest.main()
