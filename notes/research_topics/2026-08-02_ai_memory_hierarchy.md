# 人工智慧資料為什麼要分層存放：正在運算、等待取用與長期保存各有位置

<!-- research_topic
topic_id: MI-2026-08-02-AI-MEMORY-HIERARCHY
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-01-05
last_reviewed_at: 2026-08-12
review_due: 2026-08-17
source_type: mixed
publisher: NVIDIA
publisher_domain: developer.nvidia.com
canonical_url: https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/
source_chain_id: rubin-memory-hierarchy-20260802
stock_ids:
group_ids: memory,serverodm
trigger_type: platform_memory_architecture
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C8
base_confidence: medium
confidence_basis: NVIDIA、Micron 與 CXL Consortium 一手來源可交叉確認 HBM、SOCAMM、context storage、storage processing 與 coherent expansion 是不同但相接的角色；Micron 又把 192GB SOCAMM2 的量產與 256GB 的較早送樣公告拆成不同容量時鐘，NVIDIA 文件則把 placement、搬移與 CPU 端處理接進 BlueField-4 STX 資料路徑，但 256GB 的具名量產、CMX／CXL 客戶部署、端到端系統結果及台灣財務曝險仍未證實
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: primary_source_ai_memory_hierarchy_scan
evidence: source_chain:rubin-memory-hierarchy-20260802
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_platform_tiers_from_product_sampling_and_supplier_financial_exposure
evidence: sources:S1,S2,S3,S4
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
reason: editorial_plain_language_wave4_memory_learning_no_conclusion_change
evidence: editorial:plain_language_wave4
-->
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave89_memory_layers_and_maturity_no_conclusion_change
evidence: editorial:plain_language_wave89_memory_layers_and_maturity
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: superseded_static_memory_tier_thesis_after_vera_storage_data_path_evidence
evidence: sources:S8
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: separated_socamm2_family_capacity_clocks_and_extended_five_role_data_path
evidence: sources:S9,S10,S11
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_kv_tiering_measurement_passport_and_refreshed_exact_host_storage_edges
evidence: sources:S12,S13,S14,S15,S16,S17
-->

<!-- research_source
source_id: S1
role: company_release
source_kind: document
publisher: NVIDIA
title: Inside the NVIDIA Vera Rubin Platform: Six New Chips, One AI Supercomputer
published_at: 2026-01-05
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/
locator: Vera CPU memory capacity table；Rubin GPU HBM4 段落；PCIe／CXL 欄位
limitation: 平台規格與 NVIDIA 效能主張不等於客戶部署、利用率、記憶體採購量或供應商份額
independence_group: nvidia
-->

<!-- research_source
source_id: S2
role: company_release
source_kind: document
publisher: NVIDIA
title: Introducing NVIDIA BlueField-4-Powered CMX Context Memory Storage Platform
published_at: 2026-03-16
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://developer.nvidia.com/blog/introducing-nvidia-bluefield-4-powered-inference-context-memory-storage-platform-for-the-next-frontier-of-ai/
locator: G1–G4 hierarchy 段落；CMX G3.5 context tier；KV cache placement 說明
limitation: CMX 的效能與效率為 NVIDIA 平台主張；沒有提供獨立客戶實績、採用量或台灣供應商財務拆分
independence_group: nvidia
-->

<!-- research_source
source_id: S3
role: competitor_primary
source_kind: document
publisher: Micron Technology
title: Micron Introduces 256GB LPDRAM SOCAMM2
published_at: 2026-03-05
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://investors.micron.com/news-releases/news-release-details/meiguangtuichuquanqiushoukuangaorongliang256gb-lpdram
locator: 256GB SOCAMM2 capacity 段落；customer sampling 段落；內部測試註腳
limitation: 產品仍在客戶送樣；效能、功耗與尺寸比較是 Micron 內部測試及公司定義，本文不拿來推估跨公司優勢
independence_group: micron
-->

<!-- research_source
source_id: S4
role: standard
source_kind: document
publisher: Compute Express Link Consortium
title: CXL 4.0 Specification Release
published_at: 2025-11-18
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://computeexpresslink.org/wp-content/uploads/2025/11/CXL_4.0-Specification-Release_FINAL_Website-Copy.pdf
locator: CXL 4.0 release；bandwidth、bundled ports 與 memory RAS 摘要
limitation: 標準發布不等於主機、記憶體裝置、retimer 已完成互通或形成出貨；Rubin 文件列的是 CXL 3.1，不可改寫成已採 CXL 4.0
independence_group: cxl-consortium
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: living_index
publisher: NVIDIA
title: NVIDIA Technical Blog
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://developer.nvidia.com/blog/
locator: 2026-08-02 查得 Vera Rubin 與 CMX 技術文章；用於偵測後續部署、架構與軟體更新
limitation: 索引頁只用來找新文件；任何新增平台主張仍須回到具體文章或產品文件
independence_group: nvidia
-->

<!-- research_source
source_id: S6
role: competitor_primary
source_kind: living_index
publisher: Micron Technology
title: Micron News Releases
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://investors.micron.com/news-events/news-releases
locator: 2026-08-02 查得 SOCAMM2、HBM4 與資料中心記憶體更新入口
limitation: 新聞索引不證明產品量產、客戶採用或財務貢獻；需回到具體公告與財報
independence_group: micron
-->

<!-- research_source
source_id: S7
role: standard
source_kind: living_index
publisher: Compute Express Link Consortium
title: About CXL and current specification
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://computeexpresslink.org/about-cxl/
locator: 2026-08-02 顯示 CXL 是 cache-coherent processor／memory expansion／accelerator interconnect，CXL 4.0 為現行規格
limitation: 規格入口不代表任一平台或裝置完成互通、驗證、量產或收入認列
independence_group: cxl-consortium
-->

<!-- research_source
source_id: S8
role: company_release
source_kind: document
publisher: NVIDIA
title: NVIDIA Vera Storage Benchmarks: Faster Encryption, Compression, Integrity Checking, and Recovery for AI-Native Storage
published_at: 2026-08-03
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://developer.nvidia.com/blog/nvidia-vera-storage-benchmarks-faster-encryption-compression-integrity-checking-and-recovery-for-ai-native-storage/
locator: Storage data path 段落；Vera CPU／BlueField-4 STX／SOCAMM2 架構段落；Measuring foundational storage performance 的測試範圍與 end-to-end 限制
limitation: NVIDIA 自建、非現成公開 benchmark；資料已在記憶體，排除 file I/O、disk、network、command startup 與 external-device bottleneck，未報可核對的獨立重複樣本、誤差或客戶部署，本文不採用跨平台倍數並保留來源明示的端到端測試缺口
independence_group: nvidia
-->

<!-- research_source
source_id: S9
role: competitor_primary
source_kind: document
publisher: Micron Technology
title: Micron in High-Volume Production of HBM4 Designed for NVIDIA Vera Rubin, PCIe Gen6 SSD and SOCAMM2
published_at: 2026-03-16
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin
locator: News highlights 的 192GB SOCAMM2 high-volume production 與 48GB–256GB portfolio；Vera Rubin NVL72／Vera CPU 段落
limitation: 這是 Micron 的產品與量產宣稱；只明列 192GB 為 high-volume production，48GB–256GB 是產品組合範圍，不證明每個容量都量產，也未揭露客戶數、供應份額或 SOCAMM2 財務貢獻
independence_group: micron
-->

<!-- research_source
source_id: S10
role: company_filing
source_kind: document
publisher: Micron Technology
title: Micron Technology, Inc. Reports Record Results for the Third Quarter of Fiscal 2026
published_at: 2026-06-24
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-record-results-third-quarter
locator: Product highlights 的 LP5X SOCAMM2 products high-volume production 與 multiple capacity points 敘述
limitation: 財務結果新聞稿只把 SOCAMM2 產品家族與多容量產品組合列為量產進展，沒有逐一列出量產容量、客戶、出貨量、收入、毛利或供應份額；本文不使用同頁公司財務總數推估 SOCAMM2 貢獻
independence_group: micron
-->

<!-- research_source
source_id: S11
role: company_release
source_kind: document
publisher: NVIDIA
title: Scaling Agentic AI Factories Through Extreme Co-Design with NVIDIA BlueField
published_at: 2026-07-16
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://developer.nvidia.com/blog/scaling-agentic-ai-factories-through-extreme-co-design-with-nvidia-bluefield/
locator: Agentic AI infrastructure data path；BlueField data movement；AI-native storage and context memory 的 KV I/O、metadata、placement、security 與 control operations
limitation: NVIDIA 平台文章可界定元件與軟體角色，但效益敘述是公司主張；沒有具名客戶部署、相同工作負載對照、獨立重複樣本、誤差、完整端到端結果或台灣供應商財務拆分
independence_group: nvidia
-->

