# AI 資料讀取與儲存路徑知識圖譜

本圖把訓練時餵資料、故障前保存進度與服務擴充時搬模型拆成三種工作，並把 checkpoint 的
暫存、上傳、耐久、正確回載與訓練有效時間分成不同驗證節點，再分開應用資料、主機寫入、
NAND 寫入與額定壽命四本帳。公司線只表示已核驗的儲存能力
或平台路徑；沒有買方客戶認證、部署分母與財務資料前，不把相鄰能力畫成訂單。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: ai-storage-data-plane
root_node_id: concept:ai-storage-data-plane
label: AI 資料讀取與儲存路徑
summary: 以最慢讀取時間 checkpoint 完成與復原 以及模型副本位置分開三種人工智慧資料工作 再用十欄效能護照 八格復原護照與十二欄耐久護照把 IOPS 吞吐 延遲 併行 裝置狀態 應用主機NAND寫入 額定壽命 I/O模擬 暫存上傳 耐久回載 訓練有效時間與公司能力保持在不同證據層。
article_ids: MI-2026-08-09-AI-STORAGE-DATA-PLANE
status: active
-->

<!-- knowledge_edge
edge_id: KG-ASD-C01
view: company
from_id: company:8299
to_id: concept:ai-storage-data-plane
relation: has_capability
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C4,MI-2026-08-09-AI-STORAGE-DATA-PLANE#C6
note_refs: 8299#S1,8299#S4
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-16
review_due: 2026-08-28
status: active
boundary: 群聯文件只證實 NAND 控制器 韌體 企業級 SSD 與廣義 AI Ecosystem 產品能力；沒有把具名產品接到資料集 checkpoint 或模型分發的客戶資格 部署 訂單 收入或毛利。
next_trigger: 平台與群聯雙向揭露具名產品 路徑角色 qualification production 數量及財務分母。
-->

<!-- knowledge_edge
edge_id: KG-ASD-C02
view: company
from_id: company:meta
to_id: concept:ai-storage-data-plane
relation: owns_platform
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C1
note_refs:
evidence_state: verified
commercial_stage: deployment
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-01
review_due: 2026-08-31
status: active
boundary: Meta 公開自身 BLOB storage production 架構與 stall 機制；不代表其他 operator 採同一架構或外部設備供應商與財務曝險已知。
next_trigger: Meta 公布具名硬體配置 pMax cache hit failure domain 與前後期部署分母。
-->

<!-- knowledge_edge
edge_id: KG-ASD-C03
view: company
from_id: company:nvidia
to_id: concept:ai-storage-data-plane
relation: owns_platform
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-24
review_due: 2026-08-31
status: active
boundary: ModelExpress 文件證明權重來源與 transport fallback 能力；不證明所有 inference stack 採用 production deployment 或各路徑硬體增量。
next_trigger: NVIDIA 或客戶公布 production rollout cold-start SLO 路徑命中率與具名設備配置。
-->

