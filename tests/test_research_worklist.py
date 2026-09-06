import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import research_worklist as rw


def item(target, kind, priority="P1", due="2026-08-31"):
    return dict(target=target, kind=kind, priority=priority, due=due, detail=kind)


class WorklistTest(unittest.TestCase):
    def test_review_schedule_only_defers_topic_checks_not_actions_or_quality(self):
        alerts = [item("topic:A", "topic_due"), item("topic:B", "topic_due"),
                  item("topic:B", "topic_action_due"), item("topic:C", "topic_due", "P0")]
        snapshot = {"items": alerts, "as_of": "2026-09-07"}
        schedule = {f"topic:{t}": "2026-09-14" for t in "ABC"}
        result = rw.build_worklist(snapshot, 5, schedule)
        self.assertEqual([g["target"] for g in result["reviewed_waiting"]], ["topic:A"])
        self.assertEqual({g["target"] for g in result["selected"]}, {"topic:B", "topic:C"})
        self.assertEqual(result["reviewed_waiting"][0]["due"], "2026-08-31")

    def test_multiple_alerts_become_one_work_item_without_losing_deadlines(self):
        items = [item("stock:A", "formal_note_due"),
                 item("stock:A", "formal_note_financial_period", "P2", "2026-09-07"),
                 item("stock:B", "formal_note_due", due="2026-08-01")]
        result = rw.build_worklist({"items": items, "as_of": "2026-09-07"}, 1)
        self.assertEqual((result["raw_alerts"], result["work_items"], result["remaining"]), (3, 2, 1))
        selected = result["selected"][0]
        self.assertEqual((selected["target"], selected["due"]), ("stock:A", "2026-08-31"))
        self.assertEqual(selected["items"], items[:2])
        self.assertEqual(rw.build_worklist({"items": list(reversed(items)), "as_of": "x"}, 1)["selected"][0]["target"], "stock:A")

    def test_limit_never_hides_p0_or_promotes_p2_over_p1(self):
        items = [item(str(i), "quality", "P0") for i in range(4)]
        items += [item("stock:A", "formal_note_financial_period", "P2"), item("stock:B", "hypothesis_due")]
        result = rw.build_worklist({"items": items, "as_of": "2026-09-07"}, 1)
        self.assertEqual(len(result["selected"]), 5)
        self.assertEqual(result["selected"][-1]["target"], "stock:B")
        with self.assertRaises(ValueError):
            rw.build_worklist({"items": []}, 0)
