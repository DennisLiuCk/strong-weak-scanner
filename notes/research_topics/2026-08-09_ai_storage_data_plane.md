# AI 儲存不是容量越大越好：先分清餵資料、保存進度與搬模型

<!-- research_topic
topic_id: MI-2026-08-09-AI-STORAGE-DATA-PLANE
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-09
source_published_at: 2026-07-01
last_reviewed_at: 2026-08-12
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
confidence_basis: Meta、AWS 與 NVIDIA 三條獨立一手鏈分別公開訓練資料讀取、checkpoint 與模型權重分發的路徑及失效代價；MLCommons、PyTorch 與 Google Cloud 又把 I/O 模擬、暫存／上傳完成、故障復原及訓練有效時間分成不同證據層，足以支持三種 I/O 契約與 checkpoint 復原護照必須分開驗證；8299 群聯只由公司法說與已獨立核驗筆記確認企業級 SSD 與廣義 AI Ecosystem 能力，尚無任何文件把其產品接到上述 operator 架構、production qualification 或可辨識損益
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
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave96_ai_storage_three_jobs_five_positions_and_six_gate_ladder
evidence: editorial:reader_layer_only_no_claim_source_monitor_or_impact_change
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: expanded_checkpoint_completion_recovery_and_training_goodput_measurement_contract
evidence: sources:S9,S10,S11,S12,S13
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **訓練資料**：用來讓模型學習的文字、圖片、聲音或其他樣本；訓練期間必須持續送到運算晶片。
- **餵資料（Dataset fetch）**：在每一步運算前，把下一批訓練資料讀出並送到運算晶片；任何一台機器讀得太慢，都可能讓整群一起等待。
- **保存進度（Checkpoint）**：定期把模型狀態與訓練進度存下來，故障後才能從最近一次紀錄接著跑，而不是全部重來。
- **暫存完成（Staging completion）**：非同步存檔先把當下狀態複製到 CPU 記憶體等暫存位置；這只表示訓練中的權重可以繼續變動，不表示遠端寫入或耐久保存已完成。
- **上傳完成（Upload completion）**：checkpoint 已完成寫入指定儲存位置；它比暫存完成更接近「存好了」，仍要另做回載、正確性與故障範圍驗證。
- **回載驗證（Restore validation）**：實際讀回 checkpoint、重建模型與 optimizer 狀態並接續訓練，檢查步數、資料與結果是否符合預期。
- **訓練有效時間（Runtime Goodput）**：在訓練資源可用的時間內，真正用於向前完成有效訓練進度的比例；存檔、故障後重跑與恢復等待都會吃掉它。
- **故障注入**：在可控測試中刻意中斷節點、機架或儲存路徑，確認 checkpoint 能否在預定故障範圍內被找回，而不是等真實事故才知道。
- **基準組／處理組（Baseline／treatment）**：基準組維持原本存檔路徑，處理組只改同步／非同步、儲存層或其他一項因素；若模型、機器與存檔頻率一起變，就無法判斷改善來自哪裡。
- **模型檔案**：已訓練模型的參數與執行所需資料；服務上線、更新或擴充機器時要先把它送到工作節點。
- **模型分發**：把模型檔案從遠端、本機或已經上線的另一台機器送到新節點的過程。
- **運算晶片（GPU）**：大量平行處理人工智慧運算的晶片；本文關心它是否因等資料而閒置，不把 GPU 數量直接當成儲存需求。
- **張量處理器（TPU）**：Google 為機器學習工作設計的加速器；本文只用 Google 公開的單一 TPU 案例說明量測邊界，不把結果外推到 GPU 或其他平台。
- **TPU v5p**：Google 第五代 TPU 家族中面向大規模訓練的型號名稱；型號只標示該案例的受測平台，不代表同樣結果會出現在其他世代。
- **機器學習（ML）**：讓系統從資料中建立模型的方法總稱；本文的 ML Goodput 專指訓練有效時間，不是模型品質分數。
- **隨機存取記憶體（RAM）**：節點工作期間可快速讀寫、但通常不具斷電持久性的記憶體；可當 checkpoint 快速層，仍需要其他層承擔預定故障範圍。
- **同步訓練**：多顆運算晶片完成同一步後才一起進到下一步；其中一顆落後，其他晶片也可能停下來等。
- **最慢讀取時間（pMax／尾端延遲）**：一批讀取中最慢端所花的時間；平均速度良好，不代表最慢一次不會拖住整體工作。
- **讀取／寫入速度**：資料在指定時間內能讀出或寫入多少；峰值速度只描述一項能力，不能替最慢延遲、故障復原與持久性背書。
- **本地儲存**：放在單一伺服器或附近機櫃內的 SSD；距離近、讀取快，但容量、共享與故障保護有不同限制。
- **共享儲存**：讓多台機器共同存取的儲存系統；方便分享資料，卻也可能受網路與共同佇列影響。
- **物件儲存**：以物件方式保存大量資料與模型檔案的遠端儲存；適合持久保存，不代表每一步訓練都直接從這裡讀取。
- **快取**：把近期可能再用的資料暫存在更靠近運算的位置，減少重複向遠端讀取。
- **預先讀取**：在運算真正需要前先把下一批資料準備好，用等待時間換取較少的停算。
- **附近節點互傳（P2P）**：讓已持有模型的機器直接傳給另一台機器，可能避開再次讀取遠端或本地儲存。
- **副本**：同一份資料或模型檔案的另一份複製品；副本放在哪裡會改變讀取路徑、速度與設備需求。
- **冷啟動**：新服務節點尚未載入模型時，從開始準備到能接受請求的等待時間。
- **擴容**：增加新的工作節點來承接更多服務需求；新增節點不一定都從同一個儲存位置載入模型。
- **AWS**：Amazon Web Services；本文只引用它對訓練進度保存的架構說明，不把單一雲端做法當成跨平台實測。
- **故障範圍**：一次故障會影響單一硬碟、單台機器、整個機架或更大區域；保存進度的位置要能承受預定的故障範圍。
- **復原點**：故障後可以回到的最近一次有效進度；存檔越少，故障後可能重跑越多工作。
- **持久性**：資料在設備或區域故障後仍能被找回的能力；寫得快與保存得久不一定由同一層負責。
- **服務目標（SLO）**：系統預先約定要守住的結果，例如最慢讀取、存檔完成或冷啟動時間。
- **儲存直達運算晶片（GPUDirect Storage）**：讓儲存資料少經一層主機記憶體搬運，較直接送到 GPU 的路徑；有這項能力不等於已取得客戶訂單。
- **遠端記憶體直通（RDMA）**：讓不同機器更直接交換記憶體資料、減少處理器中轉的傳輸方式；它是搬運路徑，不是供應商認證。
- **網路介面卡（NIC）**：把伺服器接上網路並搬運資料的元件；出現在架構圖中，不代表具名料號已被採用。
- **快閃記憶體（NAND）**：SSD 用來長期保存資料的非揮發性媒體；媒體容量只是整條資料路徑的一部分。
- **NVMe**：主機存取非揮發儲存的協定家族；支援 NVMe 不代表最慢延遲、耐用度與系統認證都已達標。
- **儲存控制器**：管理資料如何寫入、讀出、校錯與分配到快閃記憶體的晶片與韌體組合。
- **客戶資格認證（Qualification）**：客戶依功能、效能、可靠度與製造條件確認產品是否可採用；產品存在不等於已通過認證。
- **部署分母**：用來判斷需求規模的共同基準，例如機器數、每台容量、路徑使用比例、存檔頻率與設備利用率。
- **廣義 AI 產品組合（AI Ecosystem）**：公司把企業 SSD、AI PC、網路、伺服器與其他產品合併計算的分類；不能直接當成資料中心儲存收入。

