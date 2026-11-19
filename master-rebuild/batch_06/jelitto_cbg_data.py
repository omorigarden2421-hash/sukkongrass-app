# Jelitto（s11）とシカゴ植物園（s08）: ポテンティラ・パニカム・アキレア・スタキス・ヒューケラ。
# Jelitto は 2026-11-19 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/jelitto_cbg_data.py と同じ
#   （英語のサイト内検索: Achillea 19件・Heuchera 20件・Panicum 6件・Potentilla 30件・Stachys 11件）。一致は24ページ。1ページごとに6秒あけて読んだ（確認画面は出なかった）。
# パニカムのページは /Seed/Ornamental+Grasses/ の下にある（/Seed/Perennials/ ではない）。
# Jelitto の書き方: 'Parker's Variety' は 'Parkers Varietät'、'Firefly' は 'Leuchtkäfer'、ベルナは POTENTILLA neumanniana。
# 'Love Parade' は Jelitto が発表した品種（試作 P05 と同じ。DECISIONS.md）。'Silky Fleece' は Gaißmayer のページに「Jelitto 2006」とある。
# 今回は Historical・Distinction の欄を読み飛ばしたので、ほかに Jelitto が発表元の品種があるかは未確認。
# 使っていないもの: POTENTILLA atrosanguinea 'Red'（種子系）、ACHILLEA tomentosa 'Aurea'・'Golden Fleece'（種そのもののページはなし）。日照の欄は記号で読めなかった。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-19"
JELITTO = [
 (["Ac01"], "ACHILLEA filipendulina 'Parkers Varietät'", "cultivar", "Caucasus", "yellow", "July - September", "Z3 - Z8", "erect", "120 cm", "well-drained / average", "",
  "Flat yellow flowers and green finely divided foliage. honey-bee food plant / suitable for cutting", "コーカサス（種の原産地）"),
 (["Ac05"], "ACHILLEA millefolium 'Cassis'", "cultivar", "Cultivar. Europe to Siberia: meadows, pastures, wasteland, dry grasslands, roadsides.", "cherry-red", "June - October", "", "", "", "", "",
  "Cherry-red umbels, rich flowering. A second flowering after deadheading is possible at good locations. Drought tolerant. Attractive for butterflies and other pollinators. Deer resistant.",
  "ヨーロッパからシベリアの草地・牧草地・荒れ地・乾いた草原・道ばた（種の原産地）"),
 (["Ac06"], "ACHILLEA millefolium wild form", "species", "Europe to Siberia: meadows, pastures, wasteland, dry grasslands, roadsides.", "white", "June - October", "Z2 - Z9",
  "stoloniferous / vigorous", "40 cm", "dry / well-drained / average", "",
  "ACHILLEA millefolium has a second flowering in autumn when pruning. attractive to bees, butterflies and other insects. Deer resistant.",
  "ヨーロッパからシベリアの草地・牧草地・荒れ地・乾いた草原・道ばた"),
 (["Ac07"], "ACHILLEA ptarmica fl. pl. 'Noblessa'", "cultivar", None, "pure white", "May - September", "Z3 - Z9", "stoloniferous / compact", "50 cm", "moist / average / humus rich, fertile", "",
  "double. Deer resistant. Easy to grow. Long blooming perennial. suitable for cutting", None),
 (["Ac08"], "ACHILLEA sibirica ssp. camtschatica 'Love Parade'", "cultivar", "Kamtschatka peninsula in Eastern Russia", "soft pink", "June - September", "Z4 - Z8", "clumping", "60 cm",
  "dry / well-drained", "", "Outstanding combination of foliage and flowers. Excellent border plant and cut flower. suitable for cutting", "ロシア東部のカムチャツカ半島（種の原産地）"),
 (["He01"], "HEUCHERA americana 'Dale's Strain'", "cultivar", "Eastern USA", "cream-colored", "June - August", "Z3 - Z9", "clumping / low-growing", "60 cm", "average", "",
  "Handsome, silver mottled foliage, variable. ornamental foliage plant / groundcover; for the rock garden / suitable for cutting", "アメリカ東部（種の原産地）"),
 (["He10"], "HEUCHERA micrantha", "species", None, "white", "May - August", "Z4 - Z7", "evergreen", "40 cm", "average", "", "ornamental foliage plant / groundcover; for the rock garden", None),
 (["He11"], "HEUCHERA sanguinea 'Leuchtkäfer'", "cultivar", None, "dark scarlet", "May - July", "Z3 - Z8", "", "60 cm", "average", "", "groundcover; suitable for cutting", None),
 (["He12"], "HEUCHERA sanguinea 'White Cloud'", "cultivar", "Arizona and New Mexico (USA)", "white", "June - August", "Z3 - Z8", "cushion-forming", "60 cm", "average", "",
  "groundcover; for the rock garden", "アメリカのアリゾナ・ニューメキシコ（種の原産地）"),
 (["Pa01"], "PANICUM virgatum 'Blue Giants'", "cultivar", None, "", "August - October", "Z5 - Z9", "clumping", "180 cm", "dry / average", "",
  "Greenish blue spikes, variable, impressive foliage clumps. ornamental foliage plant / solitary plant / groundcover; suitable for cutting", None),
 (["Pa04"], "PANICUM virgatum 'Emerald Chief'", "cultivar", "North America, southwards to Central America", "pinkish-red", "July - September", "Z4 - Z10", "erect / sturdy", "", "", "",
  "Graceful and especially sturdy habit. Long-lived, tolerating a wide range of soils. A prairie species, an outstanding species for naturalizing in meadows.", "北アメリカから中央アメリカ（種の原産地）"),
 (["Pa02", "Pa03", "Pa05", "Pa06", "Pa07", "Pa08"], "PANICUM virgatum", "species", "North America", "brownish", "July - September", "Z4 - Z10", "erect / clumping", "160 cm", "dry / average", "",
  "Variable. beneficial plant / groundcover; suitable for cutting", "北アメリカ"),
 (["Po02"], "POTENTILLA atrosanguinea var. argyrophylla", "species", "Himalayas", "yellow-orange with red eye", "June - August", "Z5 - Z8", "mat-forming / lax", "40 cm", "well-drained / average", "",
  "Lovely bi-colored flowers and silky foliage. groundcover; for the rock garden", "ヒマラヤ"),
 (["Po05"], "POTENTILLA nepalensis 'Helen Jane'", "cultivar", "Western Himalayas", "brilliant pink with red eye", "May - July", "Z5 - Z8", "cushion-forming / compact", "30 cm",
  "dry / well-drained / average", "", "An outstanding, low-growing choice for container production. groundcover; for the rock garden", "ヒマラヤ西部（種の原産地）"),
 (["Po07"], "POTENTILLA nepalensis 'Miss Willmott'", "cultivar", "Himalayas", "carmine-rose", "May - July", "Z5 - Z8", "clumping / compact", "40 cm", "dry / well-drained / average", "",
  "For heath- and cottage gardens as well as for perennial borders. groundcover", "ヒマラヤ（種の原産地）"),
 (["Po08"], "POTENTILLA nepalensis 'Ron McBeath'", "cultivar", "Western Himalayas", "carmine-red", "May - July", "Z5 - Z8", "stoloniferous / cushion-forming", "30 cm",
  "dry / well-drained / average", "", "a more compact habit than the long popular 'Miss Willmott'. groundcover", "ヒマラヤ西部（種の原産地）"),
 (["Po09"], "POTENTILLA thurberi 'Monarch's Velvet'", "cultivar", "Arizona and New Mexico (USA) and Northern Mexiko", "raspberry-red with velvet-red center", "June - August", "Z5 - Z8",
  "cushion-forming", "40 cm", "dry / well-drained / average", "", "Beautiful velvety blossoms. groundcover", "アメリカのアリゾナ・ニューメキシコとメキシコ北部（種の原産地）"),
 (["Po12"], "POTENTILLA neumanniana", "species", "Europe: dry meadows, slopes, walls, roadsides.", "golden", "April - May", "Z4 - Z8", "stoloniferous / mat-forming", "15 cm",
  "dry / rocky / poor, lean / loamy / warm", "", "groundcover; honey-bee food plant / for the rock garden / for green roofs", "ヨーロッパの乾いた草地・斜面・石垣・道ばた"),
 (["St01", "St02"], "STACHYS byzantina", "species", "Caucasus", "lilac", "July - September", "Z4 - Z7", "stoloniferous", "40 cm", "dry / well-drained", "",
  "Exquisite, broad, silvery leaves. ornamental foliage plant; honey-bee food plant", "コーカサス"),
 (["St03"], "STACHYS byzantina 'Silky Fleece'", "cultivar", "Türkiye, Iran", "lilac-plum", "July - August", "Z4 - Z7", "stoloniferous / cushion-forming / low-growing", "25 cm",
  "well-drained / average", "", "A dwarf lambs' ear. The silver gray foliage blends well with virtually all groundcovers.", "トルコ、イラン（種の原産地）"),
 (["St04"], "STACHYS macrantha", "species", "Caucasus", "purple-rose", "July - August", "Z4 - Z7", "clumping", "45 cm", "well-drained / average", "",
  "Larger flowering selection from seed. groundcover; suitable for cutting", "コーカサス"),
 (["St05"], "STACHYS macrantha 'Morning Blush'", "cultivar", "Caucasus", "white, pink-flushed", "July - August", "Z4 - Z7", "clumping / compact / low-growing", "40 cm", "dry / well-drained", "",
  "Large flowering. ornamental foliage plant / groundcover", "コーカサス（種の原産地）"),
 (["St08"], "STACHYS officinalis", "species", None, "pink", "July - August", "Z4 - Z7", "", "30 cm", "dry / average", "", "medicinal plant / tea herb / culinary herb; honey-bee food plant", None),
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes（試験地は USDA 5b）。pdftotext -raw で読んだ。総合評価の星は記号で取り出せなかった（本文に書かれている評価だけ入れた）。
#   no27 Stachys（https://www.chicagobotanic.org/downloads/planteval_notes/no27_stachys.pdf）Table 1 と本文。草丈は「葉の高さ／花を含む高さ」で、ここには花を含む高さを入れた
#   no21 Coral bells（https://www.chicagobotanic.org/downloads/planteval_notes/no21_coralbells.pdf）Table 1・2 と本文
#   no5 Yarrow（アキレア）は PDF が画像だけで、文字として読めなかった。ポテンティラ・パニカムの号はない
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {
 "He01": ("americana 'Dale's Strain'", "cultivar", None, None, None, None, None, "評価が低かった品種の一覧（Table 2）に入っている。茎や株元の腐れで冬に枯れた品種の一つ（no21）"),
 "He12": ("sanguinea 'White Cloud'", "cultivar", 26, 22, None, None, None, "最高評価の6品種の一つ（草姿・葉の健全さ・花つき・耐寒性とも良い）。花つき 80%。花茎が倒れにくい（no21）"),
 "St01": ("byzantina", "species", 30, 26, None, None, None, "花つき 60〜80%（no27）"),
 "St02": ("byzantina 'Primrose Heron'", "cultivar", 16, 20, None, None, None,
          "花つきは20%未満。広がるより株立ちになる。冬の傷みが繰り返し出て、春の芽吹きが遅く、勢いが弱かった。葉はライムイエローで、のちに灰緑色に変わる（no27）"),
 "St04": ("macrantha", "species", 18, 24, None, None, None, "総合評価は fair（花つきが20〜40%と少なく、草姿が弱い）（no27）"),
 "St07": ("monieri 'Hummelo'", "cultivar", 24, 20, None, None, None, "総合評価 excellent（試験の中で最高評価）。花つき 80〜100%、葉が健全で草姿がそろう（no27）"),
 "St08": ("officinalis", "species", 30, 30, None, None, None, "花つき 80〜100%（no27）"),
}
