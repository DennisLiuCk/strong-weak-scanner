# Universe R1 業務歸屬覆核：powersupply 第一批 — 2026-07-17

依據 README「Universe 治理」R1 準則，逐檔核對 `config/candidates.csv` 中
`powersupply` 的 11 檔候選。資料以公司年報、財報、法說簡報與官網產品頁為主；
本報告是**拍板前唯讀覆核**，產出時尚未修改 `groups.csv`、`universe.csv`、
`candidates.csv`、事件 guidance 或質化筆記。

**拍板結果（2026-07-17）**：使用者同意按建議名單執行；10 檔納入
`powersupply`、2420 留候選，並同批納入 3 檔檢測實驗室。

## 判斷口徑

1. **R1 硬門檻仍是現行規則**：主營收逾 50% 屬於族群定義業務。`powersupply`
   在本次提案中指 PSU、電源轉換／管理系統、BBU／電池模組等成品層，與既有
   `power` 的功率半導體元件層分開。
2. **AI／資料中心占比是曝險品質，不另創未經治理的新硬門檻**：公司若只揭露
   「企業用」、「Cloud & AIoT」、「Non-IT」或「雲端及邊緣運算」，均不可直接
   當成 AI／資料中心電源營收。
3. **「未揭露」不等於零**：有量產產品但沒有營收拆分者，明列為未量化；只有
   研發／積極切入敘述者，再降一級標示。
4. **跨域一檔一群**：台達電同時有電源、資料中心基礎設施與液冷；若納入，依
   主要投資敘事與官方最大營運段歸 `powersupply`，不重複放入 `thermal`。

## 摘要與建議

- **建議納入 10 檔**：2308 台達電、2301 光寶科、6412 群電、6282 康舒、
  3078 僑威、3015 全漢、3211 順達、6781 AES-KY、2457 飛宏、8109 博大。
- **建議保留候選 1 檔**：2420 新巨。2025 年 PSU 僅 46.88%，2026Q1 亦僅
  46.02%，未過現行 R1；微動開關才是過半主業，且不等同既有 `power` 的功率
  半導體元件。
- **需使用者明示接受的人工判定**：2308 台達電。最新 Power Electronics 段占
  54%，但該段混合電源、零組件與風扇／散熱，沒有「純電源」拆分；本報告基於
  grid-to-chip 電源與資料中心基礎設施的主要敘事，建議通過並歸 `powersupply`。
- **AI 純度最低但 R1 仍合格**：2457 飛宏與 8109 博大。飛宏的「車充為主」前提
  經一手資料推翻（2026Q1 PSU 68.3%、EV 31.7%），但資料中心仍只有切入敘述；
  博大電源占 98.34%，最新年報卻未提資料中心／伺服器。兩者納入理由是現行 R1
  的「電源主業過半」，不是宣稱它們已有高 AI 營收。
- 按建議名單加上已定案併入 `semiequip` 的 3587／3289／6830，共新增 13 檔：
  **98 → 111 檔**；沿用交接的日常粗估基準，本批固定新增 13×5 個核心個股
  datasets，使約 **593 → 658（約 650）**；事件 coverage 依缺口發生，連同
  指數／交易所備援另計。

| 股號 | 公司 | R1 主業證據（最新可得） | AI／資料中心電源證據 | R1 建議 |
|---|---|---|---|---|
| 2308 | 台達電 | 2026Q1 Power Electronics 54%，但混合電源、零組件、風扇與熱管理 | AI 電源、800VDC／±400VDC、rack power 與液冷均已量產／展示；精確占比未揭露 | **人工判定納入**，歸 powersupply |
| 2301 | 光寶科 | 2025 Cloud & AIoT 45% + ITCE 38%；年報稱兩段多數產品為電源 | AI 相關業務已逾 20%；2026 約 30% 是公司目標，非已實現全年數 | **納入** |
| 6412 | 群電 | 2025 電子零組件產品 81.09%，產品清單與產業定位以各式 PSU 為核心 | 已有 500–5500W AI／cloud server PSU；占比未揭露 | **納入** |
| 6282 | 康舒 | 2025 電源 93.92%；1Q26 電源 93.14% | 「企業用電源」占總營收 2025 37.7%、1Q26 42.4%，但內含多種非 AI 應用，只能當上限代理 | **納入** |
| 3078 | 僑威 | 2025 Desk PC PSU 81.19% + 其他電源 18.01% = 99.20% | 已有 CRPS、Edge AI server／workstation、BBU 產品；占比未揭露，現有營收仍以桌機 PSU 為主 | **納入** |
| 3015 | 全漢 | 2025 電源供應器、外接式電源、基板電源合計 92.27% | 雲端及邊緣運算占 2025 7%、1Q26 10%；此分類不等同純 AI／資料中心 | **納入** |
| 3211 | 順達 | 2025 鋰電池組 99.8% | 已有伺服器 UPS／資料中心電池組；2026 Non-IT 預估逾 50% 但混合 BBU、LEV、儲能，BBU 單項未拆 | **納入** |
| 6781 | AES-KY | 2025 鋰電池模組 99.7% | 年報稱資料中心備援已帶來效益，但仍稱目前銷售主要為輕型電動載具；精確占比未揭露 | **納入** |
| 2420 | 新巨 | 2025 微動開關 53.12%、PSU 46.88%；1Q26 PSU 46.02% | 有 AI server 54V／資料中心冗餘電源開發項目；占比未揭露 | **保留候選（R1 未過）** |
| 2457 | 飛宏 | 1Q26 PSU 68.3%、EV 31.7%；2025 PSU 66.72% | PoE／數位電源平台為「積極切入」資料中心／網路交換器，未見量產占比 | **納入，但標低 AI 純度** |
| 8109 | 博大 | 2025 電源供應器 98.34% | 最新年報聚焦工業、鐵道、醫療、通訊、國防；未提資料中心／伺服器，AI 占比未揭露 | **納入，但標低 AI 純度** |

