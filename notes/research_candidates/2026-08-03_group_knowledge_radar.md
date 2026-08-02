# 2026-08-03 族群知識缺口研究雷達

本輪從現有族群的研究與圖譜覆蓋缺口出發。排名先於深研凍結；研究完成後只更新成熟度與
路由，不回寫初始排名、第一拒絕或下一份證據。升格代表通過研究文章與圖譜契約，不是投資建議。

<!-- research_radar
schema_version: 2
radar_id: RADAR-2026-08-03-02
as_of: 2026-08-03
next_review: 2026-08-10
status: retired
method: 先以族群文章與圖譜端點覆蓋找缺口，再按一手來源獨立性、能否建立可證偽機制、相對既有研究的新增知識、台灣公司映射風險與維護成本排序；候選先寫入 append-only selection log，深研後只更新 research grade、promoted 或 deferred 結果
selection_cycle_id: RS-2026-08-03-02
-->

<!-- research_candidate
candidate_id: RC-AI-POWER-BUFFERING
rank: 1
title: AI 功率緩衝的 CBU／BBU／BESS 時間尺度
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: NVIDIA 已把毫秒至秒的 rack-side capacitors／supercapacitors 與秒至分鐘的 facility BESS 分層，OCP Diablo 400 又把 BBU 與 CBU 分列，TI 提供 EDLC CBU reference design；三個獨立一手來源可重建機制
knowledge_gain: 補上 passive 族群零圖譜端點的缺口，並把電容緩衝、rack ride-through、設施儲能與既有 800V power tree 分開，避免把所有儲能與被動元件合成同一需求
first_rejection: 若一手文件無法把瞬態抑制、rack ride-through、facility load smoothing 的時間尺度、位置與失效條件分開，就不建立被動元件族群研究或圖譜。
next_evidence: 核對 NVIDIA、OCP 與元件／電源供應商對 CBU、BBU、BESS、DC bus、轉換級與時間尺度的精確定義，並明示沒有台灣供應商 BOM／收入證據。
next_check: 2026-09-01
route: article_and_graph
article_topic_id: MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY
graph_id: ai-power-buffering
sources: NVIDIA multi-timescale energy storage => https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/ | OCP Diablo 400 0.7.0 => https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf | TI EDLC capacitor bank reference design => https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html
-->

<!-- research_candidate
candidate_id: RC-LIQUID-COOLING-LOOP-BOUNDARY
rank: 2
title: 液冷 FWS／TCS／ITE／控制責任邊界
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: OCP Rev 2 明確劃出 TCS、FWS 與 ITE scope，OCP 現行工作流涵蓋流體、快接、manifold 與 cold plate，Lenovo 和 NVIDIA DSX 再由場域實作與 BMS contract 補強；可回答既有 CDU 資格文章未涵蓋的系統責任
knowledge_gain: 把液冷研究從容量與平台列名推進到 interface control、water chemistry、telemetry、leak isolation、site acceptance 與維護，讓 thermal、powersupply、serverodm 族群能用同一成熟度階梯被檢驗
first_rejection: 若只能得到供應商產品頁或概念圖，無法由正式要求文件重建 TCS／FWS 邊界、可量測介面與維運條件，就不另建研究。
next_evidence: 逐項核對 OCP 冷板迴路 Rev 2、冷板要求、流體／快接工作流與平台驗證入口，區分 requirement、specification、validated product 與實際部署。
next_check: 2026-09-03
route: article_and_graph
article_topic_id: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES
graph_id: liquid-cooling-loop-boundaries
sources: OCP Cold Plate Cooling Loop Requirements Rev 2 => https://www.opencompute.org/documents/cold-plate-cooling-loop-requirements-rev-2-pdf | Lenovo Neptune Direct Water-Cooling Standards => https://lenovopress.lenovo.com/lp2018-lenovo-neptune-direct-water-cooling-standards | NVIDIA DSX BMS Integration => https://docs.nvidia.com/dsx-exchange/bms-integration
-->

