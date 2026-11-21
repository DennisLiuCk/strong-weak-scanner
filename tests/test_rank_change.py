"""rank_change:選週規則、首次正式發布、三日窗口與名次拆解(小型 SQLite fixture)。"""
import contextlib
import datetime as dt
import hashlib
import io
import json
import os
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import db_ro
import rank_change as rc

TPE = rc.TAIPEI_TZ


def at(text):
    return dt.datetime.fromisoformat(text).replace(tzinfo=TPE)


def weekdays(start, end, skip=()):
    d, last, out = dt.date.fromisoformat(start), dt.date.fromisoformat(end), []
    while d <= last:
        if d.weekday() < 5 and str(d) not in skip:
            out.append(str(d))
        d += dt.timedelta(days=1)
    return out


def snap(scores, grp="g"):
    return {s: {"stock_id": s, "grp": grp, "composite_s": v, "composite": v} for s, v in scores.items()}


class Fixture:
    """Isolated temp SQLite; production code reads it only via db_ro."""

    def __init__(self, market):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.tmp.name, "fixture.db")
        con = sqlite3.connect(self.path)
        con.executescript("""
            CREATE TABLE market(date TEXT PRIMARY KEY, taiex REAL);
            CREATE TABLE oos_snapshot_runs(snapshot_id TEXT PRIMARY KEY, data_date TEXT, captured_at TEXT,
                source TEXT, is_official INTEGER, quality_json TEXT, stock_count INTEGER, group_count INTEGER,
                universe_hash TEXT);
            CREATE TABLE oos_signal_snapshots(snapshot_id TEXT, date TEXT, stock_id TEXT, grp TEXT,
                composite REAL, composite_s REAL, tier TEXT, s_price INT, s_resil INT, s_vol INT,
                s_foreign INT, s_trust INT, s_dip INT, s_margin INT);""")
        con.executemany("INSERT INTO market VALUES(?,1)", [(d,) for d in market])
        con.commit()
        con.close()

    def run(self, sid, day, rows, captured=None, official=1, stock_count=None, universe="u1", spec="s1"):
        """rows: {stock_id: (grp, composite, composite_s)};預設擷取時間=當日台北 23:52。"""
        captured = captured or f"{day}T15:52:00+00:00"
        con = sqlite3.connect(self.path)
        con.execute("INSERT INTO oos_snapshot_runs VALUES(?,?,?,?,?,?,?,1,?)",
                    (sid, day, captured, "github-actions", official, json.dumps({"score_spec_sha": spec}),
                     len(rows) if stock_count is None else stock_count, universe))
        con.executemany("INSERT INTO oos_signal_snapshots VALUES(?,?,?,?,?,?,'潛在/中性',0,0,0,0,0,0,0)",
                        [(sid, day, s, g, c, cs) for s, (g, c, cs) in rows.items()])
        con.commit()
        con.close()

    def fill(self, days, rows=None):
        for d in days:
            self.run(f"r-{d}", d, rows or {"T": ("g", 1.0, 1.0), "Q": ("g", 0.0, 0.0)})

    def con(self):
        return db_ro.connect(self.path)

    def no_trade(self, day, stock):
        """官方零成交:price 列 OHLC 空白且量/額/筆數 0,trading_status 標 no_trade。"""
        con = sqlite3.connect(self.path)
        con.executescript("""
            CREATE TABLE IF NOT EXISTS price(date TEXT, stock_id TEXT, open REAL, high REAL, low REAL,
                close REAL, volume INT, amount INT, trades INT);
            CREATE TABLE IF NOT EXISTS trading_status(date TEXT, stock_id TEXT, status TEXT, source TEXT,
                reason TEXT);""")
        con.execute("INSERT INTO price VALUES(?,?,NULL,NULL,NULL,NULL,0,0,0)", (day, stock))
        con.execute("INSERT INTO trading_status VALUES(?,?,?,?,?)",
                    (day, stock, rc.trading_status.NO_TRADE, rc.trading_status.OFFICIAL_PRICE_SOURCE, "fixture"))
        con.commit()
        con.close()

    def close(self):
        self.tmp.cleanup()


EARLY = "2026-01-01T00:00:00+08:00"


def calendar(start, end, closed=None, announced=(), closures=None, fetched_at=EARLY):
    """固定交易日曆:start~end 逐月成交日(扣掉 closed;fetched_at=取得時間);
    closed 列入該年開休市表;announced=只有開休市表的年份;closures={日: (原因, 公告時間)}。"""
    closed = closed or {}
    announced = set(announced) | {k[:4] for k in closed}
    realized, d, last = {}, dt.date.fromisoformat(start), dt.date.fromisoformat(end)
    while d <= last:
        m = str(d)[:7]
        e = realized.setdefault(m, {"fetched_at": fetched_at, "trading_days": [], "sources": ["fixture"]})
        if d.weekday() < 5 and str(d) not in closed:
            e["trading_days"].append(str(d))
        d += dt.timedelta(days=1)
    return rc.market_calendar.MarketCalendar({
        "realized": realized,
        "announced": {y: {"source": "fixture-schedule", "closed": [{"date": k, "name": v} for k, v in closed.items()
                                                                  if k[:4] == y]} for y in announced},
        "closures": [{"date": k, "reason": r, "announced_at": t, "source": "fixture-news"}
                     for k, (r, t) in (closures or {}).items()]})


