# 開放 AI 互連不是單一標準戰：UALink 管 scale-up，UEC 管 scale-out

<!-- research_topic
topic_id: MI-2026-08-02-OPEN-AI-FABRICS
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-04-07
last_reviewed_at: 2026-08-02
review_due: 2026-08-10
source_type: mixed
publisher: UALink Consortium
publisher_domain: ualinkconsortium.org
canonical_url: https://ualinkconsortium.org/wp-content/uploads/2026/04/UALink-2.0-Specification-PR_FINAL.pdf
source_chain_id: open-ai-fabrics-ualink-uec-20260802
stock_ids:
group_ids: serverodm,ipdesign,pcb
trigger_type: interconnect_specification_and_platform_update
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C5
base_confidence: medium
confidence_basis: UALink、UEC、AMD、Oracle 與 Marvell 一手來源可交叉確認 scale-up／scale-out 分工、規格與具名規劃；但合規互通、商用 silicon、Oracle 實際可用狀態及台灣財務曝險仍待驗證
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: primary_source_open_interconnect_scan
evidence: source_chain:open-ai-fabrics-ualink-uec-20260802
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_scale_up_scale_out_specification_product_and_deployment_stages
evidence: sources:S1,S2,S3,S4,S5
-->

<!-- research_source
source_id: S1
role: standard
source_kind: document
publisher: UALink Consortium
title: UALink Consortium Publishes UALink 2.0 Specifications
published_at: 2026-04-07
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ualinkconsortium.org/wp-content/uploads/2026/04/UALink-2.0-Specification-PR_FINAL.pdf
locator: page 1 New UALink Specifications；page 2 UCIe 3.0 compliance 與 future interoperability／compliance programs
limitation: 規格 ratification 不等於 multi-vendor silicon、交換器、互通測試、客戶部署或收入
independence_group: ualink-consortium
-->

<!-- research_source
source_id: S2
role: standard
source_kind: document
publisher: Ultra Ethernet Consortium
title: UEC Launches Specification 1.0 for AI and HPC at Scale
published_at: 2025-06-11
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ultraethernet.org/ultra-ethernet-consortium-uec-launches-specification-1-0-transforming-ethernet-for-ai-and-hpc-at-scale/
locator: Specification 1.0 launch；AI／HPC scale-out network；NIC、switch、optics 與 cable ecosystem 段落
limitation: 初版規格與生態系範圍不證明各元件已量產、互通、部署或取得市場份額
independence_group: ultra-ethernet-consortium
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: living_index
publisher: Advanced Micro Devices
title: AMD Helios Rackscale Solution
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.amd.com/en/products/rackscale-solutions/helios.html
locator: 2026-08-02 查得 Helios scale-up cartridges、UALink／UALoE、UEC-ready scale-out 與 reference design FAQ
limitation: AMD 產品頁與工程規格不等於所有合作夥伴已出貨、客戶驗收、雲端 GA 或財務貢獻
independence_group: amd
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: document
publisher: Advanced Micro Devices and Oracle
title: Oracle and AMD Expand Partnership to Help Customers Achieve Next-Generation AI Scale
published_at: 2025-10-14
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://newsroom.amd.com/news/oracle-and-amd-expand-partnership-to-help-customers-achieve-next-gen-ai-scale/
locator: Q3 2026 initial deployment plan；Helios rack design；UALink protocol over UALoE fabric 段落
limitation: 這是前瞻部署計畫；截至本輪未找到 Oracle 已公開 GA、實際部署數、利用率或收入的後續一手確認
independence_group: amd-oracle-joint
-->

<!-- research_source
source_id: S5
role: competitor_primary
source_kind: document
publisher: Marvell Technology
title: Marvell Expands Custom Compute Platform with UALink Scale-up Solution
published_at: 2025-06-11
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.marvell.com/company/newsroom/marvell-expands-custom-compute-platform-with-ualink.html
locator: custom UALink offering；interoperable IP portfolio；accelerator-to-switch scale-up 段落
limitation: 公司產品公告不等於客戶採用、量產出貨、收入占比或開放標準已完成多廠互通
independence_group: marvell
-->

