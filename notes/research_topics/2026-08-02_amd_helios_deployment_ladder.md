# AI 機櫃做出來，不等於客戶已上線：用六個關卡讀懂 AMD Helios

<!-- research_topic
topic_id: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-07-23
last_reviewed_at: 2026-08-12
review_due: 2026-08-15
source_type: mixed
publisher: AMD / Microsoft
publisher_domain: amd.com
canonical_url: https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era
source_chain_id: amd-microsoft-helios-20260720-0723
stock_ids: 2356,3037,3189,3231,3693,3711,6239,6669,8046
group_ids: packtest,pcb,serverodm
trigger_type: product_ramp_and_named_deployment
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C11
base_confidence: medium
confidence_basis: Microsoft 與 AMD 對 2026-07-20 同一合作事件做雙方一手確認；AMD 現行產品頁與 OCP 的 Open Rack Wide 文件再把 reference design、品牌系統化、整櫃責任與客戶部署分開，但部署節點仍多為 AMD 或合作方的前瞻時程，且沒有完整 OEM 資格矩陣、客戶機群分母或台灣公司訂單與財務證據
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: recent_primary_source_market_scan
evidence: source_chain:amd-microsoft-helios-20260720-0723
-->

<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: named_deployment_ladder_separated_from_taiwan_order_mapping
evidence: sources:S1,S2,S3,S4,S5
-->
<!-- transition
date: 2026-08-08
from: triaged
to: triaged
reason: editorial_glossary_for_repeated_terms_no_conclusion_change
evidence: editorial:readability
-->

<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_plain_language_wave6_compute_interconnect_learning_no_conclusion_change
evidence: editorial:plain_language_wave6
-->

<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave97_helios_six_stage_five_customer_timeline_and_six_gate_ladder
evidence: editorial:reader_layer_only_no_claim_source_monitor_or_impact_change
-->

<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: corrected_production_reading_with_reference_design_and_integrated_rack_contract
evidence: sources:S12,S13,S14,S15
-->

<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_configuration_passport_change_triggered_regression_and_company_stage_refinement_no_thesis_change
evidence: sources:S16,S17,S18,S19,S20,S21
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **機架級系統（Rack-scale）**：把運算晶片、網路、電力、散熱與軟體整合成一整櫃交付；它比單顆晶片更接近可用設備，但不代表客戶已正式上線。
- **參考設計（Reference design）**：平台方公開的整體藍圖與共同介面，讓製造夥伴能做自己的品牌系統；藍圖本身不一定是平台方直接出售的成品。
- **品牌系統**：整機廠依參考設計選定零件、韌體與製造版本後，以自己的產品名稱交付；它仍要另做資格驗證與客戶驗收。
- **開放式寬機架（Open Rack Wide／ORW）**：為高密度人工智慧設備設計的雙寬機架標準，提供較高功率、液冷、較寬托盤與共同機械介面。
- **第三代開放式機架（Open Rack v3／ORV3）**：Open Compute Project 的第三代機架規格家族；它與較寬的 ORW 都提供共同機械與設施介面，但不是同一份完整產品資格。
- **運算托盤（Compute tray）**：可抽換的運算模組，通常承載主機處理器、加速器、記憶體與網路介面；一個托盤合格不等於整櫃合格。
- **交換托盤（Switch tray）**：承載機架內高速交換晶片與管理元件，讓多個運算托盤互相傳資料。
- **機架內擴充（Scale-up）**：讓同一台或同一機架內的多顆加速器像更大的共同運算單元一樣協作。
- **跨機架擴充（Scale-out）**：用網路把多個機架或伺服器連成更大的叢集；機架內外的頻寬、延遲與故障責任不同。
- **電力架與垂直匯流排（Power shelf／busbar）**：集中轉換、監控並沿機架分配電力的模組與導體；有電不等於每個托盤在負載變化下都穩定。
- **液冷分歧管與快接（Cooling manifold／quick disconnect）**：把冷卻液分送到運算與交換托盤，並允許維修時快速接合或分離的管路介面。
- **機架管理控制器（BMC／rack manager）**：監控電力、溫度、風扇、漏液與硬體狀態，並執行啟停、告警、更新或隔離等低階管理工作。
- **軟體堆疊（Software stack）**：讓驅動、運算函式庫、框架與機群管理共同操作硬體；硬體能開機不等於工作負載已可持續運行。
- **ROCm**：AMD 的開放式人工智慧運算軟體平台，涵蓋驅動、函式庫與開發工具；軟體名稱出現在方案中不等於特定版本已通過整櫃驗證。
- **Redfish**：DMTF 定義的硬體管理資料模型與介面，可描述系統、盤點、更新與遙測；能讀到資料不等於數值已校正或系統已驗收。
- **可維修性與生命週期控制（Serviceability／lifecycle control）**：設備能否快速定位故障、抽換模組、更新版本、復原並持續管理整個機群的能力。
- **開始生產（Production）**：製造端已進入生產階段；這比只有設計圖更前進，但不等於產品已送到客戶手上。
- **實際出貨（Shipment）**：產品真正離開供應端並交付客戶；預告未來會出貨，不等於已發生出貨。
- **客戶測試與驗證（Validation）**：客戶仍在確認系統能否穩定執行自己的工作；開始測試不等於已通過、採購或部署。
- **正式上線（Online）**：系統已接通並投入運行；本文來源中的預計上線，不等於截至資料日已上線，也不自動代表已對外商用或已有收入。
- **部署（Deployment）**：把設備放進實際環境、接好並開始使用的過程；可以是一小批，也可以是後續擴張，必須看日期、範圍與容量。
- **雲端產品規格（SKU）**：雲端客戶可以選購或使用的具體產品配置；被預告的規格不等於已普遍開放使用。
- **即將推出（Upcoming）**：產品已被預告，但尚未證明進入測試開放或正式推出。
- **測試開放（Preview）**：產品開放給部分使用者測試；仍可能限制區域、名額、功能與服務承諾。
- **正式推出（Launched／GA）**：產品已進入正式供應狀態；仍要另外看可用區域、使用量與收入。
- **可用區域**：雲端產品實際在哪些資料中心區域可選用；公布型號但沒有區域，仍不能證明客戶可以立即使用。
- **利用率**：設備真正被工作負載使用的程度；設備已安裝，不等於一直在有效運轉。
- **吉瓦（GW）**：十億瓦，本文用來描述大型人工智慧基礎設施的電力規模；它是容量尺度，不是設備台數或採購金額。
- **最高可達（Up to）**：合作或容量的上限，不是目前已啟用、已採購或最後一定會達到的數量。
- **具名客戶**：公開文件直接點名的客戶；被點名比匿名市場傳聞更具體，但仍要分清預告、測試與實際使用。
- **生態系夥伴**：公開參與設計、製造、封裝或材料供應的公司；被列名只能證明合作角色，不能自動推成新增訂單、收入或毛利。
- **Helios**：AMD 的機架級人工智慧系統平台名稱，也就是本文追蹤的整櫃系統。
- **MI455X**：AMD 的 Instinct 加速器型號，是 Helios 裡執行人工智慧運算的核心晶片。
- **ND MI455X v7**：微軟 Azure 雲端虛擬機器的規格名稱；它是一個雲端產品型號，不是硬體出貨數量。
- **高架扇出橋接（EFB）**：用橋接結構連接同一封裝內多顆晶片的先進封裝路徑；合作文件出現此技術，不代表封裝商已有可辨識訂單。
- **2.5D 封裝**：把多顆晶片放在中介層或橋接結構上互連的封裝方式；具備技術能力不等於已進入具名產品量產。
- **客製晶片（ASIC）**：為特定客戶或任務設計的晶片；雲端客戶可能同時採用客製晶片與外部加速平台。
- **多架構共存**：同一客戶同時使用不同供應商或自研晶片；單一平台上線不等於其他架構被完全取代。
- **整機代工（ODM）**：把伺服器或機架系統設計、組裝並交付客戶的製造角色；合作列名不等於已取得新增份額。
- **機構件**：承載並固定機架、運算托盤與其他零件的結構；參與設計不等於量產數量或收入已確定。
- **載板**：承接晶片封裝內部電性連接與支撐的基礎材料；廣泛 AMD 合作不等於 Helios 專屬訂單。
- **資格認證（Qualification）**：客戶或平台確認產品符合規格與可靠度要求的過程；參與認證不等於已通過或已量產。
- **配置身分證（Configuration passport）**：本文給「硬體、韌體、軟體、網路、電力、冷卻、場站與測試條件版本清單」的白話名稱；它讓測試結果能對回真正受測的那一櫃。
- **工廠盤點檔（Factory inventory）**：機櫃離廠時記錄托盤、交換器、電力架、序號與數量的清單；名稱相同但盤點不同，不能直接共用結果。
- **物料清單（BOM）**：製造某個品牌型號所需的硬體零件與版本清單；參考設計不等於每家整機廠採用相同物料。
- **軟體物料清單（SBOM）**：列出韌體或軟體元件與目標版本的清單；本文引用的 NVIDIA 範例用它核對應更新到哪個版本，不代表所有業者都用同一格式。
- **黃金配置（Golden configuration）**：已經測過並被允許複製部署的基準版本；只有名稱相同、版本不同的機櫃不能自動繼承它的資格。
- **回歸測試（Regression test）**：硬體、韌體、線纜或其他關鍵配置改變後，重跑受影響測項，確認原本通過的功能沒有退步。
- **變更控制（Change control）**：記錄誰改了什麼、為什麼改、影響哪些測項，以及是否要回退或重新簽核的管理方法。
- **機櫃啟用（Rack bring-up）**：機櫃抵達場站後，依序盤點、供電、設定、更新、連線、測試並交接的過程；成功開機只是其中一步。
- **生產交接（Production handover）**：工程團隊把已驗證的配置、測試結果、告警基準、維護方法與簽核交給日常營運團隊；交接完成仍不等於已有大量利用率或財務貢獻。
- **COMPUTEX（台北國際電腦展）**：業者展示新產品、設計與合作的展會；展位能運作或新聞稿預告量產，不等於客戶已驗收、出貨或形成收入。
- **以 Helios 為基礎（Helios-based）**：系統以 Helios 架構為基礎，但不必然代表每個零件都只供 Helios 使用。
- **Helios 專屬（Helios-specific）**：文件明確把產品或出貨限定到 Helios；一般 AMD 合作不能自動改寫成專屬供應。
- **可辨識收入**：公司財報或說明能把收入與具名產品、客戶或業務分部合理連結，而不是只看產業總需求。
- **日月光／矽品／力成（ASE／SPIL／PTI）**：三家台灣封裝測試業者的中英文名稱；被 AMD 文件列為合作角色，仍不等於已有 Helios 訂單或財務貢獻。
- **現金流足跡**：訂單與收入最後是否轉成現金，並能在存貨、應收帳款或營業現金流看到合理變化。

