# 材料表寫著低損耗，整板仍可能出錯：224G PCB 從 Dk／Df 到 BER 的七關資格鏈

<!-- research_topic
topic_id: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN
schema_version: 3
status: triaged
priority: p2
captured_at: 2026-08-12
source_published_at: 2024-03-26
last_reviewed_at: 2026-08-12
review_due: 2026-09-15
source_type: mixed
publisher: OIF
publisher_domain: oiforum.com
canonical_url: https://www.oiforum.com/wp-content/uploads/OIF_CEI_Demo_OFC2024_Final.pdf
source_chain_id: 224g-pcb-material-to-ber-primary-scan-20260812
stock_ids: 6274
group_ids: pcb
trigger_type: 224g_pcb_material_channel_ber_qualification_chain
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C4
base_confidence: medium
confidence_basis: IPC 已把 Dk／Df 與成板高頻損耗列成不同測法，IEEE 802.3 貢獻把具名 M7N 材料、走線與 via 設計放進一組 224G PCB 研究，OIF 又把具名 ISI loss board、插入損耗與 BER 放進互通展示；三條獨立一手鏈足以建立七關資格框架。公開資料仍未把同一塊板的樹脂、玻纖、銅箔、stackup、coupon、via／connector、COM 與 BER 全部串起，也沒有本 universe 的 224G 量產與財務歸因
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-12
from: initial
to: inbox
reason: captured_material_measurement_board_channel_and_ber_evidence_layers
evidence: source_chain:224g-pcb-material-to-ber-primary-scan-20260812
-->
<!-- transition
date: 2026-08-12
from: inbox
to: triaged
reason: separated_seven_qualification_gates_and_preserved_same_board_and_commercial_gaps
evidence: sources:S1,S2,S3,S4,S5,S6,S7,S8,S9
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: db_reference_plane_fixture_removal_and_log_ratio_passport_added_without_thesis_or_clock_refresh
evidence: sources:S1,S4,S13,S14,S15
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **224G**：本文指每條高速電氣通道約 200 多 Gb/s 的世代名稱；不同文件可能寫 212、212.5 或 224 Gb/s，必須連同編碼、測試圖樣與介面草案一起讀，不能只比標題數字。
- **Gbps**：每秒傳送多少十億個位元；它描述原始位元速率，不等於扣除編碼、FEC 與協定負擔後的有效資料量。
- **PAM4**：每次用四個電壓層級傳送兩個位元；它提高單次傳輸資訊量，也縮小各層之間可容忍的雜訊空間。
- **56 GHz**：224G PAM4 文件常用的奈奎斯特頻率附近；這不是產品的時脈標籤，而是觀察通道損耗、反射與串擾的重要頻率點。
- **CCL（銅箔基板）**：由樹脂、玻纖等介質與銅箔組成、可再加工成多層電路板的基礎材料。
- **黏合片（prepreg）**：尚未完全固化的樹脂與補強材料，壓合後把各層電路黏成完整多層板；樹脂含量與壓合厚度會改變實際電性。
- **介電常數（Dk）**：訊號在介質中傳播速度與阻抗設計的重要輸入；同一材料用不同頻率、方向、樣品與測法得到的值可能不同。
- **介電損耗（Df）**：介質把部分訊號能量轉成熱的程度；數字較小通常代表介質損耗較低，但不包含所有導體、孔洞與連接器損耗。
- **測法與頻率**：Dk／Df 數字必須連同儀器、試片、頻率、方向、溫濕度與計算方式保存；只有一個小數不能直接跨產品比較。
- **SPDR**：用上下兩個介電共振器夾住試片、由共振變化求 Dk／Df 的方法；它和 stripline 成板方法觀察的試片與場型不同。
- **stackup（疊構）**：多層板中銅層、介質、玻纖、厚度、訊號層與參考平面的排列方式；同一材料換一個疊構，走線與孔洞表現也可能不同。
- **玻纖編織效應**：玻纖束與樹脂的 Dk 不同；差分線兩側若走過不同材料比例，可能產生延遲差與偏斜。
- **銅粗糙度**：銅面不是理想平面；高頻電流集中在表面時，較粗的路徑可能增加導體損耗。
- **coupon（測試片）**：與正式電路板用相同或相近製程一起製作、專門量測阻抗、損耗或可靠度的結構；測試片合格仍要確認它是否代表正式板的關鍵路徑。
- **插入損耗（insertion loss）**：訊號通過材料、走線、孔洞、連接器或線材後減少多少，常以 dB 表示；參考平面與去嵌入方式不同，數字不能直接相加比較。
- **S 參數（S-parameter／S-parameters）**：以頻率描述高速通道反射、傳輸與耦合的量測資料；它比一句「低損耗」更接近可重算的通道證據。
- **分貝（dB）**：用對數表示兩個同類量的比值；波幅類用 `20 log10`、功率類用 `10 log10`，必須交代被比的量與參考值，32 dB 不是 32%。
- **S21／SDD21**：S21 表示由 port 1 傳到 port 2 的傳輸係數；SDD21 則是差分輸入到差分輸出的 mixed-mode 傳輸係數，兩者不能只因都用 dB 就互換。
- **參考平面（reference plane）**：量測結果被定義在哪兩個電氣位置之間；平面移到 connector、fixture 或 DUT 端，包含的路徑就會改變。
- **治具（fixture）**：讓同軸儀器接上 PCB、connector 或元件的轉接結構；它自己也有 loss、phase shift 與 mismatch，可能比受測物更顯著。
- **校正（calibration）**：在量測前用已知標準修正儀器、線纜與指定參考平面以前的系統誤差；校正到哪裡不等於受測物已去嵌入到哪裡。
- **時間閘門（gating）**：在時域選出一段反射或不連續點並以數學方式移除／替換，再觀察頻域 S 參數如何改變；選窗本身也要保存。
- **Port extension**：用理想傳輸線假設把量測平面數學移到另一位置；它假設平坦幅度、線性相位與固定阻抗，不能自動取代完整 fixture model。
- **去嵌入（de-embedding）**：用量測或模型得到的 fixture S 參數，從「fixture＋DUT」總結果中數學移除 fixture；模型不準，去嵌入結果也會不準。
- **ISI loss board**：刻意用不同長度與損耗模擬通道衰減的測試板；ISI 是前後符號彼此干擾，板名不會自動揭露材料與疊構。
- **BGA**：晶片封裝底部以陣列焊球連接電路板的結構；訊號從封裝焊球展開到板內走線的區域叫 BGA breakout。
- **AIC**：插在主機板插槽上的附加卡；一組 standard AIC stackup 是參考板型，不代表所有伺服器板都採相同疊構。
- **PCIe**：主機與附加卡、儲存或加速器常用的高速連線規格；IEEE 文件引用 PCIe AIC 板型，不表示本文在驗證 PCIe 世代合規。
- **via 與 via stub**：via 是讓訊號跨電路板層的金屬孔；未被訊號使用的殘留孔段叫 stub，可能在高頻形成共振與額外損耗。
- **連接器不連續點**：訊號從板路進入接頭時，幾何與阻抗突然改變；連得上不表示反射、串擾與長時間錯誤率都合格。
- **loss budget（損耗預算）**：把封裝、板路、孔洞、連接器、線材與其他路徑的允許損耗分配到同一參考平面；它是設計限制，不是單一材料的成績。
- **COM**：Channel Operating Margin，以通道模型、發射端、接收端、雜訊與等化假設估算操作餘裕；模型通過仍須用實體硬體驗證。
- **BERT**：位元錯誤率測試儀，產生已知資料圖樣並比較接收結果；要交代圖樣、資料率、錯誤門檻、測試長度、FEC 與儀器配置。
- **PRBS**：用固定規則產生、看似隨機的已知位元序列，供 BERT 重現與比較；PRBS13Q 與 PRBS31Q 等圖樣的壓力條件不同。
- **BER（位元錯誤率）**：錯誤位元數除以總傳輸位元數；若沒有總位元數、錯誤數、測試期間與信賴界線，就不能把「零錯誤」當成零風險。
- **FEC（前向錯誤更正）**：接收端用額外編碼修復一定範圍的錯誤；FEC 後通過不代表原始通道沒有錯，也不能和 FEC 前 BER 混為同一指標。
- **link establishment（建立連線）**：兩端成功協商並開始傳輸；它早於完整 BER、壓力、環境、可靠度與量產資格。
- **互通展示（interoperability demo）**：多家公司元件在指定組合與條件下共同工作；它只支持公開的那組拓撲、儀器與測項。
- **資格驗證（qualification）**：客戶或標準組織依明定條件確認材料、電路板或系統可採用；材料合格、板廠製程合格與整機通道合格是三張不同證書。
- **QPL**：標準組織維護的合格產品清單；每一列只支持列出的公司、料號、規格段落、場址與有效日期。
- **IPC-4103**：IPC 的高速／高頻基材規格家族；slash sheet 17、在製 C 版與整板 224G 資格不是同一件事。
- **M7N**：IEEE contribution 對一組 reference PCB 使用的具名材料代號；它只屬該設計研究，不能替其他材料或量產板背書。
- **TU-1300N／TU-1300E**：台燿列在 IPC-4103/17 QPL 的兩個基材料號；列名範圍不包含本文尚缺的同板 224G BER。
- **CEI-224G**：OIF 推進的 224G class 電氣介面系列，依封裝內、模組、晶片間或背板距離分成 XSR、VSR、MR、LR 等 project。
- **SerDes**：把平行資料轉成高速串列訊號並在另一端還原的收發器；它的等化與雜訊能力會影響同一通道的 BER。
- **MR／LR**：OIF 的中距與長距電氣介面類別；不同 reach 與 connector 數會改變材料與通道要求。
- **P802.3dj**：IEEE 802.3 正在推進的 200 Gb/s lane 與 200G 到 1.6T Ethernet amendment 專案。
- **D3.2**：P802.3dj 的一個 ballot draft 版本；草案編號不是正式標準版本，也不證明產品通過。
- **ILT**：在兩端建立高速連線時交換訓練資訊、調整通道參數的機制；少量實作表示生態系尚不能假設所有組合都支援。
- **IPC-4103C**：IPC-4103 正在修訂的 C 版 working draft；它和現行 QPL 的 IPC-4103/17 列項不能互換。
- **MEGTRON 9**：Panasonic 對高速低損耗電路板材料使用的產品系列名稱；event page 的 224G readiness 仍要由同板資格資料驗證。
- **OFC**：光纖通訊產業的年度會議與展覽，OIF 在此進行互通展示；展場 demo 不等於量產 qualification。

