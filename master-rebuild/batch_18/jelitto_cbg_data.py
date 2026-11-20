# Jelitto（s11）とシカゴ植物園（s08）: 在庫のない1品種の属19（アゲラティナからバレリアナまで）。batch_18/input の19属。
# Jelitto は 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。17個目のまとまり（batch_17）の分と同じときに続けて読んだ
#   （探し方・読み方は batch_17/jelitto_cbg_data.py と batch_17/gaissmayer_data.py の冒頭）。
#   英語のサイト内検索: 属名19個と Eupatorium rugosum・Epilobium・Chamaenerion。Chamerion・Convallaria・Oenanthe・Prostanthera は 0件。一致は14ページ。このまとまりの間は確認画面は出なかった。
# Jelitto の書き方（角かっこは流通名・別名）: 'Chocolate' の品種のページはなく、種の EUPATORIUM rugosum (AGERATINA altissima) だけ、アンテミスは ANTHEMIS tinctoria 'Alba' (COTA)、
#   ヤナギランは EPILOBIUM angustifolium (CHAMAENERION)、ミツバシモツケは GILLENIA trifoliata (PORTERANTHUS)、コエレリアは KOELERIA glauca [Coolio, Blue Sprite]、
#   テンニンソウの黄金葉は LEUCOSCEPTRUM japonicum f. aureum (ELSHOLTZIA, COMANTHOSPHACE) [Golden Angel]〔マスターと同じ f. aureum。流通名に Golden Angel〕、
#   オルラヤは ORLAYA grandiflora [White Lace, White Finch]（Life Cycle: Biennial）、ロシアンセージは PEROVSKIA atriplicifolia (SALVIA yangii)、
#   クリーピングセボリーは SATUREJA spicigera (repanda)、セリナムは SELINUM wallichianum (tenuifolium)(CORTIA)。
# Jelitto が発表した品種（Historical の欄。育種会社 s12 と同じ扱いにできる）: アンテミス ティンクトリア 'Alba'（2006）。
# 種のページを当てたもの: ユーパトリウム ルゴサム（Af01 'Chocolate'）。
#   当てていないもの: セラスチウム トメントサム（var. columnae の品種 'Celine'・'Silberteppich' だけ）、スズラン、コリダリス 'Silver Spectre'、セリ、プロスタンテラ（掲載なし）。
# 日照の欄（Location）は記号で読めなかった。
# Jelitto の「Heat and drought resistant」（ロシアンセージ）、土の欄の「warm」（コエレリア）は暑さに関わる記述だが、Jelitto は耐暑性の判定に使わない（記録だけ）。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-20"
JELITTO = [
 (["Af01"], "EUPATORIUM rugosum (AGERATINA altissima)", "species", None, "white", "July - September", "Z4 - Z8", "", "90 cm", "moist / average", "", "toxic plant", None),
 (["Tn01"], "ANTHEMIS tinctoria 'Alba' (COTA)", "cultivar", "Europe to Iran", "white", "July - September", "Z3 - Z7", "clumping", "40 cm", "dry / well-drained / poor, lean", "",
  "Pure white daisies and lovely dissected foliage. Introduced by JELITTO PERENNIAL SEEDS in 2006. "
  "culinary herb; honey-bee food plant / for the rock garden / suitable for cutting", "ヨーロッパからイラン（種の原産地）"),
 (["Cp01"], "CEPHALARIA gigantea", "cultivar", "Caucasus to Sibirica", "light yellow", "June - August", "Z4 - Z7", "erect", "200 cm", "well-drained / average", "",
  "Lovely, light-yellow colored scabiosa-like blooms on tall stems. Attracts honeybees. honey-bee food plant / suitable for cutting", "コーカサスからシベリア"),
 (["Cj01"], "EPILOBIUM angustifolium (CHAMAENERION)", "cultivar", "Northern parts of northern hemisphere: wastelands, riverbanks, roadsides.", "lilac-rose",
  "June - September", "Z2 - Z7", "stoloniferous", "110 cm", "moist / average", "",
  "Epilobium angustifolium can form large numbers on difficult areas. Fast propagation due to underground runners and seeds. Very beautiful inflorescences, especially in large groups. "
  "Attractive for butterflies and other pollinators. Suitable for natural landscaping. Use for low maintenance plantings. Erosion control. Tolerates temporary inundation by water. "
  "medicinal plant / beneficial plant / tea herb / culinary herb; honey-bee food plant", "北半球の北部の荒れ地・川岸・道ばた"),
 (["Gi01"], "GILLENIA trifoliata (PORTERANTHUS)", "cultivar", None, "white, calyx reddish", "June - July", "Z3 - Z7", "", "80 cm", "well-drained / average", "",
  "Award of Garden Merit (RHS). medicinal plant", None),
 (["Gb01"], "GLOBULARIA trichosantha", "cultivar", None, "bright blue", "May - June", "Z5 - Z9", "stoloniferous / mat-forming", "20 cm", "well-drained / average", "",
  "for the rock garden", None),
 (["Ko01"], "KOELERIA glauca [Coolio, Blue Sprite]", "cultivar", "Central Europe to West Asia", "", "May - July", "Z3 - Z8", "round / clumping / compact / wintergreen", "25 cm",
  "dry / well-drained / poor, lean / warm", "", "Foliage: narrow, blue. ornamental foliage plant / groundcover; for the rock garden", "中央ヨーロッパから西アジア"),
 (["Ls01"], "LEUCOSCEPTRUM japonicum f. aureum (ELSHOLTZIA, COMANTHOSPHACE) [Golden Angel]", "cultivar", None, "white", "July - September", "Z4 - Z8", "", "50 cm", "average", "",
  "White spikes, precious ornamental foliage plant. Foliage: vigorous golden green. ornamental foliage plant", None),
 (["Ol01"], "ORLAYA grandiflora [White Lace, White Finch]", "cultivar", "Europe, Morth Africa to Central Asia: meadows, fields.", "white", "June - September", "Z5 - Z9", "graceful",
  "60 cm", "dry / average", "",
  "Life Cycle: Biennial. Magnificent white umbels with large white outer blossoms, shortlived but outstanding. Suitable for natural landscaping. "
  "Attractive for butterflies and other pollinators. Moderate self-sowing at suitable locations. Long blooming. Easy to grow. "
  "culinary herb / groundcover; honey-bee food plant / suitable for cutting", "ヨーロッパ・北アフリカから中央アジアの草地・畑"),
 (["Pg01"], "PEROVSKIA atriplicifolia (SALVIA yangii)", "cultivar", None, "heavenly blue", "July - September", "Z4 - Z8", "bushy / richly branched", "120 cm",
  "dry / well-drained / average", "", "Variable. Perennial Plant of the Year 1995 in North America. Heat and drought resistant. suitable for cutting", None),
 (["Sj01"], "SATUREJA spicigera (repanda)", "cultivar", None, "white", "August - November", "Z6 - Z9", "stoloniferous / wintergreen", "20 cm", "dry / average", "",
  "Rich flowering, attractive late flowering groundcover. Foliage: aromatic. medicinal plant; for the rock garden", None),
 (["Sx01"], "SELINUM wallichianum (tenuifolium)(CORTIA)", "cultivar", "Kashmir, India and Pakistan", "white", "June - August", "Z6 - Z9", "erect / clumping", "120 cm",
  "well-drained / average", "",
  "White flat-topped umbels on red stems with fine fern-like foliage. ornamental foliage plant / groundcover; suitable for cutting", "カシミール・インド・パキスタン"),
 (["Sb01"], "SPOROBOLUS heterolepis", "cultivar", None, "", "July - September", "Z4 - Z9", "clumping / graceful", "60 cm", "dry / average / poor, lean", "",
  "Silvery flower panicles, fine textured foliage clumps with reddish fall-colour. suitable for cutting", None),
 (["Va01"], "VALERIANA officinalis", "cultivar", "Europe, Asia: mountain meadows, damp meadows, river banks.", "white to pale pink", "May - September", "Z3 - Z9", "erect", "100 cm",
  "moist / average", "", "medicinal plant / tea herb / culinary herb; honey-bee food plant", "ヨーロッパ・アジアの山の草地・湿った草地・川岸"),
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes（試験地は USDA 5b）。pdftotext -raw で読んだ。
#   no37 Joe-Pye Weeds and Their Relatives（https://www.chicagobotanic.org/downloads/planteval_notes/no37_joepyeweed.pdf）Table 3 と本文。
#     Ageratina altissima 'Chocolate' が入っている。総合評価は星5つ（excellent）〜1つ（very poor）。日なたの試験区。
#   ほかの18属を題にした号は一覧（no1〜no40）にない。
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {
 "Af01": ("Ageratina altissima 'Chocolate'", "cultivar", 36, 36, None, None, None,
          "総合評価 ★5（excellent。26種類のうち最高評価の4つの1つ）。花は白、花つき excellent、花期は9月上旬〜10月下旬、うどんこ病への強さ excellent。"
          "濃い紫の葉は、季節の終わりには緑（裏は紫）に褪せた。毎年、株はそろって丈夫で花つきが多かった。"
          "夏のいちばん暑い日や土が乾いたときは、しおれることが多かった。試験区でこぼれ種で増えたが、雑草になるほどではなかった。"
          "同じ試験区で、種そのもの（緑葉）は弱く、ほとんどの年に冬に枯れる株が出た（総合評価 ★2）（no37）"),
}
