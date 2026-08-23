# 元件通過短路測試，電源仍不能直接上機：SiC 從 JEP203／JEP204 到 AI BBU／PSU 的七關資格鏈

<!-- research_topic
topic_id: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION
schema_version: 3
status: triaged
priority: p2
captured_at: 2026-08-12
source_published_at: 2026-06-03
last_reviewed_at: 2026-08-12
review_due: 2026-09-15
source_type: mixed
publisher: JEDEC
publisher_domain: businesswire.com
canonical_url: https://www.businesswire.com/news/home/20260603176123/en/JEDEC-Releases-New-SiC-Guidelines-to-Improve-Reliability-and-Evaluation-in-Power-Electronics
source_chain_id: sic-ai-power-qualification-primary-scan-20260812
stock_ids: 2308
group_ids: power,powersupply
trigger_type: sic_device_to_ai_power_system_qualification_chain
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C11
base_confidence: medium
confidence_basis: JEDEC 的文件索引與發布稿直接界定 JEP203／JEP204 的元件級範圍，三份具名 OCP 規格又提供系統故障、derating、DFMEA、MTBF、HALT、mixed-source 與 NPI 驗收條款；Infineon、ROHM 與台達資料補上 reference design、供應商採用及系統產品證據，onsemi 與 Infineon 的官方應用手冊再把 DESAT 偵測、blanking、soft turn-off、過衝及特定元件實例拆成可定位時鐘。這些獨立一手鏈足以建立七關資格與四參考面框架，也一致顯示公開的元件／驅動資料尚未和本輪三份平台規格接成同一條可重算驗收鏈
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-12
from: initial
to: inbox
reason: captured_new_sic_guidelines_reference_design_adoption_and_platform_specs
evidence: source_chain:sic-ai-power-qualification-primary-scan-20260812
-->
<!-- transition
date: 2026-08-12
from: inbox
to: triaged
reason: separated_device_test_reference_design_system_qualification_and_financial_attribution
evidence: sources:S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_fault_current_device_waveform_and_protection_timing_reference_plane_crosswalk
evidence: sources:S13,S14
-->
<!-- transition
date: 2026-08-24
from: triaged
to: triaged
reason: added_same_package_pinout_to_customer_acceptance_mixed_source_passport_without_thesis_clock_refresh
evidence: sources:S5,S13,S14,S15,S16
-->

<!-- research_source
source_id: S1
role: standard
source_kind: living_index
publisher: JEDEC
title: JEP203 Guideline for Short Circuit Evaluation in Power Conversion Transistors
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.jedec.org/document_search?search_api_views_fulltext=JEP203
locator: 2026-08-12 的 JEP203 文件列；日期 May 2026，abstract 說明以一系列 test methods 與 circuits 評估 power conversion transistor 的 short-circuit capability，committee 為 JC-70／JC-70.1／JC-70.2
limitation: 公開索引只提供標題、日期、abstract、committee 與關鍵字；下載全文需要 JEDEC 登入／註冊，本輪沒有審閱完整 test circuit、waveform、sample、failure criterion 或報告格式
independence_group: jedec-jc70
-->

<!-- research_source
source_id: S2
role: standard
source_kind: living_index
publisher: JEDEC
title: JEP204 Catalog of Stress Procedures for Silicon Carbide Devices for Power Electronic Conversion
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.jedec.org/document_search?search_api_views_fulltext=JEP204
locator: 2026-08-12 的 JEP204 文件列；日期 May 2026，abstract 說明它是 SiC PECS devices 可用 reliability 與 ruggedness stress procedures 的 overview，committee 為 JC-70／JC-70.2
limitation: 公開索引沒有完整 catalog、逐項條件、抽樣、失效門檻或 application-specific pass criteria；本文不把未讀全文中的可能項目自行補成 gate-oxide、thermal-cycle 或 lifetime 數字
independence_group: jedec-jc70
-->

<!-- research_source
source_id: S3
role: standard
source_kind: document
publisher: JEDEC
title: JEDEC Releases New SiC Guidelines to Improve Reliability and Evaluation in Power Electronics
published_at: 2026-06-03
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.businesswire.com/news/home/20260603176123/en/JEDEC-Releases-New-SiC-Guidelines-to-Improve-Reliability-and-Evaluation-in-Power-Electronics
locator: 發布稿 JEP203／JEP204 段落；JEP203 對 short-circuit capability、protection design 與 testing consistency，JEP204 對 reliability、environmental 與 ruggedness stress procedures 的共同框架
limitation: 這是 JEDEC 經 Business Wire 發布的摘要，不是兩份 guideline 全文；發布一套共同語言也不表示任何 BBU／PSU 客戶已引用、設定 pass threshold 或完成 qualification
independence_group: jedec-jc70
-->

<!-- research_source
source_id: S4
role: standard
source_kind: document
publisher: Open Compute Project
title: OCP Specification Diablo 400 v0.7.0
published_at: 2026-03-01
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf
locator: PDF pp.11–18、21、25；800 kW–1 MW+ disaggregated power rack、±400 VDC、45–90 秒 BBU、動態負載、10–40 kA available short-circuit fault current 與 system integrator responsibility
limitation: 文件明示部分 configuration figure 是 illustration 而非 final design；它是系統架構／需求，不提供 SiC 料號、JEP203／JEP204 mapping、元件 qualification report、production BOM、客戶部署或財務
independence_group: ocp-diablo400
-->

<!-- research_source
source_id: S5
role: standard
source_kind: document
publisher: Open Compute Project
title: Open Rack V3 HPR V2 12kW PSU Module Specification Rev 1.0.0
published_at: 2026-06-12
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/documents/open-rack-v3-hpr-v2-12kw-psu-module-spec-v1-0-0-pdf
locator: PDF pp.18、40–43；output short-circuit protection、IPC-9592B Class II derating、Telcordia SR-332、500K-hour DMTBF target at 90 percent confidence、DFMEA、HALT、EVT／DVT／PVT、mixed-source build 與 PCN
limitation: 500K hours at 90 percent confidence 是規格要求，不是本研究觀測樣本；文件沒有指定 SiC、JEP203 或 JEP204，也不能由 PSU-level 條款反推某個元件已通過或哪家供應商得標
independence_group: ocp-hpr12kw-psu
-->

<!-- research_source
source_id: S6
role: standard
source_kind: document
publisher: Open Compute Project
title: Open Rack V3 48V BBU Module Specification Rev 1.4
published_at: 2023-09-12
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/documents/open-rack-v3-bbu-module-spec-1-4-pdf
locator: PDF pp.1、18、24、40–41、44；Meta／Delta contribution、overcurrent／short-circuit thresholds、mixed-supplier interoperability、IPC-9592B derating、Telcordia SR-332 1M-hour target、DFMEA、burn-in／ORT 與 Delta supplier listing
limitation: 這是 48V BBU 的 2023 revision，用來示範 platform qualification 欄位而非代表 2026 高壓架構；文件沒有 JEP203、JEP204、SiC 或 800V BBU 元件條件
independence_group: ocp-orv3-48v-bbu
-->

<!-- research_source
source_id: S7
role: competitor_primary
source_kind: document
publisher: Infineon Technologies
title: 24 kW SiC-based Battery Backup Unit Reference Design for High-Voltage AI Data Centers
published_at: 2026-06-02
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.infineon.com/technology-news/2026/infpss202606-093
locator: 24 kW BBU、battery stack-to-800 V bus、650 V／1200 V SiC、450 W per cubic inch、greater-than-99-percent efficiency、IMT65R033M2H、175 C Tj、dv/dt、thermal cycling、full Infineon BOM 與 ORing／hot-swap 段落
limitation: 這是一套單一供應商 reference design 與供應商性能主張，N=1 設計而非統計樣本；沒有具名平台 qualification、JEP mapping、production customer、deployment、跨廠重現、出貨或收入
independence_group: infineon-hv-bbu
-->

<!-- research_source
source_id: S8
role: competitor_primary
source_kind: document
publisher: ROHM
title: ROHM SiC MOSFET Adopted in BBU for AI Servers as HVDC Architectures Advance
published_at: 2026-06-03
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.rohm.com/news-detail?defaultGroupId=false&news-title=2026-06-03_news_sic-mosfet
locator: SCT4013DLL 750 V SiC MOSFET、AI server ±400 V power architecture BBU power section、175 C Tj，以及約 560 V BBU battery voltage 下可延伸到 800 V architecture 的公司說明
limitation: 供應商沒有具名 BBU 廠、平台、客戶、測試條件、JEP203／JEP204、出貨量、deployment 或財務；單一供應商所稱 adopted 不代表市場普遍滲透或客戶端獨立確認
independence_group: rohm-sic-bbu-adoption
-->

<!-- research_source
source_id: S9
role: management_commentary
source_kind: living_index
publisher: ROHM and Delta Electronics
title: Special Dialogue - HVDC for AI Servers
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.rohm.com/ir/dialogue/ai-server
locator: Delta Power and System Business Group 主管談 800 VDC／±400 VDC coexistence、planned Q2–Q3 2026 mass production、two-stage PSU 及 planned ROHM Si／SiC MOSFET adoption 的段落
limitation: 頁面沒有可定位發布日期；這是公司管理層的 forward-looking plan，沒有 customer acceptance、production shipment、JEP citation、料號數量、收入或毛利，且由 ROHM 主站刊載
independence_group: rohm-delta-hvdc-dialogue
-->

<!-- research_source
source_id: S10
role: company_release
source_kind: living_index
publisher: Delta Electronics
title: 2025 Chairman Statement
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.deltaww.com/en-US/investors/chairman-statement
locator: 2025 Power Electronics 段落；90 kW 800 V-to-50／48 V DC-DC shelf、約 10 秒 supercapacitor backup、800 V-to-50／12 V PDB peak efficiency up to 98.5 percent、1.1 MW in-row rack 與 106 kW AC-DC rack units
limitation: 公司級產品與架構揭露不拆 SiC／Si／GaN BOM、JEP qualification、具名客戶、各產品出貨、收入或毛利；不能和 Infineon stage efficiency 做直接比較
independence_group: delta-2025-chairman-statement
-->

