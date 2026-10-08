# 研究中心：概念圖 1 實作驗收

final result: passed

驗收日期：2026-10-08。範圍是現有研究中心的閱讀流程、導覽、版型與回歸；本檔記錄部署前驗收，部署狀態以 GitHub Pages 建置 commit 為準。

## 比對基準與證據

- Source visual truth：`reports/assets/research_center_ux_2026-10-08/design-library.png`。
- Implementation：`http://127.0.0.1:8767/research.html#topic-MI-2026-08-08-AI-RACK-TRUST-ROOT`。
- 最終實作截圖：`reports/assets/research_center_ux_2026-10-08/implementation-desktop-final.jpg`。
- 原圖實際尺寸為 **1487 × 1058 px**；最終瀏覽器 viewport 與截圖同為 **1487 × 1058**，devicePixelRatio=1。無裝置外框、無密度縮放。前期 1488 × 1056 的近似比對已在最後一輪改為精確原尺寸。
- 狀態：淺色、文章庫、全部類型、最新排序，開啟「AI 機櫃如何判斷控制指令可信」同篇文章，面板關閉、正文頂端。
- 完整原圖與最終截圖已放在同一次影像輸入中檢視；另有可開啟的[並排比對頁](reports/research_center_design_comparison_2026-10-08.html)。
- 細節比對：閱讀標題／metadata／正文起始（原圖及實作 x≈490、y≈150），導覽／閱讀工具（x≈675、y=0）。[全景](reports/assets/research_center_ux_2026-10-08/comparison-full.jpg)與[局部](reports/assets/research_center_ux_2026-10-08/comparison-detail.jpg)記錄最後字級修正後的並排檢視；這兩張比較頁截圖採展示寬度，精確尺寸判定以最終獨立截圖為準。

概念圖採縮寫文章與示意清單；正式實作沿用目前已發布全文、原排序與原查核狀態。標題保持原句、內容更長、選中文章是清單第二篇，皆屬資料差異；未為追求相同換行而改寫研究。mock 沒有描述的手機、空結果及深色模式，依現有網站模式補齊。

## Findings 與修正歷程

| 輪次 | 問題與影響 | 修正與複驗 |
| --- | --- | --- |
| 初版 | P1：舊標題底色卡片與窄閱讀欄仍搶走正文空間 | 移除題名前框、加寬正文，清單固定在左；證據為 `implementation-desktop-v1.jpg` → `implementation-desktop-v2.jpg`。 |
| 操作驗收 | P1：篩選抽屜層級低於遮罩，點擊無法操作 | `.filters.open` 設為 z-index 60，遮罩 59；實際清除、勾選散熱、完成後得到 23 篇；320px 抽屜、Escape 與焦點返回通過。 |
| 操作驗收 | P2：目錄關閉時的額外焦點回送，讓章節被工具列遮住 | 使用原生 dialog 關閉，章節捲動後 `focus({preventScroll:true})`；手機跳到四關章節時標題在工具列下方，焦點落在該 section。 |
| 全景比對 | P2：桌面字級偏小、品牌偏右，工具缺少概念圖的視覺辨識 | 桌面正文 22px／1.75、標題 40px、章節 28px；品牌置中、閱讀工具 15px，加入正式 Heroicons。最終全景及局部比對無剩餘 P0／P1／P2。 |

## 必要視覺檢查

| 面向 | 結果與保留差異 |
| --- | --- |
| 字體與階層 | 沿用 Noto Sans TC 與系統後備字體；主標 700、正文正常字重。桌面主文接近原圖的閱讀密度；手機 25px 標題／16px 正文。完整原題較示意題長，保留自然換行，沒有縮寫或截斷正文。 |
| 間距與版型 | 左欄約 31%，主文左右 42px；平面清單、細分隔線、選中列淡青底。標題後直接接日期與查核狀態、正文，沒有額外導讀牆。桌面第一個正文 section 位於 y=396.5px；這是單一固定版型量測，非使用者成效統計。 |
| 色彩 | 沿用米白背景、近黑正文、青色導覽及選中狀態。可信度到期警示保留語意色與文字；深色模式圖示反白、選中狀態可辨認。沒有用陰影卡片取代原圖的平面閱讀區。 |
| 圖像與圖示 | 原圖沒有照片／插圖資產。箭頭、搜尋、篩選、目錄、文件與展開使用未改寫的 Heroicons 2.2.0 outline SVG，存於 `assets/heroicons/`，附 MIT 授權；未用自畫 SVG／CSS 圖案替代。最終頁面圖示均載入。 |
| 文案與研究內容 | 保留既有文章類型名稱與研究邊界，不把示意圖的「公司／產業」硬套成新的分類。新手、研究摘要、角色與學習路線移至閱讀輔助；原本文內的限制與反證仍在正文。來源、查核附錄與過期警示完整保留。 |

