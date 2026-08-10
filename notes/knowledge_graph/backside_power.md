# 背面供電路徑與製程接力知識圖譜

本圖先把正面訊號與背面送電分開，再把晶圓廠的製造成熟度、一般製程步驟與供應商證據時鐘
分開。台灣設備、材料與 IP 只保留成待驗證的搜尋路由；沒有具名資格認證與財務足跡前，
不建立公司受惠線。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: backside-power
root_node_id: concept:backside-power
label: 背面供電路徑與製程接力
summary: 先用背面金屬、奈米級背面導通孔與埋置電源軌讀懂送電路徑，再以 A16／18A 製造時鐘連接薄化、背面對準與六關公司證據，阻止必要步驟被誤寫成供應商訂單。
article_ids: MI-2026-08-02-BACKSIDE-POWER-DELIVERY
status: active
-->

<!-- knowledge_edge
edge_id: KG-BSP-C01
view: company
from_id: company:tsmc
to_id: concept:backside-power
relation: plans_production
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C1
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-16
review_due: 2026-08-09
status: active
boundary: 台積電年報證實 A16 的 Super Power Rail 與 2026 下半年量產計畫，不等於截至 2026-08-02 已量產、客戶採用、良率或收入。
next_trigger: 台積電正式確認 A16 進入量產並提供客戶產品、爬坡或製造範圍。
-->

<!-- knowledge_edge
edge_id: KG-BSP-C02
view: company
from_id: company:intel
to_id: concept:backside-power
relation: produces
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C2
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-16
review_due: 2026-08-09
status: active
boundary: Intel 表示 18A 已生產、18A-P 進入風險生產；這不證明外部 foundry 客戶大量採用，也不能直接與 A16 的量產定義相比。
next_trigger: Intel 揭露外部客戶產品、實際出貨或 18A-P 由風險生產進入量產。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I01
view: industry
from_id: concept:backside-power
to_id: process:super-power-rail
relation: includes
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C1
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-16
review_due: 2026-08-09
status: active
boundary: Super Power Rail 是台積電 A16 的實作名稱；不代表其他晶圓廠採相同流程或供應商。
next_trigger: A16 量產文件進一步揭露實際成熟度、產品與製程邊界。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I02
view: industry
from_id: concept:backside-power
to_id: process:powervia
relation: includes
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C2
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-16
review_due: 2026-08-09
status: active
boundary: PowerVia 是 Intel 18A 家族實作；不能由名稱推定台積電 A16 的結構、效能或供應商相同。
next_trigger: Intel 公布外部客戶產品、量產規模與後續 18A-P 成熟度。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I03
view: industry
from_id: concept:backside-power
to_id: component:buried-power-rail
relation: uses_component
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2022-11-25
review_due: 2026-08-16
status: active
boundary: imec 把 BPR 列為一種關鍵實作元件；不證明所有量產流程都採同一材料、尺寸或工具。
next_trigger: 晶圓廠量產文件或供應商 qualification 明確核對 BPR 的實際流程與材料。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I04
view: industry
from_id: concept:backside-power
to_id: component:nano-tsv
relation: uses_component
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2022-11-25
review_due: 2026-08-16
status: active
boundary: nano-TSV 是 imec 所述實作路徑，不等於 A16／PowerVia 均使用相同結構或已形成特定供應商訂單。
next_trigger: 晶圓廠或設備材料商公開具名 nTSV qualification、量產與產品對應。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I05
view: industry
from_id: concept:backside-power
to_id: process:wafer-thinning
relation: requires
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2022-11-25
review_due: 2026-08-16
status: active
boundary: imec 流程需要極薄晶圓，但技術必要性不等於任一台灣薄化、CMP 或蝕刻公司已供貨或受惠。
next_trigger: 晶圓廠與供應商可雙向核對具名量產工具、材料與資格。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I06
view: industry
from_id: concept:backside-power
to_id: process:backside-alignment
relation: requires
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2022-11-25
review_due: 2026-08-16
status: active
boundary: 背面對準是 imec 流程中的工程難題；尚未核對 A16／18A 的實際工具、規格或供應商。
next_trigger: 量產流程或設備商文件揭露具名背面 overlay／alignment qualification 與出貨。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I07
view: industry
from_id: concept:backside-power
to_id: group:semiequip
relation: routes_to
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-16
status: active
boundary: 這只是薄化、接合、蝕刻、量測與對準的研究入口；沒有 universe 設備公司具名 qualification、出貨或收入證據。
next_trigger: 晶圓廠與設備商雙向核對同一背面供電步驟、量產資格及財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I08
view: industry
from_id: concept:backside-power
to_id: group:material
relation: routes_to
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-16
status: active
boundary: BPR、蝕刻停止層與背面金屬形成材料研究入口，但沒有台灣材料商具名量產資格與財務足跡。
next_trigger: 材料商揭露具名 A16／18A 背面供電材料、qualification、量產與收入。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I09
view: industry
from_id: concept:backside-power
to_id: group:ipdesign
relation: routes_to
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-16
status: active
boundary: 新 PDK 與設計技術共同最佳化是研究入口，不證明任何 universe IP／ASIC 公司已有 design win 或授權收入。
next_trigger: 公司以具名 A16／18A PDK、客戶採用與授權收入完成雙向核對。
-->