<!-- research_source
source_id: S11
role: company_release
source_kind: living_index
publisher: Delta Electronics
title: Delta Debuts Solid-State Transformer System at a Hyperscale Data Center Campus in China
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://brandnews.deltaww.com/en/SpecialDetail/12748
locator: 2026/02 brand report；Chindata North China site／Meituan、Delta SiC high-frequency power conversion、240／400／800 V DC outputs、up-to-98.5-percent conversion efficiency 與 local fault containment
limitation: 這是 Delta 品牌報導的具名 SST deployment，不是獨立客戶技術報告，也不是 BBU／PSU JEP203／JEP204 qualification、料號 BOM 或可分辨財務貢獻
independence_group: delta-sst-deployment
-->

<!-- research_source
source_id: S12
role: standard
source_kind: living_index
publisher: Open Compute Project
title: Data Center Facility Power Distribution Sub-Project
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/wiki/Data_Center_Facility/Power
locator: 2026-08-12 的 Power Distribution sub-project；System Architecture、Protection and Safety、Main Components、Codes and Standards、Rack and Power 等 workstream 與公開資料入口
limitation: 動態工作頁只供追蹤新規格與 revision；workstream 存在不表示 JEP203／JEP204 已被採用、任何元件通過 qualification 或產品已部署
independence_group: ocp-power-distribution-index
-->

<!-- research_source
source_id: S13
role: competitor_primary
source_kind: document
publisher: onsemi
title: Short-Circuit Protection Circuit Design for High Power Modules — AND90337/D
published_at: 2025-04-01
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.onsemi.com/download/application-notes/pdf/and90337-d.pdf
locator: April 2025 Rev.0（published_at 以文件月份首日正規化）；PDF pp.4–6 的 DESAT threshold／blanking、normal-versus-fault timing、soft turn-off／overvoltage-clamp trade-off
limitation: 文件以 motor／traction inverter 為應用脈絡，沒有 AI BBU／PSU、JEP203／JEP204、OCP platform、客戶 acceptance、production BOM 或 field result；電路與波形是設計指引，不是本研究的量產樣本
independence_group: onsemi-gate-driver-protection
-->

<!-- research_source
source_id: S14
role: competitor_primary
source_kind: document
publisher: Infineon Technologies
title: EiceDRIVER F3 — Single-channel enhanced isolated gate driver family with short-circuit protection, AN-2022-03 V1.2
published_at: 2023-05-08
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.infineon.com/assets/row/public/documents/60/42/infineon-1ed332xmc12n-technical-description-applicationnotes-en.pdf?fileId=8ac78c8c7e7124d1017ef7883db65158
locator: PDF 第 18–19 頁；Section 5.2 的 400 V、IMW120R045M1、CDESAT 51 pF、約 250 A、約 2 microseconds 與 3 microseconds device capability，以及 Section 5.3 移除外加 DESAT capacitor 後約 1.2 microseconds 的固定實例
limitation: N＝1 個供應商、具名 driver／device 與固定 lab circuit 的示範；不是跨元件規格、JEP report、AI BBU／PSU system qualification、客戶測試、失效率、production shipment 或財務證據
independence_group: infineon-eicedriver-short-circuit
-->

<!-- research_source
source_id: S15
role: competitor_primary
source_kind: document
publisher: onsemi
title: M1 1200 V SiC MOSFETs & Modules — Characteristics and Driving Recommendations, AND90103/D Rev.3
published_at: 2022-06-01
captured_at: 2026-08-24
accepted_at: 2026-08-24
status: active
url: https://www.onsemi.com/download/application-notes/pdf/and90103-d.pdf
locator: June 2022 Rev.3（published_at 以文件月份首日正規化）；PDF file pp.2–4 的 VDS／VGS／VTH、跨供應商 RDS(on) 應在 application temperature 比較，file pp.7–12 的 switching loss、RG、EMI、SCWT 與 package／PCB parasitic，file p.26 的 dynamic measurement boundary；原檔 SHA-256 3d26f07426fa8c906e9178ec6cf9628d14a58395facfa716a3f5b8fae352dbee，引用頁與相鄰 file pp.1–13、25–26 已渲染核對
limitation: 文件只涵蓋 onsemi M1 1200 V 家族與典型 reference values；vendor 曲線沒有完整原始分布，也不是兩家 SiC alternate part、AI BBU／PSU 同板 qualification、客戶 acceptance、production BOM、field reliability 或財務證據
independence_group: onsemi-sic-engineering-guidance
-->

