# AI 機櫃為什麼要重新驗證電磁干擾：零件合格，不等於整櫃合格

<!-- research_topic
topic_id: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-09
source_published_at: 2026-06-05
last_reviewed_at: 2026-08-09
review_due: 2026-08-31
source_type: mixed
publisher: Open Compute Project
publisher_domain: opencompute.org
canonical_url: https://www.opencompute.org/index.php/ocp-podcast
source_chain_id: ai-rack-emc-certification-primary-scan-20260809
stock_ids: 2327
group_ids: passive,powersupply,serverodm
trigger_type: rack_scale_emc_test_capacity_and_responsibility
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C5
base_confidence: medium
confidence_basis: OCP 上由 Meta EMC 工程負責人提出整櫃重量、供電、chamber 與實驗室容量問題，IEC 與 FCC 兩條獨立標準／監管鏈則可定位 equipment emission、measurement procedure 與測試機構能力責任；三者足以建立元件抑制、設備合規與整櫃測試能力不可互相替代的責任階梯，但全球僅一至兩家實驗室與時程瓶頸仍是單一 practitioner 主張，未取得全球 lab census、具名排程或台灣 rack qualification
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-09
from: initial
to: inbox
reason: captured_ai_rack_emc_lab_capacity_bottleneck
evidence: source_chain:ai-rack-emc-certification-primary-scan-20260809
-->
<!-- transition
date: 2026-08-09
from: inbox
to: triaged
reason: separated_component_suppression_equipment_compliance_and_full_rack_test_capacity
evidence: sources:S1,S2,S3,S4,S5,S6
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
reason: editorial_plain_language_wave85_full_rack_emc_layers_no_conclusion_change
evidence: editorial:plain_language_wave85_full_rack_emc_layers
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: expanded_large_eut_test_site_report_scope_uncertainty_contract
evidence: sources:S8,S9,S10,S11
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **電磁干擾／電磁相容（EMI／EMC）**：電磁干擾是設備產生或受到的雜訊；電磁相容則是整套設備在限制干擾的同時仍能正常運作。兩者是問題與結果，不是同一種零件。
- **雜訊路徑**：電磁雜訊從來源走到其他設備或量測天線的路線；重新接線、增加機構開口或改變接地，都可能形成新路徑。
- **傳導／輻射排放**：雜訊可能沿電源線或訊號線傳出去，也可能像天線一樣從機構與纜線輻射出去；一種濾波方式不會自動處理所有路徑。
- **整櫃**：把運算、網路、電源、液冷、機構與外接纜線組成實際運作配置後的完整機櫃系統，不只是其中一台設備。
- **解耦式機櫃**：把運算、電源或液冷拆成不同機櫃與側掛設備，再用纜線和管路連接的架構；各模組分開合格，不代表重新組合後仍維持相同結果。
- **運算托盤**：裝有處理器、加速器、記憶體與網路元件的可抽換運算模組。
- **電源側櫃**：放在運算機櫃旁、提供高功率轉換或配電的獨立櫃體；它的纜線與接地會成為整櫃測試的一部分。
- **液冷側掛設備**：放在機櫃旁、負責冷卻液循環或分配的設備；泵浦、管路、控制線與供電都可能改變完整配置。
- **共模扼流圈／濾波器**：用來抑制特定電流或頻率雜訊的元件；實際效果取決於放置位置、接線、頻率及周邊設計。
- **屏蔽／吸波材料**：前者阻擋或導引電磁能量，後者吸收指定頻帶的能量；材料規格不能單獨證明整櫃合格。
- **被測設備**：正式測試時被視為一個完整測試對象的設備範圍；必須先說清楚包含哪些機櫃、側掛設備與纜線。
- **被測配置**：被測設備在測試當下的接線、運作模式、外接設備與軟體負載；配置改變後，原結果未必能直接沿用。
- **正式送驗前測試（pre-compliance）**：在正式測試前用較小場地、探棒或簡化配置先找出風險，可降低重測機率，但不是最終合格結果。
- **模擬（simulation）**：以模型預估雜訊與耦合路徑；可協助設計，仍須用實際設備與量測確認模型是否成立。
- **子系統測試**：只測電源、運算托盤或冷卻設備等一部分；它能定位局部問題，不能自動涵蓋重新組合後的整櫃。
- **正式整櫃測試**：用最後被測配置、指定程序與具備能力的實驗室，量測完整機櫃的排放結果。
- **CISPR 32**：IEC 體系針對多媒體設備排放與可重複量測所制定的標準；它說明設備層要測什麼，不替特定機櫃出具通過證明。
- **FCC**：美國聯邦通信委員會；本文只使用其量測指引與合格測試機構資料入口，不替特定設備判定法律適用性。
- **ANSI C63.4／C63.4a**：美國非刻意輻射器的量測方法版本；FCC 23-14 保留 2014 版並納入 2017 修訂作替代選項，不能因此推定所有 AI rack 都適用同一路徑。
- **NIST／NVLAP**：NIST 是美國國家標準與技術研究院；NVLAP 是其實驗室認可計畫。本文引用其 Handbook 與 EMC 計畫頁檢查實驗室能力範圍，不把認可標誌當成產品認證。
- **量測程序**：規定設備如何擺放、運作、接線及量測的步驟；換一套方法或配置，結果可能不能直接比較。
- **實驗室認可／認可範圍（accreditation／accredited scope）**：認可是對實驗室能力的第三方確認，scope 則列出其特定地點可執行的產品、方法與測試；出現在機構名錄，不等於能測任何尺寸與功率的設備。
- **大型被測設備／測試體積**：被測物的高度、寬度與旋轉時占用空間都可能改變可用場地、量測距離與程序；「設備放得進去」仍不等於場地與方法適用。
- **場地等效性**：使用替代場地或不同佈置時，要用記錄與量測證明它能提供指定方法要求的量測條件，而不是只看房間名稱相同。
- **測試裕量（margin）**：在指定量測條件下，結果距離限制值還有多少空間；沒有同時列出限制值、偵測器、頻寬與不確定度，單看裕量不能判斷結果是否穩健。
- **量測不確定度**：儀器、校正、場地、天線、接線與重複量測等誤差來源，合成後表示結果可能落在哪個合理範圍；它不是把不合格數字任意改成合格。
- **判定規則**：結果靠近限制值時，預先約定如何把量測值與不確定度轉成通過、未通過或需重測的決定；不同規則可能讓同一數字有不同處置。
- **量測溯源**：用不中斷且有文件的校正鏈，把量測結果連回指定參考；有溯源不代表整台產品合格，卻是數字能否被信任與重現的基礎。
- **測試報告護照**：本文把一份結果要隨身攜帶的配置、方法、場地、量測與認可資訊整理成九欄查核表；這是研究中心的閱讀工具，不是 FCC、NIST 或 IEC 聯合發布的正式表單。
- **隔離測試室／旋轉台（chamber／turntable）**：隔離外界雜訊的測試空間與旋轉被測設備的平台；機櫃太大、太重時，實驗室硬體可能放不下或帶不動。
- **實驗室量能（lab capacity）**：實驗室是否有足夠空間、承重、供電、冷卻、量測範圍與人員，可安全完成指定配置的測試。
- **可用時槽／等待時間**：符合條件的實驗室何時能排進測試，以及從預約到開始測試要等多久；機構家數不等於可立即使用的量能。
- **重測**：設計或配置修改後再次測試；是否必須重測，要由變更範圍、標準與驗收計畫判定。
- **資格驗證（qualification）**：客戶、平台或規範確認產品能否被採用的程序；元件資格驗證與整櫃合格是不同層次。
- **PSU**：電源供應器；它可能是傳導雜訊路徑與被測配置的一部分，但元件或單機測試不會自動覆蓋整櫃。