### 三句話抓重點

- 材料規格表的 Dk／Df，只是高速連線的第一組輸入；玻纖、銅面、疊構、走線、孔洞、連接器與收發器仍會共同決定通道結果。
- IPC、IEEE 與 OIF 的公開資料已分別提供材料／成板測法、224G 板路設計，以及含插入損耗與 BER 的互通展示，但本輪沒有一份公開資料把它們串成同一塊板的完整病歷。
- 台燿兩個料號列入 IPC-4103/17 QPL，只能證明該規格段落的基材資格；它不能改寫成 224G 整板 BER、具名客戶量產、份額、價格或收入。

### 為什麼重要

**材料表像食材標籤，不是整桌菜的驗收單。** Dk／Df 可以幫工程師選料與建模，但正式板還要
決定樹脂含量、玻纖樣式、銅面、壓合厚度、走線幾何、孔洞與連接器。任何一項改變，都可能讓
規格表上的材料數字和實際通道出現距離。

**損耗合格也不是錯誤率證書。** 接收端能否正確判斷資料，還取決於發射端、接收端、等化、
雜訊、串擾、測試圖樣與 FEC。研究時如果只看到「低損耗」或「224G ready」，下一個問題應是
「在哪個測法、哪塊板、哪個參考平面、哪組收發器、跑了多少位元」。

**把關卡拆開，才知道公司證據缺在哪裡。** 材料商可以證明料號與基材資格，板廠要證明指定
stackup 與量產一致性，系統端要證明完整通道與 BER。只有同一產品與同一期間能由客戶、公司及
財務文件雙向核對，才有資格討論訂單、單價、份額與獲利。

### 接下來怎麼追

- 先取得同一 reference board 的材料料號、樹脂與玻纖結構、銅箔等級、層數、介質厚度、線寬／線距、via stub 與連接器型號。
- 再保存 Dk／Df 的測法與頻率、coupon 的 S 參數、去嵌入參考平面，以及 package-to-package 完整 loss budget。
- BER 測試要同時記錄收發器、資料率、PRBS 圖樣、FEC 前後、總位元數、錯誤數、測試期間、溫度與供電條件。
- 最後要求至少兩個獨立元件組合與量產板重現結果，再由平台端與台灣公司端對上料號、認證、出貨與財務分母。

### 想一想

- 兩張材料表都寫 Df 0.002，若一張在 10 GHz 量、一張在其他頻率與試片量，它們真的是同一成績嗎？
- 一塊測試片的直線走線損耗合格，能替正式板上的 BGA breakout、via、連接器與較長路徑背書嗎？
- 一場展示讓連線建立並量到 BER，若沒有公開 laminate、stackup 與總位元分母，能反推哪一家材料的規格與市占嗎？
- 若更好的收發器等化或 FEC 吸收了通道損耗，材料升級需求會增加、延後，還是只轉移到特定 reach？

## 主張與證據帳本

本文的「證實」只涵蓋指定測法、設計貢獻、展示配置、標準進度與 QPL 列項。七關資格鏈是跨來源
推論；同板完整鏈、量產多來源重現與公司財務仍是待驗證主張。

<!-- research_source
source_id: S1
role: standard
source_kind: living_index
publisher: IPC
title: IPC TM-650 Test Methods Manual
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.ipc.org/test-methods
locator: 2026-08-12 的 Electrical Test Methods；TM 2.5.5.14 為成板高頻訊號損耗與傳播的頻域方法，TM 2.5.5.15 為 SPDR Dk／Df，並另列 stripline、TDR 與其他 Dk／Df 方法
limitation: 方法索引證明測項與方法不同，不提供任何 224G 料號、同板 stackup、測試結果、BER、量產資格或公司財務；動態頁可能隨方法版本更新
independence_group: ipc-test-methods
-->

<!-- research_source
source_id: S2
role: standard
source_kind: living_index
publisher: IPC
title: IPC Status of Standardization
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.ipc.org/Status
locator: 2026-08-12 的 Working Draft 區；IPC-4103C 高速／高頻基材、IPC-4414 超低 Dk 玻纖及 IPC-4562C 金屬箔仍列 working draft
limitation: 工作草案狀態不代表正式版內容、通過日期、任何公司料號符合新版本，或新版本必然改變價格與份額
independence_group: ipc-standards-status
-->

<!-- research_source
source_id: S3
role: standard
source_kind: document
publisher: IEEE 802.3
title: 224G Package and PCB Investigations and COM Reference Model
published_at: 2022-03-17
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.ieee802.org/3/df/public/22_03/mli_3df_01_220316.pdf
locator: PDF pp.20–27；package-PCB co-modeling、M7N standard PCIe AIC stackup、56 GHz trace loss、skip-layer trade-off、via stub effects與 PCB design summary
limitation: 這是一份 2022 task-force contribution，不是 2026 最終標準、量產 qualification 或跨公司統計；公開頁沒有同一板的完整 Dk／Df 測法、玻纖、銅箔、連接器、實測 BER 與公司財務
independence_group: ieee-8023-pcb-study
-->

