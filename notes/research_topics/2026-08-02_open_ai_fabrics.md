# 資料從一顆運算晶片走到另一顆：先分清六張網，再判斷跨廠互通

<!-- research_topic
topic_id: MI-2026-08-02-OPEN-AI-FABRICS
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-04-07
last_reviewed_at: 2026-08-12
review_due: 2026-08-17
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
thesis_claim_id: C18
base_confidence: medium
confidence_basis: UALink 與 UEC 規格、OCP 現行計畫與參考架構可交叉確認網路工作和平臺契約必須分成兩條軸；UEC 已公開自我聲明與部分層級測試框架，但仍沒有具名產品通過、多供應商互通、系統壓力結果、客戶部署或台灣財務曝險
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
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: corrected_single_fabric_path_frame_with_network_plane_and_stack_contract
evidence: sources:S15,S16,S17,S18,S19,S20
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_collective_algorithm_bus_bandwidth_and_training_outcome_performance_passport_without_thesis_or_clock_refresh
evidence: sources:S17,S19,S21,S22,S23,S24
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

<!-- research_source
source_id: S15
role: standard
source_kind: living_index
publisher: Open Compute Project
title: Open Cluster Designs for AI
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/index.php/community/cluster-designs-for-ai
locator: 2026-08-12 查得 Scope and Contribution Overview；明列 scale-up、scale-out、front-end、storage、management networking，以及實體／邏輯拓撲、佈線、電力與散熱
limitation: 現行計畫範圍與可供採購部署參考的文件入口，不證明特定產品符合規格、具名客戶部署、效能或財務結果
independence_group: open-compute-project
-->

<!-- research_source
source_id: S16
role: standard
source_kind: document
publisher: Open Compute Project
title: OCP Educational Webinar — New OCP Reference Architectures for AI Networking
published_at: 2026-06-02
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/events/past-events/ocp-educational-webinar-new-ocp-reference-architectures-for-ai-networking
locator: 活動日期與 Overview；明列 front-end ingress／egress、storage、backend scale-out、in-band management、control／data plane、生命週期自動化、configuration drift 與 BOM
limitation: Webinar 與參考架構摘要提到 production examples，但沒有提供可獨立核對的完整客戶、組態、測試矩陣、失敗、利用率或財務結果
independence_group: open-compute-project
-->

<!-- research_source
source_id: S17
role: standard
source_kind: living_index
publisher: Ultra Ethernet Consortium
title: UEC Working Groups
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://ultraethernet.org/working-groups/
locator: 2026-08-12 查得 Physical、Link、Transport、Software、Storage、Compliance、Management、Performance and Debug 八個工作組及各自範圍
limitation: 工作組範圍表示規格與工具由哪些層負責，不等於所有輸出已核定、產品已通過、跨廠互通或客戶部署
independence_group: ultra-ethernet-consortium
-->

<!-- research_source
source_id: S18
role: standard
source_kind: living_index
publisher: Ultra Ethernet Consortium
title: UEC Compliance
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://ultraethernet.org/compliance/
locator: 2026-08-12 查得合規說明檔、測試床建議、Transport 與 PHY／LL checklist；說明檔明定前三類文件供 implementors 進行 compliance self-attestation，另頁會員聲明實為必要專利權利登錄
limitation: 自我聲明工具與清單入口不是具名產品聲明／通過結果、第三方認證、多供應商互通矩陣、系統部署或效能；必要專利權利聲明更不是產品合規聲明
independence_group: ultra-ethernet-consortium
-->

<!-- research_source
source_id: S19
role: standard
source_kind: document
publisher: Ultra Ethernet Consortium
title: UEC Compliance Test Test Bed Recommendations
published_at: 2025-06-10
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://ultraethernet.org/wp-content/uploads/sites/20/2025/06/UEC-Compliance-Test-Test-Bed-Recommendations.pdf
locator: page 3 Scope；涵蓋 Link／PHY 與部分 Transport 的 compliance test bed 建議，並明列 interoperation、system stress／scale 與 performance testing 不在本文範圍
limitation: 測試床建議只涵蓋部分層級且明確排除互通、系統壓力／規模與效能；不提供任何具名產品通過清單
independence_group: ultra-ethernet-consortium
-->

<!-- research_source
source_id: S20
role: standard
source_kind: document
publisher: Open Compute Project
title: Open Pod Group for M xPUs System Architecture
published_at: 2026-01-14
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/documents/opg-m-system-architecture-final-14-january-2026-pdf
locator: pages 7–10 Network Overview；叢集視角列出 scale-up、scale-out、SO-C、storage、in-band 與 out-of-band management 六張網，OPG-M 參考設計採非匯聚實體資源且五張外部網不要求冗餘
limitation: 這是一套 air-cooled 400G 參考架構並帶有不要求冗餘等明示假設；不能外推為所有叢集的唯一拓撲、認證、客戶部署或公司收入
independence_group: open-compute-project
-->

<!-- research_source
source_id: S21
role: other_primary
source_kind: living_index
publisher: NVIDIA
title: Performance reported by NCCL tests
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://github.com/NVIDIA/nccl-tests/blob/master/doc/PERFORMANCE.md
locator: 2026-08-14 查得 Time、Algorithm bandwidth、Bus bandwidth 與 Summary；定義 algbw=S／t，AllReduce busbw=algbw×2(n−1)／n，ReduceScatter／AllGather／AlltoAll 係數為 (n−1)／n，Broadcast／Reduce 為 1，並明示 AllReduce 推導以 point-to-point send／receive 為條件
limitation: NCCL tests 的 busbw 是 collective-specific 正規化數，不是實測 wire counter、唯一 payload goodput 或端到端訓練結果；點對點推導不能無條件外推到硬體 offload、階層式演算法、不同拓撲、協定、故障或產品 qualification
independence_group: nvidia-nccl
-->

<!-- research_source
source_id: S22
role: other_primary
source_kind: living_index
publisher: NVIDIA
title: NCCL Tests
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://github.com/NVIDIA/nccl-tests
locator: 2026-08-14 查得 Usage 與 Arguments；總 rank=process×thread×GPU、message-size sweep、warm-up／iteration／cycle、rank Avg／Min／Max、per-iteration p99／max、raw JSON、correctness check、blocking mode、parallel group 與每 group bandwidth 邊界
limitation: 測試參數與輸出欄位只建立 microbenchmark 重現契約，不提供本篇任何具名產品結果、production traffic、跨廠互通、長時間故障、訓練品質、成本或台灣公司財務
independence_group: nvidia-nccl
-->

