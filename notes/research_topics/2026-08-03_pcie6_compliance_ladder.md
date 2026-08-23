# PCIe 6 元件寫著第六代，不代表整套系統已通過：先分清裝置、連線、正式測試與部署

<!-- research_topic
topic_id: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-03
source_published_at: 2025-05-01
last_reviewed_at: 2026-08-12
review_due: 2026-08-19
source_type: mixed
publisher: PCI-SIG
publisher_domain: pcisig.com
canonical_url: https://pcisig.com/events/pci-sig-compliance-workshop-140
source_chain_id: pcie6-compliance-ladder-20260803
stock_ids:
group_ids: ipdesign,serverodm,pcb
trigger_type: interconnect_compliance_and_deployment_ladder
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C10
base_confidence: medium
confidence_basis: PCI-SIG 的規格、FAQ、Compliance Program、Workshop #140 與 Integrators List 可把 PAM4／FLIT／錯誤控制、四類合規測試、跨廠互通及公開列名分開，Synopsys 技術資料獨立確認設計連動，Astera Labs 與 Micron 則只支持不同元件的量產主張；但正式 64 GT/s listing、完整跨廠矩陣、具名系統部署與台灣公司財務仍未完成
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-03
from: initial
to: inbox
reason: frozen_candidate_selected_after_first_pcie6_official_testing_window
evidence: source_chain:pcie6-compliance-ladder-20260803
-->
<!-- transition
date: 2026-08-03
from: inbox
to: triaged
reason: separated_product_label_vendor_interop_official_testing_listing_and_deployment
evidence: sources:S1,S2,S3,S4,S5
-->

<!-- research_source
source_id: S1
role: standard
source_kind: living_index
publisher: PCI-SIG
title: PCI-SIG Compliance Workshop 140
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://pcisig.com/events/pci-sig-compliance-workshop-140
locator: 2026-08-03 查得 2026-07-27 至 07-31 workshop、PCIe 6.x official testing 最高 64 GT/s，以及 PCIe 5.0／6.x retimer official testing
limitation: 活動頁證明可註冊與執行的測試範圍，不公布每項產品結果，也不代表參加者全部通過或已加入列表
independence_group: pci-sig
-->

<!-- research_source
source_id: S2
role: standard
source_kind: living_index
publisher: PCI-SIG
title: PCI-SIG Integrators List
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://pcisig.com/developers/integrators-list
locator: 2026-08-03 查得 Astera Aries Gen6 PT6161／PT6162 與 Credo Toucan Gen6 等功能名稱，但各列 Spec Revision 仍為 PCIe 5.0 at 32GT/s
limitation: 動態列表只表示列示產品在指定 revision／rate 的 official testing；不能反向推論產品不支援更高速度，也不能證明 64 GT/s 結果尚不存在於其他未公開或待更新流程
independence_group: pci-sig
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: Astera Labs
title: Astera Labs Ramps Production of PCIe 6 Connectivity Portfolio
published_at: 2025-05-01
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://ir.asteralabs.com/news-releases/news-release-details/astera-labs-ramps-production-pcie-6-connectivity-portfolio
locator: 新聞摘要、產品組合與管理層引言；retimer、switch、gearbox、active cable portfolio，完成領先 AI／cloud server 客戶 qualification 並 ramp production
limitation: 公司自述 qualification 與 Cloud-Scale Interop Lab 不等於 PCI-SIG official 64 GT/s pass、Integrators List revision、客戶具名部署或整體生態系成熟
independence_group: astera-labs
-->

<!-- research_source
source_id: S4
role: competitor_primary
source_kind: document
publisher: Micron
title: Micron in High-Volume Production of HBM4 Designed for NVIDIA Vera Rubin PCIe Gen6 SSD and SOCAMM2
published_at: 2026-03-16
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin
locator: News highlights 與 PCIe Gen6 SSD 段落；9650 data center SSD 宣稱 high-volume production，並針對 NVIDIA BlueField-4 STX reference architecture
limitation: Micron 的產品與量產宣稱不提供 PCI-SIG official compliance 結果、客戶部署數、實際利用率或跨供應商 production fleet 分母
independence_group: micron
-->

<!-- research_source
source_id: S5
role: standard
source_kind: living_index
publisher: PCI-SIG
title: PCI Express Base Specification Index
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://pcisig.com/specification-overview/pci-express-base
locator: 2026-08-03 查得 current approved PCIe 7.0 與 previous approved PCIe 6.4、6.3、6.2、6.1、6.0.1 及 6.0 文件日期
limitation: 規格索引只確認版本，不證明 silicon、official testing、Integrators List、平台部署或財務貢獻
independence_group: pci-sig
-->

<!-- research_source
source_id: S6
role: company_release
source_kind: living_index
publisher: Astera Labs
title: Astera Labs News Releases
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://ir.asteralabs.com/news-events/news-releases
locator: 2026-08-03 查得 Aries、Scorpio、gearbox、AEC、客戶 qualification 與量產更新入口
limitation: 公司 IR 索引只供找新附件，不是獨立互通、官方合規或客戶部署證據
independence_group: astera-labs
-->

<!-- research_source
source_id: S7
role: competitor_primary
source_kind: living_index
publisher: Micron
title: Micron News Releases
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://investors.micron.com/news-releases
locator: 2026-08-03 查得 9650 SSD qualification、production、平台與客戶部署後續入口
limitation: IR 索引不能替代產品附件、PCI-SIG 結果或客戶端部署文件
independence_group: micron
-->

<!-- research_source
source_id: S8
role: standard
source_kind: living_index
publisher: PCI-SIG
title: PCI Express 6.0 Specification
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://pcisig.com/pci-express-6.0-specification
locator: 2026-08-12 查得 Specification Features；64.0 GT/s、PAM4、lightweight FEC、CRC、Flit-based encoding、updated packet layout 與 backwards compatibility
limitation: 規格頁定義技術機制與現行 6.4 索引，不證明任何具名產品已通過測試、列入 Integrators List、完成客戶 qualification 或形成出貨與收入
independence_group: pci-sig
-->

<!-- research_source
source_id: S9
role: standard
source_kind: living_index
publisher: PCI-SIG
title: PCI-SIG Compliance Program
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://pcisig.com/developers/compliance-program
locator: 2026-08-12 查得 interoperability 與 compliance tests 的分工、正式 compliant 門檻，以及 Electrical／Configuration／Link Protocol／Transaction Protocol 四類 test areas
limitation: 通用計畫頁只定義測試制度與合格條件；不公布 Workshop #140 個別產品結果，也不代表某件 PCIe 6 產品已完成全部必測項或公開列名
independence_group: pci-sig
-->

<!-- research_source
source_id: S10
role: standard
source_kind: living_index
publisher: PCI-SIG
title: PCI Express 6.0 FAQ
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://pcisig.com/faq?field_category_value%5B%5D=pci_express_6.0&keys=PAM4
locator: 2026-08-12 查得 PAM4 相對 NRZ 的四電位／兩 bit、256-Byte Flit、FEC／CRC 與 Link 保持 Flit Mode 的問答
limitation: FAQ 是規格教育資料，不提供實體 channel、板材、產品測試分布、客戶平台或量產可靠度結果；本文不把規格內誤碼假設外推成任一產品實測
independence_group: pci-sig
-->

<!-- research_source
source_id: S11
role: standard
source_kind: document
publisher: PCI-SIG
title: The Evolution of the PCI Express Specification: On its Sixth Generation Third Decade and Still Going Strong
published_at: 2022-01-11
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://pcisig.com/blog/evolution-pci-express-specification-its-sixth-generation-third-decade-and-still-going-strong
locator: Error Model with PAM4 Signaling、Error Handling with PCIe 6.0 Architecture at 64.0 GT/s 與 Flit Mode 段落；PAM4／burst errors、FEC、CRC、link-level replay 與 fixed-size Flit 的連動
limitation: PCI-SIG 作者的架構分析說明規格取捨，不是跨廠產品 benchmark、量產板卡可靠度、Workshop pass 結果或客戶 production fleet 證據；本文不引用其模擬數值做公司比較
independence_group: pci-sig
-->

<!-- research_source
source_id: S12
role: other_primary
source_kind: living_index
publisher: Synopsys
title: Optimizing PCIe 6.0 Designs at 64GT/s
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.synopsys.com/articles/pcie-6-designs.html
locator: The Channel and PAM-4、FLITS、PHY and Controller Integration 與 Testing and Debug Considerations；四電位訊號、board／package noise、FEC／CRC／retry、Flit mode 與 PHY-controller 整合
limitation: IP 供應商技術文章可獨立交叉確認設計連動，但不是 PCI-SIG official pass、具名客戶 qualification、所有 channel 的共同量測或任何台灣公司 design win 與財務證據
independence_group: synopsys
-->

<!-- research_source
source_id: S13
role: standard
source_kind: living_index
publisher: PCI-SIG
title: PCI-SIG Integrators List - Cadence Gen6 filtered capture
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://pcisig.com/developers/integrators-list?field_il_comp_product_type_value=All&keys=Cadence&order=field_il_spec_rev&sort=asc
locator: 2026-08-12 以官方清單的 Cadence 篩選與 Spec Revision 排序捕捉；多筆產品名稱或 identifier 含 Gen6／64GT/s 的 Cadence controller／PHY IP demo platform 仍列 PCIe 5.0 at 32GT/s，頁面當時的 Filter By 只列 PCI Express 5.0 至 2.0
limitation: 這是指定供應商與捕捉日的公開篩選結果，不是全體產品的不存在證明；也不能推論 64 GT/s 測試失敗、產品能力不足、結果未完成或稍後不會送出 listing form
independence_group: pci-sig
-->

<!-- research_source
source_id: S14
role: standard
source_kind: living_index
publisher: PCI-SIG
title: PCI-SIG Compliance Workshop #140 Invitation and Testing Policy
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://pcisig.com/sites/default/files/2026-05/PCIWorkshop140%20Invitation%20Draft.pdf
locator: 第 1 頁列出 PCIe 6.x System Configuration Space test 與 5.0／6.x Add-In Card／System Lane Margining 的必要性，並界定 CEM connector 後方 redriver／retimer 的 component listing 邊界；第 3 頁列出 one-on-one interoperability、Integrators List 80% 門檻、必要 compliance tests 與 Product Listing Request Form
limitation: 工作坊邀請與政策文件只定義測試角色、邊界及列名程序，不公布任何個別產品結果；頁面未顯示可可靠採用的正式發布日，因此只登錄捕捉日
independence_group: pci-sig
-->

<!-- research_source
source_id: S15
role: standard
source_kind: living_index
publisher: NIST／SEMATECH
title: Constant repair rate (HPP/exponential) model
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.itl.nist.gov/div898/handbook/apr/section4/apr451.htm
locator: §8.4.5.1 的 Confidence Interval Equation and zero fails case；零失效時 MTBF 單側下限為 T／(-ln alpha)，取倒數可得固定事件率單側上限 -ln(alpha)／T
limitation: 這是 HPP／exponential 固定失效率的可靠度方法，不是 PCI-SIG BER 或 compliance 規範；把操作時間 T 改寫成儀器實際計數的 bit／Flit 暴露量 E 是本文的條件式類比，只有事件定義、分母與固定率假設成立時才可使用
independence_group: nist
-->

