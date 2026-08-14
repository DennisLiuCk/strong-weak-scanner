# 同樣叫混合接合，成熟度可以差很多：先分應用世代，再看五個製程窗口

<!-- research_topic
topic_id: MI-2026-08-02-HYBRID-BONDING-READINESS
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-05-28
last_reviewed_at: 2026-08-12
review_due: 2026-08-19
source_type: mixed
publisher: imec
publisher_domain: imec-int.com
canonical_url: https://www.imec-int.com/en/press/imec-and-ev-group-demonstrate-wafer-wafer-hybrid-bonding-200nm-interconnect-pitch-and-record
source_chain_id: hybrid-bonding-pdk-test-vehicle-tool-20260802
stock_ids:
group_ids: packtest,semiequip,material
trigger_type: advanced_packaging_readiness_update
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C8
base_confidence: medium
confidence_basis: Sony、TSMC 與 AMD 一手資料證明特定影像感測器、N7 SoIC 與 3D V-Cache 路徑已有應用、產品或 production 證據；imec 的 200nm W2W 試驗車、NanoIC D2W pathfinding PDK 與 Applied／Besi 工具則仍停在另一組較早關卡，因此成熟度必須按應用、接法、介面世代與產品逐格判定；各格 HVM 良率、throughput、成本及台灣公司財務映射仍未公開
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: primary_hybrid_bonding_readiness_sources_captured
evidence: source_chain:hybrid-bonding-pdk-test-vehicle-tool-20260802
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_pathfinding_test_vehicle_customer_tool_use_and_hvm_evidence
evidence: sources:S1,S2,S3
-->
<!-- transition
date: 2026-08-08
from: triaged
to: triaged
reason: editorial_glossary_for_repeated_terms_no_conclusion_change
evidence: editorial:readability
-->

<!-- research_source
source_id: S1
role: other_primary
source_kind: document
publisher: imec NanoIC
title: NanoIC opens access to fine-pitch RDL and D2W hybrid bonding interconnect PDKs
published_at: 2026-03-02
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.imec-int.com/en/press/nanoic-opens-access-first-ever-fine-pitch-rdl-and-d2w-hybrid-bonding-interconnect-pdks
locator: exploratory／pathfinding PDK、design rules、validated building blocks 與 future fabrication-ready tape-out 段落
limitation: 這是 pilot line 的 early-access pathfinding PDK；尚未具備完整 tape-out 能力，也不證明客戶量產、良率、throughput 或供應商收入
independence_group: imec
-->

<!-- research_source
source_id: S2
role: other_primary
source_kind: document
publisher: imec and EV Group
title: Wafer-to-wafer hybrid bonding with 200nm interconnect pitch and record overlay accuracy
published_at: 2026-05-28
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.imec-int.com/en/press/imec-and-ev-group-demonstrate-wafer-wafer-hybrid-bonding-200nm-interconnect-pitch-and-record
locator: 200nm Cu pad pitch test vehicle、sub-40nm post-bond overlay、full 300mm wafer 與 CMP／SiCN／pre-bond correction 段落
limitation: 結果來自 imec 試驗車與合作設備；robust、highly yielding 與 world first 是發布者措辭，未提供量產客戶、good-die yield、產能或成本
independence_group: imec-evg-joint
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: Applied Materials
title: Applied Materials unveils Kinex integrated die-to-wafer hybrid bonding system
published_at: 2025-10-07
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://investors.appliedmaterials.com/node/28506/pdf
locator: PDF page 1 lines 17–31；Kinex integration、inline metrology 與 multiple logic／memory／OSAT customers
limitation: 公司稱設備被多家客戶使用，但未揭露客戶名稱、qualification 階段、出貨量、良率、throughput、收入或終端產品
independence_group: applied-materials-besi
-->

<!-- research_source
source_id: S4
role: other_primary
source_kind: living_index
publisher: imec
title: imec 3D integration research and press updates
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.imec-int.com/en/expertise/cmos-advanced/3d-integration
locator: 2026-08-02 建立的 hybrid bonding、W2W／D2W 與後續試驗結果重查入口
limitation: living index 只用來偵測新文件；頁面敘述本身不會自動升級量產或公司財務狀態
independence_group: imec
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: living_index
publisher: Applied Materials
title: Applied Materials investor news releases
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.appliedmaterials.com/news-releases
locator: 2026-08-02 建立的 Kinex、hybrid bonding、customer qualification 與 advanced packaging 財務更新入口
limitation: 新聞索引只用來找後續文件；產品行銷、合作或市場預測不能代替客戶 qualification 與財務證據
independence_group: applied-materials
-->

<!-- research_source
source_id: S6
role: company_release
source_kind: document
publisher: Sony Group
title: 3D Stacking Process Technologies for Advanced CMOS Image Sensors
published_at: 2024-04-22
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.sony.com/en/SonyInfo/technology/publications/3d-stacking-process-technologies-for-advanced-cmos-image-sensors/
locator: VLSI TSA 2024 abstract；2015 Cu-Cu hybrid bonding、stacked BI-CIS、2019 InGaAs／Si、2020 edge-AI logic 與 2023 large-chip CoW 段落
limitation: 公司技術回顧可證明應用與製程世代不是從 2026 試驗才開始，但未公開各代量產流程、出貨量、good-product yield、throughput、成本或供應商份額；2023 large-chip CoW 仍只是 announced process
independence_group: sony
-->

<!-- research_source
source_id: S7
role: company_release
source_kind: document
publisher: TSMC
title: TSMC FINFLEX N2 Process Innovations Debut at 2022 North American Technology Symposium
published_at: 2022-06-17
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://pr.tsmc.com/english/news/2939
locator: 3DFabric 3D Silicon Stacking Solutions 段落；SoIC-based CPU CoW、IPU WoW、N7 chips already in production 與 N5 support schedule
limitation: 公司公告可證明 N7 CoW／WoW production 與兩種具名應用，但沒有逐產品良率、throughput、成本、產能利用、客戶採購量或 SoIC 財務分子；不同節點與後續細間距路徑不能沿用同一成熟度
independence_group: tsmc
-->

<!-- research_source
source_id: S8
role: company_release
source_kind: document
publisher: AMD
title: Leadership Performance for Technical Computing Workloads
published_at: 2022-03-21
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.amd.com/ko/solutions/data-center/insights/leadership-performance-for-technical-computing-workloads.html
locator: EPYC 7003 with 3D V-Cache product launch 與 Under the Hood 的 copper-to-copper hybrid bonding bumpless design 段落
limitation: 可把具名商用處理器與 Cu-Cu hybrid bonding 對上，但效能、互連密度與效率是 AMD 公司主張；未揭露接合良率、throughput、成本、供應商設備材料或產品收入拆分
independence_group: amd
-->

<!-- research_source
source_id: S9
role: company_release
source_kind: living_index
publisher: TSMC
title: TSMC-SoIC platform and current technology status
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/SoIC.htm
locator: 2026-08-12 建立的 CoW／WoW、known-good-die、bond pitch 與後續 node production 狀態重查入口
limitation: 活頁只用來偵測新一代 SoIC 節點、產品與 production 更新；頁面行銷敘述不能替代逐產品良率、throughput、成本或客戶與供應商財務雙向核對
independence_group: tsmc
-->

<!-- research_source
source_id: S10
role: company_release
source_kind: document
publisher: EV Group
title: EV Group Achieves Breakthrough in Hybrid Bonding Overlay Control for Chiplet Integration
published_at: 2025-09-08
captured_at: 2026-08-13
accepted_at: 2026-08-13
status: active
url: https://www.evgroup.com/company/news/detail/ev-group-achieves-breakthrough-in-hybrid-bonding-overlay-control-for-chiplet-integration
locator: EVG40 D2W 的 300mm wafer 全 die overlay measurement、最高 2,800 measurement points／four minutes、customer-site installation 與 HVM production services 段落
limitation: EVG 產品發布只證明量測覆蓋、設備規格與未具名客戶服務使用；100% 是被量到的 die 覆蓋率，不是位置全數合格、無空洞、電性或最終產品良率，也沒有客戶、產品、批次或財務分母
independence_group: ev-group
-->

