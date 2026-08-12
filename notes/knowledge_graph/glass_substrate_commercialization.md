# 玻璃基板商業化知識圖譜

本圖先把暫時玻璃載板、TGV／玻璃中介層、玻璃核心與完整封裝基板分開，再追 pilot、proof sample、
局部結構可靠度、客戶產品驗證與 production yield。公司有工廠、合作或樣品並不等於量產；財務
內圈目前刻意保持空白。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: glass-substrate-commercialization
root_node_id: concept:glass-substrate-commercialization
label: 玻璃基板商業化
summary: 先分清 carrier、TGV／interposer、glass core 與完整 package substrate，再追 pilot、sample、三層 reliability、yield 與量產，並保存 HVM 與 roadmap 被後續證據修正的歷史。
article_ids: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION
status: active
-->

<!-- knowledge_edge
edge_id: KG-GLS-C01
view: company
from_id: company:absolics
to_id: concept:glass-substrate-commercialization
relation: tests
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C8
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-27
review_due: 2026-08-19
status: active
boundary: Absolics 的 embedding 初始可靠度測試已開始，non-embedding 原型已供應；兩者都沒有公開 qualification completion、量產良率、商業出貨或重複訂單。
next_trigger: 任一路徑公開客戶通過結果，並提供 production start、yield／throughput、commercial shipment 或 repeat order。
-->

<!-- knowledge_edge
edge_id: KG-GLS-C02
view: company
from_id: company:intel
to_id: concept:glass-substrate-commercialization
relation: develops_packaging
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C3
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Intel 與 Lens 公告探索互補能力，且只證實合作；沒有排他、供應份額或固定量產路徑。
as_of: 2026-07-24
review_due: 2026-09-02
status: active
boundary: Explore／potential cooperation 不等於產品、sample、qualification、mass production 或財務貢獻。
next_trigger: Intel 公布具名 glass substrate package、sample、customer qualification 與 production plan。
-->

<!-- knowledge_edge
edge_id: KG-GLS-C03
view: company
from_id: company:lens-technology
to_id: concept:glass-substrate-commercialization
relation: supports_substrate
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C3
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Lens 提供精密玻璃加工與大規模製造能力，但合作仍在 explore 階段且未宣稱獨家。
as_of: 2026-07-24
review_due: 2026-09-02
status: active
boundary: 一般精密玻璃量產能力不等於半導體 glass core 已完成 TGV、metallization、reliability 與 HVM。
next_trigger: Lens／Intel 公布具名 package、pilot sample、qualification 與 production。
-->

<!-- knowledge_edge
edge_id: KG-GLS-C04
view: company
from_id: company:samsung-electro-mechanics
to_id: concept:glass-substrate-commercialization
relation: plans_production
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C9
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-11-05
review_due: 2026-09-12
status: active
boundary: Samsung Electro-Mechanics 的 Sejong pilot 仍在製作原型，合資量產路線改為 2027 年後；MOU 與 roadmap 不等於主協議、qualification、yield 或投產。
next_trigger: 合資主協議、production equipment、customer qualification、yield 與 2027 年後正式投產時程。
-->