<!-- research_source
source_id: S16
role: standard
source_kind: document
publisher: PCI-SIG
title: PCI Express 5.0 Compliance Testing
published_at: 2023-01-25
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://pcisig.com/sites/default/files/files/PCI-SIG%20PCIe%205.0%20Compliance%20Webinar_1.25.23_FINAL.pdf
locator: 封面為 January 25 2023 webinar；所下載版本引用頁頁尾為 2023-04-27、PDF metadata creation 為 2023-04-28；投影片 28–29 的接收端 lane margining 在 16.0 GT/s 以上含 retimer 的必要性、L0 狀態、時間／電壓方向、software step、hardware error report，以及 AIC／System 測試角色
limitation: PCIe 5.0 教材定義功能與測試分工，不提供 PCIe 6.0 test ID、共同可追溯的數值及格線、具名 DUT 結果、跨環境重現、field reliability 或公司財務
independence_group: pci-sig
-->

<!-- research_source
source_id: S17
role: other_primary
source_kind: document
publisher: Keysight
title: Keysight P5578CTSA PCIe 6.0 Protocol Compliance Test Application User Guide
published_at: 2026-07-01
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://www.keysight.com/lb/en/assets/9926-01135/user-manuals/Keysight-P5578CTSA-PCIe-6.0-Protocol-Compliance-Test-App-UserGuide.pdf
locator: Edition 1.1 July 2026（published_at 以文件月份首日正規化），pp.108、110–111；AIC 75-20／75-21／75-22 測項、PHY2-7／PHY2-8 capability 說明，以及 retimer 使用 PCI-SIG tool 與 approved system 的程序分界
limitation: 測試工具供應商手冊不是 PCI-SIG 規格或 MOI；PHY2-7／PHY2-8 的 capability／traceability 說明不能外推成 75-22 或全部 64 GT/s 測試都沒有數值門檻，也沒有提供任何具名 DUT 的 pass、量測分布或可靠度
independence_group: keysight
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: PCI-SIG Compliance Workshop #140 於 2026-07-27 至 07-31 舉行，活動頁明列 PCIe 6.x Official Testing 可註冊至 64 GT/s，並包含 PCIe 5.0／6.x Retimer Official Testing
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-08-03
basis: S1 的 registration options 與 Testing Includes 段落直接列出版本、速率及 retimer 類別
boundary: 測試選項存在不等於任何特定產品已通過、已加入 Integrators List、已量產部署或具有財務貢獻
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
claim: 截至 2026-08-03，PCI-SIG Integrators List 可見功能名稱含 Gen6 的 Astera Aries PT6161／PT6162 與 Credo Toucan 等產品，但這些列的 Spec Revision 顯示為 PCIe 5.0 at 32GT/s
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-08-03
basis: S2 同一列表列可直接核對 Product Name、Identifier、Spec Revision、Function 與 Date Added
boundary: 32 GT/s listing 只界定該列正式測試結果，不能推論產品最高能力、64 GT/s 測試失敗、公司誤標 Gen6 或未來不會新增結果
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
claim: Astera Labs 於 2025-05-01 表示其 PCIe 6 portfolio 涵蓋 retimer、fabric switch、gearbox 與 active cable module，並稱方案已完成領先 AI／cloud server 客戶 qualification、正在 ramp production
supporting_source_ids: S3
contrary_source_ids:
as_of: 2025-05-01
basis: S3 的產品清單與管理層引言直接支持公司所揭露的產品範圍與階段
boundary: 客戶未具名，且公司 qualification／interop 不等於 PCI-SIG official 64 GT/s compliance、列表結果、實際 fleet 部署或生態系分母
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
claim: Micron 於 2026-03-16 表示 9650 data center SSD 已進入 PCIe Gen6 high-volume production，並將產品對應 NVIDIA BlueField-4 STX reference architecture
supporting_source_ids: S4
contrary_source_ids:
as_of: 2026-03-16
basis: S4 的 news highlights 與 9650 段落直接列出產品、量產宣稱與 reference architecture
boundary: 量產 endpoint 與 reference architecture 不等於 PCI-SIG official listing、具名客戶 production deployment、利用率或整個 host／switch／retimer 生態系就緒
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
claim: PCIe 6 成熟度不能以一個「Gen6 已量產」標籤表示；至少要分開產品功能名稱、供應商或客戶互通、PCI-SIG official testing、Integrators List 實測 revision，以及具名平台部署，因為截至 2026-08-03 已有量產元件與 64 GT/s 官方測試窗口，但公開列表仍可顯示 Gen6 功能產品只列到 PCIe 5.0 at 32GT/s
supporting_source_ids: S1,S2,S3,S4,S5
contrary_source_ids:
as_of: 2026-08-03
basis: S1／S2／S5 由標準組織界定規格、官方測試與公開列表，S3／S4 兩條獨立公司鏈提供 connectivity 與 endpoint 量產主張；各欄位的成熟度與分母不同
boundary: 不把 32 GT/s listing 解讀為 64 GT/s 失敗，也不把供應商量產宣稱解讀為整體生態系、客戶部署、台灣公司訂單或市場尚未反映
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: unverified
status: active
claim: Workshop #140 已產生可公開核對的 PCIe 6.x 64 GT/s pass 結果、Integrators List 已完成更新，或具名 production platform 已以不同廠商 host、switch、retimer 與 endpoint 完成 fleet deployment
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-03
basis: 活動頁只列測試選項，現行列表捕捉仍顯示部分 Gen6 功能產品在 32 GT/s revision；供應商公告沒有完整公開 host-to-endpoint 測試矩陣與部署分母
boundary: 找不到公開結果不是反證；在新文件前只停在 test available、company-qualified／production 與部分 32 GT/s listing 並存
verification_needed: PCI-SIG 發布 #140 後的 64 GT/s Integrators List 結果，並由至少兩家獨立 host／retimer／endpoint 供應商及具名客戶交叉確認 production deployment
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: unverified
status: active
claim: universe 內高速介面 IC、伺服器 ODM 或 PCB 公司已因 PCIe 6 official compliance 或 production deployment 取得可辨識 design win、訂單、收入或毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-03
basis: PCI-SIG、Astera Labs 與 Micron 文件沒有完成 universe 公司與產品、客戶、qualification、出貨及財務的雙向核對
boundary: PCIe 會員、一般高速介面能力、server platform 或高階 PCB 能力只形成搜尋路由，不構成公司受惠事實
verification_needed: 平台端與台灣公司端同時揭露具名 PCIe 6 產品、64 GT/s 測試／qualification、量產部署及可辨識財務貢獻
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: PCIe 6 的 64 GT/s 不是只把時脈加倍；規格以 PAM4 在一個訊號時間單位承載兩個 bit，並把固定 256-Byte Flit、輕量 FEC、強 CRC 與鏈路重送串成同一套錯誤控制路徑
supporting_source_ids: S8,S10,S11,S12
contrary_source_ids:
as_of: 2026-08-12
basis: S8／S10 直接列出 PAM4、Flit、FEC 與 CRC，S11 說明 burst error、CRC 後重送及固定 Flit 的設計取捨，S12 從獨立 IP 設計角度確認 PAM4→FEC→Flit 與 PHY／controller 連動
boundary: 這只證實規格機制與設計責任，不把規格的誤碼假設、延遲或通道取捨改寫成任何產品實測，也不證明官方 pass、量產良率、客戶部署或公司財務
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: verified
status: active
claim: PCI-SIG 的 Compliance Program 把跨廠 interoperability 與依 test modules 執行的 compliance 分成兩種測試，並把 compliance 再拆成 Electrical、Configuration、Link Protocol 與 Transaction Protocol 四個 test areas
supporting_source_ids: S9
contrary_source_ids:
as_of: 2026-08-12
basis: S9 直接定義兩種 testing、正式 compliant 條件及四類 test areas
boundary: 制度頁的分類和門檻不是 Workshop #140 的個別產品結果；不能由其中一類 pass 推論其他類別、完整跨廠組合、公開列名、客戶 qualification 或 production deployment 已完成
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: inference
status: active
claim: PCIe 6 成熟度應同時用兩條不可互相替代的軸追蹤：連線正確性軸由 PAM4 電氣與通道、Flit／FEC／CRC／重送、設定、鏈路、交易走到跨廠互通；商業落地軸則由產品宣稱、官方測試與列名、客戶 qualification、完整平台部署走到財務歸因
supporting_source_ids: S1,S2,S3,S4,S8,S9,S10,S11,S12,S13
contrary_source_ids:
as_of: 2026-08-12
basis: S8／S10／S11／S12 建立規格與連線錯誤控制鏈，S9 明列四類 compliance 與 interoperability 分工，S1／S2／S13 提供測試入口與不同捕捉日的公開列名，S3／S4 只前進到公司 qualification／元件量產；這些證據位在不同軸、不能壓成單一 Gen6 標籤
boundary: 兩軸是證據整理框架，不是效能、成熟度或投資分數；不宣稱 64 GT/s 列名已出現、整體生態系完成、任何台灣公司取得訂單，亦不判斷市場是否反映
verification_needed: 同一具名 host-to-endpoint 組合公開電氣、設定、鏈路、交易與跨廠結果，並能接到 PCI-SIG 列名、客戶 production fleet、出貨及同期間財務分母
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: unverified
status: active
claim: 至少一套具名 PCIe 6、64 GT/s 產品組合已同時完成必要 Electrical／Configuration／Link Protocol／Transaction Protocol 測試、跨廠互通、Integrators List 列名與具名客戶 production deployment
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: S9 只定義測試制度，S1 只證明 64 GT/s test option，S13 的指定供應商捕捉仍只有 32 GT/s listing；S3／S4 的公司 qualification 與元件量產也沒有完整公開四類 test area、跨廠矩陣及 production fleet
boundary: 未找到完整公開鏈不是失敗或不存在的證據；在具名產品與測項出現前，只能把各段分開標成可測、公司自述 qualification、元件量產或未驗證
verification_needed: PCI-SIG、至少兩家獨立元件供應商與具名客戶三方文件共同列出同一拓撲、產品、revision、64 GT/s、四類 test area、互通結果、listing 與 production fleet
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: Synopsys 的 PCIe 6 技術資料指出，PAM4 的四電位使封裝與電路板的雜訊、串擾與回損控制更關鍵，且 Flit mode 使 PHY、controller、protocol 與測試除錯需要一起規劃
supporting_source_ids: S12
contrary_source_ids:
as_of: 2026-08-12
basis: S12 的 Channel and PAM-4、FLITS、PHY and Controller Integration 與 Testing and Debug Considerations 段落直接連結 board／package channel、PHY、controller 與 protocol testing
boundary: 這是設計責任與失效位置的技術證據，不表示任一 PCB／CCL、IP、ODM 公司已有具名 qualification、份額、ASP、訂單、收入或毛利
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C13
label: verified
status: active
claim: 截至 2026-08-12，PCI-SIG Integrators List 的 Cadence 篩選仍把多筆產品名稱或 identifier 含 Gen6／64GT/s 的 controller／PHY IP demo platform 列在 PCIe 5.0 at 32GT/s，頁面當時的版本篩選也只列 PCI Express 5.0 至 2.0
supporting_source_ids: S13
contrary_source_ids:
as_of: 2026-08-12
basis: S13 的官方篩選頁逐列提供產品、identifier、Spec Revision、lane、function 與 date，並顯示當時可選的世代與 revision 篩選項
boundary: 這是捕捉日的 Cadence 篩選結果，不是全清單不存在 64 GT/s 項目的數學證明，也不表示測試失敗、產品能力不足、結果不存在或 listing form 尚未／不會提交
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C14
label: verified
status: active
claim: Workshop #140 政策把 PCIe 6.x System Configuration Space test 列為 Integrators List eligibility 的必要通過項，並要求 5.0／6.x Add-In Card 與 System 執行 Lane Margining；CEM 測試邊界位在 connector，因此板卡或系統通過不能自動替位於 connector 後方、未另行測試的 redriver／retimer 取得 component listing
supporting_source_ids: S14
contrary_source_ids:
as_of: 2026-08-12
basis: S14 第 1 頁的 mandatory tests、Lane Margining 與 Critical Components 政策直接界定測試角色、必要項及 connector 邊界
boundary: 政策只說明怎樣才有資格列名與哪個物件真正受測，不表示任何具名板卡、系統或元件已通過，也不證明未列名產品失敗
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C15
label: inference
status: active
claim: 每一筆 PCIe 6 合規證據都應綁定受測產品、測試角色、暴露介面與測試邊界、規格版本與速率、必要測項、互通樣本，以及列名申請與公開狀態；板卡或系統結果不能移植給藏在測試邊界後方、未以元件角色另測的訊號元件
supporting_source_ids: S9,S13,S14
contrary_source_ids:
as_of: 2026-08-12
basis: S9 分開 interoperability 與四類 compliance tests，S14 分開 Add-In Card／System／Component 角色與 CEM connector 邊界，S13 顯示公開列項又有產品、功能、revision／rate 與日期欄位；合併後形成可重現的測試物件合約
boundary: 這是證據整理與防止外推的研究框架，不是 PCI-SIG 新增的單一認證名稱，也不對任何產品效能、通過機率、生態系完成度或公司財務評分
verification_needed: 對第一項公開 PCIe 6.x 64 GT/s 列項保存註冊產品、角色、connector 邊界、所有必要測項、互通分母與 form／listing 日期，驗證欄位是否足以重建證據範圍
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C16
label: verified
status: active
claim: PCI-SIG 的正式 compliant 條件要求 interoperability tests 至少達 80% 並通過所有必要 compliance tests；進入 Integrators List 還要送出 Product Listing Request Form，而該表可在工作坊後任何時間提交、沒有截止期限
supporting_source_ids: S9,S14
contrary_source_ids:
as_of: 2026-08-12
basis: S9 的 Compliance Program 直接列出 80% interoperability 與 required compliance test 門檻；S14 第 3 頁列出 Integrators List 三項條件及 listing form 的提交時間規則
boundary: 未在工作坊後立刻列名只能記為公開狀態或流程時間缺口，不能直接解讀為測試失敗；門檻也不替具名產品公布各項結果、客戶驗證或部署
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
claim: NIST／SEMATECH 的 HPP／exponential 固定事件率模型指出，零失效時 MTBF 的單側 100(1-alpha)% 下限為 T／(-ln alpha)；等價地，固定事件率的單側上限為 -ln(alpha)／T
supporting_source_ids: S15
contrary_source_ids:
as_of: 2026-08-14
basis: S15 §8.4.5.1 直接列出 zero fails 的 MTBF lower bound；事件率上限是同一式取倒數的代數等價表達
boundary: 公式依賴固定事件率模型、清楚的失效定義與正確總暴露；它不是 PCIe 6 的 BER 合規門檻，也不能處理未揭露的 burst、跨 lane 共因、計數器漏記或停機暴露
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C18
label: inference
status: active
claim: PCIe 6 的「零錯誤」報告應把受測物件與版本、協商速度與 lane、通道及環境、實際有效暴露與分母單位、counter 層級與重置規則、raw／FEC corrected／CRC residual／replay／application 結果，以及降速、重訓與停機分開保存；否則不同錯誤層級的 0 不能比較
supporting_source_ids: S8,S10,S11,S15
contrary_source_ids:
as_of: 2026-08-14
basis: S8／S10／S11 把 PAM4、FBER、FEC、CRC、Flit 與 replay 分成先後不同的錯誤處理層，S11 並指出 burst 與跨 lane 共因；S15 則要求零事件界線必須有清楚事件定義與總暴露，合併後形成本文的暴露護照
boundary: 暴露護照是研究中心的證據整理框架，不是 PCI-SIG 新增的認證名稱或強制報告格式；本輪沒有任何具名產品的原始 counter、測試分母、通過結果或跨廠比較
verification_needed: 第一份公開具名 PCIe 6 長時間結果同時揭露完整配置、儀器實際分母、各錯誤層 counter、重置／彙總規則、降速／重訓／停機與應用資料正確性
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C19
label: inference
status: active
claim: 在純示範情境中，若儀器實際記錄的有效暴露 E 恰為 10^12 bits、事先定義的錯誤事件為 0，且同質 Poisson／固定率假設成立，alpha=0.05 對應的單側 95% 錯誤率上界為 2.995732273553991×10^-12 errors/bit，而不是 0
supporting_source_ids: S15
contrary_source_ids:
as_of: 2026-08-14
basis: 依 C17 的 lambda_upper=-ln(alpha)／E，以 Python Decimal 50 位精度得 2.9957322735539909934352235761425407756766016229890E-12，獨立 awk log 路徑得 2.995732273553991e-12，兩路一致
boundary: 這是 N=1 個假想暴露量的條件式確定性換算，沒有 sampling SE／t，並非產品樣本、實測 BER、規格 pass、效能比較或投資證據；若錯誤成串、lane 有共因、分母不是儀器實計或 counter 漏記，該上界不適用
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C20
label: verified
status: active
claim: PCI-SIG 的 PCIe 5.0 教材把接收端 lane margining 定義為 16.0 GT/s 以上所有 port（含 retimer）的必要功能；link 在 L0 active 時，由系統軟體逐步移動接收端取樣點，取得時間與電壓方向的 margin，硬體回報錯誤，而且這不是 Recovery.Equalization 的硬體程序
supporting_source_ids: S16
contrary_source_ids:
as_of: 2026-08-23
basis: S16 投影片 28–29 直接列出適用速度與角色、L0 狀態、時間／電壓、software step、hardware error report，以及 AIC／System 三種測試分工
boundary: 這只證實 PCIe 5.0 的功能語意與必要性；不提供 PCIe 6.0 test ID、共同可追溯及格線、具名產品 pass、跨環境重現或量產可靠度
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C21
label: verified
status: active
claim: Keysight 2026 年 7 月指南把 PCIe 6.0 AIC 的 16、32、64 GT/s lane-margining 測項分別列為 75-20、75-21、75-22，且 75-22 只列 FLIT Mode；同一指南在 PHY2-7／PHY2-8 的具名說明中要求檢查 AIC 是否實作能力，並明說該段回報值不對任何 traceable metric 檢查，另把 retimer 程序分開，建議以 PCI-SIG Lane Margining tool 搭配 approved PCIe system 執行
supporting_source_ids: S17
contrary_source_ids:
as_of: 2026-08-23
basis: S17 p.108 的 PCIe 6.0 Table 7 列出 75-20／75-21／75-22 與 supported mode，pp.110–111 分別列 PHY2-7／PHY2-8 及其 capability／traceability 文字，並在下一段另寫 retimer 路徑
boundary: traceable-metric 句只明確指向 PHY2-7／PHY2-8，不能套到 75-22 或全部 64 GT/s 測試；指南使用 should 而非 must，也沒有證明 P5578 本身是 PCI-SIG approved tool／system、任何具名產品已通過，或不同角色與工具的數值可直接比較
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C22
label: inference
status: active
claim: 通道餘裕證據至少要綁定 DUT 角色、實際 port／方向、速度／lane 數、test ID、規格／MOI／工具版本、approved system、取樣擾動方法、原始時間／電壓回報、校正／traceability／acceptance rule、溫度／電壓／unit／lot／lane 分母，以及同時間的 raw error、FEC、replay、retrain、downshift 與應用結果；「功能必測」「有 margin 數字」或「某項 pass」都不能單獨改寫成共同品質分數或 field reliability
supporting_source_ids: S8,S10,S11,S16,S17
contrary_source_ids:
as_of: 2026-08-23
basis: S16 定義量測如何在 L0 由軟體移動 timing／voltage sampling point 並分開 AIC／System，S17 又顯示 test ID、mode、PHY2 capability check、traceability 與 retimer tool／approved-system 路徑會隨測項和角色改變；S8／S10／S11 則分開 raw、FEC、CRC／replay 與 link state，合併後形成可比較證據所需欄位
boundary: 這是研究中心的證據合約，不是 PCI-SIG 或 Keysight 的新認證模板；本輪沒有 64 GT/s 具名 DUT 原始量測、共同門檻、跨 unit／lot／環境分布、qualification、field failure 或公司財務，產品與部署共同觀測 N=0，沒有 sampling SE／t
verification_needed: 第一份具名 64 GT/s 結果把 DUT 角色、port／方向、75-22 或後繼 test ID、規格／MOI／工具、approved system、原始 timing／voltage margin、可追溯校正、預先門檻、unit×lane×環境分母及錯誤／重訓／降速／應用結果共同公開
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: retired
claim_ids: C1,C2,C5,C6
metric: Workshop #140 後 PCIe 6.x 64 GT/s official testing 與 Integrators List 結果
source_ids: S1,S2,S5
watch_source_ids: S1,S2,S5
frequency: weekly
frequency_detail: 每週核對 Workshop、Integrators List 與規格頁；新增 64 GT/s listing 時逐產品保存 revision、lane、function 與日期
next_check: 2026-08-10
trigger: PCI-SIG 公開至少一項 64 GT/s official pass／listing，並可辨認產品類型及測試 revision
invalidation: Workshop 後長期沒有 64 GT/s 公開結果、測試要求重大修正，或產品只能在較低速率穩定互通
retired_at: 2026-08-12
retirement_reason: T1 的 2026-08-12 no_new_evidence 回查已保留在 monitor_reviews；新 S8–S12 顯示 official compliance 本身還要拆成四類測試與跨廠互通，後續由 T3 以兩軸框架逐項追蹤，不覆寫舊檢查結果
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C3,C4,C5,C6,C7
metric: 跨廠 host／switch／retimer／endpoint qualification、具名平台部署與財務足跡
source_ids: S3,S4
watch_source_ids: S6,S7
frequency: monthly
frequency_detail: 每月檢查供應商與客戶文件；只有官方測試、雙向客戶 qualification 及實際部署各自有證據才升級
next_check: 2026-09-15
trigger: 具名客戶公布 production PCIe 6 platform，並列出至少兩家獨立元件、測試條件、部署量或可重現運行結果
invalidation: 客戶 rollout 延後、gearbox 長期只橋接 Gen5、跨廠互通不穩，或 Gen6 元件沒有形成可核對 production fleet
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C1,C2,C5,C9,C10,C11,C13
metric: 具名 PCIe 6、64 GT/s 產品在 Electrical、Configuration、Link Protocol、Transaction Protocol、跨廠互通與 Integrators List 的逐項結果
source_ids: S1,S9,S13
watch_source_ids: S1,S2,S8,S9
frequency: weekly
frequency_detail: 每週核對 PCI-SIG Compliance Program、Workshop、Test Guide 與 Integrators List；逐產品保存功能、revision、rate、lane、四類 test area、interop 組合與 listing 日期
next_check: 2026-08-19
trigger: 至少一件具名 64 GT/s 產品可公開核對必要 compliance test areas 與 Integrators List，或跨廠結果公開足以重建同一拓撲
invalidation: 64 GT/s 測試長期只能完成部分 test area、產品反覆降速、跨廠組合無法重現，或 Test Guide／listing program 重大延後
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C7,C8,C10,C12
metric: 同一具名平台的 PAM4 channel、Flit／錯誤恢復、PHY-controller、板路材料、長時間運行與台灣公司資格／財務橋接
source_ids: S8,S10,S11,S12
watch_source_ids: S6,S7,S8,S9
frequency: monthly
frequency_detail: 每月檢查標準、IP／連接元件商、平台與客戶文件；只有同一產品與期間能跨設計、測試、部署及財務核對才升級
next_check: 2026-09-12
trigger: 具名平台公開 channel／board、PHY／controller、Flit／replay、長時間運行與供應商 qualification，且台灣公司端可雙向核對產品、出貨與財務
invalidation: 平台需長期降速或大量依賴 Gen5 bridge、錯誤恢復影響穩定運行，或台灣公司只有一般高速能力而無具名 qualification
-->