### 三句話抓重點

- 每一個零件或子系統各自合格，全部設備重新接線並同時運作後，仍可能彼此干擾，所以還要再測一次完整系統。
- 完整驗證至少跨四關：零件能否降低雜訊、正式被測物包含哪些設備、要依什麼程序量測，以及實驗室能否承受整櫃的尺寸、重量與供電。
- 公開資料能證明這四層責任不能互相替代，但不能證明全球只剩一兩家可用實驗室，也不能把國巨的通用抑制材料直接寫成 AI 機櫃訂單。

### 為什麼重要

**先看問題怎麼從單機變成整櫃。** 一般伺服器可以把單機送進既有測試室。AI 系統卻把運算、
供電與液冷拆到多個櫃體，再用高速纜線、管路與高功率供電重新組合。原本能測單機的實驗室，
未必放得下、帶得動，也未必供得起完整機櫃。

**別把元件測試當成整櫃合規。** 零件測試回答「這顆零件能降低哪種雜訊」；子系統測試回答「局部
設計是否有風險」；正式整櫃測試才回答「最後配置同時運作時是否符合要求」。前一層通過，
不能替後一層保證結果。

**再拆開每一層的責任。** 即使已有量測標準，實驗室仍要有足夠空間、承重、供電、
冷卻與認可範圍。名錄上有很多機構，不等於它們都能立即測量同一套大型機櫃。

**看到「通過」先別急著比較。** 兩份報告若測的是不同軟硬體版本、不同工作負載或纜線，
使用不同量測距離、場地與判定規則，即使都寫 pass，也可能回答不同問題。報告要先帶齊
被測配置、方法、場地、裕量、不確定度與認可範圍，才有資格進入橫向比較。

**最後用三個責任盒查證。** 先說清楚公司負責零件、電源子系統、整櫃整合還是測試服務，再找具名
產品、配置、客戶驗證與財務分母。不能因為「電磁相容很重要」，就直接把任一族群寫成受惠者。

### 接下來怎麼追

- 先找具名整櫃的測試計畫：正式被測配置包含什麼、使用哪套程序，以及實驗室的空間、承重、供電、認可範圍與等待時間。
- 拿到報告後，再用九欄護照核對版本、工作負載、纜線、方法版本、場地幾何、儀器溯源、裕量與不確定度、認可範圍及重測觸發；缺欄時先標示不可比，不自行補故事。
- 再追國巨或 KEMET 是否首次把具名抑制元件連到 AI 機櫃的位置、頻率目標、客戶驗證、量產料號與可辨識收入；只重複廣義 AI 成長不算。
- 最後等大型雲端業者或系統組裝廠說清楚：哪些模組證書可以沿用、哪些配置變更必須重測，以及模擬與正式送驗前測試能替代到哪個邊界。

### 想一想

- 即使運算、電源與液冷設備都各自通過測試，重新接線並同時運作後，為什麼完整系統仍可能不合格？
- 兩份報告都寫「通過」，但其中一份沒有工作負載、纜線、量測距離與不確定度，你能確定它們測的是同一件事嗎？
- 全球測試機構數量看起來很多，但若只有少數能承受完整機櫃，真正該追的是機構家數，還是可預約的測試時槽？
- 一片吸波材料只有自身規格，卻沒有安裝位置、目標頻率與整櫃測試結果時，能不能量化它對完整機櫃的價值？

## 主張與證據帳本

