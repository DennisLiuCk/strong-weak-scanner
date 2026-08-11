# 市場研究取得、驗證與持續修正方法

本文件是 `notes/research_topics/` 的方法論總入口，回答「去哪裡找、什麼能說、數字能不能
比較、何時要重查、錯了怎麼留下修正紀錄」。操作節奏與佇列見
`RESEARCH_MAINTENANCE.md`；公司正式事實仍由 `QUALITATIVE_RESEARCH_RUNBOOK.md` 的
evidence pack 與獨立 reviewer 治理；可證偽 H# 仍由
`LEADING_HYPOTHESES_PHASE2_RUNBOOK.md` 治理。市場 topic 不是第四套正式事實庫，也不改
量化分數。

## 研究產物的最小閉環

每篇市場議題都必須走完以下鏈條：

```text
候選快掃
  → 研究前凍結初始排名／第一拒絕／下一份證據
  → 可證偽問題
  → 至少兩條可定位的來源
  → claim–evidence ledger
  → 反方來源與證據邊界
  → 跨公司數字的可比性裁決
  → 可觀察 monitor 與失效條件
  → review due／可信度新鮮度
  → 新證據追加或保留待重新驗證
```

「找不到公司級證據」是有效結果。這時應把公司映射標成 `unverified`，而不是用同業、
平台生態系名單或市場轉述補洞。

### 選題前承諾：先留下可被打臉的選擇

候選文章開始深研前，先在 `notes/research_candidates/selection_log.csv` 追加一個 cycle，凍結
`candidate_id`、初始 `rank`、`priority`、`knowledge_value`、`evidence_posture`、
`selection_decision`、`selection_reason`、`first_rejection` 與 `next_evidence`。同一 cycle 的
候選共用一個含 `+08:00` 的 `selected_at`，rank 必須從 1 連續排列。這份帳本 append-only；
`research_method_audit.py --baseline-ref` 會以 Git 前版檢查既有列前綴，不能在看到深研結果後
回填或改寫初始理由。

Active radar 使用 schema 2 並以 `selection_cycle_id` 指向該輪凍結記錄。雷達可以另記深研後
的 `promoted／watch／deferred` 與 evidence posture，但初始 rank、priority、knowledge value、
第一拒絕和下一份證據必須逐字等於 selection log。`advance → promoted` 只表示完成本輪研究產物；
`advance → watch/deferred` 是研究後拒絕，也同樣是有效方法結果。兩者都不能稱為題材、投資或
報酬命中。首個 cycle 以獨立 Git commit 先凍結，再提交文章與圖譜；後續每輪沿用同一順序。

Active 候選的讀者卡必須在 `reader_question` 與 `reader_next_step` 之間提供
`reader_starting_point`。它固定是兩句白話：第一句只把同一候選 `why_now` 已有的起始線索
說清楚，第二句以「目前還」標出證據缺口或推論邊界。這是 reader-only 編輯層，不加入 selection
log、method fingerprint、知識圖譜或文章 claim，也不得藉此提高 evidence posture、宣告升格或
補出新的公司關係。完整 `why_now` 仍留在預設關閉的查核區供回查。

Active 候選另必須宣告 1–4 個 `group_ids`，值域逐一對齊 `config/groups.csv`。這是讀者從
「研究什麼」前往族群矩陣查看起讀文章與缺口的導覽索引，不屬 selection log 凍結欄位，也不
構成公司曝險、供應鏈認證或受惠判斷；原候選沒有寫明的族群責任，不可由介面關鍵字自行補上。
每個 `group_id` 必須依相同順序各有一個 `reader_group_questions` 白話問句，逐一說明該族群在
同一研究題要回答的問題。問句只能縮寫候選已記錄的知識缺口、責任角色或驗證動作；不能排成
上下游順序、替族群命名受惠方向，或把未升格候選補成公司與圖譜關係。介面由雷達前往矩陣時
必須保留同一問句並選取相同族群，避免讀者只剩族群名稱而失去原研究脈絡。若候選已升格，矩陣
的本題主要行動必須開同一 `candidate.article_id`，不得以通用族群起點替代；完成度、財務缺口與
下一步只屬族群整體盤點。雷達承接區須先橫跨所選矩陣列的四個盤點欄，依序保留原題次、原問句、
本題文章與返回行動，再讓讀者進入族群起點、完成度、缺口與下一步；不得把承接卡留在第一欄，
使本題答案與族群盤點看似同一層。未升格候選則必須明示本題尚無文章，不得由介面猜測，也不得
在寬幅配置留下空白文章欄。已有文章時寬桌面可用三欄、中幅兩欄、窄幅單欄；返回後須恢復同一
承接卡、所選族群與整列焦點。
若候選已升格並指向正式 article ID，介面開文時必須帶同一 candidate ID 的一次性來處；
文章首尾要繼續說明「雷達第 N 題」只是研究資源安排，返回後恢復同一候選卡位置與焦點。
同一工作階段也可把該候選既有 `reader_group_questions` 逐字帶到相符的文章角色卡，但只限
`radar` 直接來處，或雷達先定位族群矩陣後開同一升格 article 的 `maturity-radar` 來處；目前文章
仍必須是該候選自己的正式 article ID。後者文章首尾須保留族群、雷達題次與問句，返回後聚焦原
矩陣列；換到下一站文章後不得沿用。
直接文章連結不得顯示這個來處，也不得將導覽狀態寫進研究 payload。

研究雷達卡的第一閱讀層必須在題目與 status 後立即回答「這題現在怎麼讀」：可解析正式文章時
前移同一 article 行動；沒有文章的 `watch` 題明說先把它視為待驗證問題，使用原
`reader_group_questions` 拆分研究責任並等待下一份證據；`deferred` 題明說目前不投入完整研究。
文字只能由既有 status、article／graph 可解析性與正式族群數套用固定句型，不得讀正文補摘要、
改變 candidate 排序或把候選升格成結論；前移後卡尾不得再出現第二組相同行動。

族群矩陣的名稱查找入口必須先把既有 `learningStart` 說清楚，再進公司證據。每個正式族群的
預覽只能逐字使用同列 article ID／title、route／phase／step／total，以及該 article 已發布的
`readerQuestion` 與 `readingMinutes`；角色與混淆邊界後依序顯示「建議先讀 → 文章題名 →
帶著這題讀 → 完整路線位置 → 讀這篇」。第 N／M 站只描述該文在完整路線的位置，不得寫成必須
先讀前 N−1 站，也不得靠標題、正文、相似度或模型換一篇較像入門的文章。解析不到既有 article
時明示缺口。公司證據與完整族群進度仍保留，但須排在上述起讀文章與系統問題之後。

族群矩陣可以把已登錄的公司級關係提前成讀者入口，但不能在介面生成新關係。可顯示公司只取
active 的公司視角圖譜 edge、台股 universe 節點與該公司的正式族群；每家公司只挑一條可追溯
edge 當起點，所有公司與其餘 edge 仍須完整保留。讀者順序固定為「正式公司筆記確認本業 →
圖譜 edge 檢查題材關係 → 財務 assessment 檢查可歸因影響」；三層不得互相替代。具名關係仍不
等於供應鏈認證、訂單、收入、受惠或投資排名，找不到公司或財務證據也是有效的研究缺口。

退役雷達仍是方法歷史，不因換成新 active radar 就退出稽核。`research_radar.py` 會逐輪核對
所有 schema 2 radar 與 selection log，並把它們納入 method fingerprint。候選若在前一輪
`next_check` 前被重選，自 2026-08-07 起，新的 frozen `selection_reason` 必須以
`early_trigger:<source title>@YYYY-MM-DD=>https://URL` 留下觸發來源；URL 必須是前輪尚未列
過的一手來源，日期不可晚於本輪 selected date。它可以是新發布文件，也可以是前輪漏看的
既有文件；兩者都只授權**提前重查**，不預先保證升格。cutover 前未留 trigger 的重選保留
原紀錄並在 audit 揭露，不回溯粉飾。

## 一、先按文件角色取得來源

搜尋順序以能直接承擔主張的文件為先，不以搜尋結果排名或文章數量為準：

1. 發行人新聞稿、正式法說、財報與監管申報。
2. 客戶、平台、交易對手或競爭者的一手文件，用來交叉驗證與找替代路徑。
3. 政府、監管、交易所與標準組織文件。
4. 管理層直接談話；若只是轉述，必須降低來源角色。
5. 市場估計與媒體只適合提供搜尋 trigger；不能單獨把公司主張標為 `verified`。

### 台灣季報的三層取得順序

公司 IR 頁面不是完整性判定的唯一入口。季報窗口必須把「事件／數值索引、正式附件、內容
驗證」拆成三層：

1. 同時掃 TWSE 與 TPEx 的重大訊息、當季損益表及資產負債表 OpenAPI，對照完整 universe；
   這一層只負責找 trigger。單一當日端點或只掃一個市場必須標 `partial`。
2. 對每個命中逐檔查 MOPS `t57sb01` 直接文件索引，記錄檔名、申報時間與大小。公司官網
   還沒更新時，不能據此寫「完整附件不存在」；反過來，索引有檔案也只證明可取得。
   優先名單使用 `scripts/research_filing_index.py` 產出唯讀 JSON，避免人工只開公司 IR 而
   重複漏掃；工具的網路／解碼／表格解析失敗必須整輪標紅，不能降格成「查無資料」。
3. 要把附件內容升為公司事實，仍須封存同一版本、記錄 SHA 與引用頁，並依
   `QUALITATIVE_RESEARCH_RUNBOOK.md` 由另一位 reviewer 離線重算期間、單位、數字與推論
   邊界。OpenAPI 列與檔案索引都不能替代這一步，也不能單獨刷新 thesis evidence clock。

這個順序處理兩種不同錯誤：只看公司 IR 可能漏掉已申報附件；只看 OpenAPI 或 MOPS 檔名，
又可能把「檔案存在」誤寫成「內容已驗證」。scan log 的 `full` 只描述已明示的市場、端點與
日期窗完整，不延伸為所有公司 IR、所有語意公告或全市場題材皆已掃完。

`research_source.role` 值域：

- `company_release`：公司新聞稿、產品公告或 IR 公告。
- `company_filing`：財報、10-K／10-Q、法定申報或含正式附註的文件。
- `regulator_or_policy`：政府、監管與政策文件。
- `exchange`：交易所或正式公開資訊站。
- `standard`：標準組織發布的規格或公告。
- `competitor_primary`：競爭者、替代方案供應商或另一條獨立公司消息鏈。
- `management_commentary`：可定位的管理層直接說法。
- `market_estimate`：公司或研究機構提出的市場規模與預測；不是已實現事實。
- `media`：媒體報導或二手轉述。
- `other_primary`：不屬於上述類別、但可驗證的一手來源。

### Source block

