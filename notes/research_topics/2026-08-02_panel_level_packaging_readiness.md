# 面板排得更滿，成品不一定更便宜：要一起看面積、良率、速度與報廢

<!-- research_topic
topic_id: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-06-25
last_reviewed_at: 2026-08-12
review_due: 2026-09-12
source_type: mixed
publisher: Lam Research
publisher_domain: lamresearch.com
canonical_url: https://newsroom.lamresearch.com/wafer-to-panel-lam-scaling-advanced-packaging-panel-level-processing
source_chain_id: panel-level-packaging-pilot-readiness-20260802
stock_ids:
group_ids: packtest,semiequip,pcb
trigger_type: advanced_packaging_manufacturing_readiness
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C8
base_confidence: medium
confidence_basis: ASE 技術文章與 2026-05-26 正式公告可把 fan-out 架構、chip-first／chip-last 先後及 310x310mm planned production line 分開，SEMI current-standard page 另界定 panel 載體條件；Lam 與 Applied Materials 兩條獨立鏈支持 pilot／設備布局，但仍沒有具名客戶 HVM、同產品 good-package yield／throughput／cost 或可辨識財務貢獻
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: official_panel_processing_readiness_sources_captured
evidence: source_chain:panel-level-packaging-pilot-readiness-20260802
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_area_efficiency_pilot_qualification_hvm_and_financial_stages
evidence: sources:S1,S2,S3
-->

<!-- research_source
source_id: S1
role: company_release
source_kind: document
publisher: Lam Research
title: Lam Research establishes Panel-Level Packaging Center of Excellence
published_at: 2026-05-20
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://newsroom.lamresearch.com/Lam-Research-Establishes-Panel-Level-Packaging-CoE
locator: Salzburg facility、panel-focused wet processing R&D、development／pilot stages、early qualification 與 customer co-development 段落
limitation: 研發中心與 pilot／early qualification 能力不證明具名客戶 HVM、良率、產能、工具訂單或財務貢獻
independence_group: lam-research
-->

<!-- research_source
source_id: S2
role: company_release
source_kind: document
publisher: Lam Research
title: From Wafer to Panel: Scaling Advanced Packaging with Panel-Level Processing
published_at: 2026-06-25
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://newsroom.lamresearch.com/wafer-to-panel-lam-scaling-advanced-packaging-panel-level-processing
locator: key takeaways；roughly 100x100mm package discussion；uniformity、yield、throughput、automation 與 panel-size standards 段落
limitation: 面積效率與 HVM readiness 是設備商的技術與前瞻敘事；未提供客戶線 good-package yield、cycle time、成本、採用量或收入
independence_group: lam-research
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: Applied Materials
title: Applied Materials broadens advanced packaging portfolio with acquisition of NEXX
published_at: 2026-05-03
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-broadens-advanced-packaging-portfolio
locator: pending acquisition、large-area ECD、panel form factors as large as 510x515mm or more 與 closing conditions 段落
limitation: 交易當時仍待完成；公司對 panel transition、served market 與 customer roadmap 的描述不等於 HVM adoption、交易綜效或財務實現
independence_group: applied-materials
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: living_index
publisher: Lam Research
title: Lam Research newsroom
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://newsroom.lamresearch.com/
locator: 2026-08-02 建立的 panel qualification、tool release、customer adoption 與 HVM 結果重查入口
limitation: 新聞索引只用來找到後續文件；HVM readiness 或 customer co-development 不能代替實際 qualification 與量產資料
independence_group: lam-research
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
locator: 2026-08-02 建立的 NEXX closing、panel ECD、customer qualification 與財務揭露重查入口
limitation: 新聞索引不證明交易完成、技術整合、客戶採用或收入；每一節點需回到新文件核對
independence_group: applied-materials
-->

<!-- research_source
source_id: S6
role: company_release
source_kind: document
publisher: ASE
title: The Opportunities and Challenges of FOPLP Technology
published_at: 2025-10-07
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://ase.aseglobal.com/ch/blog/technology/the-opportunities-and-challenges-of-foplp-technology/
locator: PLP 製程優勢、FOCoS Chip First vs Chip Last、Fan-out PLP 實踐與發展及 FOCoS-Bridge panel test-vehicle process 段落
limitation: 公司技術文章可界定自家 fan-out 流程、panel test vehicle 與製造問題，但沒有具名客戶 qualification、連續批次良率、HVM throughput、同產品成本或財務分子
independence_group: ase
-->

<!-- research_source
source_id: S7
role: standard
source_kind: living_index
publisher: SEMI
title: SEMI 3D20 Specification for Panel Characteristics for Panel Level Packaging Applications
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://store-us.semi.org/products/3d02000-semi-3d20-en-specification-for-panel-characteristics-for-panel-level-packaging-plp-applications
locator: current revision 與公開 abstract 中 panel external dimensions、with／without process carrier、thickness、warpage、mass 及 common-equipment rationale
limitation: 公開摘要只界定共同設備所需的物理特性；標準存在不證明任一產品已 qualification、量產、達到經濟良率或採用特定尺寸
independence_group: semi
-->

<!-- research_source
source_id: S8
role: company_release
source_kind: document
publisher: ASE
title: ASE Launches Automated 310mm Panel-Level Packaging to Accelerate AI Innovation
published_at: 2026-05-26
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.aseglobal.com/press-room/310x310/
locator: announcement date、310x310mm automated line、FOCoS／FOCoS-Bridge compatibility、2/2um／8/8um line-space statements 與 expected production in first-half 2027
limitation: 公司公告證實具名平台、線寬能力敘述與前瞻投產目標；不證明截至 2026-08-12 已 production release、完成客戶 qualification、達到穩定良率／throughput／cost 或形成收入
independence_group: ase
-->

<!-- research_source
source_id: S9
role: company_release
source_kind: living_index
publisher: ASE
title: ASE financials and investor information
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://ase.aseglobal.com/about-ase/financials/
locator: 2026-08-12 建立的 monthly revenue、stock-exchange filing、quarterly result、financial report 與 investor information 重查入口
limitation: 財務索引只用來定位後續文件；公司總營收、封裝部門收入或一般先進封裝資本支出都不能代替 310x310 PLP 的具名出貨、收入或毛利
independence_group: ase
-->

