# Gaißmayer（s17）: ミント・ゲウム・ビンカ・プルモナリア・ペンステモン。2026-11-19 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。
# 探し方は batch_03/gaissmayer_data.py と同じ（サイト内検索: Geum 12件・Pulmonaria 11件・Penstemon 6件・Vinca 7件・Mentha 29件の掲載名を照合 → 一致した商品ページ ?static）。
# Gaißmayer の書き方: 'Mai Tai'・'Flames of Passion' は Geum x cultorum、'Blue Ensign' は Pulmonaria angustifolia、'Trevi Fountain'・'Lewis Palmer' は Pulmonaria saccharata、
#   'Husker Red' は 'Husker's Red'、ストロベリーミントは Mentha species 'Erdbeere'、ケンタッキーカーネルは Mentha species 'Kentucky'、ブラックペパーミントは 'Nigra'。
# 質問への回答は読んでいない。価格・在庫は写していない。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-19"
S3 = "sonnig, absonnig, halbschattig"
_VIN = (4047, "Vinca minor", "species", "blau", "IV–V", "10 cm–15 cm", "halbschattig, schattig", "G/GR2", "Z5", "keine Gefahr", None,
        {"Giftklasse": "giftig +", "Wildstaude": "ja", "Wintergrün": "ja"},
        [("spread_mode", "Sie bildet mit Hilfe von langen, wurzelnden Trieben pflegeextensive Teppiche."), ("use", "Sehr gut zur Unterpflanzung von Gehölzen geeignet.")])
_RIV = (1839, "Geum rivale", "species", "rosa-gelblich, Kelch purpur", "V–VI", "20 cm–40 cm", "absonnig, halbschattig", "Fr2-3 WR4", "Z3", "keine Gefahr", None,
        {"Wildstaude": "ja", "Schnittgeeignet": "ja", "Wintergrün": "ja"},
        [("self_seed", "Verwendung findet die recht stark versamende Staude an Bach- und Teichrändern sowie in größeren Naturgartenpartien."),
         ("native_range", "an Ufern, in Flachmooren, Auwäldern sowie auf Feucht- und Nasswiesen")])
