# 800VDC 從路線圖進入 2026 系統展示與驗證，full-scale 仍待 2027

<!-- research_topic
topic_id: MI-2026-08-01-800VDC-EXECUTION-READINESS
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-01
source_published_at: 2025-05-20
last_reviewed_at: 2026-08-01
review_due: 2026-08-08
source_type: mixed
publisher_domain: nvidia.com
canonical_url: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/
source_chain_id: nvidia-800v-ecosystem-update-20260731
stock_ids: 2301,2308,8255
group_ids: power,powersupply,thermal
trigger_type: architecture_update_and_validation
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C4
base_confidence: medium
confidence_basis: 架構、展示與公司產品階段有一手資料，但客戶驗收、量產與財務貢獻尚未證實
cross_company_numbers: false
schema_migrated_at: 2026-08-02
-->

<!-- transition
date: 2026-08-01
from: initial
to: inbox
reason: primary_source_architecture_and_company_stage_scan
evidence: source_chain:nvidia-800v-ecosystem-update-20260731
-->
<!-- transition
date: 2026-08-01
from: inbox
to: triaged
reason: separated_800v_validation_from_50v_shipments_and_2027_full_scale_timing
evidence: sources:S1,S2,S3,S4,S5
-->

<!-- research_source
source_id: S1
role: company_release
publisher: NVIDIA
title: 800V HVDC architecture 技術文章
published_at: 2025-05-20
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/
locator: 1MW racks、2027 Kyber 與 full-scale production 段落
limitation: 效率與 TCO 數字是架構目標，未提供客戶營運實績或量產數量
-->

<!-- research_source
source_id: S2
role: company_release
publisher: NVIDIA
title: GTC Taipei 800V power rack 與 hybrid bridge 更新
published_at: 2026-06-01
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/
locator: 800VDC power rack 與 hybrid AC bridge 段落
limitation: 參考設計與生態系列名不等於資料中心全面部署或供應商訂單
-->

<!-- research_source
source_id: S3
role: company_release
publisher: Delta Electronics
title: 台達電 GTC 800VDC 系統展示
published_at: 2026-03-16
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.delta-americas.com/en-US/news/40116
locator: 660kW power rack、480kW BBU 與 2.4MW CDU 展示規格
limitation: 展示規格與公司效能主張不證實客戶驗收、量產數量、收入或毛利
-->

<!-- research_source
source_id: S4
role: company_release
publisher: LITEON Technology
title: 光寶科 2026Q1 結果與電源產品時程
published_at: 2026-04-29
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.liteon.com/en/news/press-center/content/quarterly-first-eps-2026
locator: 50V power rack、110kW power shelf 與 800V validation 段落
limitation: 公司時程不等於驗證完成、量產出貨或客戶採購承諾
-->

<!-- research_source
source_id: S5
role: company_release
publisher: LITEON Technology
title: 光寶科 2026 年 6 月營收
published_at: 2026-07-09
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.liteon.com/en/news/press-center/content/liteon-monthly-sales-june-2026
locator: Cloud and AIoT 營收占比與成長段落
limitation: 月營收沒有拆出 800V 產品，不能把整體 Cloud and AIoT 成長歸因於 800V
-->

<!-- research_source
source_id: S6
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-08-01 以台灣電源供應商代號重查重大訊息、法說與季度財報的入口
limitation: 查詢入口會持續更新；入口本身不證明 800V 驗證、量產、訂單或財務貢獻
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: NVIDIA 仍把 1MW 以上機櫃與 800VDC full-scale production 錨定於 2027 Kyber 世代
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-07-31
basis: NVIDIA 更新後的技術文章直接提供架構定位與量產時鐘
boundary: 這是平台商路線圖，不是已完成的客戶驗收、部署量或營收
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: 台達電已展示 800VDC power rack、BBU 與 CDU 系統規格
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-03-16
basis: 公司官方展示公告列出系統與功率規格
boundary: 證實的是展示內容，不代表客戶訂單、量產、利用率或財務貢獻
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: 光寶科表示 50V power rack 已量產、110kW power shelf 已出貨，而 800V power rack 預計在 2026 下半年進入驗證
supporting_source_ids: S4
contrary_source_ids:
as_of: 2026-04-29
basis: 公司季度結果直接區分量產、出貨與待驗證三個產品階段
boundary: 50V 出貨不可改寫成 800V 出貨，預計驗證也不等於驗證完成
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C4
label: inference
status: active
claim: 2026 年較合理的基準情境是 800VDC 從參考設計與展示走向驗證的過渡期，而非全面商用年
supporting_source_ids: S1,S2,S3,S4
contrary_source_ids:
as_of: 2026-07-31
basis: 平台量產時鐘仍在 2027，供應商證據分別停在展示、過渡產品量產與 800V 驗證
boundary: 沒有全產業客戶驗收、部署數、出貨占比或供應商收入資料可估計轉換速度
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: 台達電、光寶科或其他台灣供應商已由 800VDC 取得可量化的大規模訂單與獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-01
basis: 現有來源是架構、展示、驗證時程與未拆分的 Cloud and AIoT 營收
boundary: 不建立 800V 客戶、出貨量、收入占比、市占、毛利或朋程供應關係
verification_needed: 需平台客戶驗收與台灣公司法說或財報雙向核對產品、數量及財務貢獻
resolution:
-->