### 三句話抓重點

- 人工智慧系統有三種容易混在一起的工作：訓練時持續餵訓練資料、故障前先保存進度，以及服務擴充時把模型檔案送到新機器；三種工作卡住的原因不同。
- 餵資料怕最慢的一次讀取讓整群運算晶片等待；保存進度要依序證明暫存、上傳、耐久保存、正確回載與故障後接續訓練，不能只報寫入速度；搬模型則取決於副本放在哪裡，以及能否從附近機器直接取得。
- 所以「資料變多」不能直接換算成更多硬碟或某家公司營收；還要看到哪條路徑被實際使用、哪個元件真的承擔瓶頸，以及客戶認證、部署數量與財務資料。

### 為什麼重要

**三種工作像三種物流。** 餵資料像產線不能斷料，保存進度像定期留下可復原的保險紀錄，
搬模型則像新店開張前先把完整貨品送到現場。三者都會讀寫資料，卻不能只用一個容量或速度
數字判斷好壞。

**資料放在哪裡，也會改變硬體需求。** 常用資料可能先被放進快取，第一台機器可能從遠端
載入模型，後續機器也可能直接向附近節點取得副本。軟體若減少重複搬運，運算量成長就不會
自動讓每一層儲存設備等比例增加。

**最後才把平台需求接回公司。** 研究要先知道哪一種工作卡住、資料實際走哪條路、瓶頸落在
軟體、儲存、網路或系統整合，再核對具名產品、客戶認證、部署數量與財務貢獻。只有平台架構
或供應商產品清單，都還不足以證明訂單。

