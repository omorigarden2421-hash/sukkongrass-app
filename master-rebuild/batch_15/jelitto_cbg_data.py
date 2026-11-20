# Jelitto（s11）とシカゴ植物園（s08）: アスクレピアス・クロコスミア・ガイラルディア・アガスタチ・カリオプテリス・クナウティア・レウイシア・ルピナス・オリガヌム・ペオニア・パルテノキッスス・
#   シダルセア・アラビス・カルーナ・カマエメルム・クリサンセマム・キミキフーガ・ドラコセファラム。
# Jelitto は 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_11/jelitto_cbg_data.py と同じ
#   （英語のサイト内検索: Asclepias 26件・Crocosmia 1件・Gaillardia 18件・Agastache 19件・Caryopteris 0件・Knautia 6件・Lewisia 44件〔longipetala で絞って12件〕・Lupinus 30件・Origanum 11件・
#     Paeonia 5件・Parthenocissus 0件・Sidalcea 5件・Arabis 10件・Calluna 2件・Chamaemelum 2件・Chrysanthemum 29件・Cimicifuga 4件・Actaea 9件・Dracocephalum 15件・Nipponanthemum 1件）。
#   一致は26ページ。7秒おき、1回の指示は6ページまで。最初の1ページで確認画面が出たが、操作せずに置き、3分ほどで自動で通った。そのあとは出なかった。
# Jelitto の書き方（角かっこは流通名・別名）: アスクレピアス インカルナータは ASCLEPIAS incarnata [Soulmate, Cinderella]（種のページに流通名を併記。Ak02・Ak04 に当てた）、
#   'Milkmaid' は ASCLEPIAS incarnata 'Iceballet' [Milkmaid, Ice Follies]（'Iceballet' の別名として載っている。【要確認】このページを Ak03 に当てた。マスターの花色も白）、
#   ガイラルディアはどれも GAILLARDIA aristata（'Burgunder' [Burgundy]、'Kobold' [Goblin]、Mesa F1-Series 'Mesa Peach'）、
#   クナウティア マケドニカは KNAUTIA macedonica [Red Knight, Red Cherries]、ルピナスは LUPINUS perennis Russell Band of Nobles Series 'Kronleuchter' [Chandelier]・'Fräulein' [Noble Maiden]、
#   'Party Girl' は SIDALCEA malviflora 'Partygirl' [Rosanna]、'Pixie Cream' は ARABIS caucasica 'Pixie Cream'、レウイシアは LEWISIA longipetala Little-Series、
#   ローマンカモミールは CHAMAEMELUM nobile (ANTHEMIS)、ハマギクは NIPPONANTHEMUM nipponicum (CHRYSANTHEMUM)、オレガノ ブルガレは ORIGANUM vulgare wild form。
# Jelitto が発表した品種（Historical の欄。育種会社 s12 と同じ扱いにできる）: アスクレピアス 'Iceballet'（1992）、ガイラルディア 'Amber Wheels'（2009）、クナウティア 'Mars Midget'（2002）・
#   'Midget Mauves'（2019）、シダルセア 'Bianca'（1989）・'Rosaly'（1990）、アラビス 'Pixie Cream'（2007）、ドラコセファラム 'Fuji Blue'・'Fuji White'（2001）、
#   レウイシア 'Little Mango'（2012）・'Little Raspberry'（2015）・'Little Snowberry'（2018）。
# 種のページを当てたもの: オレガノ ブルガレ（Or02・Or03）、カルーナ ブルガリス（Cu01・Cu02）、ローマンカモミール（Cm02）。
#   当てていないもの: クロコスミア（paniculata 'Orangerot' だけ）、アガスタチの3品種（栄養繁殖の交配品種。mexicana は 'Sangria' だけ）、カリオプテリス・パルテノキッスス（掲載なし）、
#   ペオニア（原種の4つだけ）、'Herrenhausen'、アラビス フェルディナンディコブルギ（procurrens 'Glacier' だけ）、コハマギク（ARCTANTHEMUM arcticum は別の種）、
#   サラシナショウマ（CIMICIFUGA ramosa 'Atropurpurea' (ACTAEA simplex) だけ。別の品種）。
# 日照の欄（Location）は記号で読めなかった。
# Jelitto の「Full sun in cool summer climates to semi-shade elsewhere」（シダルセア 'Rosaly'）、土の欄の「warm」（オレガノ ブルガレ）は暑さに関わる記述だが、
#   Jelitto は耐暑性の判定に使わない（記録だけ）。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-20"
_GA = ("Suitable for natural landscaping. Attractive for butterflies and other pollinators. Use for low maintenance plantings. "
       "Drought tolerant/ for xeriscaping/ waterwise design when established. Deer and rabbit resistant. Abundant and long lasting flowering. Easy to grow.")
