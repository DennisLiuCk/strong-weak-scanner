# 2026-08-09 族群覆蓋補強研究雷達

本輪從 11 個正式族群的文章、圖譜與具名公司邊覆蓋出發廣搜，不以熱門度或固定篇數選題。
八題排名在深研前凍結於 RS-2026-08-09-01；前六題通過 article＋graph 契約，其餘保留原
watch／defer 決策。第三題的升格結論是小晶片公開合規鏈仍不完整；第四題只對齊 SDC 分類、
測試交接與單站隔離；第五題確認材料、板路與 BER 公開證據仍無法對上同一塊板；第六題則確認
JEP203／JEP204 尚未在本輪三份 OCP 公開規格中形成平台驗收文字橋。後四題都不建立
公司財務價值線。升格只表示可形成
可證偽責任鏈，不代表訂單、營收、毛利或投資建議。

<!-- research_radar
schema_version: 2
radar_id: RADAR-2026-08-09-01
as_of: 2026-08-12
next_review: 2026-08-16
status: active
method: 先以 universe 族群規模 研究文章路由 知識圖譜及具名公司邊做覆蓋盤點，再廣搜 operator 標準組織 監管機關與公司一手來源；依可證偽性 至少兩條獨立一手鏈 能否補現有知識缺口 公司映射風險及後續維護成本排序。候選先寫入 append-only selection log 並獨立 commit；深研後只更新 evidence posture route 與結果，不改凍結排名 第一拒絕與下一份證據
selection_cycle_id: RS-2026-08-09-01
-->

<!-- research_candidate
candidate_id: RC-AI-RACK-EMC-CERTIFICATION
rank: 1
title: AI 機櫃 EMC 測試容量與驗收責任階梯
group_ids: passive,powersupply,serverodm
reader_group_questions: passive => 零件層如何抑制或隔離電磁干擾？ | powersupply => 電源子系統由誰整合測試並修正干擾？ | serverodm => 整櫃送驗、跨模組除錯與最終簽收由誰負責？
reader_question: 大型 AI 機櫃送驗時，零件、子系統與整櫃的電磁干擾，分別由誰測試、修正與簽收？
reader_starting_point: 零件各自合格，不等於整櫃一定合格；尺寸、供電與設備互相干擾仍要另外確認。目前還缺可重複的整櫃驗收方法與足夠測試空間。
reader_terms: EMC => 電磁相容，檢查設備是否會干擾別人或被外界干擾 | chamber => 隔離外界電磁干擾的專用測試室 | qualification => 產品正式採用前必須通過的合格驗證
reader_next_step: 先找整櫃測試方法、合格實驗室與買方驗收條款，確認大型機櫃是否真的面臨測試容量瓶頸。
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: OCP 2026 EMC 專題已把 megawatt-scale、重型且解耦式 AI 機櫃的 chamber、供電、承載與 lab capacity 列為實際測試難題；IEC CISPR 32 與 FCC Part 15 又提供設備排放範圍及認可測試入口，足以研究元件合規、子系統預掃與整櫃驗收是否形成新的責任階梯，而不是把 EMI 元件需求直接當成答案。
knowledge_gain: 把被動元件最薄的公司橋補到 2327 具名 EMI 產品能力，並把 component suppression、equipment standard／procedure 與 full-rack lab capacity 分層；公司邊維持推論，未升格成 AI rack qualification 或財務曝險。
first_rejection: 若可用測試實驗室、供電與 chamber 能力並不稀缺，或平台可由既有模組證書完整覆蓋整櫃而不需系統級重驗，這就不是獨立瓶頸；找不到本 universe 的具名測試、設備、機構或 EMI 產品資格證據時，也不做受惠映射。
next_evidence: 取得 OCP AI rack EMC 測試方法、CISPR／FCC 適用邊界、具備高功率與大 chamber 能力的認可實驗室名單及 lead time；再找平台買方的整櫃驗收條款、失敗模式與台灣供應商可定位的 qualification。
next_check: 2026-08-31
route: article_and_graph
article_topic_id: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION
graph_id: ai-rack-emc-certification
sources: OCP Podcast Episode 21 EMC testing challenge => https://www.opencompute.org/index.php/ocp-podcast | IEC CISPR 32 publication => https://webstore.iec.ch/en/publication/22046 | FCC KDB Part 15 measurement procedures => https://apps.fcc.gov/oetcf/kdb/forms/FTSSearchResultPage.cfm?id=21079&switch=P | FCC EAS accredited test firms => https://opendata.fcc.gov/Engineering-Technology/EAS-Accredited-Test-Firms/nubx-v54a | Yageo KEMET FLEX SUPPRESSOR => https://www.yageo.com/jp/PressRoom/Content/press_room?category=product_event&news_id=20210226&page=14
-->

