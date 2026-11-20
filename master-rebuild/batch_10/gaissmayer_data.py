# Gaißmayer（s17）: ダイアンサス・ヘレニウム・ミューレンベルギア・アルメリア・ユーフォルビア・ヘリアンセマム・クニフォフィア・ペニセタム・ルドベキア・タイム。
# 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/gaissmayer_data.py と同じ（サイト内検索9回 → 一致した商品ページ ?static 16ページ）。6秒おき。
#   最初の検索で確認画面が出たが、操作せずに Jelitto を先に読んでいる間に自動で通った。
# 【未実施】ミューレンベルギアは検索し忘れた（Gaißmayer に掲載があるかは未確認）。
# 本文は先頭の約480字だけを見ている。質問への回答は読んでいない。価格・在庫は写していない。
# Gaißmayer の書き方: Eu04 は Euphorbia epithymoides、'Salsa' は Helenium Hybride、Ty08 は Thymus serpyllum 'Coccineus'（アドレスは thymus-serpyllum-praecox-coccineus）、
#   Ty03 は Thymus longicaulis ssp. odoratus（亜種。マスターは亜種を書いていないので、種のページとして当てた）。
# 種のページを当てたもの: カシュジアノーラム（Di02）、キパリシアス（Eu02）、ロンギカウリス（Ty03）、ブルガリス（Ty11）。
# 掲載なし: ダイアンサスのほかの品種、ヘレニウムの 'Salsa' 以外、アルメリアの 'Alba' 以外、'Golden Glory'、ヘリアンセマムの該当品種、クニフォフィアの 'Ice Queen' 以外
#   （ポプシクルのシリーズは 'Mango'・'Redhot' だけ）、ペニセタムの var. viridescens 以外、'Henry Eilers'、タイムの 'Peter Davis'・マスチキナ・'Foxley'・'Magic Carpet'。
# 'Little Goldstar' の育種者の欄は「Jelitto Seeds」（Jelitto が発表元とみられる。Jelitto のサイトでは確かめていない）。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-20"
S3 = "sonnig, absonnig, halbschattig"
KG = "keine Gefahr"
RG = "relativ geringe Gefahr"
_CAR = (9576, "Dianthus carthusianorum", "species", "purpurrot", "VI–IX", "30 cm–50 cm", "sonnig", "Fr/SH/H1", "Z3", KG, None,
        {"Wildstaude": "ja", "Schnittgeeignet": "ja", "Wintergrün": "ja"},
        [("self_seed", "Kurzlebig, aber stark versamend und hervorragend zur Verwilderung geeignet."), ("soil", "Für durchlässige und kalkhaltige Böden.")])
_SER = (4752, "Thymus serpyllum", "cultivar", "rosa", "VI–VIII", "5 cm–10 cm", "sonnig", "St/M/Fr/H1", "Z5", KG, None, {"Wildstaude": "ja", "Wintergrün": "ja"},
        [("soil", "Der Sand-Thymian benötigt keinen Kalk sondern groben Sandboden."), ("habit", "Niedrige Art mit kriechendem Wuchs und üppigem Blütenflor. Er ist sehr robust und winterhart.")])