class WeekSelection(unittest.TestCase):
    NOV = calendar("2026-11-01", "2026-11-30")

    def make(self, market, snapshots=None):
        fx = Fixture(market)
        self.addCleanup(fx.close)
        fx.fill(snapshots if snapshots is not None else market)
        con = fx.con()
        self.addCleanup(con.close)
        return fx, con

    def dates(self, con, as_of, mcal=NOV):
        picked, notes = rc.select_weeks(con, as_of, mcal=mcal)
        return [w["date"] for w in picked], notes

    def test_friday_published_uses_this_week(self):
        _, con = self.make(weekdays("2026-11-02", "2026-11-20"))
        self.assertEqual(self.dates(con, at("2026-11-20T23:55"))[0], ["2026-11-13", "2026-11-20"])
        self.assertEqual(self.dates(con, at("2026-11-21T10:00"))[0], ["2026-11-13", "2026-11-20"])

    def test_friday_not_yet_published_uses_previous_weeks(self):
        _, con = self.make(weekdays("2026-11-02", "2026-11-20"))
        got, notes = self.dates(con, at("2026-11-20T20:00"))     # 23:52 才擷取
        self.assertEqual(got, ["2026-11-06", "2026-11-13"])
        self.assertIn("尚未發布", notes[0])

    def test_friday_holiday_uses_weeks_actual_last_trading_day(self):
        cal = calendar("2026-11-01", "2026-11-30", {"2026-11-13": "測試休市"})
        _, con = self.make(weekdays("2026-11-02", "2026-11-20", skip={"2026-11-13"}))
        got, notes = self.dates(con, at("2026-11-21T10:00"), cal)
        self.assertEqual(got, ["2026-11-12", "2026-11-20"])
        self.assertEqual(notes, ["2026-11-13 休市(測試休市(TWSE 2026 開休市表)),改用該週最後交易日 2026-11-12"])

    def test_friday_and_thursday_holiday_walks_back_to_wednesday(self):
        cal = calendar("2026-11-01", "2026-11-30", {"2026-11-12": "甲", "2026-11-13": "乙"})
        _, con = self.make(weekdays("2026-11-02", "2026-11-20", skip={"2026-11-12", "2026-11-13"}))
        got, notes = self.dates(con, at("2026-11-21T10:00"), cal)
        self.assertEqual(got, ["2026-11-11", "2026-11-20"])
        self.assertIn("2026-11-12 休市(甲(TWSE 2026 開休市表))、2026-11-13 休市(乙(TWSE 2026 開休市表)),"
                      "改用該週最後交易日 2026-11-11", notes[0])

    def test_friday_fetch_failure_reports_missing_day(self):
        # 日曆判定 11/13 開市;market 與正式快照都沒有該日(週一恢復)→ 不是休市,是缺漏。
        _, con = self.make(weekdays("2026-11-02", "2026-11-16", skip={"2026-11-13"}))
        for as_of in ("2026-11-16T23:55", "2026-11-17T10:00"):
            with self.assertRaisesRegex(rc.SelectionError, r"缺 2026-11-13 的正式快照:交易日曆判定該日開市"
                                        r".*market 也沒有該日,疑似資料漏抓。不退回該週前一交易日"):
                rc.select_weeks(con, at(as_of), mcal=self.NOV)
            with self.assertRaises(rc.SelectionError):
                rc.build_report(con, at(as_of), mcal=self.NOV)

    def test_market_present_but_snapshot_missing_is_reported(self):
        market = weekdays("2026-11-02", "2026-11-20")
        _, con = self.make(market, [d for d in market if d != "2026-11-20"])
        with self.assertRaisesRegex(rc.SelectionError, "缺 2026-11-20 的正式快照.*market 有該日資料"):
            rc.select_weeks(con, at("2026-11-21T10:00"), mcal=self.NOV)

    def test_scheduled_only_day_is_trading_but_says_not_yet_verified(self):
        cal = calendar("2026-11-01", "2026-11-12", announced=("2026",))
        _, con = self.make(weekdays("2026-11-02", "2026-11-19"))
        with self.assertRaisesRegex(rc.SelectionError, "缺 2026-11-20.*開休市表未列休市、無臨時休市公告\\(尚未以實際成交核對\\)"):
            rc.select_weeks(con, at("2026-11-21T10:00"), mcal=cal)

    def test_day_outside_calendar_is_unconfirmed(self):
        cal = calendar("2026-11-01", "2026-11-13")
        _, con = self.make(weekdays("2026-11-02", "2026-11-20"))
        with self.assertRaisesRegex(rc.SelectionError, "2026-11-20 不在交易日曆涵蓋範圍,無法確認是否開市"
                                    ".*market_calendar.py --refresh"):
            rc.select_weeks(con, at("2026-11-21T10:00"), mcal=cal)
        # 期限前:本週視為未完成,前兩週仍在涵蓋範圍內
        got, notes = self.dates(con, at("2026-11-20T20:00"), cal)
        self.assertEqual(got, ["2026-11-06", "2026-11-13"])
        self.assertIn("2026-11-20 尚未到發布期限,且交易日曆未涵蓋", notes[0])

    def test_whole_week_closed_is_skipped_and_noted(self):
        holidays = {d: "春節" for d in weekdays("2026-11-09", "2026-11-13")}
        cal = calendar("2026-11-01", "2026-11-30", holidays)
        _, con = self.make(weekdays("2026-11-02", "2026-11-20", skip=set(holidays)))
        got, notes = self.dates(con, at("2026-11-21T10:00"), cal)
        self.assertEqual(got, ["2026-11-06", "2026-11-20"])
        self.assertEqual(notes, ["略過 2026-11-09 當週:2026-11-09 當週整週休市:" +
                                 "、".join(f"{d} 休市(春節(TWSE 2026 開休市表))" for d in sorted(holidays))])

    def test_calendar_closed_but_data_present_is_contradiction(self):
        cal = calendar("2026-11-01", "2026-11-30", {"2026-11-20": "測試休市"})
        _, con = self.make(weekdays("2026-11-02", "2026-11-20"))
        with self.assertRaisesRegex(rc.SelectionError, "交易日曆判定 2026-11-20 休市.*日曆與資料矛盾"):
            rc.select_weeks(con, at("2026-11-21T10:00"), mcal=cal)

    def test_closure_announcement_is_point_in_time(self):
        # 10/22 週四快照台北 18:00 已發布;10/23 臨時休市 20:10 公告;11/01 才取得的 10 月成交資料
        # 已顯示 10/23 無成交,但 as-of 10/22 時還不存在,不能繞過公告時間。
        cal = calendar("2026-10-01", "2026-10-31", {"2026-10-09": "國慶補假"},
                       closures={"2026-10-23": ("臨時休市公告", "2026-10-22T20:10:00+08:00")},
                       fetched_at="2026-11-01T10:00:00+08:00")
        cal.data["realized"]["2026-10"]["trading_days"].remove("2026-10-23")
        cal = rc.market_calendar.MarketCalendar(cal.data)
        fx, con = self.make([], [])
        con.close()
        raw = sqlite3.connect(fx.path)
        raw.executemany("INSERT INTO market VALUES(?,1)",
                        [(d,) for d in weekdays("2026-10-05", "2026-10-22", skip={"2026-10-09"})])
        raw.commit()
        raw.close()
        fx.fill(weekdays("2026-10-05", "2026-10-21", skip={"2026-10-09"}))
        fx.run("thu", "2026-10-22", {"T": ("g", 1.0, 1.0), "Q": ("g", 0.0, 0.0)}, "2026-10-22T10:00:00+00:00")
        con = fx.con()
        self.addCleanup(con.close)
        before, notes_before = self.dates(con, at("2026-10-22T20:09"), cal)
        self.assertEqual(before, ["2026-10-08", "2026-10-16"])
        self.assertEqual(notes_before, ["略過 2026-10-19 當週:2026-10-23 正式快照尚未發布(期限 2026-10-24T09:00:00+08:00)",
                                        "2026-10-09 休市(國慶補假(TWSE 2026 開休市表)),改用該週最後交易日 2026-10-08"])
        after, notes_after = self.dates(con, at("2026-10-22T20:11"), cal)
        self.assertEqual(after, ["2026-10-16", "2026-10-22"])
        self.assertEqual(notes_after, ["2026-10-23 休市(臨時休市公告;公告 2026-10-22T20:10:00+08:00),"
                                       "改用該週最後交易日 2026-10-22"])

    def test_saturday_refresh_through_thursday_does_not_confirm_friday_closed(self):
        mc = rc.market_calendar
        thu = weekdays("2026-11-02", "2026-11-19")
        months = lambda y, m: (thu, thu, [{"url": "fixture", "sha256": "x"}]) if (y, m) == (2026, 11) else ([], [], [])

        def holidays(y):
            if y != 2026:
                raise mc.CalendarError("未公告")
            return {"title": "115 年市場開休市日期", "source": "fixture-schedule", "sha256": "x", "closed": []}
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        path = os.path.join(tmp.name, "cal.json")
        old = (mc.fetch_month, mc.fetch_holidays)
        mc.fetch_month, mc.fetch_holidays = months, holidays
        try:
            mc.refresh(path, now=at("2026-11-21T10:00"))
        finally:
            mc.fetch_month, mc.fetch_holidays = old
        cal = mc.load(path)
        st = cal.status("2026-11-20", at("2026-11-21T10:05"))
        self.assertEqual((st["state"], st["basis"]), ("trading", "scheduled"))
        self.assertIn("兩所已取得的成交資料只到 2026-11-19,不能證明此日休市", st["reason"])
        _, con = self.make(weekdays("2026-11-02", "2026-11-19"))
        with self.assertRaisesRegex(rc.SelectionError, "缺 2026-11-20 的正式快照:交易日曆判定該日開市"
                                    ".*market 也沒有該日,疑似資料漏抓"):
            rc.select_weeks(con, at("2026-11-21T10:05"), mcal=cal)
        _, con = self.make(weekdays("2026-11-02", "2026-11-20"))
        self.assertEqual(self.dates(con, at("2026-11-21T10:05"), cal), (["2026-11-13", "2026-11-20"], []))

    def test_1023_closure_from_repo_calendar_selects_thursday(self):
        # config/market_calendar.json:10/23 TWSE 臨時休市、10/26 開休市表假日;離線讀取,不連網。
        real = rc.market_calendar.load()
        st = real.status("2026-10-23")
        self.assertEqual((st["state"], st["basis"]), ("closed", "announced"))
        self.assertIn("115年10月23日休市一天", st["reason"])
        self.assertEqual(real.status("2026-10-23", at("2026-10-22T20:09"))["state"], "trading")
        market = weekdays("2026-10-05", "2026-10-30", skip={"2026-10-09", "2026-10-23", "2026-10-26"})
        _, con = self.make(market)
        got, notes = self.dates(con, at("2026-10-24T10:00"), real)
        self.assertEqual(got, ["2026-10-16", "2026-10-22"])
        self.assertIn("改用該週最後交易日 2026-10-22", notes[0])
        self.assertEqual(self.dates(con, at("2026-10-31T10:00"), real)[0], ["2026-10-22", "2026-10-30"])

    def test_same_day_market_row_needs_snapshot_or_provenance_before_as_of(self):
        fx, con = self.make(weekdays("2026-11-02", "2026-11-12"))
        con.close()
        raw = sqlite3.connect(fx.path)
        raw.execute("INSERT INTO market VALUES('2026-11-16',1)")
        raw.execute("CREATE TABLE market_provenance(date TEXT PRIMARY KEY, checked_at TEXT)")
        raw.execute("INSERT INTO market_provenance VALUES('2026-11-16','2026-11-16 10:05:00')")  # 台北 18:05
        raw.commit()
        raw.close()
        con = fx.con()
        self.addCleanup(con.close)
        self.assertNotIn("2026-11-16", rc.trading_calendar(con, at("2026-11-16T17:00"), {}))
        self.assertIn("2026-11-16", rc.trading_calendar(con, at("2026-11-16T18:10"), {}))

    def test_first_official_run_wins_and_late_or_unofficial_runs_ignored(self):
        fx = Fixture(weekdays("2026-11-02", "2026-11-20"))
        self.addCleanup(fx.close)
        fx.fill(weekdays("2026-11-02", "2026-11-19"))
        fx.run("unofficial", "2026-11-20", {"T": ("g", 9, 9.0)}, "2026-11-20T15:00:00+00:00", official=0)
        fx.run("first", "2026-11-20", {"T": ("g", 2, 2.0), "Q": ("g", 0, 0.0)}, "2026-11-20T15:52:00+00:00")
        fx.run("revision", "2026-11-20", {"T": ("g", 7, 7.0), "Q": ("g", 0, 0.0)}, "2026-11-20T16:30:00+00:00")
        con = fx.con()
        self.addCleanup(con.close)
        picked, _ = rc.select_weeks(con, at("2026-11-21T10:00"), mcal=self.NOV)
        self.assertEqual(picked[1]["run"]["snapshot_id"], "first")
        # as-of 早於首次擷取 → 本週視為尚未發布
        picked, notes = rc.select_weeks(con, at("2026-11-20T23:00"), mcal=self.NOV)
        self.assertEqual(picked[1]["date"], "2026-11-13")
        self.assertIn("尚未發布", notes[0])

    def test_empty_first_official_is_not_replaced_by_revision(self):
        fx = Fixture(weekdays("2026-11-09", "2026-11-20"))
        self.addCleanup(fx.close)
        fx.fill(weekdays("2026-11-09", "2026-11-19"))
        fx.run("empty", "2026-11-20", {}, "2026-11-20T15:52:00+00:00", stock_count=2)
        fx.run("revision", "2026-11-20", {"T": ("g", 1, 1.0), "Q": ("g", 0, 0.0)}, "2026-11-20T16:30:00+00:00")
        con = fx.con()
        self.addCleanup(con.close)
        with self.assertRaisesRegex(rc.SelectionError, "empty.*0/2.*不以後來修正版取代"):
            rc.select_weeks(con, at("2026-11-21T10:00"), mcal=self.NOV)


