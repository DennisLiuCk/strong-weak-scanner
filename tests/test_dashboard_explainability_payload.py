import sqlite3
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_dashboard as bd


def score_row(**overrides):
    row = {
        "s_price": 2, "s_resil": 2, "s_vol": 0, "s_foreign": -1,
        "s_trust": 0, "s_dip": 1, "s_margin": 1,
        "composite": 4.7, "composite_s": 5.8,
        "tier_raw": "真強", "tier": "強但過熱", "pending": None, "warn": 1,
    }
    row.update(overrides)
    return row


def metric_row(**overrides):
    row = {
        "rs20": 0.05, "ret20": 0.10, "dist_hi60": -0.02,
        "down_rs20": 0.01, "ret1": 0.01, "turnover_pct": 2.0,
        "vol_ratio60": 1.0, "fpct_chg20": -0.80, "dipbuy20": -0.05,
        "foreign_pct": 20.0, "trust5": -100, "trust5_pct": -0.10,
        "margin_util_pct": 3.0, "margin_chg10": -0.02,
        "short_margin_ratio": 0.0,
    }
    row.update(overrides)
    return row


def technical_history():
    rows = []
    for i in range(6):
        rows.append({
            "date": f"2026-07-{4+i:02d}", "close_adj": 100+i,
            "ma5": 99+i, "ma20": 96+i*.5, "ma60": 90+i*.2,
            "rsi14": 50+i*2, "volume": 900_000+i*20_000,
            "vol_ma20": 1_000_000, "vol_ratio20": (900_000+i*20_000)/1_000_000,
            "ret1": 0.01,
        })
    return rows