<!-- research_source
source_id: S12
role: company_release
source_kind: living_index
publisher: NVIDIA
title: NVIDIA Dynamo KVBM Overview
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/kvbm/overview
locator: Unified memory layer 摘要；When to Use KV Cache Offloading；Architecture 的 GPU／host／SSD／remote storage 與 NIXL 路徑
limitation: 這是持續更新的 NVIDIA 軟體架構文件；證實可用資料層與適用條件，不證明 CMX、SOCAMM、CXL 或具名客戶已採用，也不提供獨立端到端效益、成本或可靠度結果
independence_group: nvidia
-->

<!-- research_source
source_id: S13
role: company_release
source_kind: living_index
publisher: NVIDIA
title: NVIDIA Dynamo KVBM Guide
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://docs.nvidia.com/dynamo/latest/user-guides/kv-cache-offloading
locator: Cache Tier Configuration；Available Metrics；Benchmarking KVBM；No TTFT Performance Gain
limitation: 文件中的設定、指標與故障排除只界定 KVBM 可觀測性及可能失效方式；範例模型、容量與平均 TTFT 不是客戶 production benchmark，也不能直接外推到其他 backend、工作負載或硬體
independence_group: nvidia
-->

<!-- research_source
source_id: S14
role: company_release
source_kind: living_index
publisher: NVIDIA
title: Set up KV Cache Offloading — NVIDIA Dynamo Documentation
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://docs.nvidia.com/dynamo/dev/kubernetes/kv-cache-offloading/overview
locator: The pattern 的 tier sizing；Verify 的 repeated long-prefix requests、second-request TTFT 與 offload hit-rate 檢查
limitation: 這是一份部署驗證指南，不是正式效能比較；重複請求只建立可產生重用的測試機會，第二次 TTFT 改善也不能單獨隔離網路、排隊、模型、路由或搬移成本
independence_group: nvidia
-->

<!-- research_source
source_id: S15
role: company_release
source_kind: living_index
publisher: NVIDIA
title: NVIDIA AIPerf Metrics Reference
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://docs.nvidia.com/aiperf/reference/ai-perf-metrics-reference
locator: Record Metrics distributions；TTFT；Decode Duration；ITL；Output Token Throughput；ISL／OSL；Good Request Fraction
limitation: 指標定義能固定分母與時間邊界，但不指定哪個 workload、SLO、模型、硬體或 cache policy 對任何客戶最具代表性；client-observed TTFT 亦包含網路、排隊與 prompt processing
independence_group: nvidia
-->

<!-- research_source
source_id: S16
role: company_release
source_kind: living_index
publisher: NVIDIA
title: Benchmark a Local Deployment with AIPerf
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://docs.nvidia.com/dynamo/dev/cli/operations/benchmarking-with-ai-perf
locator: Baseline benchmark 的 model／concurrency／request count／ISL／OSL；Compare local configurations 的 one-change-at-a-time 與 fixed request-shape contract
limitation: 這是 NVIDIA 工具的比較方法與範例，不是特定記憶體分層結果；固定參數只能提高同一實驗內可比性，不能保證合成負載代表 production trace 或排除所有未觀測混雜因素
independence_group: nvidia
-->

<!-- research_source
source_id: S17
role: standard
source_kind: living_index
publisher: MLCommons
title: MLPerf Inference Rules
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc
locator: Definitions 的 system under test 與 run；General rules 的 consistent system／framework 與 replicability；datacenter LLM latency／quality／scenario tables
limitation: master 規則會持續更新；MLPerf 的模型、資料集、cache 限制與 latency target 是特定 benchmark contract，不等於任何私有 agent workload、CMX／KVBM 部署或公司商業結果
independence_group: mlcommons
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: NVIDIA 的 Vera Rubin 平台同時配置 Rubin GPU 的 HBM4 與 Vera CPU 的 SOCAMM LPDDR5X 系統記憶體，兩者位於不同運算與容量位置
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-01-05
basis: S1 分別列示 Rubin GPU HBM4 與 Vera CPU system memory／SOCAMM 架構
boundary: 平台配置不代表 HBM 與 SOCAMM 可互相替代，也不證明各供應商份額、採購量或收入
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: NVIDIA 將 CMX 定位為介於 GPU HBM、system RAM、local SSD 與 shared storage 之間的 context memory storage 層，用於放置可重建的 KV cache
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-03-16
basis: S2 的 G1–G4 hierarchy 與 G3.5 CMX 段落直接描述資料種類、位置與用途
boundary: 這是 NVIDIA 架構與產品定位，不是獨立客戶測得的成本效益，也不表示所有 agentic AI 都會採用 CMX
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: Micron 於 2026-03-05 宣布 256GB SOCAMM2 已進入客戶送樣，而不是量產或大規模出貨
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-03-05
basis: S3 明確使用 customer sampling 階段語言並列示 256GB 模組
boundary: 送樣不等於 qualification 完成、量產、客戶採購量、供應份額或財務貢獻
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C4
label: verified
status: active
claim: CXL 4.0 已成為可取得的公開規格，持續以 cache coherence 支援 processor、memory expansion 與 accelerator 間的資源共享
supporting_source_ids: S4
contrary_source_ids:
as_of: 2025-11-18
basis: S4 發布公告直接說明 CXL 4.0 規格、適用範圍與新增功能
boundary: 規格可取得不等於 Rubin 已採 CXL 4.0；S1 對 Vera 明列的是 CXL 3.1，也不代表 CXL 4.0 裝置已商用
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C5
label: inference
status: superseded
claim: AI 記憶體的增量研究應由單一 HBM 敘事改成分層問題：熱資料追求頻寬，CPU 與 context tier 補容量、功耗或共享性，CXL 則提供可組合的連接路徑；這些層更可能互補而非一對一替代
supporting_source_ids: S1,S2,S3,S4
contrary_source_ids:
as_of: 2026-08-02
basis: S1 同一平台並列 HBM 與 SOCAMM，S2 明確描述 G1–G4／G3.5 分層，S3 提供 SOCAMM2 產品階段，S4 定義 coherent expansion 路徑
boundary: 尚無統一客戶 workload、容量配置、成本或利用率資料可量化各層份額；不推估 TAM、市占或供應商收入
verification_needed:
corrected_by_claim_id: C8
resolution:
-->

