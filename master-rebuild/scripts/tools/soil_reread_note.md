# 土壌水分の読み直し（決め方）

宿根草916品種のマスター（北海道広尾町の生産者）。欧米の文献の値と文から、土壌水分（好む土の湿り）を1品種ずつ決め直す。
**推測で値を作らない。品種名や今のマスターの値だけで決めない。当てはまる文献の値も文もなければ null。**
乾燥への強さ（乾燥耐性）は別の項目。ここでは「どんな湿りの土を好むか・耐えるか」だけを決める。

## 値（5つから1つ）
- 乾燥寄り：乾いた土を好む・乾いた土でよく育つ（dry, dry to medium, dry soils）
- 適湿：ふつうの湿り・湿り気があり水はけのよい土（moist but well-drained, medium, average）
- 湿潤寄り：いつも湿った土・湿地・水辺（moist to wet, consistently moist, wet, boggy, pond/stream margins）
- 排水必須：水はけが悪いと傷む・枯れる（sharp drainage essential, must be well-drained, rots in wet soil, intolerant of wet/poorly drained soil, winter wet is fatal）
- 幅広く適応：乾いた土から湿った土まで幅広く育つ（dry から wet まで、と書いてある）

## 入力（1行1品種の JSON）
- RHS・品種：Moisture（土の湿り）と Soil
- NC State：土に関わる項目（Soil Drainage など）と段階
- MBG：Water と段階、Tolerate（Wet Soil・Drought など）
- Walters・品種：Soil Moisture
- Gaißmayer：ドイツのナーサリーの値（湿り・水はけに関わるもの）
- stauden.de：Bodenfeuchte（trocken／frisch／feucht／nass）・Lebensbereich（Fr・GR・St・FS・WR〔水辺〕・W〔水〕など）・Bodenstruktur
- 文：drain・wet・moist・dry・bog などを含む文（[文献・段階]）
- 今の値・今の値の文献・今のマスター：比べるためだけ

## 値の読み方（項目の値）
- RHS Moisture
  - Well-drained だけ → 排水必須
  - Moist but well-drained だけ → 適湿
  - Moist but well-drained or Well-drained → 適湿
  - Poorly-drained を含み、Well-drained を含まない → 湿潤寄り
  - Poorly-drained と Well-drained の両方を含む → 幅広く適応
- NC State Soil Drainage（段階が「属」なら使わない）
  - Occasionally Dry・Very Dry があり、Moist・Wet の語がない → 乾燥寄り
  - Occasionally Wet・Frequent Standing Water・Wet などがあり、Dry の語がない → 湿潤寄り
  - Dry の語と Wet の語の両方 → 幅広く適応
  - Good Drainage・Moist だけ（Good Drainage だけも）→ 適湿（排水必須は文ではっきり書くときだけ）
- MBG Water：Dry／Dry to medium → 乾燥寄り、Medium → 適湿、Medium to wet／Wet → 湿潤寄り
  - Tolerate に Wet Soil があり Drought（または Dry Soil）もある → 幅広く適応
- Walters Soil Moisture：Wet と Dry の両方 → 幅広く適応。Wet（Dry なし）→ 湿潤寄り。Dry（Moist・Wet なし）→ 乾燥寄り。それ以外（Average・Moist、Dry と Moist）→ 適湿
- stauden.de Bodenfeuchte：trocken だけ → 乾燥寄り。frisch がある（trocken と並ぶのも）→ 適湿。feucht・nass がある（trocken なし）→ 湿潤寄り。trocken と feucht／nass の両方 → 幅広く適応。Lebensbereich の WR（Wasserrand）・W・SU（Sumpf）は湿潤寄りの手がかり

## 決め方
- 同じ文献の中では、はっきりした文が項目の値より優先（例：MBG の Water: Medium でも、文に「good drainage is essential, wet soils in winter cause crown rot」→ 排水必須）
- ただの「well-drained soil」「prefers moist, well-drained soil」は 適湿（排水必須にしない）。排水必須は、水はけが悪いと傷む・枯れる・必須、とはっきり書くときだけ
- 「tolerates wet soil」「tolerates a wide range of soils, from dry to wet」→ 幅広く適応（乾燥寄り・適湿の値もある文献でも）
- 文献の段階：品種の値・文を優先。なければ種の値・文も使ってよい（土の好みは種でほぼ共通。DECISIONS.md「種で共通の性質（土など）は使う」）。属だけの文は使わない（属のほとんどに当てはまると書かれていても使わない）
- 文献の順（DECISIONS.md の「その他」の順位）：RHS → NC State → MBG → Walters → Gaißmayer → stauden.de。いちばん上の文献で決まればそれを採り、ほかの欧米の文献と違えば「食い違い」に書く
  - ただし、上の文献が 適湿（ふつうの値）で、下の文献が水はけ・湿地について はっきりした文（排水必須 または 湿潤寄り）を書くときは、そちらを採ってよい。確かさ 中、食い違いに書く
  - 1つの文献の中で割れるとき（例：bog garden にもよいとしながら sharp drainage を求める）は、いちばんよい読みを書き、確かさ 低
- 迷ったら、いちばんよい読みを書いて 確かさ を 低 にし、メモに理由

## 出力
1品種1行の JSON（JSON Lines）。全品種を書く（今と同じでも書く）。
{"商品番号": …, "土壌水分": "乾燥寄り"|"適湿"|"湿潤寄り"|"排水必須"|"幅広く適応"|null, "段階": "品種"|"種"|null, "決め手": "[文献・段階] 原語（短く引用）", "今と違う": true|false, "食い違い": "ほかの欧米の文献との食い違い（なければ null）", "確かさ": "高|中|低", "メモ": "今と違う理由・迷った点（日本語、短く）"}
- 「今と違う」は 今の値 と比べる（今のマスターとは比べない）
