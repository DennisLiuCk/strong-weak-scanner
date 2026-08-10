# AI 機櫃 EMC 驗證：元件能抑制雜訊，不代表整櫃就能進實驗室

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

## 新手先讀：這篇在講什麼

### 名詞小字典

- **EMC／EMI**：EMI 是設備產生或受到的電磁干擾；EMC 是整套設備在限制干擾、又能正常工作的相容性結果，兩者不是同一個零件名稱。
- **傳導／輻射排放**：雜訊可能沿電源線或訊號線跑出去，也可能像天線一樣從機構與纜線輻射出去；同一個濾波器不會自動處理所有路徑。
- **CISPR 32**：IEC 體系中針對多媒體設備排放要求與可重複量測程序的標準；它定義設備層測什麼，不替任何特定機櫃出具通過證明。
- **正式送驗前測試（pre-compliance）**：以較小場地、探棒、模擬或子系統測試先找出風險；它可降低重測機率，但不能冒充正式合規結果。
- **隔離測試室／旋轉台（chamber／turntable）**：隔離外界雜訊的測試空間與旋轉被測設備的平台；機櫃太大、太重或需要兆瓦級供電時，傳統實驗室硬體可能根本放不下或帶不動。
- **FCC**：美國 Federal Communications Commission；本文只用其 KDB 量測指引與 accredited-firm 資料入口，不替特定設備判定法律適用性。
- **PSU**：電源供應器；它可能是傳導雜訊路徑與正式被測配置的一部分，但元件或單機測試不自動覆蓋整櫃。

### 三句話抓重點

- OCP 2026 訪談由 Meta 的 AI 硬體電磁相容負責人指出，解耦式、重型、兆瓦級 AI 機櫃讓測試室尺寸、旋轉台承重、供電與實驗室可用量能同時成為送驗瓶頸。
- IEC CISPR 32 與 FCC 的量測指引／合格測試機構入口能定位設備排放與測試責任，但 FCC 也明說，名單本身不保證某家實驗室能測量特定裝置。
- 因此元件有抑制電磁干擾的功能、子系統做過預掃、設備符合某標準，以及整櫃能被正式測試是四件事；2327 國巨目前只接到第一層產品能力，沒有 AI 機櫃客戶驗證或財務映射。

### 為什麼重要

**先看問題怎麼從單機變成整櫃。** 一般伺服器可以把單機送進既有隔離測試室。AI 系統卻逐步
把運算、供電與液冷拆到多個機櫃或側掛設備，再用高速纜線與高壓供電組合。原本能測單機的
實驗室，未必放得下、帶得動，也未必供得起完整機櫃。

**別把元件測試當成整櫃合規。** 最容易犯的錯，是看到共模扼流圈、吸波材料或電源供應器通過
元件規格，就以為整櫃合規問題已經解決。元件測試只回答這顆零件能處理哪一類雜訊，無法回答
重新接線、裝進機構並同步運作後，整櫃會如何排放電磁雜訊。

**再拆開每一層的責任。** 零件抑制哪條雜訊路徑？子系統如何預掃？最後送驗的設備配置是什麼？
實驗室能否承擔它的尺寸、重量、供電與量測需求？測試失敗後又由誰重設計？只有把這些問題
分開，才能判斷瓶頸落在被動元件、電源、機構／系統組裝、測試服務還是系統架構，不能因為
「電磁相容很重要」就把某一族群寫成受惠者。

**最後用三個責任盒查證。** 元件層回答「能抑制哪種雜訊」；設備層回答「指定配置是否符合排放
要求」；實驗室層回答「場地是否真的能承載並量測完整配置」。一份文件若只回答其中一層，就
不能替另外兩層下結論。

### 接下來怎麼追

- 2026-08-31 重查 OCP 的測試與驗證工作組／訪談、IEC 與 FCC 入口，尋找具名整櫃測試方法、被測配置、認可範圍，以及實驗室供電、承重、測試室尺寸與排程資料。
- 國巨 2026Q2 法說後，檢查是否首次把國巨／KEMET 的電磁干擾抑制元件連到 AI 機櫃、具名客戶驗證、量產料號、客戶與可辨識收入；只重複 AI 終端成長不算。
- 等待大型雲端業者或系統組裝廠公開：模組證書能否沿用到解耦式整櫃、哪些配置變更會觸發重測，以及模擬／正式送驗前測試能替代到哪個邊界。

### 想一想

- 如果每個運算托盤、電源供應器與液冷側掛設備都各自有合規文件，整櫃重新接線與同步運作後的輻射路徑真的會保持不變嗎？
- 全球實驗室數量若不少，但只有極少數具備足夠承重、供電與 chamber 尺寸，應該量「家數」還是量「可用時槽」？
- 一片 EMI 吸波材能通過自身材料規格，卻沒有 rack placement、frequency、attenuation target 與 system test，它對整櫃合規的價值能被量化嗎？

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

## 四道關卡，不能用同一張證書跳過