class DashboardExplainabilityPayloadTest(unittest.TestCase):
    def test_technical_view_combines_self_relative_trend_momentum_and_volume(self):
        history = technical_history()
        current = dict(history[-1], ma5=106, ma20=102, ma60=94, rsi14=72,
                       volume=1_300_000, vol_ratio20=1.3)
        view = bd.build_technical_view(current, history[:-1] + [current])
        self.assertEqual((view["cls"], view["label"]), ("up", "多頭排列"))
        self.assertEqual(view["rows"][1][1], "MA5 > MA20 > MA60")
        self.assertIn("上漲力道明顯較強", view["rows"][2][1])
        self.assertIn("價漲量增", view["rows"][4][1])
        self.assertIn("不等於即將反轉", view["why"])
        self.assertEqual(
            [(x["label"], x["cls"]) for x in view["series"]],
            [("現價", "price"), ("MA5", "ma5"), ("MA20", "ma20"), ("MA60", "ma60")],
        )
        self.assertEqual(view["series"][1]["value"], "106")

    def test_rsi_copy_explains_the_50_line_in_plain_language(self):
        history = technical_history()
        current = dict(history[-1], rsi14=55)
        view = bd.build_technical_view(current, history[:-1] + [current])
        self.assertIn("上漲力道較強", view["rows"][2][1])
        self.assertIn("平均上漲力道大於平均下跌力道", view["rows"][2][2])
        self.assertIn("50是兩者的分界", view["rows"][2][2])
        self.assertNotIn("動能相對占優", view["why"])

    def test_technical_view_exposes_price_distance_and_transition(self):
        history = technical_history()
        previous = dict(history[-2], close_adj=99, ma5=99, ma20=100, ma60=95)
        current = dict(history[-1], close_adj=103, ma5=101, ma20=100, ma60=96,
                       rsi14=55, volume=700_000, vol_ma20=1_000_000, vol_ratio20=.7)
        view = bd.build_technical_view(current, history[:-2] + [previous, current])
        self.assertEqual(view["rows"][0][0], "價格與均線")
        self.assertIn("現價 103／MA5 101／MA20 100／MA60 96", view["rows"][0][1])
        self.assertIn("比MA5高2.0%", view["rows"][0][2])
        self.assertIn("現價上穿MA20", view["rows"][5][1])
        self.assertEqual(view["rows"][4][1], "價漲量縮")

    def test_mixed_ma_structure_lists_actual_order_and_all_price_positions(self):
        history = technical_history()
        current = dict(history[-1], close_adj=448.5, ma5=473.78, ma20=502.01,
                       ma60=477.93, rsi14=45, volume=1_160_000,
                       vol_ma20=1_000_000, vol_ratio20=1.16, ret1=-0.01)
        view = bd.build_technical_view(current, history[:-1] + [current])
        self.assertEqual((view["cls"], view["label"]), ("down", "趨勢偏弱"))
        self.assertEqual(view["rows"][1][1], "由高到低：MA20 > MA60 > MA5")
        self.assertIn("尚未形成標準空頭排列（MA5 < MA20 < MA60）", view["rows"][1][2])
        self.assertIn("現價低於MA5、MA20、MA60", view["rows"][1][2])
        self.assertNotIn("RSI", view["rows"][1][2])
        self.assertIn("平均下跌力道大於平均上漲力道", view["why"])
        self.assertIn("現價 448.5／MA5 473.78／MA20 502.01／MA60 477.93",
                      view["rows"][0][1])
        self.assertIn("比MA5低5.3%、比MA20低10.7%、比MA60低6.2%", view["rows"][0][2])
        self.assertIn("與MA20的差距超過10%", view["rows"][0][2])
        self.assertNotIn("短線偏離", view["rows"][0][2])

    def test_no_crossing_copy_names_two_separate_comparisons(self):
        history = technical_history()
        view = bd.build_technical_view(history[-1], history)
        self.assertEqual(view["rows"][5][0], "短線轉折（較前一交易日）")
        self.assertEqual(view["rows"][5][1], "無穿越事件")
        self.assertIn("現價沒有跨越MA20", view["rows"][5][2])
        self.assertIn("MA5也沒有跨越MA20", view["rows"][5][2])
        self.assertNotIn("現價/MA20", view["rows"][5][2])
    def test_rank_wording_never_claims_an_absolute_trade_direction(self):
        texts = (list(bd.R_PRICE.values()) + list(bd.R_RESIL.values())
                 + list(bd.R_FOREIGN.values()) + list(bd.R_TRUST.values())
                 + list(bd.R_DIP.values()) + list(bd.SALIENT.values())
                 + list(bd.TIER_DESC.values()))
        for text in texts:
            for forbidden in ("吃貨", "倒貨", "認養", "淨買", "淨賣", "外資出", "散戶接"):
                self.assertNotIn(forbidden, text)

    def test_cells_separate_raw_direction_from_relative_score(self):
        sc = score_row(s_foreign=2, s_trust=2)
        cells = bd.build_cells(sc, metric_row())

        self.assertTrue(all(len(cell) == 7 for cell in cells))
        foreign, trust = cells[2], cells[3]
        self.assertEqual(foreign[3], "外資變化位於族群前20%")
        # 動詞已帶方向 → 數值用絕對值(「減持 -0.80pp」是雙重否定);rows 內量值仍帶號
        self.assertIn("外資仍減持 0.80pp", foreign[5])
        self.assertIn("族群前20%", foreign[6])
        self.assertIn("投信仍淨賣 100張", trust[5])
        self.assertIn("族群前20%", trust[6])
        self.assertNotIn("吃貨", foreign[3])
        self.assertNotIn("認養", trust[3])

    def test_positive_raw_value_can_still_be_relative_laggard(self):
        cells = bd.build_cells(
            score_row(s_foreign=-1), metric_row(fpct_chg20=0.68))
        foreign = cells[2]
        self.assertIn("外資仍增持 0.68pp", foreign[5])
        self.assertIn("族群後20–40%", foreign[6])
        self.assertNotIn("調節", foreign[3])
        self.assertNotIn("減持", foreign[3])

    def test_warn_slot_keeps_current_direction_and_dynamic_reading_aligned(self):
        cells = bd.build_cells(score_row(), metric_row(vol_ratio60=6.0))
        volume = cells[1]
        self.assertEqual(volume[4], 1)
        self.assertIn("量比 6.0×", volume[5])
        # 固定門檻定義已集中在欄位表頭；格內 basis 只保留這檔當下的動態判讀。
        self.assertEqual("量比爆增、過熱", volume[6])

    def test_margin_display_uses_the_same_five_day_fallback_as_scoring(self):
        cells = bd.build_cells(
            score_row(s_margin=2), metric_row(margin_chg10=None, margin_chg5=-0.10))
        margin = cells[4]
        self.assertEqual(margin[2][1][0], "5日融資變化")
        self.assertIn("融資5日仍下降 10.0%（5日備援）", margin[5])

    def test_tier_keys_labels_confirmation_and_math_are_all_exposed(self):
        sc = score_row()
        tier = bd.tier_ui_payload(sc)
        self.assertEqual(tier["tier_raw"], "真強")
        self.assertEqual(tier["tier_confirmed"], "強但過熱")
        self.assertTrue(tier["tier_waiting"])
        self.assertEqual(tier["tier_label"], "相對強勢·過熱")
        self.assertEqual(tier["tier_raw_label"], "相對強勢")

        history = [
            {"date": "2026-07-07", "composite": 6.5},
            {"date": "2026-07-08", "composite": 6.2},
            {"date": "2026-07-09", "composite": 4.7},
        ]
        *_, vrows = bd.verdict(sc, history)
        self.assertEqual(vrows[0][0:2], ["今日分(未平滑)", "+4.7"])
        self.assertEqual(vrows[1][4], "× 1.4 = +2.8")
        self.assertEqual(vrows[-2][0], "近3個交易日")
        self.assertIn("7/7 +6.5 → 7/8 +6.2 → 7/9 +4.7", vrows[-2][1])
        self.assertEqual(vrows[-1][0:2], ["3日平均(評級用)", "+5.8"])
        self.assertIn("÷ 3 = +5.8", vrows[-1][2])

    def test_overview_does_not_call_least_selling_a_buy_signal(self):
        groups = [
            {"grp": "passive", "state": "中性觀察", "med_dip": -0.41, "rel20": -0.01},
            {"grp": "power", "state": "中性觀察", "med_dip": -0.80, "rel20": -0.02},
        ]
        overview = bd.build_overview(groups)
        self.assertIn("沒有族群符合", overview["headline"])
        self.assertIn("2/2 族群", overview["summary"])
        self.assertIn("調節相對最少", overview["summary"])
        self.assertIn("仍淨賣 0.41%股本", overview["summary"])
        self.assertNotIn("買超最高", overview["summary"])

    def test_group_delta_is_separate_and_signed(self):
        series = ([{"med_dip": -0.56, "rel20": -0.02}]
                  + [{"med_dip": -0.50, "rel20": -0.01}] * 4
                  + [{"med_dip": -0.41, "rel20": 0.01}])
        self.assertEqual(
            bd._five_day_delta(series, "med_dip", 0.01, 1, 2),
            "較5日前改善 +0.15pp",
        )
        self.assertEqual(bd._current_dip(-0.41), "淨賣 0.41%股本")  # 動詞帶方向 → 絕對值
        self.assertEqual(bd._five_day_value(series, "rel20"), -0.02)
        self.assertIsNone(bd._five_day_value(series[:5], "rel20"))

    def test_fundamental_badge_is_descriptive_not_a_demand_verdict(self):
        con = sqlite3.connect(":memory:")
        con.row_factory = sqlite3.Row
        con.executescript("""
            CREATE TABLE month_revenue(
                stock_id TEXT, date TEXT, revenue REAL, revenue_year INT, revenue_month INT);
            CREATE TABLE financials(stock_id TEXT, date TEXT, type TEXT, value REAL);
            INSERT INTO month_revenue VALUES
                ('1001','2026-05-31',80,2026,5),
                ('1001','2026-04-30',90,2026,4),
                ('1001','2025-05-31',120,2025,5);
        """)
        fund = bd.build_fund_map(con)["1001"]
        con.close()

        self.assertEqual(fund["label"], "營收YoY -33%")
        for phrase in ("營收不等於獲利", "需求", "基期", "收入認列時點", "工作天數"):
            self.assertIn(phrase, fund["why"])
        self.assertNotIn("營運動能轉弱", fund["why"])

    def test_overview_placeholder_is_injected(self):
        source = (ROOT / "scripts" / "build_dashboard.py").read_text(encoding="utf-8")
        self.assertIn('html.replace("__OVERVIEW_JSON__"', source)


if __name__ == "__main__":
    unittest.main()
