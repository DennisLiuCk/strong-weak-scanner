# -*- coding: utf-8 -*-
"""首頁近期研究文章：日期、證據層級、排序與可操作 UI 契約。"""
import inspect
import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_dashboard as bd


def note(date, stock_id, verification="independently_verified", **overrides):
    result = {
        "stock_id": stock_id,
        "last_updated": date,
        "verification": verification,
        "quality_invalid": False,
        "quality_errors": [],
        "summary": "正式筆記的**一句話**摘要。",
        "relpath": f"notes/qualitative/{stock_id}_公司.md",
    }
    result.update(overrides)
    return result


def report(date, stock_id, **overrides):
    result = {
        "stock_id": stock_id,
        "quality_invalid": False,
        "quality_errors": [],
        "narrative": {"updated": date},
        "hypotheses": [
            {"title": "第一項可證偽主張"},
            {"title": "第二項可證偽主張"},
        ],
        "relpath": f"notes/leading_hypotheses/{stock_id}_公司.md",
    }
    result.update(overrides)
    return result


class RecentResearchArticlesTest(unittest.TestCase):
    def test_article_date_can_advance_market_anchor_and_same_day_types_both_survive(self):
        notes = {
            "1111": note("2026-07-29", "1111", verification="ai_draft"),
            # 文章 anchor 為 7/29 時，14 個日曆日含首尾是 7/16～7/29；7/15 必須排除。
            "9999": note("2026-07-15", "9999"),
        }
        reports = {"1111": report("2026-07-29", "1111")}
        topics = [{
            "meta": {"last_reviewed_at": "2026-07-28"},
            "captured_at": "2026-07-27",
            "stock_ids": ["1111"],
            "group_ids": ["serverodm"],
            "title": "平台量產進度",
            "relpath": "notes/research_topics/platform.md",
            "quality_invalid": False,
            "quality_errors": [],
        }]
        events = {"all": [{
            "subject": "tsmc",
            "content_as_of": "2026-07-27",
            "event_date": "2026-07-26",
            "title": "台積電法說事件錨點",
            "verification": "partially_verified",
            "relpath": "notes/events/tsmc.md",
            "quality_errors": [],
        }]}

        feed = bd.build_recent_articles(
            "2026-07-28", notes, reports, events, topics,
            {"1111": "測試公司", "9999": "舊公司"},
        )

        self.assertEqual(feed["anchor"], "2026-07-29")
        self.assertEqual(feed["start"], "2026-07-16")
        self.assertEqual(feed["days"], 14)
        self.assertEqual(feed["total"], 4)
        self.assertEqual(
            {row["type"]: row["count"] for row in feed["counts"]},
            {"formal_note": 1, "narrative": 1, "topic": 2},
        )
        self.assertEqual(
            [(row["date"], row["type"], row["stockId"]) for row in feed["items"]],
            [
                ("2026-07-29", "formal_note", "1111"),
                ("2026-07-29", "narrative", "1111"),
                ("2026-07-28", "topic", "1111"),
                ("2026-07-27", "topic", "2330"),
            ],
        )
        self.assertEqual(feed["items"][0]["status"], "AI 草稿・未獨立查核")
        self.assertNotIn("**", feed["items"][0]["title"])
        self.assertEqual(feed["items"][1]["status"], "觀察層・不等於事實認證")
        self.assertEqual(feed["items"][0]["subject"], "1111 測試公司")
        self.assertEqual(feed["items"][3]["researchId"], "event-tsmc-2026-07-26")

    def test_invalid_metadata_cannot_drag_anchor_to_a_bad_future_date(self):
        notes = {
            "1111": note("2099-01-01", "1111", quality_invalid=True),
        }
        reports = {"2222": report("2026-07-28", "2222")}
        feed = bd.build_recent_articles(
            "2026-07-28", notes, reports, {"all": []}, [],
            {"1111": "壞日期", "2222": "有效文章"},
        )
        self.assertEqual(feed["anchor"], "2026-07-28")
        self.assertEqual(feed["total"], 1)
        self.assertEqual(feed["items"][0]["stockId"], "2222")

    def test_same_date_same_type_sorts_by_stock_id_not_input_order(self):
        notes = {
            "2222": note("2026-07-29", "2222"),
            "1111": note("2026-07-29", "1111"),
        }
        feed = bd.build_recent_articles(
            "2026-07-29", notes, {}, {"all": []}, [],
            {"1111": "甲公司", "2222": "乙公司"},
        )
        self.assertEqual([item["stockId"] for item in feed["items"]], ["1111", "2222"])

    def test_market_topics_and_event_anchors_use_the_documented_fallback_dates(self):
        topics = [{
            "meta": {"last_reviewed_at": ""},
            "captured_at": "2026-07-20",
            "stock_ids": [],
            "group_ids": [],
            "title": "沒有後續複核日的候選議題",
            "relpath": "notes/research_topics/fallback.md",
            "quality_invalid": False,
            "quality_errors": [],
        }]
        events = {"all": [{
            "subject": "tsmc",
            "content_as_of": None,
            "event_date": "2026-07-21",
            "title": "事件日期備援",
            "verification": "independently_verified",
            "relpath": "notes/events/fallback.md",
            "quality_errors": [],
        }]}
        feed = bd.build_recent_articles(
            "2026-07-29", {}, {}, events, topics, {},
        )
        self.assertEqual(
            [(row["date"], row["type"]) for row in feed["items"]],
            [("2026-07-21", "topic"), ("2026-07-20", "topic")],
        )

    def test_topic_transition_advances_content_date_without_refreshing_evidence_clock(self):
        topic = {
            "topic_id": "MI-2026-07-29-CONTENT-UPDATE",
            "meta": {"last_reviewed_at": "2026-07-29"},
            "captured_at": "2026-07-28",
            "transitions": [{
                "date": "2026-08-01", "from": "triaged", "to": "triaged",
                "reason": "method_update_without_thesis_clock_refresh",
                "evidence": "sources:S2",
            }],
            "last_evidence_at": "2026-07-29",
            "stock_ids": [], "group_ids": ["thermal"],
            "title": "方法補強仍應出現在最新內容",
            "relpath": "notes/research_topics/content-update.md",
            "quality_invalid": False, "quality_errors": [],
        }

        feed = bd.build_recent_articles(
            "2026-07-31", {}, {}, {"all": []}, [topic], {},
        )

        self.assertEqual(feed["anchor"], "2026-08-01")
        self.assertEqual(feed["items"][0]["date"], "2026-08-01")
        self.assertEqual(topic["meta"]["last_reviewed_at"], "2026-07-29")
        self.assertEqual(topic["last_evidence_at"], "2026-07-29")
        self.assertIn(
            "topic_date = _topic_content_date(topic)",
            inspect.getsource(bd.build_research_library),
        )

    def test_feed_has_no_wall_clock_or_file_mtime_dependency(self):
        source = inspect.getsource(bd.build_recent_articles)
        self.assertNotIn("today", source)
        self.assertNotIn("mtime", source)
        self.assertNotIn("datetime.now", source)

    def test_progress_uses_library_total_and_keeps_every_latest_batch_article(self):
        notes = {"1111": note("2026-07-29", "1111")}
        topics = [
            {
                "meta": {"last_reviewed_at": "2026-07-30"},
                "captured_at": "2026-07-30",
                "topic_id": topic_id,
                "stock_ids": [],
                "group_ids": ["packtest"],
                "title": title,
                "relpath": f"notes/research_topics/{topic_id}.md",
                "quality_invalid": False,
                "quality_errors": [],
            }
            for topic_id, title in (("TOPIC-A", "同日新研究 A"), ("TOPIC-B", "同日新研究 B"))
        ]
        feed = bd.build_recent_articles(
            "2026-07-30", notes, {}, {"all": []}, topics, {"1111": "測試公司"},
        )
        library_articles = [
            {"id": item["researchId"], "date": item["date"]} for item in feed["items"]
        ]
        progress = bd.attach_research_library_progress(feed, {
            "total": 3,
            "counts": {"formal_note": 1, "narrative": 0, "topic": 2},
            "articles": library_articles,
        })
        self.assertEqual(progress["libraryTotal"], 3)
        self.assertEqual(progress["latestDate"], "2026-07-30")
        self.assertEqual(progress["latestCount"], 2)
        self.assertEqual(
            {item["researchId"] for item in progress["items"]
             if item["date"] == progress["latestDate"]},
            {"topic-TOPIC-A", "topic-TOPIC-B"},
        )

    def test_progress_rejects_home_and_research_center_drift(self):
        feed = {
            "anchor": "2026-07-30", "start": "2026-07-17", "days": 14,
            "total": 0, "counts": [], "items": [],
        }
        with self.assertRaisesRegex(ValueError, "漏列"):
            bd.attach_research_library_progress(feed, {
                "total": 1,
                "counts": {"formal_note": 0, "narrative": 0, "topic": 1},
                "articles": [{"id": "topic-MISSING", "date": "2026-07-30"}],
            })

    def test_home_is_a_small_gateway_to_the_independent_research_center(self):
        template = (SCRIPTS / "dashboard_template.html").read_text(encoding="utf-8")
        builder = (SCRIPTS / "build_dashboard.py").read_text(encoding="utf-8")
        start = template.index("function buildRecentArticles()")
        end = template.index("/* ---------- 主題切換", start)
        recent = template[start:end]
        self.assertIn('<a href="research.html" data-research-link>研究中心</a>', template)
        self.assertIn('<section id="recent" class="blk"></section>', template)
        self.assertIn("RECENT=__RECENT_ARTICLES_JSON__", template)
        self.assertIn('html.replace("__RECENT_ARTICLES_JSON__"', builder)
        # 完整 feed 仍留在 payload；首頁 UI 只挑三篇跨類型入口，避免最新批次壓過每日掃描。
        self.assertIn("['formal_note','narrative','topic'].forEach", template)
        self.assertIn("chosen.length<3", template)
        self.assertIn(".slice(0,3)", template)
        self.assertIn("研究庫共 ", template)
        self.assertIn("attach_research_library_progress(recent_articles, research_library)", builder)
        self.assertIn("進入研究中心 →", template)
        self.assertNotIn("const RECENT_DEFAULT_LIMIT=12", template)
        self.assertNotIn("展開全部 ", recent)
        self.assertIn("class:'recent-item'", template)
        self.assertIn(".recent-item:focus-visible", template)
        self.assertIn("class:'research-grid'", template)
        self.assertIn("首頁各類型最多先取一篇", template)
        self.assertIn("新近不代表證據較強", template)
        self.assertIn("查核狀態與觀察層警語逐篇保留", template)

    def test_committed_home_progress_matches_committed_research_center(self):
        home = (ROOT / "index.html").read_text(encoding="utf-8")
        center = (ROOT / "research.html").read_text(encoding="utf-8")
        # RECENT 後面目前先注入市場提示 MKT，再宣告 DATE_ISO；以相鄰 payload
        # 邊界擷取，避免儀表板變數排序調整讓首頁／研究中心同步檢查失效。
        recent_match = re.search(r"\bRECENT=(\{.*?\}), MKT=", home, re.S)
        library_match = re.search(r"const LIB=(\{.*?\}), MARKET_DATE=", center, re.S)
        self.assertIsNotNone(recent_match, "index.html 缺 RECENT payload")
        self.assertIsNotNone(library_match, "research.html 缺 LIB payload")
        recent = json.loads(recent_match.group(1))
        library = json.loads(library_match.group(1))
        self.assertEqual(recent["libraryTotal"], library["total"])
        self.assertEqual(
            {row["type"]: row["count"] for row in recent["libraryCounts"]},
            library["counts"],
        )
        latest_date = max(article["date"] for article in library["articles"])
        expected = {article["id"] for article in library["articles"]
                    if article["date"] == latest_date}
        actual = {item["researchId"] for item in recent["items"]
                  if item["date"] == recent["latestDate"]}
        self.assertEqual(recent["latestDate"], latest_date)
        self.assertEqual(recent["latestCount"], len(expected))
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
