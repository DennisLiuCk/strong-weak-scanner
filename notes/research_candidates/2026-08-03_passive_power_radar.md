# 2026-08-03 被動元件與電源責任層研究雷達

本輪承接族群覆蓋盤點，專門檢驗被動元件與 800V 電源研究能否從「元件會增加」推進到可查核的
系統位置、故障責任與 qualification。排名已在深研前凍結；升格只代表 article＋graph 契約通過。

<!-- research_radar
schema_version: 2
radar_id: RADAR-2026-08-03-03
as_of: 2026-08-03
next_review: 2026-08-10
status: active
method: 先由現有族群文章與圖譜覆蓋確認 passive 仍是最薄的一群，再按一手來源能否對齊系統位置／故障模型、可證偽性、相對既有 CBU／800V 研究的新增知識、台灣公司映射風險與維護成本排序；候選先寫入 append-only selection log，深研後只更新 evidence posture、route 與結果，另以學習者／分析師雙讀者 gate 檢驗發布可用性
selection_cycle_id: RS-2026-08-03-03
-->

<!-- research_candidate
candidate_id: RC-AI-CAPACITOR-ROLE-MAP
rank: 1
title: AI 電源電容的系統位置與頻帶角色
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: OCP／TI 可定位 rack CBU，TDK 把 400–800V 與低壓產品分區，Murata 又把 MLCC、silicon 與 polymer capacitor 按 target impedance、transient 及 placement 分工；四條一手來源鏈足以建立角色圖
knowledge_gain: 把 passive 研究從「AI／高壓帶動電容」推進到 CBU、DC-link、board bulk、package／near-die decoupling 四個查核單位，並建立避免材料替代與顆數重複計算的順序
first_rejection: 若一手文件只能各自推銷產品，無法對齊系統位置、電壓、頻帶、主要任務與不可替代邊界，就不建立電容種類排名或族群圖譜。
next_evidence: 交叉核對 OCP／TI 的 CBU、TDK 的高低壓元件地圖與 Murata 的 PDN 頻帶角色；分開 requirement、reference design、issuer product claim、production deployment 與台灣公司曝險。
next_check: 2026-09-01
route: article_and_graph
article_topic_id: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP
graph_id: ai-capacitor-role-map
sources: OCP Diablo 400 CBU option => https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf | TI EDLC 800V CBU => https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html | TDK AI data center passive map => https://www.tdk.com/system/files/2026_4q01_0mqf56xw_en.pdf | Murata AI PDN Q&A => https://www.murata.com/-/media/webrenewal/campaign/events/asean/2026/apr26_ai-system-with-advance-packaging/qna.ashx?cvid=20260425083237000000&la=en-sg
-->

<!-- research_candidate
candidate_id: RC-800VDC-PROTECTION-LAYERS
rank: 2
title: 800VDC 的安全、故障電流與 Hot-swap 責任層
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: OCP Diablo 400 可逐項定位 interlock、spacing、overcurrent、earthing、leakage 與 ground fault；TI 把 hot-swap 與 conversion／CBU 分列，Infineon 再提供 sampling reference design、SOA-controlled inrush 與 12kW 額定
knowledge_gain: 把 power／powersupply／passive 的「800V 保護」題材改寫成可檢驗 fault matrix，分開人身維修、絕緣接地、故障電流、帶電連接與 ride-through，避免把 requirement 數量當成 BOM 顆數
first_rejection: 若無法由正式 requirement 與實測 reference design 區分 fuse／breaker、hot-swap／eFuse、ground-fault／interlock、surge clamp 與 CBU／BBU，或只能得到產品行銷詞，就不升格。
next_evidence: 逐頁核對 OCP safety／interconnect 要求、TI 800V protection white paper 與 Infineon hot-swap board 的測試範圍；明示 reference design 不等於平台採用、供應商資格或量產收入。
next_check: 2026-09-01
route: article_and_graph
article_topic_id: MI-2026-08-03-800VDC-PROTECTION-LAYERS
graph_id: 800vdc-protection-layers
sources: OCP Diablo 400 safety requirements => https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf | TI 800V hot-swap input protection => https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html | Infineon REF_XDP701_4800 launch => https://www.infineon.com/technology-news/2025/INFPSS202510-002
-->

