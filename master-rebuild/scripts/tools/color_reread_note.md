# 花色（分類）の読み直し（決め方）

宿根草916品種のマスター（北海道広尾町の生産者）。文献の値と文から、花色（分類）を1品種ずつ決め直す。
**推測で値を作らない。品種名（'Alba' など）や今のマスターの値だけで決めない。当てはまる文献の値がなければ null。**

## 入力（1行1品種の JSON）
- Walters・品種: 米国の生産者の品種ページの Flower Colour（英語の語。品種の値）
- Gaißmayer: ドイツのナーサリーの花色（ドイツ語）。段階（品種／種）と「品種に使う」（true なら使ってよい。false は種のページを品種に当てた分なので使わない）
- RHS・品種: 英国王立園芸協会の FlowerColour（季節ごとの色。品種の値）
- stauden.de: ドイツの宿根草生産者協会の Blütenfarbe など。値の後ろ（cultivar／species／genus）が段階
- MBG: ミズーリ植物園の Bloom Description と段階（品種／種／属）
- Jelitto: 種苗会社の花色と段階
- 文: 花と色の語を含む文（[文献・段階]）
- 今のマスター: 今のマスターの花色（自社の値。比べるためだけに使う）
- 今の値: いまの表の 花色（分類）・花色（文献の語）・花色（自社の値）。今の値の文献

## 決め方（trial/RULES.md・DECISIONS.md）
- 分類は 赤／ピンク／青・紫／オレンジ・アプリコット／黄／白／その他 から（複数可。主な色の順）
- 使うのは品種の値だけ（段階＝品種）。種・属の値は使わない。ただし商品が種そのもの（品種名なし、「品種名あり」が false）なら、種の値も使ってよい
- 文献の順：Walters・品種 → Gaißmayer（品種に使う＝true）→ RHS・品種 → stauden.de（cultivar）→ MBG（品種）→ Jelitto（品種）。最初に値のある文献を採る。採らなかった文献と分類が食い違えばメモに書く
- 花びら（舌状花・苞を含む、観賞する部分）の色で決める。エキナセア・ルドベキアの中心（cone, disk の Brown・Orange）は数えない（花びらが別の色のとき）
- 花が目立たない・観賞しない（グラスの穂の Green・Brown・Bronze・Beige、葉を観賞する品種の目立たない花）は ["その他"]。ただし文献が花色をはっきり（White, Pink など）書いていれば、その色
- 語の対応：
  - 白：White, Cream, Ivory, weiß, cremeweiß
  - ピンク：Pink, Light Pink, Deep Pink, Rose, Magenta, Salmon pink, rosa, pink, lachsrosa, karminrosa
  - 赤：Red, Crimson, Scarlet, Burgundy, Maroon, Wine, rot, karminrot, weinrot, dunkelrot
  - 青・紫：Blue, Purple, Violet, Lavender, Lilac, Mauve, blau, violett, lila, purpur, lavendel, blauviolett
  - 黄：Yellow, Gold, Lemon, gelb, goldgelb, zitronengelb
  - オレンジ・アプリコット：Orange, Apricot, Peach, Coral, Salmon（ピンクでないとき）, orange, aprikose
  - その他：Green, Brown, Bronze, Beige, Silver（花の色として）、grün, braun
  - 2色（gelb mit rot、bicolor）は両方。「Mixed」（色の混ざった株）は、ほかに書いてある色だけ
- 「今のマスター」や品種名と、文献の分類がはっきり違う（例：マスター 白、文献 Pink。'Alba' なのに Blue）なら、値は文献のまま、「食い違い」に書く（どちらが正しいかは決めない）
- 文献に値がなく、今のマスターだけのときは null（自社の値は別の列に残っている）

## 出力
1品種1行の JSON（JSON Lines）。全品種を書く（今と同じでも書く）。
{"商品番号": …, "花色": ["白", …]|null, "決め手": "[文献・段階] 原語", "今と違う": true|false, "食い違い": "今のマスター・品種名・ほかの文献との食い違い（なければ null）", "確かさ": "高|中|低", "メモ": "今と違う理由・迷った点（日本語、短く）"}
- 今の値の 花色（分類）と比べて「今と違う」を決める（並び順の違いだけなら false）
- 迷ったら、いちばんよい読みを書いて 確かさ を 低 にし、メモに理由