<!-- research_source
source_id: S11
role: company_release
source_kind: document
publisher: EV Group
title: EV Group Achieves Die-to-Wafer Fusion and Hybrid Bonding Milestone with 100-Percent Die Transfer Yield on Multi-Die 3D System-On-A-Chip
published_at: 2022-07-12
captured_at: 2026-08-13
accepted_at: 2026-08-13
status: active
url: https://www.evgroup.com/company/news/detail/ev-group-achieves-die-to-wafer-fusion-and-hybrid-bonding-milestone-with-100-percent-die-transfer-yield-on-multi-die-3d-system-on-a-chip/
locator: HICC 單次 transfer process 的 multiple different-size dies、complete 3D SoC 與 100-percent void-free bonding yield 段落
limitation: 這是 EVG 開發中心示範；正文的 100% 指指定轉移中的 void-free interface，沒有公開 die 數、電性合格產品、重複 lot、可靠度、throughput、成本或客戶量產
independence_group: ev-group
-->

<!-- research_source
source_id: S12
role: other_primary
source_kind: document
publisher: imec
title: Imec demonstrates die-to-wafer hybrid bonding with a Cu interconnect pad pitch of 2µm
published_at: 2024-05-29
captured_at: 2026-08-13
accepted_at: 2026-08-13
status: active
url: https://www.imec-int.com/en/press/imec-demonstrates-die-wafer-hybrid-bonding-cu-interconnect-pad-pitch-2mm
locator: 2µm D2W test vehicle、<350nm overlay、Kelvin e-yield >85% 與 daisy-chain e-yield >70% 段落
limitation: 這是 imec 試驗載具；兩種 e-yield 的受測結構不同，發布頁未提供結構數、chain 長度、die／wafer／lot 數、變異或最終產品良率，不能和其他百分比直接排名
independence_group: imec
-->

<!-- research_source
source_id: S13
role: other_primary
source_kind: document
publisher: imec
title: Wafer-to-wafer hybrid bonding: pushing the boundaries to 400nm interconnect pitch
published_at: 2024-02-19
captured_at: 2026-08-13
accepted_at: 2026-08-13
status: active
url: https://www.imec-int.com/en/articles/wafer-wafer-hybrid-bonding-pushing-boundaries-400nm-interconnect-pitch
locator: 400nm W2W 的 CMP／void-free 條件、<150nm overlay、low single-contact resistance，以及 overlay 與 dielectric breakdown／yield 關聯段落
limitation: 這是 imec 研究試驗的特定 400nm pad design；<100nm overlay 需求是該設計對 sufficient HVM yield 的研究結論，不能外推所有 pitch、產品、設備或宣稱已完成客戶 HVM
independence_group: imec
-->

<!-- research_source
source_id: S14
role: other_primary
source_kind: document
publisher: IEEE.tv
title: Reducing Wafer-to-Wafer Bonding Misalignment to Enable sub 150nm Pitch Hybrid Bonding
published_at: 2026-01-22
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://ieeetv.ieee.org/hbs/reducing-wafer-to-wafer-bonding-misalignment-to-enable-sub-150nm-pitch-hybrid-bonding
locator: 2026 IEEE Hybrid Bonding Symposium 的 TEL Technology Center America 技術簡報摘要；140nm W2W test vehicle、hybrid-bond residual misalignment <50nm，以及移除 bond-pad layout 影響的三片 fusion-bond wafer 中 99.5% points residual <40nm 段落
limitation: IEEE.tv 頁面只公開講者摘要，完整影片／下載需會員；140nm 是 TEL 試驗載具，不是具名客戶產品。三片 wafer 的 <40nm 診斷刻意移除 bond-pad layout，不能冒充同一 140nm hybrid-bond electrical yield、產品良率或量產分布；講者對未來需求的敘述不作需求預測
independence_group: tokyo-electron
-->

<!-- research_source
source_id: S15
role: other_primary
source_kind: document
publisher: IBM Research
title: Electrical Performance of Hybrid Bonding with Sub-Micron Cu-Cu Bonding Contacts: Effects of Scaling, Microstructure, and Surface Morphology
published_at: 2025-05-27
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://research.ibm.com/publications/electrical-performance-of-hybrid-bonding-with-sub-micron-cu-cu-bonding-contacts-effects-of-scaling-microstructure-and-surface-morphology
locator: ECTC 2025 conference-paper abstract；以 Kelvin four-point structures 比較 pad size／pitch scaling，並報告縮小時初始電阻及其 spread 上升、bonding yield 下降，以及高溫測試後電阻與 yield 的方向性變化
limitation: 公開頁只有摘要，沒有各 pad size／pitch 的數值、結構數、die／wafer／lot 分母、完整分布、門檻或最終產品；高溫與 current stressing 的變化是指定試驗結構結果，不能外推為 field aging、HVM 良率或產品可靠度
independence_group: ibm-research
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: imec NanoIC 於 2026-03-02 公開的 fine-pitch RDL 與 D2W hybrid bonding PDK 是 early-access exploratory／pathfinding 版本，完整 fabrication-ready tape-out 能力仍被列為後續成熟方向
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-03-02
basis: S1 直接區分 first release、pathfinding PDK 與未來 complete fabrication-ready toolset
boundary: PDK 開放不等於實體產品已 tape-out、客戶量產、製程良率或設備材料需求已形成收入
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: imec 與 EVG 在 300mm wafer 試驗車上展示 200nm Cu interconnect pad pitch，並報告所有 die 的 post-bond overlay vector 低於 40nm
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-05-28
basis: S2 明列 test vehicle、200nm pad pitch、300mm wafer 與 100% dies 的 sub-40nm overlay result
boundary: 這是合作研發試驗車的量測結果，不是具名客戶產品的 HVM yield、產能、成本或可靠度資料
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: Applied Materials 表示 Kinex 整合 D2W hybrid bonding 關鍵流程與 inline metrology，並已被多家 leading-edge logic、memory 與 OSAT 客戶使用
supporting_source_ids: S3
contrary_source_ids:
as_of: 2025-10-07
basis: S3 PDF page 1 直接列出 integrated process steps、overlay measurement 與 multiple customer categories
boundary: used by multiple customers 沒有揭露客戶、qualification、量產產品、出貨量、收入或高量產良率，不能自動解讀為 HVM adoption
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C4
label: inference
status: superseded
claim: Hybrid bonding 已同時跨入設計規則、細間距試驗車與整合設備客戶使用三個節點，但現有公開證據仍不足以把整條技術路徑判定為具名產品的高量產成熟
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-08-02
basis: S1 明示 pathfinding 而非 tape-out-ready，S2 是可路由試驗車，S3 只到未具名客戶使用；三者能建立成熟度階梯但沒有完成 HVM 的共同分母
boundary: 不推估 hybrid bonding TAM、量產良率、設備份額、台灣公司訂單或股價；不同 D2W／W2W 用例也不能用單一節距直接比較
verification_needed:
corrected_by_claim_id: C8
resolution: Sony、TSMC 與 AMD 的較早一手資料證明部分應用與產品路徑已到商用或 production；原句把不同應用、接法與介面世代放進同一條成熟度階梯，改由 C8 的四維矩陣取代
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: Universe 內封測、設備或材料公司已因上述 200nm W2W／D2W hybrid bonding 路徑取得可辨識量產訂單、收入或獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: 現有來源只涵蓋 imec／EVG 試驗線與 Applied Materials／Besi 整合設備，沒有台灣公司與客戶對同一製程步驟的雙向核對
boundary: 不以先進封裝能力、一般 CMP／清洗／檢查產品或 OSAT 身分建立公司受惠線
verification_needed: 晶圓廠或 OSAT 的具名產品 qualification，搭配台灣公司料號、製程步驟、量產出貨及財務貢獻
resolution:
-->