<!-- research_claim
claim_id: C6
label: unverified
status: active
claim: universe 內記憶體、控制 IC、模組、PCB 或伺服器公司已由 SOCAMM、CMX 或 CXL 4.0 取得可辨識訂單與獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: NVIDIA、Micron 與 CXL 文件未點名本 universe 公司，也沒有台灣公司產品、客戶、量產與財務的雙向核對
boundary: 不以產品世代、標準會員、一般記憶體能力或伺服器組裝角色自動建立受惠關係
verification_needed: 需平台或裝置端與台灣公司端雙向核對具名產品、qualification、量產、出貨與財務貢獻
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: NVIDIA 2026-08-03 文件把 Vera CPU 與 SOCAMM2 LPDDR5X 放進 BlueField-4 STX 儲存處理器，並描述資料在儲存讀寫與復原路徑會經過壓縮、加密、完整性檢查與重建；同一文件明示其測試資料已在記憶體，排除檔案 I/O、磁碟、網路、啟動與外部裝置瓶頸，完整系統或 GPU 結果仍需端到端測試
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-08-03
basis: S8 的 storage data path、Vera／BlueField-4 STX／SOCAMM2、benchmark scope 與 end-to-end testing 段落直接界定處理工作及測試邊界
boundary: 只證實 NVIDIA 公開的架構、測試範圍與公司量測主張；不採用倍數做跨平台優劣比較，也不證明 storage system、SSD、network、GPU、功耗、客戶部署或台灣供應商財務結果
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: inference
status: active
claim: AI 記憶體分層不能只畫資料「存在哪裡」；現行研究框架還要把儲存介質、CPU 端資料處理、連接路徑、實際搬運與放置決策拆成五個相接角色：HBM、system memory、context tier 與 storage 仍偏互補，但即使介質不變，壓縮、加密、完整性、復原或搬移控制也可能成為另一個瓶頸與供應鏈驗收點
supporting_source_ids: S1,S2,S3,S4,S8,S11
contrary_source_ids:
as_of: 2026-08-12
basis: correction_of:C5；S1／S3 定位 HBM 與 system memory，S2 定位 context storage、placement 與搬運，S4 定位 coherent expansion，S8 新增 storage CPU 在資料回到應用前執行壓縮、加密、完整性與復原的處理角色，S11 再把 KV I/O、metadata、placement、security、control 與資料搬移分開，因而修正原先只按位置分層的框架
boundary: 這是跨一手來源的角色分類，不主張所有平台都有相同五層、相同瓶頸或相同軟體，也不採用 NVIDIA 自建 benchmark 倍數推估端到端效能、TAM、份額、訂單、收入或市場定價
verification_needed: 同一 production 平台公開資料位置、處理步驟、搬移路徑、工作負載、端到端 SLO 與設備配置，才能驗證五角色是否遺漏、重疊或由同一元件承擔
correction_kind: supersedes
corrects_claim_id: C5
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: verified
status: active
claim: Micron 於 2026-03-16 明列 192GB SOCAMM2 已進入 high-volume production，並把它放在 48GB 至 256GB 的 SOCAMM2 產品組合中
supporting_source_ids: S9
contrary_source_ids:
as_of: 2026-03-16
basis: S9 的 news highlights 逐字把 192GB 與 high-volume production 配對，另將 48GB–256GB 描述為 portfolio 範圍
boundary: 只證實 Micron 對 192GB 產品階段與產品組合範圍的公司聲明；48GB–256GB 不代表每個容量都已量產，也不揭露客戶數、供應份額、收入或毛利
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: Micron 於 2026-06-24 表示 LP5X SOCAMM2 products 已進入 high-volume production，且產品選項擴展到多個容量點，但該段沒有逐一列出哪些容量已量產
supporting_source_ids: S10
contrary_source_ids:
as_of: 2026-06-24
basis: S10 的 product highlights 同一句分別陳述 SOCAMM2 products 的量產狀態與 multiple capacity points 的產品擴展
boundary: 這是產品家族層級的公司進度，不足以把 256GB 或所有 48GB–256GB 容量逐一升級為量產，也沒有 SOCAMM2 出貨量、收入、毛利或客戶分母
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C11
label: inference
status: active
claim: 閱讀 SOCAMM2 商業進度時必須拆到容量與型號：192GB 的具名量產、256GB 的較早客戶送樣，以及產品家族的多容量量產敘述可以同時成立，不能用同一個家族名稱把所有容量自動升到最高成熟度
supporting_source_ids: S3,S9,S10
contrary_source_ids:
as_of: 2026-08-12
basis: S3 只對 256GB 使用 customer sampling，S9 只對 192GB 明列 high-volume production，S10 則以產品家族與 multiple capacity points 表述但沒有容量對照表；三者的名詞粒度不同
boundary: 這是文件粒度與成熟度的研究規則，不表示 256GB 此後一定仍停在送樣，也不否定未公開容量已量產；需要具名容量的新文件才能更新
verification_needed: Micron 或平台文件逐一列出 48GB、96GB、128GB、192GB、256GB 等容量的 qualification／production、平台、出貨與財務邊界
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: NVIDIA 2026-07-16 文件將 BlueField-4／Vera BlueField-4 STX 的角色拆成基礎設施處理與資料搬移，並明列儲存處理器在靠近儲存與網路路徑處執行 KV I/O、metadata、data placement、security 與 control operations
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-07-16
basis: S11 的 BlueField data path、AI-native storage and context memory 段落直接列出資料搬移、KV I/O、metadata、placement、security 與 control 的分工
boundary: 只證實 NVIDIA 公開的架構與功能定位；不證明 CMX／STX 已由具名客戶正式部署、全路徑更快、成本更低，或任一供應商已取得訂單與財務貢獻
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C13
label: verified
status: active
claim: NVIDIA 現行 Dynamo KVBM 文件把 GPU memory、pinned host memory、remote RDMA memory、local／distributed SSD 與 remote file／object／cloud storage 列為同一 KV block memory API 可連接的層，並明示只有在 cache reuse 的收益高於資料搬移 overhead 時，offloading 才最有效
supporting_source_ids: S12
contrary_source_ids:
as_of: 2026-08-12
basis: S12 的摘要、When to Use 與 Architecture 段落直接列出記憶體／儲存層、NIXL 資料路徑及 reuse-versus-transfer 適用條件
boundary: 只證實 NVIDIA 軟體架構與適用條件；不證明 CMX、SOCAMM、CXL、特定 SSD 或 remote store 已進具名客戶部署，也不表示新增層必然降低成本、等待或 GPU 數量
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C14
label: verified
status: active
claim: NVIDIA KVBM Guide 同時公開 matched tokens、device／host／disk 間 offload 與 onboard blocks、host／disk cache hit rate 等機制指標，並警告下層容量過小會反覆搬出造成 churn／效能下降，TTFT 沒改善也可能源自可重用 prefix hits 不足
supporting_source_ids: S13
contrary_source_ids:
as_of: 2026-08-12
basis: S13 的 Cache Tier Configuration、Available Metrics 與 No TTFT Performance Gain 逐項給出容量條件、指標名稱與故障排除邏輯
boundary: 這些指標能診斷 KVBM 是否真的重用與搬移資料，但不是使用者 SLO、獨立 benchmark 或 CMX 客戶採用證據；有 hit 不保證搬移收益大於排隊、網路、SSD 或重算成本
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
claim: NVIDIA 的 KV cache offloading 部署指南要求用共享長 prefix 的重複請求驗證，檢查第二次請求 TTFT 是否降低，並把 offload hit-rate 一起核對，而不是只確認 worker 已啟動或容量已配置
supporting_source_ids: S14
contrary_source_ids:
as_of: 2026-08-12
basis: S14 的 Verify 段落直接把 repeated long-prefix requests、second-request TTFT 與 offload hit-rate 放在同一驗證步驟
boundary: 重複兩次請求只是最小功能檢查，不是有樣本分布、production traffic、失敗注入、成本與長時間穩定度的完整 benchmark；TTFT 下降也未單獨隔離 memory tier 因果
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
claim: NVIDIA AIPerf 將 TTFT 定義為送出請求至第一個 token 的 client-observed 時間，包含網路、排隊、prompt processing 與第一個 token 生成；ITL 則排除初始 TTFT、以輸出 token 數正規化 decode 時間，aggregate output throughput 又是所有 concurrent requests 的整體容量，三者不能互換
supporting_source_ids: S15
contrary_source_ids:
as_of: 2026-08-12
basis: S15 的 TTFT、ITL、Output Token Throughput 與 ISL／OSL 定義直接給出時間邊界、公式、必要欄位及 per-request／aggregate 差異
boundary: 指標定義不能指出瓶頸一定在記憶體、儲存、路由、模型或網路；比較仍需固定 input／output length、負載與版本，並保留 request-level 分布、錯誤與品質
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
claim: NVIDIA 的 AIPerf 比較指南要求一次只改一個 deployment setting，維持 request shape、concurrency 與 request count 不變後重跑相同命令，再另行 sweep concurrency 找飽和點
supporting_source_ids: S16
contrary_source_ids:
as_of: 2026-08-12
basis: S16 的 Compare local configurations 段落直接列出 one-setting-at-a-time、fixed request shape／concurrency／request count 與後續 concurrency sweep
boundary: 固定這些欄位只改善同一實驗的內部可比性；若模型、資料集、prefix reuse、cache 冷熱、硬體、軟體、網路、tier size 或錯誤率未固定，仍不能把差異歸因給單一記憶體層
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C18
label: verified
status: active
claim: MLCommons 的 MLPerf Inference 規則把受測系統定義為明確的硬體與軟體資源集合，把一次 run 定義為在特定 scenario 下完成 queries、前後處理並同時滿足 latency 與 quality；規則另要求同一組結果使用一致 system／framework，且結果必須可重現
supporting_source_ids: S17
contrary_source_ids:
as_of: 2026-08-12
basis: S17 的 Definitions、General rules 與 datacenter benchmark tables 直接定義 system under test、run、quality／latency、system consistency 與 replicability
boundary: MLPerf 是一套特定公開 benchmark contract；其模型、資料集、cache 規則、scenario 與 latency target 不能自動代表私有 agent trace，也不驗證 CMX／SOCAMM／CXL 或供應商財務
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C19
label: inference
status: active
claim: 要宣稱一個 AI 記憶體或 KV cache 分層方案改善服務，至少要把受測系統與版本、模型及 input／output shape、request arrival／concurrency、prefix reuse 與 cache 冷熱、各層容量／block／eviction policy、完整搬移路徑、matched／hit／offload／onboard 機制指標，以及 TTFT／ITL／throughput／good-request／error 的 request-level 分布綁成同一份 baseline-versus-treatment 量測護照
supporting_source_ids: S12,S13,S14,S15,S16,S17
contrary_source_ids:
as_of: 2026-08-12
basis: S12／S13 固定 tier、reuse、transfer、容量與機制指標，S14 提供最小 long-prefix 驗證，S15 分開 client SLO 與 aggregate capacity，S16 要求 one-change-at-a-time 與固定 request shape，S17 再要求明確 SUT、scenario、quality、latency、system consistency 與 replicability；共同支持將欄位綁成可重建比較契約
boundary: 這是由公開文件整合的研究方法，不是單一標準或已完成客戶 benchmark；欄位齊全仍不保證代表所有 workload、證明單一硬體因果、降低 TCO、改善可靠度或形成台灣公司訂單與收入
verification_needed: 具名 production 服務用版本化 trace、同一受測系統與固定 baseline／treatment 公開上述欄位、重複 run、分位數、品質、錯誤、功耗、成本與失敗復原結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C20
label: unverified
status: active
claim: 具名客戶已在 production 服務使用 CMX、SOCAMM、CXL 或其他 host／SSD／remote KV cache tier，並依同一量測護照證明代表性 trace 的 TTFT、ITL、合格吞吐、GPU 利用、成本與故障復原都有可重現淨改善
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: S12–S17 只提供 NVIDIA 軟體能力、驗證方法、指標定義及 MLCommons benchmark governance；沒有具名客戶、同一 production trace、完整 baseline／treatment、成本與可靠度結果
boundary: 不以實驗室功能 demo、單次較低 TTFT、平均 throughput、架構支援、參考設計或未具名客戶敘述替代完整 production 證據；沒有新證據也不是反方證明
verification_needed: 客戶公開版本化 SUT、模型／trace、reuse、tier 與搬移配置、baseline／treatment、request-level 分布、quality、errors、GPU／power／cost、failure injection 與恢復結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: retired
claim_ids: C1,C2,C5
metric: Rubin 實際部署中的 HBM、SOCAMM、CMX／storage tier 配置與工作負載分工
source_ids: S1,S2
watch_source_ids: S5
frequency: weekly
frequency_detail: 每週檢查 Rubin、CMX、Dynamo／NIXL 與客戶部署更新
next_check: 2026-08-10
trigger: NVIDIA 或客戶首次公布 CMX 上線、SOCAMM 配置、KV cache placement 或各層利用率
invalidation: CMX 長期未部署、軟體不支援或客戶仍只用既有 HBM／DRAM／SSD 路徑，新增 context tier 的成熟度下修
retired_at: 2026-08-12
retirement_reason: C5 已由 C8 修正為五角色資料路徑；T1 的部署觸發經本輪 no_new_evidence 檢查後，由 T3 接續追蹤 placement 與 storage processing 的端到端結果
-->