`證實` 只代表來源直接支持指定標準範圍、測試程序或產品能力；OCP 訪談中的全球 lab 數量
仍是 practitioner 主張，不是本研究完成的獨立 census，也不代表任何台灣公司已取得訂單。

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: OCP Podcast Episode 21 的官方摘要由 Meta Lead EMC AI Hardware Infrastructure Engineer 說明，AI rack 的解耦式 compute、power 與 liquid cooling 配置帶來 turntable 承重、1MW 以上供電與 chamber 尺寸三項測試瓶頸，並主張目前全球只有一至兩家 lab 能處理當代配置、AI rack 週期約 12–18 個月而 lab 建置或升級約需一年
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-08-09
basis: S1 Episode 21 的 What You'll Learn 與 chapters 直接列出三項瓶頸、lab 數量與兩種週期
boundary: 這是 OCP 對單一 Meta practitioner 訪談的官方摘要，不是獨立全球 lab census、可用 capacity 統計、法規解釋或已發生 deployment delay 的證據
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
claim: IEC 的 CISPR 32:2015 publication page 將標準範圍界定為額定 AC 或 DC 供電不超過 600V 的 multimedia equipment，涵蓋 Class A 與 Class B，目標包含 9kHz 至 400GHz 的無線電頻譜保護及量測結果的 reproducibility／repeatability
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-08-09
basis: S2 publication page 的 scope、objectives、edition 與 consolidated version 標示直接支持此句
boundary: 標準頁只描述 publication scope，不判定特定 AI rack 的 equipment configuration、600V 以上架構如何適用、是否需整櫃測試或某產品已通過
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
claim: FCC KDB Publication 300643 指出 Part 15 unintentional radiator 的一般 compliance measurement 採 ANSI C63.4，若裝置需要其他方法應向 FCC Laboratory 查詢；FCC 的 EAS accredited test firms dataset 同時提醒使用者必須自行選擇能量測特定裝置的 firm，FCC 不替名單內公司的實際量測能力背書
supporting_source_ids: S3,S4
contrary_source_ids:
as_of: 2026-08-09
basis: S3 的 measurement-procedure answer 與 S4 dataset description 分別直接支持方法入口及能力責任界線
boundary: FCC 資料不表示所有 AI rack 都走同一 authorization procedure，也不證明名單內任何 firm 具備兆瓦供電、大型 chamber、足夠承重或特定 lead time
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
claim: 國巨集團 2021 年的 KEMET 產品公告把 FLEX SUPPRESSOR 描述為用於降低 EMI 與其他雜訊的薄型柔性吸波材，EFG3 與 FS 系列頻率範圍可到 40GHz，公告應用只列 commercial、telecommunications、automotive 與 connected devices，沒有列出 AI rack、CISPR 32／FCC qualification 或整櫃測試結果
supporting_source_ids: S5
contrary_source_ids:
as_of: 2026-08-09
basis: S5 的產品特性、頻率與 application 段落直接支持功能與明示範圍，且全文未提供 AI rack qualification
boundary: 產品公告證明集團有具名 EMI 抑制材料能力，不證明其在 AI rack 的 placement、attenuation、qualified part、customer、shipment、revenue 或 margin
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
claim: AI rack EMC 應拆成元件／材料抑制能力、equipment emission 標準與量測程序、以及能承載完整配置的 lab capacity 三層責任；任何一層成立都不能替代另外兩層，因此「元件合規」或「支援 EMI 抑制」不能直接讀成整櫃已可通過驗收
supporting_source_ids: S1,S2,S3,S4
contrary_source_ids:
as_of: 2026-08-09
basis: S1 建立 full-rack 物理測試能力問題，S2 建立 equipment emission scope，S3 建立 measurement procedure，S4 明示 accredited firm 名單不替特定 device capability 背書；三條獨立組織鏈共同支持分層責任
boundary: 這是研究責任圖，不宣稱每個平台都必須以完整機櫃做相同測試、不解釋特定法域適用性，也不估計 lab TAM、零件價值量或公司受惠
verification_needed: hyperscaler／ODM 的正式 acceptance plan 把 component、subsystem、equipment configuration、simulation／pre-scan 與 accredited lab final test 逐層對齊
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: inference
status: active
claim: 2327 國巨因集團具備具名 EMI 抑制材料，且公司 2026Q1 法說把 AI 列為多產品類別成長動能，是 passive 族群檢查元件層如何接到 AI rack EMC 的第一個具名入口；兩份公司文件之間沒有證據顯示該 EMI 產品就是 AI 成長來源
supporting_source_ids: S5,S6
contrary_source_ids:
as_of: 2026-08-09
basis: S5 證明具名 EMI 產品能力，S6 證明公司對廣義 AI 終端的當期說法；因兩者未以 part、customer 或 qualification 相連，本 claim 只把 2327 定位為查核入口
boundary: 「查核入口」不是受惠、design win、份額、訂單或獲利判斷；不得把兩則獨立公司敘述拼成同一產品的 AI 營收
verification_needed: 公司或買方雙向揭露 KEMET／Pulse／YAGEO 具名 EMI part、rack placement、frequency target、qualification、production shipment 與財務分母
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: unverified
status: active
claim: 2327 國巨或任何 universe 的電源與伺服器 ODM 已取得 AI rack EMC 元件 qualification、pre-compliance、full-rack test、認證服務、訂單、出貨或可辨識毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-09
basis: 現有一手來源未提供台灣公司的具名 rack configuration、part、測試報告、accredited scope、客戶、出貨或損益
boundary: 不得由一般 EMI 產品、AI 終端成長、PSU／rack 組裝能力或法規存在推導公司已取得商業曝險
verification_needed: 買方 test plan／認證報告與公司申報雙向核對具名產品、責任層、qualification、production shipment、revenue 與 margin
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: unverified
status: active
claim: 全球可用 AI rack EMC lab capacity 的確只有一至兩家，且模組或子系統既有合規文件無法覆蓋解耦式完整機櫃，已形成可量測的排程延遲或部署 hard stop
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-09
basis: S1 提供 practitioner 主張，但沒有具名 lab census、accredited scope、可用時槽、排程紀錄、模組證書沿用規則或已延遲專案清單
boundary: 不能把單一訪談的 urgency 當成全球容量統計或既成部署損失；也不能因未找到延遲案例就反推瓶頸不存在
verification_needed: 至少兩個獨立 operator／lab 公布可測配置、chamber／weight／power capability、lead time、排程利用率，以及 equipment configuration 變更與重測判定
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: verified
status: active
claim: FCC 23-14 保留 ANSI C63.4-2014，並把 ANSI C63.4a-2017 納入替代選項；該修訂新增五公尺量測距離與較大的 test volume，以容納高度超過兩公尺的設備，FCC 同時表示大型設備可能需要調整量測作法
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-08-12
basis: S8 第 11–12 頁第 30–32 段直接記錄採用版本、替代選項、五公尺距離、expanded test volume 與 larger devices 的理由
boundary: 這只證明設備尺寸可能改變美國 Part 15 量測場地與方法選擇；不判定任何 AI rack 的法律分類、是否必須整櫃送驗、能否沿用模組證書、實驗室家數或特定產品結果
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
claim: NIST Handbook 150-11:2013 將 EMC 實驗室認可連到特定 test methods，並要求替代場地留下描述與等效性證據、場地衰減檢查與記錄、依方法建立量測不確定度預算、儀器與天線校正溯源，以及屏蔽室、接地、濾波器與自動測試軟體的品質控制
supporting_source_ids: S9
contrary_source_ids:
as_of: 2026-08-12
basis: S9 §1.3、§5.3–5.6 與 §5.9 分別直接規範特定方法認可、場地等效／衰減、不確定度、校正溯源、設施／軟體與品質控制
boundary: 這是 2013 年美國 NVLAP EMC 實驗室認可手冊，不是 AI rack 產品標準、產品合格證、當前全球實驗室名錄，也不能替任何報告證明被測配置與量測結果
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
claim: NIST Handbook 150:2020 Update 1 要求認可證書的 scope 指明測試、產品或材料與方法；NVLAP mark 只能用於認可範圍與地點內的活動，不能宣稱產品獲得 NIST／NVLAP certification、approval 或 endorsement，而同一報告若混有未認可資料必須清楚標示其範圍與來源
supporting_source_ids: S10
contrary_source_ids:
as_of: 2026-08-12
basis: S10 §3.6.4 與 Annex A 直接列出 Scope of Accreditation 的內容、mark 使用邊界、產品背書禁語及 accredited／unaccredited data 的標示責任
boundary: 這是美國 NVLAP 的一般認可政策；不取代特定法域、標準或客戶驗收要求，也不表示有認可標誌的實驗室能處理任何尺寸、功率或配置
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: NIST NVLAP 現行 Electromagnetic Compatibility and Telecommunications LAP 頁面把 radiated／conducted emissions、susceptibility／immunity 與其他 EMC 類別列為可申請的特定認可領域，並要求 quality assurance；同頁也明示該 LAP 目前不自行強制 proficiency testing 或 interlaboratory comparison，除非適當計畫可用
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-08-12
basis: S11 的 Program Description、Accreditation Requirements 與 Proficiency Testing 段落直接支持領域、品質保證與現行 PT／ILC 邊界
boundary: 動態計畫頁只描述 NVLAP ECT 認可架構，不能證明某實驗室的實際 scope、設備容量、某報告的品質、跨實驗室一致性或產品合格
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C13
label: inference
status: active
claim: 一份可比較的 AI rack EMC 結果至少應以九欄測試報告護照固定被測設備與版本、運作模式與負載、連接纜線與接地、標準／方法版本與偏離、場地幾何與等效性、儀器校正溯源與軟體、量測值／限制值／偵測器／頻寬／裕量／不確定度／判定規則、實驗室地點與認可範圍，以及報告日期、簽署者、變更與重測觸發
supporting_source_ids: S3,S8,S9,S10,S11
contrary_source_ids:
as_of: 2026-08-12
basis: S3／S8 固定方法版本與大型設備場地選擇，S9 固定場地、校正、不確定度與 QC，S10／S11 固定認可 scope 與 mark 邊界；本文把分散要求整合成逐份報告的閱讀契約
boundary: 九欄護照是研究中心的證據整合與可比性檢查，不是 FCC、NIST、IEC 或 ANSI 聯合標準，也不是完整法規 test report template；特定程序若有不同必填欄位仍以正式規則為準
verification_needed: 具名 operator／lab 的 AI rack test plan 與完整版本化報告，逐欄揭露配置、方法、場地、結果、不確定度、scope 與變更控制，並能重複或跨場地核對
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C14
label: unverified
status: active
claim: 已有具名量產 AI rack 公開完整九欄測試報告護照、跨版本或跨場地可重現結果，並把該證據連到 universe 公司客戶資格、部署、訂單、收入或毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: S8–S11 都是量測與認可制度文件，未提供具名量產 AI rack 的完整配置報告；既有公司來源 S5–S7 也未把產品、測試、客戶與財務接成同一條鏈
boundary: 不能把大型設備方法、實驗室認可標誌、一般 EMI 元件規格或廣義 AI 成長敘述升格成具名產品 pass、客戶採用或財務貢獻
verification_needed: 平台／客戶、實驗室與供應商至少兩條獨立來源對上同一 rack 版本、九欄報告、重複結果、qualification／deployment、shipment 與財務分母
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 整櫃驗證要過四關：零件、配置、量測與實驗室

