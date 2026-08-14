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
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_workload_concurrency_tail_latency_and_unit_performance_passport_without_thesis_or_clock_refresh
evidence: sources:S1,S9,S14,S15,S16,S17,S18,S19
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: separated_application_host_nand_and_rated_endurance_ledgers_without_thesis_or_clock_refresh
evidence: sources:S20,S21,S22,S23
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
- **最慢讀取時間（pMax／尾端延遲／latency）**：一批讀取中最慢端所花的時間；平均速度良好，不代表最慢一次不會拖住整體工作。
- **讀取／寫入速度（Throughput）**：資料在指定時間內能讀出或寫入多少；峰值速度只描述一項能力，不能替最慢延遲、故障復原與持久性背書。
- **SNIA／SSS PTS v2.0.2**：SNIA 是制定儲存技術方法的產業組織；SSS PTS v2.0.2 是本文用來辨識 device-level 測試範圍的現行標準入口，方法頁不等於任一產品已通過認證。
- **DWPD（Drive Writes per Day）**：在指定壽命內，每 24 小時可把 SSD 可用容量完整覆寫幾次的耐久度表達；它是壽命口徑，不是當日寫入效能上限。
- **TBW／PBW（Terabytes／Petabytes Written）**：指定壽命內的累計寫入量口徑；必須連同容量、壽命、測試條件與保固邊界閱讀，不能只拿數字大小跨產品排名。
- **主機寫入（Host writes）**：主機送到 SSD 的寫入 bytes；副本、檔案系統、壓縮、去重、metadata 與重試都可能讓它不同於應用程式眼中的邏輯資料量。
- **NAND 實際寫入（NAND writes）**：控制器最後寫進快閃記憶體媒體的 bytes；垃圾回收、資料搬移與媒體管理可能讓它高於主機寫入。
- **WAF（Write Amplification Factor）**：NAND 寫入除以主機寫入；兩個分子必須屬於同一裝置、時間窗與 workload，不能用產品型錄數字替代實測工作負載。
- **Overprovisioning（預留空間）**：不開放給使用者、留給控制器做媒體管理的容量；可用來改善壽命或效能，但可用容量減少不等於原始 NAND、成本或毛利已知。
- **Percentage Used／Available Spare**：NVMe 健康記錄中的耐久使用百分比與可用備援媒體指標；兩者要和 Data Units Written、溫度、媒體錯誤、非安全關機及產品保固共同判讀。
- **EOL（End of Life）**：規格定義的額定壽命邊界，不等於某一秒必然故障；反過來，尚未到 100% 也不能替其他健康欄位背書。
- **TLC（Triple-Level Cell）**：每個 NAND cell 儲存三個 bits 的快閃媒體類型；媒體標籤本身不能替代產品容量、耐久、韌體、工作負載與測試結果。
- **D7-PS1010／D7-PS1030**：Solidigm 同一 PCIe 5.0 產品家族的 standard-endurance 與 mid-endurance 型號；本文只用公開規格示範容量與壽命分母，沒有把它們當產業樣本。
- **OCP Datacenter NVMe SSD Specification v2.7**：Open Compute Project 的資料中心 NVMe SSD 規格；本文只引用耐久、健康與 EOL 條文，不表示任何型號已完成符合性或客戶資格認證。
- **Python Decimal／awk 雙路重算**：用十進位精確算術與另一套文字運算工具各算一次同一公式；兩路一致只排除單一路徑算術錯誤，不會把型錄轉成真實部署證據。
- **IOPS**：每秒完成多少次 I/O 操作；如果沒有同時寫出每次傳多少資料、讀寫比例與併行設定，就不知道每秒搬了多少 bytes，也不能和另一個 IOPS 數字直接排名。
- **Block size／small-I/O（傳輸大小／小筆 I/O）**：每一次 I/O 指令要求搬運的資料量；small-I/O 常讓操作次數成為重點，大 block 常讓資料吞吐成為重點。
- **KiB／GiB**：二進位資料單位，`1 KiB = 1024 bytes`、`1 GiB = 1024^3 bytes`；不能和十進位 `KB／GB` 靜默互換。
- **Queue depth（QD／QD1）**：一個工作執行緒允許同時尚未完成的 I/O 數；QD1 表示每個 thread 只允許一筆 outstanding I/O，QD 增加可能提高併行與 IOPS，也可能讓等待時間分布改變。
- **Outstanding I/O（OIO）**：主機已送出、仍在等待完成的 I/O；它描述目前有多少工作壓在資料路徑上，不是已完成的操作數。
- **Thread count（TC）**：同時發出 I/O 的工作執行緒／程序數；`TC × QD` 才接近測試施加的 total outstanding I/O。
- **Read／write mix**：測試中讀取與寫入的比例；快閃記憶體的背景整理與寫入歷史會讓不同 mix 的結果不可互換。
- **Random／sequential**：I/O 位址是隨機跳動或連續前進；同一顆裝置在兩種型態下可能呈現完全不同的 IOPS、吞吐與延遲。
- **Pre-conditioning（預處理）**：正式量測前先用指定寫入與工作負載把裝置帶到可比較狀態，避免只量到剛清空或剛開箱的短暫高點。
- **Steady state（穩態）**：在指定工作負載下，裝置效能已進入相對穩定的量測區間；它只對該工作負載與方法成立，不代表永遠不變。
- **Response-time distribution（回應時間分布）**：保留每次 I/O 完成時間的分布、百分位與最大值；平均延遲相同的兩組結果，最慢端仍可能差很多。
- **量測範圍（measurement scope）**：數字量的是單顆裝置、檔案系統、物件儲存、網路路徑，還是從訓練程式到資料完成使用的端到端時間；範圍不同不能直接相減。
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
- 所以「資料變多」不能直接換算成更多硬碟或某家公司營收；還要分開應用資料、主機送出的寫入、快閃媒體實際寫入與額定壽命，並看到實際路徑、客戶認證、部署數量與財務資料。

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
- 寫入型工作還要同時記錄每日邏輯 bytes、host bytes、NAND bytes、WAF、DWPD／TBW、可用容量、保固年限、Percentage Used 與備援媒體，不能用 GB/s 代替耐久度。
- 最後核對客戶端的具名產品與供應商端的認證、部署、出貨、收入及毛利；兩邊沒有對上，就維持待驗證。

