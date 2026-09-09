# 2026-09-10 機構市場情報：場址、資金與記憶體成本

三題依研究前凍結順序完成，補進既有液冷、現金回收與記憶體文章。
各篇「9月10日機構情報」提供更新、來源、反方與待查問題。
本輪是指定主題的人工抽樣，沒有重查全站公司筆記或新增台廠受惠關係。
原主命題的到期警示仍有效，新查到的支線資料不代替原命題複核。

<!-- research_radar
schema_version: 2
radar_id: RADAR-2026-09-10-01
as_of: 2026-09-10
next_review: 2026-09-17
status: active
method: 先由高盛、Morgan Stanley與S&P官方公開研究提出問題，再用公司原始文件核對事實與反方。三題均補進既有文章，分清預測、公司計畫與實績；本輪為定向抽樣，不代表全站已更新或台灣公司已受惠。排序只決定本輪研究順序
selection_cycle_id: RS-2026-09-10-01
-->

<!-- research_candidate
candidate_id: RC-INSTITUTION-SITE-CONSTRAINTS
rank: 1
title: 場址供電、用水與液冷驗收
group_ids: thermal,powersupply
reader_group_questions: thermal => 冷卻方案在這個場址能否同時滿足用水、耗電與維護要求？ | powersupply => 電力從哪裡來、何時能接電，會不會延後設備啟用？
reader_question: 資料中心準備擴建時，接電與用水條件會怎樣改變散熱設備的要求？
reader_starting_point: 高盛把場址環境列為限制，微軟Pecos計畫則提出表後發電與閉式冷卻。目前還缺實際運轉的用水、耗電及驗收結果，不能由計畫推成台廠訂單。
reader_terms: 表後發電 => 在用戶端由共址電源先供電，仍須核對接電與運轉安排 | 閉式冷卻 => 冷卻水在迴路內循環，節水範圍仍要看初次充填與運轉條件 | 場址驗收 => 在實際機房條件確認系統是否達到約定要求
reader_next_step: 先讀文章的9月10日更新，再由Microsoft Texas官方進度入口查Pecos是否已有啟用、實際能耗與用水資料。
priority: p1
knowledge_value: high
status: expand_existing
evidence_posture: research_grade
why_now: 高盛9/1分析與Microsoft6/22原始場址計畫，可把既有液冷研究從設備容量延伸到供電和水電取捨。
knowledge_gain: 已核對兩條發布鏈並分清分析、計畫及缺少的實績；新內容補進液冷文章，既有圖譜只供背景，未新增供應商財務線。
first_rejection: 若只有全球需求預測而無場址與冷卻條件，便不把省水或缺電外推為CDU規格與台廠订单。
next_evidence: 核對高盛原稿及Microsoft Pecos原始公告，分清規劃、通電、穩態用水與實際驗收；找後續官方營運入口。
next_check: 2026-10-10
route: expand_existing_article
article_topic_id: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER
graph_id: liquid-cooling
sources: Goldman Sachs 9/1官方逐字稿 => https://www.goldmansachs.com/insights/goldman-sachs-exchanges/the-outlook-for-data-center-power-demand-as-ai-token-use-grows | Microsoft 6/22 Pecos原始計畫 => https://blogs.microsoft.com/blog/2026/06/22/powering-the-next-wave-of-ai-expanding-capacity-with-our-new-datacenter-in-pecos/ | Microsoft Texas進度入口 => https://local.microsoft.com/communities/americas/greater-san-antonio/
-->