<!-- research_source
source_id: S6
role: standard
source_kind: living_index
publisher: UALink Consortium
title: UALink Specifications
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ualinkconsortium.org/specification/
locator: 2026-08-02 查得公開 UALink specifications 與後續規格入口
limitation: 規格索引只用來偵測版本、合規與互通更新；不能視為產品或部署證據
independence_group: ualink-consortium
-->

<!-- research_source
source_id: S7
role: standard
source_kind: living_index
publisher: Ultra Ethernet Consortium
title: Ultra Ethernet Specification History
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ultraethernet.org/specification-history/
locator: 2026-08-02 顯示 UEC 1.0.3 於 2026-07-16 發布並為 current published version
limitation: 版本歷史不證明 silicon、NIC、switch、optics 或 cable 完成互通與客戶部署
independence_group: ultra-ethernet-consortium
-->

<!-- research_source
source_id: S8
role: company_release
source_kind: living_index
publisher: Advanced Micro Devices
title: AMD Newsroom
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://newsroom.amd.com/
locator: 2026-08-02 查得 Helios、MI450、Oracle 與其他客戶部署更新入口
limitation: 新聞索引只用來找到新文件；合作、production、shipment、online 與 GA 必須逐一區分
independence_group: amd
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: UALink Consortium 於 2026-04-07 ratify 2.0 系列規格，定位仍是 accelerator scale-up interconnect，並表示後續才會導入 interoperability 與 compliance programs
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-04-07
basis: S1 的標題、組織定位、新規格列表與 page 2 future programs 段落
boundary: 規格完成不等於互通計畫已運作、商用產品已出貨或客戶已部署
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: UEC Specification 1.0 針對 AI／HPC scale-out Ethernet ecosystem，且截至 2026-08-02 的現行公開版本為 2026-07-16 發布的 1.0.3
supporting_source_ids: S2,S7
contrary_source_ids:
as_of: 2026-08-02
basis: S2 定義 scale-out 與元件範圍，S7 直接列出 1.0.3 的日期與 current published version 狀態
boundary: 規格版本更新不等於 UEC 產品在資料中心完成互通、部署或形成財務貢獻
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: AMD Helios 的公開架構同時把 UALink／UALoE 用於 scale-up，並把 Pensando networking 描述為 UEC-ready 的 Ethernet scale-out 路徑
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-08-02
basis: S3 的 scale-up cartridges、scale-out advantage、Pensando AI NIC 與 FAQ 段落
boundary: Reference design 與產品頁規格不等於多廠互通、OEM 量產、客戶驗收、雲端可用或收入
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C4
label: verified
status: active
claim: Oracle 與 AMD 在 2025-10-14 公告規劃自 2026 年第三季起部署 MI450／Helios 叢集，架構使用 UALink protocol over a UALoE fabric
supporting_source_ids: S4
contrary_source_ids:
as_of: 2025-10-14
basis: S4 的 deployment plan、Helios rack design 與 UALink／UALoE 段落
boundary: 這只證實公開規劃；截至 2026-08-02 未由本來源證實部署已開始、公開 GA、實際數量、利用率或收入
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C5
label: inference
status: active
claim: 開放 AI 互連目前較合理的研究框架不是 UALink 與 UEC 二選一，而是把 pod／rack 內 accelerator scale-up 與 rack 間 Ethernet scale-out 視為互補層，再分別追規格、silicon、互通、系統與部署成熟度
supporting_source_ids: S1,S2,S3,S4
contrary_source_ids:
as_of: 2026-08-02
basis: S1 與 S2 分別定義 scale-up／scale-out，S3 把兩者放進同一 Helios 架構，S4 提供具名雲端規劃節點
boundary: 不推估標準市占、交換器／NIC TAM、台灣供應鏈份額或市場定價；規格、產品與部署不能合併計數
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C6
label: unverified
status: active
claim: Oracle 的 MI450／Helios 叢集截至 2026-08-02 已公開可用，或 universe 內公司已因 UALink／UEC 取得可辨識訂單與獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: 現有來源提供規格、reference design、產品能力與前瞻部署計畫，沒有台灣公司產品與財務的雙向核對，也沒有本輪找到的 Oracle GA 後續文件
boundary: 不以標準會員、合作 logo、ODM 能力、網通產品或 AMD 生態系角色直接建立訂單／收入關係
verification_needed: 需 Oracle 或 AMD 公告實際 preview／GA／部署，並由台灣公司揭露具名產品、qualification、出貨與財務貢獻
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: UALink 2.0 同時發布 chiplet specification，並明列該規格 fully compliant with UCIe 3.0
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-04-07
basis: S1 page 1–2 的 UALink Chiplet Specification 1.0 條目直接列示 UCIe 3.0 compliance
boundary: 規格層相容不等於實體 chiplet、package、PHY 或 multi-vendor silicon 已通過 compliance
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: Marvell 已公告 custom UALink scale-up solution 與 interoperable IP portfolio，證實產品開發路徑但未證實客戶量產
supporting_source_ids: S5
contrary_source_ids:
as_of: 2025-06-11
basis: S5 的產品公告直接列出 custom UALink offering、IP 組合與 accelerator／switch 使用位置
boundary: 公司所稱 interoperable IP 不等於第三方 multi-vendor compliance、客戶採用、量產出貨或財務貢獻
verification_needed:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C5,C7,C8
metric: UALink／UEC／UCIe 的規格版本、compliance、multi-vendor interoperability 與商用 silicon
source_ids: S1,S2,S3,S5
watch_source_ids: S6,S7
frequency: weekly
frequency_detail: 每週檢查 UALink／UEC 規格與合規頁；出現 silicon、switch、NIC、retimer 或 chiplet 測試即重審
next_check: 2026-08-10
trigger: 公布正式 compliance／plugfest 結果，或至少兩家廠商完成可核對的 multi-vendor silicon 互通
invalidation: 規格長期沒有互通與商用產品、版本持續修正關鍵行為或生態系分裂，開放標準成熟度下修
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C4,C6
metric: Oracle／AMD Helios 叢集的實際 shipment、preview、GA、部署量與台灣供應鏈財務足跡
source_ids: S4
watch_source_ids: S8
frequency: event_driven
frequency_detail: AMD、Oracle 或 OEM 公告 MI450／Helios 交付、上線與客戶可用性時檢查
next_check: 2026-08-17
trigger: Oracle 或 AMD 確認實際部署／GA，且供應商能以具名產品、qualification 與收入完成雙向核對
invalidation: Q3 2026 規劃延後、叢集未公開可用或只停在 reference design，部署與供應鏈信心下修
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **Scale-up**：讓同一個 pod 或機架內的多顆加速器像更大的共同運算單元一樣交換資料，重點是低延遲與記憶體語意。
- **Scale-out**：把多個機架或節點連成更大的叢集，重點是 Ethernet 網路、壅塞控制、路由與大規模可靠性。
- **UALink**：針對 accelerator scale-up 的開放互連規格。
- **UEC**：針對 AI／HPC scale-out Ethernet 的規格與生態系。
- **UALoE**：把 UALink protocol 放在 Ethernet 傳輸路徑上的做法；它不表示 UALink 與 UEC 已變成同一個標準。
- **Compliance／interoperability**：前者確認產品遵守規格，後者確認不同廠商產品能互相工作；規格發布時兩件事不會自動完成。

