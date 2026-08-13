# -*- coding: utf-8 -*-
"""多視角排名的數學、治理與輸出契約。"""
import csv
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import ranking_views as rv
import score


def make_rows(n=6):
    rows = []
    for i in range(n):
        rows.append({
            "stock_id": f"S{i}", "grp": "g", "composite_s": float(i),
            "close_adj": 10 + i, "ma5": 10.0, "ret20": i / 100,
            "ma20": 10 + i, "ma60": 10.0, "down_rs20": i / 100,
            "margin_util_pct": float(n - i), "turnover_pct": 1 + i,
            "vol_ratio60": 1 + i / 10, "s_price": i % 5 - 2,
            "s_resil": i % 5 - 2, "s_vol": 0, "s_foreign": i % 5 - 2,
            "s_trust": (i + 1) % 5 - 2, "s_dip": (i + 2) % 5 - 2,
            "s_margin": 0, "tdcc_big400_chg": i / 100,
            "tdcc_people_chg": -i, "sbl_chg10": -i / 100,
        })
    return rows


class RankingMathTest(unittest.TestCase):
    def test_average_rank_ties_are_equal_and_order_invariant(self):
        values = {"A": 1.0, "B": 1.0, "C": 2.0, "D": 3.0}
        asc = rv.rank_percentiles(values)
        desc = rv.rank_percentiles(dict(reversed(list(values.items()))))
        self.assertEqual(asc, desc)
        self.assertEqual(asc["A"], asc["B"])
        self.assertAlmostEqual(asc["C"], 100 / 3 * 2, places=1)

    def test_all_four_lenses_are_order_invariant(self):
        rows = make_rows()
        fundamentals = {
            f"S{i}": {
                "revenue_3m_yoy": i / 10,
                "revenue_accel": i / 100,
                "operating_margin": 0.1 + i / 100,
                "operating_margin_yoy_delta": i / 1000,
            } for i in range(6)
        }
        first = rv.compute_group_views(rows, fundamentals=fundamentals)
        second = rv.compute_group_views(list(reversed(rows)), fundamentals=fundamentals)
        keys = ("champion_pct", "lens_a", "lens_b", "lens_c", "lens_d",
                "peer_sensitivity", "shadow_vol0", "shadow_price10")
        by_id = {row["stock_id"]: row for row in second}
        for row in first:
            self.assertIsNotNone(row["lens_d"])
            self.assertEqual(
                row["consensus_count"],
                sum(row[key] >= rv.TOP_PCT for key in (
                    "lens_a", "lens_b", "lens_c", "lens_d")))
            self.assertEqual({key: row[key] for key in keys},
                             {key: by_id[row["stock_id"]][key] for key in keys})

    def test_top_two_boundary_tie_is_reported_without_arbitrary_winner(self):
        rows = make_rows()
        values = {"S0": 10.0, "S1": 9.0, "S2": 9.0,
                  "S3": 3.0, "S4": 2.0, "S5": 1.0}
        for row in rows:
            row["composite_s"] = values[row["stock_id"]]
        result = {row["stock_id"]: row for row in rv.compute_group_views(rows)}
        self.assertTrue(result["S1"]["top_boundary_tied"])
        self.assertTrue(result["S2"]["top_boundary_tied"])
        self.assertEqual(result["S1"]["champion_pct"], result["S2"]["champion_pct"])
        self.assertFalse(result["S0"]["top_boundary_tied"])

    def test_pareto_frontier_keeps_tradeoffs_and_rejects_dominated_row(self):
        rows = [
            {"stock_id": "A", "lens_a": 90, "lens_b": 40},
            {"stock_id": "B", "lens_a": 40, "lens_b": 90},
            {"stock_id": "C", "lens_a": 30, "lens_b": 30},
        ]
        result = rv._pareto(rows, ("lens_a", "lens_b"))
        self.assertEqual(result, {"A": True, "B": True, "C": False})

    def test_risk_flag_caps_b_lens_but_not_other_lenses(self):
        rows = make_rows()
        plain = {row["stock_id"]: row for row in rv.compute_group_views(rows)}
        flagged = {row["stock_id"]: row for row in rv.compute_group_views(
            rows, risk_ids={"S5"})}
        self.assertGreater(plain["S5"]["lens_b"], rv.RISK_FLAG_CAP)
        self.assertEqual(flagged["S5"]["lens_b"], rv.RISK_FLAG_CAP)
        for key in ("lens_a", "lens_c"):
            self.assertEqual(flagged["S5"][key], plain["S5"][key])

    def test_role_rank_requires_four_peers(self):
        rows = make_rows()
        roles = {
            f"S{i}": {"group": "g", "role": "r1" if i < 4 else "r2",
                       "role_label": "角色一" if i < 4 else "角色二", "basis": "test"}
            for i in range(6)
        }
        result = {row["stock_id"]: row for row in rv.compute_group_views(rows, roles=roles)}
        self.assertTrue(all(result[f"S{i}"]["role_pct"] is not None for i in range(4)))
        self.assertTrue(all(result[f"S{i}"]["role_pct"] is None for i in range(4, 6)))

    def test_peer_sensitivity_is_exact_not_sampling_claim(self):
        values = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        result = rv.peer_sensitivity(values)
        self.assertEqual(set(result), set(values))
        self.assertTrue(all(value is not None and 0 <= value <= 100
                            for value in result.values()))

    def test_champion_and_score_weights_remain_unchanged(self):
        self.assertEqual(score.WEIGHTS, {
            "price": 1.4, "resil": 1.0, "vol": 0.3, "foreign": 0.5,
            "trust": 0.8, "dip": 0.0, "margin": 0.4,
        })
        self.assertEqual(rv.CHALLENGERS["vol_zero"]["weights"]["vol"], 0.0)
        self.assertEqual(rv.CHALLENGERS["price_1_0"]["weights"]["price"], 1.0)
        self.assertIn("unchanged", rv.RANKING_CONTRACT["champion"]["status"])

    def test_spec_sha_covers_contract_and_evaluators(self):
        self.assertRegex(rv.SPEC_SHA, r"^[0-9a-f]{64}$")
        self.assertEqual(rv.SPEC_SHA, rv.spec_digest())
        self.assertEqual(rv.CHALLENGERS["vol_zero"]["oos_start"], "2026-08-13")