<!-- research_candidate
candidate_id: RC-AI-STORAGE-DATA-PLANE
rank: 2
title: AI 訓練資料、checkpoint 與模型權重分發的 I/O 契約
group_ids: memory,serverodm
reader_group_questions: memory => 訓練資料、checkpoint 與模型權重分別需要哪種記憶與儲存層？ | serverodm => GPU、網路、儲存節點與軟體之間的資料路徑由誰整合？
reader_question: AI 訓練從讀資料、保存中途進度到分發模型，各階段卡住時是否由不同設備與軟體負責？
reader_starting_point: 讀訓練資料、保存中途進度與搬動模型，是三種不同的資料流，卡住的位置與負責設備可能不同。目前還缺一套能直接比較速度與失敗門檻的資料。
reader_terms: I/O => 資料讀入與寫出的路徑 | checkpoint => 訓練途中保存的進度快照，失敗後可從這裡恢復 | SLO => 系統承諾達到的服務目標，例如最慢回應時間
reader_next_step: 先取得三種資料流的速度與失敗門檻，再分清 GPU、網路、儲存節點和軟體各自負責哪一段。
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: Meta 2026 AI Storage Blueprint 將資料讀取的 pMax latency 與 GPU stall 直接連結，AWS 的大規模 checkpoint 架構與 NVIDIA ModelExpress 又分別公開 checkpoint burst、模型權重分發與 GPU-direct／RDMA 路徑；三條獨立來源可把資料集讀取、checkpoint 與模型載入拆成不同 I/O 契約，補足現有題庫偏重 HBM／CXL 而未處理持久儲存資料面的缺口。
knowledge_gain: 把 memory 族群從抽象容量敘事補成三條不同失敗條件與驗收分母，新增 8299 的具名能力入口，同時保留 cache、prefetch、peer transfer 可能吸收硬體需求的反證。
first_rejection: 若三種流量主要由軟體快取與網路編排吸收，無法形成可重現的 device、controller、NIC、switch 或 storage-node qualification，或找不到本 universe 的具名產品與量產證據，就不把 AI 訓練成長外推成 SSD／控制器／伺服器用量。
next_evidence: 取得 operator 級 pMax／checkpoint SLO、failure domain 與 media endurance 資料，對齊 GPU-direct、RDMA、網路與儲存節點責任；再查平台正式 BOM、qualification、部署分母及台灣公司的產品／收入足跡。
next_check: 2026-08-28
route: article_and_graph
article_topic_id: MI-2026-08-09-AI-STORAGE-DATA-PLANE
graph_id: ai-storage-data-plane
sources: Meta AI Storage Blueprint at Scale => https://engineering.fb.com/2026/07/01/data-infrastructure/metas-ai-storage-blueprint-at-scale/ | AWS scalable checkpoint storage => https://aws.amazon.com/blogs/storage/architecting-scalable-checkpoint-storage-for-large-scale-ml-training-on-aws/ | NVIDIA ModelExpress => https://developer.nvidia.com/blog/modelexpress-distributing-model-artifacts-at-the-speed-of-light/ | Phison investor meeting information => https://www.phison.com/en/investor-relations/shareholder-services/investor-meeting-information
-->