<!-- research_source
source_id: S23
role: other_primary
source_kind: living_index
publisher: NVIDIA
title: NCCL Collective Operations
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html
locator: 2026-08-14 查得 NCCL 2.31.2；collective 必須由每個 rank 以相同 count／datatype 呼叫，並逐一定義 AllReduce、Broadcast、Reduce、AllGather、ReduceScatter、AlltoAll、Gather 與 Scatter 的資料結果
limitation: API 語意頁定義工作與正確呼叫，不提供 line rate、拓撲、演算法選擇、效能分布、硬體配置、跨廠互通、production deployment 或公司採用
independence_group: nvidia-nccl
-->

<!-- research_source
source_id: S24
role: standard
source_kind: living_index
publisher: MLCommons Association
title: MLPerf Training Rules
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://github.com/mlcommons/training_policies/blob/master/training_rules.adoc
locator: 2026-08-14 查得 Definitions、General rules、Run Results 與 Benchmark Results；system 包含硬體／interconnect 與軟體版本，run result 是連續 wall-clock 到品質目標，現行表依 workload 要求至少 3 或 10 runs，benchmark result 去掉最快與最慢後平均其餘時間
limitation: MLPerf Training 是整套系統到品質目標的 benchmark contract，不是獨立網路或 NCCL 測試，也不能隔離 NIC／switch／optics 因果、代表 production workload、跨廠 qualification、價格或台灣公司財務
independence_group: mlcommons-training
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
status: superseded
claim: 開放 AI 互連不能再只用「UALink 管 scale-up、UEC 管 scale-out」理解；UALink 是 accelerator scale-up 路徑，OCP ESUN／SUE-T 與具名 Ethernet 平台也直接進入 scale-up，而 UEC 仍聚焦 scale-out ecosystem，研究上必須把每條路徑的規格、endpoint／switch、silicon、互通、系統與部署分開
supporting_source_ids: S1,S2,S3,S9,S10,S11,S12
contrary_source_ids:
as_of: 2026-08-02
basis: correction_of:C5；S9／S10 直接定義 Ethernet scale-up，S11 提供同時服務 scale-up／scale-out 的具名平台，S12 與 OCP 分工顯示 endpoint transport 也有獨立路徑，縮窄原先二層對應
boundary: 不推估 UALink、ESUN、SUE-T 或 UEC 的效能勝負、市占、TAM、部署分母、台灣供應鏈份額或市場定價
verification_needed:
correction_kind: supersedes
corrects_claim_id: C5
corrected_by_claim_id: C18
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