class SmoothingWindow(unittest.TestCase):
    def setUp(self):
        self.fx = Fixture(weekdays("2026-11-16", "2026-11-20"))
        self.addCleanup(self.fx.close)

    def window(self, as_of="2026-11-21T10:00"):
        con = self.fx.con()
        self.addCleanup(con.close)
        firsts = rc.published_first_runs(con, at(as_of))
        return rc.smoothing_window(con, firsts, rc.trading_calendar(con), "T", "2026-11-20")

    def test_three_distinct_trading_days_with_duplicate_runs_and_no_trade_day(self):
        fx = self.fx
        fx.run("d16", "2026-11-16", {"T": ("g", 4.0, 4.0)})
        fx.run("d17", "2026-11-17", {"T": ("g", 3.0, 3.5)})
        fx.run("d18", "2026-11-18", {"Q": ("g", 0.0, 0.0)})          # T 已確認零成交:不評分、不佔窗口
        fx.no_trade("2026-11-18", "T")
        fx.run("d19a", "2026-11-19", {"T": ("g", 2.0, 3.0)}, "2026-11-19T15:52:00+00:00")
        fx.run("d19b", "2026-11-19", {"T": ("g", 9.0, 9.0)}, "2026-11-19T16:30:00+00:00")
        fx.run("d20", "2026-11-20", {"T": ("g", 1.0, 2.0)})
        win = self.window()
        used = [s for s in win if s["status"] == "ok"]
        self.assertEqual([s["date"] for s in used], ["2026-11-20", "2026-11-19", "2026-11-17"])
        self.assertEqual([s["snapshot_id"] for s in used], ["d20", "d19a", "d17"])
        self.assertEqual(len({s["date"] for s in used}), 3)
        ex = rc.explain(snap({"T": 0.0}), snap({"T": 2.0}), "T")
        out = rc.render(ex, "A", "B", None, [win, win])
        self.assertIn("2026-11-17 +3.00, 2026-11-18 已確認零成交/停牌(不佔窗口), 2026-11-19 +2.00, "
                      "2026-11-20 +1.00 → 3 個不同交易日平均 +2.00(與快照 composite_s +2.00 一致,建置指紋相同)", out)

    def test_unexplained_missing_row_marks_window_incomplete_even_if_average_matches(self):
        # 11/18 有正式快照但缺 T 列,且無零成交/停牌證據。11/17 與 11/19、11/20 同分,
        # 若誤把 11/17 補進窗口,平均剛好等於快照 composite_s;仍不得標成已驗證。
        fx = self.fx
        fx.run("d17", "2026-11-17", {"T": ("g", 2.0, 2.0)})
        fx.run("d18", "2026-11-18", {"Q": ("g", 0.0, 0.0)})
        fx.run("d19", "2026-11-19", {"T": ("g", 2.0, 2.0)})
        fx.run("d20", "2026-11-20", {"T": ("g", 2.0, 2.0)})
        win = self.window()
        self.assertEqual([(s["date"], s["status"]) for s in win],
                         [("2026-11-20", "ok"), ("2026-11-19", "ok"), ("2026-11-18", "missing_row")])
        out = rc.render(rc.explain(snap({"T": 0.0}), snap({"T": 2.0}), "T"), "A", "B", None, [win, win])
        self.assertIn("2026-11-18 快照缺該股列(原因不明), 2026-11-19 +2.00, 2026-11-20 +2.00 → 不完整", out)
        self.assertNotIn("2026-11-17", out)
        self.assertNotIn("一致", out)
        self.assertNotIn("個不同交易日平均", out)

    def test_universe_rebuild_is_labelled_as_prior_published_observations(self):
        fx = self.fx
        fx.run("d18", "2026-11-18", {"T": ("g", 3.0, 3.0)}, universe="u98")
        fx.run("d19", "2026-11-19", {"T": ("g", 2.0, 2.5)}, universe="u98")
        fx.run("d20", "2026-11-20", {"T": ("g", 1.0, 4.0)}, universe="u121")
        win = self.window()
        out = rc.render(rc.explain(snap({"T": 0.0}), snap({"T": 4.0}), "T"), "A", "B", None, [win, win])
        self.assertIn("先前發布觀測值", out)
        self.assertIn("universe 與端點不同(2026-11-18, 2026-11-19)", out)
        self.assertIn("平均不等於快照 composite_s", out)
        self.assertIn("原始平滑輸入無法以快照驗證", out)
        self.assertNotIn("個不同交易日平均", out)

    def test_score_spec_change_alone_blocks_verification(self):
        fx = self.fx
        fx.run("d18", "2026-11-18", {"T": ("g", 3.0, 3.0)}, spec="old")
        fx.run("d19", "2026-11-19", {"T": ("g", 2.0, 2.5)})
        fx.run("d20", "2026-11-20", {"T": ("g", 1.0, 2.0)})
        out = rc.render(rc.explain(snap({"T": 0.0}), snap({"T": 2.0}), "T"), "A", "B", None,
                        [self.window(), self.window()])
        self.assertIn("評分規格 與端點不同(2026-11-18)", out)
        self.assertNotIn("平均不等於", out)

    def test_trading_day_without_snapshot_is_reported_as_gap(self):
        self.fx.run("d18", "2026-11-18", {"T": ("g", 3.0, 3.0)})
        self.fx.run("d20", "2026-11-20", {"T": ("g", 1.0, 2.0)})
        win = self.window()
        self.assertEqual([s["date"] for s in win], ["2026-11-20", "2026-11-19", "2026-11-18"])
        ex = rc.explain(snap({"T": 0.0}), snap({"T": 2.0}), "T")
        out = rc.render(ex, "A", "B", None, [win, win])
        self.assertIn("2026-11-19 缺正式快照", out)
        self.assertIn("不完整,無法以快照驗算", out)