<!-- research_candidate
candidate_id: RC-CHIPLET-DESIGN-KIT-CONFORMANCE
rank: 3
title: Chiplet design kit、metadata 與 conformance workflow
group_ids: ipdesign,packtest,semiequip
reader_group_questions: ipdesign => 共同設計資料與介面規則如何交給工具與各家晶粒？ | packtest => 多家晶粒組合後，誰負責封裝整合與合格驗證？ | semiequip => 哪些量測、測試與製程設備能執行共同驗證？
reader_question: 多家小晶片要組成一套系統時，熱、供電、機構與測試資料能否用共同格式交換並通過驗證？
reader_starting_point: 把小晶片連起來的介面標準只解決一部分問題，各家還要交換熱、供電、機構與測試資料。目前還缺多供應商工具與封測實作的共同驗證。
reader_terms: Chiplet => 可與其他晶粒共同封裝的小晶片 | design kit => 讓不同團隊依同一規則設計與檢查的資料包 | conformance => 是否符合共同規格的驗證流程
reader_next_step: 先找共同格式能被設計工具實際讀入、並由晶圓廠或封測廠完成多供應商驗證的案例。
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: FCSA 1.0 已正式定義系統角色與分級，OCP 3DK 教程也把 CDK／ADK／MDK／TDK 分工排入設計流程；但 TDK 明示不定義 workflow，本輪固定 commit 全查四份 XSD 又重現 CDXML／ADK 兩份因 namespace prefix 無法解析。配合一項 CDXML 單工具產品自述與 Siemens 尚為正式採用承諾，足以建立「格式存在不等於端到端 conformance」的可證偽邊界文章。
knowledge_gain: 把既有 UCIe 圖譜之後再拆出連線介面、系統角色、設計資料與合規流程四層，新增 schema 執行、單工具匯入、跨工具重現及 foundry／OSAT 簽核六關；研究結果觸發原 first rejection，因此只建立責任與反證圖，不建立 EDA、矽智財、封裝、測試或設備公司的受惠線。
first_rejection: 若 FCSA、CDXML、JEP30 與 3DK／MDK 無法落成同一套多供應商設計交換或 conformance workflow，或沒有 tape-out／foundry／OSAT 實作，就只是重疊規格清單，不建立 EDA、矽智財、封裝或測試價值鏈。
next_evidence: 取得 FCSA conformance／implementation 資料、CDXML 與 JEP30 欄位對照、3DK／MDK／test kit 的實際工具匯入與多供應商案例；再查 foundry、OSAT、EDA 與本 universe 公司是否有具名採用。
next_check: 2026-08-24
route: article_and_graph
article_topic_id: MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS
graph_id: chiplet-design-handoff-contracts
sources: OCP FCSA 1.0 specification => https://www.opencompute.org/documents/fcsa-1-0-0-pdf | OCP 3DK drop-in tutorial => https://drive.google.com/file/d/10QpQ-o-SX10qFPyrVmgM3wnWvevbemeD/view?usp=drive_link | ODSA-CDXML fixed commit => https://github.com/opencomputeproject/ODSA-CDXML/tree/5a725e45784471e7887d0359daaf4f80223fafb4 | Arm CSA ecosystem article => https://newsroom.arm.com/blog/arm-chiplet-system-architecture-accelerating-evolution-of-silicon | DankaChiplet OCP listing => https://www.opencompute.org/chiplets/57/thrace-systems-dankachiplettm-platform-for-3d-ic-architects | Siemens 3D IC workflows => https://eda.sw.siemens.com/en-US/eda-cloud-solutions/ic-packaging/3d-ic-design/
-->