<!-- research_claim
claim_id: C14
label: verified
status: active
claim: OCP 現行 Open Cluster Designs for AI 計畫把 scale-up、scale-out、front-end、storage 與 management networking 分成不同工作範圍，並同時納入實體／邏輯拓撲、佈線、電力與散熱
supporting_source_ids: S15
contrary_source_ids:
as_of: 2026-08-12
basis: S15 的現行 Scope and Contribution Overview 逐項列出五種網路工作與叢集基礎設施設計範圍
boundary: 計畫範圍不表示每個叢集都用同一拓撲，也不證明具名產品、客戶部署、效能或公司財務
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C15
label: verified
status: active
claim: OCP 的 OPG-M 參考架構在叢集視角區分 scale-up、scale-out、SO-C／服務、storage、in-band management 與 out-of-band management 六張網；其中五張外部網採分離實體資源，且該設計明示不假設或要求冗餘
supporting_source_ids: S20
contrary_source_ids:
as_of: 2026-01-14
basis: S20 pages 7–10 的 Network Overview、non-converged solution、five separate networks 與 redundancy assumption
boundary: 這是 air-cooled 400G OPG-M 的一套參考設計，不是所有人工智慧叢集的唯一或最佳架構，也不是客戶生產部署證明
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C16
label: verified
status: active
claim: UALink 2.0 文件把 Common、Data Link／Physical、Manageability 與 Chiplet 分成不同規格，UEC 現行工作組則分開 Physical、Link、Transport、Software、Storage、Compliance、Management、Performance and Debug，顯示「同一互連名稱」仍包含多層契約
supporting_source_ids: S1,S17
contrary_source_ids:
as_of: 2026-08-12
basis: S1 的 UALink 2.0 規格套件清單與 S17 現行八個工作組及其範圍可逐項核對
boundary: 規格或組織分層不表示所有層都已完成核定實作、產品通過、多供應商互通或部署
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C17
label: verified
status: active
claim: UEC 已公開供實作者進行 compliance self-attestation 的說明檔、測試床建議及 Transport、PHY／Link checklist，但測試床文件明確把 interoperation、system stress／scale 與 performance testing 排除在範圍外；同頁會員聲明是必要專利權利登錄，不是產品合規聲明
supporting_source_ids: S18,S19
contrary_source_ids:
as_of: 2026-08-12
basis: S18 所連說明檔明定文件用於 compliance self-attestation，會員聲明頁則明定必要專利權利登錄；S19 page 3 直接界定已涵蓋層級與三類 out-of-scope 測試
boundary: 合規框架與自我聲明工具不等於具名產品已提交或通過、第三方認證、多供應商互通、系統壓力、效能或客戶部署；必要專利權利登錄不得混入產品成熟度
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C18
label: inference
status: active
claim: 開放人工智慧網路研究必須同時固定兩條軸：先問資料正在服務 scale-up、scale-out、服務／CPU、storage、in-band 或 out-of-band management 哪一張網，再問實體／連結、端點／傳輸、交換／壅塞、軟體／控制、管理／遙測、單件合規、多供應商互通、系統壓力與客戶部署走到哪一層；共同使用 Ethernet 不會自動合併網路工作，也不會替尚未驗收的層級補證據
supporting_source_ids: S1,S2,S9,S13,S15,S16,S17,S18,S19,S20
contrary_source_ids:
as_of: 2026-08-12
basis: correction_of:C9；S15／S20 把叢集拆成不同網路工作，S1／S9／S13／S17 把規格與管理責任拆成不同層，S18／S19 又證明合規、自我聲明、互通、系統與效能不是同一驗收節點，因此原先只按標準與機架內外分路徑仍過度簡化
boundary: 兩軸框架不推估規格勝負、共同實體設備的實際匯聚比例、TAM、市占、效能、部署分母、台灣供應鏈份額、估值或市場定價
verification_needed:
correction_kind: supersedes
corrects_claim_id: C9
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C19
label: unverified
status: active
claim: 任何具名產品或客戶系統已同時完成相關 UEC 自我聲明、多供應商互通、系統壓力／規模／效能測試，並能在所需網路平面上對上具名部署與供應商財務結果
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: S18／S19 只證明合規工具與部分測試床框架；S15／S16／S20 只證明參考架構、範圍與設計假設，沒有本主張要求的完整產品矩陣、系統結果、客戶與財務文件
boundary: 不以必要專利權利聲明、會員名單、reference architecture、產品支援 Ethernet 或單廠展示替代產品自我聲明、跨廠、系統、部署與財務證據
verification_needed: 公開具名產品與版本、聲明／測試結果、多供應商組合矩陣、拓撲與錯誤注入、系統壓力／規模／效能、客戶站點與供應商出貨財務的同口徑文件
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C20
label: verified
status: active
claim: NCCL 現行 collective 語意要求每個 rank 以相同 count 與 datatype 共同呼叫，並把 AllReduce、ReduceScatter、AllGather 與 AlltoAll 定義成不同資料結果；因此 collective 名稱、rank 數、message count／datatype 與 rank-to-device mapping 都是效能數字不可省略的工作身分
supporting_source_ids: S23
contrary_source_ids:
as_of: 2026-08-14
basis: S23 的 Collective Operations 開頭與 AllReduce／ReduceScatter／AllGather／AlltoAll 各節直接列出呼叫約束、輸入、輸出及 rank mapping 責任
boundary: API 語意只證明工作定義，不提供拓撲、演算法、line rate、效能、正確率、跨廠互通、production deployment 或公司財務
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C21
label: verified
status: active
claim: NVIDIA nccl-tests 把 algorithm bandwidth 定義為 message size S／operation time t，另用 collective-specific 係數計算 bus bandwidth；在 point-to-point send／receive 推導下，AllReduce 係數是 2(n−1)／n，ReduceScatter／AllGather／AlltoAll 是 (n−1)／n，而測試工具另提供總 rank、message-size sweep、warm-up、iterations、rank Avg／Min／Max、per-iteration tail 與 correctness 的設定或輸出欄位
supporting_source_ids: S21,S22
contrary_source_ids:
as_of: 2026-08-14
basis: S21 的 Algorithm bandwidth、Bus bandwidth、各 collective 推導與 Summary 直接提供公式及 point-to-point 條件；S22 的 Usage／Arguments 直接列 rank 組成、size、warm-up、iteration、cycle、rank aggregation、p99／max、raw JSON 與 correctness 參數
boundary: busbw 是衍生正規化而非 wire counter；工具可保存欄位不等於任何具名測試已正確執行，也不能把點對點公式無條件套到硬體 offload、階層式演算法、不同平行 group 或端到端訓練
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C22
label: inference
status: active
claim: 在 N=1 個純教材 collective、n=8 ranks、每 rank message S=1,000,000,000 bytes、operation time t=0.020 seconds，且使用 NCCL tests 的 point-to-point AllReduce 正規化時，algbw=50 GB／s、係數 1.75、busbw=87.5 GB／s；兩個頻寬來自同一個時間與 payload，不能相加，也不能把 87.5 GB／s 改寫成應用每秒完成 87.5 GB 唯一資料
supporting_source_ids: S21
contrary_source_ids:
as_of: 2026-08-14
basis: 依 S21 的 algbw=S／t 與 AllReduce busbw=algbw×2(n−1)／n，以 Python Fraction 及獨立 awk 路徑重算，兩路均得 factor=7／4、algbw=50、busbw=175／2 GB／s
boundary: 這是 N=1 個假想設定的確定性公式展開，沒有設備、port、topology、algorithm selection、run 或抽樣，故沒有 sampling SE／t；未含協定 overhead、retries、congestion、overlap、correctness、tail、功耗、成本或 training outcome
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C23
label: inference
status: active
claim: 要宣稱開放人工智慧網路改善訓練，至少要把網路平面／量測範圍、collective 與資料語意、rank／placement、message／datatype、拓撲／link／方向、軟硬體與演算法版本、同時流量與運算重疊、時間／algbw／busbw 定義與正確性、重複 run／完整分布／失敗，以及 wall-clock-to-quality／資源／財務綁成同一份十欄效能護照
supporting_source_ids: S17,S19,S21,S22,S23,S24
contrary_source_ids:
as_of: 2026-08-14
basis: S17／S19 把 performance 從部分 compliance test bed 分離；S21–S23 顯示 collective、rank、message、時間、正確性、algbw 與 busbw 口徑不同；S24 又要求固定完整 system／software，以連續 wall-clock 跑到品質目標並用多次 run 形成 benchmark result，共同支持 microbenchmark 與訓練結果必須以共同版本鍵橋接
boundary: 十欄護照是研究中心整合 UEC／NCCL／MLCommons 的檢查框架，不是三方共同標準；欄位齊全仍不隔離單一 NIC／switch／optic 因果、不等於 multi-vendor interoperability、production qualification、部署或台灣公司收入
verification_needed: 同一具名 AI workload 固定模型、資料、品質門檻與系統版本，同時公開 collective event 分布、網路 counter、故障／重試、overlap、run-level wall-clock-to-quality、資源成本與具名設備配置
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
status: retired
retired_at: 2026-08-12
retirement_reason: 同日第一筆到期複核漏看 UEC 公開 Compliance 頁；追加更正確認 S18／S19 只前進到自我聲明與部分測試框架，且 C9 已由 C18 的網路平面 × 驗收契約兩軸框架取代，改由 T4／T5 分開續追
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

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C1,C2,C10,C12,C13,C16,C17,C19
metric: UALink、ESUN／SUE-T 與 UEC 各層規格、單件自我聲明／合規、具名產品、多供應商互通、系統壓力／規模與效能結果
source_ids: S1,S2,S9,S10,S12,S13,S17,S18,S19
watch_source_ids: S6,S7,S13,S17,S18
frequency: weekly
frequency_detail: 每週保存規格、工作組與 compliance 頁差異；把 checklist／declaration、產品 pass、跨廠矩陣、系統壓力與部署分列，不再用「有合規頁」替代後續關卡
next_check: 2026-08-19
trigger: 出現具名產品自我聲明或測試結果、至少兩家 endpoint／switch 的版本化互通矩陣、plugfest 結果，或可重現的系統壓力／規模／效能報告
invalidation: 合規工具長期沒有具名產品結果、產品只通過部分層級、跨廠或系統壓力失敗，則開放標準可部署成熟度下修
-->

