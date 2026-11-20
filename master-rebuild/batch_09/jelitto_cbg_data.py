# Jelitto（s11）とシカゴ植物園（s08）: モナルダ・トラデスカンティア・スピレア・ネペタ・アネモネ・アクイレギア・セントーレア・アジュガ。
# Jelitto は 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/jelitto_cbg_data.py と同じ
#   （英語のサイト内検索: Monarda 14件・Tradescantia 4件・Nepeta 25件・Anemone 47件・Aquilegia 99件〔Barlow・canadensis・chrysantha で絞った〕・Centaurea 25件・Ajuga 4件・Spiraea 該当なし）。
#   一致は23ページ。6秒おき。途中で一度確認画面に戻った（気づかずに検索を8回続けて開いてしまった）。操作せずに10分ほど別の作業をしている間に自動で通った。
#   【教訓】まとめて開く前に、最初の1ページの題名を見て、確認画面でないことを確かめる。
# Jelitto の書き方: バローのシリーズは AQUILEGIA vulgaris var. stellata plena Barlow-Series、Ne05 ムッシーニアイは NEPETA racemosa、Ne01 'Felix' は NEPETA racemosa 'Felix'。
# Jelitto が発表した品種（Historical の欄）: ネペタ 'Blue Dreams'（2006）。
# 種のページを当てたもの: モナルダ ディディマ（Mn01〜Mn04）、シュウメイギク（An01。var. japonica ではなく種のページ）、カナデンシス（Aq02）、モンタナ（Ce04・Ce05）、アジュガ レプタンス（Aj01・Aj02・Aj04・Aj05）。
#   当てていないもの: MONARDA didyma 'Red Colors'（'Panorama Red Shades' と同じものか分からない）、トラデスカンティア（色別の種子の系統だけ）、An02・An03（品種のページなし）、
#   Aj03 'Chocolate Chip'（おぎはらは tenorii としている）、ネペタの交配品種。
# 日照の欄（Location）は記号で読めなかった。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-20"
_DID = ("MONARDA didyma", "species", "Eastern North America: streambanks.", "mostly red", "June - September", "Z4 - Z8", "stoloniferous / erect / clumping", "110 cm", "moist / average", "",
        "Mostly red blossoms, four-sided stems, variable. Attracts hummingbirds. medicinal plant / beneficial plant / tea herb / culinary herb; honey-bee food plant", "北アメリカ東部の川岸")
_MON = ("CENTAUREA montana", "Mountains of Europe", "blue", "May - July", "Z3 - Z9", "stoloniferous", "50 cm", "dry / well-drained / average", "",
        "First year flowering. groundcover; honey-bee food plant / suitable for cutting", "ヨーロッパの山地")
_REP = ("AJUGA reptans", "species", "Europe, Iran, Caucasus", "blue", "May - June", "Z3 - Z9", "stoloniferous / mat-forming / evergreen", "15 cm", "moist / average", "",
        "First year flowering. medicinal plant / groundcover; honey-bee food plant", "ヨーロッパ、イラン、コーカサス")