### 三句話抓重點

- 一套整櫃架構可以先是公開藍圖，再由製造夥伴做成品牌系統；「架構進入生產」不等於成品已交到客戶。
- 一整櫃還要讓運算、兩類網路、供電、液冷、控制軟體與維修共同通過；結果只屬於受測版本，關鍵配置改變後還要判斷哪些測項必須重跑。
- 台灣公司被列為生態系夥伴，只能證明合作角色；還要看到具名產品、量產出貨、可辨識收入與現金流足跡，才能談公司受惠。

### 為什麼重要

把人工智慧機櫃想成一棟要交付的建築：參考設計像共同藍圖，整機廠把它做成品牌系統才像
承包商蓋出建物；出貨是送到現場，整櫃資格與客戶驗收像驗屋，正式上線才像住戶真的入住。
合作名單只表示參與工程，還不是每家公司已經收款。這篇因此把藍圖、品牌系統、整櫃驗證、
客戶採用與公司財務分開，避免把前一層的進度直接當成下一層已完成。

### 接下來怎麼追

- 先看製造端是否從「預計出貨」變成有日期、有客戶邊界的實際交付。
- 要求具名整機廠公開品牌型號、配置身分證，以及運算、網路、供電、液冷和維修共同通過的驗收與變更後重驗範圍。
- 再看各客戶是否由產品預告或測試，前進到可用區域、正式上線與可描述的部署範圍。
- 最後查台灣公司自己的季報、法說與重大訊息，是否同時出現具名產品、量產出貨及財務足跡。

### 想一想

- 如果工廠已能生產，但客戶仍在測試，哪一個部署關卡尚未完成？
- 如果平台方只提供藍圖，誰要把零件做成可出貨的品牌系統，並對整櫃結果負責？
- 產品頁只寫「即將推出」，和「已可使用」之間還差哪些證據？
- 一家公司被列為合作夥伴後，還要看到哪些公司級資料，才能把「參與」升級成「受惠」？
- 當客戶同時使用不同運算架構時，單一平台上線是否一定代表整體支出增加？

## 先看一整櫃有哪些共同責任

機架級系統不是把很多加速器塞進同一個外殼。運算、資料移動、電力、液冷、控制與維修都要
共享同一個機械和版本邊界；任何一層失效，都可能讓整櫃降速、停機或無法交付。

| 本文八條責任線 | 它負責什麼 | 本輪可確認的 Helios 設計 | 整櫃要驗收什麼 | 不能直接推成 |
| --- | --- | --- | --- | --- |
| 1. 機架與共同介面 | 固定寬度、托盤、電力、冷卻與抽換介面 | 採 Open Rack Wide 雙寬參考設計 [S12][S14] | 品牌系統的尺寸、承重、接點、安裝與機房相容 | 採用標準就已取得 OCP 認證或客戶驗收 |
| 2. 運算托盤 | 承載主機處理器、加速器、記憶體與網路介面 | AMD 公開 CPU、GPU、AI NIC 與 DPU 的托盤角色 [S12] | 型號、版本、功耗、熱、資料正確性與可抽換性 | 元件規格可用就代表整個托盤或整櫃合格 |
| 3. 機架內交換 | 讓多顆加速器在同一機架內高頻寬協作 | 交換托盤與 scale-up cartridges 使用 UALink over Ethernet [S12] | 拓撲、頻寬、壅塞、錯誤恢復與多托盤壓力 | 峰值頻寬等於工作負載長時間有效效能 |
| 4. 跨機架與前端網路 | 把機架接成叢集，並處理儲存、安全與用戶流量 | AI NIC 負責 scale-out，DPU 卸載網路、儲存與安全 [S12] | 跨機架流量、故障隔離、重試、儲存和前端服務 | 機架內網路通過就等於整個資料中心可用 |
| 5. 集中供電 | 轉換、監控並把電送到每個托盤 | Power shelf 經垂直匯流排管理與分配整櫃電力 [S12] | 穩態與突波負載、保護、備援、遙測與維修隔離 | 電力架存在就代表機房供電、備援與效率都完成 |
| 6. 液冷迴路 | 把冷卻液送到運算與交換托盤並帶走熱 | Cooling manifold 透過快接向托盤分配冷卻液 [S12] | 流量、壓差、溫度、漏液、材料相容與單托盤隔離 | 接上水管就代表散熱容量、可靠度與維修都通過 |
| 7. 控制與軟體 | 啟動硬體、執行工作負載並管理整個機群 | BMC 管理交換托盤，ROCm 支援框架、觀測與生命週期 [S12] | 驅動、韌體、函式庫、框架、遙測、更新與復原 | 硬體開機或單次跑分等於生產工作負載穩定 |
| 8. 可維修與營運 | 在不中斷整個機群下定位、抽換與恢復故障模組 | 模組化托盤及整合電力、冷卻、網路連接主打低干擾更換 [S12][S13] | 故障定位、抽換時間、備品、版本控制與復原後重驗 | 設計宣稱可維修就等於客戶現場達成可用率 |

八條責任線只是把整櫃驗收拆成可查問題，不是固定上下游、產品規格比較或供應商排名。AMD 頁面
上的效能與頻寬數字屬公司設計值；本文不用它們證明客戶實測、競品高低或台灣公司收入。

## 再分清參考設計、品牌系統與客戶機群

**本輪修正：** 原判讀把 AMD 所稱「已進入生產」寫成已跨過只有參考設計的階段；2026-08-12
接受的 AMD 現行常見問答卻明確說 Helios 是提供給 OEM／ODM 的參考設計，不是 AMD 直接出售的產品。
目前較精確的讀法是「參考設計與合作製造已前進」，但品牌型號、整櫃資格、客戶交付與機群仍要分開。

| 本文五種交付物 | 誰要交付 | 必須固定什麼 | 本輪證據 | 不能直接推成 |
| --- | --- | --- | --- | --- |
| 1. 開放標準與參考設計 | 標準組織與平台設計方 | 機架介面、元件角色、網路、電力、液冷與軟體藍圖 | OCP 已列 ORW 規格；AMD 把 Helios 定義為 ORW 參考設計 [S12][S14] | 市場上已有可採購的單一 AMD 成品 |
| 2. 整機廠品牌系統 | OEM／ODM 與供應鏈 | 品牌型號、BOM、板卡、托盤、韌體、冷卻與製造版本 | AMD 稱藍圖正與夥伴分享，品牌配置與完整 BOM 未公開 [S12] | 所有夥伴使用同一配置、已量產或已有訂單 |
| 3. 整櫃資格與驗收資料包 | 整機廠、平台方與客戶工程團隊 | 八條責任線的測試條件、版本、結果、變更與回退 | 目前沒有捕捉到一套具名品牌系統的完整公開資料包 | 單一托盤、網路、電力或液冷測試能替整櫃背書 |
| 4. 出貨與現場接收 | 製造商、物流、資料中心與客戶 | 序號、數量、日期、場址、安裝、機房介面與接收結果 | 仍只有 2026 下半年 shipment／volume deployment 的前瞻時程 [S2][S12] | 生產宣稱等於已交貨、已安裝或已驗收 |
| 5. 生產機群與財務 | 客戶營運、平台與供應商財務團隊 | 上線規模、工作負載、可用率、重複出貨、收入、毛利與現金流 | 客戶節點仍分散在預告、驗證與未來部署；台灣公司財務未證 | 合作名單、容量上限或單次上線等於持續獲利 |

這五種交付物可以由不同公司負責，也可能部分並行；它們不是一條所有系統必然同速通過的直線。
參考設計的價值是讓介面與責任更容易共用，不是把資格、互通、量產與客戶營運自動完成。