<!-- research_claim
claim_id: C6
label: verified
status: active
claim: Sony 的 2024 官方技術回顧把 Cu-Cu hybrid bonding 追溯到 2015 年的 stacked back-illuminated CMOS image sensor，並列出 2019 年異質材料影像感測器、2020 年 edge-AI logic 與後續多層堆疊演進
supporting_source_ids: S6
contrary_source_ids:
as_of: 2024-04-22
basis: S6 直接命名 Cu-Cu hybrid bonding、stacked BI-CIS 與各應用年份，證明「混合接合」並非到 2026 細間距試驗才出現的單一路徑
boundary: 只證明 Sony 公開的技術與應用演進；不補推各代 W2W／D2W 流程、良率、產量、成本、供應商或 2023 large-chip CoW 已進量產
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: TSMC 於 2022-06-17 表示 N7 SoIC 的 CoW 與 WoW chips 已在 production，並分別列出 SRAM 疊在 CPU 與 logic 疊在 deep-trench-capacitor die 的應用；AMD 於 2022-03-21 又把已加入 EPYC 7003 產品線的 3D V-Cache 處理器明確描述為 copper-to-copper hybrid bonding 的 bumpless design
supporting_source_ids: S7,S8
contrary_source_ids:
as_of: 2022-06-17
basis: S7 提供 foundry 端 CoW／WoW production 與應用，S8 提供產品端 EPYC 型號世代與 hybrid bonding 描述，兩個發行人可交叉建立特定 N7／3D V-Cache 路徑已越過純試驗車的證據
boundary: production 與商用產品不等於公開可稽核的 HVM economics；兩份文件都沒有 good-product yield、throughput、成本、產能利用或供應商財務分子，也不能證明 200nm W2W 或新 D2W PDK 同樣成熟
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C8
label: inference
status: active
claim: Hybrid bonding 不能用一條共同成熟度曲線判斷；至少要同時固定應用、W2W／D2W 接法、介面世代或 pitch、具名產品與 qualification／production 狀態，因為已商用或進 production 的影像感測器與 N7 SoIC 路徑，正和 200nm W2W 試驗車、D2W pathfinding PDK 及未具名工具使用同時存在
supporting_source_ids: S1,S2,S3,S6,S7,S8
contrary_source_ids:
as_of: 2026-08-12
basis: correction_of:C4；S6–S8 證明較早應用與具名產品／production，S1–S3 則證明另一組細間距、設計入口與工具證據仍停在 pathfinding／test vehicle／unnamed customer use；差異來自研究單位不同而非互相矛盾
boundary: 本矩陣只校正成熟度分類，不推估 hybrid bonding TAM、量產良率、設備材料份額、台灣公司訂單、財務貢獻或股價；任一已成熟格也不能替另一應用、接法或介面世代繼承資格
verification_needed:
correction_kind: supersedes
corrects_claim_id: C4
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: verified
status: active
claim: EVG 於 2025-09-08 表示 EVG40 D2W 可在 300mm wafer 上量測每一顆 die 的 overlay，最高在四分鐘內取得 2,800 個 measurement points，並稱多台系統已裝在客戶端用於 HVM production services
supporting_source_ids: S10
contrary_source_ids:
as_of: 2025-09-08
basis: S10 明列 100 percent die overlay measurement、every die、up to 2,800 points in four minutes 與未具名 customer-site HVM services
boundary: 100% 的分母是被量測 die，不是 100% die 都在對準規格內，更不是無空洞、電性、可靠度或合格產品良率；HVM services 也沒有客戶、產品、配置、批次或財務分母
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: EVG 於 2022 年在 HICC 以單次轉移示範把完整 3D SoC 的多顆不同尺寸 die 接合，正文把結果描述為 100% void-free bonding yield
supporting_source_ids: S11
contrary_source_ids:
as_of: 2022-07-12
basis: S11 直接固定 HICC、single transfer process、multiple dies of different sizes、complete 3D SoC 與 void-free 結果
boundary: 這個 100% 只支持該次示範的接合介面沒有觀察到空洞；來源未公布 die 數，也沒有證明所有接點導通、最終產品功能、重複 lot、長期可靠度、產能或成本
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C11
label: verified
status: active
claim: imec 的 2µm D2W 試驗載具同時報告小於 350nm 的 overlay error、Kelvin e-yield 大於 85% 與 daisy-chain e-yield 大於 70%，顯示幾何對準與兩種電性結構各有自己的量測結果
supporting_source_ids: S12
contrary_source_ids:
as_of: 2024-05-29
basis: S12 在同一 process-flow 段落逐一列出 overlay、Kelvin e-yield 與 daisy-chain e-yield，且兩個電性比例並不相同
boundary: Kelvin 與 daisy chain 是不同試驗結構，不是兩個可直接平均的產品良率；來源未提供完整分母、分布、lot 數與最終產品測試，也不能跨接法或 pitch 比排名
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: imec 的 400nm W2W 研究把表面平坦與 void-free bonding、低單接點電阻、overlay，以及 dielectric breakdown／yield 分開評估，並只對該 400nm 設計提出 overlay control 小於 100nm 才能取得 sufficient HVM yield 的結論
supporting_source_ids: S13
contrary_source_ids:
as_of: 2024-02-19
basis: S13 分別描述 CMP 與 void-free 條件、<150nm 實測 overlay、low single-contact resistance，及 overlay 與 dielectric breakdown／yield 的研究關係
boundary: <100nm 是特定 400nm pitch 與 pad design 的研究條件，不是所有 hybrid bonding 的共同規格；sufficient HVM yield 也不是具名客戶產品已量產或公開良率
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C13
label: inference
status: active
claim: 讀取 hybrid bonding 的百分比時，至少要用六欄品質護照固定受測物與分母、接法／pitch／試驗或產品身分、對準量測覆蓋與分布、介面完整性、電性與可靠度、重複批次產能成本與最終合格產品，否則量測覆蓋、門檻通過、無空洞、測試結構良率與產品良率不能互換
supporting_source_ids: S2,S10,S11,S12,S13
contrary_source_ids:
as_of: 2026-08-13
basis: S10 的 100% measurement coverage、S2 的 all-die overlay threshold、S11 的 void-free interface、S12 的兩種 e-yield 與 S13 的 reliability／yield 關係分屬不同受測物與判定層；六欄是研究中心為防止跨層誤讀所做的整合
boundary: 六欄護照不是 imec 與 EVG 共同標準，也不能用公開百分比倒推出單接點缺陷率或以良率次方估產品結果；缺陷可能相關且試驗拓樸、產品與製程條件不同
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C14
label: unverified
status: active
claim: 具名 AI、HBM 或 chiplet 量產產品已公開同一版本的完整六欄品質護照，並以重複 lot 同時證明合格產品良率、可靠度、throughput、成本與台灣供應商財務貢獻
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-13
basis: S2、S10–S13 分別停在試驗載具、設備量測、開發中心示範或未具名 HVM service，沒有同一具名產品的端到端共同分母
boundary: 不因文件提及 AI、HBM、chiplet、HVM、production tool 或高良率，就建立客戶產品量產、台灣公司訂單、收入、毛利或投資結論
verification_needed: 產品商、製造端與供應商對同一產品版本、接法、pitch、lot、量測門檻、合格產出、可靠度、產能、成本及財務期間完成雙向核對
resolution:
-->

