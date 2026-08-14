# 曝光次數少了，晶片不一定更便宜：先看圖形怎麼印、哪些成本又冒出來

<!-- research_topic
topic_id: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-04-22
last_reviewed_at: 2026-08-12
review_due: 2026-10-01
source_type: mixed
publisher: ASML
publisher_domain: asml.com
canonical_url: https://ourbrand.asml.com/asset/d5e933d7-78d0-406c-aed7-a46626e63381/2026_-AGM-_presentation.pdf
source_chain_id: high-na-euv-insertion-20260802
stock_ids:
group_ids: semiequip,material
trigger_type: lithography_tool_process_and_hvm_insertion
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C5
base_confidence: medium
confidence_basis: ASML、imec 與 Intel 一手來源可交叉確認工具出貨、客戶端運轉、半視場與拼接、測試結構電性結果、整合元件展示、產品晶圓測試與資格／插入時程；但完整產品層製程視窗、2026 年底 HVM readiness、2027 至 2028 客戶節點插入、台灣供應商角色與財務貢獻仍待驗證
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: primary_source_high_na_scan
evidence: source_chain:high-na-euv-insertion-20260802
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_tool_shipment_operation_process_qualification_product_wafer_and_hvm_insertion
evidence: sources:S1,S2,S3,S4
-->

<!-- research_source
source_id: S1
role: company_filing
source_kind: document
publisher: ASML
title: ASML 2026 Annual General Meeting Presentation
published_at: 2026-04-22
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ourbrand.asml.com/asset/d5e933d7-78d0-406c-aed7-a46626e63381/2026_-AGM-_presentation.pdf
locator: PDF p.15（檔案頁碼標示 Page 15）；截至 2025 年底八台 High-NA 出貨、六台運轉、首台 EXE:5200B 在客戶端，並以 2026 年底 HVM requirements、2027–2028 insertion 為目標
limitation: ASML 的出貨與時程證實工具及平台進度，不證明客戶製程已 qualification、量產良率、節點採用層數或供應商財務曝險
independence_group: asml
-->

<!-- research_source
source_id: S2
role: other_primary
source_kind: document
publisher: imec
title: Imec Receives the World Most Advanced High NA EUV System
published_at: 2026-03-18
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.imec-int.com/en/press/imec-receives-worlds-most-advanced-high-na-euv-system
locator: 正文 tool arrival、ecosystem integration 與最後一段；imec 預期 EXE:5200 於 2026Q4 fully qualified
limitation: imec 是研發與 pilot 環境；工具到廠及其 qualification 目標不等於任何晶圓代工客戶的 HVM insertion
independence_group: imec
-->

<!-- research_source
source_id: S3
role: company_filing
source_kind: document
publisher: ASML
title: ASML Q1 2026 Investor Call Transcript
published_at: 2026-04-15
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ourbrand.asml.com/asset/8e1f7393-33dd-4737-a436-cfe1b68cc577/2026_04_15-ASML-Transcript-investor-call-Q1-2026.pdf
locator: PDF p.4（文件頁標示 Page 4 of 5）；High-NA 已處理逾 50 萬片 wafer、availability 逾 80%，客戶開始在 product wafers 測試，並提到 resist 進度
limitation: 數字由 ASML 揭露且沒有逐客戶、節點、層數、良率或成本分母；product-wafer testing 不等於 HVM
independence_group: asml
-->

<!-- research_source
source_id: S4
role: competitor_primary
source_kind: document
publisher: Intel
title: Press Kit High NA EUV at Intel
published_at: 2024-04-18
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://newsroom.intel.com/press-kit/intel-high-na-euv
locator: press kit 首段與安裝說明；Intel 完成首台商用 High-NA 系統安裝並開始 calibration
limitation: 2024 安裝是早期導入基線，不證明 2026 製程資格、14A 量產插入、客戶產品或良率
independence_group: intel
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: living_index
publisher: ASML
title: ASML Press Releases
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.asml.com/en/news/press-releases
locator: 2026-08-02 查得 ASML 系統、季度結果與 High-NA 後續公告入口
limitation: 動態索引只供發現新附件；不能自行證明 HVM requirements、客戶 insertion 或收入
independence_group: asml
-->

<!-- research_source
source_id: S6
role: other_primary
source_kind: living_index
publisher: imec
title: Imec Press Releases
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.imec-int.com/en/press
locator: 2026-08-02 查得 High-NA qualification、patterning、resist、mask 與 metrology 更新入口
limitation: 新聞索引不等於 qualification 完成；每個新里程碑仍須區分 test vehicle、pilot 與 customer HVM
independence_group: imec
-->

<!-- research_source
source_id: S7
role: competitor_primary
source_kind: living_index
publisher: Intel Foundry
title: Intel Foundry Process Technologies
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.intel.com/content/www/us/en/foundry/process.html
locator: 2026-08-02 查得 Intel 14A、18A 與後續製程公開更新入口
limitation: 動態 process page 與 roadmap 不能替代 High-NA 實際使用層、qualification、量產良率或客戶產品文件
independence_group: intel
-->

<!-- research_source
source_id: S8
role: company_release
source_kind: document
publisher: ASML
title: 5 things you should know about High NA EUV lithography
published_at: 2024-01-25
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.asml.com/en/company/stories/2024/5-things-high-na-euv
locator: 正文 High-NA optics 與 productivity 段落；0.55 NA、單方向四倍與另一方向八倍的 anamorphic optics、半視場、每片兩次曝光及每小時產出路線
limitation: ASML 是設備商；光學設計、速度目標與減少多重圖形化的說明不證明客戶產品層的拼接、良率、量產成本或 HVM
independence_group: asml
-->

<!-- research_source
source_id: S9
role: other_primary
source_kind: document
publisher: imec
title: Imec demonstrates readiness of High NA EUV patterning ecosystem
published_at: 2024-02-26
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.imec-int.com/en/press/imec-demonstrates-readiness-high-na-euv-patterning-ecosystem
locator: 正文 half field、at-resolution stitching、MOR／underlayer／mask／OPC、dose、depth of focus 與 stochastic defect 段落
limitation: 研發圖形與特定材料條件只證明受測視窗；個別劑量或均勻度改善不能外推到所有圖形、完整產品、蝕刻後電性、產能或 HVM
independence_group: imec
-->

<!-- research_source
source_id: S10
role: other_primary
source_kind: document
publisher: imec
title: Imec demonstrates electrical yield of 20nm pitch metal lines obtained with High NA EUV single exposure
published_at: 2025-02-24
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.imec-int.com/en/press/imec-demonstrates-electrical-yield-20nm-pitch-metal-lines-obtained-high-na-euv-single
locator: 正文 20nm pitch、metallized test structures、serpentine／fork-fork 與 over 90 percent electrical yield 段落
limitation: 兩類測試結構的初步電性驗證不是完整產品層、全部圖形族、長期製程能力、客戶 qualification 或 HVM 良率
independence_group: imec
-->

<!-- research_source
source_id: S11
role: other_primary
source_kind: document
publisher: imec
title: Imec unlocks lever for EUV dose reduction with oxygen injection during metal-oxide resist post-exposure bake
published_at: 2026-02-25
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.imec-int.com/en/press/imec-unlocks-lever-euv-dose-reduction-oxygen-injection-during-metal-oxide-resist-post
locator: 正文 oxygen-controlled post-exposure bake、50 percent versus 21 percent oxygen、15 to 20 percent photo-speed improvement 與 preliminary mechanism 段落
limitation: 研究工具與受測光阻條件的感光速度結果尚未證明量產設備整合、跨批次穩定、缺陷／良率、產能或總成本
independence_group: imec
-->

