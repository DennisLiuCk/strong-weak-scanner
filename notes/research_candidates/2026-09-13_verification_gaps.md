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
next_review: 2026-10-19
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
next_check: 2026-10-21
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
reader_starting_point: HBF追蹤已找到HBFSim新版與部分作者原始紀錄，模擬與校準可以分開核對。目前還缺可配對的完整運行紀錄，倍率未對齊，也沒有實體HBF樣品與獨立外部驗證結果。
reader_terms: 模擬 => 用模型與假設重現部分系統行為 | 校準 => 用已知資料調整模型參數 | 外部驗證 => 用未參與調整的資料檢查模型能否成立
reader_next_step: 先對齊作者原始紀錄與倍率，再查未參與擬合的工作負載；不把NVMe校準當成HBF樣品測試。
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: 到期HBF追蹤初查找到9/9研究者HBFSim v1；模擬與校準的學習增量高，但摘要倍率有待核差異且沒有實體HBF樣品，先保留方法候選。
knowledge_gain: 把研究者方法、模型擬合、可重現運行與真實晶片分層；10/8已核v3、v0.1.1與固定proof及reference原始紀錄，仍缺相同共同鍵的fast原始run，舊倍率與秒數未對齊，沒有重跑或外部驗證，不採效能點估計。
first_rejection: 若未取得原始run或作者勘誤便無法對齊秒數與倍率，或只有擬合點沒有外部驗證，就不發布效能點估計或HBF硬體受惠結論。
next_evidence: 先核對版本化PDF與作者原始run及勘誤，再分開NVMe校準與HBF模型參數，要求未參與擬合的驗證工作負載和實體裝置邊界。
next_check: 2026-10-21
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
next_check: 2026-10-19
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

## 10月4日回查：維持原排序，區分未成熟與未完成

