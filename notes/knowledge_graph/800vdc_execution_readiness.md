# 800VDC 七關執行準備度知識圖譜

本圖把平台路線圖、設施轉換、介面與冗餘、安全標準、子系統資格、場站驗收及量產財務分開。
七關是研究端的證據分類，不是單一標準或認證；任何一條公司線都不代表已取得訂單或獲利。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: 800vdc-execution-readiness
root_node_id: concept:800vdc-execution-readiness
label: 800VDC 七關執行準備度
summary: 從 architecture timing facility boundary interoperability redundancy codes subsystem qualification site commissioning 追到 production deployment 與財務 避免把 logo demo qualification 或 MOU 當成 full-scale 商用。
article_ids: MI-2026-08-01-800VDC-EXECUTION-READINESS
status: active
-->

<!-- knowledge_edge
edge_id: KG-8ER-C01
view: company
from_id: company:nvidia
to_id: concept:800vdc-execution-readiness
relation: owns_platform
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C1
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: multi_source
exclusivity_scope: NVIDIA 提供平台架構與 2027 時鐘 但公開合作名單涵蓋多家 silicon power system 與 facility provider 並非排他供應。
as_of: 2026-07-31
review_due: 2026-09-12
status: active
boundary: 平台時鐘不等於客戶場站完成 qualification commissioning production deployment 或供應商收入。
next_trigger: NVIDIA 固定 production architecture qualification contract 與具名 site deployment denominator。
-->

<!-- knowledge_edge
edge_id: KG-8ER-C02
view: company
from_id: company:2308
to_id: concept:800vdc-execution-readiness
relation: plans_deployment
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C11
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: limited_source
exclusivity_scope: Delta 與 X LABS 的 MOU 是單一合作框架且未揭露排他條款 具約束力採購或 alternate supplier。
as_of: 2026-07-14
review_due: 2026-09-12
status: active
boundary: Expected 100MW SST deployment 是 MOU 規劃量 不是已部署樣本 800V rack acceptance 出貨收入或毛利。
next_trigger: MOU 轉固定 project contract construction as built commissioning accepted MW shipment 與財務分母。
-->

<!-- knowledge_edge
edge_id: KG-8ER-C03
view: company
from_id: company:onsemi
to_id: concept:800vdc-execution-readiness
relation: cites_demand
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C12
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: onsemi 描述 SST early commercialization 與多種 SiC voltage class 但 NVIDIA ecosystem 明示多家 silicon 與 power provider。
as_of: 2026-07-14
review_due: 2026-09-12
status: active
boundary: Supplier industry positioning 不等於 hyperscaler qualification production deployment 市占或台灣公司財務。
next_trigger: 具名 customer platform 固定 onsemi device SST revision qualification shipment deployment 與 field result。
-->

<!-- knowledge_edge
edge_id: KG-8ER-I01
view: industry
from_id: organization:open-compute-project
to_id: concept:800vdc-execution-readiness
relation: tests
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C7,MI-2026-08-01-800VDC-EXECUTION-READINESS#C8
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: OCP workstream 是多方共同架構與標準化入口 並明示 detailed component specifications 仍需由 separate workstreams 完成。
as_of: 2026-03-30
review_due: 2026-09-12
status: active
boundary: White paper 支持 stage 與問題清單 不等於共同 production specification pass report 或 deployed site。
next_trigger: OCP 發布 fixed revision voltage band redundancy protection commissioning 與 component handoff specification。
-->

<!-- knowledge_edge
edge_id: KG-8ER-I02
view: industry
from_id: concept:800vdc-execution-readiness
to_id: stage:800v-architecture-roadmap
relation: passes_through
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C1
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: multi_source
exclusivity_scope: 2027 Kyber 是 NVIDIA 平台時鐘 並不排除其他平台採不同電壓 transition 或 schedule。
as_of: 2026-07-31
review_due: 2026-09-12
status: active
boundary: Architecture need 與 date 只完成第一關 不證明後續 facility qualification production 或財務。
next_trigger: Fixed platform architecture release production date rack count power denominator 與 change control。
-->

