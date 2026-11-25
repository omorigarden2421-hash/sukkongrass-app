# 常緑性の読み直し（決め方）

宿根草916品種のマスター（北海道広尾町の生産者）。文献の値と文から、常緑性を1品種ずつ決め直す。
**推測で値を作らない。品種名や今のマスターの値だけで決めない。当てはまる文献の値も文もなければ null。**
この列は「文献（温暖地の値）」（DECISIONS.md：常緑性は1列・温暖地の値）。北海道で冬に雪の下で葉が傷むかどうかではなく、文献に書かれた性質をそのまま採る。

## 入力（1行1品種の JSON）
- RHS・品種: 英国王立園芸協会の品種ページの Foliage（Evergreen／Semi evergreen／Deciduous）と Hardiness
- stauden.de: ドイツの宿根草生産者協会の Blattphase（immergrün／wintergrün／sommergrün）など。値の後ろ（cultivar／species／genus）が段階
- Walters・品種: 米国の生産者の品種ページの Plant Uses & Characteristics のうち Evergreen など
- Gaißmayer: ドイツのナーサリーの値（冬・葉に関わるもの）と段階・「品種に使う」
- MBG: ミズーリ植物園の Type・Leaf など（段階）
- 文: 常緑・落葉・冬・地上部が枯れる などの語を含む文（[文献・段階]）。RHS・MBG・NC State・Gaißmayer・おぎはら など
- 今のマスター: 今のマスターの常緑性（自社の値。比べるためだけに使う）
- 今の値: いまの表の常緑性（文献の名前つき）

## 決め方
- 値は次の3つから **1つ**：常緑／半常緑／落葉
  - 常緑：Evergreen, immergrün, 冬も葉が残る・常緑
  - 半常緑：Semi-evergreen, semi evergreen, wintergrün（冬の間は葉が残り、春に入れ替わる）, 半常緑, 「寒い地域では落葉・暖かい地域では常緑」
  - 落葉：Deciduous, sommergrün, dies back/down in winter, 冬は地上部が枯れる, 冬季落葉
  - MBG の「Type: Herbaceous perennial」だけでは落葉にしない（常緑のヒューケラなども Herbaceous perennial。MBG は常緑なら Leaf: Evergreen・Semi-evergreen と書く）。MBG に Leaf の値がないことも、落葉の根拠にしない
- 常緑性は種でほぼ共通の性質なので、種の値・種の文も使ってよい（DECISIONS.md：種で共通の性質は使う）。ただし品種の値・文があれば品種を優先
- 文献の順：RHS → MBG・NC State（文）→ Walters → Gaißmayer → stauden.de → おぎはら などの文。最初に決まる文献を採る。ほかの文献と食い違えば「食い違い」に書く
  - 例外：RHS の値が Deciduous で、ほかの複数の文献が常緑・半常緑と書くときは、RHS のまま、食い違いに書いて 確かさ 低
- 文の中で「暖かい地域では常緑、寒い地域では落葉（evergreen in warm climates）」のように地域で変わると書かれていれば、半常緑
- 「冬に株元の葉（ロゼット）が残る」「basal leaves persist」だけなら 半常緑（迷ったら 確かさ 低）
- 「冬の傷み」「winter scorch」は常緑の葉が傷むことで、常緑を否定しない
- 今のマスターの値（常緑／半常緑／冬季落葉 など）と文献の値がはっきり違うなら、値は文献のまま、「食い違い」に書く（どちらが正しいかは決めない）
- 文献に値も文もなく、今のマスターだけのときは null

## 出力
1品種1行の JSON（JSON Lines）。全品種を書く（今と同じでも書く）。
{"商品番号": …, "常緑性": "常緑"|"半常緑"|"落葉"|null, "段階": "品種"|"種"|"属"|null, "決め手": "[文献・段階] 原語", "今と違う": true|false, "食い違い": "今のマスター・ほかの文献との食い違い（なければ null）", "確かさ": "高|中|低", "メモ": "今と違う理由・迷った点（日本語、短く）"}
- 今の値の常緑性（括弧の前）と比べて「今と違う」を決める
- 迷ったら、いちばんよい読みを書いて 確かさ を 低 にし、メモに理由
