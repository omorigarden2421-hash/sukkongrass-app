# Gaißmayer（s17）: ポテンティラ・パニカム・アキレア・スタキス・ヒューケラ。2026-11-19 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。
# 探し方は batch_03/gaissmayer_data.py と同じ（サイト内検索: Achillea 22件・Heuchera 18件・Panicum 10件・Potentilla 14件・Stachys 13件 → 一致した商品ページ ?static）。
# 【注意】商品ページを1秒おきに続けて開いたら、10ページほどで確認画面に切り替わった（待つと自動で通った。操作はしていない）。
#   1ページごとに6秒あけると出なかった。次からは最初から間をあけて読む。
# Gaißmayer の書き方: 'Parker's Variety' は Achillea filipendulina 'Parker'、'Terracotta'・'Walter Funcke' は Achillea Filipendulina-Hybride、
#   'Red Velvet' は Achillea Millefolium-Hybride、'Firefly' は Heuchera sanguinea 'Leuchtkäfer'、'Dallas Blue' は 'Dallas Blues'、ベルナは Potentilla neumanniana。
# 使っていないもの: Panicum virgatum 'Squaw Select'（'Squaw' の選抜で別もの）。質問への回答は読んでいない。価格・在庫は写していない。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-19"
S3 = "sonnig, absonnig, halbschattig"
_BYZ = (4246, "Stachys byzantina", "species", "lilarosa", "VI–VII", "40 cm–60 cm", "sonnig", "Fr/FS/St1", "Z5", "keine Gefahr", None,
        {"Blattfarbe": "silber, gezeichnet", "Schnittgeeignet": "ja", "Wintergrün": "ja"},
        [("soil", "gedeiht am besten auf durchlässigen und mageren Böden in voller Sonne"), ("spread_mode", "Sie bildet recht rasch dichte, wintergrüne Teppiche")])
