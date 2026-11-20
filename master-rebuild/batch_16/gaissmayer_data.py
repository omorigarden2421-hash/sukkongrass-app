# Gaißmayer（s17）: エピメディウム・フラガリア・ヘレボルス・イベリス・リリオペ・リクニス・ムクデニア・ファラリス・フィソカルプス・ロジャーシア・ソリダゴと、
#   アクタエアからラミアストラムまでの1品種の属27（batch_16/input の38属）。
# 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_15/gaissmayer_data.py と同じ
#   （サイト内検索: 属名37個と Silene・Lamium〔Actaea は batch_15 のときの結果を使った〕 → 一致した商品ページ ?static 17ページ。ほかに、当てなかった種のページ Fragaria vesca を1つ読んだ）。7秒おき、1回の指示は6ページまで。
#   検索の6ページ目（Lychnis）で確認画面が出た（batch_15 を読み終えてから40分ほどあいていた）。操作せずに置き、シカゴ植物園の報告を読んでいる間（4分ほど）に自動で通った。
#   確認画面のページを「0件」と読み違えないように、ページの題名を確かめてから読むようにした。Lychnis は最後に検索し直した。そのあとは出なかった。
# 本文は先頭の約500字だけを見ている（ベニチガヤだけ、冬越しの文が途中で切れたので続きを読んだ）。質問への回答は読んでいない。価格・在庫は写していない。
# Gaißmayer の書き方: 'Alexandria' は Fragaria vesca var. semperflorens 'Alexandria'、エゴポディウムは Aegopodium podagraria 'Variegata'、
#   ベニチガヤは Imperata cylindrica 'Red Baron'（RHS は 'Red Baron' を 'Rubra' のシノニムとしているので当てた）。
# 種のページを当てたもの: ヤブラン（Lr01）、リクニス コロナリア（Lc02）、アルンクス エスシフォリウス（Au01）、ブルネラ マクロフィラ（Br01）、ブフタルムム サリキフォリウム（Bu01）。
# 掲載なし・当てていないもの: 'Alpine Yellow'（種のページ Fragaria vesca は「ランナーでよく広がる」野生型の説明で、ランナーを出さない四季なりの品種には当てていない）、
#   ヘレボルス（Orientalis-Hybride は色別の 'Lady' のシリーズだけ。argutifolius はなし）、イベリス（'Schneeflocke'・'Zwergschneeflocke'・'Amethyst' だけ）、リリオペ スピカータ、
#   × haageana、ムクデニア・ファラリス（検索で該当なし）、フィソカルプス（'Tiny Wine' だけ）、ロジャーシア（pinnata 'Chocolate Wings'・podophylla 'Pagode' など別の品種）、
#   ソリダゴ 'Gold Spangles'、アクタエア ヤポニカ 'Silver Dance'（'Cheju-do' だけ）、アンペロプシス・アンドロサセ・アレナセルム・ビゲロウィア・デンドランセマ・エリオゴヌム・ユーオニマス（該当なし）、
#   オーブリエタ（交配種だけ。'Silberrand' は別の斑入り品種）、コルタデリア（'Pumila'・'Sunningdale Silver' だけ）、エラグロスティス スペクタビリス（'Purpurflirren' は品種のページなので当てていない）、
#   エリカ カルネア、エリシマム（'Orange Flame' なし）、ゴニオリモン（tataricum だけ）、ヘリアンサス 'Happy Days'、ヘリクトトリコン（'Saphirsprudel' は品種のページなので当てていない）、
#   ラミアストラム（'Florentinum'・'Silberteppich' だけ）。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-20"
S3 = "sonnig, absonnig, halbschattig"
HS = "halbschattig, schattig"
KG = "keine Gefahr"
RG = "relativ geringe Gefahr"
FP = "Frühjahrspflanzung empfohlen"
SG = "schwach giftig (+)"
_LYC = [("lifespan", "Die einzelne Pflanze ist sehr kurzlebig und wird meist nur zwei bis drei Jahre alt."),
        ("self_seed", "Der Bestand erhält sich aber durch Selbstaussaat. Grundvoraussetzung hierfür ist, dass es genug offenen Boden gibt."),
        ("soil", "für die Verwendung auf sonnigen, nicht zu nährstoffreichen Standorten")]
