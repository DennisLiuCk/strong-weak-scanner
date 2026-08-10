# Changelog

## 族群矩陣把每一站對回產業角色，並保留文章與關係圖來處 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、研究來源、主張、summary、monitor、
confidence、topic fingerprint、圖譜 edge、公司曝險與投資判斷零變動**；本次只調整學習路線
站點的 reader-only 族群標示、展開排版與文章—關係圖工作階段 origin。方法 registry fingerprint
未改變，`research_method_audit.py --baseline-ref HEAD` 通過，因此不建立內容相同的新方法快照。

- 固定走讀「族群矩陣 → 供電與散熱 → 第 1／9 站」發現，桌機展開九站路線後三個階段仍固定
  三欄；第一階段的三站全擠在左側三分之一，其餘欄只剩空白。每站只顯示讀者問題與研究節點，
  聚合卡雖列出六個相關族群，讀者仍無法判斷各站實際會接觸哪些產業角色。
- 路線 station 既有 `groupLabels` 現在逐項顯示為「這站會用到」；來源只可是同篇主文章正式
  研究範圍，不從 route 總族群、圖譜節點、題名、相似度或模型補關係。發布版四條路線共 25 站，
  25／25 都有非空族群且逐站與主文章 `groupLabels` 完全相同；另一條由
  `RESEARCH_LEARNING_ROUTES.graphIds` 獨立列舉也得到 25 站。這是完整 payload 的決定性核對，
  不是抽樣統計，SE／t／有效獨立觀測不適用。
- 桌機任一路線展開時仍跨滿問題卡整列；任一 phase 展開後再跨滿 route map，站點用至少 280px
  自適應欄寬排列。1280 × 900 實測第一階段寬 1148px，前三站各約 375px；390 × 844 維持單欄且
  `scrollWidth == innerWidth == 390`。桌機與手機都保留相同 DOM 閱讀順序、原生 details／summary、
  問句、站次、文章映射與精確追問。
- 從路線文章按「看這站證據關係」原本會以一般圖譜入口開啟，沒有文章來處、返回行動或矩陣
  origin。現在共用 article-learning origin 並另記 `route-context` 來源；圖譜首屏明示
  「文章 → 關係圖」、剛才文章與下一站。返回後仍是原文章與供電散熱矩陣路線，焦點回到同一顆
  `.learning-route-action`，不是錯誤地跳到文末延伸卡。這個狀態只存在前端工作階段，不寫入研究
  payload。
- 前後畫面、同尺寸比較與完整稽核存於
  `tmp/research-learning-audit-2026-08-11-wave108-matrix-relations/`。固定 viewport 不是實機，本輪
  未涵蓋 VoiceOver／TalkBack、200%／400% zoom、完整實體鍵盤巡覽、儀器化 WCAG 對比或真實
  讀者理解測試，因此不宣稱完整無障礙合規或實際理解成效。
- `Darwin 25.5.0 arm64`、Python 3.11.11、UTF-8 執行 508 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar 與 method audit 六項 lint 均為
  exit 0。method audit 仍如實揭露既有新鮮度、修正學習與校準提醒。連續兩次 dashboard build
  SHA 一致：`index.html`
  `82bf2fb334fb40351ce56d2448f4fec2b32594e74b927281a2463fad4652e943`、`research.html`
  `98a02078d52302476ef340a207f7c7b53dd7273d7219a585a5fbe225a740974d`。

## 市場議題首屏先用同篇白話交代已知、界線與查證方向 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、研究來源、主張、summary、monitor、
confidence、topic fingerprint、route、圖譜、公司曝險與投資判斷零變動**；本次只新增市場議題
文章的 reader-only 結論邊界 payload、窄正文欄版面與對應契約。方法 registry fingerprint 未改變，
`research_method_audit.py --baseline-ref HEAD` 通過，因此不建立內容相同的新方法快照。

- 固定走讀 AI 機櫃 EMC 議題發現，首屏「這篇目前能說到哪裡」直接重用 ledger 摘要，混有
  `AI rack EMC`、`equipment emission`、`lab capacity`、`full-rack test` 等英文與研究縮寫；
  1280px 一般模式的實際正文欄只有 365px，三卡仍並排，形成近乎逐字換行。文章末端既有
  自我檢查、下一站、公司筆記與知識圖譜承接已完整，本輪沒有再複製一套文末導覽。
- `_research_reader_boundary_brief()` 只在同篇同時有至少兩句「三句話抓重點」與一項
  「接下來怎麼追」時建立發布用 payload：`known` 逐字取第一句、`unknown` 逐字取最後一句、
  `next` 逐字取第一個追蹤動作，首屏依序標成「先知道／先別下結論／接著怎麼查」。完整研究摘要
  仍保留原始主張、待驗命題與 monitor 文字；來源不完整時安全退回原摘要，不抽長文、不讀題名，
  也不由模型補句。
- 發布版 35 篇市場議題中，34 篇具有完整 `readerBoundaryBrief`；唯一例外是未採同一新手段落
  契約的台積電事件文章 `event-tsmc-2026q2`，會使用既有摘要 fallback。這是完整發布 payload 的
  決定性列舉，不是抽樣統計，SE／t／有效獨立觀測不適用。
- 1181–1500px 且未開專注閱讀時，結論卡改為單欄；寬版專注閱讀仍保留三欄。固定瀏覽器實測
  1280 × 720 一般模式 grid 欄寬 328px、`scrollWidth == innerWidth == 1280`；390 × 844 手機
  同樣無水平溢位，同區幾何高度約由 752px 降至 654px。這只證明版面與文字密度改變，不宣稱
  真實讀者理解率已提升。
- 「看完整研究摘要」可把焦點移到「研究摘要：已知、未知與下一步」，原始技術文字仍逐字保留；
  「查本文名詞（26）」開啟 dialog 後焦點落在搜尋框，關閉後回到原按鈕。前後畫面、同尺寸比較
  與完整稽核存於 `tmp/research-learning-audit-2026-08-11-wave107-market-boundary/`。固定 viewport
  不是實機，本輪未涵蓋 VoiceOver／TalkBack、200%／400% zoom、完整實體鍵盤巡覽、儀器化
  WCAG 對比或真實讀者理解測試，因此不宣稱完整無障礙合規或實際理解成效。
- `Darwin 25.5.0 arm64`、Python 3.11.11、UTF-8 執行 508 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar 與 method audit 六項 lint
  均為 exit 0。method audit 仍如實揭露既有新鮮度、修正學習與校準提醒。連續兩次 dashboard
  build SHA 一致：`index.html`
  `82bf2fb334fb40351ce56d2448f4fec2b32594e74b927281a2463fad4652e943`、`research.html`
  `46513755cc486ffc120ff808a11c31d3dac4688641052e6ee9ce43693db45f9e`。

## 研究雷達先交代目前線索與證據缺口 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、研究排序、selection log、priority、
evidence posture、來源、主張、圖譜、公司曝險與投資判斷零變動**；本次只新增候選雷達的
reader-only 起點、發布版面與對應契約。方法 registry fingerprint 未改變，
`research_method_audit.py --baseline-ref HEAD` 通過，因此不建立內容相同的新方法快照。

- 1280×720 與 390×844 修改前畫面都顯示，候選卡在白話問題後直接跳到「接著查什麼」；
  讀者雖知道研究動作，卻沒有先看見動作所依據的已知線索與仍缺證據。8／8 個 active 候選
  現在各加入 `reader_starting_point`：第一句只摘要同一 `why_now` 已有線索，第二句固定以
  「目前還」明示證據缺口或不能跨過的推論邊界。
- parser 要求每個起點恰為兩句、32–120 字且包含「目前還」；缺欄、單句、過長或沒有邊界
  都會使 radar lint 失敗。完整 `why_now`、凍結 `next_evidence`、knowledge gain、第一拒絕與
  來源仍在預設關閉的查核區，selection log 沒有改寫。
- 候選卡閱讀順序改成「這題想弄清楚 → 先知道這件事 → 接著查什麼 → 關鍵詞 → 各族群要回答
  什麼」。桌機把起點與驗證動作並排；780px 以下依同一 DOM 順序改為單欄。沿用既有色票、
  圓角、字級與間距，沒有另造一套視覺語言。
- 固定瀏覽器實測桌機與手機 `scrollWidth == innerWidth`，分別為 1280 與 390；手機起點與下一步
  單欄排列，族群按鈕高 62px。從雷達第 1 題開啟 23 分鐘文章後，H1、hash 與 390px 寬度正確；
  返回仍恢復 `#radar`、同一候選卡與鍵盤焦點。頁面執行紀錄沒有 warning／error。
- 前後畫面、同尺寸比較與稽核素材存於
  `tmp/research-learning-audit-2026-08-11-wave106-radar-context/`。固定 viewport 不是實機，本輪
  未涵蓋 VoiceOver／TalkBack、200%／400% zoom、完整實體鍵盤巡覽、儀器化對比或讀者理解率
  測試，因此不宣稱完整無障礙合規或實際理解成效。
- `Darwin 25.5.0 arm64`、Python 3.11.11、UTF-8 執行 508 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar 與 method audit 六項 lint
  均為 exit 0。method audit 仍如實揭露既有新鮮度、修正學習與校準提醒。連續兩次 dashboard
  build SHA 一致：`index.html`
  `82bf2fb334fb40351ce56d2448f4fec2b32594e74b927281a2463fad4652e943`、`research.html`
  `908d48143d06dfa82a742590a5ed6fc3db68bfcdf5bdda8409d3e8c68639e9d1`。

## 文章清單先交代學習目標、讀後問題與證據位置 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、研究來源、主張、monitor、impact、
證據判定、複核時鐘與 `learningPathVersion` 零變動**；本次只重排研究文章清單的讀者層
介面、手機導覽預設與對應測試，不改寫任何研究 payload。建置後 `const LIB` JSON 與 Git
`HEAD` 逐 byte 相同，SHA-256 均為
`fcd37cc388506aecd30ec52cde28f706a3f94da91eb55e867e5d0f42dfa32bb5`。

- 1280×900 改寫前畫面顯示，文章卡已有讀者問題、研究題名、範圍、可信度與查核狀態，
  但「先學什麼」尚未出現，主張類型、可信度、來源數與「候選議題」邊界也分散在不同位置；
  讀者要先自行猜測文章用途。390×844 手機版的三步導覽預設全部展開，第一篇文章幾乎落在
  首屏之外。
- 274 張文章卡現在依序顯示「先認識本業／先看勝負手／先學一件事 → 讀完能回答 →
  證據位置」。第一行逐字沿用同篇 `readingMission.keyPoints[0]`，沒有重寫摘要；三種起讀
  標籤分別對應正式筆記、多空小作文與市場議題，避免把公司本業、待驗勝負手與產業概念
  混成同一種閱讀任務。
- 「證據位置」直接重用文章查核狀態；市場議題再併列同篇 `readerEvidenceGuide` 的主張類型、
  即時 `liveConfidence()` 判定與有效來源數。例如國巨 Q2 卡會顯示「候選議題・不等於正式
  公司事實 · 主張『證實』 · 可信度中 · 2 份有效來源」。這只是把既有證據標籤放到同一行，
  不把來源數換算成真實機率、受惠或投資排序。
- 桌機仍預設展開「第一次來？照三步開始」；手機只在首次載入時收起一次，使用者可原位
  展開，旋轉或 resize 不會覆寫後續手動狀態。手機首屏因此能同時看到三步導覽摘要與第一張
  文章卡；完整導覽、研究題名、範圍與證據文字均保留。
- 固定瀏覽器實測「市場議題」仍為 35／274 篇，正式筆記、多空小作文與市場議題首張卡分別
  顯示「先認識本業／先看勝負手／先學一件事」；卡片可開啟全文，焦點落到同一個讀者問題，
  返回與篩選狀態不受影響。桌機 `scrollWidth == clientWidth == innerWidth == 1280`，手機三者
  均為 390，沒有頁面水平溢位。這是完整發布 payload 與固定 viewport 的決定性契約，不是
  抽樣統計，SE／t／有效獨立觀測不適用。
- 完整前後畫面、流程紀錄與限制存於
  `tmp/research-learning-audit-2026-08-11-wave104-catalog/`。固定瀏覽器尺寸不是實機，本輪未涵蓋
  VoiceOver／TalkBack、完整實體鍵盤巡覽、200%／400% zoom、儀器化 WCAG 對比與理解率
  使用者測試，因此不宣稱完整無障礙合規或閱讀成效。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 508 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar、method audit 六項 lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被介面重排掩蓋。連續兩次 dashboard build SHA
  一致：`index.html`
  `82bf2fb334fb40351ce56d2448f4fec2b32594e74b927281a2463fad4652e943`、`research.html`
  `a6447c3b4c5728d57241f22cb8b1d8f64579476ee80c70fd35ee597a5b348be2`。

## UCIe 第八站改成五個封裝位置、五把測試尺與六關生態系證據 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有 UCIe 互通議題的讀者層文字、標題、中文優先圖譜
標籤、發布 payload 與對應測試，不改變原研究結論。該篇 `research_topic`、
`research_source`、`research_claim`、`impact` 與 `monitoring_item` 共 17 個正式區塊均與 Git
`HEAD` 逐字相同，聚合 SHA-256 維持
`049f5474f2274cc6c200f21354faeb2f024a7160a1e9db59df57347c9890bbc7`；知識圖譜 13 條
`knowledge_edge` 也逐字相同，聚合 SHA-256 維持
`a8e530716ad173e7c91139a9985ffc0d6de22e3fc55e14cf5628995ca95bf1f7`。

- 從「研究中心 → 族群矩陣 → 運算與互連 → 第八站」固定走讀發現，修改前首屏第一句直接
  放入 UCIe 3.0、64 GT/s，讀後問題接著要求理解 16G test chip；名詞速查只有 7 項。正文
  只有一張「階段／本輪證據／尚未跨過的門檻」三列表；讀者尚未看見小晶片在封裝裡有哪些
  位置，也沒有足夠欄位判斷一次互通展示測了什麼。
- `learningPathVersion` 升為 66。研究題名改成「UCIe 讓小晶片共用語言，但一次互通不代表
  生態系成熟：先分清設計、實體測試與客戶產品」；入口問句改為「把一顆大晶片拆成多顆
  小晶片後，還要通過哪些關卡，才能讓不同公司的零件一起量產？」。三句重點第一句只先建立
  同一封裝內資料、時鐘、管理訊息與錯誤狀態，名詞小字典由 7 項增為 32 項。圖譜與核心概念
  改為「UCIe 小晶片互通與量產階梯」，另追加純編輯 transition，沒有刷新來源、複核日期或
  證據時鐘。
- 核心內容先用「執行功能的小晶片／介面控制與傳輸協定／實體傳輸電路與通道／接點與封裝內
  布線／封裝整體協調與測試」五個位置建立接力；並明示這是閱讀地圖，不是完整介面分層、
  固定接線順序或封裝配方。
- 再以「傳輸率／實體路徑／協定與管理功能／廠商獨立性與晶片狀態／封裝、時間與故障條件」
  五把尺限制每筆展示的外推範圍。16 的跨廠實體展示與 64 的規格、介面送廠仍屬不同產品與
  證據物件；速度、晶片狀態或跨廠結果只要換了對象，就不能拼成一項最高速度成果。
- 共同規格、介面智財與工具、送廠設計與回片、測試晶片互通、客戶量產分成五種證據物件；
  規格聯盟、介面智財、晶片設計、晶圓製造、封裝載板測試、客戶產品與台灣財務六類角色各自
  分責，避免規格、送廠與一次展示沿著不同產品「斜著畢業」。
- 最後以「共同規格與測試合約可查 → 介面實作完成並送廠 → 實體晶片在目標速度運作 → 跨廠
  互通與正式測試對齊 → 客戶產品通過資格並量產 → 台灣公司財務足跡可雙向核對」六關分開
  技術進展與生態系成熟。本輪共同規格、64 介面送廠與 16 跨廠實體展示都各自成立，但尚未
  落在同一組 64 實體產品，因此不能升級為多廠客戶量產或公司收入。
- 1280px 與 390px 固定畫面均完成逐張開圖及同 viewport 前後對照；桌機
  `scrollWidth == innerWidth == clientWidth == 1280`，手機
  `scrollWidth == innerWidth == clientWidth == 390`。行動版五個位置、五把測試尺、五種證據
  物件、六類角色、六關成熟度與公司判斷表均重排為具欄名卡片，沒有頁面水平溢位。名詞速查
  可完整載入 32 個中文優先定義，搜尋「跨廠互通」只顯示 1／32 個名詞，關閉後焦點回到原
  按鈕；第八站可進入中文優先的公司曝險圖譜，瀏覽器主控台沒有警告或錯誤。這些是
  deterministic viewport 與互動契約，不是抽樣統計，SE／t／有效獨立觀測不適用；固定瀏覽器
  尺寸不是實機，本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、VoiceOver／TalkBack、200%／400%
  zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；第八站閱讀時間由 13 分鐘更新為 21 分鐘，族群矩陣站卡、文章題名、讀者
  問句、知識圖譜路線與正式證據數量均由建置器同步核對，`learningPathVersion: 65 → 66`。
  排除版本後 canonical payload SHA 由
  `e2927e172b0ad7a89df1138c0da3706e6ce6b1b2ed0edaa7dba4da891b09f2e8` 變為
  `5d27b5bc37f6282e61cfc8dec4046ff36e3f62652af0afd824c8b601b88cd311`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 507 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar、method audit 六項 lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被本次編輯改寫。連續兩次 dashboard build SHA
  一致：`index.html` `82bf2fb334fb40351ce56d2448f4fec2b32594e74b927281a2463fad4652e943`、
  `research.html` `3f0da9968cdaf52da1c64513a51f9b9c331ea327666cbe0cdde7a7f522c8271b`。

## PCIe 6 第七站改成五個連線位置、五把測試尺與六關部署證據 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有 PCIe 6 合規議題的讀者層文字、標題、中文優先圖譜
標籤、發布 payload 與對應測試，不改變原研究結論。該篇 `research_topic`、
`research_source`、`research_claim`、`impact` 與 `monitoring_item` 共 20 個正式區塊均與 Git
`HEAD` 逐字相同，聚合 SHA-256 維持
`1842e1e1b80d05e05ecb767ef43785c6c7588eec5375571fdab47c35bdca9a9a`；知識圖譜 14 條
`knowledge_edge` 也逐字相同，聚合 SHA-256 維持
`2a725824d7bd78bd322c7bd4107094f94cfc032ccc1c6e2db9ac79476da5e4b6`。

- 從「研究中心 → 族群矩陣 → 運算與互連 → 第七站」固定走讀發現，修改前首屏第一句直接
  放入第 140 次工作坊、PCIe 6.x、64 GT/s 與訊號重整器；名詞速查只有 7 項。正文以
  「支援、互通、通過、量產、部署」五段散文後，只留一張「時鐘／已證實／尚未證實」
  三列表；讀者尚未看見完整連線有哪些位置，就被要求判讀產品名稱、實際速度與正式程序。
- `learningPathVersion` 升為 65。研究題名改成「PCIe 6 元件寫著第六代，不代表整套系統
  已通過：先分清裝置、連線、正式測試與部署」；入口問句改為「一個高速元件已經量產，
  為什麼還不能說整台伺服器已通過第六代連線？」。三句重點第一句只先建立完整高速連線，
  名詞小字典由 7 項增為 32 項。圖譜與核心概念改為「PCIe 6 高速連線的測試與部署階梯」，
  另追加純編輯 transition，沒有刷新來源、複核日期或證據時鐘。
- 核心內容先用「主機與連線控制／板路、連接器與線材／訊號修復或速率轉換／連線交換與
  分支／終端與實際工作」五個位置建立接力；並明示第三與第四位置不是每套系統都需要，
  五格也不是固定接線順序或完整協定堆疊。
- 再以「規格版本與連線世代／每條通道傳輸率／通道數與拓撲／產品、韌體與軟體組合／
  測試主體與結果狀態」五把尺，限制每筆測試能支持的範圍。32 GT/s 正式列項只支持該列，
  不能外推成 64 GT/s 已失敗或已通過；活動提供測試也不能替具名產品補成通過結果。
- 規格與測試入口、具名產品、供應商或客戶互通、正式通過與公開列名、單一元件量產、完整
  客戶平台部署分成六個時鐘，不假設固定先後。標準組織、主機平台、連接元件、終端、客戶
  系統與台灣供應鏈查證六類角色各自分責，避免一家公司在一個位置有產品，就替其他位置
  補上證據。
- 最後以「完整連線位置可辨認 → 測試合約寫完整 → 具名產品在目標速度正式通過 → 不同廠商
  完整路徑互通 → 具名客戶穩定部署 → 台灣公司財務雙向核對」六關分開元件量產與整套系統
  通過。本輪第一關只有分散產品，第二關只有部分欄位，第三關沒有具名 64 GT/s 結果，第四關
  缺完整跨廠矩陣，第五關仍停在元件量產與參考架構，第六關也尚未通過。
- 1280px 與 390px 固定畫面均完成逐張開圖及同 viewport 前後對照；桌機
  `scrollWidth == innerWidth == clientWidth == 1280`，手機
  `scrollWidth == innerWidth == clientWidth == 390`。行動版五個位置、五把測試尺、六個時鐘、
  六類角色與六關表格均重排為具欄名卡片，沒有水平溢位。名詞速查可完整載入 32 個中文優先
  定義，搜尋「跨廠互通」只顯示 1／32 個相符項目，關閉後焦點回到原按鈕；第七站可進入
  中文優先證據圖譜，也可前往第 8／8 站。這些是 deterministic viewport 與互動契約，
  不是抽樣統計，SE／t／有效獨立觀測不適用；固定瀏覽器尺寸不是實機，本輪未涵蓋真機旋轉、
  完整實體鍵盤巡覽、VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；第七站閱讀時間由 17 分鐘更新為 26 分鐘，族群矩陣站卡、文章題名、讀者
  問句、知識圖譜路線與正式證據數量均由建置器同步核對，`learningPathVersion: 64 → 65`。
  排除版本後 canonical payload SHA 由
  `f29a0f4e7ca3ad8846d8ab9619659d8d66d70bd43c9d306e2307447d497e47ca` 變為
  `e2927e172b0ad7a89df1138c0da3706e6ce6b1b2ed0edaa7dba4da891b09f2e8`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 506 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar、method audit 六項 lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被本次編輯改寫。連續兩次 dashboard build SHA
  一致：`index.html` `5b4abaafacc6fb63a6c7b0379554cebdcdfc22b78ccf15f0d105769313b08c0f`、
  `research.html` `e2d1db44ec85ab5e97e91b0b078e9881bcc60e34d8197a58d5b28161230b9911`。

## 開放 AI 互連第六站改成五個資料位置、兩種網路範圍與六關跨廠互通 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有開放 AI 互連議題的讀者層文字、標題、中文優先
圖譜標籤、發布 payload 與對應測試，不改變原研究結論。該篇 `research_topic`、
`research_source`、`research_claim`、`impact` 與 `monitoring_item` 共 34 個正式區塊均與 Git
`HEAD` 逐字相同，聚合 SHA-256 維持
`f1c4ad5f1461e5d2ddda8ae31e13d472e89c079e195c6f951bc76b89c612a9f3`；知識圖譜 19 條
`knowledge_edge` 也逐字相同，聚合 SHA-256 維持
`f27f9a1c6ae999df5cf88d68ac03c917fce73345ce2385c62d64c89fb66c6d01`。

- 從「研究中心 → 族群矩陣 → 運算與互連 → 第六站」固定走讀發現，首屏的唯一重點同時
  放入 UALink、scale-up、UEC、scale-out、OCP、ESUN、SUE-T 與 Ethernet，名詞速查只有
  15 項。正文用五道散文關卡後，只留一張「規格／產品／部署」三列表；不熟網路的
  讀者還沒看見資料實際經過哪些位置，就被要求判斷規格分工與多廠成熟度。
- `learningPathVersion` 升為 64。研究題名改成「資料從一顆運算晶片走到另一顆：先分清
  機架內外，再判斷跨廠互通」；入口問句改為「資料要從一顆運算晶片送到另一顆，
  端點、交換器和軟體要一起通過哪些測試？」。三句重點第一句先只建立完整資料
  路徑，名詞小字典由 15 項增為 32 項。圖譜題名與核心節點改為「AI 資料路徑與
  跨廠互通」，另追加純編輯 transition，沒有刷新來源、複核日期或證據時鐘。
- 核心內容先用「資料出發的運算端點／連接與傳輸／交換與網路／協調與控制軟體／
  目的端點與工作負載」五個位置建立接力；再用距離與連線形狀、延遲與記憶體、交換路由
  與壅塞、可靠性與恢復、實際工作與客戶驗收五把尺，分開機架內與跨機架。
- UALink、ESUN、SUE-T、UEC 與 UALoE 被放回各自的距離、端點、網路與承載位置；
  規格工作組、加速器／晶片智財、交換平台、機架整合、雲端客戶與台灣供應鏈查證六類
  角色各自分責。這些表是閱讀路徑與證據分工，不是完整網路協定、供應商名單或標準勝負。
- 最後以「共同規則可查核 → 路徑各位置有具名實物 → 單件產品符合指定規格 → 不同廠商
  完成交叉互通 → 整個系統與工作可重現 → 客戶部署與公司財務對上」六關分開「能連」與
  「真正互通」。本輪第一關有多份文件，第二關只有分散產品路徑，第三至六關尚未由本輪
  證據通過；不以單廠展示、會員名單、參考設計或客戶規劃補上缺口。
- 1280px 與 390px 固定畫面均完成逐張開圖及同 viewport 前後對照；桌機
  `scrollWidth == innerWidth == 1280`，手機 `scrollWidth == innerWidth == 390`。行動版五個資料
  位置、機架內外五把尺、五條路徑、六類角色與六關互通表均重排為具欄名卡片，沒有水平
  溢位。名詞速查可完整載入 32 個中文優先定義，搜尋「跨廠互通」只顯示 1／32 個相符項目，
  關閉後焦點回到原按鈕。這些是 deterministic viewport 與互動契約，不是抽樣統計，
  SE／t／有效獨立觀測不適用；固定瀏覽器尺寸不是實機，本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、
  VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；第六站閱讀時間由 26 分鐘更新為 32 分鐘，族群矩陣站卡、文章題名、讀者
  問句、知識圖譜路線與正式證據數量均由建置器同步核對，`learningPathVersion: 63 → 64`。
  排除版本後 canonical payload SHA 由
  `fa7e0dd9f64d4ad60b9300100e3e6ae6970a4fce3db9075dab16415192cc0231` 變為
  `f29a0f4e7ca3ad8846d8ab9619659d8d66d70bd43c9d306e2307447d497e47ca`。方法 registry fingerprint 維持
  `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 505 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar、method audit 六項 lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被本次編輯改寫。連續兩次 dashboard build SHA
  一致：`index.html` `4c5527a0bda5fc3798543650591bf9f286be9027f90813a9e6a7d191fafb749f`、
  `research.html` `796e446bd67e18fcc0b607fc93d331747943f0125660c80e2f22e3a69fc77950`。

## High-NA EUV 第五站改成五個曝光位置、五把成本尺與六關量產證據 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有 High-NA EUV 導入議題的讀者層文字、標題、中文優先
圖譜標籤、發布 payload 與對應測試，不改變原研究結論。該篇 `research_topic`、
`research_source`、`research_claim`、`impact` 與 `monitoring_item` 共 20 個正式區塊均與 Git
`HEAD` 逐字相同，聚合 SHA-256 維持
`392c78061c8c297d49652ff0c3b7ff23dec2767b80364a156f9aaee46bda934f`；知識圖譜 13 條
`knowledge_edge` 也逐字相同，聚合 SHA-256 維持
`34deda80c760fff0186761c4a7e1df04471feffc0e861ce64b55a37bd3552dac`。

- 從「研究中心 → 族群矩陣 → 運算與互連 → 第五站」固定走讀發現，首屏雖已問「少做步驟
  為何不一定降低總成本」，第一句卻先放入 High-NA、wafer、product-wafer testing，精確追問
  又加入 availability、Low-NA 與 multi-patterning。唯一核心表接著連續出現 shipment、
  acceptance、throughput、maintenance、qualification、resist、mask 與 metrology；不熟
  製程的讀者還沒建立「圖形怎麼印上晶圓」，就被要求判斷設備成熟度與量產經濟性。
- `learningPathVersion` 升為 63。研究題名改成「曝光次數少了，晶片不一定更便宜：先看圖形
  怎麼印、哪些成本又冒出來」；入口問句改成「晶片圖形能一次印得更細，為什麼少做幾個步驟
  仍不一定更便宜？」。三句重點第一句只先認得「晶圓、光阻、光罩」三個中文概念，名詞
  小字典由 7 項增為 32 項。圖譜題名與核心節點改為中文優先，並追加純編輯 transition，沒有
  刷新來源、複核日期或證據時鐘。
- 核心內容先用「設計圖形與光罩／晶圓表面與光阻／曝光機與光學／顯影與圖形轉移／量測、
  檢查與下一層」五個位置建立微影接力；再以「曝光與加工次數／機器可用時間與每小時產出／
  光罩、光阻與缺陷／對準、製程視窗與良率／每顆合格晶片總成本」五把尺，比較較高數值孔徑
  與現行多步驟方案。設備商、研發整合、晶圓製造客戶、材料與圖形轉移、量測與生產經濟五類
  角色各自放回公開證據；八台出貨、六台運轉、逾五十萬片、逾八成可用率與 2027–2028 目標
  被拆回五個里程碑，不合併成假精確完成率。
- 最後以「目標圖形可以印出 → 多台設備能持續運轉 → 共同製程通過資格 → 實際產品達成視窗
  與良率 → 量產層數、產出與成本可重算 → 供應商財務足跡出現」六關，把設備進度接到客戶
  量產與公司受惠。本輪設備平台最多走到第二關，第三關仍是待完成目標，第四關只有開始測試
  而沒有產品結果，第五與第六關尚未通過；表格是閱讀與證據排序，不是完整製程配方、供應商
  名單、營收預測或投資排名。
- 1280px 與 390px 固定畫面均完成逐張開圖及同 viewport 前後並排檢查；桌機
  `scrollWidth == innerWidth == 1280`，手機 `scrollWidth == innerWidth == 390`。行動版五個
  曝光位置、五把成本尺與六關證據表均重排為具欄名卡片，沒有水平溢位。名詞速查可完整載入
  32 個中文優先定義，搜尋「每顆合格晶片成本」只顯示 1／32 個相符項目，關閉後焦點回到
  原按鈕。這些是 deterministic viewport 與互動契約，不是抽樣統計，SE／t／有效獨立觀測
  不適用；固定瀏覽器尺寸不是實機，本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、
  VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；第五站閱讀時間由 14 分鐘更新為 21 分鐘，族群矩陣站卡、文章題名、讀者
  問句、知識圖譜路線與正式證據數量均由建置器同步核對，`learningPathVersion: 62 → 63`。
  排除版本後 canonical payload SHA 由
  `888a2f961fcab653157db360072f95a2a3babe7b048e78ea14a95ee81865905a` 變為
  `fa7e0dd9f64d4ad60b9300100e3e6ae6970a4fce3db9075dab16415192cc0231`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 504 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar、method audit 六項 lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被本次編輯改寫。連續兩次 dashboard build SHA
  一致：`index.html` `e7595986eb10f9cf9cbe7c51c17505ea1202ad9e7318e58da0f86c47e4cb9bbd`、
  `research.html` `859381bedfcbc9c3976a6ca9889b1f282884c1b4315ab2e843184401d0151431`。

## CPO 第四站改成五個光電位置、五把取捨尺與六關部署證據 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有 CPO 與可插拔共存議題的讀者層文字、標題、中文優先圖譜
標籤、發布 payload 與對應測試，不改變原研究結論。該篇 `research_topic`、
`research_source`、`research_claim`、`impact` 與 `monitoring_item` 共 16 個正式區塊均與 Git
`HEAD` 逐字相同，聚合 SHA-256 維持
`518948065b324552aad50cd54a194b0e296e0dcfc44b617eb2df9adf955d62dc`。

- 從「研究中心 → 族群矩陣 → 運算與互連 → 第四站」固定走讀發現，原首屏先問 CPO 是否
  取代可插拔，三句重點又立即放入 Spectrum-X Ethernet Photonics、Spectrum-6、1.6T、Ara、
  DSP 與 SPIL。不熟產業的讀者還沒有建立「資料先是電訊號、在哪裡轉成光訊號」的路徑，
  就要先比較產品名與供應鏈角色；原文也沒有把維修、故障範圍、功耗、密度、升級彈性與
  生命週期成本放在同一組取捨尺上。
- `learningPathVersion` 升為 62。研究題名改成「資料先是電、再變成光：轉換器放哪裡，決定
  可插拔與共同封裝的取捨」；入口問句改成「資料從交換晶片送出去時，為什麼有的光模組能
  拔換，有的要和晶片放在一起？」。三句重點第一句只先認得「電訊號、交換晶片、光訊號」
  三個中文概念，名詞小字典由 11 項增為 32 項。圖譜題名與核心產品顯示改為中文優先，並
  追加純編輯 transition，沒有刷新來源、複核日期或證據時鐘。
- 核心內容先用「交換晶片內部／晶片到轉換器的高速電路／電光轉換位置／雷射與光纖耦合／
  光纖與下一台設備」五個位置建立光電接力；再以「高速電路長度與功耗／前面板空間與頻寬
  密度／維修與故障範圍／升級與多供應商彈性／封裝測試與生命週期成本」五把尺比較可插拔與
  共同封裝；最後把平台與交換器、可插拔訊號處理、雷射與光源、封裝組裝測試、客戶部署營運
  五類角色，接到「產品列名 → 進入生產 → 供應商角色雙向核對 → 客戶驗收與部署分母 →
  供應商出貨、份額與價格 → 收入、毛利與現金流」六關。這些表格是閱讀框架，不是完整交換器
  設計、架構勝負、供應商名單、部署占比或投資排序。
- 1280px 與 390px 固定畫面均完成逐張開圖及同 viewport 前後並排檢查；桌機
  `scrollWidth == innerWidth == 1280`，手機 `scrollWidth == innerWidth == 390`。行動版五個
  位置、五把取捨尺與六關證據表均重排為具欄名卡片，沒有水平溢位。名詞速查可完整載入
  32 個中文優先定義，搜尋「生命週期成本」只顯示 1／32 個相符項目，關閉後焦點回到原按鈕。
  這些是 deterministic viewport 與互動契約，不是抽樣統計，SE／t／有效獨立觀測不適用；
  固定瀏覽器尺寸不是實機，本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、VoiceOver／TalkBack、
  200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；第四站閱讀時間由 12 分鐘更新為 18 分鐘，族群矩陣站卡、文章題名、讀者
  問句、知識圖譜路線與正式證據數量均由建置器同步核對，`learningPathVersion: 61 → 62`。
  排除版本後 canonical payload SHA 由
  `cba45776516bceea4349e4a76012d8863dfe9d4ac8980ec8ed5cc4a9f536df10` 變為
  `888a2f961fcab653157db360072f95a2a3babe7b048e78ea14a95ee81865905a`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 503 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar、method audit 六項 lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被本次編輯改寫。連續兩次 dashboard build SHA
  一致：`index.html` `cde203928ad46bfbf02f854f71afb099e74fd998eea89731fe4e6de1e58fb910`、
  `research.html` `3d9cd0ea4561a985dadf5b66910f9df94220851e359a9cf29b981426b6f8214e`。

## 背面供電第三站改成五個位置、六個製程步驟與六關公司證據 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有背面供電議題的讀者層文字、標題、中文優先圖譜標籤、
發布 payload 與對應測試，不改變原研究結論。該篇 `research_topic`、`research_source`、
`research_claim`、`impact` 與 `monitoring_item` 共 16 個正式區塊均與 Git `HEAD` 逐字相同，
聚合 SHA-256 維持 `70d23616d4a3e9d61951310d3ce1cbf60cfb74f672a37e52b2fc93c51c8ddc8a`。

- 從「研究中心 → 族群矩陣 → 運算與互連 → 第三站」固定走讀發現，原首屏先問設備需求如何
  變成公司獲利，三句重點又立即放入 A16、18A、18A-P、風險生產與跨廠成熟度。讀者還沒有
  建立「訊號和電力原本都擠在正面、供電為什麼改走背面」的路徑，就要先比較公司自訂節點與
  製造用語；原文把薄化、接合、對準、nTSV、金屬與製程控制濃縮在一段，也看不出角色接力與
  公司受惠之間還缺哪些證據。
- `learningPathVersion` 升為 61。研究題名改成「晶片把供電線移到背面，不只是換條路：先看
  電力路徑、製程接力與量產證據」；入口問句改成「晶片為什麼要把供電線移到背面，這會新增
  哪些製程，又怎麼判斷公司真的受惠？」。三句重點第一句需先認得的詞改為「訊號線、供電線、
  晶圓背面」三個中文概念，名詞小字典由 6 項增為 32 項。圖譜題名與核心製程顯示改為中文
  優先，並追加純編輯 transition，沒有刷新來源、複核日期或證據時鐘。
- 核心內容先用「正面訊號佈線／背面金屬網路／奈米級背面導通孔／埋置電源軌／電晶體」
  五個位置建立送電與送訊號的最短路徑；再把「完成前側元件與電源軌／接到支撐載體／從背面
  變薄／重新對準／形成導通孔與背面金屬／驗證可重複生產」排成六個製程步驟，逐列標出晶圓廠、
  設計規則與 IP、設備、材料、量測、可靠度與客戶產品團隊的接力位置；最後以「一般機制成立
  → 晶圓廠進入製造時鐘 → 供應商具名步驟 → 資格與量產出貨 → 份額、價格與重複需求 → 收入、
  毛利與現金流」六關把製程需要接回公司。本輪只支持技術第一關與各晶圓廠各自的第二關，
  台灣公司仍停在第三關之前；三張表都不是完整晶片設計、量產配方、供應商名單或投資排序。
- 1280px 與 390px 固定畫面均完成逐張開圖及同 viewport 前後並排檢查；桌機
  `scrollWidth == innerWidth == 1280`，手機 `scrollWidth == innerWidth == 390`。行動版三張
  5 欄表都重排為具欄名卡片，沒有水平溢位。名詞速查可完整載入 32 個中文優先定義，搜尋
  「蝕刻停止層」只顯示 1／32 個相符項目，關閉後焦點回到原按鈕。這些是 deterministic
  viewport 與互動契約，不是抽樣統計，SE／t／有效獨立觀測不適用；固定瀏覽器尺寸不是實機，
  本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、VoiceOver／TalkBack、200%／400% zoom 與儀器化
  WCAG 對比量測。
- 文章數維持 274；第三站閱讀時間由 10 分鐘更新為 17 分鐘，族群矩陣站卡、文章題名、讀者
  問句、知識圖譜路線與正式證據數量均由建置器同步核對，`learningPathVersion: 60 → 61`。
  排除版本後 canonical payload SHA 由
  `6dcb38ec3cce96cf160bf0d2b0e1c938f265972e88883701dbb06d6f89e22bcc` 變為
  `cba45776516bceea4349e4a76012d8863dfe9d4ac8980ec8ed5cc4a9f536df10`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 502 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar、method audit 六項 lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被本次編輯改寫。連續兩次 dashboard build SHA
  一致：`index.html` `376d993bad3d434d167abfa52cfbbea571517702961ef010545306f334d6d8a1`、
  `research.html` `d8e0a8cfd4c73b79135fb2c02fe7055ec3f3017442453173d0fe38fdd6a527f7`。

## AMD Helios 第二站改成六個部署關卡、五條客戶時間線與六關公司證據 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有 AMD Helios 部署議題的讀者層文字、標題、中文優先圖譜
標籤、發布 payload 與對應測試，不改變原研究結論。該篇 `research_topic`、
`research_source`、`research_claim`、`impact` 與 `monitoring_item` 共 29 個正式區塊均與 Git
`HEAD` 逐字相同，聚合 SHA-256 維持
`b6a1e3650b5691f2de6a9b5fe0091a0a3f11e1a93e8363c1c9ec0ae42ee64a7f`。

- 從「研究中心 → 族群矩陣 → 運算與互連 → 第二站」固定走讀發現，原首屏與第一句先要求
  理解 Helios、production 與 SKU，三句重點又同時放入 shipment、multi-GW、online、
  validation、EFB、2.5D 與 ODM。不熟產業的讀者還沒有建立「做出來、送出去、客戶測試、
  真正上線」的順序，就要先翻譯平台、容量與供應鏈術語；原題名「從參考設計走向具名部署」
  也容易讓「具名」被誤讀成客戶已實際部署。
- `learningPathVersion` 升為 60。研究題名改成「AI 機櫃做出來，不等於客戶已上線：用六個
  關卡讀懂 AMD Helios」；入口問句改成「一整櫃人工智慧設備開始生產後，為什麼還不能算
  客戶已經上線使用？」。三句重點第一句需先認得的詞改為「機架級系統、開始生產、正式
  上線」三個中文概念，名詞小字典由 13 項增為 32 項。圖譜題名與核心階段顯示改為中文優先，
  並追加純編輯 transition，沒有刷新來源、複核日期或證據時鐘。
- 核心內容先用「方案成形 → 開始生產 → 實際出貨 → 客戶測試與產品開放 → 正式上線 →
  規模部署與財務轉換」六個關卡建立通用順序；再把 AMD 整體平台、Microsoft／Azure、
  OpenAI、Meta、Anthropic 五組公開節點放回各自時間線，避免把不同客戶、期限與容量相加成
  已部署；最後以「公開列名 → 具體角色 → 平台專屬產品 → 驗證與量產出貨 → 可辨識財務結果
  → 現金流與重複訂單」六關接回台灣整機、機構、封裝與載板公司。三張表都明示這是本文
  讀法，不是供應商名單、訂單、公司排名或投資排序。
- 1280px 與 390px 固定畫面均完成逐張開圖及同 viewport 前後並排檢查；桌機
  `scrollWidth == innerWidth == 1280`，手機 `scrollWidth == innerWidth == 390`。行動版三張
  5 欄表都重排為具欄名卡片，沒有水平溢位。名詞速查可完整載入 32 個中文優先定義，搜尋
  「現金流足跡」只顯示 1／32 個相符項目，關閉後焦點回到原按鈕。這些是 deterministic
  viewport 與互動契約，不是抽樣統計，SE／t／有效獨立觀測不適用；固定瀏覽器尺寸不是實機，
  本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、VoiceOver／TalkBack、200%／400% zoom 與儀器化
  WCAG 對比量測。
- 文章數維持 274；第二站閱讀時間由 23 分鐘更新為 25 分鐘，族群矩陣站卡、文章題名、讀者
  問句、知識圖譜路線與正式證據數量均由建置器同步核對，`learningPathVersion: 59 → 60`。
  排除版本後 canonical payload SHA 由
  `2a88f4d5597897f259c7b2231d9e17e8d9fe984278f48c414350853aa1d12cb4` 變為
  `6dcb38ec3cce96cf160bf0d2b0e1c938f265972e88883701dbb06d6f89e22bcc`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 501 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar、method audit 六項 lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被本次編輯改寫。連續兩次 dashboard build SHA
  一致：`index.html` `1bb4bb7f1c3306ae6bede4144ef243a4bb4547d06ec1edb04eaf0e5f1fb328eb`、
  `research.html` `e8cc92d151a45d71482c55a69c32bfc43a730666fcd2d32bdf18fa21040b2323`。

## AI 儲存第一站改成三種工作、五個位置與六關證據 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有 AI 儲存資料平面議題的讀者層文字、標題、中文優先圖譜
標籤、發布 payload 與對應測試，不改變原研究結論。該篇 `research_topic`、
`research_source`、`research_claim`、`impact` 與 `monitoring_item` 共 21 個正式區塊均與 Git
`HEAD` 逐字相同，聚合 SHA-256 維持
`8df4853b4fc1f42ca9b4a71833918574d20d2cb9760ccfe1e3ce6c8ed1624ef4`。

- 從「研究中心 → 族群矩陣 → 運算與互連 → 第一站」固定走讀發現，原首屏先要求理解
  pMax、I/O 合約與 peer-to-peer 分發，三句重點又把 object storage、local storage、
  checkpoint 與 qualification 放進同一層。不熟產業的讀者要先翻譯系統詞，才看得出 AI
  儲存其實同時承接「持續餵資料、故障前保存進度、把模型送到新機器」三種不同工作；390px
  畫面會把這段翻譯負擔進一步放大。
- `learningPathVersion` 升為 59。研究題名改成「AI 儲存不是容量越大越好：先分清餵資料、
  保存進度與搬模型」；入口問句改成「人工智慧為什麼會一邊餵訓練資料、一邊保存進度，還要
  把模型送到新機器？」。首屏改為只先認得「訓練資料、保存進度、模型檔案」三個中文概念，
  名詞小字典由 12 項增為 32 項。學習站名、圖譜題名與核心概念顯示改為「AI 資料讀取與
  儲存路徑」中文優先，並追加純編輯 transition，沒有刷新來源、複核日期或證據時鐘。
- 核心內容先把「訓練時持續餵資料／故障前保存進度／上線或擴充時搬模型」三種工作分開；
  再用「軟體、索引與排程／近端記憶體與快取／單機本地 SSD／共享與長期儲存／網路與系統
  整合」五個位置標出資料可能經過的路徑；最後以「三種工作已分開 → 同一平台量到瓶頸 →
  瓶頸落到具名元件 → 客戶資格認證 → 正式部署與設備分母 → 可辨識收入與毛利」六關，把
  平台需求接回公司。三張表均明示這是本文讀法，不是完整架構、供應商名單、訂單、公司排名
  或投資排序。
- 1280px 與 390px 固定畫面均完成逐張開圖及同 viewport 前後並排檢查；桌機
  `scrollWidth == innerWidth == 1280`，手機 `scrollWidth == innerWidth == 390`。行動版三張
  5 欄表都重排為具欄名卡片，沒有水平溢位。名詞速查可完整載入 32 個中文優先定義，搜尋
  「最慢讀取時間」只顯示 1／32 個相符項目，關閉後焦點回到原按鈕。這些是 deterministic
  viewport 與互動契約，不是抽樣統計，SE／t／有效獨立觀測不適用；固定瀏覽器尺寸不是實機，
  本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、VoiceOver／TalkBack、200%／400% zoom 與儀器化
  WCAG 對比量測。
- 文章數維持 274；第一站閱讀時間由 21 分鐘更新為 22 分鐘，族群矩陣站卡、文章題名、讀者
  問句、知識圖譜路線與正式證據數量均由建置器同步核對，`learningPathVersion: 58 → 59`。
  排除版本後 canonical payload SHA 由
  `d0179241021c7f6380c23a7025174701a925166c1ecb23d1c299b61585f5ea8e` 變為
  `2a88f4d5597897f259c7b2231d9e17e8d9fe984278f48c414350853aa1d12cb4`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 500 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar、method audit 六項 lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被本次編輯改寫。連續兩次 dashboard build SHA
  一致：`index.html` `0443a6b17b6137f5709f86ad9430635907d18c5e532d99a682cefa72d3cf0328`、
  `research.html` `3e1f07c3ce14a2812787177104b6b4be4a00328a51938438b5ad864cbb76b638`。

## 面板級封裝第七站改成四把成本尺、五個生產關卡與六關證據 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有面板級封裝議題的讀者層文字、標題、中文優先圖譜標籤、發布
payload 與對應測試，不改變原研究結論。該篇 `research_topic`、`research_source`、
`research_claim`、`impact` 與 `monitoring_item` 共 16 個正式區塊均與 Git `HEAD` 逐字相同，
聚合 SHA-256 維持 `5d4ac95294d1e505041978527050895eae35edd103e723e1e45ece9743863310`。

- 從「研究中心 → 族群矩陣 → 記憶體與封裝 → 第七站」固定走讀發現，首屏先要求理解
  `Pilot` 與 `Qualification`，研究題名又直接使用 `Panel-level packaging` 與
  `good-package yield`；原成本段落把 `Uniformity`、`Throughput`、`HVM`、`NEXX` 等六個詞
  與一條帶反引號的文字公式放在同一視野。390px 畫面中，名詞列先進入 sticky 閱讀列下方，
  公式又以程式碼外觀斷行；不熟產業的讀者難以分清「排得下更多」只改善幾何機會，不等於
  最後合格品更多、每小時產出更高或每顆成本更低。
- `learningPathVersion` 升為 58。研究題名改成「面板排得更滿，成品不一定更便宜：要一起看
  面積、良率、速度與報廢」；入口問句改成「面板能排進更多封裝，為什麼還要一起看良率、
  製程速度與報廢成本？」。首屏需先認得的詞由兩個英文階段詞改為「方形面板、合格品、報廢」
  三個中文概念，名詞小字典由 9 項增為 32 項。學習站名、圖譜題名與核心概念顯示改為「面板級
  封裝（PLP）」中文優先，並追加純編輯 transition，沒有刷新來源、複核日期或證據時鐘。
- 核心內容先用「面積利用率／合格封裝良率／單位時間合格產出／每顆合格品總成本」四把尺，
  拆開幾何、良率、速度與單位成本；再用「載體與共同尺寸／圖形、金屬與均勻度／翹曲、搬運與
  缺陷／封裝整合、測試與認證／良率、產出與財務」五個生產關卡放回材料、設備、封測、客戶與
  財務的接力位置；最後以「研發場域與設備能力 → 試產與工程測試 → 早期共同開發與認證 →
  共同尺寸與具名產品認證 → 穩定大量生產 → 重複出貨與收入」六關定位本輪資料只涵蓋第 1～3
  關的場域與能力敘述，尚無第 2、3 關的具名產品結果。三張表均明示這是本文讀法，不是完整
  規格、成本比較、供應商名單、訂單、公司排名或投資排序。
- 1280px 與 390px 固定畫面均完成逐張開圖及同 viewport 前後並排檢查；桌機
  `scrollWidth == innerWidth == 1280`，390px 含邊框的 iframe 內容寬 388px，亦有
  `scrollWidth == innerWidth == 388`。行動版三張 5 欄表都重排為具欄名卡片，沒有水平溢位。
  名詞速查可完整載入 32 個中文優先定義，搜尋「單位時間產出」只顯示 1／32 個相符項目，
  關閉後焦點回到原按鈕。這些是 deterministic viewport 與互動契約，不是抽樣統計，SE／t／
  有效獨立觀測不適用；固定 iframe 不是實機，本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、
  VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；第七站閱讀時間由 14 分鐘更新為 18 分鐘，族群矩陣站卡、文章題名、讀者
  問句、知識圖譜路線與正式證據數量均由建置器同步核對，`learningPathVersion: 57 → 58`。
  排除版本後 canonical payload SHA 由
  `66dcc56d3e31e1fe231edbfe4cb9317651fca0dd0ffbf215b522ae4595220f66` 變為
  `d0179241021c7f6380c23a7025174701a925166c1ecb23d1c299b61585f5ea8e`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 499 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar、method audit 六項 lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被本次編輯改寫。連續兩次 dashboard build SHA
  一致：`index.html` `27c6f775f3425bace4131ee031045c4db9c8bb289964bb161ffd9eab6828caa1`、
  `research.html` `c93b78da919cde9b1d9748ccb559a6d7a0e314c0cca6d84a550e0c91c0cd55db`。

## 混合接合第六站改成兩條接合路徑、五個製程窗口與六關證據 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有混合接合議題的讀者層文字、標題、中文優先圖譜標籤、發布
payload 與對應測試，不改變原研究結論。該篇 `research_topic`、`research_source`、
`research_claim`、`impact` 與 `monitoring_item` 共 16 個正式區塊均與 Git `HEAD` 逐字相同，
聚合 SHA-256 維持 `45ee305b2dc4cfa0c1c7644f93074006a25e4ad7ce4e8e2b6b0df968afc8bfa1`。

- 從「研究中心 → 族群矩陣 → 記憶體與封裝 → 第六站」固定走讀發現，首屏先要求理解
  `Hybrid bonding` 與 `Overlay`，研究題名又直接使用 PDK、200nm 與 HVM；原成熟度表把
  `fine-pitch RDL`、`pathfinding PDK`、`test vehicle`、`good-die yield`、`throughput`、
  `inline metrology` 與 `qualification` 集中在三列。不熟產業的讀者要先翻譯製程詞，才看得出
  「接得準」仍不足以回答表面、潔淨、良率、產能、可靠度與收入是否一起過關。
- `learningPathVersion` 升為 57。研究題名改成「晶片貼得更近，量產反而更難：混合接合要
  同時守住五個製程窗口」；入口問句改成「兩層晶片貼得更密，為什麼一次試驗成功還不能證明
  可長期量產？」。首屏需先認得的詞由兩個英文技術詞改為「銅接點、晶粒」兩個中文概念，
  名詞小字典由 10 項增為 32 項。學習站名、圖譜題名與核心概念顯示改為「混合接合
  （Hybrid bonding）」中文優先，並追加純編輯 transition，沒有刷新來源、複核日期或證據時鐘。
- 核心內容先把「單顆晶粒接晶圓／晶圓接晶圓」兩條路徑的做法、優點、風險與良率分母分開；
  再用「設計規則與試驗結構／表面平坦與銅高度／潔淨與顆粒控制／對準、接合與量測／良率、
  產能與可靠度」五個窗口，標出研究機構、材料、設備、晶圓廠、封測、產品客戶與財務的接力
  位置；最後以「設計入口 → 試驗結構 → 整合設備與流程 → 具名產品認證 → 穩定大量生產 →
  重複出貨與收入」六關定位本輪證據只到第 1～3 關。三張表均明示這是本文讀法，不是完整
  規格、路徑勝負、供應商名單、量產名次、訂單或投資排序。
- 1280px 與 390px 固定畫面均完成逐張開圖及同 viewport 前後並排檢查；桌機
  `scrollWidth == innerWidth == 1280`，390px 含邊框的 iframe 內容寬 388px，亦有
  `scrollWidth == innerWidth == 388`。行動版三張 5 欄表都重排為具欄名卡片，沒有水平溢位。
  名詞速查可完整載入 32 個中文優先定義，搜尋「對準誤差」只顯示 1／32 個相符項目，關閉後
  焦點回到原按鈕。這些是 deterministic viewport 與互動契約，不是抽樣統計，SE／t／有效
  獨立觀測不適用；固定 iframe 不是實機，本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、
  VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；第六站閱讀時間由 14 分鐘更新為 18 分鐘，族群矩陣站卡、文章題名、讀者
  問句、知識圖譜路線與正式證據數量均由建置器同步核對，`learningPathVersion: 56 → 57`。
  排除版本後 canonical payload SHA 由
  `b2a66d023fddb115a18612fa2e100b28ad8a0e49a00e777a8424e025e3a8a00e` 變為
  `66dcc56d3e31e1fe231edbfe4cb9317651fca0dd0ffbf215b522ae4595220f66`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 498 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar、method audit 六項 lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被本次編輯改寫。連續兩次 dashboard build SHA
  一致：`index.html` `0d0940e0f64fa1185b3958a62711f8487a4a4619b50fb617146bbc4e7ea5bf89`、
  `research.html` `cca4c8e74d9d030a3f1aef155cdea1a592022004d28ae897b25cb9918a46ad6c`。

## SPHBM4 第五站改成五項連線代價、五組角色與六關證據 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有 SPHBM4 議題的讀者層文字、標題、學習路線交接、發布
payload 與對應測試，不改變原研究結論。該篇 `research_topic`、`research_source`、
`research_claim`、`impact` 與 `monitoring_item` 共 14 個正式區塊均與 Git `HEAD` 逐字相同，
聚合 SHA-256 維持 `d6fb11aa3c0e5cb7c9775d16fb41ccb3778789a551d30e304a8872d17b63c1f3`。

- 從「研究中心 → 族群矩陣 → 記憶體與封裝 → 第五站」固定走讀發現，首屏先要求理解
  `JESD330-4`、HBM4、介面基礎晶片與序列化四個產品／標準術語；原規格表又直接使用
  `HBM4 DRAM dies`、`interface base die`、`data signals` 與 `throughput`。不熟產業的讀者
  容易把資料訊號由 2,048 個降到 512 個，直接讀成設計更簡單、成本必然下降或產品已可採用，
  看不出問題其實移到每線速度、訊號品質、功耗、材料、組裝、良率與系統驗證。
- `learningPathVersion` 升為 56。研究題名改成「接點變少不等於設計變簡單：SPHBM4 把難題
  移到高速傳輸、功耗與系統驗證」；族群矩陣問句改成「記憶體接點變少，為什麼不代表成本
  一定下降或產品已經可用？」。首屏需先認得的詞由四個產品／標準術語降為「接點、功耗」
  兩個中文概念，名詞小字典由 10 項增為 32 項，並追加純編輯 transition，沒有用可讀性改版
  刷新來源、複核日期或證據時鐘。
- 核心內容先用「接點與扇出／每線速度與訊號品質／功耗、延遲與熱／材料、組裝與良率／
  系統容量與配置」五項問題說清難題搬移；再把記憶體裸晶與堆疊、底部介面晶片與高速介面、
  有機基板與材料、封裝測試與熱管理、運算晶片系統與客戶五組角色放回接力位置；最後以
  「共同標準 → 底部晶片 → 記憶體與封裝樣品 → 系統整合 → 客戶資格與可靠度 → 穩定量產與
  收入」六關分開畢業證據。三張表均明示這是本文閱讀問題與搜尋路由，不是完整規格、公司
  快慢、具名供應商、訂單或投資排名。
- 1280px 與 390px 固定畫面均完成逐張開圖及同 viewport 前後並排檢查；桌機
  `scrollWidth == innerWidth == 1280`，390px 含邊框的 iframe 內容寬 388px，亦有
  `scrollWidth == innerWidth == 388`。行動版三張 5 欄表都重排為具欄名卡片，沒有水平溢位。
  名詞速查可完整載入 32 個中文優先定義，搜尋「訊號完整性」只顯示 1／32 個相符項目，關閉後
  焦點回到原按鈕。這些是 deterministic viewport 與互動契約，不是抽樣統計，SE／t／有效
  獨立觀測不適用；固定 iframe 不是實機，本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、
  VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；第五站閱讀時間由 12 分鐘更新為 16 分鐘，族群矩陣站卡、文章題名、讀者
  問句、知識圖譜路線與正式證據數量均由建置器同步核對，`learningPathVersion: 55 → 56`。
  排除版本後 canonical payload SHA 由
  `2eeca2a05090daf43a385683c4a841edd7117d888aa80afb37e73b8a7cce626e` 變為
  `b2a66d023fddb115a18612fa2e100b28ad8a0e49a00e777a8424e025e3a8a00e`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 497 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar、method audit 六項 lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被本次編輯改寫。連續兩次 dashboard build SHA
  一致：`index.html` `967554a402247fb48b22b65375f6356b9aa481dd52a2f1ebcd83f15ccaf92ae4`、
  `research.html` `d006d08970cab928e8bb6dc95884914a4a74b9da0315e0713a363b8335d708b7`。

## HBF 第四站改成五項系統條件、六關商用化與五組角色接力 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有 HBF 議題的讀者層文字、標題、發布 payload 與對應測試，
不改變原研究結論。該篇 `research_topic`、`research_source`、`research_claim`、`impact` 與
`monitoring_item` 共 17 個正式區塊均與 Git `HEAD` 逐字相同，聚合 SHA-256 維持
`81545bfadc00b4dee93cdbe61b9ce162c5e9a565e03cb84371e0fbbf20464bc1`。

- 從「研究中心 → 族群矩陣 → 記憶體與封裝 → 第四站」固定走讀發現，首屏先要求理解 HBF 與
  KV cache，原商用化表又直接使用 `logic base die`、`workstream`、`memory sample`、
  `device sample` 與 `qualification`。不熟產業的讀者容易把容量或高頻寬當成完整產品能力，
  也難以分清共同規則、實體樣品、裝置整合、客戶認證、穩定量產與財務收入需要不同證據。
- `learningPathVersion` 升為 55。研究題名改成「新記憶體層不能只靠大容量：HBF 還要通過
  讀寫、耐久、系統整合與量產」；首屏先認得的詞由 `HBF／KV cache` 改為「容量、寫入與更新、
  耐久、功耗、熱管理」五個中文概念。三句重點與反思題先建立「容量只是起點」的判斷方式，
  再放回高頻寬快閃記憶體、底部邏輯晶片、共同標準化與樣品原名。名詞小字典由 5 項增為
  32 項，並追加純編輯 transition，沒有用可讀性改版刷新來源、複核日期或證據時鐘。
- 核心內容先用「容量與資料保留／讀取與等待時間／寫入、更新與耐久／功耗、熱與封裝／
  系統整合與軟體調度」五項系統條件判斷它能否成為新記憶體層；再用「說清楚技術位置與
  工作負載 → 公開共同規則 → 交出記憶體樣品 → 完成裝置整合 → 通過客戶資格認證 → 穩定
  量產與形成收入」六關分開畢業證據。第三張表把快閃記憶體與堆疊、底部邏輯晶片與控制器、
  封裝測試與熱管理、裝置系統與軟體、客戶製造與財務五組角色放回接力位置；三張表均明示
  這是本文閱讀問題與搜尋路由，不是完整規格、公司快慢、具名供應商、訂單或投資排名。
- 1280px 與 390px 固定畫面均完成逐張開圖及同 viewport 前後並排檢查；桌機
  `scrollWidth == innerWidth == 1280`，390px 含邊框的 iframe 內容寬 388px，亦有
  `scrollWidth == innerWidth == 388`。行動版三張 5 欄表都重排為具欄名卡片，沒有水平溢位。
  名詞速查可完整載入 32 個中文優先定義，搜尋「軟體調度」只顯示 1／32 個相符項目，關閉後
  焦點回到原按鈕。這些是 deterministic viewport 與互動契約，不是抽樣統計，SE／t／有效
  獨立觀測不適用；固定 iframe 不是實機，本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、
  VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；第四站閱讀時間由 13 分鐘更新為 18 分鐘，族群矩陣站卡、文章題名、讀者
  問句、知識圖譜路線與正式證據數量均由建置器同步核對，`learningPathVersion: 54 → 55`。
  排除版本後 canonical payload SHA 由
  `fb45f50e8a921d168082248250698b6cf280154f47312b4061e088d9fcd00729` 變為
  `2eeca2a05090daf43a385683c4a841edd7117d888aa80afb37e73b8a7cce626e`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 496 tests 全綠；qual notes、leading
  hypotheses、research queue、knowledge graph、research radar、method audit 六項 lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被本次編輯改寫。連續兩次 dashboard build SHA
  一致：`index.html` `714485c9b48cd5e249b413f9a74b235ad28d308d0d702d452addc962b5e567d1`、
  `research.html` `8fa4d1f7a6063ae285c4d8fbd80d8bafd8be7d95bccab8c9dd8609f380c4bbd1`。

## 玻璃基板第三站改成五關商業化與角色接力讀法 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有玻璃基板議題的讀者層文字、標題、學習路線交接、發布
payload 與對應測試，不改變原研究結論。該篇 `research_topic`、`research_source`、
`research_claim`、`impact` 與 `monitoring_item` 共 22 個正式區塊均與 Git `HEAD` 逐字相同，
聚合 SHA-256 維持 `c0f6caf9a54c642ef88d32bf5ea884f79921ee687183cd5ce6d6c0ebb8b5734e`。

- 從「研究中心 → 族群矩陣 → 記憶體與封裝 → 第三站」固定走讀發現，首屏先要求理解
  `mass-production facility` 與 `reliability evaluation`；正文又把合作探索、試產線、原型、
  量產準備樣品、客戶測試、製造良率、量產與出貨混在時間線裡。不熟產業的讀者容易把工廠、
  樣品或合作直接讀成客戶驗證完成與穩定量產，也看不出材料、加工、載板／封裝、客戶與財務
  其實接力回答不同問題。
- `learningPathVersion` 升為 54。讀者問句改成「玻璃基板已有工廠與樣品，為什麼還不能算穩定
  量產？」；研究題名改成「玻璃基板從工廠走到穩定出貨：樣品、客戶驗證、良率與訂單不能
  跳級」。首屏兩個待認得詞由 `Production yield／Reliability evaluation` 改為「大型封裝／
  量產」，三句重點與反思題不再先要求理解 HVM、TGV、pilot、proof sample、Intel 或 Samsung；
  名詞小字典由 6 項增為 32 項，並追加純編輯 transition，沒有用可讀性改版刷新來源、複核日期
  或證據時鐘。
- 核心內容先以「能力與設備就位 → 交出可測樣品 → 完成客戶驗證 → 穩定製造 → 重複出貨與
  收入」五關，逐關列出要回答的問題、主要接力角色與不能跳級的證據；第二張表再把
  SKC／Absolics、Samsung Electro-Mechanics、Intel／Lens Technology 與 Corning 放回本輪一手
  資料可確認的位置，另列下一份證據與不能外推的結論。兩張表都明示這是本文閱讀順序與證據
  定位，不是產業共同標準、公司快慢、技術價值或投資排名。
- 1280px 與 390px 固定畫面均完成逐張開圖、同 viewport 前後並排檢查；桌機
  `scrollWidth == innerWidth == 1280`，390px 含邊框的 iframe 內容寬 388px，亦有
  `scrollWidth == innerWidth == 388`。行動版 5 列 × 4 欄商業化表與 4 列 × 5 欄公司證據表
  均重排為具欄名卡片，沒有水平溢位。名詞速查可完整載入 32 個中文優先定義，搜尋「雙向核對」
  只顯示 1／32 個相符項目，關閉後焦點回到原按鈕。這些是 deterministic viewport 與互動契約，
  不是抽樣統計，SE／t／有效獨立觀測不適用；固定 iframe 不是實機，本輪未涵蓋真機旋轉、完整
  實體鍵盤巡覽、VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；第三站閱讀時間由 15 分鐘更新為 20 分鐘，並由建置器同步更新族群矩陣、
  第三站卡片、文章標題、讀者問句、知識圖譜 `learningRoutes` 與
  `learningPathVersion: 53 → 54`。排除版本後 canonical payload SHA 由
  `5cf89fe110920f5f5288893e31ec1ed2adb5b4f0dbe7d3ea7958c6fd81c2bd5a` 變為
  `fb45f50e8a921d168082248250698b6cf280154f47312b4061e088d9fcd00729`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 495 tests 全綠；qual notes、leading
  hypotheses、research queue、research radar、method audit、knowledge graph 六項 lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被本次編輯改寫。連續兩次 dashboard build SHA
  一致：`index.html` `94894605c73843caa9ab986255ce580d0d5d7509074d6f2ed38c3cdc1b5e7fd1`、
  `research.html` `096d670a12f10ba98de937a492af0aadc780dff80758485043b9362fbb4d0f5b`。

## 客製記憶體第二站改成三種客製範圍與雙軸進度讀法 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有客製高頻寬記憶體議題的讀者層文字、標題、學習路線交接、
發布 payload 與對應測試，不改變原研究結論。該篇 `research_topic`、`research_source`、
`research_claim`、`impact` 與 `monitoring_item` 共 21 個正式區塊均與 Git `HEAD` 逐字相同。

- 從「研究中心 → 族群矩陣 → 記憶體與封裝 → 第二站」固定走讀發現，首屏先以 Samsung、
  Custom HBM 與 HBM 樣品時程起句；正文核心表再把 `Base die`、`Stream DQ`、
  `preprocessing`、`roadmap`、`qualification`、`benchmark` 與 `foundry` 混在「客製對象」與
  「本輪可確認階段」兩欄。不熟產業的讀者要先翻譯公司產品詞，才看得出「改了哪裡」與
  「公開證據走到哪一步」其實是兩個不同問題。
- `learningPathVersion` 升為 53。讀者問句改成「客製高頻寬記憶體只改規格或重做底部晶片，
  為何不能排在一起？」；研究題名改成「高頻寬記憶體可以客製到哪裡：先分規格、底部晶片與
  工作搬移」。首屏讀者任務需先認得的詞由 3 個降為 0 個，先用「調整規格／重做底部晶片／
  搬移資料整理工作」建立概念，再把三星、SK 海力士與美光放回第二句。反思題不再先要求理解
  HBM、Stream DQ、NRE、qualification 或 roadmap；名詞小字典由 7 項增為 32 項，並新增純編輯
  transition，沒有用可讀性改版刷新複核日期或證據時鐘。
- 核心內容先以「調整記憶體規格／重做堆疊底部邏輯／搬移部分資料整理工作」三種本文讀法，
  分別說明改了什麼、可能共同參與的角色、可能增加的功能與不能外推的結論；第二張表再把
  三家公司分成公開改法、公開證據、目前階段與仍不能說的事項。文末明確說明第一張表回答
  「改了哪裡」，第二張表回答「走到哪一步」，沒有共同產品、測試、數量與財務分母就不產生
  單一供應商名次。
- 1280px 與 390px 固定畫面均完成逐張開圖、同 viewport／同路線狀態前後並排檢查；桌機
  `scrollWidth == innerWidth == 1280`，390px 含邊框的 iframe 內容寬 388px，亦有
  `scrollWidth == innerWidth == 388`。行動版兩張 3 列 × 5 欄表均重排為具欄名卡片，沒有水平
  溢位。名詞速查可完整載入 32 個中文優先定義，搜尋「毛利」只顯示 2／32 個相符項目並可正常
  關閉。這些是 deterministic viewport 與互動契約，不是抽樣統計，SE／t／有效獨立觀測不適用；
  固定 iframe 不是實機，本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、VoiceOver／TalkBack、
  200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；第二站閱讀時間由 14 分鐘更新為 17 分鐘，並由建置器同步更新族群矩陣、
  第二站卡片、文章標題、讀者問句、知識圖譜 `learningRoutes` 與
  `learningPathVersion: 52 → 53`。排除版本後 canonical payload SHA 由
  `7e81282a8682fc319d4db14bf49037731d3f9f57ef119a9cb71e2e42d2975c94` 變為
  `5cf89fe110920f5f5288893e31ec1ed2adb5b4f0dbe7d3ea7958c6fd81c2bd5a`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 494 tests 全綠；qual notes、leading
  hypotheses、research queue、research radar、method audit、knowledge graph 六項 lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被本次編輯改寫。連續兩次 dashboard build SHA
  一致：`index.html` `04b2ebcebf4b016436f120938de1dbf2de33ddabbfb53322e2833ab9d6fd3582`、
  `research.html` `8d99cf04622887f2c18766c31319c097229bfb18b0988209e22c4a22d5271110`。

## AI 記憶體第一站改成四層資料與商業進度讀法 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有 AI 記憶體分層議題的讀者層文字、標題、學習路線交接、
發布 payload 與對應測試，不改變原研究結論。該篇 `research_topic`、`research_source`、
`research_claim`、`impact` 與 `monitoring_item` 共 18 個正式區塊均與 Git `HEAD` 逐字相同。

- 從「研究中心 → 族群矩陣 → 記憶體與封裝 → 第一站」固定走讀發現，首屏先要求讀者理解
  Rubin 與 Vera、HBM、SOCAMM、KV cache 與 Context storage／CMX 五個產品或英文術語；正文
  雖已把資料分成四層，仍以 GPU／HBM、CPU／SOCAMM、CMX 與 SSD 起句。成熟度表又直接使用
  `qualification`、`placement` 與 `context tier`，不熟產業的讀者要先翻譯名詞，才看得出
  「資料為什麼放這裡」和「商業進度走到哪裡」是兩個不同問題。
- `learningPathVersion` 升為 52。讀者問句改成「人工智慧資料為什麼要分層存放，越常用的資料
  就一定要離運算晶片越近嗎？」；研究題名改成「人工智慧資料為什麼要分層存放：正在運算、
  等待取用與長期保存各有位置」。首屏需先認得的詞由 5 個產品／英文術語降為「容量、等待時間」
  2 個中文概念，反思題不再先要求理解 HBM、SOCAMM、CMX、KV cache 或 Rubin。名詞小字典由
  12 項增為 32 項，並新增純編輯 transition；原本已逾期的複核日期與可信度降級完整保留，
  沒有用可讀性改版假裝取得新證據。
- 核心內容先用「正在計算 → 系統快速取用 → 可重建且可共享 → 長期保存」四種資料任務說明
  存放位置，再在最後一欄放回 HBM4、SOCAMM／SOCAMM2、CMX 與 SSD 原名；第二張表另把
  「平台規格 → 客戶送樣 → 架構與軟體設計 → 公開標準」和仍缺的資格認證、量產、具名部署、
  利用率與財務證據分開。320／390px 的資料位置表 4 列 20 格、商業進度表 4 列 16 格均重排
  為具欄名卡片；780／884／1280px 保留原生 table row／cell，五個固定 iframe 寬度都有
  `documentElement.scrollWidth == innerWidth`。同一路線、同 viewport 的前後畫面完成並排檢查；
  桌機、390px、深色與淺色均完成目視走讀。點擊 `CXL 4.0` 會開啟本文 32 詞名詞速查、預填
  搜尋並只顯示對應定義，關閉後焦點回到原按鈕。這些是 deterministic viewport 契約，不是
  抽樣統計，SE／t／有效獨立觀測不適用；固定 iframe 不是實機，本輪未涵蓋真機旋轉、完整實體
  鍵盤巡覽、VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；第一站閱讀時間由 13 分鐘更新為 16 分鐘，並由建置器同步更新族群矩陣、
  第一站卡片、文章標題、讀者問句、知識圖譜 `learningRoutes` 與
  `learningPathVersion: 51 → 52`。排除版本後 canonical payload SHA 由
  `9fed1caf4521ceba022644dec9df29e70dafcd476b09b61913b8238d0a214331` 變為
  `7e81282a8682fc319d4db14bf49037731d3f9f57ef119a9cb71e2e42d2975c94`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 493 tests 全綠；qual notes、leading
  hypotheses、research queue、research radar、method audit、knowledge graph lint 均以
  exit 0 通過。research queue 保留 11 個既有提醒；method audit 仍揭露新鮮度與修正學習
  `ATTENTION`、校準可用性 `NOT_READY`，未被本次編輯改寫。連續兩次 dashboard build SHA
  一致：`index.html` `f93acbaa2458d2425e22cbb7326b2dd70fab5a9af9b1537e9e59aeb93fbff78a`、
  `research.html` `a5a0b93ebccb35903056085a3885253f03e85fe95767a27259ea2c7fb671eebb`。

## 液冷第九站改成五次交接與五關證據讀法 — 2026-08-11

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、monitor、impact、證據判定與
複核時鐘零變動**；本次只改寫既有液冷迴路議題的讀者層文字、標題、學習路線交接、發布
payload 與對應測試，不改變原研究結論。該篇 `research_topic`、`research_source`、
`research_claim`、`impact` 與 `monitoring_item` 共 19 個正式區塊均與 Git `HEAD` 逐字相同。

- 從「研究中心 → 族群矩陣 → 供電與散熱 → 第八站 → 第九站」固定走讀發現，第九站首屏先
  使用 FWS、TCS、ITE 與 CDU 四個縮寫，再要求讀者從責任矩陣自行推導冷源、循環水路、機櫃
  分流、伺服器冷板與控制系統的交接關係；另一張成熟度表則以 Requirement、Qualification、
  Integration、Reliability 與 Commercial 組織證據層級。責任資料完整，但不熟產業的讀者要
  先翻譯兩套術語，才看得出「誰跟誰交接」以及「目前只走到哪一關」。
- `learningPathVersion` 升為 51。研究題名改成「液冷不是買完設備就能運作：冷源、管路、
  伺服器與控制必須共同交接」；首屏閱讀任務由 4 個英文縮寫改成 2 個中文概念，反思題不再
  要求先理解 FWS、TCS 或 `rackLocationId`。名詞小字典由 7 項增為 27 項；三句重點、重要性、
  持續追蹤、研究判定與推翻條件均改為中文概念先行，並新增純編輯 transition。原 OCP、
  Lenovo、NVIDIA 與平台產品清單的來源角色、公司映射、商業階段和限制均保留。
- 責任矩陣改成「機房設施 ↔ 冷卻設備 → 循環水路 → 機櫃分流 → 伺服器冷板」，另把建築控制
  與 IT 控制列為第五個交接點；欄位為「交接點／這一段由誰或什麼負責／雙方要說清楚什麼／
  沒說清楚會怎樣／本輪依據」。證據層級改成「責任與範圍寫清楚 → 零件與設備通過測試 →
  平台列出具名產品 → 具名場域完成驗收 → 長期運作與財務出現」五關。320／390px 的責任表
  5 列 25 格與證據表 5 列 15 格均重排為具欄名卡片；780／884／1280px 保留原生 table
  row／cell，五個固定 viewport 都有 `documentElement.scrollWidth == innerWidth`。桌機、
  390px、深色與淺色均完成目視走讀；點擊「水質／腐蝕／污染」會開啟本文 27 詞名詞速查、
  預填搜尋並只顯示對應定義，關閉後焦點回到原按鈕。這些是 deterministic viewport 契約，
  不是抽樣統計，SE／t／有效獨立觀測不適用；固定 iframe 不是實機，本輪未涵蓋真機旋轉、
  完整實體鍵盤巡覽、VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；第九站閱讀時間由 17 分鐘更新為 19 分鐘，並由建置器同步更新第八站的
  下一站題名、問句、閱讀時間、知識圖譜 `learningRoutes` 與
  `learningPathVersion: 50 → 51`。排除版本後 canonical payload SHA 由
  `41ae8a980839f1e7339c5e22d22a0c5aed6b7d115fe255218672138e48b3d1a2` 變為
  `9fed1caf4521ceba022644dec9df29e70dafcd476b09b61913b8238d0a214331`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 492 tests 全綠；qual notes、leading
  hypotheses、research queue、research radar、method audit、knowledge graph lint 均通過，
  research queue 保留 11 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `2021cbf7d33121f6564454c7951b8f7e6f07c3a740df0e8cac05ebf1701aaa06`、`research.html`
  `09c00befcc3a0cf2b23d2d0eca008cc8f080e54b3c8c914b1ea9913c09562e1b`；輸出已包含推送前
  rebase 的 GitHub Actions `2026-08-10` 資料更新。

## 液冷第八站改成從容量規格到收入證據的五關讀法 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、comparison、monitor、
impact、證據判定與複核時鐘零變動**；本次只改寫既有液冷市場議題的讀者層文字、標題、
學習路線交接、發布 payload 與對應測試，不改變原研究結論。該篇 `research_topic`、
`research_source`、`research_claim`、`metric_comparison`、`impact` 與 `monitoring_item` 共 31 個
正式區塊均與 Git `HEAD` 逐字相同。

- 從「研究中心 → 族群矩陣 → 供電與散熱 → 第七站 → 第八站」固定走讀發現，第八站首屏先列
  1.2MW、1MW、380kW，再要求讀者比較 `Sample Ready／MP Ready`；五關概念雖已存在，核心表
  仍用「階段／本輪可定位證據／尚不能知道」呈現，容量帳本又以 capture、M1、reported value、
  verdict 與 Supply Chain Status 起句。不熟產業的讀者必須先翻譯術語，才能分清容量、資格、
  供應準備、部署與收入是不同證據。
- `learningPathVersion` 升為 50。讀者標題改成「液冷設備容量比較大，為什麼不代表已量產或有
  訂單？」；研究題名改成「液冷設備不能只比容量：平台列名、供應準備與收入是三種不同證據」。
  首屏需先認得的詞由 3 個降為 1 個，反思題不再先要求理解兩個英文供應標籤；名詞小字典由
  9 項增為 32 項，容量比較、重要性、持續追蹤、反方路徑、到期複核與判定改變條件都改為
  中文概念先行，並新增同日純編輯 transition。原 NVIDIA、LG、Daikin、奇鋐、台達電、光寶科
  的證據角色、數值、公司映射、商業階段與限制均保留。
- 核心內容改成「容量規格 → 平台列名與測試 → 供應準備 → 場域整合與客戶部署 → 公司收入」
  五關；表格欄位為「先問哪一關／這一關能回答什麼／本輪已有的公開證據／仍然缺什麼」。
  容量帳本另把欄名改為供應商、產品、來源原始容量、換算值、平台原始標籤與證據界線。
  320／390px 的 5 列、20 個儲存格完整重排為具欄名卡片；780／884／1280px 保留原生 table
  row／cell，五個固定 viewport 都有 `documentElement.scrollWidth == innerWidth`。桌機、390px、
  深色與淺色均完成目視走讀；點擊「MW／kW」會開啟本文 32 詞名詞速查、預填搜尋並顯示
  2 個相關定義，關閉後焦點回到原按鈕。這些是 deterministic viewport 契約，不是抽樣統計，
  SE／t／有效獨立觀測不適用；固定 iframe 不是實機，本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、
  VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；相對前版改動第八站
  `topic-MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER`，並由建置器同步更新第七站文章的
  下一站題名、問句、閱讀時間、知識圖譜 `learningRoutes` 與 `learningPathVersion: 49 → 50`。
  排除版本後 canonical payload SHA 由
  `eec9eb42e2ce0d560b1a1b71969469367b3af8d2a4e5b5d1be03c51df659a3ca` 變為
  `41ae8a980839f1e7339c5e22d22a0c5aed6b7d115fe255218672138e48b3d1a2`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 491 tests 全綠；qual notes、leading
  hypotheses、research queue、research radar、method audit、knowledge graph lint 均通過，
  research queue 保留 8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `a7a1ca628fe372c19c21e802a5f36541c5457469504a85f645b2da102ceb2c18`、`research.html`
  `05f47d9fc19de856a87dd9ef966cc1ca6cd1573887352182be4a8bbe61d0e8c8`。

## AI 機櫃信任第七站改成身分到查證的四關流程 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、comparison、monitor、
impact、證據判定與複核時鐘零變動**；本次只改寫既有 AI 機櫃信任市場議題的讀者層文字、
標題、學習路線敘述、發布 payload 與對應測試，不改變原研究結論。該篇 `research_topic`、
`research_source`、`research_claim`、`impact` 與 `monitoring_item` 共 23 個區塊均與 Git `HEAD`
逐字相同。

- 從「研究中心 → 族群矩陣 → 供電與散熱 → 第六站 → 第七站」固定走讀發現，第七站已用
  「一道斷電指令為什麼可信」建立具體場景，但研究題名先丟出「信任根」，讀後問題再要求讀者
  先理解 `attestation`；核心四關則用 Caliptra、SPDM、OCP S.A.F.E. 四段長文呈現，讀者必須
  一邊翻譯術語，一邊自己整理身分、版本、權限與第三方查證的責任順序。
- `learningPathVersion` 升為 49。文章標題改成「AI 機櫃如何判斷控制指令可信：確認身分、版本
  與權限，還要有人查證」；首屏先認得的詞由 1 個降為 0 個，三句重點與反思題先問送出者是誰、
  目前執行哪一版，以及驗證失敗後系統會做什麼。名詞小字典由 7 項增為 30 項；重要性、追蹤、
  判定改變條件、公司新聞查核與結論邊界均改為中文概念先行，並新增同日純編輯 transition。
  原 OCP、DMTF、Caliptra、SPDM 與 5274 信驊的證據角色、公司映射、商業階段和限制均保留。
- 核心內容改成「確認身分 → 確認版本 → 核對權限 → 查證是否照做」四關，表格欄位為「系統先
  問什麼／已有的公開機制／還不能因此判定」；公司段另用四問把功能、獨立查證、買方採用與財務
  足跡分開。320／390px 的 4 列、16 個儲存格完整重排為具欄名卡片；780／884／1280px 保留
  原生 table row／cell，五個固定 viewport 都有 `documentElement.scrollWidth == innerWidth`。
  桌機、390px、深色與淺色均完成目視走讀；點擊「授權」會開啟本文 30 詞名詞速查、預填搜尋
  並只顯示對應定義，關閉後焦點回到原按鈕。這些是 deterministic viewport 契約，不是抽樣
  統計，SE／t／有效獨立觀測不適用；固定 iframe 不是實機，本輪未涵蓋真機旋轉、完整實體鍵盤
  巡覽、VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；相對前版改動第七站
  `topic-MI-2026-08-08-AI-RACK-TRUST-ROOT`，並由建置器同步更新第六站文章的下一站標題、問句、
  閱讀時間、供電與散熱路線說明、知識圖譜 `learningRoutes` 與
  `learningPathVersion: 48 → 49`。排除版本後 canonical payload SHA 由
  `8d4a157381cfe1c47d9b4413b5190b5c1a75c783d6d1542a846c4bbb404d5f09` 變為
  `eec9eb42e2ce0d560b1a1b71969469367b3af8d2a4e5b5d1be03c51df659a3ca`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 490 tests 全綠；qual notes、leading
  hypotheses、research queue、research radar、method audit、knowledge graph lint 均通過，
  research queue 保留 8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `9e199380c4d458bc062044519596312022844f62e9460334a5d54fde4daa0d55`、`research.html`
  `7fdc8d8ac1ef3323fd8345c42a984a53d3dc4ce9c8430c5c2515aeb4732161c4`。

## AI 機櫃 EMC 第六站改成零件到實驗室的四關驗證 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、comparison、monitor、
impact、證據判定與複核時鐘零變動**；本次只改寫既有 AI 機櫃 EMC 市場議題的讀者層文字、
標題、發布 payload 與對應測試，不改變原研究結論。三篇連續改寫文章的 `research_topic`、
`research_source`、`research_claim`、`impact` 與 `monitoring_item` 區塊均與 Git `HEAD` 逐字相同。

- 從「研究中心 → 族群矩陣 → 供電與散熱 → 第五站 → 第六站」固定走讀發現，第六站主問題已能
  用「單一設備合格，整櫃仍可能不合格」建立懸念，但研究題名與第一張架構表仍用 `EMC`、
  `placement`、`attenuation`、`configuration` 與 `lab capacity` 組織內容；讀者必須先翻譯術語，
  才能看出零件、完整配置、量測程序與實驗室是四種不能互相代替的責任。
- `learningPathVersion` 升為 48。文章標題改成「AI 機櫃為什麼要重新驗證電磁干擾：零件合格，
  不等於整櫃合格」；首屏先認得的詞由 1 個降為 0 個，三句重點與反思題改為先問設備重新接線
  並同時運作後為何仍會彼此干擾。名詞小字典由 7 項增為 26 項；重要性、追蹤方法、測試資料
  判讀、公司研究與結論邊界均改為中文概念先行，並新增同日純編輯 transition。OCP、IEC、FCC
  與國巨的原角色、公司映射、商業階段和證據限制均保留。
- 核心內容改成「零件降低雜訊 → 定義完整被測配置 → 依程序完成量測 → 確認實驗室能承載」
  四關，表格欄位為「先問什麼／現有證據能證明／還不能證明」。320／390px 的 4 列、16 個
  儲存格完整重排為具欄名卡片；780／884／1280px 保留原生 table row／cell，五個固定 viewport
  都有 `documentElement.scrollWidth == innerWidth`。桌機、390px、深色與淺色均完成目視走讀；
  點擊「被測配置」會開啟本文 26 詞名詞速查、預填搜尋並顯示 3 筆相關定義，關閉後焦點回到
  原按鈕。這些是 deterministic viewport 契約，不是抽樣統計，SE／t／有效獨立觀測不適用；
  固定 iframe 不是實機，本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、VoiceOver／TalkBack、
  200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；相對前版改動第六站
  `topic-MI-2026-08-09-AI-RACK-EMC-CERTIFICATION`，並由建置器同步更新第五站文章的下一站標題、
  問句、閱讀時間、知識圖譜 `learningRoutes` 與 `learningPathVersion: 47 → 48`。排除版本後
  canonical payload SHA 由 `31f276f53ce395640b5162949730988e8dd69ecda841d67322c4831a6745e5f2`
  變為 `8d4a157381cfe1c47d9b4413b5190b5c1a75c783d6d1542a846c4bbb404d5f09`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 489 tests 全綠；qual notes、leading
  hypotheses、research queue、research radar、method audit、knowledge graph lint 均通過，
  research queue 保留 8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `481b6038a9190d92dd3aa687faca4bf9e4479190c18096fcdd35680ed1ccc985`、`research.html`
  `ff8d6fb7ff1c608e006061f710a438f56537ae19348466a88a20be6212e18945`。

## AI 機櫃控制第五站改成從警報到復原的七步流程 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、comparison、monitor、
impact、證據判定與複核時鐘零變動**；本次只改寫既有 AI 機櫃控制市場議題的讀者層文字、
標題、發布 payload 與對應測試，不改變原研究結論。

- 從「研究中心 → 族群矩陣 → 供電與散熱 → 第四站 → 第五站」固定走讀發現，第五站已用
  過熱、漏液與找對機櫃建立好問題，但首屏重點又以 `metadata`、`rack identity`、`request`、
  `guardrail` 起句；第一張表再用「契約層／DSX 可定位證據／production 證據」組織內容，
  不熟產業的讀者必須先翻譯欄位，才看得出控制流程。
- `learningPathVersion` 升為 47。文章標題改成「AI 機櫃如何從感測警報走到安全隔離：先找對
  設備，再決定動作」；首屏先認得的詞由 3 個降為 2 個，三句重點與反思題改為先問設備編號
  是否一致、讀數是否可信、誰能決定動作。名詞小字典由 8 項增為 28 項；重要性、追蹤方法、
  規格分工、公司新聞判讀、研究判定與證據缺口均改為中文概念先行，並新增同日純編輯
  transition。NVIDIA、OCP、DMTF 的原角色、公司映射、商業階段與證據限制均保留。
- 核心表格改成「控制步驟 → 這一步要回答什麼 → 公開文件目前支持什麼 → 還缺哪些現場證據」，
  從找到正確設備、確認讀數一路走到結果回報與維修閉環。320／390px 的 7 列、28 個儲存格
  完整重排為具欄名卡片；780／884／1280px 保留原生 table row／cell，五個固定 viewport
  都有 `documentElement.scrollWidth == innerWidth`。桌機、390px、深色與淺色均完成目視走讀；
  點擊「隔離」會開啟本文 28 詞名詞速查、預填搜尋並顯示逐字定義，關閉後焦點回到原按鈕。
  這些是 deterministic viewport 契約，不是抽樣統計，SE／t／有效獨立觀測不適用；固定 iframe
  不是實機，本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、VoiceOver／TalkBack、200%／400% zoom
  與儀器化 WCAG 對比量測。
- 文章數維持 274；相對前版改動第五站
  `topic-MI-2026-08-07-AI-RACK-ACTION-CONTRACT`，並由建置器同步更新第四站文章的下一站標題、
  問句、閱讀時間、知識圖譜 `learningRoutes` 與 `learningPathVersion: 46 → 47`。排除版本後
  canonical payload SHA 由 `91e799b2b8d8547816224c828a62eeeb47c840e7254eda8a26730e5801324740`
  變為 `31f276f53ce395640b5162949730988e8dd69ecda841d67322c4831a6745e5f2`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 488 tests 全綠；qual notes、leading
  hypotheses、research queue、research radar、method audit、knowledge graph lint 均通過，
  research queue 保留 8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `4235c98193742f116035dfc203828a660881cfc5dbf5863ca8f12bebff2bbed5`、`research.html`
  `658221dd64903b006de865b6e5ba76867cef6f24089457d825a4f26f8efc66c7`。

## AI 儲能第四站先按事件持續時間拆分三層任務 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、comparison、monitor、
impact、證據判定與複核時鐘零變動**；本次只改寫既有 AI 功率緩衝市場議題的讀者層文字、
標題、發布 payload 與對應測試，不改變原研究結論。

- 從「研究中心 → 族群矩陣 → 供電與散熱 → 第三站 → 第四站」固定走讀發現，第四站首屏已能
  用電力尖峰與停電時間建立問題，但第一張架構表又以 `rack／DC bus`、`ride-through`、
  `facility／utility interconnection` 與設備縮寫起句；讀者剛理解「不同時間長度要分工」，
  就必須重新翻譯位置與任務。
- `learningPathVersion` 升為 46。文章標題改成「AI 機櫃儲能要接力：短暫尖峰、機櫃備援與設施
  儲能各有任務」；首屏先認得的詞由 3 個降為 2 個，反思題改成以毫秒到秒和數十秒的差異發問。
  名詞小字典由 8 項增為 22 項；三句重點、重要性、追蹤方法、三列架構表、800V 文章分工、
  研究判定與推翻條件均改為中文概念先行，並新增同日純編輯 transition。NVIDIA、OCP、TI 的
  原角色、三層時間與位置邊界、公司映射、商業階段及證據限制均保留。
- 架構表改成「事件持續多久 → 誰來處理 → 設備在哪裡 → 一手證據 → 還不能判定」；320／390px
  三列完整重排為具欄名卡片，780／884／1280px 保留原生 table row／cell，五個固定 viewport
  都有 `documentElement.scrollWidth == innerWidth`。桌機、390px、深色與淺色均完成目視走讀；
  點擊「備援」會開啟本文 22 詞名詞速查、預填搜尋並顯示逐字定義，關閉後焦點回到原按鈕。
  這些是 deterministic viewport 契約，不是抽樣統計，SE／t／有效獨立觀測不適用；固定 iframe
  不是實機，本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、VoiceOver／TalkBack、200%／400% zoom
  與儀器化 WCAG 對比量測。
- 文章數維持 274；相對前版改動第四站
  `topic-MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY`，並由建置器同步更新第三站文章的下一站
  標題、問句、閱讀時間、知識圖譜 `learningRoutes` 與 `learningPathVersion: 45 → 46`。排除版本後
  canonical payload SHA 由 `d584694bb7f6a4adbd472ce24be53fe17bcb6ccf614aada6f1197a9e0d669eea`
  變為 `91e799b2b8d8547816224c828a62eeeb47c840e7254eda8a26730e5801324740`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 487 tests 全綠；qual notes、leading
  hypotheses、research queue、research radar、method audit、knowledge graph lint 均通過，
  research queue 保留 8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `cfd985c1fa7720bcda7f6240f24d20e0cb780180e6f40aae800b7a1554b16b8d`、`research.html`
  `6f71ec4567243ba643ac0ce263b4e7b5dc8fa12ac0a2fb52254b900e360c8cd8`。

## AI 電容第三站先用四個位置建立角色地圖 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、comparison、monitor、
impact、證據判定與複核時鐘零變動**；本次只改寫既有 AI 電容市場議題的讀者層文字、
發布 payload 與對應測試，不改變原研究結論。

- 從「研究中心 → 族群矩陣 → 供電與散熱 → 第三站」固定走讀發現，首屏同時要求讀者理解
  Rack、CBU、EDLC、DC link 與 BOM，角色表又以 `capacitive energy storage`、
  `board bulk`、`near-die decoupling` 等英文概念起句；不熟產業的讀者必須先翻譯名詞，才能
  理解電容其實位於四個不同位置、負責四種不同任務。
- `learningPathVersion` 升為 45。首屏先認得的詞由 5 個降為 2 個，三句重點與反思題改為先問
  「電容放在哪裡、處理什麼變化」；名詞小字典由 8 項增為 20 項，角色表、表後結論、公司新聞
  判讀步驟與研究判定均改為中文概念先行，並新增同日純編輯 transition。OCP、TI、TDK、Murata
  的原角色、公司映射、商業階段與證據限制均保留。
- 320／390px 四欄角色表完整重排為具欄名卡片，780／884／1280px 保留原生 table row／cell；
  五個固定 viewport 都有 `documentElement.scrollWidth == innerWidth`。桌機、390px、深色與淺色
  均完成目視走讀；點擊「紋波」會開啟本文 20 詞名詞速查、預填搜尋並顯示逐字原始定義，關閉
  後焦點回到原按鈕。這些是 deterministic viewport 契約，不是抽樣統計，SE／t／有效獨立觀測
  不適用；固定 iframe 不是實機，本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、VoiceOver／TalkBack、
  200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；相對前版改動第三站
  `topic-MI-2026-08-03-AI-CAPACITOR-ROLE-MAP`，並由建置器同步更新第二站文章的下一站問句／
  閱讀時間、知識圖譜 `learningRoutes` 與 `learningPathVersion: 44 → 45`。排除版本後 canonical
  payload SHA 由 `d4553d02469ab40bec6276073fd1cce061c542e2261cf3db22a860108816aee9` 變為
  `d584694bb7f6a4adbd472ce24be53fe17bcb6ccf614aada6f1197a9e0d669eea`。方法 registry fingerprint
  維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增 append-only
  方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 486 tests 全綠；qual notes、leading
  hypotheses、research queue、research radar、method audit、knowledge graph lint 均通過，
  research queue 保留 8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、`research.html`
  `f32d1f9f9a7f5928bc52f597fc44a4a6d1981606883f3b41b04612939a7f0d29`。

## 800V 保護第二站先分保護對象與事件 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、comparison、monitor、
impact、證據判定與複核時鐘零變動**；本次只改寫既有 800V 保護市場議題的讀者層文字、
發布 payload 與對應測試，不改變原研究結論。

- 從「研究中心 → 族群矩陣 → 供電與散熱 → 第二站」固定走讀發現，頁名雖已說明保護不能只靠
  保險絲，但首屏把 `safety requirements`、`live-access interlock`、`creepage／clearance`、
  `protective earthing`、`leakage current` 與 `ground-fault detection` 同時交給新手；反思題又以
  `bulk capacitor` 與「預充軌跡」表達，讀者必須先翻譯名詞，才能理解保護責任。
- `learningPathVersion` 升為 44。文章改成先分「保護誰、發生什麼事、誰來處理」，再介紹技術
  名稱；三句重點、重要性、追蹤方法、反思題、五列責任表與表後判讀均改為中文概念先行。名詞
  小字典由 11 項增為 20 項，並新增同日純編輯 transition；OCP、TI、Infineon 的原角色、公司映射、
  商業階段與證據限制均保留。
- 320／390／780／884／1280px 固定 iframe 契約皆有
  `documentElement.scrollWidth == innerWidth`；320／390px 四欄責任表完整重排為具欄名卡片，780px
  起維持原生 table row／cell。桌機、390px、深色與淺色均完成目視走讀；「湧入電流／預充」名詞
  速查顯示 1／20 的精確定義，關閉後焦點回到原按鈕。這些是 deterministic viewport 契約，不是
  抽樣統計，SE／t／有效獨立觀測不適用；固定 iframe 不是實機，本輪未涵蓋真機旋轉、完整實體
  鍵盤巡覽、VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；相對前版改動第二站
  `topic-MI-2026-08-03-800VDC-PROTECTION-LAYERS`，並由建置器同步更新第一站文章的下一站問句／
  閱讀時間、知識圖譜 `learningRoutes` 與 `learningPathVersion: 43 → 44`。排除版本後 canonical
  payload SHA 由 `fc7e797773308701c0a48f1169c70ce0f621abf6b910177c3ef14d7d2e18cc45` 變為
  `d4553d02469ab40bec6276073fd1cce061c542e2261cf3db22a860108816aee9`。方法 registry fingerprint
  維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增 append-only
  方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 485 tests 全綠；qual notes、leading
  hypotheses、research queue、research radar、method audit、knowledge graph lint 均通過，
  research queue 保留 8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、`research.html`
  `19e8eb6fecf119a5498ca7762fa2765c46986c28bb6f43fb7a14491e8a629bcf`。

## 800V 第一站改用中文概念解釋電力轉換 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、comparison、monitor、
impact、證據判定與複核時鐘零變動**；本次只改寫既有 800V 市場議題的讀者層文字、族群矩陣
問句、發布 payload 與對應測試，不改變原研究結論。

- 從「研究中心 → 族群矩陣 → 供電與散熱 → 第一站」固定走讀發現，原文把 `grid`、`core`、
  `device classes`、`qualification`、`production BOM`、`HVM` 與 `topology` 混在第一層閱讀，
  且「功率元件內容量會增加還是消失」沒有說清楚是在問元件數量、需求位置或價值占比。
- `learningPathVersion` 升為 43。族群矩陣入口改問「哪些轉換環節會保留、轉移或被整合」；
  文章反思題改為追問取消一層轉換後，元件需求會轉移或消失。文章新增同日純編輯 transition，
  名詞小字典由 8 項增為 15 項，並把「為什麼重要」、追蹤方法、段落標題、五列功能表與表後
  邊界全面改成中文概念先行；Si／SiC／GaN、公司、商業階段與證據限制均保留。
- 320／390／780／884／1280px 固定 iframe 契約皆有
  `documentElement.scrollWidth == innerWidth`；780px 以下五列表格完整重排為具欄名卡片，884px
  起維持原生 table row／cell。桌機、390px、深色與淺色均完成目視走讀；「參考設計」名詞速查
  顯示 1／15 的精確定義，關閉後焦點回到原按鈕。這些是 deterministic viewport 契約，不是
  抽樣統計，SE／t／有效獨立觀測不適用；固定 iframe 不是實機，本輪未涵蓋真機旋轉、完整實體
  鍵盤巡覽、VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- 文章數維持 274；相對前版只改
  `topic-MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION`、其知識圖譜學習站問句與
  `learningPathVersion: 42 → 43`。排除版本後 canonical payload SHA 由
  `1df222fbbfe61c45f9708ecf26d0de5410ed00085aacee9341727083d5fbb189` 變為
  `fc7e797773308701c0a48f1169c70ce0f621abf6b910177c3ef14d7d2e18cc45`。方法 registry
  fingerprint 維持 `322e5d8604570e10bac53ee0f18dc13b1957e072c8d99e96f447a6d165415c6b`，因此不新增
  append-only 方法快照。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 484 tests 全綠；qual notes、leading
  hypotheses、research radar、method audit、knowledge graph lint 均通過，research queue 保留
  8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、`research.html`
  `a5327a91efbd65c75542892c91de13fdf1fd6ca33b4221a2037ac6d9a6fb65ca`。

## 寬螢幕長段落改依正文寬度保留句子停頓 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章／圖譜映射、來源、
claim、comparison、monitor、證據判定與複核時鐘零變動**；本次只把既有長段落視覺停頓由
viewport 判斷改成正文容器判斷，並同步說明文件與發布版本。

- 固定 1280×720 走讀 31 分鐘「液冷 CDU 額定容量」市場議題發現，表後 161 字、3 句的結論
  位在 836px 專注閱讀欄，卻因整體 viewport 大於 1180px 而把兩個既有零文字停頓隱藏；「只有
  容量可比／供應標籤不能換成量產率／公司財務仍不可比」因此重新黏成單一文字塊。390px 同篇
  已有自然的三句停頓，可直接作為既有設計目標，不需新增摘要或改寫研究文字。
- `learningPathVersion` 升為 42。`.article-section` 原本已有 inline-size container；現在內容欄
  不超過 860px 時顯示既有 `reader-sentence-break`，寬視窗用 0.45em，`≤1180px` 仍保留原本
  0.55em。原段落仍是單一 `<p>`，兩個 span 都是空字串且 `aria-hidden="true"`；DOM `textContent`、
  原字序、runs、連結、粗體與複製文字完全不變。
- 320／390／780／781／884／1181／1280px 固定 iframe 契約中，實際 section 寬分別為
  284／354／684／664／664／836／836px；兩個停頓全部為 block，且每個
  `documentElement.scrollWidth == innerWidth`。這些是固定 viewport 的 deterministic layout
  契約，不是抽樣統計，SE／t／有效獨立觀測不適用。深色、淺色、原大綱跳節、手機第 3/7 節
  閱讀位置與表格卡片均保留；修改前、手機既有目標、正式修改後與同畫面比對留在
  `tmp/research-learning-audit-2026-08-10-wave79/`。固定 iframe 不是實機；本輪未涵蓋真機旋轉、
  完整實體鍵盤巡覽、VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- payload 相對前版只改 `learningPathVersion: 41 → 42`；文章數維持 274，排除版本後 canonical
  payload SHA 維持 `1df222fbbfe61c45f9708ecf26d0de5410ed00085aacee9341727083d5fbb189`。
  `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 483 tests 全綠；qual notes、leading
  hypotheses、research radar、method audit、knowledge graph lint 均通過，research queue 保留
  8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、`research.html`
  `0ec3a9b2722f2ca0f5f7b036188aecc361e7d676bad5f51cd845a2926ef96ba4`。

## 市場議題先用本文問句拆角色，通用族群指南改為可展開補充 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、候選與族群資料、原始 Markdown、
`readingMission`、文章／圖譜映射、來源、claim、comparison、monitor、證據判定與複核時鐘零變動**；
本次只調整三句重點後的產業角色 renderer、候選問句解析、說明文件與發布版本。

- 固定 390px 走讀 23 分鐘「AI 機櫃 EMC 驗證」發現，三句重點後雖立即顯示本文三個正式族群，
  但 701px 高的區塊只放通用角色與混淆界線；研究雷達已為同篇登錄「零件層／電源子系統／整櫃
  送驗」三個本文問句，清單或 deep link 進文時卻完全不顯示，讀者仍要自行把通用介紹對回 EMC。
- `learningPathVersion` 升為 41。`articleRadarRoleContext()` 現在先接受同一 origin 的精確候選；
  沒有 origin 時只在目前 article ID **唯一**匹配一個已升格候選時使用，歧義或無匹配都安全退回
  一般角色卡。候選問句依正式 `groups`／`group_id` 逐字顯示為「本文先問」，不讀正文、不摘要、
  不沿用前一篇候選，也不替 deep link 虛構雷達題次或返回脈絡。
- 三個本文問句成為角色區主層；既有 `readerRole／readerBoundary` 完整保留在一個原生
  `details／summary`，摘要明示「需要背景？再看平常角色與界線」。390px 角色區由 701px 降為
  520px，縮短 181px；884px 由 417px 降為 361px，縮短 56px。320／390／780／781／884／1280px
  皆有 `documentElement.scrollWidth == innerWidth`，補充摘要為 49–52px 且預設收合；這些是固定
  viewport 的 deterministic layout 契約，不是抽樣統計，SE／t／有效獨立觀測不適用。
- 實際驗證直接 deep link 會顯示本文問句但不顯示雷達來處；由研究雷達開文會同時保留真正的返回
  脈絡；沿路線由第 6/9 站換到第 7/9 站後，前一篇三個 EMC 問句全數消失。正式點擊補充摘要後，
  三個通用角色 heading、原角色說明與原混淆界線全部出現，狀態切成「收合」。修改前、source／
  target、正式前後、補充展開與桌機畫面留在
  `tmp/research-learning-audit-2026-08-10-wave78/`。固定 iframe 不是實機；本輪未涵蓋真機旋轉、
  完整實體鍵盤巡覽、VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG 對比量測。
- 本輪相對 wave77 的 payload 只改 `learningPathVersion: 40 → 41`；文章數維持 274，排除版本後
  canonical payload SHA 維持
  `1df222fbbfe61c45f9708ecf26d0de5410ed00085aacee9341727083d5fbb189`。
  `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 483 tests 全綠；qual notes、leading
  hypotheses、research radar、method audit、knowledge graph lint 均通過，research queue 保留
  8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、`research.html`
  `7f06d063a515b28b5f6717e2bc7145f23439b91a2d1275da9cedba5c15b52ea9`。

## 手機市場議題先露出起讀行動，完整反思題移到按鈕後 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、候選與族群資料、原始 Markdown、
`readingMission`、文章／圖譜映射、來源、claim、comparison、monitor、證據判定與複核時鐘零變動**；
本次只調整手機文章首屏的 renderer 排序、查核警語密度與發布版本。

- 固定 390px 走讀 23 分鐘「AI 機櫃 EMC 驗證」發現，頁首問題與查核警語之後，任務的第一句
  重點、完整「讀完能回答」反思題都先於主要行動，導致 44px「開始讀三句重點」位於約 y=836；
  720–844px 高的常見首屏只能看到第一句或按鈕極小一部分。
- `learningPathVersion` 升為 40。780px 以下現在用 `display: contents` 保留原 DOM／輔助科技
  閱讀順序，視覺上改成「第一句重點 → 主要行動 → 完整反思題 → 選用輔助」。查核警語同步縮短
  padding、gap 與次要文字行高；390px 主要行動提前至 y=680，共提前 156px。反思題仍逐字顯示於
  y=758，沒有 `display:none`、截斷、摘要或第二份 payload。
- 響應式邊界量測為：320px 行動／反思題 y=753／831、780px 582／660、781px 622／471、
  884px 622／471、1280px 554／428；所有寬度皆有
  `documentElement.scrollWidth == innerWidth`。781px 起恢復桌機兩欄，第一句與反思題同列、主行動
  在兩欄下方。這些是固定 viewport 的 deterministic layout 契約，不是抽樣統計，SE／t／有效
  獨立觀測不適用。
- 實際點擊新位置的「開始讀三句重點」後，畫面與鍵盤焦點仍抵達同篇三句重點；三句順序、完整
  反思題、名詞提示、來源邊界與文末理解檢查都保留。修改前、同畫面 source／target、正式修改後、
  反思題與桌機畫面留在 `tmp/research-learning-audit-2026-08-10-wave77/`。固定 iframe 不是實機；
  本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、VoiceOver／TalkBack、200%／400% zoom 與儀器化 WCAG
  對比量測。
- 本輪相對 wave76 的 payload 只改 `learningPathVersion: 39 → 40`；目前相對 Git `HEAD` 的完整
  payload 也只有版本 `36 → 40`，文章數維持 274。排除版本後 canonical payload SHA 前後均為
  `1df222fbbfe61c45f9708ecf26d0de5410ed00085aacee9341727083d5fbb189`。
  `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 483 tests 全綠；qual notes、leading
  hypotheses、research radar、method audit、knowledge graph lint 均通過，research queue 保留
  8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、`research.html`
  `9bb471a23da354b3e5cccd7c0545afd886fd306613a41d3b341f5399d449eba7`。

## 中幅族群矩陣改成具欄名的 2×2，雷達承接卡不再溢出 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、候選與族群資料、原始 Markdown、文章／
圖譜映射、來源、claim、comparison、monitor、證據判定與複核時鐘零變動**；本次只調整由研究
雷達進入族群矩陣後的 responsive layout、承接卡盒模型與發布版本。

- 用同一個「雷達第 1 題 → 被動元件」狀態量測發現，884px 仍把四個盤點欄壓成
  `240／220／210／175px`，欄名只在遠處共用表頭；`.maturity-origin-wide` 又以 `width:100%`
  加左右 margin，造成 830px row 內的承接卡寬 845px，問句、文章或返回行動可能被 row 的
  `overflow:hidden` 裁切。
- `learningPathVersion` 升為 39。781–1000px 現在隱藏共用表頭，將同一列四個 cell 改成 2×2，
  每格直接顯示既有「族群起點、已完成、最大缺口、下一步」欄名；884px 每格寬 415px，選取列
  由 482px 增為 524px。1000px 為 `473px × 2`，1001px 立即恢復四欄與共用表頭。
- 雷達承接卡改用 auto width 把外距算進 grid area。884px 由 845px 收進 806px；390px 由
  368px 收進 348px，為了完整換行高度由 280px 增為 299px。1280px 仍是三欄承接卡與四欄矩陣，
  780px 以下仍依 DOM 單欄；780／781、1000／1001 邊界及 390／884／1280 均無全頁水平溢出。
- 實際完成「雷達族群問句 → 矩陣本題文章 → 返回被動元件本題」：文章從頂端開啟，首尾保留
  原問句；返回後同一矩陣列重新取得焦點、問句與「先讀本題文章」行動仍在。排版沒有改動任何
  數字、文字、DOM 順序、article ID 或一次性 origin 狀態。
- 修改前、視覺 mock、正式修改後與各 breakpoint 畫面留在
  `tmp/research-learning-audit-2026-08-10-wave76/`。固定 iframe 不是實機；本輪未涵蓋真機旋轉、
  完整實體鍵盤巡覽、螢幕閱讀器、200%／400% zoom 與儀器化 WCAG 對比量測。
- 本輪相對 wave75 的 payload 只改 `learningPathVersion: 38 → 39`；目前相對 Git `HEAD` 的完整
  payload 也只有版本 `36 → 39`，文章數維持 274。排除版本後 canonical payload SHA 前後均為
  `1df222fbbfe61c45f9708ecf26d0de5410ed00085aacee9341727083d5fbb189`。
  `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 482 tests 全綠；qual notes、leading
  hypotheses、research radar、method audit、knowledge graph lint 均通過，research queue 保留
  8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、`research.html`
  `003dbe9148b38b191fa457f00cd3a48dab215f86a5f81c9c010cc4ec5e758d60`。

## 研究雷達把待辦順序與投資排名分開，卡片正文改用完整寬度 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、候選 rank／status、selection log、原始
Markdown、文章／圖譜映射、來源、claim、comparison、monitor、證據判定與複核時鐘零變動**；
本次只調整研究雷達候選卡的閱讀層級、顯示翻譯與發布版本。

- 固定 884px、390px iframe 走讀發現，原本的「順序 N」置於 72px／51px 左側直欄，既可能被
  新手誤讀成股票排名，也把 390px 卡片正文壓到 291px。設計 mock 與同狀態修改前畫面並排後，
  採用卡頂橫列「研究順序 N · 只排研究待辦，不是股票或投資排名」，正文改用完整卡寬。
- `learningPathVersion` 升為 38。884px 第一張卡由 635px 降為 581px，正文內寬由 720px 增為
  792px，三個族群問句可同列；390px 正文內寬由 291px 增為 342px，卡高因新增完整邊界句由
  910px 微增為 916px。320px、390px、884px、1280px 均有
  `documentElement.scrollWidth == body.scrollWidth == innerWidth`，水平溢出為 0。這些是固定 viewport
  的 deterministic layout 契約，不是抽樣統計，SE／t／有效獨立觀測不適用。
- 卡面只把既有 status 顯示翻成「已有文章與關係圖」、「補進既有研究」、「等待更多證據」與
  「暫緩研究」；已升格文章按鈕改為「閱讀這題的文章 · N 分鐘」。原始 status label、rank 與
  audit payload 均保留，沒有改寫研究判定。實際點擊第一題後能在文章首尾看到雷達來處，返回時
  恢復原候選 `radar-RC-AI-RACK-EMC-CERTIFICATION` 的焦點與捲動位置。
- 深色、淺色與 1280／884／390／320px 完成目視與 DOM 走讀；修改前、設計 mock、正式修改後與
  量測紀錄留在 `tmp/research-learning-audit-2026-08-10-wave75/`。固定 iframe 不是實機；本輪未
  涵蓋真機旋轉、完整實體鍵盤巡覽、螢幕閱讀器、200%／400% zoom 與儀器化 WCAG 對比量測。
- 本輪相對 wave74 的 payload 只改 `learningPathVersion: 37 → 38`；目前相對 Git `HEAD` 的完整
  payload 也只有版本 `36 → 38`，文章數維持 274。排除版本後 canonical payload SHA 前後均為
  `1df222fbbfe61c45f9708ecf26d0de5410ed00085aacee9341727083d5fbb189`。
  `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 482 tests 全綠；qual notes、leading
  hypotheses、research radar、method audit、knowledge graph lint 均通過，research queue 保留
  8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、`research.html`
  `55ae6b63426e5537f8df3f6aec6bb6b1fa5357ece873d0077811503e42eeefbe`。

## 窄幅專注閱讀移除已隱藏的大綱空欄 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章／圖譜映射、來源、
claim、comparison、monitor、證據判定與複核時鐘零變動**；本次只修正 781–1180px 專注閱讀的
CSS grid 契約與對應發布版本。

- 固定 884px iframe 走讀 AI 機櫃 EMC 文章發現，`.outline` 雖已隱藏，較高 specificity 的
  `body.focus-mode .reader-inner` 仍保留 240px 大綱欄與 48px gap；專注閱讀正文因此只有 540px
  且靠左，畫面右側留下無內容空間。一般 master-detail 狀態則是清單 360px、正文 468px，並非
  同一根因。
- `learningPathVersion` 升為 37。`≤1180px` 現在明確把 focus-mode reader grid 改為單欄、
  `max-width:720px`、`gap:0`；同一 884px 契約量得容器 x=82／720px、正文 x=110／664px，
  `documentScrollWidth == bodyScrollWidth == innerWidth == 884`。這是單一 deterministic viewport
  契約，不是抽樣統計，SE／t／有效獨立觀測不適用；獨立 CSS 算式
  `720 - 2×28 = 664` 與 `(884 - 720) / 2 = 82` 和瀏覽器量測一致。
- 1280px 專注閱讀仍維持 `836px 240px` 雙欄與 48px gap，右側大綱可見；關閉專注閱讀後 884px
  仍還原清單／文章雙欄。正文中段的浮動名詞速查右緣為 88px，置中文章左緣為 110px，相隔
  22px，畫面不再壓住本文。深色、淺色、返回清單與正文中段均完成本輪目視檢查。
- 修改前後、寬幅與名詞速查畫面留在 `tmp/research-learning-audit-2026-08-10-wave74/`。884px 是
  固定 iframe 契約，不是實機；本輪未涵蓋真機旋轉、完整實體鍵盤巡覽、螢幕閱讀器、200%／400%
  zoom 與儀器化 WCAG 對比量測。
- 相對 Git `HEAD`，payload 頂層只改 `learningPathVersion: 36 → 37`；文章數維持 274，排除版本後
  canonical payload SHA 前後均為
  `1df222fbbfe61c45f9708ecf26d0de5410ed00085aacee9341727083d5fbb189`。`Darwin 25.5.0 arm64`、
  Python 3.11.11 預設環境執行 482 tests 全綠；qual notes、leading hypotheses、research radar、
  method audit、knowledge graph lint 均通過，research queue 保留 8 個既有時效提醒。連續兩次
  dashboard build SHA 一致：`index.html`
  `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、`research.html`
  `cfa1f4d0effaaf37fd119a39e0a9118c3517b6c6d08dccfac614de4130df2710`。

## 文末關聯依實際閱讀欄重排且可穿越原搜尋 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章／圖譜映射、來源、
claim、comparison、monitor、證據判定與複核時鐘零變動**；本次只修正文末延伸學習的響應式
閱讀順序，以及文章內換篇與左側搜尋／篩選的狀態邊界。

- 1280×720 深色走讀「AI 儲存資料平面 → 從這篇接著學」發現，整個視窗雖寬，三欄
  master-detail 中延伸區實際只有 365px、內部 319px；理解檢查與下一站仍被排成 136px／174px
  兩欄，中文幾乎逐字換行，讀者無法先回答本篇問題再理解下一站為何相連。
- `learningPathVersion` 升為 36。`.learning-path` 改成 inline-size container；內容寬度不超過
  620px 時，`.learning-handoff` 與 `.learning-path-grid` 一律依 DOM 順序單欄，寬專注閱讀仍保留
  並排比較。沒有改卡片文字、文章選擇、route、graph、phase、共同公司／族群或關係線。
- 同一流程另驗出功能錯誤：文章若從只命中自己的搜尋結果開啟，下一站雖可見，`renderAll()` 卻會
  讓 `ensureSelected()` 依 `filteredArticles()` 把選取立刻改回舊文。現在開啟中的正式 article
  優先於左側結果；下一站可正常更新 hash、H1 與站次。原搜尋與篩選不清除，左側明示「目前閱讀
  不在左側結果」；首次選文的 article ID 與捲動位置另行保存，返回清單時可重建原選取與焦點。
- 1280×720 深色、淺色窄閱讀欄與淺色專注閱讀均完成目視檢查：前者為單欄，後者有足夠寬度時維持
  兩欄。固定 884px iframe 中兩張交接卡各為 494px，且 `documentScrollWidth == bodyScrollWidth ==
  frameWidth == 884`。從只命中 AI 儲存文章的搜尋實際前往第 2/8 站後，hash 變為 AMD Helios article
  ID，H1 變為「平台開始出貨後，還要看到哪些客戶節點才算真正部署？」；左側原搜尋與提示同時
  保留。修改前、預覽與最終畫面留在 `tmp/research-learning-audit-2026-08-10-wave73/`。884px 為
  固定 iframe 契約測試，不是實機；本輪未涵蓋實機手機、完整實體鍵盤巡覽、螢幕閱讀器與 WCAG
  對比量測。
- 相對緊鄰本輪實作前的 wave72 產物，payload 只改 `learningPathVersion: 35 → 36`；排除版本後
  canonical payload SHA 維持
  `1df222fbbfe61c45f9708ecf26d0de5410ed00085aacee9341727083d5fbb189`。相對目前 Git `HEAD`，
  頂層差異仍只有 `articles` 與 `learningPathVersion: 33 → 36`；文章數維持 274，只有 wave71 已
  記錄的兩篇市場議題 `sections` 不同。`Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行
  482 tests 全綠；qual notes、leading hypotheses、research radar、method audit、knowledge graph
  lint 均通過，research queue 保留 8 個既有時效提醒。連續兩次 dashboard build SHA 一致：
  `index.html` `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、
  `research.html` `64ff5a1f09402a346b13f02657e35c6219bcd29959756f5cfc74425ff071257c`。

## 雷達問句先跨滿族群矩陣再進入整體盤點 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、候選排序、文章／圖譜映射、
來源、claim、comparison、monitor、證據判定與複核時鐘零變動**；本次只調整雷達族群問句進入
矩陣後的閱讀層級與響應式排版。

- 1280×720 深色走讀「雷達第 1 題被動元件問句 → 族群矩陣」發現，本題問句與文章雖已正確承接，
  卻被塞進四欄盤點的第一欄；完成度、財務缺口與待辦同時包圍它，新手容易把「這題要回答什麼」
  誤認成族群整體進度的一部分。
- `learningPathVersion` 升為 35。`renderMaturityOrigin()` 改為所選 `.maturity-reader-row` 的直接子項，
  在四個盤點 cell 之前以 `grid-column: 1 / -1` 橫跨整列。已升格候選依序顯示原題次、同一逐字問句、
  同一篇本題文章與返回行動；下方才是族群起點、已完成、最大缺口與下一步。未升格候選明示尚無
  本題文章，改用兩欄／單欄配置，不留下空白文章欄，也不猜替代內容。
- 1280×720 深色與淺色驗收已升格三欄版，深色另驗收未升格兩欄版；固定 884px iframe 驗收兩欄
  版，量得 `documentScrollWidth == bodyScrollWidth == innerWidth == 884`，承接卡欄寬各 397px。
  本題文章開啟後可返回原矩陣列，承接卡、問句、所選族群與鍵盤焦點均恢復。修改前後畫面與走讀
  筆記留在 `tmp/research-learning-audit-2026-08-10-wave72/`。884px 是固定 iframe 契約測試，不是
  實機裝置；本輪未涵蓋實機手機、完整實體鍵盤巡覽、螢幕閱讀器與 WCAG 對比量測。
- 相對緊鄰本輪實作前的 wave71 產物，payload 只改 `learningPathVersion: 34 → 35`；排除版本後
  canonical payload SHA 維持
  `1df222fbbfe61c45f9708ecf26d0de5410ed00085aacee9341727083d5fbb189`。相對目前 Git `HEAD`，
  頂層差異仍只有 `articles` 與 `learningPathVersion: 33 → 35`；文章數維持 274，只有 wave71 已
  記錄的兩篇市場議題 `sections` 不同。`Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行
  482 tests 全綠；qual notes、leading hypotheses、research radar、method audit、knowledge graph
  lint 均通過，research queue 保留 8 個既有時效提醒。連續兩次 dashboard build SHA 一致：
  `index.html` `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、
  `research.html` `6ba146f8976afb4899af05e6df8f469d4b5b3b4c89279616f5ae95bd84ee06c2`。

## 市場議題主正文先建立多步機制全貌 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、文章／圖譜映射、來源、claim、comparison、
monitor、證據判定與複核時鐘零變動**；本次只調整兩篇已升格市場議題的技術段落用詞，並在作者
已連續寫出至少三個粗體段首時，把相同主句先排成同節閱讀地圖。

- 884×863 深色走讀 EMC 市場議題發現，大綱跳轉與標題定位正常，但「四道關卡」雖已有四個作者
  段首，畫面仍直接進入英文密度較高的連續長段落；新手必須自行抽出各關卡負責什麼、哪裡不同。
  AI 儲存文章的「三條路徑」也有相同結構，因此選為第二篇交叉驗證。
- `learningPathVersion` 升為 34。`readerSectionMapItems()` 只從市場議題讀者正文的一節開頭，連續
  取得 paragraph 第一個非空 bold run；遇到非段落或非粗體段首即停止，至少三項才顯示「本節先看」。
  卡片置於同節名詞與完整 blocks 之前，label 逐字重用原文；`ol` 保留順序語意，視覺編號對輔具
  隱藏，畫面明示編號不代表重要性、上下游或因果關係。新手導讀、研究摘要、查核附錄、正式筆記
  與多空小作文不套用；section 容器不超過 480px 時改成單欄。
- EMC 四個段首改為「元件與材料／被測設備範圍／量測程序與責任／實驗室可用量能」，AI 儲存的
  `Checkpoint` 改為「訓練存檔（checkpoint）」並把 `transport` 先寫成「資料傳輸路徑」；兩篇
  各追加同狀態 `editorial:reader_section_leads_plain_language` transition。baseline method audit
  證明 source／claim／comparison／monitor 與鎖定 meta 未變。
- EMC 與 AI 儲存深色、EMC 淺色固定 884×863 viewport 均完成目視檢查，三個狀態的
  `documentScrollWidth == bodyScrollWidth == innerWidth == 884`；EMC 顯示 4 項、AI 儲存顯示 3 項，
  正式公司筆記維持 0 張。修改前後畫面與走讀筆記留在
  `tmp/research-learning-audit-2026-08-10-wave71/`。本輪未涵蓋實機手機、完整實體鍵盤巡覽、
  螢幕閱讀器與 WCAG 對比量測；容器單欄由程式契約測試覆蓋，不表述為實機手機驗收。
- 相對 wave70 基線，payload 頂層只改 `learningPathVersion: 33 → 34` 與 `articles`；文章數維持 274，
  只有 `topic-MI-2026-08-09-AI-RACK-EMC-CERTIFICATION`、
  `topic-MI-2026-08-09-AI-STORAGE-DATA-PLANE` 的 `sections` 改變，其餘文章欄位零變動。排除版本後
  canonical payload SHA 由 `780c8bb050fc994f0b05eaaed1b16f5ed4c7135263e3d197b5746ad154bafb62`
  變為 `1df222fbbfe61c45f9708ecf26d0de5410ed00085aacee9341727083d5fbb189`。
  `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 482 tests 全綠；qual notes、leading
  hypotheses、research radar、method audit、knowledge graph lint 均通過，research queue 保留
  8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、`research.html`
  `8a4d0d260c02c25da5642795b11ef7983d36c958e77df56caa5cf759c7120deb`。

## 市場議題在技術細節前先說結論邊界 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章／圖譜映射、
來源、claim、comparison、monitor、證據判定與複核時鐘零變動**；本次只把同篇既有研究摘要的
結論、未知與下一步提到讀者導讀後，讓不熟產業的讀者先知道本文能下到哪一層。

- 884×863 深色走讀 EMC 市場議題發現，閱讀任務約在文章內 571px，既有「研究摘要：已知、未知
  與下一步」約在 4,304px；大綱跳轉本身正常，但讀者必須先穿過三句重點、角色、路線、重要性、
  名詞與追蹤，才知道本文現在能說、不能說與接著查什麼。
- `learningPathVersion` 升為 33。只有市場議題既有五項摘要標籤完整且唯一時，導讀後才新增
  「這篇目前能說到哪裡」，逐 run 重用「一句話結論、尚未知道、下一步看什麼」，並沿用 active
  主張類型與 `liveConfidence(article)`。缺欄或重複標籤不猜測；正式筆記與多空小作文不套用。
- 「看完整研究摘要」會把捲動與鍵盤焦點送到原摘要標題；「查本文名詞」只在同篇有字典時開啟
  既有原生 dialog，關閉後回到原按鈕。完整五項摘要仍留在原位置，沒有建立第二套結論或術語。
- 深色與淺色固定 884×863 viewport 均完成目視檢查，`documentScrollWidth == bodyScrollWidth ==
  innerWidth == 884`；另一篇市場議題可依同一契約顯示，正式公司筆記維持 0 張。修改前後畫面留在
  `tmp/research-learning-audit-2026-08-10-wave70/`。本輪未涵蓋實機手機、完整實體鍵盤巡覽、
  螢幕閱讀器與 WCAG 對比量測，仍保留為人工裝置／輔具驗收項目。
- 相對修改前的 wave70 基線，payload 頂層只改 `learningPathVersion: 32 → 33`；文章數維持 274，
  排除版本後完整 canonical payload 逐項相同，前後 SHA 均為
  `780c8bb050fc994f0b05eaaed1b16f5ed4c7135263e3d197b5746ad154bafb62`。
  `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 480 tests 全綠；qual notes、leading
  hypotheses、research radar、method audit、knowledge graph lint 均通過，research queue 保留
  8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、`research.html`
  `cf06dc08a2eda92be4711930a14868542fb49d805a88baf8ab456f3d99236d92`。

## 雷達問句在族群矩陣維持同一篇本題文章 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、候選排序、文章／圖譜映射、
來源、claim、comparison、monitor、證據判定與複核時鐘零變動**；本次只修正讀者由雷達族群問句
進入矩陣後的文章承接與一次性導覽狀態。

- 1280×720 深色走讀「雷達第 1 題的被動元件問句 → 族群矩陣 → 起讀文章」發現，矩陣雖保留
  「零件層如何抑制或隔離電磁干擾？」，主要按鈕卻改開通用的 AI 電容角色文章；進文後也只記得
  被動元件矩陣，EMC 問句完全消失。讀者不是看不懂單句，而是在跨頁時被換成另一個學習任務。
- `learningPathVersion` 升為 32。由雷達定位矩陣時同步選取正式族群；已升格候選在矩陣新增
  「本題起讀文章」，只開同一 `candidate.articleId`，通用 `learningStart` 降為「再讀族群基礎」。
  卡片明示「已完成／最大缺口／下一步」是族群整體盤點、不是本題答案。未升格候選不猜替代文章，
  改寫明「本題尚未升格文章」，再以族群基礎協助認識角色。
- 本題文章使用前端一次性 `maturity-radar` origin，保存正式 candidate、group 與同一逐字問句；
  文章首尾顯示「被動元件 · 雷達第 1 題」、問句與返回矩陣行動，相符角色卡仍重用同候選既有
  `readerGroupQuestions`。返回後重建矩陣來處、選取並聚焦原列；切到任何非該候選正式 article
  的下一站或相關文章時立即清除舊雷達脈絡，不把 EMC 問句錯套到別篇。
- 最終 1280×720 深色走讀證實矩陣主要行動開啟 EMC 升格文章，而不是 AI 電容文章；返回後問句、
  本題文章與焦點均保留，下一站則三者清除。淺色首屏亦完成目視檢查，`documentScrollWidth ==
  bodyScrollWidth == innerWidth == 1280`。修改前後畫面留在
  `tmp/research-learning-audit-2026-08-10-wave69/`。本輪未涵蓋實機手機、實體鍵盤完整巡覽、
  螢幕閱讀器與完整 WCAG 對比量測，仍保留為人工裝置／輔具驗收項目。
- 相對修改前的 wave69 基線，payload 頂層只改 `learningPathVersion: 31 → 32`；排除版本後完整
  canonical payload 逐項相同，前後 SHA 均為
  `780c8bb050fc994f0b05eaaed1b16f5ed4c7135263e3d197b5746ad154bafb62`。
  `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 479 tests 全綠；qual notes、leading
  hypotheses、research radar、method audit、knowledge graph lint 均通過，research queue 保留
  8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、`research.html`
  `150a140499bf18db5fb1d03a89d270f437a37821c7ae5d47703acb84278d8957`。

## 升格文章「為什麼重要」改為主句先行 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、來源、claim、comparison、monitor、
證據判定與複核時鐘零變動**；本次只改寫兩篇已升格研究雷達文章的白話導讀，並讓作者明寫的
段落主句成為可掃讀錨點。

- 1280×720 深色走讀「雷達候選 → 角色問句 → 為什麼重要」發現，角色卡已把被動元件、電源與
  整櫃責任拆開，下一段卻立即回到四個沒有主句的長段落；讀者必須重新從內文整理情境、常見
  誤讀、責任與證據邊界，角色脈絡沒有順利接回正常文章。
- `learningPathVersion` 升為 31。AI 機櫃 EMC 與 AI 儲存資料平面的「為什麼重要」分別改為
  4 個與 3 個作者明寫的粗體白話主句，並把長複句拆成較短句子；原結論、公司邊界與反證方向
  保留。renderer 只在粗體確實是段落第一個 run 時加 `data-reader-lead`、青色主句與分隔線，
  沒有主句的文章維持原樣，不從正文自動摘要。
- 兩篇各追加 `editorial:reader_led_why_it_matters` 同狀態 transition；baseline lint 證明全部
  source／claim／comparison／monitor 與鎖定 meta 未變。registry 變動另以 append-only
  `notes/research_method_reviews/2026-08-10_01.json` 保存 `RMA-2026-08-10-01`，測試判定日同步
  到 2026-08-10；快照如實保留目前 4 個待回顧 monitor、修正學習 attention 與校準 not-ready，
  不把可讀性改寫冒充新證據或完成回查。
- 瀏覽器實測 EMC 文章顯示 4 個主句、儲存文章顯示 3 個，深色與淺色
  `documentScrollWidth == innerWidth == 1280`；直接文章 deep link 不虛構雷達來處。修改前後畫面
  留在 `tmp/research-learning-audit-2026-08-10-wave68/`。本輪未涵蓋實機手機、實體鍵盤、
  螢幕閱讀器與完整 WCAG 對比量測，仍保留為人工裝置／輔具驗收項目。
- 相對 `HEAD`，payload 頂層只改 `learningPathVersion` 與新 method audit；文章只改上述兩篇的
  `sections` 與由「為什麼重要」首段逐字擷取的 `readingMission.orientation`，文章數與 ID 零
  變動。`Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 478 tests 全綠；qual notes、
  leading hypotheses、research radar、method audit、knowledge graph lint 均通過，research
  queue 保留 8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、`research.html`
  `22a4a01ea531116a58881d2176b2ded7cfe19049523ca1dbc3a4a215d690fbfb`。

## 雷達族群問句帶進原升格文章 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章／圖譜映射、
學習路線、候選排序、證據與研究進度零變動**；本次只把研究雷達既有的族群分工問題帶到
同一候選自己的升格文章，補齊新手從選題進文後遺失的一層脈絡。

- 1280×720 深色走讀「雷達第 1 題 → 已升格 EMC 文章 → 產業角色」發現，候選卡已分別問清
  被動元件、電源供應與整櫃組裝要驗證什麼，進文後三張角色卡卻只剩通用族群介紹；新手必須
  自己重新把三個角色接回本題，容易把一般角色與這次研究責任混在一起。
- `learningPathVersion` 升為 30。前端只在 origin 為 `radar`、candidate 可解析，且
  `candidate.articleId === article.id` 時，把同一候選既有 `readerGroupQuestions` 逐字放到相符
  角色卡；通用角色與混淆邊界仍沿用正式族群指南。直接文章 deep link 與沿路線切到下一站都
  顯示 0 張雷達問句卡，不把前一題脈絡套到另一篇文章，也不新增或改寫研究 payload。
- 1280×720 深色與淺色瀏覽器實測，原升格文章顯示 3 張問句卡且全文可見，
  `documentScrollWidth == innerWidth == 1280`；直接 deep link 與下一站各為 0 張。修改前後及
  淺色畫面留在 `tmp/research-learning-audit-2026-08-10-wave67/`。本輪以固定桌機 viewport、
  瀏覽器語意樹與程式化焦點／入口檢查為證據，未涵蓋實機手機、實體鍵盤與螢幕閱讀器，仍保留
  為人工裝置／輔具驗收項目。
- 排除 `learningPathVersion` 後，相對 `HEAD` 的完整 payload canonical SHA 皆為
  `50862ce6c16d786e1ee530944eeea7417f5c68c77a1ae2220f129de76ace1018` 且逐項相同。
  `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 477 tests 全綠；qual notes、leading
  hypotheses、research radar、method audit、knowledge graph lint 均通過，research queue
  保留 8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48aeae784116da44274eb81cb38f9ba38c5d04e3e7efd6e41c97b94e4861`、`research.html`
  `6930ddc24026cfe53f07329ab39d08490e95f4cb4dc960e8375dcb0705bb0d75`。

## 雷達文章保留原研究問題 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章／圖譜映射、
學習路線、候選排序、證據與研究進度零變動**；本次只補上已升格雷達候選進文後的
工作階段導覽脈絡。

- 走讀「研究雷達候選題 → 已升格文章 → 返回雷達」發現，候選卡原本已說明順序只是研究資源
  安排，但按下「閱讀研究」後這個邊界完全消失；文章也沒有顯示原白話問題或返回同一候選卡的
  行動，讀者容易把雷達名次誤讀成受惠或投資排序。
- `learningPathVersion` 升為 29。已升格文章按鈕補上既有閱讀時間，開文時只在前端保存正式
  candidate ID、雷達與 window 捲動位置；文章頁首、行動版返回鈕與閱讀末端會顯示原第 N 題、
  同一白話問句與非投資排名邊界。返回恢復同一候選卡位置與鍵盤焦點；一般文章清單與直接文章
  deep link 不顯示雷達來處，也不把導覽狀態寫進研究 payload。
- 884×863 in-app browser 深色實測，文章來處完整可見、`documentScrollWidth == innerWidth`；返回後
  雷達捲動位置恢復為 309.5px，焦點回到同一候選卡。淺色狀態與直接文章 deep link 另行走讀，
  前者保留相同導覽，後者維持「返回研究清單」。修改前後畫面留在
  `tmp/research-learning-audit-2026-08-10-wave66/`；本輪未涵蓋實機手機、實體鍵盤與螢幕閱讀器，
  仍保留為人工裝置／輔具驗收項目。
- 排除 `learningPathVersion` 後，相對 `HEAD` 的完整 payload canonical SHA 皆為
  `50862ce6…` 且逐項相同。`Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 476 tests 全綠；
  qual notes、leading hypotheses、research radar、method audit、knowledge graph lint 均通過，
  research queue 保留 8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48ae…`、`research.html` `066388ae…`。

## 圖譜關係解讀改為單一捲動 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章／圖譜映射、
學習路線、階段、站次、關係、證據與研究進度零變動**；本次只改善文章進圖後閱讀一條關係與
回到原學習路線的顯示層。

- 1280×720 走讀「文章 → 公司曝險圖 → 示範讀一條關係」發現，關係詳情只有 328px 可視高度，
  實際內容為 875px，形成圖譜頁與詳情卡兩層捲動；三步解讀首屏只露出約兩步。讀到卡片內部後，
  原本的文章返回脈絡也離開視野，必須再找回圖譜頂端。
- `learningPathVersion` 升為 28。桌機寬度至少 981px、可視高度不超過 840px 時，詳情取消 sticky
  與自身 overflow，改由 `graphPage` 單一捲動；從下方關係清單選線時同步聚焦並捲到新詳情。
  article-learning origin 另投影到三步解讀末端，顯示剛才文章、下一站與至少 44px 的返回按鈕；
  返回沿用原契約恢復延伸卡位置、焦點與矩陣起點。直接圖譜入口不顯示這份一次性狀態。
- 1280×720 深色與淺色實測，修改後詳情 `clientHeight == scrollHeight`（NVIDIA 關係均為
  1025px）、`overflow-y: visible`、頁面無水平溢位；返回按鈕高度 44px。從關係清單改選
  Infineon 後，標題、焦點與捲動都到新詳情；從文章進圖再返回時 URL、系統問題、第 1/9 站、
  原圖譜按鈕焦點與約 4599px 閱讀位置均保留。修改前後畫面留在
  `tmp/research-learning-audit-2026-08-10-wave64/`；固定桌機 viewport 未涵蓋實機手機、實體鍵盤
  導覽與螢幕閱讀器，仍保留為人工裝置／輔具驗收項目。
- 排除 `learningPathVersion` 後，相對 `HEAD` 的完整 payload canonical SHA 皆為
  `50862ce6…`，`articles`、`knowledgeGraph` 與 `groupMaturity` 逐項相同。`Darwin 25.5.0 arm64`、
  Python 3.11.11 預設環境執行 476 tests 全綠；qual notes、leading hypotheses、research radar、
  method audit、knowledge graph lint 均通過，research queue 保留 8 個既有時效提醒。連續兩次
  dashboard build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `afec3f9c…`。

## 圖譜保留文章學習脈絡 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章／圖譜映射、
學習路線、階段、站次、關係、證據與研究進度零變動**；本次只補齊文章延伸卡進入圖譜後的
一次性讀者導覽狀態。

- 完整走讀「系統問題 → 第一站文章 → 從這篇接著學 → 查看公司曝險圖」發現，圖譜雖能顯示
  同一學習路線與階段，首屏卻沒有說明讀者從哪篇文章來、如何回去繼續下一站；原按鈕被移除後
  鍵盤焦點也落到 `body`，使建立關聯的步驟反而切斷原學習脈絡。
- `learningPathVersion` 升為 27。文章的圖譜卡現在保存文章 ID、閱讀欄與 window 捲動位置，並
  連同文章原本的矩陣／圖譜起點建立一次性 `article-learning` origin。圖譜首屏新增「文章 →
  關係圖」、剛才文章、下一站與至少 44px 的「回到剛才文章」；進圖焦點送到此脈絡，返回後恢復
  同一張圖譜卡位置、按鈕焦點與原系統問題。直接圖譜 deep link、頁首圖譜分頁、雷達與其他入口
  都清空 origin，不會虛構文章來源或把狀態寫進 payload。
- 1280×720 深色與淺色實測，文章進圖後 origin 可見、返回按鈕高度 44px、焦點落在脈絡標題；
  返回後 URL、矩陣起點與第 1/9 站文章都保留，焦點回到「查看公司曝險圖」，頁面寬度等於
  viewport。一般圖譜分頁會隱藏空 origin。修改前後畫面留在
  `tmp/research-learning-audit-2026-08-10-wave63/`；固定桌機 viewport 未涵蓋實機手機與螢幕閱讀器，
  仍保留為人工裝置／輔具驗收項目。
- 排除 `learningPathVersion` 後，相對 `HEAD` 的完整 payload canonical SHA 皆為
  `50862ce6…`，`articles`、`knowledgeGraph` 與 `groupMaturity` 逐項相同。`Darwin 25.5.0 arm64`、
  Python 3.11.11 預設環境執行 476 tests 全綠；qual notes、leading hypotheses、research radar、
  method audit、knowledge graph lint 均通過，research queue 保留 8 個既有時效提醒。連續兩次
  dashboard build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `026ca800…`。

## 市場議題先顯示閱讀行動與三句讀法 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章／圖譜映射、
學習路線、階段、站次、問題、證據與研究進度零變動**；本次只調整文章開場的既有閱讀任務與
三句重點顯示方式。

- 1280×720 新手走讀發現，文章開場先連續顯示符號、名詞與背景三個可展開輔助區，真正的
  「開始讀三句重點」落在首屏之外；進入三句後又只有「重點 1／2／3」，未交代新手應如何依序
  建立主線。
- `learningPathVersion` 升為 26。閱讀任務改為「兩個任務句 → 主要閱讀行動 → 選用輔助說明 →
  原文來源」，主要行動至少 44px；市場議題既有三句只在恰好三句時依原順序標成「先看資料 →
  再補脈絡 → 最後看邊界」，並保留 list／listitem、H3 與 `evidence／context／boundary` 讀法角色。
  其他文章類型仍顯示「重點 N」。所有標籤都屬 renderer 讀法，不是新 claim 或證據分級。
- 1280×720 深色畫面確認主要行動回到文章首屏，點擊後焦點落在同篇三句重點，頁面沒有水平溢位；
  修改前後畫面留在 `tmp/research-learning-audit-2026-08-10-wave62/`。固定桌機 viewport 未涵蓋
  實機手機與螢幕閱讀器，仍保留為人工裝置／輔具驗收項目。
- 排除 `learningPathVersion` 後，相對 `HEAD` 的完整 payload canonical SHA 皆為
  `50862ce6…`，`articles`、`knowledgeGraph` 與 `groupMaturity` 逐項相同。`Darwin 25.5.0 arm64`、
  Python 3.11.11 預設環境執行 476 tests 全綠；qual notes、leading hypotheses、research radar、
  method audit、knowledge graph lint 均通過，research queue 保留 8 個既有時效提醒。連續兩次
  dashboard build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `7a3d3bfb…`。

## 研究中心首次進入不再自動選文 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章／圖譜映射、
學習路線、階段、站次、問題、證據與研究進度零變動**；本次只調整研究文章第一次進入時的
未選文狀態與既有入口焦點。

- 1280×720 首屏走讀發現左側已要求新手「先選一個系統問題」，右側卻自動顯示最新文章全文；
  最新更新與建議起點因而同時成為兩個互相競爭的主要任務。
- `learningPathVersion` 升為 25。尚未開文時不再由 `ensureSelected()` 自動選取清單第一篇；預設
  閱讀欄改為同一條「系統問題 → 市場議題 → 知識圖譜」順序，且只把「先看族群矩陣」設為主要
  行動，並明示清單第一篇只代表更新排序。搜尋／篩選後若仍未選文，改顯示一般選文或無結果提示；
  已開文章被篩掉時才沿用既有第一筆 fallback。直接文章深連結仍立即開文，並補齊標題焦點；從
  首屏前往族群矩陣後，焦點改送到矩陣標題。
- 1280×720 淺色與深色實測，首屏沒有 `.result.selected` 或文章標題，右側只顯示未選文起點，
  `documentElement.scrollWidth` 等於 1280px。主按鈕可進入 `#maturity` 並聚焦
  `maturityIntroTitle`；主動選文與直接深連結都開啟同一文章、閱讀欄回頂且聚焦白話主標。搜尋
  有結果／無結果時分別顯示一般選文／空結果提示。修改前後畫面留在
  `tmp/research-learning-audit-2026-08-10-wave61/`；固定桌機 viewport 未涵蓋實機手機與螢幕閱讀器，
  仍保留為人工裝置／輔具驗收項目。
- 排除 `learningPathVersion` 後，相對 `HEAD` 的完整 payload canonical SHA 皆為
  `50862ce6…`，`articles`、`knowledgeGraph` 與 `groupMaturity` 逐項相同。`Darwin 25.5.0 arm64`、
  Python 3.11.11 預設環境執行 476 tests 全綠；qual notes、leading hypotheses、research radar、
  method audit、knowledge graph lint 均通過，research queue 保留 8 個既有時效提醒。連續兩次
  dashboard build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `385c0a24…`。

## 族群路線展開改用整列階段圖 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章／圖譜映射、
學習路線、階段、站次、問題、證據與研究進度零變動**；本次只調整族群矩陣的既有路線預覽排版。

- 完整走讀「第一次進入 → 系統問題 → 第一篇文章 → 三句重點 → 延伸學習 → 關係圖譜」後，
  文章與圖譜已有明確起點；較大的剩餘斷點是桌機展開 9 站路線時，全部階段仍被塞在四欄中的
  單一窄卡，形成很長的直向清單，也讓讀者難以先看出三個學習階段。
- `learningPathVersion` 升為 24。780px 以上只要路線 map 展開，該卡就跨滿整列；多階段路線按
  至少 240px 的自適應欄寬並排，單階段站點使用至少 280px 的自適應欄寬。路線收合時仍保留四張
  問題卡比較，780px 以下仍維持單欄，不以橫排犧牲閱讀順序。路線 summary 另明確處理 Enter／
  Space，展開後焦點留在原控制上。
- 1280×720 淺色與深色實測，收合時四張路線卡同列，展開後三個既有階段同列且頁面無水平溢位；
  Enter 可展開、Space 可收合，兩次焦點都留在同一個 summary。修改前後與完整流程畫面留在
  `tmp/research-learning-audit-2026-08-10-wave60/`。固定桌機 viewport 未涵蓋實機手機與螢幕閱讀器，
  仍保留為人工裝置／輔具驗收項目。
- 排除 `learningPathVersion` 後，相對 `HEAD` 的完整 payload canonical SHA 為 `50862ce6…`，
  `articles`、`knowledgeGraph` 與 `groupMaturity` 逐項相同。`Darwin 25.5.0 arm64`、Python 3.11.11
  預設環境執行 476 tests 全綠；qual notes、leading hypotheses、research radar、method audit、
  knowledge graph lint 均通過，research queue 保留 8 個既有時效提醒。連續兩次 dashboard build
  SHA 一致：`index.html` `1e3a48ae…`、`research.html` `c3dd548d…`。

## 族群矩陣第一屏改為問題優先 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章／圖譜映射、
學習路線、族群、站次、證據與研究進度零變動**；本次只調整族群矩陣兩個既有入口的顯示順序與標題。

- 頁首已告訴新手「先選一個想弄懂的問題」，但桌機第一個互動區原本仍是 11 個正式族群名稱，
  四張系統問題卡落在其後，讓尚不熟產業分類的讀者又先做一次名詞選擇。
- `learningPathVersion` 升為 23。桌機 DOM 與視覺順序改為先顯示四張既有系統問題卡，再顯示
  「已知道族群名稱？直接查找」；兩個面板仍同時可見。780px 以下仍預設「從問題開始」，並保留
  使用者切換入口、從雷達定位族群及文章返回原路線的既有狀態。
- 1280×720 淺色與深色畫面確認四張問題卡都在族群名稱查找之前，頁面沒有水平溢位；從第一張
  問題卡開啟文章後，頁首保留原系統問題與返回入口，返回時回復同一路線卡與鍵盤焦點。畫面留在
  `tmp/research-learning-audit-2026-08-10-wave59/`。固定桌機 viewport 未涵蓋實機手機與螢幕閱讀器，
  仍保留為人工裝置／輔具驗收項目。
- 排除 `learningPathVersion` 後，相對 `HEAD` 的完整 payload canonical SHA 為 `50862ce6…`，
  `articles` 與 `knowledgeGraph` 逐項相同。`Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行
  476 tests 全綠；qual notes、leading hypotheses、research radar、method audit、knowledge graph
  lint 均通過，research queue 保留 8 個既有時效提醒。連續兩次 dashboard build SHA 一致：
  `index.html` `1e3a48ae…`、`research.html` `e13ae64c…`。

## 市場議題技術表加入原欄名讀法 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章／圖譜映射、
學習路線、節點、關係、表格內容、數字、證據層級與財務判定零變動**；本次只在市場議題主閱讀
流程替既有正文表加入顯示層閱讀順序。

- 本輪從「800VDC 功率半導體鏈」文章實際進入第一個技術段落後，名詞卡雖已解釋 6 個縮寫，
  下一張三欄表仍直接要求新手同時理解「電力鏈位置、材料／元件路徑、成熟度邊界」，沒有說明
  一列應該先看哪裡、最後用哪一欄限制結論。
- `learningPathVersion` 升為 22。`readerTableGuide()` 只在市場議題 `mode=reader` 且非查核附錄時，
  逐字讀取原表欄名：兩欄依序讀左、右，三欄以上依序讀最左、中間、最右。提示以 `aside`、有序
  步驟與 data marker 發布，不讀 row／cell 生成摘要，也不改寫原 table；窄於 620px 的 section
  容器與手機 viewport 都把步驟改成單欄。
- 1280×720 淺色專注閱讀實測，讀法卡位於 330.5–474.7px，原表從 484.7px 開始，首屏仍可看到
  表頭與部分原始列；深色版位置相同。兩者 `documentElement.scrollWidth` 均為 1280px。關閉專注
  閱讀後，實際 365px 正文欄的讀法改成 341px 單欄，原表維持既有 block 卡片與雙欄 cell，沒有
  水平頁面溢位。本輪畫面留在 `tmp/research-learning-audit-2026-08-10-wave58/`。固定 1280×720
  Browser 未涵蓋實機手機 viewport 與螢幕閱讀器，仍保留為人工裝置／輔具驗收項目。
- 排除 `learningPathVersion` 後，相對 `HEAD` 的完整 payload canonical SHA 均為
  `50862ce6…`，`articles` 與 `knowledgeGraph` 逐項相同。`Darwin 25.5.0 arm64`、Python 3.11.11
  預設環境執行 476 tests 全綠；qual notes、leading hypotheses、research radar、method audit、
  knowledge graph lint 均通過，research queue 保留 8 個既有時效提醒。連續兩次 dashboard build
  SHA 一致：`index.html` `1e3a48ae…`、`research.html` `9fb41f2c…`。

## 圖譜開文保留學習起點與返回狀態 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章／圖譜映射、
學習路線、節點、關係、證據層級、篩選結果與財務判定零變動**；本次只補齊圖譜與既有文章之間
的一次性導覽狀態及返回操作。

- 本輪從「800VDC 功率半導體鏈」公司曝險圖實際進入主題文章後，文章原本只呈現一般閱讀畫面，
  沒有說明讀者從哪張圖、哪個投影或哪條關係而來；讀完只能自行切換全域分頁，容易中斷
  「先讀文章、再把內容對回關係線」的學習脈絡。
- `learningPathVersion` 升為 21。所有 `openGraphArticle()` 入口現在先保存 graph ID、公司曝險／
  產業依賴視角、已選節點或關係，以及圖譜捲動位置；文章首尾沿用既有「本次學習起點」元件，
  行動版則沿用黏性返回鍵。返回後重建原圖、恢復選取與捲動位置，並把焦點送回關係詳情或原本的
  起讀按鈕。直接文章深連結與一般清單仍保持無 origin，不會虛構圖譜來源。
- 1280×720 實測從 NVIDIA 證實關係開文，首屏新增 79.5px 起點列並仍看得到新手閱讀任務；
  返回後網址、800VDC 主題、公司曝險視角、NVIDIA 關係與 `graphDetail` 焦點皆恢復。深／淺色
  `documentElement.scrollWidth` 均等於 1280px，沒有水平溢位；本輪畫面留在
  `tmp/research-learning-audit-2026-08-10-wave57/`。目前 Browser 的固定 viewport 未涵蓋實機
  手機重排與螢幕閱讀器，仍保留為人工裝置／輔具驗收項目。
- 排除 `learningPathVersion` 後，相對 `HEAD` 的完整 payload canonical SHA 均為
  `50862ce6…`，`articles` 與 `knowledgeGraph` 逐項相同。`Darwin 25.5.0 arm64`、Python 3.11.11
  預設環境執行 475 tests 全綠；qual notes、leading hypotheses、research radar、method audit、
  knowledge graph lint 均通過，research queue 保留 8 個既有時效提醒。連續兩次 dashboard build
  SHA 一致：`index.html` `1e3a48ae…`、`research.html` `9a84f233…`。

## 知識圖譜首屏先看目前關係再展開控制 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章／圖譜映射、
學習路線、節點、關係、證據層級、篩選狀態與財務判定零變動**；本次只調整知識圖譜完整控制的
初始開合、摘要層級與可逆操作。

- 本輪新擷取的 1280×720 圖譜首屏顯示，四步讀法後仍同時攤開 4 條路線、9 個目前路線主題、
  2 個投影與 4 個證據／台股篩選，真正的關係畫布直到 644px 才開始，首屏只剩 76px 可見。
  這讓產業新手在看到關係前先處理一整面控制，與「最後追產業關係」的入口承諾不一致。
- `learningPathVersion` 升為 20。完整控制現在於所有寬度預設收進原生 `details`，摘要改為
  「目前這張圖」，直接同步目前路線、主題、階段、投影視角與已選證據。桌機仍保留四步新手讀法；
  手機依既有規則再收合讀法。展開完整控制後 summary 不再消失，可再次收合，且切換狀態不會
  另造或覆寫任何圖譜資料。
- 同一 1280×720 狀態下，關係畫布起點提前到 556px，首屏可見範圍由 76px 增為 164px；深／淺色
  均無水平溢位，summary 觸控高度 56px，瀏覽器 console 無錯誤。滑鼠實測可展開 4 條路線與完整
  控制後再收合；本輪畫面留在 `tmp/research-learning-audit-2026-08-10-wave56/`。目前 Browser 的
  固定 viewport 未涵蓋實機手機重排與螢幕閱讀器，仍保留為人工裝置／輔具驗收項目。
- 排除 `learningPathVersion` 後，相對 `HEAD` 的完整 payload canonical SHA 均為
  `50862ce6…`，`articles` 與 `knowledgeGraph` 逐項相同。`Darwin 25.5.0 arm64`、Python 3.11.11
  預設環境執行 475 tests 全綠；qual notes、leading hypotheses、research radar、method audit、
  knowledge graph lint 均通過，research queue 保留 8 個既有時效提醒。連續兩次 dashboard build
  SHA 一致：`index.html` `1e3a48ae…`、`research.html` `0c6538f6…`。

## 族群矩陣從白話問題進入精確追問 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、文章與圖譜映射、
學習路線順序、主張、證據及原本的白話／精確問題零變動**；本次只調整閱讀入口、問題顯示順序
與文章開啟後的鍵盤焦點。

- 本輪新擷取的首頁與矩陣畫面顯示，首頁原本承諾「先看產業全貌」，實際卻開啟問題式族群矩陣；
  路線展開後又直接以 `bulk capacitor`、`800V bus`、`rack ID`、`overlay` 等精確追問當入口。
  首頁第一步因此改成「先選一個系統問題」，逐字對齊矩陣實際提供的入口。
- `learningPathVersion` 升為 19。完整盤點發布中的 4 條路線、25 個站點後，25／25 篇站點文章都
  已有既存 `readerQuestion`。路線站點現在先顯示同篇白話問題，原本的
  `readingMission.question` 逐字留在「讀完再試著回答精確追問」原生 `details` 與文章「想一想」；
  欄位缺漏時安全退回原問題，不從正文或題名生成新文案。瀏覽器 DOM 與獨立解析的發布 payload
  逐站比對為 25／25 完全一致。
- 從清單、矩陣、雷達或圖譜開啟文章後，window 與閱讀欄都回到頂端，鍵盤焦點改送到新文章的
  H1；實測焦點、文章 ID 與網址 hash 相符，避免入口按鈕被移除後把焦點留在頁面根節點。
- 深／淺色 1280×720 實測無水平溢位、console 無錯誤；本輪畫面與逐站 DOM 留在
  `tmp/research-learning-audit-2026-08-10-wave55/`。實機螢幕閱讀器與無法在目前 Browser 固定
  viewport 中執行的手機重排，仍保留為人工輔具／裝置驗收項目。
- 排除 `learningPathVersion` 後，相對 `HEAD` 的完整 payload canonical SHA 均為
  `50862ce6…`，`articles` 與 `knowledgeGraph` 逐項相同。`Darwin 25.5.0 arm64`、Python 3.11.11
  預設環境執行 475 tests 全綠；qual notes、leading hypotheses、research radar、method audit、
  knowledge graph lint 均通過，research queue 保留 8 個既有時效提醒。連續兩次 dashboard build
  SHA 一致：`index.html` `1e3a48ae…`、`research.html` `efcef630…`。

## 正式筆記開場改用讀者語言 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、原始 Markdown、sections／runs payload、
主張、證據、graph edge、族群映射、學習路線與文章推薦零變動**；本次只翻譯正式筆記
「研究定位與重要註記」的可見維運文字。

- 本輪新擷取畫面顯示，讀者沿「先看產業角色 → 接著讀 30 秒摘要」進入第一段正文後，仍直接
  遇到 `族群：power`、`Universe 質化參考`、`meta`、`qual_notes.py --lint` 與
  `last_updated`。由原始筆記與發布 `research.html` payload 兩條獨立路徑完整盤點，結果同為
  121 篇正式筆記中 100 篇含「研究定位與重要註記」及 `族群：<ID>`、97 篇含 Universe 維運語、
  81 篇含查核指令與更新欄位；不是抽樣，兩條路徑的族群 ID 也都沒有錯配。
- `learningPathVersion` 升為 18。閱讀模式只在上述正式筆記段落，把同時屬於該篇
  `article.groups` 的 `族群：<ID>` 顯示為「本文族群：<正式中文標籤>」，並將三組固定維運語
  顯示為「研究中心的公司質化參考／文章上方查核標示／更新日期」。其他文章類型、段落與不完全
  符合白名單的文字原樣保留；轉換只在建立 DOM 時發生，不寫回 run、section 或 payload。
- 瀏覽器實測 8261 茂達及 2337 旺宏，`power／memory` 代碼與固定維運語都已消失，深／淺色
  1280×720 無水平溢位、console 無錯誤。實機螢幕閱讀器與本輪未能調整 viewport 的手機重排，
  仍保留為人工輔具／裝置驗收項目。
- 排除 `learningPathVersion` 後，相對 `HEAD` 的完整 payload canonical SHA 均為
  `50862ce6…`，`articles` 與 `knowledgeGraph` 逐項相同。`Darwin 25.5.0 arm64`、Python 3.11.11
  預設環境執行 475 tests 全綠；qual notes、
  leading hypotheses、research radar、method audit、knowledge graph lint 均為 0 errors，research
  queue 保留 8 個既有時效提醒。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48ae…`、`research.html` `39763345…`。

## 正式筆記與多空文章先看產業角色再進正文 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、topic／正式筆記／多空 Markdown、正文、
主張、證據、graph edge、族群映射、路線順序、文章推薦、閱讀問題與來源段落零變動**；本次只修正
正式筆記與多空文章的起讀焦點順序。

- 以本輪新擷取畫面逐類走過文章首屏。市場議題原本已是「三句重點 → 產業角色」；正式筆記與
  多空文章的角色卡雖緊接閱讀任務，主行動卻直接跳到「30 秒摘要／多空觀點」。台達電桌機樣本
  點擊後角色卡頂端落在視窗上方 278px，390px 手機樣本則整張角色卡底端仍在視窗上方 271px，
  讀者會在不知公司位於哪一層時直接進入研究正文。
- `learningPathVersion` 升為 17。`readingMissionStartsWithRole()` 只對正式筆記／多空文章且至少
  有一筆正式族群白話指南時啟用：首個按鈕改為「先看產業角色」，角色卡尾端再由原
  `startLabel` 產生「接著讀 30 秒摘要／接著讀多空觀點」，兩步都移動鍵盤焦點；缺族群指南時
  直接退回原來源段落。市場議題仍顯示「開始讀三句重點」，不增加第二顆按鈕。
- 由原始筆記／假說與 `research_group_guide.csv` 重新建 library，以及由發布 `research.html`
  獨立解碼 payload，兩條路徑都得到 239／239 篇可採兩段式導引：正式筆記 121／121、多空文章
  118／118，缺口 0。瀏覽器實測第一步分別落在角色標題，第二步落在「30 秒摘要／多空觀點」；
  市場議題仍落在「三句話抓重點」。320×760、390×844、884×900、1280×900 的深／淺色畫面
  均無水平溢位；螢幕閱讀器實機朗讀仍保留為人工輔具驗收項目。
- 排除 `learningPathVersion` 後，相對 `HEAD` 的完整 payload canonical SHA 均為
  `50862ce6…`，`articles` 與 `knowledgeGraph` 逐項相同。`Darwin 25.5.0 arm64`、Python 3.11.11
  預設環境執行 474 tests 全綠；research queue、radar、method audit、knowledge graph lint 均為
  0 errors（queue 保留 8 warnings）。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48ae…`、`research.html` `f758c474…`。

## 清單問題一路延續到文章首屏 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、topic／正式筆記／多空 Markdown、正文、
主張、證據、graph edge、族群映射、路線順序、文章推薦、清單問題與卡片順序零變動**；本次只讓
文章頁首沿用同張清單卡的既有問題。

- 完整盤點 274 篇發布文章（不是抽樣）：35 篇市場議題原本已由 `readerQuestion` 同時驅動清單
  與文章 `h1`；121 篇正式筆記和 118 篇多空文章雖已在清單顯示 `readingMission.question`，
  點入後 0／239 篇延續同一問題，首屏重新回到「質化研究筆記／領先假說報告」等研究頁名。
- `learningPathVersion` 升為 16。`articleReaderHeading()` 現在與清單共用
  `catalogReaderQuestion()`：三類文章都先顯示「這篇先弄懂」與同一問句，再把 topic 原
  `readerTitle` 標為「研究題名」、正式筆記／多空文章原 `readerTitle` 標為「原研究頁名」；
  沒有既有問題時仍退回原 `h1`，不另生問句。
- 完整 payload 與共用 renderer 枚舉 274／274 篇首屏均有既有問題，正式筆記 121／121、多空
  文章 118／118、市場議題 35／35，缺口為 0。瀏覽器另逐類核對清單問題、文章 `h1`、閱讀任務、
  type／article ID 與原頁名標籤；代表文章與 10 篇市場議題互動均吻合。320×760、390×844、
  884×900、1280×900 都無水平溢位。相對 `HEAD` 的 version 14，排除現行 version 16 後完整
  payload canonical SHA 同為 `50862ce6…`，`articles` 與 `knowledgeGraph` 逐項相同；螢幕閱讀器
  實機朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 473 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `580ce5d8…`。

## 三類文章清單都先交代閱讀問題 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、topic／正式筆記／多空 Markdown、正文、
主張、證據、graph edge、族群映射、路線順序、文章推薦與卡片順序零變動**；本次只把既有閱讀
問題提升為清單第一閱讀層。

- 完整盤點 274 篇發布文章（不是抽樣）：35 篇市場議題清單原本已是問題先讀；121 篇正式筆記與
  118 篇多空小作文雖全都有非空 `readingMission.question`，改版前清單卻 0／239 篇顯示，讀者
  選文時仍先看到 `fabless`、`MOSFET`、季度或待驗假說等原始文字。
- `learningPathVersion` 升為 15。`catalogReaderQuestion()` 對市場議題只讀既有
  `readerQuestion`，對正式筆記／多空文章只讀既有 `readingMission.question`；三類卡片都先顯示
  「這篇先回答」，原內容依類型完整保留為次要的「研究題名／原始摘要／待驗命題」。缺既有問題時
  仍退回原卡片，不從正文、題名、搜尋字或公司題材另生問句。
- 移除本次 renderer 並把版本還原為 14 後，改版前後正規化 payload canonical SHA 均為
  `50862ce6…`，`articles` 與 `knowledgeGraph` 逐項相同。瀏覽器另逐類核對 274／274 張卡：
  正式筆記 121／121、多空文章 118／118、市場議題 35／35 的問題文字與既有 payload 完全一致，
  data type／article ID、三種原文標籤與點擊後文章 hash 也正確。320×760、390×844、884×900、
  1280×900 均無水平溢位；螢幕閱讀器實機朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 472 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `630259b5…`。

## 正文每節先說明閱讀目的 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、topic／正式筆記／多空 Markdown、原段落標題、
正文、主張、證據、graph edge、族群映射、路線順序與文章推薦零變動**；本次只在閱讀模式替既有
正文標題補一行白話閱讀目的。

- 完整盤點 239 篇正式筆記／多空文章（不是抽樣），共 2,008 個正文段落：121 篇正式筆記有
  1,435 段，118 篇多空文章有 573 段。原標題多以「資本配置、護城河、驗證 KPI、量化背景、
  H# 假說」描述研究分類，卻沒有直接告訴不熟悉產業的讀者該節要找哪個答案。
- `learningPathVersion` 升為 14。閱讀模式現在會依文章類型與原段落標題，在每個非空標題下加入
  「這節先看」；常見正式筆記與多空段落使用固定白話目的，其他標題使用不新增產業結論的中性
  說明。原 `section`、標題、正文與 payload 都不改寫；市場議題已有新手起讀層，因此不重複顯示。
- 移除本次顯示層並把版本還原為 13 後，改版前與改版後正規化 payload canonical SHA 均為
  `789f246a…`，`articles` 與 `knowledge_graph` 逐項相同。瀏覽器另獨立重算 239／239 篇、
  2,008／2,008 個段落全部有閱讀目的（正式筆記 1,435／1,435、多空文章 573／573），市場議題
  顯示 0 個重複目的。320×760、390×844、884×900、1280×900 均無水平溢位；螢幕閱讀器實機
  朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 471 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `fedb2d32…`。

## 新手閱讀任務就地解碼研究符號 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、topic／正式筆記／多空 Markdown、文章原句、
主張、證據、graph edge、族群映射、路線順序與文章推薦零變動**；本次只替首屏既有重點補上
符號讀法與視覺停頓。

- 完整盤點 239 篇正式筆記／多空小作文（不是抽樣）：121 篇正式筆記的首屏任務原本 0 篇命中
  共通名詞提示，118 篇多空文章只有 6 篇命中；但 238／239 篇至少出現一種來源編號、假說編號、
  季度／半年、MOPS 或研究中心內部分類名稱。這是符號缺少就地解碼，不是文章沒有閱讀任務。
- `learningPathVersion` 升為 13。建置端只用固定正則與既有 `group_names` 產生
  `readerNotations`：`[S#]` 定位來源、多空文章裸 `H#` 定位可證偽假說、`Q#／YYYYQ#` 與
  `YYYYH#` 解釋期間、MOPS 說明公告平台，`Universe／serverodm` 等只翻譯研究分類；每項都附
  「還不能推到哪裡」的邊界。現行 274 篇發布文章中 242 篇共產生 387 項，其中正式筆記 121／121、
  多空文章 117／118；唯一無符號的文章不顯示空入口。
- 任務標題改為「先抓住一個重點，再帶著問題讀」。80 字以上重點只在原有 `；。！？` 後加入
  `aria-hidden` 的零文字停頓；原字序與來源索引保留。符號指南使用原生 `details／summary`、
  預設收合、觸控高度 44px，Enter／Space 均可切換。
- 移除 242 組衍生 `readerNotations` 並把版本還原為 12 後，改版前後完整 payload canonical SHA
  均為 `11ce509f…`，證明文章、段落、來源、主張與關係資料沒有改寫。瀏覽器完整驗收 239／239 篇
  正式筆記／多空文章、382／382 項符號說明：文字與 payload 逐項吻合、238 張指南預設收合、
  1 篇無空卡、0 個水平溢位；320×760、390×844、884×900、1280×900 完成視覺複核。
  螢幕閱讀器實機朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 470 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `2186383c…`。

## 學習路線站點改成問題先讀 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、topic Markdown、文章正文、主張、證據、
graph edge、族群映射、路線順序與文章推薦零變動**；本次只調整族群矩陣與文章內共用路線地圖的
閱讀層級。

- 完整盤點 4 條正式學習路線、25 個站點（不是抽樣）：25／25 都有既有
  `readingMission.question` 與 graph label，但改版前以技術節點名作主標、讀者問題縮在次要小字，
  與研究雷達及族群矩陣入口已採用的「問題先讀」層級不一致。
- `learningPathVersion` 升為 12。共用站點 renderer 現在先顯示「這站先回答」，逐字把既有問題
  放在主標，再以「研究節點：」保留既有 graph label；按鈕最小高度提高為 72px，無障礙名稱同時
  包含問題與研究節點。族群矩陣與文章定位同步套用，原站次、階段、閱讀時間、跳轉與返回路線
  邏輯都不變。
- 把版本還原為 11 後，改版前後完整發布 payload canonical SHA 均為 `5382b6b7…`，證明研究內容
  與關係資料沒有改寫。瀏覽器另獨立重算 4／4 條路線、25／25 個站點：問題主標、節點脈絡、
  72px 高度與無障礙名稱全部吻合，舊「讀完試著回答」為 0；代表站點可進入正確文章並保留目前
  站次及返回原路線。320×760、390×844、884×900、1280×900 皆無水平溢位；螢幕閱讀器實機
  朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 469 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `da888029…`。

## 正式筆記與多空文章先交代閱讀任務 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、topic Markdown、正式筆記／多空正文、
主張、證據、graph edge、族群映射與文章推薦零變動**；本次只把既有文章內容重排成新手起讀與
讀後檢核。

- 完整盤點 274 篇發布文章（不是抽樣）：121 篇正式筆記與 118 篇多空小作文原本 0 篇有首屏
  閱讀任務；121 篇正式筆記全都有「30 秒摘要」，其中 29 篇只有 1 點、其餘 92 篇至少 3 點；
  118 篇多空小作文全都有恰好 3 個「勝負手」。既有 35 篇市場議題中 34 篇已有任務，唯一事件
  錨點沒有結構化新手來源，繼續不從長文抽句或生成新結論。
- `learningPathVersion` 升為 11。正式筆記逐字取「30 秒摘要」前 1～3 點，固定問題只要求讀者
  分清本業、收入來源與證據邊界；多空小作文逐字取 3 個「勝負手」，固定問題只要求比較兩邊各需
  哪些證據。起讀按鈕分別定位「30 秒摘要」或完整「多空觀點」，文末回看再定位「30 秒摘要」或
  「勝負手」；手機與桌機都同步移動鍵盤焦點，不只改變捲動位置。
- 移除本次新增的正式筆記／多空 `readingMission` 並把版本還原後，完整發布 payload 與 `HEAD`
  canonical SHA 逐位元相同（`8c7a80c8…`），證明文章、段落、來源、主張、推薦與既有市場議題
  任務均未被改寫。完整瀏覽器驗收 274/274 篇：273/273 張應有的任務卡與讀後檢核都精確吻合，
  29 篇單點摘要也正常呈現，0 個水平溢位或卡片裁切；320×844、390×844、884×863、1280×900
  完成視覺複核。螢幕閱讀器實機朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 469 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `0227ea45…`。

## 推薦下一篇先給可比較的閱讀問題 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、topic Markdown、文章正文、主張、證據、
graph edge、族群映射與正式學習路線零變動**；本次只補齊一般跨文章推薦的閱讀任務。

- 完整盤點 274 篇發布文章（不是抽樣）：813 張延伸卡中有 522 張 article card。21 張正式 route
  下一站原本已逐字顯示下一篇閱讀任務；其餘 501 張一般推薦雖已揭露共同公司／族群，改版前卻
  0 張告訴讀者打開下一篇時要比較什麼。這是完整母體描述，無抽樣誤差。
- `learningPathVersion` 升為 10。501 張一般推薦新增 `questionLabel: 讀下一篇時比較` 與非空
  `question`；固定句型只使用來源／目標文章類型，以及同卡既有 `relationBasis.labels[0]`，引導
  比較公司事實、題材情境、多空假說或證據邊界。多個共同標記只顯示第一個名稱與既有數量；不讀
  正文、題名或關鍵字，不使用模型生成，也不建立新的公司、供應鏈、受惠或因果結論。21 張正式
  route 卡維持原問題與「下一站試著回答」標籤。
- 移除 501 組 `question／questionLabel` 並把版本還原為 9 後，完整發布 payload 與 `HEAD`
  canonical SHA 逐位元相同（`0b076ad2…`），證明本次沒有改寫文章、證據、卡片順序或既有關係。
  完整瀏覽器母體驗收 274/274 篇、501/501 張一般推薦與 21/21 張 route 卡：問題、標籤、共同
  標記與顯示順序均吻合，0 個卡片或文件水平溢位；代表卡實際跳到正確文章並回頁首。
  320×844、390×844、884×863、1280×900 均完成視覺複核；螢幕閱讀器實機朗讀仍保留為人工
  輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 468 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `67c8e506…`。

## 推薦下一篇先說清楚兩篇為什麼相連 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、topic Markdown、文章正文、主張、證據、
graph edge、族群映射與正式學習路線零變動**；本次只公開一般跨文章推薦既有的連結依據。

- 完整盤點 274 篇發布文章（不是抽樣）：813 張延伸卡中有 522 張 article card；21 張正式 route
  下一站已用 graph／phase 解釋閱讀順序，其餘 501 張一般推薦分布在 258 篇文章。這 501 張全部
  都能由兩篇既有 `stockIds` 或 `groups` 交集精確說明，但改版前 0 張把交集顯示給讀者。這是完整
  母體描述，無抽樣誤差。
- `learningPathVersion` 升為 9。一般推薦先找共同公司，沒有時才找共同族群；326 張顯示共同公司、
  175 張顯示共同族群。卡片新增 machine-readable `relationBasis` 與「這兩篇為什麼相連」，並明示
  共同標記不代表上下游、受惠、訂單或因果關係。3 張超過三個共同族群的卡先顯示三個，可用 44px
  入口原位展開全部；正式 route 與 72 張已有關係示範的圖譜卡不重複加資訊。
- 移除 501 筆 `relationBasis` 並把版本還原為 8 後，完整發布 payload 與 `HEAD` canonical SHA
  逐位元相同（`6518ef5d…`），證明本次沒有改寫文章、證據或既有導覽。完整瀏覽器母體驗收
  274/274 篇、813/813 張卡、501/501 個理由：標題、順序、kind、ID、顯示名稱、ARIA 與收合狀態
  皆吻合，501/501 個目標文章存在；代表卡實際跳到正確文章並回頂。沒有多餘 route 理由或水平
  溢位。320×844、390×844、884×863、1280×900
  均完成視覺複核；螢幕閱讀器實機朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 468 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `53c59f09…`。

## 中文正文保留原文、改成可掃讀句群 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、topic Markdown、文章正文、主張、證據、
graph edge、族群映射與發布 payload 零變動**；本次只改善讀者顯示層的中文排版與長段落節奏。

- 完整盤點 274 篇發布文章（不是抽樣）：主正文共有 1,764 個段落、涵蓋 248 篇，中位數 129 字、
  最長 520 字；989 段原始文字達 120 字且含至少兩個中文句末。另找到 1,542 處可機械判定的中文
  換行空白，以及主正文 3,929 處可安全中文化的半形標點。這是完整母體描述，無抽樣誤差；
  120 字／兩個句末只是版面契約，不是內容品質或統計門檻。
- 顯示層只清除中文標點前後、中文開括號後與兩個漢字間的換行空白；含漢字的 run 只在不連接
  英文字母、數字、網址或時間語法時把半形 `,;:` 顯示成中文標點。英文詞列會補回必要空格，
  原始 Markdown、run 邊界、連結、粗體與發布 payload 都不回寫；本次 payload canonical SHA 與
  `HEAD` 同為 `6518ef5d…`。
- 正規化後共有 981 個長段落、涵蓋 222 篇；`≤1180px` 在既有句末加入 2,329 個零文字視覺停頓，
  寬幅仍保持連續文章排版。完整瀏覽器母體驗收 274/274 篇、1,764/1,764 段：文字、section、
  長段落 class、字數、句數與停頓數皆零錯配，中文空白、英文詞列黏連與頁面水平溢位皆為 0。
  另修正 2 篇正式筆記的長 SHA 來源名在手機證據列溢位；螢幕閱讀器實機朗讀仍保留為人工驗收。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 466 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `b7a37172…`。

## 長文正文持續顯示目前閱讀章節 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、topic Markdown、文章正文、主張、證據、
graph edge、族群映射與學習站次零變動**；本次只補窄幅文章的閱讀位置與原文大綱導覽。

- 完整盤點 274 篇發布文章（不是抽樣）：全部閱讀時間至少 5 分鐘，82 篇至少 10 分鐘；閱讀時間
  最短 5、中位數 8、最長 31 分鐘。依文章原始章名、既有延伸學習與實際查核附錄計算，每篇都有
  4–14 個可導覽停靠點，中位數 7 個；因此窄幅讀者離開開場後需要持續知道目前讀到哪一節。
- `≤1180px` 在既有新手導讀後新增黏性「閱讀位置 · 第 N/M 節」：只逐字重用文章原始章名，進度線
  代表目前停靠點，不代表研究完成度；展開後可直接跳章、延伸學習或實際存在的查核附錄，選取後
  自動收合。附錄標籤同步顯示真實節數；`>1180px` 繼續沿用既有右側大綱，不重複顯示新元件。
- 完整瀏覽器母體驗收 274/274 篇、2,465 個導覽按鈕：每篇只產生一個元件，章名、順序、索引、
  附錄節數、桌面大綱、`aria-valuemin/max/now` 與進度皆精確一致，沒有舊元件、缺漏或錯配。
  320×844、390×844、884×863 與 1280×900 均無水平溢位；章節、延伸學習與附錄跳轉都未被
  sticky 元件遮住。螢幕閱讀器實機朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 465 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `9b03d103…`。

## 文章讀完後先看兩站概念如何交接 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、topic Markdown、主張、證據、graph edge、
族群映射與站次零變動**；本次只讓既有學習路線的文章交接更容易理解。

- 對 274 篇發布文章中的 25 篇正式路線主文章做完整母體盤點（不是抽樣）：21 篇非末站原本都有
  下一篇問題與 CTA，但 0 篇會把剛讀完與下一站的 graph／phase label 並列；其中 15 次留在同一
  phase、6 次跨 phase。另 4 篇是正式末站，繼續保留完成路線狀態，不虛構下一站。
- 21 張下一站卡現在都以兩步 ordered list 顯示「這一站／下一站」，逐字重用兩篇既有
  `learningRoute.graphLabel／phaseLabel`；並明示這只是學習次序，不代表供應鏈、受惠或因果關係。
  `learningPathVersion` 升為 8；沒有用題名、相似度或模型補 label，也沒有建立 knowledge graph edge。
- 兩條獨立路徑皆驗證 21/21 個交接精確吻合、4/4 個末站無交接卡；逐篇瀏覽器 DOM 驗收沒有空白、
  重複或錯配。320×844、390×844 與 884×863 均無水平溢位；「繼續第 2/7 站」仍開啟正確文章、
  回到頁首並顯示第 2/7 站。`Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 464 tests 全綠；
  research queue、radar、method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。
  連續兩次 dashboard build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `881dc078…`。

## 閱讀任務先解釋首屏已出現的名詞 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、topic Markdown、主張、證據、族群映射與
metadata 零變動**；本次只把既有名詞解釋提前到市場議題首屏。

- 對 34 篇具有閱讀任務的一般市場議題做完整母體盤點（不是抽樣）：32 篇的「先抓住這一句／
  讀完能回答」可確定性命中既有解釋，共 91 組文章－名詞（86 組同篇字典、5 組研究中心共通語），
  每篇最多 5 個。另 2 篇沒有安全命中，發布頁不顯示空入口，也不以模型或新文案補詞。
- 閱讀任務新增預設收合的「先認得這兩句的 N 個詞」，本文字典優先，再只用既有共通語補研究
  流程／常見指標；兩句重複詞合併一次。展開列與原本逐句重點共用同一個 definition renderer，
  逐字保留來源標籤、定義與判讀邊界；完整字典、下方逐句提示與「為什麼值得讀」仍保留。
- 瀏覽器逐篇 DOM 驗收 34/34：32 個非空入口、91 列、2 篇無入口，資料屬性與實際列數全數一致。
  320×844、390×844 與 884×863 都沒有水平溢位；原生 `details` 可展開／收合且不改文章 hash，
  「開始讀三句重點」仍把鍵盤焦點送到原標題。`Darwin 25.5.0 arm64`、Python 3.11.11 預設環境
  執行 464 tests 全綠；research queue、radar、method audit、knowledge graph lint 均為 0 errors
  （queue 保留 8 warnings）。連續兩次 dashboard build SHA 一致：`index.html` `1e3a48ae…`、
  `research.html` `2c22a00c…`。

## 市場議題先用中文問題開場，再保留研究題名 — 2026-08-10

**策略權重、tier 條件、regime 門檻、`IS_CUTOFF`、topic 原文、主張、證據與 metadata
零變動**；本次只調整 35 篇發布中市場議題的讀者入口。

- 完整盤點 35 篇發布內容（34 篇一般市場議題與 1 篇事件錨點）：34 篇一般文章都有既有閱讀
  問題，但其中 15 篇的英文術語數不比原技術標題少；34 個標題合計 78 個英文術語、既有問題
  仍有 64 個。新增 `config/research_topic_guide.csv`，逐篇人工撰寫 35 個不含英文字母的中文
  問題，讓讀者先知道本文要解開什麼，不以自動刪詞假裝白話化。
- 市場議題清單卡與文章 `h1` 現在先顯示「這篇先回答／這篇先弄懂」和中文問題；原技術標題完整
  保留為次要「研究題名」，研究範圍也留在卡片。既有閱讀任務、三句重點、文章正文、查核附錄、
  搜尋範圍與深連結均沿用，只有中文問題另加入搜尋索引。
- 建置採 fail-closed 契約：導覽問題須為 18–56 字、以全形問號結尾且不含英文字母或反引號，並
  與所有發布中的 `type=topic` 文章精確一對一覆蓋；缺漏、重複或多出未發布 ID 都停止建置。
- 瀏覽器驗收 320×844、390×844 與 884×863：市場議題清單與代表文章水平溢出皆為 0；原技術
  標題在手機套用 12px 小字下限，仍可讀但不與中文問題搶層級。`Darwin 25.5.0 arm64`、Python
  3.11.11 預設環境執行 464 tests 全綠；research queue、radar、method audit、knowledge graph
  lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48ae…`、`research.html` `e0204f55…`。

## 研究雷達先說想弄懂的問題，再補技術題名 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只調整研究雷達與
族群矩陣的讀者入口，不修改 topic／candidate 原文、研究主張、證據、族群映射、研究排序或
投資判斷。

- 完整盤點 8 個發布中的研究雷達候選：8/8 都已有 `reader_question`、`reader_next_step` 與
  `reader_terms`，但舊版仍先把技術題名當主標。8 個技術題名合計含 30 個英文術語，白話問題
  合計只含 5 個；現在卡片標題先顯示「這題想弄清楚」與既有白話問題，原技術題名完整保留為
  次要資訊，再接「接著查什麼」、關鍵詞、族群閱讀問題與原生研究判定明細。
- 族群矩陣把「各族群研究完整度／先選一個系統問題」的行政語氣改成「先從一個想弄懂的問題
  開始」，手機入口同步改為「從問題開始」；4/4 條路線既有問題與 11/11 族群的角色／邊界
  全數沿用，族群重複出現仍明示不代表重要性或投資排名。
- 市場議題本輪保留原標題：35 篇發布內容中 33 篇標題含英文術語；34 篇既有閱讀問題雖可用，
  但合計仍有 64 個英文術語，尚不足以安全取代原標題。下一輪應先改寫並逐篇複核閱讀問題，
  不以自動刪詞假裝白話化。
- 瀏覽器驗收 320×844、390×844 與 884×863：研究雷達與族群矩陣水平溢出皆為 0；研究判定
  `details` 仍可展開。`Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 463 tests 全綠；
  research queue、radar、method audit、knowledge graph lint 均為 0 errors（queue 保留 8
  warnings）。連續兩次 dashboard build SHA 一致：`index.html` `1e3a48ae…`、`research.html`
  `6194b980…`。

## 文章先進入三句重點，角色與路線緊接在後 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只調整研究文章的讀者順序與
漸進揭露，不修改 topic 原文、主張、證據、學習路線、族群映射或投資排序。

- 代表文章原本在 390×844 手機中，要到頁面 1,903px 才開始「三句話抓重點」；前面連續堆疊
  學習起點、查核警語、閱讀任務、族群角色、metadata 與路線定位。現在手機沿用黏性返回鈕、
  隱藏重複的整張起點卡，並把完整三句重點移到閱讀任務後，起點提前至 913px，早 990px。
- 閱讀任務不再用一段充滿縮寫的「為什麼重要」先轟炸新手；正面逐字重用同篇第一句重點與
  第一個「想一想」，標成「先抓住這一句／讀完能回答」。原「為什麼重要」開場完整保留在
  44px 原生收合說明，需要脈絡時才展開；主按鈕仍把焦點送到同篇「三句話抓重點」。
- 「新手先讀」拆成前後兩張讀者卡：前張只放完整三句重點，卡片結束後 12px 就進本文族群角色，
  再接所在學習階段；後張以「再補重要性、名詞與追蹤」接回原本的重要性、字典、追蹤與想一想。
  390×844 代表文章的角色區由頁面 y=2,552 提前至 y=1,637，早 915px；884×863 桌機則由
  y=2,344 提前至 y=1,565，早 779px。metadata 改放在角色與路線後；研究文字、runs、名詞字典、
  角色邊界、路線站次與大綱索引均保留。320px、390px 與 884px 實測水平溢出均為 0。
- 273 篇具有正式族群指南的文章中，241 篇只有一個角色；28 篇有 2–4 個角色，現在直接以語意清單
  與獨立 heading 同時顯示全部卡片，兩角色文章從切換 1 次降為 0 次。其餘 4 篇超過四個角色，
  先保留一張起點卡，其餘一次展開全部；十一角色事件錨點從「展開後最多再切 10 次」降為只展開
  1 次。卡片只重用既有 `readerRole`／`readerBoundary`，並持續明示並列不代表上下游、受惠或排序。
- 發布 payload 獨立解析得到 35 篇市場議題，其中 34/34 篇既有閱讀任務都同時保有第一句重點、
  orientation 與第一個問題；事件錨點未憑空補任務。`Darwin 25.5.0 arm64`、Python 3.11.11
  預設環境執行 463 tests 全綠；research queue、radar、method audit、knowledge graph lint 均為
  0 errors（queue 保留 8 warnings）。連續兩次 dashboard build SHA 一致：`index.html`
  `1e3a48ae…`、`research.html` `a5ea2bcd…`。

## 族群矩陣讓新手先從系統問題開始 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只調整族群矩陣的行動版
入口順序，不修改 topic 原文、學習路線、族群映射、證據關係或投資排序。

- 原本 390×844 手機首屏先放 11 個族群名稱，「先選一個系統問題」頂端位於頁面 942px，
  不熟產業分類的讀者得先穿過一整個術語選擇器。現在手機新增雙入口並預設系統問題，問題區
  頂端提前到 392px，早 550px 進入同一個首屏；11 個正式族群完整保留在另一個入口。
- 入口使用原生按鈕與 `aria-pressed`，可在「從系統問題開始／依族群名稱查找」間切換；
  從族群預覽點既有系統問題會自動切回並定位正確路線。桌機仍同時顯示兩區，桌機／手機
  resize 不會遺失本次選擇，390px 與 884px 實測水平溢出均為 0。
- 這次沒有新增文章、族群或學習路線，也沒有用文字相似度建立關係；發布集合仍維持
  4 路線／10 階段／25 站與 11 個正式族群。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 463 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `a70adf52…`。

## 學習路線只先展開目前階段 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只調整既有學習階段的
漸進揭露，不修改 topic 原文、文章問題、route／graph 站次、證據關係或投資排序。

- 上一版雖把 9 站路線分成 3 個可辨識階段，390px 手機展開後仍高 1,019px，所有 9 個問題
  同時出現。多階段路線現在使用巢狀原生 `details／summary`：文章只預先打開目前所在階段，
  族群矩陣只預先打開第一階段，其餘摘要直接保留 phase 名稱、站數與站次範圍。
- 代表文章在同一 390×844 狀態的路線高度降至 545px（縮短 474px，約 47%）；320×844 為
  651px、1440×900 為 471px，三個尺寸的水平溢出皆為 0。9 個原站點、逐站「想一想」問題、
  閱讀時間與 `aria-current="step"` 全數保留，沒有把內容截短來換高度。
- 每個 phase 摘要至少 44px，可用滑鼠、Enter 或 Space 切換；resize 不會重新打開已收合階段。
  使用者可同時展開多個階段，系統不保存或推測閱讀進度。螢幕閱讀器實機朗讀仍保留為人工輔具
  驗收項目。
- source registry 與發布 `research.html` 兩條獨立解析路徑仍為 4 路線／10 階段／25 站；
  25/25 篇主文章保有路線定位，21 張跨文章下一站卡與 4 張末站完成卡未變。
  `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 463 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `046acdd3…`。

## 學習路線從平面站點拆成可辨識的系統階段 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只補研究中心的閱讀章節與
跨介面定位，不修改 topic 原文、文章問題、graph 站次、節點／關係、公司映射或投資排序。

- 代表「供電與散熱」路線原有 9 個站點與逐站問題，但手機展開後是一張 892px 高的平面清單；
  現行總述還略過機櫃控制、EMC 與信任鏈三站，讀者知道下一篇是哪篇，卻不容易看出整條路線
  正在建立哪一層系統理解。
- `RESEARCH_LEARNING_ROUTES` 新增明示 `phases`：4 條路線共 10 個階段、25 個原有站點；每個
  phase 必須以唯一 id／白話 label，把 route `graphIds` 依原順序逐站且恰好覆蓋一次，遺漏、
  重複或換序會直接讓建置失敗。階段是閱讀章節，不新增上下游、供應鏈或受惠方向。
- 文章頁首、可展開路線地圖、族群起點與下一站卡共用同一份 phase；目前文章同時標示站次與
  階段，下一站明說是留在原階段或進入下一階段。從文章進入知識圖譜後，「目前位置」仍保留
  同一階段，行動版原生主題選單以 `optgroup` 分組；payload 升為 `learningPathVersion: 7`。
- source registry 與發布 `research.html` 兩條獨立解析路徑均得到 4 路線／10 階段／25 站；
  25/25 篇主文章 phase 與 station 完全一致，21 張下一站卡全數指向下一站的正式 phase，
  0 failures。這是完整發布集合，不是抽樣。
- 瀏覽器驗收 320×844、390×844 與 1440×900：全頁水平溢出皆為 0；目前階段、跨階段標題、
  下一站 phase 與圖譜 `optgroup` 均可回查。DOM 保留巢狀有序清單、`aria-current="step"`、
  原生 `details／select／optgroup`；螢幕閱讀器實機朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 463 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `fe6ab763…`。

## 研究摘要把主張類型與證據可信度拆成兩把尺 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只新增市場議題的證據
閱讀輔助，不修改 topic 原文、主張 label、可信度、來源、圖譜關係、公司映射或投資排序。

- 現行摘要把「主結論標記為推論」與「證據可信度為中」放在同一句，手機首屏沒有立即解釋兩者
  差異。34 篇結構化 topic 中，33 篇主命題為 `inference`、1 篇為 `verified`；若讀者把
  claim label 當成有無證據，或把高／中／低當成發生機率，會系統性誤讀多數市場議題。
- 研究摘要導言後新增「先分清兩把尺」：主張類型逐篇沿用 active `thesis_claim_id` 的正式
  `verified／inference／unverified`，說明結論是由來源直接支持、由已接受資料連接而成或仍待
  驗證；證據可信度則明示只衡量來源品質、獨立消息鏈、反方證據與主要缺口，不是真假或機率。
- 畫面只計 active thesis 實際引用的 active supporting sources 與其 `independence_group`，並
  明示兩把尺都不能換算成公司訂單、受惠程度或投資排名。前端沿用 `liveConfidence(article)`；
  到期文章實測會由「中」同步顯示成「中 → 低（已到期）」，且說明降級不代表主張被推翻。
- source-loader 與發布 `research.html` 兩條獨立解析路徑均得到 34 篇／34 組導讀，claim 分布
  33 推論＋1 證實、effective confidence 分布 26 中＋7 低＋1 高；主張、可信度、來源數與獨立
  鏈數逐篇比對均為 0 failures。這是完整發布集合，不是抽樣。
- 瀏覽器驗收 320×844、390×844 與 1440×900：全頁水平溢出皆為 0；手機兩把尺改為單欄，
  320px 導讀卡仍完整落在 viewport 內，桌機維持雙欄。DOM 保留 complementary、heading、list
  與 `data-claim-key／data-confidence-key`；螢幕閱讀器實機朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 462 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings），JavaScript 語法檢查
  通過。連續兩次 dashboard build SHA 一致：`index.html` `1e3a48ae…`、`research.html`
  `cbef5f95…`。

## 文章到知識圖譜的同視角關係導讀 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只校正文章與既有知識圖譜
之間的閱讀交接，不修改研究主張、證據、圖譜節點／關係、公司曝險、財務歸因或投資排序。

- 代表文章原本在交接卡顯示整張圖譜 13 個節點／12 條關係，但點入後預設開啟的「公司曝險」
  實際只有 4 個節點／3 條關係，容易讓新手誤以為內容遺失。現在卡片先選定即將開啟的視角，
  並只計算該視角真正存在的節點與關係；若沒有公司關係才明確退回產業關聯視角。
- 每張交接卡新增一條既有關係示範，逐字重用圖譜登錄的起點、終點、關係、證據、商業階段與
  推論邊界；CTA 同時保留視角與該 edge，開圖後直接選中同一條關係。這不是重要性、受惠程度
  或投資排序，也不由題名、公司或相似度補造關係。
- source-loader 重建與發布 `research.html` 兩條獨立解析路徑均盤點 274 篇文章、72 張圖譜交接卡；
  每張卡的視角、節點數、關係數與導讀 edge 皆和實際圖譜一致，兩路結果完全相同、0 個失敗。
- 瀏覽器驗收 320×844、390×844 與 1440×900：全頁水平溢出皆為 0；手機邊界 summary 與 CTA
  均至少 44px。代表文章卡片顯示「公司曝險 · 4 個節點 · 3 條關係」，點入後仍為同一視角、
  同一組數量並選中 `KG-ACR-C01`。螢幕閱讀器實機朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 461 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings），JavaScript 語法檢查
  通過。連續兩次 dashboard build SHA 一致：`index.html` `1e3a48ae…`、`research.html`
  `a2dc17a1…`。

## 研究中心共通語與內部族群名稱中文化 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只補閱讀層的中文詞解與
顯示名稱，不修改原始研究文章、主張、證據層級、族群關係、機器欄位或投資排序。

- 完整盤點 35 篇市場議題、102 句三句重點：同篇字典原有 161 筆命中、涵蓋 77 句；新增的
  10 筆受治理共通語實際補上 18 筆命中、涵蓋 14 句，合計讓 81 句至少有一筆就地詞解。
  source-loader 重建與發布 `research.html` JSON 兩條獨立解析路徑結果完全一致；本輪不是抽樣。
- 新增 `config/research_reader_terms.csv`，只收 BOM、qualification、production、TAM、ASP 等
  可跨文章維持相同字面邊界的研究流程與常見指標。每筆均有明示 alias、中文 label、definition
  與 boundary；同篇字典永遠優先，畫面也逐筆標示「本文名詞」或「研究中心共通語」，不使用
  模型、相似度或自動擴詞。實測 HVM 仍取本文 `HVM insertion` 定義，只有 qualification 由
  共通語補上。
- 發布建置另只在可見 heading／run 中，把 `passive`、`powersupply`、`serverodm` 等明確白名單
  內部族群 ID 換成正式中文名稱；URL、來源檔、`group_id(s)` 與原始 topic 帳本不動，`power`、
  `memory`、`material` 等可能出現在正常技術英文中的字串也不自動替換。
- 瀏覽器驗收 390×844、320×844 與 1440×900：全頁水平溢出皆為 0，手機原生 `summary`
  高 46.4px；390px 展開後可讀到 BOM 定義、判讀邊界與共通語來源標籤，1440px 同一句正確顯示
  4 筆本文名詞＋1 筆共通語。螢幕閱讀器實機朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 460 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `82e1f58d…`。

## 市場議題三句重點就地解釋專有名詞 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只重排既有新手重點並
就地重用同篇字典，不修改文章文字、主張、證據層級、族群關係或投資排序。

- 目前 35 篇市場議題中，34 篇有「三句話抓重點」，共 102 句；83 句含兩個字母以上的英文詞，
  77 句能命中同篇字典，共可就地帶回 161 筆既有詞解。完整 source-loader 重建與發布 HTML
  兩條獨立解析路徑得到相同文章與重點總數；先前單向逐 block 掃描因一篇文章的字典排在重點
  後方而少算 1 句／1 詞解，現改為先依 heading 分組再比對。
- 「三句話抓重點」改成保有 `<ol>` 語意的逐句卡片；原始 runs、順序、粗體與連結不變。每句只
  比對同篇名詞小字典，命中時按名詞在原句第一次出現的位置列出，原生 `details` 展開後逐字
  顯示原定義；沒有命中時不顯示空提示，也不靠相似度、模型或第二份詞表補解釋。
- 390×844 實際流程中，三句原文與 payload 逐字相同；第一句依原句順序列出 Rack、CBU、EDLC、
  DC link，展開後焦點留在 `summary`，四筆定義皆來自同篇字典。320px／390px／1440px 均無
  水平溢出，手機 summary 最小實測 46.4px。螢幕閱讀器實機朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 458 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `95fe3e36…`。

## 文章閱讀任務直接進入三句重點 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只替既有新手摘要補上
明確閱讀入口，不修改文章主張、文字內容、證據層級、族群角色、圖譜關係或投資排序。

- 390×844 的市場議題深連結原本從標題到「三句話抓重點」需捲動約 1,300px，途中依序經過
  閱讀任務、產業角色、metadata 與路線提示，但閱讀任務本身沒有正文出口。卡片現在新增
  「開始讀三句重點」，並保留「想先比較族群角色」的向下提示，讓兩種閱讀意圖在同一處分流。
- 首屏按鈕與正文後「回看本篇三句重點」共用 `focusBeginnerHighlights()`：只尋找同篇既有
  heading、同步移動鍵盤焦點與捲動位置，不改變文章 hash，也不新增第二份摘要。若目標不存在則
  保持原位，不從其他段落猜測替代內容。
- 瀏覽器實測同一篇文章：390px 點擊一次後焦點落在「三句話抓重點」，heading 位於 viewport
  `y=119.9px`；320px／390px 按鈕皆高 44px且全頁水平溢出為 0。1440px 桌機按鈕高 36px，
  heading 位於 reader 頂端下方 `76.0px`。螢幕閱讀器的實機朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 458 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `7821eea6…`。

## 文章前段先分清產業角色 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只把正式族群白話指南帶到
文章前段，不修改文章主張、圖譜關係、公司曝險、財務歸因、上下游判斷或投資排序。

- 直接分享連結進入市場議題時，頁首雖已有閱讀問題，卻只顯示族群名稱；讀者要到後段技術表格
  才能逐一卡片推回「被動元件」與「電源供應」各自負責哪一層。文章閱讀任務後新增「再把產業
  角色分開」，逐字重用 `groupMaturity.rows` 的 `readerRole` 與 `readerBoundary`，先分工再讀名詞。
- 選項只取本文正式 `groups` 並保留原順序；由族群矩陣開文時優先顯示原族群，其餘入口顯示本文
  第一個族群。多族群用唯一 `aria-pressed` 按鈕與 `aria-live` 預覽切換；超過四個族群時預設收合
  完整選項，避免十一族群事件文在手機首段鋪滿按鈕。沒有正式族群的政策文章保持不顯示，不靠
  題名、公司或相似度補關係。
- 建置 JSON 與瀏覽器內獨立解析一致：274 篇中 273 篇有正式族群，共 346 個族群引用，0 個缺
  白話角色或混淆邊界；4 篇超過四族群，最大 11 個。瀏覽器另實際驗收兩族群切換、十一族群
  展開與末項切換、族群起點預選、無族群不顯示；320px／390px／1280px 均無水平溢出，手機
  選項最小高 44px。螢幕閱讀器對 `aria-live` 的實機朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 458 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `5e285a6c…`。

## 研究文章保留族群／系統問題學習起點 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只補齊族群矩陣與文章之間的
讀者導覽狀態，不修改文章主張、圖譜關係、公司曝險、財務歸因、上下游判斷或投資排序。

- 390×844 實際流程中，從「被動元件 → 第一篇」進入文章後只剩「返回研究清單」；讀完返回會
  落在 274 篇一般文章清單中段，讀者失去剛選的族群與系統問題脈絡。文章現在以暫存狀態保留
  `maturity-group` 或 `maturity-route` 起點，跨到下一站仍沿用；一般清單、圖譜、雷達與直接文章
  深連結都會清除，不從文章標籤猜測來源。
- 文章頁首新增精簡的「本次學習起點」，「從這篇接著學」末端也提供同一返回動作；族群起點顯示
  既有收錄路線並明示不是上下游或受惠排序，系統問題起點則沿用既有族群／站數。返回後會重選並
  聚焦原族群按鈕或原路線卡，而不是把讀者送回通用清單。
- 瀏覽器逐一驗收族群入口、系統問題入口、下一站延續、兩種精準返回及直接深連結無虛構起點。
  320×844 下全頁與起點列水平溢出皆為 0，三個行動控制項高度皆為 44px；另完成 390×844、
  1280×720 視覺複核與改版前後對照。螢幕閱讀器實機朗讀仍保留為人工輔具驗收項目。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 458 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `ccf7fbf7…`。

## 族群矩陣新手族群入口 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只把既有族群白話指南、
學習路線與起讀文章組成更早出現的讀者入口，不修改文章主張、圖譜關係、公司曝險、財務歸因、
上下游判斷或投資排序。

- 原頁首說明有族群與系統問題兩種入口，但桌機及 390×844 行動版首屏都只有四張系統問題卡；
  11 個族群的角色與混淆邊界要跨過路線卡及完成度數字後才看得到。矩陣頂端新增「先認識一個
  族群」，直接列出 11 個正式族群，選取後即時顯示既有 `readerRole`、`readerBoundary`、所在
  學習路線、第一篇與完整進度入口。
- 「會出現在」只反查 `RESEARCH_LEARNING_ROUTES` 已保存的 `groupIds`，並在畫面明示不是
  上下游、重要性或受惠排序；路線按鈕聚焦既有系統問題卡，完整進度按鈕聚焦同一族群列，第一篇
  按鈕則開啟既有 `learningStart`，沒有另造文章或關係。
- 瀏覽器逐一操作 11／11 個族群，白話角色、混淆邊界與所屬路線皆非空，且 `aria-pressed`
  始終只有一個選項。320×844 下新控制項最小高 44px，explorer 與全頁水平溢出皆為 0；另完成
  390×844、1280×720 視覺複核，以及「伺服器組裝／機構 → 第一篇」、路線聚焦、完整列聚焦流程。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 458 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `097e6eec…`。

## 族群矩陣白話角色與混淆邊界 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只替正式族群補上
讀者導覽用的角色說明與混淆邊界，不修改 `groups.csv`、universe、文章主張、圖譜關係、
公司曝險、財務歸因或投資判斷。

- 原矩陣從「被動元件／封測／矽智財」等族群名稱直接跳到進階起讀文章；不熟產業的讀者在
  閱讀文章前，無法先建立該族群負責哪一層工作、又不該和哪一個相鄰角色混為一談。
- 新增 `config/research_group_guide.csv`，逐一覆蓋 `config/groups.csv` 的 11 個正式族群；每列
  只保存一個白話角色與一個「先別混淆」邊界。建置器會拒絕缺族群、多餘族群、重複值、空句、
  欄位錯誤或未以句號收尾，避免介面靜默退回不完整說明。
- 族群矩陣先顯示「研究中心怎麼分」，再接既有研究雷達問句、起讀文章、完成度與下一步。
  這份指南是讀者分類層，不會建立上下游順序、公司認證、受惠方向或新的研究證據。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 458 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `ae296bc8…`。

## 研究雷達族群分工問句與矩陣脈絡延續 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只把候選已寫明的知識
缺口、責任角色與驗證動作縮成讀者問句，不修改 rank、priority、selection log、evidence
posture、文章主張、graph edge、公司曝險、財務歸因或投資判斷。

- 原雷達已能把 8 張候選卡連到 18 個正式族群，但桌機與手機都只顯示族群名稱；新手無法從
  「被動元件／電源供應／伺服器組裝」理解各自要處理零件抑制、子系統除錯或整櫃驗收哪一層
  問題，進入矩陣後也只剩「從研究雷達定位」，原研究問題沒有跟著移動。
- Active radar 新增必填 `reader_group_questions`：必須依 `group_ids` 順序逐一提供白話問句，
  parser 擋缺項、錯序、重複族群與非問句。現行 8／8 候選共 18／18 條路由都有問句；卡片以
  完整問題按鈕取代單字籤，並明示這是在拆分研究責任，不代表上下游順序、受惠或已證實公司
  連結。
- 點任一族群後，矩陣目標列保留「這個族群要回答」與同一問句，再接既有起讀文章、完成度、
  缺口與下一步；返回原候選仍恢復同一卡片焦點。首題被動元件與末題散熱兩端流程都實際往返，
  後者另以鍵盤聚焦確認按鈕可達；完整鍵盤啟動與螢幕閱讀器朗讀仍留待人工輔具驗收。
- Python parser 與瀏覽器 DOM 兩條獨立路徑都重算出 8 張卡、8 個關聯區、18 個問句按鈕，0 個
  缺問句、錯序、空問句或無問句可及名稱。320×844 下 18 個按鈕最小高 `70.594px`，按鈕、
  卡片與全頁水平溢出皆為 0；390×844 與 1280×720 版面亦完成視覺檢查。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 457 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `1333caea…`。

## 研究雷達連回正式族群與雙向定位 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只替候選雷達補上由
既有候選責任範圍宣告的正式族群導覽，不修改 rank、priority、selection log、evidence posture、
文章主張、graph edge、公司曝險、財務歸因或投資判斷。

- 原雷達 8 張候選卡都能說明白話問題、名詞與下一個證據，但 8／8 都沒有顯示題目會使用哪些
  正式族群資料；只有 2 張已升格卡另有文章／圖譜動作，6 張 watch／deferred 卡讀完後沒有可
  繼續建立產業位置的讀者路由。
- Active radar 新增必填 `group_ids`：每題只能宣告 1–4 個 `config/groups.csv` 既有族群，parser
  擋未知、重複與超量值。現行 8 題共 18 個族群路由；每張卡正面以「這題會碰到哪些族群」顯示，
  並明示這只是研究資料路由，不代表族群、公司或題材已被證實受惠。
- 點族群會直接開啟族群矩陣並聚焦同一族群的起讀文章、已完成、最大缺口與下一步；目標列顯示
  「從研究雷達定位」與「返回原候選」，返回後原候選卡取得焦點且標題讓開 sticky header。
  兩個方向都使用可辨識的按鈕名稱，並保留鍵盤焦點與原候選脈絡。
- 建置 JSON 獨立解析確認 8／8 候選都有路由、18 個值全屬正式族群，0 個缺值、未知值、重複值；
  2 張已升格候選的宣告族群與對應文章完全一致。瀏覽器第二條路徑確認 8／8 張卡渲染 18 個按鈕；
  320px 時按鈕最小高 44px，卡片與全頁水平溢出皆為 0，首題與末題都能往返矩陣並把焦點送回。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 457 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `c3cc2dd9…`。

## 市場議題窄欄表格完整閱讀與返回定位 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只重排既有文章 table 的
窄欄顯示與清單返回定位，不修改 Markdown、table 欄名／cell、研究主張、來源、graph edge、
公司映射、財務歸因或投資判斷。

- 390×844 代表文章的三欄功能表原本水平溢出 `248px`，首屏只見「電力鏈位置」與元件路徑，
  最右側「成熟度邊界」必須橫向捲動才看得到；1280px 桌機 master-detail 的實際正文欄也只有
  `365px`，所以單看 viewport 斷點仍會漏掉同一欄。
- 市場議題一般正文表為每個 `th` 補上 `scope="col"`，每個 cell 的窄欄標籤逐字取自同欄表頭；
  article section 容器不足 `620px` 時按 row 改排成卡片，365px master-detail 與 320／390px 手機
  都直接看得到全部欄位。836px 專注閱讀自動回復原生 table；查核附錄不套卡片，只有實際溢出
  時才加可聚焦 region 與水平捲動提示。
- 建置 JSON 的獨立解析與瀏覽器逐篇渲染兩條路徑重算一致：35 篇市場議題中 25 篇共有 27 張
  一般正文表、436 個 cell；0 個空表頭、0 個無表頭對位 cell。320×844 全文枚舉時 436／436
  個 cell 都有原欄名，27／27 張表與 35／35 篇頁面水平溢出皆為 0，窄欄 wrapper 也沒有留下
  多餘 `tabindex`／region。
- 修正返回清單時沿用 `article-open` render 結果、使「第一次來」導覽維持 hidden 的狀態錯誤。
  由清單開文會保存 window／catalog 捲動位置，返回後聚焦同一文章卡；由深連結或其他表面開文
  則把對應卡捲入可視區後聚焦。兩條流程均實際驗收 hash 清除、導覽重現與焦點可見。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 457 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings）。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `cfa851fe…`。

## 正文段落原字典詞直達 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只把同篇「名詞小字典」
帶到實際使用術語的正文節，不修改 Markdown、研究摘要、主張、來源、graph edge、公司映射、
財務歸因或投資判斷。

- 390×844 代表流程顯示：第一個專業正文節直接進入含 SST、BBU、IBC、PSU、SiC／GaN 等詞的
  表格；原字典已相隔多個螢幕，浮動「名詞速查」也未提示本節應先查哪些詞。
- 一般正文節新增「本節先認得」：以確定性字串比對同節 heading、段落、清單、表頭與表格列，
  只列同篇字典粗體詞名。詞鈕開啟既有原生 dialog 並預填完整詞名，解釋仍逐字取自同一份 list
  runs；新手段落、研究摘要、研究查核附錄與零命中節不插入，不使用模型或相似度補詞。
- 代表 800VDC 功能節命中 6 個詞；手機卡高 `188.5px`，6 個詞鈕皆為 `44px`，水平溢出為 0。
  實際點擊 SST 後搜尋欄取得焦點、只顯示原字典 1／8 筆，直接指標點擊前後 window scroll 都是
  `3401.5px`；關閉後焦點回到 SST 詞鈕。最高密度案例「分層不是替代排行榜」命中 9 個詞、卡高
  `238.5px`，仍無溢出；1280×720 桌機代表卡高 `152.672px`。
- 完整 registry 枚舉由建置 JSON 獨立解析與瀏覽器逐篇渲染兩條路徑重算一致：25 篇 route 主文章
  中 24 篇共有 57 個命中節、246 個詞鈕；公司財務案例只有摘要與查核區，依契約不插入正文詞鈕。
  246／246 個詞鈕都可回查同篇字典，0 個未知詞、0 個空卡、25／25 篇水平溢出為 0。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 456 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留 8 warnings），連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `faa91891…`。

## 學習路線全站地圖與文章定位 — 2026-08-10

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只把既有學習路線、圖譜
主文章與同篇閱讀任務重排成可展開的路線地圖，不修改研究主張、來源、graph edge、公司映射、
財務歸因或投資判斷。

- 原文章頁的「查看完整路線」實際只開啟當站圖譜，手機圖譜控制又預設收合；讀者離開文章後
  仍看不到整條閱讀順序。族群矩陣也只提供第一站入口，無法先比較後續問題或跳到指定站。
- 矩陣四張系統問題卡與文章站次定位新增原生 `details` 路線地圖；每站逐字重用 route
  `graphIds`、各 graph 第一篇既有 `articleIds` 與同篇 `readingMission.question`，並顯示閱讀
  時間。文章目前站使用 `aria-current="step"`，任一站可直接開文並回到頁首；單站圖譜動作改為
  誠實的「看這站證據關係」。輸出契約升為 `learningPathVersion: 5`。
- 完整枚舉建置 payload 與瀏覽器 DOM：4 條路線共 25／25 站都有既有文章與問題，0 個停用站點、
  0 個水平溢出。實際從供電與散熱第 1 站展開 9 站、跳到第 2 站並確認目前站標記，再開啟同站
  800VDC 保護圖譜；站次、文章與圖譜 deep link 皆一致。
- 390×844 同狀態中，第一張路線卡由 `224.414px` 增為 `284.586px`，收合地圖高
  `51.172px`，起讀按鈕仍在首屏 `y=633.875–677.875px`。1280×720 展開第一條 9 站路線時，
  只有該卡增高至 `1288.188px`，其他卡維持 `272.945–297.641px`；深淺色與兩種寬度皆無溢出。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 455 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 依 2026-08-10 時點保留 8 warnings），
  `git diff --check`、衝突標記與 `CLAUDE.md`／`AGENTS.md` 同步檢查通過。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `6f180fda…`。

## 知識圖譜手機入口漸進展開 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只重排知識圖譜既有導讀與
控制區，不修改 learning route、graph registry、edge、claim、source、evidence state、公司映射、
財務歸因或投資判斷。

- 390×844 同狀態基準中，四步導讀、四條路線、主題、視角與證據控制合計高 `630.023px`；主題
  標題到 `y=782.023px` 才開始，關係示範按鈕則在 `y=1004.820px`，第一次進入看不到真正內容。
- 「新手讀圖」與完整控制分成兩個原生 `details`。markup 預設展開以保留無 JavaScript fallback；
  手機只在載入時收起一次，之後不以 resize 覆寫使用者狀態；桌機仍預設完整展開。第二個摘要
  直接顯示目前路線、主題、視角、證據層級與台股範圍，切換路線／視角／證據時同步更新。
- 同一 390×844 深連結中，收合後控制區高 `168.188px`，主題標題提前到 `y=320.188px`；「先讀
  主題文章」與「示範讀一條證實關係」分別位於 `y=491.984–535.984px`、`542.984–586.984px`，
  都進入首屏且水平溢出為 0。展開後四個路線按鈕、主題選擇、兩個視角與四個證據控制皆維持
  至少 `44px` 觸控高度；深淺色手機與 1280×720 桌機畫面均完成檢視。
- 實際互動驗收確認：四步導讀與完整控制可獨立展開；取消「推論」後摘要變為「證實＋待驗證」；
  切到產業依賴會同步更新標題、摘要與 deep link，並停用只看台股；切換到記憶體與封裝後摘要
  顯示「記憶體與封裝 · AI 記憶體分層」，控制區保持展開。瀏覽器 console 為 0 筆訊息。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 455 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留既有 6 warnings），`git diff --check`、
  衝突標記與 `CLAUDE.md`／`AGENTS.md` 同步檢查通過。連續兩次 dashboard build SHA 一致：
  `index.html` `1e3a48ae…`、`research.html` `534699f5…`。

## 知識圖譜關係白話解讀與示範入口 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只重排既有知識圖譜 edge
欄位與延伸入口，不修改 graph registry、endpoint、relation、claim、source、evidence state、
commercial stage、materiality、boundary、next trigger、公司映射、財務歸因或投資判斷。

- 1280×720 與 390×844 同狀態基準顯示：關係列原本把「揭露技術能力 · 推論 · 能力／研發」
  等不同維度排成未命名狀態串；點選後詳情直接進入「證據邊界」等研究術語，讀者沒有先得到
  「現在能說什麼、不能推到哪裡、接下來等什麼」的閱讀框架。
- 每個目前篩選後仍有 edge 的圖譜新增一個關係示範；固定先取未到期 verified、再取 verified、
  最後才取第一條可見 edge，並明示只教讀法，不代表重要性、受惠或投資排序。關係列改為直接
  標出「關係／證據／階段」，詳情 badges 另標出「商業位置」。
- 關係詳情新增「用三步讀這條線」：第一步只組合 endpoints、relation、evidence、materiality
  與 commercial stage；第二、三步逐字顯示同一 edge 的 `boundary`、`nextTrigger`。卡片下方的
  「讀完整研究脈絡」只解析該 edge 既有 `articleIds`，不另寫摘要或建立文章／公司關係。
- 示範操作會把鍵盤焦點送到 `aria-live` 關係詳情，並遵守 reduced-motion；390×844 實機定位
  的詳情頂端為 `y≈74px`，避開黏性頁首，三步與文章按鈕同屏可見。按鈕實際開啟既有 800VDC
  主文章、回到 `scrollY=0`，並保留「供電與散熱 · 第 1/9 站」。桌機仍維持圖與詳情並排。
- `Darwin arm64`、Python 3.11.11 預設環境執行 454 tests 全綠；research queue、radar、method
  audit、knowledge graph lint 均為 0 errors（queue 保留既有 6 warnings），inline JavaScript、
  `git diff --check`、衝突標記與 `CLAUDE.md`／`AGENTS.md` 同步檢查通過。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `4b896e5d…`。

## 文章讀後理解檢查與下一站交接 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只把同篇新手段落與既有
學習路線重排成讀後交接，不修改研究來源、主張、三句重點、想一想、證據層級、圖譜 edge、
公司映射、財務歸因或投資判斷。

- 390×844 同狀態基準顯示：正文後只有「下一篇／看關係／看同族群」三個平行出口；讀者可選
  去向，卻沒有先確認本篇應帶走的因果問題，也看不到下一站將補哪個問題。
- 「從這篇接著學」先加入讀完檢查，逐字重問首屏「想一想」；三句提示使用原生 `details`
  預設收合，展開後逐字呈現同篇「三句話抓重點」，並明示沒有新增或改寫結論。回看按鈕會把
  「三句話抓重點」移入鍵盤焦點，手機停在 viewport `y≈120px`、桌機停在 reader `y≈142px`
  （捲動容器頂端 `66px`），不再被黏性導覽遮住。
- 下一站主卡另顯示下一篇既有閱讀任務的問題，主按鈕直接標示「繼續第 2/9 站」。代表流程在
  390×844 的第一屏仍看得到主按鈕（底部 `y≈742px`）；點擊後開啟既有 800VDC 保護文章、回到
  `scrollY=0`，並顯示「供電與散熱 · 第 2/9 站」及相同的下一站問題。
- 產出 payload 與瀏覽器執行時各自完整枚舉：4 條路線的 25／25 篇主文章都有理解問題與 3 點
  原文提示。建置新增硬閘門，任何 route 主文章缺閱讀任務或三句重點都直接失敗；下一站仍只由
  `RESEARCH_LEARNING_ROUTES` 與 graph 第一篇既有 `articleIds` 決定，payload 升為
  `learningPathVersion: 4`。
- 另以 390×844 逐篇渲染全部 25 個 route 主文章：25／25 都有理解檢查與主動作、0 篇水平
  溢出，主按鈕全數留在交接區第一屏；最長的是液冷產品資格站，按鈕底部 `y≈806px`。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 453 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留既有 6 warnings），inline JavaScript、
  `git diff --check`、衝突標記與 `CLAUDE.md`／`AGENTS.md` 同步檢查通過。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `ce883bda…`。

## 族群矩陣系統問題選路 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只把既有學習路線與
文章宣告族群整理成矩陣起讀入口，不修改研究來源、主張、證據層級、圖譜 edge、公司映射、
財務歸因或投資判斷。

- 390×844 同狀態基準顯示：矩陣首個「開始學這個族群」在 `y=980px`，第一屏只有三層方法與
  四組覆蓋數字；整頁高 `9,144px`。讀者被要求從 11 個族群任選一個，卻沒有先看到它們如何
  共同回答同一個系統問題。
- 矩陣頂端新增「先選一個系統問題」，逐卡呈現供電與散熱、記憶體與封裝、運算與互連、公司
  財務案例四條既有學習路線。每張卡直接顯示白話問題、主文章已宣告的相關族群、站數與第一站；
  同一族群跨卡出現明示為多個系統角色，不是重複計分。
- route guide 由 `RESEARCH_LEARNING_ROUTES`、25 篇既有 route 主文章與其 `article.groups`
  決定；第一站固定取 route step 1，不使用最新、熱門度、相似度或模型另推關係。獨立解析
  建置 payload 與瀏覽器 DOM 均得到 4 張路線卡；供電與散熱卡的 6 個族群逐項一致。
- 手機第一個可執行起點提前到 `y≈574px`，且無水平溢出；桌機 1280×720 同時看得到四條路線
  與四個起讀按鈕。點擊供電與散熱第一站會開啟既有 800VDC 文章、回到 `scrollY=0`，並顯示
  「第 1/9 站」。原本的三層完成度方法改為原生 `details` 預設收合，展開後三層與非多空分數
  警語完整保留。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 453 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留既有 6 warnings），inline JavaScript、
  `git diff --check`、衝突標記與 `CLAUDE.md`／`AGENTS.md` 同步檢查通過。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `782cb79e…`。

## 長文名詞速查與原位返回 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只增加既有文章字典的
閱讀期回查入口，不修改研究來源、主張、術語解釋、證據層級、圖譜 edge、公司映射、財務歸因
或投資判斷。

- 390×844 同狀態基準顯示：記憶體起點文章全長 `6,486px`，原名詞小字典與正文
  「分層不是替代排行榜」相隔 `2,117px`；1280×720 的同段距離也有 `1,287px`。讀者在正文
  遇到 HBM4、SOCAMM、CMX、CXL 4.0 時，原本只能離開當下位置回捲查字典。
- 窄幅畫面在原字典離開閱讀區後才顯示左下「名詞速查」，桌機則在 sticky 本頁大綱與來源摘要
  之間固定顯示入口；兩者共用同一個原生 `dialog`，不和右下回頂端按鈕重疊，也不會在仍看得到
  原字典時重複催促。
- dialog 的標題詞數、搜尋索引與每一列內容都直接從同篇「名詞小字典」list runs 取得；沒有
  字典的 `event-tsmc-2026q2` 實測為 0 個 dialog、0 個速查入口。搜尋 `CXL` 得到 1／12 個結果，
  顯示文字逐字等於原字典，不生成第二份定義。
- 390×844 與 1280×720 都在同一正文位置驗證：開啟後搜尋欄取得焦點，window／reader scroll
  保持不變；關閉後回到原觸發按鈕與閱讀位置。按鈕具 `aria-haspopup=dialog`／`aria-controls`，
  結果狀態以 `aria-live` 回報，對話框沿用原生 Escape 行為並支援明示關閉與背景點擊。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 453 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留既有 6 warnings），inline JavaScript、
  `git diff --check`、衝突標記與 `CLAUDE.md`／`AGENTS.md` 同步檢查通過。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `316b3381…`。

## 研究摘要結論與驗證卡 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只重排既有 generated
研究摘要，不修改主命題、證據文字、可信度、影響路由、monitor、來源、圖譜 edge 或投資判斷。

- 390×844 基準顯示：摘要五個項目全塞在同一個 `497px` bullet list；一句話結論、已知、未知、
  影響範圍與下一步沒有視覺層級。1280×720 雖縮至 `258px`，但變成一整塊橫向密集小字。
- 讀者畫面將相同五段內容重排為一張全寬「一句話結論」主卡，以及「目前已知、尚未知道、
  對哪些族群有意義、下一步看什麼」四張驗證卡；桌機用兩欄、手機單欄，文字標籤與 H3 語意
  同時保留，不以顏色單獨表意。
- renderer 只有在五個預定標籤完整、唯一時才轉成 `role=list`／`role=listitem` 卡片，否則退回
  原本清單；每張卡只拆出既有 bold label，正文 runs 的文字與連結不重寫、不摘要。
- 目前 34／34 篇一般市場議題都符合五標籤契約；唯一不同的 `event-tsmc-2026q2` 是事件錨點，
  本來就沒有這組 generated summary，因此保留既有格式。以瀏覽器 DOM 對建置 JSON 逐欄比較，
  代表文章的 5／5 個 label 與正文完全一致；另以獨立 Python 解析重算得到相同 34＋1 範圍。
- 手機卡片版高度由 `497px` 增至 `712px`，用較大的正文與分組空間交換掃讀清楚度；390×844
  畫面仍能同時看到五張卡與下一個可信度區塊起點，深淺色均無水平溢出。桌機版為 `388px`、
  兩欄各 `390.5px`，結論固定全寬。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 453 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留既有 6 warnings），inline JavaScript、
  `git diff --check`、衝突標記與 `CLAUDE.md`／`AGENTS.md` 同步檢查通過。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `1b08bdae…`。

## 新手名詞小字典漸進展開 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只調整既有新手字典的
顯示方式，不修改研究來源、主張、術語解釋、證據層級、圖譜 edge、公司映射、財務歸因或
投資判斷。

- 390×844 同狀態基準顯示：記憶體起點文章有 12 個名詞，從「名詞小字典」到
  「接下來怎麼追」相隔約 `1,231px`；即使三句重點已提前，讀者仍會在追蹤與反證問題前遇到
  一整段定義牆。
- 讀者畫面把名詞小字典改成原生 `details`，預設收合並顯示詞數與「遇到陌生詞再展開」；
  收合狀態讓「接下來怎麼追」與「想一想」直接接續重要性，展開後仍逐項呈現原始定義。
- 展開控制保留瀏覽器原生展開狀態、鍵盤操作與焦點輪廓，手機觸控高度至少 56px。來源
  Markdown、parser blocks、搜尋文字與研究查核內容不變；這是顯示層的漸進揭露，不是摘要或刪節。
- 同一篇文章收合後，小字典到下一節只剩約 `83px`，「接下來怎麼追」由頁面 `y=3,064px`
  提前到 `y=1,914px`；390×844 與 1280×720 均無水平溢出。實機展開核對 12／12 項，首項
  HBM、末項 NIXL 與原始內容一致，收合控制為可聚焦的原生 `SUMMARY` 且保留 3px 焦點輪廓。
- `Darwin 25.5.0 arm64`、Python 3.11.11 預設環境執行 453 tests 全綠；research queue、radar、
  method audit、knowledge graph lint 均為 0 errors（queue 保留既有 6 warnings），inline JavaScript、
  `git diff --check`、衝突標記與 `CLAUDE.md`／`AGENTS.md` 同步檢查通過。連續兩次 dashboard
  build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `3dbcc9bf…`。

## 研究文章首屏閱讀任務與新手段落重排 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只改善文章首屏定位與
新手段落的顯示順序，不修改研究來源、主張、證據層級、圖譜 edge、公司映射、財務歸因或
投資判斷。

- 390×844 同狀態基準顯示：文章雖在首屏底部露出「新手先讀」，但記憶體起點文章先排 12 個
  名詞，真正的「三句話抓重點」位於頁面 `y=2,041px`；讀者還沒知道文章要解決什麼，就先穿過
  查核狀態、日期、路線、大綱與整份字典。
- 標題與查核警語後新增「新手閱讀任務」，只逐字擷取同篇「為什麼重要」開頭的完整句子與
  「想一想」第一題，分別顯示「這篇先釐清」與「讀完試著回答」。卡片明示來源在本文
  既有段落，不另寫摘要、不新增或提高研究主張；有學習路線時同步顯示路線與站次。
- 完整「新手先讀」在讀者畫面重排為「三句話抓重點 → 為什麼重要 → 名詞小字典 → 接下來
  怎麼追 → 想一想」，並提醒先抓主線、遇到陌生詞再查。Markdown、parser blocks 與查核附錄
  內容維持原樣。
- 現行 25／25 個學習路線主文章均可由原始 Markdown 獨立回查上述兩個來源段落；
  `attach_research_learning_paths()` 新增發布閘門，任何路線主文章缺少閱讀任務即停止建置。
  方法 registry 與 selection fingerprint 未變動，最新 append-only 快照仍為
  `RMA-2026-08-09-12`。
- `Darwin 25.5.0 arm64`、Python 3.11.11 執行 453 tests 全綠；research queue、radar、method
  audit、knowledge graph lint 均為 0 errors（queue 保留既有 6 個證據時效／影響映射 warning），
  inline JavaScript、`git diff --check`、衝突標記與 `CLAUDE.md`／`AGENTS.md` 同步檢查通過。
  連續兩次 dashboard build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `ff3dca0c…`。
- 以 1280×720 與 390×844 同狀態前後對照：兩種寬度都在文章頂端直接看到閱讀任務；手機卡片
  完整落在第一屏內、頁面寬度等於 viewport；25 站中內容最長的 HBF 任務卡底部仍在
  `y=830px`。第二篇記憶體起點亦顯示正確內容，完整新手段落
  的三句重點與重要性已排在字典之前；「查看完整路線」仍能抵達同一中心主題並回到頁首。
  瀏覽器 console 無 warning／error。

## 族群矩陣起讀文章與篩選上下文 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只改善族群矩陣到文章的
新手學習入口，不修改研究來源、主張、證據層級、圖譜 edge、公司映射、財務歸因或投資判斷。

- 同狀態實機稽核發現：族群名稱雖是按鈕，視覺上卻像靜態標題；390px 手機從矩陣中段點擊後
  會停在文章清單 `scrollY=471`，畫面既看不到族群篩選名稱，也沒有建議起讀文章。
- 11／11 個現行族群現在都有一篇既有學習路線主文章作為起點。每張族群卡直接顯示路線、站次、
  文章標題、「開始學這個族群」與「全部 N 篇」；起點只先找 `article.groups[0]` 等於該族群的文章，
  再沿用既有路線與站次，不使用最新、熱門度、文字相似度或模型判斷。未來若有族群尚無路線，
  會明示缺口而不自動補位。
- 新增族群起點發布契約：文章數逐族群與 library 完整計數一致；起讀文章開啟後位於頁首並保留
  原路線定位；「全部文章」同樣回到頁首，工具列與清單標題持續顯示目前族群。這只是整理既有
  導覽，不新增文章／圖譜映射、產業關係、公司曝險或受惠排名。
- 方法 registry 與 selection fingerprint 均未變動，最新 append-only 快照仍為
  `RMA-2026-08-09-12`、fingerprint `322e5d86…`；README、研究維護與發布檢查契約已同步。
- `Darwin 25.5.0 arm64`、Python 3.11.11 執行 453 tests 全綠；research queue、radar、method
  audit、knowledge graph lint 均為 0 errors（queue 保留既有 6 個證據時效／影響映射 warning），
  inline JavaScript、`git diff --check`、方法快照 JSON／LF、衝突標記與 `CLAUDE.md`／`AGENTS.md`
  同步檢查通過。連續兩次 dashboard build SHA 一致：`index.html` `1e3a48ae…`、`research.html`
  `00445335…`。
- 以 1280×720 與 390×844 同狀態前後對照：族群卡的起點與兩個動作均可見，手機按鈕高 44px、
  頁面寬度等於 viewport；被動元件起點抵達「供電與散熱」第 3／9 站且 `scrollY=0`，全部 30 篇
  清單也在 `scrollY=0` 顯示「被動元件 · 全部文章」，瀏覽器 console 無 warning／error。

## 研究雷達白話問題、關鍵詞與驗證動作 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只改善研究雷達的
讀者入口與查核層次，不修改候選排序、priority、knowledge value、第一拒絕條件、下一份研究
證據、升格決定、研究來源、文章／圖譜映射、公司曝險或投資判斷。

- 同狀態實機稽核發現，雷達雖已收起方法細節，卡片正面仍把 OCP、CISPR、FCC、chamber、
  lab capacity 與 qualification 等規格語言排成長段落；新手還沒理解研究問題就先被術語擋住。
  8／8 個 active 候選現改為先顯示一句白話研究問題、2–4 個關鍵詞解釋與一個下一步驗證動作。
- 完整 `why_now`、`next_evidence`、knowledge gain、first rejection 與來源沒有刪除或改寫，統一
  收進每張卡片預設關閉的「查看研究判定、原始文字與來源」查核區；已升格候選的「閱讀研究」
  與「查看證據關係」仍留在正面，點擊後文章與圖譜都由頁首開啟。
- `research_radar.py` 新增 reader-only 欄位解析與契約：active 候選必須有問句、下一個驗證動作
  及 2–4 個不重複的「術語 → 白話解釋」。這些欄位不納入 selection fingerprint，也不能改變
  凍結值、研究證據姿態或發布新的公司／投資結論；README 與兩份研究方法文件同步記錄邊界。
- 研究雷達 lint 確認 8 個候選、2 個已升格、8 個研究前凍結，方法 fingerprint 維持
  `322e5d86…`；新增 append-only 方法快照 `RMA-2026-08-09-12`。
- `Darwin 25.5.0 arm64`、Python 3.11.11 執行 452 tests 全綠；research queue、radar、method
  audit、knowledge graph lint 均為 0 errors（queue 保留既有 6 個證據時效／影響映射 warning），
  inline JavaScript、`git diff --check`、方法快照 JSON／LF、衝突標記與 `CLAUDE.md`／`AGENTS.md`
  同步檢查通過。連續兩次 dashboard build SHA 一致：`index.html` `1e3a48ae…`、`research.html`
  `dffadb2a…`。
- 以 1280×720 與 390×844 同狀態前後對照：桌機與手機首張卡均先出現白話問題、關鍵詞與驗證
  動作；390px 手機頁面寬度等於 viewport。查核區展開後原始文字仍完整可見，文章與圖譜入口
  均抵達正確 deep link 且 `scrollY=0`，瀏覽器 console 無 warning／error。

## 研究中心路線定位、站次一致與最後一站返回 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只改善學習路線定位、
文章接續與五篇文章用詞，不修改研究來源、主張、證據層級、comparison、monitor、圖譜 edge、
公司映射或財務歸因。

- 修正「記憶體與封裝」圖譜顯示 7 個主題、文章卡卻標成 8 站的不一致：每張 graph 固定只取
  第一篇可解析的既有 `article_ids` 作為主題站，補充文章不再膨脹站次。契約測試確認 25／25
  張 active graph 的主文章均存在且不重複；發布 payload 升為 `learningPathVersion: 3`。
- 深連結進文章時，標題下方新增「所屬學習路線、目前第幾站／共幾站、中心主題」定位與
  「查看完整路線」入口；正文後的下一站卡讀同一份 route 順序。最後一站改為明示閱讀路線完成，
  同時提醒不代表研究結論完成。手機驗收另修正返回圖譜仍停在文章原捲動位置的問題，現在會回到
  原路線與中心主題，且文件與圖譜捲動位置都重設到頂端。
- 完成國巨法說、優先 Q2 文件、AI 資本支出現金轉換、推論算力測試機 TAM、先進封裝區域化
  五篇白話補強，補齊正式研究／可驗證假說、eMMC、ASIC、CPO、AI1.pdf、pp.5、FY2026、ROI、
  CY2026、SoC 與 OSAT 等讀者會遇到的術語。五篇 source、claim、comparison、monitor 與鎖定
  meta 均未改動；baseline editorial lint 通過。
- 完整 34 篇 topic registry 的 warning 由 13 降至 6（非抽樣；剩餘皆為證據時效或尚未完成
  影響映射的治理提醒），新增 append-only 方法快照 `RMA-2026-08-09-11`。讀者學習升級測試
  擴為 28 篇，並新增主文章唯一性、站次一致、末站完成與跨介面返回頂端契約。
- `Darwin 25.5.0 arm64`、Python 3.11.11 執行 451 tests 全綠；research queue、radar、method
  audit、knowledge graph lint 均為 0 errors（queue 保留前述 6 個 warning），inline JavaScript、
  `git diff --check`、方法快照 JSON／LF、衝突標記與 `CLAUDE.md`／`AGENTS.md` 同步檢查通過。
  連續兩次 dashboard build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `ce74dad5…`。
  以 1280×720 與 390×844 同狀態前後對照：文章頁首可見第 1／7 站、下一站為第 2／7 站，末站
  為第 7／7 站；兩個手機狀態的頁面寬度皆等於 viewport，返回後 `scrollY=0`、圖譜捲動位置為 0。

## 研究中心液冷閱讀接力與名詞補齊 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只改善供電與散熱路線的
閱讀順序、文章接續入口與三篇文章用詞，不修改研究來源、主張、證據層級、monitor、圖譜 edge、
公司映射或財務歸因。

- 將四條讀者學習路線集中到 `RESEARCH_LEARNING_ROUTES`，發布 payload、知識圖譜入口與文章
  接續卡共用同一份順序。供電與散熱路線明示先辨識液冷產品資格、再拆迴路責任邊界；契約測試
  確認 25／25 張 active graph 各被一條路線覆蓋且沒有重複。
- 市場議題的「從這篇接著學」優先顯示同一路線的下一篇既有文章，並揭露路線站次與閱讀時間。
  接續關係只依 `route.graphIds → graph.articleIds` 解析；卡片明示這是閱讀順序，不新增供應鏈、
  客戶、受惠關係或任何研究證據。
- 完成液冷 CDU 資格、液冷迴路責任邊界與 AI 機櫃控制契約三篇白話補強：新增設備型號、TSE、
  FY2027、QD／UQD、`rackLocationId` 與 Value payload 的中文解釋。三篇 source、claim、comparison、
  monitor 與鎖定 meta 均未改動；baseline editorial lint 通過。
- 完整 34 篇 topic registry 的 warning 由 18 降至 13（非抽樣；其餘為既有時效、映射與其他文章
  可讀性債），新增 append-only 方法快照 `RMA-2026-08-09-10`。讀者學習升級測試擴為 23 篇，
  並新增路線唯一覆蓋與下一站優先順序契約。
- `Darwin 25.5.0 arm64`、Python 3.11.11 執行 451 tests 全綠；research queue、radar、method
  audit、knowledge graph lint 均為 0 errors（queue 保留前述 13 個 warning），inline JavaScript、
  `git diff --check`、方法快照 JSON／LF 與 `CLAUDE.md`／`AGENTS.md` 同步檢查通過。連續兩次
  dashboard build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `81a27c7d…`。以
  1280×720 與 390×844 實機前後對照：路線文案與下一站卡可見、點擊抵達正確文章且閱讀區回到
  頂端，頁面寬度等於 viewport，三篇字典補詞可見、查核附錄預設關閉，console 無 warning／error。

## 研究中心圖譜起讀入口與運算／互連白話升級 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只改善知識圖譜的
學習順序與三篇文章用詞，不修改研究來源、主張、證據層級、monitor、圖譜 edge、公司映射
或財務歸因。

- 「運算與互連」路線由概括描述改為可執行的建議順序：先讀 AI 儲存資料平面，再看開放
  AI 互連，最後用 PCIe 6／UCIe 檢查成熟度；其他三條路線同步明示起讀與接續順序。
  每張 active graph 的摘要下方新增「先讀主題文章」入口，且只解析 graph 已登錄的
  `article_ids`。契約測試確認 25／25 張圖譜都有可解析的既有文章，不以標題或關鍵字推測
  新文章映射。
- 完成 AMD Helios、High-NA EUV 與 UCIe 互通成熟度三篇白話升級：補齊 ASIC、SKU、
  ASE／SPIL／PTI、Helios-based／Helios-specific、Low-NA 與 GT／GT/s 等高頻術語。
  三篇 source、claim、comparison、monitor 與鎖定 meta 均未改動；baseline editorial lint 通過。
- 完整 34 篇 topic registry 的 warning 由 24 降至 18（非抽樣；其餘為既有時效、映射與
  其他文章可讀性債），新增 append-only 方法快照 `RMA-2026-08-09-09`。讀者學習升級測試
  擴為 20 篇，避免已改善文章回退。
- `Darwin 25.5.0 arm64`、Python 3.11.11 執行 449 tests 全綠；research queue、radar、method
  audit、knowledge graph lint 均為 0 errors（queue 保留前述 18 個 warning），inline JavaScript
  語法通過。連續兩次 dashboard build SHA 一致：`index.html` `1e3a48ae…`、`research.html`
  `fbedadd3…`。以 1280×720 與 390×844 實機複核：桌機可直接看到起讀入口；手機按鈕高 44px、
  頁面寬度等於 viewport，點擊後文章與閱讀區皆回到頂端；三篇新手導讀字典可見、查核附錄
  預設關閉，console 無 warning／error。

## 研究中心知識圖譜漸進導覽與 800V 電力學習路徑白話升級 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只改善知識圖譜導覽、
首屏說明與文章用詞，不修改研究來源、主張、證據層級、monitor、公司映射或量化資料。

- 同狀態實機稽核發現：行動版知識圖譜在主內容前平鋪 25 個主題按鈕，讀者尚未學會讀圖就先面對
  大量縮寫。改為「學習路線 → 中心主題 → 投影視角 → 關係來源」四步，並以供電與散熱 9、
  記憶體與封裝 7、運算與互連 8、公司財務案例 1 四條路線縮小選擇範圍。路線只分組現有 graph ID；
  新增未分類 graph 會自動落入其他主題，不會生成新 edge 或受惠關係。
- 行動版只顯示當前路線的 44px 主題下拉選擇，桌機版則保留可掃讀的主題 chips。路線、主題與公司／
  產業視角切換都會同步 deep link；圖譜首屏把 `v2 direct assessment`、`bounded proxy`
  等內部語彙改寫為「公司直接揭露且能用同期間分母重算」，財務帳本與判定不變。
- 完成 800V 執行成熟度、功率半導體分工、保護責任層、AI 電容角色與功率緩衝五篇白話升級：
  補齊 CDU、GTC、Kyber、HV、POL、DC、BBU、SiC、JFET 與 Rack 等高頻名詞，並把電容角色的
  過長段落拆成機架緩衝、高壓匯流排、板級與晶片旁四種位置。五篇的 source、claim、comparison、
  monitor 與鎖定 meta 均未改動；baseline editorial lint 通過。
- 完整 34 篇 topic registry 的 warning 由 33 降至 24（非抽樣；剩餘為既有時效、映射與其他文章的
  可讀性債），新增 append-only 方法快照 `RMA-2026-08-09-08`。讀者學習升級測試擴為 17 篇，
  避免已改善文章回退。
- `Darwin 25.5.0 arm64`、Python 3.11.11 執行 449 tests 全綠；research queue、radar、method audit、
  knowledge graph lint 均為 0 errors（queue 保留前述 24 個 warning），inline JavaScript 語法通過。
  連續兩次 dashboard build SHA 一致：`index.html` `1e3a48ae…`、`research.html` `f27bc990…`。
  以 1280×720 與 390×844 實機複核：四條路線合計完整覆蓋 25 張圖譜，路線、主題下拉與投影視角
  皆可操作；兩個 viewport 的頁面寬度等於 viewport，五篇文章均以新手導讀開場、研究查核附錄預設關閉，
  console 無 warning／error。

## 研究中心首次進站三步導覽與 HBM／先進封裝白話升級 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只改善首次進站導覽、
文章解釋順序與文字，不修改研究來源、主張、證據層級、monitor 或量化資料。

- 研究文章清單在未搜尋、未篩選、未開啟文章的乾淨狀態新增「第一次來？照三步開始」：
  先到族群矩陣看產業全貌，再只看市場議題建立共同語言，最後到知識圖譜追可回查的關係。
  導覽可收合，讀者開始操作後即隱藏；三個入口會回到頁面頂端，不把原清單捲動位置帶進
  新表面。這只是安排既有內容的閱讀順序，不新增公司映射、圖譜線或投資排名。
- 完成 SPHBM4、有層次的 AI 記憶體、hybrid bonding 與 panel-level packaging 四篇白話升級：
  分別加入封裝四層、資料放置四層、三種成熟度新聞與合格封裝單位經濟的判讀框架，補齊
  SerDes／CoWoS／ABF／BT、Dynamo／NIXL、RDL／Kinex、HBM／ECD 等高頻名詞。來源、claim、
  comparison、monitor 與鎖定 meta 均未改動；baseline editorial lint 通過。
- 完整 34 篇 topic registry 的 warning 由 40 降至 33（非抽樣；本輪刻意處理上述四篇，
  其餘 33 個既有可讀性／時效／映射 warning 留待後續批次），新增 append-only 方法快照
  `RMA-2026-08-09-07`。讀者學習升級測試擴為 12 篇，避免已改善文章回退。
- `Darwin 25.5.0 arm64`、Python 3.11.11 執行 448 tests 全綠；research queue、radar、method
  audit、knowledge graph lint 均為 0 errors（queue 保留前述 33 個 warning），inline
  JavaScript、`git diff --check`、`CLAUDE.md`／`AGENTS.md` 同步及連續兩次 dashboard build
  SHA 均通過。以 1280×720 與 390×844 實機複核：三個新手入口皆到達正確表面且 `scrollY=0`，
  頁面寬度等於 viewport；導覽摘要高 57px、三個入口高 64–72px，console 無 warning／error，
  四篇文章均以新手導讀開場且研究查核附錄預設關閉。

## 研究中心新手第一屏、族群矩陣讀法與第二批白話升級 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只改善研究中心的
閱讀順序、解釋層與文章文字，不修改研究來源、主張、證據層級、monitor 或量化資料。

- 市場議題改為先顯示「新手先讀：這篇在講什麼」，再顯示由結構化 register 合成的
  「研究摘要：已知、未知與下一步」。桌機首屏的新手導讀頂端由約 730–774px 提前到 355px；
  390×844 手機由 1,128px 提前到 535px，讀者不必先穿過研究帳本語言才看到名詞與判讀框架。
- 族群矩陣新增「公司本業底稿 → 題材具名連結 → 財務落地」三層讀法，並明示矩陣數字是
  研究覆蓋進度、不是多空分數；「0 個能直接辨識」只表示公司尚未拆出題材財務分子。
- 完成優先 Q2 文件、CPO／可插拔光模組、AI 製程控制強度與 PCIe 6 合規階梯四篇白話升級：
  先寫中文概念再附英文術語，補齊判讀步驟與成熟階段，並拆開過長句。四篇的來源、claim、
  comparison、monitor 與鎖定 meta 均未改動；baseline editorial lint 通過。
- 完整 34 篇 topic registry 的 warning 由 52 降至 40（非抽樣；本輪刻意處理上述四篇，
  其餘 40 個既有可讀性／時效／映射 warning 留待後續批次），新增 append-only 方法快照
  `RMA-2026-08-09-06`。讀者學習升級測試同步擴成八篇，避免本輪文章回退。
- 同狀態瀏覽器複核另發現：段落重排後，初次排版完成前的大綱座標會誤把「從這篇接著學」
  標成目前段落；改為跨兩個 animation frame 重算並加回歸契約。修正後桌機與手機第一項均
  正確高亮新手導讀，研究查核附錄維持預設關閉。
- `Darwin 25.5.0 arm64`、Python 3.11.11 執行 448 tests 全綠；research queue、radar、method
  audit、knowledge graph lint 均為 0 errors（queue 保留前述 40 個 warning），inline
  JavaScript、`git diff --check`、`CLAUDE.md`／`AGENTS.md` 同步及連續兩次 dashboard build
  SHA 均通過。以同狀態 1280×720 與 390×844 前後對照複核，頁面寬度等於 viewport、console
  無 error／warning。

## 研究中心文章接續學習路徑與白話導讀試行 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只改善研究中心文章的
閱讀順序與站內導覽，不修改研究來源、主張、證據層級或量化資料。

- 每篇文章正文後新增「從這篇接著學」，最多提供三個延伸入口：同公司／同族群既有文章、
  已引用本文或包含具名公司的知識圖譜，以及範圍不超過三個族群的研究清單。延伸規則只讀
  現有 library 與 knowledge graph，不以關鍵字相似度新增供應鏈、客戶或受惠關係。
- 無具名公司、宣告族群或圖譜關係的政策議題，明示「尚未建立可驗證的公司或族群連結」，
  只退回市場議題資料庫，不硬做產業映射。完整 registry 274／274 篇都有接續入口（非抽樣）：
  269 篇有 3 張卡、4 篇有 2 張卡、1 篇使用安全退路。
- 市場議題的選題原因、來源與證據邊界、研究判定、主張／比較／追蹤控制表統一收進預設關閉的
  「研究查核附錄」；正文仍保留結論、機制、新手導讀與族群影響，查核資料沒有刪除或改寫。
  桌機與行動版大綱同步加入延伸學習入口，文章、圖譜、同族群與安全退路按鈕都可實際操作。
- 以 Open AI 網路、客製 HBM、AI 儲存資料面與 AI 機櫃 EMC 四篇高影響文章試行白話改寫：
  先寫中文概念再附英文術語，將新聞拆成範圍、角色與成熟階段，並把長句拆成可逐步查核的問題。
  四篇來源、主張、比較、monitor 與證據層級均未改動；baseline editorial lint 通過。
- 完整 34 篇 topic registry 的 warning 由 64 降至 52（非抽樣；本輪刻意處理四篇，另 52 個
  既有可讀性／時效 warning 保留待後續分批改善），並新增 append-only 方法快照
  `RMA-2026-08-09-05`。
- `Darwin 25.5.0 arm64`、Python 3.11.11 執行 448 tests 全綠；research queue、radar、method
  audit、knowledge graph lint 均為 0 errors（queue 另保留前述 52 個 warning），
  inline JavaScript、`git diff --check` 與 `CLAUDE.md`／`AGENTS.md` 同步檢查通過。以同狀態
  1280×720 前後對照與 390×844 手機複核，頁面寬度分別等於 viewport、瀏覽器 console 無
  error／warning，查核附錄預設關閉且完整保留 6 節。

## 研究中心讀者優先發布層 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只調整研究中心的
資訊架構、白話呈現與發布品質閘門，不修改任何研究來源、主張、證據層級或量化資料。

- 市場議題第一屏改為「先看重點：已知、未知與下一步」，固定回答一句話結論、目前已知、
  尚未知道、對哪些族群有意義與下一步看什麼；原本 inline 顯示的主張、影響、跨公司比較與
  追蹤表完整保留，但收進預設關閉的查核附錄。桌機從清單開啟文章時預設進入專注閱讀，讀者
  可用 topbar 的「文章清單／專注閱讀」切換並保存偏好。
- 研究雷達改名為「下一步研究什麼」：候選卡正面只保留現在值得看的原因與下一份證據，知識
  增量、放棄條件與來源逐卡收合；整體排序方法與方法健康度移到候選之後的查核區。
- 族群矩陣改為「各族群研究完整度」：預設用四欄回答族群、已完成、最大缺口與下一步，另以
  四張摘要卡交代公司筆記、具名公司證據、題材財務檢查與可直接辨識貢獻；原九欄矩陣與完整
  方法說明收進查核附錄，資料沒有刪除。
- 研究待辦與首屏合成文案改用一般中文，移除 `active claim`、`impact route`、`monitor`、
  `bounded_proxy` 等維運詞。2026-08-10 起新建 topic 的新手導讀若出現內部狀態碼、未解釋
  英文術語或超過 180 字的單一段落，lint 直接失敗；既有文章只警告，不回溯破壞簽核。
- `qualitative-quality` workflow 新增發布頁重建比對；模板、資料產生器或研究內容變更後，
  `index.html`／`research.html` 未同步即標紅。
- 預設環境 `Darwin 25.5.0 arm64`、Python 3.11.11 執行 446 tests 全綠；topic、radar、
  method audit、knowledge graph、質化筆記與領先假說 lint 均為 0 errors，inline JavaScript、
  `git diff --check`、`CLAUDE.md`／`AGENTS.md` 同步及連續兩次 dashboard build SHA 亦通過。
  研究中心另以同狀態 1280×720 前後對照，加做 1440×900 桌機與 390×844 手機實機複核；
  文章、研究雷達、族群矩陣及展開後查核表皆無全頁水平溢出。

## 財務材料性契約 v2 與散熱／電源試點 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只修正研究中心對
「公司有財務數字」與「題材對公司可直接歸因」的語意，不把任何研究欄位接入量化評分。

- 新增 `financial_materiality` contract v2：每筆 assessment 必須有穩定 ID、linked company
  edge、期間、揭露值、同期間分母、單位、分子／分母定義、exact source refs、證據邊界、
  複核時鐘與下一個升降級節點。歸因固定分為 `direct`、`bounded_proxy`、`not_disclosed`；
  lint 會重算占比、檢查來源與 universe company，並阻止 `company_total`／代理值被升成
  `materiality: financial`。只有 v2 direct 才能進入「題材財務可歸因」內圈。
- 修正國巨舊 pilot 的語意：2026Q2 合併營收 444.56327 億元仍保留兩份官方來源與重算結果，
  但它只能建立 `company_total／not_disclosed` 分母錨點，不能辨識 AI、MLCC、鉭質電容或
  其他產品貢獻。因此目前 edge 由 financial 改回 adjacent；前一版 changelog 與方法快照保留
  當時紀錄，不回溯改寫歷史。
- 完成散熱試點：3017 奇鋐 2026Q1 散熱產品收入 311.91 億元／合併營收 490.38 億元＝
  63.6%。公司未拆液冷／CDU，故正式裁決為 `product／bounded_proxy`，不是液冷收入占比。
- 完成電源供應試點：2301 光寶科雲端及物聯網外部營收 229.03／434.07 億元＝52.8%，
  2308 台達電電源及零組件 856.23／約 1,594 億元＝重算 53.72%、公司簡報四捨五入 54%；
  兩者的事業部都含非 CDU／非 AI 電源產品，故均為 `segment／bounded_proxy`。
- 11 族群、121 檔 universe 的 registry census 現為 4 筆 v2 assessment、3／11 族群已評估、
  0／11 族群可直接歸因；其中 bounded proxy 3、題材分子未揭露 1。根因佇列因此由 10 件
  財務 open task 改為 8 件 open task，另有 3 件「等待題材分母」watch 與 1 件政策 watch。
  這是全 registry 計數，不是抽樣估計，沒有抽樣 SE，也不是題材或投資評分。
- 方法稽核升為 v1.6，將 assessment 全欄納入 registry fingerprint，新增「財務材料性 v2」
  gate；研究中心矩陣與圖譜關係詳情同步顯示 scope、分子、分母、占比、歸因狀態與邊界。
- 預設環境 `Darwin arm64`、Python 3.11.11、UTF-8 執行 442 tests 全綠；knowledge graph、
  radar、method audit、topic 與質化筆記 lint、inline JavaScript、`git diff --check` 及
  `CLAUDE.md`／`AGENTS.md` 同步檢查均通過。研究中心另以 1280×720 與 375×812 實機瀏覽器
  複核矩陣、行動佇列、圖譜收合及 v2 明細，兩個 viewport 皆無全頁溢出，console 0 errors。

## 研究成熟度根因行動佇列、證據補強與閱讀修正 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只補研究證據、
知識圖譜、研究中心操作與文章可讀性，不把研究成熟度接進量化評分。

- 族群成熟度矩陣前新增「根因去重」行動佇列：同一 topic 即使映射五個族群仍只算一件，
  到期 monitor 以 topic＋monitor 去重；每張卡明示受影響族群、證據邊界、下一份證據與日期，
  並可直接開啟指定文章、證據圖譜或研究前凍結候選。矩陣的「建議補強」也改為精確捲到
  對應根因卡，不再只把使用者丟進數十篇族群文章。現況為 10 件財務材料性待辦與 1 件
  Section 301 政策觀察；後者明示「暫不路由」是證據邊界，不是假裝漏接。
- 補完兩個獨立來源鏈缺口。Vera Rubin 追加 GIGABYTE 自有頁面的具名 HGX Rubin NVL8
  系統證據，只佐證系統設計與元件配置，不外推 shipment、驗收或收入；國巨以公司 Q2
  簡報與 TWSE 4／5／6 月營收 140.39098／150.58220／153.59009 億元獨立重算，合計
  444.56327 億元，與簡報 444.56 億元四捨五入一致。34／34 個 active thesis 因此都有
  至少兩個獨立來源群組；完整 Q2 核閱報告仍保留成新的 active monitor，不以月營收索引
  冒充附註、毛利、EPS 或現金流驗證。
- 功率元件與半導體材料補上第一條 universe 公司橋接：2481 強茂連到 800V 功率樹、
  5234 達興材料連到 panel-level packaging。兩條都維持 `inference／named_product`，
  明示尚無具名 800V qualification、PLP HVM 客戶或財務貢獻；族群具名公司橋接由
  9／11 補到 11／11。
- 以國巨完成第一個財務材料性 pilot：公司級 2026Q2 合併營收由兩份官方來源可重算，
  建立 `verified／financial` edge；同時在圖譜第一句就聲明這不是 AI、MLCC、鉭質電容
  或其他產品線收入，也不代表被動元件全族群。財務材料性覆蓋由 0／11 到 1／11，
  其餘族群的下一步要求同一具名產品取得收入、毛利、現金流或出貨量×單價分母，不能用
  公司總營收代替產品貢獻。
- 研究中心文案把 `stale` 改寫為「證據逾期／已完成回查」，並把方法帳本的「仍 active
  monitor 到期回查」與「含退役 monitor 的全部回顧事件」分開標示。手機開啟文章時隱藏
  搜尋、類型與排序工具列，保留返回研究清單，讓第一屏直接進入標題與分析師快讀。
- 19 篇既有 topic 以 `editorial:high_frequency_glossary` 留痕補足高頻縮寫，沒有修改
  source、claim、monitor、路由或任何證據時鐘；出現至少 5 次卻未解釋的術語警告清為 0。
  可讀性檢查另改為只量瀏覽器真正顯示的連結文字，不再把 percent-encoded URL 的 `EC`
  或 endpoint 當成讀者要查的小字典術語。全體既有研究 lint 由 48 降為 34 warnings、
  維持 0 errors；剩餘項目是 3～4 次的軟提醒、既有正文／帳本比例與明示的逾期邊界。
- 上述覆蓋數是 34 篇 topic、11 族群、121 檔 universe 與 335 條 active graph edge 的
  registry 全數盤點，不是抽樣估計，因此沒有抽樣 SE。預設環境 `Darwin arm64`、
  Python 3.11.11、`C.UTF-8` 執行 438 tests 全綠；knowledge graph、radar、method audit、
  topic history lint、`git diff --check` 與 `CLAUDE.md`／`AGENTS.md` 同步檢查均通過。

## 研究中心選單收合與文章大綱動態高亮 — 2026-08-09

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只調整研究中心的
閱讀導覽與知識圖譜可用空間，不改研究內容、證據狀態或任何量化資料。

- topbar 新增可隨時復原的「收合選單／展開選單」。在桌機／平板進入收合狀態後，
  研究文章會同時隱藏 220px 篩選欄、400px 文章清單與上方搜尋工具列；圖譜、雷達與
  族群矩陣則收起共同上方工具列。狀態以 `localStorage` 保留，切換鈕本身留在 topbar，
  不會出現收起後找不到入口；≤780px 沿用既有清單→閱讀器流程，因此不顯示此鈕。
- 單一 1440×900 viewport 的 deterministic layout QA（不是抽樣統計）中，DOM bounding box
  與 CSS／viewport 算式獨立核對一致：文章 reader 由 820px 擴為 1440px，內文最大寬
  1180px；圖譜可用高度由 536.5px 擴為 834px。
- 「本頁大綱」改為真正的 scroll-spy：桌機監聽實際捲動的 `#readerScroll`，手機監聽
  `window`，並在 resize／版面收合後重算。章節與按鈕以 `data-section-index` 對應，避免
  「分析師快讀」提前排版後 DOM 順序與原文章順序不同；現行章節同步寫入
  `aria-current="location"`。移除「新手先讀」永久藍綠高亮，現在只會有一個現行章節。
- 瀏覽器實測 1440×900 桌機與 390×844 手機：高亮皆可由「分析師快讀」切換到後續章節，
  console warning／error 0。預設環境 `Darwin 25.5.0 arm64`、Python 3.11.11、
  `C.UTF-8` 執行 `python -m unittest discover -s tests`：436 tests OK。

## 雙讀者 gate 改成可判定條件，並開放可讀性改寫 — 2026-08-08

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**。使用者回報 AI 機櫃信任根
一文「完全看不懂」，量測後確認並非個案感受，而是 gate 設計問題。

- 量測讀者實際看得到的文字（正文＋研究中心會渲染成表格的帳本欄位）後：該文有
  **9 個術語出現 5 次以上卻沒進名詞小字典**，其中 SPDM 31 次、Caliptra 28 次——
  全文最重要的兩個主角一次都沒解釋；正文只占讀者可見文字的 46%。原本的雙讀者 gate
  只驗結構（新手導讀在不在、幾個 bullet），可以完全機械式通過而文章不可讀。
- `research_queue.py --lint` 新增可判定條件：術語在讀者可見文字出現 5 次以上未進
  小字典 → 2026-08-09 起新建 topic 直接 error、既有 topic warning；3～4 次一律 warning；
  正文解釋低於讀者可見文字 50% 同樣受限。術語偵測排除 registry 已登錄的公司／組織名、
  常見縮寫與帳本 ID。**衡量基準必須含帳本**：只量 markdown 正文會把帳本裡的術語全部
  漏掉，而讀者是看得到那些的（該文只量正文時僅偵測到 6 個，量讀者可見文字則是 42 個）。
- 32 篇 v3 topic 全數重跑：0 errors、62 warnings，既有已簽核文章不因新規則失效。
- **開放 editorial revision。** 原本已發布文章要改正文，只能追加綁定 sources 的
  revision transition，等於預設每次改寫都由新證據驅動；純粹改善可讀性沒有新證據，
  唯一的路是假裝有，結果是文章一旦難讀就永遠難讀。新增 `evidence: editorial:<slug>`
  同狀態 transition，但要求 lifecycle 不變、所有 source／claim／comparison／monitor
  逐字不變、meta 時鐘與路由不變；同時動到任何一項即失效。四案驗證：無標記改寫拒絕、
  純敘述改寫接受、夾帶 claim 變更拒絕、順帶延後 review_due 拒絕。
- 依新規則改寫該文並留下 editorial transition：未解釋術語 9 → **0**、正文占比
  46% → **50%**。改寫內容包含以具體場景（維修員要斷一整櫃的水電，系統憑什麼相信
  這道指令）取代抽象敘述、小字典改為解釋真正的主角、把五個規格編號收進帳本與來源、
  並新增「這篇對個股判斷的用處與界線」明講目前不支持任何個股動作。

## 掃描覆蓋、新鮮度時鐘與佐證回填三項方法修正 — 2026-08-08

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只修正研究中心方法層
與新增一篇研究，不動量化評分。三項修正都由本輪實際執行時撞到的問題觸發，不是預想。

- 新增 AI 機櫃信任根研究與圖譜（12 條線）：把 silicon RTM、device attestation、
  action authorization 與第三方保證分成四層，並把「規格層」與「可獨立查證的保證層」
  分開。主命題為推論——OCP Caliptra 側已有 S.A.F.E. 稽核報告與 Security Review Provider
  制度，DMTF SPDM 側的一致性測試指引 DSP-IS0023 至 2026-08-08 仍為 Work in Progress、
  日期停在 2022-07-11，故「支援 Caliptra／SPDM」不等於授權鏈已被第三方驗證。
  5274 信驊為唯一直接對應 universe 個股，其出貨與財務貢獻維持 unverified。
- **修正事件掃描 coverage 規則可誤標 `full`。** 實測重大訊息日端點只保留單一出表日期
  批次：TWSE 384 列與 TPEx 308 列的發言日期全部只有出表日期減一那一天，批次不具保留性。
  以合成的 1150810 批次（僅含 1150809 發言）重跑 2026-08-06～08-07 窗口，舊規則回傳
  `scope=full`、`complete=True`，但窗內命中 0 列、窗內發言日為空——批次完全不含窗內
  任何一天仍被認證為完整覆蓋。新規則另要求批次實際觀測到的發言日期落在窗口內，
  並在輸出加上 `observedSpeechDatesByMarket` 與 `batchCoversWindowByMarket`。
  三案驗證：批次已滾過窗口→partial、批次尚未到窗尾→partial、批次正好覆蓋窗尾→full。
- **修正新鮮度時鐘可被新找到的舊文件刷新。** `last_evidence_at` 原取 active thesis
  source 的 `accepted_at` 最大值，而 `accepted_at` 必然是研究者接受它的當天；因此回填
  一份 2024 年文件會把時鐘刷成當天。改為先取 effective published date（`document` 用
  `published_at`、`living_index` 用 `captured_at`）最新的來源，再於其中取 `accepted_at`
  最大值。全 32 篇 topic 重跑後 0 errors、warning 數不變，既有時鐘未受擾動。
- **開放 claim 證據清單的窄口追加。** 原本 `supporting_source_ids` 完全 immutable，使
  「補上第二條獨立來源鏈」只能借用 supersede 完成，而那會在方法帳本記錄一次從未發生的
  修正、汙染修正學習計數。改為只可追加（既有 ID 必須逐字保留為前綴），且追加來源的
  effective published date 必須 `<=` 該 claim 的 `as_of`；發布日晚於 `as_of` 者仍屬新
  證據，必須另立新 claim。四案驗證：回填舊文件接受、追加新文件拒絕、改寫既有順序拒絕、
  追加不存在 source 拒絕。
- 依修正後的規則替 MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION 回填 S7
  （TSMC 自有新聞室 2024-10-04 MOU），其五份既有來源全在 ir.amkor.com。獨立交叉驗證
  缺口由 3 篇降為 2 篇，且 `last_evidence_at` 維持 2026-08-01、`review_due` 與
  `last_reviewed_at` 均未變動——佐證變寬但新鮮度不動，正是本次兩項修正的合力結果。
- 修正契約測試把 `not_yet_testable` 誤當成帶證據結果。原測試以「非 no_new_evidence」
  一律要求附 source 與 `new_claim`，在本輪出現第一筆 `not_yet_testable` 時即誤判；
  改為只有 `new_support`／`new_contrary` 算帶證據，並與 audit 的 calibration 計數對齊。
  另把雷達測試中寫死的候選張數改為「雷達與凍結帳本逐一對應且排名連續」，
  不再讓每次發佈都必須改測試。410 → 418 tests，UTF-8 與 cp950 兩種環境皆 OK。
- 三個到期 monitor 全數留下 review event（兩筆 no_new_evidence、一筆 not_yet_testable，
  後者因 Advantest FY2026 Q2 業績排定 2026 年 10 月才公布）。修正學習與校準可用性
  兩道 gate 由 ATTENTION／NOT_READY 轉為 PASS；校準仍只報 counts，不計支持率。

## 研究雷達歷史問責、事件 coverage 與校準語意 — 2026-08-07

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只強化研究中心方法、
候選雷達與發布內容，不動量化評分。

- 新增 AI 機櫃 action-contract 研究與圖譜：由 NVIDIA DSX 的 rack identity、
  Value／Metadata、publisher ownership、liquid／electrical isolation request、BMS guardrail
  與 isolation status 建立可反證階梯；OCP OpenRMC／DMTF Redfish 只作獨立管理邊界。
  Production interoperability、field outcome 與台灣公司財務曝險維持 unverified。
- 雷達不再假設「前兩名必須升格」。本輪 5 題只有 rank 1 通過 article＋graph，rank 2–5
  維持 watch；測試改驗 promotion 是否具 route／來源契約，而不是固定產出配額。
- `research_radar.py` 開始稽核所有 schema 2 歷史雷達，不讓 retired cycle 退出
  fingerprint；共回查 4 輪、32 個候選。偵測到 4 次未到期重選，其中 3 次為 cutover 前
  未留 trigger 的歷史紀錄，原樣揭露；本輪 telemetry 以新 URL 的
  `early_trigger` 通過 2026-08-07 起的新 gate。
- 新增唯讀 `scripts/research_event_scan.py`。它不開 DB，以兩市場重大訊息出表批次的
  coverage-through 防止把尚未發布的同日事件誤標 full，並把 universe N、公告列、Q2
  損益／資產負債交集明示為母體 census。8 月 7 日實跑 N=121、公告 60 列、Q2 pair=43，
  但兩市場 coverage 只到 8 月 6 日，因此正確標為 partial。
- 方法 v1.5 移除 `supportRate`。7 筆 review event 中具新證據者只有 3 筆，且
  `new_support` 不能等同主命題為真；新快照只發布 `new_support=3`、
  `new_contrary=0` 與 N，舊快照 append-only 保留。

## 手機版寬表格改排與長頁面導覽 — 2026-08-05

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；接續同日的手機版修復，
處理剩下兩類問題：橫向捲動區在窄幅只看得到不到一半，以及長頁面沒有導覽。

- **族群熱圖窄幅改「每族群一張卡」**。原本 640px 內容塞在 285px 視窗裡橫向捲動，
  一次只看得到 44% 欄位，還會跟頁面縱向捲動搶手勢。版面從 inline style 改成
  `.heatgrid`／`.heatrow`／`.heat-cell` class（inline 會贏過 media query，這是必要條件），
  只有資料驅動的底色留在 inline；欄位語意改由每格自帶的 `.heat-cell-label` 承載，
  表頭在窄幅隱藏。375px 實測：11 張卡、55 格全部帶標籤、格高 44px、已不再橫向捲動。
  桌機（1265px）軌道與格內排版與改版前逐項一致。
- **知識圖譜畫布收進 `<details>`**。SVG `min-width:820px` 在 375px 只看得到 43%，
  縮放後節點標籤更不可讀。窄幅預設收合，讓「可逐條查核的關係」清單成為主檢視；
  預設 `open` 由 JS 在窄幅收起，JS 掛掉時退回原行為而不是整張圖消失。
- **研究資料表保留橫向捲動但加上提示**。數字表拆成卡片會失去對照關係，因此只在
  `scrollWidth > clientWidth` 時掛 `data-scrollable`，由 CSS 顯示「← 可左右捲動 →」。
  實測 4/4 張表正確標記，桌機不顯示。
- **行動版文章大綱**。`.outline` 在 ≤1180px 隱藏，但文章可達 19,000px，等於只能盲捲。
  用同一份 `article.sections` 做可收合大綱（預設收合），斷點與 `.outline` 一致以免出現
  兩邊都沒有大綱的區間；`.article-section` 補 `scroll-margin-top:112px`，否則錨點捲動
  會被 topbar 58px + 返回鍵 44px 兩層 sticky 蓋住標題。
- **回頂端按鈕**（研究中心，捲過 900px 才淡入）與 **`100dvh`**（`.shell`／`.catalog`／
  `.reader`，保留 `100vh` 在前作為舊瀏覽器 fallback）：iOS 的 `100vh` 含網址列，
  會讓內容被工具列蓋住。
- 實測 320／430／844／905／1265px：`scrollWidth` 皆等於視窗寬，觸控目標未達標者 0
  （行動版門檻 44px、桌機 24px），五元素 tile 0 溢出。
- 測試：412 tests OK，`PYTHONUTF8=1` 與預設 cp950 各一次。`test_research_center`
  的文章組裝順序斷言改成含行動版大綱的新順序（該契約保護的是組裝順序，不是某一行字面值）。

## 手機版版面溢出、返回路徑與字級／觸控目標 — 2026-08-05

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只改儀表板兩份 HTML
模板的版面與導覽，不動任何計分、資料或發布契約。

- 兩頁 `html` 補上 `-webkit-text-size-adjust:100%`。缺這行時 iOS Safari 的
  text autosizing 會挑特定區塊放大字級，被放大的卡片 min-content 隨之變寬而撐破視窗，
  其他區塊維持視窗寬 —— 就是「有些區塊很寬、有些正常」的成因。以 1.6 倍字級模擬：
  修復前 `.command-headline` 單一元素 min-content 就到 407px（視窗 375px），
  修復後全頁 `scrollWidth` 375px、零個元素超出視窗。
- `.command-headline` 在 ≤720px 解除 `word-break:keep-all`。keep-all 讓中文只能在標點
  斷行，最小內容寬 = 最長無標點詞組；當日標題實測 min-content 254px，改回一般斷行
  後為 28px。標題文字每日由資料產生，沒有標點的長句會直接撐破版面。
- `.tier-counts span` 的 `white-space:nowrap` 會套到 `.tier-counts-label`（實測 287px），
  窄幅改回可斷行；`.wrap` 手機左右內距 22px→14px。
- 兩處 JS 產生的 grid 由 `minmax(320px,1fr)`／`minmax(310px,1fr)` 改為
  `minmax(min(…,100%),1fr)`，並在 ≤720px 為 grid/flex 子項補 `min-width:0`
  （特異度 0,0,1，刻意低於 `.hscroll>*{min-width:640px}`，橫向捲動表格不受影響）。
  修復後 320／360／375／430／760／900／1280px 七個寬度的 `scrollWidth` 皆等於視窗寬。
- 研究中心手機版原本把唯一的 `index.html` 連結整個 `display:none`，回主頁只剩瀏覽器
  上一頁。改為保留精簡版返回鍵（44px 觸控目標）、`.topbar` 改 `position:sticky`，
  並讓「返回研究清單」sticky 在 58px 下方 —— 文章高度上看 19,000px，非 sticky 等同沒有。
- 手機版 `.reader-scroll` 是 `height:auto`、真正捲動的是 window，`resetReaderScroll()`
  只重設前者，導致從清單中段點開文章會落在文章中段；補上 window 重設，並把 inline
  `overflow-y` 一律清成空字串（原本還原「上次讀到的值」，重入時會把暫時的 `hidden`
  永久留下，使 `.reader-scroll` 變成不捲動的 scroll container）。
- 小字級改走 `--fs-8`～`--fs-115` token（兩份模板共 170 處 `font-size` 字面值改成
  `var(--fs-*)`）。桌機 token 值等於改版前的 px，外觀零變動（`.chip` 11px、
  `.tile .lb` 9px、`.tile .vv` 9.5px、`.recent-date` 10.5px 等逐項比對一致）；
  手機斷點統一抬高下限。原本 614/809 個小字節點的字級寫死在 JS 產生的 inline style 裡，
  media query 碰不到，這是改用 token 的主因——不要再在別處寫死 8~11.5px。
- 375px 下 <11px 的文字節點：儀表板 667→64（剩 60 個 `ⓘ` 圖示 10.5px 與 4 個圖表座標
  刻度 10px，都不是內文），研究中心 1198→0。
- 字級下限的斷點設在 **900px**（版面仍走原本的 720／780／1180）：iPhone 橫向是
  844~932px，落在這段的多半仍是手邊的手機，物理字級跟直向一樣小。實測 844×390
  兩頁 <11px 節點皆為 0、無溢出；920px 以上回到桌機值。
- 觸控目標（WCAG 2.5.5）：375px 下未達 44px 且非行內豁免者，儀表板 9→0、
  研究中心 26→0。桌機另補 2.5.8 的 24×24 下限（`.sel` 19→28px、`.pulse-head a`
  18→24px、`.strategy-body a` 19→24px），1265px 下非行內豁免者 3→0。
  句子裡的行內連結刻意不放大（2.5.5／2.5.8 的 Inline 例外；放大會撐開行高）。
- 順手修掉一個既有溢出（與本次字級無關）：`.srow` 的軌道下限
  `44px+210px+340px+200px+3*22px=860px` 是硬下限，但 901~955px 視窗扣掉 `.wrap` 44px
  與卡片內距 50px 後只剩 811px，整列會溢出（`≤900px` 才換三欄版，剛好漏掉這段）。
  各軌下限改 0；1265px 下新舊定義解析出的軌道完全相同（`44px 340px 340px 240px`），
  桌機外觀零變動，905px 由 `docSW 913 > 視窗 905` 變成相等。
- 四象限散布圖是 `viewBox="0 0 470 380"` 的 `width:100%`，375px 手機被縮到 scale 0.64、
  `font-size:9` 的座標標籤實際只有 5.8px。改成卡片內橫向捲動維持 1:1（與熱圖同一套），
  並把座標刻度 9→10、象限標籤 10.5→11；實測最小有效字級 5.8px→10px。
- 字級抬高後五元素 tile（一列 5 格）在 320px 只剩 42px 寬，「投信 -1,807張」放不下：
  `.strip` gap 6→5、`.tile` 左右內距 3→1，並在 ≤360px 改成 3+2 換行。
  320／375／430／720px 四個寬度重測 60 個 tile 皆 0 溢出。
- 測試：`python -m unittest discover -s tests` 412 tests OK，`PYTHONUTF8=1` 與預設
  cp950 兩種環境各跑一次皆綠。`test_dashboard_ux_contract` 的圖例斷言改釘 token 形式
  （該契約要保護的是「圖例帶數值文字、不只靠顏色」，不是某個 px 值）。

## 研究到期監測加入 MOPS 直接索引檢查 — 2026-08-05

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只改善研究來源取得、
到期監測與證據邊界。

- 新增唯讀 `scripts/research_filing_index.py`，逐公司查 MOPS `t57sb01`，保存檔名、大小、
  民國上傳時間與下載定位；網路、解碼或解析失敗會直接報錯，不再把抓取失敗誤記成無附件。
- 以六檔到期名單做完整 census（N=6）：2308、2337、3264、8261 已定位 115Q2 附件，
  6239、6488 截至 2026-08-05 查詢仍無索引附件。這只證明附件可取得，不代表內容已完成
  evidence pack 或獨立複核。
- 環球晶 8 月 4 日官方簡報／新聞稿顯示 Q2 營收季增 8.8%、毛利率季減 0.2pp、營業利益
  季減 3.6%；淨利季增 99.3% 主要來自 Siltronic 持股評價利益。Novara 火災目前只確認
  侷限 8 吋產線局部、12 吋新廠未受影響，尚不能推論復工日期、ASP 或漲價貢獻。
- 兩個舊 monitor 依新證據退役並由 evidence-pack／復工與 ASP 監測接續；更新既有 Q2
  研究，不為湊篇數新增文章，也不新增缺乏財務曝險證據的知識圖譜邊。

## TWSE 官方含息指數升為正式主來源 — 2026-08-04

**策略權重、tier 條件、regime 門檻與 `IS_CUTOFF` 零變動**；本次只更換同口徑大盤
序列的來源優先權與發布資料契約。

- `market` canonical 現在優先使用 TWSE `MI_INDEX` 的「發行量加權股價報酬指數」；
  FinMind `TaiwanStockTotalReturnIndex/TAIEX` 改為逐日交叉驗證，只有官方同日值缺少時
  才作備援。FinMind 尚未發布不再阻擋已有 TWSE 正式值；兩邊都缺仍硬停。
- 新增 `market_provenance`，逐日保存 canonical 來源、TWSE／FinMind 原值、絕對差異與
  對帳時間。雙邊值差異超過 `1e-6` 會保存衝突證據並拒絕衍生表與 OOS 發布；衝突日
  下次會重查 FinMind，讓上游修正後可自行恢復。正式快照也會驗證來源與 canonical 一致。
- 切換前以正式 DB 全重疊區間 2026-03-02～2026-07-31 做逐日配對：105/105 個交易日
  完全相同，最大絕對差 0；這是全重疊資料的確定性 census，不是抽樣估計，SE 不適用。
  2026-08-03 TWSE 已有 100027.02，而當次 FinMind 尚未發布，正是本次備援方向調整要處理
  的失敗型態。
- 原始資料稽核、每日簡報、儀表板 tooltip 與 OOS quality JSON 均揭露來源、待交叉驗證、
  備援或衝突狀態；TPEx 報酬指數維持不進 regime 的觀察層。
- 在正式 DB 的隔離複本完成 migration、補入 2026-08-03、重建 metrics／score 後，
  `market`、`price_adj`、`daily_metrics`、`observation_metrics`、
  `group_observation_metrics`、`group_metrics`、`market_daily`、`daily_scores`、
  `chip_health` 截至 2026-07-31 均逐列完全相同；獨立 SQL 雙向 `EXCEPT` 也全為 0。
  稽核為 121 檔 × 106 日、五表完整、canonical 106/106、衝突 0；最新日評分 121 檔。
- 驗收環境為 Windows、python.org CPython 3.12、預設 console：
  `python -m unittest discover -s tests` 共 405 項全綠；`git diff --check` 通過。

## 終版大盤缺口前移至 checkpoint 閘門 — 2026-08-04

**策略權重、tier、regime 門檻、資料來源與 `IS_CUTOFF` 零變動**；本次只修正每日抓取
失敗時的進度保存時點。

- 事故證據：`daily-fetch` #57 正確鎖定 2026-08-03，五張官方表的終版補抓與計分皆完成，
  但 FinMind TAIEX 查詢回傳 0 筆，`market_daily` 仍停在 2026-07-31。OOS 閘門正確拒絕
  發布，卻因失敗發生在 `fetch_daily` step 之後，8/3 的 margin／holding／sbl 各 121 筆
  與已抓到的 TDCC 2026-07-31 快照都未被 checkpoint commit。
- `--final-pass` 現在於 TAIEX 抓取後要求 `market` 精確存在目標交易日；落後時在衍生表
  重建前以失敗退出，讓既有 workflow 先保存五表／TDCC「每日抓取進度（未完成）」並
  停止 score、OOS 與網站發布。下一次仍沿 SQLite 缺口冪等續跑。
- 新增 stale／exact-date 回歸測試，並驗證 stale 情境不會進入參考序列抓取或
  `daily_metrics` 重建。上述筆數是正式資料格與 run log 的確定性計數，SE 不適用。
- 驗收環境為 Windows、python.org CPython 3.12、預設 console：
  `python -m unittest discover -s tests` 共 391 項全綠；`git diff --check` 通過。

## 市場議題可持續驗證契約（schema v3）— 2026-08-02

- `notes/research_topics/` 的 11 篇現行市場議題全面升級為 schema v3；每篇都必須建立
  claim–evidence ledger，逐項標示「證實／推論／待驗證」、證據支持與反證、推論邊界、
  下一個驗證步驟，並保留 superseded／refuted 的追加式修正歷史。
- 跨公司數字改用結構化 comparison ledger，強制記錄期間、單位、完整定義、來源、
  可比性判定與正規化方法；不可比的異質證據只能作診斷，不能包裝成同口徑排名。
- 每個現行議題至少配置兩個不重複的追蹤節點，明列來源、固定頻率、下次檢查、觸發條件
  與失效條件；來源、主張與追蹤節點均有 lifecycle，舊紀錄不得刪除或靜默覆寫。
- 可信度時鐘只沿主命題的現行有效證據鏈計算；複核期限屆滿且沒有新證據時，研究中心會
  自動逐級降為中、低或「需要重新驗證」，並把「主張查核狀態」與「證據可信度」分開顯示。
- `research_queue.py --lint` 新增時間截點、來源唯一性、主張關係、比較口徑、監控排程與
  Git 前版不可變欄位稽核；品質 workflow 會對前一版執行 append-only 歷史檢查。
- 新增 `MARKET_RESEARCH_METHOD.md` 與 schema v3 範本；研究中心文章同步顯示新手導讀、
  主張帳本、可比性表、追蹤節點及來源帳本，手機版保留證據摘要與可鍵盤操作的橫向表格。

**策略權重、tier 條件與 `IS_CUTOFF` 零變動**；本次只建立研究治理、驗證與呈現契約。

## 市場議題新手導讀與三題追加研究 — 2026-08-01

- `notes/research_topics/` 新增 schema v2：第一段固定提供名詞小字典、三句重點、重要性、
  後續追蹤與反證問題；`research_queue.py --lint` 會檢查結構與最低內容量，既有 v1 不回溯
  失效，2026-08-02 起的新題強制使用 v2。
- 新增 NVIDIA Spectrum-X CPO／1.6T 可插拔共存、JEDEC SPHBM4 有機基板選項、以及
  Microsoft／Meta／Amazon AI CapEx 與現金轉換三題。所有公司映射均保留一手來源邊界，
  未具名台廠只做族群 watch，不把標準、平台量產或買方 CapEx 外推成個股訂單。
- 研究中心將新手導讀在正文與大綱以獨立樣式標示，並使用導讀三句作為議題搜尋摘要。

## 研究中心獨立閱讀頁 — 2026-08-01

- 新增 `research.html`，把正式研究筆記、多空小作文與市場議題整合為可搜尋、篩選、深連結的三欄式研究中心；右側保留全文、章節目錄、查核狀態與來源證據。
- 台積電「法說會脈絡與族群方向」自首頁搬入研究中心，沿用「市場議題」閱讀模式與穩定深連結；KPI、全文與結構化族群方向仍由同一事件錨點產生，首頁不再保留大型專區或重複 payload。
- 儀表板首頁只保留三類最新研究入口，個股詳情改為連往研究中心，不再重複內嵌長文內容；本次實際建置 245 篇研究，`index.html` 由約 5.7 MB 降至約 3.2 MB。
- 每日建置與質化品質 workflow 納入研究頁模板、輸出與契約測試，避免漏發或產生空頁。

版本沿革與各版設計決策的實證依據。週度滾動驗證見 `reports/validate_*.md`。

## 官方零交易狀態與有效評分母體 — 2026-08-01

**策略權重、tier 條件與 `IS_CUTOFF` 零變動**；本次修正交易資格與資料完整性語意，
不把停牌股票的凍結值寫成當日正式分數。

- 3587 閎康自 2026-07-31 起暫停交易；TPEx 當日價格表仍有該股，但 OHLC 全空且
  成交量／金額／筆數皆為 0，法人表不列該股，融資券、外資持股與借券表仍有資料。
  舊管線固定要求五表各 121 筆，因此四次排程都在 `inst=120/121` 中止，後三表與儀表板
  無法更新。這是交易狀態，不是可用補零處理的來源缺口。
- 新增 `trading_status` 衍生索引；只有可由官方 price 原始列嚴格重算的零交易狀態，
  才把 inst 的當日預期母體由 universe 扣除。price／margin／holding／sbl 仍要求完整
  universe；一般可交易股票少法人資料仍 hard fail。狀態索引不補造或覆蓋原始資料。
- `daily_metrics` 與描述性 observation 只沿有效收盤序列計算：停牌日不產生分數、
  不推進 3 日平滑或兩日 tier 遲滯，復牌後 ret／MA／RSI 接續前一有效交易日。
  OOS quality JSON 現在同時保存 `universe`、`eligible` 與附來源的 `excluded` 清單；
  dashboard 保留停牌股票，但獨立列示「暫停／未交易」及最後訊號日期。
- 2026-07-31 正式資料驗收為 price 121、inst 120（排除 3587 一個可驗證 pair）、
  margin／holding／sbl 各 121；`audit_raw_data.py` 全期 121 檔 × 105 交易日 PASS，
  八項原始公式 mismatch 皆 0，只有 1 個既有 off-spine warning。正式 OOS 快照為
  `universe=121、eligible=120、signals=120、excluded=[3587]`；儀表板資料日 7/31，
  仍顯示 121 檔，3587 的訊號明標截至 7/30。這些是完整資料格／確定性重算，SE 不適用。
- 隔離 DB 固定上游事件資料的前後對照中，7/30 以前 `daily_metrics` 12,584 筆與
  `daily_scores` 12,584 筆逐欄 SHA-256 比對完全相同，確認本次狀態排除本身沒有改寫既有
  歷史；正式每日流程另取得 7/31 新除權息事件，依既有還原價規則正常重算，不與本項混稱。
- 驗收環境為 Windows、python.org CPython 3.12、預設 console：
  `python -m unittest discover -s tests` 共 321 項全綠；產出 HTML 的 JavaScript
  `node --check` 通過，`AGENTS.md`／`CLAUDE.md` 完全一致。

## 最近研究索引與八檔優先更新 — 2026-07-29

**策略規則、權重、tier、H# 生命週期與 `IS_CUTOFF` 零變動**；本次只更新研究維護、
正式筆記、觀察層小作文與儀表板閱讀入口。

- 以研究佇列、正式財報覆蓋與官方事件頁盤點 3035、6510、3037、3260、6271、3675、
  3711、3131 八檔。這是明標 `partial` 的優先掃描，不冒充 121 檔完整重大訊息普查。
  6510 與 3037 已有可封存的 Q2 法說，故先完成 focused evidence pack 與不同 reviewer
  的離線重算；3035 列下一順位，其餘依 8/1、8/4、8/5 等正式文件節點重查。
- 6510 的 Q2 公司法說列營收 16.40 億元、毛利率 57.5%、營業利益率 35%、EPS
  15.02 元與 HPC 56.3%；完整季報 role 保守沿用 2026Q1 會計師核閱財報，公司另列的
  三頁 Q2 摘要未放入 pack。3037 的 Q2 法說列營收 428.90 億元、毛利率 24.8%、
  營業利益率 15.5%、ABF 52%與 AI Data Center 61%，但簡報明示可能含未經會計師
  審閱資訊，完整季報 role 同樣使用 2026Q1。兩篇皆維持長約、產能、具名客戶與材料
  交期的未證邊界。
- 八檔多空小作文的量化背景全部更新至 2026-07-28；正式文件足夠的 6510／3037 同步
  重寫多空論證，其餘六檔只更新已量到的價格、籌碼、月營收與事件等待點。219 則 H#
  沒有因單週價格或一場法說自動轉移生命週期。
- 修正 `leading_hypotheses.py --context` 的顯示單位：資料庫 `ret20` 與 `rs20` 是比例，
  舊輸出卻直接加 `%`，造成 100 倍縮小。現在分別乘 100 後顯示 `%`／`pp`；例如 3035
  原始 `ret20=-0.118765`、`rs20=-0.028619`，正確呈現為 −11.9%／−2.9pp。這是同一
  交易日全集中的確定性重算，不是抽樣估計，SE 不適用。
- 儀表板新增「最近 14 天更新文章」：聚合正式筆記、多空小作文、市場議題與事件錨點，
  日期只讀文章 metadata，不碰 wall clock、git mtime 或舊 archive。文章 anchor 取市場
  資料日與有效文章日期較晚者，預設顯示最近 12 篇，可展開全部；每列保留證據狀態與
  觀察層警語，並直接連到 GitHub 全文。2026-07-29 anchor 的 7/16–7/29 視窗實際為
  152 篇：正式筆記 30、多空小作文 118、市場議題 3、事件錨點 1；這是文章 metadata
  全集計數，SE 不適用。
- 本輪完成後仍是 121/121 正式筆記已獨立核驗；2026-06 月營收與 2026Q1
  financials／balance sheet／cash flow 均為 121/121。這些是全 universe 普查，不是
  抽樣，SE 不適用。
- 驗收環境為 Windows 11、python.org CPython 3.12.10、預設 cp950 console：
  `python -m unittest discover -s tests` 共 315 項全綠；正式筆記 121 篇與事件錨點
  lint 皆 0 error／0 warning，118 篇小作文共 219 則 H# 全數通過，研究議題 lint
  為 0 error／1 個既有「尚未完成映射」警告。

## 研究更新佇列、候選議題與財報完整度閘門 — 2026-07-27

**策略規則、權重、tier 與 `IS_CUTOFF` 零變動**；本次只改研究維護與觀察層資料完整度。
完整普查與來源見 `reports/research_maintenance_2026-07-27.md`。

- 121/121 有正式筆記，118 篇已獨立核驗、3 篇仍為 draft；0 篇逾期，但 81 篇在 30 日內
  到期，65 篇集中 8/20–8/21。118 份領先假說報告含 219 則 H#，全部仍 open；196 則
  回溯基線集中於 8/20、8/21、8/31 到期。這些是全集普查，非抽樣，SE 不適用。
- 新增唯讀 `scripts/research_queue.py`，聚合正式筆記、H#、事件、財務 coverage、
  `notes/research_topics/` 與 scan log；四個族群平衡 cohort 為 31/30/30/30，
  每週輪一組。季報應有期由申報截止日推導，不拿全 DB `MAX(date)` 自我證明完整。
  已簽筆記的 `next_review` 不拿來 snooze，避免內容 SHA 失效。
- 新增 `notes/research_topics/`。首批收錄 NVIDIA Vera Rubin／Spectrum-6 量產部署，
  以及美國 Section 301 台灣商品框架；兩者都保留個股映射與證據邊界，不自動改正式筆記、
  H# 終態或量化分數。本次只把 2376 小作文未加日期的 Rubin 階段敘述改回 5/15 歷史
  切面；政策 Annex 初查確認 8471、8473.30、8486、8517.62、8541／8542 等一般豁免，
  仍待公司 HTS／原產地／Incoterms 映射。本次 scan 因缺歷史逐日 log 明標 `partial`。
- 2026-06 月營收初查 117/121，缺 3016、3661、3680、3707；TWSE／TPEx 官方 OpenAPI
  已有四筆，定向補入後為 121/121。三張季報表皆為 121/121、最新 2026Q1。
- `fetch_financials.py` 加官方當期月營收 fallback；workflow 在每月 12 日首抓、非季報月
  17 日定向重試，季報月 17 日由全抓順帶重驗；兩種 17 日路徑都用完整度閘門標紅。
  新增 `research-watch.yml` 每週一及財報 workflow 後產出唯讀 Actions
  summary／artifact，不寫 main。
- 修正 `leading_hypotheses.quant_context()`：改用 `db_ro.connect()`，不再以裸
  `sqlite3.connect()` 違反唯讀宣稱。

## 儀表板補上兩個缺席的軸:絕對報酬與時間尺度 — 2026-07-26

**策略規則、權重、tier 與 `IS_CUTOFF` 零變動**；兩者都是觀察層顯示，未計分、
未進 `daily_metrics`／`daily_scores`、不作前瞻報酬主張。

系統原本只在一個座標上說話：**族群內相對**、**20 日**。兩個軸都只存在於個股明細抽屜
裡（⑤ 融資券展開有「20日還原價報酬」、技術面有 MA5/20/60 排列），**逐檔瀏覽與排名的
畫面上一個都沒有**；一缺席，讀者就只能把相對排名讀成漲跌。

- **絕對報酬軸**。2026-07-24：相對強勢（真強／蓄勢·外資佈局／強但過熱）23 檔裡
  15 檔 20 日絕對報酬為負，最深凱美 −38.2%、興勤 −21.8%（相對分 +5.5）。族群排行榜
  「動能 vs 全體」第 3 名電源供應 +4.4%，絕對是 −10.4%、10 檔僅 1 檔在漲；第 1 名
  伺服器組裝 +18.2% 則絕對 +3.4%、6/10 檔漲——同一欄名次，一個真的在漲，一個只是
  跌得比較少。同窗口大盤 −5.01%、universe 中位 −14.8%（121 檔僅 14 檔為正），已對
  `close_adj` 自算核對一致（2428 ret20 −21.75% vs 自算 −21.75%，原始 308→241）。
  四個逐檔介面（分層帶 pill、族群內個股表格、時間尺度卡、兩視角分歧卡）都在
  相對分數旁並列絕對報酬；**↓ 與紅框標記只在分層帶 pill 上**（其餘三處以顏色
  區分正負）。族群卡加「絕對 −10.4% · 1/10 檔漲」。導言檔數由當日資料現算，
  0 檔時整句消失。
- **時間尺度軸**。同一檔在短期（close/ma5）、波段（ret20）、趨勢（ma20/ma60）
  三個尺度各排一次族群內名次。窗口為 41 個交易日（2026-05-27 起，ma60 需 60 日
  暖身）；逐日 ρ 取中位（部署中實際執行的統計量）為 短↔趨 +0.04、短↔波 +0.32、
  波↔趨 +0.49，pooled 4961 stock-days 為 +0.02/+0.34/+0.49，結論相同。
  ρ(ret20, rs20) = +1.00 且每日皆然——這是恆等式不是發現（`rs20 = ret20 − 族群中位`
  是族群內保序平移），意思是波段欄即現行視角，真正新增的是短期與趨勢兩欄。
  今日三欄極差中位 46 個百分位點，58/121 檔達 50 點以上——例:南電 tier=真強、
  波段與趨勢皆 100 分位而短期僅 9；健策波段 100 而趨勢 0。
- **`close_adj/ma60` 的否決是判斷，不是門檻擋下來的**。它在逐日中位下是 +0.789
  （對波段）與 +0.799（對 `ma20/ma60`），**低於 0.8，冗餘門檻擋不住它**（先前只引
  pooled 法的 +0.78/+0.79 而未標明換了統計量）。否決理由是它同時像另外兩欄，
  等於把第三欄花在重複資訊上；且以 41 天、日 ρ 一階自相關 +0.59~0.76 推估約
  5~11 個有效獨立觀測，0.789 與 0.80 本來就分不開。門檻是篩子，不是判準。
- ρ 逐日算再取中位，不取單日：2026-07-24 的短↔趨單日是 −0.29，全期中位 +0.04。
  窗口 41 天**不是單一走勢**：大盤先漲 8.2% 到 06-22 的期間高，再回 7.9%
  （初版誤寫成「幾乎全在同一段回檔裡」，實測後更正）。但 41 天仍短，ρ 在其他行情
  下未必相同；且 ρ 低不等於獨立——波段與趨勢共用同一段 20 日價格，機械相關底線
  尚未拆解。只當冗餘篩、不當假設檢定，故不附標準誤——這些都寫在畫面上。
- **名次不得敘述漲跌，全站一致**。這條規矩踩了三次才收乾淨：先是個股分層（相對強
  ≠ 在漲），修完在時間尺度的 `lensShape` 又犯（「波段轉強」14 檔裡 10 檔絕對為負），
  修完在兩視角分歧的卡片標題第三次犯——「漲了但沒人接」的 8 檔裡 6 檔絕對報酬為負，
  「有人在買但價格還沒動」的 8 檔**全部**為負，最深頎邦 −34.3%、台半 −33.1%
  （它們不是沒動，是跌了三成）。標題與象限角標一律改為名次／相對用語
  （「價格名次領先、籌碼名次落後」、「跑贏 · 有人接」），每列附 20 日絕對報酬。
- **頁面上的事實敘述一律由資料現算**。修正版曾把「窗口先漲 8.2% 到 6/22 再回 7.9%」
  寫死在動態的「${n_days} 個交易日」旁邊——隔一個交易日兩者就會互相矛盾，
  「再回 x%」（高點到最新日）更是每天都不同，大盤收破前高則整句變假。改由
  `build_lenses` 從 `market_daily` 現算漲幅、期間高日期與位置、回檔幅度。
- 百分比格式化真正收斂成 `fmtPct`／`pctCol` 單一入口（先前宣稱收斂，實際模板裡
  還有 5 處自寫正負號，其中族群動能欄的 `mom>=0?strong:weak` 正帶著 −0 的漲色 bug）。
  測試改為掃全檔，任何「判正負號後接 % 或 pp」的寫法都算違規。
- `build_dashboard.py` 改用 `db_ro.connect()`（鐵律要求，且 bare `sqlite3.connect`
  在路徑打錯時會無聲建空 db、再產出一份「0 檔」頁面覆蓋正常的那份）。
- **每日管線現在會因為頁面少一塊而變紅**。`tests.yml` 的 paths 刻意排除
  `index.html`/`data/`，所以產出物契約測試不會在每日 commit 上跑；先前一個區段
  落到 `except sqlite3.Error` 回 None，結果就是頁面少整塊、導覽留死連結、
  Actions 全綠、Pages 照常部署。新增 `test_dashboard_sections_present.py`（4 條，
  唯讀 index.html、純 stdlib、約 2 秒），由 `daily-fetch.yml` 在 build 後直接點名執行。
- 契約測試現況：`test_absolute_return_contract.py` 10 條、`test_time_lens_contract.py`
  13 條、`test_dashboard_js_behaviour.py` 6 條、`test_dashboard_sections_present.py`
  4 條，共 33 條。**其中 10 條做過突變檢查**（破壞後確實失敗）：候選 1 的 6 條裡
  2 條已被後續改寫取代，故不再計入；候選 2 的 4 條沿用，另 4 條為本次新做
  （標籤敘述漲跌、`fmtPct` 判號、`pctCol` 上色、`_lens_raw` 用 `_get`）。
  JS 那 6 條用 node 實際執行模板抽出的函式，不再只比對原始碼字串，並擋重複定義
  （後定義者勝，抽第一個會驗到被遮蔽的死版本）。
  釘住的實際坑：payload 漏欄、`D.allStocks` 投影欄名與 payload 不一致導致警語靜默
  空掉、`toFixed(0)` 把 −0.4% 印成「-0%」、`−0.0` 被印成綠色的「+0.0%」、
  缺值被 `_get` 捏造成 0 而排進名次。
  全套 289 tests OK（Windows 11、python.org CPython 3.12.10、預設 cp950、
  未設 `PYTHONUTF8`/`PYTHONIOENCODING`、node v24.18.0 在 PATH 上——沒有 node 時
  那 6 條會 skip，結果會是 `OK (skipped=6)`）。

## 修正終版排程跨午夜目標日 — 2026-07-24

**策略規則、權重、tier、23:40 終版門檻與 `IS_CUTOFF` 零變動**；本次只修正
workflow 延遲跨日的資料日期判定。

- 事故證據：7/23 的 23:47 安全網 run `30027825142` 延遲到台灣 7/24 01:04 啟動，
  `fetch_daily.py` 預設把目標日設為 7/24，遂被「7/24 尚未到 23:40」拒絕；7/23
  僅留下價格／法人 checkpoint，評分、OOS 與網站停在 7/22。
- workflow 現在以 runner 的 UTC 日期顯式傳入 `--end`。台灣 18:07～23:47 的 cron
  在 UTC 均屬同一交易日，即使 runner 延遲跨過台北午夜，仍會補原交易日。
- 新增 workflow 契約測試，固定要求 complete 路徑使用
  `fetch_daily.py --final-pass --end "$TARGET_DATE"`。
- 首次補跑已正確鎖定 7/23，但 TWSE 舊版 `exchangeReport/MI_MARGN` 回傳 HTTP 307；
  融資融券來源改用交易所現行 `rwd/zh/marginTrading/MI_MARGN` 路徑，並新增 URL 契約測試。

## Daily Fetch 新增 21:47 提前排隊 — 2026-07-23

**策略規則、權重、tier、終版資料門檻與 `IS_CUTOFF` 零變動**；本次只增加排程提前量。

- 新增台灣 21:47（UTC 13:47）排程，以吸收 GitHub Actions 延遲。實際啟動若仍早於
  23:40，只重試價格／法人 checkpoint；延遲跨過 23:40 才直接走完整補完。
- 保留台灣 23:47 終版安全網及 `fetch_daily.py --final-pass` 的 23:40 硬門檻，避免
  TPEx 18:00 持股初版或 TWSE 23:30 前借券資料被凍結成正式 OOS。

## Actions 寫入可靠性與終版門檻 — 2026-07-22

**策略規則、權重、tier 與 `IS_CUTOFF` 零變動**；本次只修正自動化可靠性。

- 事故證據:`daily-fetch` run `29924075052` 已建立完整場 commit `2f4bddd`，但早場
  `5ac4fdc` 先推上 `main`，導致 SQLite rebase 衝突；workflow 卻 `exit 0`，呈現綠燈但
  資料、archive 與 Pages 都未落地。補跑 run `29924837966` 後才以 `78bacc2` 正式發布。
- `daily-fetch`、`fetch-financials`、`weekly-validate` 統一使用 `repo-main-writer`
  + `queue: max`，並在實際執行時 checkout 最新 `main`；push 後再驗證遠端包含本次
  commit。rebase 衝突改為 exit 1，不再假成功；完整場另輪詢 Pages latest build，
  只有同一 commit 狀態為 `built` 才通過部署驗證。
- 避開 GitHub 整點高負載：台灣 18:07 早場、19:07 第二次提前觸發；19:07 實際
  啟動若仍早於 23:40，只做 checkpoint。新增 23:47 終版安全網。
- `fetch_daily.py --final-pass` 對當日資料新增台北 23:40 硬門檻；原始表滿檔仍不足以
  證明 18:00/22:00 日內版本已是終版。明確回補過去日期不受此時間門檻限制。
- 官方 Actions 升級為 `actions/checkout@v6`、`actions/setup-python@v6`，清除 Node 20
  deprecation 警告；新增排程、共用鎖、fresh checkout、衝突失敗與終版門檻回歸測試。

## Daily Fetch 排程提早 — 2026-07-22

- 因 GitHub Actions 實際啟動延遲，平日早場由台灣 20:17 提早為 18:00，完整場由
  23:40 提早為 19:00（GitHub cron 分別為 UTC 10:00、11:00）。資料完整性門檻不變；
  19:00 時上游資料未齊仍會停止 score、OOS 快照與儀表板發布。

## 儀表板視覺重構(claude.ai/design 移植) — 2026-07-19

**策略規則、資料 payload 與 `IS_CUTOFF` 零變動**;`build_dashboard.py` 注入層不變,
只換 `scripts/dashboard_template.html`(claude.ai/design 專案 fa6ce597 的純 JS/SVG 重寫版,
模板內建 adapter 吃同一組 `__*_JSON__` placeholder)。

- 新版面:結論先行首屏、族群價籌四象限+熱圖+排行榜、分層帶+近5日變層軌跡、
  族群內個股分數卡(族群選單/搜尋/排序)、點列開個股完整研究抽屜(七因子拆解、
  均線/營收圖、籌碼健康度、研究筆記與領先假說分頁)。
- 落地修正設計稿缺陷:族群 tag 取自 grpMeta(原 `g.tag` 會顯示 undefined)、個股列表
  族群選單取代寫死示範族群、`buildDetail` 對 tech/chip/fund/note 加 null 防護、
  筆記查核狀態改吃真實 `note.label/cls/reviewScope`(原寫死「✓ 已獨立核驗」,對當日
  3 檔 ai_draft 是不實宣稱)。
- 補回舊版 UX 契約的守護語與無障礙:4 句公開文案 guardrail、籌碼健康度「純描述性,
  不是選股排名」、≤720px 卡片化+44px 觸控目標+熱圖橫向捲動、快速導覽+`main#main`、
  抽屜 focus 管理(開啟聚焦關閉鈕、Esc/關閉後還原焦點)。
- 移除設計稿殘留的底部常駐「畫面 5 · 個股詳情」展示區(開頁自動選第一檔有筆記+假說
  的個股常駐頁尾,易被誤讀為推薦);個股詳情一律點列開抽屜,抽屜 460→880px 維持
  兩欄可讀排版。
- 全面清除設計提案殘留:畫面 1~4 螢幕編號、1a/1b/1c 選項徽章與評審式副標
  (「最白話」等)、header kicker 與 H1 同文重複(改 `__SCOPE__` 動態範圍詞);
  demo 股寫死值改動態——趨勢標籤/營收 YoY 顏色跟資料方向(當日 20 檔多頭誤標弱色、
  13 檔 YoY 負值誤標強色)、台積電 IR 期別吃 `T.quarter`、查核狀態 chip 色對映
  vcls、熱圖族群數 `G.length`、綜合分尺度 ±8.8 改由 2×ΣWEIGHTS 導出;新增頁尾
  資料來源說明(header 承諾的落點)。UX 契約測試同步鎖住以上各點。
- 個股詳情卡去重:右欄「研究筆記品質」框(meta 四格+30 秒摘要 bullet)與「領先假說」
  teaser 皆為下方個股研究面板的複述,整組移除;筆記/假說內容單一歸屬研究面板,
  卡片頂部僅保留一句話結論(結論先行 → 依據攤開的分層)。
- `tests/test_dashboard_ux_contract.py` 對齊新模板全面改寫(builder 側、策略凍結、
  公開文案、2330 觀察層鐵律斷言原樣保留);全套 193 tests 綠。**明示放棄待議**:
  術語 glossary、MA/RSI 教學區、圖表節點 tooltip/鍵盤導覽。
- 個股分層區加族群篩選(比照個股層下拉):選定族群時各層與變層軌跡改為全列該族群
  成員;全部族群模式下「＋N 檔」改為可點擊展開(原為純文字,中性觀察 62 檔僅見 8 檔)。
  分層 pill 與變層列可點開個股完整明細。
- 官方資料數據解剖(183a8f1 引入)以新設計回補:`flowSection` 把個股/族群 flow
  payload(rows 標籤/數值/公式白話 + why/how/來源)渲染成抽屜內可折疊段,個股在
  詳情卡研究面板前、族群在五項指標後,均標「觀察層 · 不計分」;頁尾前恢復
  `#flow-guide` 交易/部位觀察指南(9 條公式原文自舊版移植),快速導覽同步加錨點。
  test_observation_dashboard.py 恢復模板 marker 契約。

## 官方資料數據解剖觀察層 — 2026-07-19

**策略規則零變動**：沒有修改 `score.py`、tier、regime 或 `IS_CUTOFF`，只把新增官方欄位
轉成可閱讀、可驗算的觀察指標。

- 新增 `scripts/observation_metrics.py`，全量重建 `observation_metrics` 11,495 筆與
  `group_observation_metrics` 1,045 筆。個股層涵蓋法人方向強度、總活動占成交量、
  自營自行／避險、融資券流量與官方限額、外資法令上限、借券三分解，以及依上市／上櫃
  扣除 TWSE／TPEx 官方報酬指數的 1／5／20 日超額報酬；族群層用中位數、廣度與樣本數，
  避免股本大小主導原始加總。
- `security_market` 保存官方價格批次辨識出的 77 檔 TWSE、44 檔 TPEx 歸屬；儀表板新增
  個股與族群「數據解剖」抽屜，逐列顯示實際分子、分母、公式與初學者說明，所有入口均
  標示「不計分」。
- 在原先 29 個擴充欄之外，另保存 `margin_prev_bal`、`short_prev_bal` 兩個官方前日餘額。
  餘額變動改用同一份日報的前日／今日餘額，而不是資料庫上一日舊值；95 日、11,495 筆
  回補後，融資、融券、借券三條餘額恆等式皆為 0 mismatch。
- 官方指數涵蓋為 TWSE 95 日、TPEx 12 日，因此最新日 TWSE 77 檔可算 1／5／20 日超額，
  TPEx 44 檔可算 1／5 日、20 日暫顯示「資料不足」；不以 TWSE 指數冒充上櫃基準。
- 新增觀察公式、雙市場短歷史、群組樣本門檻、儀表板數字／教學文案與兩欄 migration／
  parser／upsert 測試；資料稽核同步加入融資、融券餘額公式。

## 原始表可續跑欄位回補與唯讀稽核 — 2026-07-19

**策略規則與資料值零變動**。把 P0 正式 DB 回補時驗證過的一次性流程收斂為可重複工具：

- `fetch_daily.py --backfill-expanded-fields` 只掃 `price∪market` 已知交易日，並以
  `RAW_COLUMN_MIGRATIONS` 任一欄為 `NULL` 判定 dataset-day／股票缺口；逐來源 checkpoint、
  自動 raw-only、不耗 FinMind token，中斷後重跑只補剩餘缺口。它與 `--force` 互斥且要求
  明確 `--start`；來源已修正、連既有非空值也須覆寫時才使用 `--force`。
- 新增唯讀 `scripts/audit_raw_data.py`：以 current universe × `price∪market` 交易日 spine
  驗證五表 grid、core／expanded 非空、SQLite integrity、法人買賣淨額與借券餘額公式；
  `market_index` 與 off-spine legacy row 明確列為非阻斷 warning，退出碼為 0/1/2。
- 新增 `RAW_DATA_BACKFILL.md`，固定 audit → 欄位回補 → 零請求重跑 → audit → metrics／score／
  首頁／tests 的 restatement 順序，並禁止覆寫 as-seen OOS snapshot／archive。正式 DB 實測
  121 檔 × 95 日五表各 11,495/11,495、八項公式零 mismatch、TWSE 95/95、TPEx 當月
  12/12；既有 off-spine `inst` 74 筆只警告、不灌入完整度。

## P0 官方原始欄位擴充與 market_index — 2026-07-19

**策略規則零變動**（`score.py` 權重／tier、`fetch_daily.py` 族群／市場條件與
`validate.py` 的 `IS_CUTOFF` 皆未動）。新增資料先留在原始／觀察層：

- 五張既有表保留同一主鍵並擴充官方回應原本已提供、先前丟棄的欄位：`price.trades`；
  `inst` 外資／投信買賣與自營自行／避險分項；`margin` 融資券流量、現金／現券償還、
  限額與資券互抵；`holding` 外資持有／尚可投資股數、比率及法令上限；`sbl` 前餘額、
  賣出、還券、調整與次日限額。五表呼叫數仍是完整新日 10 次。
- 新增 `market_index(date,market,index_key,index_name,index_type,close)`：TWSE 同一份
  `MI_INDEX` 順手保留全部報酬指數（零額外請求）；TPEx `tpex_reward_index` 每日最多
  1 次並按最新日缺口冪等補入當月櫃買報酬指數。此表非阻斷、不取代 FinMind `market`，
  暫不餵 `market_daily`／regime／分數／tier。
- `ensure_schema()` 以 `PRAGMA table_info`＋`ALTER TABLE ADD COLUMN` 原地升級 repo 既有
  SQLite，保留舊列與舊值；所有 raw upsert 改用明確欄名，避免新舊 DB 欄位順序造成錯寫。
- 2026-07-17 官方端點記憶體 DB 驗收：五表均 121/121，29 個新增欄位逐欄皆 121/121
  非空；`market_index` 為 TWSE 129 條＋TPEx 1 條。migration、雙市場欄位位置、upsert、
  checkpoint 與 market_index 補缺／冪等均有單元測試。
- 本地正式 DB 已回補 2026-03-02～2026-07-17 共 95 個交易日、121 檔 universe：五表各
  11,495 筆且新增欄位完整，補上既有 `inst` 3 個與 `holding` 6 個歷史缺口；TWSE
  `market_index` 共 12,255 筆（129 指數 × 95 日），TPEx 官方端點可取得的當月區間為
  2026-07-01～2026-07-17 共 12 日。SQLite integrity、法人買賣淨額與借券餘額公式稽核
  均無異常；非交易日 2026-06-19 的 75 筆既有 `inst` 資料保留但不進衍生表。

## 質化複核機器輔助 triage 與領先假說多空觀點 — 2026-07-18

**量化策略規則零變動**;本次只優化人工研究層的複核效率與領先假說資料豐富度,
依據與實測見 `reports/review_optimization_2026-07-18.md`:

- 新增 `scripts/qual_review.py`(唯讀):沿用 `_claim_units` 解析 claim 數字,
  pdftotext 抽同 pack cited/rendered 頁文字做數值比對(單位限定倍率換算、絕對值、
  兩數加減推導),產出六段 triage(HARD/未命中/推導/高風險詞/無文字層/命中明細)。
  實測 3693、6669 兩篇已簽核筆記:76–96 個數字機器定位 67–78%、0 HARD、單篇
  10–20 秒;「僅鄰頁命中」可自動抓 6451 型 cited 缺頁。純函式測試 23 條。
- `QUALITATIVE_RESEARCH_RUNBOOK.md`:drafter 交接前先跑 triage(shift-left),
  reviewer 由全量逐張目視改為「④⑤+抽查,發現錯誤回全量」;不可放行條件新增
  「HARD 未解決」,並明文 triage 是搜尋輔助、不得取代人工重算與推論邊界判讀。
- 領先假說報告層新增「多空觀點(小作文)」契約(`narrative_meta` v1):看多/看空
  各 100–800 字、須引用現有 H#、結尾自陳「最脆弱處」,加 1–3 條「勝負手」;
  lint 於 narrative 存在時強制檢查,196 則回溯基線不回溯補寫,2026-07-18 起前瞻
  捕捉未附時 warning。示範:3693 營邦。新增 lint 測試 8 條。
- `leading_hypotheses.py --context <股號>`:自家 db 產「量化背景」快照(月營收
  YoY、價格動能、族群排名、外資/借券/融資、TDCC 大戶、處置注意、台積電法說族群
  指引);警語「不得作為生命週期轉移證據」被 lint 鎖住。PHASE2 runbook 新增
  七面向來源 checklist 與「db 異常=捕捉觸發器、非證據」原則。

## 五張原始表全面改用 TWSE／TPEx 官方批次 — 2026-07-18

**策略規則零變動**（`score.py` 權重／tier、`fetch_daily.py` 族群／市場條件與
`validate.py` 的 `IS_CUTOFF` 皆未動）。本次只替換資料取得方式與發布時序：

- `inst` 改用 TWSE `T86`／TPEx `dailyTrade`；`margin` 改用 TWSE `MI_MARGN`／
  TPEx `margin/balance`；`holding` 改用 TWSE `MI_QFIIS`／TPEx `insti/qfii`；`sbl`
  改用 TWSE `TWT93U`／TPEx `margin/sbl`。既有 FinMind dataset 名稱保留為 CLI selector，
  歷史回補指令不必改名。
- 正常新增交易日的四張表由 `121×4=484` 次 FinMind 個股請求改成 8 次免 token 官方
  全市場請求；連同已遷移的價格，五張原始表共 10 次。FinMind 正常日理論量由 609
  降至 125（除權息 121＋分割 1＋TAIEX 1＋參考個股 2），單一免費 token 即有餘裕。
- Action 拆成台灣 20:17 早場與 23:40 正式補完：早場只抓價格／三大法人並 commit
  raw checkpoint，不重算衍生表；晚場在 TWSE 23:30 借券資料產製後補齊所有表、重試
  早場缺口，再評分／凍結 OOS／發布。手動 workflow 預設走 `complete`。
- 每張表逐交易所 commit；任一來源失敗或 universe 覆蓋不足會保存成功市場後標紅，
  下次依缺口續跑。`holding` 的 TPEx 日內有 18:00／22:00 兩版；23:40 `final_pass`
  會刷新最新日一次並於所有指定表成功後才寫 final coverage，避免初版卡住終版。
- 2026-07-17 最終資料唯讀對帳：`inst` 3 欄、`margin` 2 欄、`holding` 2 欄、`sbl`
  1 欄均為 121/121 覆蓋，對既有 DB 共 968 個欄位差異為 0。新增八端點解析、錯日期拒絕、
  單一市場失敗 checkpoint、缺口批次與 holding final-pass 冪等測試。

## 日價格改用 TWSE／TPEx 官方全市場批次 — 2026-07-18

**策略規則零變動**（`score.py` 權重／tier、`fetch_daily.py` 族群／市場條件與
`validate.py` 的 `IS_CUTOFF` 皆未動）。本次只替換五張原始表中 `price` 的取得方式：

- 上市日 OHLCV 改抓 TWSE `MI_INDEX`、上櫃改抓 TPEx `dailyQuotes`；每個待補日期各
  1 次全市場批次，再只保留 universe 股票。其餘 `inst`／`margin`／`holding`／`sbl`
  仍依 FinMind 個股缺口抓取，既有 `TaiwanStockPrice` CLI selector 保留相容性。
- 正常新增交易日由 121 次 FinMind 個股價格請求降成 2 次免 token 官方請求；FinMind
  邏輯請求由約 730 降至 609（四張原始表 484＋除權息 121＋分割 1＋TAIEX 1＋
  參考個股 2）。單一免費 token 的 600 次時額仍差 9 次，現階段仍需第二把 token；
  下一個可獨立遷移的主要項目是 121 次除權息事件查詢。
- TWSE、TPEx 分來源 commit；若其中一邊失敗，先保存另一邊成功資料供 Action checkpoint，
  但任務仍標紅。任一待補交易日未達 universe 全覆蓋時會拒絕完成，不會進入評分／發布；
  重跑依 SQLite 缺口接續。
- 2026-07-17 真實資料唯讀對帳：TWSE 77 檔＋TPEx 44 檔＝121/121，對既有 FinMind
  `price` 的 open／high／low／close／volume／amount 共 726 個欄位差異為 0；解析、
  休市、完整性與單一市場失敗 checkpoint 測試均通過。

## Universe 第二批擴充：伺服器組裝／機構 — 2026-07-17

**策略規則零變動**（`score.py` 權重/tier、`fetch_daily.py` 族群/市場條件與
`validate.py` 的 `IS_CUTOFF` 皆未動）。依
`reports/universe_gap_proposal_2026-07-17.md` 的分批順序與
`reports/screen_2026-07-17.md` 的 R2/R3/R4 結果執行第二批；R1 一手文件覆核、
人工判定與推論界線完整記於 `reports/biz_audit_serverodm_2026-07-17.md`：

- **11 群 121 檔**：新增 `serverodm`「伺服器組裝/機構」族群 10 檔（廣達、
  緯創、緯穎、英業達、技嘉、神達、勤誠、營邦、川湖、晟銘電），Universe
  由 10 群 111 檔增為 11 群 121 檔。鴻海、和碩依提案既定決策不納；微星
  因 2025 Component 50%、System 42% 且伺服器未拆，無過半證據；迎廣維持
  R3 流動性落榜（20 日中位成交值 18M < 30M）。四檔均留候選並記錄理由。
- **R1 推論邊界**：緯創 2025 營收年增 108%，AI 與一般伺服器均三位數成長並
  被公司列為主要驅動，但 3C 分部沒有拆 server，故標成治理人工判定；英業達
  依公司揭露的季度 server-related 區間與季度營收加權，2025 合理範圍
  49.86%–53.86%、中點 51.86%，亦以臨界人工判定納入，不把中點冒充公司正式
  占比。川湖導軌占 97.87%，但伺服器／AI 終端占比未揭露，biz 同步保留限制。
- **資料與額度**：10 檔定向回補 2026-03-01 起資料，實際皆自 2026-03-02 起
  有 94 筆價格資料；日資料實際 49 個核心 dataset 請求（2382 已有一個完整 pair
  因智慧補缺跳過）+ 10 個事件請求，財報四表另 40 次，沒有全量重抓。固定
  核心個股 datasets 粗估由約 658 增至 708（約 710）；事件 coverage、指數與
  交易所備援另計，仍由雙 token 輪替。
- **質化與事件契約**：10 檔與 `universe.csv` 同批建立 `focused_v1`／`ai_draft`
  質化筆記；台積電 2026Q2 事件錨點同步補 `guidance_serverodm`，維持 guidance
  鍵與 11 個正式族群一一對齊。第三批 `optnet` 仍留到 2026-10 季度窗口。
- **驗收**：離線執行 `screen.py` A 段，121 檔全數 `✅ 續留`；全庫
  `qual_notes.py --lint` 為 121 篇筆記 0 errors／0 warnings、事件錨點 1 篇
  0／0，領先假說 lint 全綠；完整 unittest 122 項全過。儀表板重建為
  11 族群／121 檔，`serverodm` 卡含台積電指引 chip，既有 `archive/2026-07-16.html`
  明確保留且無舊快照 diff。
- **重算與 OOS 邊界**：`daily_metrics`／`daily_scores` 依 121 檔新名單重算，
  新族群 10 檔各有 94 列 metrics／scores；回補含事後選樣，不作策略證據。
  `serverodm` OOS 自加入後第一份正式 as-seen 快照起算，至少累積 8 週才具
  裁決力。

## Universe 第一批擴充：電源供應 + 檢測實驗室 — 2026-07-17

**策略規則零變動**(`score.py` 權重/tier、`fetch_daily.py` 族群/市場條件與
`validate.py` 的 `IS_CUTOFF` 皆未動)。依
`reports/universe_gap_proposal_2026-07-17.md` 的分批治理提案與
`reports/screen_2026-07-17.md` 的 R2/R3/R4 體檢，完成第一批 Universe 擴充；
R1 逐檔一手文件覆核與推論界線記於
`reports/biz_audit_powersupply_2026-07-17.md`：

- **10 群 111 檔**：新增 `powersupply` 電源供應族群 10 檔（台達電、光寶科、
  群電、康舒、僑威、全漢、順達、AES-KY、飛宏、博大），並把閎康、宜特、汎銓
  三家材料／失效分析與驗證測試服務商併入 `semiequip`；Universe 由 9 群 98 檔
  增為 10 群 111 檔。新巨(2420)因 2025 PSU 僅 46.88%、2026Q1 46.02%，未過
  R1 主營收 >50% 門檻，留在 `candidates.csv` 並記錄理由。
- **R1 邊界**：台達電以複合 Power Electronics／Infrastructure 的人工判定歸
  `powersupply`，不重複放入 `thermal`；飛宏最新 PSU 68.3% 推翻「車充為主」
  疑慮，但資料中心仍僅切入敘述；博大電源占 98.34%，卻沒有 AI／資料中心直接
  營收證據。AI 曝險品質與 R1 主業門檻分開記錄，沒有暗增新策略條件。
- **資料與額度**：13 檔定向回補 2026-03-01 起資料，實際均自首個交易日
  2026-03-02 起有 94 筆價格資料；日資料 65 個 dataset 請求 + 13 個事件請求，
  財報四表另 52 次請求，未做全量重抓。沿用交接的日常粗估基準，本批固定新增
  13 檔 × 5 個核心個股 datasets = 65 次，使約 593 增至 658（約 650）；事件
  coverage 依缺口發生，連同指數與交易所備援另計，仍由雙 token 輪替。
- **質化與事件契約**：13 檔同步建立 `focused_v1`／`ai_draft` 質化筆記，避免
  `universe.csv` 先行造成 quality CI 失敗；台積電 2026Q2 事件錨點同步補齊
  `guidance_powersupply`，維持 guidance 鍵與 10 個正式族群一一對齊。
- **重算與 OOS 邊界**：`daily_metrics`／`daily_scores` 依 111 檔新名單全歷史重算；
  回補結果含事後選樣，不當成策略證據。`powersupply` 的 OOS 自加入後第一份正式
  as-seen 快照起算，至少累積 8 週才具裁決力。

## 台積電專區(觀察層)上線 — 2026-07-17

**策略規則零變動**(`score.py` 權重/tier、`fetch_daily.py` 族群/市場條件與
`validate.py` 的 `IS_CUTOFF` 皆未動)。台積電(2330)是全 universe 的上游錨定股
(capex 決定設備/材料訂單、先進封裝產能決定封測外溢、HPC 占比是 AI 需求證據),
本次把「上游方向性指引」補上儀表板,全程觀察層、不進任何評分:

- **資料流三條**:① 每日 `fetch_ref_series()`(仿 fetch_index 前例)抓 2330 收盤/
  外資持股 → `ref_price`/`ref_holding` 隔離表,**+2 req/日(591→593,單 token 上限
  600/hr,雙 token 輪替後盾)**;回補 2026-03-02 起 94 交易日(2 req)。
  ② `fetch_financials` ids 併入 `REF_IDS`,2330 月營收/財報四表 +1 req/月、+4 req/季;
  `build_fund_map` 不過濾 universe → `fund_map["2330"]` 零下游改動自動可用
  (實測「營收YoY +68%」)。③ `notes/events/*.md` 事件錨點 machine-readable meta
  (必填 6 鍵 + guidance 九鍵全齊 + kpi 四鍵),`qual_notes.py` 新增 `load_events()`
  並把事件稽核併入 `--lint`(破壞 guidance 一行實測 exit 1)。
- **儀表板**:`#tsmc-section`(anchor-nav 5→6)= 摘要 4 格(收盤/外資持股/月營收/
  最新事件,逐格 attachTip 標 FinMind 來源與未還原、保管行雜訊註記)+ 折疊深度區
  (法說 KPI 四格 + 九族群指引對照)+ 事件全文 sheet(新 `renderEventDetail`,
  借質化筆記 nb-* 樣式)+ GitHub 原始檔連結;九張族群卡各加「台積電指引」chip
  (click/keydown stopPropagation 防冒泡——實測 chip 點擊開指引詳情、非族群詳情)。
  從缺分級降級:移除 notes/events 實測 build exit 0、事件格與九卡 chip 消失;
  ref 未回補時對應格不出現。
- **鐵律驗證**:2330 不進 universe/daily_metrics/daily_scores(三查=0);
  `daily_scores` 不變量(9,212 筆、抽樣 composite)改動前後一致;ref 抓取刻意
  **不併入 data_changed**(不觸發無謂 metrics 重建);archive as-seen 快照未被覆寫
  (本地重跑實測「保留既有快照」)。
- **測試**:unittest 三模組 65→70(事件契約 4 條 + 專區契約 1 條——含 `REF_IDS`
  凍結、universe.csv 無 2330、score.py 原始碼不讀 ref 表的守護斷言;
  fundSparkDates 消費者 2→3);Chrome 實測同步 JS 斷言全過(6 錨點/4 格/9 指引/
  9 chip/事件 sheet 8 章節/深淺主題),console 零錯誤。
- **維護節奏**:每季法說會後更新事件錨點(guidance/kpi/prose)並跑
  `qual_notes.py --lint`;`next_review` 設下季法說估日(本季=2026-10-15)。
  指引若未來要驗證「方向 vs 族群後續報酬」,走 validate.py 另立觀察因子,
  不直接進評分。

## 圖表節點可追溯讀值：桌機 hover／鍵盤、手機點按 — 2026-07-14

**策略規則零變動**（`score.py` 權重/tier、`fetch_daily.py` 族群/市場條件與
`validate.py` 的 `IS_CUTOFF` 皆未動）。本次只補齊圖表的逐點查讀能力：

- 共用節點提示套用到 20 日還原價與 MA5／20／60、近 13 月營收、族群 30 日迷你趨勢、
  族群四象限五日前／目前端點、五日變層軌跡，以及綜評近 3 日殘影點與平均值。
- 每個提示固定列出日期、指標名稱、帶單位數值、數字意義與該圖實際資料來源；價格／均線
  同一日期一次並列，避免在重疊線段間猜測。歷史節點使用固定指標定義，不混入今日方向文案。
- 桌機滑過節點顯示並加垂直定位線，展開型股價／營收圖另支援 Tab 聚焦與左右方向鍵逐期讀值；
  手機點節點改用固定底部提示，並阻止事件冒泡，避免誤觸外層族群篩選或個股詳情。
- 1280px／390px 實頁檢查皆無水平溢出；手機提示完整落在 viewport，四象限、變層、迷你趨勢
  與綜評節點點按皆未誤觸原操作；完整測試 117 項通過，瀏覽器 console 無錯誤。

## 儀表板三項比較圖：族群熱圖、五日變層軌跡、七因子發散條 — 2026-07-14

**策略規則零變動**（`score.py` 權重/tier、`fetch_daily.py` 族群/市場條件與
`validate.py` 的 `IS_CUTOFF` 皆未動）。本次只擴充既有儀表板的比較與趨勢呈現：

- **族群熱圖矩陣**：五個族群指標各自依跨族群名次著色，格內保留原始值，另以
  ▲／▼／→ 雙編碼相對五個交易日前的改善、惡化或持平；族群名稱沿用既有複選篩選。
- **五日變層軌跡**：只列近五個交易日已確認分層曾改變的個股，穩定個股改顯示計數；
  共用日期與上下分層尺度，族群篩選後即時重算變層／未變層檔數。
- **七因子發散條**：綜評詳情新增 −2～+2 同尺度的七因子輪廓，條長顯示元素分，
  右欄另列權重與加權貢獻，權重 0 因子明確標示只參與分層條件。
- 1280px／390px 實機檢查無水平溢出；熱圖與軌跡篩選連動、詳情 7 列因子皆通過，
  完整測試 116 項通過。

## 領先假說補齊全 Universe 與封存回溯基線 — 2026-07-12

**策略規則零變動**。為正式筆記較晚完成獨立複核的 20 檔公司，各補 2 則具來源、正式基準、
可證偽條件與假說層期限的代表性回溯假說；觀察層由 78 檔／156 則增至全 Universe
98 檔／196 則。新增內容全部標為 `retrospective`，不進前瞻成效分母。

- 補齊材料5檔、功率4檔、散熱3檔、記憶體3檔、被動元件3檔、PCB與封測各1檔。
- 回溯基線封存日固定為 2026-07-12；lint 拒絕研究收錄日晚於封存日的回溯假說，之後新增
  H# 一律使用 `prospective`，避免事後補消息污染30／60／90日成效。

## 儀表板圖形化改版:SVG 元件庫、機制圖形與互動樞紐 — 2026-07-12

**策略規則零變動**(`score.py` 權重/tier、`fetch_daily.py` 族群/市場條件與
`validate.py` 的 `IS_CUTOFF` 皆未動)。依同日圖形化設計提案分 8 個 commit 落地,
設計主軸「元件跟著計分機制走」:排名制欄位畫五分位條、門檻制欄位畫量尺、
時間序列畫迷你趨勢;文字與 aria 語意全數保留,圖形 aria-hidden 不重複發聲。

- **SVG 元件庫**:零依賴 6 函式(quintile/meter/divergeBar/compositeBar/
  spark/rangePos),顏色走 CSS 變數自動雙主題;方向與名次由位置/形狀承載,
  紅強綠弱只重申不獨挑(protan ΔE 14.7 實測過標仍雙編碼)。
- **綜評視覺化**:綜評鈕加 ±CMAX 綜合分條(實條=3日平均、殘影點=近3日
  未平滑分);權重分解每列加等尺度貢獻條(CMAX=Σ|權重|×2 動態計算)。
- **矩陣格 stat-tile**:小標+大數值+機制圖形取代 98×5 格的重複句式;
  量尺刻度注入自 score.py 門檻常數(單一事實來源)。
- **族群卡**:修正日中位/動能列加 30 日趨勢線,廣度列改量尺(0.5=過半
  =族群現象門檻);「中位距60日高」與①價詳情加區間定位(蓄勢門檻刻度)。
- **技術面**:歷史 6→20 日,詳情加還原價+MA20 強調式小圖(MA20藍/MA60紫
  deutan ΔE 6.2 驗證不合格→不畫三色均線)與 RSI/量比量尺。
- **基本面**:詳情加近 13 個月營收柱形,基期效應一眼識破。
- **互動**:四象限圖升級為篩選控制器(點圓點=套用/取消族群篩選,未選點
  調淡不隱藏);①~⑤/綜評表頭可點排序;分層卡股名開綜評詳情;日期 ‹ ›
  步進;「/」聚焦搜尋。
- payload 2.75→2.89MB(+5.2%,gzip 後更低);整合驗收 12/12、113 tests OK。

## 領先假說第二階段 v2 前瞻稽核設計 — 2026-07-12

**策略規則零變動**。78 份報告、156 則既有主張機械遷移至 `report_version: 2`，主張正文與
狀態不改寫，全部明確標成 `retrospective`，避免把消息發布日冒充研究實際捕捉日。

- 每則新增消息發布／研究收錄／來源存取日期、前瞻或回溯模式、生命週期、證據強度、可複選
  警示、來源類型、來源主機、獨立消息鏈與假說層驗證期限。
- 閱讀狀態與底層生命週期分離，新增「到期仍無法判定」終態；未決不強迫歸類為成立或錯誤。
- 狀態改變必須新增可串接且不可跨越終態的 transition，保存日期、前後狀態、理由與證據。
- `--due [--as-of]` 提供可重建的到期佇列，`--summary` 輸出捕捉模式、生命週期與來源分布；
  報告層複核日必須等於所有追蹤中假說的最早期限。
- `--metrics [--as-of]` 只納入前瞻樣本，輸出 30／60／90 日可判定率與正式證據領先天數；
  回溯基線不會混入成效分母。
- 儀表板新增前瞻／回溯、生命週期、獨立消息鏈與到期數；既有中文閱讀狀態保留。

## 領先假說第一階段研究基線 — 2026-07-12

**策略規則零變動**。新增 `LEADING_HYPOTHESES_PHASE1_REVIEW.md`，凍結第一階段 78 檔、
156 則假說的狀態分布、可下結論與限制。基線明確記錄目前尚無驗證終態、151 則僅有單一
來源連結、全部報告集中於 2026-08-31 複核，以及「首次捕捉」在回溯建檔中不能冒充研究
系統實際捕捉日；第二階段必須用前瞻時間戳、結構化來源、狀態歷程與事件驅動複核驗證價值。

## 儀表板 UIUX 修正六項:導覽、對比、點按目標、版面、陳舊警示、文案 — 2026-07-12

**策略規則零變動**(`score.py` 權重/tier、`fetch_daily.py` 族群/市場條件與
`validate.py` 的 `IS_CUTOFF` 皆未動)。本次依全站 UIUX review 的量測結果
(390px/1280px 雙 viewport 實測:點按目標、WCAG 對比、頁面結構)依序修正:

- **手機導覽**:全頁 21,200px 而 sticky/fixed 導覽元素為 0,≤720px 讓 anchor-nav
  sticky 置頂(scroll-padding 74px 對齊錨點落點)。
- **對比**:淺色主題 tinted 底小字多處低於 AA(格內評分依據 3.81、綜評副行 3.81、
  籌碼待 3.97);說明小字改 `--ink-2`,淺色三語彙色加深,深色 `@media` 與
  `[data-theme]` 兩套不一致的色票統一為一套。修正後 14 組實測淺色最低 4.75、
  深色最低 4.62。
- **點按目標**:手機日期選擇器 18px→44px、市場籤條 26px→44px、展開鈕 40→44px;
  搜尋框字級 16px 防 iOS 聚焦自動放大。
- **族群卡版面**:9 卡在 4 欄 grid 產生孤兒列,桌機改 auto-fit(3×3,區塊
  1,950→1,335px);手機直排 4,029px 改橫向 snap 滑動(→475px,全頁 21,200→17,728px)。
- **資料陳舊警示**:最新頁「(最新)」標籤無從分辨管線是否停更;資料日距瀏覽日
  ≥4 個日曆日(避開週末+單日假期)或 manifest 顯示本頁為舊快取時,以 histNote 提示。
- **文案**:「淨賣 -0.27%股本」等動詞+帶號值的雙重否定,統一為「動詞帶方向 →
  絕對值」(數據表量值欄維持帶號);投信 0 張不再顯示「+0張」。對應更新 4 筆
  釘住舊格式的契約測試,測試意圖(原始方向與相對分數分離)不變。

## 領先假說觀察層與儀表板對照 — 2026-07-12

**策略規則零變動**（`score.py` 權重／tier、`fetch_daily.py` 族群／市場條件與
`validate.py` 的 `IS_CUTOFF` 皆未動）。本次新增市場流傳主張的研究觀察層，不把新聞、
社群、匿名法人或管理層談話升格為量化因子或正式一手證據。

- 新增 `notes/leading_hypotheses/` 與研究方法文件，只允許為有效
  `independently_verified` 正式筆記建立報告；每份報告以正式筆記內容 SHA 錨定比較基準。
- 先行版本涵蓋訊芯-KY、萬潤、高力、富喬、金居、雙鴻、京元電子、世芯-KY、金像電、
  台光電，以及第二批奇鋐、欣興、南亞科、華邦電、群聯、旺矽、穎崴、創意、健策、國巨，
  第三批旺宏、凱美、立隆電、晶豪科、漢磊、信驊、力成、矽格、環球晶、南茂，以及
  第四批中砂、光洋科、嘉晶、健鼎、弘塑、京鼎、辛耘、家登、均華、昇陽半導體，
  第五批智原、力旺、譜瑞-KY、祥碩、愛普、晶心科、M31、精測、日月光投控、南電，以及
  第六批華新科、禾伸堂、大毅、華容、興勤、鈺邦、強茂、台半、富鼎、大中，以及
  第七批菱生、超豐、景碩、威剛、欣銓、宜鼎、鈺創、頎邦、合晶、同欣電，以及
  收尾批德微、聯茂、台燿、矽力-KY、捷敏-KY、博智、朋程、華泰，合計
  78 檔、156 則具時間戳、來源層級、正式資料基準、可證偽條件與下次驗證的假說。
- 狀態區分管理層具名轉述、方向一致但未確認、合理線索、歸因錯誤、無依據的精確主張、
  正式反證與已解決；多篇轉載同一訊息鏈不算獨立確認，失效或證實後保留歷史而不回寫。
- 讀者介面改用「管理層說法・待驗證／方向相符・細節待證／合理線索・證據不足／歸因錯置／
  精確細節無法核實／已驗證成立／已驗證不成立」；英文代碼只保留為穩定內部格式，並新增
  「初次捕捉 → 持續觀察或證據警示 → 驗證終態」狀態機與轉移規則。
- 新增 `leading_hypotheses.py --lint`，檢查固定欄位、HTTPS 來源、狀態、日期、連續 H# 編號、
  正式筆記有效狀態與 SHA；並納入獨立質化品質 workflow。
- 儀表板同一公司研究入口改為「正式筆記／領先假說」Tab；78 檔以紫點提示，領先假說頁顯示
  狀態分布、品質邊界與完整主張。此層不影響 `composite`、tier 或任何 OOS 計算。

## 質化研究一手文件取得與官方備援 — 2026-07-12

**策略規則零變動**（`score.py` 權重／tier、`fetch_daily.py` 族群／市場條件與
`validate.py` 的 `IS_CUTOFF` 皆未動）。本次只補齊 focused 質化研究的取件操作，避免 agent
因公司 IR 改版、MOPS 動態下載或舊書籤失效而無限追逐來源。

- 新增公司 IR → MOPS／TWSE → TPEx 的角色別取件表，並以 TWSE／TPEx 公司基本資料 OpenAPI
  定位官方公司網站；搜尋引擎與二手資料仍只能用於發現入口。
- 實測並記錄 `doc.twse.com.tw/server-java/t57sb01` 的財報／年報查詢參數。`step=1` 回傳的是
  文件清單，點擊後才產生短效 PDF，因此 evidence 優先記永久附件直鏈；動態文件則記完整
  官方清單 URL，加上精確檔名、期間及上傳日，不把首頁或短效 `/pdf/` 位址當來源。
- 補上 MOPS 法說附件、TPEx 法說附件與單筆重大訊息的常見 URL 形態，以及 popup、HTML
  偽 PDF、JavaScript／session、文件更正與舊路由失效時的官方備援。
- 收件新增 `%PDF-`、`pdfinfo`、公司／期間、頁數與 SHA 驗收；10 分鐘搜尋止損、缺必備 role
  維持 `ai_draft`、reviewer 不重新下載與來源替換必須建立新 pack SHA 等品質門檻均未放寬。

## 個股自身技術面觀察：MA／RSI／價量關係 — 2026-07-11

**策略規則零變動**（`score.py` 權重／tier、`fetch_daily.py` 族群／市場條件與
`validate.py` 的 `IS_CUTOFF` 皆未動）。本次只新增個股相對自身歷史的描述性觀察，
不以既有 in-sample 歷史把技術指標直接升格為計分因子。

- `daily_metrics` 新增還原價 MA5／20／60、Wilder RSI14、原始成交量、5／20／60 日均量與
  當日量÷20日均量；完整視窗不足或中間缺值時保留 NULL，不用短樣本冒充完整週期。
- OOS as-seen 個股快照同步保存新增欄位；既有快照只新增 NULL 欄，不用現行規則回填舊日，
  避免前視與 restated history。
- 儀表板新增獨立技術面觀察卡，解讀均線排列、現價偏離、RSI 水位與五日變化、價量確認、
  最近一日穿越與均線五日方向。所有文字明示為狀態描述，不是隔日預測或買賣建議，且不影響
  `composite`、`tier` 或籌碼健康診斷。
- 頁尾新增 MA／RSI／VOL 白話辭典、五步盤讀順序與常見訊號組合；RSI 改以「近14日平均
  上漲力道與平均下跌力道」解釋 50 分界，避免只寫「動能占優」而缺乏可驗算的直覺。
- 技術卡與頁尾指南加入固定系列識別色：MA5 橘、MA20 藍、MA60 紫，現價維持主文字色；
  顏色只區分時間尺度，不沿用紅／綠強弱語意，並保留文字標籤以兼顧色覺差異與黑白閱讀。
- 移除「現價/MA20 或 MA5/MA20 穿越」的斜線縮寫；技術卡分開說明現價跨越 MA20 與
  MA5 跨越 MA20，頁尾並列出上穿、跌破的前一日／今日判定方式。
- 混合均線不再只寫「均線交錯、現價在 MA20 上／下」；改列 MA5／20／60 由高到低的
  實際順序，並完整說明現價相對三條均線的位置。RSI 保留在獨立力道段落，不混入均線結構。
- 價格列移除需自行上下對位的斜線表頭，改讓現價與每條 MA 的數字各自帶標籤；距離改寫成
  「比 MA5／20／60 高或低多少」，並把「短線偏離」明確改為「與近20日平均價格的差距」。

## 質化研究 focused_v1：縮短逐篇驗證工時 — 2026-07-11

**策略規則零變動**（`score.py` 權重／tier、`fetch_daily.py` 族群／市場條件與
`validate.py` 的 `IS_CUTOFF` 皆未動）。60/98 篇完成全文獨立核驗後，實務瓶頸已從寫作
轉為整本 PDF 渲染、來源無限追逐，以及 reviewer 重複下載同一文件；本次只收斂研究流程，
不把質化內容作為量化策略的 OOS 證據。

- 新建或重新完整研究的筆記改用向後相容的 `research_profile: focused_v1`；既有未標
  profile 的 v2 筆記不回溯失效。每家公司只保留 3–5 份核心一手文件，正文以約 25–35 個
  真正重要 claim block 為目標；年報、年度財報、最新季報與最新法說 role 必須齊全，
  股東會僅必要時加入。文件與 role 是簽核硬門檻，主張數是防止失焦的 warning。
- 新增 `qual_evidence.py`：drafter 把本機 PDF 建成內容定址的 SHA-256 evidence pack，
  payload mode 標成唯讀並以完整 SHA／精確目錄驗證竄改，只提交小型 manifest；這是
  流程封存而非不可繞過的 ACL。PDF／PNG 留在 `tmp/`，渲染圖放在 pack 外，計畫固定
  只有正文實際引用頁及前後各一頁，不再全本轉圖，也不改動 SHA payload。
- evidence manifest 固定記錄 10 分鐘來源搜尋止損與「未驗證主張已刪除」attestation。
  找不到穩定一手來源就停止追逐、從正文刪除主張；只有兩份一手來源互相矛盾才可標示
  `conflicted`。
- reviewer 必須與 drafter 不同，使用同一 SHA pack 離線驗證文件、獨立重算數字／期間／
  單位並判讀推論邊界，不重新下載；固定 `review_method`、pack SHA 與全文內容 SHA 共同
  鎖住簽核版本。lint 另核對 note、核心來源清單與 tracked manifest 的股票、日期、URL、
  文件 ID 及 pack SHA。
- 改為每完成一篇 `independently_verified`，只提交該 note 與對應 manifest 並立即做一個
  中文 commit，不再等待三篇成批。獨立品質 workflow 已納入 evidence pack 測試。

## 質化研究品質系統 v2＋已確認錯誤優先修正 — 2026-07-11

**策略規則零變動**（`score.py` 權重／tier、`fetch_daily.py` 族群／市場條件與
`validate.py` 的 `IS_CUTOFF` 皆未動）。本次只處理 `notes/qualitative/` 的研究正確性、
一手證據、獨立複核與對外狀態語意；不以這批質化修正作為調整量化策略的 OOS 證據。

- 優先修正交叉查證已確認的錯誤：大毅 2025 前三季／Q3 營收小數位放大十倍、立隆電
  2026 Q1 營收、富鼎 2025 前三季營收、德微 2026 年 1 月營收與 YoY、昇陽半導體把
  2026 Q1 成果誤寫成 Q2、訊芯-KY 把越南北江省光州誤寫為廣州、愛普星號與上市市場
  說明、朋程法說場次、世芯-KY 否認專案遞延，以及華容無研究必要且無來源的股價敘事。
  每個存續更正主張都補公司／交易所直接 `[S#]`；華容為純刪除。
- 改寫者以兩組分工完成修正，另一位未參與改寫的 reviewer 逐篇打開原始 PDF／公司頁，
  重新核對數字、期間、單位、引用映射與推論邊界，10/10 通過。這十篇只標
  `partially_verified` 與 `confirmed_corrections_only`（華容為
  `confirmed_correction_deletion_only`），明確不代表全文查核。
- `qual_notes.py` 將時效（fresh/due）與查核品質（AI 草稿／部分核驗／全文獨立核驗／
  來源衝突）拆成兩軸。舊筆記不再因 `last_updated` 新就看似已驗證；本次盤點結果為
  98 篇中 10 篇局部修正已核驗、88 篇 AI 草稿、0 篇全文獨立核驗。
- template v2 新增產業結構、獲利模式、財務品質、護城河、KPI、風險、治理與證據索引；
  固定來源格式為 `一手/二手/衍生｜文件｜定位｜直接 URL`。全文獨立核驗採 claim-block
  Boolean gate：每個實質段落、bullet 與表格資料列都必須在同一 block 引用一手來源。
- 簽核契約要求 `drafted_by != reviewed_by`、reviewer 日期／範圍及內容 SHA-256；任何正文
  或 meta 後續變動都會使 hash 失效並保守降回 AI 草稿。新增 `--lint`、`--quality`、
  `--needs-review`、`--invalid`、`--hash`，並攔截未定義／重複來源、假日期、重複 stock ID、
  reviewer 自審、二手-only 與表格列漏引等錯誤。另設 `qualitative-quality` workflow 專門
  gate 質化檔與 parser 變更，不阻斷每日市場資料 ingestion；dashboard 對無效狀態保守降級。
- 儀表板改顯示查核狀態、reviewer、核驗範圍、資料截至日、claim／一手證據覆蓋；逾期只
  加外圈警示，不改寫既有查核程度。另修正舊 parser 會丟掉第一個 `##` 前 Universe 警語、
  多行摘要被截斷與 Windows 檔名含 `*` 無法建立骨架等問題。

## 儀表板解釋層重構:原始方向、相對排名與確認狀態分離 — 2026-07-10

**策略規則零變動**(`score.py` 權重、排名、平滑、tier 條件，`fetch_daily.py` 族群/市場
條件與 `validate.py` 的 `IS_CUTOFF` 皆未動)，只調整儀表板 payload、資訊架構與互動。
既有畫面會把相對排名的正負分數讀成外資/投信真的買進或賣出，也不容易分辨「今日條件」
與「連續兩日確認後的正式分層」，使數學上正確的結果產生語意誤導。

- 五個觀察面向同時顯示「原始數值方向」「族群相對位置或固定門檻」「元素分數」；例如
  外資仍減持但在同族群減持較少，可得相對正分，反向案例也明確說明。點開分層可查看
  當日各元素分 × 權重、近 3 日綜合分與 3 日平均，並分開標示今日初判 1/2 與已確認分層。
- 首屏新增今日摘要與族群價籌四象限；族群卡把「目前水位」和「相較 5 個交易日前的變化」
  分列，當全族群皆為修正日淨賣時，明說相對最好仍是淨賣，不再用箭頭或名次暗示買超。
- 桌機改為 hover 精簡預覽、首次 click 即開啟可持續閱讀的 drawer；手機改用直向個股卡片，
  搜尋/排序/族群篩選同步。個股分層每層預設只列前 6 檔、可展開全部；快速導覽保留已選
  族群。補上鍵盤焦點管理、Esc、焦點返回、語義標籤與較高文字對比。
- 月營收改成事實描述，明示單月 YoY/MoM 不等於需求、獲利或整體強弱；質化筆記增加
  30 秒摘要、章節折疊與依內容顯示的財經術語說明。
- 新增 payload 與 UX 契約回歸測試，鎖定原始方向與相對分數可同時成立、三日平滑算式、
  分層確認狀態、全族群負值摘要與策略參數凍結；同資料日 archive 仍維持首次建立後不覆寫。

## 籌碼現況診斷移除名次、明示正負方向 — 2026-07-10

**策略規則零變動**(`chip_health` 門檻、淨分、label、composite/tier 與 `IS_CUTOFF`
皆未動),只修正儀表板資訊表達。先前 tooltip 同時顯示原始正負值與健康色,例如
`借券餘額 −0.21pp` 會被判為健康,卻沒有明說「負值=借券下降=壓力減輕」；另外
`族群內 8/12` 容易被誤讀成有選股效力的名次,與 2026-07-10 對抗性審查結論衝突。

- 儀表板完全移除 chip health 的族群名次,改稱「籌碼現況診斷 · 非排名/不計分」。
  `chip_health.grp_rank/grp_n` 暫留 db 與 OOS snapshot 作歷史稽核/schema 相容,不再對外顯示。
- 七列名稱直接標出語意方向(如「融資↓去槓桿」「股東人數↓集中」「借券↓減壓」),
  每列新增「原始方向 → 健康/中性/警示」判讀。tooltip 首句明示原始正負號不等於好壞。
- TDCC 大戶/股東人數、借券三項仍是未完成 OOS 裁決的觀察因子,每列固定加註
  「方向仍待 OOS 驗證」,避免健康色被誤認為已有預測證據。

## OOS 改採 append-only as-seen 原始訊號快照 — 2026-07-10

**策略規則零變動**(權重/tier/族群狀態條件皆未動,`IS_CUTOFF` 不動),修正驗證資料的
point-in-time 完整性。對抗性 review 發現:HTML archive 雖是 as-seen,但
`daily_scores`/`daily_metrics` 每日仍以最新資料、universe 與分組重算全歷史,
`validate.py` 原本直接讀重算表,使 cutoff 後數字不是真正 OOS。實測凍結頁 vs 現行 db:
2026-07-06 有 21/98 檔 composite、1 檔 tier 被事後改寫;07-07 有 19/98 檔 composite
被改寫(主要來自 19 檔外資持股缺值補回 + 6525 捷敏-KY 換組)。

- 新增 `scripts/snapshot_signals.py`:每日正式管線在 `score.py` 後把最新資料日 append-only
  凍結到 `oos_snapshot_runs/oos_signal_snapshots/oos_group_snapshots/
  oos_market_snapshots`。保存當時分組、34 個 daily_metrics 原始欄、13 個評分欄、
  chip health、risk flags、族群雷達、大盤 regime,以及 git SHA 與 score/metrics/
  universe/groups SHA-256。98 檔或族群表不完整時拒絕凍結、主管線失敗。
- 正式性與觸發來源解耦:`source` 只記 GitHub Actions / local provenance，另以
  `is_official` 決定 OOS 資格。本地 `scripts/run_daily.py` 與 Actions 都能發布正式快照；
  `validate.py` 固定採資料日最早正式版，後續修正版只供稽核。相同內容跨來源去重。
- `fetch_daily.py` 改為預設智慧補缺:一檔價格探針發現新交易日後，逐一比較 SQLite 的
  股票×dataset 日期，完整者零請求、只抓缺口；事件資料另記 coverage，中斷後可接續。
  提早執行而部分 dataset 延遲時，已到資料先落地、晚點重跑只補剩餘缺口；`--force`
  保留給來源修正。休市且既有資料完整時只需一次新交易日探針，不再重打全 universe。
- 正式快照新增五張原始表完整性門檻；資料未齊時拒絕發布，避免提早本地 run 污染 OOS。
  `archive/<資料日>.html` 也改為首次建立後不覆寫。
- 快照最早資料日鎖為 2026-07-10;實測該日颱風休市、五張原始表皆停在 07-09 時會
  正常略過,不把上線前 restated 07-09 誤建為第一份 OOS。完全相同的休市日重跑也以
  content hash 去重,不製造假 revision。
- `validate.py`:OOS bucket 只接受正式快照;cutoff 後沒有機器快照的舊日期標為 restated、
  不計 OOS。報告分列快照累積日數與前瞻已成熟日數;tier 轉移、族群 state 也新增 OOS 欄。
- 不從既有 HTML 反向拼湊缺欄位的假快照;正式 OOS 從本功能上線後第一個成功每日 run
  重新累積。原 07-06~07-09 數字仍保留在全期/背景欄,但不再作策略調整證據。

## 對抗性審查:chip_health / risk_flags(觀察層,不涉 OOS)— 2026-07-10

**策略規則零變動**(IS_CUTOFF 不動)。針對本週新增的兩個觀察層功能做「try to break it」
審查,同 2026-07-05 對抗性標準 review 的方法論。

- **risk_flags 抓取健康度缺口(已修復)**:TWSE/TPEx 處置+注意四端點任一失敗只印
  stderr、exit 0 不擋管線,且當天名單整表重建、不保留前一天資料——`daily_brief.py`
  品質快檢原本只查 `price/inst/margin/holding/sbl` 五表 + TDCC 鮮度,risk_flags 完全
  不在監控範圍。**實測命中**:2026-07-09 當天 TWSE 處置+TPEx 處置兩端點同時失敗,
  比對官方列管期間發現 2481 強茂、3189 景碩、5425 台半三檔當天本應仍在處置期內
  (期間涵蓋 07-09),卻因抓取失敗從名單消失,chip_health 一票否決當天漏判、品質
  快檢原本顯示「無異常」(假陰性)。已於 `daily_brief.py` 加入「處置/注意」筆數
  日對日比對(非零掉到零 → 示警),同 TDCC 鮮度檢查的簡單門檻風格。
- **chip_health 兩項設計疑慮(記入 `WEEKLY_REVIEW.md` §4,暫不調整實作)**:
  (1) 族群內淨分排名(`grp_rank`)所用 7 訊號中,外資/投信/融資水位/融資變化 4 項
  本質上就是 v2.1 已實證「族群內無選股力」的籌碼因子(fpct_chg20 族群內 IC −0.007、
  dipbuy20 −0.096)——「跟 tier 完全獨立的兩把尺」在程式碼層面成立,但統計層面
  這把尺量的東西正是被自己 IC 診斷否證過的假說,使用者看到排名容易誤讀為選股資訊。
  (2) 7 訊號等權相加,但證據等級不一致:4 項用已實證校準門檻,另外 3 項
  (TDCC 大戶/人數、借券)是 §⑥ 觀察因子、方向尚未經 OOS 驗證(裁決日
  約 2026-08-29),且沒有雜訊死區保護(不同於 DZ_FOREIGN/DZ_TRUST 的既定設計)。

## Universe biz 描述全面覆核:29 項文字修正 + 3 項族群歸類疑慮待議 — 2026-07-09

**策略規則零變動**(僅 biz 欄描述文字修正,不涉及族群/tier 變動,IS_CUTOFF 不動)。
9 個族群平行以 `notes/qualitative/*.md`(98 檔質化筆記)回頭比對 `universe.csv` 現有
biz/group 是否對齊(唯讀複核,判斷框架同 R1 商業模式準則),完整清單見
`reports/biz_audit_2026-07-09.md`。

- **29 項 biz 文字修正已套用**:多數是「現有描述只反映歷史核心產品線,筆記揭露的
  最新營收結構已有新產品線躍居主力或占比相當」,例如 6451 訊芯-KY(biz 寫「SiP模組
  封測」,實際光收發模組 63% 才是最大宗,SiP 僅 31%,並補上已查證的「鴻海系」持股
  60%)、2337 旺宏(補上已占營收 30%、年增 382% 的 NAND Flash)、3583 辛耘(補上占
  營收 58% 最大宗的設備代理業務)、6531 愛普*(原描述的 3D堆疊/HBM 產品僅占營收
  3%,改寫為實際占 70% 的 IoT RAM 主力產品)。`universe.csv` + `data/findmind.db`
  的 `universe` 表已同步、儀表板已重建(純 metadata 更新,未動 price/score)。
- **3 項族群歸類疑慮擱置**,留待下次 Universe 治理(`scripts/screen.py` 季度覆核)
  處理:3707 漢磊/3016 嘉晶(磊晶代工服務費模式,現行 9 族群無對應服務型分類可放)、
  8028 昇陽半導體(晶圓再生/薄化代工服務費模式,與 6525 案例性質類似但 packtest
  定義為 OSAT 封測不完全對應)、6271 同欣電(商業模式混合,83% 仍為代工服務費,
  判定維持 packtest 不變)。
- **另查得 1 項未查證的集團附註**待後續確認:3675 德微「達爾系」(與 Diodes Inc.
  的股權/合約關係未經查證,僅為市場慣稱)。

## Universe 主業描述修正:8131 福懋科、5328 華容 — 2026-07-09

**策略規則零變動**(僅 `universe.csv` biz 欄描述文字修正,不涉及族群/tier 變動,IS_CUTOFF 不動)。
補全 96 檔質化研究筆記過程中,研究順帶查證出兩處既有主業描述失準:

- **8131 福懋科**:「記憶體封測(力成系)」→「記憶體封測(**南亞科/台塑系**)」。查無福懋科與
  力成(6239)的集團/持股關聯——福懋科 1990 年由台塑集團旗下福懋興業(1434)轉投資成立,
  南亞科技(2408)持股由 19% 增持至 32%,為南亞科 DRAM 垂直整合鏈的封測後段;力成係獨立
  記憶體封測廠,兩者為同業競爭關係,非集團關係。查證依據見 `notes/qualitative/8131_福懋科.md`。
- **5328 華容**:「鋁質電解電容」→「**塑膠薄膜/金屬化膜電容器**」。多方查證(口袋學堂、
  MoneyDJ、NOWnews 等)一致指向華容實際產品線為塑膠薄膜電容(國內唯一掛牌塑膠薄膜電容廠),
  與鋁質電解電容(如立隆電 2472、智寶/凱美 2375)屬不同技術路線,原標註應為建立筆記時沿用
  舊資料的誤植。查證依據見 `notes/qualitative/5328_華容.md`。
- 兩檔皆不影響族群歸屬(仍分屬 packtest / passive),僅描述文字修正;`data/findmind.db` 的
  `universe` 表已用 `fetch_daily.load_universe()` 直接從修正後 CSV 重建同步(未動 price/score)。

## 新增個股質化研究筆記系統 — 2026-07-09

**策略規則零變動**(不進 daily_metrics/daily_scores,不影響權重/tier,IS_CUTOFF 不動)。
年報 MD&A、法說會重點這類質化揭露原本完全缺乏收錄管道,新增：

- `notes/qualitative/<股號>_<名稱>.md`:人工撰寫(非自動抓取),固定結構
  (業務概況/客戶產品結構/財務亮點/成長動能/風險重點/法說會頻率/資料來源/下次更新
  建議時機),`<!-- meta -->` 註解區塊放 `stock_id`/`template_version`/`last_updated`/
  `next_review`(GitHub 渲染時隱形,不干擾正文閱讀)。首批範例:6525 捷敏-KY
  (中小型股,法說會約年 1~2 場)、8299 群聯(權值股,法說會嚴格季頻)——刻意選一大
  一小對照更新頻率差異。
- `scripts/qual_notes.py`:唯讀狀態追蹤 + 骨架建立(`--missing`/`--stale`/
  `--outdated`/`--new`),對照 `config/universe.csv` 全量名單。**已有筆記的股票
  不會被要求重寫**,除非模板版本升級(`TEMPLATE_VERSION` +1)或人工判斷需要——
  避免「重新整理」變成隱性的重複勞動。
- 儀表板個股列新增「📝 筆記」badge(`build_dashboard.py` 讀 meta 狀態,`next_review`
  逾期上色提醒);點擊直接在頁內展開完整筆記全文——標題/段落/清單/表格都有排版
  (`qual_notes.py` 把每個 `##` 章節解析成結構化 blocks,前端無 innerHTML 組 DOM,
  借用既有底部詳情面板,桌機/手機同一套互動,不做 hover 預覽,底部另附 GitHub 原始檔
  連結)。無筆記股票不顯示 badge,不影響既有版面。

## Universe 覆核調整:6525 捷敏-KY 改歸 packtest — 2026-07-09

**策略規則零變動**(IS_CUTOFF 不動,同 2026-07-05/06 三次族群異動先例——universe
治理屬資料/歸類層,非 score.py CONFIG 的權重或 tier 條件變動),R1 業務歸屬覆核。

- **6525 捷敏-KY:power → packtest**(power 14→13、packtest 13→14)。原歸類業務欄
  寫「功率半導體封測」卻放在 power(功率IC/MOSFET/二極體 IDM 族群),對照同批
  2026-07-05 加入的 8131 福懋科(記憶體封測,力成系)已歸 packtest——同屬「服務
  特定終端市場的 OSAT 封測代工廠」卻歸類相反,判定為當時 R1 覆核疏漏。
- 查證(公開資訊):公司自述「捷敏賺的是功率半導體的封測代工財……向客戶收取
  封測加工費」;客戶結構為國際 IDM 大廠(~45%)+ IC 設計公司(~55%),鉅亨網
  簡介稱其為「全球前三大專業功率半導體封裝測試公司之一」——確認為純代工服務商,
  非自有品牌功率元件 IDM,business model 與 packtest(OSAT/先進封裝/AI測試)一致,
  不符 power(MOSFET/二極體/功率IC 設計製造商)定義。
- `universe.csv` biz 欄同步修正:「功率半導體封測」→「功率半導體封測(OSAT)」,
  標註代工屬性避免未來覆核再誤判。
- 全歷史依新分類重算(`fetch_daily.py`+`score.py`);6525 最新 3 日於 packtest
  族群下重算為「真強」(綜合分 ~4.0~4.2)。power/packtest 兩族群其餘成員的族群內
  排名同步因同儕組成改變而重算(1 檔換組,非新增/剔除,影響幅度小)。

## 新增第七~九族群:半導體材料+散熱+PCB/CCL;定位擴為「台股半導體與 AI 供應鏈」— 2026-07-06

**策略規則零變動**(IS_CUTOFF 不動),universe 治理事件 + **定位變更**。
依據:`reports/screen_2026-07-06.md`(36 檔候選,33 過 R2~R4,R1 覆核收 29)。

- **半導體材料 10 檔**(material):環球晶/台勝科/合晶(矽晶圓)、中砂/光洋科/
  勝一/三福化/達興/昇陽半/上品(化學品·耗材)。矽晶圓與化學品全含(同記憶體
  先例:共同驅動=晶圓廠稼動率,拆開各剩 3~4 檔不過 GRP_MIN_N)。與設備族群
  形成「稼動率 vs 擴產 capex」對照;半導體垂直鏈補完:材料→設備→設計→元件→封測。
- **散熱 7 檔**(thermal):奇鋐/雙鴻/建準/健策/力致/泰碩/高力。高力(熱交換
  多元)R1 存疑但收——無爭議僅 6 檔恰卡 GRP_MIN_N 下限,安全邊際優先於純度。
  尼得科超眾(成交值 9M)、動力-KY(23 億)被 R2/R3 刷掉,散熱池深度先天有限。
- **PCB/CCL 12 檔**(pcb):台光電/台燿/聯茂(CCL)、金居/富喬(CCL 上游,
  全含先例)、金像電/健鼎/博智/高技(板廠)、欣興/南電/景碩(載板)。
- **R1 覆核不收**:中美晶(控股+與子公司環球晶母子重疊,族群內排名會被連動
  污染)、崇越/華立(通路,同至上前例)、世禾(服務型,同帆宣前例)。
  定穎 6251 已改制投控,下季以新代號 3715 評估。
- **定位變更**:散熱與 PCB 超出「半導體」——範圍詞統一改「台股半導體與 AI
  供應鏈」(儀表板 ALL_SCOPE/60 秒導讀、README、CLAUDE.md);並修掉導讀寫死
  的「三個族群」過期殘句。
- 兩族群加入日 2026-07-06(IS_CUTOFF 後一日):回補資料(至 07-03)全落 IS 期,
  OOS 欄天然乾淨;**三族群 OOS 自 2026-07-06 起算**。
- **⚠ 規模躍遷**:69→98 檔、六→九族群。rel20 全體基準再位移;每日排程請求
  ~590/輪已貼近單 token 時額(600/hr)——FINMIND_TOKEN2 輪替自此為必要而非
  備援(secret 已設)。

## 新增第五、六族群:矽智財(ipdesign,9 檔)+ 半導體設備(semiequip,9 檔)— 2026-07-05

**策略規則零變動**(IS_CUTOFF 不動),universe 治理事件,流程同記憶體
(README「Universe 治理·新增族群」)。依據:`reports/screen_2026-07-05.md`。

- **矽智財 9 檔**:世芯-KY 3661、創意 3443、智原 3035(ASIC 設計服務)、
  力旺 3529、M31 6643、晶心科 6533(純 IP)、祥碩 5269、信驊 5274、
  譜瑞-KY 4966(高速介面/伺服器管理 IC)。市值 101 億~6,754 億,全過 R2~R4;
  共同驅動 = AI 晶片設計案 + 台積電先進製程生態系。產品型大廠(聯發科/聯詠/
  瑞昱)不屬此定義——產品線多元、非單一題材。
- **半導體設備 9 檔**:弘塑 3131、辛耘 3583(濕製程)、萬潤 6187、均華 6640
  (先進封裝)、家登 3680(EUV 光罩盒)、京鼎 3413(AMAT 代工)、旺矽 6223、
  穎崴 6515、精測 6510(測試介面)。共同驅動 = 台積電資本支出/CoWoS 擴產;
  與封測族群形成同一條 capex 鏈的上下游對照。
- **R1 覆核不收 6 檔**(純度優先,留 candidates.csv):帆宣(工程服務非設備,
  若收應與漢唐成對)、志聖/迅得/均豪(PCB/面板兼營占比存疑)、致茂(產品線
  橫跨電池/EV/光電)、鈦昇(業務雜)。
- 歷史回補 2026-03-02 起;TDCC 自加入日累積。**兩族群 OOS 從 2026-07-05 加入日
  起算**(恰為 IS_CUTOFF,週檢視只看 OOS 欄即自動排除回補 look-ahead)。
- **⚠ 族群層統計位移**:`rel20` 全體基準 51→69 檔(且新增兩族群以大型高價股
  為主,全體中位數會被拉動);個股層族群內排名獨立,既有族群個股分數不受影響。
- **工具面:FinMind token 402 輪替**(本次實戰教訓)。同日兩輪「screen +
  全量回補」耗盡單組時額(600 req/hr),第二輪回補中途 402、新股資料缺漏——
  `api_get` 改為多 token 輪替池(環境變數/`.mcp.json` 的 `FINMIND_TOKEN`/
  `FINMIND_TOKEN2`,402 立即換組、黏性沿用),daily-fetch.yml 加選配 secret
  `FINMIND_TOKEN2`。教訓:回補一輪 ≈ 5×檔數 個請求,同日多族群應一次 screen、
  一次回補;**缺漏勿全量重跑**(額度剛恢復就被 350 個請求再次燒乾,實測連環
  402 兩輪)——新增 `--stocks` 定向補缺參數(可與 `--datasets` 疊加,事件段
  同步過濾),先盤點 db 缺口再只抓缺的。

## 新增第四族群:記憶體(memory,12 檔)— 2026-07-05

**策略規則零變動**(權重/tier 條件未動,IS_CUTOFF 不動),universe 治理事件。
依據:`reports/screen_2026-07-05.md`(R1~R4 全流程)。

- **成員 12 檔**:南亞科 2408、華邦電 2344、旺宏 2337、群聯 8299、晶豪科 3006、
  鈺創 5351、愛普* 6531、威剛 3260、創見 2451、十銓 4967、宇瞻 8271、宜鼎 5289。
  邊界全含(製造/模組/控制IC 單一族群)——族群層訊號前提是共同題材驅動,
  且拆子鏈每段 <6 檔過不了 `GRP_MIN_N`。
- **R1 人工覆核不收**:力積電 6770(記憶體代工+邏輯混合,主營收歸屬存疑)、
  至上 8112(純通路商)、安國 8054(記憶體營收占比 >50% 存疑)——後兩檔留
  `candidates.csv` 下季再議。**規則刷掉**:點序 6485(39 億)、品安 8088(36 億)
  市值未達 50 億;勁永 6145 近 150 日僅 4 個交易日。
- **記憶體封測不動**:力成/南茂/福懋科續留 packtest(一檔一族群;其產能服務
  多客戶,籌碼行為同封測同業)。
- 歷史回補 2026-03-02 起(與現有基期齊);TDCC 週快照自加入日起累積,之前為永久洞
  (觀察層不計分,可接受)。
- **⚠ 選擇偏誤警告**:記憶體是「事後」(族群正熱時)加入,回補的 2026-03 至今
  歷史分數含挑贏家 look-ahead——週檢視引用時僅供參考,**該族群 OOS 從 2026-07-05
  加入日起算**,不進更早期間的 OOS 裁決。
- **⚠ 族群層統計位移**:`rel20`(20 日動能 vs 全體)的「全體」基準自此含記憶體
  12 檔,既有三族群的族群層數字與回補後歷史會輕微位移;個股層族群內排名彼此獨立,
  既有三族群個股分數不受影響。archive 快照 as-seen,不回填。

## Phase 4a:觀察層資料源——TDCC 大戶 + 借券賣出餘額 — 2026-07-05

**策略規則零變動**(不進評分/tier/儀表板;IS_CUTOFF 不動),純資料層 + 驗證層:

- **TDCC 股權分散**(週頻):新增 `scripts/fetch_tdcc.py` 直抓 opendata(免 token)
  → 新表 `tdcc_holding`(universe ∪ candidates,17 級距,append-only)。可行性實測
  (2026-07-05):FinMind `TaiwanStockHoldingSharesPer` 免費層被 400 擋(需 Backer);
  opendata 對 39 檔 universe **全覆蓋**(含 KY 股)但**僅供最新一週、不可回補**——
  自 2026-07-03 起累積,每缺一週=永久洞,故排在每日管線最前(同週冪等重抓=5 次保險,
  失敗 exit 0 不擋 FinMind 抓取)。
- **借券賣出餘額**(日頻,免費層實測可用):`fetch_daily.py` DATASETS 第 5 個
  dataset `TaiwanDailyShortSaleBalances` → 新表 `sbl`;歷史已回補 2026-03-01 起。
  ⚠ `sbl_bal` 單位是**股**(`margin_bal` 才是張)。
- **daily_metrics 新增 10 個觀察欄**:`tdcc_date`、`tdcc_big400_pct/chg`(級距 12~15)、
  `tdcc_big1000_pct/chg`(級距 15)、`tdcc_people_chg`(級距 17 人數週變化)、
  `sbl_pct/chg5/chg10/chg20`。防前視:TDCC 快照以 **T−3 日曆日生效**(週五結算、
  週六公布 → 次週一才進指標,旋鈕 `TDCC_LAG_DAYS`);pct 分母為集保庫存(非發行股本)。
- **validate.py 新增 §⑥ 觀察因子**:四因子族群內 IC(TDCC 另出「快照生效日取樣版」——
  週頻 forward-fill 使日頻 IC 的 n 虛胖 ~5 倍,8 週歸宿裁決以取樣版為準)+ 與
  fpct_chg20 共線性(族群內/混池,|ρ|≥0.7 = 疑為 s_foreign 慢版)。
  裁決條件記 `WEEKLY_REVIEW.md` §4-8:方向穩定且不共線 → 優先升格族群層訊號/
  蓄勢條件(Phase 1 結論:籌碼在族群內無選股力),不進族群內排名。
- 工具面:`fetch_daily.py --datasets` 過濾(單 dataset 回補,跳過事件段);
  `daily_brief.py` 品質快檢加 sbl 覆蓋 + TDCC 鮮度(>10 天=漏抓警告)。
- 範圍決策:當沖(TaiwanStockDayTrading)延後;分點(需 Sponsor)與自營商不做。

## 歷史報告快照(archive)— 2026-07-05

網站可回看任一日報告。策略規則零變動,純呈現層:

- 每日 build 把當日儀表板**原樣**凍結成 `archive/<資料日>.html`,並維護
  `archive/manifest.json` 日期清單;頁首「資料至」chip 改為日期選單,歷史頁
  顯示快照橫幅 + 回最新連結。
- **語義:as-seen,不做 db 回填**——daily_scores 等衍生表每日全量重建,事後從
  db 重繪舊日期會被現行規則污染(restated history,違反「歷史判定不可事後改寫」);
  快照自 2026-07-03 起累積(repo 歷史中無更早的每日頁面可回填)。
- 舊快照頁內嵌的日期清單凍結於 build 當下,執行期自動抓 manifest 補上其後
  新增的日期;`file://` 本機預覽退回內嵌清單。

## 可讀性與可稽核性改版(陳述層)— 2026-07-05

依「所有對外文字服務於讀者」原則重寫,策略規則零變動:

- **儀表板**:新增收合式 60 秒新手導讀;五元素圖例改「每欄回答一個問題」;
  tooltip 評分依據白話化並逐格加註 FinMind 資料來源;頁尾兩行密集說明改為
  「方法與資料」六卡結構(評分四步驟、權重、個股/族群層指標辭典附公式+白話、
  評級規則含判定優先序、資料集對照表、檢驗/質疑入口與已知侷限);權重 chips
  改由 build_dashboard 注入(score.py 單一事實來源);移除 ④投信 tooltip 殘留的
  寫死 IC 數字(對抗性 review 既定政策)。補 `<meta charset/viewport>`
  (原缺:本機 file:// 開啟會亂碼、手機上 CSS 斷點不觸發)。
- **README**:重寫為現行系統的深度說明(兩層設計理念、資料結構與防前視、
  評分與 tier 條件全表、驗證與治理),修正過期資訊(30→39 檔、儀表板連結改
  GitHub Pages);版本敘事一律歸本檔,README 與網站只描述現行系統。

## 對抗性標準 review — 2026-07-05

九項攻擊電池打向評分/判讀標準本身(非程式碼)。**被擋下**:權重非裝飾(等權
IC +0.016 vs 現行 +0.050)、3 日平滑有貢獻(+0.057)、排名日穩定(自相關 0.94)、
遲滯無病態震盪(僅 1 檔卡 ≥5 天)、雜訊死區方向正確(trust 去死區 IC 轉負)、
週規則誤殺率僅 ~6%。**命中並處置**:

- 儀表板 tooltip 寫死的歷史數字全面過期且方向反(蓄勢寫 +8.5%,39 檔重算後
  實為 −0.50%)→ **移除所有寫死歷史數字**,改「以 reports/ 最新週報為準」。
- med_dip「最高者領漲」以非重疊視窗檢驗僅 2/7(≈隨機)→ 對外措辭由「主訊號」
  降級為「候選主訊號(OOS 驗證中)」。
- 蓄勢條件鏈逐層遞減(籌碼+2 單獨 +2.94% → 全條件 −0.01%)、STRONG_MIN 冗餘、
  rs20 單因子濃度(去 price 後 IC −0.034)→ 記入 WEEKLY_REVIEW §4 待 OOS 裁決。

策略規則**零變動**(OOS 紀律);修正全在陳述與監測層。

## Universe 治理上線 + 首次調整 — 2026-07-05

- **治理規則 R1~R4**(業務歸屬 / 市值遲滯 50↔30 億 / 流動性 3,000 萬 / 上市 60 日)
  + 季度節奏 + 提名工具 `scripts/screen.py`(候選清單 `config/candidates.csv`);
  族群定義配置化 `config/groups.csv`(加族群 = 一行 csv,消除五處硬編碼)。
- **剔除**:虹揚-KY 6573(市值 20 億 < 剔除線 30 億)。
- **納入 10 檔**(universe 30 → 39):passive +興勤、鈺邦(→12 檔);
  power +漢磊、嘉晶、捷敏-KY、茂達、致新(→14 檔);
  packtest +同欣電、福懋科、訊芯-KY(→13 檔)。
- **覆核擋下**:4916 事欣科(通過財務規則但業務不符——候選誤植「智寶」,
  智寶已併入凱美)、2437 旺詮(近 220 日無交易資料)。工具+人工覆核各擋一筆,
  治理迴圈第一次跑即生效。
- **⚠ in-sample 統計位移**(全歷史按新 39 檔重算):composite_s 族群內 IC
  +0.145 → +0.090(仍約 v1 同期的 2 倍);med_dip 領漲命中 63% → 41%;
  蓄勢濾網 cohort 反轉(放行 +1.64% vs 擋下 +2.62%)——顯示原數字部分擬合於
  特定 30 檔。**濾網與權重的存廢一律交由 OOS(validate 週報)裁決,不因此
  臨時改規則。**

## v2.1 — 2026-07-05

### 評分重構:絕對門檻 → 族群內排名制(commit 6ba01d1)

- 各元素改在**族群內取分位數排名**給 −2..+2(前 20% = +2、後 20% = −2),
  解決 v1 絕對門檻的個股結構偏誤(日月光永遠拿不到外資 +2、小型股躺著滿分)。
- **關鍵實證發現**:族群內選股力在「價格相對」因子——rs20(20 日報酬 − 族群中位)
  族群內 IC **+0.155**、down_rs20(修正日抗跌)**+0.119**;籌碼因子(外資 pp 變化
  −0.007、逆勢買超 −0.096)在族群內**無**選股力——它們是「族群層」訊號
  (v1 混池 IC +0.07 全部來自「選對族群」;v1 族群內 IC 僅 **−0.009**)。
  → 架構定調:**個股層用價格相對因子選強弱、族群層用籌碼聚合找佈局**。
- 新元素:s_price=rank(rs20) 權重 1.4、s_resil=rank(down_rs20) 權重 1.0;
  籌碼降權(投信 0.8、外資 0.5、融資 0.4、量 0.3、逆勢買超 0 僅供 tier)。
- ⑤融資改「價×融資交互」(價跌融資減=洗盤/價跌融資增=接刀);②量改「量比」
  (相對自身 60 日中位)。
- 蓄勢 tier 加質量濾網(修正日抗跌 ≥0)——v1 無濾網時蓄勢事件平均超額 −0.92%
  (華泰式假佈局);cohort 實證:濾網放行組 10 日超額 +2.43% vs 擋下組 −1.42%。
- 遲滯:綜合分 3 日平滑、tier 連 2 日同向才轉層(日均換層 6.5 → 3.2 檔)。
- **驗證(86 日 in-sample)**:混池 IC +0.068 → **+0.148**;族群內 IC −0.009 →
  **+0.152**;真強-真弱前瞻分離度 2.6pp → **8.0pp**;蓄勢 10 日超額 +8.5%、
  真弱 −2.5%(勝率 38%)。tier 轉移單調:蓄勢→真強 +8.38%、陷阱→真弱 −6.97%。
- v1 最後結果凍結於 `daily_scores_v1` 供對照。

### 族群層 + 大盤 regime(commit 23e611e、c3314f8)

- 新表 `market`/`market_daily`(TAIEX 報酬指數、距 20 日高、修正 regime 旗標)、
  `group_metrics`(佈局廣度、中位距高、rel20、修正日中位淨買 med_dip、
  投信買超廣度、族群狀態)。
- 實證:族群層 **med_dip 最高者領漲命中 63~68%(基準 33%)**= 選族群主訊號;
  修正 regime 下族群內因子 IC 全面升高(抗跌 +0.096→+0.253、rs20 →+0.214、
  投信 →+0.117)→ 現行權重已偏向修正期有效因子,**不做 regime 權重切換**
  (修正樣本僅 21 組,切換即 overfit)。
- regime 用「報酬指數(含息)」是刻意設計:除息季價格指數會機械性下跌,
  含息指數只反映經濟性修正——與個股層用還原價同一邏輯。

### 資料正確性(commit db89dcf、457271b)

- **還原股價**:FinMind 付費 PriceAdj 不可用 → 抓 TaiwanStockDividendResult(免費)
  本地倒推重算 `price_adj`(倒推法,最新區段=原始價);分割/反分割走
  TaiwanStockSplitPrice;減資(付費)以「無事件 >15% 跳空偵測」兜底示警。
- 股本改逐日 forward-fill(消除用最新股本回填歷史的前視);dist 視窗最少樣本
  防護(新增股冷啟動不再假新高);margin_bal 缺值不再 crash;事件異常一律
  stderr 示警不靜默。

### 驗證與監測(commit 24b77db、8ac9738)

- `validate.py` 週度報告(每週六 09:00 自動):元素 IC(族群內/混池 × IS/OOS ×
  修正/多頭)、tier 超額與轉移事件、v1/v2 對照、蓄勢濾網 cohort、族群層命中率。
  **IS/OOS 分界 2026-07-05**;OOS <10 日時報告明示勿調旋鈕。
- 「◇蓄勢候補」:籌碼已吃貨但尚未升蓄勢者,標示差哪些條件(daily_scores.pending)。

### 儀表板(commit 813ca10 ~ 17d2fcb)

- 族群雷達卡片、市場 regime chip、蓄勢候補獨立卡片。
- tooltip 教學化:數據表格 → 判讀 → 評分依據(排名制/門檻/權重的來源說明);
  綜合評級顯示元素×權重分解(權重 import 自 score.py,單一事實來源)。
- 個股主業標示(universe.csv `biz` 欄)。

## v1 — 2026-07-04

- 初版五元素(價/量/外資/投信/融資券)**絕對門檻**評分 + tier
  (真強/蓄勢/強但過熱/潛在/真弱/陷阱)。
- 每日 GitHub Actions 抓取(FinMind,4 datasets × 30 檔)→ SQLite → 評分 →
  儀表板(GitHub Pages)。
- 事後檢討(2026-07-05 方法論 review):混池 IC +0.068 但族群內 IC −0.009
  (預測力全來自選對族群,族群內分不出強弱)、tier 日均換層 7.2/30 檔、
  蓄勢事件超額 −0.92%、絕對門檻有個股結構偏誤 → 促成 v2 重構。