<!-- research_claim
claim_id: C15
label: verified
status: active
claim: TEL 在 2026 IEEE Hybrid Bonding Symposium 的 140nm W2W 試驗摘要中，把含 bond-pad layout 的 hybrid-bond residual misalignment <50nm，與移除 pad-layout 影響後三片 fusion-bond wafer 中 99.5% points residual <40nm 分開報告，並據此判斷 pad layout 也是 misalignment contributor
supporting_source_ids: S14
contrary_source_ids:
as_of: 2026-01-22
basis: S14 摘要逐一固定 140nm test vehicle、hybrid-bond high-accuracy recipe 的 <50nm，以及 fusion-bond diagnostic 的三片 wafer／99.5% points／<40nm 與 pad-layout interpretation
boundary: 兩組數字的結構與分母不同，不能互相平均或當成同一 overlay distribution；三片 fusion wafer 不是三個產品、客戶或量產 lot，摘要也沒有公開 hybrid electrical yield、可靠度、throughput、成本或 good-product yield
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C16
label: verified
status: active
claim: IBM Research 的 ECTC 2025 摘要報告，在其 sub-micron Cu-Cu Kelvin 試驗結構中，pad size 與 pitch spacing 縮小時初始電阻及其 spread 呈上升、bonding yield 呈下降；高溫測試又使電阻下降、yield 上升
supporting_source_ids: S15
contrary_source_ids:
as_of: 2025-05-27
basis: S15 Abstract 直接描述 four-point Kelvin 方法及 scaling、initial resistance／spread、bonding yield 與 high-temperature testing 的方向性結果
boundary: 只證實 IBM 指定試驗結構的方向性關係；公開摘要沒有各 pitch 數字、樣本與完整分布，不能量化 slope、因果拆分、產品良率、field lifetime、成本或跨公司優劣
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C17
label: inference
status: active
claim: Hybrid bonding 的 pitch 應先拆成理想站點密度、pad geometry／Cu density、overlay 定義與分布、表面／微結構、電阻與良率，再用同一份十欄互連縮放護照連到重複批次、throughput、可靠度與產品經濟；pitch 平方幾何與 overlay-to-pitch 比只能做條件化教材，不能單獨排名製程成熟度或公司受惠
supporting_source_ids: S2,S12,S13,S14,S15
contrary_source_ids:
as_of: 2026-08-14
basis: S2／S12／S13／S14 提供不同接法、pitch 與 overlay 角色，S14 額外拆出 pad-layout contributor，S15 證明 pad／pitch scaling 同時牽動電阻 spread 與 yield；十欄護照是跨來源的研究整合
boundary: 平方密度與 ratio 都是假想方形網格及公開 bound 的確定性換算，不是 routing density、usable link count、overlay budget、產品性能、yield model、TAM、需求、收入、毛利或股價未反映；跨來源數字不構成同條件比較
verification_needed: 同一具名產品版本公開 grid／pad geometry、overlay vector distribution、surface／microstructure、electrical／reliability、die／wafer／lot、throughput、合格產品、成本、BOM 與財務共同鍵
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: retired
claim_ids: C1,C2,C3,C4
metric: Hybrid bonding 由 PDK／試驗車進入具名產品 qualification、HVM yield、throughput 與可靠度的成熟度
source_ids: S1,S2,S3
watch_source_ids: S4,S5
frequency: event_driven
frequency_detail: imec、設備商、晶圓廠或 OSAT 發布新 PDK、test chip、qualification 或 HVM 結果時重審
next_check: 2026-08-16
trigger: 具名邏輯或記憶體產品完成客戶 qualification，且公開可定位的 good-die yield、throughput 或量產可靠度
invalidation: 後續證據持續停在 pathfinding PDK、試驗車或未具名客戶使用，HVM 成熟度維持未證並下修商業急迫性
retired_at: 2026-08-12
retirement_reason: Sony、TSMC 與 AMD 新納入的歷史一手資料顯示不同應用、接法與世代已處於不同商用階段；單一 monitor 把整體 hybrid bonding 當成一條 maturity ladder 會混淆已 production 格與 200nm／pathfinding 格，改由 T3 四維矩陣接續
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C5
metric: 台灣封測、設備與材料公司的 hybrid bonding 客戶、製程步驟、量產與財務貢獻
source_ids: S2,S3
watch_source_ids: S5
frequency: quarterly
frequency_detail: 每季重查公司法說、財報與客戶平台文件，要求同一料號或製程步驟可雙向核對
next_check: 2026-10-31
trigger: 台灣公司與客戶對同一 hybrid bonding 產品或製程完成 qualification／量產雙向核對，並出現收入或毛利資訊
invalidation: 公司只使用 hybrid bonding、2.5D／3D 或先進封裝概念詞，未揭露客戶、產品、階段與財務足跡
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C1,C2,C3,C6,C7,C8
metric: Hybrid bonding 應用×W2W／D2W 接法×介面世代／pitch×具名產品階段矩陣
source_ids: S1,S2,S3,S6,S7,S8
watch_source_ids: S4,S5,S9
frequency: event_driven
frequency_detail: imec、TSMC、產品商、設備商或 OSAT 公布新 PDK、test vehicle、具名產品 qualification、production、yield、throughput 或可靠度時，先固定四個維度再更新該格
next_check: 2026-08-19
trigger: 任一既有或新應用同時披露可定位的接法、介面世代或 pitch、具名產品與 qualification／production 狀態，或進一步提供 good-product yield、throughput、可靠度與成本
invalidation: 新文件只使用 generic hybrid bonding、3D stacking、customer use 或最小 pitch，卻沒有固定應用、接法、產品與階段；該資料不得讓其他矩陣格自動升級
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C9,C10,C11,C12,C13,C14
metric: Hybrid bonding 百分比六欄品質護照與量測層級
source_ids: S2,S10,S11,S12,S13
watch_source_ids: S4,S5,S9
frequency: event_driven
frequency_detail: 研究機構、產品商、設備商、晶圓廠或 OSAT 發布 overlay、void、electrical yield、reliability、product yield 或 HVM economics 時，先固定受測物與完整分母再更新
next_check: 2026-08-19
trigger: 具名產品以同一版本公開 die／wafer／lot 數、pitch／拓樸、量測覆蓋與分布、介面缺陷、電性／可靠度、合格產品、throughput 與成本，且能與供應商資料雙向核對
invalidation: 新百分比仍只給 best result、測試結構或不明分母，或把 measurement coverage、void-free、e-yield 與 product yield 混寫；該資料只留在原量測層，不得升級量產經濟與公司歸因
-->

