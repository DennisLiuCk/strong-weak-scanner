# AI 電容角色知識圖譜

本圖按位置、電壓、頻帶與任務拆分 rack CBU、高壓 DC-link、板級 bulk 與近晶片去耦，
再以有效容量、頻率阻抗、紋波溫升與任務壽命核對實際可用能力。公司節點只投影其公開產品角色；
族群線仍是搜尋路由，沒有一條線代表台灣公司已供貨。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: ai-capacitor-role-map
root_node_id: concept:ai-capacitor-role-map
label: AI 電容角色地圖
summary: 把 rack CBU、高壓 bus／DC-link、板級 bulk 與 package／near-die decoupling 分成不同查核單位，再用四道工作條件區分標稱容量與實際可用能力；產品角色不等於台灣供應商量產或財務曝險。
article_ids: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP
status: active
-->

<!-- knowledge_edge
edge_id: KG-ACR-C01
view: company
from_id: company:texas-instruments
to_id: concept:ai-capacitor-role-map
relation: has_capability
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C1
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: TI 展示 EDLC 800V CBU；OCP 同時保留 application-specific CBU，沒有排他供應證據。
as_of: 2026-03-16
review_due: 2026-09-01
status: active
boundary: Reference design 支持 EDLC CBU 技術角色，不證明客戶 qualification、production BOM、部署量、供應份額或收入。
next_trigger: 具名 production rack 採用 CBU 並公布 qualification、field duty cycle、BOM 與量產出貨。
-->

<!-- knowledge_edge
edge_id: KG-ACR-C02
view: company
from_id: company:tdk
to_id: concept:ai-capacitor-role-map
relation: names_application
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C2
note_refs:
evidence_state: verified
commercial_stage: application_opportunity
materiality: named_product
exclusivity: multi_source
exclusivity_scope: TDK 公開自身高低壓產品地圖；Murata 與 TI 提供其他 capacitor 路徑，沒有排他供應證據。
as_of: 2026-04-28
review_due: 2026-09-01
status: active
boundary: 公司產品地圖支持 aluminum／MLCC／film／polymer 等角色，不是客戶共同 BOM、跨公司份額或台灣供應商證據。
next_trigger: TDK 或買方公布具名 part、qualification、production configuration、出貨量與可辨識財務分母。
-->

<!-- knowledge_edge
edge_id: KG-ACR-C03
view: company
from_id: company:murata
to_id: concept:ai-capacitor-role-map
relation: names_application
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C3
note_refs:
evidence_state: verified
commercial_stage: application_opportunity
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Murata 公開 MLCC、silicon 與 polymer capacitor 的 PDN 角色；文件沒有聲稱唯一材料或排他供應。
as_of: 2026-04-25
review_due: 2026-09-01
status: active
boundary: Webinar Q&A 支持公司技術角色，不固定共同頻帶、替代率、量產客戶、BOM、份額或財務貢獻。
next_trigger: 具名客戶 qualification 與 production BOM 對齊 Murata part、placement、測試、出貨及財務結果。
-->

<!-- knowledge_edge
edge_id: KG-ACR-I01
view: industry
from_id: concept:ai-capacitor-role-map
to_id: concept:ai-power-buffering
relation: integrated_with
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C4
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-01
status: active
boundary: CBU 是 capacitor role map 與 power-buffering hierarchy 的交集；不代表其他 DC-link、board 或 package capacitors 也屬儲能模組。
next_trigger: 同一 production rack 公布 CBU 到 board／package PDN 的完整 architecture、duty cycle 與 BOM。
-->

<!-- knowledge_edge
edge_id: KG-ACR-I02
view: industry
from_id: concept:ai-capacitor-role-map
to_id: component:rack-capacitor-bank
relation: contains
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C1
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: OCP 與 TI 均支持 rack CBU 路徑，且容量與實作依 application 決定。
as_of: 2026-03-16
review_due: 2026-09-01
status: active
boundary: CBU 角色已具體，不固定 chemistry、容量、元件數、供應商或 production deployment。
next_trigger: OCP 或客戶公布 CBU interface、qualification、field operation 與 production BOM。
-->

<!-- knowledge_edge
edge_id: KG-ACR-I03
view: industry
from_id: concept:ai-capacitor-role-map
to_id: component:dc-link-capacitor
relation: contains
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C2
note_refs:
evidence_state: verified
commercial_stage: application_opportunity
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-28
review_due: 2026-09-01
status: active
boundary: TDK 公司地圖支持 400–800V aluminum／MLCC／film 路徑，不等於所有平台三類同時採用或具有固定份額。
next_trigger: Production platform 公布 DC-link voltage、ripple、lifetime、qualified parts、數量與供應商。
-->

<!-- knowledge_edge
edge_id: KG-ACR-I04
view: industry
from_id: concept:ai-capacitor-role-map
to_id: component:board-bulk-capacitor
relation: contains
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C2,MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C3
note_refs:
evidence_state: verified
commercial_stage: application_opportunity
materiality: named_product
exclusivity: multi_source
exclusivity_scope: TDK 與 Murata 兩條供應商鏈皆提供低壓／bulk capacitor 角色，未主張排他材料或供應。
as_of: 2026-04-28
review_due: 2026-09-01
status: active
boundary: 支持 board bulk 的技術角色，不固定容量、顆數、替代率、客戶、份額或財務貢獻。
next_trigger: 同一 production board 公布 transient target、qualified parts、placement、數量與 field validation。
-->