class FundamentalPointInTimeTest(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        self.con.row_factory = sqlite3.Row
        self.con.executescript("""
          CREATE TABLE month_revenue(date TEXT,stock_id TEXT,revenue INTEGER,
            revenue_month INTEGER,revenue_year INTEGER,PRIMARY KEY(date,stock_id));
          CREATE TABLE financials(date TEXT,stock_id TEXT,type TEXT,value REAL,
            origin_name TEXT,PRIMARY KEY(date,stock_id,type));
          CREATE TABLE fundamental_availability(dataset TEXT,data_date TEXT,stock_id TEXT,
            source_published_at TEXT,first_seen_at TEXT,source TEXT,
            PRIMARY KEY(dataset,data_date,stock_id));
        """)
        for sid, multiplier in (("A", 1), ("B", 2)):
            for year in (2025, 2026):
                for month in range(1, 8):
                    storage = f"{year}-{month + 1:02d}-01"
                    revenue = multiplier * (100 + (year - 2025) * 20 + month)
                    self.con.execute("INSERT INTO month_revenue VALUES(?,?,?,?,?)",
                                     (storage, sid, revenue, month, year))
                    self.con.execute("INSERT INTO fundamental_availability VALUES(?,?,?,?,?,?)",
                                     ("TaiwanStockMonthRevenue", storage, sid, None,
                                      "2026-08-13T01:00:00+00:00", "test"))
            for date, revenue, operating in (("2025-03-31", 100, 10),
                                              ("2026-03-31", 120, 18)):
                for kind, value in (("Revenue", revenue * multiplier),
                                    ("OperatingIncome", operating * multiplier)):
                    self.con.execute("INSERT INTO financials VALUES(?,?,?,?,?)",
                                     (date, sid, kind, value, None))
                self.con.execute("INSERT INTO fundamental_availability VALUES(?,?,?,?,?,?)",
                                 ("TaiwanStockFinancialStatements", date, sid, None,
                                  "2026-08-13T01:00:00+00:00", "test"))

    def tearDown(self):
        self.con.close()

    def test_as_of_before_first_seen_has_no_fundamental_rank(self):
        values, meta = rv.load_fundamental_inputs(
            self.con, as_of="2026-08-12T23:59:59+00:00")
        self.assertEqual(values, {})
        self.assertFalse(meta["available"])

    def test_as_of_after_first_seen_computes_growth_and_margin(self):
        values, meta = rv.load_fundamental_inputs(
            self.con, as_of="2026-08-13T01:00:00+00:00")
        self.assertTrue(meta["available"])
        self.assertEqual(meta["month_period"], "2026-07")
        self.assertAlmostEqual(values["A"]["operating_margin"], 0.15)
        self.assertAlmostEqual(values["A"]["operating_margin_yoy_delta"], 0.05)
        self.assertIsNotNone(values["A"]["revenue_3m_yoy"])


class RolesConfigTest(unittest.TestCase):
    def test_role_config_exactly_covers_universe(self):
        with (ROOT / "config" / "universe.csv").open(encoding="utf-8", newline="") as handle:
            universe = [{"stock_id": row["stock_id"], "grp": row["group"]}
                        for row in csv.DictReader(handle)]
        roles = rv.load_roles(rv.ROLES_CONFIG, universe, strict=True)
        self.assertEqual(len(roles), len(universe))
        self.assertTrue(all(role["basis"] == "universe.biz manual_v1"
                            for role in roles.values()))


class DashboardContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template = (SCRIPTS / "dashboard_template.html").read_text(encoding="utf-8")
        cls.builder = (SCRIPTS / "build_dashboard.py").read_text(encoding="utf-8")

    def test_template_has_multi_view_section_and_disclosures(self):
        for fragment in ('id="perspectives"', 'href="#perspectives"',
                         "同一族群，換個問題會得到不同答案", "正式 Champion 的權重與分層",
                         "至少兩個視角同進前 20% 才稱共識",
                         "不是第五個預測分數"):
            self.assertIn(fragment, self.template)
        for undefined_token in ("var(--purple)", "var(--purplebg)",
                                "var(--surface)", "var(--neutral-tint)"):
            self.assertNotIn(undefined_token, self.template)

    def test_multi_view_ui_is_single_group_master_detail(self):
        for fragment in (
                "class:'rv-context'", "class:'rv-lens-tabs'",
                "class:'card rv-list-card'", "class:'card rv-detail-card'",
                "以下數值均為族群內相對名次，非機率、預測或投資建議",
                "同分以「=」共享名次", "為什麼這個名次可能變動？",
                "查看完整個股", "localStorage.getItem(key)",
                "row.id===selectedId?'true':'false'",
        ):
            self.assertIn(fragment, self.template)
        ranking_source = self.template[
            self.template.index("function buildRankingViews()"):
            self.template.index("/* 時間尺度視角", self.template.index("function buildRankingViews()"))
        ]
        self.assertNotIn("全部族群", ranking_source)
        self.assertNotIn("onlyConsensus", ranking_source)
        self.assertIn("R.rows.filter(x=>x.g===groupKey)", ranking_source)
        self.assertIn("event.key!=='ArrowDown'", ranking_source)
        self.assertIn("role:'tabpanel'", ranking_source)
        self.assertIn("tabs.scrollLeft=Math.max", ranking_source)

    def test_payload_placeholder_is_built_and_consumed(self):
        self.assertIn("__RANKING_VIEWS_JSON__", self.template)
        self.assertIn('html.replace("__RANKING_VIEWS_JSON__"', self.builder)
        self.assertIn("build_ranking_views(con", self.builder)
        self.assertIn('obj["views"]', self.builder)
        self.assertIn("同一檔的多視角位置", self.template)
        self.assertIn("不是五票多數決，也不預測未來報酬", self.template)

    def test_built_dashboard_contains_complete_payload(self):
        index = ROOT / "index.html"
        if not index.exists():
            self.skipTest("index.html 尚未產生")
        text = index.read_text(encoding="utf-8")
        self.assertNotIn("__RANKING_VIEWS_JSON__", text)
        payload = json.JSONDecoder().raw_decode(
            text, text.index("RANKV=") + len("RANKV="))[0]
        self.assertEqual(payload["coverage"]["stocks"], 121)
        self.assertEqual(len(payload["rows"]), 121)
        self.assertEqual(len({row["g"] for row in payload["rows"]}), 11)
        self.assertEqual(payload["specSha"], rv.SPEC_SHA)
        data = json.JSONDecoder().raw_decode(
            text, text.index("DATA=") + len("DATA="))[0]
        self.assertEqual(len(data), 121)
        self.assertTrue(all("views" in row for row in data))

    def test_validate_uses_same_day_paired_challenger_gate(self):
        source = (SCRIPTS / "validate.py").read_text(encoding="utf-8")
        for fragment in (
                "Challenger 相對 Champion 的同日配對差",
                "challenger_daily[d] - champion_daily[d]",
                'summary["eff_obs"] < 10',
                "仍需另驗 tier／成本後才可改 production",
                'row["spec_sha"] == rv.SPEC_SHA'):
            self.assertIn(fragment, source)


if __name__ == "__main__":
    unittest.main()
