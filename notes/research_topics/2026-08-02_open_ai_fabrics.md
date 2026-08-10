# 資料從一顆運算晶片走到另一顆：先分清機架內外，再判斷跨廠互通

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
thesis_claim_id: C9
base_confidence: medium
confidence_basis: UALink、UEC、OCP ESUN／SUE-T、AMD、Arista、Broadcom 與 Oracle 一手來源可交叉確認多條 scale-up／scale-out 路徑；但各規格的 multi-vendor compliance、實際 silicon、客戶部署、相對份額及台灣財務曝險仍待驗證
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
<!-- transition
date: 2026-08-02
from: triaged
to: triaged
reason: superseded_two_layer_ualink_uec_frame_after_esun_scale_up_evidence
evidence: sources:S9,S10,S11,S12
-->
<!-- transition
date: 2026-08-08
from: triaged
to: triaged
reason: editorial_glossary_for_repeated_terms_no_conclusion_change
evidence: editorial:readability
-->
<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_plain_language_wave2_no_conclusion_change
evidence: editorial:plain_language_wave2
-->
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave101_data_path_two_network_scopes_roles_and_six_gate_interoperability
evidence: editorial:reader_layer_only_no_claim_source_monitor_or_impact_change
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

<!-- research_source
source_id: S9
role: standard
source_kind: document
publisher: Open Compute Project Networking Project
title: The OCP ESUN 1.0 Specification Has Been Released
published_at: 2026-03-10
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.opencompute.org/blog/the-ocp-esun-10-specification-has-been-released
locator: ESUN 1.0 highlights；Ethernet scale-up、lossless、4-byte ESUN header、link-level retry 與 multi-hop 段落
limitation: OCP 規格發布與參與公司數不等於 silicon、compliance、互通、客戶部署或 UALink／UEC 的市場份額
independence_group: open-compute-project
-->

<!-- research_source
source_id: S10
role: standard
source_kind: document
publisher: Open Compute Project
title: OCP ESUN Network Operator Requirements Base Specification 1.0
published_at: 2026-02-09
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.opencompute.org/documents/ocp-esun-network-operator-requirements-base-specification-rev-1-0-final-pdf
locator: PDF 封面與 Scope／Requirements；effective 2026-02-09，定義 ESUN network operator requirements
limitation: 規格文件描述要求，不提供已通過的產品、測試報告、客戶部署、效能比較或財務資料
independence_group: open-compute-project
-->

<!-- research_source
source_id: S11
role: competitor_primary
source_kind: document
publisher: Arista Networks
title: Arista Introduces Next-Generation 1.6Terabit Portfolio for AI Fabrics
published_at: 2026-06-09
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://investors.arista.com/Communications/Press-Releases-and-Events/Press-Release-Detail/2026/Arista-Introduces-Next-Generation-1-6Terabit-Portfolio-for-AI-Fabrics/default.aspx
locator: 標題摘要與 7060XE7 前三段；產品組合明列 scale-up、scale-out、rack-scale 與 intra／inter-rack 用途
limitation: 產品公告證實具名平台與用途，不證明它遵守 ESUN 1.0、完成 multi-vendor compliance、量產部署數或市占
independence_group: arista
-->

<!-- research_source
source_id: S12
role: competitor_primary
source_kind: document
publisher: Broadcom
title: Scale-up Is Simple Ethernet Makes It Smarter
published_at: 2025-05-21
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.broadcom.com/blog/scale-up-is-simple-ethernet-makes-it-smarter
locator: Introducing the Scale-Up Ethernet framework；SUE endpoint、memory model、packet format 與貢獻給 OCP 段落
limitation: Broadcom 自述架構與產品方向不等於 OCP 最終規格、跨廠互通、客戶採用或相對 UALink 的效能／份額
independence_group: broadcom
-->