### 想一想

- 如果軟體已讓附近機器吸收大部分重複搬運，運算量增加時，長期保存設備還會等比例增加嗎？
- 一顆硬碟的峰值速度很快，但最慢讀取、故障復原與連續運作都沒有通過驗收，它真正解決了哪一種工作？
- 一個非同步存檔在暫存完成後就讓訓練繼續，但上傳途中節點立刻故障，這份進度紀錄算完成了嗎？
- 同一份進度存檔若讓應用程式增加 1 TB 邏輯資料，主機與快閃媒體真的都只增加 1 TB 嗎；若沒有三層計數器，能判斷硬碟壽命嗎？
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

<!-- research_claim
claim_id: C14
label: verified
status: active
claim: SNIA 的現行標準入口列出 SSS PTS v2.0.2，而同站方法頁把 IOPS、Throughput 與 Latency 分成不同測試：IOPS 依 random block size 與 read／write mix 展開，Throughput 量 large-block sequential read／write，Latency 在 steady-state 與 total outstanding I/O=1 下保留 average 與 maximum；術語頁另把 queue depth 定義為每 thread 的 outstanding I/O，thread count 與 QD 必須分開保存
supporting_source_ids: S14,S15,S16,S17,S18,S19
contrary_source_ids:
as_of: 2026-08-14
basis: S14 直接列出現行 v2.0.2 與發布日；S15、S16、S18 的 Summary／Test Setup／Benefits 分別列 IOPS、LAT、TP 的 workload shape 與 steady-state 方法；S17 定義 QD／TC／OIO；S19 定義 KiB、random／sequential 與 steady state
boundary: S15–S19 是 SNIA 的 HTML 方法導讀，頁面沒有版本與發布日，可能保留較早 PTS 的版面或術語，不能替代 v2.0.2 完整 normative PDF；它們是 device-level 測試方法，不驗證 AI 叢集、資料正確性、耐久性、production qualification 或公司採用
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C15
label: inference
status: active
claim: AI 儲存效能數字只有在同時保存工作與量測範圍、系統與版本、I/O shape、單位、client／thread／queue 併行、裝置狀態與 cache、完成語意、延遲分布與事件數、量測視窗與重複執行，以及訓練使用者結果／資源／財務分母的十欄護照後，才適合做 baseline／treatment 比較
supporting_source_ids: S1,S9,S14,S15,S16,S17,S18,S19
contrary_source_ids:
as_of: 2026-08-14
basis: S15–S19 顯示 block size、R／W mix、random／sequential、pre-conditioning、steady state、QD／TC、average／maximum latency 與單位都會改變 device result；S1 顯示同步訓練關心 pMax 與 stall；S9 要求 workload、backend、system description、run configuration 與重跑，合併形成本文十欄可比性框架
boundary: 十欄護照是研究中心整合不同官方文件的檢查方法，不是 SNIA、Meta 或 MLCommons 共同標準；欄位齊全也不保證隔離單顆 SSD 因果、通過 durability／correctness／qualification，或形成任何台灣公司收入
verification_needed: 同一 production AI workload 公開端到端與 device-level pair、完整十欄、重複 run、失敗操作、延遲分布、goodput／restore 結果、資源成本與具名設備配置
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C16
label: inference
status: active
claim: 在每次成功操作都精確傳輸指定 payload 的純算術條件下，1,000,000 IOPS × 4 KiB／op 等於 3.814697265625 GiB／s（4.096 GB／s），而 100,000 IOPS × 128 KiB／op 等於 12.20703125 GiB／s（13.1072 GB／s）；後者 IOPS 只有十分之一，payload rate 卻是前者 3.2 倍
supporting_source_ids: S15,S18,S19
contrary_source_ids:
as_of: 2026-08-14
basis: S15 要求 IOPS 按 block size 展開，S18 把 throughput 與 large-block sequential workload 分開，S19 定義 KiB=1024 bytes；以 Python Fraction 與獨立 awk 路徑重算，兩路對 3.814697265625、12.20703125 與 3.2 倍完全一致
boundary: 這是 N=2 個假想 workload 的確定性單位展開，沒有裝置、run 或抽樣，也沒有 sampling SE／t；只有在每個計數操作都成功且 payload size 固定時才成立，未包含協定 overhead、壓縮、cache、failed／retried I/O、latency、durability、application goodput 或功耗
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C17
label: inference
status: active
claim: 高 queue depth／thread count 下的高 IOPS、QD=1 的 baseline latency 與 production AI 同步步驟的尾端延遲回答不同問題；要判斷餵資料是否少停算，必須在實際 client／thread／QD／OIO 下保存完整 response-time distribution、最慢端與 accelerator stall，而不能用 average latency 或單一 peak IOPS 代替
supporting_source_ids: S1,S15,S16,S17
contrary_source_ids:
as_of: 2026-08-14
basis: S17 把 QD、TC 與 outstanding I/O 分開；S16 明示 QD=1 latency 是無 queue benefit 的 baseline，且更多 outstanding I/O 時 maximum latency 可能不同；S15 顯示 IOPS 依工作負載與穩態而變；S1 則把 storage-fetch pMax 直接接到同步 GPU stall
boundary: 這是 device method 與單一 operator mechanism 的整合推論，不提供跨 SSD 的 tail-latency effect size，也不證明任何 production bottleneck 位於 SSD、控制器、網路或檔案系統，更不建立供應商採用與財務方向
verification_needed: 同一 AI cluster 固定 dataset、cache、network、client／thread／QD 與 device state，同時公開 per-I/O distribution、accelerator stall、failed／retried operations、run-level replication 與設備版本
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C18
label: verified
status: active
claim: KIOXIA 將 DWPD 定義為在指定壽命內每天可覆寫 SSD 可用容量的次數，將 TBW 定義為指定壽命內的累計寫入量，並給出 TBW＝DWPD×SSD 容量×年數×365 的換算；同一文件另將 WAF 定義為 NAND 寫入除以 host 寫入，指出垃圾回收可能使兩者分離
supporting_source_ids: S20
contrary_source_ids:
as_of: 2026-08-14
basis: S20 PDF pp.2–4 直接界定 DWPD、TBW、換算公式、host／NAND writes、garbage collection、WAF 與 overprovisioning
boundary: 這是 KIOXIA 的通用技術說明與 predictive model，不是任一 AI workload 的實測 WAF、產品保固裁決、跨供應商共同測試或 universe 公司財務證據
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C19
label: verified
status: active
claim: Solidigm D7-PS1010／PS1030 產品簡報把同一 PCIe 5.0、176L TLC 3D NAND 家族分成 standard endurance 與 mid-endurance：前者最高 15.36 TB、五年 1 DWPD、28 PBW，後者最高 12.8 TB、五年 3 DWPD、70 PBW
supporting_source_ids: S21
contrary_source_ids:
as_of: 2026-08-14
basis: S21 PDF p.1 的 Performance and Features at a Glance 逐欄列出 interface、media、user capacity、五年 DWPD 與最高 lifetime PBW
boundary: 同一產品家族與同一 media 標籤不證明兩型號有相同 raw NAND 容量、controller／firmware 配置、製造成本、售價、需求、qualification 或毛利；型錄也不是 production workload 成效樣本
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C20
label: inference
status: active
claim: 依 KIOXIA 公式重算，D7-PS1010 15.36 TB×1 DWPD×365×5＝28.032 PBW、D7-PS1030 12.8 TB×3 DWPD×365×5＝70.080 PBW，分別接回型錄四捨五入的 28 與 70 PBW；後者可用容量少 16.6667%，但額定每日寫入與五年累計寫入均為前者 2.5 倍，而不是 3 倍
supporting_source_ids: S20,S21
contrary_source_ids:
as_of: 2026-08-14
basis: S20 提供換算式，S21 提供兩個產品組態的容量、DWPD、年數與 PBW；Python Decimal 與獨立 awk 兩路重算對 15.36、38.4、28.032、70.080、2.5 與負 16.6667% 一致
boundary: 這是 N＝1 個發行人、N＝1 個產品家族、N＝2 個規格組態的確定性換算，不是隨機產品或 deployment 樣本，沒有 sampling SE／t；2.5 倍只描述額定 writes，不代表效能、使用率、替換率、售價、收入或獲利同倍增加
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C21
label: verified
status: active
claim: OCP Datacenter NVMe SSD Specification v2.7 要求文件提供 WAF＝1 假設下的可寫 physical bytes，並以固定 read／write mix、block size、位址型態、active range、fullness、compressibility 與溫度預處理 EOL 效能；Percentage Used 要隨 bytes written 線性前進並在額定 EOL 對到 100%，但裝置依規格仍可繼續 read／write，直到備援媒體或其他失效條件觸發模式切換
supporting_source_ids: S22
contrary_source_ids:
as_of: 2026-08-14
basis: S22 pp.33、187–189 的 SMART-25、ENDUD-1～3、EOL-1、EOL-4～7 直接定義 endurance estimate、預處理、Percentage Used、EOL 與 Available Spare／read-only 行為
boundary: S22 是 datacenter SSD 的 OCP 規格契約，不代表 S21 產品宣告符合全部 v2.7 條文，也不把 Percentage Used＝100% 定義成保固一定延長、資料一定安全或裝置必然立即故障
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C22
label: inference
status: active
claim: AI 儲存的耐久度應同時保留應用邏輯資料、host writes、NAND writes 與額定壽命四本帳；只有在同一 checkpoint／dataset／model-distribution 工作、裝置、時間窗與副本範圍下量到各層 bytes，才能分開系統放大 H／A、媒體 WAF N／H 與總 NAND 放大 N／A，不能用容量、IOPS、GB/s 或 DWPD 任一單值代替
supporting_source_ids: S2,S10,S11,S20,S21,S22,S23
contrary_source_ids:
as_of: 2026-08-14
basis: S2、S10、S11 顯示 checkpoint 會跨 staging、upload、replica 與多層路徑；S20 分開 host／NAND writes 與 WAF；S21 分開 user capacity、DWPD、年數與 PBW；S22／S23 提供 endurance estimate、Percentage Used、Data Units Written 與其他健康欄位，共同支持四帳不可互填
boundary: 四帳與十二欄護照是研究中心整合不同官方文件的量測框架，不是各組織共同標準；H／A 與 N／H 只有在 scope、clock 與 bytes definition 完全一致時才能相乘，也不直接估算 SSD 顆數、NAND bit demand、replacement、客戶 qualification 或公司財務
verification_needed: 同一具名 production AI workload 公開 application bytes、host Data Units Written、physical NAND bytes、WAF、device health、replication／compression／retry、產品規格、故障重建與部署分母
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