<!-- monitoring_item
monitor_id: T2
status: retired
claim_ids: C3,C4,C6
metric: SOCAMM2 由送樣到量產、CXL 4.0 互通裝置，以及台灣公司具名產品與財務足跡
source_ids: S3,S4
watch_source_ids: S6,S7
frequency: event_driven
frequency_detail: Micron 產品公告、CXL integrators／spec 更新及台灣公司法說出現具名產品時重審
next_check: 2026-08-17
trigger: SOCAMM2 qualification／量產，CXL 4.0 主機與裝置互通，或台灣公司揭露可核對的產品與收入
invalidation: SOCAMM2 樣品延後、CXL 4.0 缺乏互通產品或台灣公司只有概念性 AI memory 敘事，個股映射維持未證
retired_at: 2026-08-12
retirement_reason: S9／S10 已命中 SOCAMM2 量產方向，但同時顯示產品家族、192GB 與 256GB 必須分開追蹤；T2 退役，由 T4 以容量型號、互通與台灣財務三條證據線接續
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C1,C2,C7,C8
metric: Rubin／CMX／BlueField-4 STX 實際部署中的資料位置、CPU 端處理、搬移路徑與端到端結果
source_ids: S1,S2,S8
watch_source_ids: S5
frequency: weekly
frequency_detail: 每週檢查 Rubin、CMX、Dynamo／NIXL、BlueField-4 STX 與具名客戶 deployment／benchmark 更新
next_check: 2026-08-19
trigger: NVIDIA 或客戶首次公布 production data path，能同時定位 HBM／SOCAMM／CMX／storage、壓縮或保護處理、搬移方式及端到端等待／利用率
invalidation: 端到端測試顯示 storage processing 或搬移抵銷容量收益、CMX／STX 未進客戶服務，或 production path 不需要新增層，五角色的商業成熟度與映射下修
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C3,C4,C6,C9,C10,C11
metric: SOCAMM2 各容量型號的送樣、資格與量產對照，CXL 4.0 互通裝置，以及台灣公司具名產品與財務足跡
source_ids: S3,S4,S9,S10
watch_source_ids: S6,S7
frequency: event_driven
frequency_detail: Micron 容量級產品公告／財報、CXL integrators／spec 更新及台灣公司法說出現具名產品時重審
next_check: 2026-08-17
trigger: 256GB 或其他具名容量出現 qualification／production，CXL 4.0 主機與裝置互通，或台灣公司揭露可雙向核對的產品、出貨與收入
invalidation: 後續文件顯示容量標示、產品世代或平台對應改變，須逐型號改寫成熟度；只有家族量產、一般 AI memory 能力或概念性受惠敘事時，公司映射維持未證
-->

<!-- monitoring_item
monitor_id: T5
status: active
claim_ids: C12
metric: BlueField-4／STX 的 KV I/O、metadata、placement、security、control 與資料搬移是否在同一 production data path 被具名驗證
source_ids: S11
watch_source_ids: S5
frequency: weekly
frequency_detail: 每週檢查 BlueField-4、STX、CMX／DOCA Memos 與具名客戶的部署、架構及端到端結果
next_check: 2026-08-19
trigger: NVIDIA 或客戶公布同一正式服務的設備配置、資料位置、控制／搬移責任、工作負載與端到端等待／利用率
invalidation: 具名部署顯示這些角色由不同元件承擔、未使用新增處理器，或端到端結果無法改善瓶頸時，圖譜的角色映射與商業成熟度下修
-->