## 同一型號還要有一張配置身分證

**先固定你測的是哪一櫃。** 同一個平台名稱可以有不同托盤數、硬體修訂、韌體、網路拓撲、
電力與冷卻條件。NVIDIA 的機櫃啟用清單是一個具體例子：它先匯入工廠盤點檔，核對運算托盤、
交換托盤與電力架數量，再記錄序號、網路與設定；這不是 Helios 已通過的證據，只示範如何避免
把「同名機櫃」誤當成「同一配置」[S16]。

**再把測試結果綁到同一版本。** 盤點硬體只回答「有什麼」，還要用 BOM／SBOM、目前與目標
韌體、軟體映像、網路設定、場站輸入及測試條件回答「用哪個版本、在哪種環境通過」。DMTF
Redfish 把軟硬體盤點與更新服務、遙測服務做成不同的機器可讀資源，能協助記錄與觀察；資料模型
存在本身卻不等於感測器已校正、門檻合理或整櫃已驗收 [S18]。

**任何關鍵變更都要決定重跑哪些測試。** NVIDIA 要求初次安裝、韌體升級，以及托盤、交換器、
線纜等維修替換後重新啟動並驗證服務、連線、交換網路與點對點拓撲；Google 的 ORV3 實作規格
也要求以共同決定的最壞情境測試、審查資料並記錄設計變更 [S17][S19]。這些是競品與通用機架的
方法證據，不是 Helios、任何品牌型號或台灣公司的資格結果。

| 本文六個配置欄位 | 要留下什麼 | 它防止哪種誤讀 | 變更後先問什麼 |
| --- | --- | --- | --- |
| 1. 工廠硬體與盤點 | 品牌型號、托盤／交換器／電力架數量、料號、序號、硬體修訂 | 同型號就一定同 BOM | 零件、數量或修訂是否改變，影響哪條責任線？ |
| 2. 韌體、軟體與 SBOM | 每個元件目前／目標韌體、作業系統、驅動、函式庫、管理映像 | 更新一個元件不會影響其他層 | 相容矩陣、更新順序、回退與穩定測試要不要重跑？ |
| 3. 網路、拓撲與設定 | 位址、命名、機架內外連線、線纜、設定檔與修改紀錄 | 連得上就代表拓撲和效能都正確 | 路徑、頻寬、錯誤恢復與點對點拓撲是否仍一致？ |
| 4. 電力、冷卻與場站輸入 | 供電、備援、冷卻水溫／流量／壓力、環境與機房介面 | 工廠測過就能直接搬到任何機房 | 場站條件是否仍在資格包絡內，需不需要重做熱與功率測試？ |
| 5. 工作負載、條件與基準 | 測試版本、負載、持續時間、通過門檻、效能／熱／功率／穩定基準 | 單次開機或峰值跑分等於長期可用 | 原測試是否涵蓋這次變更與最壞情境？ |
| 6. 簽核、交接與變更紀錄 | 技術／客戶簽核、未解問題、監測基準、維護計畫、改版與重驗範圍 | 文件交付就等於生產機群已穩定 | 誰核准變更、誰驗證、誰接手營運，結果綁到哪一版？ |

這張表是本文依 NVIDIA、DMTF 與 Google／OCP 文件整理的研究框架，不是宣稱業界已有唯一標準
「配置身分證」。它的用途是讓讀者能追問一個結果到底屬於哪一套硬體、軟體與場站版本，而不是
替尚未公開的 Helios 品牌系統補出測試資料。

## 先把六個部署關卡排成順序

一套機架級系統可以「已經做得出來」，卻還沒有真正送到客戶、通過測試或投入使用。先把
六個關卡排好，後面看到任何公司或客戶動詞時，才知道它回答的是哪一題。

| 本文六個關卡 | 白話意思 | 可接受的證據 | 本篇目前到哪裡 | 不能直接推成 |
| --- | --- | --- | --- | --- |
| 1. 方案成形 | 整櫃架構、主要元件與合作角色已被公開 | 具名參考設計、標準、元件表與合作文件 | AMD 公開 Helios 架構並明示它是供 OEM／ODM 使用的參考設計 [S12] | 市場上已有可採購的單一 AMD 成品或所有夥伴配置相同 |
| 2. 開始生產 | 製造端把參考設計做成可重複組裝的系統 | 整機廠品牌型號、BOM、版本與製造狀態 | AMD 曾稱平台 now in production，但現行常見問答仍把它定義為參考設計 [S4][S12] | 品牌系統已出貨、整櫃已驗收或已有收入 |
| 3. 實際出貨 | 產品真的離開供應端並交到客戶 | 已發生的出貨日期、客戶與範圍 | 目前只有 2026 下半年開始出貨的規劃 [S2] | 規劃已如期完成或數量已確定 |
| 4. 客戶測試與產品開放 | 客戶測試自己的工作，或雲端規格開始可用 | 驗證完成、測試開放、正式推出與可用區域 | Meta 仍在測試；Azure 規格仍是預告 [S1][S4] | 已通過驗證、已普遍可用或已有利用率 |
| 5. 正式上線 | 客戶把系統接通並投入實際運行 | 客戶或供應商確認上線日期與部署範圍 | OpenAI 只有 2026 年第四季預計上線 [S4] | 截至資料日已上線、已對外商用或已有收入 |
| 6. 規模部署與財務轉換 | 小批上線持續擴張，並落到供應商財務 | 已部署容量、重複出貨、收入、毛利與現金流 | 只有廣義容量目標與未來首批規劃 [S3][S5] | 容量上限已落地或台灣公司已受惠 |

這六關是本文整理資訊的閱讀順序，不是所有平台都會依同一節奏前進，也不是公司排名、
訂單推估或投資建議。

## 主張與證據帳本

<!-- research_source
source_id: S1
role: other_primary
source_kind: document
publisher: Microsoft
title: Microsoft expands Azure AI and HPC infrastructure with AMD
published_at: 2026-07-20
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://blogs.microsoft.com/blog/2026/07/20/microsoft-expands-azure-ai-and-hpc-infrastructure-with-amd/
locator: 開頭 infrastructure strategy、three upcoming Azure offerings 與 Production-scale AI inference — ND MI455X v7 段落
limitation: Microsoft 把 ND MI455X v7 稱為 upcoming offering，未提供 GA 日期、可用區域、部署數量或台灣供應商；同文並稱 Azure 同時採用自研 purpose-built silicon
independence_group: amd-microsoft-20260720
-->

<!-- research_source
source_id: S2
role: company_release
source_kind: document
publisher: AMD
title: Microsoft to Deploy Next-Gen AMD Instinct and AMD EPYC Processors as the Companies Expand Their Long-Term Strategic Partnership
published_at: 2026-07-20
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.amd.com/news-events/press-releases/detail/1291/microsoft-to-deploy-next-gen-amd-instinct-and-amd-epyc-processors-as-the-companies-expand-their-long-term-strategic-partnership
locator: News Highlights、Microsoft will deploy Helios 與 AMD will begin shipping Helios to customers including Microsoft in 2H 2026 段落；Cautionary Statement
limitation: 2026 下半年出貨與產品時程是 AMD 的前瞻性陳述，不是已完成出貨、Azure GA、收入或毛利
independence_group: amd-microsoft-20260720
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: AMD
title: AMD and Anthropic Announce Strategic Partnership to Deploy Up to 2 Gigawatts of AMD Instinct MI450 Series GPUs
published_at: 2026-07-22
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus
locator: News Highlights 與首段的 up to 2 GW、first gigawatt beginning in 1H 2027；另見最高 50 億美元股權投資段落
limitation: up to 2 GW 是合作上限且首個 GW 尚待未來部署；最高 50 億美元是 AMD 對 Anthropic 的股權投資承諾，不能與設備採購額混為一談
independence_group: amd
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: document
publisher: AMD
title: AAI 2026: AMD Delivers Full-Stack Compute for the Agentic AI Era
published_at: 2026-07-23
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era
locator: Helios now in production 段落；AMD Helios 與 partner deployment bullets，特別是 OpenAI Q4 online、Meta testing and validating
limitation: in production 是 AMD 對平台製造階段的敘述；客戶節點仍包含預期上線與驗證，且 AMD 的效能／經濟性數字屬自家測試，本文不據此做跨公司排名
independence_group: amd
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: document
publisher: AMD
title: AMD Announces More Than $10 Billion in Taiwan Ecosystem Investments to Accelerate AI Infrastructure
published_at: 2026-05-21
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.amd.com/news-events/press-releases/detail/1286/amd-announces-more-than-10-billion-in-taiwan-ecosystem-investments-to-accelerate-ai-infrastructure
locator: News Summary 的 multi-gigawatt deployments beginning 2H 2026、EFB ecosystem development、Panel-based innovation with PTI、Ecosystem Accelerates AMD Helios Deployment，以及 Unimicron／AIC／Nan Ya PCB／Kinsus 引言
limitation: 2H26 multi-GW 是 AMD 未分配到具名客戶的前瞻平台目標；超過 100 億美元是廣泛台灣生態系總投資敘述，未分配到個別公司；所有列名都沒有訂單、數量、ASP、收入或毛利，且載板三家公司未被寫成 Helios-specific
independence_group: amd
-->

