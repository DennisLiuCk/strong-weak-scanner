# Custom HBM 不是單一產品賽跑：先拆客製範圍，再追樣品、資格與量產

<!-- research_topic
topic_id: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-03
source_published_at: 2026-02-12
last_reviewed_at: 2026-08-03
review_due: 2026-09-15
source_type: mixed
publisher: Samsung Electronics
publisher_domain: news.samsung.com
canonical_url: https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing
source_chain_id: custom-hbm-scope-ladder-20260803
stock_ids:
group_ids: memory,packtest,ipdesign
trigger_type: memory_architecture_and_customer_customization
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C5
base_confidence: medium
confidence_basis: Samsung、SK hynix 與 Micron 三條獨立一手來源可確認各自揭露的客製範圍與階段，但用語、產品世代、客戶、qualification、NRE、量產與財務口徑不同，因此只能建立分層框架，不能做供應商領先排名
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-03
from: initial
to: inbox
reason: frozen_candidate_selected_for_scope_disambiguation
evidence: source_chain:custom-hbm-scope-ladder-20260803
-->
<!-- transition
date: 2026-08-03
from: inbox
to: triaged
reason: separated_customization_object_sampling_qualification_and_production
evidence: sources:S1,S2,S3,S4,S5
-->

<!-- research_source
source_id: S1
role: company_release
source_kind: document
publisher: Samsung Electronics
title: Samsung Ships Industry-First Commercial HBM4 With Ultimate Performance for AI Computing
published_at: 2026-02-12
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing
locator: Comprehensive Yet Agile Production Capabilities 最後一段；HBM4E 樣品與 custom HBM 2027 客戶樣品時程
limitation: Samsung 自述的 roadmap 與商業主張不證明 2027 樣品一定如期、具名客戶資格、量產或相對競爭位置
independence_group: samsung-electronics
-->

<!-- research_source
source_id: S2
role: company_release
source_kind: document
publisher: Samsung Electronics
title: 삼성전자 세계 최초 업계 최고 성능의 HBM4 양산 출하
published_at: 2026-02-12
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://news.samsung.com/kr/%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90-%EC%84%B8%EA%B3%84-%EC%B5%9C%EC%B4%88-%EC%97%85%EA%B3%84-%EC%B5%9C%EA%B3%A0-%EC%84%B1%EB%8A%A5%EC%9D%98-hbm4-%EC%96%91%EC%82%B0-%EC%B6%9C%ED%95%98
locator: 2026년 HBM4E·2027년 Custom HBM 샘플 출하로 차세대 라인업 가동；腳註定義容量、速度、電力特性與介面依客戶架構客製
limitation: 與 S1 同一公司消息鏈，只補足韓文官方頁的定義；不能當作第二條獨立驗證，也沒有具名客戶或資格結果
independence_group: samsung-electronics
-->

<!-- research_source
source_id: S3
role: competitor_primary
source_kind: document
publisher: SK hynix
title: SOD's Review GTC 2026 From Models to Infrastructure
published_at: 2026-03-27
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://news.skhynix.com/gtc-2026-review/
locator: cHBM 展示段落；Stream DQ Architecture 位於 base die，將部分 preprocessing 從 GPU 移到 base die
limitation: 公司展場回顧與自有架構效能宣稱不是共同 benchmark、客戶 qualification、量產或財務貢獻
independence_group: sk-hynix
-->

<!-- research_source
source_id: S4
role: competitor_primary
source_kind: document
publisher: Micron
title: Micron Fiscal Q4 2025 Earnings Slides
published_at: 2025-09-23
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://investors.micron.com/static-files/5fb98d73-2134-4446-8d1b-0f90285f6c02
locator: p.13 Data center HBM4E；standard 與 customized base logic die、TSMC 製造分工及毛利預期
limitation: 管理層揭露的是 HBM4E 選項與預期；未提供客戶名稱、NRE、qualification、量產數量或已實現毛利
independence_group: micron
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: document
publisher: Samsung Electronics
title: Samsung Electronics Begins Shipment of Industry-First HBM4E Samples
published_at: 2026-05-29
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://news.samsung.com/global/samsung-electronics-begins-shipment-of-industry-first-hbm4e-samples
locator: 標題、產品配置與量產段落；12-layer HBM4E 樣品已出貨，使用 Samsung Foundry 4nm logic base die，量產仍依客戶時程
limitation: 這是標準 HBM4E 樣品的公司公告，不能替代 2027 custom HBM 樣品、具名客戶 qualification 或量產證據
independence_group: samsung-electronics
-->