<!-- research_candidate
candidate_id: RC-AI-SILENT-DATA-CORRUPTION
rank: 4
title: AI 硬體 silent data corruption 的跨生命週期責任鏈
group_ids: packtest,semiequip,serverodm
reader_group_questions: packtest => 工廠測試與 burn-in 能提早抓到哪些無聲錯誤？ | semiequip => 哪些測試與分析工具負責定位錯誤來源？ | serverodm => 整機驗收與資料中心運行時，誰隔離設備並追查？
reader_question: AI 硬體算錯卻沒有警報時，工廠、整機驗收與資料中心運行階段要由誰發現、隔離並追查？
reader_starting_point: 無聲錯誤可能在出廠測試、整機驗收或上線運行後才被發現，三個階段的發現與處置責任不同。目前還缺跨平台一致的錯誤分類與隔離門檻。
reader_terms: silent data corruption => 系統沒有報錯，但資料或運算結果已悄悄損壞 | burn-in => 用長時間或高負載提早找出不穩定硬體 | RMA => 故障品退回供應商分析或更換的流程
reader_next_step: 先對齊不同平台如何分類錯誤、何時隔離設備，再確認測試機、伺服器與管理控制器的責任。
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: OCP SDC in AI v1.1 已對齊 benign／corrected／DUE／SDC，Server Component Resilience v1.0 又把 manufacturing、post-manufacturing、test input／output、part history、coverage、repeatability、cost 與 time-to-fail 串成共同契約；Meta、NVIDIA DCGM、Google Research 與 Google Cloud 分別證實機群偵測、主動診斷、應用檢查與主機隔離可執行。反證同樣明確：OCP 說列出的三套框架尚未符合共同格式，DCGM 不決定 RMA，公開資料也沒有共通誤報漏報與隔離門檻。
knowledge_gain: 補出 factory→burn-in→system acceptance→active diagnostics→runtime detection→quarantine／supplier feedback 六站，並將「測試 pass」「主機隔離」「FRU／RMA」「製造改善」拆成不同責任；研究結果只支持邊界文章與圖譜，不支持把測試時間、tester／socket、BMC、ODM 或維修需求外推成 universe 公司營收。
first_rejection: 若不同來源連 SDC 的錯誤分類、偵測覆蓋與隔離門檻都無法對齊，或只能證明單一 operator 的內部軟體實務，便不建立通用設備／測試需求；沒有具名平台 qualification 與本 universe 曝險時，也不外推測試時間或營收。
next_evidence: 取得至少兩個平台的 SDC taxonomy、IST／SLT 覆蓋、誤報漏報與 quarantine 條件，逐層對齊 factory、burn-in、cluster acceptance、runtime 與 RMA；再查 tester、socket、ODM 與 BMC 的具名驗收責任。
next_check: 2026-08-31
route: article_and_graph
article_topic_id: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE
graph_id: ai-hardware-sdc-lifecycle
sources: OCP SDC in AI v1.1 => https://www.opencompute.org/documents/sdc-in-ai-ocp-whitepaper-ver-1-1-final-pdf | OCP Server Component Resilience v1.0 => https://www.opencompute.org/documents/external-ver-1-0-open-compute-specification-server-component-resilience-sdc-workstream-docx-1-pdf-1 | Meta AI hardware reliability => https://engineering.fb.com/2025/07/22/data-infrastructure/how-meta-keeps-its-ai-hardware-reliable/ | NVIDIA DCGM diagnostics => https://docs.nvidia.com/datacenter/dcgm/latest/learn/modules/dcgm-diagnostics.html | Google Cloud report faulty host => https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host | Google Research Spanner SDC => https://research.google/pubs/detection-and-prevention-of-silent-data-corruption-in-an-exabyte-scale-database-system/ | OCP GPU and Accelerator RAS v1.0 => https://www.opencompute.org/documents/ocp-gpu-and-accelerators-ras-requirements-1-0-final-pdf
-->