<!-- monitoring_item
monitor_id: T6
status: active
claim_ids: C13,C14,C15,C16,C17,C18,C19,C20
metric: 同一 AI memory／KV cache tier 方案的 workload、reuse、tier configuration、data path、機制指標與使用者 SLO baseline-versus-treatment
source_ids: S12,S13,S14,S15,S16,S17
watch_source_ids: S12,S13,S14,S15,S16,S17
frequency: monthly
frequency_detail: 每月檢查 Dynamo／AIPerf／MLPerf 規則更新與具名 operator 的 production KV tier benchmark；重大 deployment 或 methodology 變更時提前重審
next_check: 2026-08-31
trigger: 具名客戶以版本化 SUT 與 production trace 公開固定 request shape／load／reuse／tier／path 的 baseline／treatment，並同時給 request-level TTFT／ITL／goodput／errors、mechanism counters、品質、成本及 failure-recovery
invalidation: 新版工具或 production 證據顯示目前八格仍遺漏會改變結論的 cache state、routing、network、quality、power、reliability 或成本欄位；屆時追加新 claim 縮窄 C19，不回寫舊量測護照
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **圖形運算晶片（GPU）**：負責大量平行運算的晶片。本文把它當成最靠近正在運算資料的位置，不代表所有人工智慧工作都只在這裡完成。
- **中央處理器（CPU）**：負責一般運算與系統協調的晶片。本文討論的系統記憶體放在它的一側，與 GPU 旁的高速記憶體分工。
- **頻寬**：單位時間內可以搬動多少資料。頻寬高不代表容量一定大，也不代表產品已量產。
- **延遲／等待時間**：提出資料要求到取得資料之間的時間。等待時間短與總容量大是兩個不同問題。
- **容量**：一個位置能存放多少資料。容量較大不表示存取一定較快。
- **持久性**：斷電或工作結束後，資料是否仍需保留。需要長期保存的資料通常不必一直占用最靠近晶片的位置。
- **共享性**：同一份資料能否供多個運算工作或設備使用。共享方便不等於存取速度與近端記憶體相同。
- **近端高速記憶體（HBM）**：貼近 GPU、以高頻寬服務正在運算的資料；速度高，但容量與成本受到封裝位置限制。
- **第四代高頻寬記憶體（HBM4）**：HBM 的下一個世代，本文指 Vera Rubin 平台在 Rubin GPU 旁配置的版本。
- **系統記憶體（system memory／RAM）**：CPU 可直接使用的工作空間，容量角色與 GPU 旁的高速記憶體不同。
- **中央處理器記憶體模組（SOCAMM）**：以低功耗 DRAM 做成的可維護模組，放在 CPU 系統記憶體一側，重點偏向容量、功耗與機架密度。
- **第二代 SOCAMM（SOCAMM2）**：一個包含不同容量型號的產品家族。Micron 明列 192GB 已量產，較早的 256GB 公告則只到客戶送樣；家族名稱本身不能替每個容量決定成熟度。
- **鍵值快取（KV cache）**：模型推論時保存先前文字片段的中間結果，避免每一步都重新計算全部上下文。
- **前綴重用（prefix reuse）**：不同請求前段有相同 token 時，系統重新使用先前算好的 KV block；沒有足夠重複內容，即使多一層容量也可能只增加搬移。
- **冷快取／熱快取（cold／warm cache）**：冷快取表示測試開始時沒有可直接重用的內容；熱快取表示先前請求已留下可命中的資料。兩種起點不能混成同一成績。
- **快取命中率（cache hit rate）**：需要的資料已在可重用位置而不用重新計算的比率；命中高只證明機制有工作，不等於搬回速度與整體服務一定更好。
- **首字等待時間（TTFT）**：請求送出到收到第一個 token 的時間，會同時包含網路、排隊、prompt processing 與第一個 token 生成，不是單獨的記憶體速度。
- **逐字等待時間（ITL）**：第一個 token 之後，連續生成 token 的平均間隔；它把初始 TTFT 排除，因此不能和 TTFT 或總 request latency 混用。
- **合格吞吐（goodput）**：在預先定義的等待、錯誤與品質門檻內完成的工作量；若只算成功留下來的快請求、把逾時或錯誤丟掉，吞吐會看起來過度樂觀。
- **基準組／處理組（baseline／treatment）**：基準組保留原配置，處理組只改一個待驗因素；若模型、負載、快取狀態與硬體同時變動，就無法知道差異來自哪裡。
- **鍵值區塊管理器（KVBM）**：NVIDIA Dynamo 用來管理、重用及在 GPU、主機記憶體與儲存間搬移 KV block 的軟體元件；軟體支援不等於客戶已部署。
- **人工智慧效能量測工具（AIPerf）**：NVIDIA 用來對推論服務產生請求並量測等待、吞吐與錯誤的工具；工具給的是量法，不保證測試負載具代表性。
- **機器學習效能推論基準（MLPerf Inference）**：MLCommons 維護的公開 benchmark 規則與結果制度；它有固定模型、資料、情境與通過條件，不能直接代表私有工作負載。
- **受測系統（SUT）**：本次結果涵蓋的完整硬體與軟體集合；少寫一段網路、儲存或版本，就可能把結果錯歸給另一個元件。
- **服務目標（SLO）**：服務事先承諾要達到的等待、錯誤、品質或可用條件；不是測完後才挑一個最好看的門檻。
- **輸入／輸出序列長度（ISL／OSL）**：一次請求送入與產生的 token 數；長度不同會改變 prompt processing、decode 時間與可重用資料量。
- **共享上下文層（Context storage／CMX）**：NVIDIA 為可重建、又在意等待時間的鍵值快取設計的共享位置，介於本機記憶體與一般共享儲存之間。
- **固態硬碟（SSD）**：使用快閃記憶體保存資料的儲存裝置；容量通常比近端記憶體大，但存取較慢。
- **本機儲存（local storage）**：直接放在同一台伺服器內的儲存位置，通常比機房共享儲存更靠近運算。
- **共享儲存（shared storage）**：可由多台伺服器共同使用的儲存位置；適合共享或長期保存，不等於近端高速記憶體。
- **Vera Rubin 平台**：NVIDIA 下一代平台名稱；Rubin 是 GPU、Vera 是 CPU。代號只表示產品世代，不表示已量產或已出貨。
- **資料層（tier）**：依資料用途、速度與容量把存放位置分組；本文的層級不是產品優劣排行榜。
- **G1–G4 與 G3.5**：NVIDIA 在 CMX 文章裡把資料存放位置由近到遠編成 G1 到 G4；新增的 CMX 位於 G3 與 G4 之間，因此稱 G3.5。這不是產業共通標準。
- **資料放置（placement）**：決定一份資料目前應放在哪一層，以及何時移動。軟體能做放置決策，不代表客戶已正式部署。
- **工作集（working set）**：一段工作期間會反覆用到的資料集合。工作集有多大、多久再用一次，會影響資料是否值得留在較近的位置。
- **重新計算成本**：資料沒有保留時，從原始輸入再算一次所需的時間與運算資源。可以重建不代表重建一定便宜。
- **搬移成本**：把資料從一層送到另一層所占用的時間、連接頻寬與系統資源。遠端容量較大，不代表搬過去必然划算。
- **控制決策**：判斷資料何時、往哪裡移動的規則。本文把 Dynamo／KV block manager 放在這個角色，不把它和實際承載資料的記憶體或儲存混為一談。
- **資料搬運**：依控制決策真正讀取、傳送與寫入資料的動作。NIXL 提供跨多種記憶體與儲存位置的搬移介面，但介面存在不等於每次搬移都更快。
- **儲存資料處理**：資料在寫入、讀回或故障復原途中可能要壓縮、加密、檢查完整性或重建。這些工作由處理器執行，媒體容量與連接速度不會自動回答它是否成為瓶頸。
- **BlueField-4 STX**：NVIDIA 把 Vera CPU、SOCAMM2 與儲存資料處理放在一起的產品架構名稱。本文只採用其資料路徑與測試邊界；STX 列名不等於客戶已部署或完整系統較快。
- **端到端測試**：把應用、處理器、記憶體、軟體、網路與儲存裝置放在完整路徑一起量。只在記憶體內測一個演算法，不能替整套系統背書。
- **一致性記憶體互連（CXL）**：讓處理器、記憶體擴充裝置與加速器維持一致記憶體視圖的開放連接標準。
- **CXL 4.0**：CXL 的公開規格版本；規格發布不等於主機與裝置已完成互通或形成收入。
- **記憶體擴充（memory expansion）**：透過外接裝置增加處理器可使用的記憶體容量，不等於把所有資料移到同一位置。
- **快取一致性（cache coherence）**：多個處理器或裝置看到同一份資料時，能維持相容狀態的機制；有規格不等於產品已互通。
- **客戶送樣（customer sampling）**：供應商把樣品交給客戶測試的階段；仍不能當成認證完成、量產或收入。
- **資格認證（qualification）**：客戶或平台確認產品符合要求的流程；通過認證仍需另外確認量產與採購。
- **量產（production）**：產品進入穩定製造與交付階段；量產不會自動揭示客戶數、供應份額或獲利。
- **互通（interoperability）**：不同廠商的主機、連接元件與記憶體裝置能按同一規格共同運作。
- **交換器與訊號重整器（switch／retimer）**：前者分配連接路徑，後者整理高速訊號；列入規格不代表已通過整套互通測試。
- **Dynamo**：NVIDIA 開源的推論服務軟體；它可協調模型運算，但軟體存在不等於 CMX 已被客戶部署。
- **NIXL**：協助不同記憶體與儲存位置搬移資料的軟體函式庫；它回答「資料怎麼移動」，不直接回答哪一層會形成收入。

### 三句話抓重點

- 人工智慧系統不會把所有資料都塞在同一個地方：正在運算、最怕等待的資料放近晶片，容量較大或可以重新建立的資料則放遠一些。
- 在 Vera Rubin 平台裡，圖形運算晶片旁使用高頻寬記憶體（HBM4），中央處理器旁使用系統記憶體（SOCAMM）；兩者負責的資料位置不同。
- NVIDIA 提出共享上下文層（CMX）；Micron 明列 192GB 第二代 SOCAMM 已量產，較早的 256GB 公告只說客戶送樣。架構、容量型號、樣品、量產與收入必須分開判讀。

### 為什麼重要

如果看到人工智慧資料量增加，就直接把全部需求算到同一種高速記憶體，會漏掉中央處理器旁的
系統記憶體、可共享的上下文層與固態硬碟，也可能把同一份資料重複計算。先分清每一層處理哪種
資料，再比較頻寬、容量、等待時間、保存需求與共享方式，最後才檢查供應商是否已從樣品走到
量產與收入。