### 接下來怎麼追

- 先辨識新資料談的是餵訓練資料、保存進度或搬模型，並記下最慢讀取、存檔完成、故障復原或新機器啟動時間。
- 若資料談 checkpoint，先問「完成」是暫存完成、上傳完成、耐久副本完成，還是已實際回載並接續訓練；四者不能互換。
- 再查同一平台的快取命中、路徑使用比例、機器數、每台容量與設備利用率，避免把三家不同架構直接相加。
- 最後核對客戶端的具名產品與供應商端的認證、部署、出貨、收入及毛利；兩邊沒有對上，就維持待驗證。

### 想一想

- 如果軟體已讓附近機器吸收大部分重複搬運，運算量增加時，長期保存設備還會等比例增加嗎？
- 一顆硬碟的峰值速度很快，但最慢讀取、故障復原與連續運作都沒有通過驗收，它真正解決了哪一種工作？
- 一個非同步存檔在暫存完成後就讓訓練繼續，但上傳途中節點立刻故障，這份進度紀錄算完成了嗎？
- 公司公布的人工智慧產品占比同時包含硬碟、個人電腦、網路與伺服器時，能用這個百分比判斷資料中心儲存收入嗎？

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
supporting_source_ids: S1,S2,S3,S11,S12,S13
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

