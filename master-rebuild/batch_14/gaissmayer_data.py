# Gaißmayer（s17）: チャスマンティウム・ケロネ・エキノプス・エリムス・エリゲロン・ガリウム・グレコマ・カリメリス・ラベンダー・レウカンセマム・リスラム・パキサンドラ・フロミス・サギナ・
#   サポナリア・センペルビブム・シルフィウム・スティパ・シンフィオトリクム・ビバーナム・ユッカ・ヒューケレラ・トリフォリウム。
# 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/gaissmayer_data.py と同じ
#   （サイト内検索: 属名23個と Nassella・Aster・Bronco・Jolly Jumper・Jenny → 一致した商品ページ ?static 23ページ）。7秒おき、1回の指示は6ページまで。
#   このまとまりの最初の1ページでまた確認画面が出た（前のまとまりから30分ほどあいていた）。操作せずに置き、3分ほどで自動で通った。そのあとは出なかった。
# 本文は先頭の約400字だけを見ている。質問への回答は読んでいない。価格・在庫は写していない。
# Gaißmayer の書き方: 'Star Frost' は Echinops banaticus（n が1つ）、'Profusion' は Erigeron karvinskianus 'Blütenmeer'（Jelitto が 'Blütenmeer' [Profusion, Stallone] としているので当てた）、
#   サギナは「Sagina subulata (vegetativ)」（栄養繁殖の不稔の選抜）、シャスターデージーは Leucanthemum Maximum-Hybride。
# 種のページを当てたもの: ワイルドオーツ（Ch02）、ケロネ オブリクア（Cl02）、グレコマ（Gc02）、カリメリス インシサ（Ka02）、ラベンダー（La01。'Hidcote Blue' は同じ品種か分からないので当てていない）、
#   エゾミソハギ（Lt02）、フッキソウ（Pc02）、フロミス チューベロサ（Ph02）、サポナリア オフィシナリス（Sn01・Sn02）、ユッカ フィラメントサ（Yu01）。
# 掲載なし・当てていないもの: 'Little Tickler'、エリゲロン 'Rosa Juwel'（'Rosa Triumph' は別の品種）、エリムス カナデンシス、ヒューケレラの3品種（'Revolution' のシリーズだけ）、
#   シャスターデージーの2品種、'Happy Snow'、シルフィウム ラシニアツム、センペルビブム 'Bronco'、アスターの2品種（Aster 74件に 'Jolly Jumper'・'Jenny' はなかった）、
#   トリフォリウム・ビバーナム（検索で該当なし）、ユッカ グロリオーサ。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-20"
S3 = "sonnig, absonnig, halbschattig"
KG = "keine Gefahr"
RG = "relativ geringe Gefahr"
FP = "Frühjahrspflanzung empfohlen"
_CHA = (6786, "Chasmanthium latifolium", "species", "hellbraun", "VIII–X", "80 cm–100 cm", S3, "Fr2-3 GR2", "Z4", KG, None, {"Schnittgeeignet": "ja"},
        [("seasonal_foliage", "Das ebenfalls überhängende, bambusartige Laub ist frischgrün und färbt sich zum Herbst hin goldgelb."),
         ("habit", "An bogig überhängenden Halmen hängen \"platte\" Blütenähren, die im Aufblühen rosa getönt sind, um dann in einen warmen Kupferton überzugehen.")])
_CHE = (10001, "Chelone obliqua", "species", "tiefrosa", "VII–IX", "60 cm–80 cm", S3, "GR/Fr/G2-3", "Z5", KG, None, {"Schnittgeeignet": "ja"},
        [("native_range", "In ihrer Heimat wächst die attraktive Wildstaude in feuchten bis nassen lichten Wäldern."),
         ("soil", "Im Garten bevorzugt sie einen nährstoffreichen und sonnigen Standort wo sie mit der Zeit üppige Bestände bilden kann.")])
_GLE = (6398, "Glechoma hederacea", "species", "blau-violett", "III–IV", "5 cm–15 cm", S3, "GR/G/Fr2-3", "Z5", None, None,
        {"Giftklasse": "schwach giftig (+)", "Wildstaude": "ja", "Wintergrün": "ja"}, [])
_KAL = (6371, "Kalimeris incisa", "species", "weiß", "VII–IX", "60 cm–80 cm", S3, "B/Fr/GR2", "Z5", KG, None, {"Schnittgeeignet": "ja"},
        [("pruning", "Bei laufendem Rückschnitt der verblühten Triebe zuverlässig bis in den Herbst blühend."), ("habit", "Kräftiger Wuchs und schöne, reich verzweigte Blütenstände.")])