<!-- research_source
source_id: S10
role: standard
source_kind: living_index
publisher: SEMI
title: SEMI E181 Specification for Panel FOUP for Panel Level Packaging
published_at:
captured_at: 2026-08-13
accepted_at: 2026-08-13
status: active
url: https://store-us.semi.org/products/e18100-semi-e181-specification-for-panel-foup-for-panel-level-packaging
locator: E181-0526 current revision、Purpose／Scope、510–515mm 與 600mm subordinate standards 清單及 E182 reference
limitation: 公開頁只提供標準摘要與現行 subordinate-standard 清單，未讀取付費全文、公差與驗收方法；清單沒有 310mm 不代表專有 310mm 載具不存在，也不證明任何具名產線已互通或量產
independence_group: semi
-->

<!-- research_source
source_id: S11
role: standard
source_kind: living_index
publisher: SEMI
title: SEMI E182 Specification for Panel FOUP Load Port for Panel Level Packaging
published_at:
captured_at: 2026-08-13
accepted_at: 2026-08-13
status: active
url: https://store-us.semi.org/products/e18200-semi-e182-specification-for-panel-foup-loadport-for-panel-level-packaging
locator: E182-0326 current revision、semiconductor manufacturing equipment load-port interface、Panel FOUP loading／unloading 與 semi-automated／automated mode 段落
limitation: 公開摘要只界定設備端介面角色，未讀取付費全文與各尺寸公差；標準存在不證明 ASE 310x310 line、任一 FOUP 或設備組合已採用、互通或通過產品資格
independence_group: semi
-->

<!-- research_source
source_id: S12
role: standard
source_kind: document
publisher: SEMI
title: SNARF for Doc 7405 — New Standard: Specification for 310mm Square Panel FOUP
published_at: 2025-09-01
captured_at: 2026-08-13
accepted_at: 2026-08-13
status: active
url: https://downloads.semi.org/web/wstdsbal.nsf/b8865fa87d9e7b57882579fb005c3cd7/37743881840e595b88258d29001c7d0a%21OpenDocument
locator: Document 7405 title、310mm rationale／scope、2025-09-26 activity approval、projected 2026-10-01 TC Chapter approval 與 3D20 revision note
limitation: SNARF 證明新標準活動獲准啟動與當時規劃，不是已完成 ballot、TC approval 或正式發布的標準；時程是 projected timetable，不能當成完成承諾或產線相容證據
independence_group: semi
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: Lam 在 2026-05-20 開設的 Salzburg panel center 是 panel-focused wet processing R&D site，公開定位包含 development、pilot、engineering testing 與 early qualification
supporting_source_ids: S1,S2
contrary_source_ids:
as_of: 2026-06-25
basis: S1 與 S2 直接說明 facility scope、pilot lines、customer co-development 與 early qualification
boundary: R&D／pilot／early qualification 不等於客戶 HVM、量產良率、工具訂單或收入
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: Lam 將 panel-level processing 的優點描述為大型封裝的面積利用率與擴展性，同時明列 uniformity、yield、throughput、automation 與 panel-size standards 為轉換難題
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-06-25
basis: S2 key takeaways、wafer-to-panel challenge 與 FAQ 段落逐項列出優點和限制
boundary: 這證實設備商的問題定義，不證明 panel 在客戶線已比 wafer 有較低 good-package cost 或較高經濟良率
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: Applied Materials 於 2026-05-03 公告簽約收購 NEXX 以增加 large-area panel-level ECD 能力，並明示交易仍受一般 closing conditions 約束
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-05-03
basis: S3 的 transaction、technology、form factor 與 expected closing 段落
boundary: 簽約不等於交易已完成或整合成功；510x515mm or more 是公司路線描述，不是全產業已採用的單一標準
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C4
label: inference
status: active
claim: Panel-level packaging 是否具有商業優勢，應以每個合格大型封裝的總成本判斷，而不能只用方形面板比圓形晶圓的幾何利用率判斷
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-08-02
basis: S2 同時揭示 area efficiency 與 uniformity／yield／throughput／standards 約束，S1 顯示技術仍在 pilot／early qualification，S3 顯示設備布局但交易和採用未完成
boundary: 不量化 wafer 與 panel 的成本差、TAM、市占或台灣公司份額；缺少一致的 panel size、good-package yield、cycle time、設備折舊與材料成本
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: Panel-level packaging 已在具名 AI accelerator 客戶進入 HVM，或 universe 內封測、設備與 PCB 公司已取得可辨識量產收入
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: 現有來源是設備商 R&D／readiness、pilot 與交易布局，沒有具名 end product、HVM yield 或台灣公司財務雙向核對
boundary: 不以大型 AI package 趨勢、panel 工具能力、先進封裝身分或方形載板供應能力直接建立訂單關係
verification_needed: 具名客戶產品、panel form factor、qualification、good-package yield、量產節拍，搭配台灣公司料號、出貨與財務貢獻
resolution:
-->