class PeersNotRanked(unittest.TestCase):
    """上週兩檔同業排在目標前;本週兩檔未列入排名,其餘分數完全不變。"""

    def setUp(self):
        self.A = snap({"P1": 5.0, "P2": 4.0, "T": 3.0, "Q": 2.0, "R": 1.0})
        self.B = snap({"T": 3.0, "Q": 2.0, "R": 1.0})

    def test_absent_peers(self):
        ex = rc.explain(self.A, self.B, "T")
        out = rc.render(ex, "A", "B")
        self.assertEqual((ex["rankA"], ex["rankB"]), (3, 1))
        self.assertIn("名次上升 2 席", out)
        self.assertIn("實際超越 0 檔", out)
        self.assertIn("2 檔未列入本週族群排名(上週前 2、同分 0、後 0;快照無此股 2、轉族群 0、composite_s 缺值 0)", out)
        self.assertIn("P1: A 1 cs=+5.00 → B —(快照無此股)", out)
        self.assertIn("變動 +0.00", out)

    def test_moved_group_and_null_score_use_same_summary(self):
        B = dict(self.B)
        B["P1"] = {"stock_id": "P1", "grp": "other", "composite_s": 9.0, "composite": 9.0}
        B["P2"] = {"stock_id": "P2", "grp": "g", "composite_s": None, "composite": None}
        out = rc.render(rc.explain(self.A, B, "T"), "A", "B")
        self.assertIn("名次上升 2 席", out)
        self.assertIn("快照無此股 0、轉族群 1、composite_s 缺值 1", out)
        self.assertIn("P1: A 1 cs=+5.00 → B —(在族群 other)", out)
        self.assertNotIn("缺席", out)

    def test_joined_peer_from_other_group(self):
        A = dict(self.B)
        A["N"] = {"stock_id": "N", "grp": "other", "composite_s": 0.0, "composite": 0.0}
        B = dict(self.B)
        B["N"] = {"stock_id": "N", "grp": "g", "composite_s": 8.0, "composite": 8.0}
        out = rc.render(rc.explain(A, B, "T"), "A", "B")
        self.assertIn("名次下降 1 席", out)
        self.assertIn("1 檔本週新列入族群排名(本週前 1、同分 0、後 0;上週快照無此股 0、轉族群 1", out)