<!-- knowledge_edge
edge_id: KG-GLS-C05
view: company
from_id: company:corning
to_id: concept:glass-substrate-commercialization
relation: has_capability
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C10
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: Corning 分別揭露 carrier glass 與 TGV／interposer 能力；材料角色存在不等於完整 glass-core package substrate、下游客戶 HVM、份額或收入。
next_trigger: 具名 semiconductor customer 對同一角色公開 qualification、production shipment 與 financial contribution。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I01
view: industry
from_id: concept:glass-substrate-commercialization
to_id: component:glass-core
relation: includes
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C10,MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C12
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: Glass core 是完整 package substrate 內的核心材料；它仍須整合增層線路與封裝，角色存在不代表共同規格、可互換供應或量產成熟。
next_trigger: 客戶產品公開完整 glass-core substrate 規格、supplier、qualification、yield 與 production。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I02
view: industry
from_id: concept:glass-substrate-commercialization
to_id: process:through-glass-via
relation: requires
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C10,MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C11,MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C12
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: TGV 可服務玻璃中介層或 glass core 的垂直互連；孔洞與熱循環結果不證明完整基板、特定設備材料商或台灣公司已通過量產供貨。
next_trigger: 同一 package 公開 TGV pitch、metallization、defect、throughput、supplier 與 customer qualification。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I03
view: industry
from_id: concept:glass-substrate-commercialization
to_id: stage:pilot-line
relation: reaches_stage
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C9
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-11-05
review_due: 2026-09-12
status: active
boundary: Samsung 已揭露 pilot line 與原型；小規模試產線、MOU 與 2027 年後 roadmap 不等於客戶 HVM 或穩定良率。
next_trigger: Pilot prototype 通過客戶 qualification，並轉入合資 production equipment 與實際投產。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I04
view: industry
from_id: concept:glass-substrate-commercialization
to_id: stage:proof-sample
relation: reaches_stage
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C4,MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C8
note_refs:
evidence_state: inference
commercial_stage: sample
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-27
review_due: 2026-08-19
status: active
boundary: SKC 的 production-ready proof sample 與 non-embedding prototype 支持工程樣品階段；production-ready、supplied prototype 與 POC plan 都不等於 production。
next_trigger: 具名 customer qualification、production start、yield 與 repeat order。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I05
view: industry
from_id: concept:glass-substrate-commercialization
to_id: stage:reliability-evaluation
relation: reaches_stage
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C8
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-27
review_due: 2026-08-19
status: active
boundary: Embedding 初始可靠度測試已開始，non-embedding 原型另進入美國通訊公司專案；尚未證實任一路徑通過 qualification、量產或商業出貨。
next_trigger: 分產品路徑公開客戶結果、qualification completion、production start 與 shipment。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I06
view: industry
from_id: concept:glass-substrate-commercialization
to_id: capability:production-yield
relation: requires
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C6,MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C12
note_refs:
evidence_state: inference
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: 新文件仍只到 initial test、prototype 與 POC plan；沒有任何角色的 production yield 數值、分布或成本窗口。
next_trigger: 供應商按產品角色公布 production yield、throughput、scrap／rework 與客戶 acceptance。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I07
view: industry
from_id: concept:glass-substrate-commercialization
to_id: component:organic-substrate
relation: competes_with
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C2
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: 玻璃是有機核心的潛在替代路徑；不同 package、成本與成熟度可能讓兩者長期共存。
as_of: 2026-07-24
review_due: 2026-09-02
status: active
boundary: Intel 的材料比較支持技術差異，不證明全面替代、時間、成本或客戶份額。
next_trigger: 同一 customer package 比較 glass／organic 的 qualification、yield、cost 與 production volume。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I08
view: industry
from_id: concept:glass-substrate-commercialization
to_id: group:material
relation: routes_to
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: Glass composition、metallization、film 與 chemicals 是搜尋入口；沒有 universe 公司具名供貨與財務證據。
next_trigger: 客戶與材料商雙向核對料號、qualification、volume、share 與收入。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I09
view: industry
from_id: concept:glass-substrate-commercialization
to_id: group:pcb
relation: routes_to
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: Package substrate 製造能力是搜尋路由；ABF／PCB 能力不等於 glass core qualification 或訂單。
next_trigger: 具名 glass substrate、customer qualification、production shipment 與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I10
view: industry
from_id: concept:glass-substrate-commercialization
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: Handling、assembly、inspection 與 reliability 形成 OSAT 搜尋入口；沒有具名量產服務與收入。
next_trigger: OSAT 與客戶共同確認 glass substrate package、qualification、yield、shipment 與財務。
-->

<!-- knowledge_edge
edge_id: KG-GLS-C06
view: company
from_id: company:intel
to_id: concept:glass-substrate-commercialization
relation: has_capability
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C11
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-02
review_due: 2026-09-12
status: active
boundary: Intel 的填銅 TGV 試驗結構通過指定熱循環，只支持局部互連研發能力；文件仍將玻璃基板定位為 future development，不是客戶完整產品資格或 HVM。
next_trigger: 具名 package 公開完整 glass-core substrate 樣品、customer qualification、production yield 與 shipment。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I11
view: industry
from_id: concept:glass-substrate-commercialization
to_id: component:glass-carrier
relation: includes
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C10
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: Carrier glass 是製造期間的暫時支撐與剝離路徑；它的產品、出貨或 panel form factor 不能證明 glass core 已被封裝基板採用。
next_trigger: 出貨或客戶文件明確標記 carrier 的製程位置、temporary bond／de-bond、volume 與對應應用。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I12
view: industry
from_id: concept:glass-substrate-commercialization
to_id: component:glass-interposer
relation: includes
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C10,MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C11
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: TGV glass 可作為 RF／interposer 的電性重新分配層；它會留在部分產品中，但仍不等於已整合增層線路的完整 glass-core package substrate。
next_trigger: 同一具名 package 公開 interposer 角色、TGV／RDL 規格、客戶資格、量產良率與出貨。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I13
view: industry
from_id: concept:glass-substrate-commercialization
to_id: component:substrate
relation: integrated_with
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C10,MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C12
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: Glass core 只是完整封裝基板的核心材料；還要整合金屬化、兩側增層線路、組裝與客戶產品測試，才能討論完整基板量產。
next_trigger: 客戶與供應商雙向核對完整 substrate stack、package product、qualification、yield 與 repeat shipment。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I14
view: industry
from_id: concept:glass-substrate-commercialization
to_id: stage:test-vehicle
relation: reaches_stage
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C11
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-02
review_due: 2026-09-12
status: active
boundary: 局部 TGV 試驗結構的熱循環結果只驗證指定構造與條件；沒有完整客戶 package、qualification、production yield、shipment 或財務證據。
next_trigger: 把同一結構整合進具名完整封裝，公開客戶資格、壽命條件、量產良率與出貨。
-->
