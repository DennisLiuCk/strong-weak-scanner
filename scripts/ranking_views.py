#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""多視角族群內排名（觀察層）與影子 challenger（OOS 累積層）。

本模組刻意不寫 ``daily_scores``、不改 production tier，也不把任何視角稱為未來報酬
預測。它回答的是四個不同的現在式問題：

* A / leadership：短、波段、趨勢三個價格週期中，誰的相對位置靠前？
* B / resilience：誰較抗跌、槓桿較低、量價較不過熱？
* C / positioning：誰的法人相對位置靠前？TDCC／借券只作未驗證的旁證。
* D / fundamental：截至 ``available_at`` 已知資料，誰的營收與營運品質相對靠前？

所有新視角一律用平均秩百分位，平手拿相同名次，輸入順序不影響結果。正式 Champion
仍沿用 ``score.py`` 的既有分數／tier；本模組只替它建立 tie-safe 的顯示百分位，以及
兩個不回填歷史的 challenger。正式發布時由 ``snapshot_signals.py`` 把輸出 append-only
凍結，供後續 OOS 評估。
"""
from __future__ import annotations

import csv
import datetime as dt
import hashlib
import inspect
import json
import os
import statistics
from collections import defaultdict, deque

from hypotheses import CHIP_WEIGHTS
from score import VOL_OVERHEAT, VOLR_OVERHEAT, WEIGHTS


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROLES_CONFIG = os.path.join(ROOT, "config", "ranking_roles.csv")
SCHEMA_VERSION = 1
REGISTERED_AT = "2026-08-13T00:00:00+08:00"
MIN_ROLE_N = 4
TOP_PCT = 80.0
RISK_FLAG_CAP = 10.0

CHALLENGERS = {
    "vol_zero": {
        "label": "C1 量能移出綜合分",
        "purpose": "測試量能只保留為過熱 gate，是否降低無效自由度",
        "weights": {**WEIGHTS, "vol": 0.0},
        "registered_at": REGISTERED_AT,
        "oos_start": "2026-08-13",
    },
    "price_1_0": {
        "label": "C2 降低價格集中度",
        "purpose": "測試價格權重 1.4→1.0，其他條件不變",
        "weights": {**WEIGHTS, "price": 1.0},
        "registered_at": REGISTERED_AT,
        "oos_start": "2026-08-13",
    },
}

RANKING_CONTRACT = {
    "schema_version": SCHEMA_VERSION,
    "registered_at": REGISTERED_AT,
    "universe": "current universe, ranked only within formal group",
    "rank_method": "average-rank percentile (0..100)",
    "tie_policy": "exact ties receive the same midpoint rank",
    "cadence": {
        "A": "daily",
        "B": "daily",
        "C": "daily; TDCC overlay weekly",
        "D": "monthly/quarterly and point-in-time gated",
    },
    "lenses": {
        "A": {
            "name": "領先／進攻",
            "question": "誰正在不同價格週期中相對領先？",
            "components": ["close_adj/ma5", "ret20", "ma20/ma60"],
            "aggregate": "mean component percentile, then average-rank percentile",
        },
        "B": {
            "name": "風險／懷疑",
            "question": "誰目前較不脆弱？",
            "components": ["down_rs20", "-margin_util_pct", "-overheat_ratio"],
            "aggregate": "mean component percentile, then average-rank percentile",
            "official_risk_flag": f"hard cap at {RISK_FLAG_CAP:g}",
        },
        "C": {
            "name": "籌碼／偵察",
            "question": "誰的已校準法人相對位置較靠前？",
            "components": dict(CHIP_WEIGHTS),
            "aggregate": "weighted score, then average-rank percentile",
            "observation_only": ["tdcc concentration", "sbl balance relief"],
        },
        "D": {
            "name": "基本面／全局",
            "question": "截至已知資料，誰的成長與營運品質較靠前？",
            "components": ["3m revenue yoy", "3m revenue yoy acceleration",
                           "operating margin", "operating margin yoy delta"],
            "minimum": "growth and operating margin present; at least 3/4 components",
            "point_in_time": "fundamental_availability.first_seen_at <= as_of",
        },
    },
    "champion": {
        "status": "unchanged production composite/tier",
        "display_rank": "average-rank percentile of composite_s",
        "legacy_factor_ties": "kept unchanged until a separately governed production reset",
    },
    "challengers": CHALLENGERS,
    "usage": "descriptive comparison, research triage, hypothesis registration",
    "forbidden_claims": [
        "future return forecast", "buy/sell signal", "tradable edge", "analyst accuracy winner",
    ],
}


def _value(row, key):
    """同時支援 dict / sqlite3.Row；原始值缺失維持 None，不捏造中性 0。"""
    try:
        return row[key]
    except (KeyError, IndexError):
        return None


def _score(row, key):
    """daily_scores 的缺值語意是無訊號＝0；只供離散 s_* 使用。"""
    value = _value(row, key)
    return 0 if value is None else value


def rankdata(values):
    """平均秩；平手取區段中點，與餵入順序無關。"""
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        rank = (i + j) / 2 + 1
        for pos in range(i, j + 1):
            ranks[order[pos]] = rank
        i = j + 1
    return ranks


def rank_percentiles(values):
    """``{stock_id: raw}`` → tie-safe ``{stock_id: 0..100}``；None 不參與。"""
    usable = sorted((stock_id, value) for stock_id, value in values.items()
                    if value is not None)
    if not usable:
        return {}
    if len(usable) == 1:
        return {usable[0][0]: 50.0}
    ranks = rankdata([value for _stock_id, value in usable])
    return {
        stock_id: round((rank - 1) / (len(usable) - 1) * 100, 1)
        for (stock_id, _value), rank in zip(usable, ranks)
    }


def _ratio(row, numerator, denominator):
    a, b = _value(row, numerator), _value(row, denominator)
    if a is None or b is None or not b:
        return None
    return a / b - 1


def _overheat_ratio(row):
    ratios = []
    turnover = _value(row, "turnover_pct")
    volume_ratio = _value(row, "vol_ratio60")
    if turnover is not None:
        ratios.append(turnover / VOL_OVERHEAT)
    if volume_ratio is not None:
        ratios.append(volume_ratio / VOLR_OVERHEAT)
    return max(ratios) if ratios else None


def _aggregate_component_percentiles(component_maps, stock_ids, *, minimum,
                                     required=()):
    """先平均各 component percentile，再把平均值重新轉成族群內 percentile。"""
    raw = {}
    for stock_id in stock_ids:
        if any(stock_id not in component_maps[key] for key in required):
            raw[stock_id] = None
            continue
        values = [mapping[stock_id] for mapping in component_maps.values()
                  if stock_id in mapping]
        raw[stock_id] = statistics.mean(values) if len(values) >= minimum else None
    return rank_percentiles(raw), raw


def _quintile(percentile):
    if percentile is None:
        return None
    if percentile >= 80:
        return 4
    if percentile >= 60:
        return 3
    if percentile >= 40:
        return 2
    if percentile >= 20:
        return 1
    return 0


def peer_sensitivity(values):
    """每檔在 leave-one-peer-out 情境下，顯示五分位改變的比例。

    這是排行定義的結構壓力測試，不是抽樣誤差或未來報酬信賴區間。
    """
    usable = {stock_id: value for stock_id, value in values.items() if value is not None}
    if len(usable) < 4:
        return {stock_id: None for stock_id in values}
    base = rank_percentiles(usable)
    out = {}
    for stock_id in usable:
        changed = total = 0
        for removed in usable:
            if removed == stock_id:
                continue
            scenario = rank_percentiles({key: value for key, value in usable.items()
                                         if key != removed})
            total += 1
            changed += _quintile(scenario[stock_id]) != _quintile(base[stock_id])
        out[stock_id] = round(changed / total * 100, 1) if total else None
    return out


def _top_boundary_tie(values, top_n=2):
    usable = sorted(((value, stock_id) for stock_id, value in values.items()
                     if value is not None), reverse=True)
    if len(usable) <= top_n:
        return set()
    boundary = usable[top_n - 1][0]
    above = sum(value > boundary for value, _stock_id in usable)
    tied = {stock_id for value, stock_id in usable if value == boundary}
    return tied if above < top_n < above + len(tied) else set()


def _pareto(rows, dimensions):
    """同族群 Pareto frontier；dimensions 必須是全組共同可用的視角。"""
    if len(dimensions) < 2:
        return {row["stock_id"]: None for row in rows}
    out = {}
    for row in rows:
        dominated = False
        for other in rows:
            if other is row:
                continue
            weakly_better = all(other[key] >= row[key] for key in dimensions)
            strictly_better = any(other[key] > row[key] for key in dimensions)
            if weakly_better and strictly_better:
                dominated = True
                break
        out[row["stock_id"]] = not dominated
    return out


def load_roles(path=ROLES_CONFIG, universe_rows=None, *, strict=False):
    """讀取不影響 production 的角色同儕設定；role n<4 時只顯示標籤、不硬排名。"""
    if not path or not os.path.exists(path):
        if strict:
            raise ValueError(f"缺少 ranking role 設定：{path}")
        return {}
    roles = {}
    with open(path, encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        expected = ["stock_id", "group", "role", "role_label", "basis"]
        if reader.fieldnames != expected:
            raise ValueError("ranking_roles.csv 欄位必須是 " + ",".join(expected))
        for line_no, row in enumerate(reader, 2):
            stock_id = row["stock_id"].strip()
            if not stock_id or stock_id in roles:
                raise ValueError(f"ranking_roles.csv:{line_no} stock_id 空白或重複")
            if not all((row[key] or "").strip() for key in expected[1:]):
                raise ValueError(f"ranking_roles.csv:{line_no} 欄位不可留空")
            roles[stock_id] = {key: row[key].strip() for key in expected[1:]}
    if universe_rows is not None:
        universe = {row["stock_id"]: row["grp"] for row in universe_rows}
        missing = sorted(set(universe) - set(roles))
        extra = sorted(set(roles) - set(universe))
        wrong = sorted(stock_id for stock_id in set(universe) & set(roles)
                       if roles[stock_id]["group"] != universe[stock_id])
        if strict and (missing or extra or wrong):
            raise ValueError(
                "ranking role 覆蓋錯誤："
                f"missing={missing[:5]},extra={extra[:5]},wrong_group={wrong[:5]}")
    return roles


def _month_index(year, month):
    return int(year) * 12 + int(month) - 1


def _quarter_last_year(date_text):
    try:
        value = dt.date.fromisoformat(date_text)
        return value.replace(year=value.year - 1).isoformat()
    except (TypeError, ValueError):
        return None


def load_fundamental_inputs(con, *, as_of=None):
    """只讀 first-seen ledger 已證明當時可見的基本面資料。

    既有歷史資料在 baseline 前不會被冒充為過去已知；初始化只證明「從 baseline 起已知」。
    """
    meta = {"available": False, "as_of": as_of, "month_period": None,
            "quarter_period": None, "reason": "availability ledger missing"}
    have = con.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='fundamental_availability'"
    ).fetchone()
    if not have:
        return {}, meta
    predicate = " AND a.first_seen_at<=?" if as_of else ""
    args = (as_of,) if as_of else ()
    revenue_rows = list(con.execute(
        """SELECT m.stock_id,m.revenue_year,m.revenue_month,m.revenue,a.first_seen_at
           FROM month_revenue m JOIN fundamental_availability a
             ON a.dataset='TaiwanStockMonthRevenue' AND a.data_date=m.date
            AND a.stock_id=m.stock_id
           WHERE m.revenue IS NOT NULL""" + predicate,
        args,
    ))
    financial_rows = list(con.execute(
        """SELECT f.stock_id,f.date,f.type,f.value,a.first_seen_at
           FROM financials f JOIN fundamental_availability a
             ON a.dataset='TaiwanStockFinancialStatements' AND a.data_date=f.date
            AND a.stock_id=f.stock_id
           WHERE f.type IN ('Revenue','OperatingIncome') AND f.value IS NOT NULL""" + predicate,
        args,
    ))
    if not revenue_rows or not financial_rows:
        meta["reason"] = "point-in-time rows not yet available"
        return {}, meta

    latest_month = max(_month_index(row["revenue_year"], row["revenue_month"])
                       for row in revenue_rows)
    revenues = defaultdict(dict)
    month_seen = {}
    for row in revenue_rows:
        idx = _month_index(row["revenue_year"], row["revenue_month"])
        revenues[row["stock_id"]][idx] = row["revenue"]
        month_seen[(row["stock_id"], idx)] = row["first_seen_at"]

    latest_quarter = max(row["date"] for row in financial_rows)
    financials = defaultdict(dict)
    quarter_seen = {}
    for row in financial_rows:
        financials[(row["stock_id"], row["date"])][row["type"]] = row["value"]
        quarter_seen[(row["stock_id"], row["date"])] = row["first_seen_at"]

    out = {}
    stock_ids = sorted({row["stock_id"] for row in revenue_rows}
                       | {row["stock_id"] for row in financial_rows})
    for stock_id in stock_ids:
        series = revenues.get(stock_id, {})
        current_idx = [latest_month - offset for offset in (2, 1, 0)]
        prior_idx = [idx - 12 for idx in current_idx]
        earlier_idx = [latest_month - offset for offset in (3, 2, 1)]
        earlier_prior_idx = [idx - 12 for idx in earlier_idx]

        def growth(now_keys, prior_keys):
            if not all(key in series for key in now_keys + prior_keys):
                return None
            current = sum(series[key] for key in now_keys)
            prior = sum(series[key] for key in prior_keys)
            return current / prior - 1 if prior else None

        growth_3m = growth(current_idx, prior_idx)
        earlier_growth = growth(earlier_idx, earlier_prior_idx)
        acceleration = (growth_3m - earlier_growth
                        if growth_3m is not None and earlier_growth is not None else None)
        current_fin = financials.get((stock_id, latest_quarter), {})
        prior_date = _quarter_last_year(latest_quarter)
        prior_fin = financials.get((stock_id, prior_date), {})

        def margin(values):
            revenue, operating = values.get("Revenue"), values.get("OperatingIncome")
            return operating / revenue if revenue and operating is not None else None

        op_margin = margin(current_fin)
        prior_margin = margin(prior_fin)
        margin_delta = (op_margin - prior_margin
                        if op_margin is not None and prior_margin is not None else None)
        first_seen = [month_seen.get((stock_id, latest_month)),
                      quarter_seen.get((stock_id, latest_quarter))]
        first_seen = [value for value in first_seen if value]
        out[stock_id] = {
            "revenue_3m_yoy": growth_3m,
            "revenue_accel": acceleration,
            "operating_margin": op_margin,
            "operating_margin_yoy_delta": margin_delta,
            "month_period": f"{latest_month // 12:04d}-{latest_month % 12 + 1:02d}",
            "quarter_period": latest_quarter,
            "first_seen_at": max(first_seen) if first_seen else None,
        }
    meta.update({
        "available": True,
        "month_period": f"{latest_month // 12:04d}-{latest_month % 12 + 1:02d}",
        "quarter_period": latest_quarter,
        "reason": "point-in-time ledger",
    })
    return out, meta


def shadow_composites(con, date):
    """依各 challenger 權重重算最近三個有效交易日平均；不重跑 tier。"""
    columns = [f"s_{key}" for key in WEIGHTS]
    rows = con.execute(
        f"""SELECT date,stock_id,{','.join(columns)} FROM daily_scores
            WHERE date<=? ORDER BY date,stock_id""", (date,))
    history = {
        challenger: defaultdict(lambda: deque(maxlen=3)) for challenger in CHALLENGERS
    }
    for row in rows:
        for challenger, spec in CHALLENGERS.items():
            value = sum(spec["weights"][key] * _score(row, f"s_{key}") for key in WEIGHTS)
            history[challenger][row["stock_id"]].append(value)
    return {
        challenger: {stock_id: round(statistics.mean(values), 4)
                     for stock_id, values in by_stock.items() if values}
        for challenger, by_stock in history.items()
    }


def compute_group_views(rows, *, fundamentals=None, risk_ids=None,
                        challenger_values=None, roles=None):
    """計算單一正式族群的多視角；回傳順序固定為 stock_id。"""
    rows = sorted((dict(row) for row in rows), key=lambda row: row["stock_id"])
    stock_ids = [row["stock_id"] for row in rows]
    by_id = {row["stock_id"]: row for row in rows}
    fundamentals = fundamentals or {}
    risk_ids = set(risk_ids or ())
    challenger_values = challenger_values or {}
    roles = roles or {}

    champion_raw = {stock_id: _value(by_id[stock_id], "composite_s") for stock_id in stock_ids}
    champion_pct = rank_percentiles(champion_raw)
    sensitivity = peer_sensitivity(champion_raw)
    boundary_ties = _top_boundary_tie(champion_raw)

    a_raw = {
        "short": {stock_id: _ratio(by_id[stock_id], "close_adj", "ma5") for stock_id in stock_ids},
        "swing": {stock_id: _value(by_id[stock_id], "ret20") for stock_id in stock_ids},
        "trend": {stock_id: _ratio(by_id[stock_id], "ma20", "ma60") for stock_id in stock_ids},
    }
    a_components = {key: rank_percentiles(values) for key, values in a_raw.items()}
    lens_a, _a_mean = _aggregate_component_percentiles(a_components, stock_ids, minimum=3)

    b_raw = {
        "resilience": {stock_id: _value(by_id[stock_id], "down_rs20") for stock_id in stock_ids},
        "leverage_safety": {
            stock_id: (-_value(by_id[stock_id], "margin_util_pct")
                       if _value(by_id[stock_id], "margin_util_pct") is not None else None)
            for stock_id in stock_ids
        },
        "heat_safety": {
            stock_id: (-_overheat_ratio(by_id[stock_id])
                       if _overheat_ratio(by_id[stock_id]) is not None else None)
            for stock_id in stock_ids
        },
    }
    b_components = {key: rank_percentiles(values) for key, values in b_raw.items()}
    lens_b, _b_mean = _aggregate_component_percentiles(b_components, stock_ids, minimum=3)
    for stock_id in risk_ids:
        if stock_id in lens_b:
            lens_b[stock_id] = min(lens_b[stock_id], RISK_FLAG_CAP)

    c_raw = {
        stock_id: sum(weight * _score(by_id[stock_id], column)
                      for column, weight in CHIP_WEIGHTS.items())
        for stock_id in stock_ids
    }
    lens_c = rank_percentiles(c_raw)
    tdcc_components = {
        "big": rank_percentiles({
            stock_id: _value(by_id[stock_id], "tdcc_big400_chg") for stock_id in stock_ids}),
        "people": rank_percentiles({
            stock_id: (-_value(by_id[stock_id], "tdcc_people_chg")
                       if _value(by_id[stock_id], "tdcc_people_chg") is not None else None)
            for stock_id in stock_ids}),
    }
    tdcc_pct, _tdcc_mean = _aggregate_component_percentiles(
        tdcc_components, stock_ids, minimum=2)
    sbl_pct = rank_percentiles({
        stock_id: (-_value(by_id[stock_id], "sbl_chg10")
                   if _value(by_id[stock_id], "sbl_chg10") is not None else None)
        for stock_id in stock_ids})

    d_keys = ("revenue_3m_yoy", "revenue_accel", "operating_margin",
              "operating_margin_yoy_delta")
    d_raw = {key: {stock_id: fundamentals.get(stock_id, {}).get(key)
                   for stock_id in stock_ids} for key in d_keys}
    d_components = {key: rank_percentiles(values) for key, values in d_raw.items()}
    lens_d, _d_mean = _aggregate_component_percentiles(
        d_components, stock_ids, minimum=3,
        required=("revenue_3m_yoy", "operating_margin"))

    challenger_pct = {}
    for challenger in CHALLENGERS:
        challenger_pct[challenger] = rank_percentiles({
            stock_id: challenger_values.get(challenger, {}).get(stock_id)
            for stock_id in stock_ids})

    role_pct, role_counts = {}, defaultdict(int)
    for stock_id in stock_ids:
        info = roles.get(stock_id)
        if info:
            role_counts[(info["group"], info["role"])] += 1
    for role_key, count in role_counts.items():
        if count < MIN_ROLE_N:
            continue
        values = {stock_id: champion_raw[stock_id] for stock_id in stock_ids
                  if roles.get(stock_id)
                  and (roles[stock_id]["group"], roles[stock_id]["role"]) == role_key}
        role_pct.update(rank_percentiles(values))

    tie_counts = defaultdict(int)
    for value in champion_raw.values():
        if value is not None:
            tie_counts[value] += 1
    output = []
    for stock_id in stock_ids:
        fund = fundamentals.get(stock_id, {})
        available_lenses = [value for value in (
            lens_a.get(stock_id), lens_b.get(stock_id), lens_c.get(stock_id), lens_d.get(stock_id))
            if value is not None]
        role = roles.get(stock_id)
        output.append({
            "stock_id": stock_id,
            "grp": by_id[stock_id].get("grp"),
            "champion_pct": champion_pct.get(stock_id),
            "lens_a": lens_a.get(stock_id),
            "lens_b": lens_b.get(stock_id),
            "lens_c": lens_c.get(stock_id),
            "lens_d": lens_d.get(stock_id),
            "a_components": {key: values.get(stock_id) for key, values in a_components.items()},
            "b_components": {key: values.get(stock_id) for key, values in b_components.items()},
            "c_components": {"core": lens_c.get(stock_id), "tdcc": tdcc_pct.get(stock_id),
                             "sbl_relief": sbl_pct.get(stock_id)},
            "d_components": {key: values.get(stock_id) for key, values in d_components.items()},
            "d_raw": {key: fund.get(key) for key in d_keys},
            "d_periods": {"month": fund.get("month_period"),
                          "quarter": fund.get("quarter_period"),
                          "first_seen_at": fund.get("first_seen_at")},
            "consensus_count": sum(value >= TOP_PCT for value in available_lenses),
            "disagreement": (round(max(available_lenses) - min(available_lenses), 1)
                             if len(available_lenses) >= 2 else None),
            "peer_sensitivity": sensitivity.get(stock_id),
            "champion_tie_n": tie_counts.get(champion_raw[stock_id], 0),
            "top_boundary_tied": stock_id in boundary_ties,
            "risk_flagged": stock_id in risk_ids,
            "role": role["role"] if role else None,
            "role_label": role["role_label"] if role else None,
            "role_n": (role_counts.get((role["group"], role["role"])) if role else None),
            "role_pct": role_pct.get(stock_id),
            "shadow_vol0": challenger_pct.get("vol_zero", {}).get(stock_id),
            "shadow_price10": challenger_pct.get("price_1_0", {}).get(stock_id),
        })

    common_dimensions = [key for key in ("lens_a", "lens_b", "lens_c", "lens_d")
                         if output and all(row[key] is not None for row in output)]
    pareto = _pareto(output, common_dimensions)
    for row in output:
        row["pareto"] = pareto[row["stock_id"]]
        row["pareto_dimensions"] = len(common_dimensions)
    return output


def _spearman(values_a, values_b):
    pairs = [(a, b) for a, b in zip(values_a, values_b)
             if a is not None and b is not None]
    if len(pairs) < 4:
        return None
    rank_a = rankdata([a for a, _b in pairs])
    rank_b = rankdata([b for _a, b in pairs])
    mean_a, mean_b = statistics.mean(rank_a), statistics.mean(rank_b)
    numerator = sum((a - mean_a) * (b - mean_b) for a, b in zip(rank_a, rank_b))
    denominator_a = sum((a - mean_a) ** 2 for a in rank_a) ** 0.5
    denominator_b = sum((b - mean_b) ** 2 for b in rank_b) ** 0.5
    return numerator / (denominator_a * denominator_b) if denominator_a and denominator_b else None


def _group_summary(rows):
    champion = [row["champion_pct"] for row in rows]
    correlations = {}
    for key in ("lens_a", "lens_b", "lens_c", "lens_d", "shadow_vol0", "shadow_price10"):
        value = _spearman(champion, [row[key] for row in rows])
        correlations[key] = round(value, 3) if value is not None else None

    def leaders(key):
        usable = [row for row in rows if row[key] is not None]
        return [row["stock_id"] for row in sorted(
            usable, key=lambda row: (-row[key], row["stock_id"]))[:3]]

    champion_top = set(leaders("champion_pct")[:2])
    overlap = {}
    for key in ("shadow_vol0", "shadow_price10"):
        candidate_top = set(leaders(key)[:2])
        overlap[key] = len(champion_top & candidate_top)
    return {
        "grp": rows[0]["grp"] if rows else None,
        "n": len(rows),
        "correlations": correlations,
        "leaders": {key: leaders(key) for key in ("lens_a", "lens_b", "lens_c", "lens_d")},
        "d_coverage": sum(row["lens_d"] is not None for row in rows),
        "role_rank_coverage": sum(row["role_pct"] is not None for row in rows),
        "pareto_n": sum(row["pareto"] is True for row in rows),
        "top_boundary_tied": any(row["top_boundary_tied"] for row in rows),
        "challenger_top2_overlap": overlap,
    }


def spec_digest():
    """規格＋核心 evaluator 原始碼雜湊；改定義即得到新 spec、OOS 時鐘重啟。"""
    evaluators = {
        function.__name__: inspect.getsource(function)
        for function in (
            rank_percentiles, peer_sensitivity, load_fundamental_inputs,
            shadow_composites, compute_group_views,
        )
    }
    payload = {"contract": RANKING_CONTRACT, "evaluators": evaluators}
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


SPEC_SHA = spec_digest()


def build_from_db(con, date, *, as_of=None, roles_path=ROLES_CONFIG, strict_roles=False):
    """從 production DB 建立完整 dashboard／snapshot payload；全程只讀。"""
    rows = [dict(row) for row in con.execute(
        """SELECT u.stock_id,u.name,u.grp,u.biz,s.*,m.*
           FROM daily_scores s JOIN daily_metrics m USING(date,stock_id)
           JOIN universe u USING(stock_id) WHERE s.date=?
           ORDER BY u.grp,u.stock_id""", (date,))]
    if not rows:
        return None
    risk_ids = {row["stock_id"] for row in con.execute(
        "SELECT stock_id FROM risk_flags WHERE date=?", (date,))}
    fundamentals, fundamental_meta = load_fundamental_inputs(con, as_of=as_of)
    roles = load_roles(roles_path, rows, strict=strict_roles)
    challengers = shadow_composites(con, date)
    grouped = defaultdict(list)
    for row in rows:
        grouped[row["grp"]].append(row)
    output = []
    summaries = []
    for group in sorted(grouped):
        group_rows = compute_group_views(
            grouped[group], fundamentals=fundamentals, risk_ids=risk_ids,
            challenger_values=challengers, roles=roles,
        )
        output.extend(group_rows)
        summaries.append(_group_summary(group_rows))
    output.sort(key=lambda row: (row["grp"], row["stock_id"]))
    return {
        "schemaVersion": SCHEMA_VERSION,
        "specSha": SPEC_SHA,
        "registeredAt": REGISTERED_AT,
        "date": date,
        "asOf": as_of,
        "tiePolicy": RANKING_CONTRACT["tie_policy"],
        "championStatus": RANKING_CONTRACT["champion"]["status"],
        "contract": RANKING_CONTRACT,
        "fundamental": fundamental_meta,
        "coverage": {
            "stocks": len(output),
            "lensD": sum(row["lens_d"] is not None for row in output),
            "roleRank": sum(row["role_pct"] is not None for row in output),
            "peerSensitivity": sum(row["peer_sensitivity"] is not None for row in output),
        },
        "groups": summaries,
        "rows": output,
    }


def snapshot_rows(payload):
    """轉成 snapshot table 的固定欄位＋完整 JSON；schema 演進時舊 JSON 仍可稽核。"""
    if not payload:
        return []
    out = []
    for row in payload["rows"]:
        out.append({
            "date": payload["date"],
            "stock_id": row["stock_id"],
            "grp": row["grp"],
            "spec_sha": payload["specSha"],
            "champion_pct": row["champion_pct"],
            "lens_a": row["lens_a"],
            "lens_b": row["lens_b"],
            "lens_c": row["lens_c"],
            "lens_d": row["lens_d"],
            "shadow_vol0": row["shadow_vol0"],
            "shadow_price10": row["shadow_price10"],
            "payload_json": json.dumps(row, ensure_ascii=False, sort_keys=True,
                                       separators=(",", ":")),
        })
    return out
