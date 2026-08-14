# HBF 商用化知識圖譜

本圖把 HBF 的規格時鐘與產品時鐘拆開：第一版共同技術規格已由廠商公告發布，但直接規範
原文、合規互通、實體樣品、裝置整合及客戶資格仍是不同節點，不能跨級變成量產、財務曝險
或 HBM 的已證實替代品。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: hbf-commercialization
root_node_id: concept:hbf-commercialization
label: HBF 商用化
summary: 以規格時鐘與產品時鐘追蹤 HBF 從 NAND／logic base die 架構、第一版技術規格、合規互通到 memory sample、device sample、客戶資格與量產的證據階梯，並用三張成績單分開名目／可用／工作集容量、內部模擬與固定品質的推論服務結果。
article_ids: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER
status: active
-->

<!-- knowledge_edge
edge_id: KG-HBF-C01
view: company
from_id: company:sandisk
to_id: concept:hbf-commercialization
relation: develops_ip
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C1,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C3,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C7
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Sandisk 與 SK hynix 共同推進 HBF 標準化；產品與樣品時程由 Sandisk 揭露，不構成排他供應或量產。
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: Sandisk 是具名發起者並共同公告第一版技術規格及樣品目標，不等於 memory sample 已交付、客戶資格、量產或財務貢獻。
next_trigger: Sandisk 公布實體 HBF sample、測試條件、接收方與 qualification。
-->

<!-- knowledge_edge
edge_id: KG-HBF-C02
view: company
from_id: company:sk-hynix
to_id: concept:hbf-commercialization
relation: develops_ip
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C1,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C2,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C7,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C8,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C12
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: multi_source
exclusivity_scope: SK hynix 與 Sandisk 共同標準化，並公開 NAND／logic base die／KV cache 技術方向；未證明唯一供應或量產角色。
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: 技術願景、第一版規格摘要與分層架構不等於 SK hynix 已有 HBF 樣品、客戶、出貨或收入。
next_trigger: SK hynix 公布具名 sample、測試條件、客戶資格與量產節點。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I01
view: industry
from_id: concept:hbf-commercialization
to_id: standard:hbf-workstream
relation: passes_through
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: OCP 列有 HBF workstream，廠商另公告第一版規格發布；工作組本身不等於直接規範原文、compliance 或 multi-vendor product。
next_trigger: OCP 公開可定位的版本化規範原文、條款與 compliance 計畫。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I02
view: industry
from_id: concept:hbf-commercialization
to_id: component:nand-flash
relation: uses_component
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-23
review_due: 2026-10-15
status: active
boundary: SK hynix 將 HBF 定義為 NAND solution；不證明標準 SSD NAND 可直接替代或所有 NAND 供應商都能生產 HBF。
next_trigger: 公開 HBF die、cell、stack、controller 與量產製程規格。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I03
view: industry
from_id: concept:hbf-commercialization
to_id: component:logic-base-die
relation: uses_component
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-23
review_due: 2026-10-15
status: active
boundary: HBF 技術方向使用 logic base die；沒有最終 node、foundry、介面、良率或供應商證據。
next_trigger: 樣品或規格公開 base die 功能、製程與製造路徑。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I04
view: industry
from_id: concept:hbf-commercialization
to_id: concept:kv-cache
relation: names_application
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-23
review_due: 2026-10-15
status: active
boundary: SK hynix 將 KV cache 列為目標資料；不證明所有 KV cache 工作負載、寫入模式與耐久條件都適用。
next_trigger: 具名裝置提供 KV cache 讀寫、延遲、耐久、容量與端到端效能結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I05
view: industry
from_id: concept:hbf-commercialization
to_id: stage:hbf-memory-sample
relation: passes_through
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-08-11
review_due: 2026-08-26
status: active
boundary: Sandisk 公布的是 2026 下半年目標，不是 sample 已交付；verified 只指時程原文。
next_trigger: 公告實際交付日、規格、測試條件、接收方與結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I06
view: industry
from_id: concept:hbf-commercialization
to_id: stage:hbf-device-sample
relation: passes_through
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-08-11
review_due: 2026-10-15
status: active
boundary: 2027 年初 device sample 是公司預期；不等於具名裝置已整合、能運行或完成客戶資格。
next_trigger: 裝置端與記憶體端雙方公布樣品、記憶體拓撲、工作負載與測試結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I07
view: industry
from_id: concept:hbf-commercialization
to_id: concept:ai-memory-hierarchy
relation: integrated_with
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C9,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C12
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-10-15
status: active
boundary: SK hynix 把 HBF 放入分層記憶體架構，本文據此保留 NAND 型中間層推論；尚未有實體系統證明它與 HBM、DRAM、CXL memory 或 SSD 如何分工。
next_trigger: 具名 AI 系統公布 HBF memory map、軟體調度、工作負載與端到端結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I08
view: industry
from_id: concept:hbf-commercialization
to_id: stage:hbf-customer-qualification
relation: passes_through
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C11
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: 客戶 qualification 是必要的未來節點；本輪沒有具名客戶、測試條件或完成結果。
next_trigger: 客戶與供應商雙方確認 qualification 範圍、結果與下一步量產。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I09
view: industry
from_id: concept:hbf-commercialization
to_id: group:memory
relation: routes_to
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: HBF 形成記憶體與 controller 搜尋路由，沒有 universe 公司具名產品、qualification、訂單或財務證據。
next_trigger: 平台端與公司端雙向核對 HBF 產品、客戶資格、出貨與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I10
view: industry
from_id: concept:hbf-commercialization
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: 堆疊與 base die 形成封裝測試搜尋路由，不證明 universe 公司參與 HBF 或取得收入。
next_trigger: HBF 平台端具名 OSAT／設備／測試路徑，且公司端揭露 qualification、出貨與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-HBF-C03
view: company
from_id: company:google
to_id: concept:hbf-commercialization
relation: tests
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C7
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-08-26
status: active
boundary: Sandisk／SK hynix 聯合公告只把 Google 列為協助 technology validation 與標準工作的 consortium member；不是 Google 自身公告的產品採用、qualification、部署或採購。
next_trigger: Google 以自有一手文件具名 HBF 裝置、工作負載、測試條件、qualification 或 deployment。
-->

