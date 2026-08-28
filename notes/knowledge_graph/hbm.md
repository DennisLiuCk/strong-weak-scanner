# HBM／SPHBM4／製程控制知識圖譜

本檔只保存研究中心的顯示關係。線條的證據狀態、來源與文章入口由 `claim_refs` 或
`note_refs` 解析；不能用關聯數量、同業身分或文章共現補成公司訂單、市占或獨家供應。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: hbm
root_node_id: concept:hbm
label: HBM／SPHBM4／製程控制
summary: 從記憶體產品世代、SPHBM4 四層介面封裝契約、PHY 效能護照與資格節點，延伸到製程控制、control-plan 六欄及具名公司角色；台灣公司能力與財務轉換分開顯示。
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
review_due: 2026-08-26
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
review_due: 2026-08-26
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
edge_id: KG-HBM-C10
view: company
from_id: company:onto-innovation
to_id: concept:hbm
relation: reports_financials
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C8
note_refs:
evidence_state: verified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-06
review_due: 2026-11-05
status: active
boundary: Onto 只表示較寬的 Specialty Devices and Advanced Packaging 收入創季度新高，支撐含 2.5D logic、HBM 與 silicon photonics；沒有類別金額、題材占比、產品分子或客戶名稱，因此不能改寫成 Dragonfly／HBM 專屬收入。
next_trigger: 公司以同期間公司分母拆出 HBM／2.5D 或具名 process-control 工具收入、工具數、客戶廣度與重複採購。
-->

