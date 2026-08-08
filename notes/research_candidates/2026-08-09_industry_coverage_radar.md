# 2026-08-09 族群覆蓋補強研究雷達

本輪從 11 個正式族群的文章、圖譜與具名公司邊覆蓋出發廣搜，不以熱門度或固定篇數選題。
八題排名在深研前凍結於 RS-2026-08-09-01；前兩題通過 article＋graph 契約，其餘保留原
watch／defer 決策。升格只表示可形成可證偽責任鏈，不代表訂單、營收、毛利或投資建議。

<!-- research_radar
schema_version: 2
radar_id: RADAR-2026-08-09-01
as_of: 2026-08-09
next_review: 2026-08-16
status: active
method: 先以 universe 族群規模 研究文章路由 知識圖譜及具名公司邊做覆蓋盤點，再廣搜 operator 標準組織 監管機關與公司一手來源；依可證偽性 至少兩條獨立一手鏈 能否補現有知識缺口 公司映射風險及後續維護成本排序。候選先寫入 append-only selection log 並獨立 commit；深研後只更新 evidence posture route 與結果，不改凍結排名 第一拒絕與下一份證據
selection_cycle_id: RS-2026-08-09-01
-->

<!-- research_candidate
candidate_id: RC-AI-RACK-EMC-CERTIFICATION
rank: 1
title: AI 機櫃 EMC 測試容量與驗收責任階梯
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
priority: p1
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: OCP FCSA 1.0 把 chiplet 系統分割與介面置於 UCIe 連結之上，Open Chiplet Economy 又推進 CDXML、3DK／MDK 與 test kit；Arm 的獨立 FCSA 說明亦強調架構中立與多供應商重用。這可檢驗真正瓶頸是否從 die-to-die PHY 轉向可機讀的 thermal、power、SI／PI、mechanical、test 與 security model 交換。
knowledge_gain: 若證據成熟，可把既有 UCIe 互通圖從 PHY／實體展示推進到多供應商設計資料交換、tool import 與 test-kit conformance，並分開 EDA、IP、foundry 與 OSAT 責任。
first_rejection: 若 FCSA、CDXML、JEP30 與 3DK／MDK 無法落成同一套多供應商設計交換或 conformance workflow，或沒有 tape-out／foundry／OSAT 實作，就只是重疊規格清單，不建立 EDA、矽智財、封裝或測試價值鏈。
next_evidence: 取得 FCSA conformance／implementation 資料、CDXML 與 JEP30 欄位對照、3DK／MDK／test kit 的實際工具匯入與多供應商案例；再查 foundry、OSAT、EDA 與本 universe 公司是否有具名採用。
next_check: 2026-09-15
route: watch_only
sources: OCP FCSA 1.0 specification => https://www.opencompute.org/documents/fcsa-1-0-0-pdf | OCP FCSA workstream => https://www.opencompute.org/wiki/Server/OCE/FCSA | OCP Open Chiplet Economy => https://www.opencompute.org/community/open-chiplet-economy | OCP FCSA introduction => https://www.opencompute.org/blog/building-the-foundation-for-an-open-chiplet-future-foundation-chiplet-system-architecture-fcsa
-->