<!-- research_candidate
candidate_id: RC-INSTITUTION-AI-FUNDING
rank: 2
title: AI資本支出、融資義務與現金回收
group_ids: serverodm,pcb,powersupply,thermal
reader_group_questions: serverodm => 客戶的建設承諾何時轉成可核對的交付與收款？ | pcb => 採購規格與驗收時程是否有客戶及公司的雙向證據？ | powersupply => 客戶的供電投資是計畫、已交付設備，還是已支付現金？ | thermal => 融資或租賃安排改變後，散熱設備驗收和付款條件是否改變？
reader_question: AI建設支出持續增加時，公司能否收回現金，要從哪幾份資料核對？
reader_starting_point: S&P預測指定公司的現金流承壓，微軟則提供正自由現金流指引。目前還缺相同期間與定義的調節，不能只用正負號判定哪份預測錯誤。
reader_terms: CapEx => 公司披露的資本支出，可能含現金購置與租賃 | FCF與FOCF => 不同發布者使用的現金流指標，須先核對公式與期間 | 租賃分類 => 融資與營業租賃的呈現不同，可能改變支出標題
reader_next_step: 先讀9月10日的對帳表；下一份Microsoft法說公布後，同看期間、現金購置、租賃付款與現金流指引，再對照S&P原情境。
priority: p1
knowledge_value: high
status: expand_existing
evidence_posture: research_grade
why_now: S&P Ratings8/27機構展望與Microsoft7/29公司指引提供待對帳分歧，可補上融資義務、會計分類與變現條件。
knowledge_gain: 已核對母體與預測期限並建立季度檢查表；未取得完整模型，不把兩份前瞻資訊當成同口徑實績，也不宣稱所有公司已出現融資惡化。
first_rejection: 若無法區分機構模型、公司已報現金流及未來義務，或只剩支出大數字，就不宣稱融資惡化已發生於所有公司。
next_evidence: 核對S&P發布稿的公司集合及預測口徑，再以官方公司財報交叉讀現金支出、租賃與自由現金流邊界。
next_check: 2026-10-31
route: expand_existing_article
article_topic_id: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION
graph_id: ai-capex-cash-conversion
sources: S&P Ratings 8/27官方研究發布稿 => https://press.spglobal.com/2026-08-27-AI-Infrastructure-Investment-To-Exceed-1-3-Trillion-By-2027,-S-P-Global-Ratings-Says | Microsoft 7/29官方法說 => https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4 | Microsoft IR後續文件入口 => https://www.microsoft.com/en-us/investor/default
-->

<!-- research_candidate
candidate_id: RC-INSTITUTION-MEMORY-COSTS
rank: 3
title: 記憶體成本、供應優先序與下游利潤率
group_ids: memory,serverodm
reader_group_questions: memory => 公司賣的是哪種記憶體或控制器，售價、出貨與毛利率是否一起改善？ | serverodm => 記憶體成本和取得供應能力，如何影響系統交付、售價與利潤率？
reader_question: 記憶體漲價時，哪些買方拿得到貨，又能把多少成本轉給客戶？
reader_starting_point: 機構提出買方採購分化，HP季報則顯示售價上升與毛利率承壓並存。目前還缺多家買方及台廠同口徑證據，不能將單一公司的情況推到全族群。
reader_terms: ASP => 平均售價，也受產品組合與匯率影響 | 毛利率 => 收入扣除銷售成本後占收入的比例，不等同毛利金額 | 成本轉嫁 => 以售價或條件調整抵銷投入成本上升
reader_next_step: 先讀9月10日更新中的HP反方與三類公司問題；取得新財報時按同產品、同期間比較成本、售價、出貨及利潤。
priority: p2
knowledge_value: high
status: expand_existing
evidence_posture: research_grade
why_now: Morgan Stanley6/8與S&P MI7/28文章提供研究框架，HP8月申報補上較新的買方事實及供應改善反方，可避免只寫短缺利多。
knowledge_gain: 已核對HP季度同比與毛利率含義；按晶片、模組/控制IC及系統買方分開研究，未把HBM短缺泛化成台股記憶體全部受惠。
first_rejection: 若沒有下游公司成本及售價轉嫁的原始揭露，就只保留機制觀察；不能由HBM短缺推全族群受惠。
next_evidence: 核對兩機構原文並找HP或Dell最新官方財報，檢查零件成本、產品售價與利潤的原說法；分清HBM、DRAM與NAND。
next_check: 2026-10-01
route: expand_existing_article
article_topic_id: MI-2026-08-02-AI-MEMORY-HIERARCHY
graph_id: ai-memory-hierarchy
sources: Morgan Stanley 6/8公開研究背景 => https://www.morganstanley.com/insights/podcasts/thoughts-on-the-market/high-cost-of-AI-memory-shawn-kim | S&P Market Intelligence 7/28分析 => https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/behind-ai-boom-electronics-supply-side-constraints | HP截至7/31季度10-Q => https://www.sec.gov/Archives/edgar/data/47217/000004721726000051/hpq-20260731.htm | HP8/26官方財報稿 => https://www.hp.com/us-en/newsroom/press-releases/2026/hp-inc-reports-fiscal-2026-third-quarter-results.html
-->