<!-- research_claim
claim_id: C6
label: verified
status: active
claim: Fan-out 是把晶粒嵌入重構載體並以 RDL 把連接延伸到晶粒外的封裝架構；chip-first 與 chip-last／RDL-first 又代表不同先後順序，而 panel 是可承載這些流程的方形或長方形批次格式，三者不是同一個成熟度名詞
supporting_source_ids: S6,S7
contrary_source_ids:
as_of: 2026-08-12
basis: S6 直接分列 chip-first、chip-last、fan-out RDL 與 panel test vehicle，S7 明示許多但非全部 panel applications 包含 fan-out 並把 panel 定義到外形與載體物理特性
boundary: 只界定架構、製程先後與批次載體；不宣稱所有 PLP 都是 fan-out、所有 fan-out 都用 panel，也不比較任一流程的效能、良率或成本
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: ASE 公開的 310x310mm 自動面板線對應 FOCoS／FOCoS-Bridge 平台並列出 2/2um 與 8/8um 線寬／線距能力，但同一頁把新線狀態寫為預計 2027 年進入生產
supporting_source_ids: S6,S8
contrary_source_ids:
as_of: 2026-08-12
basis: S8 直接列出 panel size、compatible platforms、line-space statements 與 expected production in first-half 2027；S6 補足兩種 fan-out 流程與較早的 panel test-vehicle／line-building 位置
boundary: 這證實具名 planned line 與公司所述能力，不證明截至 2026-08-12 已 production release、完成客戶產品資格、達到穩定良率／產出／成本或形成可辨識收入
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C8
label: inference
status: active
claim: 判讀 panel-level packaging 必須同時沿「封裝架構與製程先後」及「面板尺寸、搬運、製造與商用階段」兩條軸前進；ASE 的具名 310x310mm planned line 讓公開成熟度前進到量產規劃，但在 2027 實際投產、客戶資格、連續良率、合格產出與同產品成本出現前，仍不能把面積利用率或 planned production 改寫成已實現的 HVM 成本優勢
supporting_source_ids: S1,S2,S3,S6,S7,S8
contrary_source_ids:
as_of: 2026-08-12
basis: S6 分開 fan-out 與 chip-first／chip-last，S7 固定 panel 物理特性，S8 新增具名 planned line；S1／S2 仍顯示 pilot、qualification readiness 與 yield／throughput 難題，S3 的設備交易仍不等於採用結果
boundary: 本框架不量化 wafer／panel 成本差、TAM、市占或公司份額，也不把 ASE 一條 planned line 外推成全產業量產、客戶採用或台灣供應鏈財務受惠
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C9
label: verified
status: active
claim: 截至 2026-08-13，SEMI E181 current page 把 Panel FOUP 定義為運送與儲存 panel 的載具，並分開界定內外部尺寸、支撐／約束空間及與 load port 共用的參考平面；公開 subordinate standards 列出 510–515mm 與 600mm panel，未列 310mm
supporting_source_ids: S10
contrary_source_ids:
as_of: 2026-08-13
basis: S10 公開 Purpose／Scope 直接固定 transport／store、reference planes、interoperability、support／restrain volumes 與四個現行尺寸／slot subordinate standards
boundary: 這是 SEMI 公開商店頁在捕捉日的完整列名，不含付費全文；未列 310mm 不能解讀為專有載具不存在、技術不可行或 ASE 一定延遲，也不證明清單外沒有尚未發布的草案
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: SEMI E182 current page 把 Panel FOUP load port 定義為半導體製造設備上供 FOUP 裝卸的介面，並明示半自動與自動搬運模式，證明 panel 載具與設備端裝卸介面是兩個需另外對齊的規格層
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-08-13
basis: S11 Purpose 與 Scope 分別固定 equipment-side load port、Panel FOUP loading／unloading、interoperability 目的及 semi-automated／automated mode
boundary: 標準摘要只證明介面責任分層，不證明任一 310mm FOUP、load port、搬運車或 ASE line 已採用同一版本、完成跨廠互通或通過產品放行
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C11
label: verified
status: active
claim: SEMI Doc 7405 SNARF 明列建立 310mm square Panel FOUP 新標準的活動，說明既有 E181 已標準化 515x510mm 與 600x600mm 載具、310mm 仍有標準化需求，並把 2026-10-01 列為 projected TC Chapter approval date
supporting_source_ids: S12
contrary_source_ids:
as_of: 2026-08-13
basis: S12 固定 document number、new-standard title、rationale、scope、2025-09-26 SNARF approval 與 projected timetable，並說 panel 本體尺寸另規劃由 3D20 revision 處理
boundary: SNARF approval 是標準活動獲准啟動，不是 310mm 規格已完成或發布；2026-10-01 是文件中的預定里程碑，不保證 ballot、approval、publication、採用或量產結果
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C12
label: inference
status: active
claim: 閱讀 310x310mm panel line 時，至少要把 panel 本體物理條件、Panel FOUP 載具、設備端 load port／自動搬運，以及整線與客戶產品放行分成四層；ASE planned line 與 SEMI 310mm 標準活動是互補的準備度訊號，任一層都不能替其他層畢業
supporting_source_ids: S7,S8,S10,S11,S12
contrary_source_ids:
as_of: 2026-08-13
basis: S7 固定 panel 本體物理特性，S10 固定載具，S11 固定設備介面，S12 顯示 310mm 共通載具仍在制定活動，S8 則只到 ASE 具名 automated line 與 2027 expected production
boundary: 四層是研究中心整合 SEMI 與 ASE 文件的閱讀框架，不是共同標準；共通標準未完成不代表專有整合線不能先運作，也不能據此判斷 ASE 時程、改機需求、成本或競爭力
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C13
label: unverified
status: active
claim: ASE 310x310mm line 已符合最終發布的 310mm panel／FOUP／load-port 共通標準，完成跨廠牌自動搬運互通、實際 production release、具名客戶 qualification 與穩定 HVM 經濟性
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-13
basis: S8 只揭露 ASE line 格式、平台、能力與 2027 expected production；S12 仍是標準活動文件，S10／S11 的 current public lists 也沒有提供 ASE 310mm adoption 或互通測試
boundary: 不把 automated、310x310、planned production、標準活動或 FOUP／load-port 需求改寫成已互通、已投產、客戶採用、設備訂單、收入、毛利或投資結論
verification_needed: 最終 310mm panel／FOUP／load-port 標準正式發布，ASE 與具名設備／載具對同一版本公布介面採用與互通測試，再由 ASE／客戶揭露 production release、qualification、連續良率、throughput、破損／停機與成本
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: retired
claim_ids: C1,C2,C3,C4
metric: Panel-level packaging 的交易完成、form-factor 標準、客戶 qualification、good-package yield、throughput 與 HVM 狀態
source_ids: S1,S2,S3
watch_source_ids: S4,S5
frequency: event_driven
frequency_detail: 設備商、OSAT、基板商或 AI 平台公布 panel qualification／HVM／standard 時重審
next_check: 2026-08-23
trigger: 具名客戶產品披露 panel size、qualification 與可定位的 good-package yield／throughput，或 NEXX 交易完成並出現整合與出貨證據
invalidation: 量產仍受 panel 標準、翹曲、均勻度、良率或節拍阻擋，pilot 長期無法轉入 HVM，則商業急迫性下修
retired_at: 2026-08-12
retirement_reason: S6／S7 把 fan-out 架構與 panel 物理載體分開，S8 又新增 ASE 具名 310x310mm planned line；舊 T1 的單軸 readiness 由 T3 以製程軸與製造商用軸接續，且 2027 預計投產仍未命中客戶 qualification、good-package yield／throughput 或 HVM trigger
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C5
metric: 台灣封測、設備與 PCB 公司在 panel-level packaging 的具名客戶、料號、量產與財務貢獻
source_ids: S1,S3
watch_source_ids: S4,S5
frequency: quarterly
frequency_detail: 每季法說與財報檢查客戶 qualification、panel 工具／基板出貨、收入占比與毛利
next_check: 2026-10-31
trigger: 台灣公司與客戶對同一 panel 產品或流程完成雙向核對，並揭露量產出貨或財務資訊
invalidation: 公司只描述先進封裝或大尺寸基板機會，未披露 form factor、客戶、qualification 與財務足跡
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C1,C2,C3,C5,C6,C7,C8
metric: Panel flow／form factor、SEMI common-carrier progression、ASE 310x310 line production release、客戶 qualification、good-package yield、throughput、cost 與 HVM 狀態
source_ids: S1,S2,S3,S6,S7,S8
watch_source_ids: S4,S5,S7,S9
frequency: monthly
frequency_detail: 每月先固定 chip-first／chip-last 與 panel size，再核對 planned line、production release、具名客戶批次、良率／throughput／cost 和財務分子；單一線寬或面積數字不替代整線結果
next_check: 2026-09-12
trigger: ASE 或另一具名 OSAT 公布同一 panel platform 的實際 production release，並同時提供客戶 qualification、連續批次 good-package yield／throughput、可靠度或可辨識出貨中的至少一項
invalidation: 2027 投產目標後移、共同載體或搬運條件分裂、良率／節拍／成本無法達標，或 planned line 長期沒有客戶產品與實際製造結果
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C9,C10,C11,C12,C13
metric: 310mm panel 本體×Panel FOUP×load port／自動搬運×整線產品放行四層介面
source_ids: S7,S8,S10,S11,S12
watch_source_ids: S7,S9,S10,S11,S12
frequency: event_driven
frequency_detail: SEMI 更新 3D20／E181／E182／Doc 7405，或 ASE、載具商、設備商、客戶發布 310mm adoption、interoperability、production release、qualification 與 HVM 結果時逐層重審
next_check: 2026-09-12
trigger: 310mm panel、FOUP 與 load-port 標準正式發布，且至少一條具名產線以同一版本公開載具／設備互通、實際投產與客戶產品放行結果
invalidation: 新資料仍只到標準活動、專有尺寸、設備可處理或 expected production，卻沒有發布版本、adoption、互通測試與產品放行；證據留在原層，不得升級 HVM 或公司財務
-->