<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_plain_language_wave4_packaging_learning_no_conclusion_change
evidence: editorial:plain_language_wave4
-->
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave94_hybrid_bonding_paths_process_windows_and_six_gate_ladder
evidence: editorial:reader_layer_only_no_claim_source_monitor_or_impact_change
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: split_hybrid_bonding_maturity_by_application_process_generation_and_product_stage
evidence: sources:S6,S7,S8
-->
<!-- transition
date: 2026-08-13
from: triaged
to: triaged
reason: separated_hybrid_bonding_percent_denominators_and_added_quality_passport_without_thesis_clock_refresh
evidence: sources:S10,S11,S12,S13
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_pitch_squared_density_overlay_ratio_and_scaling_tradeoff_passport_without_thesis_clock_refresh
evidence: sources:S14,S15
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **混合接合（Hybrid bonding）**：不靠凸塊隔開兩層晶片，而讓平坦介電層與細小銅接點直接貼合；連線可更短、更密，表面與對準條件也更嚴格。
- **凸塊（Bump）**：傳統封裝常用的微小金屬連接點，會在兩層晶片之間留下高度；移除凸塊不代表接合製程就更簡單。
- **接點間距（Pitch）**：相鄰接點中心之間的距離。間距變小代表接點更密，不等於良率、成本或量產能力已經更好。
- **理想方形網格站點密度（Square-grid site density）**：假設接點排成相同方形網格時，單位面積可放的理想位置數約和 1÷pitch² 成正比；它還沒扣 pad 尺寸、keep-out、電源／備援、繞線與缺陷。
- **Overlay-to-pitch ratio**：把某個對準誤差數字除以 pitch 的條件化比值；分子若一個是規格、一個是最大值、一個是 99.5% points，就不能只看比值排高低。
- **Pad size／Cu density（接點尺寸／銅面積比例）**：Pitch 只說中心距；銅墊多大、上下是否等尺寸、單位區域有多少銅，會改變接觸、空洞、應力與電性，不能由 pitch 自動推出。
- **Resistance distribution／spread（電阻分布／離散）**：不能只報平均接點電阻；分布尾端與跨 die／wafer／lot 變化，才會顯示是否有局部高阻或製程漂移。
- **Fusion-bond diagnostic（無金屬接點的融合接合診斷）**：暫時拿掉 bond-pad layout 影響，觀察 wafer deformation、工具與流程本身的對準殘差；這種診斷不能替含銅接點的 hybrid-bond 電性或產品良率背書。
- **TEL（Tokyo Electron）**：本輪 140 奈米 W2W 試驗摘要的研究團隊所屬設備商；其試驗數字只固定該載具與診斷，不能改寫成客戶產品量產或公司訂單。
- **HBM（高頻寬記憶體）**：把多顆記憶體晶粒垂直堆疊以提高頻寬的產品類別；本文只把它列為後續應用查核格，沒有用本輪試驗證明具名 HBM 已採同一接法或 pitch。
- **晶粒（Die）**：晶圓切割後的單顆晶片。晶粒能否先被挑選，會改變後續接合的良率分母。
- **晶圓（Wafer）**：尚未切成單顆晶粒的圓形半導體基板；整片處理效率高，但也要一起管理全片缺陷與對準。
- **單顆晶粒接晶圓（D2W）**：先挑選單顆晶粒，再逐顆接到目標晶圓；可混搭不同晶粒，但放置速度與逐顆對準也要計入。
- **晶圓接晶圓（W2W）**：把兩片晶圓整面對準後一次接合；平行處理效率高，但上下晶圓的良品位置與缺陷分布會一起影響結果。
- **晶片接晶圓（CoW）**：產品與製造文件常用的另一個寫法，意思是把已切割晶片接到晶圓；本文只在來源原文使用 CoW 時保留該名稱，研究分組仍放在 D2W。
- **晶圓疊晶圓（WoW）**：台積電文件使用的 wafer-on-wafer 縮寫，研究分組對應本文的 W2W；保留不同縮寫是為了能逐字回查來源。
- **銅對銅接合（Cu-Cu）**：讓上下兩層銅接點直接形成電性連接；本文來源明確稱為 hybrid bonding 時才把它放入混合接合證據，不把所有銅互連都自動歸類。
- **N7**：台積電七奈米製程家族的名稱；N7 SoIC production 只能證明該節點與具名接法，不能替 N5、N3 或 200 奈米研究介面升級。
- **應用世代**：同一技術被用在哪種產品、哪一代製程與哪種介面；影像感測器、CPU 快取與 200 奈米試驗結構不能只因都叫混合接合就共用成熟度。
- **設計製程套件（PDK）**：把製程可做的線寬、間距、材料與驗證元件整理成設計規則；有套件不等於已有實體量產產品。
- **探索型設計製程套件（Pathfinding PDK）**：讓設計者先找可行路徑的早期版本；可以開始試畫與驗證，不代表已具備完整送製能力。
- **試驗結構（Test vehicle）**：為量測製程、電性與缺陷而設計的測試結構，不是客戶最終商品，也不能直接代表量產良率。
- **對準誤差（Overlay）**：上下兩層接點實際位置的偏差；接點越密，可容忍的偏差通常越小。
- **表面平坦度**：接合前表面的高低差與粗糙程度；表面不夠平，即使平均位置正確也可能貼不牢或導通失敗。
- **潔淨度與顆粒控制**：避免灰塵、殘留物或微小顆粒卡在接合面；局部污染可能造成空洞、未接合或電性缺陷。
- **化學機械研磨（CMP）**：用化學反應與機械研磨把晶圓表面整平，控制介電層、銅接點與凹陷高度。
- **重新佈線層（RDL）**：在晶片或封裝表面重新安排金屬線與接點位置，讓不同晶片能接到更細的互連。
- **介電層**：隔離導電線路的絕緣材料；混合接合時，介電層表面品質會和銅接點一起決定貼合結果。
- **銅接點**：上下兩層用來傳遞訊號或電力的細小銅墊；不只要對準，也要控制表面狀態與接合後電阻。
- **已知良品（Known good die）**：在接合前已完成篩選、較有把握正常工作的晶粒；能先挑良品不代表後續接合不會新增缺陷。
- **合格晶粒良率（Good-die yield）**：經製程與測試後可用晶粒占投入晶粒的比例；必須說清投入、測試與合格定義才能比較。
- **電性良率（Electrical yield）**：通過指定電性測試的比例；接點對準達標不等於所有電路都能正常工作。
- **量測覆蓋率（Measurement coverage）**：實際被量測的 die 或位置占目標母體的比例；100% 覆蓋只代表全部量到，不代表全部合格。
- **無空洞接合（Void-free bonding）**：檢查接合介面是否出現未貼合空洞；看不到空洞不等於所有銅接點都導通或產品功能合格。
- **Kelvin 測試結構**：用特定四端結構量測單一或少數接點的電阻，降低導線電阻干擾；它不是完整產品電路。
- **菊鏈測試結構（Daisy chain）**：把許多接點串成一條電性路徑，任一處開路都可能讓整條鏈失敗；鏈長與接點數會改變分母。
- **線上量測（Inline metrology）**：在製程進行中量測位置、表面或缺陷，及早發現漂移；能量到不等於製程已穩定量產。
- **客戶資格認證（Qualification）**：客戶依功能、可靠度與製造條件確認產品是否可採用；設備被使用不等於認證已完成。
- **穩定大量生產（HVM）**：在持續生產中同時守住良率、產能、可靠度與成本，而不是只做出一次試驗結果。
- **每小時產能（Throughput）**：設備或產線在一定時間內可完成的數量；速度要和良率、停機、返工與成本一起看。
- **長期可靠度**：產品經過時間、溫度循環與使用負載後仍能維持功能；短期導通成功不能替代長期測試。
- **返工能力**：發現接合問題後是否能拆解、重做或挽救產品；不同接合路徑的可返工程度會影響實際成本。
- **設計定稿送製（Tape-out）**：設計完成並交給製造端產生實體晶片的節點；探索型規則可用不等於已經完成送製。
- **試製晶片（Pilot silicon）**：用早期製程做出的實體晶片，用來驗證設計與製造；仍排在穩定量產之前。
- **委外封測廠（OSAT）**：承接晶粒封裝、互連與測試的外包廠商；具備一般先進封裝能力不等於已量產特定混合接合產品。
- **Kinex**：Applied Materials 與 Besi 合作的單顆晶粒接晶圓整合設備；多類客戶使用設備，仍不等於具名產品已量產。
- **imec**：進行半導體研發與試驗線驗證的研究機構；試驗結果可證明技術能力，但不能替代客戶產品量產資料。
- **EV Group（EVG）**：參與本輪晶圓接晶圓試驗的設備公司；合作試驗證明設備角色，不等於市場份額或台灣供應商受惠。
- **EVG40 D2W**：EVG 用於逐顆接晶圓後對準量測的設備；可量測每顆 die 不代表每顆都合格。
- **異質整合能力中心（HICC）**：EVG 用來協助客戶開發與示範製程的中心；中心內成功不等於客戶產品已量產。
- **堆疊式影像感測器（Stacked CIS）**：把感光像素與邏輯電路分層製作再垂直連接；Sony 的公開技術回顧顯示這條應用早於本輪 200 奈米試驗。
- **TSMC-SoIC**：台積電的晶圓級三維晶片堆疊平台，包含晶片接晶圓與晶圓接晶圓路徑；平台已有 production 證據，不代表每個節點、pitch 與產品都同時成熟。
- **AMD 3D V-Cache**：把額外快取晶片垂直疊到處理器上的產品技術；AMD 把 EPYC 7003 的作法明確描述為無凸塊的銅對銅混合接合。

### 三句話抓重點

- 混合接合讓平坦絕緣表面與細小銅接點直接貼合，連線可更短、更密；但用途、整片貼或逐顆貼、介面世代與產品階段不同，成熟度就不能互相繼承。
- 影像感測器與處理器快取已有正式產品或生產證據，證明這項技術不是整體都停在試驗；成熟的是其中幾個明確格子。
- 200 奈米整片試驗、逐顆貼合的早期設計規則與未具名客戶使用設備仍是另外幾格，還缺逐產品良率、產能、可靠度、成本與財務分子。

### 為什麼重要

混合接合讓邏輯、記憶體與小晶片之間的接點更密，可能縮短資料路徑與降低傳輸能耗；但接點越密，
表面平坦度、潔淨度、對準、良品挑選與接合後檢查就越需要一起控制。若只問「混合接合量產了嗎」，
會同時犯兩種錯：把舊應用已商用的事實刪掉，或把舊應用的成熟度移植給新 pitch、新接法與新產品。

### 接下來怎麼追

- 先替每份新資料填四格：應用、W2W／D2W 接法、介面世代或 pitch、具名產品與資格／生產階段。
- 再把逐顆接合與整片接合分開，分別核對良率分母、對準分布、每小時產能、返工與長期可靠度。
- 遇到更小 pitch，另填方形網格假設、pad geometry、Cu density、overlay 定義、電阻分布與 die／wafer／lot 分母；不要讓單一幾何紀錄替整份縮放護照畢業。
- 公司映射必須同時找到客戶端的具名製程與供應商端的料號、量產及收入，缺一邊就維持待驗證。