<!-- research_source
source_id: S12
role: other_primary
source_kind: document
publisher: imec
title: World-first: imec presents quantum dot qubit device using High NA EUV lithography
published_at: 2026-05-19
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.imec-int.com/en/press/world-first-imec-presents-quantum-dot-qubit-device-using-high-na-euv-lithography
locator: 正文 functional quantum dot qubit network、approximately 6nm gaps、300mm fab-compatible flow 與 reproducibility 說明
limitation: 功能性研究元件把證據推進到整合裝置，不等於邏輯或記憶體客戶產品層、量產樣本、長期良率、成本或 HVM
independence_group: imec
-->

<!-- research_source
source_id: S13
role: competitor_primary
source_kind: document
publisher: Intel Foundry
title: Delivering Technologies to Power the AI Era - Intel Foundry at SPIE 2026
published_at: 2026-02-20
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://community.intel.com/t5/Blogs/Intel-Foundry/Systems-Foundry-for-the-AI-Era/Delivering-Technologies-to-Power-the-AI-Era-Intel-Foundry-at/post/1737961/jump-to/first-unread-message
locator: High-NA direct-print、half-field seam stitching、21nm pitch、roughness／defectivity 與 resist／mask co-optimization 段落
limitation: Intel 的會議技術摘要支持客戶端研發項目，不提供完整產品層、製程能力分布、qualification、量產層數、HVM 良率或成本
independence_group: intel
-->

<!-- research_source
source_id: S14
role: company_release
source_kind: living_index
publisher: ASML
title: The Rayleigh criterion for resolution
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.asml.com/en/technology/lithography-principles/rayleigh-criterion
locator: 現行正文 Rayleigh criterion equation 段落；CD＝k1×波長÷NA，並分別定義 critical dimension、波長、數值孔徑與製程相依的 k1
limitation: ASML 的教育頁固定光學關係與名詞，不提供 High-NA 產品層的焦深、視場拼接、缺陷、良率、合格產出或成本；頁面沒有可核對的發布日
independence_group: asml
-->

