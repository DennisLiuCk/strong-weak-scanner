# 半導體 PFAS 七關曝險鏈知識圖譜

本圖把歐盟限制、美國歷史申報、半導體多用途、替代再驗證及公司財務歸因分開。
4770、4755 只畫到公開產品／能力入口；最終法規適用、近期成本、中斷與受惠仍未證實。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: semiconductor-pfas-exposure
root_node_id: concept:semiconductor-pfas-exposure
label: 半導體 PFAS 七關曝險鏈
summary: 從 substance identity process function product form jurisdiction duty derogation transition change qualification 追到 company site product financial attribution 避免把提案 申報 含氟產品或替代研發直接寫成禁用與獲利。
article_ids: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE
status: active
-->

<!-- knowledge_edge
edge_id: KG-PFAS-C01
view: company
from_id: company:4770
to_id: concept:semiconductor-pfas-exposure
relation: produces
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C8
note_refs: 4770#S1
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: limited_source
exclusivity_scope: 公司公開氟素樹脂半成品 內襯設備 管件及應用材料並服務高純電子化學品 但沒有 specific PFAS legal exposure 的供應商比較。
as_of: 2026-08-12
review_due: 2026-10-15
status: active
boundary: 具名 fluoropolymer product 支持產品位置 不等於 specific CAS EU US obligation derogation replacement need order revenue or margin。
next_trigger: 公司揭露固定 product grade composition customer jurisdiction legal crosswalk qualification impact and financial denominator。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-C02
view: company
from_id: company:4770
to_id: concept:semiconductor-pfas-exposure
relation: names_application
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C10
note_refs: 4770#S1
evidence_state: inference
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-10-15
status: active
boundary: 上品只作 fluoropolymer sealing machinery technical-textile 相鄰搜尋入口 不代表已受最終規則衝擊或因替代困難受惠。
next_trigger: Substance product site customer law qualification and financial numerator denominator 全部對上。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-C03
view: company
from_id: company:4755
to_id: concept:semiconductor-pfas-exposure
relation: has_capability
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C9
note_refs: 4755#S1,4755#S4
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-10-15
status: active
boundary: 含氟界面活性劑是 R&D entry 不自動等於 covered PFAS PFAS-free substitute customer qualification production or revenue。
next_trigger: 公司公開 structure definition baseline formulation qualification POR volume and attributed financial result。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-C04
view: company
from_id: company:4755
to_id: concept:semiconductor-pfas-exposure
relation: names_application
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C10
note_refs: 4755#S1,4755#S4
evidence_state: inference
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-10-15
status: active
boundary: Process chemistry capability 只形成 substance recipe qualification 搜尋路由 不證明 legal exposure substitute win or financial materiality。
next_trigger: Supplier company and customer documents jointly identify chemistry law qualification production volume price cost and company denominator。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I01
view: industry
from_id: organization:echa
to_id: concept:semiconductor-pfas-exposure
relation: raises_need
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C2,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C3
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: ECHA 科學委員會與程序支援由會員國專家及 dossier submitters 多方參與 最終決策仍在 Commission 與 Member States。
as_of: 2026-08-12
review_due: 2026-12-15
status: active
boundary: ECHA opinion and use mapping 不等於 final REACH legal text effective date or company exemption。
next_trigger: SEAC final Commission proposal REACH Committee adoption and Official Journal publication。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I02
view: industry
from_id: organization:us-epa
to_id: concept:semiconductor-pfas-exposure
relation: raises_need
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C5
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: EPA 維護聯邦 TSCA reporting rule 但 covered entities 包含多種製造者與進口者 且 scope revision 仍在程序中。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: Historical reporting requirement 不是 use prohibition and current start date depends on forthcoming revision effective date。
next_trigger: EPA final scope revision effective date submission window exemptions and updated guidance。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I03
view: industry
from_id: process:eu-reach-pfas-restriction
to_id: concept:semiconductor-pfas-exposure
relation: raises_need
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C2,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C3
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: Broad restriction targeted derogation and emission control options create multiple compliance and substitution paths rather than a sole winner。
as_of: 2026-08-12
review_due: 2026-12-15
status: active
boundary: Proposed and draft paths do not establish final sector term company duty cost disruption or beneficiary。
next_trigger: Fixed legal text maps each use sector to scope derogation transition conditions and effective date。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I04
view: industry
from_id: process:us-tsca-pfas-reporting
to_id: concept:semiconductor-pfas-exposure
relation: raises_need
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C5
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: One-time historical reporting spans manufacturers and importers while proposed exemptions and final timing remain regulatory questions。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: Reporting inventory effort cannot be translated into a ban replacement order or revenue without product importer and financial evidence。
next_trigger: Final scope rule plus company import inventory reporting and attributable compliance cost disclosure。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I05
view: industry
from_id: concept:semiconductor-pfas-exposure
to_id: stage:pfas-substance-identity
relation: passes_through
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C1,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C12
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-10-15
status: active
boundary: Company disclosures name material families or R&D items but do not expose complete substance structure grade additive concentration and supplier inventory。
next_trigger: Auditable substance inventory maps each structure or identifier to product grade batch concentration and supplier。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I06
view: industry
from_id: concept:semiconductor-pfas-exposure
to_id: stage:pfas-process-function
relation: passes_through
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C4,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C6
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: ECHA SEMI and SIA separately map multiple semiconductor uses while no single source claims one universal function。
as_of: 2026-08-12
review_due: 2026-12-15
status: active
boundary: Use category existence does not prove each company uses each PFAS or that alternatives share qualification paths。
next_trigger: Substance-to-recipe tool module function failure-mode and release-path crosswalk for fixed products。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I07
view: industry
from_id: concept:semiconductor-pfas-exposure
to_id: stage:pfas-product-form
relation: passes_through
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C1,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C4
note_refs:
evidence_state: inference
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-10-15
status: active
boundary: ECHA sector split implies product form matters but company mixture article spare-part and concentration determinations are missing。
next_trigger: Fixed BOM SDS declaration and legal classification identify substance mixture article spare and emission forms。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I08
view: industry
from_id: concept:semiconductor-pfas-exposure
to_id: stage:pfas-jurisdiction-duty
relation: passes_through
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C2,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C5,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C12
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: No universe company product site import or customer path is mapped to a fixed final duty。
next_trigger: Legal review maps each product site importer and market placement to final versioned obligations。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I09
view: industry
from_id: concept:semiconductor-pfas-exposure
to_id: stage:pfas-derogation-transition
relation: passes_through
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C3,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C4,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C11
note_refs:
evidence_state: unverified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-12-15
status: active
boundary: No final use-specific exemption duration concentration emission spare-part or reporting term exists for company attribution。
next_trigger: Adopted text provides article clause use sector conditions transition and effective date。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I10
view: industry
from_id: concept:semiconductor-pfas-exposure
to_id: stage:pfas-change-qualification
relation: passes_through
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C7
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: limited_source
exclusivity_scope: PAG photoresist paper demonstrates a detailed qualification route but does not cover every PFAS use or fab。
as_of: 2026-08-12
review_due: 2026-10-15
status: active
boundary: Generic industry timeline and workflow are not observed cross-fab samples and cannot forecast company orders or all substitutions。
next_trigger: Fixed baseline candidate test matrix pass fail pilot yield POR date and customer approval for named product。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I11
view: industry
from_id: concept:semiconductor-pfas-exposure
to_id: stage:pfas-company-financial-attribution
relation: passes_through
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C10,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C12,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C13
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-10-15
status: active
boundary: No substance product site customer qualification volume price cost revenue or margin denominator closes the financial chain。
next_trigger: Supplier buyer and company filings align the same product period numerator denominator and attribution status。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I12
view: industry
from_id: concept:semiconductor-pfas-exposure
to_id: component:pfas-process-chemistry
relation: uses_component
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C6,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C7,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C9
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Photolithography wet chemistry and company R&D show multiple chemistry roles rather than a sole formulation path。
as_of: 2026-08-12
review_due: 2026-10-15
status: active
boundary: Process chemistry category does not establish covered substance alternative performance qualification production or market share。
next_trigger: Named chemistry formulation layer qualification customer production and financial disclosure。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I13
view: industry
from_id: concept:semiconductor-pfas-exposure
to_id: component:fluorinated-process-gases
relation: uses_component
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C4,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C6
note_refs:
evidence_state: verified
commercial_stage: production
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: Industry documents name multiple etch deposition and chamber-clean gases with different functions and emissions paths。
as_of: 2026-08-12
review_due: 2026-12-15
status: active
boundary: Gas use existence does not prove final restriction alternative availability abatement performance or universe company exposure。
next_trigger: Fixed gas recipe emissions baseline substitute abatement qualification and supplier product disclosure。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I14
view: industry
from_id: concept:semiconductor-pfas-exposure
to_id: component:fluoropolymer-process-components
relation: uses_component
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C4,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C6,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C8
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: multi_source
exclusivity_scope: SEMI use mapping and Allied Supreme product evidence identify articles across different equipment and facility roles。
as_of: 2026-08-12
review_due: 2026-10-15
status: active
boundary: Fluoropolymer component category spans multiple grades forms and legal sectors and does not imply one substitution or beneficiary。
next_trigger: Product-grade inventory final law sector customer qualification alternative supply and financial denominator。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I15
view: industry
from_id: concept:semiconductor-pfas-exposure
to_id: component:fluorinated-thermal-fluids
relation: uses_component
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C4,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C6
note_refs:
evidence_state: verified
commercial_stage: production
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: Heat-transfer fluid refrigerant and immersion or soldering uses have different mapping boundaries and potential alternatives。
as_of: 2026-08-12
review_due: 2026-12-15
status: active
boundary: Category existence does not identify exact fluid equipment loop jurisdiction replacement safety or company supplier。
next_trigger: Named fluid loop conditions release path alternative safety qualification and final use-specific legal treatment。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I16
view: industry
from_id: concept:semiconductor-pfas-exposure
to_id: group:material
relation: routes_to
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C8,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C9,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C10
note_refs: 4755#S1,4770#S1
evidence_state: inference
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-10-15
status: active
boundary: Named fluoropolymer and fluorinated-chemistry entries support research routing only not material-group cost disruption beneficiary or ranking。
next_trigger: Company and customer jointly disclose fixed substance product law qualification commercial result and financial denominator。
-->

<!-- knowledge_edge
edge_id: KG-PFAS-I17
view: industry
from_id: concept:semiconductor-pfas-exposure
to_id: group:semiequip
relation: routes_to
claim_refs: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C4,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C6,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C12,MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE#C13
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-12-15
status: active
boundary: Equipment PFAS use taxonomy exists but no universe semiequip company has a named part fluid law change qualification order or financial line。
next_trigger: Equipment supplier and customer publish PFAS BOM substitution or conditional-use plan validation service impact production order and financial attribution。
-->