每個唯一文件使用穩定 ID `S1`、`S2`……；不可因排序改變而重編。所有欄位均為單行
`key:value`：

```markdown
<!-- research_source
source_id: S1
role: company_filing
source_kind: document
publisher: Example Corp.
title: 2026Q2 Form 10-Q
published_at: 2026-07-30
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://example.com/filing
locator: liquidity section, table 3
limitation: 此表是 TTM，不能直接與另一公司的單季數字排名
-->
```

三個日期不可混用：

- `published_at`：來源正式發布日。
- `captured_at`：研究流程實際取得文件的日期。
- `accepted_at`：研究者已核對 locator、期間、單位及 limitation，正式接受進 ledger 的日期。

日期必須符合 `published_at <= captured_at <= accepted_at`。`accepted_at` 不是來源為真的
保證，也不是獨立 reviewer 簽核；它只表示該版本已被納入本篇 topic 的可追溯證據。

`source_kind` 預設為 `document`，必須有正式 `published_at`。公司 IR 文件清單、交易所查詢
入口等會持續改變、且本身沒有單一發布日的頁面，改用 `living_index`：`published_at` 留空，
由 `captured_at` 表示實際觀察日，locator 必須寫明當日看到或沒看到什麼，limitation 必須
說明頁面之後可能改變。不得把掃描日冒充發布日；living index 也不能替代已發布附件。

`status` 值域為 `active`、`superseded`、`rejected`。只有 `active` source 可以被 active
claim 或 monitor 引用。若來源後來失效，不刪除原 block；依「八、修正採追加保存」處理。

獨立消息鏈不是靠自由填寫的 publisher 名稱計數。系統預設以 URL 的註冊網域近似分組；
同一 nvidia.com 上的共同新聞稿仍算同一發布鏈。若監管網站代為託管不同發行人的文件，可用
`independence_group` 明示內容原始發行人。至少兩份來源必須真的被 active claim 引用；只放
一個未引用的 IR／MOPS 查詢入口不能湊足證據數。

### Thesis evidence clock

topic 不手填 `last_evidence_at`。它固定由下列集合推導：

1. 找出 `thesis_claim_id` 指向之 active claim 的 `supporting_source_ids` 與
   `contrary_source_ids`。
2. 只保留 `status: active` 的被引用 source。
3. 取其中 **effective published date 最新**的來源（`document` 用 `published_at`，
   `living_index` 用 `captured_at`），再取這些來源的 `accepted_at` 最大值。

第 3 步自 2026-08-08 起改為以發布時間決定、`accepted_at` 只作同日排序。原先直接取
`accepted_at` 最大值，會讓「後來才找到的舊文件」把時鐘刷成當天——因為 `accepted_at`
必然是研究者接受它的那一天。回填一份 2024 年的佐證可以增加獨立來源鏈，但它不是更新的
證據，不得改變新鮮度。

其他 active claim 的最新證據另保留為 `ledger_last_evidence_at` 供稽核，但不能刷新主命題
的 confidence clock。未被 claim 引用的書目、只出現在 monitor 的未來來源，或
`superseded/rejected` source，都不能刷新任一 evidence clock。`last_reviewed_at` 不得早於
衍生的 `last_evidence_at`。

## 二、Claim–evidence ledger

每篇 v3 至少要有一則 `verified` 與一則 `unverified`；只有在文章確實提出超出來源原文、
但仍可由證據推導與反證的研究判讀時才建立 `inference`，不可為了湊齊標籤製造假推論。
主命題由 meta 的 `thesis_claim_id` 指向。Claim ID `C1`、`C2`……永久穩定，不因改稿重編。

### 三種標籤的精確語意

- `verified`（證實）：**只表示指定來源直接支持 claim 欄位的精確措辭**。若公司說
  「預計明年量產」，能證實的是公司做出這項預期，不是量產必然實現。生態系列名也不等於
  新增訂單、收入、市占或毛利。
- `inference`（推論）：由已列來源或 verified claim 推導的研究判讀。`basis` 必須交代
  推導鏈，`boundary` 必須說明不能外推到哪裡。
- `unverified`（待驗證）：現有來源不足以支持的主張。`verification_needed` 必須寫出需要
  哪種文件或觀測才能升級，不得用空泛的「持續追蹤」。

```markdown
<!-- research_claim
claim_id: C2
label: inference
status: active
claim: 目前兩種架構較可能先共存，而不是立即全面替代
supporting_source_ids: S1,S2
contrary_source_ids:
as_of: 2026-08-01
basis: S1 顯示新架構量產，S2 同時顯示既有架構仍大量出貨
boundary: 未知兩種架構的實際出貨配比、使用位置與生命週期成本
verification_needed: 後續產品組合、部署數量與公司量產收入
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->
```

規則：

- `verified` 與 `inference` 至少引用一個 active supporting source。
- `unverified` 可以沒有 supporting source，但必須填 `verification_needed`。
- `contrary_source_ids` 只放**直接反駁或實質縮窄這句 claim** 的 active source；「來源沒有
  提到」、「搜尋沒有找到」或資料仍不足，都是證據缺口，不是反方證據。
- `resolution` 預設留空，且只用於有 active contrary source 時的人工作法裁決：說明正反
  證據的權重、目前保留或縮窄哪一段措辭，以及仍不能排除什麼。它不是 claim 狀態、
  「active」標記或修正鏈欄位。
- `correction_kind`、`corrects_claim_id` 與 `corrected_by_claim_id` 平時留空；只有追加修正
  claim 時依「八、修正採追加保存」填寫。
- `basis` 說明「為什麼能這樣寫」，`boundary` 說明「這句話不能被用來證明什麼」。
- `as_of` 是該 claim 的資訊截點，不是文章發布日。
- `evidence_role: trigger_only` 的 topic 不得只靠 trigger 建立 verified 公司事實。
- `status` 值域為 `active／superseded／refuted`。`thesis_claim_id` 必須指向 active 的
  verified 或 inference claim，不可讓未驗證主張顯示高證據可信度。

## 三、跨公司數字與可比性

只要文章用兩個以上 entity 的數字形成比較、排序或共同結論，meta 就必須設為：

```text
cross_company_numbers: true
```

每個「entity × observation」各建一個 `metric_comparison` block。不能用一個 block 塞三家
公司的數字，也不能只寫表格標題而省略期間、單位或定義。

```markdown
<!-- metric_comparison
comparison_id: M1
observation_id: M1-O1
claim_id: C4
entity: Microsoft
metric: free_cash_flow
reported_value: 19.6
value_kind: point
period_start: 2026-04-01
period_end: 2026-06-30
period_basis: fiscal_quarter
unit: USD_billion
definition_key: ocf_minus_cash_ppe
definition: 公司定義的 OCF 減 cash paid for PP&E
evidence_ids: S1
comparability: not_comparable
comparability_reason: 另一家公司揭露 TTM，且 FCF 扣除項目不同
normalization_method:
normalized_value:
normalized_unit:
-->
```

同一 `comparison_id` 預設為 `comparison_kind: aligned_metric`，必須：

- 至少有兩個不同 entity。
- 全部 observation 指向同一 claim、metric 與 comparability verdict。
- 各自附 `reported_value`、期間起訖、`period_basis`、unit、`definition_key`、完整 definition
  與 evidence IDs。

`value_kind` 預設 `point`，另可用 `range`（值寫成 `min..max`）、`lower_bound` 或
`upper_bound`；`reported_value` 必須是可重算數字，不能寫 `N/A`、`greater_than_25` 等
不可運算字串。`period_start`／`period_end` 描述這筆觀測實際成立的資訊期間，不得晚於
關聯 claim 的 `as_of` 或研究判定日；若數字是對未來年度的 forecast，將「預測涵蓋
CY2027」寫進 metric、`period_basis` 與 definition，觀測期間則記錄預測發布／資訊截點，
不可用未來日期偽裝成已發生 observation。正規化比較另須保存共同目標期間與
`normalized_definition_key`。

可比性值域：

- `directly_comparable`：期間、期間類型、單位與 `definition_key` 必須完全一致。
- `normalized_comparable`：原始口徑不同，但有可重建的 normalization method；每個 observation
  必須另填 normalized value／unit。
- `not_comparable`：不能可靠正規化。這是有效結論，正文不得再排高低榜或暗示精確差距。

`cross_company_numbers: false` 時不可放 `metric_comparison` block。多家公司出現在合作協議
中，不一定構成跨公司數字比較；但只要研究結論真的利用兩家公司數字，就不能以此例外規避。

comparison observation 採 append-only。既有 `observation_id` 的 entity、數字、期間、單位、
定義、來源與可比性裁決不得覆寫或刪除；來源改版、數字重編或定義改變時，追加新的穩定
`observation_id`。若共同 metric、目標期間、正規化方法或研究問題已實質改變，另建新的
`comparison_id`，保留舊比較作為當時可得證據的歷史紀錄。

若文章的結論正是「不同公司揭露的是完全不同的診斷量，不能冒充同一指標」，可明示
`comparison_kind: heterogeneous_evidence`。此時各 observation 的 `metric` 必須不同、
`comparability` 只能是 `not_comparable`，且 reason 要交代為何這組數字只能作證據籃子、
不能排名。這個例外不得用來逃避本來可以對齊的同一財務指標。

## 四、Monitor：把「接下來看什麼」變成可執行條件

每篇至少兩個 monitoring item。Monitor ID 使用 `T1`、`T2`……且保持穩定。

```markdown
<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C2,C3
metric: 客戶採用、量產出貨與收入認列
source_ids: S1,S2
watch_source_ids: S3
frequency: quarterly
next_check: 2026-08-15
trigger: 公司季報首次列出量產產品、客戶階段與可辨識收入
invalidation: 產品時程延後，或只有合作名單而沒有量產與財務足跡
-->
```

各欄用途：

- `claim_ids`：這個 monitor 裁決哪些主張。
- `metric`：實際觀察的產品、工程、營運或財務變數。
- `source_ids`：建立此 monitor 時所依據的當前／基線 evidence；它回答「為什麼現在值得
  追」，可以引用 `document` 或 `living_index`，但不是未來回查入口的替代品。
- `watch_source_ids`：未來實際重查的已登錄入口；每個 active monitor 至少要有一個，且
  所列 active source 中至少一個必須是 `source_kind: living_index`。不得只用不會更新的
  PDF、新聞稿或事件公告充當 watch endpoint。入口出現新附件時，另追加 `document` source
  並由 claim 引用；不可覆寫 living index 或把索引頁冒充附件。
- `frequency`：固定使用 `event_driven／weekly／monthly／quarterly／annual`；補充節點放在
  `frequency_detail`，不能填無法排程的自由文字。
- `next_check`：下一個明確研究日期。
- `trigger`：何種結果會增加或升級證據。
- `invalidation`：何種結果會推翻、縮窄或降級目前判讀。

