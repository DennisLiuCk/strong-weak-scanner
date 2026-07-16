# Universe R1 業務歸屬覆核：serverodm 第二批 — 2026-07-17

依據 README「Universe 治理」R1 準則，逐檔核對 `config/candidates.csv` 中
`serverodm` 的 14 檔候選。資料以公司年報、財報、法說簡報與公司官網為主；
R2／R3／R4 結果沿用 `reports/screen_2026-07-17.md`，不重跑全量 API 體檢。

**執行結果（2026-07-17）**：使用者要求接續執行第二批，並沿用「按建議名單
執行」授權。10 檔納入 `serverodm`；2317、4938、2377、6117 留在候選池並記錄
理由。第三批 `optnet` 仍依原提案留到 2026-10 季度治理窗口。

## 判斷口徑

1. **R1 沿用主營收逾 50% 原則**：本群定義為 AI／雲端資料中心伺服器 ODM、
   整機櫃與其機構件（伺服器／儲存機殼、導軌）。對整機廠看 server-related／
   cloud product；對機構件廠看群組所定義的機殼／導軌產品收入。
2. **AI-only 占比不是新增硬門檻**：公司只揭露 server、cloud、data-center product
   或機構件大類時，不自行把整個大類改稱 AI 營收；AI 純度與 R1 主業判定分開。
3. **區間與複合分部保留推論界線**：3231、2356 沒有可直接重算的單一 server
   年度占比，採治理人工判定並明列證據限制；不把中點估計寫成公司正式揭露。
4. **投控看合併營運實質**：3706 雖為投控，合併 cloud product 已近九成，且官方
   定義明確涵蓋伺服器與整機櫃，故不因法律型態排除。
5. **固定決策不重開**：2317、4938 依提案既定結論不納；6117 已在 R3 因流動性
   落榜，不補做 R1。2377 則由本輪官方產品組合覆核後判定 R1 不足。

## 摘要與建議

- **納入 10 檔**：2382 廣達、3231 緯創、6669 緯穎、2356 英業達、2376 技嘉、
  3706 神達、8210 勤誠、3693 營邦、2059 川湖、3013 晟銘電。
- **保留候選 4 檔**：2317 鴻海、4938 和碩、2377 微星、6117 迎廣。
- **人工判定 2 檔**：3231 緯創的官方分部未拆 server，但 2025 營收翻倍且 AI／
  一般伺服器皆三位數成長、被公司列為主要驅動；2356 英業達依官方季度區間
  加權，2025 server-related 合理範圍為 49.86%–53.86%、中點 51.86%。兩檔均
  納入，但不得宣稱公司已用精確分部數字證明逾 50%。
- **低 AI 可見度 1 檔**：2059 川湖的導軌占 97.87%，足以通過機構件產品層 R1；
  官方同時列出伺服器、交換器、儲存、UPS、KVM、POS 等用途，沒有拆伺服器或
  AI 終端占比，因此 biz 明列限制。
- 本批使正式 Universe 由 **10 群 111 檔 → 11 群 121 檔**；固定核心個股資料集
  以每檔約 5 requests 粗估，日常約 **658 → 708（約 710）**，事件 coverage、
  指數與交易所備援另計。

