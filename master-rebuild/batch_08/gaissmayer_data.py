# Gaißmayer（s17）: タリクトラム・コレオプシス・リアトリス・リシマキア・ベロニカストラム・エリンジウム・ミスカンサス・モリニア。
# 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/gaissmayer_data.py と同じ（サイト内検索8回 → 一致した商品ページ ?static 26ページ）。6秒おき。
#   パソコンの再起動のあと、最初の検索で確認画面が出た（気づかずに4回続けて開いてしまった）。操作せずに Jelitto を先に読んでいる間に自動で通った。
# 今回は1ページ1回の読み取りにしたので、本文は先頭の約560字だけを見ている（長い本文の後半は読んでいない）。質問への回答は読んでいない。価格・在庫は写していない。
# Gaißmayer の書き方: 'Black Stockings'・'Elin'・'Adoration'・'Fascination'・'Lavendelturm' は「Hybride」、'Moonbeam' は Coreopsis Verticillata-Hybride、
#   Li03 は Liatris scariosa var. alba 'Alba'、Li06 は 'Floristan Weiß'、モリニアは亜種を書かない。Th03 のページのアドレスは thalictrum-delavayi-dipterocarpum-hort。
# 種のページを当てたもの: スピカータ（Li05・Li07）、プンクタータ（Ly06）、プラナム（Er02・Er03・Er04）。
# 使っていないもの: Eryngium planum 'Blauer Zwerg'（'Blue Hobbit' と同じ品種か分からない。RHS は別のページ）・'Blaukappe'、Veronicastrum sibiricum の品種（'Amethyst'・'Red Arrows'）。
# 掲載なし: アキレジフォリウム（'Purpureum'・'Thundercloud'）、コレオプシスの交配品種・'American Dream'、ピクノスタキア・'Floristan Violett'・'Kobold'、
#   コンジェスティフロラ・クサレダマ、シビリクムの種そのもの・白花、'Blue Glitter' などプラナムの品種・バリフォリウム、ススキの種そのもの・'Cosmopolitan'・'Little Zebra'・'Purpurascens'、
#   'Heidebraut'・'Transparent'・'Moorflamme'。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-20"
S3 = "sonnig, absonnig, halbschattig"
KG = "keine Gefahr"
_SPI = (7995, "Liatris spicata", "species", "lila", "VII–IX", "30 cm–80 cm", "sonnig", "B/Fr2", "Z4", KG, None, {"Schnittgeeignet": "ja"},
        [("soil", "Der Boden sollte ausreichend mit Wasser versorgt sein, wobei aber die Knollen der Pflanzen (vor allem im Winter) keine Staunässe vertragen."),
         ("soil", "eignet sich am besten für einen sonnigen, nährstoffreichen, durchlässigen, locker-humosen Standort")])
