# AMD Helios 部署階梯知識圖譜

本圖把開始生產、預計出貨、客戶測試、正式上線與未來部署分開，並將台灣夥伴的具名角色
停在生態系層級；沒有公司財務證據前，線條不升級成訂單或獲利。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: amd-helios
root_node_id: product:amd-helios
label: AMD Helios 部署階梯
summary: 以六個部署關卡連結具名客戶與台灣整機、封裝、載板角色，同時保留多架構競爭及財務未驗證邊界。
article_ids: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER
status: active
-->

<!-- knowledge_edge
edge_id: KG-HEL-C01
view: company
from_id: company:amd
to_id: product:amd-helios
relation: owns_platform
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-23
review_due: 2026-08-09
status: active
boundary: AMD 稱 Helios 已 in production；這不是所有客戶已收到、驗收、上線或收入已認列。
next_trigger: AMD 確認實際出貨或 multi-GW deployment，並提供客戶、容量與收入邊界。
-->

<!-- knowledge_edge
edge_id: KG-HEL-C02
view: company
from_id: company:microsoft
to_id: product:amd-helios
relation: planned_customer
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C3,MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C7
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Azure AI 基礎設施同時使用外部方案與 purpose-built silicon，不是 Helios 排他採用。
as_of: 2026-07-20
review_due: 2026-08-09
status: active
boundary: 2026 下半年出貨規劃與 upcoming Azure SKU 不等於已出貨、preview、GA、區域、利用率或雲端收入。
next_trigger: Azure 將 ND MI455X v7 列為 preview／launched，或 AMD 確認向 Microsoft 實際出貨。
-->

<!-- knowledge_edge
edge_id: KG-HEL-C03
view: company
from_id: company:openai
to_id: product:amd-helios
relation: planned_customer
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C4
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-23
review_due: 2026-08-09
status: active
boundary: 證實的是 AMD 轉述 OpenAI 預期 2026Q4 online，不是已上線、對外商用、利用率或收入。
next_trigger: OpenAI 自有文件或 AMD 新文件確認 Helios 已 online 並提供日期與部署範圍。
-->

<!-- knowledge_edge
edge_id: KG-HEL-C04
view: company
from_id: company:meta
to_id: product:amd-helios
relation: tests
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C4
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-23
review_due: 2026-08-09
status: active
boundary: 測試與 validation 不等於通過驗證、採購量、部署日期或排他採用。
next_trigger: Meta 或 AMD 確認 validation 完成並開始實際部署。
-->

<!-- knowledge_edge
edge_id: KG-HEL-C05
view: company
from_id: company:anthropic
to_id: product:amd-helios
relation: plans_deployment
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C5
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-21
review_due: 2026-08-09
status: active
boundary: 最高 2 GW 是合作上限，首個 GW 仍預計 2027H1 開始部署；不是目前已上線容量或 AMD 已認列收入。
next_trigger: Anthropic 或 AMD 確認首批部署開始並提供日期、容量與後續擴張。
-->

<!-- knowledge_edge
edge_id: KG-HEL-C06
view: company
from_id: company:2356
to_id: product:amd-helios
relation: builds_systems
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-21
review_due: 2026-08-09
status: active
boundary: Inventec 被列為協助打造 Helios-based systems 的夥伴，不等於新增訂單、份額、收入、毛利或現金流。
next_trigger: 2356 公司文件把 Helios／MI450 系列連到量產出貨與可辨識財務足跡。
-->

<!-- knowledge_edge
edge_id: KG-HEL-C07
view: company
from_id: company:3231
to_id: product:amd-helios
relation: builds_systems
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-21
review_due: 2026-08-09
status: active
boundary: Wistron 生態系列名不等於 Helios 新訂單、分配份額、收入或毛利。
next_trigger: 3231 正式揭露 Helios／MI450 量產、出貨與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-HEL-C08
view: company
from_id: company:6669
to_id: product:amd-helios
relation: builds_systems
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-21
review_due: 2026-08-09
status: active
boundary: Wiwynn 被列名協助打造系統，不證明具名客戶、量產數量、收入、毛利或營運資金轉換。
next_trigger: 6669 公司文件揭露 Helios／MI450 出貨、收入與現金流。
-->

<!-- knowledge_edge
edge_id: KG-HEL-C09
view: company
from_id: company:3693
to_id: product:amd-helios
relation: builds_systems
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-21
review_due: 2026-08-09
status: active
boundary: AIC 參與機架與 compute-tray 機構設計只證明合作角色，不等於新增訂單、量產收入或獲利。
next_trigger: 3693 揭露具名 Helios 機構產品、量產出貨與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-HEL-C10
view: company
from_id: company:3711
to_id: product:amd-helios
relation: develops_packaging
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-21
review_due: 2026-08-09
status: active
boundary: ASE／SPIL 的 EFB／2.5D 技術開發或資格角色不等於 Helios 專屬訂單、產能利用、收入或獲利。
next_trigger: 3711 公司文件把具名封裝產品連到 Helios／MI450 量產與財務結果。
-->

<!-- knowledge_edge
edge_id: KG-HEL-C11
view: company
from_id: company:6239
to_id: product:amd-helios
relation: develops_packaging
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-21
review_due: 2026-08-09
status: active
boundary: PTI 的 EFB／2.5D 技術開發或資格角色不等於 Helios 專屬訂單、量產收入或獲利。
next_trigger: 6239 公司文件揭露 Helios／MI450 封裝量產、收入與毛利。
-->

