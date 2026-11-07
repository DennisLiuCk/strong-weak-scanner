"""Versioned evidence is not product acceptance or a renewed thesis clock."""
import csv
import unittest
from collections import Counter

from test_research_cycle_20261012 import ROOT, bd, records
from test_research_cycle_20261019 import keyed

FABRIC = "notes/research_topics/2026-08-02_open_ai_fabrics.md"
GRAPH = "notes/knowledge_graph/open_ai_fabrics.md"
AS_OF = "2026-11-07"


class ResearchCycleNovember7Test(unittest.TestCase):
    def test_fabric_thesis_clock_is_not_checklist_capture_date(self):
        meta = records(FABRIC, "research_topic")[0]
        self.assertEqual((meta["thesis_claim_id"], meta["last_reviewed_at"], meta["review_due"]),
                         ("C18", "2026-08-12", "2026-08-17"))

    def test_checklist_observation_preserves_unknown_publication_date(self):
        sources = keyed(FABRIC, "research_source", "source_id")
        source = sources["S30"]
        self.assertEqual(source["source_kind"], "living_index")
        self.assertFalse(source["published_at"])
        self.assertEqual((source["captured_at"], source["accepted_at"]), (AS_OF, AS_OF))
        self.assertEqual(source["independence_group"], sources["S18"]["independence_group"])
        self.assertIn("17993f235ddb62fe5106efb03a6774168ab55e7ca2c146a957b95f0a27f4b2b4", source["locator"])
        self.assertIn("沒有可核實的公開發布日", source["limitation"])

    def test_three_versions_and_conflict_do_not_become_full_compliance(self):
        claims = keyed(FABRIC, "research_claim", "claim_id")
        for term in ("1.0", "1.0.1", "1.1", "UEC 1.0", "釐清"):
            self.assertIn(term, claims["C29"]["claim"])
        self.assertEqual(claims["C29"]["label"], "verified")
        self.assertEqual(claims["C30"]["label"], "inference")
        self.assertIn("不是11/7發布新規格", claims["C29"]["boundary"])
        self.assertIn("T8的AND條件不變", claims["C30"]["boundary"])
        self.assertIn("原始結果", claims["C30"]["verification_needed"])

    def test_existing_monitor_retains_conjunctive_product_requirement(self):
        monitor = keyed(FABRIC, "monitoring_item", "monitor_id")["T8"]
        self.assertEqual(monitor["next_check"], AS_OF)
        self.assertIn("且具名產品版本", monitor["trigger"])
        self.assertIn("原始結果", monitor["trigger"])

    def test_graph_remains_a_standard_not_a_commercial_upgrade(self):
        edge = keyed(GRAPH, "knowledge_edge", "edge_id")["KG-FAB-I02"]
        self.assertEqual((edge["to_id"], edge["commercial_stage"], edge["materiality"]),
                         ("standard:uec", "concept", "named_product"))
        self.assertIn("#C29", edge["claim_refs"])
        self.assertIn("尚未逐條確認覆蓋", edge["boundary"])
        self.assertIn("不代表產品通過", edge["boundary"])

    def test_reader_and_homepage_receive_revision_not_new_thesis_date(self):
        text = (ROOT / FABRIC).read_text(encoding="utf8")
        for term in ("11 月補充", "誰考過", "填有產品身分及結果", "修訂紀錄（revision history）"):
            self.assertIn(term, text)
        meta = records(FABRIC, "research_topic")[0]
        topic = dict(topic_id=meta["topic_id"], title=meta["topic_id"], relpath=FABRIC,
                     meta=meta, transitions=[t for t in records(FABRIC, "transition") if t["date"] <= AS_OF])
        recent = bd.build_recent_articles(AS_OF, {}, {}, topics=[topic])
        self.assertEqual(recent["items"][0]["date"], AS_OF)

    def test_due_cohort_has_no_duplicate_successor_or_side_claim_support(self):
        with (ROOT / 'notes/research_method_reviews/monitor_reviews.csv').open(encoding='utf8', newline='') as handle:
            rows = [r for r in csv.DictReader(handle) if r['checked_at'] == AS_OF]
        self.assertEqual(len(rows), 18)
        self.assertEqual(len({(r['topic_id'], r['monitor_id']) for r in rows}), 18)
        self.assertEqual(Counter(r['result'] for r in rows),
                         {'new_support': 2, 'no_new_evidence': 1, 'not_yet_testable': 15})
        for row in rows:
            if row['result'] != 'new_support':
                self.assertEqual((row['evidence_source_ids'], row['claim_action']), ('', 'none'))
        ge = next(r for r in rows if r['topic_id'].endswith('POWER-EQUIPMENT-CONVERSION'))
        self.assertEqual(ge['result'], 'not_yet_testable')
        self.assertIn('出貨不等於當季產出', ge['notes'])

    def test_cpo_keeps_original_monitor_and_unknown_financial_materiality(self):
        path = 'notes/research_topics/2026-08-01_cpo_pluggable_coexistence.md'
        monitors = keyed(path, 'monitoring_item', 'monitor_id')
        self.assertNotIn('T8', monitors)
        self.assertEqual(monitors['T2']['status'], 'active')
        self.assertIn('量產、客戶或收入', monitors['T2']['trigger'])
        edge = keyed('notes/knowledge_graph/cpo_networking.md', 'knowledge_edge', 'edge_id')['KG-CPO-C05']
        self.assertEqual((edge['commercial_stage'], edge['materiality']), ('production', 'unknown'))
        claim = keyed(path, 'research_claim', 'claim_id')['C28']
        self.assertIn('不是客戶驗收', claim['boundary'])

    def test_existing_five_theses_do_not_inherit_article_revision(self):
        for path in [FABRIC,
                     'notes/research_topics/2026-08-01_cpo_pluggable_coexistence.md',
                     'notes/research_topics/2026-08-03_custom_hbm_scope_ladder.md',
                     'notes/research_topics/2026-09-10_dc_phase_delivery.md',
                     'notes/research_topics/2026-09-10_power_equipment_conversion.md']:
            with self.subTest(path=path):
                meta = records(path, 'research_topic')[0]
                self.assertLess(meta['last_reviewed_at'], AS_OF)
                self.assertLess(meta['review_due'], AS_OF)
                self.assertTrue(any(r['date'] == AS_OF for r in records(path, 'transition')))

    def test_backfilled_nvhbm_source_keeps_original_date(self):
        path = 'notes/research_topics/2026-08-03_custom_hbm_scope_ladder.md'
        source = keyed(path, 'research_source', 'source_id')['S16']
        claim = keyed(path, 'research_claim', 'claim_id')['C18']
        self.assertEqual((source['published_at'], claim['as_of']), ('2026-08-26', '2026-08-26'))
        self.assertEqual(source['accepted_at'], AS_OF)


if __name__ == "__main__":
    unittest.main()