## 操作與響應式驗收

- 桌面清單開文、換文、搜尋、類型切換、族群篩選、清除篩選、零結果皆可操作；搜尋不重建同篇正文。
- 手機清單 → 文章 → 返回清單，瀏覽器上一頁／下一頁、重新整理會還原搜尋及閱讀位置；曾以 windowY=1402 的實際狀態驗證重新整理與前進還原。
- 深連結直接載入同篇文章；「專注閱讀」可進入與退出，預設保留清單。
- 目錄可跳正文；查核資料與閱讀輔助按需開啟，Escape 關閉。篩選面板鍵盤焦點留在抽屜內，日期 radio 保留原生群組操作。
- 族群矩陣開文仍進同一閱讀器，可返回原學習路線；知識圖譜、研究追蹤入口正常。原文檔及外部一手來源保留外開用途。
- 1487×1058 桌面、1024×900 平板、390×844 手機與 320×740 窄手機檢查；已測頁面沒有 document 水平溢出，固定返回與閱讀工具可用。
- [手機正文](reports/assets/research_center_ux_2026-10-08/implementation-mobile-final.jpg)、[平板深色](reports/assets/research_center_ux_2026-10-08/implementation-tablet-dark.jpg)、[查核面板](reports/assets/research_center_ux_2026-10-08/implementation-evidence-final.jpg)為實際瀏覽器截圖。
- 使用 Codex in-app browser；檢查已操作流程的 console error 為空。語意按鈕、輸入 label、dialog 名稱與鍵盤焦點有人工檢查；未宣稱完整 WCAG 認證。

## 程式與資料檢查

- 系統 `python` 3.12.10、Windows 11 10.0.26200；`PYTHONUTF8`／`PYTHONIOENCODING` 未設定，`utf8_mode=0`，工具管線 `stdout_encoding=utf-8`。不能將此 stdout 宣稱為 cp950。
- `unittest` 完整探索：735 tests，0 failures，0 errors，1 skipped。Node JavaScript 語法檢查通過。新增 history 序列化、路由去重、原段落／邊界保留的執行式回歸；移除強制舊導讀卡存在的過時 UI 斷言。
- 全部 282 篇文章的完整序列化 `LIB` 與 HEAD 逐字相同，並非只比文章數；[驗證紀錄](reports/research_center_implementation_validation_2026-10-08.json)附 SHA-256 與執行環境。
- 發布前另執行 `prepublish_check.py --baseline-ref origin/main`：六項研究 lint／歷史檢查、完整測試及隔離重建全部通過，DB／archive 前後 SHA-256 相同。首次隔離重建只因研究頁 LF／Windows CRLF 差異失敗；確認正規化後逐字相同並同步建置產物，再完整重跑通過。基準為 `1c82e03ad09f3bbf9c73ee64a05e944c7f5724e9`。
- 本次從已發布 payload 套入新模板更新 `research.html`；沒有執行資料抓取、評分或 DB 寫入。正式 DB、archive、研究帳本與策略檔案均不在變更清單中。
- 上述數量與座標是確定性檢查／固定條件量測，不是抽樣統計，SE／t 不適用；也不代表已驗證閱讀速度或理解率改善。

## Follow-up Polish 與限制

- P3：若後續有編輯需求，可另行制定長研究標題的短題名與副標；此版保留正式原題，不自動改寫。
- 尚未做真實讀者可用性訪談、螢幕閱讀器全流程、Safari／Firefox 或實體手機驗收；此次成果是瀏覽器操作與設計比對，不是使用者成效實驗。
- 本地預覽用於版面驗收；正式部署另核對 GitHub Pages 的建置 commit。

## Implementation Checklist

- [x] 全景與局部來源比對，修正 P0／P1／P2。
- [x] 清單、正文、面板、返回與 history 核心流程。
- [x] 桌面／平板／手機、深色、空結果與焦點。
- [x] 測試、資料一致性、README 與 CHANGELOG。
- [x] 保留可操作的本地預覽與實際畫面證據。