<!-- monitoring_item
monitor_id: T5
status: active
claim_ids: C14,C15,C18,C19
metric: 人工智慧叢集六張網的實體／邏輯分工、是否匯聚、冗餘、BOM／組態、生命週期管理、系統驗收與具名客戶部署
source_ids: S15,S16,S20
watch_source_ids: S15
frequency: monthly
frequency_detail: 每月檢查 OCP Open Cluster Designs for AI 新貢獻；只有具名設計固定網路平面、組態、冗餘與驗收結果才升級，不把參考架構摘要當成 production validation
next_check: 2026-09-12
trigger: OCP、平台商或客戶公開具名叢集的六張網映射、交換器／NIC／軟體版本、BOM、冗餘、測試矩陣、站點與運轉結果
invalidation: 實際部署廣泛把平面匯聚、採不同責任邊界或參考架構假設無法通過可靠度／營運驗收，則六張實體網的可泛化程度下修但仍保留邏輯工作分層
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **資料路徑**：資料從一個運算端點出發，經過連接、傳輸、交換與軟體控制，最後到達另一個端點的完整接力。
- **加速器**：專門加快人工智慧或高效能運算的晶片；有加速器不等於它已能和其他廠商晶片共同工作。
- **端點（endpoint）**：資料路徑的出發點或目的地，例如加速器、網路介面卡或它們的控制電路。
- **機架**：安裝多台運算、網路、電源與散熱設備的櫃體；「同一機架」不代表所有設備都在同一塊電路板上。
- **機架內擴充（scale-up）**：讓同一運算群組或機架內的多顆加速器高速交換資料，重點是低延遲與彼此如何使用記憶體。
- **跨機架擴充（scale-out）**：把多個機架或節點連成更大叢集，重點是路由、壅塞、大規模可靠性與故障恢復。
- **網路平面**：依工作目的分開的一組連線、規則與營運責任；兩個平面可以共用同類設備，卻不一定共用設定與驗收。
- **前端／服務網路（SO-C）**：讓處理器、服務入口與運算節點交換一般服務資料；它和加速器彼此同步的網路不是同一工作。
- **儲存網路**：把運算節點連到共享資料與持久儲存；重點包括資料吞吐、完整性、恢復與存取隔離。
- **帶內管理**：沿著系統正常使用的網路路徑發現、設定或觀察設備；主資料路徑故障時，它也可能受影響。
- **帶外管理**：使用獨立管理路徑處理開機、重置、維修與故障救援，使主網路失效時仍能接觸設備。
- **資料平面**：真正搬運工作資料的部分；它回答資料怎麼走，不負責決定所有設定與政策。
- **控制平面**：計算路徑、下達設定、協調設備狀態與故障處置的部分；控制正確不等於資料搬運已通過壓力測試。
- **自我聲明（self-attestation）**：供應商依共同清單自行申報產品實作狀態；它需要可核對附件，也不同於第三方認證或跨廠互通。
- **系統壓力與規模測試**：在高負載、擴大節點數、長時間運轉與故障注入下檢查整套系統，而不只測單一連線。
- **生命週期自動化**：把設備上線、設定、更新、監控、故障替換與退役變成可重複流程，並追蹤設定是否悄悄偏離。
- **OPG-M**：OCP 針對多顆加速器開放運算櫃提出的參考架構名稱；本文只把它當成一套可核對設計，不當成所有叢集標準答案。
- **傳輸層（Transport）**：在實體連線之上規定資料如何分段、送達、排序、重試與回報狀態；它仍需和端點、交換與軟體一起驗收。
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
- **集體通訊（collective communication）**：多個運算 rank 共同參與的一次資料交換，例如把每個 rank 的結果加總後再分發；它不是單一端點傳給另一端點的普通拷貝。
- **Rank**：參與同一 collective 的一個運算程序／裝置身分；rank 數、所在節點與裝置映射都會改變資料路徑。
- **AllReduce**：把所有 rank 的輸入依指定運算合併，並讓每個 rank 都取得相同完整結果；常見於同步梯度。
- **ReduceScatter**：先合併所有 rank 的輸入，再把結果切成不同區塊分給各 rank；它只完成 AllReduce 的其中一段責任。
- **AllGather**：收集每個 rank 的不同區塊，再讓所有 rank 都取得完整集合；ReduceScatter 後接 AllGather 可構成 AllReduce 的資料語意。
- **AlltoAll**：每個 rank 都把不同資料區塊送往每一個其他 rank；流量形狀與 AllReduce 不同，不能共用同一個頻寬係數。
- **線速（line rate）**：連結或埠在指定方向宣告的 bit rate；它不是扣除編碼、協定、重試與壅塞後送達應用的有效資料速度。
- **Payload goodput（有效資料吞吐）**：在指定起訖點真正完成且可用的 payload bytes／time；失敗、重試與額外標頭要依事先定義決定是否計入。
- **Algorithm bandwidth（algbw）**：NCCL tests 以 collective 的 message size 除以 operation time 得到的 S／t；它回答指定大小完成多快，不是硬體 wire counter。
- **Bus bandwidth（busbw）**：NCCL tests 依 collective 類型與 rank 數，把 algbw 乘上理論流量係數的正規化數；它可以協助讀硬體利用，但不是另一份獨立量測 payload。
- **Bisection／oversubscription（對切頻寬／超額匯聚）**：前者看把拓撲切成兩半時可通過多少流量，後者看端點總注入能力是否大於上游容量；埠速相加不等於所有端點能同時用滿。
- **運算—通訊重疊**：讓資料傳輸與晶片計算同時進行，試圖把部分通訊時間藏在計算後面；microbenchmark 變快不代表實際 step 一定少等同樣時間。
- **慢端／step tail**：同一步中最慢 rank 或最慢一次 collective 決定同步等待；平均 operation time 良好，仍可能被尾端延遲、重試或壅塞拖住。
- **Avg／Min／Max／p99**：Avg 是平均，Min／Max 是指定 rank 或 iteration 集合的最低／最高值，p99 是約 99% 觀測不超過的尾端門檻；必須連同事件數與集合定義閱讀。
- **JSON**：以固定鍵值結構保存文字、數字與陣列的可機器讀取格式；輸出原始 JSON 有助重算，但不保證量測方法或資料本身正確。
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

