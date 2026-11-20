# Gaißmayer（s17）: 在庫のない1品種の属19（アゲラティナからバレリアナまで）。batch_18/input の19属。
# 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。17個目のまとまり（batch_17）の分と同じときに続けて読んだ（探し方・読み方は batch_17/gaissmayer_data.py の冒頭）。
#   サイト内検索: 属名19個と Eupatorium・Epilobium・Chamaenerion → 一致した商品ページ ?static 10ページ。このまとまりの間は確認画面は出なかった。
# 本文は先頭の約600字だけを見ている。質問への回答は読んでいない。価格・在庫は写していない。
# Gaißmayer の書き方: 'Chocolate' は Ageratina altissima 'Chocolate'（育種者 Bruce〔英国〕1989）、オルラヤは種子の商品（Saatgut: Orlaya grandiflora。ゾーンの欄はない）。
# 【要確認】テンニンソウの黄金葉（Ls01）に Leucosceptrum japonicum 'Golden Angel' のページを当てた（Jelitto が f. aureum の流通名として 'Golden Angel' を書いているため）。
# 掲載なし・当てていないもの: セラスチウム（'Silberteppich' は品種のページなので当てていない）、ヤナギラン（'Stahl Rose'・'Album' だけ）、スズラン（Convallaria majalis とその品種だけで、種が違う）、
#   コリダリス 'Silver Spectre'、グロブラリア トリコサンタ（punctata だけ）、ペロフスキア（'Blue Spire'・'Little Spire'・'Filigran'・'Lacey Blue' は品種のページなので当てていない）、
#   セリ・プロスタンテラ・セリナム（検索で該当なし）。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-20"
S3 = "sonnig, absonnig, halbschattig"
KG = "keine Gefahr"
RG = "relativ geringe Gefahr"
GAISS = {
 "Af01": (8035, "Ageratina altissima 'Chocolate'", "cultivar", "weiß", "VII–X", "80 cm–100 cm", S3, "Fr/GR2-3b/WR4", "Z5", RG, "Bruce (Großbritannien) 1989",
          {"Blattfarbe": "rot", "Schnittgeeignet": "ja"},
          [("soil", "Die Staude ist sehr anpassungsfähig: sie bevorzugt frische bis feuchte, lehmig-humose, nährstoffreiche Böden - kommt allerdings auch mit zeitweise "
                    "trockenen Standorten gut zurecht."),
           ("native_range", "In Nordamerika wächst diese Pflanze in lichten Wäldern oder Gebüschen.")]),
 "Tn01": (12133, "Anthemis tinctoria 'Alba'", "cultivar", "reinweiß", "VI–IX", "50 cm–60 cm", "sonnig", "B/Fr1", "Z6", RG, None, {"Duftend": "ja", "Schnittgeeignet": "ja"},
          [("soil", "Wie alle Anthemis-Vertreter ist auch die Sorte 'Alba' ein Trocken-Held an sonnigem Standort."),
           ("pruning", "Wer die Triebe nach der Blüte auf die Hälfte einkürzt, verlängert die Lebensdauer der Staude."),
           ("self_seed", "Auch die – übrigens samenechte – Versamung lässt sich auf diese Weise besser steuern.")]),
 "Cp01": (3476, "Cephalaria gigantea", "cultivar", "hellgelb", "VII–VIII", "200 cm–220 cm", S3, "Fr/GR2-3", "Z5", KG, None, {"Schnittgeeignet": "ja"},
          [("self_seed", "Am zusagenden Standort versamt sie sich reichlich, was durch einen rechtzeitigen Rückschnitt aber gut eingedämmt werden kann."),
           ("soil", "Besonders gut ist sie für die Pflanzung in größeren, sonnigen Naturgärten mit locker-humosem Boden geeignet.")]),
 "Gi01": (3738, "Gillenia trifoliata", "cultivar", "weiß, Kelch rötlich", "VI–VII", "60 cm–80 cm", S3, "GR2", "Z4", KG, None,
          {"Blattfarbe": "gelb rot", "Schnittgeeignet": "ja"},
          [("seasonal_foliage", "Im Herbst erglüht das Laub der aparten Pflanze in besonders leuchtenden Orange- und Gelbtönen."),
           ("native_range", "Ihre Heimat liegt im östlichen Nordamerika."),
           ("habit", "Buschig-aufrecht wachsend mit schwebenden, lockeren Blütenrispen und grazilen dreiteiligen Blättern")]),
 "Ko01": (1957, "Koeleria glauca", "cultivar", "bräunlich", "VI–VII", "15 cm–40 cm", "sonnig", "Fr/SH/St1", "Z4", KG, None,
          {"Blattfarbe": "silber blau", "Wildstaude": "ja", "Wintergrün": "ja"},
          [("soil", "Sonniger Standort, durchlässiger, sandiger, gerne auch trockener Boden - nicht zu nährstoffreich, sonst ist das Gras recht kurzlebig."),
           ("native_range", "Am Naturstandort in Mitteleuropa wächst das Blaue Schillergras auf sandigen Böden auf Heideflächen und in lichten Kiefernwäldern.")]),
 "Ls01": (1203, "Leucosceptrum japonicum 'Golden Angel'", "cultivar", "weiß", "IX–X", "60 cm–90 cm", "halbschattig, schattig", "GR/G2-3", "Z6", None, None,
          {"Schnittgeeignet": "ja"},
          [("habit", "Das leuchtend goldgrüne Laub dieses aus Japan stammenden, vollkommen winterharten Halbstrauchs ist einfach sensationell!"),
           ("habit", "Der buschig-kompakte Wuchs ermöglicht viele Kombinationen.")]),
 "Ol01": (12037, "Saatgut (konventionell): Orlaya grandiflora", "cultivar", "weiß", "VI–VIII", "40 cm–50 cm", "sonnig", "Fr/B2", "", None, None,
          {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
          [("lifespan", "Die Strahlen-Breitsame ist ein aparter einjähriger Doldenblütler, der sich im Beet durch Selbstaussaat erhält, dabei aber nie lästig wird."),
           ("native_range", "Die ursprünglich aus dem Mittelmeergebiet stammende Wildpflanze ist bei uns selten geworden und gilt mittlerweile als stark gefährdet.")]),
 "Sj01": (7856, "Satureja spicigera", "cultivar", "weiß", "VIII–X", "10 cm–15 cm", "sonnig", "St/FS1", "Z6", KG, None, {},
          [("pruning", "Nach dem Winter sollte ein bodentiefer Rückschnitt erfolgen."),
           ("habit", "Das kriechende Berg-Bohnenkraut macht als wüchsiger, wertvoller, weißer Spätblüher im Steingarten, auf Mauerkronen etc. viel her."),
           ("habit", "Da Satureja spicigera danach recht spät austreibt, kann es sehr gut mit Frühjahrsblühern, wie z.B. Krokussen unterpflanzt werden.")]),
 "Sb01": (4902, "Sporobolus heterolepis", "cultivar", "silbrig-braun", "VIII–IX", "40 cm–70 cm", "sonnig", "Fr1-3", "Z4", KG, None,
          {"Blattfarbe": "gelb rot", "Duftend": "ja", "Schnittgeeignet": "ja"},
          [("soil", "Von Kanada bis nach Mexico verbreitet ist dieses grazile Präriegras, welches keine weiteren Ansprüche hat, als einen warmen, sonnigen Standort."),
           ("seasonal_foliage", "Im Herbst färben sich die feinen, grünen Blätter leuchtend ockergelb.")]),
 "Va01": (10032, "Valeriana officinalis", "cultivar", "hell-rosa", "VII–VIII", "50 cm–100 cm", "sonnig", "Fr3", "Z6", None, None, {"Duftend": "ja", "Wildstaude": "ja"},
          [("soil", "Baldrian gedeiht am besten auf feuchten, schweren, nährstoffreichen Böden, sowohl in der Sonne als auch an schattigeren Plätzen."),
           ("pollinator", "Das Pollenangebot wird gerne von Honigbienen und Sand- bzw. Furchenbienenarten genutzt.")]),
}
