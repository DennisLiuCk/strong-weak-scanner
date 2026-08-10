# AI 儲存資料平面：不是 SSD 容量越大越好，而是三條 I/O 契約要分開驗

<!-- research_topic
topic_id: MI-2026-08-09-AI-STORAGE-DATA-PLANE
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-09
source_published_at: 2026-07-01
last_reviewed_at: 2026-08-09
review_due: 2026-08-28
source_type: mixed
publisher: Meta
publisher_domain: engineering.fb.com
canonical_url: https://engineering.fb.com/2026/07/01/data-infrastructure/metas-ai-storage-blueprint-at-scale/
source_chain_id: ai-storage-data-plane-primary-scan-20260809
stock_ids: 8299
group_ids: memory,serverodm
trigger_type: ai_storage_io_contract_separation
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C5
base_confidence: medium
confidence_basis: Meta、AWS 與 NVIDIA 三條獨立一手鏈分別公開訓練資料讀取、checkpoint 與模型權重分發的路徑及失效代價，足以支持三種 I/O 契約必須分開驗證；8299 群聯只由公司法說與已獨立核驗筆記確認企業級 SSD 與廣義 AI Ecosystem 能力，尚無任何文件把其產品接到上述 operator 架構、production qualification 或可辨識損益
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-09
from: initial
to: inbox
reason: captured_distinct_dataset_checkpoint_and_model_artifact_io_contracts
evidence: source_chain:ai-storage-data-plane-primary-scan-20260809
-->
<!-- transition
date: 2026-08-09
from: inbox
to: triaged
reason: separated_operator_mechanisms_from_taiwan_company_exposure
evidence: sources:S1,S2,S3,S4
-->
<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_plain_language_wave2_no_conclusion_change
evidence: editorial:plain_language_wave2
-->
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_reader_led_why_it_matters_no_conclusion_change
evidence: editorial:reader_led_why_it_matters
-->
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_reader_section_leads_plain_language_no_conclusion_change
evidence: editorial:reader_section_leads_plain_language
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **資料集讀取（dataset fetch）**：訓練時持續把下一批樣本送到 GPU；只要最慢的一筆讀取超時，同步訓練的其他 GPU 也可能一起等。
- **訓練存檔（checkpoint）**：定期把模型參數、最佳化器狀態與訓練進度存下來，故障後才能接著跑；寫得太慢會停算，讀得太慢會拖長復原。
- **模型權重分發（model artifact distribution）**：把已訓練好的模型權重與執行快取送到新的推論節點，決定 cold start、擴容與滾動更新要等多久。
- **pMax／尾端延遲**：不是平均讀取時間，而是最慢端的上界；同步工作只要被一個落後者卡住，平均值再漂亮也救不了整步完成時間。
- **GPUDirect Storage／RDMA**：讓儲存或另一台機器更直接地把資料送進 GPU，減少主機記憶體搬運；它是一條資料路徑，不是某種 SSD 已取得訂單的證明。
- **AWS**：Amazon Web Services；本文只引用其 checkpoint 架構文章，不把雲端服務建議當成跨平台實測。
- **AI Ecosystem**：群聯法說使用的廣義產品組合，包含企業級 SSD、aiDAPTIV、AI PC／網通／伺服器與 Boot Drive，不是純資料中心儲存收入。
- **NIC**：網路介面卡；在遠端儲存與 RDMA 路徑負責資料搬運，但存在於架構圖不等於特定供應商取得訂單。
- **SLO**：服務水準目標，例如允許的尾端延遲、checkpoint 完成時間或模型冷啟動時間；沒有共同 SLO 就不能直接比較三條路徑。
- **NAND／NVMe**：NAND 是快閃記憶體媒體，NVMe 是主機存取非揮發儲存的協定家族；兩者都只是資料路徑的一層。
- **HBM（高頻寬記憶體）**：放在運算晶片附近、供 GPU 高速使用的記憶體；它和長期保存資料的 SSD 承擔不同工作。
- **P2P**：peer-to-peer，讓已持有模型的節點直接把資料交給另一節點；它可能避開重複讀取遠端或本地儲存。

### 三句話抓重點