- 一座人工智慧叢集同時有運算同步、跨機架傳送、一般服務、儲存與維修管理等不同工作，不能只看成「一張網」。
- 即使幾張網使用同一類線材或交換設備，也可能有不同的資料、設定、故障與驗收責任。
- 測試清單或單件聲明只走到中途；還要再看跨廠組合、整套系統壓力、客戶部署與公司財務能否逐層對上。

### 為什麼重要

人工智慧叢集像一座同時有高速道路、貨運道路、服務道路與救援通道的城市。運算同步、
跨機架傳送、一般服務、儲存和維修管理搬的是不同資料，也承受不同的延遲、故障與權限要求。
它們可能共用設備家族，甚至匯聚在同一台設備，卻不能因此共用結論或把需求重複計算。

閱讀新聞時，先把整條路徑展開，找出「資料從哪裡出發、途中經過什麼、由哪個軟體
控制、最後到哪裡」。再問測試是否同時涵蓋不同廠商、不同版本、正常傳輸、錯誤恢復與
實際工作負載。這樣才能分辨「一個零件能動」、「兩個零件能連」和「整個系統可交付」。

### 接下來怎麼追

- 先判斷資料正在服務運算同步、跨機架、一般服務、儲存、帶內或帶外管理哪一張網，再展開端點、連接、交換與軟體。
- 再把 UALink、ESUN、SUE-T 與 UEC 放回正確網路工作，分別追實體／連結、端點／傳輸、交換／壅塞、軟體／管理與驗收層。
- 互通報告要列出廠商組合、產品版本、測試拓撲、正常與故障測項、軟體版本、通過條件與重現方法。
- 最後依序追樣品、出貨、客戶驗收、正式開放、實際部署與利用率；任何一步都不能跳過。

### 想一想

- 兩家公司的零件已能傳送正常資料，還要故意製造哪些錯誤，才能知道它們真的會一起恢復？
- 同一類網路技術能服務不同工作時，研究者要如何分開延遲、資料、權限、路由與故障要求？
- 如果同一台設備同時服務幾張網，如何避免把同一份連接數、出貨或收入計算兩次？

## 先把一座人工智慧叢集拆成六張網

| 本文六張網 | 它搬什麼／做什麼 | OCP 參考架構如何分 | 失效時先看到什麼 | 不能直接推成 |
|---|---|---|---|---|
| 1. 加速器機架內擴充 | 讓同一運算群組的加速器快速同步資料與記憶體狀態 | 在叢集視角列為獨立 scale-up network，位於開放運算櫃內部 | 加速器等待、同步停頓、工作無法像單一大系統完成 | 有高速連線不等於端點、記憶體與錯誤恢復已互通 |
| 2. 跨機架／後端擴充 | 讓多個運算櫃共同完成大型工作 | 列為 scale-out network，使用獨立實體資源 | 集體運算變慢、熱點壅塞、跨櫃工作失敗 | 同為乙太網路不等於它和一般服務或儲存使用同一設定 |
| 3. 一般服務／處理器網路 | 搬運處理器與服務入口的資料，不負責加速器彼此的最低延遲同步 | OPG-M 稱為 SO-C；OCP 現行計畫以 front-end networking 涵蓋此類入口 | 服務請求、排程或處理器資料路徑受阻 | 有前端連線不等於後端運算網已完成壓力驗收 |
| 4. 儲存網路 | 讀寫模型、資料集、檢查點與其他持久資料 | 列為獨立 storage network | 讀取等待、檢查點寫入失敗、復原時間拉長 | 儲存吞吐高不等於加速器互連延遲低，也不能把容量重複歸因 |
| 5. 帶內管理網路 | 沿正常系統路徑發現、設定、觀察與維護設備 | 和 SO-C 一起屬前端工作，但在 OPG-M 中另列獨立網路 | 設定下不去、遙測中斷、軟體與設備狀態漂移 | 管理介面能連不等於資料平面正確或故障時仍可救援 |
| 6. 帶外管理網路 | 主網失效時仍能開機、重置、診斷與維修 | 列為獨立 out-of-band management network | 無法遠端救援、重置或確認硬體狀態 | 有救援通道不等於生產資料路徑具備冗餘 |

這六項是 S20 參考架構可逐項核對的完整列舉，不是抽樣估計，所以沒有抽樣誤差或標準誤。
它也不是「所有叢集一定有六套獨立交換器」：S20 特別採五張外部網分離的非匯聚設計，並明示這套
設計不假設或要求冗餘。其他系統可以在實體上匯聚部分平面，但仍要保留邏輯責任、流量分母、故障
邊界與驗收條件，否則同一設備的埠數、需求與收入容易被重複計算。

## 再把每張網拆成八層驗收契約