<!-- research_source
source_id: S16
role: competitor_primary
source_kind: document
publisher: onsemi
title: Performance Comparison of 1200 V SiC MOSFET and Si IGBT Used in Power Integrated Module for 1100 V Solar Boost Stage, AND90082/D Rev.0
published_at: 2020-12-01
captured_at: 2026-08-24
accepted_at: 2026-08-24
status: active
url: https://www.onsemi.com/pub/Collateral/AND90082-D.PDF
locator: December 2020 Rev.0（published_at 以文件月份首日正規化）；PDF file pp.2–6／文件 pp.1–5 的同一 Q0 package、pin-to-pin compatible PIM-IGBT／PIM-SiC，以及不同 rated current、Qg、gate voltage、RthJC、gate driver、PCB layout、EMI、thermal 與 high-bandwidth measurement 要求；原檔 SHA-256 cec7fe152ed03de0681f5fa618048c553983c399f220d93545ee22602745b4fe，全 6 個 file pages 已渲染核對
limitation: N＝1 組同供應商、Si IGBT 對 SiC、solar boost 的跨技術案例；它證明相同 package／pinout 不保證相同電氣與熱行為，但不是兩家 SiC、AI BBU／PSU mixed-source、客戶資格、量產或財務比較
independence_group: onsemi-sic-engineering-guidance
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: JEDEC 於 2026 年 5 月列出 JEP203 與 JEP204；公開摘要把前者界定為 power conversion transistor 的 short-circuit evaluation test methods／circuits，把後者界定為 SiC power-electronic-conversion devices 的 reliability 與 ruggedness stress-procedure overview
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-08-12
basis: S1／S2 的官方 document index 與 abstract、S3 的 JEDEC 發布稿直接列出文件名稱、日期、committee 及目的
boundary: JEP 是共同評估語言，不自動設定某一 BBU／PSU application 的 pass threshold；本輪未取得全文，故不宣稱其逐項 gate-bias、thermal-cycle、sample size、waveform 或 failure criterion
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
claim: OCP Diablo 400 v0.7.0 把公開系統需求放在 800 kW–1 MW+ sidecar power rack、±400 VDC、45–90 秒 BBU hold-up、動態負載與各應用可用 10–40 kA short-circuit fault current；它要求設計者把測試表現轉到 system-integrator 條件
supporting_source_ids: S4
contrary_source_ids:
as_of: 2026-03-01
basis: S4 PDF pp.11、15–18、21、25 的 scope、battery backup、dynamic loading、distribution 與 safety 條款
boundary: 系統功率、時間與 fault-current envelope 不指定 SiC device、JEP test、turn-off waveform、元件 pass threshold、供應商或 production BOM
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
claim: 2026 Open Rack V3 HPR V2 12 kW PSU 規格要求 output short circuit 時保護 PFC、DC-DC 與 load，並把 component derating、Telcordia SR-332、DFMEA、HALT、EVT／DVT／PVT、mixed-source build、PCN 與 first-customer-shipment 前的 demonstrated MTBF 放進平台資格流程
supporting_source_ids: S5
contrary_source_ids:
as_of: 2026-06-12
basis: S5 PDF pp.18、40–43 的 protection、Reliability and Quality 與 Manufacturing Quality Control and Testing
boundary: 文件的 500K-hour DMTBF at 90 percent confidence 是 normative target，不是本研究抽樣估計；它引用 IPC-9592B／Telcordia，而不是 JEP203／JEP204，也沒有指定 SiC
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
claim: 2023 Open Rack V3 48 V BBU 規格已要求 overcurrent／short-circuit protection、mixed-supplier interoperability、IPC-9592B derating、Telcordia SR-332 reliability prediction、DFMEA 及 DC-DC converter burn-in／ORT，並由 Meta 與 Delta contribution、列出 Delta supplier
supporting_source_ids: S6
contrary_source_ids:
as_of: 2023-09-12
basis: S6 PDF pp.1、18、24、40–41、44 的 contributor、protection、interoperability、reliability 與 supplier sections
boundary: 這是歷史 48 V BBU 的 system contract，不是 2026 800 V qualification；1M-hour target 也不是 field hours 或本研究統計，且文件沒有 SiC 或 JEP
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
claim: 本輪對三份具名 OCP PDF 的完整可搜尋文字層逐字檢索 JEP203、JEP 203、JEP204、JEP 204、SiC 與 silicon carbide，六組字串在每份文件的命中數都為 0
supporting_source_ids: S4,S5,S6
contrary_source_ids:
as_of: 2026-08-12
basis: 對 S4 全 36 頁、S5 全 50 頁與 S6 全 47 頁可搜尋文字層做 case-insensitive exact-string census；另人工定位各自 fault／reliability 段落，確認公開引用停在 system requirements、IPC-9592B 與 Telcordia SR-332
boundary: N=3 是目的性文件盤點，不是隨機抽樣、全世界 platform census 或私有 qualification 搜索，故不報 SE／t，也不推論「沒有任何平台使用 JEP」；只證明這三份公開版本沒有文字橋
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
claim: Infineon 於 2026-06-02 公開一套 24 kW high-voltage BBU reference design，從 battery stack 直連 800 V DC bus，使用 650 V／1200 V SiC，並具名 IMT65R033M2H、gate driver、sensor、MCU、auxiliary supply 及 SiC JFET ORing／hot-swap 等供應商 BOM
supporting_source_ids: S7
contrary_source_ids:
as_of: 2026-06-02
basis: S7 的 architecture、DC-DC stage、device／package、complete BOM 與 availability 段落
boundary: 24 kW、450 W per cubic inch、greater-than-99-percent efficiency、175 C 與 dv/dt／thermal-cycling 描述都屬 N=1 supplier reference design；沒有客戶平台、JEP mapping、mixed-source qualification、deployment 或統計不確定度
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
claim: ROHM 於 2026-06-03 表示 750 V SCT4013DLL SiC MOSFET 已用在 AI server ±400 V BBU power section，並說該 750 V class 可用於約 560 V battery voltage 的 next-generation 800 V architecture
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-06-03
basis: S8 adopted product、±400 V architecture 與 next-generation 800 V paragraph 直接具名 part number、voltage class 與 application
boundary: 這是 N=1 supplier-reported adoption；未具名 BBU maker、客戶、平台、qualification method、JEP、出貨量或財務，不能改寫成 broad penetration
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: 台達 2025 董事長報告已具名 90 kW 800 V-to-50／48 V DC-DC shelf、約 10 秒 supercapacitor backup、800 V-to-50／12 V PDB 與 1.1 MW in-row power rack，證明公司有多個高壓電力系統產品入口
supporting_source_ids: S10
contrary_source_ids:
as_of: 2026-08-12
basis: S10 Power Electronics 段落直接列出產品、輸入輸出、功率／時間與 company-reported efficiency
boundary: 公司沒有在此文件拆出 SiC BOM、JEP203／JEP204、BBU／PSU qualification、具名客戶、產品收入或毛利；98.5 percent peak overall efficiency 與 Infineon stage efficiency 邊界不同，不做比較
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
claim: ROHM 主站的 Delta／ROHM 對談記錄 Delta 規劃在 Q2–Q3 2026 開始 800 VDC 與 ±400 VDC power-system mass production，planned two-stage PSUs 將採 ROHM Si 與 SiC MOSFET，出貨量預期在 2027 後達高峰
supporting_source_ids: S9
contrary_source_ids:
as_of: 2026-08-12
basis: S9 由 Delta Power and System Business Group 主管直接回答 architecture coexistence、production timing、PSU topology 與 planned ROHM product adoption
boundary: 網頁沒有可定位發布日期，內容仍是 forward-looking management plan；不等於已出貨、客戶 acceptance、JEP qualification、料號數量、收入或毛利
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
claim: Delta 品牌報導另有一個 Chindata／Meituan 具名資料中心的 SiC SST deployment，支援 240／400／800 V DC output 與 local fault containment，顯示 SiC 系統能力可以進入實際場域
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-08-12
basis: S11 具名 site、operator／tenant、Delta SST、SiC high-frequency conversion、voltage outputs 與 deployment
boundary: 這是 company-authored SST case，不是 BBU／PSU、JEP203／JEP204 test mapping、獨立 field-reliability dataset、production BOM 或可分辨財務；不能替本題缺口背書
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
claim: 對本輪公開來源而言，SiC 進入 AI BBU／PSU 至少要分成 application stress envelope、標準化 device evaluation、supplier qualification data、converter validation、system reliability／protection、mixed-source customer qualification，以及 deployment／financial attribution 七關；標準、reference design、adoption 與 platform spec 各自通過一關，不能替下一關簽名
supporting_source_ids: S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11
contrary_source_ids:
as_of: 2026-08-12
basis: JEDEC 定義 device evaluation 語言，Infineon／ROHM 提供 design 或 adoption，OCP 提供 system／customer qualification contract，Delta 提供 company plan、products 與相鄰 deployment；各來源的 test object、責任主體與商業階段不同
boundary: 七關是對已審閱來源的責任分層，不宣稱窮盡私有 qualification，也不推導 SiC content、滲透率、壽命改善、供應商份額、ASP、收入、毛利、估值、股價或市場是否反映
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: unverified
status: active
claim: JEP203／JEP204 已被 AI BBU／PSU platform qualification 明文引用，並實際改變 short-circuit failure criteria、gate／thermal stress、protection timing、derating、life model 或 mixed-source acceptance
supporting_source_ids:
contrary_source_ids: S4,S5,S6
as_of: 2026-08-12
basis: 三份目的性抽查的 OCP 公開規格均沒有 JEP203／JEP204／SiC 字串；它們的系統流程引用 IPC-9592B、Telcordia SR-332、DFMEA、HALT 與 NPI tests，尚未出現可重算 crosswalk
boundary: 三份公開文件沒有文字橋不代表所有私有客戶規格都沒有；在 JEP full text、平台 crosswalk、revision diff 與 test report 出現前，只能說本輪 first rejection 已觸發
verification_needed: 平台或買方發布固定 revision 的 qualification matrix，逐項把 JEP procedure 對上 part／lot、application waveform、sample、pass／fail、protection timing、derating、DFMEA、EVT／DVT／PVT 與 change control
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C13
label: unverified
status: active
claim: universe 內功率元件或電源供應公司已因 JEP203／JEP204 導入而取得可辨識 AI BBU／PSU qualification、量產份額、訂單、收入或毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: 台達已有具名高壓產品、planned SiC PSU adoption 與相鄰 SST deployment，但 S9／S10／S11 都沒有把 JEP、特定 SiC BBU／PSU BOM、customer acceptance 與 financial numerator／denominator 接在一起；power 族群也沒有公司端閉環
boundary: 元件平台、reference design、roadmap、supplier adoption、system product 或 deployment 只能形成搜尋入口，不是本題的財務歸因
verification_needed: 買方與台灣公司雙向確認同一 platform revision、device／module part、JEP／system qualification report、production BOM、出貨期間與數量，並由公司文件拆出可重算收入、成本或毛利分母
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C14
label: verified
status: active
claim: Infineon AN-2022-03 的固定實例把 400 V DC link、IMW120R045M1、正 15 V／負 2 V gate supply、51 pF 外加 DESAT capacitor、約 250 A 短路電流與約 2 microseconds 關斷放在同一張波形，並將它和該元件 3 microseconds short-circuit withstand capability 對照；同一實例移除外加 capacitor 後約為 1.2 microseconds
supporting_source_ids: S14
contrary_source_ids:
as_of: 2023-05-08
basis: S14 第 18–19 頁的 Section 5.2／5.3 逐項列出 device、driver supply、DC link、DESAT capacitor、current、turn-off time 與 device capability
boundary: 這只是一個供應商 N＝1 固定 lab circuit 的觀測，不是所有 SiC、所有 driver、800 V、AI BBU／PSU、JEP203 pass line、可靠度分布或 production customer 結果；1.2／2／3 microseconds 不能跨 reference plane 排名
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C15
label: verified
status: active
claim: onsemi AND90337/D 將 SiC DESAT threshold 的高接面溫度驗證、blanking time 的防誤觸發與及時保護、soft turn-off／voltage clamping 的過衝抑制，以及較慢關斷增加 short-circuit energy 的代價放在同一設計取捨中
supporting_source_ids: S13
contrary_source_ids:
as_of: 2025-04-01
basis: S13 p.4 的四項 DESAT design considerations、p.5 的 normal／fault timing 與 fast-response-versus-overshoot trade-off、p.6 的 clamping／soft-turn-off circuit
boundary: 文件是 motor power module 的 supplier application note，證明設計變數互相牽制，不證明任何 AI power platform 已採同一 circuit、threshold、timing、qualification 或 field result
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C16
label: inference
status: active
claim: Diablo 400 的 10–40 kA available short-circuit fault current 與供應商應用手冊中的單顆 SiC 電流／微秒數位於不同 reference plane；要把系統故障接到元件資格，至少要同時保存故障點與 source impedance、converter 電流路徑、元件 VDS／ID／VGS／Tj 波形，以及 sensing／blanking／driver turn-off／clamp／fuse-breaker clearing 時間
supporting_source_ids: S4,S13,S14
contrary_source_ids:
as_of: 2026-08-14
basis: S4 固定 rack-level available fault-current envelope；S13 固定 device／driver detection、blanking、turn-off 與 stray-inductance trade-off；S14 用一個 fixed circuit 示範微秒數如何隨 DESAT capacitance 改變
boundary: 四參考面是跨文件建立的可重算 crosswalk，不是任何 AI BBU／PSU 已完成的 fault test、JEP adoption、客戶 acceptance 或安全認證；不同地點、阻抗、拓撲與量測邊界的 kA、A 與 microseconds 不可相除、相減或排成材料優劣
verification_needed: 具名 production BBU／PSU 以固定 platform／board revision 公開 fault location、source impedance、全部 source contribution、device／driver raw waveforms、tolerance、clearing sequence、pass／fail 與 post-fault disposition
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C17
label: verified
status: active
claim: onsemi AND90103/D 明示跨供應商比較 SiC MOSFET 時，RDS(on) 不能只看行銷常用的 25°C，而要對齊目標 application temperature；同一文件又把 VGS／VTH、RG、VDS／Tj、package／PCB parasitic 分別接到導通、切換、EMI、短路耐受與過衝
supporting_source_ids: S15
contrary_source_ids:
as_of: 2022-06-01
basis: S15 file pp.2–4 直接要求 different vendors 的 RDS(on) 在 target application temperature 比較，file pp.7–12 逐項展示 switching loss、RG／dv/dt、EMI、SCWT 與 critical-loop parasitic 的條件依賴
boundary: 這是 onsemi M1 1200 V 家族的供應商技術指引與 typical reference values，不是跨廠隨機樣本、共同 acceptance limit、兩顆 AI 電源替代料的實測或公司財務
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
claim: onsemi AND90082/D 的兩個 power integrated modules 雖使用同一 Q0 package 且 pin-to-pin compatible，PIM-IGBT 與 PIM-SiC 仍有不同 rated current、Qg、gate voltage 與 RthJC，換成快速 SiC 後還要重新處理 gate driver、PCB layout、EMI、thermal 與量測方法
supporting_source_ids: S16
contrary_source_ids:
as_of: 2020-12-01
basis: S16 file p.2／文件 p.1 直接列出 Q0 package、pin-to-pin compatible 及 Table 1 的差異；file pp.3–6 再說明 switching、driver、layout、EMI、junction temperature 與 probe bandwidth／loop 的重新設計責任
boundary: 這是 N＝1 組同供應商、Si IGBT 對 SiC 的 solar boost 跨技術反例，不是兩家 SiC supplier、AI BBU／PSU 同板 A／B、客戶 qualification 或量產 field result
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C19
label: inference
status: active
claim: SiC mixed-source 應以共同版本鍵分開九關：封裝腳位、靜態、動態、gate、保護、熱、EMI／控制、同板 A／B 與客戶驗收；通過前一關不能替下一關簽名，若 B 料必須調整 RG、VGS、dead time、DESAT、firmware、散熱或濾波後才通過，只能稱受控變更後的 alternate candidate，不是 production-config drop-in
supporting_source_ids: S5,S13,S14,S15,S16
contrary_source_ids:
as_of: 2026-08-24
basis: S15／S16 顯示相同或相鄰額定／封裝仍會在靜動態、driver、寄生、EMI 與熱分岔；S13／S14 固定 protection timing 取捨；S5 則把 mixed-source build、EVT／DVT／PVT、PCN 與客戶流程放進 system qualification，本文據此整合九關與 A-production／B-drop-in／B-tuned 護照
boundary: 九關與三版本護照是研究中心的可互換性框架，不是 OCP／onsemi／Infineon 的共同表單；本輪實際兩家 SiC、同一 AI BBU／PSU、同板客戶 acceptance／production／field／financial 的共同觀測 N＝0
verification_needed: 同一 platform／module／board revision，以凍結的 A-production 設定測 A 與 B-drop-in，再把任何 B-tuned 變更另立 revision，逐關保存 raw data、acceptance limit、sample／lot、customer sign-off、production BOM 與 field／financial 分母
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **SiC（碳化矽）**：寬能隙半導體材料；在高電壓、高溫或高頻率的電力轉換中可能降低損耗，但價格、驅動、封裝、保護與可靠度仍要一起設計。
- **功率 MOSFET**：用閘極控制大電流通斷的功率開關；datasheet 耐壓不是系統在所有故障下都安全的保證。
- **RDS(on)**：MOSFET 導通時 drain 到 source 的等效電阻；它會隨 VGS、電流與接面溫度改變，所以不同料件不能只比 25°C 的 typical 值。
- **RG／RGon／RGoff**：gate 回路電阻及分開控制開啟／關閉的電阻；它會改變切換速度、損耗、振鈴、EMI 與故障關斷過衝。
- **Qg／Miller 區**：把 gate 從關閉推到開啟所需的電荷，以及 drain voltage 轉換時的關鍵平台區；Qg 不同會改變 driver current 與 switching timing。
- **RthJC／RthCS**：熱由 junction 到 case、再由 case 到 heatsink 的熱阻；同封裝不代表這兩段熱路徑與安裝壓力相同。
- **SCWT**：Short-Circuit Withstand Time，元件在指定電壓、VGS、Tj、電路與 failure criterion 下可承受短路的時間；不能跨條件直接搬用。
- **Q0 package**：AND90082/D 兩個 power integrated module 共用的封裝家族；同封裝與 pin-to-pin compatible 只描述機械／腳位入口，不保證驅動、熱或動態行為一致。
- **AND90103/D／AND90082/D**：本文新增核對的兩份 onsemi 應用手冊；前者拆 SiC 靜動態與驅動條件，後者提供同封裝、同腳位仍需重設計的跨技術反例。
- **閘極（gate）**：控制 MOSFET 開或關的端點；電壓過高、過低、震盪或長期偏壓都可能影響可靠度，所以要保存 driver 與實際 waveform。
- **VGS／VDS／ID**：分別是 gate-to-source voltage、drain-to-source voltage 與 drain current；三條帶時間的波形要一起看，不能用其中一個峰值代表完整元件壓力。
- **Vbus（直流匯流排電壓）**：轉換器功率級兩端的主要 DC 電壓；同一顆料在不同 Vbus 下的切換、短路能量與安全餘裕會不同。
- **短路（short circuit）**：原本應經負載流動的電流遇到極低阻抗路徑，可能在很短時間內產生極大電流與熱。
- **短路耐受時間**：在指定電壓、閘極、溫度、電流限制與測試電路下，元件尚未失效的時間；離開條件就不能沿用同一數字。
- **故障能量**：故障期間電壓、電流與時間共同形成的能量；只看峰值電流或只看微秒數都不完整。
- **JEP203**：JEDEC 2026 發布的 power conversion transistor short-circuit evaluation guideline；它提供評估方法語言，不是某台 AI 電源的自動及格章。
- **JEP204**：JEDEC 2026 發布的 SiC power-device stress-procedure catalog；公開摘要只支持 reliability／ruggedness framework，本輪未審閱完整項目與條件。
- **JEP 與 JESD**：都是 JEDEC publication 類型；本文只依 JEP203／JEP204 自己的標題與摘要解讀，不能把 guideline 自動當成買方強制標準。
- **stress procedure**：刻意施加電、熱、環境或故障壓力，觀察元件是否劣化或失效的程序；程序與 pass threshold 是兩件事。
- **application stress envelope**：產品在正常、瞬態與故障情況下實際會遇到的電壓、電流、溫度、dv/dt、時間與重複次數範圍。
- **qualification**：供應商或客戶依固定樣品、條件、門檻與變更控制，決定元件、模組或系統是否能被正式採用。
- **BBU**：Battery Backup Unit，電池備援單元；主電源中斷或負載突增時，在電池與直流匯流排間充放電。
- **PSU**：Power Supply Unit，把輸入電力轉成設備需要的電壓與電流，並負責一部分保護、監測與故障回應。
- **rack（機櫃）**：把運算、網路、電源與冷卻設備按固定空間和介面整合的機構；同一機櫃內的模組會共同影響電力與故障結果。
- **Diablo 400 v0.7.0**：OCP 對高功率 sidecar power rack 的公開規格與本文審閱版本；數字是專案名稱或版號，不是單一輸出電壓或元件型號。
- **Open Rack V3／HPR V2**：OCP 機櫃與高功率 rack 架構的版本名稱；每份文件仍要連同 revision、日期與適用模組閱讀。
- **DC-DC**：把一個直流電壓轉成另一個直流電壓的轉換級；BBU 可能需要雙向 DC-DC 來充電與放電。
- **Converter（電力轉換器）**：由功率開關、driver、磁性元件、電容、感測與控制組成，把輸入電力轉成產品所需電壓與電流；元件測過不等於整個 converter 已通過。
- **pF（皮法拉）**：電容量單位，1 pF 是 10 的負 12 次方法拉；DESAT pin 的外加與寄生電容會影響偵測時間，也會牽動雜訊免疫。
- **kA**：kiloampere，千安培；在本文是系統可用短路故障電流的單位，不是單顆 MOSFET 自動承受的測試電流。
- **參考面（reference plane）**：一個電壓、電流、功率或時間究竟在哪個物理位置、哪段電路與哪種量測邊界成立；機架匯流排、轉換器支路與單顆 MOSFET 是三個不同參考面。
- **Source impedance（電源等效阻抗）**：故障點往上游看見的電阻、電感、導線與供電路徑綜合效果；它會限制電流上升與峰值，因此只有電壓和名目 kA 還不能重建元件波形。
- **DESAT protection（去飽和／導通壓降偵測保護）**：監看功率開關導通時的 VDS 或 VCE；電壓超過設定門檻後觸發關斷。門檻、溫度、雜訊、blanking 與 driver delay 都會改變結果。
- **AND90337/D**：onsemi 2025 年 4 月的高功率模組短路保護應用手冊編號；本文只借它拆 DESAT 與關斷取捨，不把 motor 例子當 AI 電源驗收。
- **Leading-edge blanking（前緣遮蔽時間）**：開關剛導通、波形尚在轉換與振鈴時，暫時不讓 DESAT 判定故障的時間窗；太短可能誤跳，太長又可能讓真短路累積更多能量。
- **Soft turn-off（緩關斷）**：故障發生後刻意降低關斷速度，以減少寄生電感造成的電壓過衝；代價是元件保持導通更久，可能增加故障能量。
- **Voltage overshoot（電壓過衝）**：電流快速改變時，寄生電感在穩態母線電壓之上疊出的瞬時尖峰；它不是另一個獨立電源，也不能只靠降低關斷時間同時消除。
- **800 VDC／±400 VDC**：兩種高壓直流分配方式；兩者的導線、接地、絕緣、保護與元件電壓條件不完全相同。
- **reference design**：供應商把元件、拓撲與控制組成可評估的設計；它能證明工程可行性，不能代替客戶 platform qualification。
- **SCT4013DLL**：ROHM 在採用公告中具名的 750 V SiC MOSFET 料號；具名料號仍要對上客戶、平台、測試與出貨。
- **BOM**：Bill of Materials，產品用到的料件清單；供應商 reference BOM 與量產 customer BOM 不是同一張表。
- **Tj**：半導體接面溫度；標示 maximum Tj 不表示產品可以長期在該溫度運作，也不等於壽命已被證明。
- **dv/dt**：電壓隨時間變化的速度；切換越快可能提高效率與功率密度，也會增加驅動、絕緣、寄生耦合與誤觸發難度。
- **derating**：刻意讓元件工作在額定極限以下，保留電壓、電流、溫度或功率餘裕；餘裕多少要由 application、壽命與失效模式決定。
- **failure criterion**：測試何時算失敗的可觀察門檻，例如無法關斷、電性漂移超限、永久損壞或保護未在期限內動作。
- **fault coordination**：偵測器、driver、MOSFET、fuse／breaker、控制器與上游／下游保護依正確順序隔離故障，避免局部問題擴大。
- **DFMEA**：Design Failure Mode and Effects Analysis，設計階段逐項列出可能失效、影響、原因、風險與緩解措施。
- **HALT**：Highly Accelerated Life Test，以加速壓力找設計弱點；它不是直接把測試小時等同實際使用壽命。
- **MTBF**：Mean Time Between Failures，可靠度預測或示範常用指標；要分清計算模型、測試證明、信賴水準與實際 field data。
- **IPC-9592B**：電腦與通訊產業 power-conversion device 的設計、可靠度與品質參考；本輪 OCP PSU／BBU 規格明文引用它。
- **Telcordia SR-332**：電子設備可靠度預測方法；模型算出的 MTBF 不等於實際部署已累積同樣時數。
- **EVT／DVT／PVT**：Engineering／Design／Production Validation Test，產品從工程樣品、設計定型到量產製程驗證的不同階段。
- **NPI**：New Product Introduction，新產品從工程設計走到量產導入的流程；不同階段要重跑相應的可靠度與製程測試。
- **MCU**：Microcontroller Unit，執行感測、控制、保護狀態與通訊的微控制器；它的軟體與延遲也可能影響故障回應。
- **mixed-source build**：把主料與第二來源／替代料放進同一批測試，檢查換料後的功能、環境與可靠度；不是只比較兩張 datasheet。
- **Drop-in alternate（直接可換替代料）**：在凍結的量產設定下換入 B 料，不改 gate、保護、韌體、散熱、濾波或其他設計，仍逐項通過原 acceptance limits。
- **A-production／B-drop-in／B-tuned**：A-production 是量產基準；B-drop-in 是 B 料直接換入；B-tuned 是為 B 料調過設定後的新版本。B-tuned 通過不會倒推 B-drop-in 也通過。
- **PCN**：Product Change Notice，料件、材料、製程、軟硬體或測試改變時的正式通知與重新 qualification 入口。
- **ride-through／hold-up**：主電力短暫異常時，PSU、電容或 BBU 讓系統繼續供電的能力；它和切斷短路是不同任務。
- **interoperability**：不同供應商模組或料件在固定介面與條件下共同工作；能互換不代表每個元件用相同技術或同一家供應商。
- **deployment**：產品已在具名場域安裝運作；部署 SST 不能自動替 BBU／PSU qualification 背書。
- **財務歸因**：把技術與同一期間的料號、出貨、價格、收入、成本和公司總額分母接起來；沒有分子與分母就不能算題材貢獻。