<!-- research_source
source_id: S13
role: standard
source_kind: living_index
publisher: Open Compute Project
title: OCP Networking ESUN Workstream Wiki
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.opencompute.org/wiki/Networking/ESUN
locator: 2026-08-02 查得 ESUN documents、SUE-T 分工、key focus、meeting records 與後續 specification 入口
limitation: 動態 wiki 只供追蹤新規格與會議；不能把會議、參與或草案視為產品互通與部署
independence_group: open-compute-project
-->

<!-- research_source
source_id: S14
role: competitor_primary
source_kind: living_index
publisher: Arista Networks
title: Arista Investor Press Releases and Events
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://investors.arista.com/Communications/Press-Releases-and-Events/default.aspx
locator: 2026-08-02 查得 7060XE7、Etherlink、scale-up／scale-out 與客戶部署後續入口
limitation: 新聞索引只用來找到新附件；不證明 ESUN compliance、shipment、客戶部署或收入
independence_group: arista
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
status: superseded
claim: 開放 AI 互連目前較合理的研究框架不是 UALink 與 UEC 二選一，而是把 pod／rack 內 accelerator scale-up 與 rack 間 Ethernet scale-out 視為互補層，再分別追規格、silicon、互通、系統與部署成熟度
supporting_source_ids: S1,S2,S3,S4
contrary_source_ids:
as_of: 2026-08-02
basis: S1 與 S2 分別定義 scale-up／scale-out，S3 把兩者放進同一 Helios 架構，S4 提供具名雲端規劃節點
boundary: 不推估標準市占、交換器／NIC TAM、台灣供應鏈份額或市場定價；規格、產品與部署不能合併計數
verification_needed:
corrected_by_claim_id: C9
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

