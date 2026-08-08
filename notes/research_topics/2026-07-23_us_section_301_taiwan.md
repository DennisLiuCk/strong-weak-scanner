# 美國強迫勞動 Section 301 對台灣商品的新增關稅框架

<!-- research_topic
topic_id: MI-2026-07-23-US-SECTION301-TAIWAN
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-07-27
source_published_at: 2026-07-23
last_reviewed_at: 2026-07-27
review_due: 2026-07-30
source_type: official_policy
publisher: USTR
publisher_domain: ustr.gov
canonical_url: https://ustr.gov/about/policy-offices/press-office/press-releases/2026/july/ustr-takes-action-forced-labor-section-301-investigations
source_chain_id: ustr-forced-labor-section301-20260723
stock_ids:
group_ids:
trigger_type: trade_policy
evidence_role: candidate_source
route: policy_watch
thesis_claim_id: C3
base_confidence: medium
confidence_basis: 關稅框架與豁免附件由政府文件支持，但公司實際 HTS、原產地、直出占比與承擔方尚未完成映射
cross_company_numbers: false
schema_migrated_at: 2026-08-02
-->

<!-- transition
date: 2026-07-27
from: initial
to: inbox
reason: weekly_primary_source_scan
evidence: source_chain:ustr-forced-labor-section301-20260723
-->
<!-- transition
date: 2026-07-27
from: inbox
to: triaged
reason: policy_is_material_but_company_mapping_requires_hts_and_export_exposure
evidence: sources:S1,S2,S3
-->

<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_glossary_for_repeated_terms_no_conclusion_change
evidence: editorial:high_frequency_glossary
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **Section 301**：美國可針對被認定不公平的外國政策或做法採取關稅等措施的貿易法工具，不是所有商品自動套用同一稅率。
- **HTS code**：美國進口報關使用的商品分類號碼；產品俗稱相同，也可能因規格、組態或用途而落在不同 code。
- **MFN 稅率**：美國對一般貿易夥伴適用的基礎關稅；本題的 Section 301 稅要和它一起判讀。
- **Incoterms**：買賣雙方約定運輸、報關、風險與部分費用由誰負擔的條件，會影響新增關稅最終由誰承受。
- **Annex（附件）**：正式公告附帶的清單，用來逐項列出適用品目、豁免或條件；它不是另一套獨立關稅。

### 三句話抓重點

- USTR 已公布對台灣商品的最終行動，但 10% 是未豁免商品與 MFN 合計的框架，不是所有台灣科技品一律加徵。
- 電腦、伺服器相關品、半導體設備、資料傳輸設備與晶片等多類 HTS 已列入一般豁免，必須逐 code 判讀。
- 在取得公司實際報關分類、原產地、美國直出占比與 Incoterms 前，不能估算任何公司的毛利衝擊。

### 為什麼重要

政策新聞最容易把國家層級稅率誤寫成公司層級損益。真正的傳導要依序確認商品 code、豁免、
原產地、出貨路徑與合約承擔方；少一層都可能把本來豁免的伺服器或晶片，和未必豁免的裸
PCB、電源、散熱或被動元件混為一談。

### 接下來怎麼追

- 追 USTR／Federal Register 是否修改 Annex、豁免、在途規則或生效條件。
- 追公司一手文件或可追溯報關資料是否揭露實際 HTS、原產地、美國直出占比與 Incoterms。
- 優先核對裸 PCB、電源、散熱與被動元件，不用產品俗稱猜測報關分類。

### 想一想

- 同一台伺服器裡的整機、零件與材料，為什麼可能適用不同關稅結果？
- 即使某項產品未豁免，新增稅負一定由台灣供應商吸收嗎？
- 缺少公司報關 code 時，直接用美國營收占比估毛利衝擊會漏掉哪些變數？

## 為何值得進佇列