<!-- research_source
source_id: S4
role: standard
source_kind: document
publisher: OIF
title: OIF CEI-112G and CEI-224G Demonstrations at OFC 2024
published_at: 2024-03-26
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.oiforum.com/wp-content/uploads/OIF_CEI_Demo_OFC2024_Final.pdf
locator: PDF pp.8–10；CEI-224G reach／BER 目標、VSR 的 Cadence silicon、Wilder／MultiLane ISI board、Keysight BERT、PRBS31Q PAM4 212.5 Gbps、32 dB die-to-die insertion loss at 56 GHz，以及 LR multi-vendor connector／cabling 配置
limitation: 單次展示只支持公開拓撲與儀器；沒有公開 laminate 料號、Dk／Df 測法、玻纖、銅箔、完整 stackup、總傳輸位元分母、長期可靠度、量產良率或台灣公司財務
independence_group: oif-ofc2024-demo
-->

<!-- research_source
source_id: S5
role: standard
source_kind: living_index
publisher: OIF
title: Current OIF Work
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.oiforum.com/technical-work/current-work/
locator: 2026-08-12 的 CEI-224G XSR／VSR／MR／LR project；MR 目標至少 500 mm 與一個 connector，LR 目標至少 1000 mm 與兩個 connectors，均為 advanced materials 上的在製 IA project
limitation: Project objective 不是完成 IA、產品通過或客戶部署；advanced materials 沒有指定本 universe 料號、供應商、stackup、成本或份額
independence_group: oif-cei-current-work
-->

<!-- research_source
source_id: S6
role: standard
source_kind: living_index
publisher: IEEE 802.3
title: IEEE 802.3 Ballot and Task Force Review Announcements
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.ieee802.org/3/ballots/announce.html
locator: 2026-08-12 查得 P802.3dj D3.2 為第二次 Standards Association recirculation ballot，期間 2026-07-31 至 2026-08-15 AOE
limitation: Ballot 進度只描述標準程序；在正式發布前內容仍可修改，也不證明任何材料、板、連接器或系統已通過量產資格
independence_group: ieee-p8023dj-ballot
-->

<!-- research_source
source_id: S7
role: standard
source_kind: document
publisher: Ethernet Alliance
title: From Plugfest to Progress - Key Lessons from the 2025 HSN Plugfest
published_at: 2026-03-31
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://ethernetalliance.org/blog/2026/03/31/from-plugfest-to-progress-key-lessons-from-the-2025-hsn-plugfest/
locator: 224G-focused plugfest 段落；約 90% link establishment、約 10% failure，並明示 ILT 尚屬 minimally implemented 及仍有 untested areas
limitation: 文章沒有公布組合總數 N、逐配置分母、信賴區間、完整 BER、壓力條件、材料與 stackup；因此不能重算不確定度、比較供應商或把 link-up 率當量產良率
independence_group: ethernet-alliance-plugfest
-->

<!-- research_source
source_id: S8
role: company_release
source_kind: document
publisher: Panasonic Industry
title: Panasonic Industry Electronic Materials is Enabling the 224 Gbps Revolution with MEGTRON 9
published_at: 2025-01-15
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://na.industrial.panasonic.com/whats-new/panasonic-industry-electronic-materials-enabling-224-gbps-revolution-megtron-9
locator: 2025-01-15 event page；公司稱其高速低損耗 laminate 已準備面對 224 Gbps，並邀請 DesignCon 來賓討論 MEGTRON 9 如何適用 future designs
limitation: 這是公司活動與產品路線主張；沒有同板 Dk／Df-to-BER data、multi-source qualification、具名客戶、量產分母、價格、份額或財務資料
independence_group: panasonic-megtron9
-->

<!-- research_source
source_id: S9
role: standard
source_kind: living_index
publisher: IPC
title: IPC-4103 Qualified Products List
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.ipc.org/ipc-validation-services-qualified-products-list-qpl-ipc-4103
locator: 2026-08-12 的 Taiwan Union Technology Corp 列；TU-1300N 與 TU-1300E 共兩個料號列為 IPC-4103/17，listing 2022-08-30，expiration 2027-08-30
limitation: N=2 是該頁具名 QPL 列項數，不是抽樣或市場份額；IPC-4103/17 基材資格不等於 IPC-4103C、224G reference board、BER、客戶量產或收入
independence_group: ipc-qpl
-->

<!-- research_source
source_id: S10
role: company_release
source_kind: living_index
publisher: Taiwan Union Technology Corp
title: TUC Product Portfolio
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.tuc.com.tw/products2
locator: 2026-08-12 的產品表；包含 ThunderClad 400G／TU-885 Sp、ThunderClad 3+／TU-933+ 與其他低損耗產品，供未來追料號、datasheet 與應用更新
limitation: 產品分類與應用欄不是 224G 整板 qualification、客戶採用、出貨、價格、份額或財務證據；動態目錄不能替代正式附件
independence_group: tuc-product-catalog
-->

<!-- research_source
source_id: S11
role: standard
source_kind: living_index
publisher: OIF
title: OIF Interoperability Demos and Showcase Displays
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.oiforum.com/meetings-events/oif-interoperability-demos-showcase-displays/
locator: 2026-08-12 可見 2024、2025、2026 的 CEI-224G 展示索引，以及 2026-09-21 至 09-23 ECOC 的 224G／448G demo 入口
limitation: 活動索引只供找新展示附件；不能替代測試矩陣、完整材料／stackup、BER 分母、正式 IA、量產板資格或公司財務
independence_group: oif-demo-index
-->

<!-- research_source
source_id: S12
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-08-12 起追蹤 PCB／CCL 族群法說、季報、重大訊息、具名高速料號、客戶資格、量產與財務分母
limitation: 查詢入口本身不證明任何公司有 224G qualification、訂單、收入、價格、份額或毛利
independence_group: twse-mops
-->

<!-- research_source
source_id: S13
role: standard
source_kind: living_index
publisher: IEEE 802.3
title: P802.3dj Tools and Channel Data
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.ieee802.org/3/dj/public/tools/index.html
locator: 2026-08-12 的 P802.3dj tools、COM code、test fixture 與 channel S-parameter data 入口，供未來查找 reference channel 與重算資料
limitation: 工具與通道檔存在不表示其包含完整 laminate／stackup／製程病歷，也不代表任何公司產品通過 qualification 或量產
independence_group: ieee-p8023dj-tools
-->

<!-- research_source
source_id: S14
role: standard
source_kind: living_index
publisher: NIST
title: NIST Guide to the SI, Chapter 8
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-8
locator: §8.7 Logarithmic quantities and units；波幅類 level 為 20 lg(F／F0) dB、功率類為 10 lg(P／P0) dB，且報告時必須給定 quantity nature 與 reference level
limitation: NIST 只定義對數量與單位，不定義 224G channel、S-parameter port／mode、fixture、reference plane、合規門檻或任何產品結果；本文把公式用於 insertion-loss 教材時仍需額外明示匹配與參考平面條件
independence_group: nist
-->

