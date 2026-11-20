# Jelitto（s11）とシカゴ植物園（s08）: ジギタリス・プリムラ・ユーパトリウム・ベルゲニア・カラマグロスティス・デスカンプシア・フクシア・アイリス・ロニセラ。
# Jelitto は 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/jelitto_cbg_data.py と同じ
#   （英語のサイト内検索: Digitalis 46件・Primula 122件〔japonica・denticulata・veris・cortusoides・Lace で絞った〕・Eupatorium 16件・Eutrochium 4件・Bergenia 8件・
#     Calamagrostis 4件・Deschampsia 3件・Fuchsia 5件・Iris 45件・Lonicera 0件）。一致は31ページ。6秒おき。
#   最初の検索で確認画面が出たが、操作せずに Gaißmayer を先に読んでいる間に自動で通った。そのあとは出なかった。
#   商品ページのアドレスは商品ごとに置き場所が違う（/Seed/Perennials/…、/Seed/Ornamental+Grasses/…、/Jelitto+Perennial+Seeds/New+Varieties/… など）。検索結果のリンクから拾う。
# Jelitto の書き方: 'Milk Chocolate' は DIGITALIS parviflora [Milk Chocolate]（種のページに流通名を併記）、'Redstart' は BERGENIA cordifolia 'Rotblum' [Red Beauty, Red Start]、
#   Bg02 は BERGENIA cordifolia 'New Hybrids' [New Winterflowering Hybrids]、'Snow Time' は 'Snowtime'、'Ivory Towers' は EUPATORIUM purpureum var. angustifolium f. albidum 'Ivory Towers'、
#   'Primadiente Rose' は PRIMULA cortusoides hort. 'Primadiente Rose'(TM)、セレスチナムは EUPATORIUM coelestinum (CONOCLINIUM)、フレクシオーサは DESCHAMPSIA flexuosa (AVENELLA)。
#   【要確認】'Elsie Kelsey' は DIGITALIS purpurea 'Pam's Choice' [Elsie Kelsey] と、'Pam's Choice' の別名として載っている。このページを Dg06 に当てた
#   （RHS は 'Elsie Kelsey' を独立した名前として載せ、おぎはらは 'パムズチョイス' を別に載せている）。
# Jelitto が発表した品種（Historical・Origin の欄。育種会社 s12 と同じ扱いにできる）: ジギタリス 'Monstrosa Purple'・'Monstrosa White'（2022）、プリムラ 'Blue Selection'（1994）・
#   'Primadiente Rose'（2014）、ユーパトリウム 'Ivory Towers'（2010）、ベルゲニア 'Rotblum'（1978）・'Snowtime'（2023）、デスカンプシア 'Pixie Fountain'（2010）。
# 種のページを当てたもの: デスカンプシア セスピトーサ（Ds02・Ds03）、フクシア マジェラニカ（Fu02〜Fu05）、アイリス クリソグラフェス（Ir01）・エンサータ（Ir02。日本の新しい交配の混合）・シビリカ（Ir05）。
#   当てていないもの: マートネンシス・'Green Lace'（'Gold Lace' は別の品種）・サンギネア（掲載なし）、ユーパトリウム マクラツムの2品種
#   （EUPATORIUM purpureum var. atropurpureum (maculatum) [Glow] は別の系統）、カラマグロスティス アクティフローラ（不稔で種子がない）、ロニセラ（掲載なし）。
# 日照の欄（Location）は記号で読めなかった。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-20"
_TOX = "toxic plant; honey-bee food plant / suitable for cutting"
_PUR_O = "Western Europe to East Germany: open woodlands, forest margins."
_PUR_J = "西ヨーロッパからドイツ東部の明るい林・林のふち（種の原産地）"
_JAP = "erect / clumping"
_JAPJ = "日本の沢沿い・川沿い（種の原産地）"
_CES = (["Ds02", "Ds03"], "DESCHAMPSIA cespitosa", "species", None, "", "June - September", "Z4 - Z7", "erect / clumping / wintergreen", "150 cm", "moist / average", "",
        "Foliage: green. beneficial plant / groundcover", None)