<!-- monitoring_item
monitor_id: T5
status: active
claim_ids: C13,C14,C15,C16
metric: 每件具名產品的受測物件、測試角色、CEM connector 邊界、revision／rate、必要測項、互通分母、listing form 與公開列名時間差
source_ids: S9,S13,S14
watch_source_ids: S1,S2,S9
frequency: weekly
frequency_detail: 每週核對 Integrators List、Compliance Program 與工作坊後續；首項 64 GT/s 列名出現時，逐欄保存產品身分、AIC／System／Component 角色、測試邊界、必要測項、interop 門檻、申請與列名日期
next_check: 2026-08-19
trigger: 首項具名 PCIe 6.x 64 GT/s 公開列名可把受測物件、角色、connector 邊界、所有必要測項與 interoperability 結果連在一起
invalidation: 公開資料只有較低速率、部分測項、模糊物件或板卡／系統結果被錯接到未另測元件；若 form 延後才列名，維持流程時間差而不回寫成測試失敗
-->

<!-- monitoring_item
monitor_id: T6
status: active
claim_ids: C20,C21,C22
metric: 首份具名 64 GT/s lane-margining 結果是否把 DUT 角色、port／方向、75-22 或後繼 test ID、規格／MOI／工具版本、approved system、原始 timing／voltage margin、traceable calibration、預先 acceptance threshold、unit×lane×環境分母及 raw error／FEC／replay／retrain／downshift／application 結果綁在一起
source_ids: S16,S17
watch_source_ids: S1,S2,S9,S14
frequency: monthly
frequency_detail: 每月核對 PCI-SIG workshop／Compliance Program／Integrators List 與測試工具指南；只在同一具名 DUT 的角色、測項、原始 margin、校正、門檻、重現分布及運行結果可共同重建時升級
next_check: 2026-09-23
trigger: PCI-SIG、approved lab 或具名供應商公開可重現的 64 GT/s 結果，且跨 unit／環境重複性與 qualification 或 field outcome 的關聯可核對
invalidation: 新 PCI-SIG 6.x MOI 定義跨角色通用且可追溯的共同品質門檻，並由多 unit／lot／環境的 production 樣本穩定預測故障；若仍只驗 capability／response、角色與工具不可比或沒有 field correlation，維持本文界線
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
reason: editorial_plain_language_wave3_no_conclusion_change
evidence: editorial:plain_language_wave3
-->
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave102_complete_link_test_dimensions_roles_and_six_gate_deployment
evidence: editorial:plain_language_wave102
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: expanded_single_compliance_ladder_into_link_correctness_and_commercialization_axes
evidence: sources:S8,S9,S10,S11,S12
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_test_object_boundary_post_workshop_listing_snapshot_and_listing_lag_contract
evidence: sources:S9,S13,S14
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: zero_observed_error_exposure_counter_layers_and_conditional_upper_bound_added_without_thesis_or_clock_refresh
evidence: sources:S8,S10,S11,S15
-->
<!-- transition
date: 2026-08-23
from: triaged
to: triaged
reason: clarified_lane_margining_functional_check_and_numeric_quality_boundary_without_thesis_or_clock_refresh
evidence: sources:S16,S17
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **完整高速連線**：資料從主機出發，經過電路板、連接器、線材與必要的訊號元件，最後抵達儲存或加速裝置；低階控制軟體也要一起工作。
- **第六代高速周邊連接（PCIe 6／Gen6）**：PCI Express 第六代規格家族，每條通道最高原始傳輸率為 64 GT/s；規格存在不表示任何產品已通過測試。
- **主機端（host）**：發起資料讀寫並管理連線的一端，通常包含處理器、控制器與平台軟體。
- **終端裝置（endpoint）**：連線另一端真正收發資料的裝置，例如固態硬碟、網路介面卡或加速器。
- **固態硬碟（SSD）**：用快閃記憶體儲存資料的終端裝置；硬碟量產不等於主機、訊號元件與軟體已一起通過。
- **運算加速器**：專門加快人工智慧或高效能運算的晶片或裝置；它也可以是高速連線的終端。
- **高速訊號重整器（retimer）**：重新整理衰減或變形的高速電訊號，讓資料能穿過較長板路或線材；它不負責證明整套協定已互通。
- **高速連線交換器（switch）**：讓一個主機端連向多個終端，並把資料送往正確裝置；不是每條連線都需要交換器。
- **速率轉換器（gearbox）**：在兩側速度或介面條件不同時做轉換；用它橋接較舊系統，不等於整條路徑已用最高速度運作。
- **主動式電纜（active electrical cable）**：把訊號處理元件放進電纜組件，協助較長距離的電傳輸；仍要和兩端裝置一起測試。
- **電路板、連接器與線材（PCB／CCL）**：訊號實際穿過的物理路徑；材料與幾何會影響損耗、反射、串擾與可用距離。
- **通道（lane）**：一組可雙向傳輸的基本連線單位；產品常把多條通道合併成 x4、x8 或 x16。
- **每秒傳輸次數（GT/s）**：每秒完成多少十億次訊號傳輸，不等於扣除編碼與協定負擔後的實際資料量。
- **32 與 64 GT/s**：本篇用來區分第五代與第六代每條通道的原始傳輸率；32 的正式結果不能自動替 64 背書。
- **規格版本（specification revision）**：測試所依據的確切規格版本；產品名稱相同，依據版本不同，證明範圍也不同。
- **連線世代**：主機與終端實際協商後運作的規格世代；產品名稱寫第六代，不保證每次連線都跑在第六代。
- **連線拓撲（topology）**：主機、交換器、訊號重整器與終端如何連接；多一層元件就多一組要驗證的組合。
- **韌體（firmware）**：控制裝置啟動、設定與錯誤處理的低階軟體；版本不同可能改變連線結果。
- **驅動程式（driver）**：讓作業系統識別並操作硬體的軟體；硬體可連線不表示驅動與工作負載已穩定。
- **連線訓練（link training）**：兩端啟動時協商速度、通道與訊號參數的程序；最高速度失敗時，系統可能退回較低速度。
- **訊號完整性**：電訊號穿過板路與線材後仍能被正確辨識的程度；瞬間連得上不等於長時間或不同環境都穩定。
- **相容性**：產品依共同規則完成指定功能；必須寫清楚版本、速率、通道與測試範圍。
- **跨廠互通（vendor interoperability）**：不同公司的主機、訊號元件、交換器與終端，在同一組條件下能一起工作並重現結果。
- **符合規格（compliance）**：一件產品依共同程序通過指定版本、速率與功能的測試；單件合格不等於所有廠商組合都互通。
- **周邊元件互連標準組織（PCI-SIG）**：維護 PCI Express 規格、相容性活動與公開合格清單的產業組織。
- **相容性計畫與工作坊（Compliance Program／Compliance Workshop）**：標準組織用計畫定義測試制度，再由工作坊讓會員執行正式測試與交叉連接；提供某項測試不表示參加產品都通過。
- **官方測試（Official Testing）**：依標準組織指定程序執行的正式測試；還要看到具名產品與結果，才能說誰通過。
- **合格產品清單（Integrators List）**：公開記錄產品在指定規格版本與速率下結果的列表；每一列只支持自己寫出的條件。
- **客戶驗證（qualification）**：客戶用自己的平台、韌體與工作負載確認產品可用；它可能早於或晚於公開的官方結果。
- **參考架構（reference architecture）**：展示元件可以如何組成系統的設計範例；被放進參考架構不等於客戶已部署。
- **元件量產（production）**：供應商能穩定製造並出貨某一產品；它沒有回答整套平台是否通過或實際使用多少。
- **客戶正式部署（production fleet）**：具名客戶把完整平台放進生產環境持續運作，並能交代組合、規模、期間與結果。
- **第五代高速連線（PCIe 5／Gen5）**：前一代 PCI Express 規格，每條通道原始傳輸率為 32 GT/s；第六代裝置仍可能和它向下相容或降速連線。
- **兩電位訊號（NRZ）**：用高、低兩個電位表示資料的傳輸方式；前五代 PCIe 在最高速度使用這種訊號。
- **四電位訊號（PAM4）**：用四個電位、在同一訊號時間單位承載兩個 bit；資料率提高，但接收端更難分辨相鄰電位。
- **實體層（PHY）**：負責把數位資料轉成電訊號、送過封裝、板路與連接器，再由接收端還原的硬體層。
- **固定資料單元（Flit）**：第六代把資料整理成固定 256 Byte 單元，讓錯誤修正、偵測與重送有共同處理範圍。
- **前向錯誤修正（FEC）**：接收端利用附加資訊先修正一定範圍內的錯誤；修不了的錯誤仍要交給後續偵測與重送。
- **循環冗餘檢查（CRC）**：用檢查碼判斷資料經修正後是否仍有錯；它負責偵測，並不自行把所有錯誤修好。
- **否定回覆與鏈路重送（NAK／replay）**：接收端發現資料仍有錯時要求發送端重送；成功恢復不等於錯誤從未發生。
- **位元錯誤率／首個位元錯誤率（BER／FBER）**：描述接收端出現錯誤的頻率或第一個錯誤事件的機率；規格假設不等於每件產品實測。
- **原始錯誤層**：錯誤修正前，由接收端或儀器看到的 bit、symbol 或 FBER 事件；它和修正後交給上層的資料結果不是同一個 counter。
- **錯誤修正層**：FEC 已偵測並成功修正的 symbol、group 或 Flit；這個數字大於零時，上層仍可能完全看不到錯誤。
- **殘留錯誤層**：經 FEC 後仍由 CRC 找到的錯誤資料單元；它可能觸發 NAK 與 replay，不能和原始錯誤直接相加。
- **應用失敗層**：交易逾時、資料不一致、輸入輸出錯誤或工作中斷等使用者真的感受到的結果；數字為零不表示底層沒有修正或重送。
- **有效暴露量（valid exposure）**：受測連線在指定速度、lane、方向與狀態下，儀器真正計數的 bits、symbols、Flits、transactions 或時間；不能只用銘牌速度乘牆鐘時間替代。
- **零事件單側上界**：在事件定義、分母與固定事件率假設都成立時，用零次觀察算出的「真實事件率仍可能有多高」；它不是零風險或零 BER。
- **同質卜瓦松過程（HPP）**：假設事件以固定平均率、在不重疊暴露區間彼此獨立發生的模型；錯誤成串或共因存在時，這個假設可能失效。
- **平均失效間隔（MTBF）**：固定失效率模型下，兩次失效之間的平均操作時間；本篇只借用其零事件界線方法，不把 bit 暴露說成設備壽命。
- **設定空間測試（Configuration Testing）**：檢查裝置設定欄位、能力宣告與存取行為是否符合規則。
- **鏈路協定測試（Link Protocol Testing）**：檢查裝置在連線建立、狀態轉換、錯誤回報與鏈路層行為上是否符合規則。
- **交易協定測試（Transaction Protocol Testing）**：檢查讀寫請求、回覆、排序與交易層封包等上層行為是否符合規則。
- **受測物件（tested object／DUT）**：這張成績單真正掛在哪一件產品上；同名產品家族、整張卡與卡上的單一元件不是同一個受測物件。
- **測試邊界（test boundary）**：儀器或另一台裝置實際看得到、能施加條件並判斷結果的介面範圍；邊界後方的零件不能自動沿用結果。
- **擴充卡機電連接器（CEM connector）**：擴充卡與系統板相接的共同電氣與機構介面；工作坊政策以它界定板卡／系統測試和內部關鍵元件的證據範圍。
- **擴充卡（Add-In Card／AIC）**：插入系統插槽、承載終端或其他功能的完整板卡；它可以是一個受測角色，但不等於板上每顆元件都被單獨測過。
- **通道餘裕量測（lane margining）**：由系統讀取接收端可用電壓與時間餘裕的標準化檢查；必要性不等於結果已通過或長期工作負載穩定。
- **功能檢查與品質門檻**：功能檢查回答裝置會不會依程序回報，品質門檻還要用可追溯校正、共同條件與預先及格線判斷數字好不好；會顯示數字不等於已有共同健康分數。
- **連線正常工作狀態（L0／L0 active）**：連線已完成訓練、可以正常傳送資料的狀態；在這個狀態量餘裕，不等於故意進入重新等化或故障恢復程序。
- **測試程序文件（MOI）**：把規格要求轉成儀器接法、操作步驟與判定方式的實作方法；版本不同時，結果可能不能直接比較。
- **PHY2-7／PHY2-8 測項**：Keysight 指南逐名提到的 16／32 GT/s lane-margining 測試編號；它們不是 64 GT/s 的 75-22，也不能互相替代證據。
- **統計標準誤（SE）**：描述樣本估計值因抽樣而可能波動多少；本輪沒有產品樣本分布，因此不能計算這個誤差。
- **產品列名申請表（Product Listing Request Form）**：完成門檻後仍要提交的公開列名程序文件；可在工作坊後另行送出，因此列名時間不必等於測試日期。
- **系統測試角色（System）**：以主機板、插槽與必要平台元件組成的系統身分受測；系統結果只涵蓋當次配置與測試邊界。
- **Credo**：公開清單中的一家高速連接元件供應商；本文只引用其具名產品列的規格版本與速度，不比較公司能力或投資價值。

