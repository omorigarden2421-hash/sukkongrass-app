# Jelitto（s11）とシカゴ植物園（s08）: ダイアンサス・ヘレニウム・ミューレンベルギア・アルメリア・ユーフォルビア・ヘリアンセマム・クニフォフィア・ペニセタム・ルドベキア・タイム。
# Jelitto は 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/jelitto_cbg_data.py と同じ
#   （英語のサイト内検索: Dianthus carthusianorum 3件・Dianthus deltoides 7件・Helenium 9件・Muhlenbergia 7件・Armeria maritima 5件・Euphorbia 18件・Helianthemum 7件・
#     Kniphofia 12件・Pennisetum 9件・Rudbeckia 33件・Thymus 21件）。一致は23ページ。6秒おき。確認画面は出なかった。
# Jelitto の書き方: Eu04 ポリクロマは EUPHORBIA epithymoides、Ru01 は RUDBECKIA fulgida var. sullivantii 'Goldsturm'、Ty11 は THYMUS vulgaris 'French Summer'、
#   Mu01 は MUHLENBERGIA capillaris hort.、タイムのセパイラムは THYMUS serpyllum hort.。
# Jelitto が発表した品種（Historical の欄）: タイム 'Magic Carpet'（2001。種子の系統）。
# 種のページを当てたもの: カシュジアノーラム（Di02）、ヘレニウム オータムナーレ（Hl01〜Hl03。wild form）、キパリシアス（Eu02）・グリフィシー（Eu03）、
#   ヘリアンセマム ヌンムラリウム（Hm03・Hm04）、ペニセタム アロペキュロイデス（Pn01）、サブトメントーサ（Ru03・Ru04）、プレジオイデス（Ty05）、セパイラム（Ty08）。
#   当てていないもの: アルメリアの 'Alba' 以外（種そのもののページがない）、ペニセタム 'Fairy Tails'（orientale のページはあるが、マスターは種小名なし）、クニフォフィア（該当品種なし）。
# 'Goldsturm' のページは本文が長く、表の後半（ゾーン・高さ・土）を読み取れなかった。日照の欄（Location）は記号で読めなかった。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-20"
_CAR = ("DIANTHUS carthusianorum", "European Alps, Türkiye, Middle East: roadsides, nutrient poor grasslands, slopes.", "purple-red", "June - September", "Z3 - Z8",
        "cushion-forming / erect / clumping / wintergreen", "40 cm", "dry / well-drained", "",
        "Suitable for natural plantings on dry meadows and slopes. Attracts butterflies. Plant of the Year 1989 in Germany. honey-bee food plant / for the rock garden",
        "ヨーロッパアルプス・トルコ・中東の道ばた、やせた草地、斜面")
_SER = ("THYMUS serpyllum hort.", "Europe", "purple-violet", "May - September", "Z4 - Z8", "", "15 cm", "dry / well-drained", "",
        "medicinal plant / tea herb / culinary herb / groundcover; honey-bee food plant / for the rock garden", "ヨーロッパ")
