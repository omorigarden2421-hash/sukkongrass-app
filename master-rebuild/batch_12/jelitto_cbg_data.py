# Jelitto（s11）とシカゴ植物園（s08）: シレネ・ゲンチアナ・プルサティラ・ティアレラ・アルケミラ・アンドロポゴン・ヘデラ・リグラリア・パトリニア・プルネラ・トリキルティス・ハイドランジア・アストランティア。
# Jelitto は 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_11/jelitto_cbg_data.py と同じ
#   （英語のサイト内検索: Silene 38件・Silene uniflora 2件・Gentiana 61件〔paradoxa・septemfida でも検索〕・Pulsatilla vulgaris 16件・Tiarella 3件・Alchemilla 16件・Andropogon 9件・
#     Schizachyrium 5件・Ligularia 5件・Patrinia 4件・Prunella 11件・Tricyrtis 9件・Astrantia 3件・Hydrangea 0件・Hedera 該当なし）。一致は27ページ。6秒おき。
#   最初の検索で確認画面が出たが、操作せずに Gaißmayer を先に読んでいる間に自動で通った。そのあとは出なかった。
# Jelitto の書き方（角かっこは流通名・別名）: 'Nikita' は GENTIANA dahurica [Nikita]、'Pearl Bells' は PULSATILLA vulgaris 'Perlen Glocke' [Pearl Bells]、
#   'Rose Bells' は 'Rosen Glocke' [Rose Bells]、'White Bells' は 'Alba' [Weiße Glocke, White Bells, White Swan]、'Robin Whitebreast' は SILENE uniflora 'Weißkehlchen' [Icecups, Robin White Breast]、
#   'Orange Queen' は LIGULARIA dentata [Orange Queen] (clivorum)、アンドロポゴン スコパリウスは ANDROPOGON scoparius (SCHIZACHYRIUM)、タイワンホトトギスは TRICYRTIS formosa、
#   ティアレラ ウェリーは TIARELLA wherryi [Silverado, Sugar Scoop] (cordifolia ssp. collina)、アルケミラ モリスは ALCHEMILLA mollis [Thriller, Irish Silk]。
# Jelitto が発表した品種（Historical の欄。育種会社 s12 と同じ扱いにできる）: ゲンチアナ 'Blue Herald'（1989）・'Blue Cross'（2009）・'Bella Alpinella'（2018）、
#   プルサティラ 'Perlen Glocke'（2010）・'Rosen Glocke'（2014）。
# 種のページを当てたもの: シレネ ディオイカ（Si01）、リグラリア デンタータ（Lg01）、オミナエシ（Pt02）、プルネラ グランディフローラ（Pv01）、タイワンホトトギス（Tc01）、ホトトギス（Tc02）、
#   アストランティア マヨール（As01〜As06）。
#   当てていないもの: シレネ ユニフローラのほかの品種、ティアレラの交配品種、プルネラ 'Bella Blue'（'Freelander Blue' は別の品種）、'Tojen'、ヘデラ・ハイドランジア（掲載なし）。
# 'Blue Cross'・'Prairie Blues' のページは本文が長く、表の後半（土など）が途中までしか読み取れなかった。日照の欄（Location）は記号で読めなかった。
# Jelitto の「Full sun in cool summer climates to semi-shade elsewhere」（ゲンチアナ ダフリカ、リグラリア）は暑さに関わる記述だが、Jelitto は耐暑性の判定に使わない（記録だけ）。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-20"
_PUO = "Europe, Great Britain and Western France to Sweden, east to Ukraine."
_PUJ = "ヨーロッパ（イギリス・フランス西部からスウェーデン、東はウクライナ）（種の原産地）"
_PUU = "honey-bee food plant / for the rock garden / flowering pot plant"
_PUS = "Beautiful large flowering, bell-shaped flowers that resemble little anemones. Reliable early spring flowering. Drought resistant. "
_LIG = ("LIGULARIA dentata [Orange Queen] (clivorum)", "China and Japan", "orange-yellow", "July - September", "Z3 - Z8", "clumping", "100 cm", "moist / humus rich, fertile", "",
        "Large, decorative foliage and orange-yellow blooms. Easy from seed. Full sun in cool summer climates to semi-shade elsewhere.", "中国と日本（種の原産地）")
