# Jelitto（s11）とシカゴ植物園（s08）: スカビオサ・ポレモニウム・フィリペンデュラ・サンギソルバ・トロリウス。
# Jelitto は 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/jelitto_cbg_data.py と同じ
#   （英語のサイト内検索: Scabiosa 21件・Polemonium 14件・Filipendula 5件・Sanguisorba 9件・Trollius 19件）。一致は17ページ。1ページごとに6秒あけて読んだ。
# 【経過】最初に検索ページを開いたとき、Cloudflare の確認画面（チェックボックス）が出たまま1分待っても進まなかったので、操作せずにいったん飛ばした。
#   15分ほど別の作業をしている間に、同じタブで確認が自動で通っていた（操作はしていない）。そのあとは一度も出なかった。
# Jelitto の書き方: Sc02 は SCABIOSA caucasica 'Perfecta' [Blue Perfection]（マスターの学名 'Blue Perfection' と商品名パーフェクタが同じ品種だと分かる）、
#   Sc04 は 'Perfecta Alba' [White Perfection]、Pl02 は POLEMONIUM caeruleum f. album、Sa07 は SANGUISORBA tenuifolia var. tenuifolia f. alba、
#   Pl07 は POLEMONIUM yezoense 'Purple Rain Strain'、Tr04 は TROLLIUS europaeus f. compactus 'Lemon Supreme'。
# Jelitto が発表した品種（Historical の欄。育種会社 s12 と同じ扱いにできる）: 'Purple Rain Strain'（2006）、'Lemon Supreme'（2010）、'New Moon'（2011。Coen Jansen から種子を受けた）。
# Sc03 'Fama' は、'Fama Deep Blue' と 'Fama White' の2つがあり、どちらか決められないので当てていない（マスターの花色は要確認）。
# 掲載なし: 'Kompliment'・'Vivid Violet'・'Moon Dance'、ポレモニウム ボレアル 'Heavenly Habit'・'Blue Whirl'・'Filigree'（カエルレウムの種のページを Pl05・Pl06 に当てた）、
#   'Apricot Delight'（carneum の種のページはある。マスターが caeruleum なので当てていない）、キョウガノコ・シモツケソウ、アルビフローラ・オブツーサ・'Pink Tanna'（あるのは 'Little Red Tanna'）・'Bordeaux'、
#   'Lemon Queen'・'Yellow Queen'・'Cheddar'。日照の欄（Location）は記号で読めなかった。
# シカゴ植物園 Plant Evaluation Notes: 一覧（no1〜no40）に、この5属の号はなかった（2026-11-20 に確認）。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-20"
_NH = "Northern Hemisphere: meadows, riparian forests, roadsides from the hills to the mountains."
_EU = "Europe to Western Siberia: damp grassland, edges of ponds, riverbanks."
JELITTO = [
 (["Sc02"], "SCABIOSA caucasica 'Perfecta' [Blue Perfection]", "cultivar", None, "lavender blue", "June - September", "Z4 - Z8", "", "50 cm", "average", "",
  "First year flowering. suitable for cutting", None),
 (["Sc04"], "SCABIOSA caucasica 'Perfecta Alba' [White Perfection]", "cultivar", None, "white", "June - September", "Z4 - Z8", "", "50 cm", "average", "",
  "First year flowering. suitable for cutting", None),
 (["Sc06"], "SCABIOSA ochroleuca (columbaria ssp. ochroleuca)", "cultivar", None, "light yellow", "June - October", "Z5 - Z8", "", "80 cm", "dry / average", "",
  "honey-bee food plant / suitable for cutting", None),
 (["Sc07"], "SCABIOSA ochroleuca (columbaria ssp. ochroleuca)", "species", None, "light yellow", "June - October", "Z5 - Z8", "", "80 cm", "dry / average", "",
  "honey-bee food plant / suitable for cutting", None),
 (["Pl02"], "POLEMONIUM caeruleum f. album", "cultivar", "Northern Hemisphere", "white", "June - July", "Z2 - Z8", "erect / clumping", "60 cm", "moist / average", "",
  "White flowering form of this popular widespread species. Reblooms after dead-heading. groundcover; suitable for cutting / flowering pot plant", "北半球（種の原産地）"),
 (["Pl05", "Pl06"], "POLEMONIUM caeruleum", "species", _NH, "Lavender blue", "June - July", "Z2 - Z8", "clumping", "60 cm", "moist / average", "",
  "Reblooms after dead-heading. medicinal plant / groundcover; honey-bee food plant / suitable for cutting / flowering pot plant", "北半球の、丘陵から山地の草地・川沿いの林・道ばた"),
 (["Pl07"], "POLEMONIUM yezoense 'Purple Rain Strain'", "cultivar", "Cultivar. North Japan, Hokkaido: open, moist forest, roadsides in the mountains.", "violet", "June - July", "Z4 - Z9",
  "erect / clumping", "50 cm", "moist / well-drained / average", "",
  "Very attractive reddish-purple pinnate foliage from late winter to early summer. Variable. Reblooms after dead-heading. Introduced by JELITTO PERENNIAL SEEDS in 2006. "
  "ornamental foliage plant / groundcover; suitable for cutting / flowering pot plant", "日本北部・北海道の、明るく湿った林や山地の道ばた（種の原産地）"),
 (["Fi04"], "FILIPENDULA rubra", "species", None, "dark pink to reddish", "June - July", "Z2 - Z7", "stoloniferous / erect", "150 cm", "moist / average", "",
  "solitary plant; suitable for cutting", None),
 (["Fi05"], "FILIPENDULA ulmaria", "cultivar", None, "yellowish-white", "June - August", "Z3 - Z7", "stoloniferous", "150 cm", "moist / boggy", "",
  "medicinal plant / beneficial plant / culinary herb; honey-bee food plant / water or marshplant", None),
 (["Fi06"], "FILIPENDULA ulmaria", "species", None, "yellowish-white", "June - August", "Z3 - Z7", "stoloniferous", "150 cm", "moist / boggy", "",
  "medicinal plant / beneficial plant / culinary herb; honey-bee food plant / water or marshplant", None),
 (["Sa02"], "SANGUISORBA hakusanensis", "cultivar", None, "dark pink", "June - August", "Z4 - Z8", "", "60 cm", "moist / average", "", "Arching flower spikes. suitable for cutting", None),
 (["Sa03"], "SANGUISORBA menziesii", "cultivar", None, "brilliant black-red", "June - July", "Z4 - Z8", "", "80 cm", "moist / average", "", "Brilliant black-red spikes. suitable for cutting", None),
 # 2026-11-27 Sa04 'Lemon Splash' は種が officinalis になったので、この種のページを当てた（Jelitto に品種のページはない）
 (["Sa04", "Sa06"], "SANGUISORBA officinalis", "species", None, "blood-red", "June - August", "Z3 - Z8", "", "60 cm", "moist", "",
  "medicinal plant / beneficial plant / tea herb / culinary herb; honey-bee food plant", None),
 (["Sa07"], "SANGUISORBA tenuifolia var. tenuifolia f. alba", "cultivar", None, "white", "July - September", "Z3 - Z8", "", "120 cm", "moist / average", "",
  "Nodding flower spikes. solitary plant; suitable for cutting", None),
 (["Tr01"], "TROLLIUS chinensis 'Golden Queen'", "cultivar", "Russia, Mongolia, Northeastern China: grassy slopes.", "golden", "July - August", "Z4 - Z7", "erect", "80 cm",
  "moist / average / cool", "", "Award of Garden Merit (A.G.M.) from the Royal Horticultural Society. suitable for cutting", "ロシア・モンゴル・中国東北部の草の斜面（種の原産地）"),
 (["Tr04"], "TROLLIUS europaeus f. compactus 'Lemon Supreme'", "cultivar", _EU, "Lemon yellow", "May - June", "Z4 - Z7", "compact / vigorous", "30 cm", "moist / cool", "",
  "An abundance of lemon yellow, bowl-shaped blossoms on a much shorter and compact plant. First year flowering. Introduced by JELITTO PERENNIAL SEEDS in 2010. "
  "for the rock garden / flowering pot plant", "ヨーロッパから西シベリアの、湿った草地・池のふち・川岸（種の原産地）"),
 (["Tr05"], "TROLLIUS europaeus", "species", _EU, "egg yolk yellow", "May - June", "Z4 - Z7", "erect", "60 cm", "moist / cool", "",
  "Good for the border or for meadow plantings in cooler climates. toxic plant; suitable for cutting", "ヨーロッパから西シベリアの、湿った草地・池のふち・川岸"),
 (["Tr03"], "TROLLIUS x cultorum 'New Moon'", "cultivar", "Cultivar, garden origin", "brilliant creamy-yellow", "April - July", "Z3 - Z7", "erect", "60 cm", "moist / average", "",
  "Large flowering, with bigger blooms and more vigor than Trollius 'Alabaster'. Requires two growing seasons for abundant flowering. Introduced by JELITTO PERENNIAL SEEDS in 2011. "
  "suitable for cutting", "園芸品種"),
]
AUTUMN = {}
CBG = {}
CBG_V = {}
