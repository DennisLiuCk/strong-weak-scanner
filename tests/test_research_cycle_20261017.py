"""October 17: issuer milestones stay separate from qualification and revenue."""
import csv
import json
import unittest
from collections import Counter

from test_research_cycle_20261012 import ROOT, bd, records


HELIOS = "notes/research_topics/2026-08-02_amd_helios_deployment_ladder.md"
CPO = "notes/research_topics/2026-08-01_cpo_pluggable_coexistence.md"
COOLING = "notes/research_topics/2026-08-02_liquid_cooling_qualification_ladder.md"
HEL_GRAPH = "notes/knowledge_graph/amd_helios.md"
CPO_GRAPH = "notes/knowledge_graph/cpo_networking.md"


def keyed(path, block, key):
    return {row[key]: row for row in records(path, block)}


class ResearchCycleOctober17Test(unittest.TestCase):
    def test_partial_reviews_do_not_claim_support_or_clear_unattempted_work(self):
        with (ROOT / "notes/research_method_reviews/monitor_reviews.csv").open(
                encoding="utf-8", newline="") as stream:
            rows = [r for r in csv.DictReader(stream) if r["checked_at"] == "2026-10-17"]
        self.assertEqual(len(rows), 69)
        self.assertEqual(len({r["review_id"] for r in rows}), 69)
        reviewed = {(r["topic_id"], r["monitor_id"]) for r in rows}
        self.assertEqual(len(reviewed), 69)
        self.assertEqual(Counter(r["result"] for r in rows),
                         {"not_yet_testable": 68, "no_new_evidence": 1})
        for row in rows:
            self.assertEqual(row["claim_action"], "none")
            self.assertFalse(row["evidence_source_ids"])
        # These eight members of the frozen 77-task cohort were not inspected.
        unattempted = {
            ("MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM", "T4"),
            ("MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY", "T10"),
            ("MI-2026-08-09-AI-RACK-EMC-CERTIFICATION", "T2"),
            ("MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE", "T3"),
            ("MI-2026-08-03-800VDC-PROTECTION-LAYERS", "T2"),
            ("MI-2026-08-03-AI-CAPACITOR-ROLE-MAP", "T2"),
            ("MI-2026-08-03-AI-CAPACITOR-ROLE-MAP", "T4"),
            ("MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY", "T2"),
        }
        known = set()
        for path in (ROOT / "notes/research_topics").glob("*.md"):
            meta = records(path, "research_topic")
            if meta:
                known.update((meta[0]["topic_id"], r["monitor_id"])
                             for r in records(path, "monitoring_item"))
        self.assertTrue(unattempted <= known)
        self.assertFalse(reviewed & unattempted)

    def test_snapshot_preserves_partial_coverage_and_unresolved_freshness(self):
        snapshot = json.loads((ROOT / "notes/research_method_reviews/2026-10-17_01.json")
                              .read_text(encoding="utf-8"))
        self.assertEqual(snapshot["monitors"]["dueOrOverdue"], 8)
        self.assertEqual(snapshot["monitors"]["overdue"], 8)
        self.assertEqual(snapshot["freshness"]["staleTopics"], 40)
        self.assertEqual(snapshot["scans"]["latestScope"], "partial")
        self.assertEqual(snapshot["corrections"]["monitorReviewEvents"], 623)
        self.assertFalse(snapshot["calibration"]["descriptiveBreakdownReady"])

    def test_three_side_updates_do_not_reset_main_evidence_clock(self):
        expected = {
            HELIOS: ("C11", "2026-08-12", "2026-08-15"),
            CPO: ("C9", "2026-08-12", "2026-08-26"),
            COOLING: ("C21", "2026-08-14", "2026-08-16"),
        }
        for path, clock in expected.items():
            with self.subTest(path=path):
                meta = records(path, "research_topic")[0]
                self.assertEqual(tuple(meta[k] for k in (
                    "thesis_claim_id", "last_reviewed_at", "review_due")), clock)

    def test_helios_initial_operation_is_one_issuer_chain_not_four_acceptances(self):
        claims = keyed(HELIOS, "research_claim", "claim_id")
        sources = keyed(HELIOS, "research_source", "source_id")
        claim = claims["C29"]
        self.assertEqual(claim["supporting_source_ids"], "S26")
        self.assertEqual(sources["S26"]["published_at"], "2026-10-12")
        self.assertEqual(sources["S26"]["captured_at"], "2026-10-17")
        self.assertEqual(sources["S26"]["independence_group"], "amd")
        for name in ("OpenAI", "Meta", "Microsoft", "Oracle"):
            self.assertIn(name, claim["claim"])
        for boundary in ("一條供應商消息鏈", "不是四個獨立", "不能判定所有驗證已完成"):
            self.assertIn(boundary, claim["boundary"])
        self.assertIn("不能把 AMD 四家初始系統接成緯穎供貨", claims["C30"]["boundary"])
        topic = (ROOT / HELIOS).read_text(encoding="utf-8")
        self.assertNotIn("仍只有 2026 下半年 shipment／volume deployment 的前瞻時程", topic)
        self.assertIn("新增 T14 的下一節點是 2026-10-23", topic)

    def test_helios_graph_preserves_initial_operation_and_unknown_financials(self):
        edges = keyed(HEL_GRAPH, "knowledge_edge", "edge_id")
        for edge_id in ("KG-HEL-C02", "KG-HEL-C03", "KG-HEL-C04", "KG-HEL-C15"):
            edge = edges[edge_id]
            self.assertIn("#C29", edge["claim_refs"])
            self.assertEqual(edge["commercial_stage"], "validation")
            self.assertEqual(edge["materiality"], "named_product")
            self.assertNotEqual(edge["exclusivity"], "sole_source")
        self.assertEqual(edges["KG-HEL-I04"]["commercial_stage"], "deployment")
        self.assertIn("初始系統", edges["KG-HEL-I04"]["boundary"])
        self.assertIn("不是獨立驗收", edges["KG-HEL-I04"]["boundary"])

    def test_cpo_demo_is_integration_not_signal_mode_or_qualification(self):
        meta = records(CPO, "research_topic")[0]
        self.assertIn("6669", meta["stock_ids"].split(","))
        self.assertIn("serverodm", meta["group_ids"].split(","))
        impact = next(r for r in records(CPO, "impact") if r["group_id"] == "serverodm")
        self.assertEqual(impact["direction"], "uncertain")
        self.assertIn("不是獨立量測", impact["evidence_boundary"])
        claims = keyed(CPO, "research_claim", "claim_id")
        sources = keyed(CPO, "research_source", "source_id")
        self.assertEqual(sources["S19"]["published_at"], "2026-10-13")
        self.assertEqual(sources["S19"]["captured_at"], "2026-10-17")
        self.assertEqual(claims["C25"]["supporting_source_ids"], "S19")
        for boundary in ("不是獨立現場量測", "未列訊號處理模式", "量產出貨", "收入"):
            self.assertIn(boundary, claims["C25"]["boundary"])
        edges = keyed(CPO_GRAPH, "knowledge_edge", "edge_id")
        for edge_id in ("KG-CPO-C04", "KG-CPO-I19"):
            edge = edges[edge_id]
            self.assertTrue(edge["claim_refs"].endswith("#C25"))
            self.assertEqual(edge["commercial_stage"], "integration")
            self.assertEqual(edge["materiality"], "named_product")
            self.assertEqual(edge["exclusivity"], "unknown")

    def test_delta_ratings_do_not_become_same_product_downgrade(self):
        claims = keyed(COOLING, "research_claim", "claim_id")
        sources = keyed(COOLING, "research_source", "source_id")
        self.assertEqual(sources["S34"]["independence_group"],
                         sources["S35"]["independence_group"])
        self.assertEqual(sources["S34"]["published_at"], "2026-10-08")
        self.assertEqual(sources["S35"]["published_at"], "2026-10-15")
        self.assertIn("2027年第一季", claims["C40"]["claim"])
        self.assertIn("3°C條件只屬", claims["C40"]["boundary"])
        self.assertIn("不能稱為同款降規", claims["C41"]["boundary"])
        self.assertEqual(claims["C42"]["label"], "inference")
        self.assertIn("不可排成同款設備", claims["C42"]["claim"])
        self.assertIn("不是同條件性能比較", claims["C42"]["boundary"])
        edge = keyed("notes/knowledge_graph/liquid_cooling.md", "knowledge_edge", "edge_id")["KG-LC-C10"]
        self.assertEqual(edge["commercial_stage"], "capability")
        self.assertEqual(edge["materiality"], "named_product")
        self.assertEqual(edge["exclusivity"], "unknown")
        self.assertIn("不能改為已量產", edge["boundary"])

    def test_three_source_bound_revisions_reach_homepage_without_build_snapshot(self):
        topics = []
        for path in (HELIOS, CPO, COOLING):
            meta = records(path, "research_topic")[0]
            transitions = records(path, "transition")
            current = [r for r in transitions if r["date"] == "2026-10-17"]
            self.assertEqual(len(current), 1)
            self.assertTrue(current[0]["evidence"].startswith("sources:"))
            topic = {"topic_id": meta["topic_id"], "title": meta["topic_id"],
                     "relpath": path, "meta": meta, "transitions": transitions}
            self.assertEqual(bd._topic_content_date(topic), "2026-10-17")
            topics.append(topic)
        recent = bd.build_recent_articles("2026-10-17", {}, {}, topics=topics)
        self.assertEqual({r["researchId"] for r in recent["items"]},
                         {"topic-" + t["topic_id"] for t in topics})

    def test_new_monitors_require_same_object_and_keep_old_trigger(self):
        hel = keyed(HELIOS, "monitoring_item", "monitor_id")
        cpo = keyed(CPO, "monitoring_item", "monitor_id")
        self.assertEqual(hel["T14"]["next_check"], "2026-10-23")
        self.assertEqual(cpo["T6"]["next_check"], "2026-10-23")
        self.assertIn("配置版本", hel["T14"]["trigger"])
        self.assertIn("原測試對象", cpo["T6"]["invalidation"])
        self.assertIn("品牌系統 validation 完成", hel["T8"]["trigger"])
        self.assertIn("首次公開三軸組態", cpo["T5"]["trigger"])


if __name__ == "__main__":
    unittest.main()
