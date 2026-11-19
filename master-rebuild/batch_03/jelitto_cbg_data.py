# Jelitto（s11）とシカゴ植物園（s08）: フロックス・ペルシカリア・サルビア。
# Jelitto は 2026-11-19 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ（アプリ内のブラウザーでは確認画面から進まなかった）。
# 探し方: 英語のサイト内検索 index.php?lang=0&cl=search&searchparam=<名前>（Phlox・Persicaria・Bistorta・Polygonum・Salvia nemorosa／pratensis／superba／officinalis／verticillata）。
#   一致は11ページ。宿根フロックスは品種混合の種子だけ、アンプレクシカウリス・アフィニスは掲載なし。
#   'Merleau' は 'Merleau Compact Blue／Rose／White' という別の商品しかないので使っていない。
# バレエシリーズ（'Rose Rhapsody' 2005、'Sweet Esmeralda'・'Twilight Serenade' 2008、'Sky Dance' 2014）は Jelitto が発表した品種（育種会社 s12 と同じ扱いにできる）。
# 'Madeline' はページがなく、プラテンシス（種）のページを当てた。日照の欄は記号で、文字として読めなかった。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-19"
_PRO = "The species is native to Europe, Caucasus, Ukraine: calcareous nutrient poor grassland, dry meadows, slopes."
_PRJ = "ヨーロッパ・コーカサス・ウクライナの、石灰質でやせた草地・乾いた草原・斜面（種の原産地）"
_BAL = "Dense flower heads, rich flowering. Reblooms after dead heading, September - October. honey-bee food plant / suitable for cutting"
JELITTO = [
 (["F19"], "PHLOX pilosa", "species", None, "purple-pink", "April - June", "Z4 - Z7", "", "30 cm", "well-drained / average", "", "Rich flowering. for the rock garden", None),
 (["R17"], "POLYGONUM virginianum", "species", None, "red", "July - August", "Z4 - Z9", "", "50 cm", "average", "", "ornamental foliage plant; for the rock garden", None),
 (["S06"], "SALVIA officinalis", "species", None, "lilac", "June - August", "Z4 - Z10", "", "50 cm", "dry / well-drained", "",
  "Herb of the Year 2003 in Germany. Aromatic. medicinal plant / beneficial plant / tea herb / culinary herb; honey-bee food plant", None),
 (["S07"], "SALVIA pratensis", "species", "Europe, Caucasus, Ukraine: calcareous nutrient poor grassland, dry grassland, slopes.", "blue", "June - August", "Z3 - Z8",
  "erect / rosettes-forming / clumping / bushy", "60 cm", "dry", "", "culinary herb; honey-bee food plant", "ヨーロッパ・コーカサス・ウクライナの、石灰質でやせた草地・乾いた草原・斜面"),
 (["S08"], "SALVIA pratensis Ballet-Series 'Rose Rhapsody'", "cultivar", _PRO, "pale pink shades", "June - August", "Z3 - Z8", "cushion-forming", "50 cm", "dry", "",
  "Introduced by JELITTO PERENNIAL SEEDS in 2005. " + _BAL, _PRJ),
 (["S09"], "SALVIA pratensis Ballet-Series 'Sky Dance'", "cultivar", _PRO, "light blue", "June - August", "Z3 - Z8", "cushion-forming / rosettes-forming", "50 cm", "dry / rocky", "",
  "Introduced by JELITTO PERENNIAL SEEDS in 2014. Dense flower heads, reblooms after dead heading, September - October. honey-bee food plant / suitable for cutting", _PRJ),
 (["S10"], "SALVIA pratensis Ballet-Series 'Sweet Esmeralda'", "cultivar", "Europe", "intensive dark pink", "June - August", "Z3 - Z8", "cushion-forming / rosettes-forming", "50 cm", "dry", "",
  "Introduced by JELITTO PERENNIAL SEEDS in 2008. " + _BAL, "ヨーロッパ（種の原産地）"),
 (["S11"], "SALVIA pratensis Ballet-Series 'Twilight Serenade'", "cultivar", "Europe", "blue-violet", "June - August", "Z3 - Z8", "cushion-forming / rosettes-forming", "50 cm", "dry", "",
  "Introduced by JELITTO PERENNIAL SEEDS in 2008. " + _BAL, "ヨーロッパ（種の原産地）"),
 # マスターは 'Queen Blue'。'Blaukönigin'（Blue Queen）として当てた
 (["S12"], "SALVIA nemorosa 'Blaukönigin'", "cultivar", "Cultivar. Europe, Asia, Middle East: dry meadows, slopes, roadsides.", "blue-violet", "May - September", "Z4 - Z8",
  "clumping / bushy", "40 cm", "dry / well-drained / average", "", "groundcover; honey-bee food plant / suitable for cutting", "ヨーロッパ・アジア・中東の乾いた草地・斜面・道ばた（種の原産地）"),
 (["S13"], "SALVIA nemorosa 'Violettkönigin'", "cultivar", "Europe, Asia, Middle East: nutrient poor grasslands, slopes, forest margins.", "violet", "May - September", "Z4 - Z8",
  "clumping / bushy", "60 cm", "dry / well-drained / average", "", "Perennial Plant of the Year 1997 in Sweden. groundcover; honey-bee food plant / for the rock garden",
  "ヨーロッパ・アジア・中東のやせた草地・斜面・林縁（種の原産地）"),
 (["S16"], "SALVIA verticillata", "species", None, "lilac-blue", "July - September", "Z4 - Z8", "", "50 cm", "dry", "", "", None),
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes（試験地は USDA 5b）。pdftotext -raw で表を読んだ。総合評価の星は記号で、文字として取り出せなかった。
#   no35 A Comparative Study of Phlox paniculata Cultivars（https://www.chicagobotanic.org/downloads/planteval_notes/no35_phloxpaniculata.pdf）Table 2
#   no13 Phlox（https://www.chicagobotanic.org/downloads/planteval_notes/no13_phlox.pdf）Table 1 … 'David' とピローサ
#   no14 Sage（https://www.chicagobotanic.org/downloads/planteval_notes/no14_sage.pdf）Table 1
#   ペルシカリアの号はない（一覧 https://www.chicagobotanic.org/collections/ornamental_plant_research/plant_evaluation で確認）
# うどんこ病への強さ: excellent＝発生なし、good＝25%未満、fair＝26〜50%、poor＝51〜75%。ハダニ: low＝25%未満、moderate＝26〜50%
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in（幅のあるものは (下限, 上限)）, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {
 "F05": ("paniculata 'Blue Paradise'", "cultivar", 34, 28, None, None, None,
         "うどんこ病への強さ good（25%未満）、ハダニ low。草姿は毎年ゆるく不揃いで、葉の斑点病で下葉が落ちやすかった（no35）"),
 "F08": ("paniculata 'David'", "cultivar", (34, 49), (29, 40), None, None, None, "うどんこ病への強さ fair（26〜50%）（no13）"),
 "F09": ("paniculata 'Harlequin'", "cultivar", 31, 18, None, None, None,
         "うどんこ病への強さ good（25%未満）、ハダニ low。斑入りの品種はどれも晩夏に葉焼け（sunscald）がよく出た（no35）"),
 "F14": ("paniculata 'Laura'", "cultivar", 29, 26, None, None, None, "うどんこ病への強さ good（25%未満）、ハダニ low（no35。'Uspekh' は別の行で載っている）"),
 "F15": ("paniculata 'Norah Leigh'", "cultivar", 34, 22, None, None, None,
         "うどんこ病への強さ good（25%未満）、ハダニなし。花つきは 40〜60%。斑入りの品種はどれも晩夏に葉焼け（sunscald）がよく出た。斑の消えた茎（先祖返り）が珍しくなかった（no35）"),
 "F16": ("paniculata 'Red Riding Hood'", "cultivar", 36, 34, None, None, None, "うどんこ病への強さ good（25%未満）、ハダニ low（no35）"),
 "F19": ("pilosa", "species", (10, 12), (32, 36), None, None, None,
         "うどんこ病への強さ excellent（葉の病気は見られなかった）。花つきは毎年多いが、花後は草姿が開いて乱れ、最終評価は fair（no13）"),
 "S12": ("× sylvestris 'Blaukönigin'（'Blue Queen'）", "cultivar", (18, 24), (28, 36), None, None, None,
         "こぼれ種の苗あり、冬の傷みなし。花つきは 40〜60%。多くの年で6月下旬までに株の中心が開いて倒れた（no14。マスターの品種名は 'Queen Blue'）"),
 "S14": ("× sylvestris 'Mainacht'（'May Night'）", "cultivar", (27, 30), (28, 36), None, None, None,
         "× sylvestris の品種の中で最も成績が良かった（花つき・草姿・耐寒性とも高評価）。こぼれ種の苗なし、冬の傷みなし。花後に地際で切ると見た目は整うが、花数は増えなかった（no14）"),
 "S16": ("verticillata 'Purple Rain'", "cultivar", (20, 26), (32, 38), None, None, None,
         "最も良かったサルビアの一つ（花つき・草姿・耐寒性とも高評価）。返り咲きが最も多く、草姿が季節を通して崩れにくかった。こぼれ種の苗なし、冬の傷みなし（no14）"),
}