**第一道是元件與材料。** 共模扼流圈、濾波器、屏蔽結構、導電墊片、吸波材與 PCB 佈局，
都只能在指定位置與頻率條件下處理一部分雜訊。

**第二道先確認被測設備範圍。** 要把運算櫃、電源側櫃、液冷設備、外接纜線與運作模式列清楚，
才能知道測試結果涵蓋哪一套完整配置。

**第三道是量測程序與責任。** 要先確認使用哪套方法，再由送測者核對實驗室是否真的能測這套設備。

**第四道才是實驗室可用量能。** 場地必須放得下、撐得住、供得起，也要排得到實際測試時槽。

| 驗證關卡 | 先問什麼 | 現有證據能證明 | 還不能證明 |
|---|---|---|---|
| 1. 零件先降低雜訊 | 這顆零件處理哪一條雜訊路徑？ | 共模扼流圈、濾波器、屏蔽與吸波材料各有不同作用；國巨集團的 FLEX SUPPRESSOR 證明公司具備一項具名抑制材料能力 | 該產品已放進 AI 機櫃、處理特定位置與頻率、通過客戶驗證，或能讓整櫃合格 |
| 2. 定義完整被測配置 | 正式測試包含哪些機櫃、側掛設備、纜線與運作模式？ | CISPR 32 說明多媒體設備的排放要求與可重複量測目標 | 運算櫃、電源側櫃、液冷設備與外接纜線要用哪一種組合當成正式被測物 |
| 3. 依程序完成量測 | 要用哪套方法，誰有責任確認實驗室能測這套設備？ | FCC 指引提供一般量測方法入口，也提醒使用者自行確認名錄內機構是否能測特定裝置 | 每套 AI 機櫃都適用同一程序，或名錄中的實驗室都能處理大型高功率機櫃 |
| 4. 確認實驗室能承載 | 場地放得下、撐得住、供得起，也排得到時間嗎？ | OCP 訪談指出測試室尺寸、旋轉台承重與一百萬瓦以上供電會限制大型機櫃送驗 | 全球真的只剩一兩家可用實驗室、實際可用時槽、等待時間，以及是否已造成部署延誤 |