### 三句話抓重點

- JEP203／JEP204 已補上 SiC 元件 short-circuit 與 stress evaluation 的共同語言，但共同語言不會自動變成 AI BBU／PSU 的客戶及格線。
- 三份具名 OCP 規格已把 fault current、short-circuit protection、derating、DFMEA、MTBF、HALT、mixed-source 與 NPI 放入系統驗收；本輪逐字檢索卻沒有 JEP203、JEP204、SiC 或 silicon carbide。
- Infineon reference design、ROHM supplier-reported adoption 與 Delta 高壓產品都是真實相鄰證據；在 platform crosswalk、量產 BOM、客戶簽核與財務分母出現前，仍不能改寫成普遍滲透或台廠獲利。

### 為什麼重要

**元件測試回答「這顆開關在指定實驗條件下怎麼壞」，系統驗收回答「整台電源遇到真實故障時誰先動作」。**

兩者之間還有 gate driver、寄生電感、感測延遲、控制韌體、fuse／breaker、散熱、機構、上游與下游
負載。少一個時間或能量欄位，元件測試就不能直接換成系統安全結論。

**reference design 能降低設計起點，不會替客戶承擔風險。** 供應商可以把元件、driver、sensor、MCU、
磁性元件與保護組成一套高效率設計。

客戶仍要在自己的 voltage distribution、dynamic load、fault current、
散熱、mixed-source 與 service procedure 下重驗。這就是「能做」和「能上機」之間的距離。

