# 研究更新與市場議題維護

本文件管理「什麼時候該看、先看什麼、看完留下什麼紀錄」。來源取得、claim ledger、
跨公司可比性、monitor、可信度與修正規則統一由 `MARKET_RESEARCH_METHOD.md` 定義。
正式公司事實仍由
`QUALITATIVE_RESEARCH_RUNBOOK.md` 的 evidence pack／獨立 reviewer 契約治理；
可證偽市場主張仍由 `LEADING_HYPOTHESES_PHASE2_RUNBOOK.md` 治理。本流程不改量化分數。

## 一個佇列，四種時鐘

```powershell
python scripts/research_queue.py --attention
python scripts/research_queue.py --calendar --weeks 8 --output tmp/research_calendar.md
python scripts/research_queue.py --lint
python scripts/research_radar.py --lint
python scripts/research_method_audit.py --lint --baseline-ref HEAD
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

跨市場候選另由 `notes/research_candidates/*.md` 的單一 active radar 管理，
`research_radar.py --lint` 會驗證排名、來源、下一個證據、反證條件，以及升格文章／圖譜是否
真的存在。雷達是研究資源排序，不併入個股分數，也不是投資建議。

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

### 候選雷達：優先級與知識價值分開

候選雷達的 `priority` 回答「現在要不要投入研究時間」；`knowledge_value` 回答「完成後能否
增加可重用的產業理解」。兩者不得混成一個看似精確的分數，也不得轉譯成股價方向。每個候選
至少保存兩份一手來源，並明列：

- `why_now`：時效、事件或證據成熟度。
- `knowledge_gain`：將補上的機制、產業鏈或比較框架。
- `first_rejection`：哪個觀察最先推翻研究必要性或核心假設。
- `next_evidence`／`next_check`：下一份要找的證據與期限。
- `route`：升格文章＋圖譜、併入既有研究，或只留觀察。

只有已通過 topic v3 claim ledger 與 knowledge graph evidence contract 的候選可標為
`promoted`；其餘候選即使知識價值高，也只保留 watch／expand 狀態。

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

2. 先用交易所／MOPS 與官方法說日曆，對**全 universe** 做前次掃描窗口以來的事件
   索引快掃；法說、季報、財報董事會等事件先逐檔升為 P1 triage，再依
   `LEADING_HYPOTHESES_PHASE2_RUNBOOK.md` 的來源分層，對該週 cohort、跨族群上游錨點、
   公司 IR、關鍵客戶／平台官方公告與重大政策做語意深掃。事件快掃不能被 30 檔 cohort
   或臨時指定名單取代。
3. 有新議題時複製 `notes/research_topics/_template.md`；沒有新議題也要在
   `scan_log.csv` 寫 `result_topic_ids=none`。scan log 採 append-only：每個掃描窗口新增穩定
   `scan_id`，不得改寫或刪除既有 row；紀錄錯誤時另加新 row，並在 `coverage_note` 明示
   `correction_of:<old_scan_id>`。
4. `scope=full` 只能在預定來源與完整時間窗真的都掃完時使用。只查當前日端點、主題式
   搜尋或缺歷史頁面時必須寫 `partial` 與 coverage limitation。
   對外發布「優先更新對象」前若尚未完成全 universe 事件快掃，標題與摘要必須明示
   「部分掃描」，不可讓指定股票名單被理解成全體優先排序。
5. 先完成 topic impact 與 evidence boundary，再選 route：
   - 公司一手文件且改變既有事實 → `formal_note_candidate`。
   - 市場流傳、可證偽但未被正式資料覆蓋 → `hypothesis_candidate`。
   - 跨族群上游正式事件 → `event_anchor_candidate`。
   - 尚未能映射公司 → `market_issue_watch`／`policy_watch`。
6. 更新 active candidate radar：保留連續排名、反證條件與下次查核日；若候選升格，先完成
   topic v3 與圖譜 lint，再填入 article／graph route。
7. 執行 `research_queue.py --lint` 與 `research_radar.py --lint`。topic 不能自動貼入正式
   筆記；正式更新仍需同一 evidence pack 離線重算與獨立 reviewer。
8. 回查所有到期 monitor，在 `notes/research_method_reviews/monitor_reviews.csv` 追加
   `new_support／new_contrary／no_new_evidence／not_yet_testable`。沒有新證據時不得延後
   topic evidence clock；registry 有變動就新增 method audit snapshot，不能改舊快照。

GitHub 的 `research-watch.yml` 會在台灣每週一 09:00，以及 `fetch-financials` 成功後，
把唯讀待辦寫入 Actions summary／artifact。它只提醒，不會替代語意掃描，也不會寫 main。

### 每月方法回顧

每月第一個研究週額外執行 `research_method_audit.py --json`，新增一份
`notes/research_method_reviews/YYYY-MM-DD_NN.json`。逐項看 gate，不合成健康分數：

- **可追溯性**：active claim 是否都有邊界、圖譜線是否能回查 exact claim／source。
- **獨立交叉驗證**：每篇 active topic 的主命題是否至少有兩條獨立來源鏈；逐一處理 audit
  列出的 topic ID，不能用整體覆蓋率掩蓋單篇缺口，也不能把兩條來源當成真實性分數。
- **可證偽性**：待驗證 claim 是否寫下一份證據，monitor 是否有 living watch source。
- **新鮮度**：逾期 topic／edge／monitor 數，不以「已重新看過」消除 stale。
- **修正學習**：到期 monitor 是否留下 review event，反方證據是否真的觸發新 claim 或修正。
- **掃描覆蓋問責**：scan log 是否納入方法指紋、是否存在 full scan、partial 與最新全域
  cadence 是否如實顯示；partial 不得冒充全市場覆蓋。歷史 scan row 是不可變事件，未建立
  scope lineage 前不把舊期限永久累加為逾期，也不宣稱個別 scope 已由後續掃描關閉。
- **校準可用性**：證據型 outcome 的樣本與覆蓋是否足以描述；不足就維持 `not_ready`。

若 gate 變差，先修 evidence／monitor／review 流程；不得因候選升格率好看就宣布方法有效，
也不得用一輪 `no_new_evidence` 當成主命題獲得支持。

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

每則議題必須保存來源發布日、研究捕捉日、review due、來源鏈、route 與證據邊界；
一般 topic 另須在 impact 保存受影響族群／股票、方向、`note_action` 與 action due。尚未完成適用性或公司暴露
映射的 `policy_watch` 可以沒有 impact，此時必須維持 warning／watch、不得路由正式筆記；
只有追加公司層級 impact evidence 後才可建立 impact 與正式 route。`candidate_source` 只表示
可作後續研究來源；`trigger_only` 連候選證據都不是。狀態轉移追加保存，不覆寫歷史。

### Topic schema v2 → v3

v2 是 2026-08-01 三篇研究先導入新手導讀的短暫過渡契約；原訂自 2026-08-02 起成為
新建 topic 的最低版本，但同日即由 v3 的持續驗證契約取代。2026-08-02 起新建 topic
一律使用 `schema_version: 3`。parser 對 cutover 前的 v1／v2 只保留歷史相容；舊格式
沒有結構化 ledger，應顯示為「未結構化驗證」，不可默認具有一般可信度。

live `notes/research_topics/` register 現已全數遷移，loader 只接受 v3；v1／v2 parser 僅供
歷史檔案的個別分析相容，不能把已登錄議題降版或用回填舊 `captured_at` 規避契約。

v3 繼承 v2 的新手導讀。第一個 H2 固定為「新手先讀：這篇在講什麼」，並依序包含五個 H3：

1. 「名詞小字典」至少 3 個 `- **術語**：白話解釋`。
2. 「三句話抓重點」恰好 3 個頂層 bullet。
3. 「為什麼重要」至少一段具體說明，不能只重複標題。
4. 「接下來怎麼追」至少 2 個可觀察節點。
5. 「想一想」至少 2 個以問號結尾、能幫助反證的問題。

另外，每篇 v3 必須具備：

1. meta 的 `thesis_claim_id`、`base_confidence`、`confidence_basis` 與
   `cross_company_numbers`。
2. 至少兩份可定位的 `research_source`，保存來源角色、發布／捕捉／接受日期、locator
   與 limitation；`verified` 只表示指定來源直接支持 claim 的精確措辭。
3. `research_claim` ledger，以 `verified／inference／unverified` 分開保存證實、推論與
   待驗證內容。主命題、公司映射與反方證據不可混在同一句。
4. 若使用跨公司數字形成判斷，逐一建立 `metric_comparison` observation，明列 entity、
   期間、單位、定義、來源及 `directly_comparable／normalized_comparable／not_comparable`
   裁決；「不可比」是有效結果。observation 採 append-only；新期間、重編數字或定義改變
   只能追加 observation，不能覆寫既有 ID。
5. 至少兩個 `monitoring_item`，各自保存 claim IDs、metric、基線 `source_ids`、未來重查的
   `watch_source_ids`、頻率、`next_check`、trigger 與 invalidation；每個 active monitor 的
   watch 至少包含一個 active `living_index`，topic 的 `review_due` 等於最早的 `next_check`。

`last_evidence_at` 不手填，而是取 active `thesis_claim_id` 引用之 active source 的
`accepted_at` 最大值；其他周邊 claim 的新證據不得刷新主命題。
active topic 以 runtime 當下的臺北日曆日（`Asia/Taipei`）判斷是否逾 `review_due`；不得用
UTC 日期、資料日或手填舊日期規避期限。沒有新 evidence 時，effective confidence 只自動
降一級；這是新鮮度處理，不會改 claim 的真假標籤、topic lifecycle 或 H# 狀態。已查但沒有
新證據時，只在 append-only scan log 留下範圍與結果，不可更新 source `accepted_at`、
`last_reviewed_at` 或把 `review_due` 往後推。

`last_reviewed_at`、延後 `review_due` 與調高 `base_confidence` 都需要新追加、被 active thesis
claim 引用且晚於原 thesis clock 的 evidence，並追加 transition；「重新看過但沒有新資料」
不能刷新 meta。`dismissed`／`resolved` 為關閉狀態，monitor 應退役、時鐘凍結。重開必須先
追加比關閉時更新的 source、active claim 與 active monitor，再以引用該新 source 的
`dismissed/resolved → triaged` transition 重開；不得覆寫原關閉紀錄。

新證據推翻或縮窄舊結論時採 append-only：保留舊 source／claim／transition ID，追加新
source 與新 claim。新 claim 以 `correction_kind: supersedes|refutes` 與
`corrects_claim_id` 指向上一代，舊 claim 以 `corrected_by_claim_id` 回指新 claim；
`resolution` 預設空白，只供存在 active contrary evidence 時的人工作法裁決。多代修正逐代
追加、只連相鄰 claim，不壓平中間版本；新 claim 的 `basis` 同時記
`correction_of:<old_claim_id>`，但不以此自由文字取代結構欄位。舊 monitor 標為 `retired`。只有第一筆
`initial → inbox` transition 可用 `evidence: source_chain:<meta.source_chain_id>`，其後一律用
`evidence: sources:S1,S2` 引用已登錄來源。詳細欄位、
來源角色、可信度及跨公司數字規則見 `MARKET_RESEARCH_METHOD.md`。

`research_queue.py --lint` 會檢查結構、引用與最低內容量；它不能替代來源核對或推論審查。
新手導讀要說清楚「已知／未知／下一步」，不可為了白話而刪除證據邊界。

特別注意：

- 平台商列名「生態系夥伴」不等於個別公司的新增訂單、營收、份額或毛利。
- 同業 HBM、先進封裝或液冷事件不等於本 universe 同族群每家公司受惠。
- 政策新聞在完成 HTS code、豁免、原產地、客戶／Incoterms 暴露前，不建立公司層級損益
  主張；`policy_watch` 可不建立 impact，但必須保留 warning，且不得路由或 promoted 到
  正式筆記。
- 敘事早於新 topic 只產生「review」提示；review 結果可以是無關、留在 watch，而不是
  必然改文。