topic 的 `review_due` 必須等於所有 active monitoring item 最早的 `next_check`。舊節點不
刪除，改成 `status: retired` 並填 `retired_at`、`retirement_reason`；retired monitor 不再
參與期限，也可以保留對 superseded source／claim 的歷史引用，且不要求仍有 active
`watch_source_ids`。影響路由的
`action_due` 可以不同，因為它管理的是公司筆記／H# 動作，不是 topic 新鮮度。

## 五、可信度與到期降級

meta 必填：

- `base_confidence: high|medium|low`
- `confidence_basis`：說明主命題的來源品質、獨立消息鏈、反方證據與主要缺口。

基準可信度是研究者對 `thesis_claim_id` 的明示判斷；它不是 claim 的真假標籤。系統另算
effective confidence：

1. `dismissed`／`resolved` 不做新鮮度降級。
2. active topic 以執行當下的**臺北日曆日**（`Asia/Taipei`）為 `as_of`；不得用 UTC 日期、
   儀表板資料日或作者手填的舊日期規避到期。當 `as_of > review_due`，且沒有發布時間較新的 active referenced
   evidence 時，**只自動降一級**：`high → medium → low → needs_revalidation`。
3. 自動降級不改 claim 的 `verified/inference/unverified`，不改 topic lifecycle，也不把
   任何主張自動判成 `refuted`。

到期當日已進 queue，隔日才反映降級。即使長期逾期也只做一次 freshness penalty，避免
把「沒有更新」誤當成反證。若查過但沒有新證據，只在 scan log 留下範圍與結果；不得更新
source `accepted_at`、`last_reviewed_at` 或把 `review_due` 往後推。只有新增且被 active claim
引用的可定位 evidence，才能刷新 evidence clock；同時必須重新設定 monitors 與 review due。

meta 時鐘亦採 evidence-gated mutation：`last_reviewed_at`、延後的 `review_due`，以及
`base_confidence` 的升級，都必須有新追加、被 active thesis claim 引用且晚於原 thesis
evidence clock 的來源，並追加對應 transition。單純重開網頁、例行掃描或「沒有新消息」
只能追加 scan log，不能刷新 meta。降低 `base_confidence` 可因既有證據重估或到期風險主動
進行，但仍須留下 transition 與理由。

`dismissed`／`resolved` 是關閉狀態：active monitor 應退役，時鐘凍結，不能只改 meta 假裝
重新啟動。重開必須先追加比關閉時更新的可定位 source，建立或更新 active claim 與 active
monitor，再追加 `dismissed/resolved → triaged` transition；該 transition 必須引用新
source ID，重新設定 `last_reviewed_at` 與 `review_due`，並完整保留原關閉紀錄。

## 六、從 topic 到公司結論的邊界

- 公司／平台列名合作只支持關係存在，不支持新增訂單金額、份額或獲利。
- 標準發布只支持技術選項存在，不支持產品採用、量產或具名供應商。
- 市場 TAM、CapEx、月營收、價格與籌碼只能觸發搜尋；不能直接成為公司 H# 終態證據。
- 跨產業需求到台灣公司至少要補「客戶／產品對應、量產階段、收入、毛利或現金流」中的
  可辨識證據；缺少時維持 `unverified` 或 group watch。
- Topic 若要 promoted 到正式筆記，仍須依 focused evidence pack 契約重做，不可把 topic
  source block 當成已完成獨立 reviewer。
- `policy_watch` 在尚未完成適用性、HTS code、豁免、原產地或公司暴露映射時，可以沒有
  `impact` block；此時必須維持 warning／watch，`stock_ids`、`group_ids` 可留空，且不得
  route 成 `formal_note_candidate`、promoted 或任何正式筆記動作。補齊可定位的公司層級
  impact evidence 後，才可追加 impact 並重新路由。

## 七、知識圖譜：把研究投影成關係，不另造一套事實

研究中心的知識圖譜只讀取已通過 topic／正式筆記契約的證據。它不以關鍵字共現、文章篇數、
同業分類或模型相似度自動建立公司關係；因此「沒有線」只表示目前沒有可發布的可追溯證據，
不表示現實世界不存在關係。

同一份底層 graph 分成兩個檢視，避免資訊混成毛線球：

1. `company`（公司曝險）：主題／產品與 universe 台股、外部公司或組織的關係。外部公司可
   顯示，但與 `config/universe.csv` 成員有明確視覺區隔。
2. `industry`（產業依賴）：主題與標準、元件、製程、能力、成熟度節點及正式族群的關係；
   此檢視不直接放公司。

線的「強弱」不能壓成單一分數，至少拆成四個正交維度：

- `evidence_state`：證實／推論／待驗證，決定實線、虛線或點線；不得強於引用 claim。
- `commercial_stage`：概念、樣品、資格、平台列名、生產、出貨、部署、財務認列等成熟度。
- `materiality`：未知、相鄰搜尋路由、具名產品角色、題材財務可直接歸因。圖上以同心環距離
  （越靠近中心代表目前證據支持的材料性越高）、節點標籤與分組清單三重呈現；線寬只作
  輔助提示，不承擔唯一判讀，也不得與證據強弱混為一談。只有下述 v2 `direct` assessment
  能進入財務內圈；空圈不表示不存在商業關係或公司財務曝險。
- `exclusivity`：未知、多路徑、少數來源、具證據的獨家。非 unknown 必須明示適用範圍；
  `unverified` 不得宣稱集中度或獨家。

每條 edge 至少要保存 `claim_refs` 或 `note_refs`、`boundary`、`next_trigger`、`as_of` 與
`review_due`。到期線會降透明度並標成需要複核，但「沒有新證據」不是反證，不會自動把
verified 改成 refuted；其上游 topic 可信度仍按第五節規則自動降級。點選關係時，研究中心
必須能回到原文章、claim 與一手來源。

讀者畫面不能把上述維度只排成一串無標籤 badge。關係清單至少直接標出「關係、證據、階段」，
詳情另標出「商業位置」，再以三題重排同一 edge：

1. 「這條線現在怎麼讀」只組合 endpoints、`relationLabel`、`evidenceState`、`materialityLabel`
   與 `commercialStageLabel`；不得增加 edge 沒有的公司事實。
2. 「還不能推到哪裡」逐字顯示 `boundary`。
3. 「看到什麼才升級」逐字顯示 `nextTrigger`。

每個有可見 edge 的投影可提供一條示範關係，固定優先未到期 verified、其次 verified、最後才是
第一條可見 edge；畫面必須同時聲明這只教讀法，不是重要性、受惠或投資排序。示範操作須把焦點
送到上述三題且避開黏性頁首；延伸閱讀只准開啟該 edge 已解析的 `articleIds`。這個 reader layer
不進知識圖譜 registry，也不能改變 edge、claim、source、evidence、materiality 或財務歸因。

### 財務材料性契約 v2：公司分母不等於題材分子

`financial_materiality` block 與 edge 分開保存。edge 回答「公司與題材為何相連」；v2 block
回答「已揭露的財務範圍有多大、能否歸因到這個題材」。每筆都必須保存：

- 穩定的 `assessment_id` 與 linked `edge_id`。
- `financial_scope`：`company_total`、`segment`、`product`、`unit_economics`。
- `metric`、`reported_value`、`unit`、`value_kind`，以及期間起訖與 `period_basis`。
- `denominator_metric`、`denominator_value`、`denominator_unit`；可比占比另存
  `share_percent`。`derived` 值必須附可重算 `calculation`。
- `metric_definition` 與 `denominator_definition`，明示會計科目、合併範圍、產品／事業部範圍。
- exact `source_refs`、`as_of`、`review_due`、`boundary` 與 `next_trigger`。

歸因狀態只有三種，不能用文字模糊帶過：

1. `not_disclosed`：只取得公司總額分母，題材分子未揭露。必須使用 `company_total`，不得填
   題材占比；公司總營收不能改寫成 AI、產品或族群收入。
2. `bounded_proxy`：取得較窄的事業部或產品值及同期間分母，但該範圍仍比題材寬。必須填可
   重算占比與明確 boundary；它表示評估已完成、等待更窄揭露，不是 direct 的較低分版本。
3. `direct`：同一期間與分母已能直接辨識題材收入、毛利、現金流或可重算的單位經濟貢獻。
   只有 `direct` 能連到 `verified／financial stage／materiality: financial` edge。

lint 會重算 `reported_value ÷ denominator_value`（容許公司百分比四捨五入 0.5 個百分點）、
檢查 source ref 必須已由 linked edge 解析、assessment 必須連到 universe company，並阻止
`company_total` 或 `bounded_proxy` 升格成題材財務內圈。若公司沒有產品級揭露，正式結果就是
`not_disclosed` 或 `bounded_proxy`；不得以同業推估、市場 TAM 或公司總額補洞。

族群成熟度矩陣把「已做 v2 評估」與「題材可直接歸因」拆成兩個欄位。未評估族群保留一件
根因去重的 open task；已完成 `bounded_proxy／not_disclosed` 的族群轉為「等待題材分母」
watch；只有 `direct` 才關閉財務歸因缺口。這些都是 registry census，不是投資分數或抽樣估計。

節點 registry 分三層：`config/knowledge_concepts.csv` 保存專有名詞與製程節點，
`config/external_entities.csv` 保存不在 universe 的公司／組織，台股公司與正式族群則直接由
`config/universe.csv`、`config/groups.csv` 注入。顯示關係保存在
`notes/knowledge_graph/*.md`；新增主題先複製 `_template.md`。MVP 每條 active edge 只允許
root 的一跳關係，先把證據品質與可讀性做穩，再考慮多跳探索。

發布前執行 `python scripts/knowledge_graph.py --lint`。lint 會檢查 endpoint、值域、雙視圖、
一跳限制、來源引用、證據不可升格、財務材料性 v2 與 exclusivity 邊界；它不重新下載來源，
也不替代內容 reviewer。讀者導覽另要求每張 active graph 至少保留一個既存 `article_ids`；
發布頁只能從這個欄位建立「先讀主題文章」，不得用關鍵字或模型相似度補出新的文章關係。
文章的路線定位與「沿學習路線往下讀」同樣只能依已發布 route 的 graph 順序，並以每個 graph
第一篇可解析的既存 `article_ids` 作為一個主題站；不可把同圖的補充文章多算成站次。頁首須顯示
路線與目前站次；下一站卡須在正式 route question 後逐字重用目前文章
`readingMission.keyPoints[0]`，讓讀者先辨認這一站替整條問題補上什麼，再看原 graph／phase
閱讀順序，不得重寫成新的結論。桌機並排的自我檢查與下一站卡不得互相強制等高。末站須明示只
完成閱讀順序、不代表研究結論完成，且返回圖譜時須從頂端開始。
這是編輯閱讀次序，不是 evidence edge、公司曝險、供應鏈或受惠關係，畫面必須把邊界寫給讀者。

