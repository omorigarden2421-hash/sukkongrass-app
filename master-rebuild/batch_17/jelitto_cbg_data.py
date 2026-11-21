# Jelitto（s11）とシカゴ植物園（s08）: 在庫のある1品種の属20（レオントポディウムからウンキニアまで）と、在庫のない2〜3品種の属12（アムソニアからビオラまで）。batch_17/input の32属。
# Jelitto は 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。18個目のまとまり（batch_18）の分も同じときに続けて読んだ。
#   英語のサイト内検索: 属名と Cotula・Bistorta・Persicaria・Ficaria・Tovara・Viola labradorica・Viola mandshurica・Delphinium Pacific・Poa glauca など61語（2つのまとまりの合計）。
#     Ophiopogon・Ficaria・Tovara・Leptinella は 0件、Physostegia は 'Alba'・'Rosea' だけ、Ranunculus に ficaria はなし、Polygonatum に odoratum はなし。
#   読んだ商品ページは51（このまとまりは37ページ。うち36ページを当てた）。読み方は batch_17/gaissmayer_data.py の冒頭（Gaißmayer のタブと交互に、1つのサイトにつき7秒おき）。
#   fetch で読む形を試したときに確認画面（403）が出た。タブで開き直して操作せずに置き、10分ほどで自動で通った。
#   検索の途中（Physostegia の次）で一度「525: SSL handshake failed」（サーバー側のエラー）になったが、同じページを開き直すと読めた。
# Jelitto の書き方（角かっこは流通名・別名）: 'Aureum' は MILIUM effusum 'Aureum' [Flash Lights]、'Superbum' は種の POLYGONUM bistorta (BISTORTA officinalis) だけ、
#   トバラは POLYGONUM virginianum (PERSICARIA) (POLYGONUM filiforme)、セセリは SESELI gummiferum [Moon Carrot]、
#   セスレリアは SESLERIA argentea (autumnalis ssp. argentea)〔argentea を種とし、マスターの書き方を別名としている〕、サーモプシスは THERMOPSIS villosa (caroliniana)、
#   ウンキニアは UNCINIA rubra (uncinata) [Firedance]、バプティシアは BAPTISIA australis [Caspian Blue]、ブロンズフェンネルは FOENICULUM vulgare 'Purpureum' (Rubrum) [Smokey, Deco, Bronze]、
#   'Heavenly Blue' は LATHYRUS vernus 'Heavenly Blues'、リモニウムは LIMONIUM latifolium (platyphyllum)・LIMONIUM species 'Blue Diamond'、
#   ビオラ ラブラドリカは VIOLA labradorica hort. 'Purpurea' (riviniana Purpurea-Group)〔紫葉。マスターの葉色も パープル／ブラック系 なので、売っている商品のページとして当てた〕、
#   デルフィニウムは DELPHINIUM elatum Pacific-Premium-Series 'Astolat Premium'・'Black Knight Premium'・'Galahad Premium' (x cultorum)
#   〔Pacific の系統の Jelitto による選抜。名前に Premium が付く。同じ色の系統として当てたが、同じものとして扱ってよいかは要確認〕。
# Jelitto が発表した品種（Historical の欄。育種会社 s12 と同じ扱いにできる）: ヘリオプシス 'Summer Nights'（2004。North Creek Nurseries の Dale Hendricks の選抜）・'Burning Hearts'（2016）、
#   ラシラス 'Heavenly Blues'（2022）、リモニウム 'Blue Diamond'（1987）、バーノニア 'White Lightning'（2014）、ポア 'Blue Hills'（2009）。
# 種のページを当てたもの: ポリゴナム ビストルタ（Pk01 'Superbum'）、トバラの2品種（To01・To02。POLYGONUM virginianum 'Variegatum' … [Painter's Palette] のページは、
#   RHS が Variegated Group と 'Painter's Palette' を分けているので当てていない）、アムソニア タバーナエモンタナ（Av03 'Blue Ice'）、ビオラ マンシュリカ（Vo02 'Mars'）。
#   当てていないもの: レプティネラ、オフィオポゴン、アマドコロ、カラスバ ヒメリュウキンカ、フィソステギアの2品種、ロサ、バプティシア 'Twilite'（掲載なし）。
# 日照の欄（Location）は記号で読めなかった。
# Jelitto の「The golden-green color holds best in cooler temperate areas」（ミリウム 'Aureum'）、「Full sun in cool summer climates to semi-shade elsewhere」
#   （ビオラ ラブラドリカ、エーデルワイス）、土の欄の「cool」（ビオラ ラブラドリカ）は暑さに関わる記述だが、Jelitto は耐暑性の判定に使わない（記録だけ）。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-20"
_TOV = ("POLYGONUM virginianum (PERSICARIA) (POLYGONUM filiforme)", "species", None, "red", "July - August", "Z4 - Z9", "", "50 cm", "average", "",
        "ornamental foliage plant; for the rock garden", None)