<!-- research_source
source_id: S6
role: company_release
source_kind: living_index
publisher: AMD
title: AMD Investor Relations Press Releases
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.amd.com/news-events/press-releases
locator: 截至 2026-08-02，首頁可見 07-20 Microsoft、07-22 Anthropic 與 07-23 AAI 2026 公告，供後續查找新的 Helios 出貨、客戶或財務附件
limitation: 索引會持續變動且沒有單一發布日；只能作為未來重查入口，新公告必須另建 document source 才能更新 claim
independence_group: amd
-->

<!-- research_source
source_id: S7
role: other_primary
source_kind: living_index
publisher: Microsoft Azure
title: Azure Updates
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://azure.microsoft.com/en-us/updates/
locator: 截至 2026-08-02，頁面提供 In development、In preview、Launched 狀態定義；當日未取得可定位的 ND MI455X v7 獨立更新項目
limitation: 此頁由動態篩選產生且會持續改變；當日沒看到項目不是不存在的證明，未來命中須另存正式更新頁
independence_group: microsoft-azure
-->

<!-- research_source
source_id: S8
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 截至 2026-08-02，作為 2356、3037、3189、3231、3693、3711、6239、6669、8046 季報、法說及重大訊息的後續查找入口
limitation: 入口會持續更新且沒有單一發布日；產業公告不能替代各公司自己的產品、訂單與財務附件
independence_group: twse-mops
-->

<!-- research_source
source_id: S9
role: other_primary
source_kind: living_index
publisher: OpenAI
title: OpenAI News
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://openai.com/news/
locator: 截至 2026-08-02 的官方 News 索引，作為 OpenAI 自有 Helios 上線、基礎設施或時程更新的後續查找入口
limitation: 動態索引沒有單一發布日且目前不等於 OpenAI 已確認 Helios online；命中後須另建可定位 document source
independence_group: openai
-->

<!-- research_source
source_id: S10
role: other_primary
source_kind: living_index
publisher: Meta
title: Meta Newsroom
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://about.fb.com/news/
locator: 截至 2026-08-02 的官方 Newsroom 索引，作為 Meta 自有 Helios validation、部署或取消更新的後續查找入口
limitation: 動態索引沒有單一發布日且目前不等於 Meta 已完成 Helios validation 或部署；命中後須另建可定位 document source
independence_group: meta
-->

<!-- research_source
source_id: S11
role: other_primary
source_kind: living_index
publisher: Anthropic
title: Anthropic Newsroom
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.anthropic.com/news
locator: 截至 2026-08-02 的官方 Newsroom 索引，作為 Anthropic 自有 Helios 首個 GW、時程、縮量或取消更新的後續查找入口
limitation: 動態索引沒有單一發布日且目前不等於 Anthropic 已開始部署；命中後須另建可定位 document source
independence_group: anthropic
-->

<!-- research_source
source_id: S12
role: company_release
source_kind: living_index
publisher: AMD
title: AMD Helios Rackscale Solution
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.amd.com/en/products/rackscale-solutions/helios.html
locator: 現行常見問答明示 Helios is a reference design and not a product for sale，並稱藍圖供 OEM／ODM 打造品牌系統；System Architecture、Rack Scale Networking、Power and Cooling、Software and Lifecycle Management 段落分列 compute tray、switch tray、scale-up／scale-out、power shelf／busbar、cooling manifold／quick disconnect、BMC、ROCm、serviceability 與 lifecycle control
limitation: AMD 的現行產品頁會持續改變；設計架構、行銷值與夥伴時程不是獨立的品牌系統資格、實際出貨、客戶機群或財務證據，後續實質改版須另做 capture
independence_group: amd
-->

<!-- research_source
source_id: S13
role: company_release
source_kind: document
publisher: AMD
title: AMD Showcases “Helios” Rack-Scale Platform Built on the Open Compute Project Open Rack for AI Introduced by Meta
published_at: 2025-10-14
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://newsroom.amd.com/news/amd-showcases-helios-rack-scale-platform-built-o/
locator: News Highlights 與正文把展示品稱為 static display／reference design，並說明 Open Rack Wide、scale-up／scale-out、雙寬配置、quick-disconnect liquid cooling、power、serviceability 與 lifecycle management
limitation: 這是 AMD 對靜態展示與參考平台的公司公告，不是具名 OEM 品牌型號、完整 BOM、整櫃資格、實際出貨或客戶部署證據
independence_group: amd
-->

<!-- research_source
source_id: S14
role: standard
source_kind: living_index
publisher: Open Compute Project
title: Open Rack Specs and Designs
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/wiki/Open_Rack/SpecsAndDesigns
locator: 現行索引列出 APR26 的 Open Rack Wide Base Specification 1.0 與 Meta Open Rack Wide Design Specification 1.0，並把一致介面及 infrastructure creator／IT gear builder 文件層分開
limitation: 規格索引與版本存在不證明 Helios 或任一 OEM 品牌系統已符合規格、取得資格、量產、出貨或部署
independence_group: open-compute-project
-->

<!-- research_source
source_id: S15
role: standard
source_kind: document
publisher: Open Compute Project Foundation
title: Delivering an Open Data Center Ecosystem for AI
published_at: 2026-04-29
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/blog/delivering-an-open-data-center-ecosystem-for-ai
locator: 正文把人工智慧資料中心的 IT 與 physical facilities 放在同一生態系，並列 Open Rack Wide、power distribution、telemetry／management 與 AI cluster connectivity 等共同責任
limitation: OCP 的生態系範圍不是 Helios 品牌產品資格、供應量、客戶驗收、部署或財務歸因證據
independence_group: open-compute-project
-->

<!-- research_source
source_id: S16
role: other_primary
source_kind: living_index
publisher: NVIDIA
title: Deployment Summary & Validation Checklist
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://docs.nvidia.com/mission-control/docs/rack-bring-up-install/2.0.0/deployment-summary-validation-checklist.html
locator: Factory Rack Inventory File、Firmware Validation、Network Documentation、Configuration Backup & Recovery、Performance and Stress Test、Documentation and Handover 段落；核對托盤／電力架數量、SBOM 目標版本、硬體修訂、設定、全負載熱功率穩定、簽核與交接
limitation: 這是 NVIDIA Mission Control 對 GB200／GB300 機櫃啟用的具體實作清單，不是 Helios 的固定 BOM、資格標準、測試結果、客戶驗收或部署證據
independence_group: nvidia
-->

<!-- research_source
source_id: S17
role: other_primary
source_kind: living_index
publisher: NVIDIA
title: Rack Reboot Sequence
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://docs.nvidia.com/dgx/dgxgb200-user-guide/rack-reboot-sequence.html
locator: Cold Rack Reboot Sequence 的適用情境與 Post-reboot verification；初次安裝、韌體升級、完整機櫃診斷前，以及更換托盤、交換器、trunk 或線纜後，核對服務、連線、fabric state 與 P2P topology
limitation: 這是 NVIDIA DGX GB200 機櫃程序，不是 Helios 必須採用的步驟，也不證明 Helios 品牌系統已重驗、通過、出貨或上線
independence_group: nvidia
-->

<!-- research_source
source_id: S18
role: standard
source_kind: living_index
publisher: DMTF
title: Redfish Schema Index
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://redfish.dmtf.org/redfish/schema_index
locator: TelemetryService 與 UpdateService schema 摘要；前者收集／回報 metric data，後者連結 firmware／software inventory 並提供更新方法
limitation: Redfish 資料模型只支持機器可讀盤點、更新與遙測的能力邊界，不保證感測器校正、量測不確定度、告警門檻、整櫃資格、場站驗收或長期可用率
independence_group: dmtf
-->

<!-- research_source
source_id: S19
role: standard
source_kind: document
publisher: Google / Open Compute Project
title: Google Implementation Open Rack v3 Specification
published_at: 2022-09-23
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/documents/google-implementation-orv3-spec-1-pdf
locator: p.19 Testing；要求機架對文件要求與額外設計功能進行測試、共同制定最壞情境配置、審查測試資料並記錄設計變更
limitation: 這是 Google 的 ORV3 實作要求與較早期機架方法，不是 Helios／ORW 全系統規格、品牌系統資格、液冷與工作負載完整矩陣、客戶驗收或財務證據
independence_group: google-open-compute-project
-->

<!-- research_source
source_id: S20
role: company_release
source_kind: document
publisher: Wiwynn
title: Wiwynn Advances Datacenter Design at COMPUTEX 2026 with High-Power and Optical Interconnect
published_at: 2026-05-26
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.wiwynn.com/zh/news/wiwynn-advances-datacenter-design-at-computex-2026-with-high-power-and-optical-interconnect
locator: AMD Helios Rack-scale Solution 段落；緯穎稱以 OCP ORv3／ORW、MI400、EPYC、Pensando 與 ROCm 展示方案，並自述身為 ODM 夥伴將平台從參考設計推進至量產
limitation: 這是展會前公司自述的整合能力與前瞻量產路徑，沒有品牌型號、固定 BOM／版本、整櫃 qualification、具名客戶、實際出貨數量、收入、毛利或現金流分母
independence_group: wiwynn
-->