## 八、修正採追加保存

研究結論改變時，不刪除舊 source、claim 或 transition，也不重用其 ID：

1. 追加新 source，保留新的 locator、limitation 與 accepted date。
2. 舊 claim 改為 `superseded` 或 `refuted`，並在 `corrected_by_claim_id` 填新 claim ID；
   它可以繼續引用非 active 的歷史 source。`resolution` 不承擔這條關係。
3. 追加 active 新 claim，以新 ID 寫精確的新結論；`correction_kind` 填 `supersedes` 或
   `refutes`，`corrects_claim_id` 填被修正的舊 claim ID，`corrected_by_claim_id` 預設留空。
   `basis` 另以 `correction_of:C1` 說明本次重新判讀；結構化關係仍以前述三欄為準。新舊
   兩端必須雙向對齊。
4. 若主命題改變，meta 的 `thesis_claim_id` 指向新 claim。
5. 舊 monitor 改為 retired，追加新的 active monitor；只有 active monitor 決定 review due。
6. 追加同狀態 topic transition（例如 `triaged → triaged`），寫明原因及 evidence source IDs；
   不得覆寫既有 transition。
7. 正文明示「原判讀、何時被什麼證據修正、目前仍未知什麼」。

修正可以有多代：例如 C4 修正 C1，之後 C7 再修正 C4。此時 C4 同時保留
`correction_kind`／`corrects_claim_id: C1` 與 `corrected_by_claim_id: C7`；不得把 C4 改寫成
直接修正 C7，也不得壓平、刪除中間一代。每一代只連相鄰 claim，才能重建當時的判斷。

transition 的 evidence 也有固定契約：只有第一筆 `initial → inbox` 可以使用
`evidence: source_chain:<meta.source_chain_id>`；其後所有 transition 一律使用
`evidence: sources:S1,S2` 形式引用已登錄 source ID。

唯一的例外是**可讀性改寫**（2026-08-08 起）。原本已發布文章要改正文，只能追加綁定
sources 的 revision transition——等於預設每次改寫都由新證據驅動。純粹把文章寫得更好懂
並沒有新證據，於是唯一的路是假裝有，結果是文章一旦難讀就永遠難讀。此時可追加
`evidence: editorial:<slug>` 的同狀態 transition，但它受三重限制：lifecycle 狀態不可改變；
所有 source／claim／comparison／monitor 必須逐字不變；`thesis_claim_id`、`base_confidence`、
`review_due`、`last_reviewed_at`、`stock_ids`、`group_ids`、`route` 等 meta 也必須不變。
只要同時動到其中任何一項，這個窄口即失效，必須改用綁定 sources 的 revision。
它記錄的是「敘述重寫、結論未變」，不刷新任何時鐘，也不是修正鏈的一環。修正、關閉、重開或 meta 時鐘變動都
不得再用自由文字或 `source_chain:` 取代實際 evidence。

歷史方法快照若用較早的 `as_of` 重播，可保留快照日之後追加的同狀態 `editorial:<slug>` 記號，
不得因此把當時原本合格的研究判成品質不合格；因為這類記號不改研究狀態、帳本或時鐘。這個例外只
適用於歷史重播：當日 lint 仍會拒絕日期晚於臺北今天的 editorial transition，綁定 sources 或會改變
lifecycle 的 transition 也一律不得越過 `as_of`。

`scan_log.csv` 與 comparison observation 同樣 append-only：新的掃描窗口、coverage、結果、
限制與下一期限只能新增一列；不得回頭改寫或刪除舊 scan row。若更正記錄錯誤，追加明確
指向舊 scan ID 的 correction row，在 `coverage_note` 寫
`correction_of:<old_scan_id>`，並保留原始紀錄。

Git 歷史能看到文字變更，但不能以 Git 歷史取代文章內的修正鏈；研究中心讀者必須在當前
版本就能理解結論為何改變。CI 另以 `--baseline-ref` 比對 Git 前版：既有 source、claim、
monitor 的 immutable 欄位及 transition 前綴不可刪改；只能新增 ID，或把 lifecycle 單向
改成 superseded／refuted／retired 並補齊雙向修正關係。

唯一的例外是 claim 的 `supporting_source_ids` 與 `contrary_source_ids`：自 2026-08-08 起
改為**只可追加**（既有 ID 的順序與內容必須逐字保留為前綴），且追加來源的 effective
published date 必須 `<=` 該 claim 的 `as_of`。這個例外只開放「事後才找到、但本來就已存在」
的佐證回填；發布日晚於 `as_of` 的來源屬於新證據，仍須依第八節另立新 claim，讓結論措辭
重新被推導一次。開放這個窄口是因為原本完全凍結的清單，使「補上第二條獨立來源鏈」只能
借用 supersede 完成，而那會在方法帳本上記錄一次從未發生的修正、汙染修正學習的計數。

## 九、方法本身也要留下可回測的歷史

文章逐篇通過 lint，只能證明欄位與引用完整；它不能回答研究是否有回頭檢查、是否願意
承認沒有新證據，或錯誤是否真的被修正。方法層另使用：

- `notes/research_method_reviews/YYYY-MM-DD_NN.json`：append-only 稽核快照，保存當時的
  topic、claim、source、monitor、圖譜、候選雷達與 scan log 覆蓋。registry 有任何變動都
  要新增快照，不得改寫舊檔；scan row 也納入 fingerprint，避免文章有更新、掃描責任卻未
  留痕。
- `notes/research_method_reviews/monitor_reviews.csv`：append-only 到期檢查帳本，每列連到
  既有 topic／monitor，結果只能是 `new_support`、`new_contrary`、`no_new_evidence` 或
  `not_yet_testable`。
- `notes/research_candidates/selection_log.csv`：append-only 研究前選擇帳本；把初始選擇、
  第一拒絕與下一份證據和研究後 route 分開，使日後能檢查 selection drift 與事後重排。
- `scripts/research_method_audit.py`：驗證 snapshot fingerprint、review 引用與歷史不可改寫，
  並在研究雷達顯示選題前承諾、可追溯、獨立交叉驗證、可證偽、新鮮度、修正學習、
  掃描覆蓋問責、財務材料性 v2 與校準可用性九道
  gate。獨立交叉驗證會直接列出仍缺第二條消息鏈的 topic ID，避免缺口被總體比例掩蓋；
  兩條來源鏈只代表降低單一來源偏誤，不代表多數決或主張已被證真。

掃描覆蓋問責把 `full`、`partial`、最新全域 cadence 是否逾期與最新 scan ID 分開揭露。
只有至少存在一筆 `full` 且最新 cadence 沒有逾期時才可通過這一 gate；`partial` 是誠實的
主題式抽樣，不是失敗，但不能用來宣稱全 universe 或全市場沒有漏網題材。舊 scan row 是
不可變的歷史事件，不把每列已過的 `next_scan_due` 永久累加為逾期；在建立 scope lineage
之前，也不宣稱個別歷史 scope 已被後續掃描完整覆蓋。這個 gate 只檢查工作範圍有沒有被
如實記錄，不證明每則公告都被看見或正確解讀。

交易所重大訊息日端點是**不保留的單日批次**：它只帶一個出表日期，實測全部列的發言日期
只有出表日期減一那一天，批次更新後舊發言日永久消失。因此逾期的窗口不能靠「之後再重跑
一次」補回——重跑讀到的是另一天的批次。`full` 除了日期算術，還必須有該批次實際觀測到的
發言日期落在窗口內；批次已滾過窗口時維持 `partial`，並在 coverage_note 說明缺口只能沿用
當時真的讀到該日的 scan row。把 `next_scan_due` 排到端點不會前進的日子（例如週末）只會
再產生一列相同的 partial，不會關閉缺口。

同一天若出現新反證，可以用新增 source、append-only correction claim 與綁定該 source 的
revision transition 立即修正 `thesis_claim_id`；日期相同不應阻止修錯。這種同日修正不得
順便延後 `review_due`、提高 `base_confidence` 或刷新 `last_reviewed_at`，後三者仍要求
accepted date 嚴格晚於舊主命題 evidence clock。

`no_new_evidence` 是有效的回顧結果，但**不得**刷新 topic source 的 `accepted_at`、
`last_reviewed_at` 或 `review_due`。它只在方法帳本設定下一次工作期限；原文章仍照既有
evidence clock 降級，直到真的有新 evidence。

候選升格數、文章數與圖譜線數是研究產出，不是正確率。只有到期 monitor 全數留下 review
event，且至少三個結果帶有新證據時，audit 才允許分列 `new_support／new_contrary` 與 N；
**不計算支持率**。`new_support` 只表示該 monitor 找到支持其檢查方向的新證據，現有 outcome
schema 尚不能把它等同於主命題為真，更不是投資命中率、報酬率或因果效果。樣本不足時只報
counts 與 `not_ready`，不補零、不把未到期主張算成功。

## 十、發布前檢查

