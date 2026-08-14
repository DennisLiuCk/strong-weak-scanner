# Custom HBM 客製範圍與商用階梯

<!-- knowledge_graph_meta
schema_version: 1
graph_id: custom-hbm-scope-ladder
root_node_id: concept:custom-hbm-commercialization
label: Custom HBM 客製範圍與商用階梯
summary: 顯示 Samsung SK hynix 與 Micron 各自揭露的客製入口、工作搬移效能分母及 sample qualification production 門檻；不能用來比較領先 市占或台灣公司收入。
article_ids: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER
status: active
-->

<!-- knowledge_edge
edge_id: KG-CHBM-C01
view: company
from_id: company:samsung-electronics
to_id: concept:custom-hbm-commercialization
relation: samples
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-02-12
review_due: 2026-09-15
status: active
boundary: Samsung 公開的是 2027 客戶樣品 roadmap；不是樣品已交付 客戶已 qualification 或產品已量產。
next_trigger: Samsung 與客戶雙方公布實體 custom HBM sample 產品世代 客製欄位及測試條件。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-C02
view: company
from_id: company:sk-hynix
to_id: concept:custom-hbm-commercialization
relation: has_capability
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-27
review_due: 2026-09-15
status: active
boundary: GTC 展示支持 Stream DQ 位於 base die 與 preprocessing 搬移；不證明客戶資格 量產或跨廠效能領先。
next_trigger: 具名客戶與 SK hynix 公布可重現 workload qualification 及量產結果。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-C03
view: company
from_id: company:micron
to_id: concept:custom-hbm-commercialization
relation: develops_ip
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C4
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-09-23
review_due: 2026-09-23
status: active
boundary: Micron 揭露 HBM4E 客製 base logic die 選項與 TSMC 分工；較高毛利仍是預期而非已實現結果。
next_trigger: Micron 公布具名客戶 qualification 量產與可核對的 NRE 售價 良率或毛利。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I01
view: industry
from_id: concept:custom-hbm-commercialization
to_id: product:custom-hbm
relation: includes
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C5
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-15
status: active
boundary: Custom HBM 是多種客製對象的集合；本線不建立共同規格或供應商排名。
next_trigger: 產業形成可共同核對的產品世代 客製欄位與 qualification 定義。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I02
view: industry
from_id: concept:custom-hbm-commercialization
to_id: component:logic-base-die
relation: uses_component
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C3,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C4
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-27
review_due: 2026-09-15
status: active
boundary: SK hynix 與 Micron 資料把 base die 放入各自客製路徑；不表示架構 定義或功能完全相同。
next_trigger: 公開 die function 介面 PPA 熱與客戶 qualification 的共同測試邊界。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I03
view: industry
from_id: concept:custom-hbm-commercialization
to_id: capability:workload-offload
relation: includes
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-27
review_due: 2026-09-15
status: active
boundary: 只支持 SK hynix 展示的 preprocessing 搬移方向；不是所有 custom HBM 的必要功能。
next_trigger: 客戶端可重現 workload 與端到端 latency power thermal 結果。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I04
view: industry
from_id: concept:custom-hbm-commercialization
to_id: process:customer-codesign
relation: requires
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C2,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C4
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-15
status: active
boundary: 客戶別規格與客製 base logic die 推導共同設計需求；不證明任何具名客戶 NRE 或獨家關係。
next_trigger: 供應商與客戶雙向揭露設計範圍 tape-out qualification 與責任分工。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I05
view: industry
from_id: concept:custom-hbm-commercialization
to_id: stage:custom-hbm-sample
relation: passes_through
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-02-12
review_due: 2026-09-15
status: active
boundary: 2027 是 Samsung roadmap；不能套用到所有公司或視為已完成節點。
next_trigger: 實體 sample shipment 與接收方 測試條件及產品世代。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I06
view: industry
from_id: concept:custom-hbm-commercialization
to_id: stage:custom-hbm-qualification
relation: passes_through
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C6
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-15
status: active
boundary: Qualification 是尚未被三家公司以共同口徑證實的未來節點。
next_trigger: 客戶與供應商雙方公布 qualification 範圍 結果與後續量產決策。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I07
view: industry
from_id: concept:custom-hbm-commercialization
to_id: stage:custom-hbm-production
relation: passes_through
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C6
note_refs:
evidence_state: unverified
commercial_stage: production
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-23
status: active
boundary: 標準 HBM4 或 HBM4E 的量產不可替代 custom HBM 量產證據。
next_trigger: 具名 custom product 進入穩定量產並揭露數量 良率或財務分母。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I08
view: industry
from_id: concept:custom-hbm-commercialization
to_id: group:memory
relation: routes_to
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-15
status: active
boundary: 只建立記憶體族群搜尋路由；沒有 universe 公司具名產品 qualification 或財務曝險。
next_trigger: 平台端與公司端完成產品 客戶資格 出貨與財務雙向核對。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I09
view: industry
from_id: concept:custom-hbm-commercialization
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-15
status: active
boundary: Base die 與堆疊只形成封測搜尋路由；不證明任何公司參與或收入。
next_trigger: 具名封裝測試供應商 qualification 出貨與可辨識財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I10
view: industry
from_id: concept:custom-hbm-commercialization
to_id: group:ipdesign
relation: routes_to
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-15
status: active
boundary: 客製 base-die 邏輯只形成 IC 設計搜尋路由；不證明 design win NRE 或收入。
next_trigger: 客戶與公司雙向確認具名 IP tape-out qualification 與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I11
view: industry
from_id: concept:custom-hbm-commercialization
to_id: concept:custom-hbm-workload-contract
relation: requires
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C3,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C8,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C12
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: SK hynix 展示與三星研發分工支持工作負載設計入口；本線是查核框架，不表示所有 custom HBM 都搬移工作、使用相同輸入或已通過客戶端到端驗證。
next_trigger: 具名客戶與供應商公開同一 workload 的輸入 正確答案 latency power 失效條件及 sample qualification 結果。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I12
view: industry
from_id: concept:custom-hbm-commercialization
to_id: concept:custom-hbm-interface-contract
relation: includes
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C2,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C8
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: Samsung 文件直接列出容量 速度 電力 介面與 I/O architecture 工作，但沒有公開同一 custom product 的完整版本 通道 錯誤規則 客戶 sign-off 或共同標準。
next_trigger: 同一具名產品公開可重現的 interface version channel power envelope error handling 與客戶通過條件。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I13
view: industry
from_id: concept:custom-hbm-commercialization
to_id: concept:custom-hbm-base-die-contract
relation: includes
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C3,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C4,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C8,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C9,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C10
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: 多份供應商文件直接把 controller additional logic IP 與製程路徑放進 base die 設計，但沒有共同 die identity PPA 熱 sign-off 客戶 qualification 或量產分母。
next_trigger: 同一產品公開 base-die function IP ownership foundry node tape-out PPA thermal 與 customer qualification。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I14
view: industry
from_id: concept:custom-hbm-commercialization
to_id: concept:custom-hbm-firmware-contract
relation: includes
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C8
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: Samsung Memory Labs 直接列出 custom HBM firmware 工作，只支持該公司公開能力範圍；不表示所有客製路徑都需要相同韌體或任何版本已和客戶 runtime 完成整合。
next_trigger: 具名產品公開 firmware runtime compiler data format error recovery 版本及客戶驗收結果。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I15
view: industry
from_id: concept:custom-hbm-commercialization
to_id: concept:custom-hbm-manufacturing-thermal-contract
relation: requires
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C10,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C11,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C12
note_refs:
evidence_state: inference
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: TSMC 製程分流與 Samsung D2D PHY 熱點共同支持製造封裝熱需另列，但兩條不是同一產品鏈，也沒有證明任何具名 custom HBM 已完成共同 sign-off。
next_trigger: 同一產品公開 DRAM logic process stacking package power thermal hotspot test yield 與 change-control 結果。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I16
view: industry
from_id: concept:custom-hbm-commercialization
to_id: stage:custom-hbm-handoff-qualification
relation: passes_through
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C6,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C12
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: 現有公開資料沒有把同一具名客戶的六份交接 版本 責任人 變更控制 pass criteria 與量產財務接起；此節點只保存待驗證條件。
next_trigger: 客戶與供應商雙向公布同一 custom HBM 的六份 versioned handoff sign-off qualification 與 production outcome。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I17
view: industry
from_id: concept:custom-hbm-commercialization
to_id: process:custom-hbm-work-movement-performance-passport
relation: measured_by
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C16
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-09-15
status: active
boundary: 十欄護照把 SK hynix 公司敘事與 Intel LBNL 通用方法對齊成研究工具；不是 JEDEC 規格 公司 benchmark 產品評分 客戶 qualification 或供應鏈訂單。
next_trigger: 同一具名 custom HBM 與客戶公開 baseline offload raw runs 品質功耗熱 silicon qualification production 及財務共同鍵。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I18
view: industry
from_id: concept:custom-hbm-commercialization
to_id: metric:affected-fraction-operational-intensity-boundary
relation: measured_by
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C13,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C14,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C15,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C16
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-09-15
status: active
boundary: 公司 maximum throughput 不提供 affected fraction local speedup 或同邊界 bytes；Amdahl 與 Roofline 只給理論分母和上限 不能替代 achieved 端到端品質能源熱與客戶結果。
next_trigger: 具名產品以相同 workload 精度 baseline treatment 公開時間分解 boundary bytes sustainable bandwidth compute ceiling local end-to-end distributions 及 qualification。
-->
