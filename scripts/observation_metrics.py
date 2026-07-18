#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Expanded official fields -> descriptive observation metrics.

This module deliberately does not import score.py and does not write daily_scores,
tier, regime, or any OOS snapshot.  It rebuilds two replaceable observation tables:

* observation_metrics: stock/day flow decomposition and official-index excess return
* group_observation_metrics: size-neutral group medians/breadth from the stock table

All ratios are descriptive.  No value is labelled bullish/bearish or used as a
strategy threshold here.
"""
from collections import defaultdict
import statistics


OBS_COLUMNS = (
    ("date", "TEXT"), ("stock_id", "TEXT"), ("market", "TEXT"),
    ("benchmark_name", "TEXT"),
    ("avg_shares_per_trade", "REAL"), ("avg_value_per_trade", "REAL"),
    ("foreign_gross", "INTEGER"), ("foreign_imbalance_pct", "REAL"),
    ("trust_gross", "INTEGER"), ("trust_imbalance_pct", "REAL"),
    ("dealer_self_gross", "INTEGER"), ("dealer_self_imbalance_pct", "REAL"),
    ("dealer_hedge_gross", "INTEGER"), ("dealer_hedge_imbalance_pct", "REAL"),
    ("inst_gross", "INTEGER"), ("inst_participation_pct", "REAL"),
    ("dealer_self_net_volume_pct", "REAL"),
    ("dealer_hedge_net_volume_pct", "REAL"),
    ("margin_balance_change", "INTEGER"), ("margin_net_flow", "INTEGER"),
    ("margin_flow_residual", "INTEGER"), ("margin_limit_util_pct", "REAL"),
    ("margin_net_flow_shares_pct", "REAL"),
    ("short_balance_change", "INTEGER"), ("short_net_flow", "INTEGER"),
    ("short_flow_residual", "INTEGER"), ("short_limit_util_pct", "REAL"),
    ("short_net_flow_shares_pct", "REAL"),
    ("foreign_shares_change", "INTEGER"), ("foreign_limit_used_pct", "REAL"),
    ("sbl_balance_change", "INTEGER"), ("sbl_net_flow", "INTEGER"),
    ("sbl_flow_residual", "INTEGER"), ("sbl_sell_limit_pct", "REAL"),
    ("sbl_sell_shares_pct", "REAL"), ("sbl_return_shares_pct", "REAL"),
    ("sbl_adjustment_shares_pct", "REAL"), ("sbl_net_flow_shares_pct", "REAL"),
    ("stock_ret1", "REAL"), ("stock_ret5", "REAL"), ("stock_ret20", "REAL"),
    ("index_ret1", "REAL"), ("index_ret5", "REAL"), ("index_ret20", "REAL"),
    ("excess_ret1", "REAL"), ("excess_ret5", "REAL"), ("excess_ret20", "REAL"),
)


GROUP_COLUMNS = (
    ("date", "TEXT"), ("grp", "TEXT"), ("n", "INTEGER"),
    ("foreign_buy_breadth", "REAL"), ("trust_buy_breadth", "REAL"),
    ("med_foreign_imbalance_pct", "REAL"), ("med_trust_imbalance_pct", "REAL"),
    ("med_inst_participation_pct", "REAL"),
    ("med_dealer_self_net_volume_pct", "REAL"),
    ("med_dealer_hedge_net_volume_pct", "REAL"),
    ("med_margin_net_flow_shares_pct", "REAL"),
    ("med_short_net_flow_shares_pct", "REAL"),
    ("med_margin_limit_util_pct", "REAL"), ("med_short_limit_util_pct", "REAL"),
    ("med_foreign_limit_used_pct", "REAL"),
    ("med_sbl_sell_shares_pct", "REAL"), ("med_sbl_return_shares_pct", "REAL"),
    ("med_sbl_adjustment_shares_pct", "REAL"), ("med_sbl_net_flow_shares_pct", "REAL"),
    ("med_excess_ret1", "REAL"), ("med_excess_ret5", "REAL"),
    ("med_excess_ret20", "REAL"),
    ("excess_breadth1", "REAL"), ("excess_breadth5", "REAL"),
    ("excess_breadth20", "REAL"),
    ("n_excess1", "INTEGER"), ("n_excess5", "INTEGER"), ("n_excess20", "INTEGER"),
)


def _dict_rows(cursor):
    names = [item[0] for item in cursor.description]
    return [dict(zip(names, row)) for row in cursor.fetchall()]


def _complete_sum(*values):
    return None if any(value is None for value in values) else sum(values)


def _ratio_pct(numerator, denominator):
    return (numerator / denominator * 100) if (numerator is not None and denominator) else None


def _difference(current, previous):
    return (current - previous) if (current is not None and previous is not None) else None


def _return(current, previous):
    return (current / previous - 1) if (current is not None and previous) else None


def _create_table(con, table, columns, primary_key):
    con.execute(f'DROP TABLE IF EXISTS "{table}"')
    body = ",".join(f'"{name}" {sql_type}' for name, sql_type in columns)
    con.execute(f'CREATE TABLE "{table}"({body},PRIMARY KEY({primary_key}))')


def _insert_dicts(con, table, columns, rows):
    names = [name for name, _ in columns]
    marks = ",".join("?" for _ in names)
    quoted = ",".join(f'"{name}"' for name in names)
    con.executemany(
        f'INSERT INTO "{table}"({quoted}) VALUES({marks})',
        [tuple(row.get(name) for name in names) for row in rows],
    )


def _stock_rows(con):
    return _dict_rows(con.execute("""
        SELECT p.date,p.stock_id,p.volume,p.amount,p.trades,
               COALESCE(pa.close,p.close) AS close_adj,
               i.foreign_net,i.foreign_buy,i.foreign_sell,
               i.trust_net,i.trust_buy,i.trust_sell,
               i.dealer_self_net,i.dealer_self_buy,i.dealer_self_sell,
               i.dealer_hedge_net,i.dealer_hedge_buy,i.dealer_hedge_sell,
               m.margin_bal,m.margin_prev_bal,m.margin_buy,m.margin_sell,m.margin_cash_repay,m.margin_limit,
               m.short_bal,m.short_prev_bal,m.short_sell,m.short_buyback,m.short_stock_repay,m.short_limit,
               h.shares_issued,h.foreign_shares,h.foreign_limit_pct,
               s.sbl_prev_bal,s.sbl_sell,s.sbl_return,s.sbl_adjustment,s.sbl_bal,s.sbl_next_limit,
               sm.market
        FROM price p
        JOIN universe u USING(stock_id)
        LEFT JOIN price_adj pa ON pa.date=p.date AND pa.stock_id=p.stock_id
        LEFT JOIN inst i ON i.date=p.date AND i.stock_id=p.stock_id
        LEFT JOIN margin m ON m.date=p.date AND m.stock_id=p.stock_id
        LEFT JOIN holding h ON h.date=p.date AND h.stock_id=p.stock_id
        LEFT JOIN sbl s ON s.date=p.date AND s.stock_id=p.stock_id
        LEFT JOIN security_market sm ON sm.stock_id=p.stock_id
        ORDER BY p.stock_id,p.date
    """))


def _benchmark_closes(con, twse_key, tpex_key):
    keys = {"TWSE": twse_key, "TPEx": tpex_key}
    out = {"TWSE": {}, "TPEx": {}}
    for market, key in keys.items():
        out[market] = dict(con.execute(
            """SELECT date,close FROM market_index
               WHERE market=? AND index_key=? AND close IS NOT NULL ORDER BY date""",
            (market, key),
        ).fetchall())
    return keys, out


def _build_stock_observations(con, twse_key, tpex_key):
    benchmark_names, benchmark = _benchmark_closes(con, twse_key, tpex_key)
    by_stock = defaultdict(list)
    for row in _stock_rows(con):
        by_stock[row["stock_id"]].append(row)

    observations = []
    for stock_id, rows in by_stock.items():
        for index, row in enumerate(rows):
            shares = row["shares_issued"]
            volume = row["volume"]
            market = row["market"] if row["market"] in benchmark_names else None

            foreign_gross = _complete_sum(row["foreign_buy"], row["foreign_sell"])
            trust_gross = _complete_sum(row["trust_buy"], row["trust_sell"])
            dealer_self_gross = _complete_sum(row["dealer_self_buy"], row["dealer_self_sell"])
            dealer_hedge_gross = _complete_sum(row["dealer_hedge_buy"], row["dealer_hedge_sell"])
            inst_gross = _complete_sum(
                foreign_gross, trust_gross, dealer_self_gross, dealer_hedge_gross)

            margin_flow = (None if any(row[name] is None for name in
                                      ("margin_buy", "margin_sell", "margin_cash_repay"))
                           else row["margin_buy"] - row["margin_sell"] - row["margin_cash_repay"])
            short_flow = (None if any(row[name] is None for name in
                                     ("short_sell", "short_buyback", "short_stock_repay"))
                          else row["short_sell"] - row["short_buyback"] - row["short_stock_repay"])
            sbl_flow = (None if any(row[name] is None for name in
                                   ("sbl_sell", "sbl_return", "sbl_adjustment"))
                        else row["sbl_sell"] - row["sbl_return"] + row["sbl_adjustment"])

            previous = rows[index - 1] if index else None
            # Use the previous balance printed in the same official daily report. Exchanges
            # can restate it, so yesterday's stored current balance is not always identical.
            margin_change = _difference(row["margin_bal"], row["margin_prev_bal"])
            short_change = _difference(row["short_bal"], row["short_prev_bal"])
            foreign_change = _difference(
                row["foreign_shares"], previous["foreign_shares"] if previous else None)
            sbl_change = _difference(row["sbl_bal"], row["sbl_prev_bal"])
            previous_sbl_limit = previous["sbl_next_limit"] if previous else None

            stock_returns = {}
            index_returns = {}
            excess_returns = {}
            for horizon in (1, 5, 20):
                start = rows[index - horizon] if index >= horizon else None
                stock_return = _return(row["close_adj"], start["close_adj"] if start else None)
                index_return = None
                if start and market:
                    index_return = _return(
                        benchmark[market].get(row["date"]),
                        benchmark[market].get(start["date"]),
                    )
                stock_returns[horizon] = stock_return
                index_returns[horizon] = index_return
                excess_returns[horizon] = (
                    stock_return - index_return
                    if stock_return is not None and index_return is not None else None)

            allowed_foreign_shares = (
                shares * row["foreign_limit_pct"] / 100
                if shares and row["foreign_limit_pct"] is not None else None)
            observations.append({
                "date": row["date"], "stock_id": stock_id, "market": market,
                "benchmark_name": benchmark_names.get(market),
                "avg_shares_per_trade": _ratio_pct(volume, row["trades"]) / 100
                if row["trades"] else None,
                "avg_value_per_trade": _ratio_pct(row["amount"], row["trades"]) / 100
                if row["trades"] else None,
                "foreign_gross": foreign_gross,
                "foreign_imbalance_pct": _ratio_pct(row["foreign_net"], foreign_gross),
                "trust_gross": trust_gross,
                "trust_imbalance_pct": _ratio_pct(row["trust_net"], trust_gross),
                "dealer_self_gross": dealer_self_gross,
                "dealer_self_imbalance_pct": _ratio_pct(row["dealer_self_net"], dealer_self_gross),
                "dealer_hedge_gross": dealer_hedge_gross,
                "dealer_hedge_imbalance_pct": _ratio_pct(row["dealer_hedge_net"], dealer_hedge_gross),
                "inst_gross": inst_gross,
                # Market volume counts shares once; buy+sell counts the two trading sides.
                "inst_participation_pct": _ratio_pct(inst_gross, 2 * volume) if volume else None,
                "dealer_self_net_volume_pct": _ratio_pct(row["dealer_self_net"], volume),
                "dealer_hedge_net_volume_pct": _ratio_pct(row["dealer_hedge_net"], volume),
                "margin_balance_change": margin_change, "margin_net_flow": margin_flow,
                "margin_flow_residual": _difference(margin_change, margin_flow),
                "margin_limit_util_pct": _ratio_pct(row["margin_bal"], row["margin_limit"]),
                "margin_net_flow_shares_pct": _ratio_pct(
                    margin_flow * 1000 if margin_flow is not None else None, shares),
                "short_balance_change": short_change, "short_net_flow": short_flow,
                "short_flow_residual": _difference(short_change, short_flow),
                "short_limit_util_pct": _ratio_pct(row["short_bal"], row["short_limit"]),
                "short_net_flow_shares_pct": _ratio_pct(
                    short_flow * 1000 if short_flow is not None else None, shares),
                "foreign_shares_change": foreign_change,
                "foreign_limit_used_pct": _ratio_pct(row["foreign_shares"], allowed_foreign_shares),
                "sbl_balance_change": sbl_change, "sbl_net_flow": sbl_flow,
                "sbl_flow_residual": _difference(sbl_change, sbl_flow),
                # Yesterday's "next-day limit" is the limit applicable to today's sale.
                "sbl_sell_limit_pct": _ratio_pct(row["sbl_sell"], previous_sbl_limit),
                "sbl_sell_shares_pct": _ratio_pct(row["sbl_sell"], shares),
                "sbl_return_shares_pct": _ratio_pct(row["sbl_return"], shares),
                "sbl_adjustment_shares_pct": _ratio_pct(row["sbl_adjustment"], shares),
                "sbl_net_flow_shares_pct": _ratio_pct(sbl_flow, shares),
                **{f"stock_ret{h}": stock_returns[h] for h in (1, 5, 20)},
                **{f"index_ret{h}": index_returns[h] for h in (1, 5, 20)},
                **{f"excess_ret{h}": excess_returns[h] for h in (1, 5, 20)},
            })
    return observations


def _median(values, min_n):
    clean = [value for value in values if value is not None]
    return statistics.median(clean) if len(clean) >= min_n else None


def _breadth(values, min_n):
    clean = [value for value in values if value is not None]
    return (sum(value > 0 for value in clean) / len(clean)) if len(clean) >= min_n else None


def _build_group_observations(con, min_group_n):
    rows = _dict_rows(con.execute("""
        SELECT o.*,u.grp FROM observation_metrics o JOIN universe u USING(stock_id)
        ORDER BY o.date,u.grp,o.stock_id
    """))
    grouped = defaultdict(list)
    for row in rows:
        grouped[(row["date"], row["grp"])].append(row)

    med_fields = (
        "foreign_imbalance_pct", "trust_imbalance_pct", "inst_participation_pct",
        "dealer_self_net_volume_pct", "dealer_hedge_net_volume_pct",
        "margin_net_flow_shares_pct", "short_net_flow_shares_pct",
        "margin_limit_util_pct", "short_limit_util_pct", "foreign_limit_used_pct",
        "sbl_sell_shares_pct", "sbl_return_shares_pct", "sbl_adjustment_shares_pct",
        "sbl_net_flow_shares_pct", "excess_ret1", "excess_ret5", "excess_ret20",
    )
    output = []
    for (day, group), members in grouped.items():
        row = {"date": day, "grp": group, "n": len(members)}
        row["foreign_buy_breadth"] = _breadth(
            [member["foreign_imbalance_pct"] for member in members], min_group_n)
        row["trust_buy_breadth"] = _breadth(
            [member["trust_imbalance_pct"] for member in members], min_group_n)
        for field in med_fields:
            row["med_" + field] = _median([member[field] for member in members], min_group_n)
        for horizon in (1, 5, 20):
            values = [member[f"excess_ret{horizon}"] for member in members]
            clean = [value for value in values if value is not None]
            row[f"excess_breadth{horizon}"] = (
                sum(value > 0 for value in clean) / len(clean)
                if len(clean) >= min_group_n else None)
            row[f"n_excess{horizon}"] = len(clean)
        output.append(row)
    return output


def build_observation_metrics(con, twse_key, tpex_key, min_group_n=6):
    """Rebuild both observation tables and return their row counts."""
    _create_table(con, "observation_metrics", OBS_COLUMNS, '"date","stock_id"')
    stock_rows = _build_stock_observations(con, twse_key, tpex_key)
    _insert_dicts(con, "observation_metrics", OBS_COLUMNS, stock_rows)
    con.execute("CREATE INDEX idx_observation_metrics_stock_date "
                "ON observation_metrics(stock_id,date)")

    _create_table(con, "group_observation_metrics", GROUP_COLUMNS, '"date","grp"')
    group_rows = _build_group_observations(con, min_group_n)
    _insert_dicts(con, "group_observation_metrics", GROUP_COLUMNS, group_rows)
    con.commit()
    return {"stock_rows": len(stock_rows), "group_rows": len(group_rows)}
