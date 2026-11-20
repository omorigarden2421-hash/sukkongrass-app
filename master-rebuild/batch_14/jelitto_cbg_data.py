# Jelitto（s11）とシカゴ植物園（s08）: チャスマンティウム・ケロネ・エキノプス・エリムス・エリゲロン・ガリウム・グレコマ・カリメリス・ラベンダー・レウカンセマム・リスラム・パキサンドラ・フロミス・
#   サギナ・サポナリア・センペルビブム・シルフィウム・スティパ・シンフィオトリクム・ビバーナム・ユッカ・ヒューケレラ・トリフォリウム。
# Jelitto は 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_11/jelitto_cbg_data.py と同じ
#   （英語のサイト内検索: Chasmanthium 3件・Chelone 8件・Echinops 7件・Erigeron 12件・Elymus 4件・Glechoma 2件・Galium 6件・Kalimeris 1件・Lavandula angustifolia 18件・Leucanthemum 12件・
#     Lythrum 5件・Pachysandra 0件・Phlomis 6件・Sagina 1件・Silphium 6件・Sempervivum 6件・Saponaria 8件・Stipa 13件・Trifolium 6件・Aster ericoides 1件・Yucca 4件・Heucherella 0件）。
#   一致は31ページ。7秒おき、1回の指示は6ページまで。最初の1ページで確認画面が出たが、操作せずに置き、3分ほどで自動で通った。
# Jelitto の書き方（角かっこは流通名・別名）: ワイルドオーツは CHASMANTHIUM latifolium (UNIOLA) [Green Dangles]、'Pink Jewel' は ERIGERON speciosus 'Rosa Juwel' [Pink Jewel]、
#   'Profusion' は ERIGERON karvinskianus 'Blütenmeer' [Profusion, Stallone]、'Bronze Flamingo' は PHLOMIS tuberosa (PHLOMOIDES) [Bronze Flamingo]（種のページに流通名を併記）、
#   エゾミソハギは LYTHRUM salicaria [Rosy Gem, Red Beauties]、サギナは SAGINA subulata hort. [Crispy, Puzta]、スティパ テヌイッシマは STIPA tenuissima (NASSELLA) [Pony Tails, Angel Hair]、
#   スティパ イチュは STIPA ichu (NASSELLA, JARAVA)、トリフォリウム ルーベンスは TRIFOLIUM rubens [Red Feathers]、'Snowdrift' は LEUCANTHEMUM x superbum fl. pl. 'Snowdrift' (CHRYSANTHEMUM maximum)、
#   ケロネの白花は CHELONE obliqua var. alba、エリムス マジェラニカスは ELYMUS magellanicus (AGROPYRON)、アスター エリコイデスは ASTER ericoides (SYMPHYOTRICHUM)。
# Jelitto が発表した品種（Historical の欄。育種会社 s12 と同じ扱いにできる）: エキノプス 'Star Frost'（2008）、シャスターデージー 'Snowdrift'（1996）、トリフォリウム 'Frosty Feathers'（2016）。
# 種のページを当てたもの: グレコマ（Gc02）、カリメリス インシサ（Ka02）、ラベンダー（La01・La02。'Hidcote Blue-Strain'・'Munstead-Strain' は種子の系統なので当てていない）、
#   エゾミソハギ（Lt02）、サギナ（Sg02）、センペルビブムの交配種の混合（Sm01・Sm02）、サポナリア オフィシナリス（Sn01・Sn02）、アスター エリコイデス（Sy01）、ユッカ フィラメントサ（Yu01）。
#   当てていないもの: パキサンドラ・ヒューケレラ・ビバーナム（掲載なし）、'Broadway Lights'、'Happy Snow'（'Happy Lights' は別の品種）、トリフォリウム レペンス、ノビベルギ 'Jenny'、ユッカ グロリオーサ。
# 日照の欄（Location）は記号で読めなかった。
# Jelitto の「Full sun in cool summer climates to semi-shade elsewhere」（ケロネ オブリクア）、土の欄の「cool」（エリムス マジェラニカス）、「Heat tolerant」（ユッカ フィラメントサ）は
#   暑さに関わる記述だが、Jelitto は耐暑性の判定に使わない（記録だけ）。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-20"
_GLE = ("GLECHOMA hederacea", None, "violet", "April - May", "Z2 - Z10", "stoloniferous", "20 cm", "average / humus rich, fertile", "",
        "Reblooming September-October. medicinal plant / tea herb / groundcover; honey-bee food plant", None)
_KAL = ("KALIMERIS incisa (ASTER)", None, "pale purple", "July - September", "Z4 - Z8", "erect", "60 cm", "average", "",
        "Pale purple ray florets, stable. honey-bee food plant / for the rock garden / suitable for cutting", None)
