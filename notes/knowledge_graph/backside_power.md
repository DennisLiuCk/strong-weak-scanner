# 背面供電路徑與製程接力知識圖譜

本圖先把正面訊號與背面送電分開，再沿著設計、製程成形、製程控制、節點產品與供應商財務
五個時鐘串起證據；效能百分比另經八格比較護照分開靜態壓降、動態下陷與條件式 PPA，再用
電力—熱十欄護照接上 rail reference、總／局部電流、焦耳損耗、熱路徑與 hotspot。台灣設備、
材料與 IP 只保留成待驗證的搜尋路由；沒有具名資格認證、重複出貨與財務足跡前，不建立公司
受惠線。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: backside-power
root_node_id: concept:backside-power
label: 背面供電路徑與製程接力
summary: 先用背面金屬、奈米級背面導通孔與埋置電源軌讀懂送電路徑，再用八格效能護照區分靜態壓降、動態下陷與條件式 PPA，以十欄電力—熱護照分開參考電壓、總／局部電流、路徑損耗與 hotspot，最後沿設計、製程控制、節點產品、供應商資格與財務歸因五個時鐘前進。
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

<!-- knowledge_edge
edge_id: KG-BSP-C03
view: company
from_id: company:lam-research
to_id: concept:backside-power
relation: has_capability
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C7,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C10
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-29
review_due: 2026-08-26
status: active
boundary: Lam／imec 研究把虛擬製程與電性或應力模型用在背面供電失效機制；沒有公開 A16／18A qualification、量產工具台數、客戶出貨或收入。
next_trigger: Lam 或晶圓廠把具名工具對上具名節點、客戶資格、重複出貨與可定位財務結果。
-->