<!-- knowledge_edge
edge_id: KG-8ER-I03
view: industry
from_id: concept:800vdc-execution-readiness
to_id: stage:800v-facility-transition
relation: passes_through
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C7
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: OCP Stage 1 2 3 與 NVIDIA hybrid bridge 提供多條 transition scope 不是唯一 end state 或固定順序。
as_of: 2026-03-30
review_due: 2026-09-12
status: active
boundary: 三階段描述 DC 覆蓋範圍 不是 product maturity rank customer qualification 或 deployment result。
next_trigger: 具名 site 固定 Stage isolation conversion energy storage cooling network 與 owner boundary。
-->

<!-- knowledge_edge
edge_id: KG-8ER-I04
view: industry
from_id: concept:800vdc-execution-readiness
to_id: stage:800v-interface-redundancy
relation: passes_through
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C8
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: Voltage band redundancy fault clearing 與 maintenance 可由不同 topology 與多家設備協作完成 不支持單一排他解。
as_of: 2026-03-30
review_due: 2026-09-12
status: active
boundary: OCP 指出 maintenance bypass replacement line inductance 與 cyclic load 問題 但沒有共同 production design 或 field reliability。
next_trigger: Fixed voltage band fault matrix redundancy topology maintenance sequence interoperability test 與 pass fail。
-->

<!-- knowledge_edge
edge_id: KG-8ER-I05
view: industry
from_id: concept:800vdc-execution-readiness
to_id: stage:800v-standards-readiness
relation: passes_through
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C9
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: UL OCP IEC IEEE NEC 與地方 AHJ 各自負責不同 standard code 與 approval domain 無單一機構可替其他邊界背書。
as_of: 2026-01-13
review_due: 2026-09-12
status: active
boundary: Gap analysis 與 workstream 啟動不等於 standards revised adopted commissioned 或 workers qualified。
next_trigger: Fixed revision code adoption AHJ approval training credential commissioning practice 與具名 site record。
-->

<!-- knowledge_edge
edge_id: KG-8ER-I06
view: industry
from_id: concept:800vdc-execution-readiness
to_id: stage:800v-subsystem-qualification
relation: passes_through
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C10
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: NVIDIA BESS guide 是 partner run qualification 且 safety cyber site equipment 各有不同 owner 與 standard boundary。
as_of: 2026-05-28
review_due: 2026-09-12
status: active
boundary: BESS evidence packet 是 boundary 教材 不是 power rack BBU protection facility 的共同 qualification 或 pass result。
next_trigger: 每個 800V subsystem 固定 revision scope raw test pass fail change control 與 owner acceptance。
-->

<!-- knowledge_edge
edge_id: KG-8ER-I07
view: industry
from_id: concept:800vdc-execution-readiness
to_id: stage:800v-site-acceptance
relation: passes_through
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C9,MI-2026-08-01-800VDC-EXECUTION-READINESS#C10,MI-2026-08-01-800VDC-EXECUTION-READINESS#C13
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: Standards work 與 BESS boundary 證明 site commissioning 必須獨立查核 不證明任何具名 800V site 已通過。
next_trigger: As built model full load no load fault protection control utility coordination customer acceptance 與 operating hours。
-->

<!-- knowledge_edge
edge_id: KG-8ER-I08
view: industry
from_id: concept:800vdc-execution-readiness
to_id: stage:800v-commercial-attribution
relation: passes_through
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C5,MI-2026-08-01-800VDC-EXECUTION-READINESS#C11,MI-2026-08-01-800VDC-EXECUTION-READINESS#C13
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: MOU expected MW 與事業群營收沒有同產品 deployment shipment revenue cost margin denominator 無法歸因 800V 財務。
next_trigger: 買方與供應商雙向確認同 project product site accepted MW production shipment period revenue cost margin 與 cash。
-->

