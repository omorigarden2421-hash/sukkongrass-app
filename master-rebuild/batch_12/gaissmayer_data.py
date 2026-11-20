# Gaißmayer（s17）: シレネ・ゲンチアナ・プルサティラ・ティアレラ・アルケミラ・アンドロポゴン・ヘデラ・リグラリア・パトリニア・プルネラ・トリキルティス・ハイドランジア・アストランティア。
# 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/gaissmayer_data.py と同じ
#   （サイト内検索: Silene・Gentiana・Pulsatilla・Tiarella・Alchemilla・Andropogon・Schizachyrium・Hedera・Ligularia・Patrinia・Prunella・Tricyrtis・Hydrangea・Astrantia
#     → 一致した商品ページ ?static 15ページ）。6秒おき。最初の検索で確認画面が出たが、操作せずに置き、1分ほどで自動で通った。
# 本文は先頭の約420字だけを見ている。質問への回答は読んでいない。価格・在庫は写していない。
# Gaißmayer の書き方: 'Robin Whitebreast' は Silene uniflora 'Weißkehlchen'（ドイツ語の元の名前。Berggarten Hannover、1969年以前）、
#   'Prairie Blues' は Schizachyrium scoparium、'Shaggy' は別名 'Margery Fish' を併記。
# 種のページを当てたもの: シレネ ディオイカ（Si01）、ゲンチアナ セプテンフィダ var. ラゴデチアナ（Gn04。変種のページ）、プルサティラ ブルガリス（Ps02〜Ps04）、
#   オミナエシ（Pt02）、プルネラ グランディフローラ（Pv01・Pv02）、ホトトギス（Tc02）、アストランティア マヨール（As01・As03・As04・As05）。
# 掲載なし・当てていないもの: シレネ ユニフローラのほかの品種、ゲンチアナのほかの3種、プルサティラの 'Alba'・'Rote Glocke'（'White Bells'・'Rose Bells' と同じ品種か分からない）、
#   ティアレラの交配品種、アルケミラ サクサティリス・セリカータ、アンドロポゴン ジェラルディ（'Präriesommer' だけ）・'Blaze'、ヘデラ・ハイドランジア（掲載なし）、
#   リグラリア デンタータ（'Desdemona' だけ）、オトコエシ、タイワンホトトギス・'Tojen'、アストランティアの 'Hadspen Blood'・'Ruby Wedding'・'Vanilla Edge'・'Venice'。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-20"
S3 = "sonnig, absonnig, halbschattig"
KG = "keine Gefahr"
RG = "relativ geringe Gefahr"
_DIO = (2514, "Silene dioica", "species", "rosarot", "IV–VIII", "50 cm–60 cm", "sonnig", "Fr/GR2", "Z6", None, None, {"Wildstaude": "ja"},
        [("native_range", "finden wir in der Natur auf kalkreichen, feuchten Böden bis in Höhen von 2.400 Meter. Ihr Hauptverbreitungsgebiet ist Mittel- und Nordeuropa.")])
_PUL = (2665, "Pulsatilla vulgaris", "species", "violett", "III–IV", "20 cm–30 cm", "sonnig", "SH/Fr/St/FS1", "Z5", KG, None, {"Giftklasse": "giftig +", "Wildstaude": "ja"},
        [("soil", "Er liebt durchlässige, humos-sandige, kalkhaltige Böden und viel Sonne und erhält sich am zusagenden Standort durch Selbstaussaat."),
         ("drought", "Einmal etabliert verträgt die Küchenschelle Trockenheit recht gut.")])
_PAT = (6659, "Patrinia scabiosifolia", "species", "gelb", "VII–VIII", "60 cm–100 cm", "sonnig", "Fr/GR1-2", "Z5", None, None, {"Schnittgeeignet": "ja"},
        [("native_range", "Diese hübsche, ostasiatische Wildart stammt von sonnigen Wiesen in China, Japan, Korea und Taiwan."),
         ("fragrance", "Eigentlich auch eine gut haltbare und attraktive Schnittstaude, doch der \"Blütenduft\" ist nicht jedermanns Sache.")])
_PRG = (9185, "Prunella grandiflora", "species", "purpurviolett", "VI–VIII", "10 cm–20 cm", S3, "Fr/GR1-2", "Z5", None, None, {"Wildstaude": "ja"},
        [("soil", "Die niedrige, teppichartig wachsende Staude mit gemäßigtem Ausbreitungsdrang benötigt kalkhaltige, durchlässige, warme Lehmböden in sonniger bis halbschattiger Lage."),
         ("self_seed", "Die Art verbreitet sich am zusagenden Standort kräftig durch Selb[staussaat]")])
