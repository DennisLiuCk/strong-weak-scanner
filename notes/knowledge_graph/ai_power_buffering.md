# AI 功率緩衝時間尺度知識圖譜

本圖把 CBU、BBU 與 BESS 依時間尺度、系統位置及失效任務分層。公司節點只表示公開架構或
reference design；族群節點仍是待驗證搜尋路由，沒有一條線代表台灣公司已取得量產訂單。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: ai-power-buffering
root_node_id: concept:ai-power-buffering
label: AI 功率緩衝時間尺度
summary: 以機架附近的 CBU、rack ride-through BBU 與設施級 BESS 拆解 AI 負載波動，並把架構必要性與台灣供應商財務證據分開。
article_ids: MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY
status: active
-->

<!-- knowledge_edge
edge_id: KG-APB-C01
view: company
from_id: company:nvidia
to_id: concept:ai-power-buffering
relation: owns_platform
claim_refs: MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY#C1
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: multi_source
exclusivity_scope: NVIDIA 公開多時間尺度架構並列出多家 power ecosystem 夥伴；不是任何儲能層或元件的排他供應證據。
as_of: 2025-10-13
review_due: 2026-09-01
status: active
boundary: 公開架構支持時間與位置分層，不證明每個 AI factory 採用相同配置、production BOM 或供應商份額。
next_trigger: NVIDIA 公布具名 production rack 與 facility 的 CBU／BBU／BESS qualification、部署與 operating data。
-->

<!-- knowledge_edge
edge_id: KG-APB-C02
view: company
from_id: company:texas-instruments
to_id: concept:ai-power-buffering
relation: has_capability
claim_refs: MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: TI 展示 EDLC CBU 與多個 conversion／protection reference designs；NVIDIA 與 OCP 文件同時保留多家供應與多種架構路徑。
as_of: 2026-03-16
review_due: 2026-09-01
status: active
boundary: Reference design 證明技術角色，不等於 hyperscaler qualification、production deployment、訂單或收入。
next_trigger: 具名客戶採用 TI CBU design 並完成 qualification、量產出貨與 field validation。
-->

<!-- knowledge_edge
edge_id: KG-APB-I01
view: industry
from_id: concept:ai-power-buffering
to_id: concept:800v-power-tree
relation: integrated_with
claim_refs: MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY#C4
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: 儲能可接入 800VDC power tree 的不同位置，實際配置仍可能因平台與 topology 而異。
as_of: 2026-08-03
review_due: 2026-09-01
status: active
boundary: 800VDC 有利於儲能整合不代表所有 CBU／BBU／BESS 都使用 800V，也不固定轉換級或 BOM。
next_trigger: 同一 production rack 公布從 facility bus 到 CBU／BBU 與 compute tray 的完整架構。
-->

<!-- knowledge_edge
edge_id: KG-APB-I02
view: industry
from_id: concept:ai-power-buffering
to_id: component:rack-capacitor-bank
relation: contains
claim_refs: MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY#C1,MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY#C2,MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: NVIDIA、OCP 與 TI 皆支持 capacitor／supercapacitor rack buffering 路徑，且沒有任何來源主張單一元件或供應商排他。
as_of: 2026-08-03
review_due: 2026-09-01
status: active
boundary: CBU 的角色已具體，但容量、材料、壽命、供應商與量產採用依平台而定。
next_trigger: OCP 或客戶公布 CBU qualification、interface、field duty cycle 與 production BOM。
-->

<!-- knowledge_edge
edge_id: KG-APB-I03
view: industry
from_id: concept:ai-power-buffering
to_id: component:high-voltage-bbu
relation: contains
claim_refs: MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY#C2
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-01
review_due: 2026-09-01
status: active
boundary: OCP Diablo 400 的 BBU option 支持 rack ride-through 任務，不等於所有平台採同一時間範圍、電池化學或供應商。
next_trigger: 具名 production platform 公布 BBU module、qualification、可靠度與實際部署。
-->

<!-- knowledge_edge
edge_id: KG-APB-I04
view: industry
from_id: concept:ai-power-buffering
to_id: component:facility-bess
relation: contains
claim_refs: MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY#C1
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2025-10-13
review_due: 2026-09-01
status: active
boundary: NVIDIA 的 facility BESS 層支持較慢負載平滑與 generator transfer，不證明每個場域採用或可取代 rack buffering。
next_trigger: 具名 AI factory 公布 BESS topology、容量任務、併網與 field operating data。
-->

<!-- knowledge_edge
edge_id: KG-APB-I05
view: industry
from_id: concept:ai-power-buffering
to_id: stage:reference-design
relation: reaches_stage
claim_refs: MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-16
review_due: 2026-09-01
status: active
boundary: TI EDLC CBU 已到 reference design／展示階段，尚不能改寫成 customer qualification 或 production。
next_trigger: Reference design 被具名客戶採用並完成 qualification、deployment 與量產出貨。
-->

<!-- knowledge_edge
edge_id: KG-APB-I06
view: industry
from_id: concept:ai-power-buffering
to_id: group:passive
relation: routes_to
claim_refs: MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-30
status: active
boundary: 電容與超級電容形成被動元件搜尋路由；沒有 universe 公司具名 CBU BOM、qualification、訂單或財務證據。
next_trigger: 客戶與公司雙向核對具名元件、規格、量產出貨、收入及毛利。
-->

<!-- knowledge_edge
edge_id: KG-APB-I07
view: industry
from_id: concept:ai-power-buffering
to_id: group:powersupply
relation: routes_to
claim_refs: MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-30
status: active
boundary: 模組、bus conversion、hot-swap 與控制形成電源供應搜尋路由，但外部架構不證明台灣廠量產或財務貢獻。
next_trigger: 具名 CBU／BBU 模組完成 customer qualification、shipment 並有可辨識財務分母。
-->

<!-- knowledge_edge
edge_id: KG-APB-I08
view: industry
from_id: concept:ai-power-buffering
to_id: group:power
relation: routes_to
claim_refs: MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-30
status: active
boundary: 高壓保護與雙向轉換形成功率元件搜尋路由；沒有固定材料份額、supplier BOM 或公司收入證據。
next_trigger: 客戶與供應商公布具名 device、stage、qualification、量產與財務結果。
-->