<!-- knowledge_edge
edge_id: KG-HBF-C04
view: company
from_id: company:tenstorrent
to_id: concept:hbf-commercialization
relation: tests
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C7
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-08-26
status: active
boundary: Sandisk／SK hynix 聯合公告只把 Tenstorrent 列為協助 technology validation 與標準工作的 consortium member；不是 Tenstorrent 自身公告的產品採用、qualification、部署或採購。
next_trigger: Tenstorrent 以自有一手文件具名 HBF silicon、裝置、工作負載、測試條件或 qualification。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I11
view: industry
from_id: concept:hbf-commercialization
to_id: standard:hbf-technical-specification
relation: passes_through
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C7,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C8
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope: Sandisk 與 SK hynix 共同公告第一版規格，Google 與 Tenstorrent 被列為 consortium members；所有說法仍屬同一聯合規格消息鏈，不代表獨立來源或供應多元性。
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: 已驗證的是第一版技術規格發布公告與摘要範圍；本輪未直接取得可定位版本的 OCP normative document，也沒有合規或產品結果。
next_trigger: OCP 公開帶版本、條款定位與變更紀錄的 HBF 規範原文。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I12
view: industry
from_id: concept:hbf-commercialization
to_id: metric:hbf-performance-grade
relation: measured_by
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C8
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-04
review_due: 2026-08-26
status: active
boundary: 8／16 層、最高 512GB 與約 0.4 至 3.0 TB/s 是 SK hynix 公布的規格包絡，不是具名樣品的 measured result，亦沒有延遲與測試條件。
next_trigger: 具名樣品在固定堆疊、容量、存取型態、溫度與功耗條件下公布可重現結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I13
view: industry
from_id: concept:hbf-commercialization
to_id: standard:ucie-interface
relation: uses_standard
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C8
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-04
review_due: 2026-08-26
status: active
boundary: SK hynix 規格摘要描述 UCIe 連接；本輪未獨立核對 UCIe 版本、協定層、封裝映射、compliance 或具名 silicon。
next_trigger: 規範原文或具名產品公開 UCIe 版本、層級、通道、封裝與 compliance 結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I14
view: industry
from_id: concept:hbf-commercialization
to_id: component:xpu-hbf-host-interface
relation: includes
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C7
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-08-26
status: active
boundary: 聯合公告說規格涵蓋 xPU-HBF host interface；沒有任一 xPU 具名 silicon、指令集、驅動或整合結果。
next_trigger: 可定位規範條款與具名運算晶片公開主機介面、命令、錯誤處理及實體測試。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I15
view: industry
from_id: concept:hbf-commercialization
to_id: capability:hbf-software-io
relation: requires
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C7,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C8,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C12
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-10-15
status: active
boundary: 公告摘要只證明規格與架構納入 software I/O／co-design；不證明驅動、資料放置、編排或目標工作負載已完成。
next_trigger: 公開軟體介面、驅動、資料放置策略、具名裝置與端到端工作負載結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I16
view: industry
from_id: concept:hbf-commercialization
to_id: stage:hbf-compliance
relation: passes_through
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C13
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: 合規與互通是規格時鐘的必要未來節點；本輪沒有可定位方法、具名 pass list 或跨廠矩陣。
next_trigger: OCP 或參與者公開 compliance checklist、test suite、具名 pass result 或 multi-vendor interoperability matrix。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I17
view: industry
from_id: concept:hbf-commercialization
to_id: process:hbf-simulation-to-service-evidence-bridge
relation: requires
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C14,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C16,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C17
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-26
status: active
boundary: 三張成績單是研究中心用 Sandisk fact sheet 與 MLCommons inference rules 建立的比較框架，不是 HBF 或 MLPerf 共同標準；內部模擬、方法欄位與規格公告都不等於 sample、qualification 或 deployment。
next_trigger: 同一具名 HBF sample 公開裝置 raw、完整 memory map 與固定模型／資料／品質／scenario 的 TTFT／TPOT／throughput／tail／failure／power／cost，且由接收方交叉確認。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I18
view: industry
from_id: concept:hbf-commercialization
to_id: metric:hbf-nominal-usable-working-set-capacity-contract
relation: measured_by
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C14,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C15,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C17
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-26
status: active
boundary: 405B×8-bit＝405GB、405／512＝79.1015625% 與 107GB 是 N=1 weights-only 名目換算；未計可用容量、KV cache、activation、runtime、workspace、冗餘、錯誤管理、分片或 page alignment，不能證明完整工作集放得下。
next_trigger: 具名 HBF sample 與系統公開 software-visible capacity、完整 weights／KV／activation／workspace memory map、placement、page／alignment 與運行中 peak occupancy。
-->