GAISS = {
 "Ge06": (8385, "Geum x cultorum 'Flames of Passion'", "cultivar", "hellrot, halbgefüllt", "V–VIII", "20 cm–30 cm", S3, "Fr/GR2", "Z5", "keine Gefahr", "Piet Oudolf (NL) 2002",
          {"Schnittgeeignet": "ja", "Wintergrün": "ja"},
          [("heat_humidity", "Im Vergleich zu anderen Geum-Sorten ist 'Flames of Passion' recht tolerant was Trockenheit und Hitze anbelangt.")]),
 "Ge07": (1205, "Geum x cultorum 'Mai Tai' ®", "cultivar", "hell apricot", "V–VII", "30 cm–40 cm", S3, "Fr/GR2", "Z5", "keine Gefahr", "Intrinsic Perennial Gardens (US) 2005",
          {"Schnittgeeignet": "ja", "Wintergrün": "ja"},
          [("soil", "Wie alle Nelkenwurz bevorzugt sie einen sonnigen bis halbschattigen, lehmig-humosen, nicht zu trockenen Boden.")]),
 "Ge09": (1839, "Geum rivale", "cultivar") + _RIV[3:],
 "Ge10": _RIV,
 "Me03": (10108, "Mentha x piperita var. piperita 'Nigra'", "cultivar", "lila", "VI–VIII", "30 cm–60 cm", S3, "B/Fr2-3", "Z5", None, None, {"Schnittgeeignet": "ja"},
          [("foliage", "sehr dunkle, große, spitz-ovale, fast purpurfarbene Blätter")]),
 "Me04": (8788, "Mentha x piperita var. citrata 'Orange'", "cultivar", "lilarosa", "VII–VIII", "40 cm–80 cm", S3, "B/Fr2-3", "Z5", None, None, {"Schnittgeeignet": "ja"},
          [("sun", "Sie entwickelt das volle Aroma erst in der prallen Sonne und eignet sich deshalb gut als Kübelpflanze für einen sonnigen Balkon.")]),
 "Me07": (8241, "Mentha species 'Kentucky'", "cultivar", "blass-lila", "VII–VIII", "80 cm–90 cm", S3, "B/Fr2-3", "Z5", None, None, {"Schnittgeeignet": "ja"},
          [("habit", "Diese relativ großwüchsige Minze verströmt ein mild-fruchtiges Aroma mit einem Hauch von minziger Schärfe.")]),
 "Me08": (9653, "Mentha species 'Erdbeere'", "cultivar", "hell-lila", "VII–VIII", "30 cm–50 cm", S3, "B/Fr2-3", "Z6", None, None,
          {"Pflanz-Zeitpunkt": "Frühjahrspflanzung empfohlen", "Schnittgeeignet": "ja"},
          [("habit", "Eine der kleinen und zierlichen Minzen, kaum mehr als 40 cm hoch.")]),
 "Me09": (7955, "Mentha suaveolens", "cultivar", "weißlich-rosa", "VII–VIII", "25 cm–60 cm", S3, "B/Fr2-3", "Z5", None, None, {"Blattfarbe": "silber", "Schnittgeeignet": "ja"},
          [("foliage", "Die Blätter sind besonders weich und leicht pelzig.")]),
 "Me10": (3148, "Mentha suaveolens 'Variegata'", "cultivar", "weißlich-rosa", "VII–VIII", "25 cm–60 cm", S3, "B/Fr2-3", "Z6", None, None,
          {"Blattfarbe": "hellgrün, panachiert", "Schnittgeeignet": "ja"},
          [("habit", "Sie ist vergleichsweise schwachwüchsig und treibt spät aus.")]),
 "Pe04": (6867, "Penstemon digitalis 'Husker's Red'", "cultivar", "weißlich-violett", "VII–VIII", "80 cm–100 cm", "sonnig", "B/Fr1-2", "Z5", "keine Gefahr", None,
          {"Blattfarbe": "rot", "Schnittgeeignet": "ja", "Wintergrün": "ja"},
          [("winter_protection", "In rauen Lagen empfehlen wir Schutz vor Wintersonne und Kahlfrösten. Bei uns ist diese Penstemon-Sorte völlig winterhart."),
           ("habit", "eine recht robuste und langlebige Penstemon-Sorte mit attraktivem bronze-purpurfarbenem, wintergrünem Laub")]),
 "Pu02": (2611, "Pulmonaria angustifolia 'Blue Ensign'", "cultivar", "leuchtend blau", "III–V", "25 cm", "absonnig, halbschattig", "G/GR2-3", "Z4", None, None, {},
          [("foliage", "Das Laub ist bei dieser Sorte einheitlich grün gefärbt."), ("use", "Ihre Horste geben wunderbare Bodendecker im Halbschatten, etwa vor oder unter Gehölzen, ab.")]),
 "Pu04": (9753, "Pulmonaria saccharata 'Lewis Palmer'", "cultivar", "ultramarinviolett", "IV–V", "30 cm–35 cm", "absonnig, halbschattig", "G/GR2-3", "Z4", None, None,
          {"Blattfarbe": "gezeichnet"}, [("trial_rating", "'Lewis Palmer' wurde bei der Staudensichtung allerbestens bewertet.")]),
 "Pu09": (8548, "Pulmonaria saccharata 'Trevi Fountain'", "cultivar", "azurblau bis blauviolett", "III–V", "25 cm–30 cm", "absonnig, halbschattig", "G/GR2-3", "Z5", None,
          "Terra Nova (US)", {}, [("trial_rating", "'Trevi Fountain' ist wirklich eine exzellente Sorte, die in der Staudensichtung mit \"hervorragend\" bewertet wurde.")]),
 # ビンカ マジョール 'Variegata' は表で Z7、本文に「霜にやや弱い」「厳しい土地では冬の保護が必要」。ゾーンは記録だけだが、ユーザーに伝える
 "Vi01": (3534, "Vinca major 'Variegata'", "cultivar", "blauviolett", "IV–V", "25 cm–30 cm", "halbschattig", "G/GR1-2", "Z7", "keine Gefahr", None,
          {"Blattfarbe": "panachiert", "Giftklasse": "giftig +", "Wintergrün": "ja", "Pflanz-Zeitpunkt": "Frühjahrspflanzung empfohlen"},
          [("winter_protection", "eine altbekannte Sorte, die allerdings bei Kahlfrost oftmals leidet, da sie etwas frostempfindlich ist"),
           ("winter_protection", "In rauen Lagen ist Winterschutz erforderlich.")]),
 "Vi02": (7715, "Vinca minor 'Alba'", "cultivar", "weiß", "IV–V", "10 cm–15 cm", "halbschattig, schattig", "G/GR2", "Z5", "keine Gefahr", None,
          {"Giftklasse": "giftig +", "Wintergrün": "ja"},
          [("spread_mode", "Es bildet schnell dichte Teppiche aus starken Trieben und ist somit ideal zur Unterpflanzung von Bäumen und Sträuchern.")]),
 "Vi03": _VIN, "Vi04": _VIN, "Vi05": _VIN, "Vi06": _VIN, "Vi07": _VIN, "Vi08": _VIN, "Vi09": _VIN,
}