---

## 一、跨域與多角化候選

### 2308 台達電 — 建議人工判定通過，歸 powersupply

- 2025 合併營收 5,548.85 億元；Power Electronics 50%、Infrastructure 33%、
  Automation 10%、Mobility 7%。2026Q1 Power Electronics 為 856.23 億元、占
  54%，是最大營運段。
- 限制是 Power Electronics 定義同時含 components、power supplies and systems、
  fan & thermal management；公司沒有拆出純 PSU／電源系統營收，因此無法用單一
  公開數字嚴格證明「純電源 >50%」。另一方面 Infrastructure 也含 UPS、HVDC 與
  AI data-center integration，故只看單一段亦會漏計電源業務。
- 公司已明列 AI server power、AC/DC、DC/DC、power module、90kW DC/DC rack、
  1.1MW in-row power rack，並把液冷與電源整合成 grid-to-chip 方案。就一檔一群而言，
  其 AI 投資敘事由供電架構主導、冷卻為整合配套，建議歸 `powersupply`。
- 判定：**接受複合分部的人工判斷則納入；不建議歸 thermal，也不重複收錄。**

來源：

- [台達電 2025 Annual Report](https://filecenter.deltaww.com/IR/download/annual_report/2025annual.pdf)，PDF pp.139–141（年報頁 135–137）
- [台達電 1Q26 Analyst Meeting](https://filecenter.deltaww.com/ir/download/calendar/1Q26_Analyst%20Meeting.pdf)，PDF p.6
- [台達電 2026 AGM Minutes](https://filecenter.deltaww.com/ir/download/calendar/20260528_chi_Minutes%20of%202026%20AGM.pdf)，PDF pp.6–7

### 2301 光寶科 — 建議納入

- 2025 營收組合為 Cloud & AIoT 45%、IT & Consumer Electronics 38%、
  Opto-electronics 17%；年報明述 Cloud 與 ITCE 的多數產品為 power supply。
  最新 2026Q1 Cloud & AIoT 52.8%、ITCE 30.6%、Opto 16.6%。雖未拆純 PSU，
  兩個以電源為主的營運段合計 83%，足以作 R1 高信心人工判定。
- 公司在 2026 股東會稱 AI-related businesses 已逾總營收 20%；2026 全年約 30%
  是公司目標。Cloud & AIoT 不能直接當純 AI 占比，30% 也不能當已實現數。
- 高階伺服器 PSU、BBU、Power Shelf、HVDC、800VDC power rack 已是主要成長敘事；
  液冷是電能基建配套，不改變族群歸屬。

來源：

- [光寶科 2025 Annual Report](https://www.liteon.com/upload/media/ir/annual/2025%20LITEON%20Anual%20Report.pdf)，PDF pp.112–113（年報頁 107–108）
- [光寶科 2026Q1 Consolidated Financial Statements](https://www.liteon.com/upload/media/%E5%85%89%E5%AF%B6%E8%8B%B1%E6%96%87%E5%90%88%E4%BD%B5%E8%B2%A1%E5%A0%B12026Q1.pdf)，PDF p.57
- [光寶科 2026 AGM](https://www.liteon.com/en/news/press-center/content/annual-general-meeting-2026)

### 6412 群電 — 建議納入

- 2025 電子零組件產品占 81.09%、消費／其他電子產品 12.36%、智慧建築 6.11%、
  其他 0.44%。81.09% 大類不是純 AI 電源，但年報把公司主要產品定位為各式
  switching power supplies，產品清單也以 PSU 為核心，足以判定電源主業過半。
- 已列出 500–5500W cloud／AI edge server power、OCP／MHS-CRPS 與 AI／資料中心
  N+M redundant systems；未揭露這些產品的營收占比。

來源：

- [群電 2025 Annual Report](https://www.chiconypower.com/uploads/investor/financial%20report/Year/2025/CP-2025-Annual%20Report-en.pdf)，PDF pp.67、69、85–86
- [群電 2026Q1 Results](https://www.chiconypower.com/en/post/view?post_id=113)

## 二、PSU／電源系統候選

### 6282 康舒 — 建議納入

- 2025 總營收 317.27 億元，電源供應器 298.00 億元，占 93.92%；1Q26 電源
  79.92 億元、占總營收 93.14%。電源解決方案是絕對主業。
- 2025「企業用電源」119.66 億元，占總營收 37.7%；1Q26 為 36.40 億元、占
  42.4%。該分類雖含伺服器、資料中心、儲存與超級運算，也含燃料電池、網通、
  POS、工作站、智慧電網及醫療，故只能視為 AI／資料中心占比的上限代理。

來源：

- [康舒 June 2026 法說](https://mopsov.twse.com.tw/nas/STR/628220260608M001.pdf)，PDF pp.7–8
- [康舒 2025 年報（TWSE）](https://doc.twse.com.tw/server-java/t57sb01?co_id=6282&colorchg=1&filename=2025_6282_20260528F04.pdf&kind=F&step=9)

### 3078 僑威 — 建議納入

- 2025 Desk PC Power 81.19%、其他類電源 18.01%、其他原料半成品 0.80%；
  電源合計 99.20%。公司是 OEM／ODM 客製電源商，桌機 PSU 仍是核心。
- 官網已有 CRPS（data center／data storage／Edge AI server）、Edge AI workstation
  電源與 BBU；尚未揭露營收占比，不能把新產品頁推論成已具實質 AI 營收。

來源：

- [僑威 2025 年報（TWSE）](https://doc.twse.com.tw/server-java/t57sb01?co_id=3078&colorchg=1&filename=2025_3078_20260624F04.pdf&kind=F&step=9)
- [僑威 2025-05-21 法說](https://www.cwt.com.tw/uploads/images/finance/2025/20250521V.pdf)，PDF pp.4–6、12
- [僑威 AI Power Solutions](https://www.cwt.com.tw/tw/product/info/ai-power-solutions)

### 3015 全漢 — 建議納入

- 2025 電源供應器 59.75%、外接式電源 22.92%、基板電源 9.60%，三項合計
  92.27%；若加逆變器則 92.33%。
- 2025 雲端及邊緣運算占 7%，1Q26 升至 10%；該應用別不是純 AI／資料中心，
  但公司已明列 AI／Edge server、redundant PSU，並研發 3.6–6kW CRPS。

來源：

- [全漢 2025 年報](https://www.fsp-group.com/download/260624-6A3B741FBED23.pdf)，PDF pp.89、100–101、113
- [全漢 2026-06-25 法說](https://www.fsp-group.com/download/260624-6A3B6C8828EE5.pdf)，PDF p.9
- [全漢致股東報告](https://www.fsp-group.com/tw/ChairmanStatement.html)

## 三、BBU／電池模組候選

### 3211 順達 — 建議納入

- 2025 鋰電池組占 99.8%，其他 0.2%；商業模式是按客戶需求選電芯、搭配 BMS
  與機構設計後組裝電池模組，屬產品型 BBU／電池模組供應商。
- 年報明列伺服器不斷電系統與資料中心用電池組，並稱 BBU 出貨及營收占比增加。
  2026 Non-IT 預估逾 50%，但 Non-IT 同時含 BBU、LEV 與儲能，不可當 BBU 或
  AI／資料中心精確占比。

來源：

- [順達 2025 年報](https://m3.hocom.tw/Uploads/userfiles/files/i5egzpitiqarvb6.pdf)，PDF pp.5–6、60、62
- [順達 2026Q1 法說](https://mopsov.twse.com.tw/nas/STR/321120260304M001.pdf)，PDF p.8
- [順達官方產品頁](https://www.dynapack.com.tw/h/Data?cat=2877&key=iiqgi&set=9)

### 6781 AES-KY — 建議納入

- 2025 鋰電池模組占 99.7%，其他 0.3%；公司依客戶需求共同開發、客製設計、
  試作／測試／認證後量產，屬產品型電池模組供應商。
- 年報稱 2025 成長主要來自中大型工業備援系統與工控電池模組，資料中心備援已
  帶來營運效益；但另一處仍稱目前銷售主要為輕型電動載具，故不能自行推算
  BBU／資料中心比重。市場轉述的 BBU 約 70% 未出現在官方 deck／年報，不採用。

來源：

- [AES-KY 2025 年報（TWSE）](https://doc.twse.com.tw/server-java/t57sb01?co_id=6781&colorchg=1&filename=2025_6781_20260528F04.pdf&kind=F&step=9)，PDF pp.6、8、58–59
- [AES-KY 官方產品／商業模式](https://www.advancedenergysolution.com.tw/article.php?lang=tw&tb=2)
- [AES-KY 2025-11 法說](https://mopsov.twse.com.tw/nas/STR/678120251114M001.pdf)

## 四、三檔爭議候選

### 2420 新巨 — 建議保留候選，不進第一批

- 2025 微動開關 11.572 億元、占 53.12%；交換式電源供應器 10.213 億元、占
  46.88%。2026Q1 再確認微動開關 53.98%、PSU 46.02%；2024Q1–2026Q1 每季
  PSU 約 43.05%–48.84%，均未過半。
- 公司已有資料中心／高速運算冗餘 PSU 與 AI server 54V PSU 開發項目，但 R1 看
  現有主營收，不以研發題材補足未過半的產品占比。
- 微動開關屬機電開關，不是既有 `power` 的 MOSFET／二極體／power IC；若未來
  PSU 過半，歸 `powersupply` 仍比 `power` 合理。

來源：

- [新巨 2025 年報](https://www.zippy.com/upload/20260624/0001_2025_2420_20260520F04_114%E5%B9%B4%E5%A0%B1.pdf)，PDF pp.54–55、62–63
- [新巨 2026Q1 法說](https://mopsov.twse.com.tw/nas/STR/242020260507M001.pdf)，PDF p.6

### 2457 飛宏 — 建議納入，但明列 AI 證據不足

- 2025 產品營收為 PSU 65.3526 億元、占 66.72%；EV energy 32.5330 億元、占
  33.21%。2026Q1 法說再顯示 PSU 68.3%、EV 31.7%，因此「車用充電為主」的
  原始疑慮不成立，電源產品已明確過 R1。
- 公司完成 PoE 100–950W 與 350–2000W digital power platform，表述為「積極切入」
  資料中心／network switch。未見量產營收或占比，故不得標成 AI 電源高純度。
- 現行 R1 沒有另設 AI 占比門檻；依既有規則建議納入。若治理者要新增「已量產
  AI／資料中心」硬門檻，應另行修 README 並對 11 檔一致適用，不能只對飛宏加碼。

來源：

- [飛宏 2025 年報](https://www.phihongtech.com/wp-content/uploads/2026/06/114%E5%B9%B4%E5%A0%B1-_2026.05.18_FINAL%E4%B8%8A%E5%82%B3%E7%89%88.pdf)，PDF pp.106、117–120
- [飛宏 2026Q1 法說](https://www.phihongtech.com/wp-content/uploads/2026/06/2026%E5%B9%B4Q1%E6%B3%95%E8%AA%AA%E6%9C%83%E5%A0%B1%E5%91%8A_20260609_%E4%B8%AD%E6%96%87.pdf)，PDF p.7

### 8109 博大 — 建議納入，但明列非 AI 純曝險

- 2025 合併營收 17.426 億元，電源供應器占 98.34%；主業判定無歧義。
- 產品聚焦高階工業、通訊、鐵道／運輸、醫療、國防與儲能。最新年報全文未見
  「資料中心」或「伺服器」，沒有 AI／資料中心營收證據。
- 依現行 R1，工業電源同業仍可進 `powersupply` 做族群內強弱比較；biz 應寫
  「工業電源／DC-DC」，不可寫成 AI 資料中心電源。

來源：

- [博大 2025 年報](https://www.pduke.com/Upload/download/shareholder/shareholder_meeting_report/shareholder_meeting_114_.pdf)，PDF pp.4–7、98
- [博大官網產品／應用](https://www.pduke.com/tc/investor10_9_0_0.htm)

---

## 拍板採用名單

使用者已於 2026-07-17 同意按下列建議名單執行 config／回補／筆記階段：

- `powersupply` 納入：`2308,2301,6412,6282,3078,3015,3211,6781,2457,8109`
- `powersupply` 保留候選：`2420`
- 同批依既定決策併入 `semiequip`：`3587,3289,6830`

本次拍板包含下列兩項裁量：

1. 接受 2308 以「複合 Power Electronics／Infrastructure + 一檔一群」人工判定
   通過，歸 `powersupply`。
2. 維持現行 R1，因此納入低 AI 純度但電源主業明確的 2457／8109；沒有另加
   「已量產 AI／資料中心」硬門檻。