<!-- research_claim
claim_id: C9
label: verified
status: active
claim: MLCommons 在 2026-08-12 擷取的 MLPerf Storage v3.0 repository 中，把 training 與 checkpointing 列為不同工作負載；checkpointing 只模擬 Llama 3 四種模型尺度的寫入／讀取，並要求申報 file／object backend、system description、run configuration 與 submission validation；同頁也明示工具使用 CPU-only PyTorch、實際不使用 GPU，因此這套結果是儲存 I/O 模擬與可重現組態證據，不是實際訓練有效時間、回載正確性或故障復原證據
supporting_source_ids: S9
contrary_source_ids:
as_of: 2026-08-12
basis: S9 的 Workload Categories、Storage Backend Selection、submission layout／validation、history／lockfile 與 prerequisite 說明，直接列出 training／checkpointing 分流、四種 Llama 3 尺度、file／object backend、system description、組態重跑及 CPU-only 執行邊界
boundary: S9 是當日擷取的持續更新標準 repository，不是不可變更的已發布結果集；benchmark 模擬 I/O 且不用 GPU，不能代替 production 模型、真正 accelerator stall、checkpoint 內容正確性、故障域、客戶部署或供應商財務
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: PyTorch Distributed Checkpoint 現行文件把 async save 的 staging completion 與 upload completion 分成兩個 future：前者只代表 local state copy 完成，後者才代表 checkpoint saving 完成；async save 預設先把 state_dict 搬到 CPU staging storage 再由另一執行緒保存，官方教學並提醒 CPU 記憶體需求約隨每 rank checkpoint 大小乘上 rank 數增加，且一般應限制同時只有一個非同步 checkpoint
supporting_source_ids: S10,S11
contrary_source_ids:
as_of: 2026-08-12
basis: S10 的 AsyncSaveResponse、save／async_save／load API 逐項區分 staging 與 upload completion、CPU staging、distributed save 與 load；S11 的 Asynchronous Checkpointing Overview 直接列出 CPU buffer 記憶體需求及 concurrent checkpoint 管理建議
boundary: 這些是框架 API 與教學的功能及資源契約，不證明任何 storage backend 已達耐久性、checkpoint 能承受指定故障域、回載後模型正確，或非同步方案在 production 的淨有效時間與成本必然更好；S10 是持續更新 main 文件，且明示 saved state_dict 跨 PyTorch 版本沒有向後相容保證
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: verified
status: active
claim: Google Cloud 將 Runtime Goodput 定義為訓練資源可用期間真正向前完成有效訓練進度的時間比例，並把 failure 前距最近 checkpoint 的時間與恢復訓練時間列為主要損失項；其多層 checkpoint 文章另公開 node RAM、不同 slice／superblock 副本與 Cloud Storage 三層路徑，且在唯一具名的 35K-chip TPU v5p 工作負載組態報告 ML Goodput 增加 6.59%，但未揭露重複執行數、變異、原始樣本或信賴區間，因此無法計算 SE／t，也不能當成跨平台平均效果
supporting_source_ids: S12,S13
contrary_source_ids:
as_of: 2026-08-12
basis: S13 的 Runtime Goodput 定義與分析模型直接列出 useful progress、time since last checkpoint 與 resume time；S12 直接列出三層架構及 35K-chip TPU v5p 的 6.59% vendor-reported result。公開資料只辨識出一個具名工作負載組態，獨立 run 數與不確定度均未提供
boundary: 這是 Google Cloud 自述的單一具名組態與產品架構，沒有可重算原始資料、run-level 分布、對照組完整版本、獨立複現、設備 BOM 或台灣供應商映射；不得拿 6.59% 估計其他 GPU／TPU、模型、故障率、雲端或儲存層的效果
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: inference
status: active
claim: 要宣稱 checkpoint 系統改善大規模訓練，至少要把受測系統與版本、checkpoint 內容／大小／頻率、基準組與只改一項的處理組、暫存／上傳／耐久／可回載的完成語意、各層資料路徑與故障範圍、故障注入後的正確回載、停算／最多重跑進度／恢復時間／Runtime Goodput，以及 CPU 記憶體／網路／容量／功耗／成本綁成同一份八格復原護照
supporting_source_ids: S9,S10,S11,S12,S13
contrary_source_ids:
as_of: 2026-08-12
basis: S9 提供版本化 workload、backend、system description、validation 與容量／功耗正規化框架；S10／S11 分開 state、stage、upload、load 與 CPU buffer／concurrency；S12 提供跨故障範圍的多層路徑；S13 把 checkpoint 之後損失進度與恢復時間接到 useful training progress，共同支持八格欄位不能互相替代
boundary: 這是由不同官方文件整合出的研究方法，不是 MLCommons、PyTorch 或 Google 共同發布的標準，也不是已完成的 production benchmark；欄位齊全仍不保證適用所有模型、隔離單一元件因果、改善 TCO，或形成任何台灣公司訂單與收入
verification_needed: 具名 operator 用版本化 production workload 對同一受測系統公開 baseline／treatment、重複 run、分布、不確定度、故障注入、回載正確性、Runtime Goodput、資源與成本，並保留原始結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C13
label: unverified
status: active
claim: 具名 production operator 已依同一八格復原護照，對版本化 checkpoint baseline／treatment 公開重複執行、結果分布、正確回載、故障域存活、Runtime Goodput、資源成本與具名設備配置，並把改善接到 universe 公司產品資格、部署及財務貢獻
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: S9–S13 分別提供 I/O 模擬、框架完成語意、資源限制、多層架構與單一 vendor-reported goodput 案例，沒有一條證據鏈同時交付完整八格、買方 BOM、供應商 qualification、production 分母與公司損益
boundary: 缺少公開證據不等於不存在私有部署或商業關係；不得用 benchmark submission、API 支援、單次 goodput、產品能力或未具名客戶敘述替代此主張
verification_needed: 買方公開可重建 checkpoint 實驗與 deployment evidence packet，供應商再以同一產品、客戶、期間確認 qualification、出貨、收入及毛利
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 先把三種「存資料」工作分開

| 本文三種工作 | 何時發生 | 最怕什麼 | 先看哪個結果 | 不能直接推成 |
|---|---|---|---|---|
| 1. 訓練時持續餵資料 | 每一步運算前，把下一批訓練資料送到所有運算晶片 | 最慢的一台讀取落後，讓其餘晶片一起停等 | 最慢讀取時間、等待的晶片數、快取命中與持續餵料速度 | 平均速度高，不等於整群晶片不會被最慢一次讀取拖住 |
| 2. 故障前保存進度 | 訓練途中定期寫下模型狀態，故障後再載回 | 存檔太慢造成停算，或存得不夠安全而無法復原 | 每次存檔時間、故障後最多重跑多久、能承受哪種故障 | 本地硬碟寫得快，不等於進度已能跨機器或跨區保存 |
| 3. 上線或擴充時搬模型 | 第一台服務機器啟動、增加新機器或更新模型時 | 模型檔案很大，第一份副本太遠，或每台機器都重複搬一次 | 第一台與後續機器的啟動時間、模型從遠端／本機／附近節點取得的比例 | 模型越大，不等於每台機器都會等比例多讀一次硬碟 |

三種工作要分開量：餵資料是「能不能持續供應」，保存進度是「壞掉後能不能接著跑」，搬模型
是「新機器多久能開始服務」。這是本文整理三份平台資料的閱讀框架，不表示三家公司採用同一
套架構，也不是跨平台速度排名。