## 1M IOPS 不等於固定 GB/s：先建立效能護照

看到 `1M IOPS`、`10 GB/s` 或 `平均延遲 100 µs`，第一個問題不是哪個數字比較大，而是「哪一種
工作、每次搬多少、同時壓了多少工作、量到哪一層」。SNIA 把 IOPS、Throughput 與 Latency 分成
不同 device-level 測試，正是因為三個 headline 不能互相代替。[S14][S15][S16][S18]

| Headline 指標 | 分子／分母 | 最少要綁定的條件 | 它不能單獨證明 |
|---|---|---|---|
| IOPS | 每秒完成的 I/O 操作數 | block size、read／write mix、random／sequential、client、thread、QD／OIO、device state、cache 與成功／失敗計數 | 每秒搬了多少 bytes、最慢一次等多久、資料是否耐久，或訓練晶片是否少停算 |
| Throughput | 每秒完成的 payload bytes | bytes 單位、block／object size、read／write、路徑範圍、併行、壓縮、cache、量測視窗與 steady state | 操作次數、small-I/O 能力、尾端延遲、restore 正確性或 production goodput |
| Latency／tail | 一次 I/O 從送出到完成的時間與分布 | 起訖點、client／thread／QD／OIO、block size、mix、percentile、事件數、timeout／retry、暖機與裝置狀態 | 整體吞吐、耐久完成、故障域，或某一元件就是端到端瓶頸 |