**投資研究若跳過中間關卡，會把三種不同訊號疊成一條不存在的收入線。** 標準發布是方法時鐘，
adoption release 是供應商時鐘，OCP spec 是 platform contract，company product 是商業入口。

只有它們對上
同一 part、module、revision、客戶與期間，才能談出貨與財務。

### 接下來怎麼追

- 取得 JEP203／JEP204 全文後，先保存 revision、test circuit、waveform、sample、failure criterion 與報告欄位，不只摘錄標題。
- 要求平台 qualification matrix 把每個 JEP procedure 對到 application voltage／current／temperature、driver、protection timing、derating 與 DFMEA action。
- 比較 OCP 或私有平台新舊 revision，確認新增的是哪一條 normative requirement，而不是 release note 只提「reliability improved」。
- 追同一量產 BBU／PSU 的 supplier data、converter test、mixed-source EVT／DVT／PVT、customer acceptance 與 PCN／requalification。
- 最後才把台灣公司料號、出貨期間、數量、ASP、收入與公司總額分母接起，並分開 BBU、PSU、SST 與其他 power stage。

### 想一想

- 某顆 SiC MOSFET 的 short-circuit test 通過 8 微秒，若系統偵測加關斷共需更久，這個元件成績能保護整機嗎？
- 平台只規定「短路後不能損壞」，卻沒有指定元件方法，這算採用 JEP203，還是只算結果導向的 system requirement？
- 一套 reference design 效率超過 99%，另一家公司揭露整段系統 peak 98.5%，兩個 reference plane 不同，能直接排高低嗎？
- 供應商公告「adopted」但不具名客戶與 volume，最少還要哪三張文件才能畫到收入？
- mixed-source build 若換了 MOSFET，哪些 driver、thermal、firmware 與 fault tests 應該重新跑，而不能只比 pin-to-pin？

## 主張與證據帳本

本文把「已發布方法」「具名設計／採用」「平台公開條款」「公司產品／部署」和「尚缺的 crosswalk／財務」
分開。核心結論不是 SiC 不會進入 AI 電源，而是截至 2026-08-12，公開證據仍不能證明新 JEP 已經改寫
本輪三份 OCP BBU／PSU qualification。

## 先用七關看懂：同一顆 SiC 要拿七張不同的證書

| 關卡 | 真正要回答的問題 | 本輪可確認 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. Application stress envelope | 真實電壓、電流、Tj、dv/dt、fault energy、時間與重複次數是什麼 | Diablo 400 有 rack、dynamic load、BBU time 與 available fault-current envelope | 固定 BBU／PSU revision 的 component-level waveform 與 tolerance | 系統 10–40 kA 不等於 MOSFET 測試電流 |
| 2. Standardized device evaluation | 用哪個 circuit、procedure、sample 與 failure criterion 測元件 | JEP203／JEP204 的標題、abstract 與共同框架已發布 | 兩份全文與可重現附件 | guideline 發布不等於 application pass |
| 3. Supplier qualification data | 哪個 part、lot、package 與 driver 在哪些條件通過／失敗 | Infineon、ROHM 具名 part 或設計，但未公開完整 qualification pack | data report、raw waveform、failure analysis、lot／package | datasheet／press release 不等於客戶簽核 |
| 4. Converter validation | 元件放進 topology 後，效率、熱、EMI、transient 與 protection 是否仍合格 | Infineon 有 N=1 24 kW BBU reference design | 客戶硬體上的 corner／fault matrix 與多顆樣品 | reference BOM 不等於 production BOM |
| 5. System reliability／protection | DFMEA、derating、MTBF、HALT、fault coordination 與 service action 是否閉合 | OCP PSU／48V BBU 已有完整 system-contract 欄位 | 高壓 BBU／PSU 把 device 與 system timing 逐項對上 | 元件通過不能替整機保護簽名 |
| 6. Mixed-source customer qualification | 主料與 alternate part 在 EVT／DVT／PVT、shelf 與環境測試能否互換 | 12 kW PSU 規格明文要求 mix-source reliability builds | 固定 platform 的 JEP crosswalk、pass report、PCN／requalification | 單一 supplier adoption 不是多來源驗收 |
| 7. Deployment／financial attribution | 哪個客戶、平台、BOM、出貨與公司財務真正對上 | Delta 有產品、計畫與相鄰 SST deployment | BBU／PSU customer acceptance、shipment、revenue numerator／denominator | 公司能力或場域案例不等於本題收入 |

這七關不是按新聞熱度排序，而是按責任轉移排序。前一關可以縮小下一關的搜尋範圍，卻不能替下一關
承擔失效、供應或財務責任。

## JEP203 解決的是測法一致，不是替平台設定關斷時間

短路不是「電流很大」四個字就能重現的測試。至少要固定 DC bus、gate voltage、Tj、load／stray
inductance、current limit、pulse width、device package、driver、量測頻寬與 failure definition。同一顆元件在不同
條件下可以得到完全不同的 withstand result。

JEP203 的公開摘要重要之處，在於把 test methods 與 circuits 拉回共同討論；這可以減少供應商 A 與 B
用不同測法卻把兩個微秒數排在同一張圖上的錯誤。但真正的 BBU／PSU 還要回答另一組問題：sensor 何時
看到故障、controller／driver 何時下命令、MOSFET 關斷時的 overvoltage 怎麼控制、fuse／breaker 是否選擇性
動作、BBU 是否被誤觸發，以及故障後能 retry、latch-off 還是必須維修。

因此，「JEP203 測過」只支持 device evaluation。「平台引用 JEP203，且 system timing 保持在每顆 qualified
device 的 failure envelope 內」才開始接近 system qualification。本輪還沒有看到後一張公開表。

## JEP204 是 stress catalog，不是壽命保證書

JEP204 的官方 abstract 與發布稿把它描述為 SiC device reliability／environmental／ruggedness stress procedures
的共同框架。這對 qualification engineer 很有價值，因為不同供應商至少能開始用相近術語保存測試與結果。

但 catalog 只回答「可用哪些程序與怎麼描述」。特定 AI power product 還要自行決定：

1. 哪些 stress 對該 topology、package 與 cooling 真正 relevant。
2. 正常、transient、fault 與 storage condition 各自的最大 exposure。
3. sample、lot、duration、acceleration model 與 pass／fail threshold。
4. 劣化如何回到 derating、DFMEA、protection timing、warranty 與 PCN。

由於本輪沒有登入下載全文，本文不列「JEP204 必然包含某一 gate-oxide 或 thermal-cycle 條件」。這不是
缺少產業常識，而是避免把二手印象冒充文件內容。真正取得全文後，應新增 procedure-level crosswalk，
而不是改寫目前已審閱的摘要。

## 三份 OCP 規格真正教了什麼

### Diablo 400：先定義系統會遇到多大的世界

Diablo 400 描述 800 kW–1 MW+ sidecar power rack、±400 VDC、45–90 秒 BBU hold-up、不同 dynamic-load
profile 與依應用而異的 10–40 kA available short-circuit fault current。這些是 system envelope：它告訴設計者
整個 rack 要承受什麼，不告訴他哪一顆 SiC、哪套 JEP procedure 或哪個 microsecond threshold 必須使用。

