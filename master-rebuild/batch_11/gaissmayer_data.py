# Gaißmayer（s17）: ジギタリス・プリムラ・ユーパトリウム・ベルゲニア・カラマグロスティス・デスカンプシア・フクシア・アイリス・ロニセラ。
# 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/gaissmayer_data.py と同じ
#   （サイト内検索: Digitalis・Primula・Eupatorium・Eutrochium・Bergenia・Calamagrostis・Deschampsia・Fuchsia・Iris・Iris sibirica／pumila／chrysographes／ensata・Lonicera・Geissblatt
#     → 一致した商品ページ ?static 15ページ）。6秒おき。最初の検索で確認画面が出たが、操作せずに別の作業をしている間に自動で通った。
# 本文は先頭の約470字だけを見ている。質問への回答は読んでいない。価格・在庫は写していない。
# Gaißmayer の書き方: Pr02 'Blue Selection' は Primula denticulata 'Blaue Auslese'（実生で色に幅のある混合）、'Hawkshead' は Fuchsia Magellanica-Hybride、
#   ブラキトリカのアドレスは calamagrostis-achnatherum-brachytricha、グランディフローラは別名 Digitalis ambigua を併記。
# 種のページを当てたもの: ジギタリス プルプレア（Wildform）を Dg06・Dg08・Dg09 に。
# 掲載なし: ジギタリス メルトネンシス・パービフローラ・'Elsie Kelsey'・'Monstrosa'、プリムラ コルツソイデス・'Green Lace'（'Gold Lace' は別の品種）、
#   ユーパトリウムの該当品種（fistulosum は 'Album'・'Riesenschirm' など別の品種だけ。maculatum・coelestinum・fortunei はなし）、
#   ベルゲニア（交配品種だけ。'Redstart'・'Snow Time'・エメイエンシスはなし）、カラマグロスティス 'Avalanche'・エピジジョス、
#   デスカンプシア（'Goldschleier'・'Bronzeschleier'・'Palava'・'Tardiflora' だけ。'Goldtau' などはなし。種そのもの・フレクシオーサもなし）、
#   フクシアの 'Hawkshead' 以外（magellanica は var. gracilis と 'Arauco' だけ）、アイリスの該当品種、ロニセラ（掲載なし）。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-20"
S3 = "sonnig, absonnig, halbschattig"
KG = "keine Gefahr"
RG = "relativ geringe Gefahr"
TOX = "sehr stark giftig +++"
_PUR = (9497, "Digitalis purpurea (Wildform)", "species", "rot", "VI–VII", "80 cm–100 cm", S3, "GR/Fr2", "Z5", RG, None,
        {"Giftklasse": TOX, "Wildstaude": "ja", "Schnittgeeignet": "ja", "Wintergrün": "ja"},
        [("soil", "Sehr robust, versagt aber auf zu kalkreichen Standorten."), ("self_seed", "Zweijährig. Bei offenem Boden Selbstaussaat.")])