<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_glossary_for_repeated_terms_no_conclusion_change
evidence: editorial:high_frequency_glossary
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
reason: editorial_plain_language_wave95_panel_cost_four_measures_production_chain_and_six_gate_ladder
evidence: editorial:reader_layer_only_no_claim_source_monitor_or_impact_change
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: separated_fanout_architecture_panel_carrier_and_ase_310x310_planned_production_evidence
evidence: sources:S6,S7,S8
-->
<!-- transition
date: 2026-08-13
from: triaged
to: triaged
reason: separated_310mm_panel_foup_loadport_and_line_release_interfaces_without_thesis_clock_refresh
evidence: sources:S10,S11,S12
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **面板級封裝（Panel-level packaging，PLP）**：用方形或長方形大面板處理多顆封裝，而不是只在圓形晶圓上排版；載體形狀改變不會自動解決良率與成本。
- **圓形晶圓（Wafer）**：半導體製程常用的圓形基板；排入大型方形封裝時，圓周邊緣可能留下較多無法使用的面積。
- **方形面板（Panel）**：面板級製程使用的方形或長方形大載體；可排版面積較完整，但尺寸越大也越難維持平整與均勻。
- **面板載體**：承接重佈線、金屬與封裝結構的大面積基板；材料、厚度與搬運方式都會影響製程結果。
- **扇出封裝（Fan-out）**：把晶片接點經由重佈線延伸到晶粒邊界之外，以容納更多外部連接；它是一種封裝架構，不是面板尺寸。
- **扇出晶片接基板（FOCoS）**：先用扇出重佈線把多顆晶粒連成一個模組，再把模組接到球柵陣列基板的封裝平台；名稱存在不代表已在面板線量產。
- **扇出橋接封裝（FOCoS-Bridge）**：在扇出重佈線中加入局部橋接晶片，讓高密度連線集中在需要的位置；橋接試驗結構不能替代完整產品資格。
- **重構面板**：把已切割晶粒重新排列並以封裝材料固定成可批次加工的面板；它是製造中的中間載體，不一定留在最終產品裡。
- **重佈線層（RDL）**：在晶粒與外部接點之間重新安排電路連線的金屬與介電層；線路能做出來仍要通過對準、缺陷與可靠度驗證。
- **晶片先放（Chip-first）**：先把晶粒放入暫時或永久結構，再形成重佈線；晶粒在包封時移動會增加後續對準難度。
- **線路先做（Chip-last／RDL-first）**：先在載體上形成重佈線，再把晶粒接上；可減少重佈線製作期間的晶粒位移問題，但仍有接合、良率與成本關卡。
- **已知良品晶粒（Known-good die）**：在封裝前已通過指定測試的晶粒；先測過能降低把壞晶粒裝入複雜封裝的風險，不能保證封裝後仍合格。
- **晶粒位移（Die shift）**：晶粒在放置、包封或加熱後偏離原位置；位移超出補償範圍時，通孔或重佈線可能接不到正確接點。
- **線寬／線距（L/S）**：金屬線寬與相鄰線之間的距離；單一最小值只證明圖形能力，不等於整片面板良率或產品已量產。
- **預計投產**：公司對未來生產開始時間的目標；它比只有概念或設備規格更接近商用，但仍不是實際投產、客戶放行或出貨紀錄。
- **面板尺寸標準**：設備、材料、載具與自動化共同採用的長寬與厚度規格；單一公司的可處理尺寸不等於全產業共同標準。
- **面積利用率**：可用來排入產品的面積占載體可用面積的比例；它回答幾何效率，不等於最後合格品比例。
- **理論可排數**：依產品尺寸與版圖估算一片載體最多能放多少顆；尚未扣除製程缺陷、測試失敗與報廢。
- **投入數**：進入指定製程或良率計算的面板、封裝或產品數；比較良率前必須先確認分母定義相同。
- **合格品**：通過指定電性、尺寸與可靠度要求、可以交付的產品；「做出來」與「合格可交付」是兩個不同節點。
- **合格封裝良率（Good-package yield）**：最終合格封裝數占投入封裝數的比例；必須說明測試條件、分母與產品規格才能比較。
- **大面積均勻度（Uniformity）**：面板中央與邊緣的厚度、線寬、清洗、沉積或蝕刻結果是否一致。
- **翹曲**：面板受材料、溫度或應力影響而彎曲；翹曲會干擾曝光、搬運、對準與接合。
- **邊緣控制**：管理面板邊緣的厚度、圖形與缺陷；平均值達標不代表中央與邊緣都合格。
- **缺陷分布**：缺陷在整片面板上的位置與密度；同樣缺陷數若集中在關鍵區域，可能造成不同報廢結果。
- **良率管理**：追蹤缺陷來源、製程漂移、測試失敗與返工，讓合格比例能在連續批次維持穩定。
- **製程週期（Cycle time）**：一片面板從進站到完成指定流程所需的時間；面板較大不代表處理時間一定相同。
- **單位時間產出（Throughput）**：設備或產線每小時真正完成的面板或合格品數；要連同良率、停機與返工一起看。
- **設備利用率**：設備可生產時間中實際投入製造的比例；等待、換線、保養與故障都會壓低有效產出。
- **停機時間**：設備因故障、清潔、保養、調整或等待材料而不能生產的時間。
- **自動搬運**：用機械與控制系統移動、定位及追蹤大面板；尺寸與翹曲變化會增加破損、卡料與定位風險。
- **Panel FOUP（面板載具）**：用來支撐、約束、儲存及運送面板的容器；面板長寬相同，不代表載具外形、槽位與支撐方式已相同。
- **裝卸埠（Load Port）**：製程設備接收 Panel FOUP 並讓面板進出設備的介面；它是設備端規格，不是面板或載具本身。
- **互通性（Interoperability）**：不同載具、設備與搬運系統依同一版本規則正確對接；一條自動線能運作，不等於跨廠牌組合都互通。
- **新標準活動表（SNARF）**：SEMI 用來記錄標準制定理由、範圍與預定時程的文件；活動獲准不等於標準已完成、發布或被產線採用。
- **SEMI E181**：界定 Panel FOUP 基本外形、支撐約束空間與參考平面的標準家族；現行公開尺寸清單不會替未列尺寸證明相容。
- **SEMI E182**：界定 Panel FOUP 與製程設備 load port 裝卸介面的標準家族；介面標準存在不等於具名設備組合已通過互通。
- **SEMI Doc 7405**：310 mm square Panel FOUP 新標準活動的文件編號；本輪看到的是制定活動與時程，不是已發布規格。
- **返工**：產品未一次達標後，仍能重新處理或修復的流程；返工會增加時間、材料與再次失敗的風險。
- **報廢**：產品或整片面板無法再使用而必須丟棄；一片面板排得越多，整片失敗時可能損失越多產品。
- **可靠度**：產品經過溫度、濕度、機械與長時間使用後仍能維持功能；短期測試通過不能替代長期驗證。
- **每顆合格品總成本**：把面板、材料、設備折舊、製程時間、返工與報廢等成本，除以最後可交付的合格品數。
- **電鍍沉積（ECD）**：用電化學方式形成銅等金屬層；大面積處理時要同時控制厚度與跨面板均勻度。
- **薄膜沉積（PVD／CVD）**：用物理或化學方式形成薄膜的製程；設備能處理大面板，不等於厚度與缺陷已達量產要求。
- **蝕刻（Etch）**：選擇性移除材料以形成線路或結構；大面積線寬與深度的一致性會影響後續良率。
- **微影（Lithography）**：把電路圖形轉印到材料表面的製程；大面板曝光、對準與翹曲控制需一起驗證。
- **試產線（Pilot line）**：用來調整製程與做工程測試的小量產線；能試做不等於已具備穩定大量生產能力。
- **客戶資格認證（Qualification）**：客戶依功能、可靠度與製造條件確認產品是否可採用；早期共同開發還不能替代具名產品認證。
- **穩定大量生產（HVM）**：連續生產時同時守住良率、產出速度、可靠度與成本，而不是只完成一次樣品或工程批次。
- **NEXX**：Applied Materials 宣布簽約收購、用來補強大型面板電鍍能力的設備公司；簽約不等於交易完成、整合成功或客戶量產。