### 12 kW PSU：把可靠度變成跨開發階段的工作

這份 2026 PSU 規格不只寫「可靠」。它要求 worst-case thermal／electrical stress analysis、IPC-9592B Class II
derating、Telcordia SR-332、DFMEA、HALT、EVT／DVT／PVT、mixed-source build、PCN 與 change qualification。
短路條款還規定 output voltage 低於特定條件後的 shutdown／retry／latch behavior，以及不要誤觸發 BBU。

規格中的 minimum 500K-hour demonstrated MTBF at 90% confidence 是供應商必須達到的驗收目標，不是本文
觀察 500K 小時得到的估計，也不能拿來替任何 SiC part 算 field failure rate。

### 48 V BBU：舊電壓也有值得沿用的資格骨架

2023 48 V BBU 規格已經把 overcurrent／short circuit、fault thresholds、mixed-supplier interoperability、
derating、reliability prediction、DFMEA、burn-in／ORT 與 quality process 放在一起。它也具名 Meta／Delta
contribution 與 Delta supplier。

它的價值是教我們 platform qualification 應該有哪些欄位，不是證明 800 V 已照相同條件驗收。若新高壓
BBU 只換 bus voltage 卻沒有重新定義 insulation、fault energy、device／driver timing 與 cooling，研究者反而
應該把它標成待驗證，而不是假設舊證書可直接搬家。

## 「0 次命中」能說什麼，不能說什麼

本輪對 Diablo 400 v0.7.0、Open Rack V3 HPR V2 12 kW PSU Rev 1.0.0 與 Open Rack V3 48 V BBU Rev 1.4
的完整可搜尋文字層檢索六組字串：`JEP203`、`JEP 203`、`JEP204`、`JEP 204`、`SiC`、
`silicon carbide`。三份文件每一組都是 0 次。

這個結果的正確讀法是：

- 在這三個固定版本中，沒有公開文字把 JEDEC 新 guideline 或 SiC 料件接到 platform requirement。
- 文件仍有實質 short-circuit、derating、DFMEA、reliability 與 mixed-source 條款，所以「沒寫 JEP」不等於「沒做可靠度」。
- N=3 是依題目目的選出的文件盤點，不是隨機樣本；沒有 SE、t 值，也不能推論所有 OCP、GPU vendor、hyperscaler 或私有 customer spec。
- 未來若新 revision 增加 cross-reference，應新增 source／claim 並保留舊版本，不可把 2026-08-12 的 0 次命中回填成後來內容。

候選題事先寫下的第一拒絕是：若 JEP 沒有被 platform qualification 引用，就只是一組元件級指引。本輪
確實觸發這個拒絕條件；文章之所以仍值得發布，是因為它把「哪一座橋還沒接上」變成可監測、可否定的
資格鏈，而不是為 SiC 題材補一個正面故事。

## Reference design、adoption、platform qualification 是三張不同證書

| 公開訊號 | 它能證明 | 它不能證明 |
|---|---|---|
| Infineon 24 kW BBU reference design | 一套具名 SiC topology、part 與 supplier BOM 能達成公司所述 power／density／efficiency 目標 | 客戶採用、JEP pass、mixed-source、production BOM、field life、volume 或收入 |
| ROHM SCT4013DLL adopted release | 供應商具名一顆 750 V part 與 AI BBU application position | BBU maker、platform、customer confirmation、qualification method、shipment、penetration 或 financial contribution |
| Delta／ROHM planned PSU adoption | 具名 system maker 主管說明兩種 HVDC architecture、production plan 與 planned Si／SiC use | 截至本輪已 mass ship、特定 JEP、料號 count、customer acceptance、revenue 或 margin |
| OCP PSU／BBU specification | 公開 platform contract 已要求哪些 system fault、reliability、mixed-source 與 quality工作 | 任一 supplier part 已被選中或通過、private customer spec、deployment 或 company economics |

Infineon 的 greater-than-99-percent 是指定 DC-DC stage／reference design 的供應商說法；Delta 的 up-to-98.5-
percent 是公司所述另一個整體 conversion boundary。兩者電壓、topology、冷卻、reference plane 與產品不同，
本文不相減、不排名，也不從差值推估 SiC 貢獻。

## 同耐壓、同電流、同封裝／腳位，只是 mixed-source 的入場券

**同插頭只代表插得進去，不代表開關速度、發熱、雜訊與保護時鐘相同。** onsemi 的
AND90082/D 提供一個很直觀的反例：兩個模組採同一 Q0 package、pin-to-pin compatible，換入 SiC
後，rated current、Qg、gate voltage、RthJC、driver、layout、EMI、熱與量測要求仍不同。這是 Si IGBT
對 SiC、同一供應商的 N＝1 跨技術案例，不是兩家 SiC alternate part 的成績；它只足以否定
「腳位相同就可直接互換」這個捷徑。

AND90103/D 再把原因拆開：跨供應商不能只比 25°C 的 RDS(on)，而要看目標溫度；VGS、VTH、RG、
VDS、Tj、封裝與 PCB 寄生也會分別改變導通、切換、EMI、短路耐受與過衝。因此一顆替代料要進
AI BBU／PSU，至少要逐關留下以下九張證書。

| mixed-source 九關 | 同一題要固定什麼 | 第一個拒絕點 |
|---|---|---|
| 1. 封裝／腳位 | footprint、pin map、Kelvin source、creepage／clearance、固定方式、TIM | 裝不下、pin role 不同或安全距離不合 |
| 2. 靜態 | BVDSS、leakage、RDS(on)、body-diode Vf，並對齊 VGS／ID／hot-cold Tj | 只拿 25°C typical 值跨料排名 |
| 3. 動態 | Qg／Miller、Coss／Qoss／Qrr、Eon／Eoff／Err、dv/dt、di/dt、overshoot／ringing | 測試 circuit、RG、Vbus、current 或 probe 不同 |
| 4. Gate | 正負 VGS、RGon／RGoff、source／sink current、UVLO、dead time、Miller clamp | 必須改 driver 或 gate setting 才能工作 |
| 5. 保護 | threshold、blanking／filter、delay、soft turn-off／clamp、SCWT、fuse／breaker | 偵測太慢、誤跳、energy 或 overshoot 超限 |
| 6. 熱 | RthJC／RthCS、TIM／壓力、Tc／Tj hotspot、steady／transient mission profile | 只看晶片損耗，沒有完整 thermal path |
| 7. EMI／控制 | conducted／radiated、false trigger、control loop、transient、telemetry | 換料後 EMI、穩定度或告警語意失敗 |
| 8. 同板 A／B | 相同 board／revision、量測鏈、環境與 limits，比較 A-production、B-drop-in、必要時 B-tuned | 把不同設定的 pass 說成直接可換 |
| 9. 客戶驗收 | sample／lot、EVT／DVT／PVT、mixed-source build、HALT／ORT／burn-in、PCN／requalification、production BOM | 工程通過但沒有客戶 acceptance |

### 同板 A／B 要保留三個版本：A-production、B-drop-in、B-tuned

`A-production` 是已凍結的量產基準；`B-drop-in` 是不改任何設定直接換入 B 料；`B-tuned` 則把為
B 料修改的 RG、VGS、dead time、DESAT、firmware、heatsink／TIM 或 EMI filter 全部另立 revision。
三者不能共用一個籠統的 pass。共同 header 至少要保存：

`comparison_id、platform／module／board revision、A／B vendor-part-lot-package、driver／sensor／`
`protection／firmware revision、topology、Vbus／load／fsw／temperature／cooling、instrument／probe／`
`bandwidth、test-plan／acceptance revision、sample／lot、raw-file IDs`。

**第一個拒絕邊界**如下：

- B 在凍結的 A-production 設定下任一關失敗，或必須改 gate、保護、韌體、散熱或濾波，就拒絕
  `drop-in interchangeable`；B-tuned 後通過，只能升為「受控設計變更的 alternate candidate」。
- B-tuned 必須使用新 revision 重跑完整矩陣；不能把調校後結果回填到 B-drop-in。
- 前八個工程關卡全過但沒有第九關客戶 mixed-source acceptance，只能稱 engineering-qualified candidate。
- 沒有 production BOM、出貨、field return 與財務分母，不推論供應韌性、議價、份額、收入或毛利。

### 多空小作文先問替代料真正停在哪一關

| 敘事 | 較強版本 | 第一個反證 | 還缺的商業橋 |
|---|---|---|---|
| 偏多 | 同板 B-drop-in 跨 lot 通過九關，讓第二來源能在不改產品設定下進 production BOM | B 只能 B-tuned 才過，或客戶拒絕 mixed-source build | 客戶 sign-off、量產配比、缺料期間供貨、field return 與同期財務 |
| 偏空 | SiC 跨來源差異讓重驗、雙版本 BOM 與 field support 成本吃掉供應韌性 | 凍結設定下跨 lot 結果可重現，PCN／requalification 與 field 指標受控 | 實際 qualification 工時、延誤、失效率、成本與產品毛利分母 |
| 共同底線 | 相同耐壓、電流、封裝或 pinout 只允許進入測試 | 任一九關缺 raw data、共同版本鍵或 acceptance limit 即退件 | 工程可互換仍不等於採購、出貨、供應韌性或財務貢獻 |

本段新增核對 N＝2 份 onsemi 文件，但它們同屬一家公司消息鏈；S16 只是 N＝1 組跨技術
pin-compatible module 案例。實際兩家 SiC、同板 AI BBU／PSU、客戶 acceptance、production、field
與 financial 共同觀測 N＝0。文件不是隨機抽樣，sampling SE／t 不適用；本文不計算換料成功率、
可靠度、SiC 滲透率、供應商份額或投資效果。

## 從元件微秒到整機故障：時間線要閉合

一份可審查的 short-circuit qualification 至少要把以下事件放在同一時間軸：

