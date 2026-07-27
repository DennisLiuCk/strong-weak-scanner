# 美國強迫勞動 Section 301 對台灣商品的新增關稅框架

<!-- research_topic
topic_id: MI-2026-07-23-US-SECTION301-TAIWAN
schema_version: 1
status: triaged
priority: p1
captured_at: 2026-07-27
source_published_at: 2026-07-23
last_reviewed_at: 2026-07-27
review_due: 2026-07-30
source_type: official_policy
publisher_domain: ustr.gov
canonical_url: https://ustr.gov/about/policy-offices/press-office/press-releases/2026/july/ustr-takes-action-forced-labor-section-301-investigations
source_chain_id: ustr-forced-labor-section301-20260723
stock_ids:
group_ids:
trigger_type: trade_policy
evidence_role: candidate_source
route: policy_watch
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
evidence: source_chain:ustr-forced-labor-section301-20260723
-->

## 為何值得進佇列

USTR 7 月 23 日公布最終行動；對未豁免的台灣商品，Section 301 稅與 MFN 稅合計以
10% 為框架，並自美東 7 月 24 日 00:01 起生效。附件初查同時顯示，電腦／伺服器、
其零件、半導體設備、網通傳輸設備與晶片等多個核心科技類別已列入一般豁免；因此這是
需要按 HTS code 分流的成本／需求風險，不是「所有台灣科技品一律加 10%」。在確認
原產地、實際報關分類與各公司的美國出貨／Incoterms 前，不能寫成任何一家公司的
毛利衝擊。

## 來源與證據邊界

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

## 下一個可證明／否定的節點

- 由公司一手文件或可追溯報關資料確認實際 HTS、原產地、Incoterms 與美國直出占比。
- 優先釐清未被上述一般清單直接涵蓋的裸 PCB、電源、散熱與被動元件；不得用產品俗稱
  猜 HTS code。
- 只對有一手資料可重建美國出貨與關稅承擔的公司建立 impact；其餘保持政策觀察。
- 若產品被豁免或公司不是台灣原產直出，不應留下公司層級負面主張。