<!-- research_claim
claim_id: C6
label: verified
status: active
claim: 光寶科 2026 年 6 月 Cloud and AIoT 營收年增逾 80%、占營收 56%，成長驅動包含高階伺服器電源與 BBU
supporting_source_ids: S5
contrary_source_ids:
as_of: 2026-07-09
basis: S5 直接揭露事業占比、年增幅與高階資料中心伺服器電源及 BBU 需求背景
boundary: 公司沒有把 Cloud and AIoT 增量拆為 800V 產品收入，不能以此證明 800V 已出貨或貢獻獲利
verification_needed:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C4
metric: 800VDC 客戶驗證、資料中心部署與 2027 full-scale production 時程
source_ids: S1,S2
watch_source_ids: S6
frequency: monthly
frequency_detail: 每月平台更新與重大產品發布
next_check: 2026-08-08
trigger: NVIDIA 或客戶首次揭露通過驗收、部署機櫃數、功率規模或正式量產日期
invalidation: 若 2027 時程延後或客戶持續只採 hybrid bridge，快速全面切換假說失效
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C2,C3,C5,C6
metric: 台灣電源供應商 800V 產品的驗證、出貨、收入占比與毛利
source_ids: S3,S4,S5
watch_source_ids: S6
frequency: quarterly
frequency_detail: 每季法說、財報與月營收後複核
next_check: 2026-10-31
trigger: 公司首次明確區分 800V 客戶驗證、量產數量及財務貢獻
invalidation: 若成長只來自 50V 或其他 Cloud and AIoT 產品，800V 個股受惠映射維持未證
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **800VDC**：以約 800 伏特直流電在資料中心傳送電力，目的是降低超高功率機櫃的電流、線材與轉換損耗。
- **Power rack**：集中把資料中心電力轉換、分配給多個運算機櫃的電源系統，不等於伺服器本身。
- **BBU**：電池備援單元，停電或負載突升時短暫供電，避免高功率 AI 機櫃中斷。
- **驗證**：客戶測試產品是否符合規格與可靠度；開始驗證不等於驗證完成或已大量出貨。

### 三句話抓重點

- NVIDIA 仍把 800VDC full-scale production 放在 2027，2026 的證據主要是參考設計、系統展示與供應商驗證。
- 台達電已展示高功率系統，光寶科則清楚區分 50V 已量產與 800V 待驗證，兩者不能混成同一個出貨故事。
- 真正需要等待的是客戶驗收、正式量產數量，以及台灣供應商可辨識的收入與毛利，而不是更多合作夥伴名單。

### 為什麼重要

800VDC 可能改變資料中心從配電、電源轉換到備援與散熱的價值分配，但路線圖、展示、驗證與量產是完全不同的商業階段。若沒有先拆開，讀者很容易把 2027 的架構方向提前當成 2026 的訂單與獲利。

### 接下來怎麼追

- 追平台或客戶是否公布通過驗收、部署機櫃數、功率規模與正式量產日期。
- 追台達電、光寶科法說是否首次拆出 800V 的客戶、出貨、收入占比與毛利，而非只談整體 AI 電源成長。

### 想一想

- 一項產品從展示走到驗證，再走到量產，哪一個階段最容易被市場提前重複計價？
- 若 50V 過渡產品持續成長但 800V 驗證延後，這對供應商的收入與長期技術方向各代表什麼？

## 為何值得進佇列

真正的研究問題不是「800V 比 54V 新」，而是 2026 年的系統展示、參考設計與驗證，何時
轉成客戶驗收、量產出貨及可辨識的營收／毛利。NVIDIA 7 月 31 日更新技術文章後，仍把
1MW 以上機櫃與 800VDC full-scale production 錨定在 2027 Kyber；這使 2026 成為重要但
容易被誤讀的過渡年。現階段最有價值的訊號，是 50V 過渡產品已量產、800V 產品開始驗證，
不是 800V 資料中心已全面商用。

## 已驗證的成熟度階梯

