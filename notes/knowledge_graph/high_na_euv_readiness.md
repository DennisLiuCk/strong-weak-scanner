# High-NA EUV 導入成熟度知識圖譜

本圖將掃描機供應商與客戶／研發機構分開，並把出貨、運轉、製程資格、產品晶圓與 HVM
插入投影成不同節點。它不以工具數量推估客戶良率或台灣公司財務曝險。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: high-na-euv-readiness
root_node_id: concept:high-na-euv-readiness
label: High-NA EUV 導入
summary: 追蹤 High-NA EUV 從 scanner shipment、customer operation、process qualification、product wafer 到 HVM insertion 的證據階梯與生態系依賴。
article_ids: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER
status: active
-->

<!-- knowledge_edge
edge_id: KG-HNA-C01
view: company
from_id: company:asml
to_id: concept:high-na-euv-readiness
relation: produces
claim_refs: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER#C1,MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: shipment
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-22
review_due: 2026-10-01
status: active
boundary: ASML 已出貨 High-NA 並揭露平台處理量；不等於客戶 process qualification、HVM、良率或供應鏈財務貢獻。
next_trigger: ASML 確認 HVM requirements 達成並由客戶端交叉確認 insertion。
-->

<!-- knowledge_edge
edge_id: KG-HNA-C02
view: company
from_id: company:intel
to_id: concept:high-na-euv-readiness
relation: tests
claim_refs: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER#C4
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2024-04-18
review_due: 2026-10-15
status: active
boundary: Intel 完成首台系統安裝並開始 calibration；這個早期里程碑不證明 14A HVM、客戶產品或良率。
next_trigger: Intel 公布實際 High-NA 節點、層數、qualification、產品晶圓與量產結果。
-->

<!-- knowledge_edge
edge_id: KG-HNA-I01
view: industry
from_id: organization:imec
to_id: concept:high-na-euv-readiness
relation: tests
claim_refs: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-18
review_due: 2026-10-01
status: active
boundary: imec 是研發與 pilot 資格環境；EXE:5200 到廠及 2026Q4 目標不等於晶圓廠 HVM。
next_trigger: imec 公布 fully qualified 結果、範圍、限制與客戶移轉節點。
-->

<!-- knowledge_edge
edge_id: KG-HNA-I02
view: industry
from_id: concept:high-na-euv-readiness
to_id: component:high-na-euv-scanner
relation: uses_component
claim_refs: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: shipment
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-22
review_due: 2026-10-01
status: active
boundary: 導入核心設備是 0.55 NA scanner；設備存在不代表整合製程已 qualification。
next_trigger: 客戶端公開 scanner acceptance、availability、throughput 與 process window。
-->

<!-- knowledge_edge
edge_id: KG-HNA-I03
view: industry
from_id: concept:high-na-euv-readiness
to_id: product:exe-5200b
relation: includes
claim_refs: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: shipment
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-22
review_due: 2026-10-01
status: active
boundary: ASML 表示首台第二代 EXE:5200B 已在客戶端；沒有客戶名稱、製程層或 HVM 結果。
next_trigger: 客戶確認 EXE:5200B 的 acceptance、產品晶圓與量產節點。
-->

<!-- knowledge_edge
edge_id: KG-HNA-I04
view: industry
from_id: concept:high-na-euv-readiness
to_id: stage:high-na-operation
relation: reaches_stage
claim_refs: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-22
review_due: 2026-10-01
status: active
boundary: 六台系統運轉是 fleet 里程碑，不等於每台通過客戶 acceptance 或進入 production。
next_trigger: ASML 或客戶提供逐系統 acceptance、availability、throughput 與使用層級。
-->

<!-- knowledge_edge
edge_id: KG-HNA-I05
view: industry
from_id: concept:high-na-euv-readiness
to_id: stage:high-na-process-qualification
relation: passes_through
claim_refs: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-18
review_due: 2026-10-01
status: active
boundary: Verified 只代表 imec 公開 2026Q4 qualification 目標；不是資格已完成。
next_trigger: imec 公告 fully qualified，並列出測試範圍與尚未成熟項目。
-->

<!-- knowledge_edge
edge_id: KG-HNA-I06
view: industry
from_id: concept:high-na-euv-readiness
to_id: stage:high-na-product-wafer
relation: reaches_stage
claim_refs: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-15
review_due: 2026-10-01
status: active
boundary: ASML 表示客戶開始測試 product wafers；沒有客戶、節點、層數、良率或量產分母。
next_trigger: 客戶公布實際產品晶圓、層數、process window、缺陷與良率。
-->

<!-- knowledge_edge
edge_id: KG-HNA-I07
view: industry
from_id: concept:high-na-euv-readiness
to_id: stage:high-na-hvm-insertion
relation: passes_through
claim_refs: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER#C5
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-01
status: active
boundary: HVM insertion 是 2027–2028 待完成節點；工具 fleet 與 product-wafer testing 不能替它提前畢業。
next_trigger: 客戶確認節點、產品、High-NA 層數、穩定良率與量產日期。
-->

<!-- knowledge_edge
edge_id: KG-HNA-I08
view: industry
from_id: concept:high-na-euv-readiness
to_id: component:high-na-resist
relation: requires
claim_refs: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER#C8
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-01
status: active
boundary: ASML／imec 將 resist 列入成熟條件；沒有具名材料、客戶資格、份額或財務證據。
next_trigger: 客戶或研發機構公開具名 resist 的 process window、缺陷、qualification 與量產使用。
-->

<!-- knowledge_edge
edge_id: KG-HNA-I09
view: industry
from_id: concept:high-na-euv-readiness
to_id: capability:high-na-metrology
relation: requires
claim_refs: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER#C8
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-01
status: active
boundary: 量測與檢查是 ecosystem dependency，不等於任一設備商已被 High-NA 客戶 qualification。
next_trigger: 客戶具名 metrology／inspection tool、測試項目、qualification、出貨與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-HNA-I10
view: industry
from_id: concept:high-na-euv-readiness
to_id: group:semiequip
relation: routes_to
claim_refs: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-01
status: active
boundary: High-NA 形成塗佈 顯影 蝕刻 清洗 量測與檢查搜尋路由，沒有 universe 公司具名 qualification 或財務證據。
next_trigger: 客戶與公司雙向核對具名設備、qualification、出貨與收入。
-->

<!-- knowledge_edge
edge_id: KG-HNA-I11
view: industry
from_id: concept:high-na-euv-readiness
to_id: group:material
relation: routes_to
claim_refs: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-01
status: active
boundary: 光阻 化學品 晶圓與耗材形成搜尋路由，沒有具名材料規格、客戶資格、出貨或財務貢獻。
next_trigger: 客戶與材料商雙向揭露具名產品、qualification、量產用量與收入。
-->
