# 研究資料與更新時鐘稽核（2026-07-27）

## 結論

目前最急的不是全面重寫 121 篇，而是三件事：

1. 完成 `3289 宜特`、`3587 閎康`、`6830 汎銓` 的 focused evidence pack 與獨立複核；
   三篇雖未到 `next_review`，仍是 `ai_draft`，品質優先於日期。
2. 將 8 月複核懸崖改由外部研究佇列管理。81 篇正式筆記在未來 30 日內到期，其中 65 篇
   集中於 8/20–8/21；196 則回溯 H# 又集中於 8/20、8/21、8/31。不能等到日期當天才開始。
3. 建立可證明「有掃過／沒掃過」的市場議題紀錄。本次以前沒有 scan log，因此不能把
   7/19–7/27 的 0 次檔案更新解讀成「市場沒有新事」。

本次沒有修改正式個股筆記或任何 H# 的生命週期／證據強度。唯一直接過時的是技嘉小作文
把 5/15 公司法說的「Rubin early-stage」寫成未加日期的現在式；已改回歷史切面並收窄
下一驗證節點。其餘新議題只觸發複核，不足以證明個股新增訂單、營收或毛利；正式筆記
仍須沿用 evidence pack 與獨立簽核契約。

## 普查範圍與執行環境

- Windows NT 10.0.26200.0、python.org CPython 3.12.10、台灣研究日 2026-07-27。
- 起始前已 `git pull`；稽核基準 commit `5a9a7b95`。
- 正式 DB 全程以 `scripts/db_ro.connect()`、`PRAGMA query_only=1` 讀取；只有最後明確的
  4 筆官方月營收修補使用 `fetch_financials.py` 寫入。
- 下列計數為 universe 全體或檔案全集普查，不是抽樣；SE 不適用。市場事件掃描則是
  `partial`，不能外推成完整母體涵蓋。

## 正式質化筆記

| 項目 | 結果 |
|---|---:|
| universe／已有筆記 | 121／121 |
| `independently_verified` | 118 |
| `ai_draft` | 3 |
| 截至 7/27 已逾期 | 0 |
| 7 日內到期 | 0 |
| 30 日內到期 | 81 |
| 8/20–8/21 到期 | 65 |
| focused_v1 | 64（61 verified、3 draft） |
| 既有未標 profile v2 | 57（全 verified） |
| evidence manifest | 61；無 orphan、路徑或 SHA 不一致 |

最近一篇正式筆記／manifest 更新在 7/18；7/20 後沒有相關 commit。最早的固定複核 cohort：

- 8/10：2337 旺宏、2441 超豐、3035 智原、6510 精測。
- 8/15：2327 國巨、2383 台光電、3324 雙鴻、3443 創意、3529 力旺、3711 日月光投控、
  4966 譜瑞-KY、6239 力成、6643 M31。

`6182 合晶`、`6223 旺矽` 的 `latest_financial_period` 仍寫 FY2025，但 DB 已有 2026Q1，
應提前做文件 delta review；這是內容期別提示，不代表直接改 meta 即完成複核。

## 財務資料

初始稽核發現 2026 年 6 月月營收只覆蓋 117/121，缺 3016、3661、3680、3707。官方當期
OpenAPI 均已有資料，因此判定為同步／排程缺口，不是公司尚未公告：

| 股票 | 2026-06 營收（千元） | MoM | YoY |
|---|---:|---:|---:|
| 3016 嘉晶 | 448,219 | +3.33% | +41.17% |
| 3661 世芯-KY | 3,572,404 | +84.61% | +15.39% |
| 3680 家登 | 752,110 | +10.98% | +37.93% |
| 3707 漢磊 | 620,211 | +5.06% | +29.86% |

已由 [TWSE 上市公司月營收 OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap05_L) 與
[TPEx 上櫃公司月營收 OpenAPI](https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap05_O)
補入正式 DB；以唯讀查詢重算後為 121/121、缺口 0。