<!-- research_claim
claim_id: C9
label: inference
status: active
claim: 開放 AI 互連不能再只用「UALink 管 scale-up、UEC 管 scale-out」理解；UALink 是 accelerator scale-up 路徑，OCP ESUN／SUE-T 與具名 Ethernet 平台也直接進入 scale-up，而 UEC 仍聚焦 scale-out ecosystem，研究上必須把每條路徑的規格、endpoint／switch、silicon、互通、系統與部署分開
supporting_source_ids: S1,S2,S3,S9,S10,S11,S12
contrary_source_ids:
as_of: 2026-08-02
basis: correction_of:C5；S9／S10 直接定義 Ethernet scale-up，S11 提供同時服務 scale-up／scale-out 的具名平台，S12 與 OCP 分工顯示 endpoint transport 也有獨立路徑，縮窄原先二層對應
boundary: 不推估 UALink、ESUN、SUE-T 或 UEC 的效能勝負、市占、TAM、部署分母、台灣供應鏈份額或市場定價
verification_needed:
correction_kind: supersedes
corrects_claim_id: C5
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: OCP ESUN 1.0 明確以 Ethernet 支援高效能 AI scale-up network，規格要求涵蓋 lossless／congestion management、link-level reliability、精簡 header 與 multi-hop topology
supporting_source_ids: S9,S10
contrary_source_ids:
as_of: 2026-03-10
basis: S9 的 ESUN 1.0 highlights 與 S10 正式 specification 可直接定位 network scope 與要求
boundary: 規格發布不等於 endpoint、switch ASIC、NIC 或 accelerator 已完成 compliance、互通或部署
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: verified
status: active
claim: Arista 於 2026-06-09 公告 7060XE7 1.6T 網路平台，將產品定位為同時支援 scale-up 與 scale-out AI fabrics，並涵蓋 rack-scale、intra-rack 與 inter-rack 使用
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-06-09
basis: S11 的標題摘要、產品說明與 intra／inter-rack 段落直接支持
boundary: Arista 沒有在本來源證明 7060XE7 已通過 ESUN 1.0 multi-vendor compliance、部署數、利用率或市占
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: Broadcom 公開的 SUE framework 定義 XPU endpoint、memory model、packet format 與 congestion functions，並表示已把 SUE specification 貢獻給 OCP；OCP 後續將 endpoint／transport 路徑稱為 SUE-T，與 ESUN 的 network switching／framing 分工
supporting_source_ids: S12,S13
contrary_source_ids:
as_of: 2026-08-02
basis: S12 直接描述 SUE 與 OCP contribution，S13 的現行 workstream 說明區分 SUE-T endpoint／transport 與 ESUN network side
boundary: 架構分工不等於 SUE-T 規格成熟、產品 compliance、跨廠互通或客戶部署
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C13
label: unverified
status: active
claim: ESUN 1.0 或 SUE-T 已完成 multi-vendor compliance、在 7060XE7 或其他具名平台量產部署，並已取得可和 UALink／UEC 比較的效能、份額或財務分母
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: 現有來源提供規格、工作組、架構與產品用途，沒有 ESUN／SUE-T compliance report、明確產品對應、客戶部署分母或共同比較口徑
boundary: 規格成員、產品支援 scale-up 或一般 Ethernet 出貨不能替代 ESUN／SUE-T 實作與部署證據
verification_needed: OCP compliance／plugfest、至少兩家 endpoint 與 switch silicon 實體互通、具名系統採用及客戶部署結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: retired
retired_at: 2026-08-02
retirement_reason: C5 的 UALink scale-up／UEC scale-out 二層框架已由 C9 的多路徑框架取代
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

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C1,C2,C9,C10,C11,C12,C13
metric: UALink、ESUN、SUE-T、UEC 的規格分工、endpoint／switch silicon、compliance、multi-vendor interoperability 與部署
source_ids: S1,S2,S9,S10,S11,S12
watch_source_ids: S6,S7,S13,S14
frequency: weekly
frequency_detail: 每週檢查四條標準／工作組及 Arista 等產品更新；只有規格、silicon、互通與部署各自有文件才升級
next_check: 2026-08-10
trigger: OCP／UALink／UEC 公布 compliance 或 plugfest，至少兩家 endpoint 與 switch silicon 完成互通，或具名客戶部署 ESUN／SUE-T／UALink／UEC
invalidation: 規格長期沒有實作、產品宣稱無法對應正式標準、互通失敗或客戶仍只採封閉互連，多路徑開放化信心下修
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **資料路徑**：資料從一個運算端點出發，經過連接、傳輸、交換與軟體控制，最後到達另一個端點的完整接力。
- **加速器**：專門加快人工智慧或高效能運算的晶片；有加速器不等於它已能和其他廠商晶片共同工作。
- **端點（endpoint）**：資料路徑的出發點或目的地，例如加速器、網路介面卡或它們的控制電路。
- **機架**：安裝多台運算、網路、電源與散熱設備的櫃體；「同一機架」不代表所有設備都在同一塊電路板上。
- **機架內擴充（scale-up）**：讓同一運算群組或機架內的多顆加速器高速交換資料，重點是低延遲與彼此如何使用記憶體。
- **跨機架擴充（scale-out）**：把多個機架或節點連成更大叢集，重點是路由、壅塞、大規模可靠性與故障恢復。
- **乙太網路（Ethernet）**：廣泛使用的網路技術家族；它可以服務跨機架，如今也有直接進入機架內的路徑。
- **實體層電路（PHY）**：把晶片內的數位資料轉成銅線或光模組能傳送的訊號；它只是完整路徑的一層。
- **訊號重整晶片（retimer）**：在訊號穿過較長線路後重新整理時序與形狀；信號可重整不等於上層協定已互通。
- **網路介面卡（NIC）**：伺服器連入網路的介面卡；在跨機架路徑中，它還要和交換器、光模組、線材與軟體對齊。
- **交換器**：根據目的地把資料送往正確連線的設備；它還要處理緩衝、壅塞、優先順序與故障。
- **交換器專用晶片（Switch ASIC）**：交換器內負責轉送資料的核心晶片；有晶片不等於整台交換器已通過跨廠測試。
- **封包（packet）**：網路把資料切成一段段傳送時使用的格式；兩端必須一致解讀標頭、順序與錯誤。
- **記憶體使用方式（memory model）**：規定一顆晶片如何看見、讀寫或同步另一顆晶片的記憶體資料。
- **壅塞控制**：當太多資料同時進入網路時，調整發送速度與排程，避免緩衝區滿載或延遲失控。
- **無損傳輸**：目標是在指定條件下不因壅塞丟棄封包；仍需要測試緩衝、流量控制與異常恢復。
- **連結層重試**：傳輸中發現某段資料出錯時，在連結層重新傳送；有重試機制不等於整個工作負載不會失敗。
- **多跳網路**：資料到目的地前會經過不只一台交換器；每多一跳都要再處理路由、延遲與故障。
- **拓撲**：端點、交換器與線路如何連成網路的形狀；同一規格在不同拓撲下可能有不同的瓶頸。
- **UALink（加速器互連）**：主要服務機架內多顆加速器的開放互連規格路徑。
- **UEC（超乙太網路聯盟）**：主要改善人工智慧與高效能運算跨機架乙太網路的規格生態系。
- **ESUN（機架內乙太網路交換）**：OCP 開放規格，處理機架內網路交換、封包格式、無損傳輸與可靠性。
- **SUE-T（機架內乙太傳輸）**：偏向定義加速器端點、記憶體使用方式與傳輸；它與 ESUN 分工。
- **UALoE（用乙太網路承載 UALink）**：把 UALink 協定放在乙太網路傳輸路徑上；不表示 UALink 與 UEC 是同一個標準。
- **規格文件（specification）**：描述參與者要遵守的共同語言與最低要求；發布只代表規則存在。
- **符合規格（compliance）**：依共同測試方法確認一件產品是否遵守指定版本與功能；一件產品合格不等於多家已互通。
- **跨廠互通（interoperability）**：不同公司的端點、交換器與軟體能依共同規格工作，並在錯誤與故障情境下重現結果。
- **互通測試活動（plugfest）**：多家廠商將產品帶到同一測試環境交叉連接；還要看版本、組合、測項與通過條件。
- **參考設計（reference design）**：展示元件可如何組成系統的實作範例；它證明一條路徑可被設計，不代表客戶已驗收。
- **Helios / MI450**：Helios 是 AMD 的機架級人工智慧系統參考設計，MI450 是加速器世代名稱；兩個名稱都不是 Oracle 已完成部署的證據。
- **CCL（銅箔基板）**：用銅箔與絕緣材料組成、後續可製成印刷電路板的基礎材料；有高速材料能力不等於已進入具名互連系統。
- **正式對外開放（GA）**：雲端服務正式讓符合資格的客戶可購買使用；合作公告、預覽與正式開放是三個不同節點。