1. 清單卡與文章頁首是否先用 `config/research_topic_guide.csv` 的人工中文問題交代本文要解開
   什麼，原技術標題是否完整保留為次要「研究題名」；導覽是否精確覆蓋全部發布市場議題，且沒有
   回寫原 topic、替換閱讀任務或被誤當成 claim／source。清單卡 DOM 與視覺是否都先放「讀完能
   回答」，才放同篇既有重點；卡尾是否用「目前怎麼看」保留查核資訊。文章側欄與窄幅文末的
   `topicStatus`、priority、日期、可信度與來源是否預設收進原生「文章查核資料」，並明示 priority
   只排研究工作、不代表重要性、預期報酬或投資順位；展開後原欄位與來源是否仍完整可回查。
   標題與查核警語後是否再用「新手閱讀任務」
   指出本文先釐清的情境／問題與讀完問題；兩段文字是否
   可逐字回查同篇「為什麼重要」開頭與「想一想」第一題，而非另寫無 claim／source 邊界的摘要。
   已列入白話升級的「為什麼重要」是否以作者明寫的粗體短主句建立段落錨點、長句是否已拆開；
   renderer 是否只辨識第一個粗體 run 而未自行摘要。若改動歷史正文，是否追加同狀態
   `editorial:<slug>` transition，且 baseline lint 證明所有帳本與鎖定時鐘不變。
   主正文若有三個以上連續的多步機制，是否從該節第一個 block 起以作者明寫的中文粗體主句建立
   「本節先看」；renderer 是否遇到非段落或非粗體段首即停止、少於三項完全不顯示，並只逐字
   重用 bold run。卡片是否排在同節名詞與完整原段落之前，編號只表原文順序並明示不代表重要性、
   上下游或因果；新手導讀、研究摘要、查核附錄、正式筆記與多空小作文是否維持不套用。
   主正文表格若最左欄名含「位置／環節／節點／路徑」且有 3–8 個非空、不重複 row，是否把
   `row[0]` 逐字集合成「系統位置索引」，讓讀者先看本文檢查哪些位置再逐列核對；是否完全不讀
   其餘 cell 生成摘要、不改 row 順序，並明示編號不代表上下游、流程一定相連、重要性或受惠排序。
   同表在窄欄改成 row 卡時，第一欄是否把同一順序延續為 `位置 N／總數`，並保留原 `th`、原欄名
   metadata、視覺與輔具共用的實際文字節點及完整原 cell，且沒有 CSS generated label 重複朗讀；
   其餘欄與一般表格是否仍逐字使用原 `th` 標籤。系統表窄欄的每個 cell 是否改為全寬內容段，
   依欄序顯示 `01 · 先定位／NN · 接著看／NN · 最後核對` 與同欄原 `th`；固定 cue 是否對輔具
   隱藏而保留原生 table header 語意，且沒有刪欄、摘要 cell、交換 row 或把最後邊界收合。
   系統表後若緊接純文字段落，是否只在原文能唯一切成「前置原則／`這張表只…`／`它不能…`」
   三個非空片段時顯示表後收束卡；三卡文字串接是否逐字等於正規化原段，原段含連結／粗體、
   任一片段過長、句型不完整、不是緊接系統表或非 topic reader mode 時是否完全不轉換。標籤是否
   只說「先記住／能說到這裡／先不能說」，沒有讀 table cell、題名、族群、route 或模型生成摘要。
   若同表正文列入白話升級，欄名是否改成「目前看到什麼做法／證據走到哪一步」這類短問法，
   cell 是否改用明確主詞與動詞，並逐列保留 reference design、資格驗證、量產與客戶採用的原始
   成熟階段；是否追加 `editorial:<slug>` transition，且 source／claim／monitor／鎖定 meta 未變。
   若文章把市場需求、元件／設備工作量與個別公司財務串在一起，新手導讀是否逐項寫出三道證據
   關卡，並明示市場規模、年化營收、容量承諾與相對效能不能直接推成公司訂單或獲利；跨公司數字
   若判為 `not_comparable`，正文與表格是否仍用完整主詞、動詞與原始單位說明，而沒有改畫成排名。
   學習路線中的公司財報案例是否真的有主正文，而非由研究摘要直接跳到延伸閱讀；是否先分開
   公司總額、獲利結果、應用占比與產品數字的分母，再依序檢查價格、產品組合、成本與稼動率，
   最後把公司總額、題材歸因與個股結論分層。國巨 Q2 案例是否維持「四組數字 → 四種毛利原因 →
   三層判讀」三節、各至少三段作者粗體主句與一張能說／不能說邊界表，且 editorial transition
   之外的 source／claim／monitor／topic lifecycle／confidence／鎖定時間完全不變。
   不符確定性條件時是否退回既有欄名導讀；兩種提示是否都不寫回 Markdown、table、claim 或來源。
   清單是否完整枚舉三類發布文章並先顯示問題：topic 逐字取 `readerQuestion`，正式筆記／多空
   小作文逐字取 `readingMission.question`；待驗命題與研究題名是否仍完整保留為次要文字；正式
   筆記原摘要若與首個重點在移除 `[S#]`、空白及標點後互相包含，是否不再重複同一段，且只有兩者
   確實不同才顯示「原始摘要」。沒有問題時是否退回舊格式，而且沒有從正文、題名或搜尋字生成
   替代問句。
   點入每張卡後，文章 `h1` 是否逐字延續同一問題；原 topic 題名是否標為「研究題名」，正式
   筆記／多空文章原 `readerTitle` 是否標為「原研究頁名」，而沒有另建第二份首屏問題或改寫 payload。
   正式筆記是否改從既有「30 秒摘要」前 1～3 點建立同型任務，多空小作文是否改從既有「勝負手」
   3 點建立任務；兩類問題是否只用固定讀法句型與既有公司名稱，沒有讀正文補寫結論；任一發布文章
   缺來源時是否停止建置。任務卡與文末提示是否分別定位「30 秒摘要／多空觀點／勝負手」，並把
   鍵盤焦點放在黏性導覽下方；沒有結構化來源的事件錨點是否維持不生成，避免從長文抽句。
   兩句若命中同篇字典或研究中心共通語，是否先以預設收合的「先認得這兩句的 N 個詞」逐字重用
   同一筆定義與邊界、同詞只列一次；完全沒有命中時是否不顯示空入口，也沒有另寫解釋。
   兩句若含 `[S#]`、多空文章裸 `H#`、季度／半年、MOPS 或已允許的研究分類名稱，是否只由
   固定規則產生 `readerNotations`，以「先解碼這段的 N 種符號」逐項說明字面與判讀邊界；
   `H#` 假說與 `YYYYH#` 半年是否分開。正式筆記首個重點是否只把 `[S#]` 移到獨立「原文來源
   標記」列，正文、來源區、原始檔與 payload 是否仍保留全部 token；已換成中文的內部分類是否
   不再顯示指向不可見 token 的解碼項。沒有符號時是否不顯示空入口。展開摘要是否至少 44px，
   Enter／Space 都能切換；80 字以上重點是否只在既有中文分號或句末標點後加入零文字停頓，而
   沒有改寫、截斷或重排字詞。
   任務卡是否在兩句任務後立即顯示至少 44px 的主要閱讀行動，再放符號、名詞與背景說明；市場
   議題的既有三句是否只按原順序附上「先看資料／再補脈絡／最後看邊界」讀法標籤，沒有把標籤
   當成新 claim、證據分級，或改動任何句子與來源。
   市場議題只要有一般正文，任務卡是否另提供次要「直接讀第一節」行動；其 section index 與
   accessible name 是否逐字對回 `topicReaderSectionItems(article)[0]` 的第一個既有 H2，點擊後
   是否同步移動焦點並停在手機／桌機黏性導覽下方。正式筆記、多空小作文、事件錨點與無正文文章
   是否維持 0 顆；中間全部導讀、角色、路線、字典與摘要是否仍在原 DOM 順序，沒有因捷徑而刪除、
   改寫、收合或回寫閱讀進度。
   閱讀任務後的「這篇目前能說到哪裡」是否優先逐字取同篇「三句話抓重點」第一句、最後一句與
   「接下來怎麼追」第一項，依序標成「先知道／先別下結論／接著怎麼查」；完整研究摘要是否仍
   保留 ledger 層級的原始主張、待驗命題與 monitor 文字。若任一白話來源不存在，是否安全退回
   原研究摘要而不抽句或補寫；一般桌機正文欄不足時三卡是否改為單欄，專注閱讀寬版仍可並排比較。
   這個 reader-only 提前層不得改寫 topic Markdown、summary、claim、source、confidence、monitor、
   route、graph 或公司曝險。
   正式筆記與多空小作文進入主正文後，每個非空原始 section heading 下是否都有一行
   「這節先看」；用途文字是否只由文章類型、canonical heading／前綴／正則與固定兜底產生，
   沒有讀正文、題名或公司數字生成摘要。原 heading、blocks、來源與 payload 是否不變；市場議題
   是否維持 0 張此類提示，避免和既有新手段落、研究摘要重複。
   市場議題 reader mode 若命中 fenced `text` 推論鏈，是否只在原文已有 3–8 個由 `→` 分隔的
   非空項目時改成語意化 `<ol>`；每項文字與順序是否逐字不變，fence／箭頭以外的內容是否沒有
   增刪，原始 Markdown、runs 與 payload 是否完全保留。非 reader mode、其他 fence 或不符合項目
   範圍時是否安全退回原顯示，而沒有從一般技術文字推導新流程、因果或投資關係。
   市場議題 reader mode 若命中四項 KPI 判讀清單，是否同時要求 `ul`、四項、首段粗體、固定標籤
   與順序、以及每項冒號契約；實際 DOM 是否為帶非空標籤的 `<section>` 與 `<dl>`，四個 `<dt>`、
   `<dd>`、位置 1–4 是否逐字對回原項目。固定「先看／再看／避開／分辨」是否只解釋原標籤角色，
   沒有新增產業、公司、數字、方向或結論；其他清單是否完全不命中。
   完整新手導讀是否依讀者畫面順序先交代三句重點與重要性，再以預設收合、可隨時展開的名詞
   小字典提供完整解釋，並讓追蹤節點與問題在收合狀態直接可見，
   正文捲過原字典後是否仍可由桌機大綱或窄幅浮動按鈕開啟名詞速查；速查詞數、搜尋與內容是否
   逐字共用同一份字典 list runs，沒有字典的文章是否完全不顯示入口；一般正文各節若命中同篇
   字典詞，節首是否只列該節標題／段落／清單／表格真正出現的詞，點擊後是否直接篩出同一筆
   原始定義，沒有命中時是否不顯示空容器；同節命中 1–3 個是否直接完整顯示，4 個以上是否以
   預設收合的原生 `details` 明示「名詞先不用背／先讀內容」，展開後是否一次保留原字典順序的
   全部命中詞，而沒有刪詞、改序、挑選「重要詞」、另寫定義或建立第二層剩餘詞；收合時內部詞鈕
   是否不進 tab order，手機 summary 是否至少 56px，開詞、關閉與返回焦點是否不改文章位置；
   一般市場議題進入第一個主正文
   H2 前是否只顯示一張「回到這篇要回答的問題」，其問題是否逐字等於同篇首屏與文章清單既有
   `readerQuestion`，第一個主正文 H2、正文、研究摘要與 payload 是否不變；事件錨點、沒有主正文、
   第二節以後、正式筆記、多空小作文與非 reader mode 是否完全不顯示，且沒有讀 blocks、題名、
   族群、graph 或 route 另寫問題；同篇主正文若有至少三節的第一張表分別以完整且不重複的
   「本文 N 個位置／把尺／個時鐘／類角色／關」起首，正文前是否恰有一張文章級讀法地圖，
   label、順序、目標 H2 是否逐一沿用原 table header 與 section，按鈕是否可聚焦並定位原章節；
   少於三種、重複 kind、事件錨點及其他文章類型是否安全不顯示，且固定用途文案沒有讀 row、cell、
   其他 blocks、題名、族群、graph 或 route 推寫內容，並明示順序不代表上下游、因果、成熟度或
   投資排序；市場議題主正文若有 `n` 個
   有效章節，第二節起是否恰有 `max(0, n-1)` 張「章節接力」，每張 previous／current heading
   是否逐字等於相鄰原 H2，第一節、單節文章、新手導讀、研究摘要與查核附錄是否完全不顯示；
   接力文案是否明示只代表文章先後、不代表上下游、因果、成熟度或投資排序，且沒有讀 blocks、
   題名、族群、graph 或 route 另寫摘要，
   並由緊接的研究摘要以具名卡片回答一句話結論、目前已知、尚未知道、影響範圍與下一步；五張卡
   是否仍逐字對應 generated blocks，而非重新摘要或用顏色代替文字標籤；
   導讀後是否只在五項摘要完整且唯一時，提前逐字顯示「一句話結論、尚未知道、下一步看什麼」，
   同時保留 active 主張類型與即時可信度兩把尺；「看完整研究摘要」是否把焦點送回原摘要標題，
   名詞行動是否只開啟同篇既有字典。缺欄、重複、非市場議題或沒有字典時是否安全不顯示，而沒有
   自正文推寫替代內容、改變完整摘要、Markdown、payload 或查核狀態；
   新手導讀是否沒有直接暴露內部狀態碼、未解釋英文與過長段落；前三句與「為什麼重要」是否先用
   一般讀者能理解的事實、差異與限制說話，而不是用「可定位的新數字」、「更新正式研究」等維運
   動作代替內容。純可讀性改寫是否另留同狀態 editorial transition，且沒有改變 claim、source、
   confidence、monitor、route、graph 或公司曝險。
