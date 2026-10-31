"""Local evidence increments must not silently complete broader theses."""
import csv
import unittest
from test_research_cycle_20261012 import ROOT, bd, records
from test_research_cycle_20261019 import keyed

POWER='notes/research_topics/2026-08-01_800vdc_execution_readiness.md'
FAB='notes/research_topics/2026-08-02_open_ai_fabrics.md'
GEV='notes/research_topics/2026-09-10_power_equipment_conversion.md'

class ResearchCycleOctober31Test(unittest.TestCase):
    def test_due_reviews_preserve_partial_outcomes(self):
        with (ROOT/'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf8',newline='') as f:
            rows=[r for r in csv.DictReader(f) if r['checked_at']=='2026-10-31']
        self.assertEqual(len(rows),56)
        self.assertEqual(len({(r['topic_id'],r['monitor_id']) for r in rows}),56)
        supported={(r['topic_id'],r['monitor_id']) for r in rows if r['result']=='new_support'}
        self.assertEqual(supported,{('MI-2026-08-02-OPEN-AI-FABRICS','T6'),('MI-2026-09-10-POWER-EQUIPMENT-CONVERSION','T2')})
        for r in rows:
            self.assertGreater(r['next_check'],r['checked_at'])
            self.assertIn('原有效期限',r['notes'])
            self.assertIn('未完成／邊界',r['notes'])
            if r['result']!='new_support':
                self.assertEqual((r['claim_action'],r['evidence_source_ids']),('none',''))

    def test_liteon_stage_period_and_labels(self):
        c=keyed(POWER,'research_claim','claim_id')
        self.assertEqual([c[i]['label'] for i in ['C26','C27','C28','C29']],['verified','verified','inference','unverified'])
        self.assertIn('2026Q4展望',c['C26']['claim'])
        self.assertIn('而非展望已實現',c['C26']['basis'])
        for marker in ['前三季','第三季','80%','近60%','逾30%']:
            self.assertIn(marker,c['C27']['claim'])
        self.assertIn('不是同義集合',c['C27']['boundary'])
        m=keyed(POWER,'monitoring_item','monitor_id')
        for k in ['T5','T6']:
            self.assertTrue(m[k]['invalidation'])
            self.assertEqual(m[k]['watch_source_ids'],'S23,S6')

    def test_old_thesis_clock_and_new_homepage_revision(self):
        expected={POWER:('C13','2026-08-12','2026-09-12'),FAB:('C18','2026-08-12','2026-08-17'),GEV:('C1','2026-09-10','2026-10-31')}
        for path in [POWER,FAB,GEV]:
            meta=records(path,'research_topic')[0]
            if path in expected:
                self.assertEqual(tuple(meta[k] for k in ['thesis_claim_id','last_reviewed_at','review_due']),expected[path])
            transitions=[r for r in records(path,'transition') if r['date']<='2026-10-31']
            topic=dict(topic_id=meta['topic_id'],title=meta['topic_id'],relpath=path,meta=meta,transitions=transitions)
            recent=bd.build_recent_articles('2026-10-31',{},{},topics=[topic])
            self.assertEqual(recent['items'][0]['date'],'2026-10-31')

    def test_uec_acquisition_is_not_full_compliance(self):
        c=keyed(FAB,'research_claim','claim_id')
        self.assertIn('逐條全文審閱或產品合規',c['C27']['boundary'])
        self.assertIn('規範性修正',c['C28']['claim'])
        m=keyed(FAB,'monitoring_item','monitor_id')
        self.assertEqual(m['T6']['claim_ids'],'C24,C26')
        self.assertEqual(m['T6']['source_ids'],'S25')
        self.assertIn('或',m['T6']['trigger'])
        self.assertIn('T8',m)

    def test_gev_stock_and_flow_scope(self):
        c=keyed(GEV,'research_claim','claim_id')['C8']
        for marker in ['45,747','25,950','19,797','10,688','Prolec GE']:
            self.assertIn(marker,c['claim'])
        self.assertIn('九個月而非Q3單季',c['boundary'])
        self.assertEqual(45747-25950,19797)
        self.assertEqual(keyed(GEV,'monitoring_item','monitor_id')['T2']['claim_ids'],'C3,C5,C7')

    def test_graph_changes_are_not_company_upgrades(self):
        edge=keyed('notes/knowledge_graph/800vdc_execution_readiness.md','knowledge_edge','edge_id')['KG-8ER-I20']
        self.assertEqual((edge['view'],edge['evidence_state'],edge['commercial_stage'],edge['materiality']),('industry','inference','concept','adjacent'))
        self.assertIn('不升級公司曝險',edge['boundary'])
        method=(ROOT/'MARKET_RESEARCH_METHOD.md').read_text(encoding='utf8')
        self.assertIn('AND／OR',method)
        self.assertIn('第一個明確限流即停止本批',method)

if __name__=='__main__':
    unittest.main()