GAISS = {
 "Fr01": (2655, "Fragaria vesca var. semperflorens 'Alexandria'", "cultivar", "weiß", "VI–IX", "10 cm–20 cm", S3, "B2", "Z5", None, None, {"Wintergrün": "ja"},
          [("spread_mode", "Im Gegensatz zur Wildart bildet die Monats-Erdbeere keine Ausläufer."),
           ("habit", "'Alexandria' kann sehr gut auch als Bodendecker oder als Beeteinfassung eingesetzt werden")]),
 "Lr01": (9443, "Liriope muscari", "species", "violettblau", "VIII–X", "20 cm–40 cm", "absonnig, halbschattig", "GR/St2", "Z6", KG, None,
          {"Pflanz-Zeitpunkt": FP, "Giftklasse": "giftig +", "Wintergrün": "ja"},
          [("soil", "Lilientrauben bevorzugen nährstoffreiche, kalkarme, locker-humose Böden in lichtschattiger Lage."),
           ("habit", "Die langen, dekorativen Blüten dieser horstigen Staude mit grasartigem Laubschopf erinnern an die bekannten Traubenhyazinthen.")]),
 "Lc01": (3837, "Lychnis coronaria 'Alba'", "cultivar", "reinweiß", "VI–VII", "60 cm–80 cm", "sonnig", "Fr1b", "Z4", RG, None,
          {"Blattfarbe": "silber", "Schnittgeeignet": "ja", "Wintergrün": "ja"}, _LYC),
 "Lc02": (9565, "Lychnis coronaria", "species", "karminrot", "VI–VII", "60 cm–80 cm", "sonnig", "Fr1", "Z4", RG, None,
          {"Blattfarbe": "silber", "Schnittgeeignet": "ja", "Wintergrün": "ja"}, _LYC),
 "So02": (1947, "Solidago rugosa 'Fireworks'", "cultivar", "tief gelb", "VIII–X", "100 cm–120 cm", "sonnig", "B/Fr2", "Z3", KG, "Moore (US) 1993", {"Schnittgeeignet": "ja"},
          [("spread_mode", "Die gut standfeste, dichtbuschige Staude bildet durch kurze Rhizome allmählich einen breiten Horst.")]),
 "Ao01": (4463, "Aegopodium podagraria 'Variegata'", "cultivar", "weiß", "V–VII", "25 cm–40 cm", "absonnig, halbschattig, schattig", "G/GR2", "Z5", KG, None,
          {"Blattfarbe": "panachiert", "Schnittgeeignet": "ja"},
          [("spread_mode", "Doch die weißbunte Form wuchert weniger als die Art und kann durchaus als großflächiger Bodendecker unter Gehölzen "
                           "oder in anderen Schattenbereichen verwendet werden."),
           ("self_seed", "Wichtig ist es, die Blüten vor dem Versamen auszubrechen."), ("habit", "Nur mit robusten und starkwüchsigen Partnern kombinierbar.")]),
 "Ax01": (5022, "Althaea officinalis", "cultivar", "weißlich-lilarosa", "VII–IX", "150 cm–200 cm", "sonnig", "Fr2-3 WR4", "Z3", None, None, {"Wildstaude": "ja"},
          [("habit", "Locker-verzweigte, buschige Solitärstaude mit hübschen, kleinen, malvenähnlichen Blüten und samtigfeinem Laub."),
           ("soil", "Die reich blühende Heil- und Teepflanze ist salzverträglich.")]),
 "Au01": (9727, "Aruncus aethusifolius", "species", "weiß", "V–VII", "30 cm", S3, "St/Fr/GR2", "Z4", KG, None, {},
          [("seasonal_foliage", "im Herbst verfärbt sich das Laub rötlich, und im Winter geben die trockenen Fruchtstände dem Garten Struktur"),
           ("soil", "im absonnigen Beetvordergrund auf nicht zu trockenen Böden")]),
 "Ai01": (9907, "Astilboides tabularis", "cultivar", "grünlich-weiß", "VII", "70 cm–100 cm", HS, "G/GR3 WR4", "Z6", None, None, {},
          [("soil", "Die dekorative Blattschmuckstaude für feuchtkühle, humose, nährstoffreiche Böden ist eine schöne Uferpflanze, die jedoch vor Vernässung geschützt werden muss."),
           ("habit", "Sie treibt spät aus (ab Ende April)")]),
 "Br01": (9535, "Brunnera macrophylla", "species", "blau", "IV–VI", "30 cm–50 cm", S3, "GR/G2", "Z3", RG, None, {"Schnittgeeignet": "ja"},
          [("pruning", "Ein Rückschnitt lässt das Laub wieder frisch austreiben und verhindert die Selbstaussaat."),
           ("soil", "Im lichten Schatten fühlt sich das Kaukasus-Vergissmeinnicht besonders wohl. Auf lehmig-humosen, frischen Böden kann es aber auch sonnig stehen."),
           ("lifespan", "Langlebige und robuste Staude")]),
 "Bu01": (8860, "Buphthalmum salicifolium", "species", "gelb", "VI–IX", "50 cm", S3, "Fr/SH1-2", "Z4", KG, None, {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
          [("soil", "Das Ochsenauge liebt locker-humose, mäßig nährstoffreiche Böden in sonniger bis halbschattiger Lage."),
           ("pollinator", "Ihre Blüten dienen als Pollen- und Nektarquelle für Honigbienen, Hummlen und Wildbienen."),
           ("native_range", "Im Süden Deutschlands und in angrenzenden Ländern kann man das Ochsenauge gelegentlich in freier Wildbahn auf Kalkmagerrasen "
                            "und in lichten Eichen und Kiefernwäldern entdecken.")]),
 "Ct01": (4048, "Ceratostigma plumbaginoides", "cultivar", "azurblau", "VIII–X", "20 cm–25 cm", "sonnig", "Fr/FS1 St1-2", "Z6", KG, None,
          {"Blattfarbe": "rot", "Pflanz-Zeitpunkt": FP, "Schnittgeeignet": "ja"},
          [("spread_mode", "Wertvoller ausläufertreibender Bodendecker für sonnige, trockene Lagen."),
           ("seasonal_foliage", "Die hübschen azurblauen Blüten und die prachtvolle rote Herbstfärbung sorgen für jahreszeitlichen Schmuck."),
           ("soil", "Für durchlässige, eher nährstoffarme, kalkhaltige, warme Böden geeignet."), ("habit", "Die aus dem Himalaya stammende Bleiwurz treibt spät aus")]),
 "Da01": (7829, "Darmera peltata", "cultivar", "hellrosa", "IV–V", "50 cm–100 cm", S3, "Fr2-3 WR4", "Z5", None, None, {"Schnittgeeignet": "ja"},
          [("seasonal_foliage", "Schöne kupfrige Herbstfärbung."), ("spread_mode", "Bildet auf lehmigem, feuchtem, nährstoffreichem Boden mit der Zeit große Bestände."),
           ("winter", "Vorsicht bei Spätfrost - hier kann die Blüte in Mitleidenschaft gezogen werden!")]),
 "Es01": (4873, "Elsholtzia stauntonii", "cultivar", "hell-purpur", "VIII–X", "90 cm–150 cm", "sonnig", "Fr/B/H1-2", "Z4", KG, None, {"Pflanz-Zeitpunkt": FP, "Duftend": "ja"},
          [("habit", "Aufrecht wachsender, leicht verholzender Halbstrauch"),
           ("seasonal_foliage", "Später entwickelt er zusätzlich eine attraktive, gelbliche Herbstfärbung."),
           ("soil", "Am liebsten mag der Gewürzstrauch vollsonnige, offene Lagen mit durchlässigem Boden. Auch verträgt er Trockenheit recht gut.")]),
 "Im01": (6089, "Imperata cylindrica 'Red Baron'", "cultivar", "blüht nicht", "", "30 cm–40 cm", "sonnig", "B/Fr/KÜBEL2", "Z6", KG, "Kurt Bluemel (US)",
          {"Blattfarbe": "rot", "Pflanz-Zeitpunkt": FP, "Schnittgeeignet": "ja"},
          [("spread_mode", "'Red Baron' treibt relativ spät aus, breitet sich durch kurze Ausläufer aus und bildet mit der Zeit lockere Bestände."),
           ("winter_protection", "Weil die Winterhärte in unseren Breiten nur bei gutem Winterschutz gegeben ist, eignet sich dieses Gras bestens zur Kultivierung in flachen Pflanzgefäßen."),
           ("winter_protection", "Bis das Gras eingewachsen ist gut feucht halten und im Winter mit Laub und Reisig abdecken.")]),
 "Em01": (1478, "Epimedium x rubrum", "cultivar", "rot mit weiß", "IV–V", "20 cm–35 cm", HS, "G2 GR2-3", "Z5", KG, None, {"Giftklasse": SG, "Wintergrün": "ja"},
          [("spread_mode", "Epimedium x rubrum bleibt mit kurzen Rhizomen kompakt"),
           ("seasonal_foliage", "Diese zeigen im Austrieb und im Winter eine schöne, bronzene Färbung."),
           ("parentage", "bereits 1854 in England entstandenen Hybride aus der ostasiatischen E. grandiflorum und der europäischen E. alpinum")]),
 "Em02": (6750, "Epimedium x versicolor 'Sulphureum'", "cultivar", "schwefelgelb", "IV–V", "30 cm–40 cm", HS, "G2 GR2-3", "Z5", KG, "Morren (GB) 1854",
          {"Giftklasse": SG, "Schnittgeeignet": "ja", "Wintergrün": "ja"},
          [("spread_mode", "Die wintergrüne Sorte 'Sulphureum' ist wüchsig und robust und bildet durch ihr kräftiges Rhizom bald große Bestände."),
           ("seasonal_foliage", "Das Laub ist im Austrieb rötlich, den Sommer über rotbraun gezeichnet und im Winter bronzefarben.")]),
}