GAISS = {
 "Ac01": (9310, "Achillea filipendulina 'Parker'", "cultivar", "goldgelb", "VI–VIII", "120 cm", "sonnig", "B/Fr2", "Z3", "keine Gefahr", "Parker (GB) 1928", {"Schnittgeeignet": "ja"},
          [("habit", "Diese altbekannte und bewährte Standardsorte ist robust, wüchsig und standfest.")]),
 "Ac02": (3263, "Achillea filipendulina 'Coronation Gold'", "cultivar", "gelb", "VII–IX", "70 cm", "sonnig", "B/Fr2", "Z3", "keine Gefahr", "Miss Pole, Woking (GB) 1952",
          {"Schnittgeeignet": "ja"},
          [("pruning", "'Coronation Gold' remontiert leicht, sofern man die sehr lange Blütezeit rechtzeitig durch Rückschnitt unterbricht.")]),
 "Ac03": (6611, "Achillea Filipendulina-Hybride 'Terracotta'", "cultivar", "orangebraun", "VI–VII + IX", "80 cm", "sonnig", "B/Fr2", "Z3", None, "Ernst Pagels (DE)",
          {"Schnittgeeignet": "ja"}, []),
 "Ac04": (10691, "Achillea Filipendulina-Hybride 'Walter Funcke'", "cultivar", "orangerot", "VI–VII + IX", "60 cm", "sonnig", "B/Fr2", "Z3", None, "Ernst Pagels (DE) 1995",
          {"Schnittgeeignet": "ja"}, [("habit", "Aufgrund des kompakten Wuchses ist die Sorte auch gut für den Beetvordergrund geeignet.")]),
 "Ac06": (10553, "Achillea Millefolium-Hybride 'Red Velvet'", "cultivar", "tief samtrot", "VI–VII + IX", "50 cm–60 cm", "sonnig", "B2 Fr1", "Z2", None, None,
          {"Schnittgeeignet": "ja"}, [("fragrance", "über dem etwas herb duftenden, fein geteilten Laub")]),
 "Ac09": (4354, "Achillea tomentosa", "cultivar", "goldgelb", "V–VII", "5 cm–10 cm", "sonnig", "St/FS/M1-2", "Z3", None, None, {},
          [("soil", "Die Teppich-Schafgarbe bildet graufilzige Teppiche. Sie ist auf nährstoffreichen Böden eher kurzlebig.")]),
 "He05": (9676, "Heuchera Hybride 'Rachel'", "cultivar", "rosa", "VI–VIII", "20 cm–60 cm", S3, "GR/Fr/St2b", "Z5", "keine Gefahr", "Ramsdale (GB) 1990",
          {"Blattfarbe": "rot", "Schnittgeeignet": "ja", "Wintergrün": "ja"},
          [("sun", "'Rachel' gedeiht sehr gut auch an vollsonnigen Standorten, im tiefen Schatten besteht die Tendenz zum Vergrünen.")]),
 "He11": (8369, "Heuchera sanguinea 'Leuchtkäfer'", "cultivar", "scharlachrot", "V–VII", "20 cm–60 cm", S3, "GR/Fr/St2b", "Z5", "keine Gefahr", None,
          {"Schnittgeeignet": "ja", "Wintergrün": "ja"}, [("evergreen", "Auch im Winter bleibt das Laub dieser kompakt wachsenden Sorte ansehnlich.")]),
 "He12": (2559, "Heuchera sanguinea 'White Cloud'", "cultivar", "weiß", "VI–VIII", "20 cm–60 cm", S3, "GR/Fr/St2b", "Z5", "keine Gefahr", None,
          {"Blattfarbe": "gezeichnet", "Schnittgeeignet": "ja", "Wintergrün": "ja"}, [("evergreen", "Auch im Winter bleibt das Laub dieser kompakt wachsenden Sorte ansehnlich.")]),
 "Pa02": (3442, "Panicum virgatum 'Cloud Nine'", "cultivar", "blaugrün", "VII–IX", "140 cm–210 cm", "sonnig", "Fr/GR/B2", "Z5", "keine Gefahr", "Bluemount Nurseries (USA)",
          {"Blattfarbe": "blau, gelb", "Schnittgeeignet": "ja"},
          [("seasonal_foliage", "Das breite, an Miscanthus erinnernde Laub ist blau-grün gefärbt bis es im Herbst eine tiefgelbe Farbe annimmt."),
           ("habit", "Gut standfest bis in den Winter hinein!")]),
 "Pa03": (4983, "Panicum virgatum 'Dallas Blues'", "cultivar", "rötlich-violett", "VII–IX", "150 cm–180 cm", "sonnig", "Fr/GR/B2", "Z5", "keine Gefahr", "Ken & Linda Smith (US) 1995",
          {"Blattfarbe": "blau", "Schnittgeeignet": "ja"},
          [("seasonal_foliage", "breitblättrige Rutenhirse mit blaugrauem Laub und gelber Herbstfärbung bereits ab Spätsommer")]),
 "Pa05": (9806, "Panicum virgatum 'Northwind'", "cultivar", "graugrün", "VII–IX", "170 cm–180 cm", "sonnig", "Fr/GR/B2", "Z5", "keine Gefahr",
          "Roy Diblik, Northwind Perennial (US) Anfang 1980er", {"Blattfarbe": "blau", "Schnittgeeignet": "ja"},
          [("drought", "Die feste, fast wachsartige Blattsubstanz bedingt eine ganz hervorragende Trockenheitsverträglichkeit.")]),
 "Pa07": (6209, "Panicum virgatum 'Shenandoah'", "cultivar", "bräunlich", "VII–IX", "80 cm–100 cm", "sonnig", "Fr/GR/B2", "Z5", "keine Gefahr", "Hans Simon (DE)",
          {"Blattfarbe": "rot", "Schnittgeeignet": "ja"},
          [("seasonal_foliage", "Fast ganzjährig beeindruckt sie mit bordeauxroten Laubspitzen. Die frühe und intensive Herbstfärbung macht diese Sorte ganz besonders wertvoll.")]),
 "Po01": (8177, "Potentilla atrosanguinea", "cultivar", "rot", "VI–VIII", "40 cm", S3, "B/Fr/GR2", "Z5", "keine Gefahr", None, {},
          [("heat_humidity", "Das Blutrote Fingerkraut liebt helle, nicht zu heiße, ggf. auch etwas schattigere Plätze.")]),
 "Po07": (7756, "Potentilla nepalensis 'Miss Willmott'", "cultivar", "dunkelrosa, Mitte purpur", "VI–VIII", "40 cm–60 cm", "sonnig", "B/Fr/GR1-2", "Z5", "keine Gefahr",
          "Willmott (GB) 1920", {}, [("habit", "Schöne Sorte mit horstigem Wuchs, bogig niederliegenden bis ansteigenden Stängeln und sehr langer Blütezeit.")]),
 "Po10": (3291, "Potentilla x tonguei", "cultivar", "hellapricot, rotes Auge", "VII–VIII", "10 cm–20 cm", "sonnig", "Fr/B1-2", "Z5", "keine Gefahr", "Baxter (Großbritannien) 1850", {},
          [("soil", "Der Boden sollte locker, humos und nur mäßig nährstoffreich sein.")]),
 "Po12": (8422, "Potentilla neumanniana", "cultivar", "goldgelb", "IV–VI", "5 cm–15 cm", "sonnig", "Fr/St/SH1", "Z5", "keine Gefahr", None, {"Wildstaude": "ja"},
          [("spread_mode", "Die niederliegenden Triebe bilden an den Knoten Wurzeln, wodurch sich Matten von bis zu 30 cm Durchmesser bilden können.")]),
 "St01": (4246, "Stachys byzantina", "cultivar") + _BYZ[3:],
 "St02": _BYZ,
 "St03": (5140, "Stachys byzantina 'Silky Fleece'", "cultivar", "lila-pflaumenfarben", "VI–VII", "10 cm–15 cm", "sonnig", "Fr/FS/St1", "Z5", "keine Gefahr", "Jelitto (DE) 2006",
          {"Blattfarbe": "silber", "Wintergrün": "ja"},
          [("habit", "Die kleinen, weißwolligen Blätter bilden niedrige Kissen von nur ca. 5 cm Höhe."), ("soil", "gedeiht sehr schön an sonnigen, trockenen Plätzen im Steingarten")]),
 "St07": (9841, "Stachys monieri 'Hummelo'", "cultivar", "dunkelrosa", "VI–VIII", "40 cm–50 cm", "sonnig", "Fr/FS/St1-2", "Z5", "keine Gefahr", "Ernst Pagels (DE)",
          {"Schnittgeeignet": "ja"}, [("pollinator", "Zu diesen zählen verschiedene Bienen, Hummeln und Schmetterlinge.")]),
 "St08": (6326, "Stachys officinalis", "cultivar", "dunkelrosa", "VI–VIII", "40 cm–60 cm", S3, "Fr/GR1-2", "Z5", None, None, {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
          [("soil", "Er liebt mäßig nährstoffreiche, humose, lehmige oder tonige, durchlässige Standorte"), ("habit", "Stachys officinalis wächst horstig.")]),
}