<!-- knowledge_edge
edge_id: KG-HEL-C12
view: company
from_id: company:3037
to_id: product:amd-helios
relation: supports_substrate
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-21
review_due: 2026-08-09
status: active
boundary: Unimicron 被列為 AMD 載板或先進封裝夥伴，不是 Helios-specific 訂單、份額、收入或毛利證據。
next_trigger: 3037 將具名產品與 Helios／MI450 資格、出貨及財務貢獻連結。
-->

<!-- knowledge_edge
edge_id: KG-HEL-C13
view: company
from_id: company:3189
to_id: product:amd-helios
relation: supports_substrate
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-21
review_due: 2026-08-09
status: active
boundary: Kinsus 生態系列名不是 Helios-specific 新訂單、分配份額、收入、毛利或現金流。
next_trigger: 3189 公司文件揭露具名 Helios／MI450 載板資格、出貨與財務轉換。
-->

<!-- knowledge_edge
edge_id: KG-HEL-C14
view: company
from_id: company:8046
to_id: product:amd-helios
relation: supports_substrate
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-21
review_due: 2026-08-09
status: active
boundary: Nan Ya PCB 被列為 AMD 載板或先進封裝夥伴，不等於 Helios-specific 訂單、收入或獲利。
next_trigger: 8046 揭露具名 Helios／MI450 產品資格、量產出貨與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I01
view: industry
from_id: product:amd-helios
to_id: concept:rack-scale
relation: contains
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C1
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-09
status: active
boundary: 機架級系統更接近可用設備，但不表示具名客戶已驗收、上線或產生收入。
next_trigger: 客戶端文件揭露實際交付、驗收、可用區域與運行規模。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I02
view: industry
from_id: product:amd-helios
to_id: stage:production
relation: reaches_stage
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-23
review_due: 2026-08-09
status: active
boundary: Production 是製造里程碑，不等於客戶已驗收、部署或 AMD 已認列收入。
next_trigger: AMD 確認開始實際出貨並提供數量或客戶邊界。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I03
view: industry
from_id: product:amd-helios
to_id: stage:shipment
relation: moves_to
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-20
review_due: 2026-08-09
status: active
boundary: 2026 下半年 shipment 是前瞻時程，不是已出貨數量、時間點或收入。
next_trigger: AMD 或 Microsoft 確認首批 Helios 實際出貨與驗收。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I04
view: industry
from_id: product:amd-helios
to_id: stage:cloud-deployment
relation: moves_to
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C3,MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C4,MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C5
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-23
review_due: 2026-08-09
status: active
boundary: Azure upcoming、OpenAI Q4 online 與 Anthropic 2027H1 首個 GW 是不同客戶與完成度，不能相加成已部署容量。
next_trigger: 各客戶依各自期限確認 preview、online 或部署開始，並提供範圍。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I05
view: industry
from_id: product:amd-helios
to_id: stage:validation
relation: passes_through
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C4
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-23
review_due: 2026-08-09
status: active
boundary: Meta validation 仍是測試階段，不等於通過、採購量、部署日期或財務結果。
next_trigger: Meta 確認 validation 完成或改採替代平台。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I06
view: industry
from_id: product:amd-helios
to_id: component:efb
relation: uses_packaging
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-21
review_due: 2026-08-09
status: active
boundary: EFB 技術開發或資格角色不等於已取得 Helios 專屬量產訂單。
next_trigger: AMD 與封裝夥伴可雙向核對產品、資格、量產及財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I07
view: industry
from_id: product:amd-helios
to_id: process:2_5d-3d
relation: uses_packaging
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-21
review_due: 2026-08-09
status: active
boundary: 2.5D 生態系角色不證明任一台灣封裝商的 Helios 專屬份額或財務貢獻。
next_trigger: 具名產品、量產產能與收入能在 AMD 與夥伴文件雙向核對。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I08
view: industry
from_id: product:amd-helios
to_id: component:substrate
relation: uses_substrate
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-21
review_due: 2026-08-09
status: active
boundary: 廣泛 AMD 載板合作不是 Helios-specific 訂單、分配份額、收入或毛利。
next_trigger: 載板公司以具名產品連結 Helios／MI450 資格、量產與財務結果。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I09
view: industry
from_id: product:amd-helios
to_id: group:serverodm
relation: routes_to
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-21
review_due: 2026-08-09
status: active
boundary: 族群路由來自具名夥伴角色，不代表所有 ODM／機構公司都參與或已受惠。
next_trigger: 公司文件揭露具名系統、驗收、量產出貨與財務足跡。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I10
view: industry
from_id: product:amd-helios
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-21
review_due: 2026-08-09
status: active
boundary: 技術合作與資格認證不等於封測量產、利用率、收入或獲利。
next_trigger: 封裝夥伴揭露具名量產產品與可辨識財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I11
view: industry
from_id: product:amd-helios
to_id: group:pcb
relation: routes_to
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-21
review_due: 2026-08-09
status: active
boundary: 被列名的是廣泛 AMD 載板合作，不能擴張成整個 PCB 族群的 Helios 訂單。
next_trigger: 載板公司以具名產品、資格與量產財務資料完成映射。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I12
view: industry
from_id: product:amd-helios
to_id: concept:purpose-built-silicon
relation: competes_with
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C7
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: Microsoft 明確表示 Azure AI 基礎設施同時採用外部創新與自家 purpose-built silicon and systems。
as_of: 2026-07-20
review_due: 2026-08-09
status: active
boundary: Helios 成為可部署選項不等於排他標準，新增支出與既有架構份額重分配仍無法分解。
next_trigger: Microsoft 揭露各架構部署範圍、利用率、工作負載或資本支出分配。
-->
