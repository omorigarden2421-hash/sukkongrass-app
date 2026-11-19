# Jelitto（s11）とシカゴ植物園（s08）: ミント・ゲウム・ビンカ・プルモナリア・ペンステモン。
# Jelitto は 2026-11-19 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/jelitto_cbg_data.py と同じ
#   （英語のサイト内検索: Geum 24件・Penstemon 68件・Mentha 11件・Pulmonaria 2件・Vinca は該当なし）。一致は13ページ。
# Jelitto の書き方: 'Fireball' は GEUM chiloense 'Feuerball'、'Lady Stratheden' は 'Goldball'（マスターの商品名にも「ゴールドボール」とある）。
# 'Pinacolada Rosy Red Shades' は Jelitto の品種。ペンステモン ピグマエウスの白花（f. albus）は Jelitto が 2006 年に発表（育種会社 s12 と同じ扱いにできる）。
# 使っていないもの: 'Husker Red Superior Strain'（'Husker Red' の種子系で別もの）。'Cooky' は掲載なし（コクシネウムの種のページを当てた）。日照の欄は記号で読めなかった。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-19"
JELITTO = [
 (["Ge01"], "GEUM chiloense 'Goldball'", "cultivar", None, "golden", "June - August", "Z4 - Z10", "", "60 cm", "well-drained / average", "",
  "Award of Garden Merit (A.G.M.) from the Royal Horticultural Society. double. groundcover; suitable for cutting", None),
 (["Ge03"], "GEUM coccineum", "species", None, "orange", "May - July", "Z4 - Z9", "clumping", "40 cm", "moist / average", "",
  "Often reblooming September - October. for the rock garden / suitable for cutting", None),
 (["Ge04"], "GEUM chiloense 'Blazing Sunset'", "cultivar", "Hybrid Origin", "scarlet", "July - September", "Z4 - Z10", "stoloniferous / clumping / compact / wintergreen", "60 cm",
  "well-drained / average", "", "Fleuroselect Award Winner. Very large double-flowering scarlet bossoms. Lovely cut flowers. Can withstand dry periods in any good soil. groundcover; suitable for cutting", None),
 (["Ge05"], "GEUM chiloense 'Feuerball'", "cultivar", "Hybrid origin", "red", "July - August", "Z4 - Z10", "clumping / compact", "60 cm", "well-drained / average", "",
  "Award of Garden Merit (A.G.M.). Semi-double bright red blooms. Good cut flower candidate. Can withstand dry periods in any good garden soil. groundcover; suitable for cutting", None),
 (["Ge09", "Ge10"], "GEUM rivale", "species", "Northern Hemisphere", "light-yellow with reddish-brown calyxes", "April - May", "Z3 - Z7", "clumping", "35 cm",
  "moist / boggy / average / humus rich, fertile", "", "Lovely species for naturalizing in cool, moist conditions. groundcover; honey-bee food plant / water or marshplant", "北半球"),
 (["Me06", "Me07"], "MENTHA spicata", "species", None, "pink-white", "June - October", "Z2 - Z9", "stoloniferous", "30 cm", "moist / average", "",
  "Variable. medicinal plant / tea herb / culinary herb / groundcover; honey-bee food plant", None),
 (["Me09", "Me10"], "MENTHA suaveolens", "species", None, "pink-white", "July - September", "Z5 - Z8", "stoloniferous", "30 cm", "moist / average", "",
  "Variable. medicinal plant / tea herb / culinary herb / groundcover", None),
 (["Pe02"], "PENSTEMON barbatus f. nanus Pinacolada-Series 'Pinacolada Rosy Red Shades'", "cultivar", "Cultivar. Southern Nort-America: field edges, open woodlands.", "rosy-red colors",
  "May - September", "Z3 - Z9", "compact / vigorous", "", "", "",
  "Large inflorescence, densly branched flowering stems, abundant flowering and vigorous. Attractive for butterflies and other pollinators. Deer resistant. Drought tolerant. Easy to grow.",
  "北アメリカ南部の畑の縁や明るい林（種の原産地）"),
 (["Pe03", "Pe04"], "PENSTEMON digitalis", "species", None, "white with pink flush", "June - August", "Z3 - Z8", "", "100 cm", "dry / well-drained / average", "", "suitable for cutting", None),
 (["Pe06"], "PENSTEMON hirsutus var. pygmeus", "species", None, "violet", "June - August", "Z3 - Z8", "", "15 cm", "dry / well-drained / average", "", "for the rock garden", None),
 (["Pe07"], "PENSTEMON hirsutus var. pygmeus f. albus", "cultivar", "Species grows (USA): Tennessee to Wisconsin eastwards to New England", "pure white", "June - August", "Z3 - Z8",
  "compact / low-growing", "15 cm", "dry / well-drained / average", "",
  "Introduced by JELITTO PERENNIAL SEEDS in 2006. Very compact habit and dainty flowers. Diminutive size is ideal for planting terraced rock walls. for the rock garden",
  "アメリカのテネシーからウィスコンシン、東はニューイングランド（種の原産地）"),
 (["Pe09"], "PENSTEMON pinifolius", "species", None, "brilliant orange-red", "June - September", "Z5 - Z9", "evergreen", "20 cm", "dry / well-drained / average", "",
  "Award of Garden Merit (A.G.M.). groundcover; for the rock garden", None),
 (["Pu11"], "PULMONARIA officinalis", "species", None, "pink changing to violet", "March - April", "Z4 - Z8", "", "25 cm", "moist / average", "",
  "medicinal plant / culinary herb / groundcover; honey-bee food plant", None),
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes 17 Pulmonaria（https://www.chicagobotanic.org/downloads/planteval_notes/no17_pulmonaria.pdf）の Table 1・2 と本文。
# 試験地は USDA 5b。pdftotext -raw で読んだ。総合評価の星は記号で取り出せなかった。Table 2 は「評価が低い、または4年に満たなかった」品種の一覧。
# ミント・ゲウム・ビンカ・ペンステモンの号はない。
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {
 "Pu01": ("P. angustifolia 'Blaues Meer'", "cultivar", 12, 24, None, None, None,
          "草姿はゆるく開く。午後1〜3時の日差しが当たる場所で、葉がしおれたり縁が枯れたりすることがあった。うどんこ病は1年だけ軽く発生。冬に株元が傷んだ年がある"),
 "Pu02": ("'Blue Ensign'", "cultivar", None, None, None, None, None,
          "評価が低かった品種の一覧（Table 2）に入っている。葉の黄化（クロロシス）が重く、うどんこ病が3年続けて重く発生した（1996〜98年）"),
 "Pu04": ("'Lewis Palmer'", "cultivar", None, None, None, None, None,
          "評価が低かった品種の一覧（Table 2）に入っている。うどんこ病が中〜重（1996〜98年）。栽培条件が合わず弱り、1〜2年目の冬に全株が枯れた"),
 "Pu08": ("'Spilled Milk'", "cultivar", None, None, None, None, None, "評価が低かった品種の一覧（Table 2）に入っている。栽培条件が合わず弱り、1〜2年目の冬に全株が枯れた"),
 "Pu10": ("P. longifolia ssp. cevennensis", "species", 14, 29, None, None, None,
          "花つきは low。草姿はゆるく開く。longifolia の仲間は1994〜95年の冬に株元が大きく傷み、回復に時間がかかった"),
 "Pu11": ("'Sissinghurst White'", "cultivar", 12, 28, None, None, None, "草姿が良い品種の一つ。花つきは moderate"),
}