<!-- knowledge_edge
edge_id: KG-ACR-I05
view: industry
from_id: concept:ai-capacitor-role-map
to_id: component:polymer-capacitor
relation: contains
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C3
note_refs:
evidence_state: verified
commercial_stage: application_opportunity
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-25
review_due: 2026-09-01
status: active
boundary: Murata 把 polymer capacitor 放在 low-frequency bulk stability；不代表固定切點、客戶採用、顆數或優於其他材料。
next_trigger: Production board 的 target impedance、transient、part number、qualification 與 BOM 證明實際角色。
-->

<!-- knowledge_edge
edge_id: KG-ACR-I06
view: industry
from_id: concept:ai-capacitor-role-map
to_id: component:mlcc-decoupling
relation: contains
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C3
note_refs:
evidence_state: verified
commercial_stage: application_opportunity
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-25
review_due: 2026-09-01
status: active
boundary: Murata 把 MLCC 對應 high-frequency decoupling；不固定頻帶、DC-bias derating、顆數、客戶或供應份額。
next_trigger: Production package／board 公布 impedance target、placement、qualified MLCC、測試與量產配置。
-->

<!-- knowledge_edge
edge_id: KG-ACR-I07
view: industry
from_id: concept:ai-capacitor-role-map
to_id: component:silicon-capacitor
relation: contains
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C3
note_refs:
evidence_state: verified
commercial_stage: application_opportunity
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-25
review_due: 2026-09-01
status: active
boundary: Murata 把 silicon capacitor 對應 near-die ultra-fast response；不證明其取代 MLCC、量產採用、良率、份額或收入。
next_trigger: 具名 package 公布 silicon capacitor placement、qualification、production yield、BOM 與客戶部署。
-->

<!-- knowledge_edge
edge_id: KG-ACR-I08
view: industry
from_id: concept:ai-capacitor-role-map
to_id: group:passive
relation: routes_to
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-30
status: active
boundary: 角色圖只把 passive 族群導向具名產品與 qualification 搜尋；沒有 universe 公司 production BOM、份額、訂單或財務證據。
next_trigger: 買方與台灣公司雙向確認 part、位置、規格、qualification、量產、收入與毛利。
-->

<!-- knowledge_edge
edge_id: KG-ACR-I09
view: industry
from_id: concept:ai-capacitor-role-map
to_id: group:powersupply
relation: routes_to
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-30
status: active
boundary: 電源模組決定 capacitor placement 與規格只形成搜尋路由，不證明台灣廠採用、量產、訂單或獲利。
next_trigger: 具名電源模組與客戶文件公布 PDN／CBU configuration、qualified parts、shipment 與財務分母。
-->

<!-- knowledge_edge
edge_id: KG-ACR-I10
view: industry
from_id: concept:ai-capacitor-role-map
to_id: metric:capacitor-effective-capacitance
relation: measured_by
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C6
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-01
status: active
boundary: Murata 與 TDK 支持高介電常數／Class 2 MLCC 應看實際工作電壓下的有效容量；沒有全產品共同降額、platform pass line、顆數或供應商資料。
next_trigger: 具名 production platform 公布 part-specific bias／temperature curve、實際工作點、qualification pass／fail 與 BOM。
-->

<!-- knowledge_edge
edge_id: KG-ACR-I11
view: industry
from_id: concept:ai-capacitor-role-map
to_id: metric:capacitor-impedance-spectrum
relation: measured_by
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C7
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-01
status: active
boundary: KEMET／YAGEO 的頻率與溫度曲線只屬 ESE 鋁電解系列；不固定其他材料的 SRF、目標頻帶、控制穩定性或替代關係。
next_trigger: 同一 production power stage 公布完整 ripple／transient spectrum、part-specific Z／ESR／ESL curve、layout 與量測結果。
-->

<!-- knowledge_edge
edge_id: KG-ACR-I12
view: industry
from_id: concept:ai-capacitor-role-map
to_id: metric:capacitor-ripple-temperature-rise
relation: measured_by
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C8
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-01
status: active
boundary: 供應商文件支持紋波、ESR、頻率、環境與散熱共同影響溫升；不同材料與測試不能合成共同額定或跨料號排行。
next_trigger: 客戶以實際 waveform、ambient、board／busbar、cooling 與 thermal sensor 公布 qualification 溫升及失效結果。
-->

<!-- knowledge_edge
edge_id: KG-ACR-I13
view: industry
from_id: concept:ai-capacitor-role-map
to_id: metric:capacitor-mission-life
relation: measured_by
claim_refs: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C8,MI-2026-08-03-AI-CAPACITOR-ROLE-MAP#C9
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-01
status: active
boundary: 四道工作條件是研究框架；ESE 壽命公式與 TDK 溫升建議不可跨技術套用，也不等於客戶保固、field reliability 或財務貢獻。
next_trigger: 具名平台固定 mission profile、加速試驗、failure criteria、field hours、BOM 與 supplier／customer 雙向結果。
-->
