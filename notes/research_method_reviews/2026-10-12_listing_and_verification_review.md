# 2026-10-12 研究循環：名單變動可以確認，整套部署仍要驗證

## 本輪結果與範圍

先pull到`6e32a76c00baad92a39d946a47bea57589c4fa9f`，核對前輪commit／push、research-watch與
Pages均完成，Pages也是同一SHA。既有未追蹤`.superdesign/`、stash、正式DB與archive保留。
十月完整方法回溯已於10/4完成；本輪新增增量快照，不重複記成月度回溯。

起始40個到期monitor（14個已逾工作期限）逐項留下40列有界回查：**1列既有正式pack完成
進度、2列限定來源內無新證據、37列待驗**。40是工作項目數，不是40次獨立實驗，也不是
40項原trigger通過。尤其共享OCP、NVIDIA、Micron與同一公司索引的review不可重複當驗收。
本轮沒有新反證，不代表論點全成立；未取到附件的項目不記成無新消息。

更新後42篇topic、887個active claim、781個active source、156個active monitor及883條
active edge；工作到期數0，但40篇topic與803條edge仍過期，可信度照舊自動降級。
累積541列review與181次scan（2 full／179 partial）。這些是10/12登錄檔的精確盤點，
不是抽樣估計，SE／t不適用；不報支持率、投資命中率或市場代表性。

## 更新一篇既有文章：PCIe清單21列，不能減19就說本月新增兩產品