### 接下來怎麼追

- 追第二代 SOCAMM 時逐一記錄容量型號：192GB 的量產不能自動替 256GB 或整個 48GB–256GB 產品組合升級成熟度。
- 追共享上下文層是否由參考架構進入具名客戶部署，以及 Dynamo／NIXL 是否實際管理鍵值快取的放置與移動。
- 比較任何分層結果時，固定模型、輸入／輸出長度、請求到達、前綴重用、冷熱快取、各層容量與搬移路徑，並同時核對命中／搬移指標與 request-level TTFT、ITL、合格吞吐、錯誤及品質。
- 追 CXL 4.0 是否出現主機、交換器、訊號重整器與記憶體裝置的互通清單，而不是只有規格版本。

### 想一想

- 如果把一份可以重新建立的暫存資料移到較遠的位置，省下的會是近端空間、設備成本，還是運算等待時間？需要哪些不同數據驗證？
- 如果中央處理器旁的系統記憶體出貨成長，圖形運算晶片旁的高速記憶體也同步成長，這代表互相替代，還是平台把資料分配到不同位置？

## 先按資料的急迫程度分四層

| 資料任務 | 本文怎麼分位置 | 為什麼放這裡 | 本輪產品名稱 | 目前不能因此判定 |
|---|---|---|---|---|
| 正在計算、最怕等待的工作資料 | 圖形運算晶片旁的近端高速記憶體 | 優先縮短等待時間並提高資料搬運量 | HBM4 | 供應商份額、採購量與台灣公司收入 |
| 容量較大、仍需快速取用的系統資料 | 中央處理器旁的系統記憶體 | 補足容量並維持處理器可直接取用 | SOCAMM／SOCAMM2 | 各容量型號的認證／量產、客戶數與財務貢獻 |
| 可以重新建立、也可能需要共享的上下文資料 | 介於本機記憶體與一般共享儲存之間 | 避免長時間占用較昂貴的近端空間 | CMX／鍵值快取 | 具名客戶部署、實際利用率與獨立成本效益 |
| 容量最大、可接受較慢存取或需長期保存的資料 | 本機固態硬碟與機房共享儲存 | 優先取得容量、保存與共享能力 | SSD／共享儲存 | 是否取代近端記憶體，以及哪家供應商會形成收入 |

CXL 是連接處理器、記憶體擴充裝置與加速器的路徑，不是第五種資料層。把產品新聞連到公司以前，
要先確認它服務哪一層、資料如何移動，以及目前只走到送樣、資格認證、量產，還是已出現可辨識
的財務貢獻。

## 分層不是靜態樓層：還要分清介質、處理、連接、搬運與決策

把 HBM、SOCAMM、CMX、SSD 與 CXL 全畫成並排產品，會看不出它們其實在回答不同問題。研究時可先
拆成五個角色：資料放在哪裡、途中做哪些處理、沿什麼路徑走、誰執行搬運，以及誰決定何時搬。只有五個角色能接成
一條可運作的鏈，分層才不只是硬體清單。

| 角色 | 本篇例子 | 它回答的問題 | 最容易誤判成什麼 |
|---|---|---|---|
| 存放介質 | HBM、system RAM／SOCAMM、CMX、local SSD、shared storage | 資料此刻在哪裡，能容納多少、要保存多久 | 容量大的介質一定比較快，或新增一層就會全面取代舊層 |
| 資料處理 | Vera／BlueField-4 STX 文件所述的壓縮、加密、完整性與復原 | 資料在讀寫或重建途中還要做哪些工作 | 處理器 microbenchmark 較快就等於 SSD、網路、GPU 與完整系統都更快 |
| 連接路徑 | CXL，以及平台既有的記憶體、儲存與網路路徑 | 哪些處理器與裝置能互相看見或交換資料 | 規格發布就等於所有主機、交換器與裝置已互通 |
| 搬運工具 | NIXL 等資料移動介面 | 實際如何把資料由來源送到目的地 | 軟體支援某路徑就等於客戶已上線，或搬移沒有額外成本 |
| 控制決策 | Dynamo、KV block manager 與資料放置規則 | 哪份資料何時留近、移遠、取回或重建 | 有排程器就代表已找到所有工作負載的最佳答案 |

這五個角色也對應不同供應鏈證據。記憶體公司可以證明介質與模組進度，處理器文件可以界定資料服務，
控制器或互連公司可以證明連接能力，軟體文件可以證明支援的搬移路徑，系統商與客戶部署才有機會證明整條鏈真的上線。任一段
缺證據，都不能從另一段的產品公告代填。

## 一個可驗證的資料放置迴路

把分層想成圖書館，比想成速度排行榜更接近問題本身：熱門書放在伸手可及的位置，偶爾使用的書移到
較遠書庫；但系統還需要知道哪些書熱門、搬一次要多久，以及讀者等不等得起。研究一個分層方案時，
至少要能重建下面六步：

1. **辨認資料**：先分清正在運算的工作資料、CPU 端緩衝、可重建的 KV cache，或必須保存的資料。
2. **判斷急迫性**：問它多久會再被使用、能否重新計算、是否需要多人共享，以及遺失後是否必須復原。
3. **選擇位置**：在近端空間、容量、保存與共享需求之間取捨，而不是只選規格表上最快的產品。
4. **處理資料**：確認讀寫途中是否還要壓縮、加密、驗證或重建，以及這些工作由哪顆處理器承擔。
5. **執行搬移**：確認資料實際經過哪條連接與軟體路徑；搬移會占用時間與頻寬，不能當成免費動作。
6. **回看結果**：用使用者等待時間、GPU 閒置、快取重用、搬移量與失敗復原等結果檢查決策是否值得。

現有 NVIDIA 文件支持「不同層存在，放置、搬移、metadata 與資料保護是不同工作」這個架構；7 月 16 日
文件把 KV I/O、metadata、placement、security、control 與資料搬移分開，8 月 3 日的新文件再把壓縮、
加密、完整性與復原放進 CPU 端儲存資料路徑。不過後者明示測試資料已在記憶體，
排除檔案 I/O、磁碟、網路、啟動與外部裝置，仍沒有統一客戶工作負載的完整六步結果。因此這裡是一套
驗證問題，不是對 CMX／STX 成本效益或客戶採用的宣稱。

## 再用八格量測護照判斷「多一層」有沒有真的更好

新增一層記憶體或儲存空間，只證明容量與路徑存在；要說它改善服務，還要證明可重用資料真的命中、
搬移沒有吃掉收益，而且使用者端結果在相同負載下變好。NVIDIA 現行 KVBM 文件直接把適用條件寫成
「重用收益要大於搬移成本」，也警告下層容量太小可能反覆搬出、造成 churn 與效能下降。[S12][S13]
因此每一個百分比或倍數，至少先補齊下面八格：

| 八格量測護照 | 要固定什麼 | 要保存什麼 | 少了最容易誤讀成 |
|---|---|---|---|
| 1. 受測系統與版本 | 模型／權重、精度、GPU／CPU／記憶體／SSD／網路數量，推論引擎、router、connector、driver 與軟體版本 | 完整硬體、韌體、軟體、拓撲與設定檔 | 換了模型、引擎或網路，卻把全部差異算給 memory tier |
| 2. 請求形狀與資料 | input／output token 長度、context、資料集、session turns 與正確答案／品質門檻 | 每筆 ISL／OSL、資料來源、tokenizer、品質結果與早停條件 | 短 prompt、少輸出或品質下降，被誤寫成系統更快 |
| 3. 到達與併發負載 | request rate、arrival pattern、concurrency、request count／duration、warm-up 與超時 | 實際到達時間、在途請求、queue、完成／取消／錯誤數與飽和點 | 單人延遲與多人總吞吐混在一起，或只比較不同壓力 |
| 4. 重用機會與冷熱起點 | prefix overlap、重複頻率、cold／warm cache、跨 worker／session sharing 與 routing policy | matched tokens、各層 hit rate、miss、eviction、重算量及每次請求是否可命中 | 先跑過的熱資料勝過冷基準，卻被當成硬體本身更快 |
| 5. 各層容量與政策 | GPU、host、SSD、remote tier 容量，block size、write policy、filter、eviction 與預取 | 各層 occupancy、配置值、block lifecycle、容量不足與 churn | 只寫「有 100GB cache」，沒有回答能否承接上層與如何汰換 |
| 6. 完整資料路徑 | source／destination、prefill／decode、NIXL／RDMA／filesystem／object store、NIC／switch 與距離 | 每段傳輸量、方向、等待、頻寬、拓撲、網路與 storage errors | 只量 CPU 或記憶體內路徑，替 SSD、網路與遠端服務背書 |
| 7. 機制是否真的發生 | reuse、offload、onboard、prefetch、recompute 與 route decision | matched tokens、device→host／disk 與 host／disk→device blocks、hit rate、失敗及重試 | TTFT 變了就假定是 offload；其實可能根本沒命中或沒搬回 |
| 8. 使用者結果與代價 | baseline／treatment 只改一項；同時量 latency、capacity、quality、errors、power、cost 與 recovery | TTFT／ITL／request latency／throughput／good-request 的 p50／p90／p99、重複 run、品質、功耗、成本與故障復原 | 只挑平均或最高吞吐，掩蓋尾端等待、掉單、品質或成本惡化 |