**第一道是元件與材料。** 共模扼流圈、濾波器、屏蔽結構、導電墊片、吸波材與 PCB 佈局，
各自處理不同的傳導／輻射雜訊路徑。國巨集團的 FLEX SUPPRESSOR 能證明公司有一項具名
EMI 抑制能力（C4），但產品公告沒有 AI rack placement、目標頻帶或 system attenuation。

**第二道先確認被測設備範圍。** CISPR 32 說明多媒體設備的排放要求與可重複量測目標（C2）；
它不會自動回答一套由運算機櫃（compute rack）、電源側櫃（power sidecar）、液冷設備
（cooling skid）與外接纜線構成的完整系統，哪一種配置才是正式被測物。

**第三道是量測程序與責任。** FCC KDB 提供一般量測方法入口；若採用其他方法，需向
FCC Laboratory 查詢。合格測試機構資料集（accredited-firm dataset）也明示，使用者仍須自行
確認該機構是否能量測特定裝置（C3）。「在名單上」因此不等於能處理兆瓦級重型機櫃。

**第四道才是實驗室可用量能。** OCP 訪談指出重量、供電與隔離測試室尺寸同時限制實驗室
可用性，並提出全球一至兩家的急迫主張（C1）。本研究接受前三項物理限制作為待查核機制，
卻把實際家數、時槽與部署延遲留在 C8；沒有具名實驗室的全面盤點（census），就不能把訪談
升格成市場規模。

## 如何判斷一份 EMC 證據走到哪一層

先看被測物。零件 datasheet 上的 insertion loss、阻抗或吸收頻帶，只能回答該元件在指定
fixture 與條件下的能力；它沒有包含 PCB 走線、纜線、機構開口、接地、PSU、風扇與液冷管路
共同形成的耦合路徑。若公告未寫 AI rack placement、目標頻帶與 system configuration，研究線
就停在 component capability，不能直接升為設備 qualification。

再看測試名稱與配置。Pre-scan、simulation 或 subsystem test 可用來找熱點與降低重測風險，
但必須知道最後哪個 configuration 會被當成 equipment、運作模式如何排列、外接纜線與 sidecar
是否同時通電。CISPR 32 publication page 提供的是設備排放範圍與可重複量測目標（C2），FCC
KDB 則提供一般程序入口（C3）；兩者都沒有替某套解耦機櫃回答上述配置問題。

第三個檢查是實驗室的實際 scope，而不是只看名錄。對大型 AI rack，至少要核對 chamber 尺寸、
turntable 或地面承重、可安全提供的電力、冷卻與配線方式、天線距離及 accredited scope。FCC
資料集明示使用者仍須選擇能量測特定裝置的機構，所以「名單上有很多家」與「很多家能立即
測這個 configuration」是不同主張；反過來，也不能用一場訪談直接證明全球只剩一兩個時槽。

最後才問商業後果。若設計在正式送驗前已用 simulation 與 pre-compliance 收斂，lab 稀缺不一定
轉成長期部署延誤；若模組證書能在配置未改變時沿用，也可能縮小 full-rack 重測範圍。需要看到
具名 test plan、fail／retest 紀錄、lead time 與量產排程，才可把工程摩擦升為 hard stop。對公司
亦同：供應商與買方要雙向對上 part、placement、qualification、shipment 與財務分母，才會從
能力線升到商業線。這也是本文把 2327 留在具名 EMI 產品能力，而不宣稱 AI 機櫃受惠的原因。

## 這篇對個股判斷的用處與界線

2327 是被動族群新增的第一條具名橋，但橋只到元件能力。公司法說所稱 AI 動能跨多產品類別，
KEMET 產品公告又只寫 commercial／telecom／automotive，兩份文件沒有共同 part、客戶或
qualification。把它們並列的目的，是建立「下一份證據要找什麼」，不是把兩句話拼成受惠
故事（C6）。

powersupply 與 serverodm 目前甚至沒有具名公司邊，只保留搜尋路由：電源可能是 conducted
emission 與高功率測試的核心，ODM 可能負責 system configuration，但沒有 test plan、認證
報告與申報文件就不能分配價值。C7、C8 任何一項未解前，本文不支持個股排序、營收預測或
投資動作。

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

## 目前不能下的結論／待驗證

- 不能把 OCP 訪談的「全球一至兩家」當成本研究完成的全球 lab census；需要具名能力、時槽與 lead-time 資料。
- 不能把 FCC Part 15 或 CISPR 32 寫成「每一套 AI rack 都依法以完整機櫃做同一種認證」；適用 procedure 與 equipment configuration 必須逐案定位。
- 不能把元件規格、吸波材產品頁、pre-compliance、simulation 或子系統證書當成 full-rack final test 的替代品。
- 不能把 2327 的 EMI 產品能力與廣義 AI 成長敘述拼成 AI rack 訂單；兩份文件沒有共同 part、客戶或 qualification。
- 不能由 power 或 server ODM 位在責任鏈上推導受惠；沒有 test plan、認證責任、production shipment 與損益就只保留搜尋路由。