| 股號 | 公司 | R1 主業證據（最新可得） | AI／資料中心證據與限制 | R1 結論 |
|---|---|---|---|---|
| 2382 | 廣達 | 官方 2024 永續報告稱全年伺服器營收占比首次突破 50% | AI-only 未拆；2025 營收大增不另反推占比 | **納入** |
| 3231 | 緯創 | 2025 營收 2.1865 兆元、年增 108%；AI 與一般伺服器均三位數成長且為主要驅動 | 3C 98.5% 仍混合 NB 等產品，未直接拆 server | **人工判定納入** |
| 6669 | 緯穎 | 2025 data-center product 9506.63 億元、占 100% | AI／一般伺服器未再拆 | **納入** |
| 2356 | 英業達 | 2025 各季 server-related 為 46–50%、51–55%、51–55%、51–55%；全年加權 49.86%–53.86% | 中點 51.86% 是依官方區間計算，不是公司正式占比 | **人工判定納入** |
| 2317 | 鴻海 | 2025 Cloud & Networking 40%，其餘 Smart Consumer 38%、Computing 15%、Components & Other 7% | 雲網亦含 networking，非純 server；1Q26 也僅稱 nearly 50% | **保留候選（既定不納）** |
| 4938 | 和碩 | 4Q25 Computing 15%，且該類同時含 notebook、desktop、server | AI server 有研發／產品布局，營收未拆 | **保留候選（既定不納）** |
| 2376 | 技嘉 | 2026Q1 server 71.5%；2025Q1 已為 55% | AI server 年增 110%，但 AI-only 占比未拆 | **納入** |
| 2377 | 微星 | 2025 Component 50%、System 42%、Others 8%；server 只是 System 子集 | 伺服器／資料中心是成長業務，無過半收入證據 | **保留候選（R1 不足）** |
| 3706 | 神達 | 2025 cloud product 89.24%；2026Q1 90.09% | 官方定義含通用／客製／AI／GPU server 與整機櫃；AI-only 未拆 | **納入** |
| 8210 | 勤誠 | Server/Storage 占 2025 99%、2026Q1 99.6% | AI 專屬占比未拆 | **納入** |
| 3693 | 營邦 | 2024 伺服器機箱 36.09% + 系統平台 29.39% + 儲存系統 3.19% = 68.67% | 最新成長敘事未量化 AI-only 占比 | **納入** |
| 2059 | 川湖 | 2025 導軌 97.87%、滑軌 0.03%、鉸鏈 0.89%、其他 1.21% | 導軌終端多元，伺服器／AI 占比未揭露 | **納入，標示終端限制** |
| 3013 | 晟銘電 | 2025 前 9 月 SVR 41% + AI SVR 47% = 88% | AI SVR 可辨識為 47%；液冷 7% 另列，不重複加總 | **納入** |
| 6117 | 迎廣 | 未進 R1 | 20 日中位成交值 18M，低於 30M | **R3 不納** |

---

## 一、伺服器 ODM／系統廠

### 2382 廣達 — 納入

- 官方 2024 永續報告董事長訊息明載，全年伺服器業務營收占比首次突破 50%；
  這是直接跨過 R1 的公司層級證據，不以市場估值或媒體供應鏈推測替代。
- 公司沒有另拆 AI-only 占比；2025 合併營收由 1.4108 兆元升至 2.1237 兆元，
  可支持業務規模持續擴張，但本報告不把增量全數歸因 AI server。

來源：

