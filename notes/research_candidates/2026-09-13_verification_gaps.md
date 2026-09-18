# 故障隔離、模擬與玻璃核心：下一份證據要補什麼

本輪先處理到期追蹤，未為湊篇數新增文章。三題由該輪一手來源初查產生，已另行提交
選擇帳本，供下一次深入驗證；初查發現與未完成事項如實保存，不把這份帳本追認成研究前
就知道的結果。排序依可回查證據、可證偽性、知識增量及台灣產業責任角色安排，不是投資排序。

既有 Section 301、800VDC、Q2 文件及 PCIe 6 文章另做定向更新；9/10 三篇交付案例仍在
研究中心，不重複建文。原雷達與選擇歷史保留。

<!-- research_radar
schema_version: 2
radar_id: RADAR-2026-09-13-01
as_of: 2026-09-13
next_review: 2026-09-25
status: active
method: 到期monitor的一手來源初查產生三個未完成問題，先凍結再安排後續深研。SSCB按具名測試可證偽性及電源角色居前，HBFSim按方法增量次之但不採待核倍率，玻璃核心因多為既有框架重述而等待客戶結果；全部watch，不用來源篇數或公司logo當独立證據。
selection_cycle_id: RS-2026-09-13-01
-->

<!-- research_candidate
candidate_id: RC-800V-SSCB-FAULT-ISOLATION
rank: 1
title: 800V固態斷路器的故障隔離與選擇性保護
group_ids: powersupply,power
reader_group_questions: powersupply => 同一供電系統遇到故障時，哪一層負責隔離且維持其餘負載？ | power => 功率元件的型號與故障測試，如何對上系統驗收要求？
reader_question: 能提高供電效率的元件，是否也能安全切斷系統故障？
reader_starting_point: Infineon與SolarEdge合作把固態斷路器的故障隔離和電力轉換分開。目前還缺同型號實測及客戶驗收，合作消息不能當成部署或收入。
reader_terms: 固態斷路器 => 用功率半導體控制電流通斷的保護裝置 | 選擇性保護 => 故障時按設計隔離對應區段而非讓全系統斷電 | 故障包絡 => 測試涵蓋的電壓電流及故障時間條件
reader_next_step: 先找同型號同版本的故障測試與客戶驗收，確認隔離責任後才追部署數量和收入。
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: 到期追蹤初查發現Infineon9/9與SolarEdge合作把SSCB故障隔離與SST轉換分開；台灣電源及功率元件角色相關但沒有同產品實測和財務共同鍵，先凍結未來深研問題而非追認商業成功。
knowledge_gain: 區分電力轉換、故障隔離與末端降壓，建立可重用的保護責任及測試邊界；合作稿與引述公司同一消息鏈，不計為兩份獨立驗收。
first_rejection: 若仍只有合作稿或微秒級設計目標而沒有具名型號與可回查測試，就不另寫重複文章或新增公司受惠線。
next_evidence: 取得同一SSCB型號與版本的電壓故障包絡及選擇性保護實測，核對客戶驗收與可比器件或替代拓撲；之後才追部署分母和收入。
next_check: 2026-09-30
route: watch_only
article_topic_id:
graph_id:
sources: Infineon9/9原始合作稿 => https://www.infineon.com/press-release/2026/infpr202609-138 | OCP配電責任與後續工作入口 => https://www.opencompute.org/community/power-distribution
-->