### 三句話抓重點

- 「扇出」說明連線如何離開晶粒，「晶片先放／線路先做」說明製程先後，「面板」只說明用哪種大面積載體批次加工；三個詞不能混成同一個成熟度。
- 本輪新證據可確認 ASE 公開一條 310×310 mm 自動線與具名封裝平台，但公司同一頁仍寫成預計 2027 年投產，而不是截至 2026-08-12 已穩定量產。
- 因此方形面板排得更多、線路做得更細或產線已展示，都不能替代具名客戶資格、連續良率、合格產出、可靠度、成本與穩定大量生產證據。

### 為什麼重要

大型人工智慧封裝要把運算晶片、記憶體與輸入輸出晶片連成可交付產品。讀者若把「面板」當成
一種最終封裝，就會漏掉兩個先決問題：晶粒與重佈線按什麼順序接起來，以及加工用面板最後是否
留在產品裡。

圓形晶圓改成方形面板可能減少幾何浪費，卻也把難題放大到整片平整度、晶粒位移、
中央與邊緣一致性、搬運、返工與整片報廢。真正的成本問題不是「一片能排幾顆」，而是「一小時
能穩定交付幾顆合格品，以及為此花了多少材料、設備與失敗成本」。

### 接下來怎麼追

- 先標記資料是在談扇出架構、晶片先放／線路先做，還是只在談圓形晶圓改為方形面板；不要用載體名稱替產品流程補空格。
- 再標記新資料位於研發場域、試產與工程測試、預計投產、具名產品認證、實際量產或財務貢獻哪一關。
- 比較同一產品時，同時核對面板尺寸、理論可排數、投入數、合格品良率、每小時產出、停機、返工、報廢與可靠度。
- 公司映射要讓客戶端的具名產品與供應商端的設備、材料、量產出貨及財務資料互相對上，缺一邊就維持待驗證。