<!-- knowledge_edge
edge_id: KG-8ER-I09
view: industry
from_id: concept:800vdc-execution-readiness
to_id: concept:800v-power-tree
relation: integrated_with
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C13
note_refs:
evidence_state: inference
commercial_stage: integration
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: SST PSU BBU IBC protection 與 point of load 可採多材料多 topology 與多供應商組合。
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 七關決定證據成熟度 功率樹決定元件位置 兩者都不自行證明 fixed production BOM 或 company revenue。
next_trigger: 同一 production site 與 rack 公布完整 power tree qualification deployment 及 financial attribution。
-->

<!-- knowledge_edge
edge_id: KG-8ER-I10
view: industry
from_id: concept:800vdc-execution-readiness
to_id: concept:800v-protection-layers
relation: integrated_with
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C8,MI-2026-08-01-800VDC-EXECUTION-READINESS#C9
note_refs:
evidence_state: inference
commercial_stage: integration
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: Interlock earthing overcurrent ground fault hot swap 與 service procedures 分屬多個元件系統與 regulatory owner。
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 標準與介面缺口使 protection 成為必要關卡 不證明元件顆數 supplier BOM qualification 或收入。
next_trigger: Production site fault matrix protection timing isolation scope service action qualified parts 與 field log。
-->

<!-- knowledge_edge
edge_id: KG-8ER-I11
view: industry
from_id: concept:800vdc-execution-readiness
to_id: concept:ai-power-buffering
relation: integrated_with
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C10
note_refs:
evidence_state: inference
commercial_stage: integration
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: BBU CBU BESS 與 grid control 負責不同時間尺度且可由多家設備與 topology 共同完成。
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: BESS qualification 只建立一個子系統邊界 不表示 rack buffer facility storage 與 grid response 已協同通過。
next_trigger: 同一 site 公開 multi timescale buffering control protection qualification commissioning 與 operating result。
-->

<!-- knowledge_edge
edge_id: KG-8ER-I12
view: industry
from_id: concept:800vdc-execution-readiness
to_id: group:powersupply
relation: routes_to
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C3,MI-2026-08-01-800VDC-EXECUTION-READINESS#C5,MI-2026-08-01-800VDC-EXECUTION-READINESS#C11,MI-2026-08-01-800VDC-EXECUTION-READINESS#C13
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 光寶 validation 與台達 MOU 形成查找路由 但沒有同產品 customer acceptance production shipment revenue margin 閉環。
next_trigger: 2301 2308 與買方對上 product revision site qualification accepted volume shipment revenue cost margin 與 cash。
-->

<!-- knowledge_edge
edge_id: KG-8ER-I13
view: industry
from_id: concept:800vdc-execution-readiness
to_id: group:power
relation: routes_to
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C5,MI-2026-08-01-800VDC-EXECUTION-READINESS#C12,MI-2026-08-01-800VDC-EXECUTION-READINESS#C13
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: SST semiconductor 與 protection 形成 power 族群搜尋路由 本輪未證實 8255 或其他 universe 公司具名 800V qualification order 或財務。
next_trigger: 買方與台灣公司雙向確認具名 device package stage qualification production BOM shipment 與財務分母。
-->

<!-- knowledge_edge
edge_id: KG-8ER-I14
view: industry
from_id: concept:800vdc-execution-readiness
to_id: group:thermal
relation: routes_to
claim_refs: MI-2026-08-01-800VDC-EXECUTION-READINESS#C7,MI-2026-08-01-800VDC-EXECUTION-READINESS#C13
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: OCP Stage 2 可把 cooling 納入 DC IT module 只形成 thermal 搜尋路由 不證明 CDU 電壓架構 qualification 台廠內容量或毛利。
next_trigger: 具名 site 公布 cooling power control boundary qualification deployment 與 universe company financial evidence。
-->