<!-- research_candidate
candidate_id: RC-AI-SILENT-DATA-CORRUPTION
rank: 4
title: AI 硬體 silent data corruption 的跨生命週期責任鏈
priority: p1
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: Meta 已公開從工廠到機群的 AI 硬體可靠度與 silent data corruption 偵測流程，OCP Hyperscale CPU RAS／Debug 規格及 NVIDIA in-system test／DCGM 文件則提供平台需求與可執行健康檢查入口；足以研究 test insertion、telemetry、隔離、重測與供應商回饋是否形成跨生命週期閉環。
knowledge_gain: 若跨平台 taxonomy 與門檻能對齊，可補 packtest 與 serverodm 現有題材缺少的 factory→burn-in→cluster acceptance→runtime→RMA 閉環，而不先把檢測次數換成設備營收。
first_rejection: 若不同來源連 SDC 的錯誤分類、偵測覆蓋與隔離門檻都無法對齊，或只能證明單一 operator 的內部軟體實務，便不建立通用設備／測試需求；沒有具名平台 qualification 與本 universe 曝險時，也不外推測試時間或營收。
next_evidence: 取得至少兩個平台的 SDC taxonomy、IST／SLT 覆蓋、誤報漏報與 quarantine 條件，逐層對齊 factory、burn-in、cluster acceptance、runtime 與 RMA；再查 tester、socket、ODM 與 BMC 的具名驗收責任。
next_check: 2026-09-15
route: watch_only
sources: Meta AI hardware reliability => https://engineering.fb.com/2025/07/22/data-infrastructure/how-meta-keeps-its-ai-hardware-reliable/ | OCP Hyperscale CPU RAS and Debug Requirements => https://www.opencompute.org/documents/hyperscale-cpu-ras-and-debug-requirements-specification-v0-7-09-29-2025-pdf | NVIDIA DCGM diagnostics overview => https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/diag-overview.html
-->

<!-- research_candidate
candidate_id: RC-224G-PCB-MATERIAL-QUALIFICATION
rank: 5
title: 224G PCB 材料、stackup 與系統 BER 資格鏈
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: IPC 的在製 IPC-4103C、IPC-4414 與 IPC-4562C 分別碰觸高速基材、超低介電玻纖與銅箔，IPC-4103 QPL 已有台灣材料商；Panasonic 同時以 224Gbps 材料路線與擴產回應 AI server 需求，OIF 則已展示 224G／448G interoperability。這可把材料 datasheet、標準測法、板級 stackup 與系統 BER 分開驗證。
knowledge_gain: 若能以同一 reference stackup 重算 loss budget，可把 material 與 PCB 族群從 datasheet 規格推進到 coupon、via／connector、reach 與 BER 的系統資格鏈。
first_rejection: 若找不到同一塊系統板的 insertion loss、Dk／Df 測法、玻纖效應、銅粗糙度、via／connector 與 BER 對照，或只有材料商單點 coupon 數字，便不能由 224G roadmap 推成 CCL／玻纖／銅箔規格升級、份額或價格。
next_evidence: 取得 IPC 正式版與 test method、系統商 224G reference stackup、multi-source board qualification 及 OIF／IEEE reach 測試；逐項重算 loss budget，並查本 universe 材料與 PCB 公司具名料號、認證及量產足跡。
next_check: 2026-09-15
route: watch_only
sources: IPC standards status => https://www.ipc.org/Status | IPC-4103 Qualified Products List => https://www.ipc.org/ipc-validation-services-qualified-products-list-qpl-ipc-4103 | Panasonic circuit board materials => https://industrial.panasonic.com/sa/electronic-materials/products/cbm | OIF OFC 2026 interoperability => https://www.oiforum.com/oif-demonstrates-industry-wide-interoperability-at-scale-at-ofc-2026-advancing-energy-efficiency-performance-and-capacity-for-ai-era-data-center-networks/
-->