2. 每個材料性 claim 是否有正確標籤、來源 ID、basis 與 boundary。
3. `verified` 是否只重述來源直接支持的精確措辭。
4. 是否主動找過競爭者、替代方案、政策附件或財務附註等反方來源。
5. 跨公司數字是否逐 observation 記錄期間、單位、定義及可比性。
6. 財務 assessment 是否明列 scope、期間、分子、分母、定義、exact source、歸因狀態與
   boundary；公司總額與有界代理是否仍被擋在題材財務內圈之外。
7. 每個 monitor 是否分開記錄基線 `source_ids` 與未來 `watch_source_ids`，且 active watch
   至少包含一個 living index，並具備頻率、日期、trigger 與 invalidation。
8. `review_due` 是否等於最早 monitor 日期，且晚於 `last_reviewed_at`。
9. impact 是否仍清楚寫 evidence boundary，沒有把 topic 升格為公司事實。
10. Active radar 是否先有同 cycle 的 selection log，且初始 rank、第一拒絕與下一份證據沒有
   因深研結果回寫；所有 retired schema 2 radar 是否仍可逐輪核對；未到期重選是否留下新的
   `early_trigger`；執行 `python scripts/research_radar.py --lint`。
11. 執行 `python scripts/research_queue.py --lint` 與 `python scripts/knowledge_graph.py --lint`；
   lint 只驗結構與引用完整性，不會重新下載或證明來源內容為真。
12. 執行 `python scripts/research_method_audit.py --lint --baseline-ref HEAD`，確認 registry
    有新快照、舊快照未被改寫，review 與 selection ledger 也只追加新列。
13. **執行 `python -m unittest discover -s tests -q`——四個 lint 全過不等於測試會過。**
    lint 驗的是當前 register 的結構與引用，測試另外綁了幾個必須隨每輪發佈同步的常數；
    只跑 lint 就推，CI 會在 push 之後才轉紅。已知需要每輪確認的有：
    - `tests/test_research_method_audit.py` 的 `as_of`：必須 `>=` 本輪新 topic 的
      `captured_at`，否則新文章會被判為尚未存在、品質不合格，並讓整個 `setUpClass`
      error（連帶使其下所有測試靜默不執行，紅字看起來只有一條）。
    - `tests/test_research_queue.py` 綁定的最新 `scan_id` 與 `next_scan_due`。
    - `test_research_method_audit.py` 的帳本累計數：`reviewedMature`、
      `monitorReviewEvents`、`resultCounts`、獨立交叉驗證缺口名單。其中
      `supersededOrRefutedClaims` **刻意不隨佐證回填改變**——它變動就代表有人用
      supersede 假造了一次修正，應視為警訊而不是要更新的數字。
    測試若因「本輪候選張數不同」而紅，正確做法是把寫死的張數改成與凍結帳本對應的
    不變式，不是每輪改一個數字。
