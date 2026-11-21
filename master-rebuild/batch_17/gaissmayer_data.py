# Gaißmayer（s17）: 在庫のある1品種の属20（レオントポディウムからウンキニアまで）と、在庫のない2〜3品種の属12（アムソニアからビオラまで）。batch_17/input の32属。
# 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。18個目のまとまり（batch_18）の分も同じときに続けて読んだ。
#   サイト内検索: 属名と Cotula・Bistorta・Persicaria・Ficaria・Hoodless・Lipton など58語（2つのまとまりの合計）→ 一致した商品ページ ?static 28ページ（このまとまりは18ページ・19品種）。
#   読み方: 検索も商品ページも「読む → 次へ移る」の関数を sessionStorage に入れ、Jelitto のタブと交互に、1つのサイトにつき7秒おきで開いた（1回の指示は10ステップ＝各サイト5ページ）。
#   【やってはいけないこと】最初に、開いてあるページの中から fetch で検索結果を順に読む形を試したら、2〜4ページ目で確認画面（403・Just a moment）になった。
#     タブを1ページずつ開く読み方に戻し、確認画面のタブは操作せずに置いた（おぎはら図鑑と RHS を進めている間、10分ほどで自動で通った）。そのあとは出なかった。
#   商品ページは /web/shop/a/b/384/x/<番号>/?static で開いた。本文は先頭の約600字だけを見ている。質問への回答は読んでいない。価格・在庫は写していない。
# Gaißmayer の書き方: 'Platt's Black' は Cotula squalida 'Platt's Black'（別名に Leptinella angustata 'Platt's Black'）、'Superbum' は Bistorta officinalis 'Superba'、
#   コクリュウは Ophiopogon planiscapus 'Niger'（RHS は 'Nigra'・'Nigrescens' を 'Kokuryū' のシノニムとしている。本文は「いちばん黒い宿根草」で、同じ品種として当てた）、
#   ブロンズフェンネルは Foeniculum vulgare 'Rubrum'（RHS は 'Rubrum' を 'Purpureum' のシノニムとしている）、'Twilite' は Baptisia Hybride 'Twilite Prairieblues'。
# 種のページを当てたもの: ラシラス バーナス（Lh01・Lh02）、セスレリア オータムナリス（Se01。マスターは ssp. argentea。Jelitto・RHS は argentea を別の種としているので、種の記述として当てた）。
# 掲載なし・当てていないもの: パルテニウム（'Eminence' は品種のページなので当てていない）、フィテウマ・ポア・ルエリア・スポディオポゴン・ウンキニア・フィカリア（検索で該当なし）、
#   ピンピネラ マヨール（saxifraga だけ）、ラナンキュラス（aconitifolius・acris の品種だけ）、ラチビダ ピンナータ（columnifera の品種だけ）、セセリ グミフェラム（elatum・montanum だけ）、
#   サーモプシス（lanceolata だけ）、アムソニア 'Blue Ice'、バプティシア var. minor（'Dark Blue' は品種のページなので当てていない）、デルフィニウムの3品種（Pacific の名前はなし）、
#   ヘリオプシスの2品種（'Bleeding Hearts'・'Venus' など別の品種）、リモニウム 'Blue Diamond'、フィソステギアの2品種（'Vivid'・'Bouquet Rose'・'Summer Snow' だけ）、
#   ロサの2品種、トバラの2品種（Persicaria filiformis 'Lance Corporal' は別の品種）、バーノニア（noveboracensis は 'Alba' だけ。'White Lightning' と同じか分からないので当てていない）、
#   ビオラ 'Mars'。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-20"
S3 = "sonnig, absonnig, halbschattig"
KG = "keine Gefahr"
RG = "relativ geringe Gefahr"
GF = "giftig +"
_FOE = [("lifespan", "Fenchel ist meist nur zweijährig, jedoch gut versamend."), ("soil", "Er bevorzugt humus- und nährstoffreiche Böden und sonnige Standorte."),
        ("pollinator", "Er wird von verschiedenen Wildbienen und Insektenarten angeflogen.")]
_LAT = (6312, "Lathyrus vernus", "species", "rotviolett, verfärbend nach blauviolett", "IV–V", "30 cm", "halbschattig", "G/GR2", "Z4", RG, None,
        {"Giftklasse": GF, "Wildstaude": "ja", "Schnittgeeignet": "ja"},
        [("habit", "Horstige Waldrandstaude mit Schmetterlingsblüten, die den Frühling mit einläutet."),
         ("soil", "Die Platterbse steht gerne nährstoff- und humusreich und mag neutrale bis kalkhaltige Böden."),
         ("self_seed", "Sät sich moderat aus ohne lästig zu werden.")])
