# AI 光學三軸組態與產品證據知識圖譜

本圖先把交換晶片、電光轉換與光纖路徑串起來，把一條鏈路的近端／遠端配對與 port／module
分母固定，再把光引擎位置、電介面訊號處理與雷射位置拆成三個可獨立核對的軸，最後連回平台
產品、具名生態系角色、互通／現場驗證與公司財務。
線條較粗只能代表已公開的標準、角色或成熟度；沒有具名組態、部署、出貨、份額與損益證據前，
不代表某個排列組合已商品化，也不代表供應商已取得重大經濟利益。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: cpo-networking
root_node_id: concept:cpo-networking
label: AI 光學三軸組態與產品證據
summary: 以交換晶片到光纖的五個位置，先拆 endpoint pairing、官方 connector 衝突與 port／module 分母，再拆光引擎 placement、retimed／linear 訊號處理與 integrated／external laser，連接 Q3450、Spectrum-X、可插拔產品、NVIDIA、SPIL、Lumentum、互通部署分母與財務證據。
article_ids: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE
status: active
-->

<!-- knowledge_edge
edge_id: KG-CPO-C01
view: company
from_id: company:nvidia
to_id: concept:cpo-networking
relation: owns_platform
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C1
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-31
review_due: 2026-08-26
status: active
boundary: NVIDIA 將 Spectrum-X Ethernet Photonics 定義為進入生產；未揭露 CPO 交換器數、埠數、收入、客戶驗收或全網路占比。
next_trigger: NVIDIA 或首批採用者披露 production shipment、部署交換器數、埠數與實際可靠度／功耗結果。
-->