<!-- research_candidate
candidate_id: RC-224G-PCB-MATERIAL-QUALIFICATION
rank: 5
title: 224G PCB 材料、stackup 與系統 BER 資格鏈
group_ids: pcb
reader_group_questions: pcb => 材料、走線、孔洞與連接器的證據能否在同一塊板上對齊到 BER？
reader_question: 材料規格表宣稱能跑高速後，做成含走線、孔洞與連接器的完整電路板，錯誤率仍能過關嗎？
reader_starting_point: 材料規格、測試片與完整電路板，是三種不同層次的證據；單一材料數字不能直接代表整板表現。目前還缺同一塊參考板從材料到錯誤率的完整資料。
reader_terms: stackup => 電路板各層銅箔、介質與厚度的排列方式 | BER => 位元錯誤率，資料傳輸中出錯的比例 | coupon => 與正式電路板同製程製作、專門用來量測的測試片
reader_next_step: 先取得同一塊參考板的材料、走線損耗與錯誤率資料，避免只拿單一材料數字推論整板表現。
priority: p2
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: IPC 已把 Dk／Df 與成板高頻 loss 列成不同 TM-650 方法，IEEE contribution 又在具名 M7N stackup 上提供 trace 與 via 設計，OIF 則把 ISI loss board、BERT 與 BER measurement 放進同一展示；但兩者沒有對上同一 board identity。配合 IPC 三份 working draft、IEEE P802.3dj D3.2 ballot、OIF current projects 與 plugfest 的未測區域，足以建立「七關不可互相背書」的責任鏈。
knowledge_gain: 把 datasheet、測法、stackup、coupon／不連續點、channel loss budget、BER／FEC、跨廠量產與公司歸因拆成七關；台燿 TU-1300N／E 只新增 IPC-4103/17 QPL 的具名相鄰線，不升格成 224G 系統 qualification 或財務曝險。正式族群路由依 universe 治理修正為 PCB／CCL，不再誤接半導體材料族群。
first_rejection: 若找不到同一塊系統板的 insertion loss、Dk／Df 測法、玻纖效應、銅粗糙度、via／connector 與 BER 對照，或只有材料商單點 coupon 數字，便不能由 224G roadmap 推成 CCL／玻纖／銅箔規格升級、份額或價格。
next_evidence: 取得 IPC 正式版與 test method、系統商 224G reference stackup、multi-source board qualification 及 OIF／IEEE reach 測試；逐項重算 loss budget，並查本 universe 材料與 PCB 公司具名料號、認證及量產足跡。
next_check: 2026-09-15
route: article_and_graph
article_topic_id: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN
graph_id: 224g-pcb-qualification-chain
sources: IPC TM-650 test methods => https://www.ipc.org/test-methods | IPC standards status => https://www.ipc.org/Status | IEEE 224G PCB and COM investigation => https://www.ieee802.org/3/df/public/22_03/mli_3df_01_220316.pdf | OIF CEI-224G OFC 2024 demo => https://www.oiforum.com/wp-content/uploads/OIF_CEI_Demo_OFC2024_Final.pdf | OIF current work => https://www.oiforum.com/technical-work/current-work/ | IEEE P802.3dj ballot announcements => https://www.ieee802.org/3/ballots/announce.html | Ethernet Alliance 2025 HSN plugfest lessons => https://ethernetalliance.org/blog/2026/03/31/from-plugfest-to-progress-key-lessons-from-the-2025-hsn-plugfest/ | Panasonic MEGTRON 9 224 Gbps => https://na.industrial.panasonic.com/whats-new/panasonic-industry-electronic-materials-enabling-224-gbps-revolution-megtron-9 | IPC-4103 Qualified Products List => https://www.ipc.org/ipc-validation-services-qualified-products-list-qpl-ipc-4103 | TUC product portfolio => https://www.tuc.com.tw/products2
-->