三張季報表 `financials`、`balance_sheet`、`cash_flow` 都是 121/121，最新 2026Q1。
截至 7/26，[TWSE 最新季財報端點](https://openapi.twse.com.tw/v1/opendata/t187ap06_L_ci) 與
[TPEx 最新季財報端點](https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap06_O_ci)
仍只到民國 115 年第 1 季，因此現在不應把「尚無 Q2」判為缺檔；既定 Q2 全抓在 8/17。
佇列的應有季度由法定申報截止日推導後再查 121 檔，不使用全 DB `MAX(date)`；這可避免
整批落後仍顯示完整，也避免 2330 或單一早報者先出新季時把其餘 universe 誤判為缺口。

根因是月營收 workflow 只在 7/12 跑一次；四檔當次各取到 35 個月而非 36 個月，空回應
沒有 coverage gate，工作仍為綠燈。修正後每月 12 日有官方 fallback；每月 17 日重驗，
非季報月定向重抓、季報月由全抓順帶，兩者都要求完整，仍缺就標紅。

## 領先假說與小作文

| 項目 | 結果 |
|---|---:|
| 報告／假說／小作文 | 118／219／118 |
| retrospective／prospective | 196／23 |
| open／終態 | 219／0 |
| weak／medium | 178／41 |
| 7/27 `--due` | 0 |

「0 到期」會造成錯誤安全感：

- 8/20：14 則 H#／7 份報告。
- 8/21：26 則 H#／13 份報告。
- 8/31：156 則 H#／78 份報告。

23 則前瞻 H# 中有 16 則在自然語言「下次驗證」寫每月追蹤，但舊 CLI 查不到這個時鐘。
本次新增的統一佇列先把正式期限、topic action 與敘事 freshness 放在一起；未來若要精確
管理 interim check，應再把 `next_check_due/type` 升成可查詢欄位，不把它混入終局
`review_due`。

另外，`leading_hypotheses.quant_context()` 原本宣稱唯讀卻直接用 `sqlite3.connect()`；
本次已改成 `db_ro.connect()`，避免 typo 路徑建立空 DB 或唯讀宣稱失真。

## 7/19–7/27 值得關注的候選議題

### 1. Vera Rubin／Spectrum-6 進入量產與首波部署

NVIDIA 7/21 表示 Vera Rubin NVL72 正在量產爬坡，合作夥伴已有機架運行，供應鏈橫跨
350 多個 factory sites；Spectrum-6 也進入首批部署。這比單純 roadmap 更接近可觀測的
量產節點。[NVIDIA Vera Rubin 官方更新](https://blogs.nvidia.com/blog/vera-rubin/)、
[Spectrum-6 官方更新](https://blogs.nvidia.com/blog/nvidia-spectrum-six-arrives-in-gigascale-ai-factories/)。

NVIDIA 5/31 曾正式列名 GIGABYTE、QCT、Wistron、Wiwynn 等 Vera 系統廠；這只證實
生態系參與，不證實新增訂單或營收。[NVIDIA Vera 生態系名單](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Unveils-Vera-the-CPU-for-Agents/default.aspx)。

逐份對照後，只有 2376 技嘉小作文把 5/15 法說的 `early-stage development` 寫成
未加日期的現在式，已在本次修正為歷史切面；正式筆記的 5/15 公司揭露與 H1 都不變。
2382、3231、6669 沒有同類過時敘述，只排 8/3 的公司 IR 驗證節點，檢查量產、驗收、
收入與毛利／營運資金足跡，不改 H# 狀態或多空方向。

散熱、PCB、電源只做族群 `watch`；SK hynix 的 HBM 合作不能外推成台灣 DRAM 個股受惠。
NAVER／Brookfield 的非拘束性條款與 SK 的 LOI 也必須和已交付訂單分開。

### 2. 美國 Section 301 對台灣商品的新框架

USTR 7/23 最終行動對未豁免台灣商品採「Section 301 + MFN 合計 10%」框架，7/24
美東 00:01 生效；7/24 前已裝船且在最後運輸段、並於 7/28 前進口者有在途例外。
[USTR 官方說明](https://ustr.gov/about/policy-offices/press-office/press-releases/2026/july/ustr-takes-action-forced-labor-section-301-investigations)、
[Federal Register notice／Annex](https://ustr.gov/sites/default/files/files/Press/Releases/2026/FLIP%20301%20Investigation%20Final%20Action%20FRN%207-23-26%20FINAL.pdf)、
[白宮備忘錄](https://www.whitehouse.gov/presidential-actions/2026/07/actions-by-the-united-states-in-the-investigations-under-section-301-of-the-trade-act-of-1974-of-the-acts-policies-and-practices-of-60-economies-related-to-the-failure-of-each-economy-to-impose-and/)。

台灣適用 Annex I 與 Annex II Parts A、K。一般豁免清單明列 8471 電腦／processing
units、8473.30 電腦零件、8486 半導體設備、8517.62 資料傳輸設備、8541 半導體元件、
8542 積體電路及 3818 半導體材料；Section 232 商品及其零件也另受豁免。這表示
「台灣科技品全面加 10%」是錯誤讀法。

但 code-level 豁免仍不能直接映射成公司結論：裸 PCB、電源、散熱等可能使用其他 HTS，
同一公司不同組態／原產地也可能不同。在取得公司報關 code、台灣直出占比與 Incoterms
前不建立個股 impact；此議題維持 `policy_watch`，7/30 優先查未被清單直接涵蓋的品項。

### 掃描限制

TWSE／TPEx 重大訊息日端點只顯示當前批次，repo 先前也沒有逐日 scan log；因此這次只能
聲稱「查到兩個值得關注的主題」，不能聲稱 7/19–7/27 每一天、121 家公司都已完整掃過。
`scan_log.csv` 已把本次標成 `partial`，下一次為 8/3。

## 已落地的更新制度

- `scripts/research_queue.py`：唯讀聚合待辦、財務 coverage、四週 cohort 與 topic／scan lint。
- `notes/research_topics/`：獨立候選議題區，已建立兩則議題與一筆部分掃描紀錄。
- `RESEARCH_MAINTENANCE.md`：P0–P3 SLA、週／月／季／年節奏與路由規則。
- `.github/workflows/research-watch.yml`：每週一與財報 workflow 後產出 Actions 提醒，不寫 main。
- `fetch_financials.py`／workflow：官方月營收 fallback、17 日重試與完整度閘門。

後續正式更新仍要遵守：一篇 note + 一份 manifest + 同一 evidence pack 的獨立離線重算，
每篇各自 commit。候選 topic 的存在不降低這個門檻。

## 驗證

- `qual_notes.py --lint`：121 篇，0 errors／0 warnings；事件錨點 1 篇，0／0。
- `leading_hypotheses.py --lint`：118 份報告全數通過。
- `research_queue.py --lint`：2 則 topic、1 筆 scan，0 errors；1 個刻意保留的 warning
  是 Section 301 尚未完成 HTS／公司暴露映射，因此沒有 impact。
- 完整 unittest：307 tests OK。
- SQLite：`PRAGMA integrity_check=ok`、`PRAGMA query_only=1`。

測試環境同上，使用 Windows 預設 console 編碼（未設 `PYTHONUTF8`／`PYTHONIOENCODING`）與
python.org CPython 3.12.10；完整測試因會建立 SQLite 暫存檔，在 Codex filesystem sandbox
外執行。GitHub CI 為 Ubuntu／Python 3.12，新增 workflow 仍會再執行同一套純 stdlib 測試。
