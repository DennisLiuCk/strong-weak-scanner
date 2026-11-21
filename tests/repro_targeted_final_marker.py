"""Offline final-pass repro against the committed database (read-only)."""
import argparse
from pathlib import Path
import sys
from unittest import mock


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    sys.path.insert(0, str(args.repo / "scripts"))
    import db_ro
    import fetch_daily as fd

    class ReadOnlyConnection:
        def __init__(self, con):
            self.execute = con.execute

        def commit(self):
            pass

    ledger = {}
    calls = []

    def source(dataset, exchange, day, wanted):
        calls.append(set(wanted))
        return [{"date": day, "stock_id": sid} for sid in wanted], True

    def set_coverage(con, stock_id, dataset, day):
        ledger[stock_id, dataset] = day

    with db_ro.connect(args.repo / "data" / "findmind.db") as db:
        con = ReadOnlyConnection(db)
        ids = [row[0] for row in db.execute("SELECT stock_id FROM universe ORDER BY stock_id")]
        dataset = "TaiwanStockShareholding"
        with mock.patch.object(fd.tstatus, "refresh_from_prices", return_value=0), \
                mock.patch.dict(fd.UPSERT, {dataset: lambda con, rows: len(rows)}), \
                mock.patch.object(fd, "_coverage_get",
                                  side_effect=lambda con, sid, ds: ledger.get((sid, ds))), \
                mock.patch.object(fd, "_coverage_set", side_effect=set_coverage):
            for label, wanted in (("subset", ids[:1]), ("full", ids)):
                calls.clear()
                fd.fetch_missing_raw(
                    con, wanted, [dataset], "2026-11-20", "2026-11-20", None,
                    sleep=0, fetcher=source, final_pass=True)
                requested = set().union(*calls) if calls else set()
                print(f"{label}: ids={len(wanted)} requests={len(calls)} "
                      f"requested_ids={len(requested)} "
                      f"marker={ledger.get(('exchange_final', dataset))}")


if __name__ == "__main__":
    main()