GAISS = {
 "Di01": _CAR[:2] + ("cultivar",) + _CAR[3:], "Di02": _CAR,
 "Hl01": (7647, "Helenium Hybride 'Salsa'", "cultivar", "dunkelrot", "VII–IX", "60 cm–70 cm", "sonnig", "B/Fr2", "Z5", None, "Arie Blom (NL)", {"Schnittgeeignet": "ja"},
          [("habit", "Diese kompakt wachsende, sehr standfeste und schön verzweigte Sonnenbraut"), ("award", "diese in der Staudensichtung hervorragend bewertete Sorte")]),
 "Ar02": (3031, "Armeria maritima 'Alba'", "cultivar", "weiß", "V–VII", "10 cm–15 cm", "sonnig", "St/FS/Fr1", "Z6", KG, None, {"Wintergrün": "ja"},
          [("pruning", "Schneiden Sie die verwelkten Blüten immer wieder heraus, wird ein fortdauernder Blütenflor gefördert.")]),
 "Eu02": (1294, "Euphorbia cyparissias", "species", "zitronengelb", "IV–VI", "20 cm–40 cm", "sonnig", "FS/Fr/SH/GR1", "Z4", KG, None,
          {"Giftklasse": "stark giftig ++", "Duftend": "ja", "Wildstaude": "ja", "Schnittgeeignet": "ja"},
          [("spread_mode", "Die Hochblätter dieser stark Ausläufer treibenden Art verfärben sich oft rot."), ("soil", "Sie liebt trockene Magerstandorte.")]),
 "Eu04": (5376, "Euphorbia epithymoides", "cultivar", "gelb", "IV–V", "30 cm–40 cm", "sonnig", "St/FS/Fr/GR1", "Z6", KG, None,
          {"Blattfarbe": "gelb, rot", "Giftklasse": "giftig +", "Duftend": "ja", "Schnittgeeignet": "ja"},
          [("soil", "Sie liebt warme, sonnige Plätze auf durchlässigen, kalkhaltigen Böden."),
           ("drought", "Die Gold-Wolfsmilch verträgt erstaunlich viel Trockenheit und ist sehr ausdauernd.")]),
 "Eu03": (10957, "Euphorbia griffithii 'Fireglow'", "cultivar", "orangerot", "IV–VII", "70 cm–80 cm", S3, "Fr/GR2", "Z5", KG, "Alan Bloom (Großbritannien)",
          {"Giftklasse": "giftig +", "Schnittgeeignet": "ja"},
          [("spread_mode", "Die Himalaya-Wolfsmilch bildet reichlich kurze Ausläufer und mag es nährstoffreich und nicht zu trocken."),
           ("seasonal_foliage", "mit leuchtend orangeroten Hochblättern im Frühjahr und anhaltender, spektakulärer, gelbroter Herbstfärbung")]),
 "Kn02": (6592, "Kniphofia Hybride 'Ice Queen'", "cultivar", "cremeweiß", "VII–IX", "100 cm–120 cm", "sonnig", "B/Fr1-2b", "Z7", None, "Alan Bloom (Großbritannien) 1988",
          {"Schnittgeeignet": "ja", "Wintergrün": "ja"}, []),
 "Pn02": (10455, "Pennisetum alopecuroides var. viridescens", "cultivar", "schwarzbraun", "VIII–X", "60 cm–100 cm", "sonnig", "Fr2b", "Z6", KG, None, {"Schnittgeeignet": "ja"},
          [("habit", "Besonders nach warmen Sommern sind die Blüten sehr zahlreich"), ("propagation", "Bei uns erhalten Sie einen vegetativ vermehrten, sicher blühenden Typ dieser Varietät.")]),
 "Ru01": (6300, "Rudbeckia fulgida var. sullivantii 'Goldsturm'", "cultivar", "goldgelb, schwarze Mitte", "VIII–X", "60 cm–80 cm", "sonnig", "B/Fr/GR2-3", "Z4", RG,
          "Karl Foerster & Heinz Hagemann (DE) 1936", {"Schnittgeeignet": "ja"},
          [("soil", "Diese reichblühende Herbststaude liebt einen ausreichend feuchten und relativ nährstoffreichen Boden in sonniger oder halbschattiger Lage."),
           ("seasonal_foliage", "Durch seine Samenstände ist der Sonnenhut auch im Winter noch attraktiv.")]),
 "Ru02": (6264, "Rudbeckia fulgida var. sullivantii 'Little Goldstar'", "cultivar", "goldgelb, schwarze Mitte", "VIII–X", "40 cm–50 cm", "sonnig", "B/Fr/GR2-3", "Z4", RG, "Jelitto Seeds",
          {"Schnittgeeignet": "ja"},
          [("habit", "'Little Goldstar' ist die kompakte, in allen Teilen zierlicher bleibende \"kleine Schwester\" der allseits bekannten und weit verbreiteten Rudbeckia 'Goldsturm'."),
           ("pruning", "Nach der Blüte schneidet man Rudbeckien möglichst nicht zurück")]),
 "Ru04": (10961, "Rudbeckia subtomentosa 'Little Henry'", "cultivar", "hellgelb, braune Mitte", "VII–IX", "90 cm–110 cm", "sonnig", "Fr/GR2b", "Z5", None, "Harini Korlipara (US)", {},
          [("habit", "die Kompaktausgabe dieses interessanten Hoch- und Spätsommerblühers")]),
 "Ty03": (5508, "Thymus longicaulis ssp. odoratus", "species", "rosa", "VI–VII", "10 cm–15 cm", "sonnig", "St/FS/M1", "Z5", RG, None, {"Wintergrün": "ja"},
          [("habit", "Der wüchsige Kaskaden-Thymian mit seinem dichten, kissenförmigen Wuchs wirkt über Trockenmauern und aus Ampeln hängend einfach fantastisch.")]),
 "Ty06": _SER, "Ty07": _SER, "Ty10": _SER,
 "Ty08": (7247, "Thymus serpyllum 'Coccineus'", "cultivar", "karminrot", "VI–VIII", "5 cm", "sonnig", "St/M/Fr/H1", "Z5", KG, "(GB) vor 1890", {"Blattfarbe": "rot", "Wintergrün": "ja"},
          [("seasonal_foliage", "Wüchsiger, wohlriechender Bodendecker mit dunkelgrünen, im Winter rötlichen Blättern."), ("spread_mode", "Bildet schöne dichte und ordentliche Matten."),
           ("pollinator", "Seine lang anghaltende Blütezeit und das reiche Nektarangebot machen diesen Thymian zur wertvollen Trachtpflanze für Honigbienen.")]),
 "Ty11": (5734, "Thymus vulgaris", "species", "hell-lila", "VI–VII", "20 cm–30 cm", "sonnig", "St/FS/Fr1", "Z6", RG, None, {"Wintergrün": "ja"},
          [("native_range", "Der 'Echte Thymian' stammt ursprünglich aus dem Mittelmeergebiet."),
           ("propagation", "Die generativ (durch Aussaat) vermehrten Pflanzen, können in Wuchs und Aroma sehr unterschiedlich ausfallen.")]),
 "Ty01": (3648, "Thymus x citriodorus 'Aureus'", "cultivar", "hellrosa", "VI–VII", "10 cm–15 cm", "sonnig", "St/FS/M1", "Z7", RG, "Elliott (GB) 1923",
          {"Blattfarbe": "gelb", "Wintergrün": "ja"},
          [("habit", "Kissenförmiger Thymian mit goldgelber Laubfärbung"), ("winter", "Leider ist der Gold-Thymian nicht immer ganz winterhart")]),
}
