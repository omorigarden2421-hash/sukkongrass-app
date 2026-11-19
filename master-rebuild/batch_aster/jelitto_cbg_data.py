# アスター: Jelitto（s11）とシカゴ植物園の評価報告（s08）。2026-11-19。
CHECKED = "2026-11-19"
# Jelitto: Chrome で読んだ。アスターの掲載は21件。試行の品種そのもののページはなく、種のページが6つ。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
JELITTO = [
 (["A03"], "ASTER divaricatus (EURYBIA)", "species", "Eastern USA", "white", "September - October", "Z3 - Z8", None, "60 cm", "average",
  "full sun, semi-shade", "groundcover; suitable for cutting", "米国東部"),
 (["A08"], "ASTER ericoides (SYMPHYOTRICHUM)", "species", "Central and Eastern USA", "white", "August - October", "Z3 - Z8", "stoloniferous", "100 cm",
  "average", "full sun", "suitable for cutting", "米国中部・東部"),
 (["A14", "A15"], "ASTER macrophyllus (EURYBIA)", "species", "North America", "light violet to white", "August - September", "Z3 - Z7", "stoloniferous",
  "80 cm", "average", "full sun", "", "北米"),
 (["A16", "A17", "A18", "A19"], "ASTER novae-angliae (SYMPHYOTRICHUM)", "species", "Eastern North America", "pink, red, purple", "September - October",
  "Z2 - Z8", "stoloniferous", "160 cm", "average", "full sun", "suitable for cutting", "北米東部"),
 (["A20", "A21"], "ASTER novi-belgii (SYMPHYOTRICHUM)", "species", "North America", "blue, pink and white", "September - October", "Z2 - Z8", None,
  "140 cm", "average", "full sun", "suitable for cutting", "北米"),
 (["A22"], "ASTER tataricus (CRINITARIA)", "species", None, "lavender blue", "September - November", "Z3 - Z8", None, "140 cm", "average", "full sun",
  "medicinal plant; honey-bee food plant", None),
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes 36 Asters（https://www.chicagobotanic.org/downloads/planteval_notes/no36_asters.pdf）の Table 1。試験地は USDA 5b。
# 総合評価は星5つ（excellent）〜1つ（very poor）。うどんこ病・さび病は、かかった割合で excellent（なし）〜very poor（76%超）。
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {
 "A02": ("Symphyotrichum cordifolium 'Ideal'", "cultivar", 60, 35, None, None, None, "総合評価 ★3（fair）。うどんこ病への強さ excellent、さび病への強さ poor"),
 "A03": ("Eurybia divaricata", "species", 24, 46, None, None, None, "総合評価 ★5（excellent）。うどんこ病・さび病とも excellent（発生なし）"),
 "A07": ("Symphyotrichum novi-belgii 'Schneekissen'", "cultivar", 10, 16, None, None, None, "総合評価 ★3（fair）。うどんこ病 excellent、さび病 good"),
 "A12": ("Symphyotrichum 'Little Carlow'", "cultivar", 31, 23, None, None, None, "総合評価 ★2（poor）。うどんこ病 good、さび病 very poor（76%超がかかった）"),
 "A16": ("Symphyotrichum novae-angliae 'Purple Dome'", "cultivar", 16, 24, None, None, None, "総合評価 ★3（fair）。うどんこ病 fair、さび病 excellent"),
 "A17": ("Symphyotrichum novae-angliae 'Septemberrubin'", "cultivar", 45, 54, None, None, None,
         "総合評価 ★2（poor）。うどんこ病 very poor（76%超がかかった）、さび病 excellent"),
 "A20": ("Symphyotrichum novi-belgii 'Professor Anton Kippenberg'", "cultivar", 11, 26, None, None, None,
         "総合評価 ★2（poor）。うどんこ病 excellent、さび病 very poor（76%超がかかった）"),
 "A23": ("Doellingeria umbellata", "species", 60, 55, None, None, None, "総合評価 ★4（good）。うどんこ病・さび病とも excellent（発生なし）"),
}
# 報告にあるが別の品種: Aster tataricus 'Jindai'（★5）。マスターの A22 は品種名なしのシオンなので使っていない。
