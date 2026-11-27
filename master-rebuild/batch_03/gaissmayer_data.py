# Gaißmayer（s17）: フロックス・ペルシカリア・サルビア。2026-11-19 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。
# アプリ内のブラウザーでは Cloudflare の確認画面から進まなかった（ユーザーが押しても通らなかった）。Chrome では確認画面なしで開けた。
# 探し方: サイト内検索 /web/shop/suche/produkte/?filter[artikel][text_suche][werte][]=<属名>&pagination[count]=200&pagination[page]=1
#   （Phlox 96件・Salvia 57件・Bistorta 17件・Persicaria 4件）の掲載名を試行の52品種と照合し、一致した商品ページ（?static）の表と本文を読んだ。
# Gaißmayer はアンプレクシカウリスを Bistorta amplexicaulis、'Alba'・'Rosea' を 'Album'・'Roseum'、'May Night' を Salvia nemorosa 'Mainacht' と書いている。
# 'Atrosanguinea' は 'Atropurpureum' という別の名前しかなく、同じ品種か分からないので使っていない。
# 'Laura' の本文は「もとは 'Uspech' として…」と続く（'Uspech' は別の商品としても載っている）。質問への回答は今回は読んでいない。価格・在庫は写していない。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-19"
S3 = "sonnig, absonnig, halbschattig"
_NEM = (7214, "Salvia nemorosa", "species", "blauviolett", "VI + IX", "40 cm–60 cm", "sonnig", "Fr/SH1", "Z5", None, None, {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
        [("soil", "wichti ist Sonne und ein durchlässiger Boden"), ("self_seed", "An zusagenden Plätzen ist eine moderate Selbstaussaat zu beobachten")])
_PRA = (9009, "Salvia pratensis", "species", "violettblau", "V–VII + IX", "40 cm–60 cm", "sonnig", "Fr/SH1", "Z3", None, None, {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
        [("soil", "Die bekannte Wiesenblume verlangt in erster Linie einen vollsonnigen, eher trockenen Standort, ist jedoch sonst recht anspruchslos.")])
GAISS = {
 "F01": (4352, "Phlox divaricata 'Clouds of Perfume'", "cultivar", "hellblau", "IV–V", "40 cm", "absonnig, halbschattig", "B/G/GR2", "Z4", None, "Piet Oudolf (NL) 1992",
         {"Duftend": "ja", "Schnittgeeignet": "ja", "Wintergrün": "ja"},
         [("fragrance", "Der herrliche, weit schweifende Wohlgeruch erinnert an Geißblatt."), ("habit", "'Clouds of Perfume' ist wüchsig und gesund.")]),
 "F05": (8983, "Phlox paniculata 'Blue Paradise'", "cultivar", "fast blau", "VII–VIII", "100 cm", S3, "B2-3", "Z4", "relativ geringe Gefahr", "Piet Oudolf (NL) 1993",
         {"Duftend": "ja", "Schnittgeeignet": "ja"},
         [("heat_humidity", "'Blue Paradise' stellt relativ hohe Ansprüche an Boden und Klima und darf nicht zu trocken stehen. Oft gedeiht die Sorte in kühlen Regionen besonders gut.")]),
 "F08": (6200, "Phlox paniculata 'David'", "cultivar", "reinweiß", "VII–IX", "100 cm–120 cm", S3, "B/Fr2-3", "Z4", None, None, {},
         [("spread_mode", "'David' ist ein sehr wüchsiger, gesunder Wild-Phlox, der durch kurze Ausläufer allmählich große, dichte Horste bildet.")]),
 "F14": (13208, "Phlox paniculata 'Laura'", "cultivar", "rotviolett mit weißem Stern", "VII–IX", "90 cm–100 cm", S3, "B2-3", "Z4", "relativ geringe Gefahr", None,
         {"Duftend": "ja", "Schnittgeeignet": "ja"},
         [("pests", "'Laura' bildet große, dichte Blütenrispen, ist sehr wüchsig, gesund, standfest und weitgehend mehltauresistent.")]),
 "F15": (6574, "Phlox paniculata 'Nora Leigh'", "cultivar", "hell-lila, dunkles Auge", "VIII–IX", "80 cm", S3, "B2-3", "Z4", "relativ geringe Gefahr", "J. Elliott (GB)",
         {"Blattfarbe": "panachiert", "Schnittgeeignet": "ja"},
         [("foliage", "Die Panaschierung ist relativ stabil, dennoch müssen gelegentlich grüne Triebe entfernt werden."),
          ("sun", "Ein Phlox mit enormer Fernwirkung, der auch halbschattige Gartenplätze schön in Szene setzt!")]),
 "F16": (9517, "Phlox paniculata 'Red Riding Hood'", "cultivar", "kirschrot", "VII–IX", "50 cm–60 cm", S3, "B2-3", "Z4", "relativ geringe Gefahr", "Verschoor (NL) 1996",
         {"Schnittgeeignet": "ja"},
         [("habit", "Niedriger, sehr kompakter buschiger Wuchs, exzellente Standfestigkeit und eine sehr lange Blüte zeichnen 'Rotkäppchen' aus.")]),
 "R03": (3630, "Bistorta amplexicaulis 'Album'", "cultivar", "weiß", "VIII–X", "100 cm–120 cm", S3, "GR2 Fr2-3", "Z5", "keine Gefahr", None, {"Schnittgeeignet": "ja"}, []),
 "R05": (6188, "Bistorta amplexicaulis 'Blackfield' ®", "cultivar", "tiefdunkelrot", "VII–X", "80 cm–100 cm", S3, "GR2 Fr2-3", "Z5", "keine Gefahr", "Chris Ghyselen (BE) 2004",
         {"Schnittgeeignet": "ja"}, [("seasonal_foliage", "Die dunklen Blätter bekommen im Herbst eine leichte Rotfärbung an den Blatträndern")]),
 "R08": (9654, "Bistorta amplexicaulis 'Firetail'", "cultivar", "lachsrot", "VIII–X", "100 cm–120 cm", S3, "GR2 Fr2-3", "Z5", "keine Gefahr", None, {"Schnittgeeignet": "ja"},
         [("hardiness", "ist sie wohl eine der schönsten und wüchsigsten Sorten mit einer sehr guten Winterhärte")]),
 "R10": (10940, "Bistorta amplexicaulis 'JS Caliente' ®", "cultivar", "tiefrot", "VII–X", "90 cm–110 cm", S3, "GR2 Fr2-3", "Z5", "keine Gefahr",
         "Jan Spruyt - Van der Jeugd B.V.B.A. (BE) 2008", {"Schnittgeeignet": "ja"},
         [("trial_rating", "in der Sichtung verdient mit ausgezeichnet (***) bewertet, ist eine sehr attraktive, vitale, reichblütige und standfeste Sorte")]),
 "R11": (5552, "Bistorta amplexicaulis 'Orangofield' ®", "cultivar", "lachsrosa", "VII–X", "70 cm–90 cm", S3, "GR2 Fr2-3", "Z5", "keine Gefahr", "Chris Ghyselen (BE) 2005",
         {"Schnittgeeignet": "ja"}, [("habit", "Diese reich blühende, aparte Sorte ist in ihren Standort- und Pflegeansprüchen recht unkompliziert.")]),
 "R12": (7012, "Bistorta amplexicaulis 'Roseum'", "cultivar", "zartrosa", "VIII–X", "100 cm–120 cm", S3, "GR2 Fr2-3", "Z5", "keine Gefahr", None, {"Schnittgeeignet": "ja"}, []),
 "R13": (7910, "Bistorta amplexicaulise 'Taurus'", "cultivar", "dunkelrot", "VII–X", "80 cm–100 cm", S3, "GR2 Fr2-3", "Z5", "keine Gefahr", None, {"Schnittgeeignet": "ja"},
         [("group", "'Taurus' ist eine kompakt wachsende Auslese der alten Sorte 'Firetail'."),
          ("habit", "Wir schätzen an dieser kompakten Sorte die ausgezeichnete Standfestigkeit und die besonders intensive Blütenfarbe.")]),
 # 'Red Dragon' は表で Z8、Lebensbereich が「nicht winterharte Stauden」（冬越ししにくい扱い）。ゾーンは記録だけだが、ユーザーに伝える
 "R14": (1418, "Persicaria microcephala 'Red Dragon'", "cultivar", "weiß", "IX–X", "60 cm–80 cm", "halbschattig, schattig", "GR/Fr/KÜBEL2（nicht winterharte Stauden）", "Z8", None, None,
         {"Blattfarbe": "silber, gezeichnet, rot, dunkelgrün", "Pflanz-Zeitpunkt": "Frühjahrspflanzung empfohlen"},
         [("winter_protection", "Im Winter ist eine Laub- und Reisigabdeckung ratsam."),
          ("planting", "Wir empfehlen Frühjahrspflanzung, wobei man den Buntblatt-Knöterich dann vor eventuellen Spätfrösten schützen muss!")]),
 "S01": (4076, "Salvia nemorosa 'Caradonna'", "cultivar", "dunkelviolett", "VI + IX", "50 cm–60 cm", "sonnig", "Fr/B1-2", "Z5", None, "Zillmer (DE) 1996", {"Schnittgeeignet": "ja"},
         [("habit", "'Caradonna' wird etwa 60 cm hoch und hat eine schlanke, aufstrebende Figur, die kein Gewittersturm zu Fall bringt.")]),
 "S02": _NEM, "S03": _NEM, "S05": _NEM,  # 2026-11-27 S04 は種が Salvia × digenea になったので nemorosa の種のページを外した
 "S06": (3678, "Salvia officinalis", "cultivar", "violettblau", "VI–VII", "40 cm–60 cm", "sonnig", "Fr/St/FS1b", "Z6", "keine Gefahr", None,
         {"Duftend": "ja", "Schnittgeeignet": "ja", "Wintergrün": "ja"},
         [("self_seed", "Schön in naturhaften Pflanzungen, wo er sich am geeigneten Standort auch willig versamt.")]),
 "S07": _PRA,
 "S08": (2193, "Salvia pratensis 'Rose Rhapsody'", "cultivar", "rosa Töne", "V–VII + IX", "40 cm–50 cm", "sonnig", "Fr/SH1", "Z3", None, None, {"Schnittgeeignet": "ja"},
         [("pruning", "Nach Rückschnitt zuverlässig im Herbst remontierend."),
          ("soil", "Für nicht zu nährstoffreiche, warme und trockene Gartenplätze - insbesondere im Naturgarten.")]),
 "S09": (12883, "Salvia pratensis 'Sky Dance'", "cultivar", "hellblau", "V–VII + IX", "50 cm", "sonnig", "Fr/SH1", "Z3", None, "Jelitto Staudensamen GmbH (Deutschland) 2014",
         {"Schnittgeeignet": "ja"},
         [("pruning", "Ein Rückschnitt im Juli führt zu einer erneuten Blüte im Frühherbst."), ("fragrance", "Dicht verzweigt sind die Blütenähren, die dazu noch aromatisch duften.")]),
 "S10": _PRA, "S11": _PRA,
 "S14": (6290, "Salvia nemorosa 'Mainacht'", "cultivar", "dunkel-blauviolett", "V–VI + IX", "50 cm–60 cm", "sonnig", "Fr/B1-2", "Z5", None, "Karl Foerster (DE) 1960",
         {"Schnittgeeignet": "ja"}, [("habit", "Außerdem ist sie sehr standfest und hat eine hervorragende Nachblüte.")]),
 "S16": (4448, "Salvia verticillata 'Purple Rain'", "cultivar", "purpurviolett", "VII + IX", "30 cm–60 cm", "sonnig", "Fr/B1", "Z6", None, "Piet Oudolf (NL)", {"Schnittgeeignet": "ja"},
         [("soil", "Er bevorzugt lockere, humose, eher trockene Standorte in vollsonniger Lage."),
          ("pruning", "Nach der Blüte sollten die Pflanzen komplett zurückgeschnitten werden. Dies fördert ein kräftiges Remontieren und verhindert die Selbstaussaat.")]),
}