_SUB = (["Ru03", "Ru04"], "RUDBECKIA subtomentosa", "species", None, "golden", "July - September", "Z3 - Z8", "", "80 cm", "average", "", "", None)
JELITTO = [
 (["Di01"], _CAR[0], "cultivar") + _CAR[1:],
 (["Di02"], _CAR[0], "species") + _CAR[1:],
 (["Di03"], "DIANTHUS deltoides 'Arctic Fire'", "cultivar", "Cultivar", "white with brilliant red eye", "June - September", "Z3 - Z8", "", "20 cm", "dry / well-drained", "",
  "Easy to grow and undemanding in the garden. For rock garden, flower bed planting and gravel in a dry location. groundcover; for the rock garden / flowering pot plant", "園芸品種"),
 (["Hl01", "Hl02", "Hl03"], "HELENIUM autumnale wild form", "species", None, "golden", "August - October", "Z3 - Z8", "", "150 cm", "average", "",
  "honey-bee food plant / suitable for cutting", None),
 (["Mu01"], "MUHLENBERGIA capillaris hort.", "cultivar", "Southeastern USA", "purple-pink", "September - November", "Z6 - Z10", "clumping", "90 cm", "moist / well-drained", "",
  "Exquisite, hairy pink-purple flower panicles. Need a warm summer to flower. solitary plant / groundcover; for the rock garden / suitable for cutting", "アメリカ南東部"),
 (["Mu02"], "MUHLENBERGIA dumosa", "cultivar", None, "", "April - May", "Z7 - Z10", "", "120 cm", "dry / well-drained", "",
  "Foliage: delicate narrow foliage on bamboo-like stalks. solitary plant; patio plant / suitable for cutting", None),
 (["Mu03"], "MUHLENBERGIA lindheimeri", "cultivar", "Texas (USA), Mexico", "yellowish-tan turning to pale purple", "September - October", "Z6 - Z10",
  "cushion-forming / erect / round / wintergreen", "150 cm", "lime-loving, calcareous / well-drained / average", "",
  "Semi-evergreen blue-grey basal leaves and decorative flowering spikes. Need a warm summer to flower. solitary plant", "アメリカのテキサス、メキシコ"),
 (["Mu04"], "MUHLENBERGIA reverchonii Undaunted®", "cultivar", "Selection. North America, Southwest USA: rocky slopes.", "pinkish red flower veils", "August - October", "Z5 - Z10",
  "clumping", "50 cm", "dry / warm", "",
  "Plant Select. Warm season grass. Tolerant of heat, cold and humidity, grows in almost any soil. decorative fruit / solitary plant / groundcover; for the rock garden / suitable for cutting",
  "北アメリカ・アメリカ南西部の岩の斜面（種の原産地）"),
 (["Mu05"], "MUHLENBERGIA rigens", "cultivar", "Mexico and USA from Texas to California and Nevada", "tan", "August - October", "Z6 - Z10", "clumping / wintergreen", "150 cm",
  "dry / well-drained", "", "Narrow inflorescences. Very drought tolerant. solitary plant / groundcover; for the rock garden", "メキシコと、アメリカのテキサスからカリフォルニア・ネバダ"),
 (["Ar02"], "ARMERIA maritima 'Alba'", "cultivar", "Europe, North Africa to Türkiye, and North America", "pure white", "May - July", "Z3 - Z7", "cushion-forming / low-growing", "20 cm",
  "dry / well-drained", "", "Flowers shaped like little drumsticks. First year flowering. groundcover; honey-bee food plant", "ヨーロッパ、北アフリカからトルコ、北アメリカ（種の原産地）"),
 (["Eu02"], "EUPHORBIA cyparissias", "species", "Europe, Türkiye", "yellow to reddish", "June - July", "Z3 - Z8", "stoloniferous", "30 cm", "", "",
  "Give the durable, cypress spurge plenty of room to grow. Spreads by rampant underground runners. Has the intention to overgrowth. Drought tolerant species. "
  "Avoid contact with the milky sap of the leaves that can cause dermatitis.", "ヨーロッパ、トルコ"),
 (["Eu04"], "EUPHORBIA epithymoides", "cultivar", "South Germany and Southeastern Europe: dry woodland edges and slopes.", "light yellow", "May - June", "Z4 - Z8",
  "round / clumping / low-growing / bushy", "", "", "",
  "Award of Garden Merit (A.G.M.). Low maintenance perennial. Foliage with warm autumn colors of yellows to bronze. Avoid contact with the milky sap of the leaves that can cause dermatitis.",
  "ドイツ南部とヨーロッパ南東部の乾いた林のふち・斜面"),
 (["Eu03"], "EUPHORBIA griffithii", "species", "Himalayas", "orange-red", "May - June", "Z5 - Z8", "erect / bushy", "60 cm", "moist / average", "",
  "Avoid contact with the milky sap of the leaves that can cause dermatitis. ornamental foliage plant / toxic plant; suitable for cutting", "ヒマラヤ"),
 (["Hm03", "Hm04"], "HELIANTHEMUM nummularium", "species", None, "yellow", "May - July", "Z4 - Z7", "wintergreen", "10 cm", "dry / average", "", "groundcover; for the rock garden", None),
 (["Pn01"], "PENNISETUM alopecuroides", "species", "East Asia", "pale brownish", "August - December", "Z5 - Z9", "clumping / bushy", "80 cm", "dry / well-drained / alkaline / average", "",
  "Arching inflorescences like water pouring from a fountain. decorative fruit / groundcover; suitable for cutting", "東アジア"),
 (["Pn02"], "PENNISETUM alopecuroides var. viridescens", "cultivar", None, "", "October - December", "Z5 - Z9", "", "50 cm", "dry / well-drained / alkaline / average", "",
  "Broader leaves, darker heads. groundcover; suitable for cutting", None),
 (["Pn04"], "PENNISETUM macrourum", "cultivar", None, "straw-colored", "July - October", "Z6 - Z10", "stoloniferous / clumping", "140 cm", "dry / average", "",
  "Long flower spikes. groundcover; suitable for cutting", None),
 (["Ru01"], "RUDBECKIA fulgida var. sullivantii 'Goldsturm'", "cultivar", "USA (Conneticut to North Carolina, west to Michigan and Missouri)", "", "", "", "", "", "", "",
  "Award of Garden Merit (A.G.M.). Perennial Plant of the year (PPA). A durable, low maintenance, pest-free plant. Heat-treated seed is virtually Septoria free, but secondary infection is still possible.",
  "アメリカ（コネチカットからノースカロライナ、西はミシガン・ミズーリ）（種の原産地）"),
 _SUB,
 (["Ty04"], "THYMUS mastichina", "cultivar", None, "white", "May - August", "Z6 - Z9", "", "30 cm", "dry / average", "",
  "Foliage: grey-green, aromatic. medicinal plant / beneficial plant / culinary herb; honey-bee food plant", None),
 (["Ty05"], "THYMUS pulegioides", "species", None, "mauve", "July - October", "Z4 - Z8", "", "25 cm", "dry / well-drained / average", "",
  "medicinal plant / beneficial plant / culinary herb / groundcover; honey-bee food plant / for green roofs", None),
 (["Ty06", "Ty07", "Ty10"], _SER[0], "cultivar") + _SER[1:],
 (["Ty08"], _SER[0], "species") + _SER[1:],
 (["Ty09"], "THYMUS serpyllum 'Magic Carpet'", "cultivar", "Europe", "carmine-pink", "May - August", "Z4 - Z8", "stoloniferous / mat-forming / low-growing", "5 cm", "dry / well-drained", "",
  "A seed strain that forms perfectly low carpets with foliage and has the sweet fragrance of lemon thyme. Introduced by JELITTO PERENNIAL SEED in 2001. groundcover", "ヨーロッパ（種の原産地）"),
 (["Ty11"], "THYMUS vulgaris 'French Summer'", "cultivar", None, "pinkish-white", "June - September", "Z7 - Z10", "stoloniferous / cushion-forming / low-growing / evergreen", "30 cm",
  "dry / well-drained / average / poor, lean", "", "Foliage: grey, narrow. medicinal plant / culinary herb / groundcover; honey-bee food plant", None),
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes: この10属では no8 Rudbeckia だけ号があるが、PDF が画像だけで文字として読めなかった（no5・no9 と同じ）。使える記録はなし。
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {}