<!-- research_candidate
candidate_id: RC-SIC-AI-POWER-QUALIFICATION
rank: 6
title: SiC reliability guideline 到 AI BBU／PSU qualification
group_ids: power,powersupply
reader_group_questions: power => SiC 元件的短路、閘極與熱循環可靠度是否過關？ | powersupply => BBU／PSU 是否引用新指引並改變設計與驗收？
reader_question: 新的碳化矽可靠度指引，是否真的進入 AI 備援電源與電源供應器的驗收並改變設計？
reader_starting_point: 新的碳化矽測試指引、參考設計與單一產品採用案例已經出現，但三者不等於平台驗收規則已改變。目前還缺買方驗收條款與實際測試流程。
reader_terms: SiC => 碳化矽，適合高電壓與高效率電力轉換的半導體材料 | BBU => 電池備援單元，主電源中斷時短暫供電 | PSU => 把輸入電力轉成設備所需電壓的電源供應器 | derating => 刻意低於元件極限使用，以換取可靠度
reader_next_step: 先確認平台驗收是否引用新指引，以及短路、閘極壓力與熱循環測試是否因此改變。
priority: p2
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: JEDEC 2026 JEP203／JEP204 新增 SiC MOSFET 短路評估與可靠度 stress procedures；同週 Infineon 公布 24kW、800V SiC BBU reference design，ROHM 則公布 750V SiC MOSFET 被 AI server BBU 採用。標準、reference design 與產品採用三種證據已同時出現，值得檢查 reliability guideline 是否真正進入 800V AI 電源驗收。
knowledge_gain: 建立從 application stress、JEP device evaluation、supplier data、converter validation、system reliability、mixed-source customer qualification 到財務歸因的七關責任鏈；三份具名 OCP 規格雖已有 short-circuit、derating、DFMEA、MTBF、HALT 與 mixed-source 契約，卻都沒有 JEP203／JEP204／SiC 文字橋，因此事先第一拒絕已觸發，文章只建立可證偽缺口與台達具名研究入口，不建立功率元件受惠或財務線。
first_rejection: 若 JEP203／JEP204 沒有被平台 qualification 引用，短路與 gate-oxide stress 也未改變系統保護、derating 或壽命驗收，便只是一組元件級指引；單一採用與 reference design 不代表普遍滲透或台廠收入。
next_evidence: 取得 JEP203／JEP204 正文、BBU／PSU 客戶 qualification 與 failure criteria，對齊短路耐受、gate stress、熱循環、保護協同與壽命模型；再查本 universe 功率元件與電源公司具名設計、認證和財務足跡。
next_check: 2026-09-15
route: article_and_graph
article_topic_id: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION
graph_id: sic-ai-power-qualification
sources: JEDEC standards organization => https://www.jedec.org/ | JEDEC SiC guideline release => https://www.businesswire.com/news/home/20260603176123/en/JEDEC-Releases-New-SiC-Guidelines-to-Improve-Reliability-and-Evaluation-in-Power-Electronics | OCP Diablo 400 v0.7.0 => https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf | OCP Open Rack V3 HPR V2 12kW PSU => https://www.opencompute.org/documents/open-rack-v3-hpr-v2-12kw-psu-module-spec-v1-0-0-pdf | OCP Open Rack V3 48V BBU Rev1.4 => https://www.opencompute.org/documents/open-rack-v3-bbu-module-spec-1-4-pdf | Infineon 24kW 800V SiC BBU reference design => https://www.infineon.com/technology-news/2026/infpss202606-093 | ROHM 750V SiC MOSFET AI server BBU adoption => https://www.rohm.com/news-detail?defaultGroupId=false&news-title=2026-06-03_news_sic-mosfet | Delta 2025 chairman statement => https://www.deltaww.com/en-US/investors/chairman-statement
-->

