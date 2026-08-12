# AMD Helios 部署階梯知識圖譜

本圖把參考設計、整機廠品牌系統化、整櫃資格、開始生產、預計出貨、客戶測試、正式上線與
未來部署分開，並將運算、網路、電力、液冷、控制、配置基準、變更重驗與維修責任接回同一
整櫃；沒有交付與公司財務證據前，線條不升級成客戶機群、訂單或獲利。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: amd-helios
root_node_id: product:amd-helios
label: AMD Helios 部署階梯
summary: 以參考設計、品牌系統、整櫃資格與六個部署關卡連結系統責任、具名客戶及台灣夥伴，同時保留交付、財務與多架構競爭的未驗證邊界。
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
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6,MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C19
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-26
review_due: 2026-09-15
status: active
boundary: 緯穎公司頁直接展示 Helios 整合方案並自述把參考設計推向量產；仍沒有品牌 SKU、固定 BOM、完整資格、具名客戶、已發生出貨、收入、毛利或營運資金分母。
next_trigger: 6669 公開版本化品牌產品、整櫃 qualification、客戶／實際出貨與可辨識財務足跡。
-->

<!-- knowledge_edge
edge_id: KG-HEL-C09
view: company
from_id: company:3693
to_id: product:amd-helios
relation: builds_systems
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C6,MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C20
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-01
review_due: 2026-09-15
status: active
boundary: AIC 公司頁直接確認 Helios 關鍵機械架構角色與展會展示；仍沒有品牌 SKU、完整 BOM、整櫃資格、客戶驗收、量產出貨或財務分母。
next_trigger: 3693 公開具名 Helios 產品、配置清單、qualification、已發生出貨與財務貢獻。
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
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C11
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-12
status: retired
boundary: 原線條依 C1 把 Helios 寫成已跨過只有參考設計的階段；C11 已修正此讀法，改由 I13 以參考設計、品牌系統與整櫃資格邊界重建。
next_trigger: 已由 KG-HEL-I13、I14、I22 與 I23 接續；本歷史線條不再參與 active graph。
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

