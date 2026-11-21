import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))
import market_calendar as mc  # noqa: E402

DATA = {
    "announced": {"2026": {"title": "115 年市場開休市日期", "source": "schedule-url",
                           "closed": [{"date": "2026-12-25", "name": "行憲紀念日"}]}},
    "closures": [{"date": "2026-10-23", "reason": "臨時休市公告", "source": "news-url"}],
    "realized": {"2026-10": {"covered_through": "2026-10-31", "sources": ["twse", "tpex"],
                             "trading_days": ["2026-10-22", "2026-10-27"]}},
}


class Status(unittest.TestCase):
    def setUp(self):
        self.cal = mc.MarketCalendar(DATA)

    def state(self, day):
        st = self.cal.status(day)
        return st["state"], st["basis"]

    def test_states(self):
        self.assertEqual(self.state("2026-10-22"), ("trading", "realized"))
        self.assertEqual(self.state("2026-10-24"), ("closed", "weekend"))
        self.assertEqual(self.state("2026-10-26"), ("closed", "realized"))      # 已核對月份無成交
        self.assertEqual(self.state("2026-12-25"), ("closed", "scheduled"))
        self.assertEqual(self.state("2026-12-28"), ("trading", "scheduled"))
        self.assertEqual(self.state("2027-01-04")[0], "unknown")

    def test_announced_closure_reason_and_source_win(self):
        st = self.cal.status("2026-10-23")
        self.assertEqual((st["state"], st["reason"], st["source"]), ("closed", "臨時休市公告", "news-url"))

    def test_repo_calendar_has_official_1023_closure(self):
        st = mc.load().status("2026-10-23")
        self.assertEqual(st["state"], "closed")
        self.assertIn("115年10月23日休市一天", st["reason"])
        self.assertIn("twse.com.tw", st["source"])


if __name__ == "__main__":
    unittest.main()