- Meta 公開的訓練資料路徑顯示，AI 儲存要同時承受突發與持續吞吐、可預測的 pMax 延遲與跨區資料移動；尾端讀取過慢會直接讓 GPU 停等。
- AWS 的 checkpoint 架構與 NVIDIA 的模型權重分發又是另外兩種流量：前者在持久性與復原時間間取捨，後者會在 object storage、local storage 與 peer GPU 之間選最快路徑。
- 因此「AI 需要更多儲存」不能直接翻成 SSD 顆數或控制器營收；8299 群聯雖有企業級 SSD 與廣義 AI 產品組合，仍缺相同平台的 qualification、部署分母與可辨識損益。

### 為什麼重要

**先分清三條資料流。** 市場常把高頻寬記憶體（HBM）、CXL、企業級 SSD、資料湖與模型載入
混成同一個「AI 記憶體／儲存」題材。其實資料集讀取、訓練存檔與模型權重分發的失敗條件
完全不同。

**每條路徑卡住的方式不同。** 資料集讀取怕最慢的一筆拖住所有 GPU。訓練存檔要在寫入時間、
可回復進度與故障範圍間取捨。模型權重分發則取決於副本已在哪裡，以及網路能否直接送到 GPU。
同一顆 SSD 即使峰值速度很高，也不代表三條路徑都已通過驗收。

**最後才把需求接回公司。** 拆開後，研究問題會從「容量成長多少」變成「哪條路徑被驗收、
瓶頸落在儲存裝置、控制器、網路介面卡還是儲存節點，以及誰能提出正式運作數據」。只有先
回答這些問題，才有機會把產業需求接到公司，不能把雲端業者的架構文章直接讀成台灣供應商訂單。

### 接下來怎麼追

- 2026-08-31 重查 Meta、AWS 與 NVIDIA 是否新增可定位的尾端延遲、存檔時間窗、冷啟動目標、故障範圍、媒體耐用度或正式運作數據。
- 2026Q2 群聯法說後、最晚 2026-08-28，檢查企業級 SSD／AI Storage 是否首次從廣義 AI 產品組合的 38% 中拆出產品、客戶認證、出貨與毛利口徑。
- 等待同一平台把儲存節點、本地 NVMe、網路介面卡／交換器、GPUDirect Storage 路徑與實際物料表／客戶驗證串在一起；只有其中一段的產品公告不算閉環。

### 想一想

- 如果快取、預取與 peer-to-peer 分發把大部分尖峰吸收掉，AI 成長還會增加同樣比例的持久儲存設備嗎？
- 一個企業級 SSD 的順序讀寫峰值很好，但 pMax、故障域與同步 checkpoint 都未通過平台驗收，它能解決這三條契約中的哪一條？
- 廣義 AI 產品營收同時含企業 SSD、AI PC、網通與 Boot Drive 時，還能用那個百分比判斷資料中心儲存曝險嗎？

## 主張與證據帳本