<!-- research_source
source_id: S6
role: company_release
source_kind: living_index
publisher: Samsung Electronics
title: Samsung Global Newsroom HBM4 Index
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://news.samsung.com/global/tag/hbm4
locator: 2026-08-03 查得 HBM4、HBM4E、合作與後續 custom HBM 文件入口
limitation: 動態標籤頁只供未來重查；新標題不能替代附件內容或刷新證據時鐘
independence_group: samsung-electronics
-->

<!-- research_source
source_id: S7
role: competitor_primary
source_kind: living_index
publisher: SK hynix
title: SK hynix Press Center
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://news.skhynix.com/press-center/press-release/
locator: 2026-08-03 查得 cHBM、HBM4E、樣品與量產後續入口
limitation: 新聞索引只供監測，不能證明 Stream DQ 已取得客戶資格、量產或財務貢獻
independence_group: sk-hynix
-->

<!-- research_source
source_id: S8
role: competitor_primary
source_kind: living_index
publisher: Micron
title: Micron News Releases
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://investors.micron.com/news-releases
locator: 2026-08-03 查得 HBM4E custom base logic die、樣品、qualification 與量產後續入口
limitation: IR 索引只供找到新附件；不能把管理層重複說法視為獨立新證據
independence_group: micron
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: Samsung 於 2026-02-12 表示 custom HBM 樣品預計自 2027 年開始送達客戶；同一份英文公告把 HBM4E 的 2026 下半年樣品時程與 custom HBM 的 2027 時程分開
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-02-12
basis: S1 最後一段直接列出兩個不同產品與樣品時鐘
boundary: 這是公司前瞻時程，不是 2027 樣品已交付、客戶已完成 qualification 或產品已量產
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: Samsung 的韓文官方定義把 custom HBM 描述為依客戶 AI accelerator 或 GPU 架構調整容量、速度、電力特性與介面，而不是只換一個容量 SKU
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-02-12
basis: S2 的 Custom HBM 腳註逐項列出客製欄位與客戶架構
boundary: 定義範圍不表示每一個客戶都會同時客製所有欄位，也不證明產品已完成設計或資格
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: SK hynix 在 GTC 2026 展示的 cHBM 核心是實作於 base die 的 Stream DQ Architecture，並將部分 preprocessing 從 GPU 移到 base die
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-03-27
basis: S3 的 cHBM 展示段落直接說明架構位置與工作搬移方向
boundary: 展示與公司模擬不等於通用 custom HBM 定義、跨廠可比 benchmark、具名客戶資格或量產
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C4
label: verified
status: active
claim: Micron 表示 HBM4E 會同時提供標準產品與客製 base logic die 選項，兩者的 base logic die 都由 TSMC 製造；公司預期客製版本毛利較高，但沒有表示該毛利已實現
supporting_source_ids: S4
contrary_source_ids:
as_of: 2025-09-23
basis: S4 p.13 逐項列出產品選項、TSMC 分工與 expect higher gross margins 的管理層預期
boundary: 這不證明具名客戶、qualification、NRE、量產數量、實際售價或已實現毛利，也不能與其他公司的客製層次直接排名
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C5
label: inference
status: active
claim: 截至 2026-08-03，Custom HBM 應被研究成「客製對象 × 商用階段」矩陣，而不是單一供應商賽跑：Samsung 公開的是客戶規格範圍與 2027 樣品時鐘，SK hynix 展示的是 base-die 工作負載下放，Micron 揭露的是 HBM4E 客製 base logic die 與 foundry 分工；三者尚無共同產品定義、qualification 或量產分母
supporting_source_ids: S1,S2,S3,S4,S5
contrary_source_ids:
as_of: 2026-08-03
basis: S1／S2、S3、S4 分屬三個獨立公司消息鏈，揭露的客製對象與階段不同；S5 又證明 Samsung 已出貨的 HBM4E 樣品不能自動視為 2027 custom HBM 樣品
boundary: 不以公告日期、產品名稱、公司自述效能或毛利預期計算領先分數，不推估客戶份額、TAM、台灣供應商訂單或市場是否反映
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: unverified
status: active
claim: 三家公司公開的 custom HBM 已能用同一口徑比較客戶數、qualification、NRE、量產數量、售價、良率或毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-03
basis: 現有文件分別提供 roadmap、展示架構與管理層產品選項，沒有共同定義、具名客戶、測試條件、數量或已實現財務欄位
boundary: 不可把「都有 custom HBM」改寫為處在同一產品世代或同一商用階段
verification_needed: 至少兩家供應商及其客戶交叉揭露同一產品世代、客製欄位、sample／qualification／production 時點、數量與可核對財務口徑
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: unverified
status: active
claim: universe 內記憶體、IC 設計或封測公司已因 custom HBM 取得可辨識 design win、qualification、訂單、收入或毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-03
basis: Samsung、SK hynix 與 Micron 的文件沒有完成任何 universe 公司與客戶產品、資格及財務的雙向核對
boundary: HBM、base die、ASIC、TSV、bonding 或測試能力只形成搜尋路由，不是受惠事實
verification_needed: 平台／記憶體供應商與台灣公司端須同時揭露具名產品、客戶資格、量產出貨及可辨識財務貢獻
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C4,C5,C6
metric: custom HBM 客製欄位、實體樣品、具名客戶與 qualification 階段
source_ids: S1,S2,S3,S4,S5
watch_source_ids: S6,S7,S8
frequency: event_driven
frequency_detail: Samsung、SK hynix 或 Micron 發布 custom HBM 樣品、客戶設計或 qualification 文件時重審
next_check: 2026-09-15
trigger: 至少一家交付可定位的 custom HBM sample 並揭露客製對象、產品世代、接收方與 qualification 條件
invalidation: 2027 樣品時程延後、架構停留展示、客戶改採標準 HBM，或公開資料顯示客製成本與良率無法通過資格
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C4,C6,C7
metric: NRE、量產、售價、良率、毛利與台灣供應鏈財務足跡
source_ids: S3,S4
watch_source_ids: S7,S8
frequency: quarterly
frequency_detail: 每季檢查供應商季報與法說；只有共同口徑與雙向公司證據才建立比較或公司線
next_check: 2026-09-23
trigger: 公司揭露已實現 custom HBM 收入／毛利或具名客戶 qualification，且能和產品範圍及量產時點對上
invalidation: 管理層只重複較高毛利或合作敘事，沒有 NRE、產品資格、量產與財務分母
-->