14. 重建研究中心並檢查可信度、知識圖譜財務面板與 deep link 的桌機／行動版顯示。首次進入、
    尚未搜尋／篩選／開啟文章時，三步起點必須能分別前往族群矩陣、只看市場議題與知識圖譜；
    窄幅首次載入同樣預設展開，明示最新更新不是推薦順序，並逐張重用全部既有
    `groupMaturity.learningRoutes` 問題與第一站；每張捷徑須一鍵開啟可解析的正式第一篇文章，
    保留 `maturity-route` 返回脈絡；進文後頁首與行動版展開內容須逐字保留同一 route question，
    不得只留下路線 label。讀者手動收合才可保存為本地顯示偏好，resize 不得覆寫；
    不得因首頁捷徑另寫問題、猜測文章或改動路線／證據 payload。開始搜尋、篩選或閱讀後導覽即
    隱藏。未編入固定路線的已發布市場議題，須在文章前段逐張重用同篇既有 `learningPath.cards`
    明示「目前沒有固定站次」與可用的 graph／article／collection 延伸入口；只有 collection 時須
    明示尚無可回查圖譜，不得用題名、正文、族群、相似度或模型補 route／graph 關係。跳轉行動只
    前往同篇「從這篇接著學」，已有正式 route 的文章不得疊加未編路線提示。行動版不得產生水平
    溢出。進入知識圖譜後，必須先用白話說明
    「學習路線、中心主題、投影視角、關係來源」四步；行動版只顯示當前路線的主題選擇器，不先堆疊
    全部 graph 按鈕。窄幅首次載入須把四步讀法與完整控制分成兩個可由鍵盤操作的原生展開區，預設
    摘要要先顯示用途與目前路線／主題／視角／證據；完整內容仍須可展開，且切換篩選後摘要同步更新。
    控制之後另須固定顯示「目前讀圖任務」，逐字串起正式 route `question`、目前 phase `purpose` 與
    active graph `summary`；切換路線／主題後三層都要更新，行動版改單欄且保持可見。圖譜主介紹
    只保留共通讀法，不得再重複同一 graph 摘要，也不得從 edge、公司、正文、相似度或模型補寫問題、
    階段任務、供應鏈、受惠或投資排序。
    收合只在首次載入判斷一次，不得用 resize 自動覆寫使用者狀態。學習路線必須完整覆蓋目前 graph，
    但只是導覽 taxonomy，不能改變 edge、證據層級、
    公司映射或財務歸因；每條路線須明示建議閱讀順序，每張 graph 的「先讀主題文章」須能解析到
    已登錄的 `article_ids`，不得另行推測文章映射。路線內文章須以每個 graph 的第一篇既有文章
    作為一站，頁首與圖譜路線數字必須一致；下一站須由同一份 route＋`article_ids` 推導、顯示站次
    並能實際開啟。矩陣路線卡與文章站次定位都須提供原生 `details` 路線地圖，逐站逐字重用 graph
    label、第一篇既有文章及該文 `readingMission.question`；顯示時須以問題為主標、以
    「研究節點：graph label」為次要脈絡，最小觸控高度 72px，且無障礙名稱同時包含兩者。
    目前站用 `aria-current="step"`，任一站
    都能直接開文並回到頁首。單一圖譜入口須標為「看這站證據關係」並明寫實際投影，不得冒稱
    完整路線；多族群文章且有 industry edge 時須先開產業依賴，單族群或只有 company edge 時先開
    公司曝險，company edge 缺席時則安全退回既有產業依賴。此判斷只能讀既有 groups 與 edge view，
    不得以 edge 數量或文字相似度決定；兩種結果都須提示仍可在圖內切換視角，按鈕在桌機與手機
    都不得低於 44px。由多族群文章抵達其產業依賴圖時，origin 卡另須逐一把 article group 只依
    node `groupId` 對回唯一 industry edge，並逐字顯示已登錄的族群問句、edge 證據層級及商業位置；
    恰好一條才可操作，0／多條不得自動挑線。點擊須直接開同一 edge 的三步關係解讀；公司視角、
    直接 deep link、單族群文章或已切換到其他 graph 時不顯示。
    在任一唯一角色 edge 的三步解讀下方，繼續以同一 article group 順序、候選問句與 edge 狀態
    顯示「文章角色比較」；目前角色須用 `aria-current="step"` 且 disabled，其他唯一 edge 可用
    click、Enter 或 Space 原位切換並把焦點留在更新後的關係詳情。0／多條仍 disabled 且不猜線。
    詳情導覽只限同篇 article-learning origin、同 graph、多族群、industry 投影；直接 deep link、
    company、單族群、不同 graph 或非文章來處都必須為 0。所有按鈕至少 44px，窄幅不得水平溢出，
    並明示角色順序不代表上下游、受惠、訂單或投資排序。末站須
    提供清楚的完成與返回路線狀態；「看這站證據關係」須和文章延伸圖譜卡共用 article-learning
    origin，但另記 `route-context` 來源，讓圖譜首屏能回到同篇、同一閱讀位置與同一按鈕，並保留
    原本矩陣路線。不得改用相似度或熱門度排序。每個路線
    主文章另須由既有「為什麼重要」與「想一想」產生首屏閱讀任務；任何主文章缺卡都必須讓建置
    失敗。閱讀任務兩句須共用逐句重點的確定性名詞比對與同一份定義 renderer，本文字典優先、
    共通語只補研究流程與常見指標，合併後去重；命中才顯示預設收合提示，未命中不得插入空容器。
    新手完整段落的畫面順序須是「三句重點 → 為什麼重要 → 名詞小字典 → 接下來怎麼追 →
    想一想」；名詞小字典須用原生 `details` 預設收合、顯示詞數、可由鍵盤展開，且展開後不得
    缺少任一原始定義。一般正文節的「本節先認得」只能由同節 heading／blocks 文字與同篇字典
    粗體詞名做確定性比對；詞鈕須開啟同一 dialog 並以完整詞名預填搜尋，不得另存定義、使用模型
    相似度或插入未命中的詞。同節命中 1–3 個時直接完整顯示；4 個以上時以預設收合的原生
    `details` 明示先讀內容，展開後須依原字典順序一次顯示全部命中詞，不得挑詞或另建第二層
    剩餘詞清單。新手段落、研究摘要與查核附錄不重複插入。研究摘要須以「一句話
    結論」全寬主卡加四張驗證卡呈現；只有五個預定標籤
    完整、唯一時才可轉換，卡片的文字與順序不得改寫，語意結構須保留 list／listitem 與 H3 標籤。
    來源 Markdown 與 ledger 不得因此改寫。圖譜有可見 edge 時，須提供明示非排名的關係示範；
    關係列須標示「關係／證據／階段」，詳情
    須逐一顯示由既有欄位組成的「現在怎麼讀」、逐字 `boundary` 與逐字 `nextTrigger`。示範後焦點
    必須落在詳情且不被黏性頁首遮住；完整研究按鈕只能解析同 edge 的 `articleIds`。
    從文章的圖譜卡或「看這站證據關係」開圖時，首屏是否明示剛才文章與下一站；返回後是否依來源
    恢復同一延伸卡或路線按鈕的位置、焦點及原本矩陣起點；關係解讀末端是否也能用至少 44px 的
    按鈕回到同一位置並繼續下一站；直接圖譜
    入口是否不會誤顯示這份一次性脈絡，也沒有把導覽狀態寫進 payload。另以 1280×720 檢查詳情
    `clientHeight == scrollHeight`、只由圖譜頁捲動；從下方關係清單換線時須聚焦並露出新詳情。
    文章預設先進專注閱讀，正文後的「從這篇接著學」只能連到現有文章、本文宣告族群或可追溯
    圖譜關係；學習路線主文章須在這裡逐字重問同篇「想一想」，提示逐字重用同篇「三句話抓
    重點」且預設收合，下一站問題逐字取自下一篇 route 主文章。非末站是否另以兩步 ordered list
    逐字顯示目前站與下一站的 graph／phase label，且明示這只是閱讀順序、不代表供應鏈、受惠或
    因果關係；兩步次序之前是否逐字重顯同一正式 route 的 `question`，讓跨 phase 時仍能回答原本
    的系統問題；不得用題名、相似度或模型補 label、question 或建立 edge。末站完成卡是否逐字收回
    route `question`、`description`、全部 phase label 與各 phase 的原 graph 站數，並明示這是閱讀
    總複習，不代表已掌握、研究結論完成或產業關係已證實。缺任一必要項即停止建置。回看操作
    須把「三句話抓重點」放在黏性導覽下方並移入鍵盤焦點；下一站須顯示站次、開啟正確文章並
    回到頁首。延伸區自身不足 620px 時，理解檢查、下一站與其餘延伸卡須全部單欄；寬專注閱讀
    才能並排。另從只命中目前文章的搜尋結果開文，驗收下一站仍可切到不符合該搜尋的正式文章，
    hash、H1 與站次同步更新；左側原搜尋不被清空，並顯示目前文章不在結果中，返回清單後聚焦原
    選文。另逐一核對非 route 的文章推薦卡：必須顯示由兩篇現有 `stockIds` 交集產生的共同
    公司；沒有共同公司時才顯示 `groups` 交集，超過三個須可展開全部。兩種交集都沒有就停止建置，
    不得用題名或相似度補理由；畫面須明示共同標記不等於上下游、受惠、訂單或因果關係。每張一般
    推薦還須顯示「讀下一篇時比較」與非空問題；問題只能由來源／目標文章類型的固定句型加上同卡
    `relationBasis.labels[0]` 形成，不得讀正文、題名、關鍵字或模型補寫。正式 route 下一站仍須逐字
    使用下一篇既有閱讀任務問題，不得被一般比較問題覆寫。
    逐一核對圖譜推薦卡：圖譜直接引用本文時可沿用該圖既有關係示範；只因共同公司而成立時，
    是否顯示「這篇為什麼連到這張圖」與同一批 `relationBasis` 公司，且 `guidedRelation.edgeId`
    的 from／to node 至少一端 ticker 屬於 `relationBasis.ids`。畫面是否明示共同公司節點不等於
    本文主題與整張圖存在上下游、受惠、訂單或因果關係；沒有同公司可見 edge 時是否不推薦該圖，
    而非退回圖內任一高證據 edge、題名或文字相似度。
    再逐一走讀「文章 → guided relation → 完整研究脈絡 → 延伸學習」：若 relation 的脈絡文章就是
    剛才文章，是否改為明示「完整研究脈絡就是剛才文章」，且只用既有返回按鈕回復原閱讀位置；
    若開啟另一篇，延伸區是否顯示「剛才文章 → 關係圖 → 現在」，收起指向來源文章與同一張圖的
    重複入口，並讓第一張主卡成為尚未走過的下一站。須以完整 article graph cards × guided edge
    母體核對，不只測單一路徑；origin 不存在或不相符時，不得收起任何一般推薦卡。
    完整 ledger／impact／monitor 控制表與來源、研究判定收在預設關閉的研究查核附錄；
    「研究中心還在追哪些問題」是否先把「已有文章／等待更多證據／暫緩研究」翻成讀者行動，
    首屏摘要是否只留待查問題數、已有文章數與下次總檢查；priority、selection decision、
    knowledge value 與 evidence posture 是否完整收進查核區，沒有被誤放成讀者或投資急迫性；
    每張卡再用白話問句、兩句「已知線索＋目前缺口」、2–4 個關鍵詞與下一個驗證動作解釋候選；
    active 候選的頂部地圖是否先只把有可解析正式 `article_id` 的候選依原 rank 列為「現在可以
    讀」，閱讀時間是否逐字取同篇 `readingMinutes`；其後「查看全部候選問題」是否仍逐一且同序
    枚舉全部 `reader_question`、固定 status 讀者標籤與 `next_check`，沒有因第一層方便入口而漏題
    或重排。兩層每個 `aria-controls` 是否唯一對到同候選卡，點擊後捲入並聚焦正確卡片；可讀起點
    是否桌機兩欄、窄幅單欄，完整清單展開後是否桌機四欄、中幅兩欄、窄幅單欄且不得水平溢位；
    手機整張地圖首次是否預設收合，卡尾是否能回到並聚焦同一地圖。地圖是否只分開「能直接讀
    文章」與「先看問題」，沒有改寫 rank、候選內容、研究判定或投資邊界。
    原始 `why_now`、凍結的下一份證據、第一拒絕與來源收在逐卡查核區，方法稽核另行收合；
    「各族群研究完整度」是否先明示上半部是新手學習入口、下半部是研究資料齊全度，且完成度
    不被寫成產業成熟度、股票排名或受惠程度；其後頂端須以四個系統問題呈現全部既有學習路線；每張卡的 label、問題、
    第一站、站數與相關族群都必須可逐項回查 `RESEARCH_LEARNING_ROUTES`、route 主文章與其
    `article.groups`，不得靠相似度或模型新增跨族群關係。第一站按鈕須開啟 route step 1 並回到
    文章頂端；問句之後是否先逐字顯示第一站正式 `phaseLabel／phasePurpose`，再立即顯示含
    step／total、既有 graph label、`readingMinutes` 與完整文章題名 accessible name 的主要行動；
    相關族群與完整路線預覽是否保留但排在主要行動之後，且沒有改寫階段任務、站次或關係；
    同一族群跨卡重複須明示為多個系統角色，不得暗示重複計分。相關族群是否都以
    route `groupIds` 對回同一份正式族群角色入口，點擊後切到／定位同一族群的 `readerRole` 與
    `readerBoundary`，且可由該族群既有「會出現在」返回原問題；不得從文字生成角色或關係，
    780px 以下按鈕是否至少 44px 高並保留可見焦點。展開路線後，每站須
    逐項顯示同篇主文章既有 `groupLabels`，標成「這站會用到」，不得從 route 總族群、圖譜、題名
    或相似度補關係；桌機展開中的階段須跨滿路線 map，再以至少 280px 的站點欄寬重排，不能只在
    單一窄欄堆疊。多 phase 路線的每個可聚焦 phase summary 是否在站數／站次之前逐字顯示非空
    `phasePurpose`，包含收合中的非目前階段；文章定位是否同時顯示目前 phase 任務，且 route map
    邊界明示這只是正式閱讀課綱，不是上下游、重要性、研究完成度或投資排序；矩陣路線預覽是否
    先收合全部 phase 以完整比較任務，文章內則只預設展開目前 phase。三層完成度說明預設
    收合，但展開後不得少掉任一層或非多空分數警語；
    「各族群研究完整度」每列須先顯示可實際開啟的族群起讀文章與全部文章入口，再顯示已完成、
    最大缺口與下一步；起點只能依 `article.groups[0]`、既有學習路線順序與站次決定，不得改用
    最新、熱門度、文字相似度或模型判斷，兩種入口都須回到頁首。九欄矩陣收在查核附錄，
    展開後資料不得缺漏，
    同一帳本標題不得重複。
    從文章返回清單時，預設狀態的三步導覽須重新出現；由清單開文須回復原 scroll context 並把
    焦點送回同一文章卡，由深連結或其他表面開文則須把對應卡捲入畫面後聚焦。
15. 執行 `python scripts/build_dashboard.py` 後，`git diff --exit-code -- index.html research.html`
    必須為空；`qualitative-quality` workflow 以同一檢查阻止模板與發布頁不同步。

    **雙讀者 gate 有可判定條件，不能只驗結構。** `research_queue.py --lint` 會以
    「讀者實際看得到的文字」為基準檢查兩件事——基準是正文**加上**研究中心會渲染成
    表格的帳本欄位（claim、basis、boundary、rationale、metric、trigger 等）；只量
    markdown 正文會把帳本裡的術語全部漏掉，而讀者是看得到那些的。文件標題與 locator
    屬引用資訊，不計入：

    - 任何術語在讀者可見文字出現 **5 次以上**卻沒出現在「名詞小字典」→ 2026-08-09
      起新建 topic 直接 error，既有 topic 標 warning。出現 3～4 次一律 warning。
      術語偵測排除 registry 已登錄的公司／組織名、常見縮寫（AI、Q2、GPU…）與帳本
      ID（C7、S12、MI-…）。
    - 正文解釋不得低於讀者可見文字的 **50%**，否則帳本渲染後會蓋過說明。

    通過機器條件仍不等於好讀。人的部分要另外確認：產業學習者能不能先看懂名詞、
    已知／未知與機制；分析師能不能在第一個快讀區直接取得主命題、證據強度、未證實
    缺口、可行動範圍與下一個檢驗。實務上最容易失敗的是**用「一份文件還沒發布」這類
    抽象缺席當主命題卻不給具體場景**，以及**把否定邊界寫滿正文**——邊界屬於帳本，
    正文每句都被下一句收回，讀者累積不出任何圖像。