四關回答的是不同問題。第一關證明零件能力，第二與第三關定義完整設備如何被測，第四關才
確認現場是否真的能完成測試。前一關通過，不能替後一關出具結果；這張表建立的是查證順序，
不是宣稱特定機櫃已合格或特定供應商已受惠。

## 拿到一份測試資料時，照四步判讀

**先確認測了什麼。** 零件資料表上的阻抗、吸收頻帶或雜訊降低數值，只能回答該零件在指定
條件下的能力。它沒有包含電路板走線、纜線、機構開口、接地、電源供應器、風扇與液冷管路
共同形成的路徑。公告若沒寫安裝位置、目標頻率與完整配置，判定就停在零件能力。

**再分清預先測試與正式結果。** 模擬、正式送驗前測試或子系統測試可以提早找出風險，卻要
另外說明最後哪套配置會被當成完整設備、所有側掛設備是否同時通電，以及正式測試採用什麼
程序。預先發現問題，不等於最終配置已經合格。

**第三步核對實驗室，不只看名錄。** 大型 AI 機櫃至少要核對測試室尺寸、平台或地面承重、
可安全提供的電力、冷卻與配線方式、量測距離及認可範圍。「名錄上有很多家」與「很多家能
立即測這套配置」是不同主張；一場訪談也不能單獨證明全球只剩一兩個時槽。

**最後才問商業後果。** 若設計已透過模擬與預先測試收斂，實驗室稀缺未必造成長期延誤；若
配置未改變時能沿用既有證書，也可能縮小重測範圍。要看到具名測試計畫、失敗與重測紀錄、
等待時間和量產排程，才能把工程摩擦升為部署阻礙。公司還要由供應商與買方雙向對上產品、
安裝位置、資格驗證、出貨與財務分母，才能從技術能力走到商業貢獻。

## 兩份都寫「通過」，為什麼仍可能不能相比

**先看被測物是不是同一個版本。** 一份報告可能只測運算櫃，另一份把電源側櫃、液冷設備與
外接交換器一起通電；韌體、PSU、屏蔽件與纜線版本也可能不同。只要邊界不同，兩個 pass
代表的就是兩套系統，不能先當成同一產品的前後比較。

**再看它們是否在同一種最壞情境下工作。** 待機、低負載與高速運算時，時脈、網路、風扇、
泵浦與功率轉換器的活動都不同。報告若沒有留下軟體負載、埠使用、線材、長度、終端、接地與
側掛設備，就無法知道量測是否覆蓋會產生最大雜訊的實際模式。

**大型設備還會改變場地與方法。** FCC 23-14 之所以把 C63.4a 的五公尺距離與 expanded test
volume 納入替代選項，就是因為高度超過兩公尺的設備可能需要不同場地安排。這不表示每一台
AI rack 都走同一路徑；它只提醒讀者，設備尺寸、距離、測試體積與替代場地等效性必須隨結果
一起保存，不能把不同幾何條件下的 pass 當成天然可比。

**最後才看「通過」怎麼判。** 同一個量測值還要配上限制值、偵測器、頻寬、校正狀態、量測
不確定度與判定規則。實驗室有認可標誌，也只代表列在 scope 內、由指定地點執行的活動；
NIST 明確禁止把 NVLAP mark 說成產品認證、核准或背書。少了這些資訊，pass 是結論標籤，
不是可重現的工程證據。

## 用九欄 EMC 測試報告護照核對一份結果