### 三句話抓重點

- 一條完整高速連線，要讓主機、板路與線材、必要的訊號或交換元件、終端裝置，以及低階控制軟體一起工作。
- 產品名稱寫著「第六代」、實際連線跑到哪一代、通過哪一項正式測試，以及是否進入客戶系統，是四件不同的事。
- 截至本輪，公開清單仍未出現最高速度列項；而且整張卡或系統板通過，也不能自動替藏在連接器後面的訊號元件背書。

### 為什麼重要

**第六代先改變信號的語言。** 它不是單純把電訊號切換得更快，而是改用四個電位，在同一個
訊號時間單位承載更多資料。這讓接收端更難分辨相鄰電位，也把封裝、板路、連接器、雜訊與
串擾重新拉進同一個問題。

**錯誤處理也跟著改。** 資料要先放進固定大小的單元，由前向錯誤修正處理可修正錯誤，再用
檢查碼找出仍有問題的資料，必要時要求重送。只測眼圖或只看裝置能連上，都沒有證明設定、
鏈路狀態、讀寫交易與長時間工作負載已正確。

**通過測試仍是多張成績單。** PCI-SIG 把電氣、設定、鏈路協定、交易協定與跨廠互通分開；
產品名稱、公司客戶驗證、正式測試、公開列名、元件量產與客戶部署也各有自己的證據。把這些
欄位分開，才能避免一則供應商公告讓整台伺服器或所有台灣供應鏈角色同時被誤判為已受惠。

