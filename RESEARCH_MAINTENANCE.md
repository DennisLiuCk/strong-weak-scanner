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
python -m unittest discover -s tests -q
```

最後一行不可省。lint 只驗當前 register 的結構與引用；契約測試另外綁了幾個必須隨每輪
發佈同步的常數（audit `as_of`、最新 `scan_id`、帳本累計數），只跑 lint 就 push，
CI 會在推上去之後才轉紅。詳見 `MARKET_RESEARCH_METHOD.md` 發布前檢查第 12 項。

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
真的存在。Schema 2 active radar 還必須指向 `selection_log.csv` 的研究前凍結 cycle；雷達是
研究資源排序，不併入個股分數，也不是投資建議。

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

Active radar 另必須提供純編輯／導覽層的 `reader_question`、`reader_starting_point`、
`reader_terms`、`reader_next_step`、`group_ids` 與 `reader_group_questions`：
第一項用一個問句說明「研究完成後要能回答什麼」；第二項固定寫成兩句、32–120 字，第一句只
摘要既有 `why_now` 已出現的線索，第二句以「目前還」明示尚缺的證據或不能跨過的推論邊界；
第三項只挑 2–4 個會擋住新手的關鍵詞；第四項把凍結的 `next_evidence` 縮成可執行的下一步。
`reader_starting_point` 不得新增來源未支持的事實，也不得把候選寫成已證實結論。
`group_ids` 只能列 1–4 個
`config/groups.csv` 既有正式族群，且必須能由同一候選已寫明的知識缺口、責任角色或升格文章
回查，不能為了增加按鈕而擴張成受惠名單。`reader_group_questions` 必須依 `group_ids` 順序，
為每個族群各寫一個白話問句，說清它在同一研究題中負責回答哪個問題；不得寫成上下游排名、
受惠方向或已證實公司連結。發布卡必須把 `reader_question` 當成卡片 heading，先標示「還沒回答
完整的問題」；原候選 `title` 只縮成次要的「研究題名」脈絡，不得把技術題名再放回第一閱讀層。
其後依序顯示 `reader_starting_point`、`reader_next_step`、`reader_terms` 與族群問句；族群問句
按鈕負責定位族群矩陣的本題文章、
族群基礎起點與研究缺口，矩陣保留同一問句、同步選取相同族群，並提供返回原候選的焦點路徑。
候選已升格且正式 article 可解析時，矩陣主要行動必須開同一 `candidate.articleId`，不得改開該族群
通用 `learningStart`；後者只能降為「再讀族群基礎」。候選未升格時必須明示本題尚無文章，不得由
族群或題名猜一篇替代。這個雷達承接區必須由 `renderMaturityOrigin()` 直接插入所選
`.maturity-reader-row`，並以 `grid-column: 1 / -1` 排在四個盤點 cell 之前；不得再塞進第一欄的
族群起點。寬桌面可分成問句／本題文章／行動三欄，中幅改成問句與文章兩欄、行動另列，窄幅依
DOM 順序單欄。未升格狀態只保留問句與返回行動，不得因共用三欄版而留下空白文章欄。開文再返回
時必須重建同一承接卡、選取族群並把焦點送回整列起點。完整
`why_now`、`next_evidence`、knowledge gain、第一拒絕與來源仍保留在預設關閉的查核區。
這六個欄位不能改寫 rank、priority、evidence posture、selection decision 或任何凍結值，
也不能新增文章、圖譜、公司曝險或投資結論。

發布頁的候選卡之前必須提供一個可收合的「候選題地圖」，完整枚舉同一 active radar 的全部
候選，不得挑題、重排或另寫摘要。每個入口只能逐字使用該候選既有 `rank`、`reader_question`、
由正式 status 固定翻譯出的讀者標籤與 `next_check`，並以 `aria-controls` 對到唯一候選卡；點擊後
須把同卡捲入畫面並以程式焦點公開位置；每張卡尾須能展開並聚焦同一地圖，讓讀者改選問題。
寬桌面四欄、中幅兩欄，780px 以下單欄且首次載入預設
收合；使用者展開或收合後，重繪不得覆寫本次選擇。地圖必須明示順序只安排研究資源，不代表
重要性、報酬、族群受惠或投資排名；不得改寫 radar、selection log、article、graph 或任何
研究判定 payload。

族群完整度摘要在寬度大於 1000px 時保留四欄同列比較；781–1000px 必須改成 2×2 grid、隱藏
遠處共用表頭，並在每個 `.maturity-reader-cell` 顯示自己的原欄名；780px 以下維持既有單欄
DOM 順序。這三種排版只能重排同一列的族群起點、已完成、最大缺口與下一步，不得改寫數字、
缺口或行動。`.maturity-origin-wide` 的寬度必須扣除自己的左右 margin，完整留在所選 row 內；
不得用 `width:100%` 再加外距，使雷達問句、文章標題或返回行動被 row 的 overflow 裁掉。

雷達頁首必須先說明「已有文章／等待更多證據／暫緩研究」各自對應的讀者行動，摘要數字只保留
待查問題數、可直接閱讀文章數與下次總檢查日。selection freeze、priority、selection decision、
knowledge value 與 evidence posture 都是研究團隊操作資料，必須收進方法或逐卡查核區，不得與
讀者狀態並排在首屏。候選卡正文必須使用整張卡的可用寬度；研究順序改以卡頂橫列顯示「研究順序 N」，同列逐字
說明「只排研究待辦，不是股票或投資排名」，不得再用獨立直欄把窄幅正文壓窄。卡面 status
只能做顯示翻譯：`promoted`、`expand_existing`、`watch`、`deferred` 分別顯示為「已有文章與
關係圖」、「補進既有研究」、「等待更多證據」、「暫緩研究」；原始 `candidate.statusLabel`、
status、rank 與 audit payload 均須保留。已升格文章行動用「閱讀這題的文章」描述讀者接下來
會做什麼，不在第一閱讀層暴露「升格」等維護流程術語。

已升格候選從雷達卡直接開文時，顯示層必須建立一次性 `radar` article origin，只保存正式
`candidateId`、雷達捲動位置與 window 位置。文章桌機頁首、行動版返回鈕與
「從這篇接著學」末端都要顯示雷達第 N 題與同一 `reader_question`，並明示 N 只是研究資源
安排，不是族群受惠、股價方向或投資排名。返回後必須恢復同一候選卡的位置並將鍵盤
焦點送回該卡。直接文章 deep link、一般文章清單與矩陣／圖譜入口不得假造雷達來處；
切到不是該候選正式 article 的其他文章時必須清除這個來處。這個狀態不得寫進 radar、article 或
knowledge graph payload。若先由雷達族群問句進矩陣，再開同一
候選的升格文章，則使用一次性 `maturity-radar` origin 保存 `candidateId`、正式 `groupId` 與同一
問句；文章首尾須同時顯示族群、雷達題次與問句，返回後重建 `maturityOrigin`、選取並聚焦原矩陣列。
矩陣的完成度、財務缺口與下一步必須明示為族群整體盤點，不得冒充該雷達問題的答案。換到其他
文章時同時清除 `maturity-radar` 與暫存 `maturityOrigin`；只有通用 `maturity-group`／
`maturity-route` 依原契約延續。

只有已通過 topic v3 claim ledger 與 knowledge graph evidence contract 的候選可標為
`promoted`；其餘候選即使知識價值高，也只保留 watch／expand 狀態。

候選進入深研前，先在 `notes/research_candidates/selection_log.csv` 追加同一 cycle 的完整
候選集合，並單獨 commit。凍結欄位包括初始 rank、priority、knowledge value、evidence
posture、`advance／watch／defer`、選擇理由、第一拒絕及下一份證據。這一步不是增加一個綜合
分數，而是讓後續能分辨：原本就選對了可研究問題、深研後被拒絕，或看到結果才事後調整排行。
初始欄位不得因文章結果回寫；研究後 route 只留在 active radar。

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
   索引快掃；法說、季報、財報董事會等事件先逐檔升為 P1 triage。季報窗口至少依序核對：
   - TWSE 與 TPEx 的重大訊息端點，以及當季損益表／資產負債表 OpenAPI；兩市場與完整
     日期窗均成功，才可把這一小段 scope 記為 `full`。
     先以唯讀、零 DB 寫入的 census 工具固定來源批次邊界，例如：

     ```powershell
     python scripts/research_event_scan.py --window-start 2026-08-06 --window-end 2026-08-07 --quarter-year 115 --quarter 2 --output tmp/research_event_scan.json
     ```

     工具以兩市場重大訊息的 `出表日期／Date - 1 日` 作保守 coverage-through，並自
     2026-08-08 起**另要求該批次實際觀測到的發言日期落在請求窗口內**；重大訊息日端點
     只保留單一出表日期批次（實測全部列的發言日期僅有出表日期減一那一天），批次滾過
     窗口後舊發言日永久消失，只靠日期算術會把「批次完全不含窗內任何一天」誤標成
     `full`。批次已滾過窗口時一律維持 `partial`，缺口只能沿用當時真的讀到該日的既有
     scan row，不得由後來的重跑追認。任一市場
     尚未到 window end 就輸出 `partial`。只有在準備讓不完整窗口硬失敗時才加
     `--require-full`。輸出的 `universeN`、公告列與兩表交集是母體 census，不是推論樣本；
     JSON 仍只是 trigger index，不能替代附件與內容驗證。
   - OpenAPI 命中的每家公司都再查 MOPS `t57sb01` 直接文件索引；公司 IR 活頁可能落後，
     未查直接索引前不得寫「完整附件尚未定位」。
     對優先名單使用唯讀工具留下可重跑的檔名／時間／大小清單，例如：

     ```powershell
     python scripts/research_filing_index.py --stock-ids 2308,2337 --year 115 --season 2 --checked-at 2026-08-05 --output tmp/research_filing_index.json
     ```

     工具遇到連線或解析錯誤會標紅，不會把取檔失敗誤記為 `NO_FILE`；輸出的 `found` 仍只
     是索引存在，不是內容已驗證。
   - OpenAPI 數值列只是一個申報 trigger，不證明完整 PDF、會計師核閱報告或附註已取得；
     MOPS 檔名／時間／大小也只證明附件存在，不得刷新 evidence clock 或替代 evidence pack。

   完成事件索引後，再依
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
6. 先把本輪候選寫入 append-only selection log 並獨立 commit，再開始深研；完成後更新
   schema 2 active radar，保留凍結的連續排名、第一拒絕與下一份證據，只新增研究後 route。
   若候選升格，先完成 topic v3 與圖譜 lint，再填入 article／graph route。
7. 執行 `research_queue.py --lint` 與 `research_radar.py --lint`，並在 push 前補跑
   `python -m unittest discover -s tests -q`（lint 全過不等於測試會過）。topic 不能
   自動貼入正式筆記；正式更新仍需同一 evidence pack 離線重算與獨立 reviewer。
8. 回查所有到期 monitor，在 `notes/research_method_reviews/monitor_reviews.csv` 追加
   `new_support／new_contrary／no_new_evidence／not_yet_testable`。沒有新證據時不得延後
   topic evidence clock；registry 有變動就新增 method audit snapshot，不能改舊快照。

GitHub 的 `research-watch.yml` 會在台灣每週一 09:00，以及 `fetch-financials` 成功後，
把唯讀待辦寫入 Actions summary／artifact。它只提醒，不會替代語意掃描，也不會寫 main。

### 每月方法回顧

每月第一個研究週額外執行 `research_method_audit.py --json`，新增一份
`notes/research_method_reviews/YYYY-MM-DD_NN.json`。逐項看 gate，不合成健康分數：

- **選題前承諾**：所有 schema 2 radar（含 retired）是否都有同 cycle 的研究前凍結，且
  初始排名、第一拒絕與下一份證據未被改寫；未到期重選在 cutover 後是否留下新來源
  `early_trigger`。通過不代表選題有效；單輪 advance／promoted 比例不報命中率。
- **可追溯性**：active claim 是否都有邊界、圖譜線是否能回查 exact claim／source。
- **財務材料性 v2**：每筆 assessment 是否有期間、分子、分母、定義、exact source 與
  歸因邊界；`company_total` 是否維持 `not_disclosed`，`bounded_proxy` 是否沒有被升為
  題材財務貢獻。通過只代表口徑可稽核，不代表公司題材重要或投資有效。
- **獨立交叉驗證**：每篇 active topic 的主命題是否至少有兩條獨立來源鏈；逐一處理 audit
  列出的 topic ID，不能用整體覆蓋率掩蓋單篇缺口，也不能把兩條來源當成真實性分數。
- **可證偽性**：待驗證 claim 是否寫下一份證據，monitor 是否有 living watch source。
- **新鮮度**：逾期 topic／edge／monitor 數，不以「已重新看過」消除 stale。
- **修正學習**：到期 monitor 是否留下 review event，反方證據是否真的觸發新 claim 或修正。
- **掃描覆蓋問責**：scan log 是否納入方法指紋、是否存在 full scan、partial 與最新全域
  cadence 是否如實顯示；partial 不得冒充全市場覆蓋。歷史 scan row 是不可變事件，未建立
  scope lineage 前不把舊期限永久累加為逾期，也不宣稱個別 scope 已由後續掃描關閉。
- **校準可用性**：證據型 outcome 的樣本與覆蓋是否足以分列結果 counts；不足就維持
  `not_ready`。即使足夠也不計支持率，因現有 outcome 尚未編碼主命題真假。

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

上述五個 H3 的順序是 Markdown 與 lint 的寫作契約；研究中心的讀者畫面會把相同 blocks
重排為「三句話抓重點 → 為什麼重要 → 名詞小字典 → 接下來怎麼追 → 想一想」，其中完整
名詞小字典以原生 `details` 預設收合並標示詞數，讓讀者先抓主線、追蹤節點與反證問題，遇到
陌生詞時再展開。文章捲過原字典後，發布頁另提供「名詞速查」：桌機入口位於 sticky 大綱，
窄幅入口固定於左下且只在原字典離開閱讀區後出現。速查的詞數、搜尋索引與顯示內容必須直接從
同一個「名詞小字典」list runs 取得，不得另外維護第二份術語表或生成新解釋；原生 dialog 開啟
與關閉都不得移動正文位置，關閉後焦點須回到原觸發按鈕。沒有名詞小字典的事件或舊制文章不得
顯示空速查入口。一般正文節另以該節 heading、段落、清單與 table 文字比對同篇字典的粗體詞名；
只有真正命中的詞可出現在節首「本節先認得」，按鈕只把同一原生 dialog 預填為該詞並顯示原始
list runs。新手段落已有完整字典、研究摘要已有白話卡、研究查核附錄保留專業用途，三者都不重複
插入節首詞鈕。沒有命中時不顯示空容器，不得用相似度、模型或另一份詞表補詞。畫面不刪除或
改寫任何 block。同節確定性命中達 9 個以上時，節首只先顯示原字典順序前 6 個，剩餘詞鈕放入
可由鍵盤操作的原生 `details`，並明示順序不代表重要性；展開後仍須保留全部命中詞、完整詞名、
同一 dialog 與原始定義，不得因漸進揭露刪詞、重新排序或另寫解釋。8 個以下維持全部直接顯示。

市場議題主正文的章節交接由 `topicReaderSectionItems()` 先依原始 `article.sections` 順序排除
「新手先讀：這篇在講什麼」、三種 analyst heading 與非事件文章的查核附錄；
`readerSectionHandoff()` 只在所得清單的第二節起，於原 H2 前顯示「章節接力」、目前站次與
上一節逐字 heading。第一節、單節文章、正式筆記與多空小作文不得顯示。卡片不得讀 blocks、
題名、族群、graph 或 route 推寫摘要，也不得把相鄰章節解讀成上下游、因果、成熟度或投資排序；
原 heading、blocks、順序與研究 payload 必須完全不變。每篇有 `n` 個主正文節時，接力卡必須
恰為 `max(0, n-1)` 張，且每張的 previous／current heading 都須與相鄰原 H2 完全相同。

第一個主正文節另由 `readerMainQuestionAnchor()` 逐字讀取既有 `catalogReaderQuestion(article)`；
只有 `type=topic`、非 `eventKind`、確實有主正文且目前 section 是
`topicReaderSectionItems(article)` 第一項時，才可在原 H2 前顯示一次「回到這篇要回答的問題」。
其 `data-main-question-text` 必須逐字等於首屏 H1／文章清單「讀完能回答」，
`data-main-question-section` 必須逐字等於所在第一個主正文 H2。事件錨點、沒有主正文、第二節以後、
正式筆記、多空小作文及非 reader mode 都不得顯示。不得讀取 blocks、題名、族群、graph 或 route
另寫問題；卡片只作閱讀定位，不改寫正文、研究結論、證據或查核狀態。

同一組主正文節另可由 `readerArticleFrameItems()` 依原 section 順序檢查各節第一張 table 的
第一個欄名；只接受「本文 N 個位置／本文 N 把尺／本文 N 個時鐘／本文 N 類角色／本文 N 關」
五種完整格式，且至少命中三種、kind 彼此不重複時，`readerArticleFrameMap()` 才可在原主正文前
顯示文章級「正文怎麼走」。畫面 label、順序與定位目標須逐一對應原 table header／section H2；
固定 purpose 只能解釋「拆系統／核對條件／分開事件／分清責任／檢查缺口」五種閱讀工作，不得
讀取 row、cell、其他 blocks、題名、族群、graph 或 route 生成摘要。事件錨點、正式筆記、多空
小作文、少於三種或重複 kind 必須完全不顯示；手機採單欄且每個按鈕維持可觸控、可聚焦。
這是 renderer-only 導覽，必須明示順序不代表上下游、因果、成熟度或投資排序，並保持 Markdown、
原表、原 H2、主張、來源、查核狀態與 canonical research payload 不變。

市場議題主正文若一節從第一個 block 起連續出現至少三個 paragraph，且每段第一個非空 run 都有
作者明寫的 bold，`readerSectionMapItems()` 才可逐 run 建立「本節先看」。遇到非 paragraph 或
第一個非空 run 不是 bold 就立即停止，累積少於三項時回傳空清單；不得跳過中間 block 拼湊、讀取
後文摘要，或替沒有粗體主句的段落生成文字。卡片置於同節名詞提示與完整 blocks 之前，label 必須
逐字重用原 bold run，原段落、連結、順序與來源仍完整渲染。`ol` 保留原文順序語意，視覺編號須對
輔具隱藏，並明示編號不代表重要性、上下游或因果關係。這項提示只可出現在 `mode=reader` 的
`type=topic` 非查核附錄；新手導讀、研究摘要、正式筆記、多空小作文與其他 mode 都不得插入。
section 容器不超過 480px 時，標題、說明與步驟須改為單欄且不得造成水平溢出。

市場議題一般正文內的 table 在 `mode=reader` 且非查核附錄時，必須先由
`readerTableGuide()` 讀取同一個 `table.head`；至少兩個非空欄名才顯示帶 `aria-label="表格閱讀順序"`
的 `aside` 與有序步驟。兩欄表只提示左欄、右欄；三欄以上固定提示最左欄、中間欄與最右欄，
其中中間標題只能依原順序串接既有欄名。一般表格不得讀 `table.rows` 或 cell 內容生成摘要；唯一
例外是最左欄名含「位置／環節／節點／路徑」、row 數為 3–8、第一格皆非空且不重複的系統表，
`readerTableSystemPositions()` 可逐字讀取每列 `row[0]`，用同一區塊改顯示「系統位置索引」。索引
只能列第一格原文與表內順序，不得讀其餘 cell、改寫名稱或暗示每套系統必然依序包含全部位置；
畫面必須明示編號不代表上下游、流程一定相連、重要性或受惠排序。不符合上述確定性條件時安全
退回欄名導讀。兩種提示都只安排閱讀順序，不改寫表格內容、數字或證據邊界；寬欄可並排，section
容器不足 620px 與 viewport 不足 780px 都須改成單欄。查核附錄、正式筆記、多空小作文與非
reader mode 不得插入這層提示。

市場議題一般正文內的 table 另有窄欄閱讀契約：每個 `th` 必須保留原文並以
`scope="col"` 成為欄標題，一般表格每個 `td` 的窄欄視覺標籤只能逐字取自同欄 `th`。唯一例外是
已通過上述 `readerTableSystemPositions()` 條件的系統表：第一欄卡片標籤須依原 row 順序顯示
`位置 N／總數`，把前一個索引編號帶入逐列閱讀；同格仍須以 `data-reader-original-label` 保留原欄名、
插入實際文字節點供視覺與輔具共同讀取，並完整渲染原 cell；不得同時保留 CSS generated label
造成重複朗讀。其餘欄位仍逐字顯示原 `th`，一般表格不得取得位置標籤。當實際文章 section 容器
不足 620px 時，表格按 row 改排為卡片並同時顯示上述標籤；不能只看 viewport，因為桌機
master-detail 的正文欄也可能比手機窄。容器足夠時仍用原生 table；查核附錄不套卡片，真的溢出
才加上可聚焦 region 與水平捲動提示。兩種版型都不得刪欄、摘要 cell、調換 row，或把最右側
成熟度／證據邊界藏成預設不可見資訊。

列入白話升級批次的系統型 table，欄名應改成讀者能逐列回答的短問法，例如「目前看到什麼做法」
與「證據走到哪一步」，避免「目前看到的材料與元件做法」這類名詞堆疊。cell 優先使用明確主詞與
動詞，並把「已公開／尚待資格驗證／尚未量產」等成熟階段寫成完整句；不得因此省略材料、元件、
客戶階段或反證邊界，也不得把 reference design 改寫成量產。這是正文 editorial revision，仍須
追加同狀態 `editorial:<slug>` transition，並由 baseline lint 證明所有鎖定帳本與 meta 不變。

市場議題的清單卡與文章頁首必須先顯示 `config/research_topic_guide.csv` 中人工複核的
`reader_question`，原始 `title`／`readerTitle` 完整保留為次要的「研究題名」。導覽表只接受
18–56 字、以全形問號結尾且不含英文字母或反引號的中文問題，並須與所有發布中的 `type=topic`
文章精確一對一覆蓋；缺漏、重複或多出未發布 ID 時 dashboard build 必須失敗。這個欄位只進
讀者 payload 與搜尋索引，不得回寫 topic Markdown、替換下方閱讀任務、改變 claim／source／
confidence／group／route，或被當成新的研究主張。

整份研究文章清單另有問題先讀契約：`catalogReaderQuestion()` 對 topic 只讀上述
`readerQuestion`，對正式筆記與多空小作文只讀已通過來源契約的 `readingMission.question`；
沒有既有問題時退回原清單格式，不得從 `title`、正文、搜尋字或公司題材生成替代問句。問題是卡片
第一閱讀層；多空 `title` 與市場議題題名分別保留為「待驗命題／研究題名」。正式筆記則先把
`title` 與首個既有重點移除 `[S#]`、空白及標點後比較：任一方完整包含另一方時不重複顯示，只有
兩者確實不同才保留「原始摘要」。原公司、日期、查核狀態與閱讀時間必須保留。這只是 renderer
排序，不得新增 `catalogQuestion` 到 article payload，也不得改寫 `title` 或 `readingMission`。
卡片 DOM 與視覺順序都必須先渲染問句，再渲染同篇既有重點；三類重點標籤分別為「先認識公司／
先看要驗證的說法／先知道一件事」，不能讓摘要、技術題名或研究流程術語回到問題之前。卡尾以
「目前怎麼看」保留既有查核狀態、可信度與有效來源數。文章側欄與窄幅文末的研究營運欄位必須
放進預設收合的原生 `details／summary`「文章查核資料」；`topicStatus` 只做讀者翻譯，priority
必須明示只排研究工作、不代表文章重要性、預期報酬或投資順位。展開後原始狀態、日期、可信度、
來源及原始文件連結仍須完整可回查；不得因此改寫 payload、topic lifecycle 或 evidence clock。

文章頁首必須與同張清單卡共用 `catalogReaderQuestion()`，不得為正式筆記、多空文章或 topic
另取一份問題。三類都有既有問題時，頁首一律先顯示「這篇先弄懂」與同一問句；topic 原
`readerTitle` 標為「研究題名」，正式筆記／多空文章原 `readerTitle` 標為「原研究頁名」。沒有
既有問題時才退回原 `h1`，不得由 renderer 生成替代問句；`readerTitle`、Markdown、section、
reading mission 與 payload 都不能因頁首重排而改寫。

標題與查核警語後另顯示一張
「新手閱讀任務」：`build_dashboard.py` 只擷取「三句話抓重點」前三句、「為什麼重要」開頭的
完整句子與「想一想」第一題。頁首先逐字使用第一句重點與第一題，分別標成「先抓住這個重點」與
「讀完能回答」；較長的「為什麼重要」開場放進預設收合的原生 `details／summary`，標成
「為什麼值得讀」。三處都不得自行重寫、摘要或補入新主張；第一句不存在時才可退回既有
orientation，不能生成替代文案。
任務卡的 DOM 閱讀順序必須先放標題、兩個任務句與主行動，再放可選的符號解碼、名詞說明與
「為什麼值得讀」，最後才顯示來源邊界。桌機視覺順序維持兩句並排後接主行動；780px 以下可用
`display: contents` 將第一句、主行動、完整「讀完能回答」反思題依序排開，讓 44px 起讀按鈕不被
長問題推離首屏。反思題只可移到行動後方，不得隱藏、截斷或改寫；輔助說明仍不得插到主行動前。
這個 responsive 排序只作用於 renderer，不得改動 `readingMission`、原句、來源或 action target。
正式筆記與多空小作文另使用同一張讀者卡，但來源契約不同：正式筆記只取既有「30 秒摘要」
前 1～3 個 list item，多空小作文只取既有「多空觀點（小作文）」之「勝負手」前 3 個 list item；
任一發布中的正式筆記或多空小作文缺少對應來源時建置直接失敗。兩類「讀完能回答」只由文章
類型與既有 `subject` 套用固定讀法問題，不讀正文、題名或關鍵字，也不宣稱哪一方正確。事件錨點
沒有上述結構時不生成任務卡，不得從長段落抽句或用模型補寫。
市場議題頁首兩句須各自共用「三句話抓重點」的 `beginnerKeyPointMatches` 確定性比對：先找同篇
「名詞小字典」，只有未被本文定義涵蓋的研究流程／常見指標才可補
`config/research_reader_terms.csv`；合併後以來源與完整詞名去重。至少命中一詞時，才在兩句
之後、「為什麼值得讀」之前插入預設收合的「先認得這兩句的 N 個詞」，並共用逐字定義 list 與
來源／判讀邊界；完全沒有命中時不得顯示空容器。這個入口只把同一解釋提前，完整字典與下方逐句
提示仍保留，不得另造定義或改變文章 hash。
閱讀任務另可由 `_research_reading_mission_notations()` 對既有兩句做確定性符號解析：`[S#]`
來源索引、只在多空文章出現的裸 `H#` 假說編號、`Q1–Q4／YYYYQ#` 季度、`YYYYH1／H2`
半年、MOPS，以及不會與一般英文混淆的 `Universe／serverodm／semiequip／packtest／ipdesign／
powersupply` 分類名稱。每個 `readerNotations` 項目必須保留實際 token、固定 `kind`、白話
`label／definition／boundary`，依首次出現位置排序；不得讀題名、推測縮寫或由模型生成。
顯示層用原生 `details／summary` 預設收合，Enter 與 Space 都可切換，摘要與主行動至少 44px；
完全沒有符號時不得顯示空容器。正式筆記首屏另允許把首個重點的 `[S#]` 來源編號移到同卡獨立
「原文來源標記」提示列，並在正文與來源區明示完整保留；內部分類 ID 已換成中文時，不得再顯示
一個指向不可見 token 的 `internal_taxonomy` 解碼項。這只改可見 DOM，不得回寫原句、來源編號、
主張、證據或 payload。任務重點達 80 字時可在既有 `；。！？` 後加入 `aria-hidden` 的零文字視覺
停頓，仍須維持同一段落、原字序與可複製全文。
所有被登錄為學習路線主文章的文章都必須能產生這張卡，缺任一來源段落時 dashboard build
直接失敗，不能讓族群起點退回只有術語與查核資訊的首屏。
市場議題若同時有至少兩句「三句話抓重點」與一項「接下來怎麼追」，
`_research_reader_boundary_brief()` 必須再建立純發布用的 `readerBoundaryBrief`：`known` 逐字取
第一句、`unknown` 逐字取最後一句、`next` 逐字取第一個追蹤動作。頁首結論卡依序顯示
「先知道／先別下結論／接著怎麼查」，讓新手先讀同篇已寫好的白話內容；下方研究摘要仍完整保留
ledger 產生的「一句話結論／尚未知道／下一步看什麼」，不得被白話卡取代或回寫。來源不完整的
事件文章安全退回原摘要，不從長文、題名、搜尋字或模型補句。這四個 payload 欄位只屬 reader-only
導覽，不得進 claim、source、confidence、monitor、topic fingerprint、圖譜或公司曝險。
一般桌機在 1181–1500px 且未開啟專注閱讀時，master-detail 的實際正文欄仍可能只有約 365px，
因此三張結論卡固定改為單欄；`≤1180px` 沿既有窄幅規則單欄，寬版專注閱讀才保留三欄比較。
閱讀任務的主行動依文章結構分流。市場議題仍顯示「開始讀三句重點」，直接定位同篇「新手先讀」
的「三句話抓重點」。正式筆記與多空小作文只要至少一個正式族群能對回非空 `readerRole／
readerBoundary`，首個行動一律顯示「先看產業角色」並定位 `.article-role-context h2`；角色卡底部
再逐字把既有 `startLabel` 的「開始」換成「接著」，顯示「接著讀 30 秒摘要／接著讀多空觀點」，
分別定位「30 秒摘要」與整個「多空觀點（小作文）」而不跳過兩邊敘事。沒有可用族群指南時，
首個行動安全退回原來源段落，不顯示空的第二步。兩次定位都須同步移動鍵盤焦點；手機讓 heading
停在黏性導覽下方約 120px，桌機則在 `readerScroll` 頂端下方約 76px，且不得改變文章 hash。
正文後「回看本篇三句重點／30 秒摘要／勝負手」仍共用來源定位函式；多空文章回看時定位
「勝負手」。市場議題 DOM 閱讀順序固定為「閱讀任務 →
完整新手三句重點 → 產業角色 → 學習路線定位 → metadata →
其餘新手原文（重要性、字典、追蹤、想一想）→ 窄幅閱讀位置／大綱 → 研究摘要」。三句卡與產業角色之間
不得插入 metadata 或其餘新手段落；前後兩張新手卡只切分版面，原始文字、runs 與大綱索引仍屬
同一個「新手先讀」section，不得複製或改寫。主行動旁須明示三句重點後仍可比較族群角色與學習
階段。780px 以下保留唯一的黏性返回鈕，並隱藏桌機版完整 `article-learning-origin`；若本次確有
`articleOriginContext()`，返回鈕下方另顯示不含第二個返回動作的 `mobile-origin-context`，其文字
只能逐字重用同一 `context.title`，不得另寫研究摘要。341–780px 預設展開，340px 以下預設收合成
至少 44px 的原生 `details` 摘要，但完整起點仍須在同一 summary 內並可一次展開；直接 deep link
與一般清單入口不得顯示。手機開文時隱藏重複的文章類型 tabs，以換回首屏高度；黏性返回、原題、
文章問題、查核警語、第一句任務重點與 44px 主行動仍須同屏可達。桌機繼續顯示完整起點卡，文章
末端也保留返回起點動作。

`≤1180px` 隱藏桌機側欄大綱後，必須在上述固定位置渲染原生 `details` 的黏性「閱讀位置」。
節數與標題只能取自 `articleOutlineSections()` 的既有 section、既有「從這篇接著學」與實際存在的
研究查核附錄；不得依正文生成摘要、改寫標題或把進度當成研究完成度。收合摘要持續顯示
「第 N/M 節」與目前原標題，並以 `progressbar` 的 `aria-valuenow／min／max` 同步；展開後同一組
按鈕須保留 44px 觸控高度、`aria-current="location"` 與可直接跳節。手機三層黏性區
（topbar 58px、返回鍵 44px、閱讀位置 52px）下的 section、延伸學習與附錄錨點均須保留
約 160px scroll margin；寬幅右側大綱仍共用相同 scroll-spy。

同一個 `≤1180px` 契約也適用專注閱讀：較高權重的 `body.focus-mode .reader-inner` 不得繼續保留
已隱藏大綱的 240px grid track。窄幅專注閱讀須改為單欄、`max-width:720px` 並置中；此規則必須
排在寬幅專注閱讀的 `1180px + 240px` 雙欄規則之後。驗收時量正文寬度與左右外距，不能只確認
`.outline{display:none}`。

正文的讀者顯示層可正規化 Markdown 實體換行留下的空白，但只限可機械判定的中文排版邊界：
中文標點前後、中文開括號後，以及兩個漢字之間。含漢字的 run 中，半形 `,;:` 若不是連接兩個
英文字母、兩個數字或網址／時間語法，才可轉成 `，；：`；英文詞列、數字、run 邊界、連結與粗體
語意必須保留，原始 Markdown 與 payload 不得回寫。`mode=reader` 的正式筆記與多空小作文主正文
沿用「正規化後至少 120 字、至少兩個 `。！？`」；市場議題的一般主正文使用較細的 deterministic
profile：至少兩個句末且達 100 字，或至少三個句末且達 80 字。符合任一契約時才可在句末插入
`aria-hidden` 的零文字停頓；只要實際 `.article-section` 容器不超過 860px 就須顯示，不能只以
整體 viewport 判斷。`≤1180px` viewport 用 0.55em，較寬視窗中仍不超過 860px 的專注閱讀欄用
0.45em；段落仍須維持同一個 `<p>`、原字順序與可複製全文。門檻是版面契約，不是內容品質分數，
也不得據此生成摘要或改寫句子。查核附錄、研究摘要與新手三句重點不套用長段落斷句，避免改變
證據表與既有卡片結構；市場議題 profile 也不得套到正式筆記或多空小作文。

市場議題主正文若精確命中 fenced `text` paragraph，且 fence 內有 3–8 個由 `→` 分隔的非空項目，
reader mode 可把 fence 與箭頭視為 Markdown 呈現語法，依原順序改用單一語意化 `<ol>`。每個 `<li>`
必須逐字等於原項目，並保留可辨識的總步數與位置；原始 paragraph、runs、Markdown 與研究 payload
都不得回寫。非市場議題、非 reader mode、其他語言 fence、沒有箭頭或項目數超出範圍時必須安全
退回原 renderer，不能由技術文字、清單或模型自行推導流程與因果。

市場議題主正文若精確命中四項 `ul`，且四個首段粗體標籤依序為「主要驅動 KPI、次要 KPI、
常見假訊號、最關鍵分歧」，每項剩餘 runs 又以全形冒號開頭，reader mode 可改用單一
`section[aria-label="投資判讀四個位置"]` 與語意化 `<dl>` 顯示。固定提示只負責翻譯四個原標籤的
閱讀角色：先看核心條件、再看營運結果、避開假訊號、分辨關鍵路徑；不得加入公司、產業、數字、
方向或結論。每個 `<dd>` 必須逐字保留冒號後的原 runs，位置 1–4 與原順序一致；原始清單、
Markdown 與研究 payload 不得回寫。非市場議題、非 reader mode、標籤或順序不符、不是四項，或
冒號契約不符時一律退回一般清單，不能用相似詞或正文語意猜測。

正式筆記與多空小作文的 `mode=reader` 另有 section heading 白話契約：每個非空原始 `section.h`
都必須由 `readerSectionPurpose()` 產生非空的固定閱讀目的，緊接原 `h2` 顯示為
「這節先看」。正式筆記先用 canonical heading map，再用「證據索引／營運獲利／融資資本／假說」
等可判定字樣收斂，最後以不帶公司結論的固定句兜底；多空文章只分研究定位、多空觀點、量化背景、
`H#` 假說與固定兜底。提示須保留 `aria-label="本節閱讀目的"` 與原 heading 的 data attribute，
只存在顯示層，不得新增 `readerPurpose` 到 section、改寫 Markdown／payload 或拿正文生成摘要。
市場議題已有新手段落與研究摘要，`readerSectionPurpose()` 對其必須回傳空字串，避免同一目的重複。

正式筆記 `mode=reader` 另允許一組狹窄、可重現的分類與維運語翻譯。`passive／powersupply／
serverodm／semiequip／packtest／ipdesign` 只有在 ID 同時存在於該篇 `article.groups` 時，才可在
清單首個重點、閱讀任務與正文的可見文字換成 `groupById` 正式中文標籤；不得讀題名、相似度或
正文語意猜測其他分類。`power／memory／material` 等可能是正常技術英文的 ID 仍只在逐字命中
`族群：<本文 article.groups ID>` 前綴時顯示為「本文族群：<正式中文標籤>」，不得全域替換。
逐字命中的 `Universe 質化參考`、
`查核狀態以 meta 與 qual_notes.py --lint 為準`、`last_updated` 分別顯示為
「研究中心的公司質化參考」、「查核狀態請以文章上方標示為準」、「更新日期」。轉換函式只能經
`runs(..., textTransform)` 建立可見文字，不得寫回 `run.s`、`article.sections`、Markdown 或 payload；
非正式筆記、沒有正式 label／article group 的 ID，以及不完全符合上述字串的正文一律原樣保留。

「三句話抓重點」在發布頁以有序逐句卡片呈現；卡片順序、粗體與連結必須逐 run 保留，文字不得
因版型改變而摘要或改寫。唯一的讀者層例外，是把 `passive`、`powersupply`、`serverodm` 等不會
被誤認為一般技術英文的內部族群 ID，以正式 `group_names` 中文標籤替換；只改可見 run 的 `s` 與
heading，不改 link、source file 或 machine-readable metadata。
市場議題只有在既有清單恰好三句時，才依原順序附上「第 1 句 · 先看資料／第 2 句 · 再補脈絡／
第 3 句 · 最後看邊界」與 `evidence／context／boundary` 讀法角色；這些標籤只教讀者依序找資料、
脈絡與限制，不宣稱每句的證據等級，也不得重排或改寫 runs。其他文章類型與非三句結構維持
「重點 N」，避免把顯示層讀法誤當成來源語意。
每句先用該句文字比對同篇「名詞小字典」的既有粗體詞名，匹配規則須與正文「本節先認得」共用；
展開內容逐字使用同一筆字典 runs。同篇未涵蓋的跨文章研究
流程與常見指標，才可再用 `config/research_reader_terms.csv` 的顯式 aliases 比對；這份共通語
只能收 BOM、qualification、production、TAM、ASP 這類可跨產業維持同一字面邊界的詞，不得收
公司名、產品名、產業技術縮寫或用模型自動擴詞。同一概念若已命中本文字典，本文定義優先且不得
再顯示共通語。每筆展開內容必須標示「本文名詞」或「研究中心共通語」；共通語的 definition 與
boundary 都由 CSV 逐字發布，只是閱讀輔助，不得改寫文章主張、證據、成熟度或結論，也不進正文
「本節先認得」與名詞速查。沒有任何命中的句子保持只有原文，不顯示空容器。提示使用原生
`details`／`summary`，手機 summary 觸控高度至少 44px；收合與展開都不得改變文章 hash 或
正文位置。完整字典仍保留在原段落，供讀者一次查看整篇詞彙。

研究中心的讀者 payload 不得直接顯示 `passive`、`powersupply`、`serverodm` 等內部正式族群 ID；
原始 topic 帳本與 `group_ids`、`group_id` 等 machine-readable 欄位仍保留登錄值，發布建置只對
可見文字套用上述明確白名單。畫面中的三句重點、追蹤項目、主張與監測文字因此使用「被動元件」、
「電源供應」、「伺服器組裝／機構」等正式中文族群名稱；`power`、`memory`、`material` 等也可能是
正常技術英文的字串不得自動替換。正式筆記依上一段契約只翻譯該篇已登錄的不透明 ID；其餘 ID
仍只有固定 `族群：<ID>` 前綴可換。三組固定維運語也只在可見文字轉成上述讀者用語；其他文章
類型與任何 payload 欄位不得套用。

發布頁另由 v3 register 自動合成「研究摘要：已知、未知與下一步」；頁首閱讀任務後先呈現
「新手先讀：這篇在講什麼」的三句主線，立即建立產業角色與學習路線位置，再回到同一新手段落的
重要性、名詞、追蹤與反證問題，最後核對「一句話結論、目前已知、尚未知道、對哪些族群有意義、
下一步看什麼」。摘要必須
直接重用 `thesis_claim_id`、主命題來源鏈、active `unverified` claim、impact 與最早 monitor，
不得靠另一段人工摘要提升語氣。讀者畫面只在上述五個標籤完整且各自唯一時，將同一份 list
重排為一張結論主卡與四張驗證卡；卡片標籤與內文都逐字取自 generated blocks，缺標籤、重複或
順序契約不完整時退回一般清單，不能猜測分組。發布時把主張、impact、comparison、monitor 完整控制表，
以及選題原因、來源、研究判定等維運段落收進預設關閉的「研究查核附錄」；一般讀者先讀
結論與機制，需要逐項核對時再展開，原始資料與證據層級都不刪除、不改寫。

同一份五項摘要若標籤完整、各自唯一且可按固定順序解析，讀者畫面須在閱讀任務後、技術細節前
另顯示「先看結論邊界」。這張卡只逐 run 重用「一句話結論、尚未知道、下一步看什麼」，並以
`thesis_claim_id` 的 active claim label 與 `liveConfidence(article)` 顯示兩把尺；不得從正文
改寫、截短或補推論。主要行動把鍵盤焦點送到原「研究摘要：已知、未知與下一步」標題，次要行動
只在同篇已有名詞小字典時開啟既有原生 dialog。缺任一摘要欄、重複標籤、非 topic 或沒有字典時，
對應卡片／行動必須安全消失；完整五項摘要仍留在原位置，payload、Markdown 與查核狀態都不變。

研究摘要導言後的「新手證據讀法」必須把 `thesis_claim_id` 的 active claim label 與 topic
effective confidence 分成兩把尺。claim copy 固定依正式 `verified／inference／unverified`
值域解釋：`verified` 只表示指定來源直接支持精確措辭，`inference` 表示研究判讀由已接受資料
連接而成，`unverified` 仍不能當成已發生事實；不得自行提高或降低 label。可信度 copy 只說明它
衡量來源品質、獨立鏈、反方證據與主要缺口，不得寫成真假或發生機率。來源數只計 active thesis
實際引用的 active supporting sources；獨立鏈沿用同一批來源的 `independence_group`，不得拿全文
來源總數灌大。前端必須用 `liveConfidence(article)` 顯示 effective confidence，使臺北日曆日
跨過 `review_due` 時和卡片、可信度 panel 同步降級；降級仍不代表主張被推翻。整段是讀法輔助，
不得換算成公司訂單、受惠程度、投資排名或修改原始 topic 帳本。

族群矩陣頁首先用「把一個產業問題拆成角色與文章」區分本頁用途：第一次來只看上半部的問題、
第一篇與站次；下半部完成度只表示研究資料是否齊全，不是產業成熟度、股票排名或受惠程度。
其後在桌機必須先顯示 `maturityRouteGuide` 的「先選一個想弄懂的問題」，再顯示
`maturityGroupExplorer` 的「已知道族群名稱？直接查找」；兩個面板都保持可見，但 DOM 與視覺順序
必須對齊頁首「先選問題」的承諾。在 780px 以下則顯示兩個至少 56px 高的入口按鈕，預設選取
「從問題開始」，讓不熟族群名稱的讀者不必先穿過 11 個術語。
切換時用 `aria-pressed` 公開目前入口並只隱藏另一個面板；resize 到桌機不得隱藏任一面板，縮回
手機後要保留使用者本次選擇。從族群預覽定位系統問題時必須自動切回問題入口；由雷達或文章
返回特定族群時則切到族群入口。這只是行動版漸進揭露，不得重排、刪除或推導研究關係。

「已知道族群名稱？直接查找」選項必須依 `groupMaturity.rows` 的正式族群順序完整
列出，預覽只能重用同列 `readerRole`、`readerBoundary` 與 `learningStart`；「會出現在」則只
能由 `RESEARCH_LEARNING_ROUTES` 已保存的 `groupIds` 反查，不得用文字相似度、公司名或模型
推導。選取族群時必須以 `aria-pressed` 公開目前狀態；第一篇按鈕開啟既有起讀文章，完整進度
按鈕定位同一族群矩陣列，系統問題按鈕則定位既有路線卡。這些連結都是閱讀入口，不代表上下游、
重要性、成熟度或受惠排序。

族群預覽的「從公司證據接下去」只能列出同一列已計入 `companyBridges` 的公司：來源必須是
知識圖譜中 `status=active`、`view=company`、`universe=true`，且公司正式 `groupId` 等於該族群
的既有 edge。每家公司只選一條關係當穩定入口，依序避開已過複核期的 edge，再按既有
`materiality`、`evidenceState` 與 graph／edge ID 決定；所有其他 edge 仍保留在圖譜，不得因入口
選擇而刪除。介面必須完整列出所有已計數公司，不得挑「代表公司」、熱門公司或模型推薦，也不得
從題名、正文或同業名單推導新公司。

每家公司以「先認識本業 → 再看題材關係」兩步承接：第一步只能開該公司的既有正式質化筆記，
第二步必須直接開同一個已登錄 graph／edge 並顯示證據、商業階段與推論邊界；沒有正式筆記時明示
待補，不能拿題材文章代替。矩陣「已完成」欄的公司數以「家」表示，並列出同一批可回查公司，
不再用「檔」讓讀者誤以為是文件數。正式筆記、題材關係與題材財務歸因仍是三個分開的證據層；
任一層存在都不能推成供應鏈認證、訂單、收入、受惠或投資排名。從公司筆記或關係圖返回時，
前端只保存本次工作階段的正式 `groupId`、stock／graph／edge ID、入口位置與捲動位置，必須回到
同一家公司；這個 origin 不寫回研究 payload。

從族群選擇器或每列「開始學這個族群」開啟文章時，前端只保存本次工作階段的
`maturity-group` 起點與正式 `groupId`；從系統問題卡或其展開站點開文時，則保存
`maturity-route` 與既有 `routeId`。文章頁首、行動版返回鈕與「從這篇接著學」末端必須用
同一狀態顯示並返回原入口；換到下一站文章時延續，回到矩陣後把同一族群或路線聚焦。一般
文章清單、圖譜、雷達或直接深連結開文時必須清空這個**矩陣**狀態，不能由文章族群或
文字相似度猜測矩陣來處。雷達若先定位矩陣族群，再由「本題起讀文章」開啟同一已升格 article，
必須改用上述 `maturity-radar` origin；通用族群起點仍使用 `maturity-group`，兩者不得互換。
雷達卡直接開文則依獨立 `radar` origin 契約建立來處；圖譜與矩陣分別沿用自己的 origin 契約，
未帶來處的一般清單與直接連結才
保留「返回研究清單」。矩陣起點說明只可重用既有族群指南與學習路線數量／名稱，
不得新增上下游、受惠或研究排名。

每篇文章前段的產業角色區只能依該文正式 `groups` 順序，對回同一份
`groupMaturity.rows[].readerRole` 與 `readerBoundary`；不得用題名、公司名、相似度或模型補族群。
沒有相符雷達候選時，一至四個族群須依正式順序同時顯示為具清單語意與獨立 heading 的角色卡，
讓讀者直接比較責任與混淆邊界；不得退回單選按鈕、要求讀者記住上一張內容。超過四個族群時只先
顯示一張角色卡：若由族群矩陣開文且原族群確實在本文範圍內，先顯示該族群，否則顯示本文第一個
正式族群；其餘角色依原正式順序放進一個原生 `details／summary`，一次展開全部，不得再增加逐角色
切換。沒有正式族群的文章不顯示這個區塊。並列與清單順序只代表本文宣告的研究範圍，不得改寫成
上下游、受惠、訂單或投資排序。正式筆記與多空文章的角色卡若承接上述首個行動，卡尾必須顯示具
`aria-describedby` 的下一步按鈕，說明角色看完後會回到同篇原文檢查證據；市場議題不得多出這顆
按鈕，因為它的三句重點本來就位在角色卡之前。

只要目前文章能以 `candidate.articleId === article.id` 唯一解析到已升格研究雷達候選，產業角色區
須先依同一 `group_id` 逐字顯示既有 `reader_group_questions`，標成「本文先問」；這個解析跟著
article ID，不依賴 `radar`／`maturity-radar` origin，因此清單、直接連結與路線下一站都能看到目前
這篇自己的問題，但絕不可沿用前一篇或前一個 origin 的候選。一般族群 `readerRole／readerBoundary`
仍須完整保留在同一個預設收合的原生 `details／summary`，摘要明示可查看平常角色與界線；問句與
通用指南不得混成新結論。沒有相符候選時退回上述一般角色卡，不得從正文生成問題。直接 deep link
仍不得顯示雷達題次、返回雷達或其他虛構來處；本文問句只是已登錄內容，不是 origin breadcrumb。
兩種狀態都不得推成上下游、受惠、訂單或投資排序。

「先選一個想弄懂的問題」必須直接使用 `RESEARCH_LEARNING_ROUTES` 的 label、
question、既有第一站與站次；每張卡的相關族群只取該路線主文章已宣告的 `article.groups`，並依
矩陣既有族群順序去重。相同族群可以出現在多條路線，這表示同一角色連到不同系統問題，不是
重複計分。任何路線沒有可解析的主文章時不得顯示空卡，也不能用熱門度、文字相似度或模型補一條
關係。第一站按鈕必須實際開啟該路線 step 1 的文章並回到文章頂端。
路線展開後，每一站另以「這站會用到」依原順序顯示該站主文章既有 `groupLabels`；這只是把同篇
正式研究範圍放到問句旁，幫讀者分辨每站牽涉的產業角色。不得由 route 總族群、圖譜節點、題名、
相似度或模型替站點補族群，也不得把並列標籤解讀為上下游、因果、受惠或重要性排序；文章沒有
正式族群時不顯示空標籤列。

桌機的四張問題卡在路線都收合時必須維持同屏比較；任一 `.learning-route-map` 展開後，其所屬
`.maturity-route-card` 必須跨滿 `.maturity-route-cards` 整列；未展開階段仍可用至少 240px 的
自適應欄寬比較，但任一階段展開時，該階段必須跨滿路線 map 整列，並把站點用至少 280px 的
自適應欄寬呈現，不得讓展開內容只留在三分之一窄欄並空掉其餘版面。780px 以下維持單欄 DOM
閱讀順序，不得為了桌機比較而橫排。這只調整既有 route、phase 與 station 的排版；標籤、問句、
站次、文章映射、開合語意都不得另建或改寫。路線 map 的原生 summary 必須可用 Enter 或 Space
明確切換，焦點留在同一 summary；不得把鍵盤使用者迫使到第一站按鈕才能查看路線。

族群矩陣的每列先給一個可執行的族群起點：只從已登錄學習路線的主文章中選，先找
`article.groups[0]` 等於該族群的文章，再依 `RESEARCH_LEARNING_ROUTES` 與站次排序；沒有起點
時必須明示缺口，不能拿最新、熱門或文字相似文章補位。起點旁另保留「全部 N 篇」，兩種入口
都必須重設到文章或清單頂端，清單標題並持續顯示目前族群。讀完後再用「公司本業底稿 →
題材具名連結 → 財務落地」三層檢查已完成、最大缺口與下一步。這段方法說明在矩陣頂端預設
收合，避免第一次來的讀者先被覆蓋數字與方法術語擋住，但展開後三層與非多空分數警語不得
刪減。這是導覽層，不新增文章／圖譜映射、公司曝險或受惠關係；
矩陣數字只代表研究覆蓋進度，不是多空評分。題材財務可直接歸因為 0，也只表示公司尚未把
該題材收入拆出，不能反推公司沒有相關業務或研究價值。

每列的起點前另由 `config/research_group_guide.csv` 顯示「研究中心怎麼分」：`reader_role`
用一句話說明正式族群負責的產業角色，`reader_boundary` 用一句話提醒最容易混淆的相鄰層級。
CSV 必須依 `config/groups.csv` 順序完整且唯一覆蓋所有正式族群，不得缺項或多出非正式族群；
兩欄都不得留空，並須以完整句號收尾。`build_dashboard.py` 在正式建置時嚴格驗證這個契約。
這是獨立的讀者分類設定，不回寫 `groups.csv`，也不得新增文章／圖譜映射、公司曝險、供應鏈
認證、上下游順序或受惠判斷。

研究中心首次進入、尚未搜尋／篩選／開啟文章時，文章清單固定顯示三步起點：「先選一個系統問題」
前往族群矩陣、「再讀一個市場主題」套用市場議題類型、「最後追產業關係」前往知識圖譜。第一步
必須逐字對齊矩陣的問題式入口，不能再承諾一張實際上不存在的產業全貌圖，也不能要求讀者先背
11 個族群名稱。
這只是把既有三個閱讀表面排成學習順序，不新增事實、公司映射或圖譜關係；讀者開始搜尋、
篩選或閱讀文章後即隱藏，避免導覽卡持續占用工作空間。關閉文章回到清單時必須重新依同一條件
計算是否顯示導覽；不得沿用 `article-open` 時留下的 hidden 狀態。由清單開文要記住 window 與
catalog 的捲動位置，返回後恢復並把鍵盤焦點送回同一張文章卡；由雷達、矩陣、圖譜或深連結開文
而沒有清單位置時，文章開啟後必須把 window 與閱讀欄送回頂端，並將鍵盤焦點送到新文章的第一層
標題；不能把焦點留在已隱藏／已移除的入口按鈕。返回清單時才把目前文章卡捲入可視區後聚焦。

首次進入的三步導覽在窄幅也必須預設展開，不能先把 274 篇「最新更新」清單冒充推薦起點；讀者
明確收合後才以瀏覽器本地顯示偏好記住狀態，且 resize 不得覆寫。第一步另須逐張重用
`groupMaturity.learningRoutes` 的 label、question、stationCount、firstGraphLabel 與
firstArticleId，顯示全部既有問題捷徑；每個捷徑只在第一篇文章可解析時啟用，並以
`maturity-route` origin 一鍵開啟第一站，讓文章首尾仍能返回同一條完整路線。這只是縮短導覽，
不得另寫問題、猜測文章、改動路線順序、族群、站次、圖譜或研究證據。

已發布市場議題若沒有 `learningRoute`，文章前段仍須明示「目前沒有固定站次」，不能讓讀者把
缺少站次誤讀成沒有產業關聯，也不能假裝它已在四條固定路線裡。位置卡只可逐張讀取同篇既有
`learningPath.cards`：有 graph card 就顯示第一張既有圖譜題名，有 article card 就顯示第一篇既有
文章題名，只有 collection card 時明示尚無可回查圖譜或固定站次；同時分開列出三種入口數量。
「看這篇怎麼接下去」只把焦點送到同篇既有「從這篇接著學」，不得用正文、題名、相似度、模型或
族群清單補一條 route、graph、上下游、受惠或投資關係。已有 `learningRoute` 的文章繼續只顯示
正式路線定位，不得疊加這張未編路線提示。

同一個首次進入條件下，閱讀欄必須保持未選文狀態，不能因清單按更新時間排序就自動把第一篇
渲染成推薦起點。閱讀欄的起始說明必須與清單三步使用同一順序，並只把第一步「先看族群矩陣」
設為主要行動；同時明示清單第一篇只代表排序結果。搜尋、篩選或切換文章類型後若尚未選文，
閱讀欄改為一般選文提示。直接文章深連結與讀者主動選文仍須立即開啟正確文章；篩選使已開文章
失效時，才可在 `article-open` 狀態下移到新的第一筆，避免閱讀器與網址指向不存在的結果。

知識圖譜繼續以「學習路線 → 中心主題 → 投影視角 → 關係來源」分段導覽。學習路線只能把
已存在的 graph ID 分成閱讀群組，未分類的新圖譜必須自動落入「其他主題」，不得因導覽分類新增 edge、
改寫 evidence state 或推導受惠關係。行動版每次只顯示當前路線的一個主題選擇器；不能把所有主題按鈕
堆在內容之前。完整控制的原生 `details` 在所有寬度首次載入都須收合，摘要固定寫「目前這張圖」，
並同步顯示當前路線、主題、階段、視角、證據層級與可選的台股範圍；展開後 summary 仍須可見，
讓滑鼠與鍵盤都能再次收合，不能形成只能打開、不能關閉的單向控制。桌機四步讀法預設展開；窄幅
首次載入才把四步讀法也收合一次。兩個區塊都不得在旋轉或 resize 後覆寫讀者手動開合狀態。
每條路線的說明必須交代建議閱讀順序；每張 active graph 至少要有一個既存
`article_ids`，首屏的「先讀主題文章」只能解析該欄位，不得以標題或關鍵字推測新文章映射。
從圖譜開啟既有文章時，顯示層必須建立一次性的 graph origin，至少保存 graph ID、投影視角、
已選節點／關係與圖譜捲動位置。文章桌機首尾與行動版返回鍵都要清楚說明可回到原圖；返回後必須
恢復這些狀態與合理的鍵盤焦點，不能把讀者丟回圖譜頂端或未選取狀態。直接文章深連結與一般清單
開文的 origin 必須保持空值；這個往返狀態不得寫進文章、圖譜或研究證據 payload。
反向從文章「看產業關聯」卡或學習路線的「看這站證據關係」進圖時，顯示層另建立一次性的
article-learning graph origin，保存
文章 ID、文章閱讀欄與 window 捲動位置，以及文章原本的矩陣／圖譜起點。圖譜首屏必須先說明
「文章 → 關係圖」、剛才文章與返回後可繼續的站次，並把鍵盤焦點送到這條脈絡；返回後須恢復
同一篇的原捲動位置、原圖譜按鈕焦點與原本系統問題：從延伸卡開圖就回延伸卡，從路線定位開圖
就回「看這站證據關係」，不能回文章頂端、聚焦另一顆按鈕或遺失矩陣起點。
同一個 article-learning origin 也必須投影到關係解讀末端，標出剛才文章、下一站與至少 44px 的
返回行動；返回契約與首屏按鈕完全相同。直接圖譜 deep link、頁首圖譜分頁、研究雷達與非文章入口
必須清空首屏與關係卡的這個狀態；同樣不得寫進 payload。
圖譜簡介使用一般中文解釋節點距離與財務歸因，不在首屏直接暴露內部 assessment 狀態碼。

只要目前投影與證據篩選後仍有 edge，圖譜必須提供一個關係閱讀示範。選取順序固定為「未到期
verified → verified → 第一條可見 edge」，且畫面必須明示它只教讀法、不代表重要性、受惠或
投資排序。啟動示範後要把鍵盤焦點與捲動位置送到關係詳情，窄幅畫面不得讓黏性頁首遮住標題。
關係列與 badges 必須直接標出「關係／證據／階段／商業位置」，不能只排一串未命名狀態。
在桌機寬度至少 981px、可視高度不超過 840px 時，關係詳情必須取消自身 `overflow` 與 sticky，
改由 `graphPage` 單一捲動；關係清單選取 edge 時必須同步聚焦並捲到新詳情，不能更新到視野之外。

關係詳情的讀者層固定回答三題：「這條線現在怎麼讀、還不能推到哪裡、看到什麼才升級」。第一題
只能組合 edge 的兩端、`relationLabel`、`evidenceState`、`materialityLabel` 與
`commercialStageLabel`；第二、三題必須逐字使用 `boundary` 與 `nextTrigger`。延伸閱讀只能解析
同一 edge 的既有 `articleIds`。這是顯示層重排，不得替 edge 補白話主張、推測公司確認、建立
新文章映射或改變 evidence state。

學習路線的單一事實來源是 `build_dashboard.py` 的 `RESEARCH_LEARNING_ROUTES`；圖譜選單、文章
頁首定位與正文後的下一站都讀同一份順序。每個 route `graphId` 只取該 graph 第一篇可解析的
既有 `articleIds` 作為一個主題站，不把同一 graph 的補充文章膨脹成額外站次；因此路線標示的
graph 數必須與文章站次一致，且各 graph 的主文章不可重複。文章頁首須顯示路線、目前站次及
可原位展開的完整路線地圖；矩陣的系統問題卡須重用同一地圖。每個 station 只能保存 step、
既有 graph ID／label、該 graph 第一篇既有 article ID／title、同篇 `readingMission.question`、
閱讀時間、既有 group labels 與下述 phase 定位；不得生成第二份站點摘要。白話問句仍只保存在
同篇 article 的既有 `readerQuestion`，顯示時以 `articleId` 回查，不得複製進 station 形成第二份
可分岔資料。route 若宣告
`phases`，每個 phase 必須有唯一 `id`、白話 `label` 與連續 `graphIds`，把所有 route `graphIds`
依原順序逐站且恰好覆蓋一次。phase 只能整理閱讀章節，不得改寫成上下游、供應鏈、重要性或
受惠順序；建置必須在遺漏、重複或換序時失敗。發布 station 與 article route 只可由該登錄表
附加 `phaseId／phaseLabel／phaseStep／phaseTotal／phaseStationStep／phaseStationTotal`；文章
頁首、可展開路線地圖、族群起點與下一站卡都須重用同一份 phase，不得各自另寫分組。
從文章開啟圖譜後，「目前位置」必須顯示同一 phase；行動版原生圖譜主題選單須用 phase
`optgroup` 分組。無 phase 的相容路線可維持單層選單，不得依圖譜標題臨時猜分組。
多 phase 的路線地圖須以巢狀原生 `details／summary` 做逐階段揭露：文章模式只在初次 render
打開目前文章所在 phase，矩陣模式只在初次 render 打開第一個 phase，其餘 phase 預設收合；
resize 不得重設使用者已切換的開合狀態。每個 phase 摘要須顯示 phase 名稱、站數或「目前階段」
及完整站次範圍，觸控高度至少 44px，Enter 與 Space 都可切換。所有站點與原問題仍須保留在
同一有序結構中，不得為縮短畫面而刪除、截斷或改寫；單 phase 路線可維持原單層站點清單。
站點按鈕的顯示層須先由 `station.articleId` 回查同篇既有 `article.readerQuestion` 作為白話主標，
再用「研究節點：」標示既有 `station.graphLabel` 為次要脈絡；不得讓技術節點名壓過讀者要回答的
問題。只有 `readerQuestion` 缺值時才可退回 `station.question`，不能由題名、正文、關鍵字或模型
生成替代問句。當兩個問句不同時，原 `station.question` 必須逐字保留在緊接站點的原生 `details`，
摘要固定寫「讀完再試著回答精確追問」；白話問句與精確追問只改閱讀順序，不得互相覆寫。站點
按鈕最小高度 72px，精確追問摘要觸控高度至少 44px，`aria-label` 必須同時包含白話問題與研究
節點。站點按鈕直接開啟該文並回到頁首，
目前文章用 `aria-current="step"` 標示；前往圖譜的按鈕必須明寫「看這站證據關係」與實際投影
「產業依賴／公司曝險」，不能再把單一圖譜頁稱為「完整路線」。本文有兩個以上正式 `groups` 且
該 graph 存在 industry edge 時，入口固定先開產業依賴，承接剛才的多角色比較；只有一個族群、
沒有 industry edge，或只有 company edge 時先開公司曝險。若 company edge 缺席但 industry edge
存在則安全退回產業依賴。判斷只能讀既有 article groups 與 edge view，不得依邊數、標題、熱門度
或模型推測重要性；畫面須明示另一視角仍可在圖內切換，按鈕在所有寬度至少 44px 高。按下後須建立來源為 `route-context` 的 article-learning origin，
進入圖譜時重設到圖譜頂端。若同篇有兩個以上正式 `groups`、目前仍是該篇對應 graph 的產業依賴
投影，origin 卡須把每個 group 只依既有 node `groupId` 對回 industry edge：恰好一條才可產生角色
按鈕，0 或多條都須禁用並明示不能唯一定位，禁止依 edge 順序、標題或相似度任選。按鈕須逐字沿用
同篇已登錄的雷達族群問句（若有）、edge 證據層級與商業位置；點擊後直接進既有三步關係解讀，若
該證據層級曾被篩掉可明確恢復同一層再開線。公司曝險、直接 deep link、單族群文章與不同 graph
不得顯示文章角色卡。返回文章時恢復原閱讀位置、矩陣路線 origin 與同一按鈕焦點。下一站卡須
明示「閱讀順序不新增供應鏈或受惠關係」；末站另明示只完成閱讀順序、不代表研究結論完成，
再回到原本由具名公司、宣告族群與可追溯圖譜產生的延伸規則。
選定任一可唯一定位的文章角色 edge 後，三步關係解讀下方必須重用同一份 article group 順序、
候選問句與 edge 對應，顯示詳情內的「文章角色比較」。目前角色用 `aria-current="step"` 且不可
重複啟動；其他恰好一條 edge 的角色可用 click、Enter 或 Space 原位切換，必要時恢復該 edge
原證據篩選，並把焦點送到更新後的關係詳情。0 或多條 edge 仍須禁用與明示缺口，不得猜線。
這個導覽只在同篇 article-learning origin、同 graph、多族群、industry 投影且目前 edge 確實是
該角色唯一對應時出現；直接 deep link、company 投影、單族群、不同 graph 或非文章來處均須為 0。
按鈕所有寬度至少 44px，窄幅不得水平溢出；順序只供同篇角色比較，不得改寫為上下游、受惠、
訂單或投資排序。
不能用文字相似度、熱門度或模型判斷補出路線關係。

主閱讀流程在正文後固定顯示「從這篇接著學」。延伸卡只能由現有 library 與 knowledge graph
產生：文章必須共享具名公司或宣告族群；圖譜必須已引用本文，或已包含本文的具名公司；族群
入口只能使用本文已宣告的族群。它是導覽層，不得依文字相似度自行建立供應鏈、客戶或受惠關係。
正式 route 下一站已由 `routeBridge` 解釋 graph／phase 次序；除此之外，每張一般 article card
都必須附 machine-readable `relationBasis`。先依來源文章 `stockIds` 原順序列出兩篇共同公司，
只有沒有共同公司時才依來源文章 `groups` 原順序列出共同族群；公司名稱只取對應正式筆記 subject，
族群名稱只取 library groups，找不到顯示名稱時保留原 ID。共同公司與共同族群都不存在時建置必須
失敗，不得改用題名、關鍵字或模型補理由。讀者卡須明示「這兩篇為什麼相連」與共同標記；超過
三個共同族群可先顯示三個，但必須能原位展開全部。這個標記只揭露推薦 provenance，必須明示
不代表上下游、受惠、訂單或因果關係，也不得建立 knowledge graph edge。每張一般 article card
另須附 `questionLabel: 讀下一篇時比較` 與非空 `question`；問題只能依來源／目標的文章類型組合，
套用固定比較句型，再插入同一張卡 `relationBasis.labels[0]`。多個共同標記只可顯示第一個名稱與
既有數量，不得逐條生成關係。不得讀正文、題名或關鍵字補問題，也不得把問題寫成已證實的公司、
供應鏈、受惠或因果結論。正式 route 卡維持逐字重用下一篇 `readingMission.question`，不得套用
一般推薦句型。
圖譜卡若不是由 `graph.articleIds` 直接引用本文，而只因共同公司成立，也必須附 machine-readable
`relationBasis`：公司順序逐字沿用來源文章 `stockIds`，且每家公司都必須是圖譜目前可見 projection
中實際連到 edge 的 ticker 節點。卡片須明示「這篇為什麼連到這張圖」與共同公司，並說明共同
節點不代表本文主題就是該圖的上下游、受惠、訂單或因果關係。下方 `guidedRelation` 必須觸及同一
`relationBasis.ids` 內至少一家公司；不得因圖內另有更高證據層級的 edge，就改示範一條與本文
共同公司無關的線。找不到同公司可見 edge 時不得推薦該圖，也不得用公司名稱、題名或文字相似度
補一條關係。圖譜若已直接引用本文，維持原本依可見 projection 選擇證實 edge 的規則。
文章沿 `guidedRelation` 進圖譜時，必須把來源文章 ID、圖譜 ID、投影視角、已選 edge 與捲動位置
保留成 reader-only origin。若 edge 的「完整研究脈絡」就是來源文章，關係卡不得再顯示一個重開
同篇的 CTA；須明示完整脈絡就是剛才文章，並讓下方返回按鈕回復原文章與閱讀位置。若 edge 開啟
另一篇文章，該篇延伸區須收起指向來源文章與同一張圖的重複卡，顯示「剛才文章 → 關係圖 →
現在」的既有路徑，再把理解檢查與尚未走過的卡接在後面；頁首／頁尾仍保留回原圖入口。這只
改變同一次互動的卡片投影，不得刪改 `learningPath.cards`、graph edge、來源或靜態文章內容，
也不得把其他文章、族群或圖譜誤判為已讀。從清單、研究雷達、族群矩陣或直接圖譜入口開文時，
只有 origin 實際證明已走過的文章與圖譜才可收起。
列入正式學習路線的主文章另須在延伸區完成「本篇理解檢查 → 下一站問題」交接：理解問題逐字
重用同篇「想一想」，預設收合的提示只能逐字重用同篇「三句話抓重點」，不得生成答案或改寫
語氣；下一站問題逐字取自下一篇已登錄 route 主文章的閱讀任務。所有非末站另須把本篇
`learningRoute.graphLabel／phaseLabel` 與下一篇相同欄位逐字排成兩步閱讀交接；缺 label 時不得
用文章題名、相似度或模型補寫。這個 ordered list 只表示 route 既有次序，必須明示不代表
供應鏈、受惠或因果關係，也不得建立 knowledge graph edge。任何 route 主文章缺少問題或
三句重點都必須讓建置失敗。回看按鈕須把鍵盤焦點與捲動位置一起送回「三句話抓重點」，不能被
黏性導覽遮住；下一站按鈕須顯示站次、開啟既有文章並回到文章頂端。`.learning-path` 必須建立
inline-size container；實際內容寬度不超過 620px 時，`.learning-handoff` 與
`.learning-path-grid` 都改為單欄，不能只依 viewport 判斷，因桌機 master-detail 的正文也可能
只剩三百多 px。寬專注閱讀才保留並排比較。

文章內換篇時，`ensureSelected()` 必須優先保留仍開啟且存在於 `byId` 的文章，即使它不符合左側
目前搜尋、類型或族群條件；不得再由 `filteredArticles()` 的第一篇覆寫下一站。清單須保留原條件
並顯示「目前閱讀不在左側結果」，讓讀者知道差異來自延伸導覽。首次由清單開文時另保存原 article
ID、window 與 catalog 捲動位置；返回清單須重建原選取並恢復焦點，不得把下一站硬塞入搜尋結果，
也不得清除使用者的搜尋或篩選。

延伸區的圖譜卡必須描述它實際會開啟的同一投影：優先使用有 edge 的 `company` 視角，只有沒有
公司 edge 時才退到 `industry`；節點數只計 root 與該視角 edge 實際連到、且存在於 graph nodes
的節點，關係數也只計該視角 edge，不得再使用同時混合兩種 view 的 graph 全量。卡內可示範一條
同視角既有關係，優先取登錄順序中的第一條 `verified`，否則取第一條現有 edge；畫面只能逐字
顯示 node label、relation label、evidence label、commercial stage 與 boundary，並明示不是
重要性、受惠或投資排序。CTA 必須把同一 `graphView` 與 `edgeId` 帶進圖譜，使入口標題、統計與
已選關係和文章卡一致；不得靠文章文字另造 edge、改寫 evidence 或把示範關係升級。

自 2026-08-10 起，新建 topic 的新手導讀另受白話 gate：約束範圍只限第一屏導讀，不限制
機器可讀帳本。`active claim`、`watch`、`bounded_proxy`、`H1` 等內部維運詞不得直接露出；
英文術語第一次出現就要在小字典解釋；單一段落或 bullet 超過 180 個可見字必須拆開。既有
文章只警告，避免新規則回溯使已簽核研究失效。這項雙讀者 gate 是發布可用性契約，不改變
topic schema 或證據層級。

列入白話升級批次的「為什麼重要」若有兩段以上，優先以 `**短主句。**` 開頭，再用較短句子
展開情境、常見誤讀、責任或證據邊界。主句必須由作者寫進 Markdown；renderer 只在粗體確實是
該段第一個 run 時加上 `data-reader-lead`、色彩與分隔線，不得從段落自動摘要或替沒有主句的
文章生成文字。改寫仍須追加同狀態 `editorial:<slug>` transition，並由 baseline lint 證明
source／claim／comparison／monitor 與鎖定 meta 逐字未變。

若同一批次也把主正文的多步機制改成段首主句，主句先寫中文概念，必要英文放在括號；每一段仍要
保留足以理解責任、差異與證據邊界的完整說明。只有從該節第一個 block 起連續至少三段都符合
`**短主句。**`，發布頁才會顯示上述「本節先看」；不能為了湊卡片把不同位置的段落拉在一起。
這類正文改寫同樣必須追加同狀態 `editorial:<slug>` transition，且不改 source／claim／comparison／
monitor 與鎖定 meta。

文章若跨越「市場需求 → 元件／設備工作量 → 個別公司財務」三層，白話升級批次應在新手導讀
把三道證據關卡逐項寫出：每一關先說目前哪份資料能支持什麼，再說下一關仍缺哪份公司級證據。
不得把市場規模、年化營收、容量承諾或相對效能直接接成台灣公司訂單、收入或獲利。這條因果橋
必須由作者寫進 Markdown；renderer 不得依 `group_ids`、公司清單或數字自動生成，也不得把
`not_comparable` 的跨公司數字改畫成排名。純敘述整理仍使用同狀態 `editorial:<slug>`，並由
baseline lint 證明所有研究帳本與鎖定時鐘不變。

既有文章一旦列入讀者學習路徑的白話升級批次，就不得再保留 readability warning；測試以
明確文章清單鎖住這項品質債，避免後續回退。改寫先寫中文概念，再把英文專有名詞放在括號，
並優先用「範圍、角色、成熟階段」把技術新聞拆成讀者能逐步回答的問題。這仍屬同狀態
editorial revision：只能調整正文與新手導讀，來源、claim、comparison、monitor 及鎖定 meta
必須維持不變，transition 的 evidence 使用 `editorial:<slug>`。

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

`last_evidence_at` 不手填，而是在 active `thesis_claim_id` 引用之 active source 中，先取
effective published date（`document` 用 `published_at`、`living_index` 用 `captured_at`）
最新者，再取其 `accepted_at` 最大值；其他周邊 claim 的新證據不得刷新主命題。後來才找到的
舊文件只增加獨立來源鏈，不刷新新鮮度。
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
