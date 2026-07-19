import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_dashboard as bd


class ObservationDashboardTest(unittest.TestCase):
    def observation_row(self):
        return {
            "raw_trades": 1_000,
            "avg_shares_per_trade": 1_000.0,
            "avg_value_per_trade": 100_000.0,
            "foreign_imbalance_pct": 20.0,
            "trust_imbalance_pct": -50.0,
            "raw_foreign_buy": 600_000,
            "raw_foreign_sell": 400_000,
            "raw_trust_buy": 100_000,
            "raw_trust_sell": 300_000,
            "inst_gross": 1_600_000,
            "inst_participation_pct": 80.0,
            "dealer_self_imbalance_pct": 60.0,
            "dealer_hedge_imbalance_pct": -80.0,
            "raw_dealer_self_net": 60_000,
            "raw_dealer_hedge_net": -80_000,
            "margin_net_flow": 10,
            "margin_balance_change": 10,
            "margin_flow_residual": 0,
            "raw_margin_buy": 20,
            "raw_margin_sell": 5,
            "raw_margin_cash_repay": 5,
            "raw_offset_volume": 2,
            "short_net_flow": 4,
            "short_balance_change": 4,
            "short_flow_residual": 0,
            "raw_short_sell": 8,
            "raw_short_buyback": 3,
            "raw_short_stock_repay": 1,
            "margin_limit_util_pct": 60.0,
            "short_limit_util_pct": 36.0,
            "foreign_limit_used_pct": 44.0,
            "raw_foreign_available_shares": 28_000_000,
            "raw_foreign_available_pct": 28.0,
            "raw_foreign_limit_pct": 50.0,
            "sbl_net_flow": 50_000,
            "sbl_balance_change": 50_000,
            "sbl_flow_residual": 0,
            "raw_sbl_sell": 100_000,
            "raw_sbl_return": 40_000,
            "raw_sbl_adjustment": -10_000,
            "sbl_sell_limit_pct": 50.0,
            "raw_sbl_next_limit": 200_000,
            "benchmark_name": "發行量加權股價報酬指數",
            "excess_ret1": 0.01,
            "excess_ret5": 0.03,
            "excess_ret20": None,
        }

    def test_stock_payload_answers_with_numbers_and_teaches_the_formula(self):
        payload = bd.build_observation_view(self.observation_row())
        text = "\n".join("｜".join(str(value) for value in row) for row in payload["rows"])
        for phrase in (
            "外資 +20.0%", "買600.0張", "占雙邊成交 80.0%",
            "資買 20張 − 資賣 5張 − 現償 5張 = +10張",
            "券賣 8張 − 券買 3張 − 券償 1張 = +4張",
            "法令上限已用 44.0%", "新增賣出 10.0萬股",
            "1日 +1.0pp", "5日 +3.0pp", "20日 -",
        ):
            self.assertIn(phrase, text)
        self.assertIn("不改分數", payload["why"])
        self.assertIn("上櫃報酬指數目前歷史較短", text)
        self.assertEqual(payload["scLabel"], "觀察層 · 不計分")

    def test_group_payload_converts_breadth_ratio_to_reader_percentage(self):
        payload = bd.build_group_observation_view({
            "n": 9,
            "foreign_buy_breadth": 2 / 3,
            "trust_buy_breadth": 1 / 3,
            "med_foreign_imbalance_pct": 12.0,
            "med_trust_imbalance_pct": -8.0,
            "med_inst_participation_pct": 25.0,
            "med_dealer_self_net_volume_pct": 0.1,
            "med_dealer_hedge_net_volume_pct": -0.2,
            "med_margin_net_flow_shares_pct": 0.01,
            "med_short_net_flow_shares_pct": -0.01,
            "med_margin_limit_util_pct": 40.0,
            "med_short_limit_util_pct": 10.0,
            "med_foreign_limit_used_pct": 55.0,
            "med_sbl_sell_shares_pct": 0.02,
            "med_sbl_return_shares_pct": 0.01,
            "med_sbl_adjustment_shares_pct": 0.0,
            "med_sbl_net_flow_shares_pct": 0.01,
            "med_excess_ret1": 0.01,
            "med_excess_ret5": 0.02,
            "med_excess_ret20": None,
            "n_excess1": 9, "n_excess5": 9, "n_excess20": 5,
            "excess_breadth1": 2 / 3, "excess_breadth5": 5 / 9,
            "excess_breadth20": None,
        }, "測試族群", "測試")
        text = "\n".join("｜".join(str(value) for value in row) for row in payload["rows"])
        self.assertIn("外資 67%", text)
        self.assertIn("投信 33%", text)
        self.assertIn("1日 9/9", text)
        self.assertIn("20日 5/9", text)
        self.assertIn("有效樣本少於6檔就留白", payload["how"])

    def test_template_exposes_observation_anatomy_and_guide(self):
        # 2026-07-19 redesign 版:數據解剖以可折疊段呈現在個股詳情卡與族群抽屜,
        # 指南區 #flow-guide 移到主頁尾段;payload 契約(rows/why/how/src)不變。
        template = (SCRIPTS / "dashboard_template.html").read_text(encoding="utf-8")
        builder = (SCRIPTS / "build_dashboard.py").read_text(encoding="utf-8")
        for marker in (
            'id="flow-guide"', "交易／部位觀察指南", "法人方向強度",
            "法人總活動占比", "官方指數超額報酬",
            "function flowSection(f)", "flowSection(d.flow)", "flowSection(g.flow)",
            "數據解剖 · 交易與部位怎麼形成",
        ):
            self.assertIn(marker, template)
        self.assertIn("build_observation_view(observation)", builder)
        self.assertIn("build_group_observation_view", builder)
        self.assertIn('obj["flow"]', builder)


if __name__ == "__main__":
    unittest.main()