### 想一想

- 同一種扇出封裝若由圓形晶圓改在方形面板加工，改變的是封裝架構、製程先後，還是批次載體？
- 面板一次排得下更多封裝，若晶粒位移、報廢增加或製程變慢，每顆合格品還會更便宜嗎？
- 大面板的平均厚度達標時，中央與邊緣仍可能有哪些翹曲、線寬、清洗與搬運問題？
- 一條產線宣布預計 2027 年投產後，還要看到哪些實際生產放行、具名客戶、連續良率、產出、可靠度與財務資料才算量產成熟？

## 先把兩條軸拆開：封裝做法不等於面板載體

「面板級」最容易被誤讀成一種完整產品。其實讀資料時至少要同時固定兩條軸：第一條是晶粒、
包封材料與重佈線如何組成封裝；第二條是這些步驟在圓形晶圓還是方形面板上批次加工。產品架構
相同時可以更換載體，載體相同時也可能服務不同流程，兩條軸都不能替另一條證明量產。

| 本文兩軸地圖 | 它回答什麼 | 例子 | 本輪可確認 | 不能直接推成 |
|---|---|---|---|---|
| 1. 封裝架構 | 晶粒接點如何延伸並和其他晶粒或基板連接？ | 扇出重佈線、扇出晶片接基板 | ASE 技術文章把扇出核心放在重佈線與晶粒整合 | 只要使用方形面板就一定是同一種扇出產品 |
| 2. 製程先後 | 晶粒先放，還是重佈線先做？ | 晶片先放、線路先做 | ASE 公開分列兩條流程及各自限制 | 一條流程的線寬能力可替另一條流程證明良率 |
| 3. 批次載體 | 多顆封裝在什麼外形、厚度與搬運條件下共同加工？ | 圓形晶圓、310×310 mm 或更大面板 | SEMI 把外形、厚度、翹曲、重量與有無製程載體列為共同設備條件 | 面板尺寸本身就是最終封裝、基板材料或客戶產品 |
| 4. 商用階段 | 流程和產線是否已從能力走到客戶產品與穩定製造？ | 試驗結構、預計投產、實際投產、客戶放行 | ASE 已公開具名 310×310 mm planned line，目標 2027 年投產 | 自動線、平台相容或預計投產等於目前已有 HVM、出貨與收入 |

### 再用兩條簡化流程看先後順序

- **晶片先放**：先放置已知良品晶粒，再包封成重構載體，量測或補償晶粒位移後製作重佈線，最後才進入外部接點、切割與產品測試。
- **線路先做**：先在載體上完成重佈線，再把晶粒接上並完成包封與後續組裝；它降低重佈線製作期間的晶粒位移風險，卻沒有消除接合、封裝後測試、良率與成本問題。
- **改用面板**：兩條流程都可能在方形面板上做；改變的是批次外形與整線設備條件，不會自動決定最終產品是否仍要接到封裝基板。

這三條是依一手來源整理的入門地圖，不是完整製程配方。不同產品還會增加多層重佈線、通孔、
橋接晶片、基板、散熱與測試步驟；文章只用它來防止「流程名稱、載體尺寸與商用階段」互相冒充。

## 310×310 不是只改一個尺寸：面板、載具、裝卸口與整線是四層

可以把自動化面板線想成行李系統：面板是行李，Panel FOUP 是裝行李的箱子，load port 是設備的
裝卸口，整條產線則是把箱子送到每一站、完成加工並讓產品放行的系統。行李尺寸相同，不代表箱子、
裝卸口與整套搬運系統已經通用；同樣地，公司公布 310×310 mm 面板線，也不能自動補成所有設備
已採用共同載具、跨廠牌互通或客戶產品已量產。

| 本文四層介面 | 它固定什麼 | 本輪一手證據到哪裡 | 尚不能證明什麼 |
|---|---|---|---|
| 1. 面板本體 | 長寬、厚度、翹曲、重量及有無製程載體 | SEMI 3D20 公開摘要界定這些物理條件；ASE 公布 310×310 mm planned line | 相同長寬不代表材料、翹曲、公差與各站製程窗口相同 |
| 2. Panel FOUP 載具 | 槽位、面板位置、支撐／約束空間、載具外形與識別 | E181 current page 定義運送、儲存與共用參考平面；現行公開 subordinate standards 列 510–515 mm 與 600 mm | 清單未列 310 mm 不代表專有載具不存在，也不證明 ASE 使用哪一版載具 |
| 3. Load Port 與搬運 | FOUP 如何在製程設備上裝卸，以及半自動／自動系統如何交接 | E182 current page 把設備端 load port 與 Panel FOUP 分開，並涵蓋半自動與自動模式 | 標準摘要不證明 310 mm FOUP、設備、機器人或搬運車已完成跨廠牌互通 |
| 4. 整線與產品放行 | 各站版本、追溯、破損／卡料、停機、製程結果及客戶 qualification | ASE 表示 310×310 mm 自動線預計 2027 上半年投產 | Automated 或 expected production 不等於實際 production release、客戶放行、HVM 良率與成本 |

### 「正在制定」離「整線量產」還有五個動詞

