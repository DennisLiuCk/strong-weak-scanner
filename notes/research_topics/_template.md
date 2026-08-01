# 市場議題標題

<!-- research_topic
topic_id: MI-YYYY-MM-DD-SHORT-SLUG
schema_version: 3
status: inbox
priority: p2
captured_at: YYYY-MM-DD
source_published_at: YYYY-MM-DD
last_reviewed_at: YYYY-MM-DD
review_due: YYYY-MM-DD
source_type: mixed
publisher: 主要來源發布者
publisher_domain: example.com
canonical_url: https://example.com/source
source_chain_id: publisher-event-yyyymmdd
stock_ids:
group_ids:
trigger_type: industry_event
evidence_role: candidate_source
route: undecided
thesis_claim_id: C1
base_confidence: low
confidence_basis: 模板預設低；作者須依主命題實際引用的來源品質、獨立性與反證重新判定
cross_company_numbers: false
-->

<!-- transition
date: YYYY-MM-DD
from: initial
to: inbox
reason: initial_capture
evidence: source_chain:publisher-event-yyyymmdd
-->

只有這筆 `initial → inbox` transition 可以用 `source_chain:<meta.source_chain_id>`。之後的
triage、修正、關閉、重開或 meta 時鐘變動，一律追加 transition，並用
`evidence: sources:S1,S2` 引用已登錄來源；不可用自由文字或再次使用 `source_chain:`。

## 新手先讀：這篇在講什麼

### 名詞小字典

- **術語一**：不用另一個專有名詞、用日常語言解釋。
- **術語二**：說明它位在產業鏈哪裡，以及不代表什麼。
- **術語三**：若是會計或產業慣用指標，說明它怎麼計算或判讀。

### 三句話抓重點

- 第一句交代已發生、可由一手來源驗證的事件。
- 第二句說明為什麼重要，以及影響會先傳到哪個環節。
- 第三句寫清楚目前還不能知道什麼，避免把題材直接外推成個股訂單。

### 為什麼重要

用至少一段白話說明這篇如何改變讀者的判斷框架；不要只重複事件標題。

### 接下來怎麼追

- 列出至少一個有日期、數字或產品階段的可觀察節點。
- 列出至少一個公司文件、客戶採用或反證節點。

### 想一想

- 哪個可觀察結果若沒有出現，會推翻目前的說法？
- 這是市場新增需求，還是既有支出／價值在供應鏈之間重新分配？

## 主張與證據帳本

`證實` 只代表指定來源直接支持下列精確措辭，不代表消息來源的預測必然實現，也不代表
研究端已完成公司訂單、損益或估值映射。

<!-- research_source
source_id: S1
role: company_release
source_kind: document
publisher: 主要事件發布者
title: 官方文件標題
published_at: YYYY-MM-DD
captured_at: YYYY-MM-DD
accepted_at: YYYY-MM-DD
status: active
url: https://example.com/source
locator: 正文第 3 段或 PDF p.10
limitation: 來源只支持事件與時程，不支持個別供應商訂單或獲利
-->

<!-- research_source
source_id: S2
role: competitor_primary
source_kind: document
publisher: 獨立消息鏈發布者
title: 可用來交叉驗證或提出反證的官方文件
published_at: YYYY-MM-DD
captured_at: YYYY-MM-DD
accepted_at: YYYY-MM-DD
status: active
url: https://example.org/source
locator: 正文產品階段段落或 PDF p.5
limitation: 發行人只描述自身產品，沒有提供整體市場份額或台灣供應商映射
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: living_index
publisher: 主要事件發布者
title: 公司 IR／官方公告持續更新索引
published_at:
captured_at: YYYY-MM-DD
accepted_at: YYYY-MM-DD
status: active
url: https://example.com/ir
locator: 截至 YYYY-MM-DD 實際觀察的最新公告標題、日期，或明確記錄當日未見後續附件
limitation: 此頁會持續變動且沒有單一發布日，只供未來重查；不能替代已發布附件或證明沒有事件
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: 來源直接明講、可逐字定位且沒有加入研究端因果推導的精確事實
supporting_source_ids: S1
contrary_source_ids:
as_of: YYYY-MM-DD
basis: S1 的 locator 可直接支持這句話
boundary: 不把產品發布、合作列名或管理層目標改寫成訂單、收入、市占或毛利
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C2
label: unverified
status: active
claim: 目前市場常見、但現有來源尚不能支持的公司或產業主張
supporting_source_ids:
contrary_source_ids:
as_of: YYYY-MM-DD
basis: 現有來源沒有提供完成公司層級映射所需的客戶、數量與財務資料
boundary: 不得放入正式公司筆記，也不得當成 impact direction 的既成事實
verification_needed: 公司正式公告、季報或法說須同時提供客戶／產品節點與可辨識財務貢獻
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