### 三句話抓重點

- 一條完整資料路徑，要讓運算端點、連接傳輸、交換器、控制軟體與另一個端點接力。
- 同一機架與跨機架有不同的距離、延遲、記憶體與故障要求；乙太網路現在可能出現在兩種範圍。
- 共同規則、具名零件與單次展示都不等於跨廠互通；還要檢查版本、組合、錯誤處理、軟體與重現結果。

### 為什麼重要

人工智慧系統的運算能力會被「資料能否及時到達」限制。同一機架內，多顆
加速器常要像同一台大機器般協同；跨機架時，網路還要面對更多路徑、壅塞與故障。
兩邊可能使用相似的乙太網路元件，但驗收目標不相同，不能因名稱相似就當成同一市場。

閱讀新聞時，先把整條路徑展開，找出「資料從哪裡出發、途中經過什麼、由哪個軟體
控制、最後到哪裡」。再問測試是否同時涵蓋不同廠商、不同版本、正常傳輸、錯誤恢復與
實際工作負載。這樣才能分辨「一個零件能動」、「兩個零件能連」和「整個系統可交付」。

### 接下來怎麼追

- 先找出路徑中的運算端點、連接傳輸、交換器、控制軟體與目的端點，不要只看一顆晶片或一台設備。
- 再把 UALink、ESUN、SUE-T 與 UEC 放回機架內外的正確位置，分別追規格、實體晶片、符合規格與跨廠互通。
- 互通報告要列出廠商組合、產品版本、測試拓撲、正常與故障測項、軟體版本、通過條件與重現方法。
- 最後依序追樣品、出貨、客戶驗收、正式開放、實際部署與利用率；任何一步都不能跳過。

