# Gaißmayer（s17）: アスクレピアス・クロコスミア・ガイラルディア・アガスタチ・カリオプテリス・クナウティア・レウイシア・ルピナス・オリガヌム・ペオニア・パルテノキッスス・シダルセア・
#   アラビス・カルーナ・カマエメルム・クリサンセマム・キミキフーガ・ドラコセファラム。
# 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/gaissmayer_data.py と同じ
#   （サイト内検索: 属名18個と Actaea・Nipponanthemum・Tripora → 一致した商品ページ ?static 17ページ）。7秒おき、1回の指示は6ページまで。
#   このまとまりの最初の1ページで確認画面が出た。操作せずに置き、RHS とシカゴ植物園の一覧を見ている間（3分ほど）に自動で通った。そのあとは出なかった。
#   商品ページは、番号さえ合っていれば途中の語が違っても開いた（/web/shop/a/b/384/x/<番号>/?static）。検索結果からは番号だけ拾えばよい。
# 本文は先頭の約500字だけを見ている。質問への回答は読んでいない。価格・在庫は写していない。
# Gaißmayer の書き方: アガスタチの2品種は Agastache Rugosa-Hybride、'Lucifer' は Crocosmia masoniorum 'Lucifer'、ガイラルディアは Gaillardia x grandiflora 'Burgunder'・'Kobold'、
#   ルピナスは Lupinus Polyphyllus-Hybride 'Kronleuchter'・'Fräulein'、'Herrenhausen' は Origanum Laevigatum-Hybride、'Paula Fay' は Paeonia Hybride、
#   アラビスは Arabis ferdinandi-coburgii 'Variegata'（i が2つ）、八重のローマンカモミールは Chamaemelum nobile 'Plenum'（'Flore Pleno' と同じ八重の品種として当てた）。
# 種のページを当てたもの: クナウティア マケドニカ（Kt03）、オレガノ ブルガレ（Or02・Or03。'Thumbles Variety' は別の黄葉の品種なので当てていない）。
# 掲載なし・当てていないもの: アスクレピアス（tuberosa ssp. interior だけ）、クロコスミアのほかの3品種、ガイラルディア 'Amber Wheels'・'Mesa Peach'、アガスタチ 'Red Fortune'
#   （mexicana は 'Sangria' だけ）、カリオプテリス（'Dark Knight'・'Worcester Gold' はなし。ディバリカータもなし）、レウイシア・パルテノキッスス・カルーナ（検索で該当なし）、
#   ルピナス ペレニス、'Coral Sunset'（'Coral Charm' は別の品種）、シダルセア マルビフローラの2品種（'Elsie Heugh' だけ）、アラビス 'Pixie Cream'、
#   ハマギク・コハマギク（Chrysanthemum 26件は Indicum-Hybride など）、サラシナショウマの種そのもの・'Black Negligee'（simplex は 'Atropurpurea'・'Brunette'・'Chocoholic'・'White Pearl'）、
#   ドラコセファラム アルグネンセ（ruyschiana だけ）。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-20"
S3 = "sonnig, absonnig, halbschattig"
S2 = "sonnig, absonnig"
KG = "keine Gefahr"
FP = "Frühjahrspflanzung empfohlen"
_KNA = (7069, "Knautia macedonica", "species", "dunkelweinrot", "VII–IX", "60 cm–100 cm", "sonnig", "Fr/GR1-2", "Z5", KG, None, {"Schnittgeeignet": "ja"},
        [("self_seed", "Am passenden Standort kann sich die Witwenblume auch versamen."),
         ("native_range", "An ihrem Naturstandort im mittleren Balkan kann man sie in offenen Wäldern und Gebüschen finden."),
         ("habit", "Diese reich und lange blühende, anspruchslose Wildstaude eignet sich bestens für die Verwendung in sonnigen bis absonnigen Rabatten, Böschungen und Steppenpflanzungen.")])
_ORI = (4720, "Origanum vulgare", "species", "rosa", "VII–IX", "25 cm–40 cm", "sonnig", "Fr/SH/St/FS1", "Z5", KG, None,
        {"Duftend": "ja", "Wildstaude": "ja", "Schnittgeeignet": "ja"},
        [("self_seed", "Im Naturgarten ist die Magerrasenart sehr gut zur Verwilderung geeignet, weil sie sich vor allem durch Aussaat üppig ausbreitet."),
         ("native_range", "In Deutschland ist Origanum vulgare recht weit verbreitet. Man findet ihn auf Halbtrockenrasen und in lichten Gebüschen.")])