這八格不是產業標準，也不是要求每個公開新聞稿都交付完整實驗。它是一張研究護照：缺哪一格，就把
那一格列為 boundary，不用另一個漂亮數字代填。NVIDIA 的最小部署檢查只要求送出共享長 prefix 的
重複請求，確認第二次 TTFT 與 offload hit-rate；這能證明功能路徑有機會工作，仍不是有 production
trace、request distribution、品質、成本與故障復原的完整比較。[S14]

比較基準與處理組時，NVIDIA 的 AIPerf 指南要求一次只改一個 deployment setting，固定 request
shape、concurrency 與 request count，再另外 sweep concurrency 找飽和點。[S16] MLCommons 的規則
則把 hardware／software 合成明確的 system under test，要求同一組結果維持相同 system／framework、
同時滿足 scenario 的 latency 與 quality，且可重現。[S17] 兩套方法的用途不同，但共同提醒：
「測了哪套系統、用什麼負載、什麼算通過」必須先固定，才有資格比較。

## 一個 TTFT 數字不能替整條資料路徑背書

同一個服務可以首字更快、後續逐字更慢，也可以總吞吐提高但尾端請求逾時更多。AIPerf 把這些欄位
分開，正好能用來檢查分層敘事是否把不同分母混在一起：[S15]

| 指標 | 它回答什麼 | 為什麼要和其他欄一起看 | 不能直接證明 |
|---|---|---|---|
| TTFT | 使用者送出請求後多久看到第一個 token | 它包含網路、排隊、prompt processing 與第一個 token；prefix reuse 可能改善它，但也可能被 queue 或 routing 改變 | 單一 memory tier 的延遲、SSD 速度或整個 decode 都改善 |
| ITL | 第一個 token 後，平均多久產生下一個 token | 它排除 TTFT，且受 output length 影響；要與相同輸出長度、decode duration 一起比較 | 首字體驗、總 request latency 或整體系統容量 |
| Aggregate output throughput | 所有 concurrent requests 合計每秒產生多少 token | 併發越高可能提高總量，也可能讓單一使用者與尾端請求等待變長 | 每位使用者更快、SLO 達標或 dropped requests 不存在 |
| Matched／hit／offload／onboard | 可重用資料是否被找到，以及 block 是否真的搬出、搬回 | 這是機制證據，要和 TTFT／ITL／errors 同一時間窗對帳 | 搬移收益大於成本、服務品質改善或客戶願意採用 |
| Good-request／errors／quality | 有多少嘗試請求在預定 SLO 與品質內完成 | 錯誤與逾時要留在分母，避免只看存活的快請求；品質也不能為速度讓路 | TCO、可靠度、電力與所有 production workload 都改善 |

截至本輪，公開文件足以建立這張護照與觀測欄位，卻沒有具名客戶以同一 production trace 對 CMX、
SOCAMM、CXL 或其他 host／SSD／remote KV tier 公開完整 baseline／treatment。因此本文只把量測方法
升為可驗證框架，不把功能 demo、平均 TTFT 或軟體支援升為商用部署、硬體需求與供應商收入。

## 先問工作負載，再問該買哪一種記憶體

同一份資料在不同使用情境下，合理位置可能不同。下表不是自動配置規則，而是把產品新聞翻譯成可查證
問題的起點。

| 要先問的問題 | 若答案偏高，研究上傾向關注 | 仍要補的證據 |
|---|---|---|
| 很快會再次使用，而且每次等待都會卡住運算嗎？ | 較近、較高頻寬與較低等待時間的位置 | 實際重用間隔、命中率、等待時間與 GPU 閒置 |
| 資料量是否大到會擠壓近端空間？ | system RAM、context tier 或 storage 的分擔方式 | 容量配置、搬移量、取回時間與近端空間真正省下多少 |
| 資料可以重建嗎？ | 比較「保留後取回」與「直接重算」 | 重建時間、搬移時間、失敗率與兩條路徑的完整成本 |
| 多個工作或節點需要共享嗎？ | 共享 context／storage 或一致性連接路徑 | 同時使用者、資料一致性、互通與存取衝突 |
| 工作結束或斷電後仍要保留嗎？ | SSD 或 shared storage 等持久層 | 保存期限、復原目標、資料完整性與安全要求 |
| 工作負載會隨時間改變嗎？ | 動態 placement、監測與重新配置能力 | 誰量測、誰決策、多久調整一次，以及調整是否造成抖動 |

這套問法可以避免兩個相反錯誤：一是把所有資料成長都算成 HBM；二是因為遠端容量便宜，就假設所有
資料都應移遠。真正的分界不是產品名稱，而是工作集、再使用時間、重建成本、共享需求與搬移代價。

## 用一份 KV cache 看懂資料如何旅行

以下是閱讀架構文件時可套用的抽象流程，不代表每個客戶都採用相同實作：

1. 模型處理請求後產生可供後續步驟重用的 KV cache，先占用運算附近的空間。
2. 控制決策判斷哪些內容仍很急、哪些可以移到 system RAM、CMX、local SSD 或 shared storage。
3. 搬運工具沿可用路徑把資料移走，並保留之後能定位與取回它所需的資訊。
4. 後續請求需要同一內容時，系統比較取回與重新計算；如果取回太慢，省下的近端容量可能換來更長等待。
5. 只有實際部署揭露命中、搬移、等待與資源利用，才能判斷新增層是在解決瓶頸，還是把瓶頸移到別處。

因此「可卸載 KV cache」只證明一條技術路徑；「卸載後整體更划算」仍需客戶工作負載與完整系統結果。

## 新手最常混在一起的六件事

- **容量與頻寬**：能放更多資料，不代表每秒能搬更多資料。
- **頻寬與等待時間**：總搬運量高，不代表每一次小請求都更快拿到資料。
- **規格與互通**：CXL 版本存在，不代表主機、交換器、retimer、記憶體裝置與軟體已一起通過驗證。
- **支援與部署**：Dynamo／NIXL 支援某種放置或搬移，不代表客戶已在正式服務使用。
- **釋放空間與取代產品**：把部分可重建資料移出 HBM，可能讓 HBM 留給更急的資料；這不等於 storage 取代 HBM。
- **元件測試與整體結果**：處理器在記憶體內完成資料服務的測試，不等於含 SSD、網路、軟體與 GPU 的端到端路徑已驗證。

## 在研究中心裡接著怎麼學

- 先讀本篇建立「資料層 × 資料處理 × 連接 × 搬運 × 決策」框架。
- 再讀〈高頻寬記憶體可以客製到哪裡：先分規格、底部晶片與工作搬移〉，理解最靠近運算的記憶體如何再按客製範圍與商用階段拆開。
- 接著讀〈AI 儲存不是容量越大越好：先分清餵資料、保存進度與搬模型〉，把較遠的 storage 路徑放回資料生命週期。
- 最後讀〈PCIe 6 元件寫著第六代，不代表整套系統已通過：先分清裝置、連線、正式測試與部署〉與〈資料從一顆運算晶片走到另一顆：先分清機架內外，再判斷跨廠互通〉，學會把規格、retimer／switch、互通、系統與部署逐級驗證。

五篇文章合起來回答一條完整問題：資料是什麼、現在放在哪裡、經什麼路徑移動、誰做決策，以及哪一級
證據才足以建立供應鏈與財務連結。

## 四層互補，不是誰取代誰