<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_glossary_for_repeated_terms_no_conclusion_change
evidence: editorial:high_frequency_glossary
-->
<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_plain_language_wave2_no_conclusion_change
evidence: editorial:plain_language_wave2
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **HBM（高頻寬記憶體）**：把多層 DRAM 垂直堆疊、放在運算晶片附近，以很寬的介面提供高頻寬。
- **Logic base die（堆疊底部邏輯晶片）**：位在 HBM 堆疊底部，負責介面、資料路徑與控制；能做多少額外運算要看實際設計。
- **Custom HBM（客製高頻寬記憶體）**：不是一套已有共同規格的單一產品。公開資料可能指容量或介面客製、底部邏輯晶片客製，或把部分工作搬到記憶體附近。
- **樣品／客戶驗證／量產（sample／qualification／production）**：樣品可供測試，客戶驗證代表完成指定條件，量產才是穩定製造；三個節點不能互相代替。
- **HBM4E**：供應商對 HBM4 後續強化版本使用的產品名稱；公開文件中的 HBM4E 不必然採用相同客製範圍或時程。
- **Stream DQ**：SK hynix 展示的底部邏輯晶片架構名稱，將部分資料前處理從 GPU 移到 HBM 底部；架構展示不等於已送樣或量產。
- **ASIC（特殊用途晶片）**：為特定功能設計的晶片；本文只用它描述可能承擔客製邏輯的角色，不代表任何台灣公司已取得設計案。

### 三句話抓重點

- Samsung 把客製 HBM 的客戶樣品放在 2027，且韓文官方頁把客製範圍寫到容量、速度、電力與介面。
- SK hynix 展示的是底部邏輯晶片上的 Stream DQ 工作負載下放；Micron 談的是 HBM4E 客製底部邏輯晶片、TSMC 製造與較高毛利預期。
- 這些資料證明「客製」正往更多層次延伸，卻不足以比較誰領先；要先對齊客製對象、世代、樣品、客戶資格與量產。

### 為什麼重要

若把所有客製 HBM 放在同一排行榜，公告得早、效能數字大或使用「量產」一詞的公司會看起來
領先。但它們可能根本在談不同東西：標準 HBM4E 樣品、底部邏輯晶片客製、工作負載下放，
甚至只是下一代產品的共同設計。

第一個判讀軸是「客製什麼」：容量、速度、電力、介面、底部邏輯，還是特定工作負載。
第二個軸是「做到哪裡」：架構、送樣、客戶驗證、量產或已認列收入。只有兩個軸都對齊，
才適合比較進度。

這樣拆開後，讀者才能判斷價值可能落在 DRAM、邏輯設計、晶圓製造、封裝測試或客戶軟體，
也不會把整個 HBM4E 的量產時程誤套到仍未送樣的客製 HBM。

### 接下來怎麼追