### 接下來怎麼追

- 每一筆測試至少保存產品、功能、規格版本、速度、通道數、連接方式、軟體版本、電氣／設定／鏈路／交易測項與結果日期。
- 看見「零錯誤」時，先問分母是 bits、Flits、transactions 還是時間，再問它指 raw、FEC corrected、CRC residual、replay 或 application 哪一層。
- 分開記錄「測試可以報名」、「具名產品通過」與「結果進入公開清單」，不要用活動頁替產品背書。
- 跨廠結果要列出主機、訊號元件、交換器、終端與韌體來自誰，並確認目標速度、錯誤恢復與長時間讀寫能否重現。
- 量產消息要再分元件出貨、參考架構、客戶驗證與完整平台部署；台灣公司還要補客戶端與公司端的雙向財務證據。

### 想一想

- 一個產品名稱寫著「第六代」，公開清單卻只記錄較低速度，這筆資料證明了什麼，又沒有證明什麼？
- 主機、訊號元件與儲存裝置各自量產，還要補哪些共同測試，才能說整條連線穩定？
- 公司客戶驗證先完成、正式測試較晚公布時，研究者該如何分開記錄？
- 如果整張擴充卡通過，卡上的每一顆訊號元件是否都能沿用同一張成績單？
- 兩份報告都寫「跑了很久、零錯誤」，若一份沒有暴露分母、另一份只報應用層錯誤，它們能比較嗎？

## 先看 64 GT/s 為什麼牽動整條連線

第六代的幾個新名詞不是互不相干的功能清單，而是一條前一個選擇會改變下一個責任的工程鏈：

| 本文五個連動步驟 | 為什麼需要它 | 它把問題交給誰 | 要驗收什麼 | 不能直接推成 |
|---|---|---|---|---|
| 1. 以 PAM4 承載更多資料 | 四個電位可在同一訊號時間單位表示兩個 bit，達到每通道 64 GT/s | 發送端、接收端、封裝、板路、連接器與線材 | 電位是否可分辨、雜訊、抖動、串擾、回損與不同通道條件 | 規格定義 64 GT/s，不等於任何產品或板路已在該速度通過 |
| 2. 接受更敏感的原始錯誤環境 | 四個電位的判讀空間更小，錯誤還可能成群出現 | 實體層、均衡器、時鐘資料恢復與通道設計 | 位元錯誤、錯誤聚集、不同溫度／距離與降速行為 | 規格的錯誤模型不是某一產品實測，也不能比較公司高低 |
| 3. 把資料整理成固定 Flit | 錯誤修正需要固定大小的處理單元 | 控制器、鏈路層與封包格式 | 兩端是否進入相同模式、資料排列、狀態轉換與降速後行為 | Flit mode 能建立，不等於讀寫交易或應用已正確 |
| 4. 依序修正、偵測與重送 | FEC 先修可修正錯誤，CRC 找出殘留錯誤，鏈路再重送 | 接收端錯誤控制、回覆與 replay 邏輯 | 修正範圍、殘留錯誤、重送、資料正確性與長時間穩定度 | 有 FEC 不等於沒有錯誤；成功重送也不等於通道品質相同 |
| 5. 再驗設定、協定與工作負載 | 電氣連得上之後，裝置仍要正確宣告能力、轉換狀態並完成讀寫 | 設定空間、鏈路協定、交易協定、韌體、驅動與應用 | 設定、狀態機、請求／回覆、錯誤注入、壓力與恢復 | 單一眼圖、單一封包或一次開機不能替完整平台背書 |

這五步是診斷順序，不是固定由左到右發生的單一故障，也不是供應商排名。實際系統可能在
板路、接收端、韌體或交易層同時出現問題；只有把具名產品、版本、拓撲與測試結果放回每一步，
才能知道哪一層真的跨過門檻。

## 先用五個位置看一條高速連線怎麼接起來

| 本文五個位置 | 它做什麼 | 代表裝置或軟體 | 下一個要驗收 | 不能直接推成 |
|---|---|---|---|---|
| 1. 主機與連線控制 | 發起資料讀寫，決定連線世代、通道數與錯誤處理 | 處理器、主機控制器、韌體、驅動程式與作業系統 | 能否和具名終端完成訓練、長時間傳輸、降速與恢復 | 主機寫著支援第六代，不等於任何終端都能跑到最高速度 |
| 2. 板路、連接器與線材 | 把電訊號從一個裝置帶到下一個裝置 | 電路板走線、連接器、被動線材與主動式電纜 | 損耗、反射、串擾、距離、溫度、振動與插拔後穩定度 | 材料或線材規格合格，不等於整條協定連線已通過 |
| 3. 訊號修復或速率轉換 | 在訊號衰減或兩側條件不同時重新整理、延伸或轉換 | 高速訊號重整器、速率轉換器與主動電纜內晶片 | 每個埠的目標速度、通道、韌體、錯誤回報與兩側裝置組合 | 一顆訊號元件量產，不等於主機到終端的完整路徑已互通 |
| 4. 連線交換與分支 | 讓主機連到多個終端，並管理每個方向的資料流 | 高速連線交換器、管理韌體與交換器驅動 | 多裝置同時負載、路由、重置、熱插拔、故障隔離與恢復 | 一台交換器支援第六代，不等於所有分支都用最高速度運作 |
| 5. 終端與實際工作 | 收發資料並完成儲存、網路或運算任務 | 固態硬碟、網路介面卡、加速器、終端韌體與工作負載 | 資料正確、壓力、斷線重連、長時間運轉與應用層結果 | 一個終端大量生產，不等於完整平台已被客戶部署 |

不是每套系統都需要第三與第四個位置，實際順序也可能隨拓撲改變。這五個位置只是把新聞中的
零件放回完整連線，並不是固定接線圖或完整協定堆疊；任何位置缺少具名裝置、版本與結果，
都不能由其他位置代替畢業。

## 再用五把尺讀懂一筆測試到底證明什麼

