# Gaißmayer（s17）: ガウラ・ジプソフィラ・アシリウム・コルヌス・フェスツーカ・ハコネクロア・パパベル・アンジェリカ・エノテラ・バーバスカム・バーベナ・アンスリスクス・アルテミシア・カラミンサ。
# 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/gaissmayer_data.py と同じ
#   （サイト内検索: Gaura・Gypsophila・Athyrium・Festuca・Hakonechloa・Papaver・Angelica・Oenothera・Verbascum・Verbena・Anthriscus・Artemisia・Calamintha・Clinopodium・Cornus
#     → 一致した商品ページ ?static 21ページ）。6秒おき。最初の検索で確認画面が出たが、操作せずに置き、1〜2分で自動で通った。そのあとは出なかった。
# 本文は先頭の約400字だけを見ている。質問への回答は読んでいない。価格・在庫は写していない。
# Gaißmayer の書き方: 'Snowflake' は Gypsophila paniculata 'Schneeflocke'（種子で殖やす品種で、八重が大部分だが一重も出る、と書いている）、
#   'Elijah Blue' は Festuca Cinerea-Hybride 'Elijah Blue'、エノテラ マクロカルパは Oenothera missouriensis、ニシキシダは Athyrium niponicum 'Metallicum'。
# 種のページを当てたもの: ガウラ（Ga02〜Ga06）、ジプソフィラ パニキュラータ（Gy03）・レペンス（Gy06。種のページは白花）、西洋メシダ（At01）、
#   フウチソウ（Hk02・Hk03。Hk01 は種そのものを売っている商品）、エノテラ マクロカルパ（Oe02）、バーバスカム フェニセウム（Vb03）、アルテミシア ブルガリス（Am02）。
# 掲載なし・当てていないもの: ジプソフィラ セラスティオイデス、ニシキシダのほかの品種（'Metallicum' は品種のページなので広げていない）、フェスツーカ ガウティエリ（'Pic Carlit' だけ）・
#   'Boulder Blue'・アイダホエンシス、オリエンタルポピー（掲載なし）、アンジェリカ パキカルパ・'Ebony'、エノテラ スペシオーサ（'Alba'・'Siskiyou' だけ）、
#   バーバスカム シャイクシ、バーベナ ハスタータの種そのもの（'Blue Spires' など品種だけ）、アンスリスクス 'Golden Fleece'、カラミンサ グランディフローラ、コルヌス（検索で該当なし）。
# 試行ID: (商品ページの番号, 表記, level, 花色, 花期, 高さ, 日照, Lebensbereich, ゾーン, ナメクジ, 育種者, 表のその他, 本文から拾った文 [(field, 原文)])
CHECKED = "2026-11-20"
S3 = "sonnig, absonnig, halbschattig"
KG = "keine Gefahr"
RG = "relativ geringe Gefahr"
FP = "Frühjahrspflanzung empfohlen"
_GAU = (8044, "Gaura lindheimeri", "species", "weiß", "VII–X", "60 cm–100 cm", "sonnig", "Fr/B1", "Z7", KG, None, {"Pflanz-Zeitpunkt": FP, "Schnittgeeignet": "ja"},
        [("soil", "Sie eignet sich als unermüdlicher Dauerblüher für warme, vollsonnige, trockene Gartenplätze mit durchlässigem, sandigem oder schotterigem, nicht zu nährstoffreichen Boden"),
         ("habit", "Die anmutige Pflanze mit buschig-aufrechtem Wuchs schmückt sich mit elegant überhängenden lockeren Blütentrauben.")])
_HAK = (5060, "Hakonechloa macra", "species", "grünlich", "VII–VIII", "40 cm–60 cm", "absonnig, halbschattig", "GR/Fr/St2-3", "Z7", KG, None,
        {"Pflanz-Zeitpunkt": FP, "Schnittgeeignet": "ja"},
        [("native_range", "Die reine Art des Japan-Bandgrases wächst auf feuchten Felsen am Mount Hakone auf der japanischen Hauptinsel Honshu."),
         ("seasonal_foliage", "Das schmal lanzettliche Laub zeigt im Herbst eine sanfte Gelb-Färbung, die zum Winter hin einen bronzefarbenen Ton annimmt."),
         ("soil", "Auf sehr frischem Boden ist auch ein sonniger Standort möglich.")])
_MIS = (8370, "Oenothera missouriensis", "species", "zitronengelb", "VI–IX", "20 cm–25 cm", "sonnig", "St/FS/MK1", "Z5", KG, None, {},
        [("habit", "Steingartenart mit niederliegenden Trieben. Reich und lange blühende Staude, die auch für Böschungen, Trockenmauern und Tröge geeignet ist."),
         ("soil", "Warm, durchlässig, mäßig nährstoffreich.")])
