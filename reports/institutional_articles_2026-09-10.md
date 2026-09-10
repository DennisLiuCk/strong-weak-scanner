# 機構情報第二輪：文章與基本來源驗證

本輪基準：`6965507be7d8383a48158c60c9f0fad56583a19e`；研究前選題commit：`31ce132`。
`RS-2026-09-10-02`先選Beacon Point及電力設備轉單研究，鎵／基板許可初始列watch。
取材為定向抽樣，不代表全市場或全站正式公司筆記已重查；人工回查日期不是排程。

## 第一篇：資料中心分期交付

- 文章：`MI-2026-09-10-DC-PHASE-DELIVERY`，7 claims、5 documents與1 living index；
  圖譜`dc-phase-delivery`只投影公司規劃及三個分期檢查點，未新增台灣公司受惠線。
- J.P. Morgan官方8/10文章核對發行部門、交易角色、專案融資與供電段落；該行是第一期
  承銷參與者，不能當同案獨立信用背書。原HTML SHA256：
  `95228b99b58b675e552a4d5bee1a0259a0e04011df17a6ffd8eed2cfca2d87ac`。
- Hut 8官方7/20原HTML SHA256：
  `876846707d965a395b84a685f1355371864e57005a1d4ed3115acc612acb703f`；
  8/4財報稿：`5dd5a6ba19bde75372b8a39ab725d97fbd8429e8369a7f1d14ad47942c3e1b58`；
  6/9融資稿：`71cfa421cb7f7fd7b819e4e99b7ced046666221714bdd1b782374a874a989352`。
  文章部分正文藏在公開HTML的`__NUXT_DATA__` JSON，經解碼text spans並由第二位研究者
  獨立重解原HTML核對，沒有執行網頁JavaScript或改用媒體摘要補段落。
- SEC原始HTTP取得403，採已讀的官方web工具文字，明示不是完整原始附件。
  `beacon_web_extracts.json` SHA256：
  `c19bf9afde5d6666dfc66a4dc344034f1a7626ffb7e7b910d465aebabc14b905`。
  SEC官方filing index為8/4，accepted為8/4 06:31:13，報告期6/30；全文p.27、49、52、66
  逐段核對融資、兩期狀態與後續事件。接受日與報告期分開保存。
- 核對兩期各352 MW IT、園區1,000 MW公用電力容量；一期42.5億美元債券用途、第二期
  8/4仍在尋求融資；一期2027Q1初次通電、2027Q3初次資料廳交付與二期2028Q2均為
  公司預期。未計算容量差、能效、資金回收期或供應商收入；SE/t不適用。
- 後續索引實開可見8/10公開信；信中仍為開發規劃，沒有代填交付驗收。
  索引原HTML SHA256：`a16cf790bf1d6c0e1dc1c24ca2208be7b80fdce04367ec1a394a07ed96d03e2f`。
  所有取得方式與衍生文字SHA清單在`tmp/institutional-articles-20260910/`；
  `tmp/beacon-independent-qc.md`記錄離線複核範圍、11個payload重算與0444模式。
  這是基本來源驗證，不是正式focused公司筆記簽核。
- `beacon-final-check`：macOS26.6.2 arm64、預設Python3.11.11（UTF-8 mode0，未設
  PYTHONUTF8）下692項測試、六lint及隔離build通過，正式DB與既有archive雜湊不變。
  新文章必需的白話導覽及閱讀路線已補齊；測試保留歷史文章下限、原財務閱讀骨架順序，
  並繼續要求全部現行圖譜只在正式路線出現一次、全部文章都有精確問題入口。
- Headless Chrome 1440／390／320px實開文章及表格，無JS錯誤或水平溢出；已目視
  桌機與手機，手機表格依現有樣式逐列呈現。最後依複核將第二期時程標明來自8/4季報。