<!-- research_candidate
candidate_id: RC-AI-EMI-FILTER-PARTITION
rank: 3
title: AI 電源 EMI filter 的共模／差模與頻帶分工
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: TI 30kW HVDC、Infineon 800V BBU 與 Murata AI power guide 都能確認 filter／ferrite／capacitor 位於電力鏈，但現有公開資料仍無共同限值、完整 schematic、頻譜與 production BOM
knowledge_gain: 若補齊 EMC limit、conducted／radiated spectrum 與 topology，可把磁性元件和電容研究從 switching-frequency 敘事推進到可測衰減、熱與 qualification；現在資訊增益尚不足以獨立成文
first_rejection: 若沒有共同 EMC 限值、量測頻譜、filter topology 與可重建 BOM，不得由功率密度或 switching frequency 直接推成磁性元件／電容用量排行。
next_evidence: 等待 800V reference design schematic／BOM、CISPR／IEC 適用限值、conducted／radiated emission 測試與量產平台 filter qualification。
next_check: 2026-09-15
route: watch_only
sources: TI 30kW HVDC reference design => https://www.ti.com/lit/ug/slvt224/slvt224.pdf | Infineon 800V BBU reference design => https://www.infineon.com/technology-news/2026/infpss202606-093 | Murata AI power technology guide => https://www.murata.com/en-eu/news/other/other/2026/0204
-->

<!-- research_candidate
candidate_id: RC-AI-POWER-MAGNETICS
rank: 4
title: AI 高變比供電的磁性元件價值量
priority: p3
knowledge_value: medium
status: deferred
evidence_posture: assumption_led
why_now: 本輪找到更多 800V converter topology 與 transformer／inductor 說明，但仍沒有可映射本 universe 的量產磁材、電氣／熱規格、qualified supplier、份額或收入；沿用前輪拒絕
knowledge_gain: 保留候選可防止磁性元件因族群覆蓋薄弱被遺漏，也能明確記錄「轉換級存在不等於元件價值量」；目前不值得建立另一篇低證據文章
first_rejection: 若沒有可定位的量產設計、磁性元件規格與供應商／收入證據，不得由轉換級數直接推成被動元件用量或受惠排行。
next_evidence: 等待量產 reference design 或客戶文件披露 switching topology、磁性元件電氣／熱規格、BOM 位置、供應商資格與可辨識收入。
next_check: 2026-10-01
route: watch_only
sources: NVIDIA 800V power ecosystem => https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/ | TI 800V conversion reference designs => https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html
-->

<!-- research_candidate
candidate_id: RC-AI-POWER-TELEMETRY
rank: 5
title: 800V protection telemetry 的事件與維修閉環
priority: p3
knowledge_value: medium
status: expand_existing
evidence_posture: preliminary
why_now: Infineon eFuse／hot-swap 文件已有 voltage、current、energy、power 與 fault telemetry，OCP 也有 rack management 介面；但共同 event schema、timestamp、fault action、retention、site log 與維修決策仍未公開
knowledge_gain: 本輪把 telemetry 明確併入 protection fault model，要求每個量測欄位對應隔離或維修 action；在共同 contract 出現前不另造一個缺乏商業材料性的題材
first_rejection: 若 telemetry 只有控制器功能清單，沒有共同欄位、事件時間、fault action、site log 與維護決策，就不另建監測題材或公司價值主張。
next_evidence: 追蹤 OCP RMU／PMBus 欄位、800V hot-swap fault log、site telemetry 與告警到隔離／維修的 action contract。
next_check: 2026-09-15
route: expand_existing_article
article_topic_id: MI-2026-08-03-800VDC-PROTECTION-LAYERS
graph_id: 800vdc-protection-layers
sources: Infineon protection and monitoring portfolio => https://www.infineon.com/products/power/protection-and-monitoring-ics | OCP Diablo 400 rack management and safety => https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf
-->

## 本輪方法結果

- 研究前凍結五題；深研後兩題通過 research-grade article＋graph，一題併入 protection 文章，一題維持 watch，一題維持 deferred。
- 升格依據是系統位置或 fault model 可由至少三條一手來源鏈重建，不是族群覆蓋薄弱或題材熱門。
- 兩篇都把台灣 company BOM、qualification、份額、訂單與財務分母保留為 active unverified claim，圖譜族群邊一律為 unverified。
- 發布頁新增由 register 自動合成的分析師快讀，詳細 ledger 下移到機制與研究判定之後；這改善可用性，不提升任何證據層級。