_PUN = (2961, "Lysimachia punctata", "species", "gelb", "VI–VIII", "60 cm–80 cm", S3, "GR/Fr2-3", "Z5", KG, None, {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
        [("spread_mode", "Die Ausläufer treibende, wuchernde Staude stammt ursprünglich aus der Türkei und dem südlichen Europa, kommt aber auch bei uns vielfach verwildert vor."),
         ("sun", "Sie verträgt relativ viel Schatten und z. T. Wurzeldruck von Gehölzen.")])
_PLA = (7767, "Eryngium planum", "species", "blau", "VII–VIII", "40 cm–100 cm", "sonnig", "St/FS/Fr1-2", "Z4", KG, None, {"Wildstaude": "ja", "Schnittgeeignet": "ja"},
        [("soil", "Dort wächst es auf trockenen, eher mageren, warmen, sonnigen Standorten und sollte auch im Garten so verwendet werden"),
         ("propagation", "Da die reine Art über Aussaat vermehrt wird, fallen ihre Nachkommen sowohl in ihrer Wuchshöhe als auch in ihrer Blütenfärbung etwas variabel aus.")])


def _own(rec):
    return rec[:2] + ("cultivar",) + rec[3:]


GAISS = {
 "Th03": (3228, "Thalictrum delavayi", "cultivar", "violettrosa", "VII–VIII", "120 cm–180 cm", S3, "GR/G2", "Z5", None, None, {"Schnittgeeignet": "ja"},
          [("habit", "Am besten wird sie zwischen niedrige, sparrig wachsende Sträucher gepflanzt, die ihr Halt geben."),
           ("soil", "Nur auf feuchten, sehr hellen Standorten ist Thalictrum delavayi wirklich standfest.")]),
 "Th04": (9914, "Thalictrum delavayi 'Album'", "cultivar", "reinweiß", "VII–X", "80 cm–120 cm", S3, "GR/G2", "Z5", None, None, {"Duftend": "ja", "Schnittgeeignet": "ja"},
          [("soil", "Sie liebt frische bis feuchte, humose Gartenböden in halbschattiger Lage."), ("seasonal_foliage", "Ein ganz besonderer Blickfang ist der helle, lindgrüne Laubaustrieb.")]),
 "Th05": (9386, "Thalictrum flavum ssp. glaucum", "cultivar", "schwefelgelb", "VII–VIII", "120 cm–150 cm", S3, "Fr/GR2-3", "Z5", None, None,
          {"Blattfarbe": "silber, blau", "Schnittgeeignet": "ja"},
          [("habit", "Die straff aufrecht wachsende und gut standfeste Gelbe Wiesenraute"),
           ("soil", "Die anspruchslose Staude eignet sich für die Uferbepflanzung von Teichen und Bächen, für Feuchtwiesen aber auch für nicht zu trockene Standorte am Gehölzrand.")]),
 "Th06": (8798, "Thalictrum Hybride 'Black Stockings'", "cultivar", "purpurrosa", "VI–VII", "120 cm–180 cm", S3, "Fr/GR2-3", "Z5", None, None, {"Schnittgeeignet": "ja"},
          [("sun", "Am schönsten entwickelt sie sich an einem halbschattigen Standort mit gutem, frischem bis feuchtem Gartenboden. Bei ausreichender Bodenfeuchte sind auch sonnige Plätze möglich.")]),
 "Th07": (3149, "Thalictrum Hybride 'Elin'", "cultivar", "hell-lila", "VI–VIII", "150 cm–250 cm", S3, "Fr/GR2-3", "Z4", None, "Bengtsson (Schweden)",
          {"Blattfarbe": "silber, blau", "Schnittgeeignet": "ja"},
          [("parentage", "Diese Kreuzung von Thalictrum rochebrunianum x Thalictrum flavum"), ("habit", "Trotz seiner Höhe ist 'Elin' gut standfest.")]),
 "Th08": (2488, "Thalictrum rochebruneanum", "cultivar", "lilapurpur, gelbliche Staubgefäße", "VII–VIII", "150 cm–200 cm", S3, "Fr/GR2-3", "Z5", None, None, {"Schnittgeeignet": "ja"},
          [("habit", "Die Solitärstaude wächst straff aufrecht und hat bis zum Herbst eine ansehnliche Wirkung.")]),
 "Co06": (7686, "Coreopsis verticillata 'Zagreb'", "cultivar", "goldgelb", "VI–IX", "30 cm", "sonnig", "B/Fr2", "Z6", KG, "Polak (YU) 1960", {"Schnittgeeignet": "ja"},
          [("seasonal_foliage", "Das feine nadelartige Laub ist vor, während und sogar noch nach der Blüte (dann oft mit gelber Herbstfärbung) eine zusätzliche Bereicherung.")]),
 "Co05": (4014, "Coreopsis Verticillata-Hybride 'Moonbeam'", "cultivar", "schwefelgelb", "VI–IX", "40 cm", "sonnig", "B/Fr2", "Z6", KG, "Kurt Bluemel (US)", {"Schnittgeeignet": "ja"},
          [("parentage", "Diese ganz besondere Sorte entstand vermutlich durch das Einkreuzen von Coreopsis rosea."),
           ("spread_mode", "Darauf lässt sich auch die Bildung etwas längerer Ausläufer zurückführen, die jedoch nie lästig werden.")]),
 "Li02": (12871, "Liatris scariosa", "cultivar", "lila-rosa", "VII–X", "60 cm–70 cm", "sonnig", "B/Fr1-2", "Z4", KG, None, {"Schnittgeeignet": "ja"},
          [("seasonal_foliage", "Im winterlichen Garten sind die Samenstände außerordentlich attraktiv und bleibendes Strukturelement bis zum Rückschnitt im Frühjahr.")]),
 "Li03": (12327, "Liatris scariosa var. alba 'Alba'", "cultivar", "weiß", "VII–X", "60 cm–70 cm", "sonnig", "B/Fr1-2", "Z4", KG, None, {"Schnittgeeignet": "ja"},
          [("soil", "Liatris scariosa var. alba erweitert unser Prachtschartensortiment auf trockenerem Standort.")]),
 "Li04": _own(_SPI), "Li05": _SPI, "Li07": _SPI,
 "Li06": (1946, "Liatris spicata 'Floristan Weiß'", "cultivar", "weiß", "VII–IX", "30 cm–80 cm", "sonnig", "B/Fr2", "Z4", KG, "Benary (Deutschland) 1975", {"Schnittgeeignet": "ja"},
          [("soil", "Sie eignet sich am besten für sonnige, nährstoffreiche, locker-humose Standorte wobei der Boden ausreichend mit Wasser versorgt sein sollte. Staunässe wird aber nicht vertragen.")]),
 "Ly03": (7014, "Lysimachia nummularia", "cultivar", "gelb", "VI–VII", "10 cm", S3, "GR/Fr2-3 WR4", "Z4", KG, None, {"Duftend": "ja", "Wildstaude": "ja"},
          [("spread_mode", "Mit eng dem Boden anliegenden, wurzelnden Trieben."), ("soil", "Hübscher, robuster Bodendecker für den Teichrand und andere feuchte Plätze, auch für schattige Lagen.")]),
 "Ly04": (9541, "Lysimachia nummularia 'Aurea'", "cultivar", "gelb", "VI–VII", "5 cm–10 cm", "absonnig, halbschattig", "GR/Fr2-3 WR4", "Z4", KG, None, {"Blattfarbe": "gelb", "Duftend": "ja"},
          [("habit", "Etwas schwachwüchsiger als die Art."), ("sun", "Das gelbe Laub verträgt keine pralle Sonne.")]),
 "Ly05": _own(_PUN), "Ly06": _PUN,
 "Vs03": (5584, "Veronicastrum Hybride 'Adoration'", "cultivar", "rosaviolett", "VI–VIII", "140 cm–150 cm", S3, "Fr/GR2-3b", "Z3", KG, "Piet Oudolf (NL)", {"Schnittgeeignet": "ja"},
          [("habit", "die sich besonders wohlproportioniert, standfest und straff aufrecht wachsend präsentiert"),
           ("award", "'Adoration' wurde in der Staudensichtung mit der höchsten Bewertung *** (ausgezeichnet) bedacht")]),
 "Vs05": (4009, "Veronicastrum Hybride 'Fascination'", "cultivar", "purpurviolett", "VI–VIII", "160 cm–180 cm", S3, "Fr/GR2-3b", "Z3", KG, "ter Linden (NL)", {"Schnittgeeignet": "ja"},
          [("habit", "Hoch wachsende Sorte mit teils leicht überhängenden, rotvioletten Blütenständen, deren Spitzen oft verbändert sind")]),
 "Vs06": (1508, "Veronicastrum Hybride 'Lavendelturm'", "cultivar", "hellviolettblau", "VI–VIII", "150 cm–190 cm", S3, "Fr/GR2-3b", "Z3", KG, "Ernst Pagels (DE) 1998", {"Schnittgeeignet": "ja"}, []),
 "Vs04": (5238, "Veronicastrum virginicum 'Erika'", "cultivar", "hellrosa", "VI–VIII", "100 cm–120 cm", S3, "Fr/GR2-3b", "Z3", KG, "Fuß (DE) 1990", {"Schnittgeeignet": "ja"},
          [("habit", "Die Sorte ist wohlproportioniert, sehr reichblütig, sehr gut standfest und sehr gesund."), ("award", "Sie wurde in der Sichtung 2013 mit \"sehr gut\" bewertet!")]),
 "Er01": _own(_PLA), "Er02": _PLA, "Er03": _PLA, "Er04": _PLA,
 "Er06": (8414, "Eryngium yuccifolium", "cultivar", "grünlich-weiß", "VII–IX", "50 cm–120 cm", "sonnig", "Fr/FS2-3", "Z7", KG, None,
          {"Blattfarbe": "silber", "Schnittgeeignet": "ja", "Wintergrün": "ja"},
          [("soil", "Schön mit anderen Präriepflanzen auf nicht zu trockenen Standorten."),
           ("habit", "Am Wildstandort wird sie sehr hoch, bis 180 cm, bei uns bleibt sie jedoch deutlich niedriger.")]),
 "Mi06": (6717, "Miscanthus sinensis 'Gracillimus'", "cultivar", "silbrig, blüht selten", "X–XI", "140 cm–160 cm", "sonnig", "Fr/B2", "Z6", KG, "1878", {"Schnittgeeignet": "ja"},
          [("habit", "Bei uns kommt sie nur selten, nach warmen Sommern zur Blüte."),
           ("seasonal_foliage", "die feinen, elegant überhängenden Blätter, die sich im Herbst bronzefarben verfärben")]),
 "Mi04": (3985, "Miscanthus sinensis 'Morning Light'", "cultivar", "silbrig", "IX–X", "120 cm–150 cm", "sonnig", "Fr/B2", "Z6", KG, None, {"Schnittgeeignet": "ja"},
          [("habit", "wächst bei uns eher langsam, blüht kaum und erinnert mit den schmalen, weißgerandeten Blättern an einen 'Gracillimus Variegatus'")]),
 "Mo01": (7441, "Molinia caerulea 'Dauerstrahl'", "cultivar", "bräunlich", "VIII–X", "40 cm–80 cm", S3, "H/Fr/GR2-3", "Z4", KG, "Heinz Klose (DE) 1982", {"Schnittgeeignet": "ja"},
          [("seasonal_foliage", "Im Herbst erstrahlen diese in leuchtendem Gelb und sind bis weit in den Winter hinein äußerst ansprechend.")]),
 "Mo05": (7054, "Molinia caerulea 'Moorhexe'", "cultivar", "schwarz-braun", "VIII–X", "40 cm–60 cm", S3, "H/Fr/GR2-3", "Z4", KG, "Heinz Hagemann (DE)",
          {"Blattfarbe": "gelb, rot", "Schnittgeeignet": "ja"},
          [("seasonal_foliage", "Goldgelbe Herbstfärbung."), ("habit", "Eine kompakte, straff aufrecht wachsende Selektion von Heinz Hagemann.")]),
 "Mo06": (8375, "Molinia caerulea 'Variegata'", "cultivar", "schwarz-braun", "VIII–X", "40 cm–70 cm", "absonnig, halbschattig", "H/Fr/GR2-3", "Z5", KG, None,
          {"Blattfarbe": "panachiert", "Schnittgeeignet": "ja"},
          [("habit", "Mit seinen überhängenden Blütenrispen und der eher rundlichen Wuchsform bleibt 'Variegata' bis in den Spätherbst hinein sehr attraktiv und dekorativ.")]),
}