SEMI Doc 7405 的 SNARF 很適合用來辨認標準新聞的動詞。文件顯示 310 mm square Panel FOUP 的
**標準活動已獲准啟動**，並列出槽數、面板位置、FOUP 外形、支撐空間、機械手臂排除空間、port 與
識別標籤位置等預定範圍；文件也把 2026-10-01 寫成預定的技術委員會核准日。這些資訊能證明需求
與制定工作存在，卻不能提前把未來里程碑改寫成完成結果。

| 五個動詞 | 真正完成什麼 | 本輪狀態 | 不能跳到哪裡 |
|---|---|---|---|
| 1. 啟動活動 | 技術委員會接受制定問題、範圍與工作小組 | Doc 7405 SNARF 已記錄 2025-09-26 activity approval | 活動獲准不是規格內容已定稿 |
| 2. 核准草案 | 草案經 ballot 與技術委員會程序取得核准 | 文件只列 2026-10-01 projected date，本輪沒有完成證據 | 預定日期不是核准承諾 |
| 3. 發布標準 | 可引用的版本正式成為 published standard | 本輪未看到 310 mm Panel FOUP 正式列入 E181 current subordinate standards | 草案或 SNARF 不能當最終尺寸、公差與驗收規則 |
| 4. 採用與互通 | 載具、load port、設備與搬運系統採用同一版本並通過組合測試 | 本輪未公開 ASE 310 mm 的版本化採用與跨廠牌矩陣 | 標準發布也不保證每一條線立即採用 |
| 5. 整線產品放行 | 同一產品在實際產線通過製程、搬運、可靠度與客戶資格 | ASE 仍是 2027 expected production；沒有具名客戶放行 | 互通測試不能替代產品良率、產出、成本與收入 |

反過來也不能說「標準尚未完成，所以 ASE 一定無法投產」。公司可用專有 FOUP、load port 與整線
控制先行，只是公開資料尚不足以判斷是否採用未來共同標準、是否需要改機或是否能跨廠牌互換。
研究中心因此同時保留兩條可能路徑，不替產線時程、成本與競爭力選邊。

## 先用四把尺拆開「更便宜」

| 本文四把尺 | 它先回答什麼 | 最簡單的關係 | 容易忽略什麼 | 不能直接推成 |
|---|---|---|---|---|
| 1. 面積利用率 | 一片載體有多少面積真的排進產品？ | 可排產品面積 ÷ 載體可用面積 | 產品尺寸、邊緣留白與不同排版規則 | 面積用得滿，不等於做出的產品都合格 |
| 2. 合格封裝良率 | 投入後最後有多少產品可交付？ | 最終合格封裝數 ÷ 投入封裝數 | 缺陷分布、測試條件、返工與可靠度 | 幾何效率較高，不等於最終良率較高 |
| 3. 單位時間合格產出 | 一小時真正做出多少合格品？ | 每小時完成面板數 × 每片可排數 × 合格封裝良率 | 製程週期、停機、換線、搬運與設備利用率 | 面板較大，不等於每小時合格產出較高 |
| 4. 每顆合格品總成本 | 每交付一顆合格品，實際付出多少？ | 面板、材料、折舊、時間、返工與報廢成本 ÷ 最終合格品數 | 產能利用、整片損失、長期可靠度與重複生產 | 其中一把尺改善，不等於總成本一定下降 |

四把尺要按順序接起來：排得下更多，只增加理論機會；做得良、做得快且失敗成本受控，才可能
降低每顆合格品總成本。這是本文的成本讀法，不是跨公司的成本比較、價格預測或投資排序。

## 再看五個生產關卡如何接力

| 本文五個生產關卡 | 先回答什麼 | 主要接力角色 | 過不了會怎樣 | 本輪可確認到哪裡 |
|---|---|---|---|---|
| 1. 載體與共同尺寸 | 面板的長寬、厚度、材料與載具能否被整條產線共同處理？ | 面板／基板、材料、設備與自動搬運團隊 | 每站可處理尺寸不同，轉站、搬運與良率無法穩定 | SEMI 已固定外形、厚度、翹曲與重量等共同條件；ASE 另採 310×310 mm，仍不能把單一尺寸當成全產業唯一標準 |
| 2. 圖形、金屬與均勻度 | 中央與邊緣的曝光、沉積、蝕刻、清洗與線寬能否一起達標？ | 微影、電鍍、薄膜、蝕刻、清洗與量測設備 | 平均值看似合格，局部產品仍因厚度或圖形偏差失敗 | ASE 公開平台線寬／線距能力，設備商也列出多種製程入口；沒有客戶線跨面板分布與良率相關性 |
| 3. 翹曲、搬運與缺陷 | 大面板能否保持平整、乾淨並在各站安全移動？ | 材料、載具、自動化、製程整合與維修團隊 | 卡料、破損、定位偏差或整片缺陷讓理論可排數失去意義 | 公開資料把自動化與大面積製程列為轉換難題；沒有停機與報廢數據 |
| 4. 封裝整合、測試與認證 | 完整封裝能否通過電性、尺寸與長期可靠度？ | 封測、測試、產品客戶與可靠度團隊 | 製程做得出來，成品仍不能交付或需要大量返工 | ASE 已把 310×310 mm 線對到 FOCoS／FOCoS-Bridge 平台，但沒有具名客戶產品認證結果 |
| 5. 良率、產出與財務 | 合格品比例、每小時產出與總成本能否在連續批次維持？ | 製造營運、設備維護、品質、客戶與財務團隊 | 技術可做卻產量不足、成本過高或無法形成重複收入 | 沒有具名產品的合格品良率、產出速度、成本、出貨或收入 |

五個關卡是接力關係：前一關達標不會替下一關畢業。這是本文用來找資料與分責任的地圖，不是
完整製程規格、供應商名單、訂單判定或公司快慢排名。

## 最後用六關分開研發能力與收入