### 三句話抓重點

- UALink 與 UEC 解決的是不同距離與語意的網路層，不能只用「誰打敗誰」來閱讀。
- AMD Helios 把 UALink／UALoE 放在 scale-up，把 UEC-ready Ethernet 放在 scale-out，提供了兩層共存的具體架構。
- 截至 2026-08-02，最重要的缺口仍是 multi-vendor compliance、商用 silicon 與 Oracle 實際可用狀態；規格與規劃都不是部署。

### 為什麼重要

AI 系統的資料移動成本已跨過單一 GPU：機架內要解決 accelerator-to-accelerator，機架間又要處理
Ethernet 壅塞、路由與可靠性。如果把 scale-up 與 scale-out 混在一起，讀者會重複計算同一個平台，
也會把標準會員或產品 roadmap 提前當成交換器、NIC、光模組與 ODM 的收入。

### 接下來怎麼追

- 先看 UALink／UEC 是否公布 compliance、plugfest 或 multi-vendor interoperability，而不只看版本號。
- 再看 merchant switch、NIC、retimer、PHY 與 accelerator 是否有具名 silicon、樣品、量產與客戶。
- 對 Oracle／AMD，依序追 shipment、preview、GA、部署數與利用率；任何一步都不能跳過。

### 想一想

- 一個標準有很多會員，和兩家公司的晶片真的能互通，兩者中間還缺哪些測試與軟體證據？
- 若 UALink scale-up 成功、但 UEC scale-out 延後，Helios 能否用其他 Ethernet 路徑先部署？這對供應商映射有何差別？