實讀[PCI-SIG完整6.x區段](https://pcisig.com/developers/integrators-list)，按角色重數：
System 3、AIC 11、retimer 3、switch／bridge 4，共21列，皆列64 GT/s。
AMD EPYC 9006屬帶CEM插槽的System，x16、Date Added 10/5，識別碼與功能欄空白。
不同代理各自逐列重數一致；這是同一來源的獨立計數，不是三個獨立外部消息鏈。

新增S20、C27／C28；新增AMD公司列名線及接續產業線，只到`platform_listing`，材料性
只到`named_product`，集中度未知，不推成整機部署、收入、份額或台股受惠。C25、8/24
主證據時計及8/31原期限保持不變。T7／T9的完整配置、測項、互通分母與測試／送表日期
仍缺，兩列結果仍為待驗；新增可見列項只是旁支基準，不能拿來清除主命題過期狀態。

舊8/24的19列快照不改寫；當前Samsung 1763 E3列8/13，缺舊原始payload便不能把21−19
當成10月新增兩產品。另一排序取件管道回20列舊快取，也不能當名單撤回。直接取件403，
未保存原始HTML／SHA；S20只聲稱公開web文字當次觀察，明示可變性與取件限制。

新手段落把「具名成績單、考試範圍、整套客戶驗收」分開，補清單欄位中文解釋，讓讀者
能追問：是哪一塊板與韌體？哪些必要測項？與誰互通？何時由客戶驗收？10/19工作回查，
有正式結果可提前；更新已加入transition，首頁近期文章及研究中心一併重建。

## 到期工作與下一證據節點

| 範圍 | 本輪看到什麼、還缺什麼 | 下一工作 |
|---|---|---|
| 800V兩monitor | OCP索引有新配電白皮書但取件403／超限；NVIDIA公開白皮書pp11–17已目視，只有保護／隔離示意，缺同型號故障矩陣與驗收 | 10/15公開原始測試 |
| 玻璃T3 | SKC9/22仍是可靠度測試及POC準備；不是測試通過、量產良率或重複訂單 | 10/19同客戶產品結果 |
| 液冷qualification四項、loop三項 | 新PG25文字可見95頁、封面9/15，但未得可目視附件；CDU動態列項／曲線與場域COA未核 | 10/14附件；財務責任10/16 |
| 機櫃動作四項、信任根一項 | Redfish／OpenRMC方法不是兩家互通；SPDM的Q4目標、WIP與正式版分開，PDF未全驗 | 10/14；財務責任10/16 |
| Rubin、Helios、SPHBM4 | Rubin限定已讀頁無新共同配置；Azure空頁、JEDEC缺件不能当不存在 | 10/19具名配置與正式附件 |
| 記憶體六項、chiplet交付 | 角色、教學、XSD清單不等生產測試或兩工具signoff；不同case不可拼成同部署 | 10/19版本化原始結果 |
| AI capex、背面供電 | SEC403不等沒有申報；A16網址返回N2正文不能當A16結論 | 10/15準確附件 |
| Open AI fabrics、AI storage | scope及訓練儲存案例尚無同cluster六網絡／三路徑共同鍵 | 10/16設計與驗收資料 |
| 224G三項 | IEEE投票截止不等通過；OIF展示附件及COM輸入未核；材料產品矩陣不等客戶資格 | 10/16正式結果與原始配置 |
| EMC三項 | 方法、認證範圍及付費文件摘要不等實驗室可用能力或同配置passport | 10/19；公司文件10/16 |

來源入口與既有來源引用、實讀範圍、取件失敗、原工作期限及觸發／失效狀態逐筆留在monitor_reviews.csv。
上述下一日期都是人工工作期限，不是廠商交付承諾，不會改寫claim時計。

[OCP新PG25附件](https://www.opencompute.org/wp-content/uploads/2026/10/OCP-PG25-Guidelines-V1.0.0.pdf)
僅文本可取；網址的2026/10不是正式發布日。舊路徑404不等撤回。
[NVIDIA公開800V入口](https://www.nvidia.com/en-au/data-center/technologies/800-vdc-architecture/)
可連公開CDN，並非繞過另一登入連結；18頁payload SHA為
`08571f9ece9c9ded9b742a04e9314c7cc66377db752755fdeb694e3a7356a8d8`，只渲染引用pp11–17。
metadata2025-10-10及HTTP modified2026-09-22都不冒充正式發布日；不把重讀舊PDF當新市場事件。

## 正式筆記進度、財報索引與資料缺口

九家公司6271、3675、2327、2308、2337、3264、6239、6488、8261的MOPS115Q2索引本次
全成功；只證列檔存在，**本輪沒有重下載或重算這九家的財報PDF**。2327 AIA10/6之前已見，
不能再算本次新文件。Priority／Yageo兩項仍待驗，未替其他未查IR入口作完整負面判定。

Missed-priority T11原trigger是任一附件完成同版本pack與獨立reviewer。3264與6239正式
筆記在10/9已完成，兩篇各有相應manifest、不同drafter/reviewer、離線重算簽核及完整SHA；
本次只核本地登錄狀態、manifest及各自lint（各0錯誤／0警告），不是本輪重新獨立審財報。
因此追加1列行政進度`new_support`，引用既有Q2來源S21／S24，不刷新來源與主時計，不建重複文。
其餘2308、2337、6488、8261完整工作仍未完成，10/16接續。

已完成pack的登錄SHA：欣銓`4a1e1251a0ddfae98ddb2a742549521011b8f26c79065b14a234bb7fc3479bf9`；
力成`4944f4deb594157a785db9ee7be51d34fb28fcbcbe82bedf010aaa001a4a0b0d`。
7篇source_internal衝突（1560、2344、2421、2428、2472、2478、6643）未重新核PDF，不清除
conflicted，亦不以lint代替財務覆核。

事件扫描10/10–10/12：TWSE／TPEx的10/12批次各只見10/11發言，缺10/10及10/12；
universe命中0不證全窗口無公告，維持partial。121檔115Q2損益／資產負債各121與配對121
只是索引盤點，不是財報已審，也不把它們當獨立樣本。

[10/12財報Actions](https://github.com/DennisLiuCk/strong-weak-scanner/actions/runs/38196761212)
原log顯示九月營收仍缺9：5328、2481、5425、3711、6451、3661、3532、5439、2308。
12日首抓未啟用`--require-latest-month-complete`，17日既有重驗才硬驗最新月份完整，故本次
綠色CI不能當完整性聲明。10/17依既有排程重驗；本輪不寫DB、不手動重抓或改每日策略。
10/10另案daily快照問題本輪未重查，不沿用舊失敗當今日仍失敗的結論。

## 方法修正與候選

動態索引允許同URL新捕捉另存source ID，但限定不同日期、不同實讀定位、相同明確來源群組。
文件型來源／同日副本／不同群組仍拒絕，兩個不同URL及獨立群組門檻不降低。舊捕捉及
append-only帳本受baseline保護；未讀到新證據不應只更換日期來延長期限。

獨立程式審查找到反例：同URL的兩次捕捉加上未被claim引用的第二網址，可繞過原先按ID
計的實引來源門檻。現已在全局與active claim實引兩處按canonical URL去重，加入乾淨
反例回歸；主命題獨立群組與時計路徑沒有因此放寬。

追加「逐列重算而非跨輪總數相減」與「截止不等於正式結果」檢查。本次的同來源重數能
檢驗盤點，不能驗證產業因果；模擬、規格、列表、資格、量產與財務仍逐階分開。

三題原凍結排序、知識價值、第一拒絕不變；玻璃只接續10/19，SSCB／HBFSim仍10/15。
[Astera10/8 Aries7](https://ir.asteralabs.com/news-releases/news-release-details/astera-labs-announces-aries-7-industrys-first-pcie-7-signal)
只作下一輪線索，Q4預計送樣不是已量產；10/16回查OCP展示與原始測試後才決定是否值得
另行凍結。沒有為湊篇數升格，也沒有由供應鏈鄰接增加收入線。

本輪主張追蹤流程約束證據邊界，表格流程保存CSV結構與歷史，寫作流程同步新手可讀性。
新增回歸保護本輪40項、主時計、圖譜成熟度、候選凍結及首頁更新。

## 發布前驗證收據

Windows 11 10.0.26200、系統Python3.12.10：預設`utf8_mode=0`／`PYTHONUTF8`未設，
與`PYTHONUTF8=1`／`utf8_mode=1`各執行865項測試，864通過、1略過。最終兩輪
prepublish的notes、hypotheses、topic歷史、graph、radar、method歷史與隔離build皆exit0；
正式DB及65份archive SHA未變。Topic仍有42 warnings：40篇過期與2項既有術語提醒，
不把零errors寫成零警告。

本地收據分別在`tmp/prepublish/20261012-default-final/verification.json`與
`tmp/prepublish/20261012-utf8-final/verification.json`，兩者ok及protected_unchanged均true。
起始40項母體與新增40列精確吻合、snapshot為LF；原帳本、來源與主時計通過完整baseline
`6e32a76c00baad92a39d946a47bea57589c4fa9f`歷史檢查。早期測試抓出的字典、source／claim／edge
硬計數已按本次實際增量同步，並非刪除測試或放寬閱讀品質。

另從實際生成HTML抽取payload，首頁近期文章含PCIe修訂日10/12，研究中心含相同文章、
AMD新圖譜線與10/12方法快照；行情資料日仍10/8，沒有把研究更新冒充新交易日資料。
本輪獨立QA確認PCIe逐列盤點及40項帳本／快照一致，並修正實引來源去重漏洞。