| 本文八層契約 | 要回答的問題 | 本輪一手文件走到哪裡 | 升級所需證據 | 不能直接推成 |
|---|---|---|---|---|
| 1. 實體與連結 | 訊號、線材、光電轉換、速度、重試與連線狀態是否正確 | UALink、UEC 與 ESUN 都有相應規格／工作範圍 | 具名產品、版本、測試條件、長時間錯誤與通過結果 | 訊號通過不等於封包、記憶體與軟體相容 |
| 2. 端點、記憶體與傳輸 | 兩端如何發送、排序、同步、讀寫與回報錯誤 | UALink Common、SUE-T 與 UEC Transport 顯示責任被單獨定義 | 至少兩家端點實作、相同版本與正常／異常結果 | 有端點規格不等於交換器與整個工作已通過 |
| 3. 交換、路由與壅塞 | 資料如何多跳轉送、排隊、避免熱點並在失敗時改道 | ESUN 與 UEC 工作範圍涵蓋交換、連結及壅塞相關責任 | 具名交換平台、拓撲、負載、緩衝、故障與恢復結果 | 標示人工智慧用途不等於符合指定開放規格 |
| 4. 軟體與控制 | 驅動、函式庫、網路作業系統與控制平面能否協調版本及路徑 | UALink Manageability、UEC Software 與 OCP 參考架構已有分工 | 軟體版本、設定、設備發現、重啟、升級與重現腳本 | 硬體相連不等於實際工作或升級後仍正確 |
| 5. 管理、遙測與除錯 | 如何觀察能力、設定漂移、壅塞、故障與生命週期 | UEC Management／Performance and Debug 與 OCP 管理範圍已有入口 | 指標定義、事件時間線、設定差異、告警與修復結果 | 有儀表板不等於資料正確或故障已復原 |
| 6. 單件合規與自我聲明 | 一件產品是否依共同清單聲明或測試指定功能 | UEC 說明檔明定測試床與兩份 checklist 供實作者自我聲明；另頁會員聲明是必要專利權利登錄，不是產品聲明 | 具名產品、版本、已填清單、測試器、測項與結果 | 工具入口、專利聲明、自我聲明或單件通過都不等於其他廠商能一起工作 |
| 7. 多供應商互通 | 不同端點、交換器與軟體能否在共同版本下通過正常與故障組合 | S19 明確把 interoperation 排除在該測試床文件範圍外 | 廠商組合矩陣、拓撲、版本、錯誤注入、失敗與重現方法 | 合規頁、會員名單或單廠展示不能替代交叉矩陣 |
| 8. 系統、部署與財務 | 在壓力、規模與長時間運轉下能否交付，並對上客戶與供應商分母 | S19 也排除 system stress／scale 與 performance；OCP 文件仍是範圍與參考架構 | 具名站點、端點／機架數、期間、工作負載、故障、利用率、出貨與財務 | 參考架構或測試框架不等於客戶已部署、公司已取得收入 |

UEC 現行頁面列出的八個工作組同樣是組織當下範圍的完整列舉，不是成熟產品樣本。最重要的
閱讀邊界是：第六層現在已有公開工具，不等於第七、八層自動通過。要比較標準、產品或供應商，
必須先固定「哪一張網」與「哪一層契約」；只寫「支援 Ethernet」少了兩個分母，不能拿來做份額或財務歸因。

## 400G、algbw、busbw 與訓練時間不是同一個數字

看到「400G 網路」、「100 GB/s collective」或「訓練快 20%」，不能先排大小。第一個數字可能是
單一 port 的 bit rate，第二個可能是 message size／operation time，第三個才是整套系統跑到品質門檻
的 wall-clock；三者的分子、分母與量測起訖點都不同。[S21][S22][S24]

| 效能數字 | 它真正量什麼 | 最少要綁定 | 它不能單獨證明 |
|---|---|---|---|
| Port／lane line rate | 指定方向的名目 bits／second | port、lane、方向、編碼／FEC、線距、介質與版本 | payload bytes、同時可用總頻寬、collective 或訓練速度 |
| Installed aggregate | 多個 port／link 名目容量的加總 | 端點數、每端 link、雙向是否重複計、拓撲、bisection 與 oversubscription | 所有端點能同時滿載、沒有熱點，或應用可取得同樣吞吐 |
| Payload goodput | 指定起訖點真正完成且可用的 payload bytes／time | payload／wire 定義、成功、retry、compression、時間窗與並行 | collective 資料語意、尾端延遲、資料正確或訓練到品質目標 |
| Algorithm bandwidth（algbw） | NCCL tests 的 message size S／operation time t | collective、S、t、rank、datatype、group 與量測同步方式 | 實際 wire traffic、硬體利用率、跨 rank tail 或端到端 training time |
| Bus bandwidth（busbw） | 依 collective 與 rank 數把 algbw 乘上理論流量係數 | 同一 algbw、正規化公式、point-to-point／offload 假設與硬體 peak 範圍 | 第二份獨立 payload、實測 port counter、bisection，或所有演算法都適用 |
| Step／wall-clock-to-quality | 模型一步或完整訓練到指定品質所需時間 | 模型、資料、品質、batch、系統／軟體版本、run 分布與失敗 | 單一網路元件就是因果、互通已通過，或改善會變成公司收入 |

### Collective 名稱先固定，頻寬係數才有意義

NCCL 現行語意頁要求每個 rank 用相同 count 與 datatype 共同呼叫，否則可能 hang、crash 或資料
損壞；AllReduce、ReduceScatter、AllGather 與 AlltoAll 交付的資料結果也不同。[S23] NCCL tests
的 `busbw` 係數因此依 collective 改變：[S21]

| Collective | 每個 rank 最後拿到什麼 | NCCL tests 的 busbw／algbw 係數 | 不能誤讀成 |
|---|---|---:|---|
| AllReduce | 所有 rank 輸入被 reduce 後的同一完整結果 | `2(n−1)／n` | 每 rank 只送一份 S，或 busbw 是額外完成的應用資料 |
| ReduceScatter | reduce 後結果的一個 rank-specific 區塊 | `(n−1)／n` | 已讓所有 rank 取得完整結果 |
| AllGather | 所有 rank 原有區塊合併後的完整集合 | `(n−1)／n` | 已執行 reduce，或與 AlltoAll 有相同資料流向 |
| AlltoAll | 每個 rank 對每個其他 rank 發送不同區塊並收回對應區塊 | `(n−1)／n` | 流量均勻、沒有熱點，或 MoE routing 已獲得同樣結果 |
| Broadcast／Reduce | 完整資料從 root 分發，或 reduce 結果只回 root | `1` | root 不會成為瓶頸，或 rank mapping 不重要 |

這些是 NCCL tests 為 point-to-point send／receive 模型建立的正規化，不是每條 link 的封包
計數。若系統使用階層式路徑、硬體 collective offload、多個平行 group 或不同 topology，仍要把
實際 algorithm／protocol／path 寫入，不能只套係數後宣稱量到 wire bandwidth。

### 同一個 20 ms，可以同時產生兩個不同頻寬欄位

先做一個只教公式、不模擬真實網路的例子。假設 `n=8 ranks`、每個 rank 的 AllReduce message
`S=1,000,000,000 bytes`、operation time `t=0.020 seconds`，並採 NCCL tests 的 point-to-point
正規化：