class TiesWithIntegerMidrank(unittest.TestCase):
    def test_three_way_tie_is_reported_even_when_midrank_is_integer(self):
        r = rc.rank_group(snap({"X": 5.0, "T": 3.0, "U": 3.0, "V": 3.0, "Y": 1.0}))
        self.assertEqual(r["T"], (3.0, 5, 2))
        self.assertEqual(rc.fmt_rank(*r["T"]), "3/5(與 2 檔同分,共 3 檔)")
        shuffled = rc.rank_group(snap({"V": 3.0, "Y": 1.0, "T": 3.0, "X": 5.0, "U": 3.0}))
        self.assertEqual(shuffled["T"], (3.0, 5, 2))

    def test_tie_formed_keeps_rank_but_changes_tie_state(self):
        ex = rc.explain(snap({"X": 5.0, "T": 3.0, "U": 2.0, "V": 4.0, "Y": 1.0}),
                        snap({"X": 5.0, "T": 3.0, "U": 3.0, "V": 3.0, "Y": 1.0}), "T")
        out = rc.render(ex, "A", "B")
        self.assertEqual((ex["rankA"], ex["rankB"]), (3, 3))
        self.assertEqual(sorted(ex["cats"]["tie_change"]), ["U", "V"])
        self.assertIn("名次不變", out)
        self.assertIn("同分狀態改變 2 檔", out)


