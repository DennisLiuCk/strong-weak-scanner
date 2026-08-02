# AI 記憶體分層知識圖譜

本圖將 HBM、SOCAMM、KV cache、context storage 與 CXL 放回各自的系統位置。公司線只停在
平台整合或送樣；沒有量產、客戶與財務資料前，不把一般記憶體能力畫成台灣公司受惠。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: ai-memory-hierarchy
root_node_id: concept:ai-memory-hierarchy
label: AI 記憶體分層
summary: 用頻寬、容量、延遲、持久性與共享性拆開 HBM、SOCAMM、CMX 與 CXL，避免把不同層重複計入單一記憶體題材。
article_ids: MI-2026-08-02-AI-MEMORY-HIERARCHY
status: active
-->

<!-- knowledge_edge
edge_id: KG-MEM-C01
view: company
from_id: company:nvidia
to_id: concept:ai-memory-hierarchy
relation: integrates
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C1,MI-2026-08-02-AI-MEMORY-HIERARCHY#C2
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-16
review_due: 2026-08-10
status: active
boundary: NVIDIA 已在 Rubin／CMX 架構中分層 HBM、system memory 與 context storage；不等於客戶已部署 CMX、各層利用率已驗證或供應商收入可辨識。
next_trigger: NVIDIA 或客戶公布 Rubin／CMX 實際上線、容量配置、KV placement 與利用率。
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
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C2
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-16
review_due: 2026-08-10
status: active
boundary: NVIDIA 已提出 CMX G3.5 context tier；不等於具名客戶上線、獨立效能驗證、採購量或收入。
next_trigger: NVIDIA 或客戶公布 CMX 部署、可用狀態、容量與利用率。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I04
view: industry
from_id: concept:ai-memory-hierarchy
to_id: concept:kv-cache
relation: routes_to
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-16
review_due: 2026-08-10
status: active
boundary: KV cache 是 CMX 所服務的資料類型；資料重要性不證明特定儲存產品的成本效益或客戶採用。
next_trigger: 實際工作負載公開 KV cache placement、命中率、搬移成本與 GPU idle time。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I05
view: industry
from_id: concept:ai-memory-hierarchy
to_id: component:system-ram
relation: includes
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-16
review_due: 2026-08-10
status: active
boundary: NVIDIA 將 system RAM 列為 G2 staging／buffering；不代表所有平台容量、記憶體類型與供應商相同。
next_trigger: Rubin 客戶揭露實際 system memory 配置與 KV cache 使用方式。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I06
view: industry
from_id: concept:ai-memory-hierarchy
to_id: component:local-ssd
relation: includes
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-16
review_due: 2026-08-10
status: active
boundary: Local SSD 是 NVIDIA 所述 G3 warm KV 路徑；不證明特定 SSD、控制器或 NAND 供應商 design win。
next_trigger: 客戶或平台公布具名 SSD、容量、KV workload 與量產部署。
-->

<!-- knowledge_edge
edge_id: KG-MEM-I07
view: industry
from_id: concept:ai-memory-hierarchy
to_id: component:shared-storage
relation: includes
claim_refs: MI-2026-08-02-AI-MEMORY-HIERARCHY#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-16
review_due: 2026-08-10
status: active
boundary: Shared storage 是 G4 持久層；不代表一般儲存會被 CMX 取代或特定廠商因此受損。
next_trigger: 客戶公開 CMX 與 shared storage 的資料分工、容量與 TCO。
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