| 步驟 | 確定性計算 | 結果 | 不能外推 |
|---|---|---:|---|
| 1. Algorithm bandwidth | `S／t` | `50 GB/s` | 不等於單一 port、wire traffic 或 training goodput |
| 2. AllReduce 正規化係數 | `2×(8−1)／8` | `1.75` | 不是另一個量測 run，也不是所有 collective 的係數 |
| 3. Bus bandwidth | `50×1.75` | `87.5 GB/s` | 不表示應用另完成 87.5 GB/s 唯一 payload |
| 4. 仍缺的共同結果 | step time、stall、正確性、失敗、品質、資源與成本 | 未量測 | 不能宣稱網路讓訓練或公司財務改善 |

`50` 與 `87.5` 都由同一筆 S、t 與 rank 數衍生，不能相加成 `137.5 GB/s`。這是
**N=1 個假想 collective 設定**的確定性公式展開，沒有 device、port、topology、run 或抽樣，所以沒有 sampling
SE／t。Python Fraction 與獨立 awk 都得到 factor=`7／4`、algbw=`50`、busbw=`175／2 GB/s`；
一致只證明公式與算術，沒有驗證 protocol overhead、retry、congestion、overlap、tail、correctness
或任何產品效能。

### 十欄 AI collective 效能護照

| 護照欄位 | 最少要寫什麼 | 少了最容易誤讀成 |
|---|---|---|
| 1. 網路工作與量測範圍 | 六張網中的哪一張；device、node、rack、pod 或 end-to-end 起訖點 | scale-up microbenchmark 直接代表整座 scale-out 叢集 |
| 2. Collective 與資料語意 | AllReduce／ReduceScatter／AllGather／AlltoAll；reduce op、root、in-place 與 correctness | 不同資料工作的 GB/s 被放進同一排行榜 |
| 3. Rank 與 placement | total ranks、process×thread×device、每 node／rack 數、rank-to-device mapping 與 group | 8 顆同機與 8 櫃跨網路被視為同一規模 |
| 4. Message 與 datatype | per-rank／total count、bytes／GB／GiB、dtype、size sweep、alignment 與 compression | message size、單位與資料精度差異被藏起來 |
| 5. 拓撲、link 與容量 | port／lane、方向、link 數、hop、switch tier、bisection、oversubscription、銅／光與 FEC | 所有 port 名目速率相加就等於可用 collective bandwidth |
| 6. 軟硬體與演算法版本 | accelerator／NIC／switch／optic／firmware、driver、NCCL、algorithm、protocol、routing | 同時換版本與拓撲，改善卻全歸因一顆晶片 |
| 7. Demand、並行與重疊 | 同時 collective／flow／tenant、parallel group、compute overlap、background traffic 與 queue | 無競爭 microbenchmark peak 被寫成 production step 效能 |
| 8. 指標、時間與正確性 | operation time、payload goodput、algbw／busbw 公式、rank Avg／Min／Max、sync、timeout 與 data check | 衍生正規化被當 wire counter，錯誤結果也算進快速度 |
| 9. 視窗、重複與失敗 | warm-up、iterations、cycles、per-iteration raw、p50／p99／max、run 數、retry／drop／hang 與 SE／t | 單次平均掩蓋慢 rank、尾端壅塞、挑選與不穩定 |
| 10. 使用者與商業結果 | step／stall、tokens／samples、wall-clock-to-quality、功耗、成本、部署量、價格、收入與毛利 | 網路 benchmark 直接變成訓練效益、TAM、訂單或公司獲利 |

NCCL tests 現行工具已提供 message sweep、warm-up、iterations、cycles、rank Avg／Min／Max、
per-iteration p99／max、raw JSON 與 correctness 設定，讓第 3、4、8、9 欄可以被保存；工具存在不
表示任何結果已按正確條件執行。[S22] MLCommons 的另一層要求則是固定完整 system／software，
以連續 wall-clock 跑到品質目標，並依 workload 使用多次 run 形成 benchmark result。[S24]
它不是網路測試，但能防止把 microbenchmark 峰值替代真正訓練結果。

### 多空小作文要共享同一個 step

| 敘事 | 合理假說 | 必須再看到的共同證據 | 什麼會讓敘事失效 |
|---|---|---|---|
| 偏多：更大 AI 叢集提高網路內容與驗證 | ranks、AlltoAll／AllReduce 流量、tail SLO 與多層拓撲增加，可能增加 switch ASIC、NIC、retimer、optic、cable、PCB、管理與整合驗證 | 同一 workload 的十欄護照、BOM、link／port utilization、故障、qualification、部署量、價格、收入與毛利分母 | 只有 port line rate、algbw／busbw peak、產品頁或會員名單，沒有 step bottleneck、採用與財務共同鍵 |
| 偏空：軟體與拓撲吸收部分硬體增量 | sharding、compression、overlap、routing、collective algorithm 與更高利用率可能降低每單位 compute 的外部流量或設備數 | 固定模型／品質與系統的 bytes、overlap、step tail、wall-clock、設備數、功耗與成本前後比較 | 只看 network time 下降，卻漏掉品質、計算等待、其他網路平面、重試、冗餘或更大總運算量 |
| 共同底線 | 高 line rate 不等於高 application goodput，更不等於公司賺到 | 固定 plane／collective／rank／message／topology／version／metric／distribution，再做買方與供應商雙向核對 | 把不同 collective、不同 rank placement 或衍生 busbw 直接相加成 TAM、份額或投資結論 |