## 「存檔完成」其實有六層，不是按下 save 就結束

MLPerf Storage 的 checkpoint workload 可以用固定模型尺度、backend、system description 與組態重跑
寫入／讀取 I/O，但官方 repository 同時明示它只用 CPU 模擬、實際不使用 GPU。[S9] 這能回答「受測
儲存能否承接宣告的 I/O 型態」，不能回答模型是否真的恢復、GPU 少等了多久，或一次機架故障後還剩
哪份副本。研究時可把「完成」拆成六層：

| 完成階梯 | 真正完成了什麼 | 最小證據 | 仍不能證明 |
|---|---|---|---|
| 1. I/O 模擬跑完 | 指定大小與讀寫型態在申報的 file／object backend 完成 | workload、版本、組態、system description 與驗證結果 | 真模型狀態正確、GPU 等待下降或故障後可恢復 |
| 2. 暫存完成 | 當下 state 已複製到 CPU 記憶體等 staging buffer，訓練中的權重可繼續變動 | staging completion timestamp、buffer 大小與錯誤 | checkpoint 已上傳、斷電後仍存在或其他節點可讀 |
| 3. 上傳完成 | framework 回報 checkpoint saving／upload 已完成 | upload completion、寫入目的地、所有 rank 結果與錯誤 | 副本跨過預定故障範圍，或版本升級後仍能載回 |
| 4. 耐久副本完成 | 至少一份副本落在能承受預定節點、機架或區域故障的位置 | tier、replica、failure-domain mapping 與可見性 | 內容可被正確讀回，或恢復速度符合訓練目標 |
| 5. 正確回載完成 | 模型、optimizer、步數與必要 metadata 已讀回並能接續訓練 | load、checksum／state 檢查、續跑步數與錯誤 | 整體有效訓練時間、成本與所有故障情境都改善 |
| 6. 訓練結果改善 | 在相同工作負載下，停算、重跑進度與恢復等待下降，Runtime Goodput 淨提高 | baseline／treatment、故障事件、lost steps、resume time 與 useful progress | 改善一定來自某顆 SSD，或已形成供應商訂單與毛利 |

PyTorch DCP 直接把 staging completion 與 upload completion 分成不同 future，且 async save 預設先複製
到 CPU staging storage 再由另一執行緒保存；官方教學提醒，這會占用約「每 rank checkpoint 大小 × rank
數」的 CPU buffer，並建議一般只讓一個非同步 checkpoint 同時進行。[S10][S11] 所以非同步不是把成本
消失，而是把訓練 barrier 改成記憶體、執行緒、網路與儲存佇列的另一組取捨。

## 用八格復原護照檢查 checkpoint 是否真的讓訓練更有效

只報 GB/s，最多填完上一節第一層。要把機制接到「故障後少重跑、運算晶片少空等」，至少先把下面
八格綁在同一個版本化 baseline／treatment；缺一格就把它留在 boundary，不用另一個漂亮數字代填：

| 八格復原護照 | 要先固定什麼 | 要保存什麼 | 少了最容易誤讀成 |
|---|---|---|---|
| 1. 受測系統與版本 | 模型、precision、GPU／TPU／CPU／RAM、SSD／共享儲存、NIC／switch、拓撲、framework、driver、filesystem／object client 與版本 | 可重建硬體、韌體、軟體、backend、system description 與設定檔 | 同時換了模型、機器或軟體，卻把差異全部算給儲存 |
| 2. Checkpoint 內容與節奏 | model／optimizer／scheduler／metadata 是否都存、每 rank 與總大小、sharding、步數、存檔頻率及保留數 | 每次 checkpoint ID、bytes、rank、開始步數、完成步數與保留政策 | 只存權重的快結果，和可完整續跑的 checkpoint 當成同一件事 |
| 3. 比較組與訓練負載 | baseline／treatment 一次只改同步／非同步、tier 或一項政策；固定 batch、sequence、cluster size、step time、arrival 與測試期間 | 相同工作負載、warm-up、事件時間線、重複 run、成功／失敗分母 | 處理組負載較輕或同時擴機，被寫成 checkpoint 本身改善 |
| 4. 完成語意與 barrier | 哪一刻算 staging、upload、durable replica 與可 restore；哪些 rank 必須一起完成 | 四種 timestamp、future／status、barrier duration、timeout、cancel、retry 與 partial checkpoint | 暫存完成被改寫成耐久完成，或最快 rank 掩蓋最慢 rank |
| 5. 資料路徑與故障範圍 | RAM、本地 SSD、跨 slice／rack 副本、shared file／object storage 的順序、同步／背景複製與 fallback | 每層 bytes、bandwidth、queue、replica age、failure-domain placement、error 與 fallback path | 有多層就等於每層都已完成，也把跨節點副本誤當跨區耐久 |
| 6. 故障與正確回載 | 注入節點、機架、網路或 storage tier 故障；固定何時故障、從哪一層 restore、如何驗證 state 與接續步數 | failure timestamp、last valid checkpoint、checksum／state diff、load／reshard、resume step、loss／divergence 與失敗原因 | 讀得到檔案就當成模型能正確續跑，或只測最容易的單機故障 |
| 7. 訓練使用者結果 | checkpoint barrier、故障前距最後有效存檔、lost steps、reschedule、restore／resume time 與 Runtime Goodput | event-level 與 run-level 分布、p50／p90／p99、平均、重複數、SE／t 或未能計算的原因 | 只看寫入峰值，掩蓋恢復慢、重跑多或尾端停算惡化 |
| 8. 資源、可靠度與經濟 | CPU RAM、網路、各 tier 容量與功耗、rack units、storage cost、寫入量／耐用度與營運人力 | baseline／treatment 的資源時數、bytes、power、capacity、失敗率、成本與使用壽命假設 | Goodput 小幅增加被直接換算成淨省錢，卻漏算記憶體、副本與寫入代價 |