_AMO = "Eastern USA westward to Kansas, Oklahoma and Texas"
_AMJ = "アメリカ東部から西はカンザス・オクラホマ・テキサスまで"
_AMT = ("Very low maintenance, long-lived and deer resistant. Pale blue star-shaped blossoms. Foliage: broad, willow-like leaves with beautiful golden fall color. "
        "ornamental foliage plant; honey-bee food plant")
_PAC = "mostly semi-double flowers, pyramid shaped flowering stalks, original quality. suitable for cutting"
JELITTO = [
 (["Ln01"], "LEONTOPODIUM alpinum", "cultivar", "European Mountains", "white", "July - September", "Z4 - Z7", "clumping / compact", "15 cm", "well-drained / average", "",
  "Fuzzy grey-green foliage and densely pubescent, pure white star-like flowers. Full sun in cool summer climates to semi-shade elsewhere. "
  "for the rock garden / suitable for cutting", "ヨーロッパの山地"),
 (["Ms01"], "MELISSA officinalis", "cultivar", "Europe, Central Asia", "pale yellow", "May - June", "Z3 - Z9", "", "40 cm", "well-drained / average", "",
  "medicinal plant / tea herb / culinary herb / groundcover; honey-bee food plant", "ヨーロッパ・中央アジア"),
 (["Ml01"], "MILIUM effusum 'Aureum' [Flash Lights]", "cultivar", "Northern temperate areas", "pale green to purple", "May - July", "Z5 - Z8", "clumping / bushy", "60 cm",
  "moist / acidic / average / humus rich, fertile", "",
  "Golden-green foliage effect during spring and early summer. The golden-green color holds best in cooler temperate areas. Effective in shade. "
  "Award of Garden Merit (RHS). ornamental foliage plant / groundcover", "北半球の温帯（種の原産地）"),
 (["Pm01"], "PARTHENIUM integrifolium", "cultivar", None, "white", "May - July", "Z3 - Z8", "", "90 cm", "dry / average", "",
  "Very aromatic. medicinal plant; suitable for cutting", None),
 (["Pf01"], "PHYTEUMA scheuchzeri", "cultivar", None, "deep blue", "June - July", "Z5 - Z8", "", "20 cm", "well-drained / average", "",
  "Ball-shaped blossoms. for the rock garden / flowering pot plant", None),
 (["Pj01"], "PIMPINELLA major 'Rosea'", "cultivar", None, "rosy-red", "June - September", "Z5 - Z8", "", "80 cm", "average", "",
  "Foliage: feathered. decorative fruit; suitable for cutting", None),
 (["Pw01"], "POA glauca 'Blue Hills'", "cultivar", "Europe, Asia, North and South America", "pale brown", "June - September", "Z3 - Z7", "erect / clumping", "25 cm", "average", "",
  "Delicate ornamental grass of dense clumps with narrow blue-green leaves. Loose arching spikes. Introduced by JELITTO PERENNIAL SEEDS in 2009. "
  "ornamental foliage plant; for the rock garden", "ヨーロッパ・アジア・南北アメリカ（種の原産地）"),
 (["Pk01"], "POLYGONUM bistorta (BISTORTA officinalis)", "species", None, "pink", "May - August", "Z3 - Z9", "stoloniferous", "70 cm", "moist / average", "",
  "medicinal plant / culinary herb; honey-bee food plant / suitable for cutting", None),
 (["To01"],) + _TOV,
 # 2026-11-21 のユーザーの回答: To02 は 'Painter's Palette' と同じ → Jelitto の品種のページを当てる
 (["To02"], "POLYGONUM virginianum 'Variegatum' (filiforme) (PERSICARIA … [Painter's Palette]", "cultivar", None, "red", "July - August", "Z4 - Z9", "", "50 cm", "average", "",
  "Foliage: white-green-yellow marbled. ornamental foliage plant; suitable for cutting", None),
 (["Rt01"], "RATIBIDA pinnata", "cultivar", None, "light yellow with brown disk", "July - September", "Z3 - Z8", "", "120 cm", "dry / average", "", "suitable for cutting", None),
 (["Rl01"], "RUELLIA humilis", "cultivar", "North America: Pennsylvania to Florida, west to Nebraska and Texas", "pale blue-violet", "July - September", "Z4 - Z8", "", "40 cm", "dry", "",
  "A colorful, underused species with clusters of lavender-blue flowers. Large flowering. Drought resistant species adapted to open, dry woodlands, rocky slopes and dry prairies. "
  "Once germinated this is an easy-to-grow perennial and very durable. Single erect stems at first, becoming multi-branched. for the rock garden",
  "北アメリカ（ペンシルベニアからフロリダ、西はネブラスカ・テキサスまで）"),
 (["Ss01"], "SESELI gummiferum [Moon Carrot]", "cultivar", None, "white", "July - August", "Z5 - Z8", "", "80 cm", "dry / average", "",
  "Large umbels, very good cut flower, short living. Plant Select. Foliage: blue-grey. ornamental foliage plant; for the rock garden / suitable for cutting", None),
 (["Se01"], "SESLERIA argentea (autumnalis ssp. argentea)", "cultivar", None, "white", "June - October", "Z4 - Z9", "clumping", "50 cm", "average", "",
  "Dense spikes, rich and abundant flowering, very durable. groundcover; for the rock garden / suitable for cutting", None),
 (["Sq01"], "SPODIOPOGON sibiricus", "cultivar", None, "", "July - October", "Z4 - Z9", "erect", "150 cm", "moist / average", "",
  "Very decorative. solitary plant; suitable for cutting", None),
 (["Sk01"], "SUCCISA pratensis", "cultivar", None, "violet", "July - October", "Z4 - Z7", "", "50 cm", "average", "", "medicinal plant / groundcover", None),
 (["Tm01"], "THERMOPSIS villosa (caroliniana)", "cultivar", None, "yellow", "June - July", "Z5 - Z8", "", "125 cm", "dry / average", "", "Flower clusters.", None),
 (["Un01"], "UNCINIA rubra (uncinata) [Firedance]", "cultivar", None, "", "May - June", "Z6 - Z10", "clumping", "30 cm", "average", "",
  "Very attractive. Foliage: red-bronze. ornamental foliage plant; for the rock garden / flowering pot plant", None),
 (["Av01"], "AMSONIA hubrichtii", "cultivar", "USA: Arkansas and Oklahoma", "sky-blue", "May - July", "Z4 - Z9", "bushy", "90 cm", "dry / well-drained / average", "",
  "A perennial with extraordinary textural beauty, star-shaped flowers, blue blossom umbels, exploding with beautiful golden-yellow fall colour. "
  "A durable insect and disease resistant perennial. Is dealing better with dryer sites than other AMSONIA. North American perennial of the year 2011. "
  "ornamental foliage plant; suitable for cutting", "アメリカ（アーカンソー・オクラホマ）"),
 (["Av02"], "AMSONIA tabernaemontana [Stars, Blue Star]", "cultivar", _AMO, "light blue", "May - July", "Z4 - Z9", "erect / sturdy", "80 cm", "well-drained / average", "", _AMT, _AMJ),
 (["Av03"], "AMSONIA tabernaemontana [Stars, Blue Star]", "species", _AMO, "light blue", "May - July", "Z4 - Z9", "erect / sturdy", "80 cm", "well-drained / average", "", _AMT,
  _AMJ + "（種の原産地）"),
 (["Ba01"], "BAPTISIA australis [Caspian Blue]", "cultivar", "Eastern United States", "lilac-blue", "June - August", "Z3 - Z9", "stoloniferous / erect", "150 cm",
  "dry / well-drained / average", "",
  "Hundreds of pea-like blossoms. Very long-lived, low maintenance perennial. Tough, disease and insect free perennial. Award of Garden Merit (RHS). "
  "decorative fruit / solitary plant; suitable for cutting", "アメリカ東部"),
 (["Ba02"], "BAPTISIA australis var. minor", "cultivar", "Parts of Central USA; Ontario and Quebec, Canada", "lilac-blue", "June - August", "Z3 - Z9",
  "erect / compact / sturdy", "80 cm", "dry / well-drained / average", "",
  "Long-lived perennial with shorter habit than it's cousin, Baptisia australis. Flowers distinct over the foliage. Drought resistant. decorative fruit; for the rock garden",
  "アメリカ中部の一部、カナダのオンタリオ・ケベック"),
 (["Dl01"], "DELPHINIUM elatum Pacific-Premium-Series 'Astolat Premium' (x cultorum)", "cultivar", None, "pinkish tones", "June - September", "Z4 - Z8", "erect", "160 cm",
  "well-drained / average", "", "Selected colour, " + _PAC, None),
 (["Dl02"], "DELPHINIUM elatum Pacific-Premium-Series 'Black Knight Premium' (x cultorum)", "cultivar", None, "dark violet", "June - September", "Z4 - Z8", "erect", "160 cm",
  "well-drained / average", "", "Selected colours, " + _PAC, None),
 (["Dl03"], "DELPHINIUM elatum Pacific-Premium-Series 'Galahad Premium' (x cultorum)", "cultivar", None, "pure white", "June - September", "Z4 - Z8", "erect", "160 cm",
  "well-drained / average", "", "Selected colour, " + _PAC, None),
 (["Fo01"], "FOENICULUM vulgare", "cultivar", None, "yellow", "July - September", "Z6 - Z9", "clumping", "120 cm", "well-drained / average", "",
  "Yellow umbels, TCM plant. medicinal plant / tea herb / culinary herb; honey-bee food plant", None),
 (["Fo02"], "FOENICULUM vulgare 'Purpureum' (Rubrum) [Smokey, Deco, Bronze]", "cultivar", "Garden origin", "yellow", "July - September", "Z6 - Z9", "erect", "80 cm", "average", "",
  "Wonderful bronze foliage with a delicate feathery appearance. Lovely contrast between the bronze foliage and the pale yellow umbels. "
  "ornamental foliage plant / medicinal plant / tea herb / culinary herb; honey-bee food plant", "園芸で作られたもの"),
 (["Hp01"], "HELIOPSIS helianthoides var. scabra 'Summer Nights'", "cultivar", "North America: Southern Canada south to Georgia and westward to Colorado",
  "golden with orange-red center", "July - September", "Z3 - Z9", "erect / clumping / tall", "120 cm", "well-drained / average", "",
  "Sturdy, mostly red stems, reddish leaves, and showy golden yellow flowers with a deep orange-red central disk. Dramatic cut flowers. "
  "A selection made by Dale Hendricks of North Creek Nurseries, USA. Introduced by JELITTO PERENNIAL SEEDS in 2004. suitable for cutting",
  "北アメリカ（カナダ南部からジョージア、西はコロラドまで。種の原産地）"),
 (["Hp02"], "HELIOPSIS helianthoides var. scabra 'Burning Hearts'", "cultivar", None, "bicolored, vivid red-eyed and golden", "July - October", "Z3 - Z9", "", "120 cm",
  "well-drained / average", "",
  "black stems, sturdy habit, reliable first year flowering. Introduced by JELITTO PERENNIAL SEEDS in 2016. Foliage: healthy, dark purple. "
  "ornamental foliage plant; honey-bee food plant / suitable for cutting", None),
 (["Lh01"], "LATHYRUS vernus 'Heavenly Blues'", "cultivar", None, "brilliant heavenly blue", "April - May", "Z3 - Z7", "", "25 cm", "average", "",
  "Introduced by JELITTO PERENNIAL SEEDS in 2022. for the rock garden", None),
 (["Lh02"], "LATHYRUS vernus 'Rosenelfe'", "cultivar", None, "light pink", "April - May", "Z3 - Z7", "", "25 cm", "average", "", "groundcover; for the rock garden", None),
 (["Lj01"], "LIMONIUM species 'Blue Diamond'", "cultivar", "Türkiye", "bright blue", "June - August", "Z4 - Z8", "clumping", "25 cm", "dry / well-drained", "",
  "Panicles of bright blue flowers. Good for cut flowers. Introduced by JELITTO PERENNIAL SEEDS in 1987. for the rock garden / flowering pot plant", "トルコ"),
 (["Lj02"], "LIMONIUM latifolium (platyphyllum)", "cultivar", "Europe", "blue", "May - July", "Z4 - Z8", "clumping", "50 cm", "dry / well-drained", "",
  "A reliable border plant for texture, color and length of bloom with hundreds of tiny pale-blue flowers that create a lovely airy effect above the broad green paddle-shaped leaves. "
  "Good for cut flowers - fresh or dried, drought tolerant, resistant to deer. suitable for cutting", "ヨーロッパ"),
 (["Vr01"], "VERNONIA noveboracensis", "cultivar", None, "purple", "August - November", "Z4 - Z8", "", "200 cm", "moist / average", "", "Flowering heads. suitable for cutting", None),
 (["Vr02"], "VERNONIA noveboracensis 'White Lightning'", "cultivar", "Eastern North America", "white", "August - November", "Z4 - Z8", "erect / clumping / shrubby", "200 cm",
  "moist / average", "",
  "Unique white umbels, decorative seed heads. Introduced by JELITTO PERENNIAL SEEDS in 2014. decorative fruit / solitary plant; suitable for cutting", "北アメリカ東部（種の原産地）"),
 (["Vo01"], "VIOLA labradorica hort. 'Purpurea' (riviniana Purpurea-Group)", "cultivar", "Northeastern USA, Canada and Greenland", "china blue", "April - June", "Z2 - Z8",
  "stoloniferous / cushion-forming / low-growing", "15 cm", "moist / cool", "",
  "Lovely decorative foliage with a purplish hue gives this low-growing species season-long appeal. Full sun in cool summer climates to semi-shade elsewhere. "
  "ornamental foliage plant / groundcover; for the rock garden", "アメリカ北東部・カナダ・グリーンランド"),
 (["Vo02"], "VIOLA mandshurica", "species", None, "mostly blue with dark veins", "April - June", "Z6 - Z9", "", "20 cm", "moist", "", "Foliage: triangular. for the rock garden", None),
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes（試験地は USDA 5b）。pdftotext -raw で読んだ。総合評価の星は、どちらの号も記号が落ちて読めなかった。
#   no18 An Evaluation Study of Hardy Amsonia（https://www.chicagobotanic.org/downloads/planteval_notes/no18_amsonia.pdf）Table 1 と本文。試験は 1994〜1999年。
#   no11 Shrub Roses（no11_shrubroses.pdf）Table 1・Table 2 と本文。'Adelaide Hoodless'（Parkland シリーズ）は入っている。'Sir Thomas Lipton' は入っていない。
#   ほかの属の号は一覧（no1〜no40）にない。
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {
 "Av01": ("Amsonia hubrichtii", "cultivar", 44, 50, None, None, None,
          "花は淡い青、花つき 60〜80%、花期は6月上旬〜7月上旬。花つきは 1995・96年は少なく、97年から増えた。秋の葉色は多くの年で黄〜黄金色（excellent）。"
          "茎はほぼ立ち、株は幅広く整う。試験の間、冬の傷みはなかった。花つきが少し少ない分、最高評価の2種（var. salicifolia・illustris）より評価がやや低い（no18）"),
 "Av02": ("Amsonia tabernaemontana", "cultivar", 50, 54, None, None, None,
          "花は淡い青、花つき 60〜80%、花期は6月上旬〜7月上旬。花房は試験でいちばん大きい。6月に気温が上がると花色が青から白っぽい青にすぐ褪せた。"
          "葉は病害虫・クロロシスなし、10月に黄色。9〜10月に茎がゆるみ、株の中心があいた。試験の間、冬の傷みはなかった（no18）"),
 "Av03": ("Amsonia 'Blue Ice'", "cultivar", 20, 36, None, None, None,
          "花は濃い青（試験でいちばん濃い）、花つき 40〜60%、花期は6月上旬〜下旬。葉は一年中健康。株は密でこんもり（最初の3年は晩夏に株があくことがあった）。"
          "秋の葉色は弱い黄緑。'WFF Select' として入手し、2000年に 'Blue Ice' と名前が付いた、との記述。試験の間、冬の傷みはなかった（no18）"),
 "Ro01": ("Rosa 'Adelaide Hoodless'", "cultivar", None, (64, 78), None, None, None,
          "Parkland シリーズ。花は赤・半八重（2¾〜3 in）、花期は6月上旬〜8月下旬（返り咲きを含む）、最盛期の花つき 60〜80%。高さ 60〜97 in。"
          "黒星病への強さ: なし、うどんこ病への強さ: あり。バラハオレタマバエ・マメコガネの害: some、冬の傷み: some（冬の保護なしの試験）。"
          "オレンジ色の実（½ in）がよくつく。本文で「Parkland のバラでいちばん良いものの1つ」「株の形が良い」（no11）"),
}
