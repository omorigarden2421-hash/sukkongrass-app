# 葉色（分類）の読み直し（決め方）

宿根草916品種のマスター（北海道広尾町の生産者）。文献の値と文から、葉色（分類）を1品種ずつ決め直す。
**推測で値を作らない。品種名（'Variegata'・'Aurea' など）や今のマスターの値だけで決めない。当てはまる文献の値も文もなければ null。**

## 入力（1行1品種の JSON）
- Walters・品種: 米国の生産者の品種ページの Foliage Color（英語。品種の値）
- RHS・品種: 英国王立園芸協会の FoliageColour（季節ごとの色をまとめた一覧。品種の値）
- stauden.de: ドイツの宿根草生産者協会の Blattfarbe・Blatt-Farbgruppe・MS-Blattfarbe・Blattschmuck・MS-Herbstfärbung など。値の後ろ（cultivar／species／genus）が段階
- Gaißmayer: ドイツのナーサリー（葉の値があれば）と段階・「品種に使う」
- MBG: ミズーリ植物園（段階）
- 文: 葉の語を含む文（[文献・段階]）。Gaißmayer・RHS・MBG・NC State・おぎはら などの文
- 今のマスター: 今のマスターの葉色主分類（自社の値。比べるためだけに使う）
- 今の値: いまの表の 葉色（分類）・葉色（自社の値）・葉の特徴・紅葉。今の値の文献

## 決め方
- 分類は次の7つから **1つ**：グリーン系／ゴールド・ライム系／ブルー系／シルバー系／パープル・ブラック系／ブロンズ・レッド系／斑入り
- 生育期（春〜夏）の主な葉の色で決める。秋の紅葉・冬の色だけの色は数えない（グリーン系のまま。メモに「紅葉」と書く）。新芽だけの色も数えない
- 斑（Variegated、白や黄の縁取り・筋・まだら模様、panaschiert, gelbbunt, weißbunt, gezeichnet）が品種の値か品種の文にあれば「斑入り」を優先（中心・葉脈の模様は除く。下を見る）
- RHS の品種名に「(v)」が付く品種（RHS が斑入りとしている）は「斑入り」。決め手は「[RHS・品種名] (v)」（ユーザーの決定 2026-11-25。読み直しの後に combine で当てる）
- 使うのは品種の値・品種の文だけ（段階＝品種）。種・属の値は使わない。ただし商品が種そのもの（「品種名あり」が false）なら種の値・文も使ってよい
- 文献の順：Walters・品種 → RHS・品種 → stauden.de（cultivar）→ 品種の文（Gaißmayer・MBG・NC State など）。最初に決まる文献を採る。ほかの文献と食い違えばメモに書く
- RHS の一覧に Green と別の色が並ぶとき：品種の文や stauden.de（cultivar）で、その色が生育期の葉の色とわかれば その色。秋の色（紅葉）とわかれば グリーン系。**わからなければ グリーン系**（確かさ 低。メモに「RHS に ◯◯ も並ぶ」）。RHS の別の色は穂・茎・花・紅葉の色のことがある（写真で確かめた。ユーザーの決定 2026-11-25）
  - RHS に Cream・White・Yellow と Green が並ぶだけでも、斑とは読まない（斑の語・文・stauden.de の zweifarbig／gefleckt などで確かめられるときだけ斑入り）
- ヒューケラ・ティアレラ・ヒューケレラなど、葉の中心や葉脈に色の模様がある葉は「斑入り」にしない。地の色（緑・黄金・銀・紫 など）で決める。Walters の Variegated もこの模様のことがあるので、文で地の色がわかれば地の色。斑入りは、白や黄の縁取り・筋・まだら模様（斑点を含む）だけ（ユーザーの決定 2026-11-25）
- 語の対応：
  - グリーン系：Green, Deep Green, Light Green, Dark green, grün, dunkelgrün, hellgrün, frischgrün
  - ゴールド・ライム系：Yellow, Gold, Golden, Chartreuse, Lime, gelb, goldgelb, gelbgrün
  - ブルー系：Blue, Blue-green, Glaucous, blau, blaugrün, graublau
  - シルバー系：Silver, Grey, Gray, Silvery Grey, grau, silber, graugrün（灰緑）, weißfilzig
  - パープル・ブラック系：Purple, Burgundy, Black, Plum, purpur, rotbraun（紫寄りのとき）, schwarz, dunkelrot（葉の色として）
  - ブロンズ・レッド系：Bronze, Red, Copper, Orange, bronze, rot, kupfer
  - 斑入り：Variegated, gelbbunt, weißbunt, panaschiert, gezeichnet（模様。品種の葉の色として）
- 「今のマスター」や品種名（'Variegata'・'Aurea'・'Purpurea'・'Glauca'・'Silver' など）と、文献の分類がはっきり違うなら、値は文献のまま、「食い違い」に書く（どちらが正しいかは決めない）
- 今のマスターの「⑧ 季節変化型」はこの分類にない。文献で決めた値と比べて、季節の色の変化（紅葉・新芽）が文にあればメモに書く
- 文献に値も文もなく、今のマスターだけのときは null（自社の値は別の列に残っている）

## 出力
1品種1行の JSON（JSON Lines）。全品種を書く（今と同じでも書く）。
{"商品番号": …, "葉色": "グリーン系"|…|null, "決め手": "[文献・段階] 原語", "今と違う": true|false, "食い違い": "今のマスター・品種名・ほかの文献との食い違い（なければ null）", "確かさ": "高|中|低", "メモ": "今と違う理由・迷った点・紅葉など（日本語、短く）"}
- 今の値の 葉色（分類）と比べて「今と違う」を決める
- 迷ったら、いちばんよい読みを書いて 確かさ を 低 にし、メモに理由
