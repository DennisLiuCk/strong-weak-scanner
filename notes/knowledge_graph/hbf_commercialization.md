# HBF 商用化知識圖譜

本圖把 HBF 的規格時鐘與產品時鐘拆開：OCP v0.7.0 已能直接逐條核對，但 pre-1.0 缺口、
合規方法、具名產品 pass、跨廠互通、實體樣品、裝置整合及客戶資格仍是不同節點，不能跨級
變成量產、財務曝險或 HBM 的已證實替代品。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: hbf-commercialization
root_node_id: concept:hbf-commercialization
label: HBF 商用化
summary: 以規格時鐘與產品時鐘追蹤 HBF 從 NAND／logic base die 架構、OCP v0.7.0、規格到合規八欄護照、具名 pass／互通到 memory sample、device sample、客戶資格與量產的證據階梯，並用三張成績單分開名目／可用／工作集容量、內部模擬與固定品質的推論服務結果。
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
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C19,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C12
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-10-15
status: retired
boundary: 原線條把公告世代 C9 與分層架構放在一起；C9 已由直接規格世代 C19 取代，改由 I19 保留相同應用推論與新的規格／產品時鐘邊界。
next_trigger: 已由 KG-HBF-I19 接續；本歷史線條不再參與 active graph。
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
boundary: C7／C8 只驗證第一版規格的公告與供應商摘要；直接 OCP v0.7.0 另由 I21／C18 承接。兩層都不等於合規、互通或產品結果。
next_trigger: OCP 公開 v1.0／勘誤、完整 HBF Profile、條款變更紀錄與合規方法。
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
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C8,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C18
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-24
review_due: 2026-08-26
status: active
boundary: S13 已定位 UCIe 3.0、x64 host channel、Format 6 與 AoU 0.8；但第 78 頁引用的 HBF Profile Appendix D 缺失，仍未建立把具名 silicon、共同 compliance 方法、測試條件與跨廠結果串起來的證據鏈。
next_trigger: OCP 或參與者補齊 HBF Profile 與固定 compliance 方法，並由具名產品公布 UCIe／AoU 版本、端點、封裝、測試條件與結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I14
view: industry
from_id: concept:hbf-commercialization
to_id: component:xpu-hbf-host-interface
relation: includes
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C7,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C18
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-24
review_due: 2026-08-26
status: active
boundary: S13 已定位 host roles、讀寫與錯誤處理要求；仍未建立把具名 xPU／base-die silicon、驅動、系統整合與 result ID 串起來的證據鏈。
next_trigger: 具名 xPU 與 HBF part 公開介面版本、命令與錯誤處理、驅動、整合條件及實體測試結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I15
view: industry
from_id: concept:hbf-commercialization
to_id: capability:hbf-software-io
relation: requires
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C7,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C8,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C12,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C18
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-24
review_due: 2026-10-15
status: active
boundary: S13 已定位 memory mapping、refresh 與 failure rules；仍無公開驅動、runtime placement、具名裝置或目標工作負載結果。
next_trigger: 具名裝置公開固定版本的軟體介面、驅動、runtime／資料放置策略與端到端工作負載結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I16
view: industry
from_id: concept:hbf-commercialization
to_id: stage:hbf-compliance
relation: passes_through
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C20
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: retired
boundary: C13 曾把直接規格與合規結果混在同一未驗證節點；S13 已解決規格原文，合規、具名 pass 與跨廠矩陣仍由 C20／I20 接續。
next_trigger: 已由 KG-HBF-I20 接續；本歷史線條不再參與 active graph。
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

<!-- knowledge_edge
edge_id: KG-HBF-I19
view: industry
from_id: concept:hbf-commercialization
to_id: concept:ai-memory-hierarchy
relation: integrated_with
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C19,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C12
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-24
review_due: 2026-10-15
status: active
boundary: SK hynix 把 HBF 放入分層記憶體架構，OCP v0.7.0 讓共同規則可直接核對；產品時鐘仍未建立具名、已交付、可運行且附規格、測試包絡與接收方結果的完整 sample 證據鏈，也沒有系統證明它與 HBM、DRAM、CXL memory 或 SSD 的實際分工。
next_trigger: 具名 AI 系統公布 HBF part、memory map、資料放置、軟體調度、固定工作負載與端到端結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I20
view: industry
from_id: concept:hbf-commercialization
to_id: stage:hbf-compliance
relation: passes_through
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C20
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-24
review_due: 2026-09-30
status: active
boundary: v0.7.0 有 mandatory-form requirements 與 test／debug interfaces，並要求客戶依相應產品的 official test guidelines 驗證；但規格未附具名產品 guidelines、共同 test suite、具名 pass、第二供應商產品或跨廠互通矩陣，公開 no-find 也不排除私有測試。
next_trigger: OCP 或參與者公開 v1.0／errata、完整 HBF Profile、固定 test plan／pass criteria、具名 part／result ID、recognition 或至少兩家獨立供應商的同版互通結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I21
view: industry
from_id: concept:hbf-commercialization
to_id: standard:hbf-base-die-spec-v0-7-0
relation: passes_through
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C18
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-30
status: active
boundary: 已驗證 v0.7.0 文件身分、條款與未完成區；它仍有缺失 Appendix D、preliminary／TBD、單位／表格衝突與 product-specific 欄位，且不是具名 silicon、測試、合規或產品 recognition。
next_trigger: OCP 發布 v1.0／勘誤與完整 HBF Profile，並能把修訂條款對應到共同 test contract。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I22
view: industry
from_id: concept:hbf-commercialization
to_id: process:hbf-specification-to-conformance-passport
relation: requires
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C19
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-24
review_due: 2026-09-30
status: active
boundary: 八欄護照是研究中心分開規格版本、要求定位、端點、義務、條件、觀測量、測法與結果 ID 的閱讀框架，不是 OCP 官方表單或證書；欄位完整也不自動證明產品適用、可靠或可量產。
next_trigger: 具名 HBF part 以同一規格、test plan 與 result ID 填滿八欄，並由第二實作或接收方交叉確認。
-->