<!-- research_source
source_id: S15
role: other_primary
source_kind: living_index
publisher: Keysight Technologies
title: Removing Unwanted Effects from the Measurement
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://helpfiles.keysight.com/csg/N1930xB/ToolsAndUtilities/Removing_Unwanted_Effects_from_the_Measurement.html
locator: Calibration to the reference plane、Gating、Port Rotation／Extension 與 De-embedding 段落；fixtures／probes 會加入 loss 與 discontinuity，port extension 假設理想傳輸線，de-embedding 以準確線性模型或實測 S 參數移除 fixture 的 loss／phase／mismatch
limitation: 這是量測儀器供應商對其 PLTS 流程的技術文件，支持方法責任與限制，不是 IPC／IEEE／OIF 共同合規規範，也沒有 224G board、材料、測試不確定度、客戶 qualification 或財務結果
independence_group: keysight-measurement-method
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: IPC TM-650 將材料 Dk／Df 與成板高頻損耗列成不同方法：2.5.5.15 使用 SPDR 求 Dk／Df，2.5.5.14 則用頻域方法量測 printed board 的高頻訊號損耗與傳播；同一索引還列出 stripline、TDR 與其他 Dk／Df 方法
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-08-12
basis: S1 Electrical Test Methods 列表直接列出各方法編號、測量對象、方法名稱與版本月份
boundary: 方法清單不表示不同方法的數字可直接互換，也不證明任何 224G 材料、板或系統通過
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
claim: 一份 2022 IEEE 802.3 task-force contribution 在 standard PCIe AIC stackup 上具名 M7N 材料，列出 56 GHz 下 regular stripline 2.8 dB/in、skip-layer stripline 1.9 dB/in，並建議 224G PAM4 設計的 via stub 小於 8 mil
supporting_source_ids: S3
contrary_source_ids:
as_of: 2022-03-17
basis: S3 PDF pp.21–23 直接列出 stackup、材料、兩種 routing loss 及 via stub 建議
boundary: 這是一個設計研究配置與 task-force contribution，沒有統計樣本或 SE，也不是最終標準、同板實測 BER、量產規格或任何材料商的普遍成績
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
claim: OIF OFC 2024 的 CEI-224G-VSR 展示把 Cadence test silicon、Wilder／MultiLane ISI loss channel board 與 Keysight BERT 放在同一配置，讓 PRBS31Q PAM4 212.5 Gbps 訊號通過 56 GHz 時 die-to-die insertion loss 32 dB 的板路並量測 BER
supporting_source_ids: S4
contrary_source_ids:
as_of: 2024-03-26
basis: S4 PDF pp.8–9 的拓撲圖與文字直接列出參與元件、圖樣、速率、loss 與 BER measurement
boundary: 這是一組 demo 拓撲；未公布 laminate、Dk／Df 方法、玻纖、銅箔、stackup、總位元分母與長期環境結果，不能反推單一材料或量產良率
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C4
label: inference
status: active
claim: 對本輪公開來源而言，224G PCB 至少要分成材料數字、測法、reference stackup、coupon／板級不連續點、完整通道 loss budget、BER／FEC，以及跨廠量產與公司歸因七關；通過任一關都不能替下一關背書，因為 IPC、IEEE 與 OIF 分別公開了不同相鄰關卡，卻沒有一條來源完成同板全鏈
supporting_source_ids: S1,S3,S4,S5,S7,S8,S9
contrary_source_ids:
as_of: 2026-08-12
basis: S1 分開材料與成板測法，S3 把材料、stackup、trace 與 via 放在設計研究中，S4 把 loss board 與 BER 放在展示中，S5／S7 縮窄標準與互通成熟度，S8／S9 顯示公司 roadmap 與 QPL 又是不同證據時鐘
boundary: 這是對已審閱來源集合的責任分層，不宣稱窮盡全球所有私有 qualification，也不推導材料升級幅度、供應商勝負、價格、份額、收入、股價或市場是否反映
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
claim: 截至 2026-08-12，IPC-4103C、IPC-4414 與 IPC-4562C 仍列 working draft；OIF CEI-224G MR／LR 仍以 project 形式描述 reach objective；IEEE P802.3dj D3.2 正在第二次 Standards Association recirculation ballot，預定 2026-08-15 AOE 結束
supporting_source_ids: S2,S5,S6
contrary_source_ids:
as_of: 2026-08-12
basis: 三個標準組織的現行 status、current work 與 ballot 頁直接列出草案／project／ballot 狀態與日期
boundary: 進入後段 ballot 不等於內容不再修改、正式發布或產品自動符合；working draft 也不能用來宣稱公司已完成新版本認證
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
claim: Ethernet Alliance 對 2025 首場 224G-focused HSN plugfest 的公開摘要稱所有互通組合約有 90% 成功建立連線，同時指出約 10% 的失敗、ILT 僅少量實作且仍有未測區域
supporting_source_ids: S7
contrary_source_ids:
as_of: 2026-03-31
basis: S7 224G plugfest lessons 段落直接提供約略結果與未完成項目
boundary: 來源未揭露組合總數 N、逐配置結果或統計不確定度，故本文不計 SE、不比較公司，也不把 link establishment 改寫成 BER、量產良率或生態系完成率
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
claim: Panasonic Industry 於 2025-01-15 以 MEGTRON 9 表示其高速低損耗 laminate 已準備面對 224 Gbps，並邀請 DesignCon 參觀者討論該材料如何適用未來設計
supporting_source_ids: S8
contrary_source_ids:
as_of: 2025-01-15
basis: S8 標題、日期與正文直接支持公司 224 Gbps readiness／future design 的精確主張
boundary: 公司活動頁不是同板 Dk／Df-to-BER、multi-source qualification、具名客戶、量產分母、份額、價格或財務證據
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
claim: 截至 2026-08-12，IPC-4103 QPL 對 Taiwan Union Technology Corp 列出 TU-1300N 與 TU-1300E 兩個 IPC-4103/17 基材料號，listing date 為 2022-08-30、expiration date 為 2027-08-30
supporting_source_ids: S9
contrary_source_ids:
as_of: 2026-08-12
basis: S9 同一 QPL 表列直接提供公司、兩個料號、slash sheet 與日期
boundary: 兩個列項是完整頁面列示、不是抽樣；IPC-4103/17 資格不等於在製 IPC-4103C、224G reference stackup、整板 BER、具名客戶量產、訂單或收入
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: unverified
status: active
claim: 有一塊可公開重算的 224G reference board，同時揭露 laminate 料號、Dk／Df 測法與頻率、樹脂／玻纖、銅箔粗糙度、完整 stackup、coupon S 參數、via／connector、COM、FEC 前後 BER 與 multi-vendor 重現結果
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: S3 完成材料／stackup／trace／via 的部分鏈但沒有同板 BER；S4 完成 loss board／BER 的部分鏈但沒有材料與 stackup；其餘來源也未補齊同一 board identity
boundary: 本輪未找到不等於全球不存在；在可重算資料出現前，不把不同板、不同年份或不同測法的數字拼成同板結果
verification_needed: 系統商或標準組織發布固定 board ID、材料與製程 manifest、原始 S-parameter／COM 檔、BERT 配置、總位元數、錯誤數、FEC、環境條件與至少兩個獨立組合的重現資料
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: unverified
status: active
claim: universe 內任何 CCL、玻纖、銅箔或 PCB 公司已由 224G board qualification 取得可辨識料號採用、量產份額、ASP、訂單、收入或毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: S9 只支持台燿兩個 IPC-4103/17 QPL 料號；IPC、IEEE、OIF、Panasonic 與台燿產品頁沒有完成同一 224G board、客戶、量產與財務的雙向核對
boundary: 一般高速材料能力、400G 產品分類、QPL、roadmap、demo 或產業需求只形成搜尋入口，不構成 224G 受惠事實
verification_needed: 具名平台或客戶與台灣公司同時對上相同料號、reference stackup、224G channel／BER qualification、量產板分母、出貨期間、單價及可辨識收入或毛利
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: verified
status: active
claim: NIST 對 dB 的定義把波幅類量寫成 20 lg(F／F0) dB、功率類量寫成 10 lg(P／P0) dB，並要求報告 logarithmic level 時交代 quantity nature 與 reference level
supporting_source_ids: S14
contrary_source_ids:
as_of: 2026-08-14
basis: S14 §8.7 直接列出 field quantity、power quantity、bel／decibel 公式與 reference level 報告規則
boundary: 這只定義 dB 的數學與表達，不替任何 224G S-parameter 選擇 port、mixed mode、頻率、reference plane、fixture removal 或 pass threshold
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
claim: Keysight 的量測文件把 calibration、gating、port extension 與 de-embedding 分成不同操作：fixture／probe 會加入 loss 與 discontinuity；port extension 假設 fixture 是理想傳輸線，de-embedding 則需用準確線性模型或實測 fixture S 參數移除其 loss、phase shift 與 mismatch
supporting_source_ids: S15
contrary_source_ids:
as_of: 2026-08-14
basis: S15 的 opening、Gating、Port Rotation／Extension 與 De-embedding 段落直接列出各方法用途、假設與資料需求
boundary: 儀器方法文件不證明任一公開 224G demo 已採某方法或去嵌入正確，也不替 board、material、SerDes、BER、客戶 qualification 或財務背書
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
claim: 每筆 224G PCB dB 證據應保存 quantity／sign、S-parameter 與 mixed-mode direction、frequency sweep、reference impedance、measurement／device planes、fixture-removal method／model、segment identity／length normalization，以及 raw complex data／重複量測與不確定度；缺任一欄都不能把不同報告的 dB 直接相加、相減或排名
supporting_source_ids: S1,S3,S4,S13,S14,S15
contrary_source_ids:
as_of: 2026-08-14
basis: S1 分開材料與成板 loss 方法，S3／S4 的 dB 位於不同 board 與目的，S13 保存 channel／tool data 入口，S14 要求 quantity／reference 明確，S15 顯示 reference plane 與 fixture-removal 操作會改變所報 DUT 範圍；合併形成本文的 dB 參考面護照
boundary: 護照是研究中心的可比性框架，不是 IPC／IEEE／OIF 新增的共同表單；本輪沒有同一 board 的 raw／de-embedded pair、方法間偏差分布或供應商比較樣本
verification_needed: 同一 224G board 公開 calibrated raw S-parameters、fixture model／measurement、gating／port-extension／de-embedding settings、reference planes、重複量測、不確定度、COM 與 BER，讓獨立 reviewer 可重建每一步
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C14
label: inference
status: active
claim: 若把 OIF demo 公開的 56 GHz die-to-die insertion loss 32 dB 依標準傳輸係數記成 -32 dB，則 transmitted／incident wave amplitude ratio 為 10^(-32／20)=0.0251188643150958；只在 matched power-wave 條件下，其平方對應 power ratio 10^(-32／10)=0.000630957344480193，即 0.0630957344480193%，而不是 32%
supporting_source_ids: S4,S14
contrary_source_ids:
as_of: 2026-08-14
basis: S4 提供 32 dB at 56 GHz 的具名 demo quantity；依 S14 的 20 lg amplitude／10 lg power 定義，以 Python Decimal 50 位精度與獨立 awk 路徑重算，兩路分別一致到顯示精度
boundary: 這是 N=1 個既有 demo dB 值的條件式確定性單位展開，沒有 sampling SE／t；它不是 PCB efficiency、熱耗散比例、寬頻資料能量、BER、材料貢獻、另一配置比較或公司財務證據，且公開來源沒有足夠欄位重建完整 fixture／reference-plane 處理
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 先用七關看懂：一個「低損耗」標籤還缺什麼

