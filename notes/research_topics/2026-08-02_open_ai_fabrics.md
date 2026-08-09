# 開放 AI 互連不是兩分法：UALink 與 Ethernet 都進入 scale-up

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

- **機架內擴充（scale-up）**：讓同一個運算群組或機架內的多顆加速器共同交換資料，重點是低延遲，以及彼此如何讀寫記憶體。
- **跨機架擴充（scale-out）**：把多個機架或節點連成更大的叢集，重點是乙太網路、壅塞控制、路由與大規模可靠性。
- **UALink（加速器互連）**：主要服務機架內多顆加速器的開放互連規格。
- **UEC（超乙太網路聯盟）**：主要改善 AI／高效能運算跨機架乙太網路的規格與生態系。
- **ESUN（乙太網路機架內擴充）**：OCP 的開放規格，處理機架內交換、封包格式、無損傳輸與可靠性。
- **SUE-T（機架內乙太傳輸）**：偏向定義加速器端點、記憶體使用方式與傳輸；它和 ESUN 分工，但都屬乙太網路的機架內路徑。
- **UALoE（用乙太網路承載 UALink）**：把 UALink 協定放在乙太網路傳輸路徑上；不表示 UALink 與 UEC 已變成同一個標準。
- **符合規格／跨廠互通（compliance／interoperability）**：前者確認產品遵守規格，後者確認不同廠商產品能互相工作；規格發布時兩件事不會自動完成。
- **Helios**：AMD 的機架級 AI 系統平台名稱。本文只把它當作 scale-up 互連路徑的其中一個實例，不評價該平台本身的進度。
- **MI450**：AMD 對加速器產品世代使用的名稱；本文只用它定位 Oracle／AMD 公開的部署規畫，不把產品名稱當成已部署證據。
- **Specification（規格文件）**：描述共同語言與最低要求的文件；發布只代表規則存在，不代表晶片、跨廠測試或客戶部署已完成。
- **GA（General Availability）**：雲端服務正式對外開放、任何符合資格的客戶都能購買使用的階段。**合作公告、預覽與 GA 是三個不同節點**，只有 GA 才最接近可認列的收入；本文一再強調的正是不要把前兩者讀成後者。
- **NIC（網路介面卡）**：伺服器上負責連接網路的介面卡。在 scale-out 網路裡，NIC、交換器、光模組與線材必須整套互通，任何一段沒到位，整條路徑就不算完成。
- **Switch ASIC（交換器專用晶片）**：交換器內負責轉送資料的核心晶片；有晶片產品不等於整台交換器已完成跨廠互通或客戶部署。
- **PHY（實體層電路）**：把晶片內的數位資料轉成線材或光模組能傳送的訊號；它只是互連路徑的一層。

### 三句話抓重點

- 原先只用「UALink 做 scale-up、UEC 做 scale-out」的兩層說法不夠完整，因為 OCP ESUN／SUE-T 也把 Ethernet 直接帶入 scale-up。
- AMD Helios 提供 UALink／UALoE 路徑，Arista 7060XE7 又同時定位 scale-up 與 scale-out，顯示開放互連是多條規格、endpoint 與 switch 路徑的組合。
- 截至 2026-08-02，ESUN／SUE-T 的 multi-vendor compliance、具名產品對應與部署分母仍未完成；規格、產品用途與真正互通不能合併。

### 為什麼重要

AI 系統搬資料的範圍已跨過單一 GPU。機架內要讓多顆加速器快速交換資料，機架間則要處理
乙太網路的壅塞、路由與可靠性。現在連乙太網路也開始進入機架內，因此不能再把
「乙太網路」直接等同於跨機架擴充。

可把整個產業想成一套路網：規格像交通規則，端點像車輛的出入口，交換器像路口，跨廠
互通測試像實際試車，客戶部署才是正式通車。前一層完成，只能讓下一層開始，不能替下一層
宣布完成。

閱讀一則互連新聞時，先分開四個問題：資料是在機架內還是機架間移動？新聞談的是端點、
交換器、網路介面卡還是實體層電路？目前只到規格、晶片、跨廠互通、系統整合，還是已部署？
最後，證據能支持哪一層？這樣才不會漏掉替代路徑、重複計算同一平台，或把標準會員與產品
規畫提前當成交換器、光模組、系統組裝廠的收入。

### 接下來怎麼追