<!-- research_source
source_id: S15
role: other_primary
source_kind: document
publisher: EUV Litho, Inc.
title: 2023 EUVL Workshop & Supplier Showcase Abstract Book
published_at: 2023-06-03
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://euvlitho.com/2023/2023%20EUVL%20Workshop%20and%20Supplier%20Showcase%20Abstract%20Book.pdf
locator: PDF 檔案第36頁（頁尾 program P46）University of Hyogo 受邀摘要；計算 0.55 NA 的 wafer depth of focus 為 45nm、約為 0.33 NA 的三分之一，並指出薄光阻與 line-width roughness 邊界
limitation: 2023-06-03 是官方 agenda 所列研討會起始日，不主張為摘要集實際上線日；單頁受邀摘要與研究計算不是產品製程視窗、完整論文、客戶 qualification、HVM 良率或成本證據
independence_group: university-of-hyogo-euvl-workshop
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: ASML 表示截至 2025 年底已向數個客戶出貨八台 High-NA 系統，其中六台已運轉，並包含首台第二代 EXE:5200B；公司目標是 2026 年底滿足 HVM requirements、2027 至 2028 年由客戶插入
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-04-22
basis: S1 p.15 直接列出出貨、運轉、機型與兩個目標時段
boundary: 出貨與運轉不是 process qualification；HVM requirement 目標與 customer insertion 也不是已完成事件
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
claim: imec 於 2026-03-18 公告 EXE:5200 已抵達 Leuven cleanroom，並預期該系統在 2026Q4 fully qualified
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-03-18
basis: S2 的到廠與 qualification 時程段落直接支持
boundary: imec qualification 是研發環境里程碑，不等於晶圓代工客戶的產品節點或量產良率
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
claim: ASML 在 2026Q1 投資人資料表示 High-NA 平台已處理超過 50 萬片 wafer、availability 超過 80%，且客戶開始在 product wafers 測試
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-04-15
basis: S3 p.4 直接列出累計 wafer、availability 與 product wafer testing
boundary: 聚合平台數字沒有逐客戶與量產分母，不能改寫成任何特定節點已 qualification 或達 HVM
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
claim: Intel 在 2024-04-18 公開資料中表示已完成首台商用 High-NA EUV 系統安裝並開始 calibration
supporting_source_ids: S4
contrary_source_ids:
as_of: 2024-04-18
basis: S4 press kit 首段與圖片說明直接支持安裝及 calibration
boundary: 這是早期客戶導入基線，不證明 2026 製程資格、14A HVM 或外部 foundry 客戶採用
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
claim: High-NA EUV 已跨過只有單機 prototype 的階段，進入多台客戶端運轉、研發資格與 product-wafer testing；但在證據階梯上仍位於客戶 HVM insertion 之前，不能用八台出貨、50 萬片處理量或 imec 到廠替 2027–2028 量產節點提前畢業
supporting_source_ids: S1,S2,S3,S4,S12
contrary_source_ids:
as_of: 2026-08-02
basis: S1 提供 fleet 與 insertion 時程，S2 提供 imec qualification 目標，S3 提供平台與 product-wafer testing，S4 提供首個客戶安裝基線
boundary: 不推估 ASML 訂單、客戶節點份額、每片成本、台灣設備／材料用量、公司收入或市場是否已反映
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
claim: ASML 已在 2026 年底達成全部 High-NA HVM requirements，或任一客戶已完成 2027–2028 量產節點 insertion
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: S1 與 S2 都把這些節點放在未來目標，S3 只到 product-wafer testing；本輪沒有完成文件
boundary: 未到目標日期與沒有完成證據不是反證，但成熟度只能停在 testing／qualification plan
verification_needed: ASML、imec 與客戶端發布 qualification、HVM readiness、實際節點／層數、良率及量產產品證據
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: unverified
status: active
claim: universe 內半導體設備或材料公司已因 High-NA EUV 取得具名 qualification、訂單、收入、毛利或資本支出貢獻
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: ASML、imec 與 Intel 來源沒有具名 universe 公司，也沒有平台端與供應商端的財務雙向核對
boundary: 能服務先進製程、EUV、光阻、清洗、量測或耗材，只形成搜尋入口，不構成 High-NA 曝險
verification_needed: 客戶或平台端具名 qualification，加上台灣公司揭露產品、出貨與可辨識財務貢獻
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: inference
status: active
claim: High-NA 的量產準備度是 scanner、resist、mask、pattern transfer、metrology 與 process stability 的共同結果，而不是只由掃描機數量決定
supporting_source_ids: S2,S3,S8,S9,S10,S11,S12,S13
contrary_source_ids:
as_of: 2026-08-02
basis: S2 明列 patterning、metrology、materials 與 resist／mask ecosystem，S3 把 resist 進度與 product-wafer testing 連到平台成熟
boundary: 這個依賴鏈不證明任一材料或設備供應商已取得客戶資格、份額、訂單或財務貢獻
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
claim: ASML 說明 High-NA 使用一方向四倍、另一方向八倍的非等向縮放光學，因此曝光視場縮為一半、每片晶圓要以兩個半場完成；imec 另在研究環境展示解析度下的半場拼接
supporting_source_ids: S8,S9
contrary_source_ids:
as_of: 2024-02-26
basis: S8 直接說明 anamorphic 4x／8x、half field 與 two exposures per wafer，S9 直接描述 half field 與 at-resolution stitching demonstration
boundary: 光學架構與研究拼接成立不等於所有產品版圖都已處理接縫、跨場對準、長期漂移、良率或產能
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
claim: imec 於 2025-02-24 報告以 High-NA 單次曝光製作 20nm pitch 金屬化測試結構，並在用來檢查斷路與橋接的 serpentine 與 fork-fork 結構上取得超過 90 percent 的電性良率
supporting_source_ids: S10
contrary_source_ids:
as_of: 2025-02-24
basis: S10 直接列出圖形間距、金屬化、兩類電性測試結構、對應失效模式與報告良率
boundary: 這是兩類測試結構的初步結果；沒有完整產品圖形族、樣本分布、長期製程能力、客戶 qualification 或 HVM 分母
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
claim: imec 於 2026-02-25 報告在研究用烘烤工具中把金屬氧化物光阻曝光後烘烤的氧濃度由 21 percent 控制到 50 percent 時，受測條件的感光速度提升 15 to 20 percent
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-02-25
basis: S11 直接列出氧濃度比較、研究工具與 photo-speed improvement 區間
boundary: 機制仍屬初步研究，也沒有量產烘烤設備、跨批次缺陷、產品良率、每小時產出或每顆合格晶片成本
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
claim: imec 於 2026-05-19 公布以 High-NA 圖形化製作功能性量子點量子位元網路，報告約 6nm 間隙並把流程描述為與 300mm 晶圓廠相容且可重現
supporting_source_ids: S12
contrary_source_ids:
as_of: 2026-05-19
basis: S12 直接描述 functional device、approximately 6nm gaps、300mm fab-compatible flow 與 reproducibility
boundary: 單一研究裝置類別不等於邏輯或記憶體客戶產品層，也沒有 HVM 樣本、長期良率、產出或成本
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
claim: Intel Foundry 於 2026-02-20 把半視場接縫拼接列為 High-NA 客戶端挑戰，並說明 21nm pitch direct-print 的線邊粗糙度與缺陷持續改善、光阻與光罩仍在共同最佳化
supporting_source_ids: S13
contrary_source_ids:
as_of: 2026-02-20
basis: S13 的 High-NA 段落直接描述 half-field seam stitching、21nm pitch direct print、roughness／defectivity improvement 與 continued resist／mask co-optimization
boundary: 技術會議摘要沒有完整產品層、跨場統計、製程能力分布、qualification、量產層數、HVM 良率或成本
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C14
label: inference
status: active
claim: High-NA 的製程視窗必須當成一份耦合契約驗證：半視場與拼接、曝光劑量與焦距、光阻與烘烤、光罩與修正、圖形轉移、隨機缺陷、電性結構、設備產出及變更沿革要綁在同一受測版本；任何單一解析度、劑量、良率或元件展示都不能替整份契約畢業
supporting_source_ids: S8,S9,S10,S11,S12,S13
contrary_source_ids:
as_of: 2026-08-12
basis: S8 至 S13 分別揭露半視場、拼接、焦深／材料、電性測試結構、烘烤條件、整合元件與客戶端共同最佳化，顯示各結果使用不同受測物與條件，必須保留版本與邊界
boundary: 這是研究方法與證據排序，不是任何客戶已完成製程資格、任何供應商已取得訂單，亦不估算市場規模、收入、毛利或估值
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
claim: ASML 的 Rayleigh 教育頁把臨界尺寸寫成 CD＝k1×波長÷NA，並說明 k1 取決於晶片製造製程；因此只有在波長與 k1 等比較條件固定時，較大 NA 才能單獨換算成較小的理論臨界尺寸
supporting_source_ids: S14
contrary_source_ids:
as_of: 2026-08-14
basis: S14 正文直接給出公式與 CD、波長、NA、k1 定義，並明示 k1 是製程相依係數
boundary: Rayleigh 關係是解析度的一階光學框架，不給焦深、視場、光罩、光阻、隨機缺陷、圖形轉移、設備產出、產品良率或成本
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
claim: University of Hyogo 在 2023 年極紫外光微影研討會受邀摘要中報告 0.55 NA 的 wafer depth of focus 計算值為 45nm、約為 0.33 NA 的三分之一，並指出因此需要薄光阻，而光阻越薄時 line-width roughness 會惡化
supporting_source_ids: S15
contrary_source_ids:
as_of: 2023-06-03
basis: S15 PDF 檔案第36頁（頁尾 program P46）直接列出 45nm、one third、thin resist film 與 thickness thinner 時 LWR worsen
boundary: 這是研討會受邀摘要中的研究計算與材料問題陳述，不是 EXE 客戶產品層的實測焦深分布、量產 recipe、跨批次重現、良率或成本
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C17
label: inference
status: active
claim: High-NA 比較至少要把解析度、焦深、曝光視場與合格產出分成四本帳，再以同一產品層的光罩、膜堆、光阻、焦距劑量、接縫、缺陷、電性與生產分母接回成本；NA 或理論 CD 任一欄改善，都不能單獨替實際良率與經濟性畢業
supporting_source_ids: S8,S14,S15
contrary_source_ids:
as_of: 2026-08-14
basis: S14 固定 CD 關係，S15 提供焦深與薄光阻粗糙度邊界，S8 另固定半視場、兩倍曝光次數與更快 stage 的產能補償路徑，三者回答不同帳本
boundary: 這是研究中心的比較方法與證據契約；N＝2 假想光學設定及曝光指數只是確定性教材，不是設備、晶圓、產品、run、抽樣結果、客戶 qualification、財務效果或投資結論
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C5,C6,C8
metric: EXE:5200 qualification、availability、product wafer、HVM requirements 與 ecosystem readiness
source_ids: S1,S2,S3
watch_source_ids: S5,S6
frequency: monthly
frequency_detail: 每月檢查 ASML 與 imec；2026Q4 起提高為每次正式公告即重審
next_check: 2026-10-01
trigger: imec 公告 fully qualified、ASML 確認 HVM requirements 達成，或客戶披露產品晶圓層數、良率與 process window
invalidation: qualification 延後、availability／throughput 未達客戶要求、resist／mask／metrology 阻礙量產，或客戶維持 Low-NA multi-patterning
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C4,C5,C6,C7
metric: 客戶節點 insertion、量產產品與台灣設備／材料財務映射
source_ids: S1,S4
watch_source_ids: S5,S7
frequency: quarterly
frequency_detail: 追蹤 ASML 季報與 Intel／其他客戶 process roadmap；公司線須等客戶與供應商雙向文件
next_check: 2026-10-15
trigger: 客戶確認 High-NA 實際節點、層數、產品與 HVM，且供應商揭露 qualification、出貨及收入
invalidation: 客戶 insertion 延至 2029 以後、只在 R&D 使用，或 Low-NA／多重圖形化在成本與良率上持續勝出
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C5,C8,C9,C10,C11,C12,C13,C14
metric: 同一產品層的半視場拼接、劑量／焦距視窗、隨機缺陷、圖形轉移、電性良率、產出與變更後重驗
source_ids: S8,S9,S10,S11,S12,S13
watch_source_ids: S5,S6,S7
frequency: monthly
frequency_detail: 每月檢查 ASML、imec 與 Intel；出現客戶產品層或 full-field qualification 文件時立即重審
next_check: 2026-10-01
trigger: 同一客戶產品層公開版本化的 field／stitch、dose／focus、材料與烘烤、缺陷與電性、throughput／availability、變更沿革及 HVM 結果
invalidation: 拼接或焦深使產品視窗不足、降劑量放大隨機缺陷、圖形轉移後電性失敗、變更後無法重現，或客戶延後／縮減插入層
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
reason: editorial_plain_language_wave6_compute_interconnect_learning_no_conclusion_change
evidence: editorial:plain_language_wave6
-->

<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave100_high_na_five_positions_five_cost_lenses_roles_and_six_gate_ladder
evidence: editorial:reader_layer_only_no_claim_source_monitor_or_impact_change
-->

<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_anamorphic_field_stitching_dose_yield_and_electrical_evidence_ladder_without_hvm_upgrade
evidence: sources:S8,S9,S10,S11,S12,S13
-->