GAISS = {
 "Ga01": (9272, "Gaura lindheimeri 'Summer Breeze'", "cultivar", "weiß mit rosa", "VII–X", "80 cm–120 cm", "sonnig", "Fr/B1", "Z7", KG, None,
          {"Pflanz-Zeitpunkt": FP, "Schnittgeeignet": "ja"},
          [("habit", "Blütenreichtum und wunderschöne, weißen Blüten zeichnen diese Prachtkerze aus. Hinzu kommen Robustheit und Standfestigkeit."),
           ("soil", "Prachtkerzen sind unermüdliche Dauerblüher für vollsonnigen, warmen und trockenen Standort auf durchlässigem, sandigem oder schotterigem, nicht zu nährstoffreichem Boden."),
           ("winter", "Schutz vor Winternässe empfohlen, nicht zuverlässig winterhart.")]),
 "Ga02": _GAU, "Ga03": _GAU, "Ga04": _GAU, "Ga05": _GAU, "Ga06": _GAU,
 "Gy02": (4488, "Gypsophila paniculata 'Bristol Fairy'", "cultivar", "reinweiß, gefüllt", "VII–IX", "100 cm", "sonnig", "B/Fr2", "Z4", None, "Bristol Nurseries (USA) 1928",
          {"Schnittgeeignet": "ja"}, [("habit", "Dicht gefüllte, reinweiße Einzelblütchen vereinen sich zu abertausenden in großen schleierförmigen Wolken.")]),
 "Gy03": (10231, "Gypsophila paniculata", "species", "weiß, einfach", "VII–VIII", "80 cm–100 cm", "sonnig", "Fr2 St/FS1b", "Z4", None, None, {"Schnittgeeignet": "ja"},
          [("native_range", "Das Hohe Schleierkraut stammt aus dem südlichen Mitteleuropa, wo es auf trockenen, steinigen und sandigen Lebensräumen anzutreffen ist.")]),
 "Gy04": (10079, "Gypsophila paniculata 'Schneeflocke'", "cultivar", "weiß, großteils gefüllt", "VII–IX", "70 cm–100 cm", "sonnig", "B/Fr2", "Z4", None, None,
          {"Schnittgeeignet": "ja"},
          [("habit", "Gypsophila paniculata 'Schneeflocke' bildet mit der Zeit reichverzweigte, blütenübersäte Büsche von kugeligem Wuchs."),
           ("propagation", "Diese weiß blühende Sorte wird generativ, also über Aussaat vermehrt, weshalb sie in Ihrem Aussehen etwas variieren kann.")]),
 "Gy05": (9633, "Gypsophila repens 'Rosea'", "cultivar", "zartrosa", "V–VII", "10 cm", "sonnig", "St/FS/MK/FS1-2", "Z4", None, "Sündermann (DE) 1890", {},
          [("propagation", "Gypsophila repens 'Rosea' ist eine generativ vermehrte Sorte, deren Blütenfarbe etwas variieren kann."),
           ("habit", "Die robuste, gesunde Sorte entwickelt sich am passenden Standort prächtig und bildet so rasch üppige Polster.")]),
 "Gy06": (2842, "Gypsophila repens", "species", "weiß", "V–VII", "10 cm", "sonnig", "St/FS/MK/FS1-2", "Z4", None, None, {"Wildstaude": "ja", "Blattfarbe": "silber"},
          [("native_range", "Das Polster-Schleierkraut ist auch in unseren Gebirgen anzutreffen. Man findet es vor allem auf alpinen Magerrasen und Schotterfluren."),
           ("heat_humidity", "Deshalb bevorzugt es im Garten auch eher kühle und frische, dennoch aber durchlässige Böden in vollsonniger Lage.")]),
 "At01": (6807, "Athyrium filix-femina", "species", None, None, "80 cm–120 cm", "absonnig, halbschattig, schattig", "G/GR2", "Z2", KG, None, {"Wildstaude": "ja", "Blattfarbe": "hellgrün"},
          [("habit", "Horstig bis lockerhorstiger, rosettenartiger Wuchs. Mit den Jahren bildet er eine breite mehrköpfige Pflanze."),
           ("self_seed", "Der Wald-Frauenfarn vermehrt sich über Sporen und kann an passenden Standorten verwildern, ohne lästig zu werden.")]),
 "At03": (9405, "Athyrium niponicum 'Metallicum'", "cultivar", None, None, "20 cm–40 cm", "absonnig, halbschattig, schattig", "G/GR2", "Z6", KG, None,
          {"Blattfarbe": "silber, panachiert"},
          [("habit", "Sein Farbenspiel von bräunlichgrün über silbrig bis rötlich macht ihn einfach unentbehrlich für den Schattengarten.")]),
 "Fe03": (5665, "Festuca Cinerea-Hybride 'Elijah Blue'", "cultivar", "gelblich-braun", "VI–VII", "15 cm–25 cm", "sonnig", "St/FS/SH1", "Z4", KG, "Lois Woodhill (US) 1990",
          {"Wintergrün": "ja", "Blattfarbe": "blau"},
          [("habit", "Die Sorte ist zudem gut dauerhaft und wüchsig und generell eher langlebiger als andere Sorten."),
           ("heat_humidity", "Je trockener und heißer der Standort, desto intensiver die Färbung.")]),
 "Hk01": _HAK[:2] + ("cultivar",) + _HAK[3:], "Hk02": _HAK, "Hk03": _HAK,
 "Hk04": (2147, "Hakonechloa macra 'Aureola'", "cultivar", "grünlich", "VII–VIII", "20 cm–40 cm", "absonnig, halbschattig", "GR/Fr/St2-3b", "Z7", KG, None,
          {"Pflanz-Zeitpunkt": FP, "Schnittgeeignet": "ja", "Blattfarbe": "gelb, panachiert"},
          [("seasonal_foliage", "Goldbunt gestreifte Blattschöpfe leuchten uns fröhlich entgegen. Austrieb und Herbstfärbung sind rötlich getönt."),
           ("habit", "Ein edles Farbspiel, das vom sanft überhängenden Wuchs unterstrichen wird. Für wirkungsvolle Akzente im lichten Schattenbereich.")]),
 "Ag03": (10806, "Angelica sylvestris 'Vicar's Mead'", "cultivar", "hellrosa", "VII–IX", "90 cm–120 cm", S3, "Fr/GR2-3", "Z7", None, None,
          {"Giftklasse": "giftig +", "Blattfarbe": "rot"},
          [("lifespan", "Die kurzlebige, in der Regel zweijährige Pflanze liebt frische bis feuchte Böden in vollsonniger bis halbschattiger Lage."),
           ("soil", "Die kurzlebige, in der Regel zweijährige Pflanze liebt frische bis feuchte Böden in vollsonniger bis halbschattiger Lage.")]),
 "Oe01": _MIS[:2] + ("cultivar",) + _MIS[3:], "Oe02": _MIS,
 "Vb03": (8217, "Verbascum phoeniceum", "species", "violett, rot, rosa, weiß", "V–VI", "60 cm–90 cm", "sonnig", "St/FS/Fr1", "Z6", KG, None, {"Wildstaude": "ja", "Wintergrün": "ja"},
          [("lifespan", "Die Art eignet sich gut für naturnahe Pflanzungen, ist an zusagenden Standorten meist gut dauerhaft."),
           ("self_seed", "Verbascum phoeniceum sät sich aus. Die Sämlinge können in der Blütenfarbe zwischen violett, rot, rosa und weiß variieren.")]),
 "Vn01": (6720, "Verbena bonariensis", "cultivar", "blauviolett", "VII–X", "100 cm–150 cm", "sonnig", "Fr1", "Z8", KG, None, {"Pflanz-Zeitpunkt": FP, "Schnittgeeignet": "ja"},
          [("lifespan", "Als standfeste, lockerwüchsige Vertikale mit Durchblickmöglichkeit und sehr langer Blütezeit ist die eher kurzlebige Pflanze im sommerlichen und herbstlichen Garten eine wirkliche Bereicherung.")]),
 "Vn03": (7658, "Verbena hastata 'Blue Spires'", "cultivar", "rötlich-lila", "VI–VIII", "80 cm–120 cm", "sonnig", "Fr2-3 WR4", "Z4", KG, None,
          {"Pflanz-Zeitpunkt": FP, "Schnittgeeignet": "ja"},
          [("soil", "Sie bevorzugt gleichmäßig frische bis feuchte Gartenböden in vollsonniger Lage."),
           ("native_range", "'Blue Spires' ist eine einheitlich blauviolett blühende Selektion der nordamerikanischen Wildstaude.")]),
 "Ah02": (9447, "Anthriscus sylvestris 'Ravenswing'", "cultivar", "weiß", "IV–VI", "60 cm–120 cm", "sonnig", "Fr/GR1-2", "Z5", KG, None, {"Schnittgeeignet": "ja", "Blattfarbe": "rot"},
          [("self_seed", "Dieser Doldenblütlers ist meist zweijährig und sät sich reichlich an freien Stellen aus"),
           ("lifespan", "Dieser Doldenblütlers ist meist zweijährig und sät sich reichlich an freien Stellen aus")]),
 "Am01": (8083, "Artemisia schmidtiana 'Nana'", "cultivar", "hellgelb", "VI–VII", "20 cm–25 cm", "sonnig", "St/M/FS1-2", "Z4", KG, None, {"Blattfarbe": "silber"},
          [("habit", "Sehr hübsche, polsterbildende Steingartenstaude mit filigranen silbergrauen Blättern und dichter, silbriger Behaarung."),
           ("winter", "Schutz vor Winternässe ist empfehlenswert. Nährstoffarme Standorte.")]),
 "Am02": (2339, "Artemisia vulgaris", "species", "gelblich", "VII–VIII", "60 cm–120 cm", "sonnig", "Fr1", "Z3", RG, None, {"Wildstaude": "ja"}, []),
 "Ca02": (5320, "Calamintha nepeta 'Blue Cloud'", "cultivar", "blauviolett", "VI–VIII + IX", "40 cm–60 cm", S3, "Fr/FS/St1", "Z6", KG, "Kramer (NL)",
          {"Duftend": "ja", "Schnittgeeignet": "ja"},
          [("habit", "Wüchsige, kompakt-aufrechte, reichblühende Sorte des Steinquendels mit langer Blütezeit und herbem, minzig-aromatischem Duft."),
           ("pollinator", "Die thymian-ähnlichen Blüten sind bei Bienen und anderen Insekten sehr beliebt")]),
}