### 想一想

- Sony 影像感測器或 AMD 處理器已有產品證據，為什麼仍不能證明 200 奈米整片貼合已量產？
- 逐顆挑選後再接合，與兩片晶圓整面接合，為什麼不能只用一個良率分母比較？
- 若 A 試驗的「對準誤差占間距比例」比 B 小，還要先核對哪些分子定義、接點版圖與電性分布，才知道能不能比較？
- 公司說晶片已進入生產後，還要看到哪些良率、產能、成本與財務資料，才能比較量產經濟性？

## 先畫四維地圖：成熟的是哪一格

最安全的問法不是「混合接合成熟了嗎」，而是：**哪一種應用、哪一種接法、哪一代介面、哪個產品階段成熟了？**
下表把本輪一手證據放回各自格子；它是範圍地圖，不是技術排名。

| 應用或產品格 | 接法與介面範圍 | 公開證據到哪裡 | 可以說什麼 | 不能把什麼一起升級 |
|---|---|---|---|---|
| Sony 堆疊式影像感測器 | Cu-Cu hybrid bonding；官方回顧沒有把每一代產品都固定成同一 W2W／D2W 流程 | 2015 年技術導入後，官方回顧列出異質材料感測器、edge-AI logic 與後續多層堆疊演進 | 這個應用家族不是到 2026 年才從試驗起步 | 不代表 2023 large-chip CoW、多層堆疊或其他公司產品已量產，也沒有公開良率與成本 |
| AMD EPYC 7003 3D V-Cache／TSMC N7 SoIC CoW | 銅對銅無凸塊接合；晶片接晶圓 | AMD 已把具名處理器加入產品線；TSMC 表示 N7 CoW chips 已在 production | 特定 N7 CPU＋SRAM 路徑已越過純試驗結構 | 不代表所有 D2W、所有節點、200 奈米 pitch 或任何台灣設備材料商都已通過資格 |
| TSMC N7 SoIC WoW 的 logic＋DTC IPU | 晶圓接晶圓 | TSMC 表示 N7 WoW chips 已在 production，並列出 logic 疊在深溝電容晶粒的應用 | 特定 N7 WoW 應用已有 foundry production 聲明 | 不代表 imec 200 奈米 W2W 的產品良率、throughput 或成本已完成 |
| imec／EVG 200 奈米 W2W | 300 毫米晶圓、200 奈米 Cu pad pitch 的試驗結構 | 接合後對準結果與可路由試驗結構 | 能證明特定細間距與對準能力 | 不能繼承前述 N7／影像感測器的產品、qualification、HVM economics 或出貨 |
| NanoIC D2W 與 Kinex 工具 | 探索型 D2W 設計規則；整合接合與線上量測工具 | pathfinding PDK 與未具名多類客戶使用 | 設計入口與工具整合正在前進 | 不能寫成完整 tape-out、具名產品資格、穩定量產或供應商收入 |

所以本文採用的是「成熟度向量」，不是單一標籤：

> 應用 × 接法 × 介面世代／pitch × 具名產品階段

只要其中一格改變，就要重新驗證；舊格的 production 只能當可行性先例，不能替新格通過資格。

## 先分清兩種「貼法」的良率分母

| 本文兩條接合路徑 | 怎麼接 | 主要優點 | 主要風險 | 為什麼不能直接比較 |
|---|---|---|---|---|
| 單顆晶粒接晶圓（D2W） | 先挑單顆晶粒，再逐顆放到目標晶圓 | 能先挑已知良品，也較容易混搭不同尺寸或製程的晶粒 | 逐顆放置速度、每顆對準、接合後新增缺陷與返工 | 良率從「已挑過的晶粒」開始算，不能和整片晶圓用同一投入分母 |
| 晶圓接晶圓（W2W） | 兩片晶圓整面對準後一次接合 | 可同時處理大量接點，平行效率高 | 上下晶圓良品位置是否匹配、全片翹曲、顆粒與局部錯位 | 分母同時受到兩片晶圓缺陷分布與接合後成品影響，不能只比最小間距 |

這張表只說明本文為何要把兩條路徑分開閱讀，不是完整製程規格，也不代表其中一條一定更便宜、
良率更高或更早量產。

## 同樣寫 100%，先問分母：量測覆蓋不等於合格產品良率

新聞稿裡的百分比常被排在同一行，但它們可能根本不是同一張考卷。最容易辨認的方法，是先把每個
百分比還原成一句完整分數：**誰通過什麼門檻，除以哪一群受測物？** 若這句話填不完整，數字就只能
留在原本的量測層，不能往下改寫成「產品良率」。

| 公開寫法 | 分子與分母要怎麼讀 | 這一層能證明什麼 | 還不能證明什麼 |
|---|---|---|---|
| EVG40 D2W 的 100% die overlay measurement | 被量測的 die／目標量測 die；EVG 並稱最高四分鐘取得 2,800 個量測點 | 量測系統能把抽樣擴成全 die 覆蓋，讓每顆位置都有回饋 | 沒說每顆都落在對準規格，更不是接合、電性或產品良率 100% |
| imec／EVG 200 奈米試驗的所有 die 都低於 40 奈米 overlay | 低於指定門檻的 die／該 300 毫米試驗晶圓上被判定的 die | 固定試驗載具、修正流程與門檻後，全片幾何對準結果達標 | 沒證明每個接點導通、長期可靠或客戶產品全數合格 |
| EVG 開發中心示範的 100% void-free bonding yield | 在該次多 die 單次轉移中未觀察到空洞的接合介面／該次示範母體；公開頁沒有列 die 數 | 指定示範的介面完整性結果 | 空洞檢查不是電性終測，也沒有重複 lot、產品功能、產能與成本 |
| imec 2 微米試驗的 Kelvin 大於 85%、菊鏈大於 70% | 通過各自電性判定的 Kelvin 或菊鏈結構／各自被測結構；公開頁沒有列完整數量 | 單接點型與多接點串鏈型電性成績可以分開觀察 | 兩個比例不能互相平均，也不能直接當最終堆疊產品良率 |
| 具名產品合格良率 | 通過功能、可靠度與客戶規格的產品／同版本、同製程條件的投入產品 | 若再有重複批次、產能與成本，才開始回答穩定量產經濟 | 本輪來源沒有公開這個共同分母 |

還有一個常見陷阱：不能把菊鏈結果直接套進「單接點良率的接點數次方」。實際缺陷可能群聚或相關，
Kelvin、菊鏈與產品的接點拓樸、pitch、材料、測試門檻也不同。imec 的 400 奈米研究更把表面平坦、
無空洞條件、單接點電阻、overlay、介電層擊穿與 yield 分開評估；它對該設計提出的對準需求，不能變成
所有混合接合產品的共同規格。

### 六欄混合接合品質護照

每遇到新的「高良率」或「100%」主張，可先填完下面六欄。這是研究中心整合公開文件的查核方法，
不是 imec、EVG 或產業共同制定的標準。

| 品質護照欄位 | 最少要記什麼 | 缺少時最容易誤判什麼 |
|---|---|---|
| 1. 受測物與分母 | die、介面、接點、Kelvin、菊鏈、wafer、package 或最終產品；實際數量 | 把「全部量到」讀成「全部合格」 |
| 2. 製程身分 | W2W／D2W、pitch、pad／鏈路拓樸、材料、試驗載具或具名產品、版本 | 把另一接法或舊世代的成績搬過來 |
| 3. 對準量測 | 覆蓋率、門檻、全分布與邊緣值、量測方法、die／wafer／lot 數 | 用平均值或單一最佳值遮住尾端失敗 |
| 4. 介面完整性 | void 的檢查方法與判定、bond strength、表面狀態、抽樣範圍 | 把看不到空洞改寫成所有接點導通 |
| 5. 電性與可靠度 | Kelvin、菊鏈、開短路、電阻、介電擊穿、溫度循環、時間與樣本 | 把短期測試結構結果改寫成產品壽命 |
| 6. 產品與量產經濟 | 合格產品、重複 lot、返工／報廢、throughput、成本、客戶 qualification 與財務期間 | 把研究成功或設備上線改寫成量產訂單與獲利 |