| 本文七關 | 這一關真正要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 材料身分 | 料號、樹脂系統、玻纖、銅箔與版本可辨認 | Panasonic 具名 MEGTRON 9；IPC QPL 具名台燿 TU-1300N／E | 同一 reference board 的完整 material manifest | 產品名或 QPL 不等於 224G 整板合格 |
| 2. 測法對齊 | Dk／Df 的試片、頻率、方向、溫濕度與計算方式相同或可換算 | IPC 分別列出 SPDR、stripline 與其他 Dk／Df 方法 | 料號的原始量測條件、重複測量與不確定度 | 只看一個 Df 小數不能跨產品排名 |
| 3. reference stackup | 層數、介質厚度、樹脂／玻纖比例、銅面與線路幾何固定 | IEEE contribution 具名 M7N 與 standard PCIe AIC stackup | 可製造的 Gerber／stackup、材料 lot 與 coupon 對照 | 同材料換疊構仍可能得到不同通道 |
| 4. coupon 與板級不連續點 | 走線、BGA breakout、via、connector 的 S 參數與參考平面可重算 | IEEE 有 trace／via 設計；OIF 有 ISI loss board | 同板原始 S 參數、去嵌入方法與製程 lot | 直線 coupon 合格不能替正式板所有路徑背書 |
| 5. 完整通道 loss budget | package、PCB、via、connector、cable 在同一參考平面閉合 | OIF 公布部分 die-to-die loss；IEEE 提供 COM reference model 研究 | package-to-package channel manifest 與 COM input／output | 一個 dB 數字不表示損耗來自哪個元件 |
| 6. BER 與 FEC | 收發器、圖樣、總位元、錯誤數、FEC 前後、環境與門檻完整 | OIF 展示有 BERT／BER measurement；未公布完整分母 | 原始 error counter、測試時間、FEC 與環境條件 | 建立連線、眼圖或 FEC 後 pass 不等於 raw BER 相同 |
| 7. 跨廠量產與公司歸因 | 多個組合、量產 lot、客戶 qualification、出貨與財務可雙向核對 | Plugfest 有廣泛組合但 N 未揭露；台燿只有相鄰 QPL 證據 | 至少兩組獨立硬體、量產板與買賣雙方文件 | 展示、roadmap 或 QPL 不等於份額、價格、收入與獲利 |

七關不是固定要依序排隊的專案流程：板廠可能在標準定稿前先做客戶板，收發器也可能用更強等化
補償既有通道。這個框架只要求每一關各有自己的證據，不讓一張證書跨級使用。

## 為什麼同一材料會出現不同 Dk／Df

Dk／Df 不是貼在材料上的永恆常數。實際量測至少要回答五件事：

| 問題 | 會改變什麼 | 讀者要保存的欄位 |
|---|---|---|
| 用什麼試片與場型？ | 電場落在樹脂、玻纖與空氣的比例不同 | SPDR、stripline 或其他方法，以及試片厚度與方向 |
| 在什麼頻率量？ | 材料與導體損耗都可能隨頻率改變 | 完整頻率點或掃頻範圍，不只一個代表值 |
| 銅還在不在試片上？ | 銅粗糙度與導體損耗可能混入有效 Dk／Df | 銅箔型態、粗糙度、蝕刻與去嵌入方法 |
| 玻纖與樹脂比例為何？ | 局部有效 Dk、阻抗與差分 skew 會改變 | 玻纖 style、樹脂含量、壓合後厚度與走線位置 |
| 在什麼環境與製程後量？ | 溫度、濕度、壓合與回焊可能改變實際電性 | 材料 lot、製程條件、溫濕度、重複次數與量測不確定度 |

IPC 同時維護材料 Dk／Df 與成板 loss 方法，正是因為兩者回答不同問題。研究中心不把不同測法的
數字塞進同一排行榜；若來源沒有完整條件，就只保存為供應商自述，不做小數點勝負。

## 三組公開證據，為何還拼不成「同一塊板」