_BAR = ("Z3 - Z8", "", "80 cm", "well-drained / average", "")
JELITTO = [
 (["Mn01", "Mn02", "Mn03", "Mn04"],) + _DID,
 (["Mn05"], "MONARDA fistulosa", "cultivar", None, "mostly lilac", "July - September", "Z4 - Z8", "stoloniferous", "80 cm", "dry / average", "",
  "medicinal plant / tea herb / culinary herb; honey-bee food plant / suitable for cutting", None),
 (["Ne08"], "NEPETA nervosa 'Pink Cat'", "cultivar", None, "intensive pink", "June - September", "Z3 - Z9", "", "40 cm", "dry / well-drained", "",
  "Fleuroselect Award Winner. Dense spikes. Aromatic scent. First year flowering. groundcover; honey-bee food plant / for the rock garden", None),
 (["Ne05"], "NEPETA racemosa", "cultivar", None, "light blue", "May - September", "Z3 - Z8", "stoloniferous", "30 cm", "dry / well-drained", "",
  "Award of Garden Merit (A.G.M.). Blooms continuously. First year flowering. groundcover; honey-bee food plant", None),
 (["Ne06"], "NEPETA racemosa 'Alba'", "cultivar", None, "pure white", "May - September", "Z3 - Z8", "stoloniferous", "30 cm", "dry / well-drained", "",
  "First year flowering. groundcover; honey-bee food plant", None),
 (["Ne01"], "NEPETA racemosa 'Felix'", "cultivar", None, "deep lilac-blue", "May - October", "Z3 - Z8", "stoloniferous / compact", "25 cm", "dry / well-drained / average", "",
  "Uniform and compact habit, abundant flowering until frost. First year flowering. Foliage: bluish gray, aromatic. groundcover; honey-bee food plant / flowering pot plant", None),
 (["Ne11"], "NEPETA subsessilis 'Blue Dreams'", "cultivar", "Japan", "brilliant blue", "June - August", "Z3 - Z9", "clumping", "60 cm", "moist / cool", "",
  "Abundant, brilliant blue blossoms. Reblooms after deadheading. Introduced by JELITTO PERENNIAL SEEDS in 2006. Foliage: fragrant. "
  "groundcover; honey-bee food plant / for the rock garden / flowering pot plant", "日本（種の原産地）"),
 (["An01"], "ANEMONE hupehensis", "species", "Central China", "white and pink", "August - October", "Z5 - Z7", "stoloniferous / erect / bushy", "70 cm", "well-drained / average", "",
  "Pretty, white to rosy pink flowers from late summer through fall. suitable for cutting", "中国中部"),
 (["An04"], "ANEMONE leveillei", "cultivar", "Western and Central China: open woodlands, moist meadows, along creeks.", "white umbels, outside often bluish", "April - May", "Z5 - Z8", "",
  "50 cm", "moist", "", "Fast growing, early flowering. honey-bee food plant / for the rock garden", "中国西部・中部の明るい林・湿った草地・小川沿い"),
 (["An05"], "ANEMONE multifida 'Major'", "cultivar", None, "white", "June - July", "Z2 - Z9", "", "25 cm", "dry / well-drained", "", "Upright blossoms. for the rock garden", None),
 (["An06"], "ANEMONE multifida 'Rubra'", "cultivar", "Red form of the American A. multifida.", "carmine-red", "May - June", "Z2 - Z9", "erect", "30 cm", "dry / well-drained", "",
  "Attractive foliage and flowers. Full sun in cool summer climates to semi-shade elsewhere. for the rock garden", "アメリカ大陸（種の原産地）"),
 (["Aq01"], "AQUILEGIA canadensis 'Corbett'", "cultivar", "Eastern North America", "light yellow", "May - June", "Z3 - Z8", "erect", "30 cm", "well-drained / average", "",
  "Gently self-sows and is more long-lived than many columbine species. Has thick roots. Second year flowering. "
  "Chance seedling found by nurseryman Richard Simon of Bluemount Nurseries. for the rock garden", "北アメリカ東部（種の原産地）"),
 (["Aq02"], "AQUILEGIA canadensis", "species", "The wild species grows naturally throughout much of North America.", "red with pale yellow corolla", "May - June", "Z3 - Z8", "", "45 cm",
  "well-drained / average", "", "Award of Garden Merit (A.G.M.). for the rock garden", "北アメリカの広い範囲"),
 (["Aq03"], "AQUILEGIA chrysantha 'Yellow Queen'", "cultivar", "Southwestern USA", "golden", "June - August", "Z3 - Z8", "clumping", "80 cm", "well-drained / average", "",
  "Dozens of graceful, large, handsome long-spurred blooms. suitable for cutting", "アメリカ南西部（種の原産地）"),
 (["Aq04"], "AQUILEGIA vulgaris var. stellata plena Barlow-Series 'Nora Barlow'", "cultivar", None, "deep pink with edges of lime-green", "May - July", "Z3 - Z8", "erect", "80 cm",
  "well-drained / average", "", "Double, spurless flowers. suitable for cutting", None),
 (["Aq05"], "AQUILEGIA vulgaris var. stellata plena Barlow-Series 'Bordeaux Barlow'", "cultivar", None, "dark ruby", "May - July") + _BAR + ("Fully double flowers, spurless, upright. suitable for cutting", None),
 (["Aq06"], "AQUILEGIA vulgaris var. stellata plena Barlow-Series 'Black Barlow'", "cultivar", "Western, Central and Southern Europe; naturalized in North America", "purple-black", "May - July") + _BAR
 + ("Fully double flowers, spurless, upright. suitable for cutting", "ヨーロッパ西部・中部・南部（種の原産地）"),
 (["Ce01"], "CENTAUREA dealbata", "cultivar", "Caucasus Mountains", "fresh pink", "June - July", "Z3 - Z9", "erect", "80 cm", "dry / well-drained / average", "",
  "Lovely fresh pink blossoms and deeply fringed foliage. honey-bee food plant / suitable for cutting", "コーカサス山脈"),
 (["Ce02"], "CENTAUREA macrocephala", "cultivar", "Caucasus", "golden", "July - September", "Z3 - Z7", "", "150 cm", "well-drained / average", "",
  "Decorative. honey-bee food plant / suitable for cutting", "コーカサス"),
 (["Ce03"], _MON[0], "cultivar") + _MON[1:],
 (["Ce04", "Ce05"], _MON[0], "species") + _MON[1:],
 (["Ce06"], "CENTAUREA pulcherrima", "cultivar", "Transcaucasia", "pure pink", "June - August", "Z4 - Z8", "", "40 cm", "dry / well-drained / average", "",
  "Large flowering. Foliage: grey, feathered. for the rock garden / suitable for cutting", "南コーカサス"),
 (["Aj01", "Aj02", "Aj04", "Aj05"],) + _REP,
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes（試験地は USDA 5b）。pdftotext -raw で読んだ。総合評価の星は、ネペタ（no29）は読めた。モナルダ・トラデスカンティア・アネモネは記号が落ちて読めなかった。
#   no12 Monarda（https://www.chicagobotanic.org/downloads/planteval_notes/no12_monarda.pdf）Table 1。うどんこ病への強さ: good＝葉の発病・落葉が25%未満、fair＝26〜50%、poor＝51〜75%、very poor＝76%以上
#   no34 Tradescantia（no34_tradescantia.pdf）Table 1 と本文。葉の斑点病: low・moderate・severe
#   no29 Catmints（no29_catmint.pdf）Table 1 と本文。星5つ＝excellent、4つ＝good
#   no25 Fall-blooming anemones（no25_anemones.pdf）Table 1・2 と本文
#   スピレア・アクイレギア・セントーレア・アジュガの号は一覧（no1〜no40）にない。'Panorama'（no12）は 'Panorama Red Shades' と同じものか分からないので使っていない
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {
 "Mn01": ("'Blue Stocking'", "cultivar", 39, None, None, None, None, "草丈 33〜39インチ。花つき 40〜60%。うどんこ病への強さ fair（葉の発病・落葉 26〜50%）。冬の傷みが2年以上あった（no12）"),
 "Mn05": ("fistulosa", "species", 50, None, None, None, None, "草丈 40〜50インチ。花つき 80〜100%。うどんこ病への強さ very poor（葉の発病・落葉 76%以上）。冬の傷みが2年以上あった（no12）"),
 "Td01": ("'Concord Grape'", "cultivar", 24, 36, None, None, None, "花つきが安定してよかった品種の一つ。葉の斑点病は low。午後にも花が見られることがあった（no34）"),
 "Td02": ("'Innocence'", "cultivar", 16, 30, None, None, None, "花つきが安定してよかった品種の一つ。葉の斑点病は moderate（no34）"),
 "Td04": ("'Blue and Gold'", "cultivar", 16, 30, None, None, None, "葉の斑点病は moderate。報告は「'Sweet Kate' は 'Blue and Gold' の別名で、'Blue and Gold' が正しい名前」としている（no34）"),
 "Td05": ("'Little Doll'", "cultivar", 12, 32, None, None, None, "葉の斑点病は severe（試験の中で最も重い区分）（no34）"),
 "Td06": ("'Red Cloud'", "cultivar", 24, 60, None, None, None,
          "試験の中で最も勢いが強く、花つきも最高（最盛期に70%）。一日中花が開いていた。葉の斑点病は low。花が咲き始めるころに倒れやすく、6月初めには乱れることが多かった（no34）"),
 "Ne02": ("'Dropmore'", "cultivar", 18, 36, None, None, None, "総合評価 good（星4つ）。花つき excellent（no29）"),
 "Ne04": ("'Six Hills Giant'", "cultivar", 30, 48, None, None, None, "総合評価 excellent（星5つ）。花つき excellent。夏の間ずっと花が多く、勢いがよかった（no29）"),
 "Ne05": ("racemosa", "species", 14, 36, None, None, None, "総合評価 good（星4つ）。花つき good（報告での名前は racemosa）（no29）"),
 "Ne09": ("racemosa 'Blue Wonder'", "cultivar", 18, 38, None, None, None, "総合評価 good（星4つ）。花つき excellent。'Dropmore' などと違いが見られなかった、との記述（no29）"),
 "Ne10": ("racemosa 'Walker's Low'", "cultivar", 30, 36, None, None, None, "総合評価 excellent（星5つ）。花つき excellent。試験でも最上位の一つ。名前ほど小さくなく、'Six Hills Giant' と同じくらいの高さ（no29）"),
 "An02": ("hupehensis var. japonica 'Pamina'", "cultivar", 30, 28, None, None, None,
          "冬の傷みで株を失い、植え直して再試験した品種の一つ。初霜のあとも花が減らずに咲き続けた。花期は平均 46.8日（no25）"),
 "An03": ("×hybrida 'Honorine Jobert'", "cultivar", 40, 33, None, None, None, "花期は平均 45.8日（9月中旬〜11月中旬）。半日陰を明るくする白花の品種として勧められている（no25）"),
}
