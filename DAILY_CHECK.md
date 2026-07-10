# 每日檢視 Runbook(盤後 agent session / 人工)

> 每日資料預設由 GitHub Actions 台灣 21:40 自動抓取、評分、更新儀表板並 commit；
> Actions 延遲或想提早檢查時,可從本地執行同一條 `scripts/run_daily.py` 管線
>(排在 21:40 是因 FinMind 持股/融資券 21:00 才更新,留緩衝並避開整點;對照表見 daily-fetch.yml 註解)。
> 本文件是盤後想「確認執行狀況 + 討論今日資料」時的標準開場。
> 策略調整**不在每日做**——那走 `WEEKLY_REVIEW.md` 的門檻;每日只做確認、討論、資料修復。

## 步驟

1. **`git pull`**(最重要的一步:db 在 git 裡,不 pull 就是在看舊資料)。
2. **Actions 狀態**:`gh run list --workflow daily-fetch.yml -L 1`
   - 紅 → `gh run view <run-id> --log-failed`。常見:FinMind 限流(retry 已內建,
     偶發整批失敗隔日自癒)、Pages 部署偶發 `Deployment failed`(GitHub 端暫時性,
     重跑即可)。修復管線問題 → 本地驗證 → commit + push,隔天生效。
   - 即使綠的,也掃一眼 log 裡的 stderr 警告(`!` 開頭):TAIEX 抓空、price_adj 缺列、
     無事件大跳空(疑減資)、before_price 對帳不符、**TDCC 下載/解析失敗**
     (fetch_tdcc 失敗是 exit 0,綠燈看不出來;唯一硬警報是簡報品質快檢的
     「tdcc_holding 最新快照 >10 天」——TDCC 缺週不可回補,週內看到警告當天就要補跑;
     另確認最新資料日有 98 檔 `oos_signal_snapshots`,否則該日不得計入 OOS)。
3. **今日簡報**:`uv run --no-project --python 3.12 python scripts/daily_brief.py`
   (唯讀)——資料鮮度、市場 regime、族群雷達、tier 升降、蓄勢候補進出、
   綜合分大變動、資料品質快檢。這就是討論議程。
4. **深入討論**:儀表板 https://dennisliuck.github.io/strong-weak-scanner/ hover 看
   個股評分來源;要查數字直接讀 `data/findmind.db`(daily_scores / daily_metrics /
   group_metrics,唯讀查詢)。
5. **發現資料問題 / Actions 延遲**:執行
   `uv run --no-project --python 3.12 python scripts/run_daily.py`。它會只補 SQLite 缺口,
   原始資料未齊時拒絕正式發布；資料齊全才建立本地正式快照與儀表板,之後自行 review、
   commit + push。**發現策略問題**:記下來,累積到週六按 WEEKLY_REVIEW.md
   的 OOS 門檻判斷——單日數據永遠不是調旋鈕的理由。

## 環境備忘

- Python 一律 `uv run --no-project --python 3.12 python ...`(系統 python 是 Store stub)。
- 中文在 console 可能亂碼,檔案輸出 UTF-8 正常。
- 手動重跑每日管線:Actions 頁 `daily-fetch` → Run workflow,或本地跑
  `scripts/run_daily.py` 後 review、commit + push。兩者建立的正式快照地位相同；source
  只記錄 provenance。需無條件重抓來源修正版時才加 `--force`。