六欄的用途不是要求每份研發新聞稿一次交齊所有資料，而是讓讀者知道證據目前停在哪一層。公開文件
若只完成前三欄，就可以證明量測與製程能力，卻仍應把最終產品良率、量產經濟與台灣公司財務歸因
留在待驗證。

## Pitch 砍半，不等於密度、overlay 裕量與良率一起變好

Pitch 是一個幾何起點，不是一張完整成績單。相同面積、相同方形排列且其他條件完全不變時，理想
站點密度才會和 1÷pitch² 成正比；真實產品還要扣掉 pad 尺寸、電源與備援接點、keep-out、繞線、
測試、冗餘與不能使用的位置。下面只把 2µm 當作指數 1，對四個不同來源／接法做純幾何教學。

| 公開試驗語境 | 接法 | Pitch | 假想方形網格站點密度指數 | 這一欄不能代表什麼 |
|---|---|---:|---:|---|
| imec 2µm 試驗載具 | D2W | 2,000nm | 1.000 | 不等於合格 Kelvin、菊鏈或產品接點數 |
| imec 400nm 試驗 | W2W | 400nm | 25.000 | 不等於 25 倍可用 I/O、頻寬、良率或收入 |
| imec／EVG 200nm 試驗 | W2W | 200nm | 100.000 | 不等於 100 倍 good links 或相同 pad geometry |
| TEL 140nm 試驗載具 | W2W | 140nm | 204.082 | 不等於 204 倍產品密度、產能或商業價值 |

204.082 只來自（2,000÷140）²。表格把 D2W 與 W2W、不同 pad layout、不同試驗結構故意並排，是為了
顯示 headline pitch 在理想幾何上的量級，不是把四份結果改造成同條件 benchmark。只要接點排列、pad
尺寸、Cu density、冗餘或可路由面積不同，實際 usable-link density 就會和這個平方指數分開。

### Overlay 除以 pitch，先看分子的角色

把 overlay 數字除以 pitch，可以提醒讀者「同樣 40nm 在不同 pitch 下占多少比例」，但分子可能是
實測上界、設計控制條件、全 die 門檻，或刻意移除 pad layout 的診斷結果。以下保留每份來源原來的
角色；小於號表示公開 bound，不是實際平均值。

| 公開語境 | 分子是什麼 | Pitch | 算術 bound÷pitch | 為什麼不能直接排名 |
|---|---|---:|---:|---|
| imec 2µm D2W | 公開的 overlay error <350nm | 2,000nm | <17.500% | 同頁 Kelvin／菊鏈良率另有分母，沒有全分布 |
| imec 400nm W2W | 該設計對 sufficient HVM yield 提出的 control <100nm | 400nm | <25.000% | 這是設計條件，不是同一列的產品量測 |
| imec／EVG 200nm W2W | 試驗晶圓所有 die 的 post-bond vector <40nm | 200nm | <20.000% | all die 過幾何門檻不等於接點全導通 |
| TEL 140nm W2W | 含 bond-pad layout 的 hybrid-bond residual <50nm | 140nm | <35.714% | 摘要沒有 hybrid electrical-yield 分布與產品分母 |
| TEL fusion diagnostic | 三片 wafer 中 99.5% points residual <40nm | 140nm test context | <28.571% | 診斷刻意移除 pad layout，不能替上一列背書 |

TEL 的兩列尤其重要：同一份摘要先報含 pad layout 的 hybrid-bond 結果，再用三片無 pad-layout 的
fusion-bond wafer 隔離其他 deformation contributors。這不是兩種誰比較好的產品測試，而是用控制變因
找出誤差從哪裡進來。IBM Research 又從另一條鏈指出，pad size 與 pitch 繼續縮小時，其 Kelvin 試驗
結構的初始電阻與 spread 上升、bonding yield 下降；高溫測試後方向又會改變。幾何更密因此必須和
表面、微結構、電阻分布、熱歷程及良率一起讀。

本節有 N＝4 個跨來源 pitch 幾何案例與 N＝5 個公開 bound 的條件化除法；TEL 另明示 fusion 診斷
的物理樣本是 N＝3 片 wafer。Python Fraction 與獨立 awk 在顯示精度內完全一致。這些只是固定輸入
的確定性換算，不是抽樣推論或跨試驗 meta-analysis；公開資料沒有共同 raw distribution，因此不計
sampling SE／t，也沒有 die、wafer、lot、產品、客戶、throughput、成本、需求、收入、毛利或公司效果。

### 多空小作文共用的互連縮放十欄護照

| 護照欄位 | 必須固定什麼 | 少了最容易誤讀成什麼 |
|---|---|---|
| 1. 應用與產品 | CIS、logic、memory、HBM 或 chiplet；試驗載具／具名產品、版本與節點 | 一個應用成熟就代表所有 hybrid bonding 成熟 |
| 2. 接法與網格 | W2W／D2W、方形／六角／其他 grid、串並聯與功能分配 | 用方形 1÷pitch² 代表真實 usable links |
| 3. Pitch 與 pad | 中心距、上下 pad size、是否等尺寸、Cu density、keep-out 與冗餘 | Pitch 砍半就等於完整密度四倍 |
| 4. Overlay 定義 | pre／post-bond、vector／axis、mean／max／percentile／M＋3σ、coverage 與門檻 | 把規格、最大值與 99.5% points 放進同一排名 |
| 5. 誤差來源 | bonder、wafer distortion、warpage、bond wave、pad layout、熱歷程與 correction | 一個總 overlay 數字就能決定改善哪台工具 |
| 6. 表面與介面 | CMP、Cu recess／protrusion、roughness、潔淨、void、bond strength 與微結構 | 對準達標就推介面一定完整 |
| 7. 電性分布 | Kelvin／菊鏈拓樸、接點數、R distribution、open／short、stress 前後 | 平均低電阻就推全部接點與產品都好 |
| 8. 可靠度 | dielectric breakdown、current／thermal stress、溫循、時間與失效位置 | 初始 e-yield 冒充 field lifetime |
| 9. 樣本與製造 | die／wafer／lot、重複性、edge exclusion、throughput、停機、返工與 scrap | 一片試驗成功就推 HVM economics |
| 10. 產品與商業 | 合格產品、功能／效能、qualification、BOM、成本、合約與財務分母 | 更小 pitch 直接跳成台灣公司訂單與毛利 |

**較強的多方版本**不是「pitch 從 2µm 縮到 200nm，所以設備材料價值必然百倍」，而是同一具名
產品在縮放後仍把 overlay 全分布、介面、電阻尾端、可靠度、usable links、throughput 與成本一起守住，
並由客戶與供應商雙向證明新增製程步驟、設備時間或耗材價值真的落到可辨識財務。

**較強的空方版本**也不是「IBM 看到 yield 下降，所以 hybrid bonding 不可量產」，而是縮放收益被
pad geometry、表面缺陷、metrology 時間、scrap、冗餘或返工吃掉；若產品只需要較鬆 pitch，或整合
改善讓每顆合格成本下降，最小 pitch 的技術紀錄未必轉成設備台數、耗材量或供應商議價。

## 再看五個量產窗口如何接力

