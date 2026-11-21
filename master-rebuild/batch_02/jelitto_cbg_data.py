# カンパニュラ・ヘメロカリス・カレックス: Jelitto（s11）。2026-11-19 に Chrome で読んだ。
# サイト内検索の1ページ目に出た掲載名は88件（カンパニュラは glomerata までしか出ず、ほかの種は未確認）。一致は9ページ。
# 'Kiwi'（2011）と 'Blue Ridge'（2015）は Jelitto が発表した品種（育種会社 s12 と同じ扱いにできる）。
CHECKED = "2026-11-19"
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
JELITTO = [
 (["C01"], "CAMPANULA glomerata 'Bellefleur Blue'(R)", "cultivar", "Europe: meadows and semi-dry turf on stony, calcareous soil.", "deep blue flower clusters",
  "June - September", "Z3 - Z8", "stoloniferous / rhizomatous / compact / evergreen", "20 cm", "dry / well-drained / average", "full sun",
  "Rich flowering, compact uniform habit, ideal for containers.", "ヨーロッパの草地や、石の多い石灰質のやや乾いた草原"),
 (["C02"], "CAMPANULA glomerata 'Bellefleur White'(R)", "cultivar", "Europe: meadows and semi-dry turf on stony, calcareous soil.", "pure white flower clusters",
  "June - September", "Z3 - Z8", "stoloniferous / rhizomatous / compact / evergreen", "20 cm", "well-drained / average", "",
  "Rich flowering, compact uniform habit, ideal for containers.", "ヨーロッパの草地や、石の多い石灰質のやや乾いた草原"),
 (["X02"], "CAREX albula 'Frosted Curls' (comans var. stricta, fretalis)", "cultivar", "New Zealand", "", "", "Z6 - Z9", "clumping", "20 cm",
  "well-drained / average", "full sun, semi-shade", "ornamental foliage plant; for the rock garden", "ニュージーランド"),
 (["X12"], "CAREX berggrenii", "cultivar", None, "", "", "Z6 - Z9", "cushion-forming", "5 cm", "moist", "semi-shade, bright full shade",
  "ornamental foliage plant; for the rock garden", None),
 (["X01"], "CAREX buchananii [Red Rooster]", "species", "New Zealand: bogs, moist meadows, riverbanks, forest margins.", "", "", "Z6 - Z9",
  "clumping / evergreen / wintergreen", "50 cm", "moist / gritty / well-drained / rocky", "", "Award of Garden Merit; Unpretentious.",
  "ニュージーランドの湿地・湿った草地・川岸・林縁"),
 (["X04"], "CAREX divulsa", "species", None, "", "May - June", "Z4 - Z9", "cushion-forming / clumping / evergreen", "35 cm", "dry / average",
  "semi-shade, shade, light shade", "Versatile and evergreen ground cover, tolerates dry locations.", None),
 (["X05"], "CAREX flagellifera 'Kiwi' [Phoenix Green]", "cultivar", "New Zealand", "", "July - August", "Z6 - Z9", "erect / clumping", "40 cm",
  "well-drained / average", "full sun, semi-shade", "Introduced by JELITTO PERENNIAL SEEDS in 2011. A selection of Janus Gardens.", "ニュージーランド"),
 (["X08", "X09"], "CAREX muskingumensis", "species", "North America", "tan", "", "Z4 - Z9", "stoloniferous / rhizomatous", "90 cm", "moist / average",
  "full sun, semi-shade", "tolerant of wet soils; groundcover; suitable for cutting", "北米"),
 (["X10"], "CAREX plantaginea 'Blue Ridge'", "cultivar", "Eastern North America: open woodlands.", "golden brown spikes", "April - June", "Z4 - Z8",
  "stoloniferous / clumping / evergreen / wintergreen", "35 cm", "moist / average", "semi-shade",
  "Introduced by JELITTO PERENNIAL SEED in 2015. Very vigorous, absolutely hardy selection.", "北米東部の明るい林"),
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes 31 Bellflowers（https://www.chicagobotanic.org/downloads/planteval_notes/no31_bellflower.pdf）の Table 1 と本文。
# 2026-11-19 に追加。試験地は USDA 5b、土は粘土質。pdftotext -raw で読んだ。総合評価の星は記号で取り出せなかった（本文に書かれている 'Sarastro' だけ入れた）。
# ヘメロカリスとカレックスの号はない（一覧 https://www.chicagobotanic.org/collections/ornamental_plant_research/plant_evaluation で確認）。
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {
 "C07": ("'Kent Belle'", "cultivar", 40, 30, None, None, None, "倒れやすく、支柱を勧めている"),
 "C08": ("'Samantha'", "cultivar", 12, 20, None, None, None, ""),
 "C09": ("'Sarastro'", "cultivar", 22, 24, None, None, None, "総合評価 ★5（excellent。試験の中で最高評価）。コンパクトな草姿・花つき・耐寒性が高評価。広がらない"),
 "C12": ("lactiflora 'White Pouffe'", "cultivar", 13, 26, None, None, None, "花つきは low（40%未満）。直立した草姿で一貫して健全だった"),
 "C13": ("persicifolia 'Moerheimii'", "cultivar", None, None, None, None, None,
         "試験を完了できなかった：最初の冬は越したが、2年目の夏に枯れた（土の過湿による根腐れ）。persicifolia の品種は全体に成績が悪かった"),
 "C22": ("punctata 'Wedding Bells'", "cultivar", 18, None, None, None, None, "株幅は spreading（広がる）。特に勢いが強く、3年目の夏までに区画の2倍に広がった。こぼれ種の苗も出た"),
 "C23": ("takesimana", "species", 24, 36, None, None, None, "地下茎で広がるが punctata ほど密にならない。古い株の中心は冬に枯れやすい"),
 "C24": ("takesimana 'Beautiful Trust'", "cultivar", 16, None, None, None, None, "株幅は spreading（広がる）"),
}