| 公開證據 | 材料料號 | stackup／走線 | via／connector | loss | BER | 還缺什麼 |
|---|---|---|---|---|---|---|
| IEEE 2022 PCB contribution | 有，M7N | 有，standard PCIe AIC 與 regular／skip-layer | 有 via stub 與 package-PCB co-modeling；connector 未完整 | 有 56 GHz trace loss | 無同板 BER | Dk／Df 測法、玻纖、銅箔、完整連接器與 BERT 結果 |
| OIF OFC 2024 VSR demo | 未公開 | 只公開 ISI loss channel board 名稱 | 拓撲為 chip-to-module；材料與完整幾何未公開 | 有 32 dB die-to-die at 56 GHz | 有 BER measurement，但總位元分母未公開 | laminate、stackup、coupon、製程 lot、原始 BER 與環境 |
| IPC-4103 QPL | 有，台燿 TU-1300N／E | 無特定 224G board | 無 | 無同板 loss | 無 | reference board、通道與客戶量產資格 |

這張表的結論不是「資料不存在」，而是**本輪公開資料的 board identity 無法對齊**。研究者不能把
IEEE 的 M7N 板、OIF 的 ISI 板與 IPC 的台燿 QPL 料號當成同一塊板，再拼出一條看似完整的證據鏈。

## loss budget 不是把幾個 dB 隨手相加

概念上，完整電氣通道可拆成：

`封裝 → BGA breakout → PCB 走線 → via → connector／cable → PCB 走線 → 封裝`

工程模型常把各段損耗放進共同參考平面，但實際相加前要先確認：

1. 各 S 參數是否使用相同頻率網格、阻抗與端口定義。
2. 測試治具、探針與連接器是否已用一致方法去嵌入。
3. return loss、crosstalk、mode conversion 與 timing skew 是否也在模型內，而不只看 insertion loss。
4. package、PCB 與 connector 的界面是否重複計算或留下缺口。
5. COM 使用的 transmitter、receiver、equalization、noise 與 FEC 假設是否符合實際矽晶片。

IEEE contribution 的兩條走線 loss 是一組特定設計比較，OIF 的 32 dB 是另一組 die-to-die demo。
它們的參考平面、材料與目的不同，不能拿來相減後宣稱某一材料節省了多少 dB。

## 32 dB 不是 32%：先建立 dB 與參考面護照

同樣寫「插入損耗 32 dB」，可能是在 connector 外側量完整 link，也可能已把 probe、launch、
fixture 或 package 移除；可能指單端 S21，也可能指差分 SDD21；可能是 56 GHz 的單一點，
也可能是整段頻率 sweep 或每 inch 的線性擬合。數字相同，不代表量到同一段路。

### 八欄 dB 護照

| dB 護照欄位 | 每筆結果至少要寫什麼 | 缺少時會誤讀成什麼 |
|---|---|---|
| 1. Quantity 與正負號 | 正值 insertion loss 32 dB，或傳輸係數 `SDD21 = -32 dB`；不能混寫成單純 `32 dB` | 把 loss 和 gain／傳輸係數方向顛倒，甚至誤讀為 32% |
| 2. Port、mode 與方向 | S21、SDD21、SCD21 等；port 1／2 對應哪個物理端，single-ended／differential 如何轉換 | 把差分傳輸、mode conversion、return loss 與串擾當成同一數字 |
| 3. Frequency contract | 單點 56 GHz、完整 sweep 起訖、frequency grid、IF bandwidth 與平滑／擬合 | 用低頻或單點結果替整個 224G 頻帶背書 |
| 4. Reference impedance | 每個 port 的阻抗、renormalization 與 mixed-mode convention | 同一 raw network 在不同正規化下被誤當成材料或製程差異 |
| 5. Measurement／device planes | 儀器校正在哪裡、想報告的 DUT 兩端在哪裡、package／connector／launch 是否包含 | 把 probe-to-probe、die-to-die、package-to-package 與 trace-only 混在一起 |
| 6. Fixture-removal chain | calibration、gating window、port extension assumptions、fixture model／S-parameter file、de-embedding software／version | 把數學移除的路徑當成從未存在，或把模型誤差歸給 DUT |
| 7. Segment 與長度 | board ID、route、coupon、via／connector、實際長度；是 total dB、dB/in 還是兩長度差分 | 把完整通道 loss 和單位長度 trace loss直接相加、相減或排名 |
| 8. Raw data 與量測品質 | complex S-parameters、原始與處理後 pair、repeat count、校正狀態、不確定度與異常處理 | 只剩一張曲線截圖，無法重跑、檢查去嵌入或估計量測變異 |

NIST 要求 dB 報告先說明 quantity nature 與 reference level；對高速板路，這個要求還要延伸到
port、mode、frequency 與物理 reference plane。研究中心不以 `dB` 這個共同單位替不同量測
自動建立可比性。[S14]

### 校正、時間閘門、port extension 與去嵌入不是同一個按鈕

| 操作 | 它做什麼 | 它需要／假設什麼 | 不能替代什麼 |
|---|---|---|---|
| Calibration | 修正儀器、線纜與已知 standards，把可量測平面固定下來 | 可追溯的 calibration standards、頻率與 port 設定 | 不能自動移除 calibration plane 後方的 PCB launch／fixture |
| Gating | 在時域選一段不連續點並數學移除或替換，再看頻域 S 參數改變 | 明示 time window、電氣延遲、替換方式及 before／after data | 不能把複雜 fixture 無條件變成理想線，也不能隱藏被裁掉的物理問題 |
| Port extension | 把 measurement plane 延伸到 DUT 端 | fixture 近似 flat magnitude、linear phase、constant impedance 的理想傳輸線 | 不能處理所有 mismatch、frequency-dependent loss 與 mode conversion |
| De-embedding | 用模型或實測 fixture S 參數，從 fixture＋DUT 總結果移除 fixture 的 loss、phase 與 mismatch | 準確 fixture model／measurement、正確方向、port／mode 與穩定數學處理 | 不能讓錯誤模型變正確，也不能替代 raw data、repeatability 與 uncertainty |

Keysight 把這四種操作明確分開，並提醒 probe／fixture 本身會加入 loss 與 discontinuity。
因此一張 `de-embedded` 曲線必須附上「移除了什麼、用哪一份模型、平面從哪裡移到哪裡」；
只保存處理後圖片，不能讓另一位 reviewer 判斷改善來自 DUT 還是 fixture model。[S15]

### 把 OIF 的 32 dB 展開一次，但不把它改寫成效率

OIF 的 2024 VSR demo 公開一個 `32 dB die-to-die insertion loss at 56 GHz` 配置。[S4]
若只為教學，把正值 loss 改寫成傳輸係數 `-32 dB`，依 NIST 的對數定義可得：

- transmitted／incident wave amplitude ratio：`10^(-32/20) = 0.0251188643150958`。
- 只有在 matched power-wave 條件下，power ratio 才可寫成其平方：`10^(-32/10) = 0.000630957344480193 = 0.0630957344480193%`。

這不表示「有 99.9369% 的資料消失」或全部變成 PCB 熱。S 參數是在特定頻率、port、阻抗與
reference plane 下的線性傳輸比；反射、mode conversion、等化、寬頻波形、FEC 與接收判定
仍在別的帳。32 dB 也不是 32%，因為 dB 是對數比值。

樣本與誤差邊界：這是 **N=1 個既有 demo dB 值**的確定性條件換算，沒有 sampling SE／t。
Python Decimal 50 位精度重算的 wave ratio 為
`0.025118864315095801110850320677993273941585181007825`、matched power ratio 為
`0.00063095734448019324943436013662234386467294525718823`；獨立 awk 路徑分別為
`0.025118864315096` 與 `0.000630957344480`。兩路一致只證明代數，沒有補齊 OIF 未公開的
fixture model、完整 frequency data、BER 分母或材料病歷。

### 多空小作文必須先固定同一個 plane