- 先分別看 UALink、ESUN、SUE-T、UEC 是否公布 compliance、plugfest 或 multi-vendor interoperability，而不只看版本號。
- 再把加速器端點、交換器專用晶片、網路介面卡、訊號重整晶片、實體層電路與完整系統分開，找具名晶片、樣品、量產與客戶。
- 對 Arista 7060XE7，要確認產品是否對應 ESUN／SUE-T、是否出貨，以及具名客戶用在 scale-up 還是 scale-out。
- 對 Oracle／AMD，依序追 shipment、preview、GA、部署數與利用率；任何一步都不能跳過。

### 想一想

- ESUN 有很多參與者，和兩家不同廠商的加速器端點、交換器專用晶片真的能互通，兩者中間還缺哪些測試與軟體證據？
- UALink 與 ESUN 都瞄準 scale-up 時，它們是競爭、互補，還是會依 accelerator／rack 架構並存？
- 若同一台交換器能同時服務 scale-up 與 scale-out，研究者要如何避免把一份收入或埠數計算兩次？

## 用五道關卡讀一則互連新聞

互連新聞常把「規格發布、產品支援、互通成功、系統採用、客戶部署」寫在相鄰段落，讀起來
像同一件事已經一路完成。實際上，每個動詞只回答一個階段。讀者可以依序走過下面五道關卡，
把一則新聞放回正確位置。

### 第一關：資料要跨多遠

先問資料是在同一顆晶片內、同一機架內，還是跨多個機架移動。這一步決定要看機架內擴充、
跨機架擴充，或兩者交界；也能避免只因都使用乙太網路，就把不同距離、延遲與可靠性要求
合成同一市場。

### 第二關：誰和誰在說話

再找出路徑兩端：加速器端點、交換器、網路介面卡、訊號重整晶片、實體層電路或完整系統。
新聞若只具名其中一端，另一端的相容產品仍是未知；一顆交換器專用晶片存在，也不等於
伺服器、線材、光模組與軟體已全部到位。

### 第三關：目前只有規則，還是已有實物

規格文件回答「大家打算遵守什麼共同語言」。具名晶片或產品公告才回答「誰做出了什麼」。
兩者不能互換：規格可以先於晶片多年，產品也可能只支援其中部分功能。看到「支援」時，
還要找產品型號、版本、使用位置與公開文件，不能只看會員名單或合作標誌。

### 第四關：同廠能跑，不等於跨廠能跑

單一公司的示範系統可能全部由同一套軟硬體組成；跨廠互通則要讓不同公司的端點與交換器，
在共同規格、測試方法與錯誤處理下工作。讀到展示、實驗室測試或互通活動時，要確認參與者、
測試範圍、通過條件與版本，才知道它跨過哪一道門。

### 第五關：部署之後才問收入

客戶規畫、預覽、正式開放、實際部署與利用率仍是不同節點。只有公開文件能把具名產品、
客戶驗收、出貨或服務開放對上，才開始討論供應商訂單與財務貢獻。若只知道 MI450／Helios
的前瞻規畫，正確結論就是「已有下一個檢查點」，而不是「部署已發生」。

把五關串起來後，同一則新聞只會停在它真正支持的位置。後續若出現新規格、晶片、跨廠測試
或客戶文件，就逐關往前移；不需要用模糊的「生態系成熟」一次把所有階段升級。

## 三張表要分開

| 層級 | 已證實 | 未證實 |
|---|---|---|
| 規格 | UALink 2.0 已 ratify；UEC 現行版本為 1.0.3；ESUN 1.0 已發布；SUE-T 有獨立 workstream | 各路徑的多廠 compliance、互通與共同效能口徑 |
| 產品／系統 | AMD Helios 描述 UALink／UALoE 與 UEC-ready；Marvell 有 UALink offering；Arista 7060XE7 定位 scale-up／scale-out | 產品對應 ESUN／SUE-T 的正式證據、OEM 量產、客戶驗收與供應商份額 |
| 部署 | Oracle／AMD 公告 Q3 2026 起的 MI450／Helios 規劃 | 截至本輪的 shipment、preview、GA、實際部署與利用率 |

這種拆法會讓同一件新聞只進一個格子：規格升版不會自動把產品與部署兩格一起升級；產品被
reference design 列名，也不會自動產生財務貢獻。

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