<!-- research_candidate
candidate_id: RC-224G-ELECTRICAL-OPTICAL
rank: 3
title: 224G 電連接與光連接邊界
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: IEEE P802.3dj 已前進至 Draft 3.1，但 OIF CEI-224G MR／LR／XSR Implementation Agreement 仍在形成；目前能辨識標準成熟度，還不能形成可靠 reach／power 或 PCB／光學份額地圖
knowledge_gain: 若正式 IA 與 multi-vendor compliance 出現，可把 PCB、CCL、retimer、LPO／CPO 的界線從題材詞改成 reach 與 power 的可測介面；現在保留 watch 可避免過早站隊
first_rejection: 若只有 draft、roadmap 與展場 demo，沒有正式 IA／標準、可重現 reach／power 邊界與量產系統，就不建立電連接與光連接的勝負或台廠收入映射。
next_evidence: 等待 IEEE 802.3dj 正式標準、OIF CEI-224G MR／LR／XSR IA、multi-vendor compliance、系統 BOM 與可核對的 reach／power 資料。
next_check: 2026-09-14
route: watch_only
sources: IEEE P802.3dj May 2026 meeting => https://www.ieee802.org/3/dj/public/26_05/index.html | OIF current work => https://www.oiforum.com/technical-work/current-work/ | OIF CEI-224G overview => https://www.oiforum.com/technical-work/hot-topics/common-electrical-i-o-cei-224g/
-->

<!-- research_candidate
candidate_id: RC-CXL4-DEPLOYMENT
rank: 4
title: CXL 4.0 規格至 pooled-memory deployment 代差
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: CXL 4.0 規格已發布，但公開產品與部署證據仍缺 host、switch、memory device 與 software 的共同 qualification；可併入既有 AI 記憶體分層持續追蹤
knowledge_gain: 以 specification、component qualification、multi-host pooling 與 production deployment 分層，可避免把頻寬世代直接換成記憶體需求或台廠收入
first_rejection: 若 CXL 4.0 長期沒有 host、switch、memory device 與軟體共同 qualification，不能由規格頻寬推導部署或記憶體需求。
next_evidence: 追蹤 CXL 4.0 compliance、CXL 3.2／PCIe 6 產品 qualification、multi-host pooling 部署分母與軟體支援。
next_check: 2026-09-30
route: watch_only
sources: CXL 4.0 specification release => https://computeexpresslink.org/wp-content/uploads/2025/11/CXL_4.0-Specification-Release_FINAL_Website-Copy.pdf | CXL specification index => https://computeexpresslink.org/cxl-specification/ | CXL pressroom => https://computeexpresslink.org/news/
-->

<!-- research_candidate
candidate_id: RC-AI-POWER-MAGNETICS
rank: 5
title: AI 高變比供電的磁性元件價值量
priority: p3
knowledge_value: medium
status: deferred
evidence_posture: assumption_led
why_now: 800V 到低壓的高變比轉換一定需要磁性元件，但平台與半導體 reference design 主要公開 topology 與效率，沒有可對應 universe 的變壓器／電感 BOM、規格份額或量產供應商
knowledge_gain: 若取得 production BOM，可把被動元件研究從「轉換級存在」推進到頻率、磁材、熱、尺寸與 qualification；現階段資訊增益仍不足以獨立成文
first_rejection: 若沒有可定位的量產設計、磁性元件規格與供應商／收入證據，不得由轉換級數直接推成被動元件用量或受惠排行。
next_evidence: 等待量產 reference design 或客戶文件披露 switching topology、磁性元件電氣／熱規格、BOM 位置、供應商資格與可辨識收入。
next_check: 2026-10-01
route: watch_only
sources: NVIDIA 800V power path => https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/ | TI 800V conversion reference designs => https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html
-->

## 本輪方法結果

- 研究前凍結五題；深研後兩題通過 research-grade article＋graph 契約，兩題維持 watch，一題維持 deferred。
- 升格原因是三個以上一手來源能建立可反證機制，且相對既有研究有新增知識，不是因為題材熱門。
- 兩篇都把台灣供應商 BOM、qualification、訂單、收入與獲利保留為待驗證，圖譜族群邊採 unverified。
- 下一輪優先檢查 OCP／NVIDIA 規格升版與 site／production evidence，不因單一公司新聞重排本輪初始名次。
