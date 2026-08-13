# Research Center Design QA

- Visual target: `C:\Users\nossi\.codex\generated_images\019fb96b-3cd3-7862-a486-ae86f9b2c88f\exec-57bbbd43-c35c-4f98-a523-3fca7f96712b.png`
- Target pixels: 1487 × 1058; evaluated at a normalized 1440 × 1024 viewport
- Final implementation: `tmp/research-center-qa/implementation-final.png`
- Same-input comparison: `tmp/research-center-qa/comparison-final.png`
- Mobile evidence: `tmp/research-center-qa/mobile-list-v2.png`, `tmp/research-center-qa/mobile-reader.png` at 390 × 844
- Tested state: light theme, all article types, `formal-8261` selected

## Comparison history

1. Initial desktop render found a P0 content failure: the title and article sections were not attached because multiple nodes were passed to `appendChild`. Replaced those calls with `append` and added contract tests.
2. Second desktop render found P1 horizontal overflow and a selection/list-order mismatch. Added long-text wrapping and stable type ordering so the selected article is visible at the top of the catalog.
3. Initial mobile render found a P1 collapsed content column below 1180 px. Removed the zero-width grid placement at that breakpoint and added an in-panel close action for the mobile filter drawer.
4. Final side-by-side comparison confirms the intended warm off-white palette, thin dividers, compact teal/purple/amber type system, 220 px filter rail, 400 px catalog, independent reader, right-side outline/evidence rail, typography hierarchy, and content density. No visible P0, P1, or P2 differences remain that block the selected direction.

## Functional verification

- 244 real articles render: 121 formal notes, 118 long/short narratives, and 5 market topics.
- Search, article-type tabs, selected-card state, deep links, related-content tabs, copy-link feedback, theme toggle, dashboard gateway, and sorting work.
- Mobile catalog → reader → back flow and filter drawer open → close flow work at 390 × 844.
- Desktop and mobile have zero horizontal page overflow.
- Browser console errors/warnings: 0.
- Full suite: 325 tests passed with Python 3.12 and `PYTHONUTF8=1`.

final result: passed

---

# Design QA：平行視角問題導引工作台

## Evidence

- Reference: `/Users/dennisliu/.codex/generated_images/019ff74e-dddf-7360-997d-a652d8623da6/exec-dac1728e-8e53-4d63-be6a-11c4923a4ec3.png`
- Implementation: `/Users/dennisliu/Code/GitHub/strong-weak-scanner/tmp/uiux_option3/desktop-final.png`
- Combined comparison: `/Users/dennisliu/Code/GitHub/strong-weak-scanner/tmp/uiux_option3/comparison-final.png`
- Mobile verification: `/Users/dennisliu/Code/GitHub/strong-weak-scanner/tmp/uiux_option3/mobile-final.png`
- Viewport: desktop 1487×1058 CSS pixels, DPR 1；reference 與 implementation 都是
  1487×1058，未做 density normalization。手機為 390×844 CSS pixels。
- State: light theme、散熱族群、D 基本面改善、排序第一列被選取。reference 使用示意的
  2026-08-13 資料；implementation 使用本機正式 DB 的 2026-08-12 as-seen payload。

組合圖保留兩張原始桌機截圖的完整像素寬度並上下排列，文字、表格與 detail panel 均可直接
辨識，因此不需要另以放大 crop 取代 full-view 證據。Browser screenshot、DOM 狀態、水平溢位
與 console 都另行檢查。

## Fidelity review

- **Typography:** 品牌、標題、表格與說明採既有 Noto Sans TC／IBM Plex Mono；介面圖示使用
  Material Symbols Rounded，沒有手繪 SVG、文字符號假圖示或低解析替代資產。
- **Layout and spacing:** 黑色 89px site header、導言、四欄 context strip、五個視角頁籤、
  左排行／右詳情的比例與留白對齊 reference；390px 改為單欄且 page scroll width 等於 viewport。
- **Color and surface:** 黑色 header、暖白紙面、紅／青／橙／紫的視角語意、細邊框與小圓角均
  對齊 reference，並保留既有 dark theme token。
- **Copy and data truth:** 標籤改為「趨勢領先／防守韌性／籌碼支持／基本面改善」，明示族群內
  百分位不是機率、預測或投資建議。reference 的時間穩定度圓點改成 payload 真正量測的
  leave-one-peer-out 結構敏感度，不杜撰 30 日穩定性。
- **Behavior:** 問題頁籤會重排、點列與方向鍵會更新詳情、詳情中的五視角也可切換、診斷可展開、
  完整個股 drawer 可開關。quick nav 點選／點外／Escape 均收合。
- **Accessibility:** 頁籤與表格選取狀態有 ARIA；drawer 背景 inert、Tab／Shift+Tab focus trap、
  Escape 關閉並還原焦點；主要觸控目標至少 44px，支援 prefers-reduced-motion。

## Comparison history

1. Pass 1 發現 header／標題比例偏小、表格缺欄位副標、桌機名稱與代碼斷行、選中欄位過度框選、
   metadata 缺少辨識圖示；逐項修正後重建。
2. Pass 2 使用 `comparison-final.png` 重新把 reference 與 implementation 放在同一輸入中檢查；
   沒有 P0、P1 或 P2 視覺落差。剩餘差異均是有意且不影響主要任務的 P3：live payload 日期與
   示意資料不同、結構敏感度取代沒有資料依據的時間穩定度、未顯示沒有實際保存行為的收藏控制。

## Interaction and runtime checks

- Desktop 1487×1058：散熱 7 檔、D 排序、row selection、B 切換、診斷、drawer focus trap 與
  Escape／焦點還原皆通過；`innerWidth === scrollWidth === 1487`。
- Mobile 390×844：active D page tab 自動置入可見範圍、quick nav 點選後收合、無水平溢位。
- Browser console warnings/errors: 0。
- Generated JavaScript syntax check: passed。

## Final result

passed