| 本文五把尺 | 每筆結果要記錄 | 本輪可看到的例子 | 下一份證據 | 不能直接推成 |
|---|---|---|---|---|
| 1. 規格版本與連線世代 | 測試依據哪一版規格，兩端實際協商到哪一代 | 公開清單可把帶有第六代功能名稱的產品列在第五代規格 | 同一具名產品依第六代規格完成測試的結果 | 產品名稱、設計目標或最高能力不等於該列實測世代 |
| 2. 每條通道的傳輸率 | 是 32 或 64 GT/s，是否有降速，以及結果持續多久 | 工作坊提供 64 GT/s 測試入口；部分現行列表列到 32 GT/s | 具名產品在 64 GT/s 的通過結果、條件與日期 | 32 GT/s 列項不表示 64 GT/s 失敗，也不表示 64 已通過 |
| 3. 通道數與連線拓撲 | x4、x8 或 x16，是否經過交換器、訊號重整器、線材與幾層分支 | 本輪來源能指出產品功能與部分列表欄位，沒有公開完整最高速拓撲矩陣 | 主機到終端的接線圖、通道、距離、分支與每段結果 | 單一短距離或少通道通過，不等於所有拓撲都穩定 |
| 4. 產品、韌體與軟體組合 | 每一端的產品型號、硬體修訂、韌體、驅動與作業系統版本 | 供應商揭露連接產品與儲存終端，但沒有同一路徑的完整版本表 | 可重現的產品清單、版本、設定、測項與測試檔 | 同一家產品家族可用，不等於不同版本或不同廠商都相容 |
| 5. 測試主體與結果狀態 | 是供應商自測、客戶驗證、正式測試，還是已進公開清單 | 公司客戶驗證、工作坊測試入口與公開列表三種證據同時存在 | 由具名產品把測試報告、公開列項與客戶端結果串起來 | 一種測試不能替另一種背書；活動存在更不等於產品通過 |

五把尺共同決定一筆結果能證明多大範圍。若新聞只寫「第六代互通」，卻沒有版本、速度、
通道、拓撲、軟體與測試主體，研究中心只能把它記成待查線索，不能替讀者補出完整測試。

## 先認清「誰真的被測到」

同一件硬體可以用擴充卡、系統或元件等不同角色報名；成績單能證明的範圍，取決於測試儀器
實際看到哪個介面。研究者應先寫完以下五個欄位，再讀「通過」二字：

| 測試物件合約的五個欄位 | 要回答的問題 | 第 140 次工作坊政策給的線索 | 常見誤讀 | 下一份證據 |
|---|---|---|---|---|
| 1. 註冊產品身分 | 成績單掛在哪個型號、硬體修訂與功能上 | 報名與列名都以具名產品為單位 | 把同一家族或下一版產品視為同一物件 | 產品名稱、識別碼、硬體修訂與結果日期 |
| 2. 測試角色 | 它以擴充卡、系統、元件或其他角色受測 | 交換器／橋接器與訊號重整器須按政策用指定角色註冊 | 整張卡通過就說板上每顆元件都通過 | 每個角色各自的註冊、必測項與結果 |
| 3. 暴露介面與邊界 | 儀器實際在何處注入、讀取並判斷結果 | 板卡與系統的電氣測試以 CEM connector 為邊界 | 把連接器後方的內部元件當成已單獨受測 | 接線圖、連接器位置、內部訊號元件與測試點 |
| 4. 必要測項與互通門檻 | 哪些電氣、設定、鏈路、交易與跨廠項目必須完成 | 第六代系統設定測試與通道餘裕量測有明列必要性；正式合格另有互通及必測門檻 | 一個眼圖、一次開機或一類測試替全部背書 | 每個必要模組的版本、速率、結果與互通分母 |
| 5. 申請、列名與日期 | 何時測試、何時送表、何時出現在公開清單 | 完成門檻後仍要送列名申請表，且工作坊後沒有送件截止日 | 工作坊結束後沒立刻列名就判定失敗 | 測試日、送表日、接受日與公開列名日 |

這個邊界尤其重要：若訊號重整器藏在連接器後方，板卡或系統可能以完整組件通過，但那顆
元件並沒有因此取得自己的完整電氣與功能成績。反過來，工作坊結束後暫未出現在公開清單，
也只表示公開列名鏈尚未閉合；申請表可稍後提交，所以不能把「未列名」直接翻譯成「測試失敗」。
這些界線由 PCI-SIG 的 Compliance Program、公開清單與工作坊政策共同支持。[S9][S2][S14]

## 通道餘裕有數字，不等於有共同及格線

把 lane margining 想成量體溫：溫度計的數字會跟著冷熱改變，先證明感測與回報功能在工作；
要再判斷是否發燒，還要有校正過的量尺、共同量測位置、預先定義的界線，以及它和實際健康
結果的關聯。通道餘裕也是如此，**會回報數字**、**數字怎麼產生**、**數字能否預測品質**是
三層不同證據。

PCI-SIG 的官方教材把接收端 lane margining 定義得很具體：支援 16.0 GT/s 以上的 port（包括
retimer）要有這項功能；link 在 L0 active 時，系統軟體逐步移動接收端的時間與電壓取樣位置，
硬體回報錯誤。它不是連線進入 Recovery.Equalization 後由硬體自行重新等化的同一件事；教材
也把 AIC 與 System 的執行方式分開。[S16]

Keysight 2026 年 7 月指南則顯示，讀數必須和測項一起讀。PCIe 6.0 AIC 的 16、32、64 GT/s
測項分別列為 `75-20`、`75-21`、`75-22`，其中 `75-22` 只列 FLIT 模式；但指南所說
「回報值不對 traceable metric 檢查」的段落，只明確點名 `PHY2-7`／`PHY2-8`。同一頁還把
retimer 的程序另行分開，寫成應以 PCI-SIG Lane Margining tool 搭配 approved PCIe system
執行。[S17] 因此不能把 `PHY2-7`／`PHY2-8` 的限制搬到 `75-22`，也不能由一張 pass 成績單
推論不同角色、工具與 port 的 margin 數字已有共同及格線。

| 三層判讀 | 最少要保存什麼 | 這一層能證明 | 還不能越過的界線 |
|---|---|---|---|
| 1. 功能有實作 | DUT 角色、實際 port／方向、link state、速度／lane、test ID 與回報是否依程序改變 | 受測物件在該角色與程序下能執行 margining | 數值準確、不同工具可比、64 GT/s 全測項通過或長期可靠 |
| 2. 數字如何產生 | 規格／MOI／工具版本、approved system、取樣擾動、原始 timing／voltage 回報、校正與 traceability | 在同一合約內重建這個數字的來源 | 把不同 receiver 演算法、角色、方向或環境的數字排成共同品質榜 |
| 3. 數字是否預測品質 | 預先 acceptance rule、unit／lot／lane／溫度／電壓分母，以及同時段 raw error、FEC、replay、retrain、downshift、應用與 field outcome | 驗證門檻能否跨樣本重現並預測 qualification 或實際故障 | 用一次功能 pass、單 lane 讀值或最好樣本宣稱量產可靠度與公司受惠 |

這張表是研究中心的證據合約，不是 PCI-SIG 或 Keysight 新增的認證。這一輪只有 **N=2 份
官方文件、N=2 個發布者**，而且都在同一相容性測試生態裡；它們不是兩個產品重複實驗。
具名 64 GT/s DUT 原始結果、跨 unit／lot／環境分布、qualification、field deployment 與台灣
公司財務的共同觀測全部 **N=0**，沒有 sampling SE／t；三個 test ID 也不能算成三個獨立樣本。

| 多空敘事 | 合理假說 | 必須再看到 | 最強反方 |
|---|---|---|---|
| 偏多：量測與除錯內容增加 | 更細的 timing／voltage 診斷可能增加驗證工具、工程時數，並協助定位板路、receiver 或 retimer 問題 | 具名平台的測試時間、工具／BOM、qualification、出貨、價格與財務共同鍵 | 若主要只是既有硬體的軟體 capability／設定檢查，測項增加不等於新增元件或供應商收入 |
| 偏空：數字是 receiver 自己回報 | 演算法、port、方向、角色與工具不同時，margin 值可能只適合本機除錯，不能形成跨產品健康分數 | 可追溯校正、共同門檻、跨 unit／環境重現，以及與 field failure 的關聯 | 若新 MOI 定義跨角色共同門檻，且量產樣本穩定預測故障，這個不可比界線就要下修 |
| 共同底線 | 功能、量測值、品質預測與商業受惠各有自己的分母 | 同一具名 DUT 的完整證據合約，再接到部署與財務 | 用 mandatory、pass 或一個 margin 數字一次跨過後面三層 |

## 跑了很久沒錯，不等於 BER=0：先固定暴露量與錯誤層級

一份報告若只寫「連續運行、零錯誤」，讀者還不知道它到底觀察了什麼。PCIe 6 的同一筆資料
可能先在接收端出現原始錯誤，由 FEC 修正；修正後仍有問題才由 CRC 找出，再觸發 NAK／replay；
重送成功後，應用程式仍可能得到完全正確的資料。因此，同一次測試完全可能同時出現
「raw error 大於零、FEC correction 大於零、CRC residual 為零、replay 為零、application failure
為零」。這些數字沒有矛盾，只是在看不同層。[S8][S10][S11]

### 先把六層 counter 分開

| 錯誤與運行層 | 典型事件 | 合理分母 | 這一層為 0 能說什麼 | 仍不能說什麼 |
|---|---|---|---|---|
| 1. 接收端原始層 | bit／symbol error 或 FBER event | 實際接收 bits、symbols 或明確 FBER opportunity | 在已揭露的事件定義與暴露內沒有記到該事件 | FEC 沒有工作、其他 lane 沒有共因，或真實 BER 等於零 |
| 2. FEC 修正層 | corrected symbol、FEC group 或 Flit | 實際解碼 groups／Flits | 沒有被該 counter 記錄的成功修正 | 修正前沒有錯、counter 沒漏記，或 CRC／replay 也為零 |
| 3. CRC 殘留層 | post-FEC CRC error | 實際檢查 Flits | 沒有 CRC 偵測到的修正後殘留錯誤 | 原始通道零錯誤，或 CRC 絕不會 alias |
| 4. 鏈路恢復層 | NAK、replay、replay timeout | 實際傳送 Flits／transactions | 沒有符合定義的重送事件 | FEC 沒修過錯、鏈路從未重訓，或延遲完全不受影響 |
| 5. 連線狀態層 | retrain、lane／speed downshift、link down | active time、state transitions 與 downtime | 指定狀態事件未被記到 | 全部牆鐘時間都在目標速度，或停機期間也算入有效暴露 |
| 6. 交易與應用層 | I/O error、timeout、資料不一致、工作失敗 | completed transactions、bytes 或 jobs | 使用者結果在該工作負載內沒有出錯 | PHY 零錯誤、沒有修正／重送，或另一種工作負載同樣穩定 |

這張表不是 PCI-SIG 新增的測試分類，而是把既有錯誤處理順序轉成閱讀用 counter 階梯。
同一層還要保存 counter 寬度、清零時間、overflow、輪詢間隔、每 lane／每 device 彙總規則；
否則兩個同名 counter 也可能因重置與加總方法不同而不可比。