### 同一個 IOPS 數字換 block size，排名就可能反轉

先做一個只教單位、不模擬真實 SSD 的例子。假設每個被計數的 I/O 都成功，而且每次 payload
大小完全固定，則 `payload rate = IOPS × payload per operation`：

| 假想 workload | 操作速率 | 每次 payload | 條件式 payload rate | 不能外推 |
|---|---:|---:|---:|---|
| A：small-block | 1,000,000 IOPS | 4 KiB | 3.814697265625 GiB/s＝4.096 GB/s | 不代表 tail latency、QD=1 效能或應用 goodput |
| B：large-block | 100,000 IOPS | 128 KiB | 12.20703125 GiB/s＝13.1072 GB/s | 不代表 random small-I/O 能力、持久性或較低成本 |

B 的 IOPS 只有 A 的十分之一，payload rate 卻是 A 的 3.2 倍。這不是哪一個 workload「更好」，
而是證明少了 block size 與單位，IOPS 排名沒有共同比較基準。SNIA 的 IOPS 頁面因此把多個 block size
與 read／write mix 分開，而 Throughput 頁面另量 large-block sequential workload；KiB 也明定為
1024 bytes，不和 KB 靜默互換。[S15][S18][S19]

算術與誤差邊界：這是 **N=2 個假想 workload** 的確定性單位展開，不是裝置或 run 樣本，沒有
sampling SE／t。Python Fraction 與獨立 awk 兩條路徑都得到 A=`3.814697265625 GiB/s`、
B=`12.20703125 GiB/s`、B／A=`3.2`。一致只證明乘法與單位換算；protocol overhead、failed／retried
I/O、compression、cache、latency、durability、power 與 application outcome 全都還沒進來。

### Queue depth 能推高併行，也會換掉延遲問題

SNIA 術語頁把 QD 定義成每個 thread 允許的 outstanding I/O，TC 則是 thread／process 數。[S17]
因此 `TC=32、QD=32` 與 `TC=1、QD=1` 名目上分別允許最多 1024 與 1 個 total outstanding I/O；
實際同時未完成數仍要另存，即使最後都報 IOPS，兩者也不是同一種等待條件。

| 量測視角 | 它回答什麼 | 必須保存 | 不能拿來代替 |
|---|---|---|---|
| TC1／QD1 baseline latency | 沒有 queue benefit 時，一個指令往返多快 | block size、mix、average、maximum、事件數與 device state | 高併行吞吐、production tail 或整群 accelerator stall |
| QD／TC sweep | demand 增加時，IOPS、平均／最大回應時間與分布如何一起變 | 每個 TC×QD operating point、total OIO、CPU、histogram 與 steady-state window | 真實 workload 的 client 數、cache、網路與端到端 SLO |
| AI end-to-end tail | 最慢 dataset fetch 是否拖住同步訓練步驟 | per-I/O distribution、pMax／percentile、stall、timeout／retry 與 accelerator 分母 | SSD 單獨因果、checkpoint durability 或公司 qualification |

SNIA 的 Latency 導讀把 TC1／QD1 當作無 queue benefit 的 baseline，並提醒 outstanding I/O 更多時
maximum latency 可能不同。[S16] Meta 的 production 說法又把最慢 storage fetch 接到同步 GPU
step 的停等。[S1] 合起來的讀法是：peak IOPS、QD1 latency 與 production pMax 都要保留，不能互填。

### 十欄 AI 儲存效能護照

| 護照欄位 | 最少要寫什麼 | 少了最容易誤讀成 |
|---|---|---|
| 1. 工作與量測範圍 | dataset fetch／checkpoint／model distribution；device、filesystem、object store 或 end-to-end 起訖點 | 把單顆 SSD 數字直接當成訓練 goodput |
| 2. 系統、版本與路徑 | device／firmware、host、CPU／RAM、NIC／switch、filesystem／client、framework、driver、拓撲與版本 | 同時換了軟硬體，差異卻全算給儲存 |
| 3. I/O shape | block／object size、read／write mix、random／sequential、sharding、compression 與資料分布 | 不同工作負載的 IOPS／GB/s 被直接排名 |
| 4. 單位與計數 | bytes／KB／KiB／GB／GiB、成功／失敗／retry、payload 或 wire bytes、ops 定義 | 十進位與二進位、重試與有效資料被重複計算 |
| 5. 併行與 demand | clients、hosts、threads、QD／OIO、batch、accelerator 數及每層 queue | 用高 QD peak 替代低延遲或真實 client 行為 |
| 6. 裝置狀態與 cache | purge／pre-conditioning、fresh／warm／steady、active range、cache 容量／命中與 write-cache policy | 把剛清空的短暫高點寫成長期效能 |
| 7. 完成與正確性 | command completion、staging、upload、durable、restore；checksum、partial、timeout 與 retry | 寫入回報完成被改寫成可復原與正確使用 |
| 8. 延遲分布與事件數 | average、p50／p90／p99／p99.9／pMax／maximum、每格 I/O 數、censoring 與 outlier policy | 平均掩蓋同步訓練真正會遇到的慢端 |
| 9. 視窗、重複與不確定度 | warm-up、measurement window、steady-state criterion、run 數、run-level 分布、SE／t 或不能計算原因 | 單次峰值、短窗或挑選結果被寫成穩定能力 |
| 10. 使用者結果與分母 | stall、lost steps、restore／startup、Runtime Goodput、容量／功耗／成本、部署量與公司財務 | device benchmark 被直接換算成硬體需求、訂單或毛利 |

