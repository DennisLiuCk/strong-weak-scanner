# 供應承諾與供應商現金的定向回查

本輪於獨立提交39d7d3b凍結研究問題後，核對NVIDIA與Amkor、矽品、景碩官方原稿。
新增內容放回既有區域化文章，沒有另建重複文章；原active radar的三項未成熟候選不重排。
本檔是定向工作結果歷史，不替尚缺的同案實收、驗收及收入補證。

<!-- research_radar
schema_version: 2
radar_id: RADAR-2026-11-21-01
as_of: 2026-11-21
next_review: 2026-11-30
status: retired
method: 深研前單獨凍結一個問題，再核買方與供應商同案角色及條件；新增來源只補既有文章，不以雙方合作稿充當兩筆獨立驗收，不以金額或倍率排名
selection_cycle_id: RS-2026-11-21-01
-->

<!-- research_candidate
candidate_id: RC-SUPPLY-COMMITMENTS-TO-SUPPLIER-CASH
rank: 1
title: 多年供應承諾何時成為供應商現金與收入
group_ids: packtest
reader_group_questions: packtest => 同一協議的承諾、預付款、客戶驗收與封測服務收入，哪些已能對上？
reader_question: 買方和供應商都宣布合作，是否就代表資金及收入已經到位？
reader_starting_point: NVIDIA與供應商的原稿讓美韓台合作範圍更明確。目前還缺同一契約的實收、驗收及收入調節，兩方具名不能代替財務橋接。
reader_terms: 預付款 => 客戶在交付前提供的款項，收款與收入認列是不同事件 | 包含關係 => 一個公布總額究竟已涵蓋哪些舊協議，防止重複相加 | 同案調節 => 用相同契約與期間核對承諾及實際履行的差異
reader_next_step: 先讀文章的跨區合作更新，11/30回查Amkor正式申報的總額組成、實收及抵服務費條件，再追同產品驗收與收入。
priority: p1
knowledge_value: high
status: expand_existing
evidence_posture: preliminary
why_now: NVIDIA與供應商已公開美韓台具名合作安排，足以補上角色與契約版本的判讀；仍沒有逐案收款、交付及收入共同鍵。
knowledge_gain: 新增C22至C26分開Amkor協議總額、SPIL先進封裝與景碩載板角色；同一買方跨區配置不能直接推導互補、替代或台股財務受惠。
first_rejection: 若只有買方公告而無同一契約的供應商角色或條件，僅保留買方陳述；即使雙方具名也不能把承諾額當已收現或收入，未有交付及財務橋接就不新增台股財務受惠線。
next_evidence: 核對NVIDIA原稿與Amkor及台灣供應商一手文件的契約主體、日期、預付款與專用產能範圍，區分簽約、實付、驗收及收入；按既有文章缺口決定增補或保留觀察。
next_check: 2026-11-30
route: expand_existing_article
article_topic_id: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION
graph_id: us-advanced-packaging-regionalization
sources: NVIDIA 11/17供應承諾 => https://nvidianews.nvidia.com/news/nvidia-expands-commitments-with-supply-chain-partners-to-support-ai-infrastructure-buildout | Amkor 10/21美韓協議 => https://ir.amkor.com/news-releases/news-release-details/amkor-technology-and-nvidia-advance-strategic-partnership-ai | SPIL 11/18台灣先進封裝 => https://www.spilglobal.com/NewsDetail/63c1aba5d14bac8c | 景碩11/18載板合作 => https://www.kinsus.com.tw/en/news/newsroom/detail/news_category1/news_20261118
-->

## 判定與尚未接受的推論

同案供應商角色已有可定位文字，故可增補既有文章。財務歸因門檻未達，沒有新增台股財務受惠線。
Amkor的總額約數與原分項沒有精確調節，不自行補齊差額；SPIL先進封裝不是光引擎，景碩載板不是
全公司產能。雙方公告互相連結且共用引述，保守歸同一消息群。Amkor與景碩本地取件分別403／401，
閱讀服務取得官方正文；原件取得與文字已讀分開保存，未宣稱完整離線包。

主命題C18、last_reviewed_at及review_due保持不變；新增T10於11/30追Amkor協議到收款履約的共同鍵。
其他舊monitor依原回查帳本排程，本次不是它們的新支持或提前結案。