16. 在文章間切換與由雷達／圖譜開啟文章時，確認閱讀區立即回到頂端；雷達已升格候選開文後，
    頁首與末端必須同時顯示原第 N 題、非投資排名邊界與返回行動，回雷達後保留原卡捲動位置與焦點；
    直接文章 deep link 不得顯示雷達題次、返回雷達或其他虛構來處；但若目前 article ID 本身可
    唯一對回已升格候選，仍須顯示該文各正式族群既有的「本文先問」，並把通用角色與界線完整保留
    在單一可展開補充區。改從清單、直接連結、雷達或路線下一站開同一篇時，本文問句必須一致；
    780px 以下由雷達、矩陣或圖譜開文時，單一黏性返回鈕下方是否逐字顯示同一
    `articleOriginContext().title`；若 origin 是 `maturity-route`，同一區是否另逐字顯示正式
    `route.question`，且 `data-origin-route-id` 完全相同；341–780px 預設展開，340px 以下是否以
    44px 以上原生摘要預設收合並可一次看完完整起點。若從圖譜已選 edge 的「讀完整研究脈絡」開文，title 是否逐字保留
    node label 與 relation label，展開內容是否逐字保留 evidence、commercial stage、materiality，
    且 `data-origin-edge-id` 與返回後選中 edge 完全相同；沒有 edge 的圖譜主文章入口是否維持原
    graph label／view，而未猜一條關係。手機文章類型 tabs 是否收起而未移除返回能力；直接 deep link 是否
    只有「返回研究清單」且沒有虛構起點。320／390／780px 首屏仍須同時容納文章問題、查核警語、
    第一個任務重點與完整 44px 主行動，頁面不得水平溢位；884px 與 1280px 則仍只顯示桌機完整
    起點卡，不得重複手機摘要。
    另完成任一正式學習路線後，實走「末站完成卡 → 回到學習路線 → 選另一條問題路線 → 開啟
    第一站」：返回圖譜的第一個內容須逐字保留已完成 route label 與 question，只列 registry 中
    其他正式 route 的 label／question；選定後目前 graph、`aria-pressed`、reader-only
    `nextRouteId` 與第一 station 入口須指向同一路線。返回剛才文章要恢復完成卡與捲動位置；直接
    圖譜分頁與 hash deep link 必須是 0 張完成卡。390px 選項與起點行動至少 44px，桌機為三欄、
    手機為單欄，兩者都不得水平溢位；並列順序不得暗示重要性、受惠、研究完成度或投資排名。
    再由同一張完成卡開啟下一條 route 第一站：文章標題之前須出現且只出現一張跨路線接力卡，
    逐字並列前後 route 的 `question`，以及第一 station 的 `graphLabel`、第一篇
    `readingMission.keyPoints[0]` 與 `readingMission.question`。返回後須保留已選 route、第一站入口
    與焦點；再開第一站仍能重建同一接力，切到第二站則立即消失。一般圖譜開文、直接 article deep link 與其他 origin 都須為
    0 張接力卡。390px 返回至少 44px、1440px 返回至少 36px，兩種寬度皆不得水平溢位；畫面必須
    明示只是閱讀接力，不代表兩條路線存在上下游、受惠、因果或投資排序。
    另從任一正式路線非末站實走「下一站卡 → 相鄰下一篇」：下一篇標題前須出現且只出現一張
    同路線接力卡，逐字並列前一 station 的 `graphLabel`、前一篇
    `readingMission.keyPoints[0]`、目前 station 的 `graphLabel` 與目前篇
    `readingMission.question`。返回須復原前一篇接續卡、捲動位置與焦點；再前進一站須重建新的
    相鄰接力。直接 article deep link、route map 跳站、一般圖譜開文與非相鄰文章都須為 0 張。
    390px 返回至少 44px、1440px 返回至少 36px，兩種寬度皆不得水平溢位；畫面須明示文字取自
    前後兩篇已發布內容，不代表上下游、受惠、因果、成熟度或投資排序。
    對所有相鄰站再分開驗收 same-phase 與 cross-phase：same-phase 必須維持原「上一站重點／這站
    問題」且只有一張 station track；cross-phase 必須改顯前後 phase label 與各自非空的人工
    `purpose`，標題明示從哪個階段進入哪個階段，再顯示新階段第一 station 的 graph label 與原
    `readingMission.question`。前後 phaseStep 必須恰好相差 1；缺 purpose 時不得用題名、正文、
    相似度或模型補寫。320px phase cards 須改成單欄、390px 與 1440px 可並排，三種寬度皆不得
    水平溢位；返回仍須復原原接續卡、捲動位置與焦點，且畫面明示不代表已掌握或新增投資結論。
    換文後不得殘留前一候選問句。由雷達族群問句定位矩陣時，另驗收承接卡先跨滿四個
    盤點欄；已升格狀態須顯示同一篇本題文章，未升格狀態不得出現空白文章欄。在 1280px、884px
    與 780px 以下分別檢查三欄、兩欄與單欄契約，開文返回後則核對同一問句、所選族群與整列焦點。
    同一選取列的四個族群盤點欄在 1280px 保留四欄、884px 改成帶各自欄名的 2×2、780px 以下
    依 DOM 單欄；雷達承接卡含左右外距後必須完整落在 row 邊框內，問句、文章與兩個行動都不得
    被裁切。三種寬度的數字、文字、DOM 順序與開文／返回行為必須相同。
    雷達候選卡另在 390px、884px 驗收正文橫跨完整卡寬、卡頂可直接讀到「研究順序 N」及「只排
    研究待辦，不是股票或投資排名」，並確認讀者看到的是白話 status 與「閱讀這題的文章」行動；
    頁面不得水平溢出，原始 status label、rank 與 payload 不得因顯示翻譯而改寫。
    桌機與行動版均檢查
    首屏層級、表格密度、截斷與全頁水平 overflow。市場議題一般正文表在 section 容器不足
    620px 時，須逐 row 顯示原始欄名與全部 cell，且最右側成熟度／證據邊界不需橫向捲動即可讀；
    寬幅時須還原原生 table。查核附錄不得套卡片，只有實際 overflow 時才成為可聚焦 region 並
    顯示水平捲動提示。行動版首屏須能讀到頁首研究問題、查核警語、第一句任務重點與 44px 主行動，
    不能只剩狀態、日期、路線與大綱；完整「讀完能回答」反思題可排在主行動之後，但必須仍在同一
    任務卡可見且逐字不變，不能用隱藏或摘要換取首屏高度。完整新手段落也要確認三句重點在字典之前；
    三句之後的角色區須先在一個手機 viewport 內看完本文各族群問題，通用角色補充預設收合但可用
    44px 原生摘要一次展開，問句、族群順序與補充內容不得因 responsive 改寫。
    進入產業依賴圖後，再核對文章 origin 內角色數、順序與同篇 `groups` 完全相同，每個角色的
    `data-edge-id` 在該 graph 都只有一條、問句與雷達逐字相同，點擊後所選 edge、證據層級、商業
    位置及三步邊界都取自原圖譜。320／390／780／884／1280px 均不得水平溢出，角色按鈕至少 44px；
    三步解讀下方的詳情導覽須再次核對相同角色順序、目前 `aria-current="step"`、0／多條禁用與
    其他唯一 edge 的 click／Enter／Space 切換；逐篇切換後 edge、問句、證據層級與商業位置仍須
    完全相同。返回後焦點仍回文章原「看這站證據關係」按鈕；直接 deep link、公司視角、單族群與
    不同 graph 必須維持 0 張詳情導覽。
    快讀與閱讀任務只能由既有結構化 register／正文 blocks 合成，不得另寫一套無 claim ID、
    source ID 或 monitor 支撐的結論。另各抽查一般文章至少一個達 120 字、含兩個以上句末的
    主正文段落，以及市場議題
    至少一個達 100 字／兩個句末或 80 字／三個句末的主正文段落：320／390／780／781／884／
    1181／1280px 都須依實際 section 內容寬度顯示原句停頓，且全頁無水平 overflow；
    停頓 span 不得帶文字或進入輔助科技閱讀順序，原 `<p>`、字序、runs 與 payload 都不變。
    若完整母體仍有 fenced `text` 推論鏈，另須逐篇確認只命中既有 3–8 步箭頭序列、站內沒有裸露
    fence 標記、實際節點為帶非空 `aria-label` 的 `<ol>`，每個 `<li>` 與原項目逐字同序；320／390px
    不得水平溢位，其他文章的 paragraph／list 數不得因模糊比對改變。
    若完整母體仍有固定四標籤 KPI 清單，須逐篇比對 reader DOM 的命中篇數與原始 payload 完全
    相同；四個定義項的標籤、正文與順序可重建回原清單，未命中文章不得出現判讀卡。390px 必須
    單欄、無水平 overflow；600px 以上正文容器才可雙欄，不能只用整體 viewport 判斷。
    窄於 1180px 時另須在新手導讀後驗收黏性「閱讀位置」：收合時顯示目前第 N/M 節
    與同一原始 section 標題，展開時可直接跳節；附錄須是最後一節，`aria-current`、progressbar
    數值與實際捲動同步，320px 也不得水平溢出或遮住錨點。這只可重用既有大綱資料，不得生成
    段落摘要或把閱讀進度寫成研究完成度。884px 另開啟專注閱讀，確認隱藏大綱後
    `.reader-inner` 只剩一個 grid track、最大 720px 且左右置中；不得保留 240px 空欄把正文擠到
    左側。另抽查一般文章至少一個 120 字以上／兩個中文句末，以及市場議題至少一個 100 字以上／
    兩個句末或 80 字以上／三個句末的主正文段落：窄幅須逐句形成視覺停頓，寬幅仍連續；兩邊的
    `textContent` 都須和 payload 只差可確定的
    中文排版空白與半形 `,;:` 中文化，連結、粗體、段落數與字序不得改變；英文詞列、數字與網址
    標點必須保持半形。另在原字典已捲離畫面的同一正文位置驗收名詞速查：開啟後搜尋欄須取得焦點，
    正式筆記與多空小作文另須全文章枚舉 `.article-section-purpose`：每個 reader section 恰有一張、
    文字非空、`data-reader-purpose-heading` 等於同節原標題；320px、390px、884px 與 1280px 都不得
    造成水平溢出。市場議題須維持 0 張，因其已有專用新手導讀與研究摘要。
    市場議題另抽查一節符合三個以上連續粗體段首的主正文：`data-reader-section-map-count` 必須等於
    實際連續段數、各 label 逐字等於對應第一個 bold run，完整原段落仍在卡片後；正式筆記與不符合
    門檻的市場議題維持 0 張。section 容器不超過 480px 時須改為單欄，深色與淺色都不得水平溢出。
    關鍵字結果數與原字典一致，關閉按鈕、Escape 與背景點擊都能關閉，並保持 window／reader
    scroll position、把焦點送回本次觸發按鈕；再於一個含表格或專業段落的正文節，逐一核對節首
    詞鈕是同篇字典詞的子集、44px 行動版觸控高度、點擊後精確剩 1 筆原始定義且關閉後回到同一
    詞鈕。行動版浮動入口不得與右下回頂端按鈕重疊。

## Schema 沿革

- v1：保存候選議題、來源鏈、影響路由與後續節點。
- v2：2026-08-01 三篇研究先導入新手導讀，是短暫過渡契約；原訂 2026-08-02 成為新建
  topic 的最低版本。
- v3：2026-08-02 由 claim ledger、來源角色、跨公司可比性、monitor 與可信度新鮮度契約
  取代 v2。自此新建 topic 必須使用 v3；parser 對 cutover 前的 v1／v2 只保留歷史相容，
  舊格式顯示為未結構化驗證，不能默認具有一般可信度。live register 已完成全數遷移，
  loader 一律要求 v3，不能以降版或回填舊建檔日繞過契約。