這張護照是研究中心把 SNIA device method、Meta pMax mechanism 與 MLCommons 的 workload／system
description／重跑要求合併成的可比性框架，不是三方共同發布的標準。[S1][S9][S14][S15][S16]
[S17][S18][S19] 它的用途是讓同一問題可重建；填滿十欄仍不代表 durability、correctness、customer
qualification 或公司財務已成立。

### 多空小作文要共享同一份 workload

| 敘事 | 合理假說 | 必須再看到的共同證據 | 什麼會讓敘事失效 |
|---|---|---|---|
| 偏多：AI 讓高階儲存內容與驗證增加 | 更高 concurrency、small-I/O、large checkpoint 與更嚴 tail SLO，可能增加 enterprise SSD、controller、NIC、storage node、韌體與驗證工時 | 同一 production workload 的十欄護照、baseline／treatment、path share、BOM、qualification、部署量、價格、收入與毛利分母 | 只有 peak IOPS／GB/s、產品頁或廣義 AI 占比，沒有 production bottleneck、採用與財務共同鍵 |
| 偏空：軟體與資料位置吸收硬體增量 | cache、prefetch、peer transfer、compression、較少 checkpoint bytes 或 scale-out 可能讓每單位 compute 的外部 I/O／SSD 容量下降 | 相同 workload 的 cache hit、外部 bytes、device utilization、stall、goodput、設備數與前後期成本 | 只看單一路徑流量下降，卻漏掉副本、RAM、網路、耐久層或整體 compute 增長 |
| 共同底線 | 快不等於有用，更不等於公司賺到 | 固定 workload／scope／units／QD／state／completion／distribution，再做買方與供應商雙向核對 | 拿不同 block、不同 QD、不同測量層的數字相減，直接生成 TAM、份額或投資結論 |

本輪新增的是 N=6 個 SNIA 官方 HTML 頁面（1 個標準入口、5 個方法／術語頁）的一條
storage-method 消息鏈，並與既有 Meta、MLCommons 兩條獨立鏈交叉；它們不是六顆 SSD、六個 AI 叢集
或六家公司樣本。除 N=2 假想 workload 的確定性
單位換算外，沒有新的 effect size、sampling SE／t、價格、估值、共識或投資判斷。

## GB/s 跑得快，不等於耐久夠：先拆四本寫入帳

「每次 checkpoint 是 1 TB」至少可能指四件不同的事。應用程式先產生一份邏輯狀態，框架可能切片、
壓縮、加 metadata、重送或做多份副本，主機才把 bytes 送進 SSD；控制器又可能為垃圾回收與媒體管理
重寫 NAND。最後，產品型錄的 DWPD／TBW 只是額定壽命契約，不是上述任一層的即時流量。[S20][S22][S23]

| 寫入帳 | 分母與量測位置 | 可能改變它的機制 | 不能拿哪一本帳代替 |
|---|---|---|---|
| A：應用邏輯資料 | 同一 checkpoint、dataset ingest 或 model artifact 的有效 payload bytes | 模型狀態內容、sharding、checkpoint 頻率與保留政策 | 檔案大小不等於 host writes，更不等於 NAND writes |
| H：主機寫入 | 主機對指定 SSD／namespace 在同一時間窗送出的 bytes | 壓縮、去重、副本、metadata、重試、filesystem 與 tiering | Data Units Written 不知道哪些 bytes 最後形成有效訓練進度 |
| N：NAND 寫入 | 控制器實際寫入快閃媒體的 bytes | garbage collection、wear leveling、資料搬移、I/O 對齊、active range、fullness 與 overprovisioning | NAND writes 不能反推唯一 workload，也不等於使用者可見容量 |
| L：額定壽命 | 指定容量、DWPD／TBW、年限、測試條件與保固邊界 | 媒體、控制器、韌體、預留空間、工作負載與環境 | 型錄 3 DWPD 不等於當天一定寫了三次，也不是寫入 GB/s |

在同一裝置、時間窗與 bytes 定義下，H／A 是系統層放大，N／H 才是 WAF，N／A 才是應用到 NAND
的總放大；此時 N／A＝H／A×N／H 只是對帳恆等式。若 A 是壓縮前 bytes、H 混入副本與重試、N 又取
另一批 SSD 或另一個時間窗，三個比率即使各自漂亮，也不能相乘。KIOXIA 的文件只把 WAF 定義成
NAND writes／host writes，沒有替研究者補上 A；A 到 H 必須回到實際框架與部署量測。[S20]

### DWPD 是壽命分母，不是速度分母

KIOXIA 給出的換算是：TBW＝DWPD×SSD 可用容量×指定年數×365。[S20] 套到 Solidigm 同一 D7
產品家族的最大容量組態，可把型錄四捨五入值接回來：[S21]

| 產品組態 | 使用者可見容量 | 五年 DWPD | 額定每日寫入 | 公式重算五年 PBW | 型錄最高 lifetime PBW |
|---|---:|---:|---:|---:|---:|
| D7-PS1010 Standard Endurance | 15.36 TB | 1.0 | 15.36 TB／日 | 28.032 PBW | 28 PBW |
| D7-PS1030 Mid-Endurance | 12.8 TB | 3.0 | 38.4 TB／日 | 70.080 PBW | 70 PBW |

