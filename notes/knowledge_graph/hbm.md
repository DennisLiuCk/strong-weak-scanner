# HBM／SPHBM4／製程控制知識圖譜

本檔只保存研究中心的顯示關係。線條的證據狀態、來源與文章入口由 `claim_refs` 或
`note_refs` 解析；不能用關聯數量、同業身分或文章共現補成公司訂單、市占或獨家供應。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: hbm
root_node_id: concept:hbm
label: HBM／SPHBM4
summary: 從記憶體產品世代、介面與封裝路徑，延伸到製程控制及具名公司角色；台灣公司能力與財務轉換分開顯示。
article_ids: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE,MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY
status: active
-->

<!-- knowledge_edge
edge_id: KG-HBM-C01
view: company
from_id: company:micron
to_id: concept:hbm
relation: produces
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C3
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-24
review_due: 2026-08-15
status: active
boundary: 證實的是 Micron 對既有 HBM4 產品進度的公司陳述，不證明採用 SPHBM4、供應獨家或特定客戶收入。
next_trigger: Micron 首次具名揭露 SPHBM4 樣品、認證或量產，或提供 HBM4 可辨識財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-HBM-C02
view: company
from_id: company:sk-hynix
to_id: concept:hbm
relation: samples
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C3
note_refs:
evidence_state: verified
commercial_stage: sample
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-18
review_due: 2026-08-15
status: active
boundary: 12 層 HBM4E 樣品不是量產承諾，也沒有證明 SPHBM4 介面、外部封裝商或獨家供應。
next_trigger: SK hynix 公布 HBM4E 量產時程、客戶認證或 SPHBM4 產品路線。
-->

<!-- knowledge_edge
edge_id: KG-HBM-C03
view: company
from_id: company:applied-materials
to_id: concept:hbm
relation: provides_tooling
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C2
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-13
status: active
boundary: 公司陳述支持特定 eBeam 系統與 HBM／先進封裝問題，不代表全產業良率效果、市占、收入或台灣供應商訂單。
next_trigger: 客戶端或第二條獨立來源揭露工具部署數、缺陷攔截、良率改善或重複採購。
-->

<!-- knowledge_edge
edge_id: KG-HBM-C04
view: company
from_id: company:onto-innovation
to_id: concept:hbm
relation: qualified_at
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C3
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-13
status: active
boundary: 一名 HBM 客戶資格認證不是大量採購、收入規模、產業滲透率或供應獨佔證據。
next_trigger: 資格節點進入高量產並揭露客戶廣度、工具數或可辨識營收。
-->

<!-- knowledge_edge
edge_id: KG-HBM-C05
view: company
from_id: company:kla
to_id: concept:hbm
relation: cites_demand
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C1
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-13
status: active
boundary: 管理層需求說法沒有分解 KLA 成長來自工具量、市占、ASP、產品組合或服務的比例。
next_trigger: 同期間資料可重建 HBM／先進封裝製程控制工具量或客戶支出貢獻。
-->

<!-- knowledge_edge
edge_id: KG-HBM-C06
view: company
from_id: company:3443
to_id: concept:hbm
relation: develops_ip
claim_refs:
note_refs: 3443#S1
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-11
review_due: 2026-08-15
status: active
boundary: HBM4E IP 測試晶片投片或矽驗證是能力里程碑，不等於外部授權、量產收入、市占或獨家供應。
next_trigger: 公司揭露客戶導入、授權／NRE、tape-out 與後續量產收入。
-->

<!-- knowledge_edge
edge_id: KG-HBM-C07
view: company
from_id: company:3661
to_id: concept:hbm
relation: has_capability
claim_refs:
note_refs: 3661#S3
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-11
review_due: 2026-08-20
status: active
boundary: 年報列示 HBM 與 2.5D／3D 等整合能力，不證明具名 HBM 客戶、專案、量產收入或獨立市占。
next_trigger: 新增量產專案把 HBM／先進封裝能力連到可辨識 NRE、量產與收入。
-->

<!-- knowledge_edge
edge_id: KG-HBM-C08
view: company
from_id: company:3131
to_id: concept:hbm
relation: names_application
claim_refs:
note_refs: 3131#S1,3131#S2
evidence_state: verified
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-11
review_due: 2026-08-20
status: active
boundary: 公司把 HBM 列為應用機會只證明產品布局，不能改寫成具名客戶、訂單、交付台數或已認列營收。
next_trigger: 新機種、客戶驗證與設備產品收入能以公司文件連到 HBM 量產專案。
-->