`證實` 只代表指定 operator／公司文件直接支持精確措辭；它不代表三家採用同一架構，
也不代表任何台灣產品已進入其 BOM、通過 qualification 或產生可辨識收入。

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: Meta 將現代 AI 儲存工作負載描述為同時具有突發與持續高吞吐、可預測且受限的 pMax 延遲及可變 I/O 型態；其訓練範例說明單一 GPU 的 storage-fetch 尾端延遲可讓同步步驟整體延後，並以區域 flash、分散式記憶體快取、read-plan cache、hedged read 與動態 concurrency control 降低 stall
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-08-09
basis: S1 第 15–57 段直接描述工作負載特性、落後 GPU 對同步步驟的影響，以及新資料路徑、快取與擁塞控制做法
boundary: 這是 Meta 自身 BLOB-storage production 架構，不代表所有 operator 有相同 pMax、媒體層級、cache hit rate 或硬體配置，也不建立任何外部供應商份額
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: AWS 把大模型 checkpoint 分成持久化訓練狀態的 write path 與故障後回載狀態的 read path，指出同步 checkpoint 會形成訓練 barrier，並提出 asynchronous、hierarchical distribution 與 fast／durable 多層儲存來分別處理停算、外部流量與耐久性取捨
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-08-09
basis: S2 的 Checkpoint fundamentals、hierarchical distribution、asynchronous checkpointing 與 multi-level checkpointing 段落直接列出路徑及其取捨
boundary: AWS 文章包含示意算例與 AWS 服務選項，不是跨 operator 實測基準；架構建議不證明特定 NVMe、控制器、檔案系統或雲端服務已被某客戶採用
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: NVIDIA ModelExpress 把模型權重來源分成 remote object storage、local storage 與已在服務的 peer GPU，資料路徑依可用能力優先選 P2P RDMA，再退到 ModelStreamer、GPUDirect Storage 或 host-staged loader；因此權重分發的第一個節點與後續擴容節點不必走同一路徑
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-08-09
basis: S3 的 overview、bootstrap、peer transfer 與 runtime path selection 段落直接列出來源、優先序與 fallback
boundary: 這是 NVIDIA ModelExpress 的軟硬體能力與單一測試環境，不代表所有 inference stack 採用，也不證明 P2P RDMA、GDS 或 local SSD 各自的量產設備需求
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C4
label: verified
status: active
claim: 群聯 2026Q1 法說把企業級 SSD、aiDAPTIV、AI PC、AI 網通、AI 伺服器與 Boot Drive 一起納入 AI Ecosystem 模組，並揭露該廣義組合占當季營收 38%；同一頁面沒有把其中企業級 SSD、訓練資料面、checkpoint 或模型分發收入各自拆開
supporting_source_ids: S4
contrary_source_ids:
as_of: 2026-08-09
basis: S4 第 21、23–24 頁的產品與 AI Ecosystem 圖表直接支持範圍與 38% 數字，且未提供三條 I/O 契約的個別收入分母
boundary: 38% 是公司自定義的跨產品組合，不能當成資料中心 SSD、AI server、Meta／AWS／NVIDIA 曝險或高毛利產品占比
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C5
label: inference
status: active
claim: 訓練資料讀取、checkpoint 持久化與模型權重分發應被視為三條可分別驗收的 AI 儲存 I/O 契約，而不是用單一容量或峰值吞吐指標替代；三者的壓力來源分別偏向尾端延遲與同步 stall、寫入／復原與故障域取捨、以及資料副本位置與 transport path 選擇
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-08-09
basis: S1 直接建立 dataset fetch 的 pMax 與 GPU stall；S2 建立 checkpoint write／read、durability 與 recovery；S3 建立 model artifact source／transport path。三條獨立 operator／平台鏈的 failure condition 不同，支持分開驗收的研究框架
boundary: 這是跨來源的機制分類，不主張三家架構完全可比、不估計市場規模，也不預設每條契約都需要新增 SSD、NAND、controller、NIC、switch 或 storage node
verification_needed: 同一 production 平台公開三條資料流的 SLO、failure domain、設備配置與驗收結果，可檢查分類是否遺漏或重疊
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: inference
status: active
claim: 8299 群聯因具備 NAND 控制器、韌體、企業級 SSD 與儲存系統能力，是 memory 族群查核三條 I/O 契約的第一個公司端入口，但現有公司揭露只能確認產品與廣義應用位置，不能確認其產品已進入 S1、S2 或 S3 所述架構
supporting_source_ids: S1,S2,S3,S4
contrary_source_ids:
as_of: 2026-08-09
basis: S1–S3 定義待查核的 operator 路徑，S4 定義群聯產品與廣義 AI 應用；兩側存在功能鄰接，但沒有客戶、part number、qualification 或 production deployment 的雙向核對
boundary: 「第一個查核入口」只是研究路由，不是受惠、design win、份額、訂單、收入或毛利判斷
verification_needed: 平台與群聯雙向文件把具名 Pascari／控制器連到 dataset、checkpoint 或 model distribution 路徑，並揭露 qualification、部署與財務分母
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: unverified
status: active
claim: 8299 群聯或任何 universe 伺服器 ODM 已取得與三條 AI 儲存 I/O 契約直接相關的 production qualification、訂單、出貨或可辨識毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-09
basis: 現有來源沒有把 operator 架構接到 universe 公司的具名 part、客戶、量產配置、出貨分母或損益
boundary: 不得把廣義 AI Ecosystem 占比、企業級 SSD 產品頁、一般 AI server 出貨或架構相鄰關係改寫成此主張已成立
verification_needed: 買方 BOM／qualification 與公司季報／法說雙向確認具名產品、路徑角色、production 數量、收入與毛利
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: unverified
status: active
claim: 三條資料流會形成與 AI compute 成長同方向、可加總的 SSD／controller／NIC／switch／storage-node 增量需求，而不是被快取、預取、peer transfer、軟體編排或既有儲存容量部分吸收
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-09
basis: S1 與 S3 都明示快取、預取及 peer path 可避免重複外部讀取，S2 也以 hierarchical／multi-level 路徑降低外部儲存負荷；現有來源沒有共同部署分母可重算硬體增量
boundary: 現有來源是證據缺口而非「硬體不成長」的反證；在共同平台分母出現前，三條流量不可相加成 TAM 或個股營收
verification_needed: 同一 production cluster 的流量、cache hit、checkpoint frequency、model rollout、設備數量與前後期 BOM／利用率
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 三條路徑，三種失敗方式