這個例子最值得注意的不是「3 比 1」。PS1030 的可用容量比 PS1010 少 16.6667%，因此額定每日寫入與
五年累計寫入都是 2.5 倍，不是 3 倍。兩者同列 PCIe 5.0 與 176L TLC 3D NAND，只能證明型錄把
capacity 與 endurance 做成不同組態；文件沒有提供 raw NAND、預留比例、控制器差異、售價、訂單、
deployment mix 或毛利，不能把容量差自行解釋成成本結構。[S21]

算術與誤差邊界：這是 N＝1 個發行人、N＝1 個產品家族、N＝2 個規格組態的確定性換算，不是隨機
產品、SSD、機架或客戶樣本，沒有 sampling SE／t。Python Decimal 與獨立 awk 兩路都得到每日
15.36／38.4 TB、五年 28.032／70.080 PBW、比值 2.5 與容量差負 16.6667%；一致只驗證單位與乘法，
不驗證真實 workload、失效率、替換率或財務效果。

### Percentage Used 到 100%，也不是「現在立刻壞掉」

OCP Datacenter NVMe SSD Specification v2.7 把耐久度寫成一份測試契約，而不是一個孤立數字。
ENDUD-1 要求文件提供 WAF＝1 假設下可寫入的 physical bytes；ENDUD-2 的 EOL 預處理又固定為
50／50 read／write、4 KiB read、128 KiB write、random read、sequential write、100% active range、
80% full、不可壓縮資料與 35°C 環境。[S22] 這些條件少一個，就不能把自己的 AI workload 宣稱為
「等同規格測試」。

同一規格要求 Percentage Used 隨 bytes written 線性前進，並在額定 EOL 對到 100%；但 EOL-4
仍要求裝置在後續失效條件到來前維持 read／write，EOL-5 才把 Available Spare 到 0% 接到 read-only
模式。[S22] 因此 100% 是額定壽命邊界，不是保證下一秒故障；反過來，Percentage Used 低於 100%
也不能保證健康，還要看 available spare、critical warning、media errors、溫度、unsafe shutdowns、
firmware 與 self-test。NVMe 官方工具頁把這些欄位放在同一份 SMART log，Data Units Written 則以
512×1000 bytes 為一個單位再轉成十進位 TB／PB。[S23]

### 十二欄耐久度護照：先能對帳，再談買多少

| 護照欄位 | 最少要保存 | 少了會犯的錯 |
|---|---|---|
| 1. AI 工作與完成語意 | dataset fetch／checkpoint／model distribution；staging、upload、durable 或 restore | 把暫存 bytes 當成耐久副本 |
| 2. 應用邏輯量 A | 每次有效 payload、頻率、保留數、觀測日數與成功／失敗事件 | 用模型大小直接乘 GPU 數 |
| 3. 系統放大 H／A | compression、dedupe、sharding、replica、metadata、retry 與每層 bytes | 漏掉副本，或把壓縮前後重複計數 |
| 4. Host writes H | 每顆 SSD／namespace 的 Data Units Written、觀測起訖、counter reset／wrap 與 units | 把 cluster bytes 填進單顆 drive 分母 |
| 5. NAND writes N 與 WAF | physical NAND bytes、同窗 host bytes、WAF、firmware 與計數來源 | 用廠商通用 WAF 假設取代 production telemetry |
| 6. 容量契約 | user capacity、raw／reserved 未知邊界、namespace、overprovisioning 與 usable fullness | 把 TB 型號當成全部可寫空間或 raw NAND |
| 7. 額定壽命 L | DWPD、TBW／PBW、指定年限、保固、EOL 定義與 workload profile | 把 DWPD 當吞吐，或跨年限直接排名 |
| 8. I/O shape | block size、alignment、read／write mix、random／sequential、QD／TC、active range | 峰值 GB/s 被拿來估耐久消耗 |
| 9. 裝置狀態與環境 | pre-conditioning、fullness、compressibility、temperature、power state 與 duty cycle | 剛清空或較低溫結果被當長期能力 |
| 10. 健康與事件 | Percentage Used、Available Spare、critical warning、media errors、unsafe shutdown、thermal time | 單一 100% 或 0 error 被寫成完整健康結論 |
| 11. 故障與更換 | replica／erasure code、rebuild writes、spare policy、failure domain、restore 與更換門檻 | 只算正常寫入，漏掉重建與營運備援 |
| 12. 商業與財務 | 具名產品、qualification、部署量、產品組合、ASP、收入、毛利、庫存與現金 | endurance 需求直接變成某公司營收 |

護照填滿後仍要先分「每單位 compute 的寫入」與「整體 compute 數量」。前者可能因 cache、peer path、
compression、較少 checkpoint、write shaping 或較低 WAF 而下降；後者可能因叢集擴大而上升。兩個方向
可以同時成立，最後要看 A、H、N 與 drive-days 的總量，而不是挑一個方向寫故事。[S1][S2][S3][S20]

### 多空小作文共用同一張耐久帳

| 敘事 | 合理機制 | 必須看到的共同證據 | 失效條件 |
|---|---|---|---|
| 偏多：AI 把儲存價值推向高耐久與管理能力 | checkpoint 更大／更頻繁、更多副本、write-heavy cache、較高 WAF 或更嚴 EOL／recovery SLO，可能提高 mid／high-endurance SSD、controller、firmware、telemetry 與驗證價值 | 同一 production workload 的 A／H／N、WAF、drive-days、產品 endurance mix、qualification、部署量、ASP、收入與毛利 | 只有模型大小、GB/s、產品頁或 broad AI revenue，沒有 host／NAND writes 與產品組合共同鍵 |
| 偏空：軟體把寫入與磨耗增量吸收 | multi-tier checkpoint、壓縮／去重、peer transfer、write shaping、較低頻率或較大 sequential writes 可降低 H／A 或 N／H | 固定 compute 與 SLO 的 baseline／treatment，公開 bytes、WAF、goodput、restore、設備數、壽命與成本 | 只量單顆 device WAF 下降，卻漏掉更多副本、cluster 擴張、RAM／network 成本或失敗重建 |
| 共同裁決 | 高容量、高效能、高耐久與低成本是四個不同軸 | 十二欄護照加買方／供應商雙向文件 | 由 1 DWPD／3 DWPD、TLC／QLC 或單一 SMART 欄位直接生成 TAM、份額、訂單或投資結論 |