本輪新增 N=4 份一手頁面，屬 NVIDIA NCCL 與 MLCommons 兩條獨立方法鏈，不是四個產品、叢集、
客戶或 run 樣本；再與既有 UEC、OCP 方法鏈交叉，也只建立量測責任。除了 N=1 教材公式，沒有
新的 effect size、sampling SE／t、價格、估值、共識、部位或投資判斷。

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
| 4. UEC | 人工智慧與高效能運算的跨機架乙太網路為主要應用 | 工作組橫跨實體、連結、傳輸、軟體、儲存、合規、管理、效能與除錯 | 現行公開版本為 1.0.3，且有自我聲明與部分測試床工具 | 不能說任何具名元件已通過、完成跨廠互通或客戶部署 |
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
| 1. 共同規則可查核 | 規格版本、功能、角色、錯誤行為與測試入口有公開文件 | UALink 2.0、UEC 1.0.3、ESUN 1.0 可查；SUE-T 是獨立工作流；UEC 合規工具已有入口 | SUE-T 正式規格，以及各路徑持續更新的合規與互通方法 | 規格或工具發布不等於實體晶片存在或產品已通過測試 |
| 2. 路徑各位置有具名實物 | 至少能指出端點、連接傳輸、交換器與所需軟體的產品、版本和功能 | Helios、Marvell UALink 方案與 Arista 7060XE7 證明多個位置有具名開發路徑 | 對應同一規格版本的端點、交換器、韌體、驅動與測試配置 | 不同新聞中有多個產品，不等於它們已在同一路徑上工作 |
| 3. 單件產品符合指定規格 | 每件產品依共同方法通過實體層、協定、功能、計時與錯誤測項 | UEC 已有自我聲明、測試床與 checklist 工具；本輪仍未找到具名產品已填清單或通過報告 | 產品名、版本、已填清單、測試器、測項、通過條件與可查核結果 | 工具存在或一件產品合格不等於它能和其他廠商產品工作 |
| 4. 不同廠商完成交叉互通 | 至少兩家獨立端點與交換實作，在共同版本與軟體下交叉測試正常與異常情境 | UEC 測試床文件明示 interoperation 不在範圍；其他現有文件也沒有可核對交叉矩陣 | 參與廠商、組合矩陣、版本、拓撲、測項、錯誤注入、軟體與重現方法 | 單廠端到端展示、會員名單、自我聲明或產品互連宣稱不等於通過 |
| 5. 整個系統與工作可重現 | 在有壓力、擴容、故障與長時間運轉下，實際工作仍會正確完成 | UEC 文件排除 system stress／scale 與 performance；OCP／Helios 仍是範圍、參考設計或前瞻規畫 | 端點與機架數、軟硬體版本、工作負載、期間、故障、恢復與通過門檻 | 參考設計、預覽、測試清單或單次最高數字不等於可交付系統 |
| 6. 客戶部署與公司財務對上 | 具名客戶完成驗收與部署，供應商用同一產品、期間與分母提供出貨和財務結果 | Oracle 仍是規劃；台灣三個族群仍只是待驗證搜尋路由 | 出貨、預覽、正式開放、部署數、利用率，以及客戶與供應商雙向財務文件 | 規格、會員、產品用途或客戶規劃不等於台灣公司已獲利 |

本輪可確認第一關有多份規格、工作文件與合規工具，第二關有分散的具名產品路徑；第三關已有框架但沒有
本輪可核對的具名產品結果，第四關沒有跨廠矩陣，第五關仍停在參考架構與前瞻規畫，第六關也尚未通過。六關是閱讀與證據排序，
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
- [OCP Open Cluster Designs for AI](https://www.opencompute.org/index.php/community/cluster-designs-for-ai)（scale-up、scale-out、front-end、storage 與 management networking 的現行範圍）。
- [OCP AI Networking Reference Architectures webinar](https://www.opencompute.org/events/past-events/ocp-educational-webinar-new-ocp-reference-architectures-for-ai-networking)（資料／控制平面、生命週期、BOM 與多張網路的設計範圍）。
- [UEC Working Groups](https://ultraethernet.org/working-groups/)（八個規格、軟體、管理、合規與除錯工作層）。
- [UEC Compliance](https://ultraethernet.org/compliance/)（頁面所連說明檔定義自我聲明、測試床與 checklist；會員聲明是必要專利權利登錄，並非產品結果）。
- [UEC Compliance Test Bed Recommendations](https://ultraethernet.org/wp-content/uploads/sites/20/2025/06/UEC-Compliance-Test-Test-Bed-Recommendations.pdf)（部分層級與明示排除的互通、系統壓力／規模、效能邊界）。
- [OCP Open Pod Group for M xPUs System Architecture](https://www.opencompute.org/documents/opg-m-system-architecture-final-14-january-2026-pdf)（六張網、非匯聚設計與冗餘假設）。
- [NCCL tests performance definitions](https://github.com/NVIDIA/nccl-tests/blob/master/doc/PERFORMANCE.md)（operation time、algbw、collective-specific busbw 與 point-to-point 推導邊界）。
- [NCCL tests usage and arguments](https://github.com/NVIDIA/nccl-tests)（rank、message sweep、warm-up、iterations、tail、raw JSON 與 correctness 設定）。
- [NCCL collective operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html)（各 collective 的 rank、輸入與輸出語意）。
- [MLPerf Training rules](https://github.com/mlcommons/training_policies/blob/master/training_rules.adoc)（完整 system／software、wall-clock-to-quality 與多次 run 的終端結果契約）。

本篇不使用會員數、宣稱頻寬、GPU 數或公司效能數字做跨公司比較，也不推估 TAM、市占、估值或
市場預期。六張網與八個 UEC 工作組是官方文件的類別列舉，不是產品通過率或市場樣本。ESUN 1.0
發布與 7060XE7 支援 scale-up 是兩個不同事件，尚不能合併成「Arista 已部署 ESUN」；UEC 公開
合規工具也不能合併成「已有產品互通」。Oracle 規劃已進入原訂季度，仍不代表部署已發生。

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

- UEC 公開第一批具名產品的已填自我聲明／測試結果，並與 patent declaration 分開；UALink、ESUN／SUE-T 也各自公布可核對的 compliance program。
- UALink／ESUN／SUE-T／UEC 公布 plugfest 與可重現的 multi-vendor interoperability 組合矩陣，而不是只提供 checklist。
- 具名人工智慧叢集公開六張網的實體／邏輯映射、是否匯聚、冗餘、BOM、軟體版本、故障與長時間系統驗收。
- ESUN network side 與 SUE-T endpoint／transport 由至少兩家獨立 silicon 實作互通，而不是只有同一公司端到端展示。
- Merchant silicon、switch、NIC、retimer 或 chiplet 從 IP／樣品升級為 production，並能對應正式標準與具名客戶。
- Arista 或客戶確認 7060XE7 實際出貨、部署層級與 scale-up／scale-out 分母。
- Oracle 或 AMD 確認 MI450／Helios shipment、preview 或 GA，而不是沿用 2025 年的前瞻規劃。
- 台灣公司用具名產品、qualification、出貨與財務資料完成雙向核對；否則只保留產業節點，不畫公司受惠線。