_FUC = ("FUCHSIA magellanica", None, "scarlet red, puple to pink", "May - September", "Z6 - Z9", "", "90 cm", "average", "",
        "Flowers from July to the first frost, winter hardy as older plant. First year flowering.", None)
JELITTO = [
 (["Dg01"], "DIGITALIS grandiflora", "cultivar", None, "yellow", "June - July", "Z3 - Z8", "", "80 cm", "dry / well-drained / average", "",
  "Award of Garden Merit (A.G.M.). Large yellow bellflowers. Poisonous. toxic plant; suitable for cutting", None),
 (["Dg02"], "DIGITALIS lutea", "cultivar", "Central Europe and Northwest Africa: woodland edges and shrubbery borders.", "light yellow", "June - August", "Z3 - Z9", "wintergreen", "80 cm",
  "well-drained / average", "", "Foliage: lanceolate, finely serrated, rosettes, green. toxic plant / medicinal plant; honey-bee food plant / suitable for cutting",
  "中央ヨーロッパと北西アフリカの林のふち・低木の茂みのふち"),
 (["Dg04"], "DIGITALIS parviflora [Milk Chocolate]", "cultivar", "Northern Spain", "brown-red", "July - September", "Z3 - Z9", "erect", "60 cm", "dry / well-drained / average", "",
  "Sturdy, narrow flowering spikes packed with reddish-brown thimble-shaped flowers. Good cut flower potential, seed stalks for dried flower bouquets. "
  "toxic plant; honey-bee food plant / for the rock garden / suitable for cutting", "スペイン北部"),
 (["Dg05"], "DIGITALIS purpurea 'Apricot' [Sutton's Apricot, A. Delight]", "cultivar", "Cultivar. " + _PUR_O, "yellowish-pink", "June - July", "Z4 - Z8", "erect", "100 cm",
  "dry / well-drained / average", "",
  "Award of Garden Merit (A.G.M.). The pastel colored flowers make an exceptionally decorative accent. Wonderful for naturalizing at the edge of woods where they will easily reseed. " + _TOX, _PUR_J),
 (["Dg06"], "DIGITALIS purpurea 'Pam's Choice' [Elsie Kelsey]", "cultivar", "Garden origin", "creamy white with deep burgundy splotches throads", "June - July", "Z4 - Z8", "erect", "120 cm",
  "dry / well-drained / average", "", "Creamy white bell flowers with very unusual, deep burgundy splotched throats. Outstanding cut flower. " + _TOX, "園芸品種"),
 (["Dg07"], "DIGITALIS purpurea 'Excelsior'", "cultivar", None, "mixture", "June - July", "Z4 - Z8", "", "120 cm", "dry / well-drained / average", "", "Large flowering. " + _TOX, None),
 (["Dg08"], "DIGITALIS purpurea 'Monstrosa Purple'", "cultivar", None, "pink", "June - July", "Z4 - Z8", "evergreen / wintergreen", "120 cm", "dry / well-drained / average", "",
  "Every stem topped with an unusual large single flower. Biennial to short-lived. Introduced by JELITTO PERENNIAL SEEDS in 2022. " + _TOX, None),
 (["Dg09"], "DIGITALIS purpurea 'Monstrosa White'", "cultivar", None, "white", "June - July", "Z4 - Z8", "evergreen / wintergreen", "120 cm", "dry / well-drained / average", "",
  "Every stem topped with an unusual large single flower. Biennial to short-lived. Introduced by JELITTO PERENNIAL SEEDS in 2022. " + _TOX, None),
 (["Dg10"], "DIGITALIS purpurea 'Snow Thimble'", "cultivar", "Western Europe", "pure white", "May - July", "Z4 - Z8", "erect", "100 cm", "well-drained / average", "",
  "The first pure, snow-white flowering seed strain among foxgloves. Completely unblemished by any lavender to purple spots that are so common among other seed strains. toxic plant",
  "西ヨーロッパ（種の原産地）"),
 (["Pr01"], "PRIMULA cortusoides hort. 'Primadiente Rose'(TM)", "cultivar", None, "brilliant pink", "April - May", "Z3 - Z8", "clumping / compact", "20 cm", "moist / average", "",
  "Abundant flowering, compact and vigorous, perfect for container production. Introduced by JELITTO PERENNIAL SEEDS in 2014. for the rock garden / flowering pot plant", None),
 (["Pr02"], "PRIMULA denticulata 'Blue Selection'", "cultivar", "Afghanistan to Southeastern Tibet and Burma", "dark blue", "March - April", "Z4 - Z8",
  "erect / rosettes-forming / clumping", "30 cm", "moist / humus rich, fertile", "",
  "Lovely, dark blue shades on this select seed strain. Early spring flowering. Full sun in cool summer climates to semi-shade elsewhere. "
  "Introduced by JELITTO PERENNIAL SEEDS in 1994. groundcover; for the rock garden", "アフガニスタンからチベット南東部・ミャンマー（種の原産地）"),
 (["Pr03"], "PRIMULA japonica 'Alba' [Postford White]", "cultivar", "Japan", "white", "May - July", "Z4 - Z8", _JAP, "50 cm",
  "moist / boggy / along streamsides / well-drained / humus rich, fertile", "", "Award of Garden Merit (A.G.M.). groundcover; water or marshplant", "日本（種の原産地）"),
 (["Pr04"], "PRIMULA japonica 'Appleblossom'", "cultivar", "The species grows in Japan along streams and rivers.", "soft pink with red eye", "May - July", "Z4 - Z8", _JAP, "50 cm",
  "moist / boggy / along streamsides", "", "groundcover; water or marshplant", _JAPJ),
 (["Pr05"], "PRIMULA japonica 'Millers Crimson'", "cultivar", "The species grows in Japan along streams and rivers.", "intense-red", "May - July", "Z4 - Z8", _JAP, "60 cm",
  "moist / boggy / along streamsides", "", "Award of Garden Merit (A.G.M.). groundcover; water or marshplant", _JAPJ),
 (["Pr07"], "PRIMULA veris (officinalis)", "cultivar", "Europe, Siberia, West and Central Asia", "yellow", "March - May", "Z4 - Z8", "erect / rosettes-forming / clumping", "25 cm",
  "lime-loving, calcareous / average / humus rich, fertile", "",
  "Award of Garden Merit (A.G.M.). toxic plant / medicinal plant / tea herb / culinary herb / groundcover; honey-bee food plant", "ヨーロッパ、シベリア、西アジア・中央アジア"),
 (["Ep02"], "EUPATORIUM coelestinum (CONOCLINIUM)", "cultivar", None, "blue-violet, seldom white", "July - October", "Z6 - Z9", "", "80 cm", "moist / average", "",
  "Bright blue-violet umbels, seldom white. suitable for cutting", None),
 (["Ep03"], "EUPATORIUM purpureum var. angustifolium f. albidum 'Ivory Towers'", "cultivar", "Eastern North America", "ivory-coloured, almost pure white", "July - September", "Z4 - Z8",
  "erect", "200 cm", "moist / average", "",
  "A profusion of late summer blooms terminating in clusters of ivory white flower umbels, grey-green stems. A plant of great architectural merit. "
  "Introduced by JELITTO PERENNIAL SEEDS in 2010. solitary plant; suitable for cutting", "北アメリカ東部（種の原産地）"),
 (["Bg01"], "BERGENIA cordifolia", "cultivar", None, "rosy-red", "March - April", "Z3 - Z8", "stoloniferous / rhizomatous / wintergreen", "60 cm", "well-drained / average", "",
  "ornamental foliage plant / groundcover; honey-bee food plant / for the rock garden / suitable for cutting", None),
 (["Bg02"], "BERGENIA cordifolia 'New Hybrids' [New Winterflowering Hybrids]", "cultivar", None, "soft pink - dark red", "March - May", "Z3 - Z8",
  "stoloniferous / rhizomatous / wintergreen", "45 cm", "well-drained / average", "",
  "ornamental foliage plant / groundcover; honey-bee food plant / for the rock garden / suitable for cutting", None),
 (["Bg03"], "BERGENIA cordifolia 'Rotblum' [Red Beauty, Red Start]", "cultivar", None, "red", "March - May", "Z3 - Z8", "stoloniferous / clumping / rhizomatous / wintergreen", "60 cm",
  "well-drained / average", "",
  "Improved selection with beautiful red fall and winter colour. Outstanding foliage plant for year around appeal. Foliage: mostly evergreen, round, leathery, with undulating edges. "
  "Introduced by JELITTO PERENNIAL SEEDS in 1978. ornamental foliage plant / groundcover; honey-bee food plant / for the rock garden / suitable for cutting", None),
 (["Bg04"], "BERGENIA cordifolia 'Snowtime'", "cultivar", None, "pure white", "March - May", "Z3 - Z8", "", "45 cm", "well-drained / average", "",
  "Pure white flowers in spring and fall, glossy green leaves for floral arrangements. Introduced by JELITTO PERENNIAL SEED in 2023. "
  "ornamental foliage plant; for the rock garden / suitable for cutting", None),
 (["Bg05"], "BERGENIA emeiensis", "cultivar", "China, Sichuan: forests, shaded slopes, rock crevices.", "pink-white", "March - May", "Z6 - Z9", "evergreen", "30 cm",
  "average / humus rich, fertile", "", "Very large flowering, attractive foliage. ornamental foliage plant / groundcover; suitable for cutting", "中国・四川省の森、日陰の斜面、岩の割れ目"),
 (["Cg04"], "CALAMAGROSTIS brachytricha (arundinacea)", "cultivar", "Central to East Asia", "silvery-white tinged with pink", "September - December", "Z4 - Z9", "erect / clumping", "80 cm",
  "dry / well-drained / average / undemanding", "",
  "Award of Garden Merit (A.G.M.). Beautiful large inflorescences in later summer/fall. Drought tolerant and shade loving. Excellent grass for fall-winter interest. suitable for cutting",
  "中央アジアから東アジア"),
 (["Cg05"], "CALAMAGROSTIS epigejos", "cultivar", None, "brown", "July - August", "Z3 - Z9", "stoloniferous", "150 cm", "dry / moist / average", "", "Brown spikes.", None),
 (["Ds01"], _CES[1], "cultivar") + _CES[3:],
 _CES,
 (["Ds04"], "DESCHAMPSIA cespitosa 'Pixie Fountain'", "cultivar", "Europe, Asia and North America", "silver-green to golden-brown", "June - September", "Z2 - Z7",
  "erect / clumping / compact / evergreen / wintergreen", "60 cm", "moist / average", "",
  "Brilliant silver-green, followed by golden-brown flower spikes, compact habit. Forms dense evergreen clumps. Especially cold hardy. Grows even in bogs - over cooler summer regions. "
  "Introduced by JELITTO PERENNIAL SEEDS in 2010. beneficial plant / groundcover; for the rock garden / suitable for cutting", "ヨーロッパ、アジア、北アメリカ（種の原産地）"),
 (["Ds05"], "DESCHAMPSIA flexuosa (AVENELLA)", "cultivar", "Europe, Asia, North and South America temperate zone.", "inflorescence slightly tinged pink", "June - July", "Z4 - Z7",
  "erect / clumping / lax / evergreen / wintergreen", "50 cm", "avoid lime / dry / moist / acidic / average", "",
  "Tolerant of dry shade/part sun. Great for naturalization in a woodland setting. groundcover", "ヨーロッパ、アジア、南北アメリカの温帯"),
 (["Fu01"], _FUC[0], "cultivar") + _FUC[1:],
 (["Fu02", "Fu03", "Fu04", "Fu05"], _FUC[0], "species") + _FUC[1:],
 (["Ir01"], "IRIS chrysographes", "species", "China, Myanmar: forest margins, hillsides, meadows, streamside.", "velvet purple-violet", "", "Z4 - Z9", "rhizomatous", "40 cm", "moist", "",
  "Award of Garden Merit (A.G.M.). Shortly creeping. Tolerates lime.", "中国・ミャンマーの林のふち、丘の斜面、草地、沢沿い（種の原産地）"),
 (["Ir02"], "IRIS ensata(kaempferi)", "species", "China, Japan, Korea, Russia: damp meadows, water edges.", "mixture", "June - July", "Z5 - Z8", "", "60 cm", "boggy", "",
  "Award of Garden Merit (A.G.M.). Newest hybrids from Japan, flowers up to 20 cm, mixture of magnificent colors. water or marshplant", "中国・日本・朝鮮半島・ロシアの湿った草地、水辺（種の原産地）"),
 (["Ir03"], "IRIS pumila wild form", "cultivar", None, "mostly blue, rarely yellow", "April - May", "Z4 - Z8", "", "20 cm", "dry / well-drained / average", "", "for the rock garden", None),
 (["Ir05"], "IRIS sibirica wild form", "species", None, "blue", "June - July", "Z3 - Z9", "erect", "70 cm", "moist / boggy / average", "",
  "Award of Garden Merit (A.G.M.). Plant of the Year 2010 in Germany. water or marshplant", None),
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes no37「A Comparative Study of Joe-Pye Weeds (Eutrochium spp.) and Their Relatives」
#   （https://www.chicagobotanic.org/downloads/planteval_notes/no37_joepyeweed.pdf。試験地は USDA 5b）。pdftotext -raw で Table 3 と本文を読んだ。
#   総合評価: 星5つ＝excellent、4つ＝good、3つ＝fair、2つ＝poor。うどんこ病への強さ: excellent＝発病なし、good＝25%未満、fair＝26〜50%、poor＝51〜75%
#   報告での名前は Conoclinium coelestinum、Eutrochium fistulosum f. albidum 'Ivory Tower'、Eutrochium maculatum 'Gateway'。
#   'Red Dwarf'・フォーチュナイ・アルブムは試験に入っていない。マクラツムの種そのものの記録（5回の冬のうち3回で株元が傷んだ）は、品種の Ep06 には当てていない。
#   ほかの8属（ジギタリス・プリムラ・ベルゲニア・カラマグロスティス・デスカンプシア・フクシア・アイリス・ロニセラ）の号は一覧（no1〜no40）にない。
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {
 "Ep02": ("Conoclinium coelestinum", "cultivar", 17, 36, None, None, None,
          "総合評価 good（星4つ）。花つき excellent。うどんこ病は出なかった。毎年春には冬の間にほとんどの株が枯れたように見えたが、残った地下茎や実生から新しい株が出て、"
          "6月中旬〜下旬には区画がすっかり埋まった。広がりすぎるという評判があるが、試験では茎は広くは広がらなかった（no37）"),
 "Ep03": ("'Ivory Tower'", "cultivar", 67, 30, None, None, None,
          "総合評価 fair（星3つ）。花つき excellent。うどんこ病への強さ poor（葉の発病 51〜75%。うどんこ病が大きな問題だった）。"
          "咲き終わって茶色くなった花が新しい花に混じり、花が汚れて見えることがあった（no37）"),
 "Ep05": ("'Gateway'", "cultivar", 78, 57, None, None, None,
          "総合評価 fair（星3つ）。花つき excellent。うどんこ病への強さ poor（2003〜2005年に重いうどんこ病、2006年は軽かった）。"
          "種より小型で低いとされるが、株の大きさにはかなり幅がある、との記述（no37）"),
}