| 本文六關 | 這一關要證明 | 本輪公開資料 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 研發場域與設備能力 | 有可處理大面板的場域、工具與製程入口 | Lam 開設面板濕製程研發中心；Applied 簽約收購 NEXX；ASE 公開 310×310 mm 自動線 | NEXX 交易完成、工具整合與 ASE 實際 production release | 研發中心、簽約或自動線展示不等於客戶已認證、穩定量產或形成收入 |
| 2. 試產與工程測試 | 製程能在試產線重複運作並留下缺陷與量測結果 | Lam 場域涵蓋試產與工程測試；ASE 公開平台相容與線寬／線距能力 | 同一產品的重複批次、跨面板分布、停機、返工與報廢資料 | 平台與圖形能力不等於具名產品已完成工程批次或製程整合 |
| 3. 早期共同開發與認證 | 客戶把目標產品帶入早期測試，開始核對製程條件 | Lam 將客戶共同開發與早期認證列入場域定位 | 具名客戶、產品、面板尺寸、測試條件與結果 | 未具名的早期認證能力不等於產品已通過資格認證 |
| 4. 共同尺寸與具名產品認證 | 設備、材料與客戶對上同一面板規格，產品通過功能與可靠度 | ASE 已把 310×310 mm 線對到 FOCoS／FOCoS-Bridge，但頁面仍寫預計 2027 年投產 | 客戶與製造端共同揭露產品、面板規格、認證結果與 production release | 平台相容、線寬能力或預計投產不是客戶產品認證 |
| 5. 穩定大量生產 | 良率、每小時產出、停機、返工、可靠度與成本能持續達標 | 未公開；ASE 的 2027 是前瞻目標 | 具名產品的實際投產日、連續批次良率、產出、設備利用與可靠度 | 產線建成、預計投產、樣品或工程批次不等於穩定大量生產 |
| 6. 重複出貨與形成收入 | 供應商產品或服務可重複交付並反映在財務 | 未公開 | 客戶與供應商雙向核對料號、量產出貨、收入或毛利 | 製程需要某類設備、材料或基板不等於台灣公司已受惠 |

本輪資料讓成熟度從設備商的研發／試產能力前進到 ASE 具名 310×310 mm 平台與 2027 投產目標，
但這只把第 4 關的「尺寸與平台」補了一部分；客戶產品認證仍缺，第 5～6 關的實際量產、連續
良率、出貨與財務也沒有證據。六關是本文的查證順序，不是共同產業標準，也不替公司建立量產
名次、訂單、份額或投資排序。

## 來源與證據邊界

- [Lam：Panel-Level Packaging Center of Excellence](https://newsroom.lamresearch.com/Lam-Research-Establishes-Panel-Level-Packaging-CoE)
- [Lam：From Wafer to Panel](https://newsroom.lamresearch.com/wafer-to-panel-lam-scaling-advanced-packaging-panel-level-processing)
- [Applied Materials：pending NEXX acquisition and panel-level ECD](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-broadens-advanced-packaging-portfolio)
- [SEMI 3D20：panel characteristics public abstract](https://store-us.semi.org/products/3d02000-semi-3d20-en-specification-for-panel-characteristics-for-panel-level-packaging-plp-applications)
- [ASE：fan-out、chip-first、chip-last 與 panel test vehicle](https://ase.aseglobal.com/ch/blog/technology/the-opportunities-and-challenges-of-foplp-technology/)
- [ASE：310×310 mm panel line and first-half 2027 production target](https://www.aseglobal.com/press-room/310x310/)
- [SEMI E181：Panel FOUP current-standard page](https://store-us.semi.org/products/e18100-semi-e181-specification-for-panel-foup-for-panel-level-packaging)
- [SEMI E182：Panel FOUP Load Port current-standard page](https://store-us.semi.org/products/e18200-semi-e182-specification-for-panel-foup-loadport-for-panel-level-packaging)
- [SEMI Doc 7405：310mm Square Panel FOUP 新標準活動表](https://downloads.semi.org/web/wstdsbal.nsf/b8865fa87d9e7b57882579fb005c3cd7/37743881840e595b88258d29001c7d0a%21OpenDocument)

Lam、Applied Materials 與 ASE 對產品優勢與量產準備都有商業立場；SEMI 可補 panel、FOUP 與
load port 的共同介面責任，卻不替任何公司驗證產品，SNARF 也只證明標準活動已啟動。本文只把直接揭露的架構、場域、標準範圍、交易
狀態與前瞻投產目標標成已證實；「面板級封裝已更便宜」、「2027 目標已完成」與「台灣公司已
取得量產收入」均未被當成事實。

## 影響路由

<!-- impact
group_id: packtest
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-31
rationale: OSAT 可能承擔 panel process integration、良率與可靠度，但本輪沒有 universe 公司具名 HVM 產品與財務證據
evidence_boundary: 先進封裝產能、fan-out 能力或大型 AI package 討論不等於 panel-level 客戶 qualification、訂單或毛利
-->

<!-- impact
group_id: semiequip
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-31
rationale: ECD、PVD、CVD、etch、clean、lithography、metrology 與 automation 都是 panel 工具入口，但具名證據集中在 Lam、Applied 與 NEXX
evidence_boundary: 製程需要某類設備不等於任一台灣設備商能處理目標 panel size、已通過 qualification 或取得量產收入
-->

<!-- impact
group_id: pcb
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-31
rationale: 大型基板與 panel form factor 可能改變載板材料、尺寸與製程路由，但尚無 universe PCB／CCL 公司具名採用證據
evidence_boundary: 方形基板、ABF 載板或大尺寸板能力不能自動等同先進 panel-level packaging 量產供應
-->

## 下一個可證明／否定的節點

- NEXX 交易完成與實際整合結果，而不是沿用簽約日的前瞻敘述。
- ASE 310×310 mm 線從「預計 2027 年投產」前進到可定位的 production release、首批具名產品與客戶資格結果，而不是只更新設備或線寬規格。
- 具名人工智慧封裝或委外封測廠公布面板尺寸、客戶資格認證、合格封裝良率、單位時間產出與可靠度。
- 設備、材料與基板公司對同一客戶面板流程完成雙向核對，並出現量產及財務資料。
- 若面板尺寸標準長期分裂、試產無法進入穩定大量生產，或每顆合格品成本不優於晶圓路徑，研究優先級應下修。
