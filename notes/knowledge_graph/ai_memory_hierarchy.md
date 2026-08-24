# AI 記憶體分層知識圖譜

本圖將 HBM、SOCAMM、KV cache、context storage 與 CXL 放回各自的系統位置，也把 model-visible
context、可重算 KV 中間結果與跨 session Agent 狀態拆開。公司線把 Micron／SK hynix 的 192GB
量產聲明與 Micron 256GB 送樣分成容量與供應商時鐘；機制線另把 cache 命中／搬移、狀態生命週期與使用者服務結果分開。
沒有客戶與財務資料前，仍不把一般記憶體或持久化需求畫成台灣公司受惠。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: ai-memory-hierarchy
root_node_id: concept:ai-memory-hierarchy
label: AI 記憶體分層
summary: 以介質、處理、連接、搬移、放置決策與量測契約拆開 AI 資料路徑，把 context window、可重算 KV cache、跨 session Agent 狀態與使用者 SLO 分開；192GB 已有 Micron 與 SK hynix 兩條供應商量產聲明，但 mixed-source qualification、採購量與財務仍未證實。
article_ids: MI-2026-08-02-AI-MEMORY-HIERARCHY
status: active
-->

<!-- knowledge_edge
edge_id: KG-MEM-C01
view: company
from_id: company:nvidia
to_id: concept:ai-memory-hierarchy
relation: integrates
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C1,MI-2026-08-02-AI-MEMORY-HIERARCHY#C2,MI-2026-08-02-AI-MEMORY-HIERARCHY#C12
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-16
review_due: 2026-08-19
status: active
boundary: NVIDIA 已在 Rubin／CMX／BlueField 架構中分層 HBM、system memory、context storage、placement 與資料搬移；不等於客戶已部署 CMX／STX、各角色利用率已驗證或供應商收入可辨識。
next_trigger: NVIDIA 或客戶公布 Rubin／CMX／STX 實際上線、容量配置、placement／搬移責任與端到端利用率。
-->

<!-- knowledge_edge
edge_id: KG-MEM-C02
view: company
from_id: company:micron
to_id: concept:ai-memory-hierarchy
relation: samples
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C3
note_refs:
evidence_state: verified
commercial_stage: sample
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-05
review_due: 2026-08-17
status: active
boundary: Micron 256GB SOCAMM2 已進入 customer sampling，不是 qualification 完成、量產、客戶採購量或財務貢獻。
next_trigger: Micron 將 256GB SOCAMM2 升級為 qualification／production 並提供平台與出貨邊界。
-->

<!-- knowledge_edge
edge_id: KG-MEM-C03
view: company
from_id: company:micron
to_id: concept:ai-memory-hierarchy
relation: produces
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C9,MI-2026-08-02-AI-MEMORY-HIERARCHY#C10
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-24
review_due: 2026-08-17
status: active
boundary: Micron 明列 192GB SOCAMM2 量產，並在後續產品更新表示 SOCAMM2 家族已有多容量量產進展；沒有逐容量清單、客戶分母、供應份額或 SOCAMM2 財務貢獻。
next_trigger: Micron 逐一公布 256GB 與其他容量的 qualification／production、平台、出貨與財務邊界。
-->

