# 乾燥耐性の読み直し（決め方）

宿根草916品種のマスター（北海道広尾町の生産者）。欧米の文献の値と文から、乾燥耐性（強／中／弱）を1品種ずつ決め直す。
**推測で値を作らない。品種名や今のマスターの値だけで決めない。当てはまる文献の値も文もなければ null。**

この読み直しで決めるのは「欧米の文献の値と文からの値」だけ。次のものは、読み直しの後にこちらで機械的に当てる（ここでは使わない）：
- おぎはら（楽天のページの耐乾性・図鑑の文）：欧米の文献で決まらないときだけ使う（DECISIONS.md 2026-11-21）
- NC State の Resistance To Challenges（Drought・Dry Soil）と RHS の Drought Resistance: Yes：決まらないときだけ 中（2026-11-21）
- MBG の Water: Medium：それでも決まらないときだけ 中（推定。2026-11-23）
- RHS の Moisture（Well-drained など）・Walters の Soil Moisture・stauden.de の土の湿り：土の湿りの好みで、乾燥への強さではないので使わない

## 入力（1行1品種の JSON）
- MBG: ミズーリ植物園の Tolerate（Drought があるか）・Water と段階
- Walters・品種: 米国の生産者の品種ページの「Drought Tolerant」の印
- RHS・品種、NC State の Resistance To Challenges、stauden.de、おぎはら楽天：上のとおり、ここでは使わない（参考）
- Gaißmayer: ドイツのナーサリーの値（乾燥・水に関わるもの）
- 文: drought・dry・moist・trocken などを含む文（[文献・段階]）。RHS・MBG・NC State・Gaißmayer・Walters・おぎはら など
- 今の値・今の出どころ・今の値の文献：いまの表の値（比べるためだけ）

## 決め方
- 値は 強／中／弱 から1つ
  - 強：MBG の Tolerate に Drought／Walters の Drought Tolerant／文の「drought tolerant」「tolerates drought」「drought resistant」「very drought tolerant」「tolerant of dry soils」「trockenheitsverträglich」など、乾燥に強いとはっきり書く文（「once established」付きでも 強）
  - 中：「tolerates some drought」「some drought tolerance」「moderately/somewhat drought tolerant」「tolerates occasional/short periods of drought」「tolerates dry shade（乾いた日陰に耐える）」など、ある程度は耐えるという文
  - 弱：「intolerant of drought/dry soils」「does not tolerate drought」「never let dry out」「must not dry out」「keep consistently moist」「needs regular water/watering in dry periods（乾くと傷む・枯れる）」「wilts/scorches in dry soil」など、乾燥に弱いとはっきり書く文
- 「moist soil を好む」「prefers moist, well-drained soil」「average, medium moisture」だけなら値にしない（好みで、乾燥への強さではない）
- 「water during dry periods」「water regularly the first season（植え付け後）」だけなら値にしない（ふつうの手入れ）
- 文献の段階：品種の値・文を優先。なければ種の値・文も使ってよい（乾燥への強さは種でほぼ共通）。属だけの文は、属のほとんどに当てはまると書かれていなければ使わない
- 文献の順（DECISIONS.md の「その他」の順位）：RHS → NC State → MBG → Walters → Gaißmayer → stauden.de。同じ段階で食い違うときは、この順の上を採り「食い違い」に書く
  - ただし、同じ文献が「drought tolerant」と「keep moist / does not like to dry out」の両方を書くなど、1つの文献の中で割れるときは 中、確かさ 低
- おぎはらの文は使わない（後で当てる）。おぎはらと違っても「食い違い」には書かない
- 迷ったら、いちばんよい読みを書いて 確かさ を 低 にし、メモに理由

## 出力
1品種1行の JSON（JSON Lines）。全品種を書く（今と同じでも書く）。
{"商品番号": …, "乾燥耐性": "強"|"中"|"弱"|null, "段階": "品種"|"種"|"属"|null, "決め手": "[文献・段階] 原語（短く引用）", "今と違う": true|false, "食い違い": "ほかの欧米の文献との食い違い（なければ null）", "確かさ": "高|中|低", "メモ": "今と違う理由・迷った点（日本語、短く）"}
- 「今と違う」は 今の値 と比べる