這八格是研究中心整合官方文件後的檢查方法，不是三個組織共同發布的產業標準。MLCommons 提供
版本、backend、system description、驗證、重跑及容量／功耗描述；PyTorch 提供 state、stage、upload、
load 與資源語意；Google 則把 lost progress、resume time 與 useful training progress 接起來。[S9][S10]
[S11][S12][S13] 三者用途不同，合起來才能看出「I/O 更快」到「訓練更有效」中間還缺哪些證據。

Google Cloud 公開的多層案例把 checkpoint 放在 node RAM、另一個 slice／superblock 的副本與 Cloud
Storage，並在一個具名 35K-chip TPU v5p 工作負載組態報告 ML Goodput 增加 6.59%。[S12] 這是目前
可用的 operator 結果例子，但公開文章沒有給重複執行數、run-level 分布、變異、原始樣本或信賴區間，
因此無法計算 SE／t，也不能把單一 vendor-reported 組態當成跨平台效果。它填了部分路徑與結果格，
沒有填滿完整八格，更沒有把改善歸因到具名外部 SSD、控制器或台灣供應商。

## 再看資料可能經過的五個位置

| 本文五個位置 | 它負責什麼 | 常見資料去向 | 卡住時先查誰 | 不能直接推成 |
|---|---|---|---|---|
| 1. 軟體、索引與排程 | 決定下一批資料、模型副本與存檔何時從哪裡取得 | 預先讀取、快取選擇、重試與路徑切換 | 資料索引、排程、擁塞控制與軟體團隊 | 讀取變慢，不代表瓶頸一定在硬碟媒體 |
| 2. 近端記憶體與快取 | 暫存近期會再用的資料，避免反覆向遠端讀取 | 運算晶片附近的記憶體或分散式快取 | 命中率、容量、淘汰規則與資料新鮮度 | 快取需求增加，不能和長期儲存容量重複相加 |
| 3. 單機本地 SSD | 提供靠近工作節點的快速讀寫與短期副本 | 區域快閃、快速存檔或第一份模型副本 | SSD、控制器、韌體、耐用度與本機佇列 | 架構允許本地 SSD，不等於每條路徑或每台機器都會使用 |
| 4. 共享與長期儲存 | 保存原始資料、可復原進度與遠端模型檔案 | 共享檔案系統或物件儲存 | 儲存節點、共同佇列、網路與故障保護 | 遠端容量成長，不等於具名供應商已取得份額或訂單 |
| 5. 網路與系統整合 | 在儲存、伺服器與運算晶片之間搬資料並切換路徑 | 網路介面卡、交換器、儲存節點與整機 | 網路壅塞、資料路徑、機櫃配置與系統整合團隊 | 架構圖出現某類元件，不等於料號已通過客戶認證 |

同一份資料可能依當下位置走不同路徑：先從遠端取得，之後留在本機或快取，新增機器時再從
附近節點複製。因此軟體、記憶體、SSD、網路與伺服器整合是接力關係，不是固定由某一層獨占
價值；這張表也不是供應商名單或需求量估算。

## 最後用六關把平台需求接回公司