<!-- research_source
source_id: S21
role: company_release
source_kind: document
publisher: AIC
title: AIC Showcases Next-Generation AI Infrastructure at COMPUTEX 2026
published_at: 2026-06-01
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.aicipc.com/resources-detail/358/
locator: AMD Helios 段落；AIC 表示負責關鍵機械架構，並邀請參觀者於展位觀看 Helios in action
limitation: 公司頁只支持機構整合角色與展示，沒有品牌 SKU、完整 BOM／版本、資格矩陣、具名客戶、量產出貨、收入、毛利或現金流證據
independence_group: aic
-->

<!-- research_claim
claim_id: C1
label: inference
status: superseded
claim: Helios 已跨過只有參考設計的研究階段，進入具名生產與部署階梯；但 production、2026 下半年 shipment、未具名客戶的 multi-GW deployment 目標、Azure upcoming SKU、OpenAI 第四季 online、Meta validation 與 Anthropic 2027 上半年首個 GW 是七個不同完成度，不能合併成已全面部署
supporting_source_ids: S1,S2,S3,S4,S5
contrary_source_ids:
as_of: 2026-08-02
basis: S4 直接稱 Helios now in production；S1／S2 是同一 Microsoft 合作事件的雙方一手確認，S3 至 S5 是 AMD 主導的其他客戶、平台與生態系文件，合計足以把研究問題從是否存在移到各階段是否兌現，但不構成完全獨立的客戶交叉驗證
boundary: 這是產品與客戶里程碑的階段推論；S5 的 multi-GW 是未分配到具名客戶的廣義前瞻目標，不證明目前容量、每個客戶已驗收、AMD 已認列收入、Helios 取得排他份額或台灣夥伴已有新訂單
verification_needed: AMD 實際出貨公告、Azure SKU 狀態與區域、客戶上線確認及公司財務揭露
correction_kind:
corrects_claim_id:
corrected_by_claim_id: C11
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: AMD 在 2026-07-23 正式將 Helios 描述為 now in production
supporting_source_ids: S4
contrary_source_ids:
as_of: 2026-08-02
basis: S4 新聞稿首段直接使用 now in production 描述 Helios
boundary: 只證實 AMD 做出平台生產階段的正式敘述，不等於客戶已收到、驗收、上線或帶來可辨識收入
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
claim: AMD 表示將於 2026 下半年開始向包括 Microsoft 在內的客戶出貨 Helios；Microsoft 則把 Helios 驅動的 ND MI455X v7 列為 upcoming Azure offering
supporting_source_ids: S1,S2
contrary_source_ids:
as_of: 2026-08-02
basis: S2 直接給出 begin shipping in the second half of 2026，S1 直接把 ND MI455X v7 放在 three upcoming Azure offerings
boundary: 這證實兩家公司當時公布的未來時程與產品定位，不證明已出貨、已 GA、可用區域或利用率
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
claim: AMD 表示 OpenAI 預期自 2026 年第四季開始讓 Helios online；Meta 當時則仍在實驗室測試與驗證 Helios workloads
supporting_source_ids: S4
contrary_source_ids:
as_of: 2026-08-02
basis: S4 的 partner deployment bullets 分別使用 expects to bring Helios online beginning in Q4 2026 與 begun testing and validating workloads
boundary: OpenAI 是未來預期、Meta 是驗證狀態；兩者都不能寫成截至 2026-08-02 已完成大規模部署
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C5
label: verified
status: active
claim: AMD 與 Anthropic 公布最高 2 GW 的 Helios 合作，首個 GW 預計在 2027 年上半年開始部署；AMD 另承諾未來最高 50 億美元股權投資
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-08-02
basis: S3 的 News Highlights、首段與投資段落直接分開揭露部署上限、首批時程及股權投資
boundary: up to 是上限而非已部署容量；股權投資不是 Anthropic 向 AMD 採購設備的金額，也不證明收入認列
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: verified
status: active
claim: AMD 的台灣生態系公告列名 ASE／SPIL／PTI 參與 EFB／2.5D 封裝，Wiwynn／Wistron／Inventec 協助打造 Helios-based systems，AIC 參與 Helios 機架與 compute-tray 機構設計，並列名 Unimicron／Nan Ya PCB／Kinsus 支援載板或先進封裝
supporting_source_ids: S5
contrary_source_ids:
as_of: 2026-08-02
basis: S5 的 EFB、PTI、Helios deployment 段落及四家公司引言直接列出上述公司與合作角色
boundary: 列名只證實合作角色；三家載板公司的文字是廣泛 AMD packaging 支援，不是 Helios-specific，所有列名都不證實新訂單、分配份額、出貨量、ASP、收入、毛利或現金流
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: Microsoft 明確表示 Azure AI 基礎設施同時使用 AMD 等外部創新者與自家 purpose-built silicon and systems
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-08-02
basis: S1 開頭直接描述 Azure 以異質平台同時採用產業夥伴與自研晶片／系統
boundary: 這支持多架構共存的反方路徑，但沒有披露 Helios、自研晶片或其他 GPU 的份額，因此不能判斷誰將取代誰
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: unverified
status: active
claim: 緯穎、緯創、英業達、營邦、日月光／矽品、力成、欣興、南電與景碩已因 Helios 取得可量化新增訂單、收入或獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: S5 只有生態系投資、技術與合作角色，且載板列名不是 Helios-specific；S1 至 S4 也沒有提供台灣公司的訂單及財務資料
boundary: 此主張不得放入正式公司筆記、估值或 H# 終態，也不能用產業總投資或 GW 上限補洞
verification_needed: 各公司一手季報、法說或重大訊息須把具名產品與客戶階段連到出貨、收入、毛利、存貨或營業現金流
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: verified
status: active
claim: AMD 在 2026-05-21 表示 Helios on track for multi-gigawatt deployments beginning 2026 下半年，並稱生態系夥伴支援同期部署
supporting_source_ids: S5
contrary_source_ids:
as_of: 2026-05-21
basis: S5 News Summary 直接使用 multi-gigawatt deployments beginning 2H 2026，正文另稱生態系支援 Helios 在 2026 下半年部署
boundary: 這只證實 AMD 當時提出廣義平台目標；沒有具名客戶容量、已部署證據或台灣公司分配，不能與 Anthropic 2027 上半年首個 GW 合併或視為矛盾
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
claim: AMD 現行常見問答明確把 Helios 定義為參考設計而非 AMD 直接出售的產品，並說該藍圖供 OEM／ODM 打造自己的品牌系統；同頁對夥伴系統的 2026 下半年 volume deployment 仍使用預期語氣
supporting_source_ids: S12
contrary_source_ids:
as_of: 2026-08-12
basis: S12 常見問答直接分開 reference design、not a product for sale、OEM／ODM branded systems 與 expected volume deployments in 2H 2026
boundary: 只證實 AMD 現行定義與前瞻時程；不證明哪一個品牌型號已固定 BOM、通過整櫃資格、出貨、被客戶驗收或形成生產機群
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: inference
status: active
claim: Helios 已從靜態展示與參考平台前進到 AMD 所稱的 production 及夥伴品牌系統化階段，但 AMD 仍把 Helios 定義為參考設計；因此研究必須分開藍圖、OEM／ODM 品牌系統、整櫃資格、實際出貨、客戶生產機群與財務轉換，不能再把 production 寫成已跨過參考設計或視為 AMD 成品已交付
supporting_source_ids: S2,S4,S12,S13,S14
contrary_source_ids:
as_of: 2026-08-12
basis: correction_of:C1; S13 保存 2025 年 static display／reference design 起點，S4 記錄 AMD 2026 年 production 用語，S12 的現行常見問答仍把 Helios 定義為非出售品的參考設計並交由 OEM／ODM 品牌化，S14 則顯示 ORW 標準與製造者文件層本來就分開
boundary: 這是產品交付物與責任邊界的階段推論；不證明任何具名品牌系統已完成、AMD production 用語為假、2026 下半年出貨已發生、客戶機群已運行或台灣公司已有訂單與財務貢獻
verification_needed: 具名 OEM／ODM 品牌型號、固定 BOM／版本、整櫃資格資料、實際出貨與 site acceptance、客戶 production-fleet 及供應商財務文件
correction_kind: supersedes
corrects_claim_id: C1
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: AMD 現行 Helios 頁面把整櫃責任分成 compute tray、switch tray、scale-up／scale-out 網路、power shelf／busbar、cooling manifold／quick disconnect、BMC、ROCm 軟體與 serviceability／lifecycle control
supporting_source_ids: S12
contrary_source_ids:
as_of: 2026-08-12
basis: S12 的系統架構、網路、電力與散熱、軟體與生命週期管理段落逐項描述上述模組和責任
boundary: 這是 AMD 公開的參考設計組成，不是任一 OEM 實際 BOM、OCP 認證、測試結果、客戶驗收、可用率或競品比較
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
claim: 一套可交付的 Helios 品牌系統必須在同一版本邊界內共同驗證運算、機架內外資料移動、電力、液冷、控制軟體與可維修性；任何單一元件或子系統通過，都不能替整櫃資格與場站驗收背書
supporting_source_ids: S12,S13,S14,S15
contrary_source_ids:
as_of: 2026-08-12
basis: S12 與 S13 把八類責任放在同一參考平台，S14 將共同介面與建置角色分層，S15 又把 IT、物理設施、電力、遙測與叢集連線放進同一資料中心生態系；這些一手架構足以支持整合資格問題，但未提供 Helios 完整測試矩陣
boundary: 這是系統工程證據要求，不代表存在單一公開的固定測試標準，也不證明任何品牌系統已通過或每個責任都由同一家公司承擔
verification_needed: 具名品牌系統的配置清單、整櫃 test matrix、pass／fail 原始結果、變更控制、機房介面與客戶 site-acceptance 文件
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C14
label: unverified
status: active
claim: 已有具名 OEM／ODM Helios 品牌系統公開完整 BOM 與版本邊界，並同時提供整櫃資格、現場驗收與生產機群證據
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: S12 至 S15 能建立參考設計、標準與整櫃責任，但本輪沒有捕捉到具名品牌系統把 BOM、整合測試、site acceptance 與 production fleet 串成同一條可核對證據鏈
boundary: 未驗證不等於不存在；只表示截至本輪接受的一手文件，不能把平台頁、標準索引、合作列名或前瞻部署時程改寫成完整交付證據
verification_needed: OEM／ODM 正式產品頁與 datasheet、固定 BOM／韌體／軟體版本、整櫃 qualification report、客戶 site acceptance 及 production-fleet 文件
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C15
label: verified
status: active
claim: NVIDIA 的機櫃啟用清單先以工廠盤點檔核對運算托盤、交換托盤與電力架數量，再把目前與 SBOM 目標韌體、硬體修訂、網路與設定、全負載效能／熱／功率／長時間穩定、簽核及營運交接串成同一份部署紀錄
supporting_source_ids: S16
contrary_source_ids:
as_of: 2026-08-12
basis: S16 的 inventory、firmware、network、configuration、performance／stress、sign-off 與 handover 清單逐項列出上述資料與驗證步驟
boundary: 這是 NVIDIA GB200／GB300 的具體流程範例，不是 Helios 的標準、測試結果、合格門檻或任何台灣公司的交付證據
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C16
label: verified
status: active
claim: NVIDIA 的 DGX GB200 程序要求在初次安裝、韌體升級，以及托盤、交換器、trunk 或線纜維修替換後做冷重啟，並在重啟後核對服務、連線、fabric state 與點對點拓撲
supporting_source_ids: S17
contrary_source_ids:
as_of: 2026-08-12
basis: S17 明列 cold rack reboot 的適用情境與 post-reboot verification 項目
boundary: 只證實 NVIDIA 的變更後重驗程序，不代表 Helios 採用相同步驟，也不證明任何平台已通過回歸測試或生產驗收
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C17
label: verified
status: active
claim: Google 的 ORV3 實作規格要求機架對文件要求與額外設計功能進行測試，測試配置要共同制定以涵蓋最壞情境，並審查測試資料及記錄設計變更
supporting_source_ids: S19
contrary_source_ids:
as_of: 2026-08-12
basis: S19 p.19 Testing 直接列出 requirements coverage、collaborative worst-case configuration、data review 與 documented design changes
boundary: 這是較早期 ORV3 實作的機架測試方法，不是 Helios／ORW 完整資格標準，也不支持任何品牌系統已通過或已量產
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C18
label: verified
status: active
claim: DMTF Redfish schema 把 firmware／software inventory 與更新方法放在 UpdateService，把 metric data 的收集與回報放在 TelemetryService，因此盤點／版本控制與運行觀測是可分開記錄的機器可讀責任
supporting_source_ids: S18
contrary_source_ids:
as_of: 2026-08-12
basis: S18 的 UpdateService 與 TelemetryService schema 摘要直接描述兩類資源
boundary: 資料模型存在不等於感測器已校正、量測可追溯、門檻正確、整櫃已驗收或長期穩定
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
claim: 緯穎在 2026-05-26 官方展會公告展示以 OCP ORv3／ORW、AMD MI400、EPYC、Pensando 與 ROCm 為基礎的 Helios 機架級方案，並自述身為 ODM 夥伴將平台從參考設計推進至量產
supporting_source_ids: S20
contrary_source_ids:
as_of: 2026-05-26
basis: S20 的 AMD Helios Rack-scale Solution 段落直接列出展示組成與 ODM 角色敘述
boundary: 這把緯穎從平台方生態系列名提升為公司自有的具名整合與前瞻量產路徑證據；仍沒有品牌型號、固定 BOM、整櫃資格、具名客戶、已發生出貨或可辨識財務結果
verification_needed: 緯穎正式產品頁／datasheet、版本化 BOM、qualification、客戶或實際出貨文件及季報／法說財務分母
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C20
label: verified
status: active
claim: AIC 在 2026-06-01 官方展會公告表示負責 Helios 的關鍵機械架構，並於 COMPUTEX 展位展示可運作的 Helios 方案
supporting_source_ids: S21
contrary_source_ids:
as_of: 2026-06-01
basis: S21 的 Helios 段落直接描述 AIC 的 mechanical architecture responsibility 與 Helios in action 展示
boundary: 這把營邦從 AMD 單方合作列名提升為公司自有的具名機構整合與展示證據；沒有品牌 SKU、完整 BOM、整櫃資格、客戶驗收、量產出貨或財務分母
verification_needed: AIC 正式產品文件、配置清單、qualification、出貨與季報／法說資料
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C21
label: inference
status: active
claim: 可信的整櫃資格結果需要綁定一套可辨識的配置基準，包括工廠硬體、韌體與軟體、網路設定、電力與冷卻場站輸入、測試條件、簽核與交接；關鍵元件或版本改變後，還要依影響範圍重跑回歸測試，不能只沿用同一平台或型號名稱下的舊結果
supporting_source_ids: S12,S16,S17,S18,S19
contrary_source_ids:
as_of: 2026-08-12
basis: S12 建立 Helios 多子系統與生命週期責任；S16 示範 inventory、SBOM、設定、場站測試與交接紀錄；S17 示範變更後重啟及連線／拓撲重驗；S18 支持盤點、更新與遙測的機器可讀分工；S19 支持最壞情境測試與設計變更紀錄
boundary: 「配置身分證」是本文整理出的研究框架，不是宣稱存在同名強制標準；NVIDIA、DMTF 與 Google／OCP 證據不能替 Helios、OEM／ODM 品牌系統或台灣公司證明資格、出貨、部署、收入或獲利
verification_needed: 具名 Helios 品牌型號的版本化配置清單、change／retest matrix、原始 pass／fail、site acceptance、production handover 與客戶機群資料
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 再把五組公開節點放回自己的時間線