| 敘事 | 合理假說 | 必須再看到的共同證據 | 什麼會讓敘事失效 |
|---|---|---|---|
| 偏多：高頻量測與低損耗內容增加 | 224G loss budget 變緊，可能增加高階 CCL／銅箔／玻纖、coupon、VNA／BERT 與去嵌入驗證的技術與工時需求 | 同一 board／route 的 raw＋de-embedded data、fixture chain、材料 A／B、COM／BER、量產 lot、工具／材料用量、價格與財務分母 | 只有 dB headline 或儀器處理後曲線，沒有新增材料內容、測試工時、qualification、出貨或毛利 |
| 偏空：看似改善只是邊界或架構轉移 | 平面、fixture、長度正規化、SerDes 等化、較短 electrical reach 或光學化，可能吸收板材升級需求 | 同一 DUT 在固定 planes、同一 Tx／Rx 與同一 fixture model 下的 before／after，以及實際 BOM／reach 變化 | 拿不同 board、不同 planes 或 total dB 對 dB/in 比較，卻把差額全歸因材料 |
| 共同底線 | dB 可比性與公司獲利是兩個問題 | 量測護照、客戶 pass、具名料號、量產板分母、出貨期間與公司財務雙向核對 | 用單一 32 dB、QPL 或 roadmap 直接替代 224G design win、份額與收入 |

本輪只有 OIF demo、NIST 單位定義與 Keysight 方法文件三條定向消息鏈（N=3），不是 board、
材料 lot、產品、客戶、供應商或台灣 121 檔樣本；沒有同板 A／B effect size，也沒有可估的
sampling SE／t。因此這張護照只改善閱讀與查證，不形成公司排名或投資動作。

## 為什麼 Df 不能直接換算 BER

BER 是整條收發系統的結果，不是材料的單變數函數。即使材料與走線完全不變，下列項目仍可讓
BER 改變：

- 發射端輸出振幅、jitter 與預加重。
- 接收端類比前端、時鐘恢復與等化能力。
- 鄰近通道的串擾、電源雜訊與溫度。
- PRBS 圖樣、資料率、lane 數、測試期間與錯誤判定。
- FEC 類型、interleaving、pre-FEC 與 post-FEC 的計算位置。
- 連線訓練是否能依每條通道調整參數，以及失敗時是否降速或重試。

因此最有用的資料不是「材料通過 BER」，而是固定同一 board ID 與同一收發器後，逐步替換材料、
銅箔或 stackup，保存原始 S 參數、COM 與 BER。若沒有這種受控對照，就只能說某個完整配置通過，
不能把結果全歸功於材料。

## 標準、展示與量產各有自己的時鐘

| 證據時鐘 | 截至 2026-08-12 的公開狀態 | 它能證明什麼 | 它不能證明什麼 |
|---|---|---|---|
| IPC 材料與製程標準 | 4103C、4414、4562C 仍是 working draft | 產業正在定義高速基材、超低 Dk 玻纖與金屬箔規格 | 新版內容已定稿、任何公司已符合或價格必升 |
| IEEE Ethernet amendment | P802.3dj D3.2 正在第二次 SA recirculation ballot | 標準程序已進到後段草案與意見處理 | 最終條文、發布日期或任何產品已合格 |
| OIF CEI-224G project | MR／LR 等 reach objective 仍在 current work | 可定位不同 reach 與 connector 目標 | 正式 IA、量產板與客戶部署 |
| OIF interoperability demo | 有具名矽晶片、loss board、儀器、速率與 BER measurement | 指定展示配置可以實際運作並量測 | 材料病歷、全市場互通率、長期可靠度或量產 |
| Ethernet Alliance plugfest | 公開摘要稱約 90% link establishment；N 未揭露，ILT 仍少量實作 | 生態系已有廣泛組合，仍能觀察失敗與未測區域 | 可重算成功率不確定度、完整 BER、量產良率或供應商排名 |
| 公司產品與 QPL | Panasonic 有 224G roadmap；台燿有 IPC-4103/17 QPL | 公司具名產品方向與基材資格可定位 | 224G 同板資格、客戶採用、份額、ASP、收入或毛利 |

越接近標準定稿與互通活動，不代表所有公司證據會自動同步。材料、板廠、系統商與客戶可能各自
維護私有 qualification；研究中心只在公開文件能對上同一 board、料號與客戶時升級主張。

## 台燿的 QPL 應該怎麼讀

IPC QPL 對台燿列出 TU-1300N 與 TU-1300E，兩個料號都對應 IPC-4103/17，現行頁面到期日為
2027-08-30。這是**具名、可定位、有效期明確的基材資格證據**，比「公司有高速材料能力」更具體。

但它仍停在七關中的第一至第二關附近：

- QPL 沒有說兩個料號就是 224G reference board 的材料。
- slash sheet 與 QPL 沒有替特定 stackup、via、connector 或完整通道背書。
- QPL 沒有提供 BERT 配置、總傳輸位元、FEC 前後 BER 或 multi-vendor 結果。
- QPL 沒有提供具名客戶、出貨量、價格、份額、收入或毛利。

因此圖譜會建立 `6274 台燿 → IPC-4103 基材資格` 的具名相鄰線，但邊界明寫「不是 224G 系統
資格」。若未來取得同板與客戶證據，再追加新 claim；不回頭改寫今天的 QPL 範圍。

## 用七個欄位建立可重算的 qualification 記錄

| 記錄欄 | 最低必要內容 | 缺少時的風險 |
|---|---|---|
| 1. Board identity | board ID、revision、fab site、lot、日期 | 不同板結果被錯拼在一起 |
| 2. Material manifest | laminate／prepreg 料號、resin、glass style、copper type／roughness | 無法知道 loss 改善來自哪個材料或製程 |
| 3. Stackup geometry | 層序、介質厚度、線寬／線距、參考平面、via／stub、connector | datasheet 無法轉成實際阻抗與通道 |
| 4. Material methods | Dk／Df 方法、頻率、方向、溫濕度、重複次數與不確定度 | 小數看似可比，實際量測條件不同 |
| 5. Channel data | coupon 與完整通道 S 參數、治具、去嵌入、reference plane、COM 版本 | dB 無法閉合，也不能重跑模型 |
| 6. BER contract | Tx／Rx、PRBS、rate、lane、FEC、總位元、錯誤數、時間、環境 | pass／fail 無法比較或重現 |
| 7. Qualification outcome | 測試主體、multi-vendor 組合、量產 lot、客戶簽核、失敗與修正 | 展示被誤讀成量產與公司收入 |

這七欄不是要求公司公開機密配方。材料可以用受控代碼表示，但 board identity、測法、參考平面與
結果分母至少要足以讓獨立 reviewer 確認「比較的是同一題」。

## 誰負責，誰不能替別人背書

| 角色 | 應拿出的證據 | 不能替誰背書 |
|---|---|---|
| 材料供應商 | 料號、Dk／Df 方法與頻率、樹脂／玻纖／銅箔選項、lot 一致性與 QPL | 不能單獨替板廠製程、connector、SerDes 或整板 BER 背書 |
| 玻纖與銅箔供應商 | style／粗糙度、批次、與 CCL 組合後的受控比較 | 不能由單一原料數字推成客戶 stackup 或份額 |
| CCL 廠 | laminate／prepreg 組合、壓合窗口、有效 Dk／Df 與可製造性 | 不能替所有板廠、走線幾何與系統拓撲背書 |
| PCB 廠 | 固定 stackup、coupon、阻抗、S 參數、via／connector 與量產 lot | 不能替收發器、FEC、客戶部署或材料商收入背書 |
| Connector／cable 廠 | 端口、loss／return loss／crosstalk 與機械重複性 | 不能把自己一段通道當成整條 link 結果 |
| SerDes／系統商 | COM 假設、BERT、BER、FEC、link training、環境與整機驗收 | 不能用更強等化反向證明每種材料都合格 |
| 標準組織與 plugfest | 規格、測試程序、參考通道、參與組合與結果邊界 | 不能替私有量產資格、供應商份額或財務背書 |
| 投資研究 | 對齊料號、板、客戶、量產分母與公司財務 | 不能用 roadmap、QPL 或展示補出訂單、ASP、毛利與股價方向 |