這張護照把 FCC 與 NIST 文件分散在方法、場地、量測與認可制度中的要求，整理成初學者可逐欄
詢問的閱讀工具。它不替代正式 test report template，也不預設所有法域必填完全相同欄位；
用途是讓讀者在缺資料時明確停在「不可比」，而不是用一個 pass 字樣補完未知條件。

| 護照欄位 | 報告至少要留下什麼 | 缺欄時最容易誤讀成什麼 |
|---|---|---|
| 1. 被測設備與版本 | 機櫃、側櫃、交換器、冷卻設備、PSU、韌體、屏蔽件與料號版本 | 把只測一個模組當成整櫃結果，或把舊版 pass 沿用到新版 |
| 2. 運作模式與負載 | 待機或最壞工作模式、軟體工作負載、時脈、網路流量、風扇與泵浦狀態 | 把低活動量結果當成滿載結果 |
| 3. 埠、纜線與接地 | 啟用埠、線材種類與長度、終端、外接設備、接地與 sidecar 連接方式 | 忽略纜線與接地形成的新天線或傳導路徑 |
| 4. 標準、方法與偏離 | 標準／方法名稱與版次、適用類別，以及任何替代或偏離程序 | 把不同版次或不同程序的 pass 當成同一門檻 |
| 5. 場地幾何與等效性 | 測試地點、量測距離、天線與設備高度、turntable／test volume，以及替代場地等效證據 | 只確認「放得下」，卻不知道場地是否符合方法 |
| 6. 儀器、校正、溯源與軟體 | 天線、receiver／analyzer、校正日期、溯源鏈與自動測試軟體版本／驗證 | 把無法回查的數字當成可重現結果 |
| 7. 結果、限制與判定 | 頻率與量測值、限制值、偵測器、頻寬、裕量、不確定度及判定規則 | 只看 pass 或一個最大裕量，忽略邊界如何判定 |
| 8. 實驗室地點與認可範圍 | 執行地點、認可機構、scope 內的產品／方法／測試，以及未認可資料標示 | 把機構標誌當成所有測試能力或產品背書 |
| 9. 報告責任與變更控制 | 報告日期、簽署者、修訂紀錄、配置差異與需重測的觸發條件 | 新版本仍沿用舊報告，卻沒人對差異負責 |

九欄不要求先拿到所有商業機密才研究。公開文件若只提供其中幾欄，可以精確寫成「證明某一層」；
真正不能做的是把未揭露欄位默認為相同，再延伸成整櫃合格、客戶採用或供應商收入。

## 裕量不是保證：量測不確定度與判定規則要一起看

測試裕量只是在同一套方法、偵測器與頻寬下，量測結果和限制值之間的距離。量測不確定度則把
儀器、天線、校正、場地與重複性等已辨識影響合成一個結果範圍。NIST 的 EMC 實驗室手冊要求
不確定度依 test method 建立，並由校正或計算資料支持；它沒有提供一條可以套用到所有 AI rack
的通用安全裕量。

因此，看到「低於限制值」仍要問判定規則。報告是否直接以量測值判定、是否在靠近界線時納入
不確定度、何時要求重測或標示風險，都應在測試前固定並在報告中可回查。本文不自行替 FCC、
IEC、實驗室或客戶發明 guard band，也不拿不同方法下的裕量做公司或機櫃排行。

## 實驗室有認可標誌，為什麼仍不能替產品背書

認可是「誰在什麼地點，能依哪些方法測哪些產品或材料」的能力範圍，不是一張可以蓋在任何
產品上的通行證。NIST Handbook 150 要求 Scope of Accreditation 列出測試、產品／材料與方法，
而 NVLAP mark 只能用於 scope 與地點內的活動；同一報告混有未認可資料時，還要把範圍與資料
來源清楚分開。

這會留下四個實務檢查：報告上的實驗室地點是否就是認可地點、使用的方法與版次是否在 scope
內、被測產品類別是否涵蓋這套配置，以及報告哪些資料其實不在認可活動內。四項都對上，也只能
說明量測能力與報告標示符合該認可框架；不能把 NIST／NVLAP 標誌改寫成產品 certification、
approval、endorsement，更不能直接跨到客戶資格、部署與財務歸因。

## 這篇如何用在公司研究，又不能怎麼用

2327 國巨是被動元件族群第一個具名查核入口，但目前只到元件能力。公司法說提到廣義 AI 動能，
KEMET 產品公告則只證明通用抑制材料；兩份文件沒有共同產品、客戶或資格驗證，不能拼成同一筆
AI 機櫃收入。它們的用途是告訴研究者下一份證據要找什麼，不是先寫受惠故事。

電源供應與伺服器組裝／機構目前連具名公司證據都沒有，只保留搜尋方向：電源可能影響沿線路
傳出的雜訊與高功率測試，系統組裝廠可能決定最後被測配置。沒有測試計畫、認證報告與公司申報，
就不能分配價值；本文也不支持個股排序、營收預測或投資動作。

## 來源

<!-- research_source
source_id: S1
role: other_primary
source_kind: living_index
publisher: Open Compute Project
independence_group: ocp-meta-practitioner
title: OCP Podcast Episode 21 — The EMC Testing Challenge: Why AI Infrastructure Is Outpacing the Labs That Certify It
published_at:
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://www.opencompute.org/index.php/ocp-podcast
locator: 2026-08-09 觀察 Episode 21（2026-06-05）的摘要、What You'll Learn 與 5:01／11:33／21:20 chapters，列出 weight、1MW+ power、chamber、1–2 labs 與 12–18 month／one-year cycle
limitation: 動態 podcast 索引與單一 practitioner 訪談；不是全球 lab census、FCC 法律意見、具名排程或 deployment delay 證據
-->