<!-- knowledge_edge
edge_id: KG-BSP-C04
view: company
from_id: company:applied-materials
to_id: concept:backside-power
relation: provides_tooling
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C9
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-10-07
review_due: 2026-09-12
status: active
boundary: Applied Materials 將 PROVision 10 列為可服務 GAA 與背面供電的具名量測產品，但客戶、節點、背面供電資格、台數、收入與毛利未逐一揭露。
next_trigger: Applied Materials 或晶圓廠把 PROVision 10 對上具名背面供電節點、qualification、重複出貨與財務附件。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I10
view: industry
from_id: concept:backside-power
to_id: capability:backside-dtco
relation: requires
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C6,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C11
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: imec／Arm 比較特定背面連接方案的設計與製程取捨；不代表所有晶圓廠採相同結構或已公開量產 PDK。
next_trigger: 具名晶圓廠與客戶產品提供可核對的設計規則、試驗晶片及電力完整性實測。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I11
view: industry
from_id: concept:backside-power
to_id: metric:ntsv-bpr-contact-resistance
relation: measured_by
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C7
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-29
review_due: 2026-08-26
status: active
boundary: 接點電阻是 Lam／imec 研究結構的有效工程量測；文中數值與幾何窗口不能外推成 A16／18A 通用規格或跨廠排名。
next_trigger: 同一具名節點公開實體晶圓的接點電阻分布、製程窗口與電力完整性結果。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I12
view: industry
from_id: concept:backside-power
to_id: capability:backside-overlay-metrology
relation: requires
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C7,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C9
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-29
review_due: 2026-08-26
status: active
boundary: 研究證實疊對與形貌會影響接點，且外部已有具名量測產品；仍沒有 A16／18A 工具選擇、qualification 或量產出貨證據。
next_trigger: 晶圓廠與量測商雙向核對具名工具、節點、疊對規格、資格及量產使用期間。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I13
view: industry
from_id: concept:backside-power
to_id: capability:backside-stress-control
relation: requires
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C10
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2025-04-02
review_due: 2026-08-26
status: active
boundary: Lam 的虛擬製程研究建立薄化、背面金屬、導通結構與機械應力的機制關係；不是量產晶圓統計或共同可靠度標準。
next_trigger: 具名節點公開實體晶圓的應力、位移、電性與長期可靠度驗證。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I14
view: industry
from_id: concept:backside-power
to_id: stage:backside-design-validation
relation: passes_through
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C6,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C11
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: 五時鐘框架把設計驗證列為獨立成熟度節點；現有證據主要來自研究比較，尚未對上具名客戶量產產品。
next_trigger: 同一具名產品公開設計規則、試驗晶片及電力完整性實測並對上量產節點。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I15
view: industry
from_id: concept:backside-power
to_id: stage:backside-process-control
relation: passes_through
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C6,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C7,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C10
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: 接點與應力研究支持把製程控制和可靠度獨立追蹤；沒有具名節點的公開量產窗口、良率分布或可靠度統計。
next_trigger: 同一具名節點公開疊對、接點電阻、應力、良率與可靠度的量產驗收資料。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I16
view: industry
from_id: concept:backside-power
to_id: stage:backside-node-production
relation: passes_through
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C1,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C2,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C6,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C8
note_refs:
evidence_state: inference
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: 台積電與 Intel 各有具名節點及自行定義的製造里程碑；不能跨廠比較，也不證明 A16 截至 2026-08-12 已量產或具名客戶產品已出貨。
next_trigger: 晶圓廠把具名節點對上實際客戶產品、爬坡、良率、製造範圍與可定位出貨。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I17
view: industry
from_id: concept:backside-power
to_id: stage:backside-supplier-qualification
relation: passes_through
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C5,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C6,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C9
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 外部設備商已有具名產品，但沒有把客戶、節點、背面供電 qualification 與重複出貨對上；台灣設備材料與 IP 公司映射仍未證。
next_trigger: 晶圓廠與供應商文件雙向核對同一產品、製程步驟、客戶資格、出貨期間與數量。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I18
view: industry
from_id: concept:backside-power
to_id: stage:backside-financial-attribution
relation: passes_through
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C5,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C6
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 現有來源沒有任何 universe 公司可辨識的背面供電份額、價格、收入、毛利或現金流，不能由技術需要代替財務歸因。
next_trigger: 具名產品與節點的出貨可接回同期間份額、價格、收入、成本、毛利及收款分母。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I19
view: industry
from_id: concept:backside-power
to_id: concept:backside-performance-comparison-passport
relation: requires
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C17
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 八格護照是由多份官方文件的條件差異歸納出的閱讀框架，不是晶圓廠共同 benchmark 標準；缺格時只能保留文件內結論。
next_trigger: 同一 frontside／backside 產品版本公開共同受測物、baseline、iso-condition、activity、window、PDN／PVT 及完整 trade-off。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I20
view: industry
from_id: concept:backside-power
to_id: metric:static-ir-drop
relation: measured_by
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C15
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 靜態 IR drop 以直流電流與電阻路徑為核心；局部接點電阻改善不等於全晶片動態下陷、頻率或產品效能已改善。
next_trigger: 具名節點公開同一版圖與 PVT 下的全晶片靜態壓降分布，並對上接點、金屬與量產製程窗口。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I21
view: industry
from_id: concept:backside-power
to_id: metric:dynamic-voltage-droop
relation: measured_by
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C14,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C15
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 動態下陷需綁定活動向量、時間視窗及晶片到系統 PDN；Intel 的條件式結果不能外推到所有工作負載或其他晶圓廠。
next_trigger: 同一具名產品公開 workload／vector、time window、chip-package-board PDN、PVT 與原始 droop 分布。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I22
view: industry
from_id: concept:backside-power
to_id: metric:conditional-ppa-comparison
relation: measured_by
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C12,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C13,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C14,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C16,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C17
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: same-Vdd、same-speed、frequency 或 power 與不同 area 指標各有自己的固定條件；up to 與 or 不能改寫為同時保證或單一結構歸因。
next_trigger: 同一設計公開 iso-Vdd、iso-speed、iso-power 三種結果、共同面積定義、熱與可靠度代價，並分解 transistor 與 backside rail 貢獻。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I23
view: industry
from_id: concept:backside-power
to_id: process:backside-electrothermal-passport
relation: requires
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C21
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-09-12
status: active
boundary: 十欄護照是 NIST 量綱、imec／Intel 背面供電邊界與 IBM 電流／熱模型的研究整合，不是晶圓廠共同 signoff 標準、製程規格或投資評分。
next_trigger: 同一 frontside／backside 產品公開 rail reference、load、current path、distributed RLC、local current-density、loss／thermal maps、PVT、reliability 與產品資格。
-->

<!-- knowledge_edge
edge_id: KG-BSP-I24
view: industry
from_id: concept:backside-power
to_id: metric:rail-current-drop-loss-hotspot-boundary
relation: measured_by
claim_refs: MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C18,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C19,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C20,MI-2026-08-02-BACKSIDE-POWER-DELIVERY#C21
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-09-12
status: active
boundary: 本文固定 30mV 或 100W／0.2mΩ 的數值全是假想量綱教材；IBM TSV current-crowding 機制不能直接外推 nano-TSV，BSPDN thermal abstract 也沒有產品溫度與冷卻分布。
next_trigger: 同一具名產品以可重現方法公開 mV／rail percentage、total／local current-density、path loss、thermal resistance、hotspot distribution 及 die／wafer／lot reliability。
-->
