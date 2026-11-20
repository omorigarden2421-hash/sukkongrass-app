# Jelitto（s11）とシカゴ植物園（s08）: タリクトラム・コレオプシス・リアトリス・リシマキア・ベロニカストラム・エリンジウム・ミスカンサス・モリニア。
# Jelitto は 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/jelitto_cbg_data.py と同じ
#   （英語のサイト内検索: Thalictrum 13件・Coreopsis 15件・Liatris 11件・Lysimachia 12件・Veronicastrum 6件・Eryngium 21件・Miscanthus 4件・Molinia 2件）。一致は27ページ。6秒おき。
#   パソコンの再起動のあと、最初の1ページで確認画面が出たが、操作せずに1分ほど置いたら自動で通った。
# グラスのページは /Seed/Ornamental+Grasses/、ベロニカストラムの白花は /Seed/Herbs/ の下にある。
# Jelitto の書き方: Th08 は rochebruneanum、Li07 は LIATRIS spicata 'Kobold Strain'（種子の系統）、Vs07 は VERONICASTRUM virginicum f. albiflorum、
#   モリニアは亜種ごとのページ（ssp. caerulea／ssp. arundinacea）。Historical の欄に「Jelitto が発表」と書かれた品種はなかった。
# 種のページを当てたもの: アキレジフォリウム（Th01・Th02）、ロゼア（Co04）、バーティシラータ（Co05・Co06）、プンクタータ（Ly06）、バリフォリウム（Er05）、ススキ（Mi02〜Mi04・Mi06）、モリニア（全品種）。
#   当てていないもの: Co07 'Star Cluster'（RHS は種小名なし）、Mi05 'Purpurascens'（RHS は sinensis ではないとしている）、Vs02 エゾクガイソウ、西洋クガイソウの色つきの品種。
# 掲載なし: コレオプシスの交配品種、コンジェスティフロラ・ヌンムラリア、'Black Stockings'・'Elin'。日照の欄（Location）は記号で読めなかった。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-20"
_MIS = ("MISCANTHUS sinensis", None, "", "September - October", "Z4 - Z9", "erect / vigorous / tall", "250 cm", "average", "", "Variable, bio-energy-plant. solitary plant / beneficial plant", None)
_PUN = ("LYSIMACHIA punctata", None, "yellow", "June - August", "Z4 - Z9", "stoloniferous", "65 cm", "moist / average", "", "honey-bee food plant / suitable for cutting / water or marshplant", None)
JELITTO = [
 (["Th01", "Th02"], "THALICTRUM aquilegiifolium", "species", "Europe, Northern Asia", "pink and white", "May - July", "Z5 - Z8", "erect", "120 cm", "moist / average", "",
  "Significant architectural plant with dozens of wispy blooms and Aquilegia-like foliage. honey-bee food plant / suitable for cutting", "ヨーロッパ、北アジア"),
 (["Th03"], "THALICTRUM delavayi", "cultivar", None, "lilac-rose, seldom white", "July - August", "Z5 - Z8", "", "100 cm", "average", "",
  "Award of Garden Merit (A.G.M.) from the Royal Horticultural Society. suitable for cutting", None),
 (["Th04"], "THALICTRUM delavayi 'Album'", "cultivar", None, "pure white", "July - August", "Z5 - Z8", "", "100 cm", "average", "", "Foliage: lime-green. suitable for cutting", None),
 (["Th05"], "THALICTRUM flavum ssp. glaucum", "cultivar", None, "yellow", "June - July", "Z5 - Z8", "stoloniferous", "150 cm", "moist / average", "",
  "Award of Garden Merit (A.G.M.). Foliage: blue-grey. honey-bee food plant / suitable for cutting", None),
 (["Th08"], "THALICTRUM rochebruneanum", "cultivar", "Japan: meadows and forest margins.", "reddish-lilac", "July - August", "Z5 - Z8", "tall / lax", "150 cm", "moist / average / cool", "",
  "Moderate self-sowing at suitable locations. Decorative architectural plant. Easy to grow. solitary plant; suitable for cutting", "日本の草地・林のふち"),
 (["Co04"], "COREOPSIS rosea", "species", None, "pink", "June - July", "Z4 - Z9", "", "25 cm", "average", "", "for the rock garden", None),
 (["Co05", "Co06"], "COREOPSIS verticillata", "species", "Eastern North America: open woodland, open pine barrens.", "golden yellow", "June - September", "Z4 - Z9",
  "stoloniferous / erect / bushy", "80 cm", "dry / well-drained / average", "",
  "Higher than the varieties. Attractive for butterflies and other pollinators. Deer resistent. Drought tolerant. Heat tolerant. Moderate self-sowing in suitable locations. suitable for cutting",
  "北アメリカ東部の明るい林・マツの疎林"),
 (["Li01"], "LIATRIS pycnostachya", "cultivar", None, "light purple", "July - September", "Z3 - Z8", "erect / slender, narrow / tall", "160 cm", "moist / average", "",
  "Dense blossom heads. suitable for cutting", None),
 (["Li02"], "LIATRIS scariosa", "cultivar", None, "red-purple", "July - October", "Z3 - Z8", "", "120 cm", "average", "", "large single flowers on sturdy stems. suitable for cutting", None),
 (["Li03"], "LIATRIS scariosa 'Alba'", "cultivar", None, "white", "July - September", "Z3 - Z8", "erect", "90 cm", "average", "", "Large flowering. suitable for cutting", None),
 (["Li04"], "LIATRIS spicata", "cultivar", None, "lilac-rose", "July - September", "Z3 - Z8", "erect", "100 cm", "dry / average", "",
  "medicinal plant; honey-bee food plant / suitable for cutting", None),
 (["Li05"], "LIATRIS spicata 'Floristan Violet'", "cultivar", None, "violet", "July - September", "Z3 - Z8", "erect", "90 cm", "dry / average", "",
  "Long stems. honey-bee food plant / suitable for cutting", None),
 (["Li06"], "LIATRIS spicata 'Floristan White'", "cultivar", None, "white", "July - September", "Z3 - Z8", "erect", "90 cm", "dry / average", "",
  "Excellent cut flower. honey-bee food plant / suitable for cutting", None),
 (["Li07"], "LIATRIS spicata 'Kobold Strain'", "cultivar", "USA: Maine to Florida, westwards to Louisiana", "lilac-rose", "July - September", "Z3 - Z8",
  "erect / clumping / compact / low-growing", "50 cm", "dry / well-drained / average", "",
  "A lower growing seed strain. Will prefer a bit more moisture than other Liatris species. Variable. honey-bee food plant / flowering pot plant",
  "アメリカのメイン州からフロリダ、西はルイジアナまで（種の原産地）"),
 (["Ly05"], _PUN[0], "cultivar") + _PUN[1:],
 (["Ly06"], _PUN[0], "species") + _PUN[1:],
 (["Ly07"], "LYSIMACHIA vulgaris", "cultivar", None, "golden", "June - August", "Z4 - Z9", "stoloniferous", "80 cm", "moist / average", "",
  "medicinal plant; honey-bee food plant / water or marshplant", None),
 (["Vs01"], "VERONICASTRUM sibiricum", "cultivar", "East Asia and Siberia: damp meadows, river banks, forest edges.", "blue-lilac", "June - August", "Z3 - Z8", "erect / clumping / sturdy", "160 cm",
  "moist", "", "solitary plant; suitable for cutting", "東アジアとシベリアの湿った草地・川岸・林のふち"),
 (["Vs07"], "VERONICASTRUM virginicum f. albiflorum", "cultivar", "Eastern North America: damp meadows, river banks, forest edges.", "white, rarely light blue", "July - September", "Z3 - Z8",
  "erect / clumping / sturdy", "175 cm", "moist / average", "", "Perennial Plant of the Year 2006 in Sweden. medicinal plant; suitable for cutting", "北アメリカ東部の湿った草地・川岸・林のふち"),
 (["Er01"], "ERYNGIUM planum", "cultivar", None, "steel blue", "June - August", "Z4 - Z8", "", "120 cm", "dry / well-drained / average", "",
  "Small blossom heads. honey-bee food plant / suitable for cutting", None),
 (["Er02"], "ERYNGIUM planum 'Blue Glitter'", "cultivar", None, "brilliant deep blue", "July - September", "Z4 - Z8", "", "80 cm", "dry / well-drained / average", "",
  "Fleuroselect Award Winner. Richly branched, first year flowering from seed without vernalisation. honey-bee food plant / suitable for cutting", None),
 (["Er03"], "ERYNGIUM planum 'Blue Hobbit'", "cultivar", None, "brilliant blue", "July - September", "Z4 - Z8", "round / compact", "30 cm", "dry / well-drained / average", "",
  "Very rich flowering, ideal for containers. honey-bee food plant / flowering pot plant", None),
 (["Er04"], "ERYNGIUM planum 'White Glitter'", "cultivar", None, "white", "July - September", "Z4 - Z8", "", "80 cm", "dry / well-drained / average", "",
  "Richly branched, first year flowering from seed without vernalisation. honey-bee food plant / suitable for cutting", None),
 (["Er05"], "ERYNGIUM variifolium", "species", "North Africa", "grey", "July - August", "Z5 - Z9", "clumping", "40 cm", "dry / gritty / well-drained / average", "",
  "Attractive evergreen (in warmer zones) perennial with a clumping basal rosette of dark green leaves and extraordinary white veining. "
  "ornamental foliage plant; honey-bee food plant / for the rock garden", "北アフリカ"),
 (["Er06"], "ERYNGIUM yuccifolium", "cultivar", None, "white", "July - September", "Z3 - Z9", "", "120 cm", "dry / gritty / well-drained / average", "",
  "Round white blossoms, valuable cut flower. Foliage: yucca-like. suitable for cutting", None),
 (["Mi01"], _MIS[0], "cultivar") + _MIS[1:],
 (["Mi02", "Mi03", "Mi04", "Mi06"], _MIS[0], "species") + _MIS[1:],
 (["Mo03"], "MOLINIA caerulea ssp. arundinacea", "species", None, "", "June - August", "Z4 - Z7", "erect / clumping", "175 cm", "moist / alkaline / average / poor, lean / clay", "",
  "Foliage: golden-brown fall color. solitary plant; suitable for cutting / water or marshplant", None),
 (["Mo01", "Mo02", "Mo04", "Mo05", "Mo06"], "MOLINIA caerulea ssp. caerulea", "species", None, "", "July - October", "Z4 - Z7", "erect / clumping", "65 cm", "moist / average", "",
  "Foliage: bluish-green. beneficial plant; suitable for cutting / water or marshplant", None),
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes（試験地は USDA 5b、日なた）。pdftotext -raw で読んだ。
#   no28 Meadow rues（https://www.chicagobotanic.org/downloads/planteval_notes/no28_meadowrues.pdf）Table 1 と本文。総合評価は4つ星 good・3つ星 fair・2つ星 poor
#   no9 Blazing stars（リアトリス）は PDF が画像だけで、文字として読めなかった（no5 Yarrow と同じ）
#   コレオプシス・リシマキア・ベロニカストラム・エリンジウム・ミスカンサス・モリニアの号は一覧（no1〜no40）にない
#   'Thundercloud'・delavayi 'Album'・'Black Stockings' は試験に入っていない
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {
 "Th01": ("aquilegiifolium 'Purpureum'", "cultivar", 42, 20, None, None, None,
          "総合評価 good（4つ星）。花つき 60〜80%。種や var. album より丈夫で花が多い。花色は株によって幅があり、種よりわずかに濃い程度。試験地の条件（土の水分が一定でない・日なた）でアキレジフォリウムは草勢が弱った（no28）"),
 "Th03": ("delavayi", "species", 33, 14, None, None, None,
          "総合評価 poor（2つ星）。植え付け後の根づきが悪く、8株中7株が最初の冬（1998-99）に枯れ、残る1株も2000-01の冬に枯れた。再試験はしていない（no28）"),
 "Th05": ("flavum ssp. glaucum", "species", 72, 30, None, None, None, "総合評価 good（4つ星）。花つき 60〜80%（no28）"),
 "Th07": ("'Elin'", "cultivar", 96, 42, None, None, None,
          "総合評価 good（4つ星）。花つき 60〜80%。草勢は両親をしのぎ、茎は8フィート（約2.4m）に達した。夏の間も葉を落とさずよく茂った。2001年と2003年にひどいうどんこ病が出た（no28）"),
 "Th08": ("rochebruneanum", "species", 72, 30, None, None, None, "総合評価 good（4つ星）。花つき 60〜80%。夏に葉を落として株がすく（'Elin' との比較の記述）（no28）"),
}
