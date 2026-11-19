# Gaißmayer（s17）: スカビオサ・ポレモニウム・フィリペンデュラ・サンギソルバ・トロリウス。2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。
# 探し方は batch_03/gaissmayer_data.py と同じ（サイト内検索: Scabiosa 11件・Polemonium 6件・Filipendula 5件・Sanguisorba 11件・Trollius 7件 → 一致した商品ページ ?static）。
# 最初から1ページごとに6秒あけて読んだ（検索10回・商品15ページ）。確認画面は一度も出なかった。
# Gaißmayer の書き方: Sc02 は Scabiosa caucasica 'Perfecta'、'Vivid Violet' は Scabiosa Hybride、Sa07 は Sanguisorba tenuifolia 'Albiflora'（RHS では var. alba の別名）、
#   Fi04 は Filipendula rubra 'Venusta'（マスターは 'Venusta Magnifica'）、'Pink Tanna' は Sanguisorba officinalis。
# 種のページを当てたもの: カエルレウム（Pl05・Pl06）、ウルマリア（Fi06）、オフィシナリス（Sa06）、ユーロペウス（Tr04・Tr05）。
#   Pl03 'Apricot Delight'（RHS は carneum）と Pl04 'Blue Whirl'（RHS は viscosum）には、カエルレウムのページを当てていない。
# 掲載なし: 'Compliment'・'Fama'、ポレモニウム ボレアル・エゾエンス 'Purple Rain'（あるのは 'Bressingham Purple'）、シモツケソウ・キョウガノコ、
#   アルビフローラ・カライトソウの種そのもの（あるのは 'Lilac Squirrel'）・'Lemon Splash'・'Bordeaux'、'New Moon'・'Lemon Supreme'・'Yellow Queen'・'Cheddar'。
# 質問への回答は読んでいない。価格・在庫は写していない。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-20"
S3 = "sonnig, absonnig, halbschattig"
_CAE = (10018, "Polemonium caeruleum", "species", "himmelblau", "VI–VII", "60 cm–80 cm", S3, "B/Fr/GR2-3", "Z2", "relativ geringe Gefahr", None,
        {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
        [("soil", "Sie liebt frische bis feuchte, eher nährstoffreiche Böden."),
         ("native_range", "In der Natur kommt sie in Flusstälern, auf feuchten Wiesen und Auen vor.")])
_ULM = (1691, "Filipendula ulmaria", "species", "cremeweiß", "VI–VIII", "60 cm–150 cm", S3, "Fr3 WR4", "Z2", "keine Gefahr", None,
        {"Duftend": "ja", "Wildstaude": "ja", "Schnittgeeignet": "ja"},
        [("spread_mode", "Da es sich durch Ausläufer stark ausbreitet, sollte der Platz im Garten gut gewählt werden."),
         ("native_range", "Diese häufig in der Natur vorkommende Wildstaude mit den duftenden Blüten begleitet Bachläufe und Gräben")])
_EUR = (10508, "Trollius europaeus", "species", "hellgelb", "V–VI", "50 cm", "sonnig", "Fr3 WR4", "Z5", "keine Gefahr", None,
        {"Giftklasse": "giftig +", "Wildstaude": "ja", "Schnittgeeignet": "ja"},
        [("habit", "In der Höhe, aber auch in der Ausbildung der Blütenform kann diese Trollblume - je nach Standort - stark variieren."),
         ("soil", "Die geschützte, etwas variable Art eignet sich besonders schön für natürliche Pflanzungen an Teich- und Bachufern.")])
GAISS = {
 "Sc02": (3068, "Scabiosa caucasica 'Perfecta'", "cultivar", "blau", "VII–IX", "70 cm", "sonnig", "B2", "Z4", "keine Gefahr", "Köhler & Rudel (DE) 1899", {"Schnittgeeignet": "ja"},
          [("propagation", "Locker thronen die blauen Blüten dieser generativ vermehrten Sorte auf ihrem schlanken Stiel.")]),
 "Sc04": (6429, "Scabiosa caucasica 'Perfecta Alba'", "cultivar", "reinweiß", "VII–IX", "70 cm", "sonnig", "B2", "Z4", "keine Gefahr", "Haage & Schmidt (DE) vor 1899",
          {"Schnittgeeignet": "ja"},
          [("propagation", "Die reinweißen, großen Blüten dieser über Aussaat vermehrten Sorte sind eine wertvolle Bereicherung für jeden Garten."),
           ("habit", "Auch zu Rosen und anderen Prachtstauden kann man diese robuste und unkomplizierte Staude hervorragend kombinieren.")]),
 "Sc05": (11042, "Scabiosa Hybride 'Vivid Violet'", "cultivar", "violett", "V–IX", "30 cm–40 cm", "sonnig", "St/Fr1-2b", "Z6", "keine Gefahr", None, {},
          [("drought", "Alle Scabiosen gehören aufgrund ihrer Genügsamkeit, Trockenheitstoleranz und des naturhaften Charmes zu den Gewinnerinnen des Klimawandels."),
           ("parentage", "'Vivid Violet' ging aus Scabiosa columbaria 'Pink Mist' und Scabiosa columbaria 'Giant Blue' hervor."),
           ("habit", "enorm langen Blütezeit, die über Monate bis zum Frost andauert")]),
 "Sc06": (1406, "Scabiosa ochroleuca", "cultivar", "hellgelb", "VII–IX", "60 cm–80 cm", "sonnig", "Fr/St1", "Z6", "keine Gefahr", None, {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
          [("self_seed", "Sie ist meist kurzlebig, versamt sich aber gut."),
           ("pruning", "Wem des Guten zu viel wird, sollte durch einen gezielten Teil- oder Komplettrückschnitt dem Ausbreitungsdrang dieser Pflanze Grenzen setzen."),
           ("soil", "Sie wächst dort an sonnigen Plätzen auf trockenen, kalkreichen und nährstoffarmen Böden.")]),
 "Sc07": (7876, "Scabiosa ochroleuca 'Moon Dance'", "cultivar", "hellgelb", "VII–IX", "40 cm", "sonnig", "Fr/St1", "Z6", "keine Gefahr", None, {"Schnittgeeignet": "ja"},
          [("soil", "Ein sonniger, trockener, eher magerer Standort verlängert die Lebensdauer dieser eher kurzlebigen Pflanze."),
           ("habit", "Sie unterscheidet sich von der reinen Art durch ihren niedrigen und kompakten Wuchs.")]),
 "Pl02": (4308, "Polemonium caeruleum 'Album'", "cultivar", "weiß", "VI–VII", "60 cm–80 cm", S3, "B/Fr/GR2-3", "Z2", "relativ geringe Gefahr", None,
          {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
          [("fragrance", "Die weiß blühende Form der Jakobsleiter bezaubert mit ihren zart duftenden Blüten."),
           ("soil", "lassen sich auf frischen bis feuchten Böden herrliche wiesenartige Pflanzungen anlegen")]),
 "Pl05": _CAE, "Pl06": _CAE,
 "Fi04": (10560, "Filipendula rubra 'Venusta'", "cultivar", "rosarot", "VII–VIII", "100 cm–150 cm", S3, "Fr/GR3b/WR4", "Z3", "keine Gefahr", "Hidcote Garden (GB) 1853",
          {"Duftend": "ja", "Schnittgeeignet": "ja"},
          [("soil", "Die Spierstaude benötigt einen mehr oder weniger feuchten, aber mindestens frischen Boden und volle Sonne, um ihre ganze Pracht entfalten zu können."),
           ("seasonal_foliage", "Ihre attraktiven, kastanienbraunen Fruchtstände sind ein hervorragender Gartenschmuck und eine Zierde bis in den Winter hinein.")]),
 "Fi05": _ULM[:2] + ("cultivar",) + _ULM[3:], "Fi06": _ULM,
 "Sa03": (4988, "Sanguisorba menziesii", "cultivar", "braunrot", "VI–VII", "60 cm–80 cm", "sonnig, absonnig", "Fr2-3", "Z5", "relativ geringe Gefahr", None, {"Schnittgeeignet": "ja"},
          [("pruning", "Ein beherzter Rückschnitt nach der Blüte fördert einen zweiten Flor."),
           ("soil", "Die horstige Wiesenpflanze liebt eher feuchte Böden in sonniger Lage.")]),
 "Sa05": (7886, "Sanguisorba officinalis 'Pink Tanna'", "cultivar", "rosarot", "VI–VIII", "80 cm–100 cm", S3, "Fr2-3b", "Z4", "relativ geringe Gefahr", "Coen Jansen (Niederlande)",
          {"Schnittgeeignet": "ja"}, [("propagation", "bei dieser vegetativ vermehrten Sorte einen kräftigen Rosaton zeigen")]),
 "Sa06": (7522, "Sanguisorba officinalis", "species", "braunrot", "VI–VIII", "60 cm–110 cm", S3, "Fr2-3", "Z4", "relativ geringe Gefahr", None,
          {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
          [("soil", "Diese Wiesenpflanze, die auf feuchten, gerne nährstoffreichen Standorten, aber auch Magerwiesen zu finden ist"),
           ("pollinator", "Auffälliger sind die Faltergäste: 11 Tagfalter wurden mehrfach beim Besuch beobachtet.")]),
 "Sa07": (2560, "Sanguisorba tenuifolia 'Albiflora'", "cultivar", "reinweiß", "VIII–IX", "120 cm–180 cm", S3, "Fr2-3b", "Z4", "relativ geringe Gefahr", None, {"Schnittgeeignet": "ja"},
          [("soil", "Freier Stand in der Sonne oder Halbschatten auf möglichst lehmig-humosem Boden."),
           ("native_range", "Zur Blütezeit ist diese elegante, aus Japan stammende, durchscheinend wirkende Staude ein echter Blickfang.")]),
 "Tr01": (5897, "Trollius chinensis 'Golden Queen'", "cultivar", "hellorange", "VI–VII", "60 cm–80 cm", "sonnig", "B2 Fr3 WR4", "Z5", "keine Gefahr", "Cocker and Sons (Großbritannien)",
          {"Giftklasse": "giftig +", "Schnittgeeignet": "ja"}, []),
 "Tr02": (8522, "Trollius x cultorum 'Lemon Queen'", "cultivar", "gelb", "V–VI", "60 cm–70 cm", "sonnig", "B2 Fr3 WR4", "Z5", "keine Gefahr", "van der Schoot (NL) 1918",
          {"Giftklasse": "giftig +", "Schnittgeeignet": "ja"}, [("habit", "Die eher langsam wachsende, aber dennoch wirklich ausgezeichnete 'Lemon Queen'")]),
 "Tr04": _EUR, "Tr05": _EUR,
}