_PAT = ("PATRINIA scabiosifolia", None, "yellow", "July - August", "Z5 - Z8", "", "70 cm", "average", "",
        "Flower umbels. TCM plant. medicinal plant / culinary herb / groundcover; honey-bee food plant / suitable for cutting", None)
JELITTO = [
 (["Si01"], "SILENE dioica (MELANDRIUM rubrum)", "species", None, "light purple-red", "May - September", "Z5 - Z8", "clumping", "80 cm", "moist / average", "", "", None),
 (["Si03"], "SILENE uniflora 'Weißkehlchen' [Icecups, Robin White Breast] (maritima)", "cultivar", None, "white", "June - August", "Z3 - Z8", "", "20 cm", "well-drained / average", "",
  "Abundant flowering. First year flowering. Flower: single. groundcover; for the rock garden / flowering pot plant", None),
 (["Gn01"], "GENTIANA cruciata 'Blue Cross'", "cultivar", "Cultivar. Species is native to Europe, Asia Minor, Caucasus and Siberia: mountain areas, meadows, forest margins.",
  "bright dark blue", "July - September", "Z3 - Z7", "rosettes-forming / clumping", "25 cm", "dry / gritty", "",
  "Beautiful intense blue-violet blooms on compact durable, drought resistant plants. Very rich blooming, sturdy and upright flower stems. pH-tolerant. Cut flower. "
  "Introduced by JELITTO PERENNIAL SEEDS in 2009.", "ヨーロッパ・小アジア・コーカサス・シベリアの山地、草地、林のふち（種の原産地）"),
 (["Gn02"], "GENTIANA dahurica [Nikita]", "cultivar", "China, Mongolia and Siberia", "deep blue", "June - July", "Z3 - Z7", "stoloniferous / cushion-forming", "35 cm",
  "moist / well-drained / average", "",
  "Clusters of deep blue tubular blooms all along the leaf axils. Grows easily. Full sun in cool summer climates to semi-shade elsewhere. More flexibel pH than most other GENTIANA. "
  "for the rock garden / suitable for cutting", "中国・モンゴル・シベリア"),
 (["Gn03"], "GENTIANA paradoxa 'Blue Herald'", "cultivar", None, "bright blue", "August - September", "Z3 - Z8", "cushion-forming", "15 cm", "moist / well-drained / average / cool", "",
  "Excellent fall flowering gentian, very vigorous. First year flowering. Introduced by JELITTO PERENNIAL SEEDS in 1989. for the rock garden / suitable for cutting / flowering pot plant", None),
 (["Gn04"], "GENTIANA septemfida var. lagodechiana 'Bella Alpinella'", "cultivar", "Caucasus: mountain pastures, rocky areas.", "brilliant blue", "July - September", "Z3 - Z7",
  "cushion-forming / compact", "10 cm", "well-drained / average", "",
  "Short stems, forming compact cushions, fantastic summer gentian. Abundant and long lasting flowering. Uncomplicated rock garden plant on well drained soil. "
  "Introduced by JELITTO PERENNIAL SEEDS in 2018. for the rock garden / suitable for cutting / flowering pot plant", "コーカサスの山の放牧地、岩場（種の原産地）"),
 (["Ps01"], "PULSATILLA vulgaris (ANEMONE)", "cultivar", None, "lilac to blue-violet", "March - April", "Z5 - Z8", "clumping", "30 cm", "dry / well-drained / alkaline", "",
  "Award of Garden Merit (A.G.M.). Plant of the Year 1996 in Germany. decorative fruit / toxic plant / medicinal plant; " + _PUU, None),
 (["Ps02"], "PULSATILLA vulgaris 'Perlen Glocke' [Pearl Bells] (ANEMONE)", "cultivar", "Species occurs in " + _PUO, "softest pink", "March - April", "Z5 - Z8", "clumping", "30 cm",
  "dry / well-drained / alkaline", "", _PUS + "Introduced by JELITTO PERENNIAL SEEDS in 2010. decorative fruit; " + _PUU, _PUJ),
 (["Ps03"], "PULSATILLA vulgaris 'Rosen Glocke' [Rose Bells] (ANEMONE)", "cultivar", "Species originates from " + _PUO, "radiant cerise pink", "March - April", "Z5 - Z8", "clumping", "30 cm",
  "dry / well-drained / alkaline", "", _PUS + "Introduced by JELITTO PERENNIAL SEEDS in 2014. decorative fruit; " + _PUU, _PUJ),
 (["Ps04"], "PULSATILLA vulgaris 'Alba' [Weiße Glocke, White Bells, White Swan] (ANEMONE)", "cultivar", _PUO, "white", "March - April", "Z5 - Z8", "clumping", "30 cm",
  "dry / well-drained / alkaline", "",
  "Award of Garden Merit (A.G.M.). Large blossoms. Reliable early spring flowering, drought tolerant. decorative fruit; " + _PUU, _PUJ),
 (["Ti04"], "TIARELLA wherryi [Silverado, Sugar Scoop] (cordifolia ssp. collina)", "cultivar", None, "white with pink touch", "May - June", "Z4 - Z8", "stoloniferous", "20 cm",
  "avoid lime / average", "", "Award of Garden Merit (A.G.M.). Delicately fragrant. groundcover; for the rock garden", None),
 (["Al01"], "ALCHEMILLA mollis [Thriller, Irish Silk]", "cultivar", "Caucasus to Southern and Eastern Europe", "yellowish", "June - July", "Z3 - Z8", "", "50 cm",
  "average / humus rich, fertile / loamy", "",
  "Award of Garden Merit (A.G.M.). Foliage: simple, orbicular, serrated, finely hairy, gray-green. groundcover; suitable for cutting", "コーカサスから南ヨーロッパ・東ヨーロッパ"),
 (["Al02"], "ALCHEMILLA saxatilis", "cultivar", "High Pyrenees", "yellow", "June - August", "Z3 - Z8", "stoloniferous / cushion-forming", "15 cm", "well-drained / average", "",
  "Scalloped dark green leaves with an striking silver edge. Grows in non-alpine conditions better than A. alpina which is almost identical. ornamental foliage plant / groundcover",
  "ピレネー山脈の高地"),
 (["Al03"], "ALCHEMILLA sericata 'Gold Strike'", "cultivar", "Mediterranean to Caucasus", "greenish-yellow", "June - August", "Z3 - Z8", "cushion-forming", "35 cm", "moist / average", "",
  "Free flowering, bright chartreuse flowering umbels and velvety gray-green, scalloped foliage. More deeply lobed leaves than A.mollis, robust, compact and consistant habit. "
  "Thick weed-choking mounds. First year flowering. ornamental foliage plant / groundcover; for the rock garden / suitable for cutting", "地中海沿岸からコーカサス（種の原産地）"),
 (["Ad01"], "ANDROPOGON gerardii", "cultivar", None, "", "August - October", "Z3 - Z8", "erect", "150 cm", "dry / moist / well-drained / average", "",
  "Red tinged stalks. solitary plant; suitable for cutting", None),
 (["Ad02"], "ANDROPOGON scoparius 'Blaze' (SCHIZACHYRIUM)", "cultivar", "Selection. Eastern North America: prairie, grasland.", "silver", "August - October", "Z3 - Z9", "", "100 cm",
  "dry / well-drained", "",
  "Silvery spikes, sturdy selection with nice fall and winter colours. Deer resistant. Low maintenance plantings. Once established drought tolerant. "
  "Foliage: green, reddish fall and winter colours. ornamental foliage plant; suitable for cutting", "北アメリカ東部の草原（種の原産地）"),
 (["Ad03"], "ANDROPOGON scoparius 'Prairie Blues' (SCHIZACHYRIUM)", "cultivar", "North America and Northern Mexico", "silvery", "August - October", "Z3 - Z9", "erect", "100 cm", "", "",
  "Exquisite grey-blue, ribbon-like foliage with reddish-orange autumnal colors. Silvery fluffy seed heads, Outstanding for naturalizing. Deer resistant. "
  "Once established drought tolerant. Foliage: thin, ribbon-like, greyish-blue, reddish-orange fall color.", "北アメリカとメキシコ北部（種の原産地）"),
 (["Lg02"], _LIG[0], "cultivar") + _LIG[1:],
 (["Lg01"], _LIG[0], "species") + _LIG[1:],
 (["Lg03"], "LIGULARIA przewalskii", "cultivar", "Yunnan, Sichuan and Gansu provinces in Northwest China", "yellow", "July - September", "Z4 - Z8", "erect / clumping", "120 cm", "moist", "",
  "Award of Garden Merit (A.G.M.). Elegant combination with distinct, palmate leaves and dark, erect flowering stems dotted with yellow blossom racemes. Adaptable to moist soils. "
  "Full sun in cool summer climates to semi-shade elsewhere.", "中国北西部の雲南・四川・甘粛"),
 (["Pt01"], _PAT[0], "cultivar") + _PAT[1:],
 (["Pt02"], _PAT[0], "species") + _PAT[1:],
 (["Pt03"], "PATRINIA villosa", "cultivar", None, "white", "July - August", "Z5 - Z8", "", "70 cm", "average", "",
  "Flower umbels. Foliage: feathered. medicinal plant / culinary herb / groundcover; honey-bee food plant / suitable for cutting", None),
 (["Pv01"], "PRUNELLA grandiflora", "species", None, "violet-blue", "June - August", "Z4 - Z8", "stoloniferous / repent", "20 cm", "dry / poor, lean", "",
  "Abundant flowers. First year flowering. medicinal plant / tea herb / culinary herb / groundcover; honey-bee food plant", None),
 (["Pv02"], "PRUNELLA grandiflora 'Rubra'", "cultivar", None, "carmine-red", "June - August", "Z4 - Z8", "stoloniferous", "20 cm", "dry", "", "First year flowering. groundcover", None),
 (["Pv03"], "PRUNELLA vulgaris", "cultivar", None, "violet", "June - September", "Z3 - Z8", "stoloniferous", "20 cm", "moist / average", "",
  "medicinal plant / groundcover; honey-bee food plant", None),
 (["Tc01"], "TRICYRTIS formosa", "species", None, "lilac pink, spotted", "August - October", "Z4 - Z8", "stoloniferous", "60 cm", "moist", "", "suitable for cutting", None),
 (["Tc02"], "TRICYRTIS hirta", "species", None, "soft lilac with large purple spots", "August - October", "Z4 - Z8", "stoloniferous", "50 cm", "average", "", "suitable for cutting", None),
 (["As01", "As02", "As03", "As04", "As05", "As06"], "ASTRANTIA major", "species", "Central and East Europe", "white, pink veined", "June - August", "Z5 - Z7", "", "60 cm",
  "moist / average", "", "Perennial Plant of the Year 2005 in Sweden. honey-bee food plant / suitable for cutting", "中央ヨーロッパ・東ヨーロッパ（種の原産地）"),
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes（試験地は USDA 5b）。pdftotext -raw で読んだ。
#   no24 Lady's mantles（https://www.chicagobotanic.org/downloads/planteval_notes/no24_alchemilla.pdf）Table と本文。総合評価: 星4つ＝good、3つ＝fair。
#     花の見ばえ（花色の持ちと花の量）: excellent 76〜100%、good 51〜75%、fair 26〜50%。'Gold Strike'・セリカータは試験に入っていない。
#   no16 Toad lilies（no16_tricyrtis.pdf）Table 1 と本文。総合評価の星は記号が落ちて読めなかった。'Gilt Edge'・'Lightning Strike' は試験に入っていない
#     （タイワンホトトギスの種そのものは excellent の評価だが、品種の Tc01 には当てていない）。
#   ほかの属（シレネ・ゲンチアナ・プルサティラ・ティアレラ・アンドロポゴン・ヘデラ・リグラリア・パトリニア・プルネラ・ハイドランジア・アストランティア）の号は一覧（no1〜no40）にない。
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {
 "Al01": ("mollis", "cultivar", 15, 30, None, None, None, "総合評価 good（星4つ）。花の見ばえ good。試験した種はどれも寒さに強く、病害虫がなかった、との記述（no24）"),
 "Al02": ("saxatilis", "cultivar", 7, 18, None, None, None,
          "総合評価 fair（星3つ）。花の見ばえ fair。1998年の夏までは健全だったが、その夏に急に衰え、続く冬に全株で株元が傷んだ（no24）"),
 "Tc03": ("'Tojen'", "cultivar", 40, None, None, None, None,
          "草丈 24〜40インチ。花つき low（最盛期の花が40%未満）。花期は8月中旬〜11月初め。炭疽病は出なかった。株は丈夫で勢いがよかった。総合評価の星は読み取れなかった（no16）"),
}