<!-- research_source
source_id: S2
role: standard
source_kind: living_index
publisher: International Electrotechnical Commission
independence_group: iec-cispr
title: CISPR 32:2015+AMD1:2019 consolidated publication page
published_at:
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://webstore.iec.ch/en/publication/22046
locator: 2026-08-09 觀察 consolidated version、scope（MME、AC／DC 不超過 600V）、Class A／B、9kHz–400GHz 與 reproducibility／repeatability objectives
limitation: publication page 只提供標準摘要，不含付費正文全部條款，也不判定特定 AI rack configuration 或法域適用性
-->

<!-- research_source
source_id: S3
role: regulator_or_policy
source_kind: living_index
publisher: Federal Communications Commission
independence_group: us-fcc
title: FCC KDB Publication 300643 — Part 15 measurement procedures
published_at:
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://apps.fcc.gov/oetcf/kdb/forms/FTSSearchResultPage.cfm?id=21079&switch=P
locator: 2026-08-09 觀察 answer 所列 ANSI C63.4-2014 unintentional-radiator procedure，以及其他方法應向 FCC Laboratory 提 KDB inquiry 的邊界
limitation: KDB guidance 協助遵循規則但不是規則本身；頁面未說明所有 AI rack 的 authorization 路徑、lab capacity 或具名產品結果
-->

<!-- research_source
source_id: S4
role: regulator_or_policy
source_kind: living_index
publisher: Federal Communications Commission
independence_group: us-fcc
title: FCC EAS Accredited Test Firms dataset
published_at:
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://opendata.fcc.gov/Engineering-Technology/EAS-Accredited-Test-Firms/nubx-v54a
locator: 2026-08-09 觀察 dataset description 對 Parts 15／18 testing firm 的用途，以及使用者自行確認 specific-device capability、FCC 不負能力責任的警語
limitation: 名單不提供兆瓦供電、chamber 尺寸、turntable 承重、可用時槽或 AI rack scope，也不代表每家 firm 仍可立即接案
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: document
publisher: YAGEO Group / KEMET
independence_group: yageo-issuer
title: KEMET Advances Noise Suppression Solutions for Commercial, Telecommunications, and Automotive Applications
published_at: 2021-02-26
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://www.yageo.com/jp/PressRoom/Content/press_room?category=product_event&news_id=20210226&page=14
locator: FLEX SUPPRESSOR 的 thin flexible EMI-absorbent material、EFG3／FS up to 40GHz 與明示 application 段落
limitation: 舊產品公告只支持集團產品能力；沒有 AI rack、CISPR／FCC qualification、客戶、出貨或財務數字
-->

<!-- research_source
source_id: S6
role: company_release
source_kind: document
publisher: YAGEO Corporation
independence_group: yageo-issuer
title: 國巨 2026 年第一季法人說明會簡報
published_at: 2026-04-15
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://mopsov.twse.com.tw/nas/STR/232720260415M001.pdf
locator: PDF 第 4–10 頁的產品與終端組合，以及公司對 AI、標準品與特殊品當季成長的說明
limitation: 廣義終端與產品組合未把 AI 成長接到 FLEX SUPPRESSOR、其他 EMI part、rack qualification、客戶或財務分拆
-->

<!-- research_source
source_id: S7
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
independence_group: twse-mops
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-08-09 以 2327 及 passive／power／server universe 公司作後續季報、法說與重大訊息重查入口
limitation: 動態入口本身不證明任何 EMC qualification、訂單、出貨或財務貢獻；新文件出現時必須另行登錄與驗證
-->

<!-- research_source
source_id: S8
role: regulator_or_policy
source_kind: document
publisher: Federal Communications Commission
independence_group: us-fcc
title: FCC 23-14 — Updating References to Standards Related to the Commission's Equipment Authorization Program
published_at: 2023-03-14
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://docs.fcc.gov/public/attachments/FCC-23-14A1_Rcd.pdf
locator: PDF 第 11–12 頁第 30–32 段；保留 C63.4-2014、納入 C63.4a-2017 alternative，以及五公尺距離、expanded test volume 與高度超過兩公尺設備的理由
limitation: 美國 Part 15 equipment-authorization 規則更新；不判定特定 AI rack 的 equipment class、完整配置、必測方式、實驗室 capacity 或產品 pass
-->

<!-- research_source
source_id: S9
role: standard
source_kind: document
publisher: National Institute of Standards and Technology
independence_group: us-nist-nvlap-emc
title: NIST Handbook 150-11:2013 — NVLAP Electromagnetic Compatibility and Telecommunications
published_at: 2013-04-25
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.nist.gov/system/files/documents/nvlap/NIST-HB-150-11-2013.pdf
locator: §1.3 與 PDF 第 18–21 頁 §5.3–5.6、§5.9；特定方法 scope、替代場地等效／衰減、不確定度、校正溯源、屏蔽室／接地／軟體與品質控制
limitation: 2013 年美國 NVLAP EMC 實驗室認可手冊；不是 AI rack 產品標準、產品證書、現行全球 lab census 或特定報告品質證明
-->

<!-- research_source
source_id: S10
role: standard
source_kind: document
publisher: National Institute of Standards and Technology
independence_group: us-nist-nvlap-general
title: NIST Handbook 150:2020 Edition, Update 1 — NVLAP Procedures and General Requirements
published_at: 2024-10-09
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://nvlpubs.nist.gov/nistpubs/hb/2020/NIST.HB.150-2020-upd1.pdf
locator: PDF §3.6.4 與 Annex A；文件原版為 2020 年 7 月、Update 1 包含截至 2024-10-09 的更新，列出 scope、mark、產品背書禁語與未認可資料標示規則
limitation: 美國 NVLAP 一般認可政策，不是特定 EMC 方法、AI rack 法規判定、實驗室設備容量或產品合格保證
-->