## 三張表要分開

| 層級 | 已證實 | 未證實 |
|---|---|---|
| 規格 | UALink 2.0 已 ratify；UEC 現行版本為 1.0.3 | 多廠 compliance、互通與實際效能 |
| 產品／系統 | AMD Helios 公開描述 UALink／UALoE scale-up 與 UEC-ready scale-out；Marvell 有 custom UALink offering | OEM 量產、客戶驗收與供應商份額 |
| 部署 | Oracle／AMD 公告 Q3 2026 起的 MI450／Helios 規劃 | 截至本輪的 shipment、preview、GA、實際部署與利用率 |

這種拆法會讓同一件新聞只進一個格子：規格升版不會自動把產品與部署兩格一起升級；產品被
reference design 列名，也不會自動產生財務貢獻。

## 來源與證據邊界

- [UALink 2.0 release](https://ualinkconsortium.org/wp-content/uploads/2026/04/UALink-2.0-Specification-PR_FINAL.pdf)（scale-up、chiplet、UCIe 3.0 與未來 compliance）。
- [UEC Specification 1.0 launch](https://ultraethernet.org/ultra-ethernet-consortium-uec-launches-specification-1-0-transforming-ethernet-for-ai-and-hpc-at-scale/)（scale-out 與元件範圍）。
- [AMD Helios product page](https://www.amd.com/en/products/rackscale-solutions/helios.html)（scale-up／scale-out 架構與 reference design 邊界）。
- [Oracle and AMD deployment plan](https://newsroom.amd.com/news/oracle-and-amd-expand-partnership-to-help-customers-achieve-next-gen-ai-scale/)（Q3 2026 前瞻規劃）。
- [Marvell custom UALink solution](https://www.marvell.com/company/newsroom/marvell-expands-custom-compute-platform-with-ualink.html)（IP／產品開發路徑）。

本篇不使用會員數、宣稱頻寬、GPU 數或公司效能數字做跨公司比較，也不推估 TAM、市占、估值或
市場預期。Oracle 規劃已進入原訂季度，不代表部署已發生；沒有新一手文件時，狀態仍停在 planned。

## 影響路由

<!-- impact
group_id: serverodm
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-17
rationale: Helios 與開放機架會把 compute、scale-up、scale-out、電源與散熱整合成系統問題，但本輪沒有 universe ODM 的具名 UALink／UEC 量產與財務證據
evidence_boundary: Reference design、生態系夥伴或一般 AI server 能力不等於已取得 Helios／開放互連訂單
-->

<!-- impact
group_id: ipdesign
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-17
rationale: UALink、UEC、UCIe 涉及 controller、PHY、retimer、switch 與 chiplet IP，但目前只有外部公司產品與標準證據
evidence_boundary: 標準會員與可開發高速介面 IP 不證明 universe 公司完成 compliance、design win 或收入認列
-->

<!-- impact
group_id: pcb
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-17
rationale: 高速 scale-up／scale-out 會形成板級訊號、連接與光電路由研究入口，但未有具名板材、載板、連接器或光模組財務證據
evidence_boundary: 更高頻寬的工程需求不自動對應任一 PCB／CCL 公司訂單、份額或毛利
-->

## 下一個可證明／否定的節點

- UALink／UEC 公布 compliance program、plugfest 與可重現的 multi-vendor interoperability 結果。
- Merchant silicon、switch、NIC、retimer 或 chiplet 從 IP／樣品升級為 production，並有具名客戶。
- Oracle 或 AMD 確認 MI450／Helios shipment、preview 或 GA，而不是沿用 2025 年的前瞻規劃。
- 台灣公司用具名產品、qualification、出貨與財務資料完成雙向核對；否則只保留產業節點，不畫公司受惠線。