| 本文六關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 三種工作已分開 | 餵資料、保存進度與搬模型各有清楚的失敗條件 | 三份平台文件分別說明最慢讀取、存檔復原與模型副本路徑 | 第二個平台用可比較口徑重現同一種工作 | 三家公司文件不能拼成一套共同架構 |
| 2. 同一平台量到瓶頸 | 同一批機器有最慢讀取、存檔、啟動、命中率與故障範圍 | 各文件有個別機制與示例，沒有共同平台的完整分母 | 同一叢集公布三種工作的目標、流量、路徑比例與前後期利用率 | 個別峰值或示意算例不能換算整體設備增量 |
| 3. 瓶頸落到具名元件 | 能指出哪個 SSD、控制器、網路卡或儲存節點承擔限制 | 群聯只有控制器、韌體、企業 SSD 與廣義產品能力位置 | 平台公布具名料號、設備配置與失效分解 | 產品能力不能改寫成客戶採用 |
| 4. 客戶資格認證 | 具名產品依功能、效能、耐用與可靠度通過客戶測試 | 尚無買方與供應商雙向對上的認證文件 | 客戶測試結果、合格清單與供應商認證公告互相核對 | 展示、合作或產品頁不能改寫成認證完成 |
| 5. 正式部署與設備分母 | 已進入正式環境，並知道機器數、每台容量與路徑使用比例 | 尚無群聯或台灣伺服器廠對應本篇三種工作的部署資料 | 部署前後的設備數量、利用率、出貨與客戶上線紀錄 | 一次試用或小量出貨不能外推整體市場 |
| 6. 可辨識收入與毛利 | 同期間能把具名產品收入、成本與毛利接回公司總額 | 公司只公布混合多種產品的廣義 AI 組合占比 | 單獨產品收入、出貨量乘單價、成本與毛利分母 | 廣義產品占比不能當成資料中心儲存收入 |

本輪平台證據能把第一關說清楚，第二關仍是分散的個別案例；公司端最多到第三關的相鄰能力，
尚未通過第四到第六關。六關只用來定位缺少的證據，不是公司成熟度分數、訂單預測或投資排序。

## 這篇對個股判斷的用處與界線

群聯是目前可以查核的公司入口，原因是既有公司筆記已確認它具有控制器、韌體、企業級 SSD
與儲存系統能力；這只說明「可能負責哪些元件」，還沒有回答產品是否出現在本文三種工作中。

目前缺少的是買方與供應商雙向證據：平台端沒有公布群聯具名產品與客戶認證，群聯公布的 38%
又同時包含企業 SSD、個人電腦、網路、伺服器與其他產品，無法拆出餵資料、保存進度或搬模型
各自的收入。伺服器組裝廠也只保留「可能整合儲存節點」的研究入口，不能從一般整機能力推成
已取得部署或訂單。

因此個股研究的下一步不是估算受惠比例，而是依六關找出具名料號、客戶認證、正式部署分母、
出貨與財務貢獻。在這些資料出現前，本文不支持個股排序、營收預測或投資動作。

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

<!-- research_source
source_id: S9
role: standard
source_kind: living_index
publisher: MLCommons
independence_group: mlcommons-storage-standard
title: MLPerf Storage Benchmark Suite v3.0 repository
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://github.com/mlcommons/storage
locator: 2026-08-12 擷取的 Overview、submission layout／validation、Normalizing Factors、Prerequisite、Workload Categories、Storage Backend Selection、history／lockfile；頁面自述目前 package／spec 為 v3.0
limitation: 持續更新 repository，不是不可變更的正式結果快照；benchmark 以 CPU-only PyTorch 模擬 storage I/O、不使用 GPU，不能驗證實際訓練 stall、checkpoint state 正確性、failure-domain recovery、客戶部署或供應商財務
-->

<!-- research_source
source_id: S10
role: other_primary
source_kind: living_index
publisher: PyTorch
independence_group: pytorch-framework
title: Distributed Checkpoint — torch.distributed.checkpoint main documentation
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://docs.pytorch.org/docs/main/distributed.checkpoint.html
locator: 2026-08-12 擷取的 AsyncSaveResponse、save、async_save、load、FileSystemReader／Writer 與 distributed state_dict 說明
limitation: main branch 動態 API 文件，只界定 framework 行為與警告；不提供 storage durability、failure injection、restore correctness、production goodput、成本、客戶或硬體供應商證據，且明示 saved state_dict 跨 PyTorch 版本沒有向後相容保證
-->

