# 質化研究一手文件取得指南

> 最後實測：2026-07-12。官方網站可能改版；固定入口失效時，依本頁的備援順序回到官方
> 首頁重新定位，不猜測檔名或把搜尋快取當證據。

本頁只規範 **drafter 凍結 evidence pack 前**如何取得文件。核心研究與簽核流程仍依
[QUALITATIVE_RESEARCH_RUNBOOK.md](QUALITATIVE_RESEARCH_RUNBOOK.md)；reviewer 只能使用同一個
pack 離線查核，不得另走本頁重新下載。

## 來源優先順序

| 核心 role | 第一選擇 | 官方備援 | 收件時必查 |
|---|---|---|---|
| `annual_report` | 公司 IR 的完整年報 PDF | MOPS「年報及股東會相關資料／電子文件下載」 | 選「股東會年報」，不要誤拿議事手冊；核對資料年度 |
| `annual_financials` | 公司 IR 的年度查核財報 | TWSE 文件站／MOPS「財務報告書」第四季 | 合併或個體、查核意見、會計年度、是否更正 |
| `latest_quarterly_report` | 公司 IR 的最新季報 | TWSE 文件站／MOPS「財務報告書」最新已公告季 | 核閱財報而非新聞稿；核對年、季及上傳日 |
| `latest_investor_conference` | 公司 IR 的法說簡報 | MOPS 法說／重大訊息附件；上櫃公司另查 TPEx 法說平台 | 簡報日期、公司代號、是否另有較新場次 |
| `shareholder_meeting`（選填） | 公司 IR 股東會專區 | MOPS 年報及股東會資料 | 只有治理、股利或議案主張需要時才加入 |

搜尋引擎、新聞、券商報告及資料網站只能找入口。可提交證據必須回到公司自有網域、
`twse.com.tw`／`mops.twse.com.tw`／`mopsov.twse.com.tw`／`tpex.org.tw` 等官方網域的原始文件。

## 1. 先定位公司官方 IR

公司 IR 路徑沒有統一格式，不可自行拼成 `/investor/...pdf`。先用交易所公司基本資料取得
公司網址，再從「投資人專區／Investor Relations」進入「財務資訊、年報、法人說明會」。

