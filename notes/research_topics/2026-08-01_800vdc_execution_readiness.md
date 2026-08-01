# 800VDC 從路線圖進入 2026 系統展示與驗證，full-scale 仍待 2027

<!-- research_topic
topic_id: MI-2026-08-01-800VDC-EXECUTION-READINESS
schema_version: 1
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
evidence: source_chain:nvidia-800v-ecosystem-update-20260731
-->

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