<!-- research_candidate
candidate_id: RC-SEMICONDUCTOR-PFAS-EXPOSURE
rank: 7
title: 半導體 PFAS 的 substance×process×jurisdiction 曝險
group_ids: material,semiequip
reader_group_questions: material => 哪種 PFAS 用在哪道製程，替代材料是否需要重驗？ | semiequip => 設備是否依賴受限物質，替代後需改哪些製程條件？
reader_question: 哪一種 PFAS 用在哪一道半導體製程、受哪個地區規則約束，限制後是否必須重新驗證材料或設備？
reader_starting_point: PFAS 是一大類物質，不同物質、製程用途與地區規則可能完全不同。目前還不能從「限制 PFAS」直接推成全面換料或設備改造。
reader_terms: PFAS => 一大類耐熱、耐化學的含氟物質，部分用途正面臨限制 | jurisdiction => 法規實際適用的國家或地區 | qualification => 替代材料或設備正式導入前的合格驗證
reader_next_step: 先把特定物質、製程用途與適用法域逐項對上，再查豁免、過渡期與替代品驗證成本。
priority: p2
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: ECHA 2026 已讓 PFAS 限制案進入 RAC 最終意見與 SEAC 意見草案階段，SEMI 同時明列半導體製造中的關鍵 PFAS 用途，EPA reporting rule 另形成美國使用資料時鐘；這是一個有明確政策節點、但必須做到 substance×process×jurisdiction 的材料與設備供應鏈題目。
knowledge_gain: 建立 substance identity→process function→product form→jurisdiction duty→derogation／transition→change qualification→company／financial attribution 七關；上品的氟聚合物產品與三福化的含氟界面活性劑研發只升為具名搜尋入口。最終條文、特定物質到場址／產品的適用性與財務仍未閉合，因此事先第一拒絕已觸發，不建立近期成本、供應中斷或替代受惠主張。
first_rejection: 若最終限制對關鍵半導體用途給予足夠長或廣泛豁免，替代材料不需重新 qualification，或無法把任何特定物質與台灣公司／廠區／產品連上，就不建立近期成本、供應中斷或受惠替代材料主張。
next_evidence: 取得 ECHA 最終限制條文、derogation 與 transition period，將 PFAS 物質逐一對應 lithography、etch、deposition、wet clean、設備密封與冷媒用途；再核對公司化學品清單、廠區法域、替代品 qualification 與成本揭露。
next_check: 2026-12-15
route: article_and_graph
article_topic_id: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE
graph_id: semiconductor-pfas-exposure
sources: ECHA targeted derogations update => https://echa.europa.eu/-/echa-supports-pfas-restriction-with-targeted-derogations | ECHA consultation outcome => https://poisoncentres.echa.europa.eu/documents/d/guest/news_seac_pfas_cons_stats | ECHA semiconductor use mapping => https://euon.echa.europa.eu/documents/d/guest/pfas_use-mapping_annex_to_guidance_for_respondents_en?t=1765893415372 | ECHA updated restriction proposal => https://echa.europa.eu/-/echa-publishes-updated-pfas-restriction-proposal | European Commission Chemicals Industry Action Plan => https://single-market-economy.ec.europa.eu/document/download/e5006955-dd1c-45bc-8b7a-cfda71c67abf_en?filename=COM_2025_530_1_EN_ACT_part1_v6.pdf | EPA TSCA PFAS reporting rule => https://www.epa.gov/assessing-and-managing-chemicals-under-tsca/tsca-section-8a7-reporting-and-recordkeeping | EPA 2026 reporting deadline update => https://www.epa.gov/chemicals-under-tsca/update-reporting-deadline-tsca-pfas-reporting-rule | SEMI PFAS explainer => https://www.semi.org/en/EHS_PFAS_Explainer | SIA PAG qualification case => https://www.semiconductors.org/wp-content/uploads/2023/06/FINAL-PAG-Case-Study.pdf | SIA semiconductor PFAS background => https://www.semiconductors.org/wp-content/uploads/2023/05/FINAL-PFAS-Consortium-Background-Paper.pdf | 上品 2025 年年報 => https://doc.twse.com.tw/server-java/t57sb01?step=1&colorchg=1&co_id=4770&year=115&mtype=F | 上品氟素樹脂內襯設備 => https://www.alliedsupreme.com/tw/product/product_1-7/product_view-sheet_lining | 三福化 2025 年年報 => https://doc.twse.com.tw/server-java/t57sb01?step=1&colorchg=1&co_id=4755&year=115&mtype=F | 三福化產品與投資人資訊 => https://www.sfchem.com.tw/zh-hant/
-->