class DashboardPayload(unittest.TestCase):
    """儀表板「本週排名變化」:與 CLI 同一套 explain/smoothing_window,另產第一層摘要。"""

    def setUp(self):
        fx = Fixture(weekdays("2026-11-09", "2026-11-20"))
        self.addCleanup(fx.close)
        week1 = {"L": ("g", 5.0, 5.0), "T": ("g", 3.0, 3.0), "X": ("g", 2.0, 2.0), "Y": ("g", 0.0, 0.0)}
        week2 = {"X": ("g", 4.0, 4.0), "T": ("g", 1.0, 1.0), "Y": ("g", 1.0, 1.0)}
        fx.fill(weekdays("2026-11-09", "2026-11-13"), week1)
        fx.fill(weekdays("2026-11-16", "2026-11-20"), week2)
        self.con = fx.con()
        self.addCleanup(self.con.close)
        self.p = rc.dashboard_payload(self.con, at("2026-11-21T10:00"), ["2026-11-13", "2026-11-20"],
                                      {"X": "超車股", "Y": "同分股", "L": "離開股"}, {"g": "測試"})

    def test_target_summary_counts_overtake_tie_and_membership(self):
        x = self.p["stocks"]["T"]
        self.assertEqual((self.p["dateA"], self.p["dateB"]), ("2026-11-13", "2026-11-20"))
        self.assertEqual((self.p["snapshotA"], self.p["snapshotB"]), ("r-2026-11-13", "r-2026-11-20"))
        self.assertEqual((x["rankA"], x["nA"], x["rankB"], x["nB"], x["tieB"]), (2, 4, 2.5, 3, 1))
        self.assertEqual((x["posA"], x["posB"]), ("第 2", "並列第 2"))
        self.assertEqual(x["summary"], [
            "T 上週在測試族群排第 2，本週被 1 檔同業超過，和同分股並列第 2。",
            "族群成員有變動：上週 4 檔、本週 3 檔參與排名，離開股本週不在族群。"])
        self.assertEqual(x["rankDetail"], [
            "兩檔同分，占第 2、3 席，平均名次為 2.5，比上週退後 0.5 席。",
            "名次拆解：被 1 檔超過（退後 1 席）；同分狀態改變 1 檔（同分股，退後 0.5 席）；"
            "離開股本週不在族群（前進 1 席）。"])
        self.assertEqual({p["id"]: p["posB"] for p in x["peers"]}, {"X": "第 1", "Y": "並列第 2", "L": None})
        cats = {p["id"]: (p["cat"], p["rankA"], p["rankB"], p["csA"], p["csB"], p["whyB"]) for p in x["peers"]}
        self.assertEqual(cats, {"X": ("overtook_target", 3, 1, 2.0, 4.0, None),
                                "Y": ("tie_change", 4, 2.5, 0.0, 1.0, None),
                                "L": ("left", 1, None, 5.0, None, "快照無此股")})

    def test_daily_composite_and_smoothed_composite_s_are_separate(self):
        x = self.p["stocks"]["T"]
        self.assertEqual((x["daily"]["compA"], x["daily"]["compB"], x["daily"]["delta"]), (3.0, 1.0, -2.0))
        self.assertEqual(x["daily"]["line"], "+3.00 → +1.00（−2.00）")
        self.assertEqual(x["smooth"]["line"], "+3.00 → +1.00（−2.00）")
        self.assertEqual((x["smooth"]["csA"], x["smooth"]["csB"], x["smooth"]["delta"]), (3.0, 1.0, -2.0))
        w = x["smooth"]["windows"]
        self.assertEqual([s["date"] for s in w[1]["slots"]], ["2026-11-18", "2026-11-19", "2026-11-20"])
        self.assertEqual([v["state"] for v in w], ["verified", "verified"])
        json.dumps(self.p, ensure_ascii=False, allow_nan=False)

    def test_other_stocks_get_their_own_payload_or_explicit_unavailable_state(self):
        self.assertEqual(sorted(self.p["stocks"]), ["L", "T", "X", "Y"])
        x = self.p["stocks"]["X"]
        self.assertEqual((x["rankA"], x["rankB"]), (3, 1))
        self.assertEqual(x["summary"][0], "超車股上週在測試族群排第 3，本週超過 1 檔同業，升到第 1。")
        self.assertFalse(self.p["stocks"]["L"]["available"])
        self.assertIn("L", self.p["stocks"]["L"]["reason"])

    def test_unpublished_date_is_selection_error(self):
        with self.assertRaises(rc.SelectionError):
            rc.dashboard_payload(self.con, at("2026-11-21T10:00"), ["2026-11-13", "2026-11-23"])