<!-- knowledge_edge
edge_id: KG-HBM-C11
view: company
from_id: company:camtek
to_id: concept:hbm
relation: provides_tooling
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C18
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-02
review_due: 2026-08-14
status: active
boundary: Camtek 公告證實 leading HBM player 的超過 5,000 萬美元訂單全部為 Hawk 且預計 2027 交付；客戶未具名，訂單不是實際交付或收入，也沒有工具台數、產能分母、良率、毛利或獨家證據。
next_trigger: Camtek 以公司分母揭露 Hawk／HBM 實際交付、收入、台數及重複採購，並由客戶確認量產用途與結果。
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
as_of: 2026-08-12
review_due: 2026-08-26
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
review_due: 2026-08-26
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
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C15
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-28
review_due: 2026-09-04
status: active
boundary: SPHBM4 必須分開核對 DRAM 堆疊、base die、分散式主機通道與接點封裝；四層框架不是已採用產品、CoWoS 立即替代或供應鏈訂單。
next_trigger: 取得實際JESD330-4-1試算表，或記憶體與加速器公司以相同版本具名採用SPHBM4。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I04
view: industry
from_id: concept:hbm
to_id: component:interface-base-die
relation: uses_component
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C1,MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C5
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
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
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C1,MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C5
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
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
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C1,MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C14
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-28
review_due: 2026-09-04
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
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C22
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-06
review_due: 2026-08-14
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
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C22
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-06
review_due: 2026-08-14
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
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C22
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-06
review_due: 2026-08-14
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
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C22
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-06
review_due: 2026-08-14
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
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C22
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-06
review_due: 2026-08-14
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
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C15
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-28
review_due: 2026-09-04
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
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C15
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-28
review_due: 2026-09-04
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
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C15
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-28
review_due: 2026-09-04
status: active
boundary: 標準可能改變組裝與測試流程，但記憶體廠自有封裝能力使外部 OSAT 角色仍未知。
next_trigger: 記憶體與封裝商文件可雙向核對相同產品、製程、量產與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I15
view: industry
from_id: concept:hbm
to_id: concept:sphbm4-four-layer-contract
relation: includes
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C15
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-28
review_due: 2026-09-04
status: active
boundary: 四層框架只防止把記憶體、介面、通道與封裝證據混用，不判斷技術勝負、產品採用、供應商份額或財務貢獻。
next_trigger: 同一具名 SPHBM4 產品公開四層版本、責任邊界與 qualification 結果。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I16
view: industry
from_id: concept:hbm
to_id: component:sphbm4-dram-stack
relation: uses_component
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C15
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-28
review_due: 2026-09-04
status: active
boundary: 沿用 HBM4 記憶體裸晶與容量能力不代表具名 SPHBM4 堆疊已完成、良率相同、供應充足或價格較低。
next_trigger: 記憶體供應商公開具名 SPHBM4 stack、容量、層數、良率、熱與量產時程。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I17
view: industry
from_id: concept:hbm
to_id: component:sphbm4-distributed-host-interface
relation: changes_signal_path
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C5
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: JEDEC 公開摘要只證實獨立且不必同步的 16-bit DDR 通道與四倍速率映射；完整控制、訓練、錯誤與互通條件未由本輪公開原文核對。
next_trigger: 公開規格或具名 datasheet 可逐項核對 channel state、clock、training、error handling 與 host controller。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I18
view: industry
from_id: concept:hbm
to_id: stage:sphbm4-bump-map-publication
relation: moves_to
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C14
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-28
review_due: 2026-09-04
status: active
boundary: 8/28公開catalog與版本月份已取得，但未取得試算表；文件可見度不是完整規格、silicon互通、客戶資格或量產證據。
next_trigger: 取得可離線核對的JESD330-4-1實際試算表、版本與變更紀錄。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I19
view: industry
from_id: concept:hbm
to_id: stage:sphbm4-phy-device-qualification
relation: requires
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C9
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: Eliyan 的產品定位不等於具名 base die、host PHY 與記憶體 stack 已依同一版本完成 silicon 或跨廠測試。
next_trigger: 具名供應商公開版本化 datasheet、silicon、功耗延遲錯誤結果與 multi-vendor test matrix。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I20
view: industry
from_id: concept:hbm
to_id: stage:sphbm4-system-customer-qualification
relation: requires
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C9
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: 標準、PHY 產品或記憶體樣品均不能替代具名運算平台的控制器、工作負載、熱可靠度與客戶通過結果。
next_trigger: 加速器或系統客戶公開同一 SPHBM4 組合的 configuration、workload、reliability 與 qualification outcome。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I21
view: industry
from_id: concept:hbm
to_id: stage:sphbm4-commercial-attribution
relation: moves_to
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C9
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-10-31
status: active
boundary: 標準、市場總額、HBM4 出貨與公司總營收都不能替代同一 SPHBM4 產品的數量、價格、收入、成本、毛利與現金分母。
next_trigger: 買方與供應商文件可雙向核對同一版本產品、qualification、量產期間、出貨與財務分子。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I22
view: industry
from_id: concept:hbm
to_id: concept:inspection-control-plan
relation: requires
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C14
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: HBM／3D 複雜度支持把 control plan 分欄查核，但六欄框架不是客戶 recipe、設備標準、工具數或財務需求。
next_trigger: 同一 HBM production product／layer 公開版本化 control plan、六欄設定及製造結果。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I23
view: industry
from_id: concept:hbm
to_id: metric:inspection-sampling-coverage
relation: measured_by
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C11,MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C14
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: NIST public CMP dataset 支持 dynamic sampling 方法，不代表 HBM 可降低實體量測或任何 coverage 已足夠。
next_trigger: 客戶公開 lot／wafer／die／site sampling unit、coverage、模型不確定性、漂移及量產 outcome。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I24
view: industry
from_id: concept:hbm
to_id: metric:defect-sensitivity-escape
relation: measured_by
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C12,MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C14
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 供應商靈敏度陳述沒有把 defect size、killer relevance、escape 與客戶失效接成同口徑結果。
next_trigger: 同一 layer 公開 detection threshold、已知缺陷集、false negative／escape 與 downstream failure correlation。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I25
view: industry
from_id: concept:hbm
to_id: metric:nuisance-false-alarm
relation: measured_by
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C12,MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C14
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: AI classification 功能不等於公開 FAR、分類純度、人工複判負荷或可攔截的關鍵缺陷增加。
next_trigger: 客戶或中立資料公布候選母體、DOI prevalence、FAR、分類混淆矩陣與複判容量。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I26
view: industry
from_id: concept:hbm
to_id: metric:inspection-cycle-time
relation: measured_by
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C11,MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C12,MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C14
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 單機 imaging／review throughput 不等於從 sampling、排隊、複判到製程動作的完整 time-to-result。
next_trigger: 同一量產 flow 公開 inspection queue、review、classification、decision latency 與 factory cycle-time bridge。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I27
view: industry
from_id: concept:hbm
to_id: capability:excursion-containment
relation: requires
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C13,MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C14
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: Inline、post-dicing 與 screening 任務說明結果必須連到處置，但沒有客戶端隔離範圍、重工報廢或損失避免資料。
next_trigger: 客戶公開 excursion trigger、stop／hold／release rule、受影響批次追溯、containment time 與製造結果。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I28
view: industry
from_id: concept:hbm
to_id: process:sphbm4-phy-performance-passport
relation: measured_by
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C13
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-26
status: active
boundary: 十欄護照是把 JEDEC 架構、OCP 通用量測方法與供應商自報欄位對齊的研究工具，不是新增標準條文、compliance score、產品排名或供應鏈訂單。
next_trigger: 同一具名 SPHBM4 memory、base die、host PHY、package 與 system 公開完整十欄、原始結果及客戶 qualification。
-->

<!-- knowledge_edge
edge_id: KG-HBM-I29
view: industry
from_id: concept:hbm
to_id: metric:sphbm4-lane-raw-payload-energy-boundary
relation: measured_by
claim_refs: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C10,MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C11,MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C13
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-26
status: active
boundary: 2,048×1＝512×4 只固定 raw 算術；沒有共同方向、payload、量測點、BER exposure、power、幾何與產品結果時，不得推延遲、能耗、良率、成本或系統效能。
next_trigger: 具名 SPHBM4 與可比基準公開同版本 raw／payload、T0／T1、BER／retry、Tx＋Rx＋clock power、shoreline、reach 與產品結果。
-->
