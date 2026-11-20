# Gaißmayer（s17）: モナルダ・トラデスカンティア・スピレア・ネペタ・アネモネ・アクイレギア・セントーレア・アジュガ。
# 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/gaissmayer_data.py と同じ（サイト内検索8回 → 一致した商品ページ ?static 14ページ）。6秒おき。確認画面は出なかった。
# 本文は先頭の約500字だけを見ている（batch_08 と同じ）。質問への回答は読んでいない。価格・在庫は写していない。
# Gaißmayer の書き方: 秋明菊は Anemone Japonica-Hybride、バローのシリーズは Aquilegia Vulgaris-Hybride、'Six Hills Giant' は Nepeta x faassenii。
#   Td04 'Blue and Gold' は 'Sweet Kate' の名前で載っている（シカゴ植物園の報告は「'Sweet Kate' は 'Blue and Gold' の別名で、'Blue and Gold' が正しい名前」としている）。
# 種のページを当てたもの: モンタナ（Ce05 'Joyce'）、アジュガ レプタンス（Aj02・Aj04・Aj05。Aj03 'Chocolate Chip' は、おぎはらが tenorii としているので当てていない）。
# 掲載なし: モナルダの該当品種（あるのは 'Bee-Free'・'Bee-Happy' など別の品種）、スピレア（低木は扱いなし）、ネペタのほかの品種（'Snowflake' は別の品種）、
#   シュウメイギクの種そのもの・レベイエイ・ムルチフィダ、カナデンシス・クリサンサのオダマキ、プルケリマ、'Sunshine Charm'・'Little Doll'・'Red Cloud'。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-20"
S3 = "sonnig, absonnig, halbschattig"
KG = "keine Gefahr"
_MON = (3436, "Centaurea montana", "species", "blau", "V–VI", "40 cm–50 cm", S3, "GR/Fr1-2b", "Z3", None, None, {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
        [("self_seed", "Sie neigt dazu sich stark zu versamen."),
         ("native_range", "Die wüchsige Wildform hat ihr Verbreitungsgebiet in fast allen mittel- und südeuropäischen Bergregionen. Sie kommt dort unter lichten Gehölzen und an offenen Waldrändern vor.")])
_REP = (4545, "Ajuga reptans", "species", "lilablau", "V–VI", "15 cm", "sonnig, absonnig", "GR/Fr2-3", "Z6", KG, None, {"Wildstaude": "ja", "Wintergrün": "ja"},
        [("spread_mode", "Die rasch wachsende, Rosetten bildende Staude wächst schnell zu einem geschlossenen Teppich heran."),
         ("pollinator", "Die Blüten des Günsels halten reichlich Pollen uns sehr viel Nektar bereit.")])
GAISS = {
 "Td01": (1372, "Tradescantia x andersoniana 'Concord Grape'", "cultivar", "purpurviolett", "VI–VII + IX", "40 cm–50 cm", "sonnig", "Fr2-3b/WR4", "Z4", KG, "Vaughn (US)",
          {"Blattfarbe": "blau", "Schnittgeeignet": "ja"}, [("habit", "Sie blüht sehr reich und lange.")]),
 "Td02": (6119, "Tradescantia x andersoniana 'Innocence'", "cultivar", "weiß", "VI–VII + IX", "40 cm–50 cm", "sonnig", "Fr2-3b/WR4", "Z4", KG, None, {"Schnittgeeignet": "ja"}, []),
 "Td04": (10413, "Tradescantia x andersoniana 'Sweet Kate'", "cultivar", "violettblau", "VI–VII + IX", "30 cm–40 cm", "absonnig, halbschattig", "Fr2-3b/WR4", "Z4", KG, "Stevens (GB)",
          {"Blattfarbe": "blau, gelb", "Schnittgeeignet": "ja"},
          [("sun", "Eine sehr aparte Sorte mit gelber Laubfärbung, die nur an einem lichtschattigen Standort ihre Schönheit voll entfalten kann."),
           ("heat_humidity", "In der prallen Sonne leidet sie oftmals unter Blattverbrennungen.")]),
 "Ne04": (8772, "Nepeta x faassenii 'Six Hills Giant'", "cultivar", "violettblau", "V–VII + IX", "80 cm–90 cm", "sonnig", "B/Fr1-2", "Z4", KG, "Elliott (GB)",
          {"Steril": "ja", "Schnittgeeignet": "ja"},
          [("award", "Bei der Nepeta-Sichtung 2008 ausgezeichnet bewertete Sorte"), ("pruning", "Äußerst reichblütig, sehr gute Schmuckwirkung und nach Rückschnitt willig nachblühend."),
           ("self_seed", "Von ganz besonderem Vorteil ist, dass diese Hybriden weitgehend steril sind")]),
 "An03": (3470, "Anemone Japonica-Hybride 'Honorine Jobert'", "cultivar", "weiß, halbgefüllt", "VIII–X", "90 cm–110 cm", S3, "GR/Fr/B2", "Z6", "relativ geringe Gefahr", "Jobert (FR) 1851",
          {"Giftklasse": "giftig +", "Schnittgeeignet": "ja"},
          [("habit", "Sie braucht etwas Zeit zur Entwicklung, wird aber mit den Jahren immer schöner."), ("habit", "Diese sehr langlebige, großblütige, reich blühende historische Sorte")]),
 "An02": (10358, "Anemone Japonica-Hybride 'Pamina'", "cultivar", "magentarot, gefüllt", "VIII–X", "60 cm–80 cm", S3, "GR/Fr/B2", "Z6", "relativ geringe Gefahr", "Hans Simon (DE) 1983",
          {"Giftklasse": "giftig +", "Schnittgeeignet": "ja"},
          [("habit", "Sorte mit kompaktem Wuchs und besonders schöner, flacher, halbgefüllter Blütenform."), ("award", "Die Sorte wurde in der Staudensichtung als gut bewertet.")]),
 "Aq06": (4369, "Aquilegia Vulgaris-Hybride 'Black Barlow'", "cultivar", "schwarzviolett, gefüllt", "V–VII", "60 cm–80 cm", S3, "B/GR2", "Z4", KG, None,
          {"Giftklasse": "giftig +", "Schnittgeeignet": "ja"}, []),
 "Aq05": (4673, "Aquilegia Vulgaris-Hybride 'Bordeaux Barlow'", "cultivar", "dunkelweinrot, gefüllt", "V–VII", "60 cm–80 cm", S3, "B/GR2", "Z4", KG, None,
          {"Giftklasse": "giftig +", "Schnittgeeignet": "ja"}, []),
 "Aq04": (8116, "Aquilegia Vulgaris-Hybride 'Nora Barlow'", "cultivar", "mauverosa, grün-weiße Spitzen, gefüllt", "V–VII", "60 cm–80 cm", S3, "B/GR2", "Z4", KG,
          "Alan Bloom, Barlow (Großbritannien)", {"Giftklasse": "giftig +", "Schnittgeeignet": "ja"}, [("habit", "hat gefüllte, kugelige Blüten ohne Sporn")]),
 "Ce01": (4930, "Centaurea dealbata", "cultivar", "frischrosa", "VI–VII", "50 cm–80 cm", "sonnig", "F/GR1-2", "Z3", None, None, {"Schnittgeeignet": "ja"},
          [("pruning", "Die locker verzweigt wachsende Art remontiert im Herbst, wenn man nach der ersten Blüte einen radikalen Rückschnitt durchführt."),
           ("soil", "mag warme, locker-humose, durchlässige Böden"), ("spread_mode", "Mit den Jahren bildet die Wildstaude aus dem Kaukasus mittels Ausläufer größere Bestände.")]),
 "Ce02": (5843, "Centaurea macrocephala", "cultivar", "gelb", "VII–VIII", "100 cm–150 cm", "sonnig", "Fr/GR2", "Z3", KG, None, {"Duftend": "ja", "Schnittgeeignet": "ja"},
          [("soil", "Sie braucht durchlässigen, humosen, relativ nährstoffreichen Boden und Sonne."), ("native_range", "Die aus dem Kaukasus stammende Art")]),
 "Ce03": _MON[:2] + ("cultivar",) + _MON[3:], "Ce05": _MON,
 "Ce04": (8662, "Centaurea montana 'Alba'", "cultivar", "weiß", "V–VII", "40 cm–50 cm", S3, "GR/Fr1-2b", "Z3", None, None, {"Schnittgeeignet": "ja"},
          [("drought", "Die trockenheitsverträgliche Staude eignet sich für naturhafte Pflanzungen auf sonnigen Plätzen."),
           ("habit", "Diese historische Sorte remontiert während des ganzen Sommers ununterbrochen und blüht länger als die blaue Stammform.")]),
 "Aj01": (2807, "Ajuga reptans 'Black Scallop'", "cultivar", "tiefblau", "V–VI", "10 cm–15 cm", "sonnig, absonnig", "GR/Fr2-3", "Z6", KG, None, {"Blattfarbe": "rot", "Wintergrün": "ja"},
          [("sun", "besticht auch noch im tiefen Schatten mit seinen perfekt geformten Rosetten und dem glänzenden Laub"), ("habit", "Dabei ist er äußerst wüchsig und vital")]),
 "Aj02": _REP, "Aj04": _REP, "Aj05": _REP,
}