**資料集讀取**是連續餵料問題。Meta 的例子把焦點放在 pMax：同步訓練中最慢的 fetch
會拖住整個 step（C1）。解法不只加快 flash，還包含 metadata flattening、區域化、cache、
prefetch、hedged reads 與 concurrency control，所以單看 SSD sequential throughput 會漏掉真正的
瓶頸。

**訓練存檔（checkpoint）**是可靠度契約。它要回答多久存一次、停算多久、壞掉時丟多少進度、哪一層
能承受節點或區域故障。AWS 把同步／非同步、hierarchical distribution 及 fast／durable tier
分開（C2），表示 local NVMe 很快不等於具備 durable recovery，durable object storage 也不等於
適合每幾分鐘的 fast checkpoint。

**模型權重分發**是副本位置與資料傳輸路徑問題。第一個 worker 可能從 object 或 local storage
啟動，後續 worker 則可能直接從已上線的 peer GPU 取得權重（C3）。這條路徑甚至會主動避開
local disk，因此「模型越大，所有節點就等比例多讀一次 SSD」並不是可直接接受的假設。

三條路徑合起來支持 C5 的分類，但同時也形成最重要的反證：cache、prefetch、hierarchical
distribution 與 P2P 本來就是為了減少重複 I/O。只有量到共同平台的命中率、流量、設備與
qualification，才能判定硬體價值落在哪裡。

## 實際研究時，先問契約再問硬體

第一步是把工作負載寫成可失敗的句子。資料集路徑要問「最慢一次讀取拖住多少 GPU、允許的
pMax 是多少」；checkpoint 要問「多久寫一次、每次能停算多久、故障後最多丟失多少進度」；
權重分發則要問「第一個副本從哪裡來、後續節點能否從 peer 取得、cold start 的目標是多少」。
若文件只說容量、峰值頻寬或模型參數量，還沒有回答任何一條完整契約。

第二步才是把契約拆回元件責任。尾端延遲可能同時受 metadata lookup、cache miss、網路壅塞、
storage-node queue 與媒體讀取影響；checkpoint 的 fast tier 也不等於 durable tier，兩者可能由
不同設備承擔。模型分發更可能依副本位置在 object、local 與 peer path 間切換。這表示同一個
SSD benchmark 不能替整條鏈背書，也不能只憑一段 RDMA 或 GPUDirect 示意圖，把價值全部分給
NIC、switch 或 local NVMe。

第三步是要求部署分母。研究至少要知道 cluster 規模、每個節點的本地容量、cache hit、
checkpoint 頻率、模型 rollout 次數與故障域，才可能重算設備增量。若優化後外部讀取下降，
總訓練量增加也未必讓每種硬體等比例增加；反過來，若 recovery SLO 收緊，持久層可能在流量
不變時仍需要更多副本或更高耐久度。沒有前後期分母，就只保留方向問題，不產生 TAM。

最後才核對公司。平台文件要出現具名 device、controller 或 storage node，供應商文件也要能
反向確認客戶資格、量產配置與財務口徑。只有單邊產品頁時，最多畫到能力；只有廣義 AI
Ecosystem 占比時，不能把它拆成資料集、checkpoint 或模型分發營收。這套順序使 8299 的研究
橋有清楚下一步，也保留「軟體吸收大部分需求」與「硬體增量落在別層」兩個可證偽方向。

## 這篇對個股判斷的用處與界線