## 這篇對公司判斷的用處與界線

這篇把 PCB／CCL 研究從「誰的 Df 更低」改成「哪家公司能提供可重算的同板資格鏈」。真正能讓
公司主張升級的證據，至少要包含：

1. 具名 224G 平台或客戶與固定 board／stackup。
2. 公司具名料號、供應場址與 qualification 範圍。
3. 同板 S 參數、COM 與 FEC 前後 BER，且至少兩個獨立組合重現。
4. 量產 lot、出貨期間與客戶驗收，而非一次 demo 或 sample。
5. 同期間公司總收入分母，以及該料號可辨識的收入、單價、份額或毛利。

目前只有台燿 IPC-4103/17 QPL 形成具名相鄰證據；沒有 224G board identity、客戶與財務閉環。
所以本題適合繼續深研，不構成個股方向、價格、份額、營收、毛利、估值或交易建議。

## 來源與證據邊界

- [IPC TM-650 Test Methods Manual](https://www.ipc.org/test-methods)（材料 Dk／Df 與成板 loss 的不同測法）。
- [IPC Status of Standardization](https://www.ipc.org/Status)（4103C、4414、4562C working draft）。
- [IEEE 224G Package and PCB Investigations](https://www.ieee802.org/3/df/public/22_03/mli_3df_01_220316.pdf)（M7N、trace、via 與 COM 設計研究）。
- [OIF CEI-224G OFC 2024 demo](https://www.oiforum.com/wp-content/uploads/OIF_CEI_Demo_OFC2024_Final.pdf)（ISI loss board、BERT 與 BER measurement）。
- [OIF Current Work](https://www.oiforum.com/technical-work/current-work/)（MR／LR reach objective 與 project 狀態）。
- [IEEE 802.3 ballot announcements](https://www.ieee802.org/3/ballots/announce.html)（P802.3dj D3.2 ballot 狀態）。
- [Ethernet Alliance 2025 HSN plugfest lessons](https://ethernetalliance.org/blog/2026/03/31/from-plugfest-to-progress-key-lessons-from-the-2025-hsn-plugfest/)（link establishment 與未測邊界；N 未揭露）。
- [Panasonic MEGTRON 9 224 Gbps event page](https://na.industrial.panasonic.com/whats-new/panasonic-industry-electronic-materials-enabling-224-gbps-revolution-megtron-9)（公司 roadmap／future design 主張）。
- [IPC-4103 QPL](https://www.ipc.org/ipc-validation-services-qualified-products-list-qpl-ipc-4103)（台燿 TU-1300N／E 的具名基材資格）。
- [台燿產品目錄](https://www.tuc.com.tw/products2)（未來追料號更新的 living index）。
- [NIST Guide to the SI, Chapter 8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-8)（dB 的 amplitude／power 對數定義與 reference level 規則）。
- [Keysight：Removing Unwanted Effects from the Measurement](https://helpfiles.keysight.com/csg/N1930xB/ToolsAndUtilities/Removing_Unwanted_Effects_from_the_Measurement.html)（calibration、gating、port extension 與 de-embedding 的責任、假設及 fixture 邊界）。

本文沒有把 IEEE、OIF 或供應商的 dB、Dk／Df、link establishment 與 BER 數字做跨配置比較；
測法、參考平面、board identity、收發器與分母不同。Plugfest 約 90% 的來源沒有公布 N，故不估計
SE 或信賴區間。IEEE 與 OIF 的數字是各自完整設計／展示配置，不是抽樣市場統計。

## 影響路由

<!-- impact
group_id: pcb
stock_ids: 6274
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-15
rationale: IPC QPL 直接列出台燿 TU-1300N／E 的 IPC-4103/17 基材資格，足以建立具名產品查找入口；下一步要對上 224G reference board、stackup、BER、客戶量產與財務
evidence_boundary: QPL 是相鄰基材資格，不是 IPC-4103C、224G 整板 qualification、份額、ASP、訂單、收入或毛利
-->

## 持續驗證清單

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C5,C9
metric: IPC／IEEE／OIF 正式版本、reach、channel／test method 與可下載 reference data
source_ids: S2,S5,S6
watch_source_ids: S2,S5,S6
frequency: monthly
frequency_detail: 每月核對 IPC status、OIF current work 與 IEEE ballot；新版本只在正式文件可定位後另加 document source
next_check: 2026-09-15
trigger: IPC 正式發布相關新版、IEEE P802.3dj 正式核准／發布，或 OIF 發布 CEI-224G IA 並附可重算 channel／test contract
invalidation: 草案持續修改、reach 或測法顯著改變，或正式版本未提供材料到成板測試的可對齊欄位
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C2,C3,C4,C9
metric: 同一 224G reference board 的 material manifest、stackup、S 參數、COM、BER／FEC 與 multi-vendor 重現
source_ids: S3,S4
watch_source_ids: S11,S13
frequency: event_driven
frequency_detail: OIF／IEEE 新 demo、channel file 或 tool 出現時，先核對 board identity 與材料 manifest，再重算 reference plane、COM 與 BER contract
next_check: 2026-09-15
trigger: 固定 board ID 同時公開 laminate／glass／copper／stackup、raw S-parameters、via／connector、COM、總位元與 FEC 前後 BER，且至少兩個獨立組合重現
invalidation: 新展示仍只有 loss board 或 link-up、不同文件無法對上同一 board，或結果只在單一 vendor 私有配置成立
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C7,C8,C10
metric: 台灣 PCB／CCL 公司的具名 224G 料號、買方 qualification、量產板分母與可辨識財務貢獻
source_ids: S8,S9
watch_source_ids: S10,S12
frequency: monthly
frequency_detail: 每月檢查台燿產品與 MOPS；只有平台／客戶與公司端對上同一料號、板與期間才升級
next_check: 2026-09-15
trigger: 具名客戶與公司雙向確認相同 224G board／material qualification、量產 lot、出貨期間、數量或單價，並可對公司收入或毛利分母重算
invalidation: 只有 roadmap、一般高速／400G 產品、QPL、sample 或產業需求，沒有 224G board identity、客戶與財務閉環
-->

## 下一個可證明／否定的節點

- IEEE P802.3dj 完成 D3.2 後的正式程序結果，以及 OIF CEI-224G MR／LR 是否發布正式 IA 與測試附件。
- 一塊具名 reference board 同時公開 material manifest、stackup、raw S 參數、COM 與 BER／FEC 分母。
- 同一 board 同時保存 calibrated raw、gated／port-extended／de-embedded S 參數、fixture model、reference planes、重複量測與不確定度，讓第三方能重建 dB 處理鏈。
- 至少兩個獨立 SerDes／connector／board 組合用同一 test contract 重現，而不是只建立一次連線。
- 台燿或其他 universe 公司由客戶端與公司端同時對上具名 224G 料號、量產板、出貨與財務分母。
- 若標準長期修改、ILT／互通失敗未收斂，或收發器／光學路徑縮短板級 reach，使高階材料只限少數拓撲，C4 的適用範圍必須下修。
- 若仍找不到同板完整鏈，保留本文作為證據判讀框架；不得把不同板的數字拼成材料升級、份額或價格結論。