本輪新增 N＝4 份一手文件／頁面，分屬 KIOXIA、Solidigm、OCP 與 NVM Express 四條消息鏈；它們不是
四顆 SSD、四個 AI cluster 或四個客戶樣本。只有 N＝2 個同家族型錄組態的確定性換算；沒有 production
application／host／NAND 三層共同觀測、run-level 變異、sampling SE／t、價格、估值、共識、部位或
投資建議。對 8299 群聯而言，這張護照只新增企業 SSD／控制器／韌體研究問題，沒有新增具名客戶、
qualification、出貨、收入或毛利事實。

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

<!-- research_source
source_id: S14
role: standard
source_kind: document
publisher: Storage Networking Industry Association
independence_group: snia-storage-method
title: Solid State Storage (SSS) Performance Test Specification (PTS)
published_at: 2020-10-01
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.snia.org/solid-state-sss
locator: 標準入口的 v2.0.2、SNIA Standard、Published October 1 2020，以及 device-level comparative testing for Enterprise and Client systems 說明
limitation: 入口頁只確認現行版本與範圍，不包含完整 normative 條文；官方 PDF 在本執行環境直接下載與頁面影像快取均遭 HTTP 403／cache miss，故本輪沒有本地 SHA 或逐頁視覺驗證，也不以 PDF 未核頁內容支撐主張
-->

<!-- research_source
source_id: S15
role: other_primary
source_kind: living_index
publisher: Storage Networking Industry Association
independence_group: snia-storage-method
title: IOPS (I/Os per Second) Test
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.snia.org/forums/sssi/pts/iops
locator: Summary、Test Setup 與 Benefits；random I/O、7 種 read／write mix、8 種 0.5–1024 KiB block size、WIPC／WDPC、5-round steady-state window 及 box-top up-to IOPS 邊界
limitation: HTML 方法導讀沒有版本與發布日，可能保留較早 PTS 的測試矩陣或術語，不能替代 v2.0.2 normative specification；device-level synthetic test 也不是 AI production workload、durability、qualification 或財務證據
-->

<!-- research_source
source_id: S16
role: other_primary
source_kind: living_index
publisher: Storage Networking Industry Association
independence_group: snia-storage-method
title: LAT (Latency) Test
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.snia.org/forums/sssi/pts/lat
locator: Summary、Test Setup 與 Benefits；steady-state random I/O 的 average／maximum response time、total outstanding I/O=1 baseline，以及更多 outstanding I/O 時 maximum latency 可能不同的限制
limitation: HTML 方法導讀沒有版本與發布日，QD1 device baseline 不能替代高併行 response-time distribution、filesystem／network／application path、AI accelerator stall、durability 或 customer SLO
-->

<!-- research_source
source_id: S17
role: other_primary
source_kind: living_index
publisher: Storage Networking Industry Association
independence_group: snia-storage-method
title: Test Terminology
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.snia.org/forums/sssi/pts/testterms
locator: QD／TC、Preconditioning、Purge、SS Rounds 與 WSAT Steady State；OIO 是 issued and awaiting completion、QD 是每 thread 的 I/O 數、TC 是 stimulus generator process 數
limitation: 動態術語導讀的例示 test system 與部分 Client／Enterprise 說法可能屬較早 PTS 世代；只用來界定名詞責任，不證明現行產品結果或 AI production 配置
-->

<!-- research_source
source_id: S18
role: other_primary
source_kind: living_index
publisher: Storage Networking Industry Association
independence_group: snia-storage-method
title: TP (Throughput) Test
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.snia.org/forums/sssi/pts/tp
locator: Summary、Test Setup 與 Benefits；large-block sequential 100% read／write、WIPC／WDPC、steady-state window、128／1024 KiB 與 up-to MB/s 邊界
limitation: HTML 方法導讀沒有版本與發布日，synthetic large-block device throughput 不能替代 small-I/O、tail latency、real AI data path、checkpoint correctness、功耗成本或公司採用
-->

<!-- research_source
source_id: S19
role: other_primary
source_kind: living_index
publisher: Storage Networking Industry Association
independence_group: snia-storage-method
title: Workload Terminology
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.snia.org/forums/sssi/pts/workload
locator: KiB=1024 bytes 而 KB=1000 bytes、Fresh Out of Box、random／sequential、read／write 與 prescribed-workload steady state 定義
limitation: 術語頁只建立單位與 workload 名詞，沒有 GB／GiB throughput result、IOPS 算例、device test、AI workload、客戶 qualification 或財務歸因
-->

<!-- research_source
source_id: S20
role: other_primary
source_kind: document
publisher: KIOXIA America
independence_group: kioxia-storage-vendor
title: How Does Endurance Work in SSDs?
published_at: 2021-03-01
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://americas.kioxia.com/content/dam/kioxia/en-us/business/memory/asset/KIOXIA-SSD-NAND-Endurance-Tech-Brief.pdf
locator: PDF pp.2–4 的 SSD Endurance Overview、DWPD／TBW conversion、Flash Memory Wear-out、WAF 與 overprovisioning；本地檔 SHA-256 a06ca25dfb59c59221682937090fb709563622455ebc76640e3aa69e498419ed
limitation: KIOXIA 通用技術簡報只在封面標示 March 2021，本 ledger 以月初作 published_at 日期鍵；DWPD／TBW 是 predictive model，產品、保固、workload、WAF 與實際結果仍須逐案核對，不能把媒體類別區間或通用機制當 AI deployment 樣本
-->