<!-- knowledge_edge
edge_id: KG-CPO-C02
view: company
from_id: company:3711
to_id: concept:cpo-networking
relation: platform_lists
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C3
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-01
review_due: 2026-10-31
status: active
boundary: NVIDIA 直接列名 SPIL 的 CPO chip-level packaging、assembly、testing 角色；沒有日月光公司級出貨量、收入、毛利或供應份額。
next_trigger: 日月光投控正式文件揭露 Spectrum-X／CPO 客戶、量產、產能利用與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-CPO-C03
view: company
from_id: company:lumentum
to_id: concept:cpo-networking
relation: platform_lists
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C5
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-03-18
review_due: 2026-10-31
status: active
boundary: Lumentum 自身公告 InP laser 的具名 Spectrum-X Photonics 角色；未證明 sole source、量產出貨量、份額、收入或毛利。
next_trigger: NVIDIA 與 Lumentum 對同一產品完成量產出貨雙向核對，並出現可辨識財務資料。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I01
view: industry
from_id: product:spectrum-x-ethernet-photonics
to_id: concept:cpo-networking
relation: generation_of
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C1
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-31
review_due: 2026-08-26
status: active
boundary: 產品名稱與 NVIDIA production 敘述已確認；不代表所有 Spectrum-6 form factor 都是 CPO，也不表示客戶已大規模部署。
next_trigger: 公開型號、shipment、客戶 deployment 與 CPO／pluggable 產品組合。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I02
view: industry
from_id: concept:cpo-networking
to_id: component:co-packaged-optics
relation: includes
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C1
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-31
review_due: 2026-08-26
status: active
boundary: Spectrum-X Ethernet Photonics 是具名 CPO 產品路徑；本線不推定其他交換器、連線距離或客戶也採 CPO。
next_trigger: 更多具名量產型號與實際部署位置。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I03
view: industry
from_id: concept:cpo-networking
to_id: component:pluggable-optics
relation: competes_with
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C9
note_refs:
evidence_state: inference
commercial_stage: production
materiality: named_product
exclusivity: multi_source
exclusivity_scope: NVIDIA Spectrum-6 同代 form factor 與 1.6T pluggable product path
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: 同代產品證據仍支持 CPO／pluggable 共存，但 C9 已把光引擎位置、訊號處理與雷射位置拆成三軸；這條競合線不能代表單一替代時鐘。
next_trigger: 平台商以同一版本公開三軸組態、型號、埠數、部署位置、可靠度與資本支出占比。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I04
view: industry
from_id: concept:cpo-networking
to_id: stage:product-production
relation: reaches_stage
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C1
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-31
review_due: 2026-08-26
status: active
boundary: 生產是平台產品階段，不等於 production shipment 已量化、客戶驗收或供應商財務認列。
next_trigger: shipment、deployment 與 supplier financial evidence。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I05
view: industry
from_id: concept:cpo-networking
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C4
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-31
status: active
boundary: SPIL 的平台列名形成封裝測試研究入口，但 C4 明確保留公司級新增訂單與財務重大性為未驗證。
next_trigger: 日月光正式文件揭露具名 CPO 量產、收入、毛利或資本回報。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I06
view: industry
from_id: concept:cpo-networking
to_id: concept:cpo-three-axis-architecture
relation: includes
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C9
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: OIF 文件支持拆開 optical-engine placement、signal-processing mode 與 laser placement；三軸是閱讀與驗證框架，不表示所有排列都可行、已標準化或已商品化。
next_trigger: 具名平台以可定位文件填滿三軸組態並公開 qualification 與部署分母。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I07
view: industry
from_id: concept:cpo-networking
to_id: component:npo-optical-engine
relation: includes
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C6
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2022-02-03
review_due: 2026-08-26
status: active
boundary: OIF framework 直接描述 on-board 與 socketed NPO 安排；沒有具名 NPO 產品、production、customer qualification 或財務證據。
next_trigger: 正式 IA 或具名產品公開 NPO placement、socket／fiber attach、返修、測試與部署結果。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I08
view: industry
from_id: concept:cpo-networking
to_id: concept:optical-interface-processing-mode
relation: includes
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C9
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: OIF current work 同時涵蓋 retimed、transmit-retimed 與 linear interfaces，並把它們放進 pluggable、NPO、CPO 的研究範圍；current project scope 不是正式 IA 或產品 pass result。
next_trigger: 正式文件或具名產品公開處理模式、PHY／DSP 責任、功耗、channel contract 與測試結果。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I09
view: industry
from_id: concept:cpo-networking
to_id: component:external-laser-source
relation: includes
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C7
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2025-01-08
review_due: 2026-08-26
status: active
boundary: OIF framework 與 ELSFP IA 證實外部雷射可和 CPO optical engine 分離並成為 field-replaceable unit；不代表具名產品已互通、部署或較可靠。
next_trigger: 具名 ELS／optical-engine 配對公開 conformity、application link budget、replacement 與長期 reliability 結果。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I10
view: industry
from_id: concept:cpo-networking
to_id: metric:optical-loss-budget
relation: measured_by
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C7
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2025-01-08
review_due: 2026-08-26
status: active
boundary: OIF 文件指出 external laser、connector／pigtail 與分光會改變 insertion loss、所需輸出功率及安全控制；沒有同一產品的完整 loss budget、margin 或失效統計。
next_trigger: 以同一雷射、連接器、分光、光引擎與環境版本公開最差條件 power／loss budget 及原始測試結果。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I11
view: industry
from_id: concept:cpo-networking
to_id: stage:optics-multivendor-field-validation
relation: requires
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C8,MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C10
note_refs:
evidence_state: unverified
commercial_stage: validation
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: 3.2T CPO 與 ELSFP IA 只固定指定互通邊界，ELSFP 明確排除應用特定 power／noise／wavelength；本輪沒有完整跨廠矩陣、field replacement、可靠度、客戶部署或財務鏈。
next_trigger: 同一具名產品與版本完成 IA conformity、應用 link budget、跨廠互通、現場更換、長期可靠度與客戶部署分母。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I12
view: industry
from_id: concept:cpo-networking
to_id: process:cpo-reliability-exposure-passport
relation: measured_by
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C11,MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C13
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-26
status: active
boundary: Broadcom／Meta 公布 100 萬 400G-equivalent port-device-hours 與零 link flap，但沒有埠數、各埠時長、共享群組、完整事件、raw log 或比較組；護照是研究中心查核框架，不是兩家公司共同標準。
next_trigger: 同一產品版本公開受測單元、暴露／設限、環境工作量、完整 failure taxonomy、共同故障、事件日誌及同條件 comparison cohort。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I13
view: industry
from_id: concept:cpo-networking
to_id: metric:zero-event-reliability-bound
relation: measured_by
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C12,MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C13
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-26
status: active
boundary: NIST／SEMATECH 公式只在 HPP／exponential、固定總暴露與相應獨立性等條件下給單側界線；333,808 port-device-hours 是條件式教材，不是 Broadcom／Meta 公布 MTBF、field lifetime 或保固。
next_trigger: 取得 Meta 完整研究與 raw exposure／event structure 後，先檢查 constant-rate、independence、censoring 與 failure-definition 假設，再決定是否估計及採哪個模型。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I14
view: industry
from_id: concept:cpo-networking
to_id: process:cpo-optical-power-budget-passport
relation: measured_by
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C14,MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C15
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-26
status: active
boundary: ITU-T 固定通用 worst-case power-budget 方法，OIF 固定 CPO／ELSFP 的介面與排除邊界；十欄護照是研究中心為具名 CPO 應用建立的查核框架，不是 ITU／OIF 共同發布的 profile 或產品 pass result。
next_trigger: 同一具名 CPO／ELS／receiver 組合公開 application version、reference points、power quantity、Tx／path／Rx limits、penalty／inclusion map、raw BER、重複與客戶 sign-off。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I15
view: industry
from_id: concept:cpo-networking
to_id: metric:worst-case-optical-power-margin
relation: measured_by
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C14,MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C15
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-26
status: active
boundary: A／B 的 +1.5／−0.5 dB low-power margin 與 +0.5／+2.5 dB overload headroom 是 N=2 個假想光路的確定性教材；不是 CPO、ELSFP、Ethernet、lane、module、switch、run、sampling SE／t 或商業結果。
next_trigger: 具名產品以共同 reference points、mean／OMA／OSNR 定義、end-of-life corners 與 BER／FEC 契約公開兩端 margin、raw measurements、跨廠矩陣及客戶 qualification。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I16
view: industry
from_id: concept:cpo-networking
to_id: concept:optical-link-endpoint-pairing
relation: includes
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C16,MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C17
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-23
review_due: 2026-09-30
status: active
boundary: NVIDIA Q3450 正式手冊直接列出 CPO↔CPO、CPO↔pluggable switch 與 CPO↔pluggable compute 的支援拓撲；同一手冊對 72／144 MPO connectors 尚有衝突，兩個數都不得做 module 算術，且不證明三種配對的客戶 deployed mix、模組數、出貨或財務。
next_trigger: NVIDIA 先在同一 revision 裁決 72／144 MPO 與一對一／一對二 port mapping；客戶或平台再公開逐鏈路 endpoint-pair BOM、part number、ports per module 與 installed／active／spare census。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I17
view: industry
from_id: concept:cpo-networking
to_id: process:cpo-endpoint-pair-deployment-passport
relation: requires
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C18
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-23
review_due: 2026-09-30
status: active
boundary: 八欄端點配對部署護照是研究中心依 Q3450 拓撲提出的需求分母框架，不是 NVIDIA 標準或市場統計；欄位齊全也不自動證明淨模組減量、成本、供應商份額或財務。
next_trigger: 同一具名 deployment 以共同版本與期間公開端點、料號、每模組埠數、installed／active／spare、維修、baseline 及採購／shipment／財務對帳。
-->