USTR 7 月 23 日公布最終行動；對未豁免的台灣商品，Section 301 稅與 MFN 稅合計以
10% 為框架，並自美東 7 月 24 日 00:01 起生效。附件初查同時顯示，電腦／伺服器、
其零件、半導體設備、網通傳輸設備與晶片等多個核心科技類別已列入一般豁免；因此這是
需要按 HTS code 分流的成本／需求風險，不是「所有台灣科技品一律加 10%」。在確認
原產地、實際報關分類與各公司的美國出貨／Incoterms 前，不能寫成任何一家公司的
毛利衝擊。

## 來源與證據邊界

<!-- research_source
source_id: S1
role: regulator_or_policy
publisher: USTR
title: USTR Takes Action in Forced Labor Section 301 Investigations
published_at: 2026-07-23
captured_at: 2026-07-27
accepted_at: 2026-07-27
status: active
url: https://ustr.gov/about/policy-offices/press-office/press-releases/2026/july/ustr-takes-action-forced-labor-section-301-investigations
locator: 台灣最終行動、稅率框架與生效時點段落
limitation: 新聞稿只提供政策框架，不能決定個別商品 HTS、公司出貨暴露或關稅承擔方
-->

<!-- research_source
source_id: S2
role: regulator_or_policy
publisher: USTR / Federal Register
title: Forced Labor Section 301 Investigation Final Action Notice and Annexes
published_at: 2026-07-23
captured_at: 2026-07-27
accepted_at: 2026-07-27
status: active
url: https://ustr.gov/sites/default/files/files/Press/Releases/2026/FLIP%20301%20Investigation%20Final%20Action%20FRN%207-23-26%20FINAL.pdf
locator: 台灣適用 Annex、一般豁免 HTS、在途例外與 Section 232 排除段落
limitation: 附件是 code-level 規則，不等於任一家公司的所有產品、組態或出貨路徑都已完成分類
-->

<!-- research_source
source_id: S3
role: regulator_or_policy
publisher: The White House
title: Presidential Memorandum on Section 301 Forced Labor Investigations
published_at: 2026-07-23
captured_at: 2026-07-27
accepted_at: 2026-07-27
status: active
url: https://www.whitehouse.gov/presidential-actions/2026/07/actions-by-the-united-states-in-the-investigations-under-section-301-of-the-trade-act-of-1974-of-the-acts-policies-and-practices-of-60-economies-related-to-the-failure-of-each-economy-to-impose-and/
locator: 總統行動與各經濟體 Annex 入口
limitation: 提供政策授權與附件入口，不提供台灣上市公司的報關 code、原產地或損益暴露
-->