<!-- knowledge_edge
edge_id: KG-HBM-C09
view: company
from_id: company:6239
to_id: concept:hbm
relation: has_capability
claim_refs:
note_refs: 6239#S1
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-11
review_due: 2026-08-15
status: active
boundary: HBM 相關製程能力與產業需求不等於已取得 HBM 客戶、訂單、設備到位或大量營收。
next_trigger: 公司正式揭露 HBM 客戶認證、量產、產品收入與毛利貢獻。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I01
view: industry
from_id: concept:hbm
to_id: product:hbm4
relation: generation_of
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C1
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-01
review_due: 2026-08-15
status: active
boundary: HBM4 是產品世代；本線不表示所有 HBM4 都採 SPHBM4，也不比較供應商優劣。
next_trigger: 產品路線圖更新 HBM4 的客戶認證、量產與後續世代時鐘。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I02
view: industry
from_id: concept:hbm
to_id: product:hbm4e
relation: generation_of
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C3
note_refs:
evidence_state: verified
commercial_stage: sample
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-18
review_due: 2026-08-15
status: active
boundary: 樣品階段不能與其他公司的 HBM4 量產陳述混成技術排名或 SPHBM4 採用。
next_trigger: HBM4E 客戶資格、量產日期與產品規格更新。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I03
view: industry
from_id: concept:hbm
to_id: standard:sphbm4
relation: alternative_standard
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C2
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-01
review_due: 2026-08-15
status: active
boundary: SPHBM4 目前是設計選項與補充路徑，不是已採用產品、CoWoS 立即替代或供應鏈訂單。
next_trigger: 任一記憶體或加速器公司首次具名採用 JESD330-4。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I04
view: industry
from_id: concept:hbm
to_id: component:interface-base-die
relation: uses_component
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-01
review_due: 2026-08-15
status: active
boundary: 標準定義 base die 角色，但尚未指定設計者、製程、供應商、成本或商業模式。
next_trigger: 產品文件揭露 base-die 架構、供應者、功耗與量產時程。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I05
view: industry
from_id: concept:hbm
to_id: process:serialization
relation: changes_signal_path
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-01
review_due: 2026-08-15
status: active
boundary: 4 比 1 序列化降低主機側訊號數，不代表系統功耗、延遲、良率與成本已優於既有路徑。
next_trigger: 公開實測量化功耗、延遲、訊號完整性與封裝良率。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I06
view: industry
from_id: concept:hbm
to_id: component:organic-substrate
relation: enables_substrate_path
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-01
review_due: 2026-08-15
status: active
boundary: 標準有機基板不能自動等同 ABF 或 BT，也未指定台灣載板公司。
next_trigger: 具名產品揭露材料規格、基板供應商與可靠度認證。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I07
view: industry
from_id: concept:hbm
to_id: process:2_5d-3d
relation: integrated_with
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C4
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-13
status: active
boundary: 交叉證據支持工程複雜度與整合關係，不證明特定封裝商收入或所有產品採相同路徑。
next_trigger: 客戶端文件揭露產品世代、封裝結構、良率與採用範圍。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I08
view: industry
from_id: concept:hbm
to_id: capability:process-control
relation: raises_need
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C4
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-13
status: active
boundary: 工程重要性上升不等於全產業設備 wallet share、工具量或供應商收入已上升。
next_trigger: 至少兩條獨立來源以同口徑量化每世代工具量、步驟或單位產能支出。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I09
view: industry
from_id: concept:hbm
to_id: capability:metrology
relation: raises_need
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C4
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-13
status: active
boundary: 量測需求機制不等於特定台灣量測設備已取得 HBM 訂單。
next_trigger: 公司與客戶文件可核對量測產品、資格、量產及財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I10
view: industry
from_id: concept:hbm
to_id: capability:inspection
relation: raises_need
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C4
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-13
status: active
boundary: 缺陷代價提高支持檢查重要性，但未量化產業工具數、採購或獲利池。
next_trigger: 客戶揭露缺陷攔截率、重複採購或高量產部署範圍。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I11
view: industry
from_id: concept:hbm
to_id: capability:yield-learning
relation: raises_need
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C4
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-13
status: active
boundary: 良率學習是工程需求，不代表封測使用端收入或毛利必然改善。
next_trigger: 量產資料揭露回饋週期、良率改善與對應工具採用。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I12
view: industry
from_id: concept:hbm
to_id: group:pcb
relation: routes_to
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C2
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-01
review_due: 2026-08-15
status: active
boundary: 只構成高階基板搜尋路由；沒有材料規格、供應商、客戶或量產，不得列個股受惠。
next_trigger: 基板供應商被具名並完成材料、可靠度與客戶量產認證。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I13
view: industry
from_id: concept:hbm
to_id: group:ipdesign
relation: routes_to
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C2
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-01
review_due: 2026-08-15
status: active
boundary: base die 與序列化提高設計問題的重要性，但尚無 IP 供應商、商業模式或訂單。
next_trigger: 具名 base-die 或高速介面 IP 完成客戶導入及量產收入。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I14
view: industry
from_id: concept:hbm
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C2
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-01
review_due: 2026-08-15
status: active
boundary: 標準可能改變組裝與測試流程，但記憶體廠自有封裝能力使外部 OSAT 角色仍未知。
next_trigger: 記憶體與封裝商文件可雙向核對相同產品、製程、量產與財務貢獻。
-->