<!-- knowledge_edge
edge_id: KG-MEM-C04
view: company
from_id: company:sk-hynix
to_id: concept:ai-memory-hierarchy
relation: produces
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C27
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: multi_source
exclusivity_scope: 192GB SOCAMM2 量產聲明另有 Micron 一條獨立公司來源；不表示客戶已採雙供或份額相等
as_of: 2026-04-19
review_due: 2026-08-31
status: active
boundary: SK hynix 明列 1cnm LPDDR5X 192GB SOCAMM2 mass production 與 Vera Rubin 設計方向；沒有模組互換、客戶 qualification、採購量、供應份額、收入或毛利。
next_trigger: 平台或客戶以同一版本與測試契約公布 Micron／SK hynix mixed-source qualification、採購量與部署分母。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I01
view: industry
from_id: concept:ai-memory-hierarchy
to_id: concept:hbm
relation: includes
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C1
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-01-05
review_due: 2026-08-10
status: active
boundary: Rubin 平台明列 GPU HBM4；不證明供應商份額、採購量、價格、收入或 HBM 是唯一記憶體層。
next_trigger: Rubin 實際部署揭露 HBM 配置、供應商與工作負載利用率。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I02
view: industry
from_id: concept:ai-memory-hierarchy
to_id: product:socamm2
relation: includes
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C1,MI-2026-08-02-AI-MEMORY-HIERARCHY#C3
note_refs:
evidence_state: verified
commercial_stage: sample
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-05
review_due: 2026-08-17
status: active
boundary: Rubin 有 SOCAMM system memory，Micron 256GB SOCAMM2 仍在送樣；兩份證據不構成 Micron 的 Rubin 獨家或量產份額。
next_trigger: 平台與供應商雙向核對 SOCAMM2 qualification、量產、容量配置與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I03
view: industry
from_id: concept:ai-memory-hierarchy
to_id: product:nvidia-cmx
relation: includes
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C2,MI-2026-08-02-AI-MEMORY-HIERARCHY#C12
as_of: 2026-07-16
review_due: 2026-08-19
status: active
boundary: NVIDIA 已提出 CMX G3.5 context tier，並描述 STX／DOCA 的 KV I/O、metadata、placement 與 control；不等於具名客戶上線、獨立效能驗證、採購量或收入。
next_trigger: NVIDIA 或客戶公布 CMX／STX 部署、可用狀態、容量、資料路徑與利用率。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I04
view: industry
from_id: concept:ai-memory-hierarchy
to_id: concept:kv-cache
relation: routes_to
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C2,MI-2026-08-02-AI-MEMORY-HIERARCHY#C12,MI-2026-08-02-AI-MEMORY-HIERARCHY#C13,MI-2026-08-02-AI-MEMORY-HIERARCHY#C14,MI-2026-08-02-AI-MEMORY-HIERARCHY#C15
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: KV cache 是 CMX／STX 與 KVBM 所服務的資料類型，NVIDIA 並描述 placement、recall、pre-staging、reuse、offload 與 onboard；功能與機制指標不證明特定儲存產品的淨效益或客戶採用。
next_trigger: 實際工作負載公開 KV cache placement、recall／pre-staging、冷熱命中、搬移／重算成本、request-level SLO 與 GPU idle time。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I05
view: industry
from_id: concept:ai-memory-hierarchy
to_id: component:system-ram
relation: includes
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C2,MI-2026-08-02-AI-MEMORY-HIERARCHY#C13
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: NVIDIA 的 CMX 架構將 system RAM 列為 G2 staging／buffering，現行 KVBM 文件另明列 pinned host 與 remote RDMA memory；不代表所有平台容量、類型、命中收益、客戶與供應商相同。
next_trigger: 具名客戶揭露 system／host memory 配置、cache 冷熱與重用、搬移等待、request-level SLO 及供應商。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I06
view: industry
from_id: concept:ai-memory-hierarchy
to_id: component:local-ssd
relation: includes
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C2,MI-2026-08-02-AI-MEMORY-HIERARCHY#C13
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: Local SSD 是 NVIDIA 所述 G3 warm KV 路徑，現行 KVBM 文件也明列 local／distributed SSD；不證明任一 SSD、控制器或 NAND 供應商 design win，也不保證搬移收益大於寫入壽命與等待成本。
next_trigger: 客戶或平台公布具名 SSD、容量、block／filter policy、KV workload、命中／搬移、耐久與 request-level SLO。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I07
view: industry
from_id: concept:ai-memory-hierarchy
to_id: component:shared-storage
relation: includes
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C2,MI-2026-08-02-AI-MEMORY-HIERARCHY#C13
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: Shared storage 是 CMX 架構的 G4 持久層，現行 KVBM 文件另明列 remote filesystem／object／cloud storage；不代表路徑已部署、一般儲存會被 CMX 取代或特定廠商因此受損。
next_trigger: 客戶公開 CMX／KVBM 與 shared／remote storage 的資料分工、容量、重用、搬移等待、可靠度與 TCO。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I08
view: industry
from_id: concept:ai-memory-hierarchy
to_id: standard:cxl4
relation: includes
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C4
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2025-11-18
review_due: 2026-08-17
status: active
boundary: CXL 4.0 規格已發布，但 Rubin 文件明列 CXL 3.1；不可把規格版本改寫成平台採用、互通或出貨。
next_trigger: CXL 4.0 host、switch、retimer 與 memory device 完成 integrators／compliance 並進入產品。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I09
view: industry
from_id: concept:ai-memory-hierarchy
to_id: group:memory
relation: routes_to
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-17
status: active
boundary: HBM、LPDRAM、NAND、SSD 與控制 IC 形成族群搜尋路由，但沒有 universe 公司具名 SOCAMM／CMX／CXL 4.0 訂單與財務證據。
next_trigger: 平台與台灣公司雙向核對具名產品、qualification、量產、出貨與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I10
view: industry
from_id: concept:ai-memory-hierarchy
to_id: group:serverodm
relation: routes_to
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-17
status: active
boundary: 多層記憶體增加系統整合問題，但一般 AI server 組裝能力不證明 CMX、SOCAMM 或 CXL 4.0 訂單。
next_trigger: ODM 揭露具名 Rubin／CMX／SOCAMM／CXL 系統、量產出貨與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I11
view: industry
from_id: concept:ai-memory-hierarchy
to_id: product:micron-socamm2-192gb
relation: includes
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C9
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-16
review_due: 2026-08-17
status: active
boundary: Micron 公司文件明列 192GB high-volume production；不代表其他容量同階段、客戶數、供應份額或財務貢獻。
next_trigger: 平台或客戶文件雙向核對 192GB 的 qualification、實際配置、出貨與利用率。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I12
view: industry
from_id: concept:ai-memory-hierarchy
to_id: product:micron-socamm2-256gb
relation: includes
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C3
note_refs:
evidence_state: verified
commercial_stage: sample
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-05
review_due: 2026-08-17
status: active
boundary: 256GB 的具名文件只到 customer sampling；較寬的產品家族量產敘述不能自動改寫這個容量的階段。
next_trigger: Micron 或平台文件明列 256GB qualification／production、配置與出貨邊界。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I13
view: industry
from_id: concept:ai-memory-hierarchy
to_id: product:nvidia-bluefield4-stx
relation: includes
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C12
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-16
review_due: 2026-08-19
status: active
boundary: NVIDIA 將 Vera BlueField-4 STX 列為 AI-native storage／context memory 的儲存處理器架構；不證明具名客戶部署、端到端改善或供應商收入。
next_trigger: 客戶公布 STX 的正式設備配置、production data path、工作負載與端到端結果。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I14
view: industry
from_id: concept:ai-memory-hierarchy
to_id: capability:ai-context-placement
relation: requires
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C12
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-16
review_due: 2026-08-19
status: active
boundary: NVIDIA 描述 storage processor 執行 placement、recall 與 pre-staging；只證明功能定位，不證明演算法對所有工作負載有效或已上線。
next_trigger: 同一具名 workload 公開 placement policy、命中／重算、等待與 GPU idle time。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I15
view: industry
from_id: concept:ai-memory-hierarchy
to_id: capability:heterogeneous-data-movement
relation: requires
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C12
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-16
review_due: 2026-08-19
status: active
boundary: NVIDIA 描述 BlueField 加速 GPU／CPU 與儲存路徑的資料搬移；介面與架構存在不等於搬移免費、客戶已部署或端到端更快。
next_trigger: 具名部署公開來源、目的地、資料量、搬移等待、頻寬占用與完整工作負載結果。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I16
view: industry
from_id: concept:ai-memory-hierarchy
to_id: capability:ai-storage-data-processing
relation: requires
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C7,MI-2026-08-02-AI-MEMORY-HIERARCHY#C12
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-08-19
status: active
boundary: NVIDIA 文件列出 KV I/O、metadata、security、control、壓縮、加密、完整性與復原；公司 microbenchmark 與架構敘述不等於含 SSD、網路、GPU 的端到端結果。
next_trigger: 同一 production path 公開處理器、媒體、網路、軟體、GPU 與完整 SLO 的可重建測試。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I17
view: industry
from_id: concept:ai-memory-hierarchy
to_id: metric:ai-data-path-end-to-end-slo
relation: measured_by
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C8
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: 端到端等待、閒置、搬移與復原是本文綜合多份一手文件提出的驗證框架；尚無單一 production workload 完整公開所有欄位。
next_trigger: 同一正式服務揭露資料位置、處理、連接、搬移、placement 與使用者 SLO 的完整對帳。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I18
view: industry
from_id: concept:ai-memory-hierarchy
to_id: metric:kv-cache-reuse-transfer-observability
relation: measured_by
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C13,MI-2026-08-02-AI-MEMORY-HIERARCHY#C14,MI-2026-08-02-AI-MEMORY-HIERARCHY#C15
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: NVIDIA 文件直接定義 matched tokens、hit rate、offload／onboard blocks 與最小 long-prefix 驗證；這些是機制可觀測欄位，不是使用者 SLO、獨立因果或客戶部署。
next_trigger: 同一 production workload 把 cold／warm cache、prefix overlap、matched／hit／offload／onboard、重算、錯誤與 request-level SLO 對在同一時間窗。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I19
view: industry
from_id: concept:ai-memory-hierarchy
to_id: metric:ai-inference-service-slo
relation: measured_by
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C16,MI-2026-08-02-AI-MEMORY-HIERARCHY#C17,MI-2026-08-02-AI-MEMORY-HIERARCHY#C18
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: AIPerf 與 MLPerf 文件可直接界定 TTFT、ITL、throughput、SUT、load、quality 與可重現性；它們不指定哪個記憶體層是瓶頸，也不證明任何私有 workload 的商業結果。
next_trigger: 具名客戶在固定 SUT、model／trace、request shape、load 與 quality 下公開 request-level latency／goodput／errors 及重複結果。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I20
view: industry
from_id: concept:ai-memory-hierarchy
to_id: process:ai-memory-tier-measurement-passport
relation: requires
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C19
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 八格護照是研究中心整合多份一手方法文件後提出的可重建比較框架，不是單一標準，也尚無具名客戶完整公開 CMX／SOCAMM／CXL／KV tier 的 production baseline-versus-treatment。
next_trigger: 具名 production 服務固定受測系統、工作負載、流量、reuse／cache state、tier policy 與 data path，並公開機制指標、request-level SLO、品質、成本、功耗及 failure recovery。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I21
view: industry
from_id: concept:ai-memory-hierarchy
to_id: process:memory-roofline-performance-passport
relation: requires
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C23
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-31
status: active
boundary: 十欄護照是研究中心依 Roofline 原始報告與 NVIDIA GPU 方法頁整合的 kernel-local 解碼器，不是產業標準、production benchmark、採購門檻或公司財務證據；它不能取代前文八格服務量測護照。
next_trigger: 具名 production workload 固定版本、精度、正確性、work、指定 memory interface bytes、兩個 ceiling、achieved performance、端到端 SLO、重複不確定度、能源成本與商業共同鍵。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I22
view: industry
from_id: concept:ai-memory-hierarchy
to_id: metric:operational-intensity-ridge-point-boundary
relation: measured_by
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C21,MI-2026-08-02-AI-MEMORY-HIERARCHY#C22,MI-2026-08-02-AI-MEMORY-HIERARCHY#C23
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-31
status: active
boundary: S18／S19 可界定操作強度、兩個 ceiling、ridge point 與 first-order limitation；把這套 kernel 邊界接到 AI memory hierarchy 是研究推論，且 Roofline 只給上限，不證明 achieved、request-level、成本或商業結果。
next_trigger: 同一模型／kernel 與軟硬體版本公開 matched-precision operations、固定參考層 bytes、sustainable bandwidth、compute ceiling、profiler achieved、latency／parallelism counters 及多次 run。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I23
view: industry
from_id: concept:ai-memory-hierarchy
to_id: capability:agent-persistent-shared-state
relation: includes
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C24,MI-2026-08-02-AI-MEMORY-HIERARCHY#C25
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-09-30
status: active
boundary: NVIDIA research preview 與 AWS 參考架構可直接證明 model context、stateless invocation、execution object 及跨 session／agent persistent state 是不同角色；不證明正式客戶普遍採用、exactly-once、硬體容量或財務需求。
next_trigger: 具名 production workflow 公開跨 session／agent state 的 owner、bytes、retention、讀寫、衝突、恢復、SLO 與成本。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I24
view: industry
from_id: concept:ai-memory-hierarchy
to_id: metric:agent-state-lifecycle-observability
relation: measured_by
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C26
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-23
review_due: 2026-09-30
status: active
boundary: 八欄狀態生命週期紀錄是研究中心整合 NVIDIA／AWS 架構後提出的比較框架，不是產業標準；欄位齊全也不自動證明因果、可靠度、成本下降、新增 SSD／NAND 或公司收入。
next_trigger: 同一正式任務固定 model／harness／workload，公開 context、KV、durable state 三帳與 baseline-versus-treatment 的重做量、衝突、SLO、recovery、storage cost 及 BOM。
-->