_GO = "Cultivar. Origin western North-America: pairie."
_GJ = "北アメリカ西部の草原（種の原産地）"
_LEW = ("Flowers the first year from seed, and do not suffer from rust and leaf crown rot. Large flowering, short upright stems, reblooms in the fall, easy in the garden.")
_DRA = ("Long-lived perennial that forms dark green mounds with distinctive foliage and colorful terminal flowering spikes. Remarkably drought tolerant. "
        "Suitable for containers, rock gardens or perennial borders. Introduced by JELITTO PERENNIAL SEED in 2001. groundcover; for the rock garden / flowering pot plant")
_ASC = ("ASCLEPIAS incarnata [Soulmate, Cinderella]", "cultivar", "Southern and Eastern USA: wet meadows, riverbanks, swamp.", "pinkred", "July - August", "Z3 - Z9",
        "clumping / bushy", "100 cm", "moist / boggy / along streamsides / loamy", "",
        "ASCLEPIAS incarnata has a delicate vanilla scent. Shores and marshes are its natural habitat, but also tolerates not quite as moist locations. "
        "ASCLEPIAS incarnata forms a taproot and should not possible be replanted. decorative fruit; honey-bee food plant / suitable for cutting / water or marshplant",
        "アメリカ南部・東部の湿った草地・川岸・沼地（種の原産地）")
_ORI = ("ORIGANUM vulgare wild form", "species", "Europe, Central Asia and Siberia: nutrient poor grasslands, roadsides, embankments and forest margins.", "pale purple",
        "July - October", "Z4 - Z8", "cushion-forming / clumping / vigorous", "35 cm", "dry / sandy / well-drained / warm", "",
        "Aromatic. Typical spice in the south-eastern Mediterranean. At its origin ORIGANUM vulgare is one of the most important native butterfly food plants. Draught resistent. "
        "Edible flowers. medicinal plant / beneficial plant / tea herb / culinary herb / groundcover; honey-bee food plant / for the rock garden / for green roofs",
        "ヨーロッパ・中央アジア・シベリアのやせた草地・道ばた・土手・林のふち（種の原産地）")
_CAL = ("CALLUNA vulgaris", "species", "Western North America, Azores, North and West Europe to Siberia", "bright pink", "August - September", "Z3 - Z9", "bushy", "30 cm",
        "avoid lime / dry / average", "", "medicinal plant / culinary herb / groundcover; honey-bee food plant", "北アメリカ西部・アゾレス諸島・ヨーロッパ北部と西部〜シベリア（種の原産地）")
_CHA = ("CHAMAEMELUM nobile (ANTHEMIS)", None, "West Europe", "silver-white with yellow disc", "June - August", "Z4 - Z9", "", "30 cm", "dry / sandy / well-drained", "",
        "medicinal plant / beneficial plant / tea herb / culinary herb; honey-bee food plant", "西ヨーロッパ")
