# Gaißmayer（s17）: セダム・エキナセア・アスチルベ。2026-11-19 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。
# 探し方は batch_03/gaissmayer_data.py と同じ（サイト内検索: Sedum 29件・Echinacea 24件・Astilbe 17件の掲載名を照合 → 一致した商品ページ ?static の表と本文）。
# 開いた直後に確認画面が一度出たが、十数秒待つと自動で通った（操作はしていない）。
# Gaißmayer は 'Autumn Joy' を Sedum Telephium-Hybride 'Herbstfreude'、'Matrona' を Sedum Telephium-Hybride と書いている。
# 使っていないもの: Echinacea purpurea 'Alba'（URL には white-swan とあるが表記は 'Alba'。'White Swan' と同じか分からない）、
#   'Magnus Superior'（'Magnus' とは別の品種）、Sedum cauticola 'Robustum'。質問への回答は読んでいない。価格・在庫は写していない。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-19"
_PUR = (2693, "Echinacea purpurea", "species", "purpurrosa", "VII–IX", "80 cm–100 cm", "sonnig", "B/Fr1-2", "Z3", None, None, {"Schnittgeeignet": "ja"},
        [("soil", "Sie liebt nährstoffreiche, sonnige Standorte und bevorzugt warme, durchlässige Böden."),
         ("native_range", "In lichten Wäldern und Prärien Nordamerikas vorkommende Wildstaude")])
GAISS = {
 "B02": (6873, "Astilbe Arendsii-Hybride 'Fanal'", "cultivar", "granatrot", "VII–VIII", "70 cm", "absonnig, halbschattig", "B/GR/G/Fr2-3", "Z5", "keine Gefahr",
         "Georg Arends (DE) 1933", {"Blattfarbe": "dunkelgrün", "Schnittgeeignet": "ja"},
         [("habit", "'Fanal' ist eine sehr schöne, auffallende, niedrige, eher spät blühende Sorte mit attraktivem dunklem Laub")]),
 "D02": (7371, "Sedum Telephium-Hybride 'Herbstfreude'", "cultivar", "altrosa, später rostrot", "IX–X", "50 cm–70 cm", "sonnig", "Fr/St/FS/B1-2", "Z5", "keine Gefahr",
         "Werner Arends (DE) 1955", {"Duftend": "ja", "Schnittgeeignet": "ja"},
         [("habit", "'Herbstfreude' zeichnet sich durch eine lange Blütezeit und standfeste Stängel aus, die noch lange im Winter zieren"),
          ("sun", "Sie gedeiht auch auf guten Gartenböden und halbschattigen Stellen noch bestens")]),
 "D04": (6684, "Sedum cauticola 'Bertram Anderson'", "cultivar", "rosarot", "VI–VIII", "15 cm–20 cm", "sonnig", "St/FS/M/MK1", "Z6", "keine Gefahr", None, {"Blattfarbe": "rot"},
         [("habit", "Niedrige, horstig wachsende Fetthenne mit niederliegend-aufsteigenden, anmutig gebogenen, dunklen Trieben und pflaumenvioletten Blättern")]),
 "D08": (3299, "Sedum Telephium-Hybride 'Matrona'", "cultivar", "rosa", "VIII–X", "60 cm–70 cm", "sonnig", "Fr/St/FS/B1-2", "Z4", "keine Gefahr", "Ewald Hügin (DE) 1994",
         {"Blattfarbe": "rot", "Schnittgeeignet": "ja"},
         [("soil", "Verträgt relativ nährstoffreiche Böden, sofern diese durchlässig sind."), ("habit", "Sehr haltbar und den ganzen Winter attraktiv.")]),
 # 'Mediovariegatum' は表で Z7、Lebensbereich が「nicht winterharte Stauden」（冬越ししにくい扱い）。鉢植えと春植えを勧めている。ゾーンは記録だけだが、ユーザーに伝える
 "D13": (4406, "Sedum sieboldii 'Mediovariegatum'", "cultivar", "rosa", "IX–X", "15 cm", "sonnig", "St1-2 MK2 KÜBEL（nicht winterharte Stauden）", "Z7", None, None,
         {"Pflanz-Zeitpunkt": "Frühjahrspflanzung empfohlen"},
         [("use", "Am besten kultiviert man diese buntlaubige Form aber in Pflanzgefäßen")]),
 "E04": (6834, "Echinacea pallida", "cultivar", "hellrosa", "VII–IX", "80 cm", "sonnig", "Fr/GR2", "Z4", None, None, {"Schnittgeeignet": "ja"},
         [("soil", "Für warme, durchlässige, nährstoffreiche Böden."), ("cut_flower", "Gute Schnittblume.")]),
 "E05": (6822, "Echinacea pallida 'Hula Dancer'", "cultivar", "weiß mit rosa Hauch", "VII–IX", "80 cm", "sonnig", "Fr/GR2", "Z4", None, "Jelitto (DE)", {"Schnittgeeignet": "ja"},
         [("soil", "Die in der Blüte variable Sämlingssorte liebt warme, durchlässige, nährstoffreiche Böden an vollsonnigen Plätzen.")]),
 "E06": (7905, "Echinacea paradoxa", "cultivar", "gelb, braunes Blütenköpfchen", "VII–X", "80 cm", "sonnig, absonnig, halbschattig", "Fr/GR/G1-2", "Z4", None, None,
         {"Schnittgeeignet": "ja"},
         [("soil", "Der Gelbe Sonnenhut liebt einen durchlässigen, trockenen Boden."),
          ("sun", "Neben dem für Echinaceen charakteristischen sonnigen Standort gedeiht Echinacea paradoxa auch noch gut im Halbschatten.")]),
 "E07": _PUR,
 "E08": (1803, "Echinacea purpurea 'Fatal Attraction' ®", "cultivar", "dunkel-purpurrosa", "VII–IX", "60 cm–70 cm", "sonnig", "B/Fr1-2", "Z3", None, "Piet Oudolf (NL) 2001",
         {"Schnittgeeignet": "ja"}, []),
 "E09": _PUR,
 "E10": (8654, "Echinacea purpurea 'Green Jewel' ®", "cultivar", "grün, dunkelgrüner Kegel", "VII–VIII", "70 cm", "sonnig", "B/Fr1-2", "Z3", None, "Piet Oudolf (NL)",
         {"Duftend": "ja", "Schnittgeeignet": "ja"}, [("fragrance", "Getoppt wird diese ungewöhnliche Erscheinung durch einen leichten, angenehmen Duft.")]),
 "E11": _PUR, "E12": _PUR,
 "E13": (2843, "Echinacea purpurea 'Vintage Wine' ®", "cultivar", "tief purpurrosa", "VII–IX", "70 cm–90 cm", "sonnig", "B/Fr1-2", "Z3", None, "Piet Oudolf (NL)",
         {"Schnittgeeignet": "ja"}, []),
 "E14": (8323, "Echinacea purpurea 'Virgin' ®", "cultivar", "weiß, grüne Mitte", "VII–IX", "50 cm–60 cm", "sonnig", "B/Fr1-2", "Z3", None, "Piet Oudolf (NL)",
         {"Schnittgeeignet": "ja"}, [("habit", "mit ihrem kompakten Wuchs und ihren nahezu reinweißen Blüten eine deutliche Verbesserung der Sorte 'Jade'")]),
 "E15": _PUR,
}