<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_na_resolution_depth_of_focus_and_half_field_passport_without_thesis_clock_refresh
evidence: sources:S8,S14,S15
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **晶圓**：用來製造許多晶片的圓形薄片；同一片上會重複進行曝光、顯影、蝕刻、沉積與量測。
- **微影**：把設計好的微小圖形複製到晶圓表面的製程，像替後續加工畫出位置與邊界。
- **曝光**：用光把光罩圖形投到晶圓表面的光阻上；曝光完成仍要顯影與後續加工才能留下實體結構。
- **光罩**：承載某一層晶片圖形的模板；圖形正確不等於曝光後的晶圓一定沒有缺陷。
- **光阻**：塗在晶圓上的感光材料；受光後的化學變化讓指定區域能在顯影時被留下或移除。
- **顯影**：依光阻受光結果洗出圖形；顯影完成仍要確認線寬、缺陷與圖形是否可轉移。
- **圖形轉移**：把光阻上的暫時圖形交給蝕刻或其他加工，變成晶圓上的實體結構。
- **蝕刻**：依圖形選擇性移除材料；曝光印得出來不等於蝕刻後仍能維持相同尺寸與良率。
- **量測**：量出線寬、位置、厚度與疊對等數值，用來判斷製程是否落在可接受範圍。
- **檢查**：尋找顆粒、刮傷、圖形破損與其他缺陷；量測與檢查常一起決定問題能否被及早發現。
- **缺陷**：可能讓圖形或晶片功能失敗的異常；缺陷數量要放回晶圓面積、層數與產品良率判讀。
- **線寬**：晶圓上某條線或間距的尺寸；能印得更細不等於整個產品都會使用相同尺寸。
- **解析度**：曝光系統分開細小圖形的能力；解析度提升只是製程成立的一項條件。
- **臨界尺寸**：指定光學與製程條件下可印出的最小圖形尺度，英文常寫 CD；它不是產品節點名稱或最終晶片良率。
- **Rayleigh 準則**：用波長、數值孔徑與製程係數連接臨界尺寸的一階光學關係；公式結果不是量產實測。
- **k1 係數**：Rayleigh 關係中的製程相依係數；光罩、照明、材料與圖形化方法不同時，不能假設 k1 相同。
- **數值孔徑**：描述光學系統收集與聚焦光線能力的指標；提高它可改善解析度，也會改變光罩、光阻與製程整合要求。
- **非等向縮放光學**：兩個方向使用不同縮小倍率的光學設計，英文常寫 anamorphic optics；High-NA 因此改變單次曝光可覆蓋的面積。
- **半視場**：單次曝光只覆蓋現行完整視場的一半；較大的產品版圖可能需要把兩個半場接起來。
- **視場拼接**：把相鄰曝光區域在接縫處正確銜接；拼得出測試線不等於所有產品圖形都通過長期穩定驗證。
- **焦深**：晶圓高度在多大範圍內仍能保持合格圖形；焦深縮小時，薄膜厚度、表面起伏與設備控制會更敏感。
- **焦距預算**：把設備控制、晶圓起伏、膜厚、量測誤差與其他高度變動分配到可用焦深內；總和超出視窗時圖形可能失效。
- **曝光劑量**：光阻接收的曝光能量；劑量較低可能提高速度，卻必須一起檢查隨機缺陷與良率。
- **EUV**：極紫外光微影，用很短波長的光印製先進晶片圖形；它只是完整製程中的一段。
- **High-NA**：把極紫外光系統的數值孔徑提高到 0.55 的方案；目標是一次印出更細圖形，但仍要驗證良率、產出與成本。
- **Low-NA**：目前較低數值孔徑的極紫外光平台；部分細圖形會搭配多重圖形化完成。
- **金屬氧化物光阻**：以金屬氧化物為核心的感光材料路徑，英文常寫 MOR；材料名稱本身不代表特定配方已通過量產資格。
- **曝光後烘烤**：曝光後用受控溫度與氣氛推動光阻反應的步驟；條件改變可能同時影響感光速度、圖形與缺陷。
- **隨機缺陷**：由少量光子、材料反應或局部波動造成的偶發圖形失敗；平均線寬合格仍可能出現斷路或橋接。
- **線邊粗糙度**：圖形邊緣相對理想直線的起伏；線越細，邊緣波動越可能侵蝕電性餘裕。
- **局部線寬均勻度**：同一小區域內圖形尺寸的一致程度；平均值好看不代表每個孔洞或線段都落在規格內。
- **多重圖形化**：把原本難以一次印出的圖形拆成多次曝光與加工；步驟增加，也會增加對準與製程控制負擔。
- **對準**：讓本次加工對到晶圓上預定位置；偏差過大可能讓圖形或電路失效。
- **疊對**：量測不同製程層彼此位置是否重合；單層印得清楚仍不代表多層能正確接起來。
- **製程視窗**：曝光、焦距、材料與加工條件仍能產生合格結果的可接受範圍；視窗太窄會增加量產波動。
- **良率**：投入後得到合格晶片的比例；設備速度快或步驟少，都必須和良率一起看。
- **可用率**：設備在預定生產時間內可正常工作的比例，英文常寫 availability；它不等於每小時產出或良率。
- **每小時產出**：設備在一小時內可處理的晶圓或合格層數，英文常寫 throughput；要和停機、返工及良率一起判讀。
- **維護時間**：設備保養、校正或故障修復占用的時間；它會影響可用率、排程與實際產出。
- **測試圖形**：為了研究或校正而設計的簡化圖形；成功不等於實際產品的所有圖形都能量產。
- **電性測試結構**：把特定線路做成可量測導通或短路的結構，讓圖形外觀進一步接受功能檢查；它仍不是完整產品。
- **斷路與橋接**：細線中斷叫斷路，相鄰線意外相連叫橋接；兩者都可能來自局部或隨機圖形失敗。
- **產品晶圓**：使用實際產品設計而非只有測試圖形的晶圓，英文常寫 product wafer；仍可能停在驗證階段。
- **校準**：調整設備與量測基準，使結果落在預定範圍；校準完成不等於製程資格或量產完成。
- **資格驗證**：依指定條件確認設備、材料與製程能否被採用，英文常寫 qualification；範圍可能只涵蓋部分圖形或條件。
- **高量產導入**：把設備與製程放進持續生產的產品節點，英文常寫 HVM insertion；需要穩定良率、產出、成本與客戶產品共同成立。
- **EXE**：ASML 對高數值孔徑極紫外光曝光機使用的產品平台前綴，例如 EXE:5200；型號到廠不等於量產導入。
- **每顆合格晶片成本**：把設備、材料、加工、維護、返工與報廢分攤到最後合格晶片的成本；它比只算曝光次數更接近經濟結果。

### 三句話抓重點

- 先在晶圓表面塗上光阻，再用光罩控制光線落在哪裡；這一步像替下一道加工留下底稿。
- 新設備可能一次印出更細的底稿，因而少做重複對準與加工；但停機、材料缺陷和做壞的比例也會改變。
- 因此不能只看機器送到或累計處理多少片；要看到實際產品通過驗證、穩定生產，以及每顆合格晶片的總成本。

### 為什麼重要

曝光設備的新聞很容易把「機器送到」誤讀成「新製程已經大量生產」。真正的問題不是圖形能否
在一次展示中印得更細，而是光罩、材料、後續加工、量測與產品設計能否一起穩定運作。少做幾個
步驟可能省時間，也可能因設備昂貴、停機、缺陷或做壞更多而失去節省；最後要看的是每顆合格
晶片，而不是單一設備的最高紀錄。

### 接下來怎麼追

- 先看研發機構是否完成資格驗證，並說清楚測了哪些圖形、材料與製程條件。
- 再看設備商是否宣布量產準備條件達成，而不是只更新累計處理片數或單機最高紀錄。
- 客戶端要揭露實際產品、使用層數、缺陷、良率、每小時產出與量產日期。
- 材料與設備公司只有在客戶具名驗證、公司出貨及財務貢獻能相互核對時才升級。