| 時間欄 | 要保存什麼 | 誰負責 |
|---|---|---|
| t0 故障形成 | fault location、bus voltage、source impedance、available current、temperature | platform／system architect |
| t1 感測到異常 | current／voltage sensor、threshold、bandwidth、filter、tolerance | sensing／controller designer |
| t2 發出關斷 | firmware／hardware path、driver delay、fail-safe state | control／gate-driver owner |
| t3 元件電流下降 | Vgs、Vds、Id、dv/dt／di/dt、overshoot、package／loop inductance | converter／device engineer |
| t4 上游保護協同 | fuse／breaker／eFuse clearing、selectivity、retry／latch | PSU／BBU／rack integrator |
| t5 故障後狀態 | damage check、telemetry、isolation、service／restart、root cause | customer operations／supplier quality |

如果只保存 t3 的 device withstand，卻沒有 t1＋t2 的 detection／shutdown delay，就不能確認保護來得及。
如果只寫「立即關斷」，卻沒有 waveform 與 tolerance，也不能拿去做 alternate-part qualification。

## 10–40 kA 不是 MOSFET 的測試電流：先對齊四個故障參考面

Diablo 400 寫的 10–40 kA，是依 application 而異的系統 available short-circuit fault current；它描述
故障點在指定配電架構下可能向上游取得多大的電流。Infineon 應用手冊中的約 250 A、約 2
microseconds，則屬於一顆 IMW120R045M1、指定 gate supply、400 V DC link、特定 driver 與 51 pF
DESAT capacitor 的 lab waveform。兩組數字都是真的，卻沒有共同物件、位置、阻抗或電路，不能把
40 kA 除以 250 A，命名為「元件要承受 160 倍」，也不能把 2 microseconds 寫成整個 rack 的清除時間。

| 公開數字 | 它所在的參考面 | 原文件真正固定 | 尚缺的交接欄位 |
|---|---|---|---|
| 10–40 kA | rack／distribution 的故障點 | S4 的 system available-fault-current 範圍，且數值依 application 而異 | fault location、source impedance、哪幾個 source 同時供應、支路限流及元件分流 |
| 約 250 A、約 2 microseconds | S14 的單顆 device＋driver lab circuit | 400 V、具名 MOSFET、正 15 V／負 2 V gate supply、51 pF 外加 DESAT capacitor | AI BBU／PSU topology、800 V 條件、量測 tolerance、跨 lot／溫度結果與客戶門檻 |
| 約 1.2 microseconds | 同一供應商實例移除外加 DESAT capacitor | 在該電路內縮短 detection／turn-off time | noise immunity、false trip、layout parasitic 與 production repeatability |
| 3 microseconds device capability | S14 對同一 MOSFET 的 device capability 陳述 | 供應商拿來判斷該 2-microsecond protection example 是否足夠的上限 | 不同 VDS、ID、VGS、Tj、package、driver、重複故障與 system margin |

### DESAT 不是只把旋鈕轉到「最快」

onsemi 的 AND90337/D 把常被拆開看的兩種失敗放在同一條時間線。Blanking 太長，真短路會在
判定前繼續累積能量；太短，正常 turn-on 的高 dv/dt、振鈴與 VDS 尚未下降，可能被誤判成短路。
DESAT threshold 又要在高 Tj 下驗證，因為 RDS(on) 會隨溫度改變。這表示 driver datasheet 上的一個
nominal threshold，不是跨溫度、跨料號與跨 layout 的永久及格線。

故障一旦被偵測，也不能只追求最快 hard turn-off。寄生電感會把快速電流變化轉成電壓過衝，
近似關係為 ΔV ≈ Lstray × |dI／dt|；soft turn-off 能壓低 |dI／dt|，卻讓元件維持導通更久。元件在
故障期間吸收的能量要由 Edevice = ∫VDS(t) × ID(t)dt 的完整波形積分，不能用一個 peak current、
一個 withstand time 或母線電容焦耳數代替。真正的設計目標是讓 false trip、故障能量與關斷過衝
同時留在各自門檻內，不是讓其中一個時間最小。

### 一張可重算的 fault passport 至少要有四個 reference plane

| 參考面 | 最低必要欄位 | 這一面回答什麼 | 不能替下一面回答什麼 |
|---|---|---|---|
| 1. 故障來源 | fault location、bus voltage、source impedance、upstream source、cap／BBU contribution、temperature | 系統在該點可能提供什麼電流與能量 | 不能直接得到每顆 switch 的 ID／VDS 波形 |
| 2. Converter 路徑 | topology、導通元件、current split、busbar／loop inductance、限流與 fuse／breaker branch | 故障如何分到 module、leg 與 device | 不能只靠 schematic 宣稱元件沒超限 |
| 3. Device stress | part／lot／package、VGS、VDS、ID、Tj、waveform bandwidth、energy integral、failure criterion | 單顆元件在指定 circuit 是否留在 qualified envelope | 不能替 sensor、driver 或上游隔離證明及時動作 |
| 4. Protection／clearing | threshold、blanking、filter、driver delay、soft／two-level turn-off、clamp、fuse／breaker clear、retry／latch、post-fault disposition | 從偵測到安全隔離的責任與總時間是否閉合 | 不能由一次 lab pass 推成 field reliability、mixed-source 或財務 |

這四面必須用同一個 platform／board revision 與事件 ID 接起來。若 fault current 是匯流排模擬值、
device waveform 來自另一塊 evaluation board、fuse clearing curve 又屬不同溫度與公差，就只能列為三份
相鄰證據，不能拼成一個「已保護」結果。

### 多空小作文要共用同一張故障護照

| 敘事 | 必須同時看見 | 何時下修或被否定 |
|---|---|---|
| 多方：SiC 與新 driver 擴大 AI 高壓電源安全工作窗 | 具名 BBU／PSU 在正常、transient 與 fault corner 下，固定 part／driver／layout 能同時控制 false trip、device energy、overshoot、clearing 與熱，並通過 mixed-source／customer qualification | 只有 supplier demo；800 V 或高溫下 margin 消失；保護必須大幅降額；客戶沒有量產接受與財務足跡 |
| 空方：保護時鐘太緊，qualification 成本與換料風險吃掉材料優勢 | 同一 system contract 下 SiC 需要更複雜 sensing／clamp、較窄 tolerance、較高降額或更多重驗，且 alternative technology 能以較低全生命週期成本通過 | Production test 顯示跨 lot／溫度仍有充足 margin、alternate-source 可互換、field return 受控，且效率／密度收益留下可重算財務 |

本節的觀察單位是 N＝1 份 OCP system specification、N＝1 份 onsemi application note，以及 N＝1
個 Infineon 固定 device／driver example；它們不是同一產品的三次試驗，也不是隨機市場樣本，因此不估
sampling SE／t 或 failure-rate confidence interval。真實 AI BBU／PSU 的同一 fault location、source
impedance、device waveform、clearing、customer acceptance、production lot、field incident 與財務共同觀測
N＝0；本節不計算 kA／A 比率、可靠度、SiC 滲透率、供應商份額、ASP、收入、毛利或投資效果。

## 用九個欄位建立可重算的 SiC qualification pack

| 記錄欄 | 最低必要內容 | 缺少時的風險 |
|---|---|---|
| 1. Identity | platform、PSU／BBU、board、revision、date、site、owner | 不同產品或版本結果被錯拼 |
| 2. Device manifest | vendor／part／lot／wafer／package／revision、driver、sensor、protection parts | 找不到真正被測的元件組合 |
| 3. Application envelope | Vbus、Id、Tj、dv/dt、switching、dynamic load、fault current／energy、repetition | lab test 無法映射 field condition |
| 4. Standard crosswalk | JEP／IPC／Telcordia／customer procedure、version、section、deviation | 只寫「符合標準」卻無法重跑 |
| 5. Device raw data | circuit、waveform、sample／lot、failure definition、pass／fail、failure analysis | supplier claim 無法獨立審閱 |
| 6. Converter test | topology、gate／control、thermal、EMI、efficiency reference plane、transient／fault matrix | 元件通過後的系統交互作用消失 |
| 7. Reliability process | derating、WCSA、DFMEA、HALT、MTBF model／demonstration、burn-in／ORT | 壽命與風險只剩形容詞 |
| 8. Customer qualification | EVT／DVT／PVT、mixed-source build、shelf／rack、acceptance、PCN／requalification | reference design 被誤寫成 production |
| 9. Commercial trace | customer、production BOM、shipment、field returns、volume／ASP／revenue／margin denominator | 技術題材無法連到公司價值 |

這個 pack 不要求公開客戶機密配方。料號可用受控代碼，但 revision、測試條件、責任人、pass／fail、
change control 與 financial numerator／denominator 必須能讓獨立 reviewer 確認「比較的是同一題」。

## 誰負責，誰不能替別人背書

| 角色 | 應拿出的證據 | 不能替誰背書 |
|---|---|---|
| JEDEC／標準組織 | procedure、circuit、術語、reporting／revision contract | 不能替 application 設 pass line、客戶採用或財務 |
| SiC device supplier | part／lot／package、raw waveform、failure analysis、qualification report | 不能替 driver、converter、rack fault coordination 或 customer acceptance |
| Driver／sensor／control supplier | threshold、delay、tolerance、fail-safe、telemetry | 不能由單一 IC spec 宣稱整機 short-circuit safe |
| BBU／PSU integrator | topology、thermal、derating、DFMEA、fault matrix、mixed-source、NPI result | 不能用 reference design 代替 production customer sign-off |
| Rack／platform owner | application envelope、system fault、interoperability、acceptance、service action | 不能由 private requirement 推成全產業共同標準 |
| Hyperscaler／operator | deployment、field incident、maintenance、return／requalification data | 不能只用場域案例替所有產品壽命背書 |
| 投資研究 | 對齊同一 part、module、revision、customer、shipment 與 company denominator | 不能用標準發布、adoption release 或效率數字補出份額與獲利 |

## 台達與 power／powersupply 族群應該怎麼讀

台達已經有三種不同層級的公開證據：公司董事長報告具名多個 800 V power products；ROHM／Delta 對談
給出 planned SiC PSU adoption 與 production timing；品牌案例又有 named-site SiC SST deployment。這足以讓
2308 成為 powersupply 族群的具名研究入口，而不是只有抽象產業映射。