原始文件出現七個動詞、時程與容量數字，但它們來自平台方及四個不同客戶。正確讀法不是
把所有節點排成一條直線，而是先問「這是誰的時間線」，再檢查下一個可驗收結果。

| 本文五條時間線 | 已公開到哪一步 | 時間或上限 | 下一個可驗收節點 | 不能混成 |
| --- | --- | --- | --- | --- |
| 1. AMD 整體平台 | 參考設計由靜態展示前進到 AMD 所稱 production 與夥伴品牌系統化，但仍不是 AMD 直接出售的產品 [S4][S12][S13] | 夥伴系統預計 2026 下半年開始大量部署 | 具名品牌型號、完整配置、整櫃資格、已發生出貨與部署容量 | AMD 已出售單一 Helios 成品、所有客戶都已部署或台灣公司已有分配 |
| 2. Microsoft／Azure | AMD 規劃向 Microsoft 出貨；Azure 預告 ND MI455X v7 [S1][S2] | 出貨規劃在 2026 下半年，雲端規格未給上線日 | 實際出貨、測試開放或正式推出，以及可用區域 | 雲端規格已可使用、已有利用率或收入 |
| 3. OpenAI | AMD 表示客戶預計讓系統上線 [S4] | 預計自 2026 年第四季開始 | 客戶或 AMD 確認實際上線日期與部署範圍 | 截至資料日已上線或已對外商用 |
| 4. Meta | 已開始測試與驗證自己的工作 [S4] | 沒有公開完成日期 | 驗證完成、開始部署或改採其他平台 | 已通過驗證、已有採購量或部署日期 |
| 5. Anthropic | 公布未來合作上限與首批部署規劃 [S3] | 最高 2 GW；首個 GW 預計 2027 上半年開始 | 首批實際部署日期、容量與後續擴張 | 2 GW 已全部啟用或 AMD 已認列收入 |

本文沒有用上述數字做跨公司排名；2 GW、第一個 GW 與最高 50 億美元分別是容量上限、
首批部署節點與股權投資，定義不同，不能相加或互相比較。

## 反方路徑與失效條件

- **不同架構同時存在**：Microsoft 表示 Azure 同時採用外部方案與自研晶片；Helios 成為
  可部署選項，不等於排他標準，也可能只是既有人工智慧支出的份額重新分配。
- **製造與軟體仍可能卡住**：時程、第三方製造、記憶體與載板供應、良率、軟體相容及客戶
  訂單都有不確定性；開始生產仍可能與大規模、可靠部署有距離。