_LYT = ("LYTHRUM salicaria [Rosy Gem, Red Beauties]", None, "carmine-pink", "June - September", "Z3 - Z9", "", "120 cm", "moist / average", "",
        "medicinal plant; honey-bee food plant / suitable for cutting", None)
_SAG = ("SAGINA subulata hort. [Crispy, Puzta]", None, "white", "June - August", "Z4 - Z9", "mat-forming", "5 cm", "average", "", "for the rock garden", None)
JELITTO = [
 (["Ch01"], "CHASMANTHIUM latifolium (UNIOLA) [Green Dangles]", "cultivar", "Eastern United States westwards to Eastern Kansas: woody slopes, moist thickets.",
  "pale green at first, turning golden brown", "August - October", "Z4 - Z10", "erect", "80 cm", "moist / well-drained / average", "",
  "One of the most adaptable of the North American grasses. Flat panicles of pendulous flowers, pale green at first, turning golden brown. decorative fruit; suitable for cutting",
  "アメリカ東部からカンザス州東部の林の斜面・湿ったやぶ"),
 (["Ch02"], "CHASMANTHIUM latifolium 'Little Tickler'", "cultivar", None, "", "August - October", "Z5 - Z10", "clumping / compact / low-growing", "50 cm", "moist / well-drained / average", "",
  "Large arching spikes, stable, a selection from Ivy Farms. Foliage: narrower than the species. for the rock garden / suitable for cutting", None),
 (["Cl01"], "CHELONE obliqua", "cultivar", "USA: Tennessee and Maryland south to Florida", "dark pink", "August - October", "Z5 - Z8", "stoloniferous / erect", "80 cm",
  "moist / along streamsides", "",
  "Plant forms a dense, bushy mass and has very interesting turtle head-shaped lilac-pink blossoms. Plant along stream banks, the edge of woods or in the perennial garden. "
  "Full sun in cool summer climates to semi-shade elsewhere. Perennial Plant of the Year 2004 in Sweden. groundcover", "アメリカ（テネシー州・メリーランド州からフロリダ州）"),
 (["Cl02"], "CHELONE obliqua var. alba", "cultivar", "USA", "white", "August - October", "Z5 - Z8", "stoloniferous", "80 cm", "moist / along streamsides", "",
  "groundcover; suitable for cutting", "アメリカ"),
 (["Ec01"], "ECHINOPS bannaticus 'Star Frost'", "cultivar", "Cultivar. The wild species grows in Europe.", "silvery-white", "July - September", "Z3 - Z8", "erect", "100 cm",
  "dry / well-drained / average", "",
  "A shorter habit with nice branching and a profusion of golf-ball sized white blooms, plus decorative foliage. Healthy dark green foliage, leaf underside grey. Good for bees. "
  "Introduced by JELITTO PERENNIAL SEEDS in 2008.", "ヨーロッパ（種の原産地）"),
 (["Ec02"], "ECHINOPS ritro ssp. ruthenicus 'Platinum Blue'", "cultivar", None, "brilliant sky-blue", "July - September", "Z3 - Z8", "", "60 cm", "dry / average", "",
  "White-woolly stems. honey-bee food plant / for the rock garden / suitable for cutting", None),
 (["Eg01"], "ERIGERON speciosus 'Rosa Juwel' [Pink Jewel]", "cultivar", None, "lilac-rose", "June - August", "Z3 - Z9", "", "70 cm", "well-drained / average", "", "suitable for cutting", None),
 (["Eg02"], "ERIGERON karvinskianus 'Blütenmeer' [Profusion, Stallone]", "cultivar", "Mexico to Panama", "white-pink", "June - October", "Z6 - Z9", "stoloniferous / low-growing", "30 cm",
  "dry / well-drained / warm", "",
  "Award of Garden Merit (A.G.M.) from the Royal Horticultural Society. Easy-to-produce, drought resistant, ground-covering perennial with lovely white to pink daisies. "
  "Suitable in filtered, dry shade, too. groundcover", "メキシコからパナマ（種の原産地）"),
 (["El01"], "ELYMUS canadensis 'Icy Blue'", "cultivar", "Cultivar. Native in North Amerika: riverbanks, prairies, open ground.", "blue spikes", "June - October", "Z3 - Z8", "clumping", "140 cm",
  "dry / moist / average", "",
  "Gently nodding spikes. Nice blue-grey clump-forming. ELYMUS canadensis has nice inflorescens, which remain attractive long into winter. Easy to grow, fast growing. "
  "ornamental foliage plant / decorative fruit; suitable for cutting", "北アメリカの川岸・草原・ひらけた土地（種の原産地）"),
 (["El02"], "ELYMUS magellanicus (AGROPYRON)", "cultivar", "South America", "straw-colored", "June - July", "Z5 - Z8", "erect / clumping", "80 cm", "well-drained / average / cool", "",
  "Foliage: intensive blue. ornamental foliage plant; suitable for cutting", "南アメリカ"),
 (["Gc01"], _GLE[0], "cultivar") + _GLE[1:], (["Gc02"], _GLE[0], "species") + _GLE[1:],
 (["Gm01"], "GALIUM odoratum (ASPERULA)", "cultivar", None, "white", "May - June", "Z4 - Z7", "stoloniferous", "15 cm", "average", "",
  "medicinal plant / beneficial plant / culinary herb / groundcover; honey-bee food plant", None),
 (["Gm02"], "GALIUM verum", "cultivar", "Europe, Asia, naturalized in the USA", "yellow", "May - September", "Z3 - Z7", "stoloniferous", "30 cm", "well-drained / average", "",
  "Abundant flower panicles. medicinal plant / culinary herb; honey-bee food plant", "ヨーロッパ・アジア（アメリカに帰化）"),
 (["Ka01"], _KAL[0], "cultivar") + _KAL[1:], (["Ka02"], _KAL[0], "species") + _KAL[1:],
 (["La01", "La02"], "LAVANDULA angustifolia (officinalis)", "species", None, "blue", "July - September", "Z5 - Z9", "", "50 cm", "dry / well-drained", "",
  "Herb of the Year 2008 in Germany. medicinal plant / beneficial plant / tea herb / culinary herb; honey-bee food plant", None),
 (["Le01"], "LEUCANTHEMUM x superbum fl. pl. 'Snowdrift' (CHRYSANTHEMUM maximum)", "cultivar", "Garden origin", "pure white", "June - August", "Z3 - Z7", "erect", "70 cm", "average", "",
  "Long-lasting, double and semi-double flowers. Healthy growth and good winter hardiness. Easy and reliable from seed. Introduced by JELITTO PERENNIAL SEEDS in 1996. suitable for cutting",
  "園芸で作られたもの"),
 (["Lt01"], _LYT[0], "cultivar") + _LYT[1:], (["Lt02"], _LYT[0], "species") + _LYT[1:],
 (["Ph01"], "PHLOMIS russeliana (samia hort.)", "cultivar", None, "yellow", "June - August", "Z6 - Z9", "wintergreen", "100 cm", "dry / undemanding", "",
  "Award of Garden Merit (A.G.M.) from the Royal Horticultural Society. Decorative fruit-stalks. groundcover; suitable for cutting", None),
 (["Ph02"], "PHLOMIS tuberosa (PHLOMOIDES) [Bronze Flamingo]", "cultivar", None, "violet", "June - July", "Z5 - Z9", "", "100 cm", "dry", "", "groundcover; suitable for cutting", None),
 (["Sg01"], _SAG[0], "cultivar") + _SAG[1:], (["Sg02"], _SAG[0], "species") + _SAG[1:],
 (["Sl01"], "SILPHIUM laciniatum", "cultivar", None, "yellow", "July - September", "Z4 - Z8", "", "200 cm", "average", "",
  "Flowers always turn eastwards. Foliage: deeply pinnatifid. solitary plant; suitable for cutting", None),
 (["Sl02"], "SILPHIUM mohrii", "cultivar", "South-eastern North-America: pairie, rocky limestone areas.", "brilliant creamy yellow", "July - November", "Z4 - Z8", "erect / clumping / lax", "160 cm",
  "dry / average", "",
  "Rich flowering, sturdy branched stems. Flowering with distinctive light yellow. Suitable for natural landscaping. Attractive for butterflies and other pollinators. "
  "Abundant and long lasting flowering. honey-bee food plant", "北アメリカ南東部の草原・石灰岩の岩場"),
 (["Sm01", "Sm02"], "SEMPERVIVUM hybridum winter hardy varieties [Hippie Chicks]", "species", None, "mixture", "June - August", "Z3 - Z8", "", "25 cm", "dry / well-drained", "",
  "Abundant mixture of small and large rosette types and cultivars. ornamental foliage plant / groundcover; for the rock garden", None),
 (["Sn01", "Sn02"], "SAPONARIA officinalis", "species", None, "pale pink", "June - September", "Z3 - Z8", "stoloniferous", "80 cm", "dry / well-drained / average", "",
  "The species produces a sticky substance (Saponin), resembling soap, hence the common name, soapwort. medicinal plant", None),
 (["Su01"], "STIPA ichu (NASSELLA, JARAVA)", "cultivar", None, "white-silver spikes", "August - October", "Z7 - Z10", "clumping / graceful", "100 cm", "dry / well-drained / average", "",
  "Award of Garden Merit (A.G.M.) from the Royal Horticultural Society. Gracile foliage clumps. solitary plant / groundcover; suitable for cutting / flowering pot plant", None),
 (["Su02"], "STIPA tenuissima (NASSELLA) [Pony Tails, Angel Hair]", "cultivar", "Southwestern and North America", "white", "July - August", "Z6 - Z10",
  "erect / clumping / graceful / wintergreen", "40 cm", "dry / well-drained / average / poor, lean / warm", "",
  "Award of Garden Merit (A.G.M.) from the Royal Horticultural Society. Drought tolerance, fine texture and white feathery spikes. In a mixed border, or en masse for a wave like, rippling effect.",
  "北アメリカ（南西部）"),
 (["Tf01"], "TRIFOLIUM ochroleucum", "cultivar", None, "brilliant light yellow", "June - July", "Z4 - Z8", "clumping / bushy", "40 cm", "average", "",
  "groundcover; honey-bee food plant / suitable for cutting", None),
 (["Tf05"], "TRIFOLIUM rubens [Red Feathers]", "cultivar", "Europe", "purple-red", "June - August", "Z4 - Z8", "erect", "60 cm", "dry / well-drained", "",
  "Dozens of plump, decorative, purple-red plumes, very decorative. groundcover", "ヨーロッパ"),
 (["Tf06"], "TRIFOLIUM rubens f. album 'Frosty Feathers'", "cultivar",
  "Cultivar. Species occurring in almost all of Europe, Mediterranean, West Asia: dry grassland, wooded borders.", "brilliant white", "June - September", "Z4 - Z8", "", "60 cm",
  "dry / average", "",
  "Dense, oval to cylindrical tapering inflorescences, reblooms after deadheading. Bright, pure white selection. Drought tolerant. Preferably calcareous soils, but overall undemanding in care. "
  "Introduced by JELITTO PERENNIAL SEEDS in 2016. groundcover", "ヨーロッパのほぼ全域・地中海沿岸・西アジアの乾いた草地、林のふち（種の原産地）"),
 (["Sy01"], "ASTER ericoides (SYMPHYOTRICHUM)", "species", "Central and Eastern USA", "white", "August - October", "Z3 - Z8", "stoloniferous", "100 cm", "average", "",
  "suitable for cutting", "アメリカ中部・東部（種の原産地）"),
 (["Yu01"], "YUCCA filamentosa", "species", "North America: sandy areas in the Rocky Mountains", "white", "July - October", "Z5 - Z9", "erect / evergreen", "150 cm",
  "dry / well-drained / average / warm", "",
  "Award of Garden Merit (A.G.M.) from the Royal Horticultural Society. Completely winter hardy. Easy to grow. Heat tolerant. Drought tolerant/ for xeriscaping/ waterwise design. "
  "Erosion control. Suitable for natural landscaping. Attractive for butterflies and other pollinators. medicinal plant / solitary plant", "北アメリカ（種の原産地）"),
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes（試験地は USDA 5b）。pdftotext -raw で読んだ。
#   no30 Leucanthemum（https://www.chicagobotanic.org/downloads/planteval_notes/no30_leucanthemum.pdf）Table 1 と本文。'Snowdrift' の総合評価の星は記号が落ちて読めなかった。
#     'Broadway Lights' は試験に入っていない。
#   no36 Asters（no36_asters.pdf）Table と本文。総合評価は星5つ（excellent）〜1つ（very poor）。'Jolly Jumper' は試験に入っていない。
#   ほかの属の号は一覧（no1〜no40）にない（no38 は屋上緑化の植物の報告で、ここでは使っていない）。
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {
 "Le01": ("×superbum 'Snowdrift'", "cultivar", 34, 36, None, None, None,
          "花つき excellent（80〜100%）。花期は6月下旬〜8月上旬。種子から育てた株で、花の形が一重から八重までばらついた。"
          "冬に株元が少し〜中くらい傷んだ年がある（寒さより、粘土質の土の湿りが原因とされている）。総合評価の星は読み取れなかった（no30）"),
 "Sy02": ("Symphyotrichum novi-belgii 'Jenny'", "cultivar", 14, 17, None, None, None,
          "総合評価 ★1（very poor）。花つき fair。うどんこ病への強さ excellent、さび病への強さ very poor（76%超がかかった）。"
          "1回目の夏を越したあと、最初の冬に枯れた（寒さより栽培上の問題と病気が原因、との記述）（no36）"),
}
