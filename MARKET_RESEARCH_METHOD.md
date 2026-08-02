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
可證偽問題
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

## 一、先按文件角色取得來源

搜尋順序以能直接承擔主張的文件為先，不以搜尋結果排名或文章數量為準：

1. 發行人新聞稿、正式法說、財報與監管申報。
2. 客戶、平台、交易對手或競爭者的一手文件，用來交叉驗證與找替代路徑。
3. 政府、監管、交易所與標準組織文件。
4. 管理層直接談話；若只是轉述，必須降低來源角色。
5. 市場估計與媒體只適合提供搜尋 trigger；不能單獨把公司主張標為 `verified`。

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
3. 取其 `accepted_at` 最大值。

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
   儀表板資料日或作者手填的舊日期規避到期。當 `as_of > review_due`，且沒有 accepted-at 較新的 active referenced
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
- `materiality`：未知、相鄰搜尋路由、具名產品角色、可辨識財務貢獻。圖上以同心環距離
  （越靠近中心代表目前證據支持的材料性越高）、節點標籤與分組清單三重呈現；線寬只作
  輔助提示，不承擔唯一判讀，也不得與證據強弱混為一談。空的財務內圈表示目前篩選結果
  尚無可辨識財務貢獻，不表示不存在商業關係。
- `exclusivity`：未知、多路徑、少數來源、具證據的獨家。非 unknown 必須明示適用範圍；
  `unverified` 不得宣稱集中度或獨家。

每條 edge 至少要保存 `claim_refs` 或 `note_refs`、`boundary`、`next_trigger`、`as_of` 與
`review_due`。到期線會降透明度並標成需要複核，但「沒有新證據」不是反證，不會自動把
verified 改成 refuted；其上游 topic 可信度仍按第五節規則自動降級。點選關係時，研究中心
必須能回到原文章、claim 與一手來源。

節點 registry 分三層：`config/knowledge_concepts.csv` 保存專有名詞與製程節點，
`config/external_entities.csv` 保存不在 universe 的公司／組織，台股公司與正式族群則直接由
`config/universe.csv`、`config/groups.csv` 注入。顯示關係保存在
`notes/knowledge_graph/*.md`；新增主題先複製 `_template.md`。MVP 每條 active edge 只允許
root 的一跳關係，先把證據品質與可讀性做穩，再考慮多跳探索。

發布前執行 `python scripts/knowledge_graph.py --lint`。lint 會檢查 endpoint、值域、雙視圖、
一跳限制、來源引用、證據不可升格、財務 materiality 與 exclusivity 邊界；它不重新下載來源，
也不替代內容 reviewer。

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
`evidence: sources:S1,S2` 形式引用已登錄 source ID。修正、關閉、重開或 meta 時鐘變動都
不得再用自由文字或 `source_chain:` 取代實際 evidence。

`scan_log.csv` 與 comparison observation 同樣 append-only：新的掃描窗口、coverage、結果、
限制與下一期限只能新增一列；不得回頭改寫或刪除舊 scan row。若更正記錄錯誤，追加明確
指向舊 scan ID 的 correction row，在 `coverage_note` 寫
`correction_of:<old_scan_id>`，並保留原始紀錄。

Git 歷史能看到文字變更，但不能以 Git 歷史取代文章內的修正鏈；研究中心讀者必須在當前
版本就能理解結論為何改變。CI 另以 `--baseline-ref` 比對 Git 前版：既有 source、claim、
monitor 的 immutable 欄位及 transition 前綴不可刪改；只能新增 ID，或把 lifecycle 單向
改成 superseded／refuted／retired 並補齊雙向修正關係。

## 九、方法本身也要留下可回測的歷史

文章逐篇通過 lint，只能證明欄位與引用完整；它不能回答研究是否有回頭檢查、是否願意
承認沒有新證據，或錯誤是否真的被修正。方法層另使用：

- `notes/research_method_reviews/YYYY-MM-DD_NN.json`：append-only 稽核快照，保存當時的
  topic、claim、source、monitor、圖譜與候選雷達覆蓋。registry 有任何變動都要新增快照，
  不得改寫舊檔。
- `notes/research_method_reviews/monitor_reviews.csv`：append-only 到期檢查帳本，每列連到
  既有 topic／monitor，結果只能是 `new_support`、`new_contrary`、`no_new_evidence` 或
  `not_yet_testable`。
- `scripts/research_method_audit.py`：驗證 snapshot fingerprint、review 引用與歷史不可改寫，
  並在研究雷達顯示可追溯、可證偽、新鮮度、修正學習與校準可用性五道 gate。

`no_new_evidence` 是有效的回顧結果，但**不得**刷新 topic source 的 `accepted_at`、
`last_reviewed_at` 或 `review_due`。它只在方法帳本設定下一次工作期限；原文章仍照既有
evidence clock 降級，直到真的有新 evidence。

候選升格數、文章數與圖譜線數是研究產出，不是正確率。只有到期 monitor 全數留下 review
event，且至少三個結果帶有新證據時，audit 才允許顯示附樣本數的描述性支持率；即使如此，
它仍不是投資命中率、報酬率或因果效果。樣本不足時只報 counts 與 `not_ready`，不補零、
不把未到期主張算成功。

## 十、發布前檢查

1. 新手導讀是否清楚說明已知、未知與下一步。
2. 每個材料性 claim 是否有正確標籤、來源 ID、basis 與 boundary。
3. `verified` 是否只重述來源直接支持的精確措辭。
4. 是否主動找過競爭者、替代方案、政策附件或財務附註等反方來源。
5. 跨公司數字是否逐 observation 記錄期間、單位、定義及可比性。
6. 每個 monitor 是否分開記錄基線 `source_ids` 與未來 `watch_source_ids`，且 active watch
   至少包含一個 living index，並具備頻率、日期、trigger 與 invalidation。
7. `review_due` 是否等於最早 monitor 日期，且晚於 `last_reviewed_at`。
8. impact 是否仍清楚寫 evidence boundary，沒有把 topic 升格為公司事實。
9. 執行 `python scripts/research_queue.py --lint` 與 `python scripts/knowledge_graph.py --lint`；
   lint 只驗結構與引用完整性，不會重新下載或證明來源內容為真。
10. 執行 `python scripts/research_method_audit.py --lint --baseline-ref HEAD`，確認 registry
    有新快照、舊快照未被改寫，review ledger 也只追加新列。
11. 重建研究中心並檢查 ledger、比較表、可信度、知識圖譜證據面板與 deep link 的桌機／
    行動版顯示。

## Schema 沿革

- v1：保存候選議題、來源鏈、影響路由與後續節點。
- v2：2026-08-01 三篇研究先導入新手導讀，是短暫過渡契約；原訂 2026-08-02 成為新建
  topic 的最低版本。
- v3：2026-08-02 由 claim ledger、來源角色、跨公司可比性、monitor 與可信度新鮮度契約
  取代 v2。自此新建 topic 必須使用 v3；parser 對 cutover 前的 v1／v2 只保留歷史相容，
  舊格式顯示為未結構化驗證，不能默認具有一般可信度。live register 已完成全數遷移，
  loader 一律要求 v3，不能以降版或回填舊建檔日繞過契約。