群聯是這篇刻意新增的 company bridge。它不是因為「做 SSD 所以受惠」，而是因為已獨立核驗
的公司筆記能確認其控制器、韌體、企業級 SSD 與系統整合能力，法說又提供廣義 AI Ecosystem
起點（C4、C6）。這使 memory 族群不再只有抽象的 NAND 路由，而有一個具名公司待查核。

但這條橋目前只到能力層。38% 的分子含多種產品，沒有 Meta、AWS、NVIDIA 客戶對應，也沒有
dataset、checkpoint 或 model distribution 的收入拆分。伺服器 ODM 同樣只保留族群路由：
整合 storage node 的可能性不等於已承擔三條契約或取得增量訂單。C7 與 C8 未被證實前，本文
不支持個股排序、營收預測或投資動作。

## 來源

<!-- research_source
source_id: S1
role: other_primary
source_kind: document
publisher: Meta Engineering
independence_group: meta-operator
title: Meta's AI Storage Blueprint at Scale
published_at: 2026-07-01
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://engineering.fb.com/2026/07/01/data-infrastructure/metas-ai-storage-blueprint-at-scale/
locator: 第 15–57 段的 workload characteristics、Why Latency Matters、regional flash／cache／protocol optimizations，以及第 60–92 段的 ingestion、tiered cache 與 future work
limitation: 單一 operator 自述自身 production 架構；不提供外部可重現原始資料、設備 BOM、供應商、採購量或財務映射
-->

<!-- research_source
source_id: S2
role: competitor_primary
source_kind: document
publisher: Amazon Web Services
independence_group: aws-cloud
title: Architecting scalable checkpoint storage for large-scale ML training on AWS
published_at: 2025-06-16
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://aws.amazon.com/blogs/storage/architecting-scalable-checkpoint-storage-for-large-scale-ml-training-on-aws/
locator: Storage infrastructure、Checkpoint fundamentals、hierarchical checkpoint distribution、Asynchronous checkpointing 與 Multi-level checkpointing 段落
limitation: AWS 技術文章含服務選項與示意算例；不是跨 operator 實測、採購文件或特定儲存產品 qualification
-->

<!-- research_source
source_id: S3
role: competitor_primary
source_kind: document
publisher: NVIDIA
independence_group: nvidia-platform
title: ModelExpress: Distributing Model Artifacts at the Speed of Light
published_at: 2026-07-24
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://developer.nvidia.com/blog/modelexpress-distributing-model-artifacts-at-the-speed-of-light/
locator: ModelExpress overview、Starting the first worker、Starting every worker after the first、runtime path selection 與 end-to-end results
limitation: NVIDIA 自身軟體與單一測試環境；產品效能結果不代表第三方 production 採用、硬體需求量或台灣供應商映射
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: document
publisher: Phison Electronics
independence_group: phison-issuer
title: 群聯電子 2026Q1 法說會簡報
published_at: 2026-05-08
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://www.phison.com/wp-content/uploads/2026/06/1Q26_Phison-Earnings-Call_CN_Official_uploaded-version.pdf
locator: PDF 實體第 21、23–24 頁的 AI Ecosystem 38%、企業級 SSD、Boot Drive、aiDAPTIV、AI 軟體與產品地圖
limitation: 公司自定義的廣義組合，沒有拆分三條 I/O 契約、客戶 qualification、production deployment、訂單或毛利
-->

<!-- research_source
source_id: S5
role: other_primary
source_kind: living_index
publisher: Meta Engineering
independence_group: meta-operator
title: Meta Engineering Data Infrastructure 持續更新索引
published_at:
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://engineering.fb.com/category/data-infrastructure/
locator: 2026-08-09 觀察到 Data Infrastructure 類別可供後續重查 AI storage、training reliability 與 production architecture 新文
limitation: 動態索引只供後續監測，不替代文章附件、原始數據、BOM 或供應商文件
-->

<!-- research_source
source_id: S6
role: competitor_primary
source_kind: living_index
publisher: Amazon Web Services
independence_group: aws-cloud
title: AWS Storage Blog 持續更新索引
published_at:
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://aws.amazon.com/blogs/storage/
locator: 2026-08-09 觀察到 storage technical posts 索引，供後續重查 checkpoint、FSx、S3 與 AI data path
limitation: 動態部落格索引不代表客戶採用或特定產品 qualification
-->