<!-- knowledge_edge
edge_id: KG-ASD-C04
view: company
from_id: company:google
to_id: concept:ai-storage-data-plane
relation: owns_platform
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C11
note_refs:
evidence_state: verified
commercial_stage: deployment
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-06-16
review_due: 2026-08-31
status: active
boundary: Google Cloud 文件證實自身多層 checkpoint 路徑與單一具名工作負載組態的 vendor-reported Goodput 結果；沒有公開重複 run 變異原始資料完整 baseline 設備 BOM 或台灣供應商映射。
next_trigger: Google 或客戶公開版本化受測系統 重複 run fault injection restore correctness Runtime Goodput 資源成本與具名設備配置。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I01
view: industry
from_id: concept:ai-storage-data-plane
to_id: capability:training-dataset-fetch
relation: contains
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C1
note_refs:
evidence_state: verified
commercial_stage: deployment
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-01
review_due: 2026-08-31
status: active
boundary: Meta 證實自身訓練資料讀取與 GPU stall；不建立跨 operator SLO 一致性或設備需求量。
next_trigger: 第二個 operator 公布可比的 dataset fetch pMax 同步停等及設備配置。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I02
view: industry
from_id: concept:ai-storage-data-plane
to_id: capability:checkpoint-persistence
relation: contains
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-31
status: active
boundary: AWS 文件支持 write read barrier 與多層 checkpoint 取捨；不是跨平台 benchmark 客戶採用或具名設備資格。
next_trigger: Operator 公布 checkpoint window recovery point failure domain media endurance 與 production 配置。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I03
view: industry
from_id: concept:ai-storage-data-plane
to_id: capability:model-artifact-distribution
relation: contains
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-24
review_due: 2026-08-31
status: active
boundary: ModelExpress 具名 remote local peer 與 fallback 路徑；不表示每個 worker 都讀 SSD 或硬體需求可按模型大小等比例外推。
next_trigger: Production fleet 公布 first-worker 與 peer-worker 路徑比例 cold start 及設備分母。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I04
view: industry
from_id: concept:ai-storage-data-plane
to_id: capability:tail-latency-control
relation: requires
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C1
note_refs:
evidence_state: verified
commercial_stage: deployment
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-01
review_due: 2026-08-31
status: active
boundary: Meta 的同步訓練案例支持尾端讀取造成 stall；不指定通用 pMax 門檻或瓶頸必在儲存媒體。
next_trigger: 公開 pMax 分解 metadata cache network queue 與 media 各自貢獻。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I05
view: industry
from_id: concept:ai-storage-data-plane
to_id: capability:direct-storage-gpu-transfer
relation: includes
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-24
review_due: 2026-08-31
status: active
boundary: GPUDirect Storage 是 ModelExpress 的條件式 fallback 之一；不是所有節點的必要路徑或特定 SSD NIC 供應商 design win。
next_trigger: 客戶公布 GDS 啟用條件 命中率 效能與 production hardware BOM。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I06
view: industry
from_id: concept:ai-storage-data-plane
to_id: component:local-ssd
relation: uses_component
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C1,MI-2026-08-09-AI-STORAGE-DATA-PLANE#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-24
review_due: 2026-08-31
status: active
boundary: Meta 與 NVIDIA 路徑都可使用 local flash storage；不表示每條資料流都經過本地 SSD 或其容量隨 compute 等比例增加。
next_trigger: 同一 production cluster 公布 local SSD 型號 容量 路徑比例 命中率與利用率。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I07
view: industry
from_id: concept:ai-storage-data-plane
to_id: component:shared-storage
relation: uses_component
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C1,MI-2026-08-09-AI-STORAGE-DATA-PLANE#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-31
status: active
boundary: Operator 架構包含共享或 durable storage 層；不證明其媒體 拓撲 供應商 TCO 或新增容量。
next_trigger: Operator 公布 shared durable tier 的設備配置 容量 耐久與前後期需求。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I08
view: industry
from_id: concept:ai-storage-data-plane
to_id: concept:ai-memory-hierarchy
relation: integrated_with
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C5
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: Google 多層 checkpoint 直接包含 node RAM 跨 slice 或 superblock 副本與 Cloud Storage；但將三條資料流統一放回記憶體分層仍是跨來源研究推論，不表示 HBM system RAM local SSD 與 shared storage 可以互換或需求可重複加總。
next_trigger: 同一平台公開資料 placement SLO 搬移成本與各層容量利用率。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I09
view: industry
from_id: concept:ai-storage-data-plane
to_id: group:memory
relation: routes_to
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C6,MI-2026-08-09-AI-STORAGE-DATA-PLANE#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-28
status: active
boundary: 控制器 SSD 與儲存系統能力只形成 memory 族群搜尋路由；沒有買方資格 產品部署 訂單或財務證據。
next_trigger: 平台與公司雙向確認具名產品在三條契約之一的 qualification production 與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I10
view: industry
from_id: concept:ai-storage-data-plane
to_id: group:serverodm
relation: routes_to
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-31
status: active
boundary: 儲存節點與機櫃整合只形成 ODM 搜尋路由；不證明 universe 公司承擔特定 I/O 契約或取得增量訂單。
next_trigger: 買方 test plan 與 ODM 文件對齊 storage-node BOM 路徑責任 部署量 收入與毛利。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I11
view: industry
from_id: concept:ai-storage-data-plane
to_id: process:checkpoint-recovery-measurement-passport
relation: includes
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C12
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 八格復原護照是研究中心整合 MLCommons PyTorch 與 Google 官方文件的檢查方法 不是三方共同標準 已完成 benchmark 或客戶採用證據。
next_trigger: 具名 operator 以同一 production workload 公開完整版本化 baseline treatment 重複 run 故障回載 訓練結果與成本。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I12
view: industry
from_id: concept:ai-storage-data-plane
to_id: metric:checkpoint-completion-semantics
relation: measured_by
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C10
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: PyTorch 直接區分 staging 與 upload completion 並提供 load API；耐久副本 正確回載與指定故障域仍需受測系統另行驗證。
next_trigger: Framework 或 operator 公開 stage upload durable replica restore 四種事件與 partial failure 的共同 trace。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I13
view: industry
from_id: concept:ai-storage-data-plane
to_id: metric:training-runtime-goodput
relation: measured_by
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C11
note_refs:
evidence_state: verified
commercial_stage: deployment
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: Google 定義 Runtime Goodput 並公開單一多層 checkpoint 組態結果；沒有 run 數 分布 變異 原始樣本或跨平台複現 因此不能形成一般效果量。
next_trigger: 具名 operator 以固定模型與 cluster 公開 event level lost steps resume time Runtime Goodput 重複 run 不確定度及完整資源成本。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I14
view: industry
from_id: concept:ai-storage-data-plane
to_id: process:ai-storage-performance-passport
relation: requires
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C15,MI-2026-08-09-AI-STORAGE-DATA-PLANE#C16,MI-2026-08-09-AI-STORAGE-DATA-PLANE#C17
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-31
status: active
boundary: 十欄效能護照是研究中心整合 SNIA device method Meta pMax mechanism 與 MLCommons reproducibility fields 的可比性框架 不是三方共同標準 benchmark pass 或客戶 qualification。
next_trigger: 同一 production AI workload 公開 device與end-to-end pair 完整十欄 重複run 失敗操作 分布 goodput 資源成本及具名設備。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I15
view: industry
from_id: concept:ai-storage-data-plane
to_id: metric:workload-conditioned-tail-latency
relation: measured_by
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C14,MI-2026-08-09-AI-STORAGE-DATA-PLANE#C15,MI-2026-08-09-AI-STORAGE-DATA-PLANE#C17
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-31
status: active
boundary: 工作負載條件化尾端延遲必須固定block mix client thread QD OIO state cache scope completion與事件數；單一average maximum或peak IOPS不能外推AI停算 公司採用或財務。
next_trigger: 同一cluster同步保存per IO distribution pMax timeout retry accelerator stall device version與多run不確定度。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I16
view: industry
from_id: concept:ai-storage-data-plane
to_id: process:ai-storage-endurance-passport
relation: requires
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C18,MI-2026-08-09-AI-STORAGE-DATA-PLANE#C19,MI-2026-08-09-AI-STORAGE-DATA-PLANE#C20,MI-2026-08-09-AI-STORAGE-DATA-PLANE#C21,MI-2026-08-09-AI-STORAGE-DATA-PLANE#C22
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-28
status: active
boundary: 十二欄耐久護照是研究中心整合KIOXIA Solidigm OCP與NVM Express官方文件的對帳框架 不是四方共同標準 production qualification 或公司採用證據。
next_trigger: 同一production AI workload公開應用host與NAND三層bytes WAF drive days健康重建產品配置及買賣雙方財務共同鍵。
-->

<!-- knowledge_edge
edge_id: KG-ASD-I17
view: industry
from_id: concept:ai-storage-data-plane
to_id: metric:application-host-nand-write-ledgers
relation: measured_by
claim_refs: MI-2026-08-09-AI-STORAGE-DATA-PLANE#C18,MI-2026-08-09-AI-STORAGE-DATA-PLANE#C21,MI-2026-08-09-AI-STORAGE-DATA-PLANE#C22
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-28
status: active
boundary: A H N三層帳只有在裝置時間窗bytes定義副本範圍與counter契約一致時才能重算H除A N除H與N除A 任一產品型錄數字都不能替代production telemetry。
next_trigger: Operator與SSD供應商以同一checkpoint或dataset workload公開application bytes Data Units Written physical NAND bytes counter lineage WAF與失效重建紀錄。
-->