### 再寫一張八欄暴露護照

| 暴露護照欄位 | 至少要保存什麼 | 為什麼不能省略 |
|---|---|---|
| 1. 受測物件與版本 | host、switch／retimer、endpoint、board、硬體修訂、韌體、driver 與測試邊界 | 換一個版本或把板卡結果移植給內部元件，證據範圍就變了 |
| 2. 協商後連線狀態 | 規格 revision、實際 GT/s、lane width、方向與是否進入 Flit Mode | 銘牌最高速度不等於整段測試都在該速度與 lane 數運作 |
| 3. 通道與環境 | 拓撲、距離、材料、連接器、loss、供電、溫度與干擾條件 | PAM4 錯誤會受通道與共因雜訊影響，換條件就不能沿用結果 |
| 4. 流量與壓力 | traffic pattern、讀寫比例、payload、併發、錯誤注入與負載期間 | 閒置連線、單一封包與長時間混合工作負載不是相同刺激 |
| 5. 有效暴露分母 | 儀器實計 bits、symbols、Flits、transactions 或 active time，並註明每 lane／全 link | 「64 GT/s × 牆鐘時間」會把重訓、降速、idle、編碼與無效期間誤算進去 |
| 6. Counter 契約 | 事件定義、所在層、單位、清零、飽和／overflow、取樣與彙總規則 | 一個 0 只有在知道什麼會讓它加一時才有意義 |
| 7. 分層結果 | raw／FBER、FEC corrected、CRC residual、NAK／replay、應用錯誤各自的分子與分母 | 成功修正或重送會讓上層 0 錯，卻不能抹掉底層事件 |
| 8. 退出與缺口 | retrain、downshift、link down、停機、counter 遺失、提前終止與納入／排除規則 | 只統計 link-up 時間可能把最嚴重的失敗排除在分母外 |

有效暴露應寫成「在聲明配置與 link state 內，由儀器實際計數的分母總和」，而不是從標稱
64 GT/s、x16 與牆鐘時間自行推算。若測試跨多條 lane、裝置或重複 run，還要先說它們是各自
報告或共同加總；共同電源、時鐘與環境會讓觀測相關，不能把 lane 數直接當獨立樣本數。

### 零事件仍有上界，而且上界有前提

NIST／SEMATECH 在 HPP／exponential 固定事件率模型下，對零次事件給出 MTBF 單側下限
`T / (-ln(alpha))`；取倒數後，事件率單側上限可寫成
`lambda_upper = -ln(alpha) / E`，其中 `E` 必須是和事件定義一致的總暴露。[S15]

只做一個**假想算例**：若儀器實際記錄 `E = 10^12 bits`、事先定義的錯誤為 0，並額外假設
事件服從同質 Poisson／固定率模型，令 `alpha = 0.05`，單側 95% 上界為
`2.995732273553991 × 10^-12 errors/bit`，不是 0。Python Decimal 50 位精度重算為
`2.9957322735539909934352235761425407756766016229890E-12`，獨立 awk `log` 路徑為
`2.995732273553991e-12`。兩路算術一致，只證明公式代入沒有分歧。

樣本與誤差邊界也要說完整：這是 **N=1 個假想暴露量**的確定性條件換算，沒有 sampling
SE／t；它不是產品實測、PCI-SIG pass criterion 或公司比較。PCI-SIG 自己指出 PAM4 錯誤
可能成串，lane 之間也可能受共同雜訊影響；若事件率會隨時間、通道或狀態改變，或 counter
漏記、分母用名目速率代替實計暴露，固定率上界便不能直接使用。[S11]

### 多空小作文先共用同一張成績單

| 敘事 | 合理假說 | 必須再看到的共同證據 | 什麼會讓敘事失效 |
|---|---|---|---|
| 偏多：測試與訊號內容增加 | PAM4、較窄 channel margin 與分層錯誤除錯，可能增加 PHY／controller IP、retimer／switch、PCB／CCL 設計及測試驗證工作 | 同一具名平台的配置、實計暴露、分層 counters、channel／lane margin、qualification、工具或材料用量、出貨與財務分母 | 只有規格複雜度，卻沒有額外元件、測試時間、價格、份額、訂單或毛利證據 |
| 偏空：錯誤控制吸收工程複雜度 | FEC、CRC 與 replay 可能讓應用結果穩定，不必讓每一層硬體內容或供應商收入等比例上升 | 同一工作負載下的 raw／corrected／residual／replay、延遲、功耗、降速、BOM 與部署數 | 只看到 application error 為零，卻不知道底層修正、重送、降速或停機成本 |
| 共同底線 | 技術能否運作與哪家公司能獲利是兩個問題 | 產品版本、測試分母、counter 契約、客戶 pass、出貨期間與公司財務雙向核對 | 用 zero error、official test 或一般高速能力直接代替 design win 與財務歸因 |

這兩段都只是可證偽敘事，不是對台灣公司、股價或市場定價的結論。本輪只有一條 PCI-SIG
錯誤架構鏈與一條 NIST 方法鏈（N=2 條獨立消息鏈），沒有具名產品、平台、客戶、供應商或
121 檔公司的樣本；因此不做排名，也不把條件式上界寫成任何產品的品質數字。

## 把「連得對」和「賣得出去」分成兩條軸

同一產品可以在商業軸走得很快，工程證據卻沒有公開完整；也可能已通過嚴格工程測試，客戶
部署和收入仍然沒有分母。兩條軸必須各自保存，不能把其中一條的里程碑抄到另一條：

| 兩條證據軸 | 第一步 | 中間要跨過 | 靠近完成時要看到 | 本輪位置 | 不能互相替代 |
|---|---|---|---|---|---|
| A. 連線正確性 | 電氣與通道：PAM4 訊號、封裝、板路、接收端 | Flit、錯誤修正／偵測／重送；設定、鏈路與交易協定 | 不同公司的主機、訊號元件、交換器與終端在同一條件下重現正常及錯誤恢復 | 規格與測試分類已明確；部分產品有公司互通主張，完整公開矩陣未見 | 元件量產不能替電氣或協定測試；一次連上不能替長時間互通 |
| B. 商業落地 | 具名產品宣稱支援、樣品或公司 qualification | PCI-SIG official testing、公開列名、客戶平台驗收 | 具名 production fleet、重複出貨、份額、價格與財務歸因 | 連接元件與儲存終端已有量產主張；64 GT/s 公開列名、完整客戶部署與台灣財務未證 | 正式測試不能替客戶採用；客戶驗證也不能替公開合規或財務分母 |

兩軸不是成熟度分數。新聞若只推進一格，就只更新那一格；缺少現價、共識、估值與部位資料時，
本文也不把技術或公司成熟度轉成股票動作。

## 把六個動作分成不同時鐘

| 本文六個時鐘 | 誰來確認 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 規格與測試入口存在 | 標準組織發布規格，並定義電氣、設定、鏈路、交易與跨廠測試 | PCIe 6.x 規格、Compliance Program 與第 140 次工作坊已提供制度和最高 64 GT/s 測試入口 | 活動後具名產品在每個必要 test area 的版本、速度與結果 | 有考場和考科不等於任何考生通過，也不等於產品已量產 |
| 2. 具名產品宣稱支援 | 供應商交代產品名稱、功能、速度目標與可用階段 | Astera Labs 有連接產品組合；Micron 有 9650 Gen6 固態硬碟 | 每項產品的硬體版本、韌體、正式結果與客戶平台 | 產品名稱中的 Gen6 不等於所有測試都在 64 GT/s 完成 |
| 3. 供應商或客戶完成互通 | 供應商實驗室或客戶平台把不同裝置接在一起驗證 | Astera Labs 宣稱已完成實驗室與客戶驗證，但參與者與矩陣未完整公開 | 不同公司主機、交換器、訊號元件與終端的組合及重現結果 | 公司或客戶自訂驗證不等於標準組織正式測試 |
| 4. 具名產品正式通過並列名 | 產品完成必要 compliance test areas 與跨廠門檻，公開列表記下產品與條件 | 制度要求已明確；現行清單可見部分帶有 Gen6 功能名稱的產品列在 PCIe 5.0、32 GT/s | 第 140 次工作坊後可核對四類測試、interop 與具名 PCIe 6.x、64 GT/s 列項 | 較低速度列項不能當作最高速度失敗，也不能替其他測項或產品背書 |
| 5. 單一元件進入量產 | 供應商確認能穩定製造、出貨或提高產量 | Astera Labs 宣稱連接產品增產；Micron 宣稱 9650 大量生產 | 出貨產品、期間、客戶資格與裝入系統的分母 | 一顆元件量產不等於同一路徑的其他元件或軟體已準備完成 |
| 6. 完整平台進入客戶部署 | 具名客戶用完整組合持續運作，交代規模、期間與利用結果 | 本輪沒有完整主機、交換器、訊號元件與終端的具名生產系統 | 客戶平台、元件表、軟硬體版本、部署數、期間與可重現運行結果 | 參考架構、未具名驗證或元件出貨不等於生產環境已部署 |

六個時鐘不保證固定先後：客戶驗證可能早於公開清單，元件也可能在正式列項更新前量產。
研究中心只要求每個時鐘各自有證據，不把它們壓成單一成熟度分數。

## 8 月 12 日複核：考場已開，最高速度公開列名仍未見

**公開清單只證明它寫出的條件。** 本輪完整頁面捕捉仍把 Cadence、Synopsys、Credo 與
Astera 等功能名稱含 Gen6 或 64GT/s 的產品列在 PCIe 5.0 at 32GT/s，沒有捕捉到
Spec Revision 為 PCIe 6.x at 64GT/s 的列。[S2]

**工作坊結束不是一鍵列名。** 產品還要以正確角色完成必要測項與跨廠互通門檻，再提交
Product Listing Request Form；表單可在工作坊後任何時間送出，沒有截止期限。[S9][S14]

**因此缺列仍是待驗證，不是反證。** 它不能證明 64 GT/s 測試失敗、產品能力不足或結果
不存在；研究中心只把「測試入口已存在」與「捕捉日尚未見最高速公開列項」分欄保存，等待
第一筆能辨認受測物件、邊界、必要測項與列名日期的結果。[S2][S14]

## 把六類角色放回同一套平台