_LYT = (9327, "Lythrum salicaria", "species", "dunkelrosa", "VII–IX", "100 cm–120 cm", S3, "Fr/B2-3 WR4", "Z3", KG, None, {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
        [("soil", "eignet sich für die Verwendung in größeren Naturanlagen auf feuchten bis nassen Böden mit bis zu 5 cm Wasserstand")])
_PAC = (5000, "Pachysandra terminalis", "species", "weiß", "IV–V", "20 cm–30 cm", "halbschattig", "G/GR2", "Z5", KG, None,
        {"Giftklasse": "giftig +", "Duftend": "ja", "Schnittgeeignet": "ja", "Wintergrün": "ja"},
        [("spread_mode", "Diese aus Japan und China stammende, Ausläufer treibende Blattschmuckpflanze mit ledrigen, glänzend-grünen Blättern bildet sehr schöne, ruhig wirkende Blattteppiche."),
         ("habit", "Der immergrüne Bodendecker ist schattenverträglich und steht gut im Halbschatten von Gehölzen.")])
_SAP = (9588, "Saponaria officinalis", "species", "zart rosa", "VII–IX", "50 cm–80 cm", "sonnig", "Fr/GR2", "Z4", None, None,
        {"Giftklasse": "schwach giftig (+)", "Duftend": "ja", "Wildstaude": "ja", "Schnittgeeignet": "ja"},
        [("spread_mode", "Anspruchslose Wildstaude, die bei uns in Flußauen, an Straßenrändern und auf Ruderalfächen anzutreffen ist, mit kriechendem Wurzelstock"),
         ("habit", "Das Echte Seifenkraut ist nicht immer ganz standfest. Es liebt frische Böden in sonniger Lage.")])
GAISS = {
 "Ch01": _CHA[:2] + ("cultivar",) + _CHA[3:], "Ch02": _CHA,
 "Cl01": _CHE[:2] + ("cultivar",) + _CHE[3:], "Cl02": _CHE,
 "Ec01": (5725, "Echinops banaticus 'Star Frost'", "cultivar", "weiß", "VII–IX", "80 cm–100 cm", "sonnig", "Fr/B/GR2", "Z4", KG, None, {"Schnittgeeignet": "ja"},
          [("habit", "'Star Frost' wächst recht kompakt und erfreut auf reich verzweigten Stielen mit einer üppigen Blütenfülle."),
           ("pollinator", "Bei uns kann man zahlreiche Insekten beobachten, die von den Kugelblüten magisch angezogen werden.")]),
 "Ec02": (10962, "Echinops ritro ssp. ruthenicus 'Platinum Blue'", "cultivar", "leuchtend himmelblau", "VII–IX", "50 cm–60 cm", "sonnig", "Fr/FS1-2", "Z3", KG, None,
          {"Schnittgeeignet": "ja"}, [("habit", "diese kompakt wachsende, aus Osteuropa stammende Wildform der Kugeldistel")]),
 "Eg02": (7574, "Erigeron karvinskianus 'Blütenmeer'", "cultivar", "weiß, im Abblühen rosa", "VI–X", "20 cm–30 cm", "sonnig", "St/FS/Fr/MK2", "Z7", RG, None,
          {"Pflanz-Zeitpunkt": FP},
          [("lifespan", "In warmen Lagen bzw. in milden Wintern ist das Spanische Gänseblümchen ausdauernd, sonst kurzlebig."),
           ("self_seed", "Es versamt sich jedoch reichlich."), ("habit", "Ein liebreizender Dauerblüher, der dichte Matten bildet")]),
 "El02": (9809, "Elymus magellanicus", "cultivar", "gelblich", "VI–VII", "30 cm–60 cm", "sonnig", "Fr/B2", "Z6", KG, None, {"Blattfarbe": "blau"},
          [("habit", "problemlos winterhart, wüchsig und robust. Dazu kommt ein horstiger Wuchs wie aus dem Bilderbuch."), ("native_range", "dieses leuchtend stahlblaue Gras aus Patagonien")]),
 "Gc01": _GLE[:2] + ("cultivar",) + _GLE[3:], "Gc02": _GLE,
 "Gm01": (4755, "Galium odoratum", "cultivar", "weiß", "V", "20 cm", "halbschattig, schattig", "G/GR2", "Z5", KG, None,
          {"Giftklasse": "schwach giftig (+)", "Duftend": "ja", "Wildstaude": "ja"},
          [("spread_mode", "Waldmeister treibt Ausläufer und bevorzugt kühle, lockere, humusreiche Böden."),
           ("heat_humidity", "Waldmeister treibt Ausläufer und bevorzugt kühle, lockere, humusreiche Böden.")]),
 "Gm02": (7556, "Galium verum", "cultivar", "gelb", "V–IX", "30 cm–50 cm", "sonnig", "Gr/Fr2", "Z3", KG, None, {"Duftend": "ja", "Wildstaude": "ja"},
          [("soil", "Das Echte Labkraut bevorzugt sandig-lehmige, mäßig nährstoffreiche, kalkhaltige Böden in sonniger bis leicht schattiger Lage."),
           ("spread_mode", "Da Galium verum stark ausläufertreibend ist, sollte die Verwendung nur mit Bedacht erfolgen.")]),
 "Ka01": _KAL[:2] + ("cultivar",) + _KAL[3:], "Ka02": _KAL,
 "La01": (10750, "Lavandula angustifolia", "species", "blauviolett", "VI–VII", "60 cm–70 cm", "sonnig", "Fr/FS/SH1", "Z5", KG, None,
          {"Duftend": "ja", "Schnittgeeignet": "ja", "Wintergrün": "ja"}, []),
 "La02": (3034, "Lavandula angustifolia 'Munstead'", "cultivar", "blauviolett", "VI–VII", "40 cm–60 cm", "sonnig", "Fr/FS/SH1b", "Z5", KG, "Gertrude Jekyll / Barr (GB) 1916",
          {"Duftend": "ja", "Schnittgeeignet": "ja", "Wintergrün": "ja"},
          [("habit", "'Munstead' ist der altbekannte, gut winterharte Klassiker unter den Lavendelsorten und wird deshalb auch in öffentlichen Grünanlagen gerne verwendet.")]),
 "Lt01": _LYT[:2] + ("cultivar",) + _LYT[3:], "Lt02": _LYT,
 "Pc01": _PAC[:2] + ("cultivar",) + _PAC[3:], "Pc02": _PAC,
 "Ph01": (8494, "Phlomis russeliana", "cultivar", "gelb", "VI–VII", "60 cm–100 cm", "sonnig", "Fr/FS/GR1-2", "Z4", KG, None, {"Schnittgeeignet": "ja", "Wintergrün": "ja"},
          [("habit", "Phlomis russeliana ist ein äußerst wirkungsvoller, wintergrüner Bodendecker, der das ganze Jahr ansprechend wirkt."),
           ("seasonal_foliage", "Die später erscheinenden Fruchtstände sind ein schöner, haltbarer Schmuck im winterlichen Garten und bleiben sogar bis ins Frühjahr hinein attraktiv.")]),
 "Ph02": (3078, "Phlomis tuberosa", "species", "rosa-purpurviolett", "VI–VII", "80 cm–120 cm", "sonnig", "Fr/GR1b", "Z5", None, None, {"Schnittgeeignet": "ja"},
          [("native_range", "Gleichwohl verdient die Staude, die in Mittel- und Südosteuropa sowie im Kaukasus wild vorkommt, einen Platz in unseren Gärten.")]),
 "Sg01": (8467, "Sagina subulata (vegetativ)", "cultivar", "weiß", "VI–VII", "5 cm", "sonnig, absonnig", "St/M/SF2", "Z4", KG, None,
          {"Wildstaude": "ja", "Steril": "ja", "Wintergrün": "ja"},
          [("habit", "Die moosartige Polsterpflanze bildet mit ihrem dichtrasigen Wuchs große, sattgrüne Polster."),
           ("propagation", "Bei uns erhalten Sie nur vegetativ vermehrte, sterile Auslesen, die einheitlicher ausfallen als die generativen Varianten")]),
 "Sg02": (5358, "Sagina subulata 'Aurea'", "cultivar", "weiß", "VI–VII", "5 cm", "absonnig", "St/M/SF2", "Z4", KG, None,
          {"Steril": "ja", "Wintergrün": "ja", "Blattfarbe": "gelb, hellgrün"},
          [("habit", "Das Gold-Sternmoos bildet dichte Teppiche von lebhafter hellgrüner-gelblicher Farbe.")]),
 "Sl02": (2551, "Silphium mohrii", "cultivar", "hellgelb", "VII–IX", "120 cm–140 cm", "sonnig", "Fr1-2", "Z5", None, None, {"Duftend": "ja", "Schnittgeeignet": "ja"},
          [("habit", "Sie wächst wesentlich zurückhaltender als die größere Silphium perfoliatum.")]),
 "Sn01": _SAP, "Sn02": _SAP,
 "Su01": (2152, "Stipa ichu", "cultivar", "silbrig", "VII–IX", "70 cm–90 cm", "sonnig", "Fr/SH/St/FS1", "Z7", KG, None, {"Pflanz-Zeitpunkt": FP, "Schnittgeeignet": "ja"},
          [("habit", "Aus dem schmalen, elegant überhängenden Laub schieben sich die fedrigen, weithin leuchtenden hellsilbernen Blütenstände")]),
 "Su02": (5506, "Stipa tenuissima", "cultivar", "silbrig-weiß", "VII–VIII", "30 cm–50 cm", "sonnig", "Fr/SH/St/FS1", "Z7", KG, None,
          {"Pflanz-Zeitpunkt": FP, "Schnittgeeignet": "ja", "Wintergrün": "ja"},
          [("native_range", "Dieses aus Patagonien, aber auch aus Texas und Mexico stammende Gras"),
           ("habit", "Schon alleine das Laub ist haarfein und wiegt sich sacht im Winde hin und her.")]),
 "Yu01": (5127, "Yucca filamentosa", "species", "milchweiß", "VII–VIII", "60 cm–120 cm", S3, "B/Fr/St/FS1", "Z5", KG, None, {"Wintergrün": "ja", "Blattfarbe": "blau"},
          [("soil", "Für gut durchlässige, kalkhaltige Böden an warmen bis heißen Plätzen."),
           ("habit", "Diese Yucca-Art ist bei uns winterhart und bildet keinen Stamm aus.")]),
}