### 想一想

- 兩家公司的零件已能傳送正常資料，還要故意製造哪些錯誤，才能知道它們真的會一起恢復？
- 同一網路技術能用在機架內與跨機架時，研究者要如何分開低延遲、記憶體、路由與故障要求？
- 如果同一台交換器同時服務兩種範圍，如何避免把同一份埠數、出貨或收入計算兩次？

## 先用五個位置看資料怎麼從一顆晶片走到另一顆

| 本文五個位置 | 它做什麼 | 代表元件或軟體 | 下一個要驗收 | 不能直接推成 |
|---|---|---|---|---|
| 1. 資料出發的運算端點 | 產生要傳送的資料，並依共同規則發出讀寫或通訊要求 | 加速器、記憶體控制、端點協定與驅動程式 | 記憶體使用方式、版本協商、順序與錯誤回報 | 有加速器產品不等於它已能和另一廠商端點工作 |
| 2. 連接與傳輸 | 把數位資料變成能穿過銅線或光路的訊號，必要時重整或重傳 | 實體層電路、訊號重整晶片、連接器、線材與光模組 | 速度、訊號品質、線距、重試、散熱與長時間穩定度 | 物理訊號通過不等於封包、記憶體與軟體已相容 |
| 3. 交換與網路 | 把資料送到正確目的地，同時管理緩衝、壅塞、路由與故障 | 交換器專用晶片、完整交換器、網路作業系統與管理平面 | 封包格式、緩衝壓力、多跳拓撲、壅塞及異常恢復 | 產品稱可用於人工智慧，不等於它已對應某一開放規格 |
| 4. 協調與控制軟體 | 發現端點、設定路徑、調度傳輸、觀察壅塞，並在異常時恢復 | 韌體、驅動程式、通訊函式庫、網路管理、遥測與集體運算軟體 | 軟體版本、設備發現、路徑變更、故障注入、重啟與重現方法 | 單純傳得過測試封包，不等於實際工作負載會正確完成 |
| 5. 目的端點與工作負載 | 收到資料、確認完整性，再交給運算工作使用 | 另一顆加速器、網路介面卡、系統軟體與實際模型工作負載 | 資料正確、延遲、集體運算、故障後重試與長時間穩定度 | 實驗室完成一次工作不等於客戶已驗收或大規模部署 |

五個位置是最短閱讀路徑，不是完整網路協定堆疊。任何一段只有自家產品、只測正常傳輸，
或沒有公開版本與錯誤結果，都只能說該位置已有進度，不能替整條路徑宣告互通。

## 再用五把尺分開機架內與跨機架網路

| 本文五把尺 | 機架內擴充 | 跨機架擴充 | 下一個要量的結果 | 不能直接推成 |
|---|---|---|---|---|
| 1. 距離與連線形狀 | 多在同一運算群組或機架，可能使用直連或專用交換 | 連接多個機架、節點與多層交換網路 | 端點數、線距、交換跳數、連線圖與擴容後結果 | 同樣使用乙太網路不等於拓撲與用途相同 |
| 2. 延遲與記憶體 | 常要讓多顆加速器像同一台大機器快速協同，並對齊記憶體使用方式 | 重點常是在更大叢集中高效交換封包與完成集體運算 | 尾端延遲、記憶體順序、同步、工作負載完成時間 | 單一最高頻寬不等於整個工作負載更快 |
| 3. 交換、路由與壅塞 | 注重低延遲交換、緩衝、流量控制與少數跳穩定度 | 還要處理更多路徑、多跳壅塞、大規模排程與網路利用率 | 同時負載、熱點、封包積壓、公平性與擴大節點後的變化 | 一台交換器支援兩者不等於兩種網路已用同一方法驗收 |
| 4. 可靠性與恢復 | 端點或連結錯誤不能讓群組長時間停住，需要快速重試與狀態同步 | 除了連結錯誤，還要面對交換器、整條路徑與機架故障 | 故障注入、取消連線、封包丟失、重新選路與恢復時間 | 正常狀態能傳不等於故障時不會錯或停機 |
| 5. 實際工作與客戶驗收 | 要在具名加速器組合上完成集體運算、長時間運轉與系統恢復 | 要在實際叢集規模與應用上驗收效能、利用率與故障管理 | 具名工作負載、規模、期間、通過條件、客戶驗收與利用率 | 參考設計或前瞻部署日期不等於已驗收或已產生收入 |

