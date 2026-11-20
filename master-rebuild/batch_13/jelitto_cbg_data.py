# Jelitto（s11）とシカゴ植物園（s08）: ガウラ・ジプソフィラ・アシリウム・コルヌス・フェスツーカ・ハコネクロア・パパベル・アンジェリカ・エノテラ・バーバスカム・バーベナ・アンスリスクス・アルテミシア・カラミンサ。
# Jelitto は 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_11/jelitto_cbg_data.py と同じ
#   （英語のサイト内検索: Gaura 5件・Gypsophila 10件・Athyrium 0件・Festuca 9件・Hakonechloa 0件・Papaver orientale 9件・Angelica 11件・Oenothera 27件・Verbascum 23件・
#     Verbena 18件・Anthriscus 5件・Artemisia 13件・Calamintha 9件・Cornus 1件〔canadensis だけ〕）。一致は28ページ。7秒おき。
#   最初の検索で確認画面が出たが、操作せずに Gaißmayer を先に読んでいる間に自動で通った。そのあとは出なかった。
#   途中、20ページをまとめて開いたら道具の返事が時間切れになった（ページは開かれたが結果が返らなかった）ので、その分は6ページずつ読み直した。まとめるのは6〜7ページまでにする。
# Jelitto の書き方（角かっこは流通名・別名）: 'The Bride' は GAURA lindheimeri (OENOTHERA) [The Bride]（種のページに流通名を併記）、
#   カーペットカスミソウは GYPSOPHILA cerastioides (ACANTHOPHYLLUM) [Pixie Splash]、'Snowflake' は GYPSOPHILA paniculata fl. pl. 'Schneeflocke' [Snow Flake]（八重は約60%）、
#   フェスツーカ ガウティエリは FESTUCA gautieri (scoparia) [Hobbit]、'Princess Victoria Louise' は 'Prinzessin Victoria Louise' [Coral Reef]、
#   'Royal Wedding' は [Choir Boy, Checkers] の別名つき、'Vicar's Mead' は ANGELICA sylvestris 'Vicar's Mead' (taiwaniana) [Purpurea]、
#   'Wedding Candles' は VERBASCUM chaixii f. album 'Wedding Candles' [Milkshake]、'Blue Cloud' は CALAMINTHA nepeta ssp. nepeta 'Blue Cloud Strain' (CLINOPODIUM)、
#   エノテラ マクロカルパは OENOTHERA macrocarpa (missouriensis)、スペシオーサは OENOTHERA speciosa [Silky, Pink Petticoats]。
# Jelitto が発表した品種（Historical の欄。育種会社 s12 と同じ扱いにできる）: ガウラ 'Summer Breeze'（2008）、オリエンタルポピー 'Royal Wedding'（1996）、
#   エノテラ 'Silver Wings'（2004）、バーバスカム 'Sixteen Candles'（2004）・'Wedding Candles'（2006）・'Violetta'（1999）。
# 種のページを当てたもの: ガウラ（Ga02・Ga03・Ga05・Ga06。Ga04 'The Bride' は流通名つきのページなので品種として）、ジプソフィラ パニキュラータ（Gy02・Gy03）・レペンス（Gy06）、
#   エノテラ スペシオーサ（Oe03）、アルテミシア ブルガリス（Am02）、カラミンサ グランディフローラ（Ca01）。
#   当てていないもの: アシリウム・ハコネクロア・コルヌス（掲載なし）、フェスツーカ グラウカ（'Blue Select' は別の品種）・アイダホエンシス、アルテミシア シュミッディアーナ。
# 日照の欄（Location）は記号で読めなかった。
# Jelitto の「Full sun in cool summer climates to semi-shade elsewhere」（フェスツーカ ガウティエリ）は暑さに関わる記述だが、Jelitto は耐暑性の判定に使わない（記録だけ）。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-20"
_GAO = "The wild species is native to Louisiana and Texas (USA)."
_GAJ = "アメリカのルイジアナ州・テキサス州（種の原産地）"
_GAF = "Numerous flower racemes, very showy, good cut flower, can be grown as an annual. honey-bee food plant / suitable for cutting"
_PAO = "Southwest Asia"
_PAJ = "南西アジア（種の原産地）"
_VHO = "North America: moist prairies, damp thicket."
_VHJ = "北アメリカの湿った草原・湿ったやぶ（種の原産地）"
_VCO = "South Central Europe"
_VCJ = "ヨーロッパ中南部（種の原産地）"
JELITTO = [
 (["Ga01"], "GAURA lindheimeri 'Summer Breeze' (OENOTHERA)", "cultivar", _GAO, "pure white", "July - October", "Z5 - Z9", "bushy", "120 cm", "dry / well-drained", "",
  "Pure white flowers with pink filaments, pink buds, very rich and abundant flowering until first frost, especially sturdy and winter hardy selection, in the 1. year 80 cm, in the 3. year 150 cm. "
  "Introduced by JELITTO PERENNIAL SEEDS in 2008. Breeding began from a sterile plant selected by Christian Kress of Sarastro Nursery in Austria. honey-bee food plant / suitable for cutting", _GAJ),
 (["Ga04"], "GAURA lindheimeri (OENOTHERA) [The Bride]", "cultivar", None, "white", "July - October", "Z5 - Z9", "", "120 cm", "dry / well-drained", "", _GAF, _GAJ),
 (["Ga02", "Ga03", "Ga05", "Ga06"], "GAURA lindheimeri (OENOTHERA) [The Bride]", "species", None, "white", "July - October", "Z5 - Z9", "", "120 cm", "dry / well-drained", "", _GAF, _GAJ),
 (["Gy01"], "GYPSOPHILA cerastioides (ACANTHOPHYLLUM) [Pixie Splash]", "cultivar", "Himalayas", "white with pink veins", "May - June", "Z4 - Z8", "stoloniferous / cushion-forming", "8 cm",
  "dry / gritty / well-drained", "",
  "A low mounding Baby's Breath with mouse-eared leaves and diminutive white flowers with pink veins on the insides. Outstanding, easy-to-grow rock garden species that is suitable also for containers and window boxes. "
  "for the rock garden / flowering pot plant", "ヒマラヤ"),
 (["Gy04"], "GYPSOPHILA paniculata fl. pl. 'Schneeflocke' [Snow Flake]", "cultivar", None, "white", "June - August", "Z3 - Z7", "", "100 cm", "dry / well-drained", "",
  "Double (approx. 60%). suitable for cutting", None),
 (["Gy02", "Gy03"], "GYPSOPHILA paniculata", "species", None, "white", "June - August", "Z3 - Z7", "", "100 cm", "dry / well-drained", "",
  "Abundant flowering. honey-bee food plant / suitable for cutting", None),
 (["Gy05"], "GYPSOPHILA repens 'Rosea'", "cultivar", None, "light pink", "May - June", "Z3 - Z8", "", "15 cm", "dry / well-drained", "", "honey-bee food plant / for the rock garden", None),
 (["Gy06"], "GYPSOPHILA repens", "species", None, "white", "May - June", "Z3 - Z8", "", "15 cm", "dry / well-drained", "",
  "Award of Garden Merit (A.G.M.) from the Royal Horticultural Society. honey-bee food plant / for the rock garden / for green roofs", None),
 (["Fe01"], "FESTUCA gautieri (scoparia) [Hobbit]", "cultivar", "Pyrenees", "greenish", "June - July", "Z4 - Z7", "stoloniferous / cushion-forming / mat-forming / low-growing / evergreen", "20 cm",
  "dry / sandy / well-drained / rocky / average", "",
  "An attractive dwarf grass. Great addition to a trough garden or in combination with walls and steps. Full sun in cool summer climates to semi-shade elsewhere. for the rock garden", "ピレネー山脈"),
 (["Pp01"], "PAPAVER orientale 'Brilliant'", "cultivar", None, "fire-red", "May - June", "Z3 - Z8", "", "80 cm", "dry / well-drained / average", "", "Large flowering. suitable for cutting", None),
 (["Pp02"], "PAPAVER orientale 'Prinzessin Victoria Louise' [Coral Reef]", "cultivar", _PAO, "salmon colored", "May - June", "Z3 - Z8", "erect", "80 cm", "dry / well-drained / average", "",
  "Large thick buds open-up to crepe paper-like large salmon-pink blossoms with alluring black interior blotches. Attractive cut flower candidate - fresh or dried seed capsules. suitable for cutting", _PAJ),
 (["Pp03"], "PAPAVER orientale 'Royal Wedding' [Choir Boy, Checkers]", "cultivar", _PAO, "pure white with black center", "May - June", "Z3 - Z8", "erect", "80 cm", "dry / well-drained / average", "",
  "Pure white flowers from seed! Large crepe paper-like pure white blossoms with black centers in single flowering stems. Tall flowering stems rising from leafy clumps which go dormant following bloom period. "
  "Introduced by JELITTO PERENNIAL SEEDS in 1996. Renamed by other companies as 'Choir Boy'. suitable for cutting", _PAJ),
 (["Pp04"], "PAPAVER orientale plena 'May Queen'", "cultivar", None, "orange red", "May - June", "Z3 - Z8", "", "80 cm", "dry / well-drained / average", "", "Flower: double. suitable for cutting", None),
 (["Ag01"], "ANGELICA pachycarpa", "cultivar", "Spain and Portugal", "white", "July - September", "Z4 - Z10", "clumping", "100 cm", "moist / average", "",
  "Exceptional glossy foliage, surprisingly hardy mediterranean species. Thumb-sized, round buds open-up to gorgeous heads of white flowers. ornamental foliage plant", "スペイン・ポルトガル"),
 (["Ag02"], "ANGELICA sylvestris 'Ebony'", "cultivar", None, "dark pink umbels", "June - September", "Z4 - Z9", "", "80 cm", "moist", "",
  "Award of Garden Merit (A.G.M.) from the Royal Horticultural Society. Foliage: intensive dark purple. ornamental foliage plant; suitable for cutting", None),
 (["Ag03"], "ANGELICA sylvestris 'Vicar's Mead' (taiwaniana) [Purpurea]", "cultivar",
  "Cultivar. The species is native to Europe and Eurasia: meadows, roadsides, woodland edges, riverbanks from the plains to the highlands.", "large umbels of pale purple pink",
  "June - September", "Z4 - Z9", "tall", "150 cm", "moist", "",
  "Dark reddish-purple stems and leaves. The color of ANGELICA sylvestris 'Vicar's Mead' can be described as maroon to burgundy. ornamental foliage plant / solitary plant; honey-bee food plant",
  "ヨーロッパ・ユーラシアの草地、道ばた、林のふち、川岸（種の原産地）"),
 (["Oe01"], "OENOTHERA macrocarpa (missouriensis)", "cultivar", "Southern Great Plains/USA: Oklahoma, Kansas and Missouri", "golden yellow", "June - September", "Z4 - Z8",
  "stoloniferous / low-growing", "20 cm", "dry / well-drained", "",
  "Award of Garden Merit (A.G.M.) from the Royal Horticultural Society. Large (10 cm) saucer-shaped, golden-yellow flowers, large torpedo-like seed heads. Will handle dry, sun-baked conditions. groundcover",
  "アメリカの南部大平原（オクラホマ・カンザス・ミズーリ州）"),
 (["Oe02"], "OENOTHERA macrocarpa ssp. fremontii 'Silver Wings' (missouriensis)", "cultivar", "United States: Kansas and Nebraska", "golden", "June - September", "Z4 - Z8", "stoloniferous", "15 cm",
  "dry / gritty / well-drained", "",
  "Wavy, slender, lanceolated, grey-green leaves and large, papery, golden cup-shaped flowers. Introduced by JELITTO PERENNIAL SEEDS in 2004. groundcover", "アメリカのカンザス州・ネブラスカ州"),
 (["Oe03"], "OENOTHERA speciosa [Silky, Pink Petticoats]", "species", "Central USA", "soft pink", "June - September", "Z5 - Z8", "low-growing", "40 cm", "dry / well-drained", "",
  "This vigorous-growing, pink evening primrose produces dozens of large 5 cm saucer-shaped blossoms day and night. Drought tolerant, easy-to-grow selection. "
  "Very low maintenance perennial for tough landscape sites. Fragrant. groundcover; for the rock garden", "アメリカ中部（種の原産地）"),
 (["Vb01"], "VERBASCUM chaixii 'Sixteen Candles'", "cultivar", _VCO, "golden", "June - August", "Z4 - Z8", "erect / rosettes-forming", "100 cm", "dry / well-drained / average", "",
  "Bold upright candelabras on this perennial mullein. Bright yellow flowers with attractive violet filaments. Richly branched. Perennial. Introduced by JELITTO PERENNIAL SEEDS in 2004. "
  "honey-bee food plant / suitable for cutting", _VCJ),
 (["Vb02"], "VERBASCUM chaixii f. album 'Wedding Candles' [Milkshake]", "cultivar", _VCO, "pure white", "June - August", "Z4 - Z8", "erect / rosettes-forming", "100 cm",
  "dry / well-drained / average", "",
  "Candelabras of pure white flowers with purple filaments. Multi branched flower stems, perennial. Consider 'Wedding Candles' for the dry garden or scree. "
  "Introduced by JELITTO PERENNIAL SEEDS in 2006. honey-bee food plant / suitable for cutting", _VCJ),
 (["Vb03"], "VERBASCUM phoeniceum 'Violetta'", "cultivar", "Cultivar. Europe, North Africa, West and Central Asia: steppes, forest edges.", "dark purple-violet", "May - August", "Z5 - Z8",
  "erect / rosettes-forming / flat / wintergreen", "90 cm", "dry / well-drained", "",
  "A reliable purple-flowering, easy-to-grow seed strain with paper-like flowers. As many verbascums are quite tall, 'Violetta' - shorter in statue - is ideally suited for smaller gardens. "
  "Introduced by JELITTO PERENNIAL SEEDS in 1999. flowering pot plant", "ヨーロッパ・北アフリカ・西アジア・中央アジアのステップ、林のふち（種の原産地）"),
 (["Vn01"], "VERBENA bonariensis [Buenos Aires, Finesse, Purple Top]", "cultivar", "South America", "bright violet-blue", "July - October", "Z7 - Z10", "erect / vigorous", "100 cm",
  "dry / well-drained", "",
  "Award of Garden Merit (A.G.M.) from the Royal Horticultural Society. Architecturally interesting, thin stems with dozens of small violet-purple blossoms. Moderately winter hardy.", "南アメリカ"),
 (["Vn02"], "VERBENA hastata", "cultivar", _VHO, "mostly blue, but also pink and white", "June - September", "Z3 - Z8", "erect / lax", "120 cm", "moist / average", "",
  "Mostly blue, few pink and white. Attractive for butterflies and other pollinators. Suitable for natural landscaping. Use for low maintenance plantings. Moderate self-sowing at suitable locations. "
  "medicinal plant; suitable for cutting", "北アメリカの湿った草原・湿ったやぶ"),
 (["Vn03"], "VERBENA hastata 'Blue Spires'", "cultivar", _VHO, "dark blue", "June - September", "Z3 - Z8", "", "120 cm", "moist / average", "", "suitable for cutting", _VHJ),
 (["Ah01"], "ANTHRISCUS sylvestris 'Golden Fleece'", "cultivar", None, "white", "April - July", "Z6 - Z9", "", "60 cm", "well-drained / average / humus rich, fertile", "",
  "Foliage: golden green. ornamental foliage plant; suitable for cutting", None),
 (["Ah02"], "ANTHRISCUS sylvestris 'Ravenswing'", "cultivar", "Europe, West Asia and North Africa", "white", "April - July", "Z6 - Z9", "bushy", "60 cm",
  "well-drained / average / humus rich, fertile", "",
  "Decorative foliage. White flowering umbels might be used in floral arrangements. Foliage: fern-like, bronze-purple-red. ornamental foliage plant; suitable for cutting",
  "ヨーロッパ・西アジア・北アフリカ（種の原産地）"),
 (["Am02"], "ARTEMISIA vulgaris", "species", "Europe to Iran and Siberia, North Africa", "red-brown", "June - August", "Z2 - Z9", "", "120 cm", "dry / average", "",
  "TCM plant. medicinal plant / tea herb / culinary herb", "ヨーロッパからイラン・シベリア、北アフリカ（種の原産地）"),
 (["Ca02"], "CALAMINTHA nepeta ssp. nepeta 'Blue Cloud Strain' (CLINOPODIUM)", "cultivar", "Cultivar. South Europe to Iran: alpine steppes, rocky meadows.", "bright light-blue",
  "June - October", "Z5 - Z9", "clumping / bushy", "30 cm", "dry / well-drained", "",
  "Selected as Perennial Plant of the year from the PPA (Perennial Plant Association). Very valuable, permanent flowering perennial, ideal for edging borders. "
  "medicinal plant / tea herb / culinary herb / groundcover; honey-bee food plant / for the rock garden", "南ヨーロッパからイランの高山のステップ、岩の多い草地（種の原産地）"),
 (["Ca01"], "CALAMINTHA grandiflora (CLINOPODIUM) [Elfin Purple]", "species", "Southeastern Europe to Iran and Caucasus: mountain forests, mixed forests.", "purple-rose", "May - July",
  "Z4 - Z7", "clumping / bushy", "20 cm", "dry / well-drained / average", "",
  "Aromatic leaves and rose-purple flowers. Well-suited for containers, the rock garden or the front of the border. Suitable for natural landscaping. Attractive for butterflies and other pollinators. groundcover",
  "ヨーロッパ南東部からイラン・コーカサスの山の林（種の原産地）"),
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes（試験地は USDA 5b）。pdftotext -raw で読んだ。
#   no39 Lady ferns and Japanese painted ferns（https://www.chicagobotanic.org/downloads/planteval_notes/no39_ferns.pdf）Table 1 と本文。総合評価: 星5つ＝excellent、4つ＝good。
#     試験地は木かげだったが、2006年に木がなくなって一部の区に午後の日が当たるようになった（Table 1 の Light Exposure）。'Metallicum' の名前では試験に入っていないので、
#     At03 には var. pictum（変種そのもの）の記録を当てた。
#   no26 Sundrops and evening primroses（no26_sundropsprimroses.pdf）Table 1 と本文。総合評価: 星4つ＝good。'Silver Wings' は試験に入っていない（fremontii 'Lemon Silver' は別の品種）。
#   no19 Artemisias（no19_artemisias.pdf）Table と本文。報告は「'Silver Mound' = A. schmidtiana 'Nana'」としている。ブルガリス 'Janlim' は試験に入っていない。
#   ほかの属（ガウラ・ジプソフィラ・コルヌス・フェスツーカ・ハコネクロア・パパベル・アンジェリカ・バーバスカム・バーベナ・アンスリスクス・カラミンサ）の号は一覧（no1〜no40）にない。
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {
 "At01": ("filix-femina 'Dre's Dagger'", "cultivar", 20, 36, None, None, "clumping",
          "総合評価 good（星4つ）。午後の日が当たる区で育てたが、しおれは見られなかった。2006〜07年の冬に株元が少し傷んだ（no39）"),
 "At02": ("niponicum var. pictum 'Burgundy Lace'", "cultivar", 15, 27, None, None, "spreading",
          "総合評価 good（星4つ）。午後の日が当たる区。2006年以降、乾燥か日の当たりすぎによる傷みが2年以上あった（no39）"),
 "At03": ("niponicum var. pictum", "species", 19, 32, None, None, "spreading",
          "変種 pictum そのものの記録。総合評価 excellent（星5つ）。日かげの区でも、乾燥によるしおれ・葉の乾きが2年以上あった（no39）"),
 "At04": ("niponicum var. pictum 'Pewter Lace'", "cultivar", 18, 30, None, None, "spreading",
          "総合評価 excellent（星5つ）。日かげの区で育て、暑さ・乾燥による傷みは見られなかった（no39）"),
 "At05": ("niponicum var. pictum 'Silver Falls'", "cultivar", 16, 28, None, None, "spreading",
          "総合評価 good（星4つ）。午後の日が当たる区。2006年以降、乾燥か日の当たりすぎによる傷みが2年以上あった（no39）"),
 "Oe01": ("macrocarpa", "cultivar", 12, 30, None, None, None,
          "総合評価 good（星4つ）。花の量は low（20〜40%）。花後に株の中心があくが、数週間で埋まる（no26）"),
 "Oe03": ("speciosa 'Woodside White'", "cultivar", 18, 24, None, None, None,
          "総合評価 good（星4つ）。花の量は high（60〜80%）。1999〜2000年と2000〜01年の冬に株元が傷んだが、茎がすぐに伸び直して区が埋まった。"
          "スペシオーサの品種はどれも地下茎で速く広がり、ボーダーには勢いが強すぎることがある（no26）"),
 "Am01": ("schmidtiana 'Silver Mound'（＝'Nana'）", "cultivar", 10, 32, None, None, None,
          "試験で特によかった6つに入る。1995年・1996年の晩夏に、蒸れ（melt-out）で株の中心があいた。高い湿度や湿った土が原因、との記述（no19）"),
}