<!-- research_source
source_id: S21
role: competitor_primary
source_kind: document
publisher: Solidigm
independence_group: solidigm-storage-vendor
title: Solidigm D7-PS1010 and D7-PS1030 Product Brief
published_at: 2024-08-06
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.solidigm.com/content/dam/solidigm/en/site/products/data-center/product-briefs/ps1010-ps1030/solidigm-d7-ps1010-d7-ps1030-product-brief.pdf
locator: PDF p.1 的 interface、media、user capacity、五年／三年 DWPD 與最大 lifetime PBW；p.7 的測試與產品限制；本地檔 SHA-256 ebda7161ea19a616c1386d6bca94fcf0c153d1b563e5f32d7b97ba62392e2a4b
limitation: 發布日依 PDF 內 Embargoed until August 6 2024；這是 vendor product brief，不提供 raw NAND、overprovisioning 比例、完整 qualification、production workload、銷量、價格、客戶或財務，效能比較亦有 vendor test 與 estimated／simulated 限制
-->

<!-- research_source
source_id: S22
role: standard
source_kind: document
publisher: Open Compute Project
independence_group: ocp-datacenter-ssd-standard
title: Datacenter NVMe SSD Specification Version 2.7
published_at: 2026-01-08
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.opencompute.org/documents/datacenter-nvme-ssd-specification-v2-7-final-pdf-1
locator: cover 的 Version 2.7 01082026；PDF p.33 SMART-25；pp.187–189 ENDUD-1～3、EOL-1、EOL-4～7；revision history 另列 v2.7 2025-10-24
limitation: 文件封面日期碼與 revision history 日期均原樣保留，不自行判定哪一個是 drafting／publication 時點；官方 PDF 可由研究瀏覽器全文擷取與引用頁檢視，但直接 curl 回 HTTP 403，故本輪沒有本地檔 SHA；規格要求不證明任一產品已符合 v2.7、通過客戶驗證或形成訂單
-->

<!-- research_source
source_id: S23
role: standard
source_kind: living_index
publisher: NVM Express
independence_group: nvme-standard-body
title: Open Source NVMe SSD Management Utility — NVMe Command Line Interface
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://nvmexpress.org/open-source-nvme-ssd-management-utility-nvme-command-line-interface-nvme-cli/
locator: Health Monitoring／SMART Log 段落的 Percentage Used、Data Units Written 512×1000 bytes、Available Spare、temperature、unsafe shutdowns、media errors 與 device self-test 欄位
limitation: 動態工具導讀沒有頁面發布日；命令輸出是官方頁面的單一示例，不是產品 benchmark、跨裝置健康門檻、保固裁決、AI workload、qualification 或供應商財務證據
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

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C18,C19,C20,C21,C22
metric: 同一 AI workload 的 application logical bytes、host Data Units Written、physical NAND bytes、WAF、DWPD／TBW、Percentage Used、Available Spare、故障重建與產品 endurance mix
source_ids: S20,S21,S22,S23
watch_source_ids: S5,S6,S7,S8,S22,S23
frequency: quarterly
frequency_detail: 每季檢查 operator storage／checkpoint 架構、OCP／NVMe 規格與 8299 公司文件；具名產品 qualification 或 production telemetry 出現時提前重審
next_check: 2026-08-28
trigger: 具名 operator 在同一版本化 AI workload 公開 A／H／N 三層 bytes、WAF、drive-days、EOL／rebuild policy 與產品配置，且買方與供應商文件雙向確認 qualification、部署量及財務分母
invalidation: 新規格或 production evidence 顯示四帳／十二欄遺漏會改變 endurance、availability 或 economics 結論的必要欄位，或同一組 scope 證明本文的 A／H／N 邊界無法重建；屆時新增修正 claim，不回寫既有研究快照
-->

## 目前不能下的結論／待驗證

- 不能把 Meta、AWS 與 NVIDIA 三家的文件拼成同一套正式運作架構；本篇只把三種工作分開比較。
- 不能把資料容量、峰值速度或模型大小直接換算成 SSD 顆數；快取、預先讀取與附近節點互傳都會減少重複讀取。
- 不能把群聯廣義 AI 產品組合的 38% 當成企業級 SSD、AI 伺服器或本文三種工作的收入；這個比例混合多種產品與終端。
- 不能由群聯具備控制器、韌體與企業 SSD 能力，推導它已進入 Meta、AWS 或 NVIDIA 的具名設計、訂單、份額或毛利。
- 不能把伺服器組裝廠的一般整合能力當成 AI 儲存路徑已通過客戶認證；仍需要同一平台的物料清單、服務目標、驗收、部署與出貨文件。
- 不能把 I/O 模擬跑完、暫存完成或上傳完成改寫成 checkpoint 已跨故障範圍耐久保存、正確回載並改善 Runtime Goodput；六層完成階梯要逐層留證據。
- 不能把模型或 checkpoint 大小直接當成 host writes，更不能把 host writes 當成 NAND writes；沒有同窗 A／H／N 與 WAF，就不能估 SSD 磨耗、替換或顆數。
- 不能把 1 DWPD／3 DWPD、Percentage Used＝100% 或 TLC／QLC 單一標籤改寫成效能、立即故障、客戶採用、售價、收入或毛利；容量、壽命、健康與商業是不同證據軸。
- 不能把 Google 單一 35K-chip TPU v5p 組態報告的 6.59% ML Goodput 改善外推成跨模型、跨平台或產業平均；公開資料沒有 run 數、變異、原始樣本或 SE／t。