這五把尺表示機架內與跨機架會共用部分元件，卻不共用所有驗收條件。研究公司時若沒有
埠數、用途、期間與客戶分母，就不能把同一台交換器、同一顆晶片或同一份收入算在兩邊。

## 把五條規格與傳輸路徑放回機架內外

| 本文五條路徑 | 主要範圍 | 它定義或承載什麼 | 本輪可確認 | 還不能說 |
|---|---|---|---|---|
| 1. UALink | 機架內的加速器擴充 | 加速器端點與交換互連，並包含晶粒規格路徑 | 2.0 系列規格已完成核定；組織表示互通與符合規格計畫將後續導入 | 不能說多廠晶片、交換器與軟體已通過計畫 |
| 2. ESUN | 乙太網路的機架內擴充 | 交換、封包格式、無損、連結可靠性與多跳網路要求 | 1.0 規格已發布，證明乙太網路也直接進入機架內 | 不能說具名端點與交換器已符合規格或跨廠互通 |
| 3. SUE-T | 乙太網路的機架內端點與傳輸 | 加速器端點、記憶體使用方式、封包與傳輸，與 ESUN 網路側分工 | OCP 現行工作流已把它列為獨立方向 | 不能說正式規格、實體產品、符合規格與互通已成熟 |
| 4. UEC | 人工智慧與高效能運算的跨機架乙太網路 | 網路介面卡、交換器、光模組與線材等跨機架生態系 | 現行公開版本為 1.0.3 | 不能說這些元件已完成跨廠互通或具名客戶部署 |
| 5. UALoE | 在乙太網路傳輸上承載機架內協定 | 讓 UALink 協定使用乙太網路傳輸路徑，可出現在具名系統設計 | AMD／Oracle 公告中有具名前瞻路徑 | 不能說它與 UEC 是同一標準，也不能說客戶已完成部署 |

這五條路徑有競爭、共存與承載關係，不是五個可直接相加的市場。本篇的修正重點是：不能再用
「一條規格只管機架內，乙太網路只管機架外」的簡單二分法閱讀。

## 把六類角色放回同一條資料路徑

