# 蜜源価値の読み直し（決め方）

宿根草916品種のマスター（北海道広尾町の生産者）。文献の値と文から、蜜源価値（ハチ・チョウなど花に来る虫にとっての価値）を1品種ずつ決め直す。
**推測で値を作らない。品種名・花の形・今のマスターの値だけで決めない。当てはまる文献の値も文もなければ null。**

## 値（3つから1つ、または null）
- ◎：虫をとてもよく呼ぶと書く（RHS の Plants for Pollinators〔RHS Plants for Pollinators の印・バッジ〕、bee magnet、butterfly magnet、highly attractive to bees/butterflies、a favourite of bees、excellent nectar source、stauden.de・Gaißmayer の「Bienenweide」「sehr gute Insektenweide」「Bienen- und Schmetterlingsmagnet」など）
- ○：虫を呼ぶ・蜜源になると書く（attracts bees / butterflies / pollinators、NC State・MBG の Attracts に Butterflies・Pollinators・Bees、Walters の Attracts Butterflies・Attracts Bees の印、stauden.de の Insekten・Bienen の値、nectar source、おぎはらの「蜜源」「チョウが来る」など）
- △：虫があまり来ない・蜜がないと、はっきり書く（double flowers have no nectar/pollen、sterile flowers offer little to pollinators、not attractive to bees など）
- null：上のどれもない

## 入力（1行1品種の JSON）
- RHS・品種：RHS のページの値で、pollinator・bee などを含むもの（[項目名] 値）
- NC State・MBG：段階と、値・文
- Walters・品種：印（Attracts Butterflies など）と文
- Gaißmayer、stauden.de（段階と値。Verwendung は全部入れてある）、おぎはら（段階・図鑑のメモ・楽天）
- 今の値・今の値の文献・今のマスター：比べるためだけ

## 決め方
- 文献の段階：虫を呼ぶかは種でほぼ共通なので、品種のページを優先し、なければ**種のページも使ってよい**（trial/RULES.md の pollinator と同じ）。属のページは使わない
  - ただし、品種のページが「八重咲きで蜜・花粉がない」「不稔」など、その品種だけ虫を呼ばないと書くときは、種のページより品種のページを採る（△ または null。メモに理由）
- ハチドリ（hummingbird）だけ、鳥（birds）だけ、シカ・ウサギの文は蜜源ではない（日本にハチドリはいない）。ハチ・チョウ・ガ・アブ・pollinators の記述だけを見る
- 害虫（aphids、beetles などが付く）や beneficial insects の住みかの話は蜜源ではない。ただし「attracts beneficial insects（花に来る益虫を呼ぶ）」は ○
- 文献の順（DECISIONS.md の「その他」の順位）：RHS → NC State → MBG → Walters → Gaißmayer → stauden.de → おぎはら
  - ◎ と ○ の違い：どれか1つの文献が ◎ にあたる値・文を書いていれば ◎（ほかが ○ でも食い違いにしない）
  - ◎／○ と △ が食い違うときは、上の段階（品種）・上の文献を採り、食い違いに書く
- 迷ったら、いちばんよい読みを書いて 確かさ を 低 にし、メモに理由

## 出力
1品種1行の JSON（JSON Lines）。全品種を書く（今と同じでも書く）。
{"商品番号": …, "蜜源": "◎"|"○"|"△"|null, "段階": "品種"|"種"|null, "決め手": "[文献・段階] 原語（短く引用）", "今と違う": true|false, "食い違い": "ほかの文献との食い違い（なければ null）", "確かさ": "高|中|低", "メモ": "今と違う理由・迷った点（日本語、短く）"}
- 「今と違う」は 今の値 と比べる（今のマスターとは比べない）