### 想一想

- 如果新設備少做兩次加工，卻更常停機或做壞更多晶片，最後每顆合格晶片會更便宜嗎？
- 八台機器送到不同場所，只回答了設備商哪一段進度，還缺哪些客戶產品與穩定生產證據？
- 如果客戶只在少數最難的圖形使用新設備，材料、量測與後續加工需求會全部一起增加嗎？

## 先用五個位置看圖形怎麼印到晶圓

| 本文五個位置 | 眼前發生什麼 | 主要接力角色 | 下一個要驗收 | 不能直接推成 |
|---|---|---|---|---|
| 1. 設計圖形與光罩 | 把某一層電路圖形做成曝光時使用的模板 | 晶片設計、光罩製作、資料準備與檢查 | 光罩缺陷、圖形修正與實際產品相容性 | 光罩完成不等於晶圓已印成功或產品能量產 |
| 2. 晶圓表面與光阻 | 清潔晶圓、塗上感光材料並控制厚度與均勻性 | 晶圓廠、材料、塗佈顯影設備與製程整合 | 光阻反應、均勻度、顆粒與後續顯影結果 | 有高數值孔徑用光阻不等於已通過客戶資格 |
| 3. 曝光機與光學 | 用光學系統把光罩圖形縮小並投到晶圓光阻上 | 曝光設備、光源、光學、校準與設備維護 | 解析度、焦距、可用率、每小時產出與長期穩定度 | 機器出貨或印出測試圖形不等於產品節點量產 |
| 4. 顯影與圖形轉移 | 洗出光阻圖形，再用蝕刻等加工把圖形留下來 | 顯影、蝕刻、材料、清洗與製程控制 | 線寬、側壁、缺陷、對準與轉移後的圖形完整性 | 曝光成功不等於後續加工仍能保住相同圖形 |
| 5. 量測、檢查與下一層 | 找出尺寸、位置與缺陷，再決定是否進入下一層 | 量測、檢查、缺陷分析、良率與產品工程 | 多層疊對、實際產品良率、返工與報廢 | 單層或單次測試合格不等於整顆晶片合格 |

五個位置是最短閱讀路徑，不是完整晶片配方。高數值孔徑方案主要改變第三個位置的光學能力，
但它能不能降低總成本，仍取決於第一、二、四、五個位置能否一起通過產品與量產驗收。

## 解析度變好，為什麼反而多出五個新難題

High-NA 把數值孔徑由 0.33 提高到 0.55，目標是一次分開更細的圖形。可是解析度不是免費午餐：
光學、材料與產品版圖的限制會一起移動。下面五題要綁在同一個受測版本，不能各拿一張最佳成績
拼成不存在的量產製程。

| 本文五個新難題 | 變化從哪裡來 | 本輪一手證據走到哪裡 | 下一個要驗收 | 不能直接推成 |
|---|---|---|---|---|
| 1. 半視場與接縫 | 兩方向使用四倍與八倍縮放，單次只覆蓋半個視場；較大版圖要接兩次曝光 | ASML 說明光學與每片兩次半場曝光；imec 展示解析度下拼接，Intel 也把接縫列為客戶端挑戰 | 同一產品版圖的跨場對準、接縫圖形、長期漂移與重複性 | 研究環境拼得出來不等於所有產品版圖都能量產 |
| 2. 焦深、薄膜與表面起伏 | 解析度提高時可容許的高度範圍縮小，光阻厚度、晶圓起伏與後續轉移更敏感 | imec 說明較小焦深需要較薄膜層與共同材料最佳化 | 實際膜堆、地形、焦距分布、蝕刻後尺寸與跨晶圓能力 | 單一平坦測試區合格不等於產品全晶圓視窗足夠 |
| 3. 劑量、速度與隨機缺陷 | 劑量下降可縮短曝光時間，但少量光子與材料反應波動可能增加局部失敗 | imec 公布特定材料比較與氧氣控制烘烤的感光速度結果，也使用電子束與深紫外光檢查隨機缺陷 | 同一圖形的劑量—焦距矩陣、缺陷面積分母、返工、報廢與合格產出 | 劑量降低不等於每小時合格產出上升或成本下降 |
| 4. 光罩、修正、光阻與烘烤 | 新光學會改變光罩圖形修正；材料、底層與曝光後烘烤又會改變圖形反應 | imec 與 Intel 都把光罩、光阻及共同最佳化列為工作項目 | 固定光罩版次、材料批次、底層、烘烤氣氛與變更後重驗 | 一項材料進步不等於整個材料家族或供應商已通過資格 |
| 5. 圖形轉移與電性 | 光阻上看得見的線，經顯影、蝕刻或金屬化後仍可能斷掉或黏在一起 | imec 已把 20nm pitch 金屬化測試結構接到斷路／橋接電性量測，也展示功能性研究元件 | 完整產品圖形族、跨批次電性、最終良率與產品壽命 | 兩類測試結構或一個研究元件不等於客戶產品層 HVM |

這五題也解釋了為什麼「材料需求變難」不等於「材料公司收入必然上升」。新配方可能減少劑量，
也可能要求更薄膜層、不同烘烤、額外檢查或重做光罩；只有客戶用同一產品層把配方、缺陷、產出與
成本完整簽核，才知道哪個角色得到多少可持續價值。

## 0.55 比 0.33 大，為什麼景深反而只剩約三分之一

### 先固定波長與 k1，再談解析度

ASML 用 Rayleigh 關係把臨界尺寸寫成：

- CD ＝ k1 × 波長 ÷ NA。

式子看似簡單，真正重要的是比較契約。波長要相同，k1 也要相同，才可以把 CD 的差異只歸給
NA。k1 不是一顆設備旋鈕，而是會隨光罩、照明、材料、圖形與製程方法改變的係數；因此「NA
提高 67%」不能直接改寫成「產品線寬縮小 67%」。

下面只做一個固定輸入的教學換算：兩個設定都使用 13.5nm 波長與假想 k1＝0.32，只把 NA 由
0.33 改為 0.55。

| 本文假想設定 | 波長 | k1 | NA | Rayleigh CD | 只回答什麼 |
|---|---:|---:|---:|---:|---|
| A：較低 NA | 13.5nm | 0.32 | 0.33 | 13.0909nm | 固定波長與 k1 時的理論臨界尺寸 |
| B：較高 NA | 13.5nm | 0.32 | 0.55 | 7.8545nm | 同一簡化公式下，CD 為 A 的 0.60、縮小 40% |

這是 N＝2 個假想光學設定的確定性換算，不是抽樣、曝光實驗或 ASML 產品規格；沒有晶圓、圖形、
run、sampling SE／t、缺陷、良率、每小時產出或成本。Python Fraction 精確有理數與獨立 awk
重算一致；13.0909nm 與 7.8545nm 只存在於這組假設，不能拿去替任何產品節點背書。

### 解析度、景深與半視場是三本帳

解析度變好，不代表晶圓高度的容許範圍也一起變大。University of Hyogo 的 2023 受邀摘要把
0.55 NA 的 wafer depth of focus 計算為 45nm，約是 0.33 NA 的三分之一，並指出因此需要薄光阻；
光阻越薄，線寬粗糙度反而更難控制。這是研究計算與材料問題，不是客戶產品的實測製程能力。

另外，ASML 的非等向光學讓 EXE 曝光視場只有 NXE 的一半，所以同一晶圓面積需要兩倍曝光次數。
若把完整視場覆蓋指數設為 100，半視場就是 50；覆蓋同一面積的曝光次數指數會由 100 變成 200，
增加 100%。這也只是幾何帳。ASML 以更快的 wafer 與 reticle stage 補償，所以不能再假設每片
時間必然加倍；實際產能要回到同一設備版本的可用率、停機、raw wafers per hour 與合格產出。