但三條線沒有完成同一個 BBU／PSU 的 JEP crosswalk、production BOM、customer acceptance 與 financial
numerator。SST deployment 也不能搬到 BBU／PSU。故本文把台達畫在 planned／capability stage，不畫到
JEP-qualified、shipment 或 financial attribution。

power 族群則保留為 device qualification 搜尋路由。本輪沒有任何 universe 功率元件公司，由平台與公司
雙向確認同一 SiC part 已依 JEP203／JEP204 及 system matrix 完成 AI BBU／PSU qualification。具備 SiC
wafer／device capability、一般 server exposure 或其他 800 V 假說都不能替這個缺口背書。

## 來源與證據邊界

- [JEDEC JEP203 document search](https://www.jedec.org/document_search?search_api_views_fulltext=JEP203) 與 [JEP204 document search](https://www.jedec.org/document_search?search_api_views_fulltext=JEP204)（官方標題、日期、abstract 與 committee；全文需登入）。
- [JEDEC release](https://www.businesswire.com/news/home/20260603176123/en/JEDEC-Releases-New-SiC-Guidelines-to-Improve-Reliability-and-Evaluation-in-Power-Electronics)（short-circuit 與 stress-framework 發布邊界）。
- [OCP Diablo 400 v0.7.0](https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf)（rack／BBU／dynamic-load／fault-current system envelope）。
- [Open Rack V3 HPR V2 12 kW PSU Rev 1.0.0](https://www.opencompute.org/documents/open-rack-v3-hpr-v2-12kw-psu-module-spec-v1-0-0-pdf)（short circuit、derating、DFMEA、MTBF、HALT、mixed-source 與 NPI）。
- [Open Rack V3 48 V BBU Rev 1.4](https://www.opencompute.org/documents/open-rack-v3-bbu-module-spec-1-4-pdf)（歷史 BBU system qualification 骨架與 Delta contributor／supplier）。
- [Infineon 24 kW HV BBU reference design](https://www.infineon.com/technology-news/2026/infpss202606-093)（單一供應商 SiC design／BOM）。
- [ROHM SCT4013DLL BBU adoption release](https://www.rohm.com/news-detail?defaultGroupId=false&news-title=2026-06-03_news_sic-mosfet)（supplier-reported N=1 adoption）。
- [ROHM／Delta HVDC dialogue](https://www.rohm.com/ir/dialogue/ai-server)（management planned production／adoption；頁面未標可定位發布日）。
- [Delta 2025 Chairman Statement](https://www.deltaww.com/en-US/investors/chairman-statement)（公司高壓 power product architecture）。
- [Delta Chindata／Meituan SST case](https://brandnews.deltaww.com/en/SpecialDetail/12748)（相鄰 SiC system deployment，不是 BBU／PSU JEP qualification）。
- [onsemi AND90337/D](https://www.onsemi.com/download/application-notes/pdf/and90337-d.pdf)（April 2025 Rev.0；DESAT threshold／blanking、soft turn-off、clamping 與 fault-energy／overshoot trade-off；motor power module 脈絡，不是 AI platform qualification）。
- [Infineon AN-2022-03 V1.2](https://www.infineon.com/assets/row/public/documents/60/42/infineon-1ed332xmc12n-technical-description-applicationnotes-en.pdf?fileId=8ac78c8c7e7124d1017ef7883db65158)（第 18–19 頁的 N＝1 固定 400 V、具名 device／driver DESAT example；不是跨元件或客戶及格線）。
- [onsemi AND90103/D Rev.3](https://www.onsemi.com/download/application-notes/pdf/and90103-d.pdf)（跨供應商 hot RDS(on)、gate、動態、EMI、SCWT 與 package／PCB 寄生邊界）。
- [onsemi AND90082/D Rev.0](https://www.onsemi.com/pub/Collateral/AND90082-D.PDF)（同 Q0 package、pin-to-pin compatible 仍須重做 driver、layout、EMI、thermal 與量測的反例）。

本輪沒有做跨公司的效率、功率密度、MTBF 或壽命排名。Infineon 與 ROHM 各是 N=1 supplier evidence；
OCP N=3 是具名文件 census；Delta 數字是不同產品與 reference plane 的公司揭露。這些都不是獨立同分布的
市場抽樣，故不估 SE／t。新增 onsemi 應用手冊與 Infineon device／driver example 也只提供不同責任面的
工程證據，不是同一 AI 產品的重複實驗。OCP 的 90% confidence 是規格文字，不是本文的統計信賴區間。

## 影響路由

<!-- impact
group_id: power
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-15
rationale: JEP203／JEP204 與 AI power fault envelope 讓 SiC device、driver、sensor、package 與 qualification data 成為 power 族群的明確搜尋路由
evidence_boundary: 沒有 universe 功率元件公司由買方與公司雙向對上同一 AI BBU／PSU part、JEP／system qualification、production BOM、出貨或財務
-->

<!-- impact
group_id: powersupply
stock_ids: 2308
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-15
rationale: 台達具名高壓產品、planned ROHM Si／SiC PSU adoption、OCP BBU contribution／supplier 與相鄰 SST deployment，形成 BBU／PSU integrator 的可定位研究入口
evidence_boundary: planning、產品能力與 SST deployment 不等於 JEP203／JEP204 已進 platform qualification、BBU／PSU customer acceptance、量產出貨或可分辨收入毛利
-->

## 持續驗證清單

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C11,C12
metric: JEP203／JEP204 全文的 test circuit、procedure、sample、failure criterion、reporting field 與 revision
source_ids: S1,S2,S3
watch_source_ids: S1,S2
frequency: monthly
frequency_detail: 每月查 JEDEC document index／revision；取得合法全文後只新增可定位 procedure crosswalk，不以二手摘要回填
next_check: 2026-09-15
trigger: JEDEC 公開新版、corrigendum、application report 或可合法審閱全文，且能逐項定位 short-circuit／stress procedure 與 reporting contract
invalidation: 文件範圍、test object 或 procedure 在正式內容中與公開摘要顯著不同，或 guideline 明示不適用本題元件／application
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C2,C3,C4,C5,C12
metric: AI BBU／PSU platform qualification 對 JEP203／JEP204 的 normative citation、revision diff、device-to-system crosswalk 與 pass report
source_ids: S4,S5,S6
watch_source_ids: S12
frequency: event_driven
frequency_detail: OCP、GPU vendor 或 hyperscaler 發布 power-spec 新版時先做 exact-token diff，再定位 normative section、test object、sample、threshold 與 system action
next_check: 2026-09-15
trigger: 固定平台 revision 明文引用 JEP203／JEP204，並公開 application waveform、device test、protection timing、derating、DFMEA、mixed-source 與 acceptance 的逐項對照
invalidation: 新版仍只有 generic reliability／short-circuit wording、只引用 IPC／Telcordia，或 JEP 只出現在 bibliography 而未改 requirement／test／acceptance
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C6,C7,C8,C9,C10,C13
metric: universe 公司具名 SiC BBU／PSU part、customer qualification、production BOM、shipment、field return 與可重算財務貢獻
source_ids: S7,S8,S9,S10,S11
watch_source_ids: S8,S9,S10,S11
frequency: monthly
frequency_detail: 每月核對台達與 power 族群 MOPS／IR、platform／customer release；只有兩端對上同一 part、module、revision 與 period 才升級
next_check: 2026-09-15
trigger: 買方與台灣公司雙向確認相同 BBU／PSU、SiC part、JEP／system qualification、production shipment，且可由公司總收入／毛利分母重算題材貢獻
invalidation: 只有 roadmap、reference design、supplier adoption、SST／EV 等相鄰 application，或 production plan 延後且沒有 customer acceptance／financial numerator
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C14,C15,C16
metric: AI BBU／PSU 同一故障事件的 system available current、source impedance、converter current path、device raw waveform、DESAT／driver timing、clamp／fuse-breaker clearing 與 post-fault disposition crosswalk
source_ids: S4,S13,S14
watch_source_ids: S12
frequency: event_driven
frequency_detail: OCP、平台商、BBU／PSU integrator 或 device／driver supplier 發布 fault test、qualification report 或規格 revision 時，以同一 platform／board revision 與 event ID 逐面核對
next_check: 2026-09-15
trigger: 具名 production AI BBU／PSU 公開 fault location、source impedance、全部 source contribution、VDS／ID／VGS／Tj raw waveform、threshold／blanking／delay、overshoot／energy、clearing sequence、tolerance、pass／fail 與 customer acceptance
invalidation: 數字仍來自不同 rack、evaluation board、voltage、topology 或 temperature；只有 supplier lab example、simulation 或 generic protection wording時，不建立 system-safe、mixed-source、field reliability 或財務結論
-->

## 下一個可證明／否定的節點

- JEP203／JEP204 全文是否提供足以固定 circuit、waveform、sample、failure criterion 與 report field 的可重算契約。
- OCP、GPU vendor 或 hyperscaler 的下一版 BBU／PSU qualification 是否首次明文引用兩份 JEP，而不只寫 generic short-circuit／reliability。
- 同一高壓 BBU／PSU 是否公開 device raw data、converter fault timeline、derating／DFMEA、mixed-source EVT／DVT／PVT 與 customer acceptance。
- ROHM 的 adopted SCT4013DLL 是否由具名 BBU maker／customer confirmation，並對上 platform revision、shipment 與 volume。
- Delta planned Q2–Q3 2026 production 是否轉為具名產品出貨，並把 SiC part、JEP mapping、customer qualification 與 financial denominator 接起。
- 下一份 AI power fault report 能否把 rack available current、source impedance、converter current path、device raw waveform、DESAT／driver timing、fuse／breaker clearing 與 post-fault disposition 用同一 event ID 接起；缺任一 reference plane 就不把 kA、A 與 microseconds 拼成同一及格線。
- 若平台長期不引用 JEP，或只把它留在 supplier quality appendix 而不改 system threshold，C12 維持未證實，研究框架應視 JEP 為 device-level harmonization 而非 AI power demand catalyst。
- 若 mixed-source 結果顯示 Si、SiC、GaN 或不同 SiC supplier 都可在相同 system contract 通過，應下修任何材料獨占、單一供應商份額與 pricing-power 推論。
