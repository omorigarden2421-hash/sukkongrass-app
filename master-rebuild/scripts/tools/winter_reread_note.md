# 冬の手入れの作り直し（文献から事実を抜き出す）

宿根草916品種のマスター（北海道広尾町の生産者）。「冬の手入れ（北海道）」「冬の手入れ（温暖地）」の文を、文献から作り直す（ユーザー「文献から作り直して」2026-11-26）。
この段階では文を書かない。**文献に書いてある冬の手入れの事実だけ**を、決まった項目に抜き出す。文はあとでこちらが、抜き出した事実と、別に読み直した常緑性・土壌水分・耐寒性を組み合わせて作る。
**推測で値を作らない。品種名・今のマスターの文だけで決めない。書いていなければ null。**

## 抜き出す項目
1. 秋の地上部（秋〜冬に向けて、地上部をどうするか）
   - 「秋に切る」：cut back in fall/autumn、cut to the ground after frost、remove foliage in late autumn、Rückschnitt im Herbst
   - 「春まで残す」：leave stems/foliage over winter、for winter interest、seed heads for birds、protects the crown、cut back in late winter / early spring（＝冬は残す）、Rückschnitt im Frühjahr
   - 「切らない」：常緑で、秋も冬も刈り込まない（evergreen; do not cut back; just tidy / remove dead leaves）
   - 「どちらでも」：fall or early spring、in late autumn or early spring
   - null：書いていない
2. 春の手入れ（春先にすること。短い日本語。例「早春に古い茎を地際で切る」「傷んだ葉・枯れ葉だけ取る」「早春に新芽が出る前に刈り込む」「花後ではなく春に軽く刈り込む」）。null 可
3. 防寒（冬の寒さへの備え）
   - 「必要」：文献が冬の防寒・マルチ・覆いを勧める（apply a winter mulch、protect in winter、needs winter protection、Winterschutz empfohlen）
   - 「寒冷地で必要」：寒い地域・北の地域・寒さの境目のゾーンでだけ勧める（mulch in colder zones / in the northern part of its range / in zone 5）
   - 「不要」：防寒はいらないとはっきり書く（no winter protection needed、kein Winterschutz nötig）
   - null：書いていない（「hardy」「winterhart」だけなら null。耐寒性の値は別の列で見る）
4. 冬の過湿（冬の湿りへの注意）
   - 「注意」：winter wet、wet soils in winter、crown rot in wet winter、Winternässe、does not tolerate wet feet in winter、Staunässe im Winter など、冬の湿りで傷むとはっきり書く
   - null：書いていない（ふつうの「well-drained soil」だけなら null。土壌水分は別の列で見る）
5. 冬の姿（冬の地上部の様子で、文献に書いてあるもの。短い日本語。例「冬は地上部が枯れる」「冬も葉が残るが傷みやすい」「冬に葉が赤く色づく」）。常緑性の値そのもの（Evergreen など）だけなら書かない（常緑性は別に読み直し済み）。null 可
6. 雪・寒冷地の記述（snow cover、北海道・寒冷地・東北での越冬についての文。おぎはらの文も可）。短い日本語。null 可

## 文献の段階と順
- 冬の手入れは種でほぼ共通なので、品種のページを優先し、なければ**種のページも使ってよい**。属のページ・RHS の [Genus] の文は使わない
  - 例外：常緑かどうかに関わる文（冬の姿）は品種で違うことがあるので、品種のページを優先し、種のページの文を使うときはメモに書く
- 文献の順（DECISIONS.md の順位。耐寒・越冬に関わる 防寒 は シカゴ植物園 > RHS > …、ほかは RHS → NC State → MBG → Walters → Gaißmayer → stauden.de → おぎはら）。食い違うときは上を採り、食い違いに書く
- 剪定の文でも、花後の切り戻し（deadhead、cut back after flowering）は冬の手入れではない（別の列「切り戻しの方法」で扱う）。ただし「花後に切り、秋にもう一度地際で切る」の後半は 秋に切る

## 出力
1品種1行の JSON（JSON Lines）。全品種を書く。
{"商品番号": …, "秋の地上部": "秋に切る"|"春まで残す"|"切らない"|"どちらでも"|null, "春の手入れ": "…"|null, "防寒": "必要"|"寒冷地で必要"|"不要"|null, "冬の過湿": "注意"|null, "冬の姿": "…"|null, "雪・寒冷地": "…"|null, "段階": "品種"|"種"|"品種と種"|null, "決め手": "[文献・段階] 原語（短く引用）／…（項目ごとに）", "食い違い": "…"|null, "確かさ": "高|中|低", "メモ": "迷った点（日本語、短く）"}