<!-- research_source
source_id: S11
role: regulator_or_policy
source_kind: living_index
publisher: National Institute of Standards and Technology
independence_group: us-nist-nvlap-emc
title: NVLAP Electromagnetic Compatibility and Telecommunications Laboratory Accreditation Program
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.nist.gov/nvlap/electromagnetic-compatibility-and-telecommunications-lap
locator: 2026-08-12 觀察頁面更新日 2025-01-16、Program Description、Accreditation Requirements 與 Proficiency Testing 段落
limitation: 動態計畫頁只描述 specific areas、quality assurance 與現行 PT／ILC 政策；不證明任何 lab scope、capacity、report quality、跨 lab 一致性或產品結果
-->

## 族群影響

<!-- impact
group_id: passive
stock_ids: 2327
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-31
rationale: 2327 集團有具名 EMI 抑制材料且公司揭露廣義 AI 動能，因此成為 passive 族群第一個可從 component capability 往 rack EMC qualification 追的具名入口
evidence_boundary: 產品公告與 AI 終端說法沒有共同 part、客戶、placement、test report、qualification 或損益；只建立能力橋，不建立受惠、份額或排行
-->

<!-- impact
group_id: powersupply
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: 高功率供電、conducted emission、filter 與實驗室 1MW+ power capability 使電源族群成為責任鏈的必要搜尋路由
evidence_boundary: 沒有 universe 電源公司具名 AI rack EMC test plan、qualified part、認證責任、lab capacity、出貨或財務分母
-->

<!-- impact
group_id: serverodm
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: ODM／rack integrator 可能決定最終 equipment configuration、纜線與 sidecar 組合，是模組證書能否沿用及誰承擔 full-rack retest 的查核位置
evidence_boundary: 一般 server／rack 組裝能力不證明承擔 EMC certification；沒有具名 test plan、責任分工、失敗案例、訂單或毛利
-->

## 監測器

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C5,C8
metric: full-rack EMC 的被測配置、法規／標準邊界、lab chamber／weight／power capability、可用時槽、lead time 與模組證書沿用規則
source_ids: S1,S2,S3,S4
watch_source_ids: S1,S2,S3,S4
frequency: monthly
next_check: 2026-08-31
trigger: 至少兩個獨立 operator／lab 公布具名 rack configuration、accredited scope、capability、排程與 final-test／simulation／pre-compliance 邊界
invalidation: lab census 顯示能力與時槽並不稀缺，或正式規則允許既有模組／子系統證書完整覆蓋解耦式整櫃且無需 system retest，則 C8 的瓶頸候選被拒絕、C5 必須縮窄
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C4,C6,C7
metric: 2327 與 universe 電源／ODM 是否首次揭露具名 EMI part、rack placement、frequency／attenuation target、qualification、認證責任、production shipment 與可辨識損益
source_ids: S5,S6
watch_source_ids: S7
frequency: quarterly
frequency_detail: 各公司 Q2 財報與法說後複核
next_check: 2026-09-30
trigger: 買方 test plan／認證報告與公司申報雙向核對同一 part、rack configuration、qualification、出貨與財務分母
invalidation: 後續仍只有通用 EMI 產品、AI 終端敘事、PSU／rack 能力或展會展示，則 C6 維持查核入口、C7 維持待驗證
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C9,C10,C11,C12,C13,C14
metric: 具名完整 AI rack 報告是否揭露九欄護照、large-EUT 場地／方法選擇、量測裕量與不確定度、認可 scope、版本差異、跨場地重現及 qualification／deployment／財務鏈
source_ids: S8,S9,S10,S11
watch_source_ids: S4,S11
frequency: monthly
next_check: 2026-08-31
trigger: operator／lab 公開同一量產 rack 版本的配置、負載、纜線、方法、場地、量測結果、uncertainty／decision rule、accredited scope、retest 與重複量測，且平台／公司文件能雙向對齊採用與財務分母
invalidation: 主管機關或認可機構若正式說明更小的欄位集即可充分重現指定結果，或具名跨場地資料顯示本文某欄與可比性無關，則縮窄 C13；完整具名證據出現則升格 C14，而不是反推所有 rack 或公司皆成立
-->

## 還不能下哪些結論

- OCP 訪談提到「全球一至兩家」，不能直接當成全球實驗室全面盤點；仍要有具名能力、可用時槽與等待時間資料。
- FCC 或 CISPR 32 提供方法與標準邊界，不代表每一套 AI 機櫃都依法用完整機櫃做同一種測試；適用程序與被測配置必須逐案確認。
- FCC 對大型設備新增替代距離與測試體積，不代表所有 AI rack 都適用該條款，更不證明大型 chamber 或時槽稀缺。
- 一份報告缺少九欄中的部分資料，只能標成不可比較；九欄護照本身也不是官方標準、法律意見或產品合格證。
- 測試裕量沒有搭配方法、偵測器、頻寬、不確定度與判定規則時，不能被讀成跨版本安全餘裕或通用 guard band。
- 實驗室有 NVLAP 或其他認可標誌，只能回到指定 scope、地點與活動查核，不能說產品獲得 NIST／NVLAP certification、approval 或 endorsement。
- 元件規格、吸波材料產品頁、模擬、正式送驗前測試或子系統證書，都不能冒充完整機櫃的最終測試結果。
- 國巨的通用抑制材料能力與廣義 AI 成長敘述，沒有共同產品、客戶或資格驗證，不能拼成 AI 機櫃訂單。
- 電源或系統組裝廠位在責任鏈上，不等於已經受惠；沒有測試計畫、認證責任、量產出貨與損益資料，就只保留搜尋方向。