同一套 Vera Rubin 平台已把兩種記憶體放在不同位置：圖形運算晶片旁使用 HBM4，中央處理器旁
使用 SOCAMM。NVIDIA 的另一份文件再把上下文資料分配到近端記憶體、系統記憶體、本機固態硬碟、
共享儲存與新增的 CMX 位置。這些位置服務不同的等待時間與容量條件，不能排成單一優劣名次。

Micron 的文件讓 SOCAMM2 產品進度再往前一步，但必須拆成容量型號：192GB 明列量產，256GB 的較早
文件只列客戶送樣，後續產品家族文件也沒有逐一對照容量。CXL 4.0 則只提供記憶體擴充的公開連接規格。
現有證據沒有支持把其中任何一層直接寫成 HBM 的全面替代，也沒有支持把平台配置直接換算成台灣公司收入。

## 同一家族也要拆到容量型號：192GB 與 256GB 不是同一個時鐘

產品新聞常把「家族名稱」與「其中一個型號」放在同一句，讀者很容易把最高成熟度套給全部產品。
SOCAMM2 正好示範為什麼要再拆一層：

| 文件層級 | 文件實際說了什麼 | 可以寫成 | 不能順手升級成 |
|---|---|---|---|
| 具名容量：192GB | Micron 3 月 16 日明列 high-volume production | Micron 表示 192GB SOCAMM2 已量產 | 48GB–256GB 每個容量都已量產 |
| 具名容量：256GB | Micron 3 月 5 日明列 customer sampling | 當時 256GB 已送樣 | 256GB 已通過資格認證、量產或形成收入 |
| 產品家族 | Micron 6 月 24 日表示 LP5X SOCAMM2 products 已量產，並擴展多個容量點 | 產品家族已有量產進展與多容量選項 | 未被逐一點名的容量都處在同一階段 |
| 客戶與財務 | 三份文件沒有 SOCAMM2 的客戶分母、容量別出貨、收入或毛利 | 保留為下一份證據 | 用公司總營收或平台名稱估算 SOCAMM2 貢獻 |

因此「SOCAMM2 已量產」與「256GB SOCAMM2 曾只到送樣」不互相矛盾：前者的主詞較寬，後者綁定
特定容量與日期。研究帳本要保存兩句話的主詞、時間與成熟度，而不是用較新的家族敘述覆寫較精確的
容量記錄。下一次若文件明列 256GB qualification 或 production，再只更新 256GB 的時鐘。

## 每一層的商業進度要各自驗證

| 資料層或連接路徑 | 已看到的一手證據 | 目前走到哪一步 | 還缺哪些商業證據 |
|---|---|---|---|
| 圖形運算晶片旁的高速層（HBM4） | Vera Rubin 平台明列 GPU 使用 HBM4 | 平台規格 | 各供應商份額、採購量與台灣公司收入 |
| 中央處理器旁的系統記憶體（SOCAMM） | 平台明列系統記憶體；Micron 明列 192GB 量產、256GB 較早送樣，另稱產品家族已有多容量量產進展 | 容量型號分別位於量產與送樣；家族層已有量產 | 逐容量資格／出貨、客戶數、供應份額與財務貢獻 |
| 共享上下文層（CMX） | NVIDIA 提出 G3.5 架構與資料放置軟體 | 架構與軟體設計 | 具名客戶上線、實際利用率與獨立成本效益 |
| CPU 端儲存資料處理 | NVIDIA 以 Vera／BlueField-4 STX 測量壓縮、加密、完整性、復原與組合路徑 | 公司架構與記憶體內 microbenchmark | 含檔案 I/O、SSD、網路、軟體、GPU 的端到端結果與具名客戶部署 |
| 記憶體擴充連接（CXL 4.0） | 公開規格已發布 | 公開標準 | Vera Rubin 是否採用 4.0、互通裝置與量產收入 |

## 來源與證據邊界

- [NVIDIA Vera Rubin architecture](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/)（HBM、SOCAMM 與 CXL 版本）。
- [NVIDIA CMX context memory](https://developer.nvidia.com/blog/introducing-nvidia-bluefield-4-powered-inference-context-memory-storage-platform-for-the-next-frontier-of-ai/)（G1–G4／G3.5 分層）。
- [Micron 256GB SOCAMM2](https://investors.micron.com/news-releases/news-release-details/meiguangtuichuquanqiushoukuangaorongliang256gb-lpdram)（customer sampling 與內部測試邊界）。
- [Micron 192GB SOCAMM2 production](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin)（192GB high-volume production 與 48GB–256GB 產品組合邊界）。
- [Micron fiscal 2026 Q3 product highlights](https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-record-results-third-quarter)（SOCAMM2 產品家族量產與多容量選項，但未逐容量列示）。
- [CXL 4.0 specification release](https://computeexpresslink.org/wp-content/uploads/2025/11/CXL_4.0-Specification-Release_FINAL_Website-Copy.pdf)（規格與功能範圍）。
- [NVIDIA BlueField data path](https://developer.nvidia.com/blog/scaling-agentic-ai-factories-through-extreme-co-design-with-nvidia-bluefield/)（KV I/O、metadata、placement、security、control 與資料搬移角色）。
- [NVIDIA Vera／BlueField-4 STX storage processing](https://developer.nvidia.com/blog/nvidia-vera-storage-benchmarks-faster-encryption-compression-integrity-checking-and-recovery-for-ai-native-storage/)（CPU 端資料服務與明示的非端到端測試邊界）。
- [NVIDIA Dynamo KVBM architecture](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/kvbm/overview)（GPU、host、SSD、remote storage 與 reuse-versus-transfer 適用條件）。
- [NVIDIA Dynamo KVBM guide](https://docs.nvidia.com/dynamo/latest/user-guides/kv-cache-offloading)（tier sizing、matched／offload／onboard／hit-rate 指標與 churn 反例）。
- [NVIDIA KV cache offloading verification](https://docs.nvidia.com/dynamo/dev/kubernetes/kv-cache-offloading/overview)（共享長 prefix、第二次 TTFT 與 hit-rate 的最小功能檢查）。
- [NVIDIA AIPerf metrics](https://docs.nvidia.com/aiperf/reference/ai-perf-metrics-reference)（TTFT、ITL、request distribution、throughput、ISL／OSL 與 good-request 分母）。
- [NVIDIA AIPerf comparison guide](https://docs.nvidia.com/dynamo/dev/cli/operations/benchmarking-with-ai-perf)（一次只改一項、固定 request shape／concurrency／request count 與 saturation sweep）。
- [MLCommons MLPerf Inference rules](https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc)（system under test、scenario、latency／quality、system consistency 與 replicability）。

Micron 的效能、功耗與尺寸數字來自公司內部測試；NVIDIA 的 CMX 效率亦是平台主張。本篇
不把它們當成跨公司可比 benchmark，也不推估產品 TAM、供應商份額或市場定價。

## 影響路由

<!-- impact
group_id: memory
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-17
rationale: HBM、LPDRAM／SOCAMM、NAND／SSD 與 memory expansion 形成不同產品路由，但目前沒有 universe 公司具名 SOCAMM／CMX／CXL 4.0 曝險
evidence_boundary: 一般 DRAM、NAND、控制 IC 或模組能力不證明已進 Rubin 分層或取得新增訂單
-->

<!-- impact
group_id: serverodm
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-17
rationale: 新的 CPU memory、context storage 與 CXL 裝置會增加系統整合問題，值得追蹤具名 Rubin／CMX 機櫃配置
evidence_boundary: ODM 能組裝 AI 伺服器不等於已取得 CMX、SOCAMM 或 CXL 4.0 訂單與財務貢獻
-->

## 下一個可證明／否定的節點

- Micron 或其他供應商逐一公布 256GB 與其他 SOCAMM2 容量的 qualification／production、平台與出貨邊界，不再只用產品家族總稱。
- NVIDIA 或客戶公布 CMX 實際上線、KV cache placement、容量與利用率，而非只有參考架構效能主張。
- NVIDIA 或客戶公布 BlueField-4 STX 的 production data path，將 CPU 端資料處理與 SSD、網路、軟體、GPU 的端到端 SLO 對上。
- 具名客戶用同一 production trace 與版本化 SUT 公開 memory／KV tier baseline-versus-treatment，固定模型、request shape、load、reuse、cache 冷熱、tier policy 與 data path，並同時交代 request-level TTFT／ITL／goodput／errors、mechanism counters、品質、成本、功耗與 failure recovery。
- CXL Consortium 出現 4.0 integrators／compliance 清單，能核對 host、switch、retimer 與 memory device。
- 台灣公司以具名產品與客戶文件雙向核對量產、收入及毛利；否則公司節點維持待驗證或不入圖。