- 每一家公司先填「客製什麼」：容量、速度、電力、介面、底部邏輯，或特定工作負載。
- 再填「做到哪裡」：架構設計、送樣、客戶驗證、量產或財務認列。
- 只有客戶與供應商雙方都能對上產品、測試條件與時點，才把客戶驗證標成完成。
- 談較高毛利時，區分管理層預期與實際認列；沒有 NRE、售價、良率或毛利分母就不比較。

### 想一想

- 若一家公司只客製底部邏輯晶片，另一家公司把資料前處理也移入底部邏輯晶片，兩者能用同一個「客製進度」排名嗎？
- 客製提高單位價值時，是否也增加 NRE、qualification 時間、良率與單一客戶風險？
- HBM4E 樣品已出貨，為什麼不能直接證明 custom HBM 已送樣？

## 三種公開說法不能合併

| 公司 | 公開客製對象 | 本輪可確認的階段 | 不能外推 |
|---|---|---|---|
| Samsung | 客戶架構下的容量、速度、電力與介面 | 2027 客戶樣品 roadmap；另有標準 HBM4E 樣品 | Custom 樣品已交付、客戶 qualification、量產 |
| SK hynix | Base die 的 Stream DQ 與 preprocessing | 架構展示 | 共同 benchmark、具名客戶、量產 |
| Micron | HBM4E 客製 base logic die 與 foundry 分工 | 產品選項／客戶討論與毛利預期 | 已實現較高毛利、客戶資格、量產數量 |

這張表刻意不做正規化。三列的「客製對象」與「階段」不同，公告年份也不是同一產品的完成時間；
因此 `not comparable` 是研究結果，而不是缺少一個更聰明的加權公式。

## 來源與證據邊界

- [Samsung HBM4／Custom HBM roadmap](https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing)（2027 樣品時程）。
- [Samsung 韓文官方定義](https://news.samsung.com/kr/%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90-%EC%84%B8%EA%B3%84-%EC%B5%9C%EC%B4%88-%EC%97%85%EA%B3%84-%EC%B5%9C%EA%B3%A0-%EC%84%B1%EB%8A%A5%EC%9D%98-hbm4-%EC%96%91%EC%82%B0-%EC%B6%9C%ED%95%98)（客製欄位）。
- [SK hynix GTC 2026 review](https://news.skhynix.com/gtc-2026-review/)（Stream DQ 與 base die）。
- [Micron FY2025 Q4 slides](https://investors.micron.com/static-files/5fb98d73-2134-4446-8d1b-0f90285f6c02)（p.13，標準／客製 base logic die 與管理層毛利預期）。
- [Samsung HBM4E sample shipment](https://news.samsung.com/global/samsung-electronics-begins-shipment-of-industry-first-hbm4e-samples)（標準 HBM4E 樣品與 custom 時鐘的分界）。

本文不採用三家公司自述效能做跨公司比較，也不把客戶數、HBM 總銷售或 HBM4 量產套用到
custom HBM。現有資料沒有同一產品世代、共同 benchmark、客戶資格、數量與財務定義，因此不報
領先者、TAM、市占或市場是否反映。

## 影響路由

<!-- impact
group_id: memory
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-15
rationale: Custom HBM 可能改變 DRAM 與 base-die 價值分配，但本輪沒有 universe 記憶體公司的具名 custom HBM 產品、客戶資格或財務證據
evidence_boundary: HBM 產能、記憶體景氣或一般 HBM 客戶不等於 custom HBM design win、量產與較高毛利
-->

<!-- impact
group_id: packtest
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-15
rationale: 客製 base die 與堆疊形成 bonding、TSV、測試與熱管理搜尋入口，但產品世代與 qualification 尚未對齊
evidence_boundary: 具備 HBM 封測能力不等於參與任一具名 custom HBM、取得訂單或收入
-->

<!-- impact
group_id: ipdesign
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-15
rationale: Base-die 邏輯與客戶 ASIC 共同設計可能增加介面、控制與邏輯 IP，但沒有 universe 公司被供應商或客戶具名
evidence_boundary: 可設計高速介面或 ASIC 不證明 custom HBM IP tape-out、qualification、NRE 或財務貢獻
-->

## 下一個可證明／否定的節點

- 供應商交付實體 custom HBM sample，並說清楚產品世代、客製欄位、接收方與測試條件。
- 客戶端獨立確認 qualification，而不是只有記憶體供應商說正在合作。
- 將 base-die 工作負載下放放入可重現 workload，揭露 latency、power、thermal 與端到端限制。
- 季報或法說把 custom HBM 的 NRE、量產、售價、良率或毛利從預期升級為可核對結果。
- 台灣公司必須由平台／記憶體端與公司端完成產品、資格、出貨及財務雙向核對，否則只保留族群搜尋路由。