| 必須分開的帳 | 一手資料能說什麼 | 還要量什麼 | 不能直接推成 |
|---|---|---|---|
| 解析度帳 | 固定波長與 k1 時，NA 進入 CD 的分母；ASML 另報 EXE 約 8nm、NXE 約 13nm 的平台尺度 | 同一產品圖形的 k1、方向、pitch、CD 定義與全晶圓分布 | 理論 CD 變小等於產品節點、良率或密度按平方改善 |
| 焦深帳 | 受邀摘要報告 0.55 NA 計算值 45nm、約為 0.33 NA 的三分之一 | 同一膜堆的焦距預算、晶圓地形、光阻厚度、劑量—焦距矩陣與轉移後結果 | 研究計算等於客戶產品已保有足夠視窗 |
| 視場帳 | EXE 半視場使同面積曝光次數幾何上加倍 | 版圖接縫、stage 速度、移動與換場 overhead、raw 及 good throughput | 曝光次數加倍等於晶圓時間或成本加倍 |
| 生產帳 | 更快 stage 是補償半視場的設備路徑 | 可用率、維護、重工、報廢、每小時合格層數與每顆合格晶片成本 | 最高 wafers per hour 等於持續產品產能或財務受惠 |

### 多空小作文共用一份十欄光學—製程護照

多方版本可以主張：在同一產品層，較小 CD 讓單次曝光替代多重圖形化，且焦距—劑量視窗、接縫、
缺陷、轉移後電性與每小時合格產出都通過，最後每顆合格晶片成本下降。空方版本可以主張：半視場、
較窄焦深、薄光阻粗糙度與新增控制吃掉簡化收益。兩邊都不能只挑自己喜歡的單一規格，必須交付
同一份護照：

| 本文十欄光學—製程護照 | 至少要固定或量測 | 為什麼重要 |
|---|---|---|
| 1. 產品與版本 | 客戶、產品、層、版次、晶圓、批次與比較期間 | 測試圖形不能替產品層畢業 |
| 2. 波長與 NA | 光源波長、NA、光學版本、照明與方向 | 先鎖定 Rayleigh 公式的光學輸入 |
| 3. k1 與圖形定義 | k1、pitch、線／孔、方向、CD 與通過門檻 | 不同圖形不能共用一個理論縮小比 |
| 4. 光罩與視場 | 光罩版次、四倍／八倍縮放、全場／半場、接縫與修正 | 半視場幾何與接縫風險要回到產品版圖 |
| 5. 焦距預算 | 焦深、leveling、晶圓起伏、膜堆、厚度與量測誤差 | 45nm 研究值不是全部高度變動可用額度 |
| 6. 光阻與劑量 | 配方、批號、厚度、底層、劑量、烘烤、LWR 與隨機缺陷 | 薄膜與速度改善可能交換粗糙度或缺陷 |
| 7. 轉移與電性 | 顯影、蝕刻、沉積、清洗、線寬、斷路、橋接與功能 | 光阻影像必須穿過後段加工與電性驗收 |
| 8. 設備生產 | 曝光數、stage 速度、換場 overhead、raw throughput、可用率與停機 | 幾何曝光數與最高機速都不是 good output |
| 9. 樣本與不確定性 | 晶圓、面積、結構、run、重複、分布、失效與量測不確定度 | 最佳點不能冒充穩定製程能力 |
| 10. 商業與變更沿革 | 合格產出、返工、報廢、成本、qualification、出貨、收入與重驗 | 技術改善要留下客戶採用與財務共同鍵 |

多方通過條件不是「0.55 大於 0.33」，而是護照第 1 至 10 欄在同一版本留下正的合格產出與成本
證據；空方也不能只靠 45nm、半視場或薄光阻宣告失敗，而要看到焦距、接縫或缺陷真正侵蝕產品
視窗與經濟結果。現有公開證據讓四本帳可以被正確提出，仍不足以裁決任何客戶產品或台灣供應商。

## 再用五把尺比較少做步驟是否真的省錢

| 本文五把尺 | 較高數值孔徑方案 | 現行多步驟方案 | 下一個要量的結果 | 不能直接推成 |
|---|---|---|---|---|
| 1. 曝光與加工次數 | 目標是一次印出更細圖形，讓部分層少做重複曝光與圖形轉移 | 可能把困難圖形拆開，多做曝光、對準與加工 | 同一產品層實際少了哪些步驟、時間與材料 | 理論少一步不等於整片晶圓或整顆晶片成本較低 |
| 2. 機器可用時間與每小時產出 | 新平台要證明長時間運轉、維護與每小時產出符合生產需求 | 既有平台已有較長的運轉經驗，但多步驟會占用更多機台時間 | 同一期間的可用率、停機原因、維護時間與合格產出 | 累計處理片數不能直接換成每台穩定產能 |
| 3. 光罩、光阻與缺陷 | 更細圖形會改變光罩、感光材料與缺陷控制要求 | 多次加工增加光罩、材料與每一步產生缺陷的機會 | 光罩數、材料用量、缺陷密度、返工與報廢 | 材料要求變高不等於任何材料商已取得份額 |
| 4. 對準、製程視窗與良率 | 少做部分重複對準可能有利，但新光學與材料仍要建立穩定視窗 | 每多一次圖形拆分與轉移，都要控制層間位置與誤差累積 | 實際產品的疊對、視窗、缺陷與最終良率 | 單一測試圖形更清楚不等於完整產品良率更高 |
| 5. 每顆合格晶片總成本 | 要把昂貴設備、材料、維護、停機與良率一起分攤 | 要把較多曝光、加工、光罩、排程與誤差成本一起分攤 | 同一產品、產量與期間的設備折舊、材料、返工、良率與合格品 | 不能只靠曝光次數或設備價格宣告哪一條路更便宜 |

這五把尺把「解析度更高」和「經濟性更好」分開。高數值孔徑方案可能先用在最難、最值得少做
步驟的少數層；現行方案也可能在其他層繼續使用。沒有同一產品、層數、產出、良率與成本分母，
就不能把技術優勢改寫成全面替代或更低總成本。

## 把五類角色放回同一段曝光接力

| 本文五類角色 | 它交付什麼 | 本輪具名例子 | 已證實到哪裡 | 不能外推 |
|---|---|---|---|---|
| 1. 曝光設備與平台 | 提供高數值孔徑曝光機、安裝、運轉與平台改進 | ASML 的 EXE 平台 | 截至 2025 年底八台出貨、六台運轉；平台累計處理逾 50 萬片 | 出貨、運轉與累計片數不等於客戶完成量產導入 |
| 2. 研發與資格整合 | 把設備、光罩、光阻、量測與圖形轉移放進共同測試環境 | imec 的 EXE:5200 | 設備已到研發環境，公開目標是在 2026 年第四季完成資格驗證 | 研發機構資格不等於晶圓製造客戶的產品節點量產 |
| 3. 晶圓製造客戶 | 安裝設備、校準並用實際產品圖形驗證製程 | Intel 的早期安裝；其他客戶產品晶圓測試 | Intel 公開完成安裝並開始校準；ASML 表示客戶已開始產品晶圓測試 | 沒有客戶、節點、層數、良率與量產日期，不能宣告導入完成 |
| 4. 光罩、材料與圖形轉移 | 讓曝光圖形能被顯影、蝕刻並保留在晶圓上 | 本輪只確認這些是共同成熟條件 | ASML 與 imec 文件支持光阻、光罩與圖形化依賴 | 沒有具名供應商資格、出貨、份額或台灣公司財務證據 |
| 5. 量測、檢查與生產經濟 | 找缺陷、量尺寸、追良率，並把結果接回產出與成本 | 本輪沒有具名台灣供應商 | 量測、檢查與製程穩定度是成熟條件；公司映射仍未證實 | 一般先進製程能力不能改寫成高數值孔徑訂單或獲利 |