- [USTR 官方新聞稿](https://ustr.gov/about/policy-offices/press-office/press-releases/2026/july/ustr-takes-action-forced-labor-section-301-investigations)（2026-07-23）。
- [USTR Federal Register notice／完整 Annex](https://ustr.gov/sites/default/files/files/Press/Releases/2026/FLIP%20301%20Investigation%20Final%20Action%20FRN%207-23-26%20FINAL.pdf)（2026-07-23，431 頁）。
- [白宮總統備忘錄與 Annex 入口](https://www.whitehouse.gov/presidential-actions/2026/07/actions-by-the-united-states-in-the-investigations-under-section-301-of-the-trade-act-of-1974-of-the-acts-policies-and-practices-of-60-economies-related-to-the-failure-of-each-economy-to-impose-and/)（2026-07-23）。

Notice 對台灣指定 Annex I 與 Annex II Parts A、K；一般豁免清單至少明列：

- 8471.30–8471.90 自動資料處理機與 processing units，以及 8473.30 相關零件；
- 8486 半導體製造設備、8517.62 資料傳輸設備；
- 8541 半導體元件、8542 積體電路，以及 3818 半導體用摻雜化學元素／化合物類別。

在途例外限於 7 月 24 日前已裝船且在最後運輸段，並在 7 月 28 日前進口；Section 232
適用商品及其零件也另受豁免。上述是 code-level 初查，不等於任一家公司的所有產品都
豁免：裸 PCB、電源、散熱等品項可能使用不同 HTS，伺服器零件也可能依組態改分類。
目前仍沒有公司別報關 code、台灣原產直出占比與關稅承擔方，故暫不建立 impact block、
不改正式筆記；`review_due` 前完成公司暴露 triage。

## Claim–evidence ledger

<!-- research_source
source_id: S4
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-07-27
accepted_at: 2026-07-27
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 受影響公司季報、法說與重大訊息的後續查找入口
limitation: 這是會持續變動的查詢入口；只有後續實際附件能支持 HTS、直出占比、Incoterms 與毛利承擔
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: USTR 在 2026-07-23 公布最終行動，對未豁免台灣商品採 Section 301 與 MFN 合計 10% 的框架並設定生效時點
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-07-27
basis: 三份政府文件的最終行動、授權與附件文字直接支持政策框架及日期
boundary: 不能把國家層級框架改寫成所有台灣科技產品一律新增 10% 或任何公司的確定毛利衝擊
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: 一般豁免清單列入多項自動資料處理機與零件、半導體設備、資料傳輸設備、半導體元件與積體電路 HTS 類別
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-07-27
basis: S2 Annex 的 8471、8473.30、8486、8517.62、8541、8542 與 3818 等 code 可直接定位
boundary: code-level 豁免不表示特定公司的所有產品、裸零件、組態或不同原產地出貨都豁免
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C3
label: inference
status: active
claim: 公司層級成本與需求風險必須依 HTS、豁免、原產地、實際直出路徑與 Incoterms 分流，不能只按產業名稱判斷
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-07-27
basis: 政策以 code、原產與進口條件執行，而不同科技產品與零件落在不同附件與排除條件
boundary: 這是研究映射方法，不是對任何公司的稅負、售價、需求或毛利方向作出估計
verification_needed: 公司或可追溯報關資料補齊實際分類、原產直出占比與合約承擔方
resolution:
-->

<!-- research_claim
claim_id: C4
label: unverified
status: active
claim: 裸 PCB、電源、散熱、被動元件或任何特定台灣公司會承擔明確新增關稅與毛利損失
supporting_source_ids:
contrary_source_ids:
as_of: 2026-07-27
basis: 現有政策文件沒有公司別 HTS、原產地、直出占比、客戶條款或關稅承擔資料
boundary: 暫不建立 impact block，不把政策框架寫入正式公司筆記或 H# 終態
verification_needed: 公司一手文件或可追溯報關資料須同時確認 HTS、原產地、美國直出占比與 Incoterms
resolution:
-->

## 持續驗證帳本

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3
metric: Annex、豁免、在途規則與 Section 232 排除的正式變動
source_ids: S1,S2,S3
watch_source_ids: S4
frequency: event_driven
next_check: 2026-07-30
trigger: USTR、Federal Register 或白宮發布修正附件、執行指引或新豁免
invalidation: 正式文件改變台灣適用稅率、豁免 code、在途期限或排除範圍
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C3,C4
metric: 公司實際 HTS、原產地、美國直出占比、Incoterms 與毛利承擔
source_ids: S1,S2,S4
watch_source_ids: S4
frequency: quarterly
next_check: 2026-08-15
trigger: 公司法說、財報或可追溯報關資料首次提供可重建的產品分類與承擔方
invalidation: 產品確認豁免、不是台灣原產直出，或客戶依合約承擔新增稅負
-->

## 下一個可證明／否定的節點

- 由公司一手文件或可追溯報關資料確認實際 HTS、原產地、Incoterms 與美國直出占比。
- 優先釐清未被上述一般清單直接涵蓋的裸 PCB、電源、散熱與被動元件；不得用產品俗稱
  猜 HTS code。
- 只對有一手資料可重建美國出貨與關稅承擔的公司建立 impact；其餘保持政策觀察。
- 若產品被豁免或公司不是台灣原產直出，不應留下公司層級負面主張。