- **SSCB，順位1維持 watch**：重讀 Infineon 9/9 合作稿，仍未取得同型號故障包絡、原始波形與客戶驗收。另見 [9/29 Eaton SST 公告](https://www.infineon.com/press-release/2026/infpr202609-146)，它是電力轉換旁支，不替固態斷路器的選擇性保護背書。10/7 先找同型號測試與買方附件，不新增受惠公司線。
- **HBFSim，順位2維持 watch 且逾期**：本輪未完成作者原始運行紀錄與勘誤回查，保留9/25期限，不用重開論文入口當成完成複核。下一工作優先補作者版本、倍率與秒數共同鍵，再決定是否具備外部驗證；不採效能點估計。
- **玻璃核心，順位3維持 watch**：重讀 Samsung 展示與 Corning 角色說明，另查 [SKC 新聞室9/22資金及工程狀態](https://www.skc.kr/m/eng/Conmmunication/newsroom/system.do?menuCd=006001)。資金、展示、可靠度測試及概念驗證準備，不是同一客戶產品資格與連續批次製造結果。10/11 再查具名 qualification、良率與出貨分母。

三題原選題理由、第一拒絕、順位與知識價值均保留，不用本輪發現重排凍結歷史。雷達下次工作日10/7只是排程，不代表HBFSim已完成回查或任何來源變新。

## 10月8日回查

**SSCB 維持順位1及觀察狀態。** 已回查 Infineon 與 SolarEdge 的合作稿，並讀到
[SolarEdge 9/10官方框架說明](https://corporate.solaredge.com/en/news-and-media/local-announcements/dc-powertrain-ai-data-centers)。
它區分實驗室轉換級帶載與完整系統驗證，SSCB 只是候選保護方案，不是通用強制要求。
[白皮書入口](https://marketing.solaredge.com/800-vdc-protection-and-grounding-white-paper)只有摘要，
[平台頁](https://www.solaredge.com/us/data-centers)另把完整規格及保護圖列為 NDA 取得資料。
未取得同型號故障包絡、原始波形或買方驗收，不能把取件不足記成查無新文件；10/15 再查公開附件，不申請或繞過限制。

**HBFSim 維持順位2及觀察狀態。** 本輪核對 [9/30 v3](https://arxiv.org/html/2609.09800v3)、
[10/6 v0.1.1](https://github.com/SlugLab/HBFSim/releases/tag/v0.1.1) 與
[固定版本作者紀錄](https://github.com/SlugLab/HBFSim/blob/d2e6ce239c117c640fe68c8b5b2a7c77cf184da6/docs/proofs/2026-08-11-hybrid-complete.md)。
新版把延遲注入誤差限於指定增量測試；舊摘要與作者紀錄的秒數、倍率仍未對齊。
雖已取得 [reference 原始紀錄](https://github.com/SlugLab/HBFSim/blob/d2e6ce239c117c640fe68c8b5b2a7c77cf184da6/docs/proofs/artifacts/2026-08-11-vllm-exact/result.json)，
仍缺可逐欄配對的 fast 紀錄，不能自行把算術商數當成實測性能。
[CPU 複核紀錄](https://github.com/SlugLab/HBFSim/blob/d2e6ce239c117c640fe68c8b5b2a7c77cf184da6/docs/proofs/2026-10-06-ucie-release-cpu.md)
也不能代替獨立 GPU 工作負載驗證或實體 HBF 測量。10/15 優先追倍率勘誤、配對運行紀錄與未參與擬合的驗證資料。

**玻璃核心本輪未重查。** 保留10/11期限、順位3與原拒絕條件，不把另外兩題的回查當成三題全數完成。
三題都沒有升格文章或新增受惠公司線；凍結排序、選題理由及第一拒絕不變。

## 10月10日有界提前回查

玻璃核心只重讀原Samsung 9/10展示稿與Corning用途頁，仍須區分glass-core、暫時carrier及
interposer；尚未取得同一客戶產品／版本的資格、連續批次良率及出貨共同鍵。未全面掃描三家公司
新聞或客戶附件，所以不是完整到期結案。維持順位3、watch及10/11期限，不把取件日當新證據日。
SSCB與HBFSim本輪未重查，保留10/15節點。三題凍結排序、第一拒絕與升格門檻均不變。

本輪可發布增量來自既有PLP到期追蹤：補齊SEMI後繼文件／CER，更新原文章與圖譜，不新增
重複候選。光寶10/9美國建廠契約公告另路由到2301正式筆記複核；只是工程承諾，不是客戶訂單，
不得把它與Microsoft Pecos場址或其他公司的AI機房計畫拼接。

## 10月12日到期回查與旁支發現

玻璃核心維持順位3／medium／watch。SKC索引直取成功，最新可見9/22；重讀其
[同日公告](https://www.skc.kr/m/eng/Conmmunication/newsroom/newsDetail.do?gubun=006005&seq=1746)，
embedding初步評估後進可靠度測試，nonembedding則準備年底前概念驗證，與10/4已讀範圍
相同。Absolics用途宣傳沒有同一客戶／版本／連續批次良率。Samsung新聞列表未完整取得，
不宣稱全產業沒有新消息。10/19再找客戶資格、製造與交付共同鍵；原選題理由和第一拒絕不變。

SSCB與HBFSim本輪未重新裁決，仍保留順位1、2及10/15節點。兩個800V既有monitor共用
OCP附件缺口，不能當成SSCB具名故障测试已完成；NVIDIA公開白皮書示意也不是客戶驗收。

既有PCIe文章已接續本次完整名單捕捉，沒有另建重複候選。另讀到
[Astera 10/8 Aries 7公告](https://ir.asteralabs.com/news-releases/news-release-details/astera-labs-announces-aries-7-industrys-first-pcie-7-signal)：
Q4 2026是對選定客戶的預計送樣，銅／光連接產品組合不等於已量產或已具名部署。這只是
下一輪初查線索，尚未升為新凍結候選或改動三題排名；10/16先查OCP10/12–15具名展示及
產品測試，再追實際送樣與qualification。不得從合作或展示新增台灣公司收入線。

## 10月14日公告線索分流：先問能否接上可核對的結果

三題本輪未重新研究或裁決，維持原順位、知識價值與第一拒絕；SSCB／HBFSim仍10/15，
玻璃核心仍10/19。Aries7的10/16初查節點也保留，沒有用新公告重排凍結歷史。

本輪[上市重大訊息](https://openapi.twse.com.tw/v1/opendata/t187ap04_L)與
[上櫃重大訊息](https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap04_O)命中18列、14家公司，
發言日期都為10/13；10/12及10/14未觀測，不能當三日完整普查。以下是初查工作順序，
不是新的凍結評分或投資排名：

1. **京元電子：客戶預付款如何變成測試服務？** 10/13兩份公告須一起讀：一份為美國子公司
   產能與客戶預付款協議，另一份因契約結構調整取消原保證安排。新協議未披露金額，
   不可把舊保證額填成新預付款，更不可當已收現或收入。先追同一契約的付款、產能驗收、
   抵服務費及會計認列；10/16查公司與客戶附件。證據與台股連結直接、可證偽性高，但
   目前仍屬單一公司公告鏈，沒有足夠共同鍵形成新文章或財務圖譜線。
2. **M31／力成法說：先等會議，再看實際財務與問答。** 公告排定M31於11/6、力成於10/27
   說明，排程不是已公布成果。M31既有來源衝突仍保留；不能拿會議預告解除衝突。
   **均華的Q3自結**另與同日媒體澄清分開：自結未經查核／核閱，媒體預測亦非公司指引。
   10/16先補正式索引與核心文件路由，不由自結直接更新完整財報結論。
3. **欣興：局部停工與生產影響是否一致？** 10/13公告事故及部分作業停工，並由公司自述
   目前不影響生產。後一句不是獨立查證結果；10/16先追主管機關與復工文件，再找同廠區
   產能／交付影響，不將事故直接寫成全公司停產或營收下修。

其餘設備交易、資本及人事公告保留逐列語境；原始解析欄位與雜湊供本地回查，不取代附件。
光寶既有美國工程契約線索的核心財報複核尚未完成，留在待辦而非宣稱已驗證。上述各題
尚未具備足夠獨立文件與可比結果，故本輪只更新既有機櫃動作文章的量測邊界。

## 10月17日回查

SSCB與HBFSim已做有界回查，仍維持順位1、2及watch，10/21補下一份證據。
SSCB重讀Infineon與SolarEdge合作／平台及白皮書入口，仍未取得同型號故障波形、
選擇性保護及買方驗收；實驗室轉換級帶載不等完整斷路器驗證，NDA附件不申請也不繞過。
Mt. Diablo v1.0.0已定位但原件403、未取得可檢視頁，本輪不接受其新技術數字。

HBFSim實讀[v0.1.1發布列表](https://github.com/SlugLab/HBFSim/releases)、
[v3版本紀錄](https://arxiv.org/abs/2609.09800)及
[CPU複核紀錄](https://github.com/SlugLab/HBFSim/blob/v0.1.1/docs/proofs/2026-10-06-ucie-release-cpu.md)。
原固定版本fast/reference配對證據本輪兩路取件失敗；CPU測試不能代GPU工作負載或
實體HBF測試，不發布倍率。玻璃本輪未查，維持順位3與10/19期限。

既有Aries7線索重讀[供應商產品介紹](https://www.asteralabs.com/resources/blog/nothing-out-of-reach-the-aries-pcie-7-family-delivers-copper-and-optical-signal-conditioning-for-ais-next-chapter/)，
尚缺同產品原始測試、送樣及買方資格，10/23接續，不改凍結名單。10/14留下的京元電子
預付款、欣興復工及光寶工程契約後續，本輪尚未完成雙端附件核對，不延後原期限或宣稱結案。

本輪文章增量回到既有Helios、CPO與液冷資格主題：公司自述初始系統運行、系統整合展示、
不同設備的規格比較，各自保留商業成熟度限制。公告另留下8358投資更正、6213集團內股利
與3211季度自結線索；這些不是新凍結候選，也不由合併數字推AI／BBU收入。
三題原始選擇理由、priority、knowledge value、第一拒絕與歷史選擇帳本均不改寫。