GAISS = {
 "Ln01": (7437, "Leontopodium alpinum", "cultivar", "silbrig-weiß", "VI–VIII", "10 cm–15 cm", "sonnig", "St/SF/M/A2-3", "Z5", KG, None,
          {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
          [("soil", "Die silbrig-weißfilzig behaarte Gebirgspflanze mit sternförmigen Blüten benötigt durchlässige, magere, kalkhaltige und voll besonnte Standorte.")]),
 "Lp01": (8770, "Cotula squalida 'Platt's Black'", "cultivar", "grün-gelblich", "VI–VII", "5 cm", S3, "St/M/FS2-3", "Z6", KG, None,
          {"Blattfarbe": "rot", "Wintergrün": "ja"},
          [("spread_mode", "'Platt's Black' ist eine flächig wachsende kleine Pflanze mit fein gegliederten rotbraunen Fiederblättchen, die fast schwarz wirken können."),
           ("soil", "Die Staude, die auf feuchten Böden zu Hause ist, verträgt auf schattigeren Standorten auch zeitweilige Trockenheit."),
           ("habit", "Sie ist dauerhaft und konkurrenzstark gegenüber anderen flach wachsenden Stauden und kann auf kleineren Flächen als Rasenersatz dienen.")]),
 "Ms01": (10120, "Melissa officinalis", "cultivar", "weißlich-rosa", "VI–VIII", "50 cm–80 cm", S3, "Fr/GR2", "Z4", KG, None, {"Schnittgeeignet": "ja"},
          [("winter", "Melissa officinalis ist robust und starkwüchsig - allenfalls strenge Kahlfröste machen ihr zu schaffen.")]),
 "Ml01": (5350, "Milium effusum 'Aureum'", "cultivar", "grüngelb", "V–VII", "30 cm–60 cm", "absonnig, halbschattig", "G/GR2-3", "Z5", KG, None, {},
          [("seasonal_foliage", "da der Austrieb sich mit dem leuchtendsten Gelb aller Ziergräser präsentiert. Zum Sommer hin verändert sich die Farbe mehr in Richtung Gelbgrün."),
           ("soil", "Die lockerhorstige Wildart kommt auf mäßig sauren, frischen Lehmböden vor."),
           ("self_seed", "Ohne lästig zu werden versamt sich das Goldflattergras - eventuell brauchen die Sämlinge bei der Wahl des richtigen Platzes jedoch Ihre Unterstützung.")]),
 "Op01": (2044, "Ophiopogon planiscapus 'Niger'", "cultivar", "rosaweiß", "VII–VIII", "10 cm–20 cm", "halbschattig", "G/GR1-2", "Z6", KG, None,
          {"Blattfarbe": "dunkelgrün", "Wintergrün": "ja"},
          [("evergreen", "Die schmalen Blätter des Schwarzen Schlangenbarts sind immergrün und schmücken auch im Winter."),
           ("lifespan", "Die sehr langlebige Staude sieht das ganze Jahr über sehr ansprechend aus und hält es sehr lange Zeit am selben Standort aus."),
           ("spread_mode", "Auf halbschattigen bis schattigen Standorten bildet sie mit der Zeit durch kurze Ausläufer lockere Teppiche.")]),
 "Pd01": (1819, "Polygonatum odoratum", "cultivar", "weiß", "V–VI", "20 cm–40 cm", S3, "GR/G/FS1-2", "Z4", None, None,
          {"Giftklasse": GF, "Duftend": "ja", "Wildstaude": "ja", "Schnittgeeignet": "ja"},
          [("soil", "Duft-Salomonssiegel ist relativ trockenheitsverträglich und kann deshalb auf trockenen Freiflächen, an Gehölzrändern und in größeren Steingärten verwendet werden."),
           ("native_range", "In der Natur findet man Polygonatum odoratum im Süden häufig in lichten Laub- und Kiefernwäldern oder buschigen Hängen.")]),
 "Pk01": (5674, "Bistorta officinalis 'Superba'", "cultivar", "hellrosa", "VI–VII", "60 cm–80 cm", S3, "Fr3", "Z4", KG, None, {"Schnittgeeignet": "ja"},
          [("spread_mode", "Im Gegensatz zur Art wuchert sie aber nicht und remontiert gut."),
           ("soil", "Für große Uferrandbepflanzungen auf kühlen, ausreichend feuchten, lehmigen oder tonigen, meist kalkarmen Böden geeignet."),
           ("pollinator", "Honigbienen sind die häufigsten Besucher der Blüten. Sie sammeln Nektar und Pollen.")]),
 "Sk01": (6899, "Succisa pratensis", "cultivar", "blauviolett", "VII–IX", "30 cm–80 cm", "sonnig", "Fr2-3", "Z5", None, None,
          {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
          [("soil", "Der Teufelsabbiss wächst bevorzugt auf wechselfeuchten, neutralen bis mäßig sauren Lehm- oder Tonböden und ist deshalb in der Natur auf Moorwiesen, "
                    "Magerrasen, Flachmooren oder mageren Wirtschaftswiesen anzutreffen.")]),
 "Av01": (3577, "Amsonia hubrichtii", "cultivar", "hellblau", "VI–VII", "50 cm–70 cm", "sonnig", "Fr/GR1-2", "Z6", RG, None, {},
          [("seasonal_foliage", "Sie unterscheidet sich von Amsonia tabernaemontana durch ihre schmale, annähernd nadelartige Belaubung, den kompakten, zierlichen Wuchs "
                                "und eine noch leuchtendere, gelbe Herbstfärbung."),
           ("habit", "Amsonia wächst horstig, braucht zwei, drei Jahre bis zur vollen Entwicklung und liebt nicht zu trockene Standorte am sonnigen Gehölzrand und auf Freiflächen.")]),
 "Av02": (3139, "Amsonia tabernaemontana", "cultivar", "hellblau", "VI–VII", "80 cm–100 cm", "sonnig", "Fr/GR2-3", "Z6", RG, None, {"Schnittgeeignet": "ja"},
          [("seasonal_foliage", "Vom Erscheinen des lilafarbenen Austriebs im Frühjahr bis zur leuchtend gelben Herbstfärbung bietet die dicht belaubte Staude immer einen erfreulichen Anblick."),
           ("native_range", "Der an der Ostküste Nordamerikas beheimatete Blausternbusch ist eine außergewöhnlich reizvolle Pflanze")]),
 "Ba01": (10593, "Baptisia australis", "cultivar", "violettblau", "VI–VII", "80 cm–120 cm", "sonnig", "Fr/GR1-2", "Z4", None, None,
          {"Giftklasse": GF, "Schnittgeeignet": "ja"},
          [("lifespan", "Langlebige Färbepflanze mit attraktivem Laub und zierenden, lupinenartigen Schmetterlingsblüten."),
           ("habit", "Bis zur vollen Entwicklung benötigt die Pflanze mit dem buschigen Wuchs einige Jahre."),
           ("soil", "Am besten in sandigem Boden und voller Sonne, doch sonst anspruchslos.")]),
 "Ba03": (4599, "Baptisia Hybride 'Twilite Prairieblues' ®", "cultivar", "dunkelviolettpurpur mit hellgelb", "V–VII", "90 cm–120 cm", "sonnig", "Fr/GR1-2", "Z4", None, None,
          {"Giftklasse": GF, "Schnittgeeignet": "ja"},
          [("parentage", "Sie geht aus Kreuzungen der beiden Arten Baptisia australis und der gelb blühenden Baptisia sphaerocarpa hervor.")]),
 "Fo01": (3313, "Foeniculum vulgare", "cultivar", "gelb", "VII–IX", "120 cm–150 cm", "sonnig", "Fr/B2", "Z5", KG, None,
          {"Duftend": "ja", "Schnittgeeignet": "ja"}, _FOE),
 "Fo02": (10397, "Foeniculum vulgare 'Rubrum'", "cultivar", "gelb", "VII–IX", "120 cm–150 cm", "sonnig", "Fr/B2", "Z5", KG, None,
          {"Blattfarbe": "rot", "Duftend": "ja", "Schnittgeeignet": "ja"}, _FOE),
 "Lh01": _LAT, "Lh02": _LAT,
 "Lj02": (4738, "Limonium latifolium", "cultivar", "zart blauviolett", "VII–VIII", "60 cm–80 cm", "sonnig", "Fr/FS/St1", "Z5", KG, None, {"Schnittgeeignet": "ja"},
          [("soil", "Wichtig ist ein durchlässiger, sandig-lehmiger, kalkhaltiger, relativ nährstoffreicher Boden in vollsonniger Lage."),
           ("cut_flower", "Sie eignet sich hervorragend als Schnittblume und für Trockensträuße.")]),
 "Vo01": (5103, "Viola labradorica", "cultivar", "blauviolett", "IV–V", "10 cm", S3, "GR2", "Z5", None, None, {"Blattfarbe": "rot"},
          [("spread_mode", "Durch reiche Selbstaussaat sowie kurze Ausläufer bildet die Art einen lockeren, schönen Teppich."),
           ("soil", "Von vollsonnig und trocken - hier ist die Blattausfärbung besonders intensiv - bis halb- oder vollschattig, mit oder ohne Wurzeldruck nahezu alles wird vertragen.")]),
}
