#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""hypotheses.py — 事先登錄的可證偽假設(唯讀評估,零第三方依賴)。

**為什麼要這個東西**(2026-07-26 對抗性審查的結論):
「多分析師比勝率」在統計上做不到——依實測變異外推,要分辨兩個正交策略真差 ΔIC=0.02
需要約 **2.3 年**。能快速分出高下的配對恰好是冗餘的(ρ=0.86)。所以與其登錄一份
分析師名單,不如登錄**一個明確、可證偽、有放棄條件的假設**。

登錄的紀律等同 as-seen 快照,只是對象從訊號換成假設:

  1. 規格(含操作定義)在登錄日凍結;`spec_sha` 同時覆蓋**規格欄位**與**評估函式原始碼**
     ——改任一邊雜湊就不符,測試會標紅。要改就是登錄一個新假設、時鐘重新起算。
  2. 方向事先宣告。事後才決定「其實反向也算成功」= 沒有假設。
  3. 最短評估窗與放棄條件事先宣告,避免看到喜歡的數字就宣布勝利。
  4. 登錄時的 in-sample 值一併記錄(`prior_is`)——誠實揭露「這個假設是從哪裡冒出來的」。
     每個假設都生於 in-sample,關鍵是登錄之後不再引用那個數字當證據。

主要判準一律**先按日聚合再算 Newey-West**(見 stats_ci)。個股-日不是獨立樣本:
實測未聚合時 t 值會從 +1.4 虛胖成 +3.3。
"""
import ast
import hashlib
import inspect
import json
import statistics
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stats_ci as sci

# 籌碼分數的固定定義(不隨 score.py 的 WEIGHTS 變動——假設的操作定義必須凍結)
CHIP_WEIGHTS = {"s_foreign": 1.4, "s_trust": 1.0, "s_dip": 1.0, "s_margin": 0.6}


def _get(row, col):
    try:
        v = row[col]
    except (KeyError, IndexError):
        return 0
    return 0 if v is None else v


def chip_score(row):
    return sum(w * _get(row, k) for k, w in CHIP_WEIGHTS.items())


MOMENTUM_MIN_SCORE = 1   # s_price ≥ 1 = 該族群內 rs20 的前 40%(由 score.py RANK_MAP 定義)


def eval_momentum_chip_agreement(ctx, hold_days):
    """H1 的操作定義。**此函式原始碼進 spec_sha,改動即視為新假設。**

    對每個 (交易日, 族群):
      1. 「動能領先者」= 該族群內 `s_price` >= MOMENTUM_MIN_SCORE 的成員
      2. 以這個子集合的 `chip_score` 中位數切成「籌碼同意」(> 中位)與「反對」(<= 中位)
      3. 兩組各算「相對族群中位的前瞻報酬」平均,相減
      4. 同一天各族群的差取平均 → 每日一個數

    **為什麼用分數門檻而不是「排名前 1/3」**(2026-07-26 審查發現):s_price 是 −2..+2 的
    整數,排名切 1/3 時 **93.0%(910/979)的 (日,族群) 格在邊界上有平手**,而 `sorted`
    是穩定排序 → 選中誰取決於 dict 插入順序(= db 列序),完全在 spec_sha 之外。實測把
    同一份資料改用 stock_id 降冪餵入,主要判準從 +0.985%(t=+1.4)變成 +0.121%(t=+0.2)。
    改用「分數 >= 門檻」後,成員集合由分數唯一決定,與任何排序或列序無關。
    註:s_price 的分位定義來自 score.py 的 RANK_MAP;若 RANK_MAP 改動,本假設的操作定義
    即改變,必須重新登錄(RANK_MAP 屬策略旋鈕,改它本來就要重設 IS_CUTOFF)。

    報酬用**隔日開盤進出**(訊號 18:07 才產出,close(d) 買不到),不扣成本
    ——兩組都是「買進」子集、各付同一筆來回成本,差值裡相消。

    回傳 {date: 當日差(%)}。
    """
    out = {}
    for d in ctx["dates"]:
        rows = ctx["scores"].get(d)
        if not rows:
            continue
        d0, d1 = ctx["shift"](d, 1), ctx["shift"](d, 1 + hold_days)
        if not d0 or not d1:
            continue
        diffs = []
        for g in ctx["groups"]:
            members = [s for s in rows if ctx["grp_of"](d, s) == g]
            rr = {s: ctx["oret"](s, d0, d1) for s in members}
            rr = {s: v for s, v in rr.items() if v is not None}
            if len(rr) < 6:
                continue
            gmed = statistics.median(rr.values())
            top = [s for s in rr if _get(rows[s], "s_price") >= MOMENTUM_MIN_SCORE]
            if len(top) < 2:
                continue
            cut = statistics.median(chip_score(rows[s]) for s in top)
            agree = [s for s in top if chip_score(rows[s]) > cut]
            against = [s for s in top if chip_score(rows[s]) <= cut]
            if not agree or not against:
                continue
            a = statistics.mean((rr[s] - gmed) * 100 for s in agree)
            b = statistics.mean((rr[s] - gmed) * 100 for s in against)
            diffs.append(a - b)
        if diffs:
            out[d] = statistics.mean(diffs)
    return out


EVALUATORS = {"momentum_chip_agreement": eval_momentum_chip_agreement}

# Historical metadata is preserved verbatim. The archive also contains the old
# evaluator/statistics source and the exact old digest payload. It is never
# evaluated with the current statistics under its original OOS clock.
LEGACY_REGISTRY = [
    {
        "id": "H1",
        "name": "動能領先者的籌碼支持",
        "plain": "族群裡已經在漲的股票中,「有法人在買」的那一半,是否比「沒人接」的那一半"
                 "後續表現更好?這是「漲了但沒人接」這句話的可檢定版本。",
        "registered": "2026-07-26",
        "evaluator": "momentum_chip_agreement",
        "hold_days": 10,
        "direction": "positive",          # 事先宣告:預期籌碼同意組較好
        "min_eff_obs": 10.0,              # 有效獨立觀測門檻(= 100 個成熟 OOS 交易日)
        "success": "OOS 主要判準 t 達 stats_ci.t_threshold(eff_obs) 所定門檻(正向)且有效獨立觀測 ≥ 10;該門檻由 MC 校準隨樣本量分級(eff≥12 時為 3.0、eff≥30 時為 2.4),固定 1.96 的實際誤判率是 10~24%",
        "abandon": "OOS 主要判準達同一門檻但方向相反(反向成立),"
                   "或有效獨立觀測 ≥ 30 仍未達門檻(無訊號)",
        "prior_is": {
            "note": "登錄時的 in-sample/restated 值,僅記錄本假設的出身,"
                    "**登錄後不得再當證據引用**",
            "source": "構想來自 2026-07-26 對抗性審查(Fable agent)的草稿檢定"
                      "(+1.94% ±1.19%, t=+1.6)。本登錄把操作定義收緊三處:改用隔日開盤"
                      "(可成交)、籌碼分數明確排除 s_vol、動能領先者改用「s_price >= 1」"
                      "分數門檻(原本的排名切 1/3 有 93% 的格在邊界平手,結果會隨 db 列序"
                      "改變 → 不可重現)。故數值不同但結論相同(與 0 無法分辨)",
            "value_pct": 0.910, "se_pct": 0.782, "t": 1.2,
            "measured_on": "2026-07-26 / data/findmind.db 2026-03-02~07-24 / 69 交易日 / "
                           "有效獨立觀測 6.9;已驗證與餵入順序無關(升冪/降冪差 <1e-12)",
        },
        "spec_sha": "562d0d24199e7561",   # 由 spec_digest() 產生;改規格或評估函式就會不符
    },
]


LEGACY_ARCHIVES = {
    "H1": {
        "path": os.path.join(os.path.dirname(__file__), "hypotheses_legacy", "H1_20260726.json"),
        "sha256_lf": "61ad920883d914d240359f0b8518f4155c0c7cdb8e3e4c8d5916c815f91cd9c4",
        "superseded_by": "H1v2",
    },
}


REGISTRY = [
    {
        **LEGACY_REGISTRY[0],
        "id": "H1v2",
        "name": "動能領先者的籌碼支持（交易日距離 HAC 第二版）",
        "version": 2,
        "registered": "2026-10-09",
        "oos_start_after": "2026-10-09",
        "supersedes_id": "H1",
        "supersedes_spec_sha": "562d0d24199e7561",
        "statistics_contract": "calendar_hac_v2",
        "planned_review_days": [100, 200, 300],
        "review_status": "separate_hypothesis_exploratory_pending_fixed_look_and_multiple_sequence_calibration",
        "success": "登錄截止日之後、首次正式且 eligible 的快照才可累積；n/F 樣本尺度 ≥ 10，"
                   "且正向 t 達既有 stats_ci.t_threshold 門檻（10≤n/F<12 為 3.0、"
                   "12≤n/F<30 為 2.5、≥30 為 2.4）。n/F 是啟發式而非量得獨立性；"
                   "本假說另列固定前 100/200/300 個成熟配對日檢視，不併入 C1/C2/C3 家族。"
                   "固定樣本存證及多重序列校準完成前僅達探索門檻，不自動採用；"
                   "門檻未保證多重比較或每週反覆檢查的整體誤判率",
        "abandon": "n/F 樣本尺度 ≥ 10 且 t 達同一門檻但方向相反，或 n/F ≥ 30 且 t 可估"
                   "卻未達門檻，均只列探索性反向／無訊號；待預定固定樣本檢視與多重序列校準"
                   "複核後才按方向或無訊號條件放棄，不按每週偷看結果放棄。SE=0/t 不可估不得判成功或無訊號",
        "prior_is": {
            **LEGACY_REGISTRY[0]["prior_is"],
            "note": "保留 H1 第一版登錄時的 in-sample/restated 出身記錄，並非 H1v2 的新估計；"
                    "舊時鐘與舊 SE 不移植為新版 OOS，**不得再當證據引用**",
        },
        "spec_sha": "176ec61328cccff3",
    },
]


def legacy_spec_digest(h):
    """Verify the LF-normalized text archive and recompute its original digest.

    Git may check text out as CRLF on Windows. Normalize only physical line
    endings; JSON string contents and all frozen source payloads stay exact.
    """
    entry = LEGACY_ARCHIVES[h["id"]]
    with open(entry["path"], "rb") as handle:
        payload = handle.read().replace(b"\r\n", b"\n")
    if hashlib.sha256(payload).hexdigest() != entry["sha256_lf"]:
        raise ValueError("legacy hypothesis archive SHA256 mismatch")
    archive = json.loads(payload)
    if archive["registry"] != h:
        raise ValueError("legacy hypothesis metadata does not match its frozen archive")
    return hashlib.sha256("\n".join(archive["spec_digest_parts"]).encode("utf-8")).hexdigest()[:16]


def spec_digest(h):
    """規格 + 操作定義 + **實際執法程式**的雜湊。任一邊改動 → 不符 → 視為新假設。

    2026-07-26 審查指出的缺口已補上:主要判準是「NW t 是否過門檻」,所以
    `stats_ci`(nw_se / summarize / MIN_EFF_OBS / t 門檻表)與 `status()` 本身都會改變判定,
    必須一起入湊——否則有人改了門檻表,舊登錄的判準就被無聲換掉了。
    `prior_is` 也入湊,免得「不得再引用」的出身數字被事後改寫。
    """
    if h["id"] in LEGACY_ARCHIVES:
        return legacy_spec_digest(h)
    core = {k: h[k] for k in ("id", "name", "registered", "evaluator", "hold_days",
                              "direction", "min_eff_obs", "success", "abandon", "version",
                              "oos_start_after", "supersedes_id", "supersedes_spec_sha",
                              "statistics_contract", "planned_review_days", "review_status")}
    core["prior_is"] = h["prior_is"]
    # Full source covers newly introduced helpers without maintaining a manual
    # closure list. Runtime function sources and constants additionally catch
    # monkeypatches that inspect.getsource(module) alone cannot see.
    statistics_source = inspect.getsource(sci)
    statistics_functions = {
        node.name: inspect.getsource(getattr(sci, node.name))
        for node in ast.parse(statistics_source).body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    statistics_constants = {name: value for name, value in vars(sci).items() if name.isupper()}
    parts = [
        json.dumps(core, ensure_ascii=False, sort_keys=True),
        inspect.getsource(EVALUATORS[h["evaluator"]]),
        json.dumps(CHIP_WEIGHTS, sort_keys=True),
        f"MOMENTUM_MIN_SCORE={MOMENTUM_MIN_SCORE}",
        inspect.getsource(chip_score), inspect.getsource(_get),
        inspect.getsource(status), inspect.getsource(evaluate),
        # 執法用的統計實作:改 SE 演算法或門檻表都會改變判定
        inspect.getsource(sci.nw_se), inspect.getsource(sci.summarize),
        inspect.getsource(sci.t_threshold),
        inspect.getsource(sci._calendar_positions), inspect.getsource(sci._aligned_values),
        inspect.getsource(sci._lag_products), inspect.getsource(sci.effective_obs),
        inspect.getsource(sci.overlap_lag), inspect.getsource(sci.autocorr1),
        inspect.getsource(sci.episodes),
        f"MIN_EFF_OBS={sci.MIN_EFF_OBS}",
        json.dumps([list(x) for x in sci.T_THRESHOLD]) + f"/{sci.T_THRESHOLD_LARGE}",
        statistics_source,
        json.dumps(statistics_functions, ensure_ascii=False, sort_keys=True),
        json.dumps(statistics_constants, ensure_ascii=False, sort_keys=True),
    ]
    return hashlib.sha256("\n".join(parts).encode("utf-8")).hexdigest()[:16]


def evaluate(h, ctx, date_filter=None):
    """Evaluate active specs; OOS needs eligible dates after the new registration.

    date_filter=None is explicitly retrospective background. A supplied filter
    must already contain only first official eligible snapshots; this function
    additionally enforces the active registration cutoff so old days cannot be
    reused even if a caller passes an overbroad set.
    """
    if h["id"] in LEGACY_ARCHIVES:
        raise ValueError("legacy hypotheses must not use current statistics under the old clock")
    series = EVALUATORS[h["evaluator"]](ctx, h["hold_days"])
    ds = sorted(d for d in series if date_filter is None or (
        d in date_filter and d > h["oos_start_after"]))
    if not ds:
        return None
    return sci.summarize([series[d] for d in ds], h["hold_days"], ds, ctx["dates"])


def status(h, s):
    """依**事先宣告**的條件判定,不臨場解釋。

    門檻沿用 `stats_ci.t_threshold(eff_obs)`;eff_obs 是 n/F 啟發式尺度,
    不是量得的獨立樣本數。新時鐘前的資料與 t 不可估均不能判成功。
    """
    if not s:
        return "累積中（尚無登錄後成熟資料）"
    if s.get("se_blocked") or s["eff_obs"] < h["min_eff_obs"]:
        return f"累積中(需 n/F 樣本尺度 ≥ {h['min_eff_obs']:.0f},現 {s['eff_obs']:.1f})"
    t, thr = s["t"], sci.t_threshold(s["eff_obs"])
    if t is None:
        return "累積中（t 不可估，不判定成功或無訊號）"
    want = 1 if h["direction"] == "positive" else -1
    if t is not None and t * want >= thr:
        return f"**達探索門檻 {thr:.1f}**；待固定樣本與多重序列校準複核，不自動採用"
    if t is not None and t * want <= -thr:
        return f"**探索性反向(門檻 {thr:.1f})**；待固定樣本與多重序列校準複核"
    if s["eff_obs"] >= 30:
        return "**探索性無訊號**；待固定樣本與多重序列校準複核"
    return f"累積中(尚未達判定門檻 {thr:.1f})"