- **參考設計不等於可採購成品**：Helios 藍圖仍要由 OEM／ODM 固定品牌型號、BOM、韌體、
  軟體與冷卻配置；沒有具名品牌系統與整櫃資料包，就不能把 AMD 的 production 用語改寫成
  一套已由 AMD 直接出售、完成資格或交付的成品。
- **客戶節點可能停滯**：如果客戶錯過自己公布的期限，官方撤回測試，或改採其他平台，
  都會削弱「部署持續前進」的推論；單純沒有新公告只代表證據變舊，不直接視為失敗。
- **公司財務不一定轉換**：若台灣公司後續仍只談合作名單，沒有產品、出貨、毛利或現金流
  足跡，就應維持公司映射為待驗證，不能用平台進度替代公司證據。

## 來源與證據邊界

- [Microsoft：Azure 與 AMD 基礎設施擴展](https://blogs.microsoft.com/blog/2026/07/20/microsoft-expands-azure-ai-and-hpc-infrastructure-with-amd/)（S1）。
- [AMD／Microsoft：Helios 2026 下半年出貨規劃](https://ir.amd.com/news-events/press-releases/detail/1291/microsoft-to-deploy-next-gen-amd-instinct-and-amd-epyc-processors-as-the-companies-expand-their-long-term-strategic-partnership)（S2）。
- [AMD／Anthropic：最高 2 GW 與首個 GW 時程](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus)（S3）。
- [AMD AAI 2026：production、OpenAI 與 Meta 階段](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)（S4）。
- [AMD 台灣生態系：封裝與 ODM 合作名單](https://ir.amd.com/news-events/press-releases/detail/1286/amd-announces-more-than-10-billion-in-taiwan-ecosystem-investments-to-accelerate-ai-infrastructure)（S5）。
- [AMD Helios 現行頁：參考設計、品牌系統與整櫃組成](https://www.amd.com/en/products/rackscale-solutions/helios.html)（S12）。
- [AMD OCP 公告：靜態展示、ORW 與服務性](https://newsroom.amd.com/news/amd-showcases-helios-rack-scale-platform-built-o/)（S13）。
- [OCP：Open Rack Specs and Designs](https://www.opencompute.org/wiki/Open_Rack/SpecsAndDesigns)（S14）。
- [OCP：人工智慧資料中心開放生態系](https://www.opencompute.org/blog/delivering-an-open-data-center-ecosystem-for-ai)（S15）。
- [NVIDIA：機櫃啟用、驗證與交接清單](https://docs.nvidia.com/mission-control/docs/rack-bring-up-install/2.0.0/deployment-summary-validation-checklist.html)（S16）。
- [NVIDIA：機櫃變更後的冷重啟與重驗程序](https://docs.nvidia.com/dgx/dgxgb200-user-guide/rack-reboot-sequence.html)（S17）。
- [DMTF：Redfish 盤點、更新與遙測 schema 索引](https://redfish.dmtf.org/redfish/schema_index)（S18）。
- [Google／OCP：ORV3 實作規格的最壞情境測試與變更紀錄](https://www.opencompute.org/documents/google-implementation-orv3-spec-1-pdf)（S19）。
- [緯穎：COMPUTEX 2026 Helios 展示與 ODM 量產路徑自述](https://www.wiwynn.com/zh/news/wiwynn-advances-datacenter-design-at-computex-2026-with-high-power-and-optical-interconnect)（S20）。
- [AIC：COMPUTEX 2026 Helios 機械架構角色與展示](https://www.aicipc.com/resources-detail/358/)（S21）。
- 未來重查使用 [AMD IR](https://ir.amd.com/news-events/press-releases)（S6）、[Azure Updates](https://azure.microsoft.com/en-us/updates/)（S7）、[MOPS](https://mops.twse.com.tw/mops/web/index)（S8），以及 [OpenAI](https://openai.com/news/)（S9）、[Meta](https://about.fb.com/news/)（S10）、[Anthropic](https://www.anthropic.com/news)（S11）官方索引；新附件出現時必須另建 document source。

## 最後用六關把平台進度接回台灣公司

平台前進與公司受惠是兩條不同的證據鏈。參考設計還要先由整機廠固定品牌系統，再從公開
列名逐關確認角色、專屬產品、量產出貨、財務與現金流；中間任何一關缺資料，就停在那一關。

| 本文六關 | 要回答的問題 | 現有資料能確認 | 下一份公司證據 | 不能外推 |
| --- | --- | --- | --- | --- |
| 1. 公開列名 | 公司是否被平台方直接點名 | AMD 列名整機、機構、封裝與載板夥伴 [S5] | 可重查的官方合作文件 | 被列名就有新增訂單 |
| 2. 具體角色 | 公司負責整機、機構、封裝還是載板 | 各家公司角色可分到三個族群 | 公司自己的產品與責任說明 | 同族群所有公司都參與 |
| 3. 平台專屬產品 | 產品是否明確只用在 Helios 或 MI450 系列 | 緯穎與 AIC 公司頁直接連到 Helios 方案／機構角色；尚無可採購品牌 SKU 與固定 BOM [S20][S21] | 具名料號、版本清單、平台資格與雙方可核對文件 | 展示一套方案就是標準化商品或客戶訂單 |
| 4. 驗證與量產出貨 | 具名產品是否通過驗證並持續出貨 | 緯穎自述往量產推進，AIC 展示可運作方案；兩者都沒有完成 qualification、客戶驗收與已發生出貨分母 [S20][S21] | 驗證完成、出貨數量、客戶邊界、產能與交付時程 | 前瞻量產路徑或展會展示等於已出貨、高利用率或獲利 |
| 5. 可辨識財務結果 | 出貨是否落到收入與毛利 | 本輪來源沒有可歸因的公司財務數字 | 季報、法說中的產品收入、毛利或分部資料 | 產業容量上限等於公司營收 |
| 6. 現金流與重複訂單 | 收入是否收得到現金並持續發生 | 本輪來源沒有訂單、存貨或現金流轉換證據 | 應收帳款、存貨、營業現金流與後續訂單 | 一次列名等於長期獲利 |

- **整機與機構**：6669 緯穎已有公司自有文件展示 Helios 方案並描述從參考設計推進量產，
  因此可放到第 3 關與第 4 關入口；3693 營邦已有公司自有文件確認關鍵機械架構與展會展示，
  可放到第 3 關入口。兩者仍缺品牌 SKU、固定版本、完整資格、客戶出貨與財務分母 [S20][S21]。
  3231 緯創與 2356 英業達本輪仍只有 AMD 列名，停在第 2 關 [S5]。
- **封裝測試**：3711 日月光投控所含日月光／矽品與 6239 力成被列名參與高架扇出橋接與
  2.5D 技術合作，目前先停在第 2 關，仍要追具名產品資格與量產。
- **載板**：3037 欣興、8046 南電、3189 景碩被列名支援載板或先進封裝成長，但原文沒有
  寫成 Helios 專屬，也沒有訂單，目前只建立較寬的 AMD 載板追蹤路由。
- 散熱、電源與其他族群在這批來源沒有具名公司；本文不因機架級系統需要相關零組件，就
  自動推成受惠。

<!-- impact
group_id: serverodm
stock_ids: 2356,3231,3693,6669
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-15
rationale: AMD 直接列名 Inventec、Wistron、Wiwynn 與 AIC；緯穎公司頁再提供 Helios 整合與前瞻量產路徑，AIC 公司頁再提供機構角色與展示，值得追版本化產品、資格、已發生出貨與營運資金
evidence_boundary: 生態系列名、展會展示與前瞻量產路徑不等於固定 SKU、整櫃資格、具名客戶、新增訂單、分配份額、收入、毛利或現金流
-->

<!-- impact
group_id: packtest
stock_ids: 3711,6239
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-15
rationale: AMD 直接列名 ASE／SPIL 與 PTI 的 EFB／2.5D 技術開發或資格認證角色，值得追量產與財務轉換
evidence_boundary: 技術合作與資格認證不等於 Helios 專屬訂單、產能利用、收入或獲利
-->

<!-- impact
group_id: pcb
stock_ids: 3037,3189,8046
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-15
rationale: AMD 直接列名 Unimicron、Nan Ya PCB 與 Kinsus 支援載板或 advanced-packaging growth，值得追產品資格、出貨與財務轉換
evidence_boundary: 三家公司列名不是 Helios-specific；廣泛 AMD 載板合作不等於 Helios 新訂單、分配份額、收入、毛利或現金流
-->

## 持續驗證帳本

<!-- monitoring_item
monitor_id: T1
status: retired
retired_at: 2026-08-12
retirement_reason: C1 已由 C11 修正為參考設計、品牌系統、整櫃資格與客戶部署分層；原 shipment／multi-GW／Azure trigger 由 T6 接續，不覆寫 2026-08-09 的 no_new_evidence review
claim_ids: C1,C3,C9
metric: Helios 由 production 進入實際出貨、廣義 multi-GW deployment，以及 Azure ND MI455X v7 的產品狀態與可用區域
source_ids: S1,S2,S4,S5
watch_source_ids: S6,S7
frequency: weekly
next_check: 2026-08-09
trigger: AMD 以新文件確認已開始出貨或 multi-GW deployment 並提供客戶／容量邊界，或 Azure 將 ND MI455X v7 列為 preview／launched 並公布區域
invalidation: AMD 或 Microsoft 官方延後／取消 2026 下半年出貨或部署，Azure 撤回產品；若截至 2026-12-31 仍無實際出貨／部署確認且 Azure 維持 upcoming，也判定原 2H26 時程未兌現
-->

<!-- monitoring_item
monitor_id: T2
status: retired
retired_at: 2026-08-12
retirement_reason: C1 已由 C11 取代；OpenAI 原時程與失效條件不變，由 T7 接續並加入 AMD 現行 Helios 頁的定義邊界
claim_ids: C1,C4
metric: OpenAI 是否在 2026 年第四季把 Helios 接通並投入運行
source_ids: S4
watch_source_ids: S6,S9
frequency: monthly
next_check: 2026-09-01
trigger: OpenAI 自有文件或 AMD 新文件確認 Helios 已 online，並提供投入運行日期或部署範圍
invalidation: OpenAI 或 AMD 官方延後／取消原時程；若截至 2026-12-31 仍無 online 確認，也判定原第四季時程未兌現
-->

<!-- monitoring_item
monitor_id: T3
status: retired
retired_at: 2026-08-12
retirement_reason: C1 已由 C11 取代；Meta validation 原 trigger 由 T8 接續，單純沒有新公告仍不視為失敗
claim_ids: C1,C4
metric: Meta Helios workloads 由 testing／validation 進入通過驗證或實際部署
source_ids: S4
watch_source_ids: S6,S10
frequency: monthly
next_check: 2026-09-01
trigger: Meta 自有文件或 AMD 新文件確認 validation 完成、開始部署，並提供產品或部署範圍
invalidation: Meta 或 AMD 官方表示 Helios validation 失敗、取消、改採其他平台或不再推進；單純沒有新公告只觸發 freshness downgrade，不視為反證
-->

<!-- monitoring_item
monitor_id: T4
status: retired
retired_at: 2026-08-12
retirement_reason: C1 已由 C11 取代；Anthropic 首個 GW 與最高 2 GW 的原時程由 T9 接續
claim_ids: C1,C5
metric: Anthropic 首個 GW 是否在 2027 年上半年開始部署，以及最高 2 GW 是否縮減
source_ids: S3
watch_source_ids: S6,S11
frequency: monthly
next_check: 2026-09-01
trigger: Anthropic 自有文件或 AMD 新文件確認首批部署開始，並提供日期、容量或後續擴張
invalidation: Anthropic 或 AMD 官方延後至 2027 下半年以後、取消或縮減原合作；若截至 2027-06-30 仍未開始首個 GW，也判定原時程未兌現
-->

<!-- monitoring_item
monitor_id: T5
status: active
claim_ids: C6,C8
metric: 台灣 ODM、機構、封裝與載板夥伴的具名產品、出貨、收入、毛利、存貨與營業現金流
source_ids: S5
watch_source_ids: S8
frequency: quarterly
next_check: 2026-08-15
trigger: 台灣公司一手文件把 Helios／MI450 系列、EFB、機構或載板角色連到量產、可辨識收入與獲利或現金流
invalidation: 公司明示合作／資格取消、沒有相關訂單或不再參與，或具名產品的可定位分部資料直接顯示零收入／無重大財務貢獻；只有未見新揭露時維持 C8 待驗證
-->

<!-- monitoring_item
monitor_id: T6
status: active
claim_ids: C3,C9,C11
metric: Helios 夥伴品牌系統是否由 production／前瞻時程進入實際出貨、廣義 multi-GW deployment，以及 Azure ND MI455X v7 的產品狀態與可用區域
source_ids: S1,S2,S4,S5,S12
watch_source_ids: S6,S7,S12
frequency: weekly
next_check: 2026-08-19
trigger: AMD 或具名 OEM／ODM 公開品牌型號並確認已出貨或 multi-GW deployment 的客戶／容量邊界，或 Azure 將 ND MI455X v7 列為 preview／launched 並公布區域
invalidation: AMD、OEM／ODM 或 Microsoft 官方延後／取消 2026 下半年出貨或部署，Azure 撤回產品；若截至 2026-12-31 仍無品牌系統實際出貨／部署確認且 Azure 維持 upcoming，也判定原 2H26 時程未兌現
-->

<!-- monitoring_item
monitor_id: T7
status: active
claim_ids: C4,C11
metric: OpenAI 是否在 2026 年第四季把具名 Helios-based 品牌系統接通並投入運行
source_ids: S4,S12
watch_source_ids: S6,S9,S12
frequency: monthly
next_check: 2026-09-01
trigger: OpenAI 自有文件或 AMD 新文件確認具名 Helios-based 系統已 online，並提供投入運行日期或部署範圍
invalidation: OpenAI 或 AMD 官方延後／取消原時程；若截至 2026-12-31 仍無 online 確認，也判定原第四季時程未兌現
-->

<!-- monitoring_item
monitor_id: T8
status: active
claim_ids: C4,C11
metric: Meta Helios workloads 是否由 testing／validation 進入通過整櫃驗證或實際部署
source_ids: S4,S12
watch_source_ids: S6,S10,S12
frequency: monthly
next_check: 2026-09-01
trigger: Meta 自有文件或 AMD 新文件確認具名品牌系統 validation 完成、開始部署，並提供配置或部署範圍
invalidation: Meta 或 AMD 官方表示 Helios validation 失敗、取消、改採其他平台或不再推進；單純沒有新公告只觸發 freshness downgrade，不視為反證
-->

<!-- monitoring_item
monitor_id: T9
status: active
claim_ids: C5,C11
metric: Anthropic 首個 GW 是否由具名 Helios-based 品牌系統在 2027 年上半年開始部署，以及最高 2 GW 是否縮減
source_ids: S3,S12
watch_source_ids: S6,S11,S12
frequency: monthly
next_check: 2026-09-01
trigger: Anthropic 自有文件或 AMD 新文件確認首批具名系統部署開始，並提供日期、容量或後續擴張
invalidation: Anthropic 或 AMD 官方延後至 2027 下半年以後、取消或縮減原合作；若截至 2027-06-30 仍未開始首個 GW，也判定原時程未兌現
-->

<!-- monitoring_item
monitor_id: T10
status: active
claim_ids: C10,C12,C13,C14
metric: 是否出現具名 OEM／ODM Helios 品牌系統，並公開固定 BOM／版本與運算、網路、電力、液冷、控制軟體、可維修性的整櫃資格及場站驗收證據
source_ids: S12,S13,S14,S15
watch_source_ids: S6,S12,S14
frequency: monthly
next_check: 2026-09-12
trigger: OEM／ODM 正式產品文件公開品牌型號與配置邊界，且平台方、製造商或客戶提供可定位的整櫃 test matrix、qualification、site acceptance 或 production-fleet 結果
invalidation: AMD 或具名 OEM／ODM 明示取消 Helios 品牌系統、撤回相容宣稱或整櫃資格失敗；只有沒有公開完整資料時維持 C14 待驗證
-->

<!-- monitoring_item
monitor_id: T11
status: active
claim_ids: C15,C16,C17,C18,C21
metric: 是否出現具名 Helios 品牌系統的配置身分證與 change／retest matrix，把硬體、韌體軟體、網路、電力冷卻場站、測試條件及簽核交接綁到同一版本
source_ids: S12,S16,S17,S18,S19
watch_source_ids: S6,S12,S16,S17,S18
frequency: monthly
next_check: 2026-09-12
trigger: AMD、OEM／ODM 或客戶公開版本化 hardware／software inventory、場站輸入、測試條件與變更後重驗結果，並能定位到同一 Helios 品牌型號
invalidation: 具名 Helios 品牌系統公開文件明示關鍵配置變更可無條件沿用原資格，或實際 change／retest matrix 與本文六欄框架存在可核對的相反責任邊界；只有沒有公開資料時維持 C21 系統工程推論
-->

<!-- monitoring_item
monitor_id: T12
status: active
claim_ids: C8,C19,C20
metric: 緯穎與 AIC 是否由 Helios 展示／角色／前瞻量產路徑進入品牌 SKU、固定 BOM、整櫃 qualification、已發生出貨與可辨識財務
source_ids: S20,S21
watch_source_ids: S8,S20,S21
frequency: quarterly
next_check: 2026-08-15
trigger: 任一公司正式產品、法說、季報或重大訊息公開 Helios 品牌型號與版本，並提供 qualification、客戶／出貨分母或可定位的收入、毛利與現金流
invalidation: 公司明示取消 Helios 計畫、未取得資格、沒有出貨或沒有財務貢獻；單純展會後未再揭露只維持現有階段並觸發 freshness downgrade
-->

## 下一個可證明／否定的節點

最先到期的是 2026-08-15 的台灣公司財務檢查，其後是 2026-08-19 的品牌系統出貨、
multi-GW 與 Azure 狀態重查，以及 2026-09-12 的整櫃配置身分證、變更重驗與資格資料包檢查。
沒有新文件時，只在
append-only scan log 記錄「未見新證據」，不能刷新主命題的 evidence clock。只有新增且被
active claim 引用的正式文件，才可更新里程碑與可信度；台灣公司映射仍須依各公司一手文件
重做，不能從本篇直接升格為正式公司事實。