只有確實存在超出來源原文、但可由證據推導與反證的研究判讀時，才另加 `inference` claim；
不可為了湊三種標籤照抄一則假推論。模板的 low confidence 也不是預設答案，完成主命題證據
審查後必須重寫 `base_confidence` 與 basis。

「來源沒提到」或「目前找不到」是證據缺口，不是 contrary evidence；`contrary_source_ids`
只放直接反駁或實質縮窄 claim 的來源。`resolution` 預設留空，只在確有 active contrary
source 時填人工作法裁決。修正舊 claim 時追加新 ID：新 claim 填
`correction_kind: supersedes|refutes` 與 `corrects_claim_id`，舊 claim 填
`corrected_by_claim_id`，新 claim 的 `basis` 另記 `correction_of:<old_claim_id>`。若之後再
修正，逐代相鄰連結，不覆寫或壓平中間一代。

## 跨公司數字與可比性

本模板預設 `cross_company_numbers: false`，因此不可加入 `metric_comparison` block。若文章
用兩家以上公司的數字形成判斷，先把 meta 改為 `true`，再依
`MARKET_RESEARCH_METHOD.md` 為每個「公司 × 觀測值」各建一個 block；期間、單位、定義
與可比性判定缺一不可。判定為 `not_comparable` 是有效研究結果，不可為了排名強行正規化。
期間起訖不可晚於關聯 claim 的 `as_of`；未來預測的 horizon 寫進 metric、`period_basis`
與 definition，觀測期間記錄預測發布／資訊截點，不把尚未發生的年度當成已觀測期間。
既有 comparison observation 採 append-only；新期間、重編數字或定義改變時追加新的
`observation_id`，研究問題或共同口徑實質改變時另建 `comparison_id`。

## 來源與證據邊界

- [S1：主要一手來源](https://example.com/source)
- [S2：獨立交叉來源](https://example.org/source)
- [S3：未來重查的 living index](https://example.com/ir)
- 尚未證實的公司層級主張必須明列，不可把產業事件自動改寫成公司營收、訂單或市占。

## 影響路由

<!-- impact
group_id: serverodm
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: YYYY-MM-DD
rationale: 為何此族群或個股需要複核
evidence_boundary: 目前只構成搜尋觸發，不構成正式筆記事實
-->

若 `route: policy_watch` 且尚未完成政策適用性／公司暴露映射，可以不建立 `impact` block；
此時維持 warning／watch，`stock_ids`、`group_ids` 可留空，且不得路由或 promoted 到正式
筆記。取得可定位的公司層級 evidence 後，才追加 impact 與正式 route。

## 持續驗證清單

`review_due` 必須等於所有 monitoring item 中最早的 `next_check`。

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1
metric: 產品採用、量產階段與可辨識出貨
source_ids: S1
watch_source_ids: S3
frequency: event_driven
next_check: YYYY-MM-DD
trigger: 發布具名客戶、認證完成、量產日期或實際部署數量
invalidation: 時程延後、產品停留展示／送樣，或官方文件撤回原先進度
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C1,C2
metric: 公司層級收入、毛利、現金流與資本支出足跡
source_ids: S1,S2
watch_source_ids: S3
frequency: quarterly
next_check: YYYY-MM-DD
trigger: 公司季報或法說把產業事件連到具名產品、量產收入與獲利
invalidation: 只有合作名單、題材轉述或營收成長，沒有產品、客戶與獲利交叉證據
-->

`source_ids` 是建立 monitor 的當前／基線 evidence；`watch_source_ids` 才是未來實際重查
入口。每個 active monitor 至少要有一個 active `living_index` watch；新附件出現時另追加
`document` source，不覆寫索引頁。

## 下一個可證明／否定的節點

- 公司正式公告、季報或法說是否明確對應這個事件。
- 若沒有新增公司層級證據，保留在候選議題；不要前移 evidence clock 或更新正式筆記。

到期以 runtime 當下的臺北日曆日判斷。沒有新 thesis evidence 時，只在 append-only
`scan_log.csv` 新增一列，不更新 `last_reviewed_at`、不延後 `review_due`，也不調高
`base_confidence`。`dismissed`／`resolved` 後 monitor 應退役；重開須先追加較新的 source、
active claim 與 active monitor，再追加引用新 source 的重開 transition，原關閉紀錄不得改寫。
