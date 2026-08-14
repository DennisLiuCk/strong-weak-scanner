# SiC 到 AI BBU／PSU 七關資格鏈知識圖譜

本圖把元件短路／stress evaluation、供應商資料、converter reference design、system reliability、
mixed-source customer qualification 及商業歸因分開，並用四個 reference plane 區分 rack available
fault current、converter 路徑、device waveform 與 protection／clearing。公開證據已支持相鄰關卡，尚未
支持 JEP203／JEP204 已改寫本輪平台驗收或台灣公司財務。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: sic-ai-power-qualification
root_node_id: concept:sic-ai-power-qualification
label: SiC 到 AI BBU／PSU 七關資格鏈
summary: 從 application stress JEP203 JEP204 supplier data reference design DFMEA derating fault 四參考面 mixed-source qualification 追到 deployment 與財務 避免把 rack kA device ampere microseconds guideline reference design 或單一 adoption 拼成 platform acceptance 與收入。
article_ids: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION
status: active
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-C01
view: company
from_id: company:infineon
to_id: concept:sic-ai-power-qualification
relation: has_capability
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C6
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: limited_source
exclusivity_scope: Infineon 公開的是全 Infineon BOM 的 N=1 24 kW HV BBU reference design；沒有第二個 supplier BOM 依同一 test contract 重現。
as_of: 2026-06-02
review_due: 2026-09-15
status: active
boundary: Reference design 支持具名 SiC topology part 與 engineering role 不等於 JEP mapping customer qualification mixed-source production deployment 或財務。
next_trigger: 具名平台以固定 JEP 與 system matrix 驗證 Infineon part 並公布 alternate-source production result。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-C02
view: company
from_id: company:rohm
to_id: concept:sic-ai-power-qualification
relation: names_application
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C7
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: limited_source
exclusivity_scope: ROHM 單方具名 SCT4013DLL 與 AI BBU application 但未具名 BBU maker customer platform 或第二來源。
as_of: 2026-06-03
review_due: 2026-09-15
status: active
boundary: Supplier-reported adopted 只建立產品應用入口 不證明 JEP qualification production volume broad penetration 份額或財務。
next_trigger: 買方與 BBU maker 雙向確認 SCT4013DLL platform revision qualification shipment 及 volume。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-C03
view: company
from_id: company:2308
to_id: concept:sic-ai-power-qualification
relation: plans_production
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C8,MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C9,MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C10
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: limited_source
exclusivity_scope: Delta 自有文件與 ROHM-hosted management dialogue 支持高壓產品 planned SiC PSU adoption 及相鄰 SST deployment；沒有 customer-side BBU PSU JEP confirmation。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: 公司 capability planning 與 SST deployment 不等於 BBU PSU JEP203 JEP204 customer qualification production shipment 或可分辨財務。
next_trigger: 台達與買方對上同一 BBU PSU SiC part JEP crosswalk acceptance production BOM 出貨及收入分母。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I01
view: industry
from_id: organization:jedec
to_id: concept:sic-ai-power-qualification
relation: owns_platform
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: JEDEC JC-70 由多家公司與技術角色共同參與標準化 但 publication 不屬任何單一 device supplier 的排他 qualification。
as_of: 2026-06-03
review_due: 2026-09-15
status: active
boundary: JEDEC 維護 JEP203 與 JEP204 的 device evaluation framework 不替特定 AI BBU PSU 設 pass threshold 或認證產品。
next_trigger: 取得兩份可定位全文 revision procedure circuit condition sample failure criterion 與 reporting contract。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I03
view: industry
from_id: organization:open-compute-project
to_id: concept:sic-ai-power-qualification
relation: tests
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C2,MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C3,MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C4,MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C5
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: 三份公開規格由不同時期與參與者建立 system fault reliability quality 及 mixed-source contract 不指定排他 SiC supplier。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: OCP 文件支持 platform qualification 骨架 但三份固定版本沒有 JEP203 JEP204 SiC 或 silicon carbide 文字橋。
next_trigger: OCP 新 revision 增加 normative JEP crosswalk device condition system action acceptance 與 change control。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I04
view: industry
from_id: concept:sic-ai-power-qualification
to_id: component:sic-power
relation: uses_component
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C6,MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C7
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Infineon 與 ROHM 提供兩條獨立 SiC device design application evidence 但 test contract 與 commercial stage 不同。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: SiC 在具名 BBU design adoption 中出現 不代表所有 BBU PSU stage 固定使用 SiC 或材料份額已定。
next_trigger: 同一 production platform 公布 SiC part count alternate technology qualification volume 及 failure results。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I05
view: industry
from_id: concept:sic-ai-power-qualification
to_id: stage:sic-application-stress-envelope
relation: passes_through
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C2,MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C11
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: Diablo 400 公開 system power dynamic load backup time 與 fault current 但各 application 仍需自己的 component waveform。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: Rack fault envelope 不能直接當成 MOSFET test current pulse width Tj dv dt 或 lifetime condition。
next_trigger: 固定 BBU PSU revision 公開 normal transient fault storage waveform tolerance 與 repetition envelope。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I06
view: industry
from_id: concept:sic-ai-power-qualification
to_id: stage:sic-device-evaluation
relation: passes_through
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C1
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: JEP203 JEP204 建立共同 device evaluation 語言 但 application pass line 由使用者與 qualification contract 另定。
as_of: 2026-06-03
review_due: 2026-09-15
status: active
boundary: Guideline publication 不等於 supplier part passed platform acceptance 或 field reliability 已驗證。
next_trigger: 具名 part lot 依固定 JEP revision 公開 circuit raw waveform failure criterion 與 pass fail report。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I07
view: industry
from_id: concept:sic-ai-power-qualification
to_id: stage:sic-supplier-qualification-data
relation: passes_through
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C11
note_refs:
evidence_state: inference
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: 本輪 supplier releases 具名 part 或 design 但沒有可重算 JEP raw data lot sample failure analysis 與 customer threshold。
next_trigger: Supplier qualification pack 對上 part lot package driver raw waveform failure criterion failure analysis 與 revision。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I08
view: industry
from_id: concept:sic-ai-power-qualification
to_id: stage:sic-converter-validation
relation: passes_through
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C6
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: limited_source
exclusivity_scope: Infineon N=1 reference design 已把 SiC device driver sensor MCU magnetics 與 protection 組成 converter 但不是跨廠 customer result。
as_of: 2026-06-02
review_due: 2026-09-15
status: active
boundary: Converter reference validation 不等於 system fault coordination mixed-source qualification production deployment 或 financial attribution。
next_trigger: 客戶硬體在固定 corner fault thermal EMI matrix 重現並公布 pass fail 與 root cause。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I09
view: industry
from_id: concept:sic-ai-power-qualification
to_id: stage:sic-system-reliability
relation: passes_through
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C3,MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C4
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: OCP PSU 與 BBU specifications 公開 derating DFMEA MTBF HALT burn-in ORT 等多種 system reliability 路徑。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: System reliability contract 存在不證明 SiC part 已被選中 也不把 normative MTBF target 改成 field statistics。
next_trigger: 高壓 BBU PSU 把 device result protection timing derating DFMEA HALT MTBF 與 service action 接成同一報告。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I10
view: industry
from_id: concept:sic-ai-power-qualification
to_id: stage:sic-mixed-source-qualification
relation: passes_through
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C3,MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C11
note_refs:
evidence_state: inference
commercial_stage: qualification
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: OCP 12 kW PSU 要求 prime 與 alternate part mixed-source builds 但未指定 SiC 或公開各來源結果。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: Mixed-source requirement 不等於任一 SiC supplier 已通過 或不同材料 topology 可直接替換。
next_trigger: 固定 platform 在 EVT DVT PVT shelf rack 用至少兩個 device source 公開共同 test contract 與結果。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I11
view: industry
from_id: concept:sic-ai-power-qualification
to_id: stage:sic-commercial-attribution
relation: passes_through
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C13
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: 沒有 universe 公司同一 SiC BBU PSU part JEP system qualification production BOM shipment revenue cost 或 margin 閉環。
next_trigger: 買方與公司雙向確認同料號模組平台資格出貨期間數量單價及可辨識財務分母。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I12
view: industry
from_id: concept:sic-ai-power-qualification
to_id: standard:ipc-9592b
relation: uses_standard
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C3,MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C4
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: 2026 PSU 與 2023 BBU specifications 都明文引用 IPC-9592B 作 derating reliability quality 或 test baseline。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: IPC-9592B system process reference 不替 SiC JEP procedure 或具名 part customer acceptance 背書。
next_trigger: 高壓 SiC BBU PSU qualification matrix 對齊 IPC-9592B 與 JEP203 JEP204 的責任分界。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I13
view: industry
from_id: concept:sic-ai-power-qualification
to_id: standard:telcordia-sr332
relation: uses_standard
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C3,MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C4
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: 12 kW PSU 與 48 V BBU 用 SR-332 建立不同條件的 reliability prediction target 並非同一實測樣本。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: Calculated 或 demonstrated MTBF requirement 不等於本文 field observation 也不能歸因單一 SiC part。
next_trigger: 具名 product 公開 model assumption demonstration sample confidence field hours failure count 與 device contribution。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I14
view: industry
from_id: concept:sic-ai-power-qualification
to_id: capability:overcurrent-protection
relation: requires
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C2,MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C3,MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C4
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: Diablo PSU 與 BBU 文件都需要 fault overcurrent short-circuit response 但可由不同 sensing switching fuse breaker control topology 實作。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: System protection requirement 不指定唯一 SiC switch clearing time supplier 或 commercial value。
next_trigger: 同一 product 公開 fault location sensor threshold delay device waveform fuse breaker selectivity retry latch 與 service result。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I15
view: industry
from_id: concept:sic-ai-power-qualification
to_id: standard:jep203
relation: uses_standard
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C12
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: 本輪三份 OCP 規格沒有 JEP203 或 JEP 203 文字命中 尚未建立 AI BBU PSU platform adoption edge。
next_trigger: 固定平台 revision normative section 引用 JEP203 並對上 application waveform pass criteria system timing 與 acceptance report。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I16
view: industry
from_id: concept:sic-ai-power-qualification
to_id: standard:jep204
relation: uses_standard
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C12
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: 本輪三份 OCP 規格沒有 JEP204 或 JEP 204 文字命中 尚未建立 stress catalog 到 system qualification 的 crosswalk。
next_trigger: 平台把 JEP204 procedure 對到 relevant application stress sample pass fail derating DFMEA life model 與 mixed-source test。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I17
view: industry
from_id: concept:sic-ai-power-qualification
to_id: group:power
relation: routes_to
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C13
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: SiC device driver sensor package 與 qualification data 只建立 power 族群搜尋路由 不建立 universe 公司受惠份額訂單收入或毛利。
next_trigger: 買方與台灣 power 公司雙向確認具名 part JEP system qualification production shipment 及財務分母。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I18
view: industry
from_id: concept:sic-ai-power-qualification
to_id: group:powersupply
relation: routes_to
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C13
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: BBU PSU integration mixed-source qualification 與 Delta 具名入口不等於台灣電源公司 JEP adoption production shipment 或可分辨財務。
next_trigger: Platform customer 與 powersupply 公司對上同一 module revision SiC part qualification BOM 出貨與收入毛利。
-->

<!-- knowledge_edge
edge_id: KG-SICQUAL-I19
view: industry
from_id: concept:sic-ai-power-qualification
to_id: stage:sic-short-circuit-coordination
relation: passes_through
claim_refs: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C14,MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C15,MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C16
note_refs:
evidence_state: inference
commercial_stage: qualification
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: OCP 固定 system available fault-current envelope，onsemi 與 Infineon 固定 device／driver timing trade-off 與一個 lab example；三者不是同一 product、fault event 或 customer report。
as_of: 2026-08-14
review_due: 2026-09-15
status: active
boundary: 四 reference plane 是跨文件的研究 crosswalk；10–40 kA、約 250 A、1.2／2／3 microseconds 不可相除相減，也不證明 AI BBU／PSU system safety、JEP adoption、mixed-source、field reliability 或財務。
next_trigger: 具名 production BBU／PSU 用同一 platform／board revision 與 event ID 公開 fault location、source impedance、converter current path、VDS／ID／VGS／Tj raw waveform、DESAT／driver timing、clamp／fuse-breaker clearing、tolerance、pass／fail 與 post-fault disposition。
-->