- 上市公司：[TWSE OpenAPI](https://openapi.twse.com.tw/) 的
  `GET /v1/opendata/t187ap03_L`，代號欄為 `公司代號`、官網欄為 `網址`。
- 上櫃公司：[TPEx OpenAPI](https://www.tpex.org.tw/openapi/) 的
  `GET /openapi/v1/mopsfin_t187ap03_O`，代號欄為 `SecuritiesCompanyCode`、官網欄為
  `WebAddress`。

PowerShell 可直接用專案規定的 Python 查詢；一邊找不到就換另一個市場端點：

```powershell
$env:STOCK_ID = "6451"
uv run --no-project --python 3.12 python -c "import json,os,urllib.request; sid=os.environ['STOCK_ID']; rows=json.load(urllib.request.urlopen('https://openapi.twse.com.tw/v1/opendata/t187ap03_L')); print(next(r['網址'] for r in rows if r['公司代號']==sid))"

$env:STOCK_ID = "3675"
uv run --no-project --python 3.12 python -c "import json,os,urllib.request; sid=os.environ['STOCK_ID']; rows=json.load(urllib.request.urlopen('https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap03_O')); print(next(r['WebAddress'] for r in rows if r['SecuritiesCompanyCode']==sid))"
```

API 可能回傳 `http://` 或沒有 scheme 的舊官網值；用瀏覽器進站並確認公司名稱、憑證與
IR 導覽後，再記錄實際 HTTPS PDF。IR 若只有 JavaScript、`blob:`、登入牆或失效連結，直接
改走 MOPS／TWSE，不繞過存取限制。

## 2. MOPS 與 TWSE 文件站查詢

固定起點是 [MOPS 公開資訊觀測站](https://mops.twse.com.tw/mops/)；可在首頁用股號／公司名
搭配「年報」「財務報告書」「法人說明會」搜尋。官方操作路徑可參考
[MOPS 操作手冊](https://dsp.twse.com.tw/public/static/downloads/announcement/official/R-1140600094-1.pdf)：
「單一公司 → 電子文件下載 → 財務報告書」可依公司、民國年及季別取得 PDF。首頁全文檢索
也可改用 [MOPS ezSearch](https://mopsov.twse.com.tw/mops/web/ezsearch)。

財報與年報常見的**可重現清單 URL**如下。整段 URL 在 PowerShell 中必須加引號，避免 `&`
被 shell 拆開：

```text
# 財務報告：seamon=1/2/3 為季報；seamon=4 為年度第四季查核財報
https://doc.twse.com.tw/server-java/t57sb01?step=1&colorchg=1&co_id=<股號>&year=<財報民國年>&seamon=<1|2|3|4>&mtype=A

# 年報／股東會文件：year 使用當次股東會民國年，再從結果列核對年報的資料年度
https://doc.twse.com.tw/server-java/t57sb01?step=1&colorchg=1&co_id=<股號>&year=<股東會民國年>&seamon=&mtype=F
```

這兩種 `step=1` 網址回傳的是 HTML 文件清單，**不是 PDF bytes**。點「電子檔案」後，網站
會以 POST 產生短效 `/pdf/<檔名>_<時間戳>.pdf`；不要把該暫時位址當永久來源。若沒有穩定
PDF 直鏈，evidence manifest 的 `url` 記錄上述完整官方查詢 URL，並在筆記的來源文件名稱中
記下結果列的精確檔名、文件名稱、資料期間與上傳日，讓下一位研究者能重現同一列。

參數判讀原則：

- `mtype=A`：`year` 是財報資料民國年；年度財報選 `seamon=4`，季報選最新已公告的
  `1`、`2` 或 `3`。結果同時有中文／英文或合併／個體時，優先選支持正文口徑的正式中文
  合併財報，並把口徑寫清楚。
- `mtype=F`：查詢年通常是股東會年度，結果中的「股東會年報」可能標示前一個財務年度；
  以結果列的資料年度與文件標題為準，不從 URL 年份推定財報期間，也不要誤選議事手冊。
- 結果若標示更（補）正，選最新正式更正版並記錄上傳日；不可把更正前後數字混用。
- 裸開舊書籤（例如只有 `/mops/web/<功能代碼>`）可能被導向錯誤頁；回到 MOPS 首頁搜尋，
  再複製帶完整公司、日期、序號等參數的結果 URL。

## 3. 法說、重大訊息與可接受的直鏈

公司 IR 仍是法說簡報第一選擇；需備援時依序查 MOPS ezSearch、MOPS 法人說明會／重大訊息、
以及上櫃公司的 [TPEx 法說平台](https://ic.tpex.org.tw/)。常見形態如下，但**只能從官方結果
複製，不得猜測檔名或雜湊**：

| 類型 | 常見 URL 形態 | manifest 記錄方式 |
|---|---|---|
| 公司 IR PDF | `https://<公司官方網域>/.../<文件>.pdf` | 記最終 HTTPS PDF 直鏈 |
| MOPS 法說附件 | `https://mopsov.twse.com.tw/nas/STR/<檔名>.pdf` | 記附件直鏈 |
| TPEx 法說附件 | `https://ic.tpex.org.tw/uploads/<股號>/<雜湊>.pdf` | 記附件直鏈 |
| MOPS 單筆重大訊息 | `.../mops/web/ajax_t05st01?...&step=2&...&co_id=...&spoke_date=...&spoke_time=...&seq_no=...` | 保留官方結果給的全部定位參數 |
| TWSE 動態文件 | `https://doc.twse.com.tw/server-java/t57sb01?...` | 記完整清單 URL，來源名稱另記精確檔名與上傳日 |

MOPS 首頁、ezSearch 首頁或缺少 `co_id`／公告日期／`seq_no` 的泛用查詢頁不能作為已核驗
主張的來源。若附件是從重大訊息進入，優先記附件 PDF；沒有穩定附件直鏈時，才記能唯一
回到該公告的完整結果 URL。

## 4. 下載後驗收

在把文件交給 `qual_evidence.py build` 前逐份完成：

- [ ] 實際 GET／瀏覽器下載成功；不要因 HEAD 失敗就判死刑，MOPS／TWSE 常對 HEAD 回傳
  HTML 或 redirect。
- [ ] 檔案開頭為 `%PDF-`，且原生 Poppler `pdfinfo.exe <檔案>` 成功；HTTP 200、`.pdf`
  副檔名或 `Content-Type` 任一項都不足以單獨證明是 PDF。
- [ ] PDF 內的公司名／代號、標題、資料期間與語言正確；`pdfinfo` 頁數等於 build 使用的
  `--page-count`。
- [ ] 記錄發布／上傳日、擷取日、官方 locator、精確檔名、頁數與 SHA-256；URL 重複使用或
  日後內容變動時，以 pack 內 PDF SHA 判定本次查核的實際 bytes。
- [ ] 在官方 IR／MOPS 列表確認是否有較新或更正版。未把列表本身納入 pack 時，只能寫
  「本輪核心文件中的法說日期為……」，不能宣稱「截至今天最新」。

## 5. 失敗備援與停止條件

| 失敗情境 | 立即動作 | 下一層備援 |
|---|---|---|
| 公司 IR 404、搬站或找不到投資人專區 | 用 TWSE／TPEx OpenAPI 重找公司官網 | 改查 MOPS／TWSE 同一 role |
| MOPS 舊路由顯示錯誤或空白 | 回首頁用股號＋文件關鍵字搜尋 | 用完整 `doc.twse.com.tw` 清單 URL 或 ezSearch |
| 點擊後沒有下載、popup 被擋、只拿到 HTML | 允許官方 popup／用互動瀏覽器點精確檔名；重新做 PDF 驗收 | 改找公司 IR 或交易所官方附件直鏈 |
| 官方頁是 JavaScript、`blob:`、403 或 session URL | 用正常瀏覽器手動下載，不繞過權限 | 換公司 IR、MOPS、TWSE／TPEx 另一官方入口 |
| 文件有更正版或期間不確定 | 回官方結果列比較資料年度與上傳日，只留最新正式更正版 | 無法確定就刪除受影響主張 |
| 找不到穩定一手文件達 10 分鐘 | 停止搜尋，記 `source_search_timeout_minutes: 10` 與 `unverified_claims_removed: true` | 刪除主張；缺必備 role 時整篇維持 `ai_draft` |
| reviewer 發現 URL、頁面或 SHA 問題 | reviewer 停止簽核，不重新下載 | 退回 drafter 取得／補頁並建立全新 pack SHA |

備援只是在官方一手入口間切換，不包含新聞、搜尋摘要、網頁快取或第三方資料庫。下載與驗收
必須在 pack 凍結前完成；凍結後任何來源替換都要建立新 pack，不能覆寫原 pack。
