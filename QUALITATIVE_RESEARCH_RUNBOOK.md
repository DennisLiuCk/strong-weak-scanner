# 質化研究單篇查核 Runbook（`focused_v1`）

本頁供沒有前一個 session 對話記憶的 drafter 與 reviewer 使用。適用於新建筆記或把既有
筆記重新展開成完整研究；品質契約細節仍以 [README「質化研究筆記」](README.md#質化研究筆記notesqualitative)
與 `scripts/qual_notes.py --lint` 為準。

## 完成定義

- 只處理一家公司；使用 3–5 份核心一手文件與約 25–35 個重要 claim block。
- note 為 `focused_v1`、狀態為 `independently_verified`，每個實質段落、bullet 與表格列
  都能由同 block 的 `[S#]` 回到實際引用頁。
- 不同於 drafter 的 reviewer 使用同一個唯讀 evidence pack，離線重算 SHA、數字、期間、
  單位與推論邊界；PDF／PNG 留在 `tmp/`。
- 最終只提交該 note 與當前 manifest，並做成一個獨立中文 commit。

## 逐步核對清單

### 1. 開始前：同步、隔離與盤點

- [ ] 執行 `git pull --ff-only` 與 `git status --short`；不得覆蓋、清理或順手提交別人的變更。
- [ ] 讀 `AGENTS.md` 本任務規則；既有筆記才先執行
  `uv run --no-project --python 3.12 python scripts/qual_notes.py --lint <股號>`。尚無筆記時此命令會
  因找不到檔案而 exit 1，應直接走下一步建立骨架，不把它誤判成既有內容品質失敗。
- [ ] 新建時用
  `uv run --no-project --python 3.12 python scripts/qual_notes.py --new <股號>`；重做既有筆記
  不使用會清空內容的 `--force`，應保留正確歷史內容，並把 meta 改為
  `research_profile: focused_v1`、`verification_status: ai_draft`，reviewer 欄位先留空。
- [ ] drafter 與 reviewer 使用不同身分；開始就指定交接人，避免最後由撰稿者自簽。

### 2. 取得核心來源：只把搜尋當入口

- [ ] 優先依序查公司 IR、MOPS／TWSE／TPEx；搜尋引擎、新聞與法說摘要只能協助定位，
  不可成為正文證據。
- [ ] 核心 role 必須涵蓋 `annual_report`、`annual_financials`、
  `latest_quarterly_report`、`latest_investor_conference`。年報若確實內含查核財報，可由同一
  PDF 同時承擔前兩個 role；股東會只在治理／股利主張必要時加入。
- [ ] 每份文件記錄直接 HTTPS URL、發布／資料日期、財務期間、PDF 實體總頁數。正文的頁碼
  一律指 PDF 實體頁，不使用文件印刷頁碼。
- [ ] 每份缺失文件最多找 10 分鐘；逾時即停止，manifest 保留
  `source_search_timeout_minutes: 10` 與 `unverified_claims_removed: true`，並刪除無法驗證的
  主張，不用二手來源補洞。10 分鐘規則不會豁免四個必備 role；若必備文件確實不存在，
  該篇維持 `ai_draft` 並回報缺口，不得冒充完整核驗。
- [ ] exact PDF 能證明文件日期，不能單獨證明「截至今天仍是最新」。除非 pack 另有一手
  時效證據，正文寫「本輪核心文件中的法說日期為……」，不要宣稱「最新官方法說」。

### 3. 先做 claim–page 對照，再寫成文章

- [ ] 在 `tmp/` 維護工作表：`claim｜S#｜PDF 實體頁｜運算元／公式｜事實/展望/研究推論`。
- [ ] 每個計算的所有運算元都要列頁碼、期間、幣別、單位與口徑；特別區分合併／歸母、
  年度／單季、現金流入／用途，以及管理層目標／已發生結果。
- [ ] 每個重要段落、bullet、表格資料列都在同一 block 標 `[S#]`。相鄰 render 只是上下文，
  **不算實際 cited evidence**；跨頁計算必須把每個運算元所在頁都列入 `cited_pages`。
- [ ] 「第一、唯一、領先、市占、客戶名稱、AI／CPO、量產、訂單、毛利較高」屬高風險
  主張；若來源只說規劃、能力、NPI 或展望，正文必須保留相同邊界。
- [ ] 聚焦讀者真正需要的公司業務、產業結構、優缺點、動能、KPI 與風險；不為湊 25–35
  個 block 拆句，也不保留即時估值或沒有一手依據的市場傳聞。

### 4. Drafter 建立、轉圖並凍結 evidence pack

- [ ] 把選定 PDF 放在 `tmp/`，依實際 S# 重複傳入 `--source/--url/--pages/--page-count/--role`：
- [ ] Windows 必須使用原生 Poppler `.exe`，不用會被 `shell=False` 拒絕的 `.cmd` 包裝器。
  Codex app 可先用 workspace dependency loader 取得 bundled 路徑；若未直接回傳路徑，使用下列
  fallback，找不到就停止並安裝／定位 Poppler，不可省略頁數驗證：

```powershell
$PDFINFO = (Get-ChildItem "$env:USERPROFILE\.cache\codex-runtimes" -Recurse -File -Filter pdfinfo.exe -ErrorAction SilentlyContinue |
  Where-Object { $_.FullName -match '[\\/]native[\\/]poppler[\\/]' } | Select-Object -First 1).FullName
if (-not $PDFINFO) { throw '找不到原生 Poppler pdfinfo.exe' }
$PDFTOPPM = Join-Path (Split-Path $PDFINFO) 'pdftoppm.exe'
if (-not (Test-Path -LiteralPath $PDFTOPPM)) { throw '找不到同目錄 pdftoppm.exe' }

uv run --no-project --python 3.12 python scripts/qual_evidence.py build --stock-id <股號> --content-as-of <YYYY-MM-DD> --source "S1=<PDF>" --url "S1=<直接URL>" --pages "S1=<實體頁>" --page-count "S1=<總頁數>" --role "S1=<role>" [...其餘 S#...] --pdfinfo "$PDFINFO"
uv run --no-project --python 3.12 python scripts/qual_evidence.py render-plan "<PACK_DIR>" --pdfinfo "$PDFINFO"
uv run --no-project --python 3.12 python scripts/qual_evidence.py render "<PACK_DIR>" --pdftoppm "$PDFTOPPM" --pdfinfo "$PDFINFO"
uv run --no-project --python 3.12 python scripts/qual_evidence.py verify "<PACK_DIR>" --renders --pdfinfo "$PDFINFO"
```

- [ ] 把 `build` 回傳的 manifest 路徑、完整 pack SHA 與 S# 填回 note meta；證據索引列出的
  實體頁必須與 manifest 一致。
- [ ] drafter 寫作時讀完所有實際 `cited_pages`，並按每份文件抽查 render 的首／中／尾、
  跨頁表格與複雜頁面，確認非空白、未裁切／旋轉、無亂碼且表頭、單位、註腳可讀；完整的
  `rendered_pages` 逐張目視留給獨立 reviewer，避免兩人重複做同一輪全量檢查。
- [ ] 完成 drafter 自查後停止改 note／manifest，回報 pack 路徑、SHA、claim 數與 render 數；
  在共用工作樹若用 `git hash-object -w -- <note> <manifest>` 建立短期復原點，必須立即記錄
  回傳的兩個 blob SHA；無 ref 的 dangling blob 可能被 Git 清理，不可當成長期備份，也不可
  stage／commit 未簽核版本。

### 5. Reviewer 獨立查核與唯一寫入權

- [ ] reviewer 接手後，drafter 不再改檔；reviewer 不重下載，也不使用另一版本 PDF。
- [ ] 先對同一 pack 執行 `verify --renders`，再逐張目視全部 renders；獨立重算每個重要數字，
  不沿用 drafter 的算式結論。
- [ ] 逐 claim 核對期間、單位、正負號、合併／歸母口徑、來源時效措辭及「事實→推論」是否
  越界；確認正文只說一手文件實際支持的程度。
- [ ] 小額差異若不改變四捨五入數字與研究結論，可保留雙方數字於 `conflict_summary` 並完成
  簽核；若可信來源對重要結論實質衝突，狀態改為 `conflicted`，不可自行挑有利版本。
- [ ] 找不到證據不是來源衝突：刪除 claim，或依下一節退回重建 pack。

### 6. 缺頁／錯頁：停止簽核，退回重建

- [ ] reviewer 發現任何重要 claim 的運算元頁未列入 `cited_pages`，立即停止簽核，不可把
  「它剛好是相鄰 render」視為合格。
- [ ] 由 drafter 使用**原本同一批 PDF**補正引用頁與 render plan；不得覆寫舊 pack，必須
  `build` 出新的內容定址 SHA、更新 note meta／證據索引，且舊 manifest 不得提交。
- [ ] reviewer 對新 pack 重跑 verify。若 PDF SHA 與舊 pack 完全相同，可比對既有 render
  SHA（用 `Get-FileHash -Algorithm SHA256`，以相同 S#／檔名配對）並集中目視新增頁；未留下
  可重現的逐檔比對結果就保守地全部重看。只要任一 PDF 內容變更，就重新做完整查核。

#### 訊芯-KY（6451）退回重建案例

原 claim「2026Q1 現金與三個月以上定存合計 86.84 億元」需 S2 p.12 的現金
5,572,071 千元及 p.13 的三個月以上定存 3,111,952 千元。舊 pack `8bb335f1…` 雖有 `[S2]`，
p.12 也只是 p.11 的相鄰 render，但 p.12／p.13 未被完整列為 cited evidence，且 p.13 根本
沒有 render；數字正確仍不符合品質契約。

處理方式：停止簽核 → drafter 以相同四份 PDF 把 S2 p.12–13 加入 `cited_pages`、render
p.11–14 → 建立新 pack `a7483e23…` → 更新 note meta 與 S2 證據索引 → 排除舊 manifest →
reviewer 確認四份 PDF SHA 未變、核對新增頁並重算 5,572,071 + 3,111,952 = 8,684,023 千元
後才簽核。核心原則是：**每個運算元頁都須明列；manifest 改動必然產生新 pack SHA。**

### 7. 簽核、驗證與單篇 commit

- [ ] reviewer 完成修文後填入：

```yaml
verification_status: independently_verified
reviewed_by: <不同於 drafted_by 的 reviewer>
reviewed_at: <YYYY-MM-DD>
review_method: offline_evidence_pack_independent_recalculation
review_scope: all_material_claims
reviewed_content_sha256:
conflict_summary: <無衝突可留空；有小幅口徑差異則保留雙方>
```

- [ ] 依序執行；若已開新的 PowerShell process，先重跑第 4 步 locator 設定 `$PDFINFO`。
  把第一個命令輸出的 hash 填回 meta 後，再重跑 hash 確認一致：

```powershell
uv run --no-project --python 3.12 python scripts/qual_notes.py --hash <股號>
# 將上列輸出填入 reviewed_content_sha256，再確認重算結果相同
uv run --no-project --python 3.12 python scripts/qual_notes.py --hash <股號>
uv run --no-project --python 3.12 python scripts/qual_notes.py --lint <股號>
uv run --no-project --python 3.12 python scripts/qual_evidence.py verify "<PACK_DIR>" --renders --pdfinfo "$PDFINFO"
uv run --no-project --python 3.12 python -m unittest discover -s tests
```

- [ ] 只 stage `notes/qualitative/<股號>_<名稱>.md` 與 meta 指向的**當前** manifest；用
  `git diff --cached --name-status` 確認恰為兩個檔案，沒有舊 manifest、`tmp/` 或無關變更，
  再執行 `git diff --cached --check`；未 stage 前的 `git diff --check` 看不到 untracked 新檔。
- [ ] 立即建立一個中文 commit，例如 `完成<公司> focused_v1 獨立複核`；不可累積多家公司。
  push 是後續獨立動作，僅在使用者或既定工作流程要求時執行。

## 不可放行條件

- reviewer 與 drafter 相同、pack SHA／PDF SHA 不符、render 不可讀、重要運算元頁未引用、
  重大來源衝突未保留、正文仍有二手／無來源主張、hash 或 lint 不通過，任一項成立都不得
  標為 `independently_verified` 或 commit。