GAISS = {
 "Aa01": (2700, "Agastache Rugosa-Hybride 'Black Adder'", "cultivar", "blauviolett, dunkle Kolben", "VII–IX", "90 cm–120 cm", "sonnig", "B/Fr1-2", "Z6", None,
          "Coen Jansen (Niederlande)", {"Duftend": "ja", "Steril": "ja", "Schnittgeeignet": "ja"},
          [("pollinator", "Diese Duftnessel begeistert mit ihren wunderschönen Blütenkerzen nicht nur uns, sondern lockt auch zahlreiche Schmetterlings- und Falterarten an"),
           ("habit", "Die gut standfeste Staude hat eine ausgesprochen lange Blütezeit."),
           ("seasonal_foliage", "Auch nach der Blüte ist sie ein ansprechender Blickfang und bietet selbst im Winter noch eine schöne, aufrechte Silhouette.")]),
 "Aa02": (6805, "Agastache Rugosa-Hybride 'Blue Fortune'", "cultivar", "blauviolett", "VII–IX", "60 cm–70 cm", "sonnig", "B/Fr1-2", "Z6", None,
          "Fortgens (NL) 1993", {"Duftend": "ja", "Steril": "ja", "Schnittgeeignet": "ja"},
          [("habit", "Kompakte, standfeste Blüten- und Blattduftstaude mit sehr langer Blütezeit und purpurblauen Blütenkerzen."),
           ("pollinator", "Die Blaunessel ist bei Schmetterlingen und Bienen sehr beliebt"),
           ("seasonal_foliage", "sie hat auch eine schöne Wintersilhouette")]),
 "Ab02": (2236, "Arabis ferdinandi-coburgii 'Variegata'", "cultivar", "weiß", "IV–V", "5 cm–10 cm", S2, "St/M/MK2", "Z6", KG, None,
          {"Blattfarbe": "panachiert", "Wintergrün": "ja"},
          [("habit", "Diese kleinblättrige Gänsekresse bildet zierliche Polster mit weiß-grünen Blättchen."),
           ("pruning", "Gelegentlich tauchen einzelne grüne Rosetten in den kompakten, weiß-bunten Polstern auf. Diese sollten entfernt werden")]),
 "Cm01": (9580, "Chamaemelum nobile", "cultivar", "weiß, Mitte gelb", "VI–VII", "15 cm–20 cm", S3, "Fr/St/MK/M 2", "Z4", None, None, {"Duftend": "ja", "Wintergrün": "ja"},
          [("pruning", "Nach der Blüte hart zurückschneiden."),
           ("soil", "Die traditionelle Heilpflanze verlangt einen sonnigen, sommerwarmen, wasserdurchlässigen, nicht zu nährstoffreichen Standort."),
           ("habit", "Die Römische Kamille bildet einen schönen Duftrasen mit Apfelduft, der jedoch nicht ganz so trittfest ist wie normaler Rasen.")]),
 "Cm02": (3633, "Chamaemelum nobile 'Plenum'", "cultivar", "weiß, gefüllt", "VI–VIII", "15 cm", S3, "Fr/St/MK/M 2", "Z4", None, None, {"Duftend": "ja", "Wintergrün": "ja"},
          [("habit", "sie wächst teppichartig und ihr Laub duftet beim Zerreiben nach Apfel"), ("pruning", "Nach der Blüte hart zurückschneiden.")]),
 "Cr01": (4917, "Crocosmia masoniorum 'Lucifer'", "cultivar", "scharlachrot", "VII–VIII", "80 cm–120 cm", S2, "B/Fr2", "Z7", KG, "Alan Bloom (Großbritannien) 1966",
          {"Pflanz-Zeitpunkt": FP, "Schnittgeeignet": "ja"},
          [("winter_protection", "Obwohl 'Lucifer' als die härteste Sorte gilt, ist in rauen Lagen Winterschutz ratsam und Frühjahrspflanzung der Knollen "
                                 "oder das Setzen bereits getopfter Pflanzen im Sommer ideal."),
           ("habit", "Außerhalb der Blütezeit schmücken die schwertförmigen Blätter.")]),
 "Gl02": (2396, "Gaillardia x grandiflora 'Burgunder'", "cultivar", "tiefrot", "VII–IX", "50 cm", "sonnig", "B2", "Z6", None, "Benary & Walther (Deutschland) 1931",
          {"Schnittgeeignet": "ja"}, [("habit", "Mit bis zu 50 cm Höhe bleibt 'Burgunder' eher kompakt.")]),
 "Gl03": (4557, "Gaillardia x grandiflora 'Kobold'", "cultivar", "gelb mit rot", "VII–IX", "30 cm", "sonnig", "B2", "Z6", None, "Benary & Walther (Deutschland) 1935",
          {"Schnittgeeignet": "ja"}, [("habit", "Die beliebte Sorte ist sehr standfest.")]),
 "Kt01": _KNA[:2] + ("cultivar",) + _KNA[3:], "Kt03": _KNA,
 "Kt02": (9942, "Knautia macedonica 'Mars Midget'", "cultivar", "rubinrot", "VI–X", "40 cm", "sonnig", "Fr/GR/B1-2", "Z5", KG, None, {"Schnittgeeignet": "ja"},
          [("soil", "'Mars Midget' gedeiht an sonnigen Standorten mit gut durchlässigen, nicht sauren Böden und ist dabei niedriger und kompakter als die reine Art."),
           ("native_range", "Beheimatet ist sie in Bulgarien und auf dem Balkan.")]),
 "Lu01": (9148, "Lupinus Polyphyllus-Hybride 'Kronleuchter'", "cultivar", "gelb", "VI–VIII", "80 cm", "sonnig", "B/Fr2", "Z3", None, "Benary (Deutschland) 1958",
          {"Giftklasse": "stark giftig ++", "Duftend": "ja", "Schnittgeeignet": "ja"}, []),
 "Lu02": (3564, "Lupinus Polyphyllus-Hybride 'Fräulein'", "cultivar", "cremeweiß", "VI–VIII", "80 cm", "sonnig", "B/Fr2", "Z3", None, "Benary (Deutschland) 1958",
          {"Giftklasse": "stark giftig ++", "Duftend": "ja", "Schnittgeeignet": "ja"},
          [("habit", "Die zart schmeichelnde, cremeweiße Sorte überzeugt durch ihre lang ausdauernde Blüte.")]),
 "Or01": (1881, "Origanum Laevigatum-Hybride 'Herrenhausen'", "cultivar", "purpurrosa", "VII–IX", "40 cm–60 cm", "sonnig", "Fr/FS/SH/St1", "Z5", KG, "Heinz Hagemann (DE) 1981",
          {"Schnittgeeignet": "ja"},
          [("pruning", "Ein kompletter Rückschnitt nach der Blüte verhindert unerwünschtes Versamen und fördert die Vitalität der Pflanze."),
           ("habit", "Reich verzweigte und lange blühende Zierform.")]),
 "Or02": _ORI, "Or03": _ORI,
 "Py02": (2668, "Paeonia Hybride 'Paula Fay'", "cultivar", "malvenrosa, halbgefüllt", "V–VI (früh)", "80 cm", "sonnig", "B2", "Z6", KG, "Fay (US) 1968",
          {"Giftklasse": "schwach giftig (+)", "Schnittgeeignet": "ja"},
          [("habit", "Ganz gerade Stiele, perfekter Wuchs und gesundes dunkelgrünes Laub runden das Gesamtbild dieser früh blühenden, mittelhohen Pfingstrose ab."),
           ("award", "Als Sämling von 'Bravura' erhielt 'Paula Fay' 1988 eine APS Goldmedaille.")]),
 "Py03": (3860, "Paeonia lactiflora 'Sarah Bernhardt'", "cultivar", "hellrosa, gefüllt", "VI (spät)", "100 cm–110 cm", "sonnig", "B2", "Z6", KG, "Victor Lemoine (FR) 1906",
          {"Giftklasse": "schwach giftig (+)", "Duftend": "ja", "Schnittgeeignet": "ja"},
          [("cut_flower", "'Sarah Bernhardt' eignet sich sehr gut zum Trocknen, denn die Blütenblätter rieseln nicht aus.")]),
 "Sd01": (7047, "Sidalcea candida 'Bianca'", "cultivar", "weiß", "VII–IX", "80 cm–100 cm", "sonnig", "B/Fr2-3", "Z5", None, None, {"Schnittgeeignet": "ja"},
          [("soil", "Sie eignet sich gut für frische und durchlässige Standorte. Schwere Lehmböden die zu Staunässe neigen werden ebenso wenig vertragen wie längere Trockenheit."),
           ("habit", "In unseren Breiten ist Sidalcea candida die ausdauerndste und problemloseste Art der Präriemalve.")]),
}