<!-- research_source
source_id: S11
role: other_primary
source_kind: document
publisher: PyTorch
independence_group: pytorch-framework
title: Asynchronous Saving with Distributed Checkpoint (DCP)
published_at: 2026-02-03
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://docs.pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.html
locator: 頁面標示 Created 2024-07-22、Last Updated 2026-02-03；Asynchronous Checkpointing Overview 的 CPU buffer memory requirements、concurrent checkpoint management 與 async_save 範例
limitation: 官方教學說明 API 整合與資源限制，不是固定 storage backend 的 benchmark、production trace、故障域驗證、客戶部署或成本效益研究；頁面另標示 Last Verified 2024-11-05，需與現行 API 文件共同閱讀
-->

<!-- research_source
source_id: S12
role: competitor_primary
source_kind: document
publisher: Google Cloud
independence_group: google-cloud
title: Save early and often with multi-tier checkpointing to optimize large AI training jobs
published_at: 2025-06-16
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://cloud.google.com/blog/products/ai-machine-learning/using-multi-tier-checkpointing-for-large-ai-training-jobs
locator: 架構圖與本文第 82–98 行附近的 35K-chip TPU v5p、node RAM、different slice／superblock replica、Cloud Storage、lost progress 與 MTTR 敘述
limitation: Google Cloud 自述的產品架構與單一具名工作負載組態；6.59% 沒有公開重複執行數、run-level 分布、原始資料、變異或信賴區間，無法計算 SE／t，也沒有獨立複現、設備 BOM 或台灣供應商映射
-->

<!-- research_source
source_id: S13
role: competitor_primary
source_kind: document
publisher: Google Cloud
independence_group: google-cloud
title: Introducing ML Productivity Goodput: a metric to measure AI system efficiency
published_at: 2024-04-10
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://cloud.google.com/blog/products/ai-machine-learning/goodput-metric-as-measure-of-ml-productivity
locator: ML Productivity Goodput、Scheduling／Runtime／Program Goodput 定義，以及 Understanding Runtime Goodput 的 useful training steps、time since last checkpoint、reschedule 與 resume time
limitation: Google 自定義的量測與分析模型，不是跨平台標準或本篇多層 checkpoint 結果的原始資料；不能單憑指標定義歸因 storage、估計硬體需求或證明任何供應商採用與財務貢獻
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

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C9,C10,C11,C12,C13
metric: 同一 checkpoint 方案是否用版本化受測系統與 workload，同時公開 stage／upload／durable／restore、failure-domain injection、lost steps、resume time、Runtime Goodput、資源成本及結果不確定度
source_ids: S9,S10,S11,S12,S13
watch_source_ids: S9,S10,S11,S12,S13
frequency: monthly
frequency_detail: 每月檢查 MLPerf Storage、PyTorch DCP、Google checkpoint／Goodput 方法更新與具名 operator production recovery benchmark；重大規格、部署或客戶證據出現時提前重審
next_check: 2026-08-31
trigger: 具名 operator 以同一版本化 production workload 公開 checkpoint baseline／treatment、重複 run 與分布，並完成 fault injection、正確回載、Runtime Goodput、資源／成本及具名設備配置
invalidation: 新版標準、framework 或 production evidence 顯示八格仍遺漏會改變結論的 completion、consistency、failure-domain、convergence、security、endurance 或 economics 欄位；屆時新增修正 claim 縮窄 C12，不回寫既有研究快照
-->

## 目前不能下的結論／待驗證

- 不能把 Meta、AWS 與 NVIDIA 三家的文件拼成同一套正式運作架構；本篇只把三種工作分開比較。
- 不能把資料容量、峰值速度或模型大小直接換算成 SSD 顆數；快取、預先讀取與附近節點互傳都會減少重複讀取。
- 不能把群聯廣義 AI 產品組合的 38% 當成企業級 SSD、AI 伺服器或本文三種工作的收入；這個比例混合多種產品與終端。
- 不能由群聯具備控制器、韌體與企業 SSD 能力，推導它已進入 Meta、AWS 或 NVIDIA 的具名設計、訂單、份額或毛利。
- 不能把伺服器組裝廠的一般整合能力當成 AI 儲存路徑已通過客戶認證；仍需要同一平台的物料清單、服務目標、驗收、部署與出貨文件。
- 不能把 I/O 模擬跑完、暫存完成或上傳完成改寫成 checkpoint 已跨故障範圍耐久保存、正確回載並改善 Runtime Goodput；六層完成階梯要逐層留證據。
- 不能把 Google 單一 35K-chip TPU v5p 組態報告的 6.59% ML Goodput 改善外推成跨模型、跨平台或產業平均；公開資料沒有 run 數、變異、原始樣本或 SE／t。