<!-- research_candidate
candidate_id: RC-SIC-AI-POWER-QUALIFICATION
rank: 6
title: SiC reliability guideline 到 AI BBU／PSU qualification
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: JEDEC 2026 JEP203／JEP204 新增 SiC MOSFET 短路評估與可靠度 stress procedures；同週 Infineon 公布 24kW、800V SiC BBU reference design，ROHM 則公布 750V SiC MOSFET 被 AI server BBU 採用。標準、reference design 與產品採用三種證據已同時出現，值得檢查 reliability guideline 是否真正進入 800V AI 電源驗收。
knowledge_gain: 若平台 qualification 明示引用 JEP203／JEP204，可把 power 與 powersupply 的 800V 架構圖補上元件 stress、保護協同、derating 與壽命驗收，而不是只看 reference design。
first_rejection: 若 JEP203／JEP204 沒有被平台 qualification 引用，短路與 gate-oxide stress 也未改變系統保護、derating 或壽命驗收，便只是一組元件級指引；單一採用與 reference design 不代表普遍滲透或台廠收入。
next_evidence: 取得 JEP203／JEP204 正文、BBU／PSU 客戶 qualification 與 failure criteria，對齊短路耐受、gate stress、熱循環、保護協同與壽命模型；再查本 universe 功率元件與電源公司具名設計、認證和財務足跡。
next_check: 2026-09-15
route: watch_only
sources: JEDEC standards organization => https://www.jedec.org/ | JEDEC SiC guideline release => https://www.businesswire.com/news/home/20260603176123/en/JEDEC-Releases-New-SiC-Guidelines-to-Improve-Reliability-and-Evaluation-in-Power-Electronics | Infineon 24kW 800V SiC BBU reference design => https://www.infineon.com/technology-news/2026/infpss202606-093 | ROHM 750V SiC MOSFET AI server BBU adoption => https://www.rohm.com/news-detail?defaultGroupId=false&news-title=2026-06-03_news_sic-mosfet
-->

<!-- research_candidate
candidate_id: RC-SEMICONDUCTOR-PFAS-EXPOSURE
rank: 7
title: 半導體 PFAS 的 substance×process×jurisdiction 曝險
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: ECHA 2026 已讓 PFAS 限制案進入 RAC 最終意見與 SEAC 意見草案階段，SEMI 同時明列半導體製造中的關鍵 PFAS 用途，EPA reporting rule 另形成美國使用資料時鐘；這是一個有明確政策節點、但必須做到 substance×process×jurisdiction 的材料與設備供應鏈題目。
knowledge_gain: 若最終條文與公司化學品足跡可定位，可補 material、semiequip 的法規時鐘與重新 qualification 路徑；在此之前不使用「PFAS 概念」推成本或替代材料受惠。
first_rejection: 若最終限制對關鍵半導體用途給予足夠長或廣泛豁免，替代材料不需重新 qualification，或無法把任何特定物質與台灣公司／廠區／產品連上，就不建立近期成本、供應中斷或受惠替代材料主張。
next_evidence: 取得 ECHA 最終限制條文、derogation 與 transition period，將 PFAS 物質逐一對應 lithography、etch、deposition、wet clean、設備密封與冷媒用途；再核對公司化學品清單、廠區法域、替代品 qualification 與成本揭露。
next_check: 2026-12-15
route: watch_only
sources: ECHA PFAS topic => https://echa.europa.eu/hot-topics/perfluoroalkyl-chemicals-pfas | ECHA targeted derogations update => https://echa.europa.eu/-/echa-supports-pfas-restriction-with-targeted-derogations | ECHA restriction registry => https://echa.europa.eu/registry-of-restriction-intentions/-/dislist/details/0b0236e18663449b?_disslists_WAR_disslistsportlet_businessIdentifier=0b0236e18663449b | SEMI PFAS explainer => https://www.semi.org/en/EHS_PFAS_Explainer | SEMI manufacturing markets overview => https://www.semi.org/en/ehs_PFAS/mfg_markets_overview
-->

<!-- research_candidate
candidate_id: RC-TWO-PHASE-COOLING-QUALIFICATION
rank: 8
title: 兩相冷卻 qualification 與單相反證
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

- 研究前凍結八題；前兩題由 preliminary 升到 research-grade article＋graph，第三至第七題維持 watch，第八題維持 deferred，沒有為了平均篇數而把薄證據升格。
- 兩篇新增文章直接補 passive 與 memory 的具名公司橋，但 2327、8299 都只畫成 inference／capability；qualification、訂單、收入與毛利仍是未證實主張。
- material 仍沒有具名公司橋，因此 224G 材料資格鏈保留 P2；先取得 reference stackup、標準測法與本 universe 具名料號，再決定擴充文章或圖譜。
- 其餘題目以明示 first rejection 與 next evidence 續追，不因雷達換輪而消耗或重排。