角色表回答「誰負責哪一段」，不是完整供應商名單。ASML、imec 與 Intel 的公開資料分屬
設備商、研發整合與早期客戶時鐘；它們能共同支持產業路徑，卻不能替任何台灣設備或材料公司
補上具名資格、出貨與財務結果。

## 把五個里程碑排成同一條導入階梯

| 本文五個里程碑 | 白話意思 | 本輪可確認 | 下一份證據 | 不能合併成 |
|---|---|---|---|---|
| 1. 機器送達 | 設備商完成出貨，客戶或研發場所收到設備 | 截至 2025 年底累計八台高數值孔徑系統出貨 | 後續安裝、客戶驗收與逐台配置 | 八台出貨不是八條量產線，也不是八個客戶量產 |
| 2. 開始運轉與校準 | 設備安裝後能啟動、調整並處理晶圓 | 六台運轉；Intel 早期系統完成安裝並開始校準 | 長期可用率、每小時產出、維護與客戶驗收 | 能運轉不等於製程資格、產品良率或量產 |
| 3. 研發資格與共同整合 | 光罩、材料、圖形轉移與量測在指定範圍通過測試 | imec 設備到廠，目標在 2026 年第四季完成資格驗證 | 完成文件、測試範圍、限制與未成熟項目 | 目標日期不是已完成結果；研發資格也不是客戶量產 |
| 4. 實際產品晶圓測試 | 用真實產品圖形而非只有測試圖形驗證 | ASML 表示客戶已開始測試；平台累計處理逾 50 萬片、可用率逾 80% | 客戶、產品、層數、視窗、缺陷與良率分母 | 聚合片數與可用率不能指定到某個客戶節點 |
| 5. 穩定量產導入 | 客戶把具名層放進持續生產，產出、良率與成本可重算 | ASML 把量產準備條件與客戶導入放在未來目標 | 2026 年底準備結果與 2027–2028 客戶產品量產文件 | 未來目標不能提前寫成已量產或已形成供應鏈收入 |

五個里程碑使用不同單位、期間與責任人。研究中心保留八台、六台、五十萬片、逾八成可用率
與未來時程，卻不把它們相加或正規化成一個假精確的「完成率」。

## 再用六級證據分清印得出來與產品能量產

同一句「High-NA 成功」可能只指材料反應，也可能指完整產品。研究時要先問受測物是什麼，再問
它通過哪一種判定。下面六級可以逐級累積，但上級不能由下級自動推得。

| 本文六級圖形證據 | 這一級回答什麼 | 本輪可確認 | 還缺什麼 | 不能替代 |
|---|---|---|---|---|
| 1. 光學或材料單項結果 | 指定曝光、材料或烘烤條件能否改善解析度、劑量或局部均勻度 | ASML 說明光學架構；imec 公布特定材料與烘烤條件結果 | 不同圖形、晶圓區域、批次與設備重現 | 轉移後圖形、電性或產品良率 |
| 2. 顯影後光阻圖形 | 光阻上是否真的留下指定線、孔與接縫 | imec 展示半場拼接與多種研究圖形 | 蝕刻或沉積後是否仍保有尺寸與低缺陷 | 實體電路可導通或不短路 |
| 3. 蝕刻或金屬化測試結構 | 暫時圖形經後續加工後能否變成實體結構 | imec 公布 20nm pitch 金屬化結構 | 足夠面積、圖形族、跨晶圓與跨批次分布 | 完整產品功能與量產良率 |
| 4. 電性測試載具 | 指定結構是否通過導通、短路等電性判定 | serpentine 與 fork-fork 結構報告超過九成電性良率 | 樣本分布、製程能力、更多失效模式與長期穩定 | 實際產品的所有電路與使用條件 |
| 5. 功能性整合元件 | 多道製程組成的元件能否執行目標功能 | imec 公布功能性量子點量子位元網路 | 客戶產品類型、完整層級、可靠度、產出與長期良率 | 邏輯或記憶體客戶產品 HVM |
| 6. 客戶產品層與高量產 | 具名產品層能否持續以可接受良率、產出與成本生產 | 本輪只有 product-wafer testing 與未來 insertion 目標 | 客戶、產品、層數、版本、視窗分布、量產日期及成本 | 供應商訂單、收入與毛利；這仍要再做財務雙向核對 |

目前公開證據已從光阻圖形走到電性測試結構與功能性研究元件，這是實質進步；但第六級仍缺同一
客戶產品層的完整分母。因此本文更新主命題的複核日期，卻不提高信心水位，也不把研究元件改寫成
邏輯或記憶體量產。

## 一份可重驗的製程視窗紀錄至少有十欄

如果兩份新聞稿都說「良率提升」，卻使用不同光罩、光阻、烘烤或測試結構，兩個數字就不能直接
相加。研究中心用下面十欄把結果鎖回受測版本；任何欄位變更，都要先決定哪些測項需要重跑。

| 本文十欄製程視窗紀錄 | 至少要記什麼 | 為什麼不能省略 |
|---|---|---|
| 1. 受測物與版本 | 測試圖形、電性載具或產品、設計版次、晶圓與批次 | 不同受測物的良率分母不能混用 |
| 2. 光罩、視場與拼接 | 光罩版次、半視場配置、接縫位置、對準與圖形修正版本 | 拼接成功可能只限特定方向、圖形與接縫位置 |
| 3. 光阻與底層 | 材料類型、配方版本、批號、厚度、底層與塗佈條件 | 同名材料家族不代表同一實際配方與膜厚 |
| 4. 曝光設定 | 劑量、焦距、照明條件、設備與校準版本 | 只報最佳點看不出可容許視窗與設備漂移 |
| 5. 烘烤、顯影與環境 | 溫度、時間、氣氛、氧濃度、顯影條件與環境控制 | 材料反應可能因後段條件改變而無法重現 |
| 6. 膜堆與表面地形 | 產品膜層、厚度、晶圓起伏與受測區域 | 平坦測試區的焦深結果不能代表產品全晶圓 |
| 7. 圖形轉移與金屬化 | 蝕刻、沉積、清洗、金屬化 recipe 與設備版本 | 光阻圖形可能在後續加工中縮短、倒塌或橋接 |
| 8. 量測與電性判定 | 被測量、工具、校準、取樣、斷路／橋接規則與決策門檻 | 平均尺寸、缺陷影像與電性良率回答不同問題 |
| 9. 樣本、失效與良率分母 | 晶圓數、面積、結構數、失效分類、返工、報廢與不確定性 | 沒有分母就無法分辨穩定能力與少數最佳樣本 |
| 10. 生產與變更沿革 | 可用率、每小時合格產出、停機、維護、成本、變更原因與重驗結果 | 技術成績只有接到穩定生產與版本沿革才可用於 HVM 判斷 |

這份十欄紀錄不是要求公司公開機密配方，而是規定研究推論不能跨越哪些欄位。公開文件若只給一個
劑量、線寬或良率，研究中心就只把它放在相應證據級別；缺少的欄位會轉成監測項，而不是用產業
常識補成客戶 qualification、供應商份額或財務結果。

## 最後用六關分開設備進度、客戶量產與公司受惠