_JAP = "GR2-3 Fr3 WR4"
GAISS = {
 "Dg01": (5889, "Digitalis grandiflora", "cultivar", "hellgelb", "VI–VIII", "60 cm–80 cm", "sonnig", "GR/Fr/H1-2", "Z5", RG, None,
          {"Giftklasse": TOX, "Wildstaude": "ja", "Schnittgeeignet": "ja", "Wintergrün": "ja"},
          [("habit", "Langlebige Art für naturnahe, warme Staudensäume mit trockenen bis frischen, durchlässigen Böden.")]),
 "Dg02": (6049, "Digitalis lutea", "cultivar", "hellgelb", "VI–VIII", "60 cm–100 cm", S3, "GR/Fr2", "Z5", RG, None,
          {"Giftklasse": TOX, "Wildstaude": "ja", "Schnittgeeignet": "ja", "Wintergrün": "ja"},
          [("habit", "Zierliche, recht ausdauernde Art mit frischgrünen Winterrosetten."),
           ("soil", "Gerne auf kalkhaltigen, warmen, steinigen Lehmböden in der Sonne und im Halbschatten.")]),
 "Dg05": (7034, "Digitalis purpurea 'Apricot'", "cultivar", "gelblich-rosa", "VI–VII", "80 cm–100 cm", S3, "GR/Fr2", "Z5", RG, "Sutton (GB)",
          {"Giftklasse": TOX, "Schnittgeeignet": "ja", "Wintergrün": "ja"},
          [("soil", "Sehr robust, versagt aber auf zu kalkreichen Standorten."),
           ("self_seed", "Zweijährig. Bei offenem Boden erhält sie sich über Selbstaussaat, ohne lästig zu werden.")]),
 "Dg07": (3954, "Digitalis purpurea 'Excelsior'", "cultivar", "weiß bis rot", "VI–VII", "80 cm–150 cm", S3, "GR/Fr2", "Z5", RG, "Sutton (GB) 1950",
          {"Giftklasse": TOX, "Schnittgeeignet": "ja", "Wintergrün": "ja"},
          [("habit", "Großblütige Farbmischung in Purpur-, Rosa- und Weißtönen. Die Einzelblüten stehen rundum waagerecht ab.")]),
 "Dg10": (5797, "Digitalis purpurea 'Snow Thimble'", "cultivar", "reinweiß", "VI–VII", "80 cm–100 cm", S3, "GR/Fr2", "Z5", RG, None,
          {"Giftklasse": TOX, "Schnittgeeignet": "ja", "Wintergrün": "ja"},
          [("self_seed", "Die zweijährige Pflanze erhält sich an zusagenden Standorten (gerne Gebüschränder und Lichtungen) durch Selbstaussaat."),
           ("soil", "Bevorzugt wird einen lockeren, nicht zu kalkreichen, humosen und frischen Boden.")]),
 "Dg06": _PUR, "Dg08": _PUR, "Dg09": _PUR,
 "Pr02": (6255, "Primula denticulata 'Blaue Auslese'", "cultivar", "blau-violette Töne", "III–V", "15 cm–30 cm", "absonnig, halbschattig", "GR/Fr/St2-3", "Z5", None, None,
          {"Schnittgeeignet": "ja"}, [("propagation", "Wir bieten Sämlingspflanzen in einer variablen Farbmischung an!")]),
 "Pr03": (6691, "Primula japonica 'Alba'", "cultivar", "weiß", "V–VII", "25 cm–60 cm", "halbschattig", _JAP, "Z5", None, None, {"Schnittgeeignet": "ja"},
          [("habit", "Die weiße Auslese der Primula japonica mit 3-5 großen Blütenquirlen")]),
 "Pr04": (4847, "Primula japonica 'Appleblossom'", "cultivar", "zartrosa mit rotem Auge", "V–VII", "60 cm", "halbschattig", _JAP, "Z5", None, None, {"Schnittgeeignet": "ja"},
          [("heat_humidity", "'Appleblossom'schätzt keine allzu sonnigen oder gar heißen Standorte."),
           ("soil", "Halbschattige Plätze und ein nicht austrocknender und eher kalkarmen Boden sind die idealen Bedingungen für gutes Gedeihen.")]),
 "Pr05": (2936, "Primula japonica 'Millers Crimson'", "cultivar", "karminrot", "V–VII", "25 cm–60 cm", "halbschattig", _JAP, "Z5", None, None, {"Schnittgeeignet": "ja"},
          [("habit", "Die leuchtend roten, großen Blüten der Sorte 'Millers Crimson' fallen besonders durch ihr schwarzrotes Auge auf.")]),
 "Pr07": (3899, "Primula veris", "cultivar", "goldgelb", "IV–V", "10 cm–20 cm", S3, "Fr/GR1-2", "Z5", None, None,
          {"Duftend": "ja", "Wildstaude": "ja", "Schnittgeeignet": "ja"},
          [("native_range", "Die bei uns, aber auch bis nach Mittelasien verbreitete Heilpflanze schmückt sich mit in Dolden vereinigten goldgelben Blüten")]),
 "Cg02": (5208, "Calamagrostis x acutiflora 'Karl Foerster'", "cultivar", "silbrigrosa", "VI–VIII", "100 cm–150 cm", "sonnig", "Fr/B1-2", "Z4", KG, "Karl Foerster (DE) 1950",
          {"Steril": "ja", "Schnittgeeignet": "ja"},
          [("self_seed", "Sein früher Austrieb sowie die frühe und sterile Blüte machen das Gras besonders wertvoll."),
           ("pruning", "Erst im zeitigen Frühjahr sollten sie rechtzeitig vor dem frühen Austrieb abgeschnitten werden."),
           ("seasonal_foliage", "Die kerzengeraden, standfesten Halme mit den weizenfarbenen Rispen bleiben den ganzen Winter hindurch erhalten und haben einen hohen Zierwert.")]),
 "Cg03": (3102, "Calamagrostis x acutiflora 'Overdam'", "cultivar", "silbrigrosa", "VI–VIII", "80 cm–130 cm", "sonnig, absonnig", "Fr/B1-2", "Z4", KG, "Petersen (DK) 1982",
          {"Blattfarbe": "panachiert", "Steril": "ja", "Schnittgeeignet": "ja"},
          [("habit", "Diese kompakte, standfeste Züchtung mit den feinen, weißgestreiften Blättern bleibt etwas kleiner als die Sorte 'Karl Foerster'."),
           ("seasonal_foliage", "Ein überaus bemerkenswertes Gras, das gut standfest und selbst im Winter noch attraktiv ist.")]),
 "Cg04": (8159, "Calamagrostis brachytricha", "cultivar", "silbrig-rosa", "IX–XI", "70 cm–100 cm", "sonnig", "B/Fr/GR2", "Z5", KG, None, {"Schnittgeeignet": "ja"},
          [("native_range", "Sehr dekoratives Gras aus Ostasien mit großen, walzenförmigen Blüterispen und straff aufrechtem Wuchs."),
           ("seasonal_foliage", "Die überhängenden Blätter erscheinen zeitig im Frühjahr und zeigen im Herbst oft einen Bronzeton.")]),
 "Fu04": (9837, "Fuchsia Magellanica-Hybride 'Hawkshead'", "cultivar", "reinweiß", "VII–X", "60 cm–100 cm", S3, "GR/Fr2", "Z7", KG, None,
          {"Pflanz-Zeitpunkt": "Frühjahrspflanzung empfohlen"},
          [("winter", "Sehr zu empfehlen für Pflanzgefäße ab 10 Liter Erdvolumen - bei geschützter Überwinterung!")]),
}