| 本文五個量產窗口 | 先回答什麼 | 主要接力角色 | 失敗會怎樣 | 本輪可確認到哪裡 |
|---|---|---|---|---|
| 1. 設計規則與試驗結構 | 設計者知道哪些線寬、間距與材料可製造嗎？ | 研究機構、設計工具與晶圓製程團隊 | 規則畫得出來，實體卻做不出或無法量測 | N7 SoIC 等較早產品格已越過本關；新 D2W PDK 仍是探索型，200 奈米 W2W 仍是試驗結構 |
| 2. 表面平坦與銅高度 | 介電層、銅接點與凹陷高度是否落在可接合窗口？ | 材料、研磨、沉積與表面處理設備 | 局部接觸不足、空洞、電阻不穩或整片報廢 | 技術文件列出研磨與表面條件；沒有把新舊各格放在同一口徑的長期製程分布 |
| 3. 潔淨與顆粒控制 | 接合面能否在搬運、清洗與貼合前維持乾淨？ | 清洗設備、化學材料、晶圓廠與封測廠 | 一顆微粒就可能造成局部未接合或缺陷擴散 | 已知潔淨是製程節點；沒有量產缺陷密度與停機資料 |
| 4. 對準、接合與量測 | 上下接點是否持續對準、導通，並能及早發現漂移？ | 接合設備、線上量測、檢查與製程整合團隊 | 接點錯位、開路、短路，或直到後段才發現損失 | 試驗結構有細間距與對準結果，整合設備也被多類客戶使用 |
| 5. 良率、產能與可靠度 | 好產品比例、每小時產能、返工與長期壽命能否一起達標？ | 晶圓廠、封測廠、產品客戶與財務團隊 | 技術可做卻成本過高、產量不足或使用後失效 | 已有特定產品與 production 聲明，但各格仍沒有可共同稽核的良率、throughput、成本、利用率與財務分子 |

五個窗口是接力關係：前一站達標不會自動替下一站畢業。這是本文的製程責任地圖，不是供應商名單、
訂單判定、公司快慢或投資排序。

## 最後用六關分開「已有產品」與「量產經濟可稽核」

| 本文六關 | 這一關要證明 | 本輪已有證據 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 開放設計入口 | 設計者有可用規則與驗證元件 | 新 D2W 格有 NanoIC 探索型 PDK | 完整送製工具、實體試製晶片與設計採用 | 規則可用不等於產品已做出或量產 |
| 2. 試驗結構成功 | 特定接點結構能被製作、對準與量測 | 新 W2W 格有 imec／EVG 200 奈米試驗結構與接合後對準結果 | 電性良率、缺陷分布、重複批次與長期可靠度 | 對準達標不等於所有電路正常或良率 100% |
| 3. 整合設備與流程使用 | 接合與量測步驟能在整合設備中運作 | Applied Materials 表示 Kinex 已被多類邏輯、記憶體與封測客戶使用 | 具名客戶、使用階段、設備數量與產品結果 | 客戶使用不等於資格認證、量產或設備收入份額 |
| 4. 具名商用產品 | 特定產品公開採用同一接合路徑 | AMD EPYC 7003 3D V-Cache 被明確描述為銅對銅無凸塊混合接合；Sony 回顧也列出多代影像感測器應用 | 同產品製造資格、批次與接合界面資料 | 一個商用產品不能替所有應用、接法與 pitch 通過資格 |
| 5. Production 聲明 | 製造端確認特定節點與接法已進生產 | TSMC 表示 N7 SoIC CoW 與 WoW chips 已在 production | 逐產品良率、throughput、停機、可靠度、成本與利用率 | production 一詞不等於上述量產經濟分母已公開，亦不證明 200 奈米格已完成 |
| 6. 量產經濟與財務歸因 | 客戶與供應商對上同一產品、期間、合格產出、成本與收入 | 本輪沒有共同口徑證據 | 客戶與供應商雙向核對料號、合格產出、重複出貨、收入或毛利 | 製程需要某類材料或設備不等於台灣公司已受惠 |

本輪不同來源顯示各格散落在第 1～5 關，第 6 關仍缺共同分母。六關是本文的查證順序，
不是共同產業標準；更不是把 Sony、TSMC、AMD、imec 與設備商放在同一條公司排名上。

## 來源與證據邊界

- [imec NanoIC：fine-pitch RDL 與 D2W pathfinding PDK](https://www.imec-int.com/en/press/nanoic-opens-access-first-ever-fine-pitch-rdl-and-d2w-hybrid-bonding-interconnect-pdks)
- [imec／EVG：200nm W2W hybrid bonding test vehicle](https://www.imec-int.com/en/press/imec-and-ev-group-demonstrate-wafer-wafer-hybrid-bonding-200nm-interconnect-pitch-and-record)
- [Applied Materials：Kinex integrated D2W hybrid bonder](https://investors.appliedmaterials.com/node/28506/pdf)
- [Sony：advanced CMOS image sensor 的 3D stacking 與 Cu-Cu hybrid bonding 演進](https://www.sony.com/en/SonyInfo/technology/publications/3d-stacking-process-technologies-for-advanced-cmos-image-sensors/)
- [TSMC：N7 SoIC CoW／WoW production 與應用](https://pr.tsmc.com/english/news/2939)
- [AMD：EPYC 7003 3D V-Cache 的銅對銅無凸塊混合接合](https://www.amd.com/ko/solutions/data-center/insights/leadership-performance-for-technical-computing-workloads.html)
- [EVG：EVG40 D2W 的全 die overlay measurement](https://www.evgroup.com/company/news/detail/ev-group-achieves-breakthrough-in-hybrid-bonding-overlay-control-for-chiplet-integration)
- [EVG：HICC 多 die 單次轉移的 void-free 示範](https://www.evgroup.com/company/news/detail/ev-group-achieves-die-to-wafer-fusion-and-hybrid-bonding-milestone-with-100-percent-die-transfer-yield-on-multi-die-3d-system-on-a-chip/)
- [imec：2µm D2W 的 overlay、Kelvin 與菊鏈電性結果](https://www.imec-int.com/en/press/imec-demonstrates-die-wafer-hybrid-bonding-cu-interconnect-pad-pitch-2mm)
- [imec：400nm W2W 的表面、電性、overlay 與可靠度關係](https://www.imec-int.com/en/articles/wafer-wafer-hybrid-bonding-pushing-boundaries-400nm-interconnect-pitch)
- [IEEE.tv／TEL：140nm W2W misalignment 與移除 pad-layout 影響的 fusion 診斷](https://ieeetv.ieee.org/hbs/reducing-wafer-to-wafer-bonding-misalignment-to-enable-sub-150nm-pitch-hybrid-bonding)
- [IBM Research：sub-micron Cu-Cu 接點縮放、電阻 spread 與 bonding yield](https://research.ibm.com/publications/electrical-performance-of-hybrid-bonding-with-sub-micron-cu-cu-bonding-contacts-effects-of-scaling-microstructure-and-surface-morphology)

本篇沒有把 imec、TEL、IBM、TSMC、AMD 或 Applied Materials 的效能與產品優勢拿來做跨公司數字
比較；各文件的應用、製程、產品與測試分母不同，也沒有 HVM 良率、每小時產能、每片成本與市場
份額的共同定義，因此 cross_company_numbers 維持 false。

## 影響路由

<!-- impact
group_id: packtest
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-31
rationale: D2W／W2W hybrid bonding 會改變 known-good-die、接合、檢查與可靠度流程，但本輪沒有 universe OSAT 的具名客戶產品與量產財務證據
evidence_boundary: 一般先進封裝能力、技術論壇或設備安裝不等於 hybrid bonding 客戶 qualification、量產訂單或毛利
-->

<!-- impact
group_id: semiequip
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-31
rationale: CMP、清洗、bonding、overlay metrology 與檢查是明確製程節點，但已證實工具來自 EVG、Applied Materials／Besi，尚未核對 universe 設備商
evidence_boundary: 製程需要某類工具不等於任一台灣設備商已通過客戶 qualification 或取得量產收入
-->

<!-- impact
group_id: material
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-31
rationale: SiCN、銅表面、清洗化學品與 CMP 耗材形成材料研究入口，但公開試驗流程未揭露 universe 材料供應商
evidence_boundary: 材料類別被研究機構使用不證明台灣公司供貨、份額、獨家性或財務貢獻
-->

## 下一個可證明／否定的節點

- NanoIC PDK 由 pathfinding 進入 fabrication-ready tape-out，並固定應用、接法、pitch 與實體 silicon 結果。
- 200 奈米 W2W、large-chip CoW 或其他新格的具名客戶公布 qualification、good-product yield、throughput 與可靠度。
- Sony、TSMC 或 AMD 若更新既有 production 格，必須分開記錄產品節點、介面世代、合格產出、成本與利用率，不能只寫「hybrid bonding 成長」。
- 台灣公司與客戶文件能對上同一工具、材料或製程，並披露量產與財務足跡。
- 若新格未來一年仍只有試驗車與未具名 customer use，該格應維持 capability，而不是借用舊格 production 升級。
