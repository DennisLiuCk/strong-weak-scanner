# 推論晶片測試需求八分母知識圖譜

本圖把晶片產品數量、測試插入點、內容與時間、多站效率、設備狀態、生產結果、合格既有
容量及公司財務歸因分開，並用產能護照把測試秒數橋接到連續 test-cell 等價數與離散實體缺口。
公開證據目前只能支持部分工程機制；圖上的族群是後續搜尋路由，不是訂單、受惠、獲利或投資排名。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: inference-compute-test-demand
root_node_id: concept:inference-compute-test-demand
label: 推論晶片測試需求八分母
summary: 從產品組合與數量 插入點 內容時間 並行效率 設備狀態 良率重測 合格既有容量與增量資本支出 追到公司財務歸因，並分開連續單元等價數與向上取整的實體缺口，避免把晶片顆數或 tester TAM 線性換算成設備台數與台股受惠。
article_ids: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM
status: active
-->

<!-- knowledge_edge
edge_id: KG-ITD-C01
view: company
from_id: company:advantest
to_id: concept:inference-compute-test-demand
relation: cites_demand
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C1
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-01
review_due: 2026-10-30
status: active
boundary: Advantest 的 CY2026 tester TAM 與驅動因素是設備商市場預估 不是已實現市場收入 分架構貢獻 台灣公司訂單或獲利。
next_trigger: Advantest 更新同口徑 TAM 並把變動橋接到具名產品數量 插入點 時間 站數 利用率 增量設備與出貨。
-->

<!-- knowledge_edge
edge_id: KG-ITD-C02
view: company
from_id: company:teradyne
to_id: concept:inference-compute-test-demand
relation: provides_tooling
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C5
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Teradyne 與 Advantest 都公開測試平台及並行或重用能力 本圖不判定市占 效能勝負或客戶選擇。
as_of: 2026-08-12
review_due: 2026-10-30
status: active
boundary: UltraFLEXplus 產品頁的 test-cell 降幅是供應商宣稱 沒有共同產品 測試程式 客戶分母或實際生產結果。
next_trigger: Teradyne 與客戶公布固定產品 test program baseline site count parallel efficiency utilization cell count 與量產前後結果。
-->

<!-- knowledge_edge
edge_id: KG-ITD-C03
view: company
from_id: company:amazon
to_id: concept:inference-compute-test-demand
relation: owns_platform
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C6
note_refs:
evidence_state: inference
commercial_stage: deployment
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: AWS 自研晶片業務與容量承諾只支持產品組合研究方向 沒有晶片數 測試插入點 設備採購或台灣供應商映射。
next_trigger: Amazon 公布具名 Trainium 世代的實際部署數 產品測試參考平面與供應商雙向可核對的採購或服務分母。
-->

<!-- knowledge_edge
edge_id: KG-ITD-C04
view: company
from_id: company:microsoft
to_id: concept:inference-compute-test-demand
relation: owns_platform
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C6
note_refs:
evidence_state: inference
commercial_stage: deployment
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: Maia 效能與部署敘述不提供晶片數 測試內容 test-cell 設備採購或台灣供應商財務分母。
next_trigger: Microsoft 公布具名 Maia 世代的部署數 測試驗收要求與供應商可對帳的產品 期間 數量及財務結果。
-->