| 本文六類角色 | 它負責什麼 | 本輪具名例子 | 已證實到哪裡 | 不能外推 |
|---|---|---|---|---|
| 1. 規格與正式測試組織 | 維護共同規則、測試程序、工作坊與公開清單 | PCI-SIG | 工作坊可測到 64 GT/s，現行清單可核對每列版本與速度 | 規格或測試入口不等於具名產品通過、量產或部署 |
| 2. 主機、控制器與平台 | 發起連線，整合處理器、主機控制、韌體、驅動與板路 | Micron 公告提到 NVIDIA BlueField-4 STX 參考架構 | 只確認一條具名參考架構路徑，沒有完整客戶部署結果 | 被終端供應商提及不等於主機平台已完成正式最高速測試 |
| 3. 連接與訊號元件 | 提供訊號重整器、交換器、速率轉換器與主動電纜 | Astera Labs PCIe 6 連接產品組合 | 公司宣稱完成客戶驗證並開始增產 | 公司產品組合不等於每項產品都有 64 GT/s 公開列項 |
| 4. 終端與儲存裝置 | 接收資料並完成儲存、網路或運算工作 | Micron 9650 資料中心固態硬碟 | 公司宣稱已大量生產，並對應具名參考架構 | 終端量產不等於主機到終端的完整路徑已互通或部署 |
| 5. 系統整合、雲端客戶與營運者 | 組合所有位置，完成驗收、上線、監控與實際工作 | Astera Labs 提到未具名人工智慧與雲端客戶 | 只確認公司自述的客戶驗證，沒有客戶名、平台矩陣與部署分母 | 未具名客戶驗證不等於正式生產系統、訂單或利用率 |
| 6. 台灣供應鏈查證 | 由平台端與公司端雙向對上產品、資格、出貨與財務 | 矽智財、伺服器組裝／機構、PCB／CCL 只是搜尋路由 | 本輪沒有 universe 公司具名 64 GT/s 結果或財務證據 | 一般高速能力、伺服器製造或高階板材能力不等於已受惠 |

六類角色用來分清「誰應該拿出哪份證據」，不是完整供應商名單，也不是上下游、份額或投資排序。
一家公司在某個位置有產品，不會自動替主機、終端、正式測試、客戶部署或台灣公司財務補上缺口。

## 最後用六關分開「元件已量產」與「整套系統已通過」

| 本文六關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 完整連線的位置與責任可辨認 | 主機、板路、必要訊號元件、交換器、終端與軟體都有具名角色 | 本輪來源分別出現連接產品、儲存終端與參考架構，但不在同一公開配置 | 同一測試中的產品表、接線圖與每個位置的負責者 | 不同新聞各有一個產品，不等於它們在同一系統裡工作 |
| 2. 測試合約寫完整 | 規格版本、速度、通道、拓撲、軟硬體版本、四類 compliance、interop 與通過條件可重現 | Compliance Program 定義 Electrical、Configuration、Link Protocol、Transaction Protocol 及跨廠測試；工作坊給出最高速度 | 具名 64 GT/s 組合在各必要 test area 的版本、錯誤情境、結果與重現方法 | 只有活動名稱、最高速度、單一測項或單一截圖不等於完整測試 |
| 3. 具名產品在目標速度正式通過 | 標準組織把產品、功能、規格版本、必要測項與 64 GT/s 結果連在一起 | 本輪只見部分 Gen6 功能產品的 32 GT/s 列項，沒有捕捉到具名 64 GT/s 完整結果 | 第 140 次工作坊後可公開核對的 PCIe 6.x、64 GT/s 測項與列項 | 32 GT/s 結果不是 64 GT/s 失敗，一類 pass 也不能替其他必測項背書 |
| 4. 不同廠商的完整路徑互通 | 至少兩家獨立供應商的主機、訊號元件、交換器與終端，在共同軟體下重現正常與錯誤結果 | Astera Labs 有實驗室與客戶驗證主張，但沒有完整參與者與測試矩陣 | 廠商組合、拓撲、速度、通道、韌體、錯誤注入、期間與重現方法 | 單廠端到端展示或未具名客戶驗證不等於跨廠通過 |
| 5. 具名客戶的完整平台穩定部署 | 客戶把同一組合放進生產環境，交代部署量、期間、工作負載、故障與利用率 | 只有元件增產、固態硬碟大量生產與參考架構，沒有完整客戶生產系統 | 客戶平台、元件與版本表、驗收結果、部署分母及實際運行指標 | 元件量產、參考架構或客戶驗證不等於生產環境已上線 |
| 6. 台灣公司財務足跡可雙向核對 | 平台或客戶文件與公司文件對上同一產品、測試、資格、出貨、期間與財務分母 | 矽智財、伺服器組裝／機構與 PCB／CCL 仍是待驗證路由 | 具名設計導入、訂單或出貨，以及營收、毛利或利用率的可辨識貢獻 | 技術能力、會員、生態系或一般人工智慧伺服器收入不等於本題受惠 |

本輪第一關已補上規格機制與分散產品，第二關知道正式測試有哪些區域，第三關仍沒有具名最高速
完整結果，第四關缺完整
跨廠矩陣，第五關仍停在元件量產與參考架構，第六關也尚未通過。六關是閱讀與證據排序，不是
效能分數、生態系完成率、供應商名單、市場份額、營收預測或投資排名。

## 這篇對公司判斷的用處與界線

矽智財研究可追主機控制器、實體層電路、Flit／錯誤控制、訊號重整與交換功能；伺服器組裝與
機構研究可追板路、連接器、線材、韌體、散熱、四類 compliance 與整機驗收；PCB／CCL 可追
PAM4 channel、材料、板層設計、訊號完整性與量產良率。
這些都只是告訴研究者下一份證據要去哪裡找，不是公司已取得訂單。

要升級任何台灣公司，必須由具名平台或客戶文件與公司文件雙向對上同一產品、64 GT/s 測試、
客戶資格、出貨期間與財務分母。本輪沒有這組證據，因此不支持個股受惠、訂單、營收、毛利或投資動作。

## 來源與證據邊界

- [PCI-SIG 第 140 次相容性工作坊](https://pcisig.com/events/pci-sig-compliance-workshop-140)（64 GT/s 與訊號重整器正式測試選項）。
- [PCI-SIG 合格產品清單](https://pcisig.com/developers/integrators-list)（動態列表，本輪再捕捉至 2026-08-12）。
- [Astera Labs 第六代 PCIe 連接產品增產公告](https://ir.asteralabs.com/news-releases/news-release-details/astera-labs-ramps-production-pcie-6-connectivity-portfolio)（公司客戶驗證與量產主張）。
- [Micron 9650 第六代 PCIe 固態硬碟](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin)（終端大量生產與參考架構）。
- [PCI Express 基礎規格索引](https://pcisig.com/specification-overview/pci-express-base)（規格版本入口）。
- [PCI-SIG PCI Express 6.0 Specification](https://pcisig.com/pci-express-6.0-specification)（PAM4、Flit、FEC、CRC 與相容性機制）。
- [PCI-SIG Compliance Program](https://pcisig.com/developers/compliance-program)（interop／compliance 分工、正式門檻與四類 test areas）。
- [PCI-SIG 第 140 次工作坊邀請與測試政策](https://pcisig.com/sites/default/files/2026-05/PCIWorkshop140%20Invitation%20Draft.pdf)（受測角色、CEM connector 邊界、必要測項與列名申請程序）。
- [PCI-SIG：PCI Express 5.0 Compliance Testing](https://pcisig.com/sites/default/files/files/PCI-SIG%20PCIe%205.0%20Compliance%20Webinar_1.25.23_FINAL.pdf)（投影片 28–29 的接收端 lane margining 功能、L0 狀態及 AIC／System 分工）。
- [Keysight P5578CTSA PCIe 6.0 Protocol Compliance Test Application User Guide](https://www.keysight.com/lb/en/assets/9926-01135/user-manuals/Keysight-P5578CTSA-PCIe-6.0-Protocol-Compliance-Test-App-UserGuide.pdf)（Edition 1.1，pp.108、110–111 的 75-22、PHY2-7／PHY2-8 與 retimer 程序邊界）。
- [PCI Express 6.0 FAQ](https://pcisig.com/faq?field_category_value%5B%5D=pci_express_6.0&keys=PAM4)（四電位訊號、256-Byte Flit 與錯誤控制問答）。
- [PCI-SIG：The Evolution of the PCI Express Specification](https://pcisig.com/blog/evolution-pci-express-specification-its-sixth-generation-third-decade-and-still-going-strong)（PAM4 error model、FEC／CRC／replay 與 Flit 連動）。
- [Synopsys：Optimizing PCIe 6.0 Designs at 64GT/s](https://www.synopsys.com/articles/pcie-6-designs.html)（獨立 IP 設計視角的 channel、PHY／controller、Flit 與測試責任）。
- [NIST／SEMATECH：Constant repair rate (HPP/exponential) model](https://www.itl.nist.gov/div898/handbook/apr/section4/apr451.htm)（零事件時的單側 MTBF 下限與等價事件率上限方法；不是 PCIe 合規規格）。

本文不比較 Astera、Micron 或 Synopsys 的效能數字，因為元件類型、測試方法與工作負載不同；
也不以公開清單筆數推估市占。規格機制、正式 test area、工作坊入口、公司互通實驗室、客戶
驗證、量產公告與合格產品清單是不同證據，不合併計數。本文沒有現價、共識、估值、部位或
台灣公司可辨識題材財務，因此不宣稱市場尚未反映，也不給個股動作。

## 影響路由

<!-- impact
group_id: ipdesign
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-10
rationale: PCIe 6 會連到 controller、PHY、retimer、switch 與 firmware，但本輪沒有 universe 公司具名 64 GT/s official pass、客戶 qualification 或財務證據
evidence_boundary: 會員資格、PCIe IP 或一般高速介面能力不等於 Gen6 design win、compliance、量產或收入
-->

<!-- impact
group_id: serverodm
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-10
rationale: 完整 PCIe 6 平台需 host、switch、retimer、endpoint、firmware 與散熱共同驗證，但沒有 universe ODM 的具名 production platform 與部署分母
evidence_boundary: 製造 AI server 或被列入生態系不證明 PCIe 6 fleet deployment、訂單或毛利
-->

<!-- impact
group_id: pcb
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-10
rationale: 64 GT/s 提高板級訊號、材料、連接與測試要求，形成 PCB／CCL 搜尋入口；本輪沒有具名 stack-up、材料 qualification 或財務證據
evidence_boundary: 更高速率的物理要求不自動對應任一 PCB／CCL 公司份額、ASP、訂單或獲利
-->

## 下一個可證明／否定的節點

- PCI-SIG 公開 Workshop #140 後具名 PCIe 6.x 64 GT/s pass／Integrators List 列項。
- 首項最高速列項把受測物件、AIC／System／Component 角色、CEM connector 邊界、必要測項、互通分母與 listing form 日期一併保存。
- 同一具名產品把 Electrical、Configuration、Link Protocol、Transaction Protocol 與 interoperability 的必要結果逐項公開。
- 至少兩家獨立 host、retimer／switch 與 endpoint 供應商公開可重現的 64 GT/s 拓撲、Flit／錯誤恢復與長時間結果。
- 第一份具名長時間「零錯誤」結果公開儀器實計暴露、counter 定義／重置／彙總、raw／FEC corrected／CRC residual／replay／application 各層結果，以及降速、重訓與停機缺口。
- 第一份具名 64 GT/s lane-margining 結果同時公開 DUT 角色、port／方向、75-22 或後繼測項、規格／MOI／工具／approved system、原始 timing／voltage 值、traceable calibration、預先門檻、unit×lane×環境分母及 field correlation。
- 具名客戶把完整平台從 qualification 升級到 production fleet，並揭露部署量或實際運行指標。
- 若 Gen6 元件長期只以 gearbox 連 Gen5 生態、64 GT/s listing 延後、必要測項不完整或跨廠互通不穩，兩軸成熟度必須分別下修。
- 台灣公司由平台端與公司端同時對上具名產品、64 GT/s 測試、客戶資格、出貨及財務後，才建立公司線。