| 本文六類角色 | 它交付什麼 | 本輪具名例子 | 已證實到哪裡 | 不能外推 |
|---|---|---|---|---|
| 1. 規格與開放工作組 | 定義端點、傳輸、交換、測試與版本要求 | UALink Consortium、Ultra Ethernet Consortium、Open Compute Project | UALink 2.0、UEC 1.0.3 與 ESUN 1.0 有公開文件；SUE-T 有獨立工作流 | 參與組織或規格發布不等於產品已符合規格與互通 |
| 2. 加速器、端點與晶片智財 | 實作記憶體、傳輸、實體層與控制功能 | AMD Helios 端點路徑、Broadcom SUE 架構、Marvell custom UALink 方案 | 公開產品與架構說明證明開發路徑存在 | 公司自述可互通不等於第三方跨廠測試、客戶採用或收入 |
| 3. 交換器專用晶片與平台 | 實作封包轉送、緩衝、壅塞與網路管理 | Arista 7060XE7 以及 Broadcom 對機架內乙太網路的架構說明 | 7060XE7 被定位為同時服務機架內外的具名平台 | 產品用途不等於已對應 ESUN／SUE-T、已出貨或已部署 |
| 4. 機架與系統整合 | 把運算、機架內外網路、軟體、電源與散熱整合成可驗收系統 | AMD Helios 參考設計 | 公開架構同時列出 UALink／UALoE 機架內與 UEC-ready 跨機架路徑 | 參考設計不等於整機廠已量產、客戶已驗收或所有組件已互通 |
| 5. 雲端客戶與實際部署 | 驗收系統，開放服務，並提供部署規模、利用率與故障結果 | Oracle／AMD 的 MI450／Helios 規畫 | 公告證實前瞻季度與 UALoE 架構規畫 | 截至本輪不能說已出貨、預覽、正式開放、部署或產生收入 |
| 6. 台灣供應鏈查證 | 用客戶與公司雙向文件，對上具名產品、資格、出貨與財務結果 | 伺服器組裝／機構、矽智財、PCB／CCL 只是本輪搜尋路由 | 尚未有 universe 公司完成具名互連與財務雙向核對 | 會員、合作標誌、一般高速能力與人工智慧伺服器出貨不等於此題收入 |

六類角色用來分責，不是完整供應商名單。一手文件能證明某家公司在某一位置有規格、架構或產品，
但不會自動替另一位置補上第三方測試，也不會替台灣公司產生訂單與財務結果。

## 最後用六關判斷「能連」到「真正互通」

| 本文六關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 共同規則可查核 | 規格版本、功能、角色、錯誤行為與測試入口有公開文件 | UALink 2.0、UEC 1.0.3、ESUN 1.0 可查；SUE-T 是獨立工作流 | SUE-T 正式規格，以及四條路徑的合規與互通測試計畫 | 規格發布不等於實體晶片存在或產品已通過測試 |
| 2. 路徑各位置有具名實物 | 至少能指出端點、連接傳輸、交換器與所需軟體的產品、版本和功能 | Helios、Marvell UALink 方案與 Arista 7060XE7 證明多個位置有具名開發路徑 | 對應同一規格版本的端點、交換器、韌體、驅動與測試配置 | 不同新聞中有多個產品，不等於它們已在同一路徑上工作 |
| 3. 單件產品符合指定規格 | 每件產品依共同方法通過實體層、協定、功能、計時與錯誤測項 | UALink 文件表示計畫將後續導入；本輪未找到 ESUN／SUE-T 具名產品通過報告 | 產品名、版本、測試器、測項、通過條件與可查核結果 | 一件產品合格不等於它能和所有其他廠商產品工作 |
| 4. 不同廠商完成交叉互通 | 至少兩家獨立端點與交換實作，在共同版本與軟體下交叉測試正常與異常情境 | 現有文件沒有讓 ESUN／SUE-T 或 UALink 路徑通過此關的可核對結果 | 參與廠商、組合矩陣、版本、拓撲、測項、錯誤注入、軟體與重現方法 | 單廠端到端展示、會員名單或產品互連宣稱不等於通過 |
| 5. 整個系統與工作可重現 | 在有壓力、擴容、故障與長時間運轉下，實際工作仍會正確完成 | Helios 是參考設計；Oracle／AMD 是前瞻規畫，都不是公開工作負載驗收結果 | 端點與機架數、軟硬體版本、工作負載、期間、故障、恢復與通過門檻 | 參考設計、預覽或單次最高數字不等於可交付系統 |
| 6. 客戶部署與公司財務對上 | 具名客戶完成驗收與部署，供應商用同一產品、期間與分母提供出貨和財務結果 | Oracle 仍是規劃；台灣三個族群仍只是待驗證搜尋路由 | 出貨、預覽、正式開放、部署數、利用率，以及客戶與供應商雙向財務文件 | 規格、會員、產品用途或客戶規劃不等於台灣公司已獲利 |