<!-- knowledge_edge
edge_id: KG-ITD-C05
view: company
from_id: company:amkor
to_id: concept:inference-compute-test-demand
relation: tests
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C8
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Amkor 與 Teradyne 都公開多階段測試能力 但不是同一客戶產品流程 本圖不判定封測份額 稼動率或採購。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: Amkor 能提供 wafer probe 組裝中測試 final ATE SLT 與 burn in 不表示同一產品全數採用 每站均為 100% 或已形成新增收入。
next_trigger: Amkor 與客戶以同一具名產品版本公布 insertion test cell configuration sample coverage exit criteria utilization 與量產結果。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I01
view: industry
from_id: concept:inference-compute-test-demand
to_id: stage:test-device-mix-volume
relation: passes_through
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C6
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 自研 ASIC CPU DRAM 與 GPU 並行只界定產品組合方向 沒有同期間合格出貨顆數與被替代產品分母。
next_trigger: 平台或製造商按具名產品與期間公布合格出貨 部署 替代量及測試參考平面。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I02
view: industry
from_id: concept:inference-compute-test-demand
to_id: stage:test-insertion-map
relation: passes_through
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C4
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-10-30
status: active
boundary: IEEE 1838 公開摘要定義測試存取情境 不規定具名產品必測站數 抽測比例 時間 良率或設備需求。
next_trigger: 具名多晶粒產品公布 pre stack partial stack complete stack package final SLT 各站實際必測與抽測流程。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I03
view: industry
from_id: concept:inference-compute-test-demand
to_id: stage:test-content-coverage
relation: passes_through
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C6
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-10-30
status: active
boundary: 設備商提及 scan data 結構測試與良率學習 不提供同產品故障模型 圖樣 覆蓋 誤判 漏測或增量內容量。
next_trigger: 固定產品與 test program 公布 fault model pattern count coverage false pass false fail 與版本變更前後結果。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I04
view: industry
from_id: concept:inference-compute-test-demand
to_id: stage:test-time-power-pin-thermal
relation: passes_through
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C5
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: Advantest 與 Teradyne 產品資料都描述高複雜度 test-cell 因素 但沒有共同產品與測試條件可比較。
as_of: 2026-08-12
review_due: 2026-10-30
status: active
boundary: 產品頁列出時間 功率 接腳 溫控或 yield learning 壓力 不等於客戶實際秒數 瓦數 pin 數 uptime 或設備台數。
next_trigger: 同一產品公布各插入點 test time power pin temperature setup downtime 與 production distribution。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I05
view: industry
from_id: concept:inference-compute-test-demand
to_id: stage:test-multisite-throughput
relation: passes_through
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C5
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: 兩家設備商都提供並行或高容量路徑 但公開數字的設備 測試階段 定義與基準不同。
as_of: 2026-08-12
review_due: 2026-10-30
status: active
boundary: up to 720 DUT 與 15% 至 50% test-cell reduction 是不可比供應商產品宣稱 不是全年有效吞吐或市場平均。
next_trigger: 同產品同程式公布 site count parallel efficiency utilization UPH yield downtime 與 cell-hour 實績。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I06
view: industry
from_id: concept:inference-compute-test-demand
to_id: stage:test-yield-retest-escape
relation: passes_through
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 現有來源沒有同產品各站良率 重測 報廢成本 escape 誤判或提早篩除後節省的完整分母。
next_trigger: 製造與封測公布同一 lot 各站投入 pass retest scrap escape 與改善前後成本。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I07
view: industry
from_id: concept:inference-compute-test-demand
to_id: stage:test-installed-base-capex
relation: passes_through
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C6
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: Advantest 與 Teradyne 都主張平台相容 升級或重用 本圖不假設所有客戶都能以相同比例吸收需求。
as_of: 2026-08-12
review_due: 2026-10-30
status: active
boundary: 可升級與可重用不等於實際重用率 已裝機餘裕 改機成本 交期或增量採購已知。
next_trigger: 客戶按平台公布 installed base available hours upgrade reuse conversion cost delivery and incremental cell purchases。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I08
view: industry
from_id: concept:inference-compute-test-demand
to_id: stage:test-company-financial-attribution
relation: passes_through
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C3,MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C7
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 全球 tester TAM 平台部署與設備商產品能力沒有台灣公司產品 份額 出貨期間 收入 毛利或現金分子。
next_trigger: 買方與台灣公司對上同產品 插入點 設備或介面 數量 期間 驗收 收入 毛利與現金。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I09
view: industry
from_id: concept:inference-compute-test-demand
to_id: group:ipdesign
relation: routes_to
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C3
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 矽智財只是一個可測試性設計與專案搜尋入口 沒有具名客戶 NRE tape out 量產收入或毛利證據。
next_trigger: 買方與公司文件對上同一晶片 DFT 或設計交付 專案節點 量產期間 收入與毛利。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I10
view: industry
from_id: concept:inference-compute-test-demand
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C3,MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C7
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 封測只是一個 test insertion 服務搜尋入口 沒有具名測項 test-cell 稼動率 報價 收入或毛利證據。
next_trigger: 客戶與封測公司對上同一產品 插入點 測項 時間 數量 稼動率 收入與毛利。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I11
view: industry
from_id: concept:inference-compute-test-demand
to_id: group:semiequip
relation: routes_to
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C3,MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C7
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 半導體設備族群只是一個探針卡 載板 測試座與自動化搜尋入口 全球 tester TAM 不證明其訂單 市占或獲利。
next_trigger: 客戶與公司文件對上同一產品 插入點 介面 part number 資格 出貨期間 收入與毛利。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I12
view: industry
from_id: concept:inference-compute-test-demand
to_id: concept:test-responsibility-passport
relation: requires
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C9
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: IEEE 設備商 封測商與晶片公司分別支持存取 插入 服務與生命週期責任 本圖未主張存在唯一共同護照標準。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: 十欄護照是研究可比性框架 不是標準強制欄位 客戶 recipe 合格門檻 測試時間 權重或設備採購公式。
next_trigger: 同一具名產品與版本公開物件 目的 故障 存取 刺激 test cell 覆蓋 結果 責任及變更十欄並能前後站對帳。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I13
view: industry
from_id: concept:inference-compute-test-demand
to_id: process:test-change-triggered-regression
relation: requires
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C9
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: AMD NXP Amkor 與 Teradyne 分別描述生命週期 資格 服務與 insertion 但沒有單一公開產品的完整 change matrix。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: 變更需要影響分析不表示每次全套重測 也不證明新增測試時數超過程式最佳化 並行 重用與既有設備餘裕。
next_trigger: 具名產品公布設計 封裝 介面 程式 製程或工作負載變更項 受影響測項 重測版本 pass fail 與簽核結果。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I14
view: industry
from_id: concept:inference-compute-test-demand
to_id: process:test-result-lineage-feedback
relation: requires
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C9
note_refs:
evidence_state: inference
commercial_stage: deployment
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: AMD 公開 DFT 到 customer return PPM 的回饋方向 NXP 補失效生命週期 本圖不主張任一公司已公開完整零件病歷。
as_of: 2026-08-12
review_due: 2026-09-15
status: active
boundary: 串接前後站與 RMA 只建立根因和修正能力 不表示每個現場事件皆為製造缺陷 也不能由單一退貨估算全體 defect rate 或 tester 台數。
next_trigger: 同一產品以序號 lot wafer package board system identity 串接各站結果 現場條件 根因 corrective action 與新增測項成效。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I15
view: industry
from_id: concept:inference-compute-test-demand
to_id: process:test-cell-capacity-passport
relation: requires
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C12,MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C13,MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C14
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: SEMI E10 E79 E116 是一條設備時間與生產力方法鏈 Advantest 與 Teradyne 則提供 test cell 產品語境 本圖不把標準摘要改寫成 tester 採購公式。
as_of: 2026-08-14
review_due: 2026-10-30
status: active
boundary: 產能護照是研究比較契約 不是 SEMI 強制的 tester 欄位 全產業標準 OEE 公式 設備採購門檻 公司訂單或財務歸因。
next_trigger: 同一具名產品與期間公開 test program 秒數 重測 有效站數 equipment state time in state good output 合格既有容量 阻塞原因與增量交付。
-->

<!-- knowledge_edge
edge_id: KG-ITD-I16
view: industry
from_id: concept:inference-compute-test-demand
to_id: metric:test-seconds-to-qualified-cell-equivalents
relation: measured_by
claim_refs: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C13,MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM#C14
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-10-30
status: active
boundary: N=2 假想情境只示範量綱與離散取整 沒有產品 設備 工廠 run 抽樣誤差 價格 收入 公司效果或投資結論。
next_trigger: 同一產品用原始設備狀態時數與 good output 重算連續 cell equivalent 扣除合格未承諾容量後 再對到實際增量採購 安裝 資格與驗收。
-->
