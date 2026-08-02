# -*- coding: utf-8 -*-
"""研究方法快照、到期 review event 與 dashboard 契約。"""
import datetime as dt
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import research_method_audit as audit


class ResearchMethodAuditTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.as_of = dt.date(2026, 8, 2)
        cls.topics, cls.graph, cls.radar, cls.scan = audit._load_context(cls.as_of)
        cls.reviews = audit.load_monitor_reviews(cls.topics, cls.as_of, strict=True)
        cls.current = audit.compute_method_audit(
            cls.topics, cls.graph, cls.radar, cls.reviews, cls.scan, cls.as_of,
        )
        cls.latest = audit.load_method_audit(strict=True)

    def test_baseline_snapshot_matches_current_registry(self):
        self.assertEqual(self.latest["snapshotId"], "RMA-2026-08-02-03")
        self.assertEqual(self.latest["methodologyVersion"], "1.2")
        self.assertEqual(
            self.latest["registryFingerprint"], self.current["registryFingerprint"],
        )
        self.assertEqual(len(self.latest["history"]), 3)

    def test_audit_exposes_counts_without_fake_accuracy_score(self):
        self.assertEqual(self.current["scope"]["topics"], 24)
        self.assertEqual(self.current["scope"]["graphs"], 14)
        self.assertEqual(self.current["scope"]["scanEvents"], 10)
        self.assertEqual(self.current["claims"]["active"], 141)
        self.assertEqual(self.current["graphs"]["activeEdges"], 206)
        self.assertEqual(self.current["graphs"]["traceableEdges"], 206)
        self.assertEqual(self.current["monitors"]["reviewedMature"], 2)
        self.assertEqual(self.current["corrections"]["monitorReviewEvents"], 2)
        self.assertEqual(self.current["corrections"]["resultCounts"]["no_new_evidence"], 2)
        self.assertEqual(self.current["corrections"]["supersededOrRefutedClaims"], 2)
        self.assertEqual(self.current["scans"]["latestId"],
                         "scan-2026-08-02-hbf-high-na-esun-correction")
        self.assertEqual(self.current["scans"]["latestScope"], "partial")
        self.assertEqual(self.current["scans"]["overdue"], 0)
        self.assertFalse(self.current["calibration"]["descriptiveRateReady"])
        self.assertIsNone(self.current["calibration"]["supportRate"])
        self.assertNotIn("score", self.current)

    def test_every_gate_keeps_its_own_status_and_boundary(self):
        gates = {item["id"]: item for item in self.current["gates"]}
        self.assertEqual(
            set(gates),
            {
                "traceability", "cross_check_depth", "falsifiability",
                "freshness", "correction_learning", "scan_accountability",
                "calibration",
            },
        )
        self.assertEqual(gates["cross_check_depth"]["status"], "attention")
        self.assertEqual(gates["freshness"]["status"], "attention")
        self.assertEqual(gates["correction_learning"]["status"], "pass")
        self.assertEqual(gates["scan_accountability"]["status"], "attention")
        self.assertEqual(gates["calibration"]["status"], "not_ready")
        for gate in gates.values():
            self.assertTrue(gate["observed"])
            self.assertTrue(gate["boundary"])

    def test_cross_check_gate_names_every_topic_missing_a_second_chain(self):
        missing = self.current["sources"]["thesesNeedingSecondIndependentGroup"]
        self.assertEqual(
            missing,
            [
                "MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP",
                "MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL",
                "MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION",
            ],
        )
        self.assertEqual(self.current["sources"]["thesesWithTwoIndependentGroups"], 21)
        gate = next(item for item in self.current["gates"]
                    if item["id"] == "cross_check_depth")
        for topic_id in missing:
            self.assertIn(topic_id, gate["observed"])

    def test_method_audit_uses_same_corporate_domain_grouping_as_topic_lint(self):
        investor = {"url": "https://investor.nvidia.com/news/example"}
        newsroom = {"url": "https://www.nvidia.com/en-us/news/example"}
        self.assertEqual(audit._source_group(investor), audit._source_group(newsroom))

    def test_no_new_evidence_reviews_do_not_claim_sources_or_actions(self):
        for row in self.reviews:
            self.assertEqual(row["result"], "no_new_evidence")
            self.assertEqual(row["evidence_source_ids"], [])
            self.assertEqual(row["claim_action"], "none")
        self.assertEqual(self.current["monitors"]["dueOrOverdue"], 0)
        self.assertEqual(self.current["freshness"]["staleTopics"], 2)

    def test_evidence_result_requires_registered_source(self):
        text = (
            ",".join(audit.REVIEW_HEADER) + "\n"
            "MR-2026-08-02-TEST,2026-08-02,"
            "MI-2026-07-23-US-SECTION301-TAIWAN,T1,new_support,,none,"
            "2026-08-09,missing source\n"
        )
        _, errors = audit._read_review_text(text, self.topics, self.as_of)
        self.assertTrue(any("必須引用已登錄 source" in error for error in errors))

    def test_dashboard_and_runbooks_publish_method_audit(self):
        builder = (SCRIPTS / "build_dashboard.py").read_text(encoding="utf-8")
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        method = (ROOT / "MARKET_RESEARCH_METHOD.md").read_text(encoding="utf-8")
        maintenance = (ROOT / "RESEARCH_MAINTENANCE.md").read_text(encoding="utf-8")
        workflow = (ROOT / ".github" / "workflows" / "qualitative-quality.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn('research_library["methodAudit"] = load_method_audit(', builder)
        for token in (
            'id="methodAudit"', "const AUDIT=LIB.methodAudit", "function renderMethodAudit()",
            "方法健康度（不合成分數）", "逐項顯示可追溯、獨立交叉驗證",
            "掃描覆蓋問責", "scope.scanEvents",
        ):
            self.assertIn(token, template)
        self.assertIn("monitor_reviews.csv", method)
        self.assertIn("獨立交叉驗證", method)
        self.assertIn("每月方法回顧", maintenance)
        self.assertIn("掃描覆蓋問責", method)
        self.assertIn("python scripts/research_method_audit.py --lint", workflow)


if __name__ == "__main__":
    unittest.main()
