import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))
import market_calendar as mc  # noqa: E402

DATA = {
    "announced": {"2026": {"title": "115 年市場開休市日期", "source": "schedule-url",
                           "closed": [{"date": "2026-12-25", "name": "行憲紀念日"}]}},
    "closures": [{"date": "2026-10-23", "reason": "臨時休市公告", "source": "news-url",
                  "announced_at": "2026-10-22T20:10:00+08:00"}],
    "realized": {"2026-10": [{"fetched_at": "2026-11-01T10:00:00+08:00", "sources": ["twse", "tpex"],
                              "trading_days": ["2026-10-21", "2026-10-22", "2026-10-27"]}]},
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
        self.assertEqual(self.state("2026-10-26"), ("closed", "realized"))      # 落在兩所成交日中間
        self.assertEqual(self.state("2026-10-28"), ("trading", "scheduled"))    # 成交資料只到 10/27
        self.assertEqual(self.state("2026-12-25"), ("closed", "scheduled"))
        self.assertEqual(self.state("2026-12-28"), ("trading", "scheduled"))
        self.assertEqual(self.state("2027-01-04")[0], "unknown")

    def test_announced_closure_reason_and_source_win(self):
        st = self.cal.status("2026-10-23")
        self.assertEqual((st["state"], st["basis"], st["source"]), ("closed", "announced", "news-url"))
        self.assertIn("公告 2026-10-22T20:10:00+08:00", st["reason"])

    def test_as_of_hides_later_announcements_and_fetches(self):
        tpe = mc.TAIPEI_TZ
        before = mc.dt.datetime(2026, 10, 22, 20, 9, tzinfo=tpe)
        after = mc.dt.datetime(2026, 10, 22, 20, 11, tzinfo=tpe)
        self.assertEqual(self.cal.status("2026-10-23", before)["basis"], "scheduled")
        self.assertEqual(self.cal.status("2026-10-23", before)["state"], "trading")
        self.assertEqual(self.cal.status("2026-10-23", after)["state"], "closed")
        self.assertEqual(self.cal.status("2026-10-22", before)["basis"], "scheduled")   # 11/01 才取得成交資料
        self.assertEqual(self.cal.status("2026-10-26", after)["state"], "trading")      # 成交缺口當時不可見

    def test_gap_needs_visible_common_trading_days_on_both_sides(self):
        nov = {"2026-11": [{"fetched_at": "2026-12-01T10:00:00+08:00", "sources": ["s"],
                            "trading_days": ["2026-11-03", "2026-11-04"]}]}
        only_after = mc.MarketCalendar(dict(DATA, realized=nov, closures=[]))
        st = only_after.status("2026-11-02")
        self.assertEqual((st["state"], st["basis"]), ("trading", "scheduled"))
        self.assertIn("只在此日之後(最早 2026-11-03),不能推定休市", st["reason"])
        no_schedule = mc.MarketCalendar(dict(DATA, realized=nov, closures=[], announced={}))
        self.assertEqual(no_schedule.status("2026-11-02")["state"], "unknown")
        # 10 月資料讓 11/02 前面也有共同成交日 → 夾在中間才推定休市
        both = mc.MarketCalendar(dict(DATA, realized={**DATA["realized"], **nov}, closures=[]))
        self.assertEqual(self.state_of(both, "2026-11-02"), ("closed", "realized"))

    def test_empty_month_list_does_not_imply_closures(self):
        realized = {**DATA["realized"],
                    "2026-11": [{"fetched_at": "2026-12-01T10:00:00+08:00", "sources": ["s"], "trading_days": []}],
                    "2026-12": [{"fetched_at": "2026-12-02T10:00:00+08:00", "sources": ["s"],
                                 "trading_days": ["2026-12-01"]}]}
        cal = mc.MarketCalendar(dict(DATA, realized=realized))
        st = cal.status("2026-11-13")
        self.assertEqual((st["state"], st["basis"]), ("trading", "scheduled"))
        self.assertIn("該月可見的成交清單是空的,不能推定休市", st["reason"])
        self.assertEqual(mc.MarketCalendar(dict(DATA, realized=realized, announced={})).status("2026-11-13")["state"],
                         "unknown")

    @staticmethod
    def state_of(cal, day):
        st = cal.status(day)
        return st["state"], st["basis"]

    def test_closure_without_announcement_time_is_rejected(self):
        bad = dict(DATA, closures=[{"date": "2026-10-23", "reason": "x", "source": "y"}])
        with self.assertRaisesRegex(mc.CalendarError, "缺 announced_at"):
            mc.MarketCalendar(bad)

    def test_repo_calendar_has_official_1023_closure(self):
        st = mc.load().status("2026-10-23")
        self.assertEqual(st["state"], "closed")
        self.assertIn("115年10月23日休市一天", st["reason"])
        self.assertIn("twse.com.tw", st["source"])


if __name__ == "__main__":
    unittest.main()