JELITTO = [
 (["Ak01"], "ASCLEPIAS asperula", "cultivar", "South-western North America: prairie, hillsides, open woodlands.", "greenish-yellow umbels", "April - August", "Z3 - Z9",
  "deep roots", "40 cm", "dry / well-drained / average", "",
  "Greenish-yellow umbels, broad lanceolate foliage. Attractive for butterflies and other pollinators. Important food plant for the monarch butterfly caterpillar. Deer resistant. "
  "Use for low maintenance plantings. Suitable for natural landscaping. suitable for cutting", "北アメリカ南西部の草原・丘の斜面・明るい林"),
 (["Ak02", "Ak04"],) + _ASC,
 (["Ak03"], "ASCLEPIAS incarnata 'Iceballet' [Milkmaid, Ice Follies]", "cultivar", "North America; Quebec to Manitoba, south to Georgia, Louisana, Texas and New Mexico", "white",
  "July - September", "Z3 - Z9", "erect", "100 cm", "moist / average", "",
  "Beautiful white flowering selection from seed. Broad colorful inflorescences of pure white, a durable border perennial, excellent cutflower. "
  "Introduced by JELITTO PERENNIAL SEED in 1992. decorative fruit; honey-bee food plant / suitable for cutting / water or marshplant",
  "北アメリカ（ケベック〜マニトバ、南はジョージア・ルイジアナ・テキサス・ニューメキシコ。種の原産地）"),
 (["Gl01"], "GAILLARDIA aristata 'Amber Wheels'", "cultivar", _GO, "golden flowers with amber-red centers", "June - September", "Z3 - Z9", "erect", "75 cm",
  "dry / well-drained / average / poor, lean", "",
  "Larger blossoms than typical species. Flowers with fringed tips. Requires two growing seasons for abundant flowering. Durable and long lived selection. " + _GA +
  " Introduced by JELITTO PERENNIAL SEEDS in 2009. suitable for cutting", _GJ),
 (["Gl02"], "GAILLARDIA aristata 'Burgunder' [Burgundy]", "cultivar", _GO, "wine-red", "June - September", "Z3 - Z9", "erect", "75 cm", "dry / well-drained / average", "",
  "Popular and easy-to-grow perennial with lovely wine red blossoms. " + _GA + " suitable for cutting", _GJ),
 (["Gl03"], "GAILLARDIA aristata 'Kobold' [Goblin]", "cultivar", _GO, "red with yellow tips", "June - September", "Z3 - Z9", "compact", "35 cm",
  "dry / well-drained / average / poor, lean", "", "Very stable variety. " + _GA + " suitable for cutting", _GJ),
 (["Gl04"], "GAILLARDIA aristata Mesa F1-Series 'Mesa Peach'", "cultivar", "Cultivar.", "yellow with peach-coloured eye", "June - September", "Z3 - Z9", "compact", "35 cm",
  "dry / well-drained / average", "",
  "Uniform and compact growth. Attractive for butterflies and other pollinators. Use for low maintenance plantings. Drought tolerant/ for xeriscaping/ waterwise design when established. "
  "Deer and rabbit resistant. Abundant and long lasting flowering. Easy to grow. honey-bee food plant / flowering pot plant", "園芸で作られたもの"),
 (["Kt01"], "KNAUTIA macedonica [Red Knight, Red Cherries]", "cultivar", "Central Europe", "red to dark red, rarely pink", "July - August", "Z5 - Z10", "erect / clumping", "80 cm",
  "dry / well-drained / average", "", "Deep crimson-colored pincushion-like blossoms which have a commanding garden presence. suitable for cutting", "中央ヨーロッパ"),
 (["Kt02"], "KNAUTIA macedonica 'Mars Midget'", "cultivar", "Central Europe", "ruby-red", "June - October", "Z5 - Z10", "compact / sturdy", "40 cm", "average", "",
  "The pincushion plant flowers tirelessly and abundantly and gently self-sows, but not to worry, it never becomes a problem. Floating, 5 cm wide brilliant ruby-red gems on widely "
  "branching flowering stems. Extremely robust, self-sowing, a valuable, long flowering perennial, attracts butterflies to feed and rest. Shorter and more compact than the species and "
  "therefore sturdier. Introduced by JELITTO PERENNIAL SEEDS in 2002. honey-bee food plant / for the rock garden / flowering pot plant", "中央ヨーロッパ（種の原産地）"),
 (["Kt03"], "KNAUTIA macedonica 'Midget Mauves'", "cultivar", None, "mauve-purple", "June - October", "Z5 - Z10", "clumping / compact", "40 cm", "average", "",
  "Branched stems, uncountable flower heads, stable upright, vigorous rosettes. Introduced by JELITTO PERENNIAL SEEDS in 2019. "
  "honey-bee food plant / for the rock garden / flowering pot plant", None),
 (["Lu01"], "LUPINUS perennis Russell Band of Nobles Series 'Kronleuchter' [Chandelier]", "cultivar", None, "light yellow", "June - August", "Z3 - Z8", "", "100 cm",
  "well-drained / average", "", "suitable for cutting", None),
 (["Lu02"], "LUPINUS perennis Russell Band of Nobles Series 'Fräulein' [Noble Maiden]", "cultivar", None, "creamy-white", "June - August", "Z3 - Z8", "", "100 cm",
  "well-drained / average", "", "suitable for cutting", None),
 (["Lu03"], "LUPINUS perennis", "cultivar", None, "mostly blue", "May - August", "Z3 - Z8", "", "110 cm", "dry / sandy / well-drained", "", "beneficial plant", None),
 (["Or02", "Or03"],) + _ORI,
 (["Sd01"], "SIDALCEA candida 'Bianca'", "cultivar", "USA: Colorado, Nevada, New Mexico, Utah and Wyoming", "white", "June - August", "Z5 - Z8", "erect", "90 cm",
  "well-drained / average", "",
  "Early flowering with white blossoms. Erect stems densely clothed with pristine white flowers. Put Sidalceas to use as a smaller version of hollyhocks. "
  "Introduced by JELITTO PERENNIAL SEEDS in 1989. suitable for cutting", "アメリカ（コロラド・ネバダ・ニューメキシコ・ユタ・ワイオミング。種の原産地）"),
 (["Sd02"], "SIDALCEA malviflora 'Partygirl' [Rosanna]", "cultivar", None, "carmine-rose", "July - September", "Z5 - Z8", "erect", "100 cm", "well-drained / average", "",
  "suitable for cutting", None),
 (["Sd03"], "SIDALCEA malviflora 'Rosaly'", "cultivar", "Garden origin", "soft pink", "July - September", "Z5 - Z8", "erect", "120 cm", "well-drained / average", "",
  "Attractive soft pink blossoms shaped like small hollyhocks Full sun in cool summer climates to semi-shade elsewhere. Introduced by JELITTO PERENNIAL SEEDS in 1990. "
  "suitable for cutting", "園芸で作られたもの"),
 (["Ab01"], "ARABIS caucasica 'Pixie Cream'", "cultivar", "Southern Europe to Iran", "creamy yellow with bright sulphur yellow eye", "March - April", "Z3 - Z7",
  "cushion-forming / compact", "10 cm", "dry / well-drained", "",
  "Dozens of tiny creamy yellow petals with sulphur-yellow centers. Wonderful in the front of the border, the rock garden or particularly in mixed containers. "
  "Introduced by JELITTO PERENNIAL SEEDS in 2007. groundcover; honey-bee food plant / for the rock garden", "南ヨーロッパ〜イラン（種の原産地）"),
 (["Cu01", "Cu02"],) + _CAL,
 (["Cm01"], _CHA[0], "cultivar") + _CHA[2:], (["Cm02"], _CHA[0], "species") + _CHA[2:],
 (["Cs01"], "NIPPONANTHEMUM nipponicum (CHRYSANTHEMUM)", "cultivar", "Japan", "white with greenish-yellow disk", "October - November", "Z7 - Z10", "bushy", "50 cm", "dry", "",
  "Valuable late flowering plant. groundcover; patio plant", "日本"),
 (["Dr01"], "DRACOCEPHALUM argunense 'Fuji Blue'", "cultivar", "Northeastern Asia", "brilliant blue with a light blue lip", "June - August", "Z4 - Z8",
  "clumping / compact / bushy", "30 cm", "dry / well-drained / average", "", _DRA, "北東アジア（種の原産地）"),
 (["Dr02"], "DRACOCEPHALUM argunense 'Fuji White'", "cultivar", "Northeastern Asia", "pure white with a hint of light blue", "June - August", "Z4 - Z8",
  "clumping / compact / bushy", "30 cm", "dry / well-drained / average", "", _DRA, "北東アジア（種の原産地）"),
 (["Lw01"], "LEWISIA longipetala Little-Series 'Little Mango'", "cultivar", "Cultivar", "dark yellow-orange", "May - June", "Z4 - Z8", "rosettes-forming", "15 cm",
  "avoid lime / dry / well-drained / average", "",
  "An abundance of spring blooms - the color of fleshy mango fruit. " + _LEW + " Introduced by JELITTO PERENNIAL SEED in 2012. for the rock garden / flowering pot plant",
  "園芸で作られたもの"),
 (["Lw02"], "LEWISIA longipetala Little-Series 'Little Raspberry'", "cultivar", None, "intense raspberry red", "May - June", "Z4 - Z8", "rosettes-forming", "15 cm",
  "avoid lime / dry / well-drained / average", "",
  "An abundance of spring blooms - colorful raspberry red. " + _LEW + " Introduced by JELITTO PERENNIAL SEEDS in 2015. for the rock garden / flowering pot plant", None),
 (["Lw03"], "LEWISIA longipetala Little-Series 'Little Snowberry'", "cultivar", None, "white with pink stamens", "May - June", "Z4 - Z8", "rosettes-forming", "15 cm",
  "avoid lime / dry / well-drained / average", "",
  "An abundance of white spring blooms. " + _LEW + " Introduced by JELITTO PERENNIAL SEEDS in 2018. for the rock garden / flowering pot plant", None),
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes: 一覧（no1〜no40）に、このまとまりの18属の号はない（no38 は屋上緑化の植物の報告で、ここでは使っていない）。
CBG_V = {}