<!-- research_candidate
candidate_id: RC-HBFSIM-MODEL-VALIDATION
rank: 2
title: HBFSim的模擬、校準與外部驗證邊界
group_ids: memory,ipdesign
reader_group_questions: memory => 文中的真實裝置是一般儲存裝置還是已交付的HBF樣品？ | ipdesign => 控制器與模型的參數如何由未參與擬合的工作負載驗證？
reader_question: 模擬器的結果，要補哪些驗證才能用來理解真實記憶體？
reader_starting_point: HBF追蹤初查找到研究者發布的HBFSim模型，模擬與校準值得分開理解。目前還有摘要倍率待核，且沒有實體HBF樣品與外部驗證結果。
reader_terms: 模擬 => 用模型與假設重現部分系統行為 | 校準 => 用已知資料調整模型參數 | 外部驗證 => 用未參與調整的資料檢查模型能否成立
reader_next_step: 先對齊作者原始紀錄與倍率，再查未參與擬合的工作負載；不把NVMe校準當成HBF樣品測試。
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: 到期HBF追蹤初查找到9/9研究者HBFSim v1；模擬與校準的學習增量高，但摘要倍率有待核差異且沒有實體HBF樣品，先保留方法候選。
knowledge_gain: 把研究者方法、模型擬合、可重現運行與真實晶片分層；9/18已核對v1 PDF引用頁與README，但摘要倍率和正文秒數仍未對齊，未取得完整原始run或重跑程式，不採效能點估計。
first_rejection: 若未取得原始run或作者勘誤便無法對齊秒數與倍率，或只有擬合點沒有外部驗證，就不發布效能點估計或HBF硬體受惠結論。
next_evidence: 先核對版本化PDF與作者原始run及勘誤，再分開NVMe校準與HBF模型參數，要求未參與擬合的驗證工作負載和實體裝置邊界。
next_check: 2026-09-25
route: watch_only
article_topic_id:
graph_id:
sources: 研究者HBFSim v1 => https://arxiv.org/html/2609.09800v1 | SK hynix9/9系統共同設計策略 => https://news.skhynix.com/en/future-forum-2026/
-->

<!-- research_candidate
candidate_id: RC-GLASS-CORE-CUSTOMER-RELEASE
rank: 3
title: 玻璃核心從展示到客戶資格與製造結果
group_ids: pcb,packtest,material
reader_group_questions: pcb => 玻璃是在基板核心還是別的位置，設計與製造要求如何不同？ | packtest => 同一封裝產品有沒有客戶資格和連續批次良率？ | material => 玻璃只是暫時承載還是留在成品內，對應哪一種材料結果？
reader_question: 看到玻璃基板展示後，如何確認它真的走入客戶產品？
reader_starting_point: 三星電機展稿說明玻璃核心與導孔加工，既有研究已區分載板與暫時承載用途。目前還缺同一封裝產品的客戶資格及製造結果，展示不能當成量產。
reader_terms: 玻璃核心 => 作為封裝基板結構核心的玻璃 | 暫時承載 => 製程中支撐材料而不一定留在成品 | 客戶資格 => 具名客戶依要求完成特定產品版本的驗證
reader_next_step: 找同一封裝產品的客戶資格、連續批次良率與量產日期，先分清玻璃的用途再比較。
priority: p2
knowledge_value: medium
status: watch
evidence_posture: preliminary
why_now: Samsung Electro-Mechanics9/10展稿新增玻璃核心與導孔加工展示，現有主題已分carrier與glass-core；知識重複較多，等待客戶資格或製造結果再深化。
knowledge_gain: 只有新客戶或製造共同鍵才會超越既有玻璃角色地圖；公司展稿與材料供應商用途說明不是互相替客戶資格背書。
first_rejection: 若仍只有展品或單站加工能力，未有同一封裝產品的客戶資格及量產结果，就不另立文章或將carrier出貨算成glass-core採用。
next_evidence: 取得同一glass-core封裝產品與版本的客戶資格及製造結果，逐項分開carrier與interposer角色，核對連續批次良率及量產時間而非展會日期。
next_check: 2026-09-30
route: watch_only
article_topic_id:
graph_id:
sources: Samsung Electro-Mechanics9/10展稿 => https://samsungsem.com/global/newsroom/news/view.do?id=10522 | Corning玻璃用途入口 => https://www.corning.com/worldwide/en/products/advanced-optics/product-materials/semiconductor-laser-optic-components/semiconductor-glass-wafers.html
-->

## 9月18日回查

三題維持原凍結順位與拒絕條件，不以本次複核重新選題。HBFSim 已取得 17 頁 v1 PDF，
只渲染引用及相鄰頁；摘要、實驗章節和作者 README 的倍率與秒數仍有待作者解釋的差異。
核對過算式不代表模型已被外部驗證，更不代表實體 HBF 樣品表現，所以繼續觀察，
9/25 再找原始運行紀錄或勘誤。SSCB 和玻璃核心仍依原定 9/30 找具名產品測試與客戶資格，
未取得新證据便不新增公司受惠線。原選題理由及來源發布日保留。