本輪可確認第一關有多份規格與工作文件，第二關有分散的具名產品路徑；第三關沒有本輪可核對的完整結果，
第四關沒有跨廠矩陣，第五關仍停在參考設計與前瞻規畫，第六關也尚未通過。六關是閱讀與證據排序，
不是網路效能分數、標準勝負、供應商名單、市場份額或投資排名。

## 這篇對公司判斷的用處與界線

伺服器組裝與機構研究可追機架、交換器、線材、軟體與整機驗收；矽智財可追控制器、實體層電路、訊號重整、
交換與晶粒介面；PCB／CCL 可追板級訊號、連接器與材料資格。這些都只是「下一份證據要去哪裡找」，
不是「這些公司已經受惠」。

要升級任何台灣公司，必須讓平台或客戶文件與公司文件雙向對上同一具名產品、規格版本、資格驗證、出貨、期間與財務
分母。本輪沒有這組證據，因此不支持個股排序、訂單推估、收入預測或投資動作。

## 來源與證據邊界

- [UALink 2.0 release](https://ualinkconsortium.org/wp-content/uploads/2026/04/UALink-2.0-Specification-PR_FINAL.pdf)（scale-up、chiplet、UCIe 3.0 與未來 compliance）。
- [UEC Specification 1.0 launch](https://ultraethernet.org/ultra-ethernet-consortium-uec-launches-specification-1-0-transforming-ethernet-for-ai-and-hpc-at-scale/)（scale-out 與元件範圍）。
- [AMD Helios product page](https://www.amd.com/en/products/rackscale-solutions/helios.html)（scale-up／scale-out 架構與 reference design 邊界）。
- [Oracle and AMD deployment plan](https://newsroom.amd.com/news/oracle-and-amd-expand-partnership-to-help-customers-achieve-next-gen-ai-scale/)（Q3 2026 前瞻規劃）。
- [Marvell custom UALink solution](https://www.marvell.com/company/newsroom/marvell-expands-custom-compute-platform-with-ualink.html)（IP／產品開發路徑）。
- [OCP ESUN 1.0 release](https://www.opencompute.org/blog/the-ocp-esun-10-specification-has-been-released)（Ethernet scale-up 的 network requirements 與規格階段）。
- [Arista 7060XE7](https://investors.arista.com/Communications/Press-Releases-and-Events/Press-Release-Detail/2026/Arista-Introduces-Next-Generation-1-6Terabit-Portfolio-for-AI-Fabrics/default.aspx)（具名 scale-up／scale-out 平台，不代表 ESUN compliance）。
- [Broadcom SUE framework](https://www.broadcom.com/blog/scale-up-is-simple-ethernet-makes-it-smarter)（endpoint／memory model／transport 起點）。
- [OCP ESUN workstream](https://www.opencompute.org/wiki/Networking/ESUN)（ESUN 與 SUE-T 分工及後續文件入口）。

本篇不使用會員數、宣稱頻寬、GPU 數或公司效能數字做跨公司比較，也不推估 TAM、市占、估值或
市場預期。ESUN 1.0 發布與 7060XE7 支援 scale-up 是兩個不同事件，尚不能合併成「Arista 已部署
ESUN」。Oracle 規劃已進入原訂季度，也不代表部署已發生；沒有新一手文件時仍停在 planned。

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

- UALink／ESUN／SUE-T／UEC 各自公布 compliance program、plugfest 與可重現的 multi-vendor interoperability 結果。
- ESUN network side 與 SUE-T endpoint／transport 由至少兩家獨立 silicon 實作互通，而不是只有同一公司端到端展示。
- Merchant silicon、switch、NIC、retimer 或 chiplet 從 IP／樣品升級為 production，並能對應正式標準與具名客戶。
- Arista 或客戶確認 7060XE7 實際出貨、部署層級與 scale-up／scale-out 分母。
- Oracle 或 AMD 確認 MI450／Helios shipment、preview 或 GA，而不是沿用 2025 年的前瞻規劃。
- 台灣公司用具名產品、qualification、出貨與財務資料完成雙向核對；否則只保留產業節點，不畫公司受惠線。