| 本文六關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 目標圖形可以印出 | 高數值孔徑設備能處理指定圖形與晶圓 | 多台設備已出貨與運轉，平台有累計處理量 | 第二個獨立環境重現實際產品圖形與限制 | 技術可行不等於量產穩定或成本較低 |
| 2. 多台設備能持續運轉 | 客戶端設備有可重算的可用率、產出與維護結果 | 六台運轉；平台聚合可用率逾 80% | 逐台、逐客戶、同期間的停機、維護與合格產出 | 聚合平均不能代替每台設備與客戶驗收 |
| 3. 共同製程通過資格 | 光罩、光阻、圖形轉移、量測與檢查在指定範圍完成驗證 | imec 公開的是 2026 年第四季目標，尚非完成結果 | 資格文件、測試範圍、材料、缺陷與未達項目 | 設備到廠或目標日期不能改寫成共同製程已成熟 |
| 4. 實際產品達成視窗與良率 | 客戶以具名產品與層數證明圖形、缺陷與良率 | 已開始產品晶圓測試，但沒有客戶與結果分母 | 產品、節點、層數、製程視窗、缺陷與良率 | 開始測試不等於完成驗證或進入大量生產 |
| 5. 量產層數、產出與成本可重算 | 客戶持續生產，能比較少做步驟後的每顆合格晶片成本 | 客戶導入仍是 2027–2028 目標 | 量產日期、層數、台數、產出、良率、設備與材料成本 | 未來導入目標不能換算市場規模、材料用量或公司營收 |
| 6. 供應商財務足跡出現 | 具名設備或材料通過客戶資格並留下出貨、收入、毛利與現金流 | 沒有任何 universe 公司完成雙向核對 | 客戶具名資格加上公司產品、出貨、份額與財務分母 | 服務先進製程或極紫外光不等於已取得高數值孔徑訂單 |

本輪設備與平台可走到第二關，第三關仍是待完成目標，第四關只有「開始測試」而沒有產品結果，
第五、六關尚未通過。六關是證據排序，不是技術分數、供應商名單、營收預測或投資排名。

## 這篇對公司判斷的用處與界線

半導體設備研究可以沿曝光、塗佈顯影、蝕刻、清洗、量測與缺陷控制尋找具名資格；材料研究
可以追光阻、光罩相關材料、化學品與耗材。但這些只是「去哪裡找下一份證據」，不是「公司
已經受惠」。同一台曝光機開始運轉，也不表示所有前後段設備與材料用量會等比例上升。

真正能升級公司信心的資料，必須把同一客戶、具名產品、使用層、資格驗證、量產出貨與財務
結果串在一起。現有來源沒有列名 universe 公司，也沒有訂單、收入、毛利、資本支出回收或
市場定價分母；因此本文不支持個股排序、營收推估或投資動作。

## 來源與證據邊界

- [ASML 2026 年股東會簡報](https://ourbrand.asml.com/asset/d5e933d7-78d0-406c-aed7-a46626e63381/2026_-AGM-_presentation.pdf)（工具出貨、運轉與客戶導入時程）。
- [Imec EXE:5200 到達研發環境](https://www.imec-int.com/en/press/imec-receives-worlds-most-advanced-high-na-euv-system)（研發整合與 2026 年第四季資格目標）。
- [ASML 2026 年第一季投資人電話會議](https://ourbrand.asml.com/asset/8e1f7393-33dd-4737-a436-cfe1b68cc577/2026_04_15-ASML-Transcript-investor-call-Q1-2026.pdf)（累計晶圓、可用率、產品晶圓與光阻進度）。
- [Intel 高數值孔徑極紫外光資料](https://newsroom.intel.com/press-kit/intel-high-na-euv)（早期客戶安裝與校準基線）。
- [ASML：High-NA 的五個重點](https://www.asml.com/en/company/stories/2024/5-things-high-na-euv)（0.55 數值孔徑、非等向光學、半視場與設備速度路線）。
- [ASML：Rayleigh 解析度準則](https://www.asml.com/en/technology/lithography-principles/rayleigh-criterion)（CD、波長、NA 與製程相依 k1 的一階關係）。
- [2023 極紫外光微影研討會摘要集](https://euvlitho.com/2023/2023%20EUVL%20Workshop%20and%20Supplier%20Showcase%20Abstract%20Book.pdf)（PDF 檔案第36頁、頁尾 program P46；0.55 NA 的 45nm 計算焦深、薄光阻與線寬粗糙度邊界）。
- [Imec：High-NA 圖形化生態系準備](https://www.imec-int.com/en/press/imec-demonstrates-readiness-high-na-euv-patterning-ecosystem)（半視場拼接、焦深、材料、劑量與隨機缺陷）。
- [Imec：20nm pitch 金屬線電性測試](https://www.imec-int.com/en/press/imec-demonstrates-electrical-yield-20nm-pitch-metal-lines-obtained-high-na-euv-single)（金屬化測試結構、斷路／橋接與初步電性良率）。
- [Imec：氧氣控制的曝光後烘烤研究](https://www.imec-int.com/en/press/imec-unlocks-lever-euv-dose-reduction-oxygen-injection-during-metal-oxide-resist-post)（特定研究條件的感光速度結果與未完成機制）。
- [Imec：High-NA 製作的功能性量子點元件](https://www.imec-int.com/en/press/world-first-imec-presents-quantum-dot-qubit-device-using-high-na-euv-lithography)（整合研究裝置證據及產品量產邊界）。
- [Intel Foundry：SPIE 2026 技術更新](https://community.intel.com/t5/Blogs/Intel-Foundry/Systems-Foundry-for-the-AI-Era/Delivering-Technologies-to-Power-the-AI-Era-Intel-Foundry-at/post/1737961/jump-to/first-unread-message)（客戶端半視場接縫、21nm pitch 與光阻／光罩共同最佳化）。

本篇沒有拿 ASML、imec 與 Intel 的數字互相比較：一組是設備商平台、一組是研發機構資格，
一組是早期客戶安裝事件，期間、單位與定義不同。也不使用設備出貨數推估台灣公司訂單、
晶圓廠良率、每顆合格晶片成本或市場定價。

該摘要集官方 PDF 共 71 頁，SHA-256 為
9b506db456f0e6d4863c0ff26c182ba1d9d69c7fb1fd837abde2182e435b8d66；實際引用檔案第36頁，並把
前後頁第35–37頁逐頁渲染核對。PDF 與 PNG 只留在 tmp、不進版控。摘要集的 2023-06-03 日期以
官方 agenda 所列研討會起始日正規化，不主張為檔案上線日；45nm 是作者計算，不是本研究重測。

## 影響路由

<!-- impact
group_id: semiequip
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-01
rationale: High-NA 需要曝光之外的塗佈 顯影 蝕刻 清洗 量測與缺陷控制，但本輪未取得 universe 公司被客戶具名 qualification 的雙向證據
evidence_boundary: 服務先進製程或 EUV 不等於直接參與 High-NA、取得訂單或形成收入毛利
-->

<!-- impact
group_id: material
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-01
rationale: ASML 與 imec 明示 resist、mask、patterning 與材料生態系是成熟條件，但沒有具名台灣材料、規格、資格或財務貢獻
evidence_boundary: 光阻 化學品 晶圓或耗材能力是搜尋路由，不是 High-NA 客戶採用或業績事實
-->

## 下一個可證明／否定的節點

- Imec 在 2026 年第四季公開 EXE:5200 資格驗證結果、測試範圍與仍未達成項目。
- ASML 確認量產準備條件是否如期達成，並提供能分開產品測試與持續生產的指標。
- Intel 或其他客戶揭露實際節點、使用層數、產品晶圓、製程視窗、缺陷、良率與量產日期。
- 同一產品層公開十欄製程視窗紀錄，能把半視場拼接、劑量／焦距、材料與烘烤、轉移後電性、產出及變更後重驗接在一起。
- 同一產品層公開十欄光學—製程護照，把波長、NA、k1、CD、焦距預算、半視場、接縫、光阻、合格產出與成本鎖在同一版本，而不是只報單一解析度或最高機速。
- 若 2027–2028 客戶導入延後、只停在研發，或現行多重圖形化在成本與良率持續更有利，C5 必須下修。
- 台灣設備與材料公司只有在客戶具名資格與公司產品、出貨及財務揭露相互吻合後，才從未驗證路由升級。