<!-- research_source
source_id: S7
role: competitor_primary
source_kind: living_index
publisher: NVIDIA
independence_group: nvidia-platform
title: NVIDIA Technical Blog 持續更新索引
published_at:
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://developer.nvidia.com/blog/
locator: 2026-08-09 觀察到 NVIDIA Technical Blog 索引，供後續重查 NIXL、GDS、RDMA、checkpoint 與 ModelExpress 更新
limitation: 動態索引與 vendor 技術文章不證明第三方 production 部署或台灣公司收入
-->

<!-- research_source
source_id: S8
role: company_release
source_kind: living_index
publisher: Phison Electronics
independence_group: phison-issuer
title: 群聯投資人會議資料持續更新索引
published_at:
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://www.phison.com/en/investor-relations/shareholder-services/investor-meeting-information
locator: 2026-08-09 顯示 2026Q1 meeting date、press release、presentation 與 audio replay 入口，供 Q2 後續重查
limitation: 索引只證明附件可定位；未發布新附件前不能刷新公司主張，也不能替代財報與客戶 qualification
-->

## 族群影響

<!-- impact
group_id: memory
stock_ids: 8299
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-28
rationale: 8299 的已核驗筆記確認 NAND controller、firmware、enterprise SSD 與系統整合能力，公司法說也提供廣義 AI Ecosystem 起點，因此是三條 I/O 契約在 memory 族群的第一個具名查核位置
evidence_boundary: 產品與 38% 廣義組合都沒有接到 operator 客戶、具名 path、qualification、production deployment 或可辨識損益；只建立能力橋，不建立受惠或排行
-->

<!-- impact
group_id: serverodm
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: storage node、local NVMe、NIC／switch 與 GPU transport 的整合責任可能落在系統商，是查核三條 I/O 契約是否進入共同 BOM 與驗收的路由
evidence_boundary: 沒有 universe ODM 具名揭露本篇三條資料流、平台 qualification、設備分母、出貨或毛利；一般 AI server 組裝能力不構成證據
-->

## 監測器

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C5,C8
metric: 三條 I/O 契約是否出現可對齊的 production SLO、failure domain、cache／prefetch 命中、checkpoint 頻率、model rollout 與設備利用率
source_ids: S1,S2,S3
watch_source_ids: S5,S6,S7
frequency: monthly
next_check: 2026-08-31
trigger: 至少一個 operator 公布同一 cluster 的 pMax、checkpoint window、artifact distribution、硬體配置與前後期利用率，足以量化哪一層承擔瓶頸
invalidation: 新資料顯示三種流量可由同一共通 SLO 完整描述，或快取／peer path 長期吸收大部分外部 I/O，則 C5 分類與 C8 硬體增量假設都必須重寫
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C4,C6,C7
metric: 8299 是否把企業級 SSD／AI Storage 從廣義 AI Ecosystem 中拆出具名產品、客戶認證、production 出貨、收入與毛利
source_ids: S4
watch_source_ids: S8
frequency: quarterly
frequency_detail: 2026Q2 財報與法說後複核
next_check: 2026-08-28
trigger: 群聯或買方文件把具名 Pascari／controller 接到 dataset fetch、checkpoint 或 model distribution，並同時揭露 qualification、部署分母及可辨識財務貢獻
invalidation: 後續仍只揭露廣義 AI Ecosystem 百分比、產品清單或合作展示，則 C6 維持研究路由、C7 維持待驗證，不得升格公司受惠
-->

## 目前不能下的結論／待驗證

- 不能把 Meta、AWS、NVIDIA 三家的文件拼成一套共同 production architecture；本篇只抽取三種可分別反證的 I/O 契約。
- 不能把容量、峰值吞吐或模型尺寸直接換算成 SSD 顆數；cache、prefetch、hierarchical distribution 與 P2P 都會改變外部 I/O。
- 不能把群聯 AI Ecosystem 38% 當成企業級 SSD、AI server 或本篇三條資料流的收入；分子混合多個產品與終端。
- 不能由群聯具備控制器、韌體與企業 SSD 能力推導 Meta／AWS／NVIDIA design win、訂單、份額或毛利。
- 不能把伺服器 ODM 的一般整合能力當成 storage data plane qualification；需要同一平台的 BOM、SLO、驗收與出貨雙向文件。