class DashboardTexts(unittest.TestCase):
    """第一層摘要用同分組第一個名次;明細才寫占哪幾席與平均名次。"""

    def texts(self, A, B, stock="T", names=None):
        return rc.stock_texts(rc.explain(A, B, stock), A, B, stock, names, {"g": "矽智財"})

    def test_three_way_tie_shows_first_seat_and_average_rank(self):
        A = snap({"a": 9.0, "b": 8.0, "c": 7.0, "d": 6.0, "T": 5.0, "U": 4.0, "V": 1.0})
        B = snap({"a": 9.0, "b": 8.0, "c": 7.0, "d": 6.0, "T": 3.0, "U": 3.0, "V": 3.0})
        summary, detail = self.texts(A, B, names={"T": "目標", "U": "甲", "V": "乙"})
        self.assertEqual(rc.rank_group(B)["T"], (6.0, 7, 2))
        self.assertEqual(summary, ["目標上週在矽智財族群排第 5，本週和甲、乙並列第 5。", "兩週都是同樣的 7 檔股票。"])
        self.assertEqual(detail[0], "三檔同分，占第 5、6、7 席，平均名次為 6，比上週退後 1 席。")
        self.assertIn("同分狀態改變 2 檔", detail[1])

    def test_same_count_but_different_members_is_not_called_same(self):
        A = snap({"a": 9.0, "T": 5.0, "b": 1.0})
        B = snap({"a": 9.0, "T": 5.0, "c": 1.0})
        summary, _ = self.texts(A, B)
        self.assertNotIn("同樣的", summary[1])
        self.assertEqual(summary[1], "族群成員有變動：上週 3 檔、本週 3 檔參與排名，b 本週不在族群，c 本週新加入。")
        self.assertEqual(summary[0], "T 上週在矽智財族群排第 2，本週仍排第 2。")

    def test_same_members_with_missing_score_is_not_called_same(self):
        A = snap({"a": 9.0, "T": 5.0, "b": 1.0})
        B = snap({"a": None, "T": 5.0, "b": 1.0})
        summary, detail = self.texts(A, B, names={"a": "缺分股"})
        self.assertEqual(summary, ["T 上週在矽智財族群排第 2，本週升到第 1。",
                                   "兩週族群名單相同，但有股票缺排名分數：上週排名 3 檔、本週 2 檔。"])
        self.assertEqual(detail, ["本週沒有同分，名次為第 1，比上週前進 1 席。",
                                  "名次拆解：缺分股缺分數，未列入排名（前進 1 席）。"])

    def test_missing_score_vs_left_group_and_rejoined_are_worded_apart(self):
        A = snap({"a": 9.0, "c": 8.0, "T": 5.0, "d": None})
        B = snap({"a": None, "T": 5.0, "d": 7.0})
        B["c"] = {"grp": "other", "composite_s": 8.0}
        _, detail = self.texts(A, B, names={"a": "甲", "c": "乙", "d": "丙"})
        self.assertEqual(detail, ["本週沒有同分，名次為第 2，比上週前進 1 席。",
                                  "名次拆解：甲缺分數，未列入排名（前進 1 席）；乙本週不在族群（前進 1 席）；"
                                  "丙上週缺分數，本週列入排名（退後 1 席）。"])

    def test_persistent_tie_says_tie_unchanged(self):
        A = snap({"a": 9.0, "T": 5.0, "U": 5.0, "b": 1.0})
        B = snap({"a": 9.0, "T": 5.0, "U": 5.0, "b": 8.0})
        summary, detail = self.texts(A, B, names={"T": "目標", "U": "甲", "b": "乙"})
        self.assertEqual(summary[0], "目標上週在矽智財族群和甲並列第 2，本週被 1 檔同業超過，和甲並列第 3。")
        self.assertEqual(detail, ["上週兩檔同分，占第 2、3 席，平均名次為 2.5。",
                                  "本週兩檔同分，占第 3、4 席，平均名次為 3.5，比上週退後 1 席。",
                                  "名次拆解：被 1 檔超過（退後 1 席）；和甲兩週都同分，同分狀態沒變（名次不受影響）。"])

    def test_change_line_uses_true_minus_and_rounded_delta(self):
        self.assertEqual(rc.change_line(6.1, -3.1), "+6.10 → −3.10（−9.20）")
        self.assertEqual(rc.change_line(6.4333, -0.9667), "+6.43 → −0.97（−7.40）")


