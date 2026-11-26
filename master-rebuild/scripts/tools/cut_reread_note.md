# 切り花適性の読み直し（決め方）

宿根草916品種のマスター（北海道広尾町の生産者）。文献の値と文から、切り花適性を1品種ずつ決め直す。
**推測で値を作らない。品種名や今のマスターの値だけで決めない（花が大きい・茎が長い、だけで決めない）。当てはまる文献の値も文もなければ null。**

## 値（3つから1つ、または null）
- ◎：切り花としてよい・すぐれていると書く（good / excellent / superb / long-lasting cut flower、long vase life、prized for cutting、florists' favourite、MBG の「Good Cut」と本文の good cut flower がそろう など）
- ○：切り花に使える・使われると書く（cut flower の印〔Walters の Cut Flower、stauden.de の Schnittblume、NC State の Cut Flowers、MBG の Good Cut だけ〕、can be used as cut flowers、suitable for cutting、dried flowers／dried arrangements、cut stems、for vases、おぎはらの「切り花にも向く」など）
- △：切り花には向かない・もちが悪いと、はっきり書く（not suitable for cutting、short vase life、flowers drop/wilt quickly when cut など）
- null：上のどれもない

## 入力（1行1品種の JSON）
- RHS・品種：RHS のページの値で、cut・Schnitt などを含むもの（[項目名] 値）
- NC State・MBG：段階と、値・文で切り花に関わるもの
- Walters・品種：Cut Flower の印と、切り花に関わる文
- Gaißmayer：値（品種に使う＝その品種のページか、種の商品に当てた種のページ）
- stauden.de：段階と Verwendung（使い方。Schnitt を含めば切り花）
- おぎはら：段階、図鑑のメモ、楽天の値・文
- 今の値・今の値の文献・今のマスター：比べるためだけ

## 決め方
- 文献の段階：切り花は品種で変わるので、**品種名のある商品（品種名あり＝true）は品種のページの値・文だけ**を使う。種のページ・属のページは使わない（trial/RULES.md の cut_flower と同じ）
  - 品種名のない商品（品種名あり＝false）は、その種のページを使ってよい。属のページは使わない
  - stauden.de の値の後ろの（cultivar）／（species）、NC State・MBG の 段階、Gaißmayer の 段階／品種に使う、おぎはら の 段階 で見分ける
- 文献の順（DECISIONS.md の「その他」の順位）：RHS → NC State → MBG → Walters → Gaißmayer → stauden.de → おぎはら
  - ◎ と ○ の違い：どれか1つの文献が ◎ にあたる文を書いていれば ◎（ほかが印だけの ○ でも、食い違いにしない）
  - ◎／○ と △ が食い違うときは、上の文献を採り、食い違いに書く
- 「dried flowers」「seed heads for dried arrangements」も ○（ドライも切り花の使い方に含める）
- 葉だけを切って使う（foliage for arrangements）は ○。メモに「葉」と書く
- 迷ったら、いちばんよい読みを書いて 確かさ を 低 にし、メモに理由

## 出力
1品種1行の JSON（JSON Lines）。全品種を書く（今と同じでも書く）。
{"商品番号": …, "切り花": "◎"|"○"|"△"|null, "段階": "品種"|"種"|null, "決め手": "[文献・段階] 原語（短く引用）", "今と違う": true|false, "食い違い": "ほかの文献との食い違い（なければ null）", "確かさ": "高|中|低", "メモ": "今と違う理由・迷った点（日本語、短く）"}
- 「今と違う」は 今の値 と比べる（今のマスターとは比べない）