<!-- research_candidate
candidate_id: RC-TWO-PHASE-COOLING-QUALIFICATION
rank: 8
title: 兩相冷卻 qualification 與單相反證
group_ids: thermal
reader_group_questions: thermal => 在相同熱負載下，兩相冷卻何時才優於單相方案？
reader_question: 當單相冷板仍能帶走熱量時，熱負載要高到什麼程度，兩相冷卻才真的有必要？
reader_starting_point: 兩相冷卻已有工程文件，但單相冷板也持續提高散熱能力。目前還缺相同負載下的直接比較與平台正式驗收。
reader_terms: 單相冷卻 => 冷卻液全程維持液態帶走熱量 | 兩相冷卻 => 冷媒利用液態與氣態轉換吸收更多熱量 | thermal resistance => 熱從晶片傳到冷卻液時遇到的阻力 | serviceability => 系統是否容易維修、更換與恢復運作
reader_next_step: 先在相同熱負載下比較單相與兩相的散熱、壓力、耗能、安全和維修，再等待平台正式驗收。
priority: p3
knowledge_value: high
status: deferred
evidence_posture: preliminary
why_now: OCP 2026 已發布 pumped two-phase refrigerant direct-to-chip 文件並舉辦 pool-boiling 教育活動，顯示兩相路徑進入可定義的工程討論；但 CoolIT 同期宣稱單相冷板已達 15kW 且可延伸至 2030 年後，反方證據足以阻止把兩相冷卻當成必然遷移。
knowledge_gain: 保留同負載下單相與兩相的 thermal resistance、pumping、pressure、冷媒、安全與維修比較題，但在 operator qualification 與部署分母出現前不新增散熱族群文章。
first_rejection: 若單相冷板在目標 accelerator 的熱通量、壓降、可靠度與總持有成本內仍可滿足 roadmap，或兩相系統缺少 operator qualification、維修、冷媒與 leak／pressure 安全準則，就不建立兩相滲透率或散熱供應商勝負。
next_evidence: 取得同一熱負載與封裝條件下的單相／兩相 case-to-fluid thermal resistance、pumping、pressure、refrigerant、serviceability 與壽命比較，並等待 operator 級 qualification、部署分母和可定位的台灣供應鏈證據。
next_check: 2026-10-15
route: watch_only
sources: OCP two-phase pool boiling webinar => https://www.opencompute.org/events/past-events/ocp-educational-webinar-two-phase-pool-boiling-the-foundation-for-scalable-ai-infrastructure | OCP Cold Plate Cooling Loop Requirements => https://www.opencompute.org/documents/cold-plate-cooling-loop-requirements-rev-2-pdf | CoolIT 15kW single-phase cold plate => https://www.coolitsystems.com/resources/news/15kw_press_release/ | OCP Cold Plate workstream => https://www.opencompute.org/wiki/Cooling_Environments/Cold_Plate
-->

## 本輪方法結果

- 研究前凍結八題；前七題完成 research-grade article＋graph，第八題維持 deferred。第三至第七題都保留 frozen watch 的初始決策，升格結果另記為 promoted-from-watch，不改寫研究前排名、第一拒絕或下一份證據。
- 兩篇新增文章直接補 passive 與 memory 的具名公司橋，但 2327、8299 都只畫成 inference／capability；qualification、訂單、收入與毛利仍是未證實主張。
- 224G 題新增台燿 IPC-4103/17 QPL 的具名相鄰線，但同板材料到 BER 與財務仍未證實；CCL、玻纖與銅箔依 universe 治理都屬 pcb，正式路由不再誤接 material 半導體材料族群。
- SiC qualification 題把 JEDEC 元件方法與三份 OCP system contract 分開；三份文件的 JEP203／JEP204／SiC exact-token census 都是 0，觸發 first rejection。台達只升為 planned／capability 具名入口，沒有 JEP-qualified、量產 BBU／PSU 或財務線。
- PFAS 題把 EU 限制程序、美國歷史申報、半導體多用途與替代 qualification 分成七關；上品與三福化只補上 material 的具名產品／能力入口。最終條文與 substance×site×product×financial 鏈仍缺，事先第一拒絕對近期成本、中斷與受惠主張已觸發；semiequip 仍沒有具名公司橋。
- 其餘題目保留明示 first rejection 與 next evidence，不因雷達換輪而消耗或重排。