| 層級 | 一手來源明講的事實 | 不能外推的結論 |
|---|---|---|
| 架構路線圖 | NVIDIA 表示 800VDC 用來支援 1MW 以上機櫃，full-scale production 將與 2027 Kyber 同步；頁面於 2026-07-31 更新合作夥伴與命名 | 2026 已大規模建置、效率／TCO 目標已由客戶實績驗證 |
| 設施過渡 | NVIDIA 2026 GTC Taipei 說明 MGX-compatible 800V power racks 可作為既有 AC 設施的 hybrid AC／800V bridge | 所有資料中心會一次由 50／54V 切換為 800V |
| 系統展示 | 台達電在 GTC 展示 660kW power rack、480kW BBU 與 2.4MW CDU；98% 等數字是公司展示規格 | 客戶訂單、量產數量、利用率、收入或毛利 |
| 公司產品節點 | 光寶科 4 月表示 50V power rack 已量產、110kW power shelf 已出貨；800V power rack 預計 2026H2 進入驗證 | 把 50V 出貨改寫成 800V 出貨，或把驗證改寫成量產 |
| 需求背景 | 光寶科 7 月公告 6 月 Cloud & AIoT 營收年增逾 80%、占營收 56%，驅動力包含高階伺服器電源與 BBU | 該增量由 800V 產品貢獻；公司未作此拆分 |

## 來源與證據邊界

- [NVIDIA 800VDC 技術文章](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)（2025-05-20；2026-07-31 更新）。
- [NVIDIA GTC Taipei／COMPUTEX 2026 更新](https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/)（800V 段落為 2026-06-01）。
- [台達電 GTC 系統展示](https://www.delta-americas.com/en-US/news/40116)（2026-03-16）。
- [光寶科 2026Q1 結果與產品時程](https://www.liteon.com/en/news/press-center/content/quarterly-first-eps-2026)（2026-04-29）。
- [光寶科 2026 年 6 月營收](https://www.liteon.com/en/news/press-center/content/liteon-monthly-sales-june-2026)（2026-07-09）。

NVIDIA 列名 Delta、LITEON 只能證實生態系參與；對 2301 而言，800V 仍停在公司預定的
驗證節點，對 2308 而言目前是系統展示，對 8255 則連 NVIDIA 列名都沒有。NVIDIA 所列
最高 5% 端到端效率改善、減銅、維護與 TCO 數字屬架構模型／目標，並非第三方驗證實績。
本輪沒有一致預期、估值或即時持倉資料，因此不宣稱市場尚未反映或已充分定價。

## 投資判讀框架

- **主要驅動 KPI**：800V 客戶驗證完成、量產日期、客戶驗收與收入認列。
- **次要 KPI**：power shelf／BBU／DC-DC／CDU 的單櫃內容量、AI 電源營收占比與毛利轉換。
- **常見假訊號**：合作夥伴 logo、展場 demo、效率目標，或把 50V 過渡產品出貨當成 800V 出貨。
- **最關鍵分歧**：價值是否由單顆 PSU 擴大到整個 power rack、備援與冷卻控制系統；若只增加研發與資本投入而未改善收入／毛利，題材不成立。

## 影響路由

<!-- impact
group_id: powersupply
stock_ids: 2301,2308
direction: mixed
hypothesis_refs: 2301:H1,2308:H1
note_action: review_due
action_due: 2026-08-08
rationale: 2301 已有 50V 量產與 800V 驗證時程，2308 有 800V 系統級展示，下一步需用公司 IR 區分驗證、量產、收入與毛利
evidence_boundary: NVIDIA 生態系名單與公司展示不證實新增訂單、出貨占比、市占或獲利
-->

<!-- impact
group_id: power
stock_ids: 8255
direction: uncertain
hypothesis_refs: 8255:H1,8255:H2
note_action: review_due
action_due: 2026-08-08
rationale: 既有 H1 與 H2 直接主張切入 800V HVDC 與 TOLT／QDPAK 量產，應用下一份公司文件核對客戶驗證與量產節點
evidence_boundary: 本批 NVIDIA、台達電與光寶科來源均未點名朋程，不構成朋程供應關係或營收證據
-->

<!-- impact
group_id: thermal
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-08
rationale: 台達電把 800V power rack、BBU 與 MW 級 CDU 整合展示，顯示電源與液冷可能成為共同系統設計問題
evidence_boundary: 來源未點名 universe 內其他散熱廠，也未證實 800V 對散熱內容量或毛利的淨增量
-->

## 下一個可證明／否定的節點

- 光寶科 2026H2 是否正式揭露 800V 驗證結果、客戶採用、量產日與收入占比；驗證延後即為最直接反證。
- 台達電是否把展示規格推進到客戶量產、實際交付與可辨識的電源／散熱財務貢獻。
- 朋程是否以一手文件證實 800V HVDC 客戶、封裝料號、驗證完成與量產，而不是只保留研究假說。
- 安全、介面與維修標準若延誤，或客戶延長 50／54V 過渡期，2027 full-scale 時程需下修。
- 若只有合作名單、展場規格或股價反應而沒有公司級收入／毛利證據，維持 `watch`，不得升格。