_AST = (10174, "Astrantia major", "species", "weißlich-rosa bis rosa", "VI–VII + IX", "50 cm–70 cm", S3, "GR/G2 Fr3", "Z6", RG, None, {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
        [("soil", "Sie mag ausreichend feuchten Boden und versamt sich."), ("self_seed", "Sie mag ausreichend feuchten Boden und versamt sich.")])
GAISS = {
 "Si01": _DIO,
 "Si03": (10315, "Silene uniflora 'Weißkehlchen'", "cultivar", "weiß", "VI–VIII", "10 cm", "sonnig", "St/FS/M/MK1-2", "Z3", None, "Berggarten Hannover (Deutschland) vor 1969",
          {"Wintergrün": "ja"},
          [("native_range", "Das weiße Leimkraut kommt an den Küsten Westeuropas vor."),
           ("soil", "Wichtig bei der Pflanzung im Garten sind ein durchlässiger, kalkhaltiger Boden und ein vollsonniger Standort.")]),
 "Gn04": (3543, "Gentiana septemfida var. lagodechiana", "species", "mittelblau", "VII–IX", "20 cm–30 cm", "sonnig", "St/FS/M2", "Z3", None, None, {"Schnittgeeignet": "ja"},
          [("soil", "Für durchlässige, steinig-lehmige, kalkhaltige Böden.")]),
 "Ps01": _PUL[:2] + ("cultivar",) + _PUL[3:], "Ps02": _PUL, "Ps03": _PUL, "Ps04": _PUL,
 "Ti04": (8406, "Tiarella wherryi", "cultivar", "weiß", "V–VII + IX", "15 cm–30 cm", "halbschattig, schattig", "G/GR2", "Z6", KG, None,
          {"Duftend": "ja", "Schnittgeeignet": "ja", "Wintergrün": "ja"},
          [("heat_humidity", "Tiarella wherryi bevorzugt lockere, humose und sauren Böden an einem kühlen Standort."),
           ("seasonal_foliage", "Die schöne kupfrige Herbst- und Winterfärbung ist ein weiterer \"Pluspunkt\" von dieser Schaumblüte."),
           ("drought", "Im Vergleich zu Tiarella cordifolia kommt sie auch zeitweise mit trockeneren Böden zurecht.")]),
 "Al01": (5735, "Alchemilla mollis", "cultivar", "grünlich-gelb", "VI–VII", "30 cm–50 cm", "sonnig, absonnig", "Fr/GR2-3", "Z5", KG, None, {"Duftend": "ja", "Schnittgeeignet": "ja"},
          [("pruning", "Ein bodennaher Rückschnitt nach der Blüte fördert einen attraktiven Neuaustrieb und verhindert zu reichliches Versamen."),
           ("soil", "Bevorzugt werden frische bis feuchte, lehmig-sandige, eher saure Böden.")]),
 "Ad03": (12882, "Schizachyrium scoparium 'Prairie Blues'", "cultivar", "silbrig-bräunlich", "VIII–X", "100 cm–120 cm", "sonnig", "Fr1-2", "Z5", KG, None, {"Schnittgeeignet": "ja"},
          [("seasonal_foliage", "mit sinkenden Temperaturen verfärbt sich das Laub von oben nach unten fortschreitend kupfer- bis orangebraun"),
           ("habit", "Blau-graues, riemenförmiges Blattwerk, dichter, halbkugeliger Wuchs")]),
 "Lg03": (5507, "Ligularia przewalskii", "cultivar", "gelb", "VII–IX", "80 cm–120 cm", S3, "GR/Fr2-3 WR4", "Z4", None, None, {"Schnittgeeignet": "ja"},
          [("drought", "Diese Art verkraftet trockenere Standorte und wird auch von Schnecken weniger \"besucht\" als die anderen Arten und Sorten."),
           ("habit", "zeichnen diese einfach zu kultivierende und anspruchslose Art aus")]),
 "Pt01": _PAT[:2] + ("cultivar",) + _PAT[3:], "Pt02": _PAT,
 "Pv01": _PRG, "Pv02": _PRG,
 "Pv03": (8691, "Prunella vulgaris", "cultivar", "blauviolett", "V–X", "10 cm–30 cm", "sonnig", "Fr/GR2", "Z3", None, None, {"Wildstaude": "ja"},
          [("spread_mode", "Die niedrige, teppichartig wachsende Staude besitzt einen enormen Ausbreitungsdrang und bildet binnen kurzer Zeit üppige Bestände."),
           ("self_seed", "Das bewältigt sie zum einen durch ihre kriechenden Triebe, die an den Nodien gerne neue Wurzeln schlagen und die überreichen Samen.")]),
 "Tc02": (4591, "Tricyrtis hirta", "species", "weißlich-lila, rot gepunktet", "VIII–X", "50 cm", "halbschattig", "GR2", "Z5", None, None,
          {"Pflanz-Zeitpunkt": "Frühjahrspflanzung empfohlen", "Schnittgeeignet": "ja"},
          [("soil", "Krötenlilien eignen sich als nicht alltäglicher Schmuck für Waldgärten und schattige Rabatten mit feuchten, kalkarmen, locker-humosen Böden."),
           ("winter", "Ein wertvoller Herbstblüher für den wir Frühjahrspflanzung empfehlen, ebenso wie ihn im Winter mit einer Laubabdeckung zu versehen.")]),
 "As01": _AST, "As03": _AST, "As04": _AST, "As05": _AST,
 "As02": (3045, "Astrantia major 'Roma'", "cultivar", "silbrig-rosa bis altrosa", "VI–VII + IX", "40 cm–60 cm", S3, "GR/G2 Fr3", "Z6", RG, "A. Geertings & Zonen B.V. (NL) 1992",
          {"Schnittgeeignet": "ja"}, [("habit", "Auf festen Stielen erscheinen ab Anfang Juni relativ große rosa bis altrosa Blütenköpfchen")]),
 "As06": (5991, "Astrantia major 'Shaggy'", "cultivar", "silbrig-weiß, grün überhaucht", "VI–VII + IX", "50 cm–60 cm", S3, "GR/G2 Fr3", "Z6", RG, None, {"Schnittgeeignet": "ja"},
          [("habit", "Diese bezaubernde Astrantie stammt aus England und ist auch unter dem Namen 'Margery Fish' im Handel.")]),
}