class Cli(unittest.TestCase):
    def test_report_file_and_run_sql_are_read_only(self):
        fx = Fixture(weekdays("2026-11-09", "2026-11-20"))
        self.addCleanup(fx.close)
        fx.fill(weekdays("2026-11-09", "2026-11-20"))
        out = os.path.join(fx.tmp.name, "r.txt")
        self.assertEqual(rc.main(["--db", fx.path, "--stock", "T", "--as-of", "2026-11-21T10:00:00+08:00",
                                  "--output", out]), 0)
        text = Path(out).read_bytes().decode("utf-8")
        self.assertNotIn("\r\n", text)
        self.assertIn("A=2026-11-13 r-2026-11-13", text)
        self.assertIn("Q3b SELECT", text)
        with self.assertRaises(sqlite3.OperationalError):
            rc.main(["--db", fx.path, "--run-sql", "DELETE FROM market"])

    def test_output_refuses_input_database_and_creates_parent_dir(self):
        fx = Fixture(weekdays("2026-11-09", "2026-11-20"))
        self.addCleanup(fx.close)
        fx.fill(weekdays("2026-11-09", "2026-11-20"))
        digest = hashlib.sha256(Path(fx.path).read_bytes()).hexdigest()
        link = os.path.join(fx.tmp.name, "alias.db")
        os.link(fx.path, link)
        rel = os.path.relpath(fx.path)
        for target in (fx.path, rel, link, fx.path + "-wal"):
            with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
                rc.main(["--db", fx.path, "--as-of", "2026-11-21T10:00:00+08:00", "--output", target])
        self.assertEqual(hashlib.sha256(Path(fx.path).read_bytes()).hexdigest(), digest)
        out = os.path.join(fx.tmp.name, "new", "dir", "r.txt")
        self.assertEqual(rc.main(["--db", fx.path, "--as-of", "2026-11-21T10:00:00+08:00", "--output", out]), 0)
        self.assertTrue(Path(out).read_bytes().decode("utf-8").startswith("as-of"))

    def test_selection_error_exits_2(self):
        fx = Fixture(weekdays("2026-11-09", "2026-11-20"))
        self.addCleanup(fx.close)
        fx.fill(weekdays("2026-11-09", "2026-11-19"))
        self.assertEqual(rc.main(["--db", fx.path, "--as-of", "2026-11-21T10:00:00+08:00"]), 2)


if __name__ == "__main__":
    unittest.main()
