# 224G PCB 材料到 BER 七關資格鏈知識圖譜

本圖把材料數字、測法、stackup、板級不連續點、通道損耗、link-up、FEC 前後 counter、
零事件上界、跨廠量產與公司歸因分開。本輪公開證據已支持多個相鄰關卡，尚未支持同一塊板的
完整鏈或台灣公司 224G 財務價值。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: 224g-pcb-qualification-chain
root_node_id: concept:224g-pcb-qualification-chain
label: 224G PCB 材料到 BER 七關資格鏈
summary: 從 Dk Df測法 玻纖 銅粗糙度 stackup coupon via connector loss budget與dB參考面護照 COM追到link-up pre-FEC corrected activity FERC post-FEC zero-event暴露 跨廠量產與公司歸因 避免把datasheet QPL 單次demo 不同fixture曲線或零事件當成整板資格與收入。
article_ids: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN
status: active
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-C01
view: company
from_id: company:panasonic-industry
to_id: concept:224g-pcb-qualification-chain
relation: names_application
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C7
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: limited_source
exclusivity_scope: Panasonic 的公開活動頁只支持 MEGTRON 9 與 224 Gbps future design 主張；本輪沒有第二份買方文件確認同一產品資格。
as_of: 2025-01-15
review_due: 2026-09-15
status: active
boundary: 公司 roadmap 不等於同板 Dk Df-to-BER multi-source qualification 客戶量產 份額 價格或財務。
next_trigger: 具名客戶公開 MEGTRON 9 board ID stackup channel BER qualification 與量產分母。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-C02
view: company
from_id: company:6274
to_id: concept:224g-pcb-qualification-chain
relation: qualified_at
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C8
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: 台燿 TU-1300N 與 TU-1300E 只確認 IPC-4103/17 QPL 列項 不等於 IPC-4103C 224G reference board BER 客戶量產或收入。
next_trigger: 客戶與台燿雙向公布同料號 224G board stackup channel BER qualification 量產與財務分母。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I01
view: industry
from_id: organization:ipc
to_id: concept:224g-pcb-qualification-chain
relation: owns_platform
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C1,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C5,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C8
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: IPC 維護測法 標準狀態與 QPL 但不替任何 224G system board BER 客戶採用或財務背書。
next_trigger: IPC 發布正式新版及可對齊材料 成板與高頻 qualification 的測試附件。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I02
view: industry
from_id: organization:ieee-8023
to_id: concept:224g-pcb-qualification-chain
relation: owns_platform
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C2,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C5
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: IEEE 802.3 task force 接收多家公司貢獻並進行公開 ballot；單份 contribution 不代表共同採納或最終條文。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: Contribution 與 D3.2 ballot 支持設計研究及標準時鐘 不證明特定材料板或產品 qualification。
next_trigger: 正式發布的 amendment test specification reference channel 與可重算 data。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I03
view: industry
from_id: organization:oif
to_id: concept:224g-pcb-qualification-chain
relation: owns_platform
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C3,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C5
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: OIF demo 由多家公司元件與儀器組成 且 CEI-224G project 由產業社群推進 不屬單一公司獨有結果。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: OIF demo 與 project objective 不等於正式 IA 同板材料病歷 量產 qualification 或公司財務。
next_trigger: CEI-224G 正式 IA 與具 board identity material manifest channel data BER 分母的 multi-vendor 附件。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I04
view: industry
from_id: organization:ethernet-alliance
to_id: concept:224g-pcb-qualification-chain
relation: tests
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C6
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: HSN plugfest 涵蓋多種 host 與 interconnect 組合 但公開摘要沒有列出完整 N 與逐配置結果。
as_of: 2026-03-31
review_due: 2026-09-15
status: active
boundary: 約 90 percent link establishment 且 N 未揭露 不可改寫成 BER 量產良率 供應商排名或統計信賴度。
next_trigger: 下一次 plugfest 公布逐配置 N board channel BER ILT condition failure root cause 與重測結果。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I05
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: metric:pcb-dk-df
relation: measured_by
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C1,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C4
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: IPC 同時列多種 Dk Df 方法 顯示量測路徑不只一種；方法結果是否可換算仍需實際資料。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: Dk Df 必須帶方法 頻率 試片 方向與環境 不建立未對齊小數的材料排名。
next_trigger: 同料號多方法重複量測 原始資料 不確定度與轉換關係被公開。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I06
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: component:pcb-stackup
relation: includes
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C2,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C4
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: IEEE contribution 直接提供一組 M7N standard PCIe AIC stackup 與 routing 研究 但不是唯一可行疊構。
as_of: 2022-03-17
review_due: 2026-09-15
status: active
boundary: 一組 reference design 不代表所有 board layer geometry material lot 或量產製程。
next_trigger: 具名 production reference board 的完整 stackup fab lot coupon 與 channel 對照。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I07
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: component:low-dk-glass-weave
relation: includes
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C4,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C5
note_refs:
evidence_state: inference
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: IPC-4414 working draft 只建立超低 Dk 玻纖研究入口 沒有同板 glass style skew BER 或 universe 公司 qualification。
next_trigger: 同一 board 公開 glass style resin ratio differential skew channel data BER 與量產 qualification。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I08
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: component:low-profile-copper-foil
relation: includes
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C4,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C5
note_refs:
evidence_state: inference
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: IPC-4562C working draft 與高頻工程需求只建立銅箔粗糙度入口 不證明特定 foil grade 224G qualification 份額或價格。
next_trigger: 同板只替換 copper foil 的受控 S parameter COM BER 與量產 lot 重現。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I09
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: stage:pcb-loss-coupon
relation: passes_through
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C1,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C4
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: IPC 提供成板 loss 方法而 IEEE OIF 各提供板路研究或 loss board；尚未對上同一 coupon identity。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: Coupon loss 只涵蓋指定結構與 reference plane 不能替完整 production board 所有路徑背書。
next_trigger: Coupon 與正式 board 同 lot stackup route raw S parameter 及去嵌入對照。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I10
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: component:pcb-via-connector
relation: includes
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C2,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C4
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: IEEE contribution 直接研究 via stub 而 OIF reach 定義包含 connector；不同文件不是同一 board qualification。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: Via 與 connector 是完整通道不連續點 但本輪沒有 universe 公司具名產品或同板 BER 因果歸因。
next_trigger: 同板 via stub connector geometry S parameter COM BER 與製程 tolerance sweep。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I11
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: stage:channel-loss-budget
relation: passes_through
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C2,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C3,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C4
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: IEEE 提供 PCB design 與 COM model 研究 OIF 提供 die-to-die demo loss；參考平面與 board identity 不同。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: 不把不同配置的 dB 相減或相加來歸因材料改善 份額 ASP 或成本。
next_trigger: 同一 package-to-package topology 的完整 S parameter manifest reference plane 與 COM input output。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I12
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: metric:pre-post-fec-ber
relation: measured_by
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C3,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C4
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: OIF demo 有 BERT 與 BER measurement 但未公開總位元 錯誤數 FEC 前後及統計不確定度。
as_of: 2024-03-26
review_due: 2026-09-15
status: active
boundary: BER 是完整收發系統結果 不能直接換算成 Df 或單一材料貢獻。
next_trigger: 固定 Tx Rx PRBS rate FEC 總位元 error count duration environment 與 raw result。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I13
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: standard:cei-224g
relation: uses_standard
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C3,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C5
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: OIF CEI-224G 由多家公司共同開發且 demo 有跨供應商配置 但 MR LR 等仍為 project objective。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: Demo snapshot 與 current project 不等於 final IA compliant product 或 production deployment。
next_trigger: 正式 IA compliance test plan named products 與 reproducible results。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I14
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: standard:ieee-p8023dj
relation: uses_standard
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C5
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: IEEE ballot 是公開多方標準程序 不屬任何單一材料或系統公司。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: D3.2 recirculation ballot 尚非正式發布 也不自動認證任何產品。
next_trigger: IEEE 正式批准發布 amendment 與相關 compliance channel data。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I15
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: standard:ipc-4103
relation: uses_standard
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C8
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: IPC-4103/17 QPL 提供基材資格時鐘 不等於在製 IPC-4103C 或 224G system board qualification。
next_trigger: IPC 新版 slash sheet 與具名 224G board test contract 對上相同 material product。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I16
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: stage:multi-vendor-board-qualification
relation: passes_through
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C9
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: 本輪沒有同一 board identity 串起材料 stackup S parameter COM BER FEC 與兩個獨立組合重現。
next_trigger: 固定 board ID 與 test contract 的 multi-vendor raw data 及 pass fail outcome。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I17
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: stage:224g-pcb-commercial-attribution
relation: passes_through
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C10
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: 沒有 universe 公司 224G board 客戶料號 qualification 量產分母 ASP 份額收入或毛利閉環。
next_trigger: 買方與公司雙向確認同料號 board qualification 出貨期間 數量 單價與可辨識財務。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I18
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: group:pcb
relation: routes_to
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C10
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: 只建立 PCB CCL 族群的材料 板路與 qualification 搜尋路由 不建立受惠 份額 價格 訂單或財務方向。
next_trigger: 平台 客戶與 PCB CCL 公司對上具名產品 同板 BER 量產與財務分母。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I19
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: process:pcb-db-reference-plane-passport
relation: requires
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C13,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C14
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-09-15
status: active
boundary: dB 參考面護照是研究中心依單位定義 量測方法與不同公開配置建立的可比性框架 不是 IPC IEEE OIF 新增共同表單或 qualification。
next_trigger: 同一224G board公開quantity sign port mode frequency impedance planes fixture chain segment raw processed pair repeatability uncertainty COM與BER。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I20
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: metric:fixture-deembedded-differential-insertion-loss
relation: measured_by
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C12,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C13
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-09-15
status: active
boundary: 去嵌入結果依fixture model與reference plane而變 且不能由單一曲線反推材料貢獻 BER 客戶資格或公司財務。
next_trigger: 固定DUT與planes公開calibrated raw fixture S-parameters deembedding version processed SDD21及獨立重複量測。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I21
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: process:pcb-link-ber-exposure-passport
relation: requires
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C18,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C19
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: OIF Ethernet Alliance 與 NIST 分別固定metric layer link establishment及zero-event模型邊界；十欄護照是本文整合而非共同表單。
as_of: 2026-08-24
review_due: 2026-09-15
status: active
boundary: 護照只提升量測可重建性；本輪文件中同一224G PCB完整七層與十欄共同觀測N=0 不建立qualification 客戶採用或公司財務。
next_trigger: 同一DUT board revision公開topology link state pattern environment FEC layer numerator instrument-counted exposure independence exclusions model及七層outcome。
-->

<!-- knowledge_edge
edge_id: KG-224GPCB-I22
view: industry
from_id: concept:224g-pcb-qualification-chain
to_id: metric:pcb-zero-event-upper-error-rate
relation: measured_by
claim_refs: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C17,MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN#C19
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: NIST提供通用HPP零事件公式 OIF提供212.5Gbps既有demo速率；兩者不是共同CEI測試或產品結果。
as_of: 2026-08-24
review_due: 2026-09-15
status: active
boundary: 只在事件定義 instrument-counted exposure 固定率與相依性假設明示時報一側上界；不是CEI compliance pass 零風險 材料效果或公司證據。
next_trigger: 具名224G DUT公開零事件層 raw counter valid exposure excluded intervals burst及lane correlation檢查與預先指定alpha。
-->
