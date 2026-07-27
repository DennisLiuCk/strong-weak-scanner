# 研究更新與市場議題維護

本文件管理「什麼時候該看、先看什麼、看完留下什麼紀錄」。正式公司事實仍由
`QUALITATIVE_RESEARCH_RUNBOOK.md` 的 evidence pack／獨立 reviewer 契約治理；
可證偽市場主張仍由 `LEADING_HYPOTHESES_PHASE2_RUNBOOK.md` 治理。本流程不改量化分數。

## 一個佇列，四種時鐘

```powershell
python scripts/research_queue.py --attention
python scripts/research_queue.py --calendar --weeks 8 --output tmp/research_calendar.md
python scripts/research_queue.py --lint
```

`research_queue.py` 以台灣研究日聚合：

1. `notes/qualitative/*.md` 的品質狀態與 `next_review`。
2. `notes/leading_hypotheses/*.md` 每則 H# 的 transition／`review_due`。
3. `notes/events/*.md` 的 `next_review`。
4. SQLite 月營收與三張季報表的「應有期間 × 全 universe」覆蓋。
5. `notes/research_topics/*.md` 的議題與 impact action。
6. `notes/research_topics/scan_log.csv` 的實際掃描窗口、範圍與下一次期限。

所有 DB 查詢都走 `db_ro.connect()`。到期是正常待辦，不使命令失敗；topic／scan schema
錯誤才 exit 1。

季報「應有期間」依年報 3/31、Q1 5/15、Q2 8/14、Q3 11/14 的截止日推導，不用資料庫
自己的 `MAX(date)` 當標準；否則整批落後一季仍會自我回報完整，單一早報者又會誤傷
其餘 universe。

已簽核正式筆記的內容 SHA 包含 `next_review` 等 meta。**不可為了打散日曆而只改
`next_review`**，那會使 `independently_verified` 簽核失效。輪掃、已看過但無變化、
snooze 與候選議題一律記在外部佇列／scan log；只有內容真的需要更新時才重做 evidence
pack 與獨立複核。

## 優先級與 SLA

| 優先級 | 典型觸發 | 目標 |
|---|---|---|
| P0 | `ai_draft`／`conflicted`、品質 invalid、已公布財務資料有 coverage 缺口 | 1 個工作日內定位責任與補救 |
| P1 | 正式重大訊息、法說／季報、H# 或事件到期、政策適用範圍待確認 | 5 個工作日內完成 triage |
| P2 | 月營收線索、產業事件、30 日內期限、敘事早於新議題 | 下一次週掃前判斷 route |
| P3 | 無事件的例行輪掃 | 依 A–D cohort 執行 |

月營收、股價、tier、法人、TDCC 或借券異常都只能是 `trigger_only`。它們可以要求搜尋，
不能直接成為 H# 生命週期轉移或正式筆記事實。

## 可持續的 121 檔節奏

| 頻率 | universe 覆蓋 | 做什麼 | 不做什麼 |
|---|---|---|---|
| 每週 | A–D 其中一個 cohort，約 30 檔；四週覆蓋一次 | 看新正式公告、既有 H# proof point、事件 trigger；留下 scan／topic | 不重寫 30 篇完整筆記 |
| 每月 | 全 121 檔機器普查 | 月營收期間完整度與變化 triage；只升級命中既有 KPI／H# 的項目 | 不把單月年增率當結論 |
| 每季 | 三張財報表齊備後全 121 檔 | 比對最新季報、法說、KPI、風險與 H#；有實質變化才更新正式筆記 | 不因「新一季到了」機械重做全文 |
| 每年 | 全 universe | 至少一次完整來源與商業模式複核；新建／重做採 `focused_v1` | 不沿用失效來源或未重算數字 |
| 事件驅動 | 命中的族群／個股 | P0/P1 triage；依 route 進正式筆記、H#、事件錨點或保留 topic | 不從跨產業新聞直接推成個股訂單 |

四個 cohort 由 `config/universe.csv` 按族群輪流分配，目前為 31／30／30／30，讓每週都
涵蓋所有族群。新增或移除成員後由腳本重算；硬期限與重大事件永遠優先於 cohort。

## 每週操作

1. 先 `git pull`，以系統 `python` 執行：

   ```powershell
   python scripts/research_queue.py --attention --output tmp/research_attention.md
   python scripts/research_queue.py --calendar --weeks 4 --output tmp/research_calendar.md
   ```

2. 依 `LEADING_HYPOTHESES_PHASE2_RUNBOOK.md` 的來源分層，掃描該週 cohort、跨族群上游
   錨點、交易所／MOPS 重大訊息、公司 IR、關鍵客戶／平台官方公告與重大政策。
3. 有新議題時複製 `notes/research_topics/_template.md`；沒有新議題也要在
   `scan_log.csv` 寫 `result_topic_ids=none`。
4. `scope=full` 只能在預定來源與完整時間窗真的都掃完時使用。只查當前日端點、主題式
   搜尋或缺歷史頁面時必須寫 `partial` 與 coverage limitation。
5. 先完成 topic impact 與 evidence boundary，再選 route：
   - 公司一手文件且改變既有事實 → `formal_note_candidate`。
   - 市場流傳、可證偽但未被正式資料覆蓋 → `hypothesis_candidate`。
   - 跨族群上游正式事件 → `event_anchor_candidate`。
   - 尚未能映射公司 → `market_issue_watch`／`policy_watch`。
6. 執行 lint。topic 不能自動貼入正式筆記；正式更新仍需同一 evidence pack 離線重算與
   獨立 reviewer。

GitHub 的 `research-watch.yml` 會在台灣每週一 09:00，以及 `fetch-financials` 成功後，
把唯讀待辦寫入 Actions summary／artifact。它只提醒，不會替代語意掃描，也不會寫 main。

## 財務資料完整度

`fetch_financials.py` 的月營收有兩段防線：

- 每月 12 日先抓 FinMind，並以 TWSE／TPEx 官方 OpenAPI 補當期缺口。
- 每月 17 日再驗一次：非季報月定向重抓月營收，5／8／11 月則由季報全抓順帶重驗；
  兩者都搭配 `--require-latest-month-complete`，仍缺就使 workflow 標紅，不再讓
  「單檔空回應」靜默綠燈。

定向修復可用：

```powershell
python scripts/fetch_financials.py --official-month-revenue-only `
  --stocks 3016,3661,3680,3707 --require-latest-month-complete
```

官方 OpenAPI 只適合補「當前最新月份」，不是歷史任意回補來源。財報表的 `date` 是財務
期間，不是精確發布時間；研究宣稱應寫「本次掃描新看到某期間」，不可倒推出公告時刻。

## Topic 不是第四套事實庫

`notes/research_topics/` 保存「值得處理的候選議題」，最小生命週期為：

```text
initial → inbox → triaged → promoted / dismissed / resolved
```

每則議題必須保存來源發布日、研究捕捉日、review due、來源鏈、受影響族群／股票、方向、
route、`note_action`、action due 與證據邊界。`candidate_source` 只表示可作後續研究來源；
`trigger_only` 連候選證據都不是。狀態轉移追加保存，不覆寫歷史。

特別注意：

- 平台商列名「生態系夥伴」不等於個別公司的新增訂單、營收、份額或毛利。
- 同業 HBM、先進封裝或液冷事件不等於本 universe 同族群每家公司受惠。
- 政策新聞在完成 HTS code、豁免、原產地、客戶／Incoterms 暴露前，不建立公司層級損益
  主張。
- 敘事早於新 topic 只產生「review」提示；review 結果可以是無關、留在 watch，而不是
  必然改文。