- [廣達 2024 永續報告－董事長的話](https://www.quantatw.com/Quanta/chinese/esg/ESG2024/ch00-2.html)
- [廣達 2025 年報頁面](https://www.quantatw.com/quanta/english/investment/annualreports.aspx)

### 3231 緯創 — 人工判定納入

- 2025 合併營收 2.1865 兆元、年增 108%；官方稱 AI server 與 general-purpose
  server 營收均為三位數百分比成長，且為營運規模與獲利擴張的主要驅動。PC
  出貨僅小幅成長、monitor 持平，手機業務已退出。
- 限制是年報產品營收只揭露 3C 電子產品 98.5%，內含 server、NB、desktop 等；
  所以本結論是「公司重心與營收增量由 server 主導」的治理人工判斷，不是已由
  分部表數學證成 server >50%。

來源：

- [緯創 2025 Annual Report](https://www.wistron.com/file/9ecdf53a-9c8a-4df8-aeed-7568724eb956/2025_WistronAnnualReport_EN.pdf)，PDF pp.2–3

### 6669 緯穎 — 納入

- 2025 年報「Percentage of business revenue」將 data-center product 列為
  9506.63 億元、占營收 100%；2024 同樣為 100%，R1 無歧義。
- data-center product 仍涵蓋不同伺服器／機櫃平台；AI-only、GPU-only 或單一 CSP
  占比不能由 100% 大類直接推得。

來源：

- [緯穎 2025 Annual Report](https://www.wiwynn.com/hubfs/Investors/Shareholders_Services/2026_Annual_Report_EN.pdf)，PDF p.126

### 2356 英業達 — 人工判定納入

- 官方 2026Q1 法說揭露 server-related 營收占比：2025Q1 為 46–50%，Q2、Q3、
  Q4 各 51–55%，2026Q1 又為 46–50%。配合同頁季度營收 1570、1866、1763、
  1713 億元加權，2025 年合理範圍為 49.86%–53.86%，中點 51.86%。
- 因區間下限略低於 50%，不能寫成「官方精確揭露 51.86%」；本批基於三季連續
  站上 51–55%、全年中點過半，以及年報明列 CSP／Neocloud server 與整機櫃組裝，
  採臨界人工判定納入。

來源：

- [英業達 2026Q1 法說簡報](https://www.inventec.com/Upload/202605/investor_2026051216121203.pdf)，PDF p.4
- [英業達 2025 年報](https://www.inventec.com/Upload/202605/investor_2026051911135103.pdf)，PDF pp.4–5

### 2376 技嘉 — 納入

- 2026Q1 官方產品組合為 server 71.5%、VGA 19.0%、MB 6.5%、Others 3.0%；
  2025Q1 server 已達 55%，伺服器已是合併主業而非板卡旁支。
- 同份簡報稱 AI server 年增 110%，並列 GB300 NVL72 rack-scale、液冷 GPU
  server 與 GIGAPOD；AI-only 營收仍未拆，不把 server 71.5% 全稱 AI。

來源：

- [技嘉 2026Q1 Investor Conference](https://www.gigabyte.com/FileUpload/TW/SiteMap/83/images/2026Q1-0515.en.pdf)，PDF pp.7、10、14–16

### 3706 神達 — 納入

- 2025 cloud computing products 外部收入 942.18 億元／合計 1055.77 億元，
  占 89.24%；2026Q1 為 287.08／318.64 億元，占 90.09%。
- 年報對該產品的定義含 general/custom servers、AI/GPU servers、storage、
  network/server equipment 與 rack-level systems。雖是投控，合併營運實質高度
  集中，符合 R1；AI-only 仍未拆。

來源：

- [神達 2025 合併財報](https://www.mitac.com/zh-TW/quarterly_statement/download/245/%E7%A5%9E%E9%81%94%E6%8E%A7%E8%82%A1%E5%90%88%E4%BD%B5%E8%B2%A1%E5%A0%B1%202025)，PDF p.68
- [神達 2026Q1 合併財報](https://www.mitac.com/zh-TW/quarterly_statement/download/252/%E7%A5%9E%E9%81%94%E6%8E%A7%E8%82%A1%E5%90%88%E4%BD%B5%E8%B2%A1%E5%A0%B1%202026%20Q1)，PDF p.52
- [神達 2025 年報](https://www.mitac.com/zh-TW/annual_report/download/50/2025%E5%B9%B4%20%E7%A5%9E%E9%81%94%E6%8E%A7%E8%82%A1%E5%B9%B4%E5%A0%B1%20-2026/5/8%E4%B8%8A%E5%82%B3)，PDF pp.61、65、67

## 二、伺服器機構件

### 8210 勤誠 — 納入

- 官方 2026Q1 法說的產品別結構顯示 Server/Storage 在 2023、2024、2025 均占
  99%，2026Q1 再升至 99.6%，PC 僅 0.4%；機殼主業跨過 R1 無歧義。
- Server/Storage 大類不等同 AI-only，故不自行估算 AI 機殼營收。

來源：

- [勤誠 2026Q1 法說](https://mopsov.twse.com.tw/nas/STR/821020260508M001.pdf)，PDF p.4

### 3693 營邦 — 納入

- 官方 2024 年報產品結構為伺服器機箱 36.09%、系統平台 29.39%、儲存系統
  3.19%、產業設備 0.34%、其他 30.99%；保守只加前三類即 68.67%。
- 這能證明伺服器／儲存機構與系統為主業，但不能把 68.67% 全稱 AI 或 CSP。

來源：

- [營邦官方年報](https://www.aicipc.com/image/images/%E5%B9%B4%E5%A0%B1.pdf)，PDF p.45

### 2059 川湖 — 納入，但標示終端限制

- 2025 產品結構為導軌 97.87%、滑軌 0.03%、鉸鏈 0.89%、其他 1.21%；依本群
  明定包含導軌，產品層 R1 明確通過。
- 同份法說列舉伺服器、交換器、儲存、UPS、KVM、POS、ATM 與影印機等應用，
  未拆伺服器終端收入；因此 97.87% 只能稱導軌占比，不能改寫成 AI server 占比。

來源：

- [川湖 2026Q1 法說](https://mopsov.twse.com.tw/nas/STR/205920260224M001.pdf)，PDF pp.5、7

### 3013 晟銘電 — 納入

- 2025 前 9 月產品組合為 SVR 41%、AI SVR 47%、Liquid Cooling 7%、DT 3%、
  Tooling 2%；SVR 與 AI SVR 合計 88%。2024 兩類合計亦達 93%。
- AI SVR 47% 是公司可辨識的產品占比；Liquid Cooling 另列 7%，本報告不把它
  再併入 AI 而造成重複或過度歸因。

來源：

- [晟銘電 2025-11-13 法說](https://mopsov.twse.com.tw/nas/STR/301320251113M001.pdf)，PDF p.6

## 三、保留候選

### 2317 鴻海 — 依既定決策不納

- 2025 產品營收組合為 Cloud & Networking 40%、Smart Consumer 38%、
  Computing 15%、Components & Other 7%。雲端網路雖為最大類，仍低於 50%，
  且同時含 networking；1Q26 公司也僅稱 Cloud & Networking 接近 50%。
- 因高度多角化與分部純度限制，維持提案的既定不納結論。

來源：

- [鴻海 2026 股東會議事手冊（英文）](https://image.honhai.com/upload/202604/global/115%E5%B9%B4%E8%AD%B0%E4%BA%8B%E6%89%8B%E5%86%8A_EN0428%E7%89%88%28%E5%90%AB%E5%B0%81%E9%9D%A2%E5%B0%81%E5%BA%95%29%282%29-%E4%B8%8A%E5%82%B3_20260429_6630.pdf)，PDF p.18
- [鴻海 2026Q1 官方新聞稿](https://www.honhai.com/en-us/press-center/press-releases/latest-news/2018)

### 4938 和碩 — 依既定決策不納

- 4Q25 營收組合為 Computing 15%、Consumer Electronics 7%、Communication
  62%、Others 16%；年報又說 Computing 同時含 notebook、desktop 與 server，
  因此 server 只是 15% 大類的子集。
- 公司已有 NVL72／AI server 研發與產品布局，但營收占比未揭露，不能以產品存在
  取代 R1 主業證據。

來源：

- [和碩 2025Q4 Business Review](https://www.pegatroncorp.com/media/20260311055630864_2025%20Q4%20Business%20Review.pdf)，PDF pp.10–11
- [和碩 2025 Annual Report](https://www.pegatroncorp.com/media/20260508074846949_2025_Annual_Report_Eng.pdf)，PDF pp.130、149–150、153

### 2377 微星 — R1 不足，保留候選

- 2025 產品組合為 Component 50%、System 42%、Others 8%；System 亦含 PC、
  notebook、display 等，server 並未獨立揭露，理論上限也不超過 42%。
- 年報把 RTX50 顯卡、主機板、AI PC／筆電／顯示器列為主力，server、IPC、車電
  則是另列成長業務；因此沒有足夠證據通過 serverodm >50% R1。

來源：

- [微星 2026 Investor Conference（FY2025）](https://storage-asset.msi.com/file/pdf/2026-MSI_Investor_TC.pdf)，PDF p.6
- [微星 2025 Annual Report](https://storage-asset.msi.com/file/pdf/investor/book/2025-annual-report.pdf)，PDF p.71

### 6117 迎廣 — R3 不納

- `reports/screen_2026-07-17.md` 顯示 20 日中位成交值 18M，低於 30M 門檻；
  已在 R3 落榜，依交接決策不再補做 R1 或回補。

---

## 採用名單與裁量紀錄

本次依使用者 2026-07-17「接續執行第二批 serverodm」指示，採用：

- 納入：`2382,3231,6669,2356,2376,3706,8210,3693,2059,3013`
- 保留候選：`2317,4938,2377,6117`

裁量僅限 R1 業務歸屬：接受 3231 的營運重心證據與 2356 的官方區間加權作人工
判定；沒有修改評分權重、tier 條件、市值／流動性門檻或 `validate.py` 的
`IS_CUTOFF`。新族群 OOS 自納入後第一個正式日快照起算，至少累積 8 週再具裁決力。