<!-- knowledge_edge
edge_id: KG-HEL-I13
view: industry
from_id: product:amd-helios
to_id: concept:rack-scale
relation: contains
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C11,MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C12
note_refs:
evidence_state: inference
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: Helios 是涵蓋運算、網路、電力、液冷、控制軟體與維修的機架級參考設計；這不表示 AMD 直接出售單一成品或任一品牌系統已通過整櫃資格。
next_trigger: 具名 OEM／ODM 品牌系統公開固定配置、整櫃資格與實際交付。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I14
view: industry
from_id: product:amd-helios
to_id: stage:reference-design
relation: reaches_stage
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C10
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: AMD 現行 FAQ 明示 Helios 是 reference design 且 not a product for sale；這不是品牌型號、量產出貨或客戶部署。
next_trigger: AMD 或 OEM／ODM 公開可採購品牌系統、配置邊界與正式產品文件。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I15
view: industry
from_id: product:amd-helios
to_id: standard:open-rack-wide
relation: uses_standard
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C10,MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C12
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 採 Open Rack Wide 參考架構不等於任一 Helios 品牌系統取得 OCP 認證、通過客戶資格或已部署。
next_trigger: 具名品牌系統提供 ORW 規格版本、符合性範圍與資格結果。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I16
view: industry
from_id: product:amd-helios
to_id: component:ai-compute-tray
relation: contains
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C12
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 參考設計包含 compute tray 角色；這不是任一 OEM 實際托盤 BOM、版本、測試結果或量產數量。
next_trigger: OEM／ODM datasheet 固定運算托盤配置並提供托盤與整櫃資格邊界。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I17
view: industry
from_id: product:amd-helios
to_id: component:ai-scale-up-switch-tray
relation: contains
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C12
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 參考設計包含 switch tray 與 scale-up 角色；峰值頻寬或單一交換模組存在不等於整櫃工作負載穩定。
next_trigger: 具名品牌系統公開拓撲、交換托盤版本、壓力測試與故障恢復結果。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I18
view: industry
from_id: product:amd-helios
to_id: component:rack-power-shelf
relation: contains
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C12
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 參考設計包含 power shelf 與垂直匯流排；這不證明機房供電、突波、保護、備援、效率或維修隔離已通過。
next_trigger: 具名品牌系統與場站文件固定電力配置並公開整櫃負載、保護與備援資格。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I19
view: industry
from_id: product:amd-helios
to_id: component:rack-manifold
relation: contains
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C12
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 參考設計包含 cooling manifold 與 quick disconnect；接上冷卻迴路不等於流量、壓差、漏液、材料相容與故障隔離已通過。
next_trigger: 具名品牌系統公開液冷版本、介面、整櫃熱負載與可靠度資格結果。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I20
view: industry
from_id: product:amd-helios
to_id: capability:rack-serviceability
relation: requires
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C12
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: AMD 公開設計強調模組抽換與低干擾維修；這不是客戶現場的故障定位時間、可用率或維修成功率。
next_trigger: OEM／ODM 或客戶公開維修程序、替換時間、故障隔離與復原後重驗結果。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I21
view: industry
from_id: product:amd-helios
to_id: capability:rack-lifecycle-control
relation: requires
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C12
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 參考設計列出 BMC、ROCm、觀測與 lifecycle 管理責任；這不證明特定硬體、韌體與軟體組合已在生產機群長期穩定。
next_trigger: 具名品牌系統固定軟硬體相容矩陣並提供更新、回退、遙測與復原證據。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I22
view: industry
from_id: product:amd-helios
to_id: stage:oem-systemization
relation: passes_through
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C10,MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C11
note_refs:
evidence_state: inference
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: AMD 說藍圖供 OEM／ODM 打造品牌系統，支持把 systemization 當成必要交接；目前仍沒有完整公開的具名型號、BOM 與版本清單。
next_trigger: OEM／ODM 正式產品頁與 datasheet 公開品牌型號、BOM 邊界、韌體、軟體、冷卻與製造狀態。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I23
view: industry
from_id: product:amd-helios
to_id: stage:integrated-rack-qualification
relation: passes_through
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C13,MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C14,MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C21
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 系統工程方法顯示整櫃資格要綁定配置與變更後重驗，但本輪沒有具名 Helios 品牌系統的完整 test matrix、pass／fail、change／retest、場站驗收與生產機群證據。
next_trigger: 平台方、OEM／ODM 或客戶公開同一 Helios 品牌型號與版本的整櫃資格資料包及 site acceptance／production-fleet 結果。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I24
view: industry
from_id: product:amd-helios
to_id: capability:rack-configuration-baseline
relation: requires
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C21
note_refs:
evidence_state: inference
commercial_stage: qualification
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 多子系統整櫃要讓測試結果對回硬體、軟體、網路、場站與測試版本；這是由通用機櫃方法推得的必要證據，不是 Helios 已公開配置身分證或已通過資格。
next_trigger: 具名 Helios 品牌系統公開 factory inventory、BOM／SBOM、設定、場站輸入、測試條件、簽核與交接的同版紀錄。
-->

<!-- knowledge_edge
edge_id: KG-HEL-I25
view: industry
from_id: product:amd-helios
to_id: process:rack-change-triggered-regression
relation: requires
claim_refs: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER#C21
note_refs:
evidence_state: inference
commercial_stage: qualification
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: NVIDIA 與 Google／OCP 文件支持變更後重驗及變更紀錄的方法，但不能替 Helios 證明 retest matrix、結果、客戶驗收或生產穩定。
next_trigger: 具名 Helios 品牌系統公開硬體、韌體、線纜、場站等變更類型與對應必重跑測項、結果及回退條件。
-->
