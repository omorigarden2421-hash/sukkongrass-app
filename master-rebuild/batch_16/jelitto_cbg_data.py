# Jelitto（s11）とシカゴ植物園（s08）: エピメディウム・フラガリア・ヘレボルス・イベリス・リリオペ・リクニス・ムクデニア・ファラリス・フィソカルプス・ロジャーシア・ソリダゴと、
#   アクタエアからラミアストラムまでの1品種の属27（batch_16/input の38属）。
# Jelitto は 2026-11-20 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_11/jelitto_cbg_data.py と同じ
#   （英語のサイト内検索: 属名38個と Lamium・Silene・Avena。Epimedium・Mukdenia・Aegopodium・Ampelopsis・Arrhenatherum・Brunnera・Ceratostigma・Dendranthema・Euonymus・Helictotrichon・
#     Imperata・Lamiastrum は 0件、Physocarpus・Erica は別の植物だけ、Liriope は 'Big Blue' だけ）。一致は21ページ。7秒おき、1回の指示は6ページまで。
#   検索の7ページ目（Mukdenia）で確認画面が出た。操作せずに置き、4分ほどで自動で通った。そのあとは出なかった。
# Jelitto の書き方（角かっこは流通名・別名）: 四季なりのワイルドストロベリーは FRAGARIA vesca var. semperflorens 'Alexandria'・'Alpine Yellow' [White Delight, White Solemacher …]、
#   ヘレボルス オリエンタリスは HELLEBORUS orientalis New Hybr. (x hybridus)（Jelitto の新しい交配の混合。種そのものの種子はない）、
#   'Angel's Blush' は LYCHNIS coronaria 'Oculata' (AGROSTEMMA, SILENE) [Angel's Blush]、'Noble Spirit' は ARUNCUS aethusifolius [Noble Spirit]（種のページに流通名を併記）、
#   ダルメラは PELTIPHYLLUM peltatum (DARMERA)、アスチルボイデスは ASTILBOIDES tabularis (RODGERSIA)、ゴニオリモンは GONIOLIMON collinum 'Sea Spray' (incanum)。
# Jelitto が発表した品種（Historical の欄。育種会社 s12 と同じ扱いにできる）: イベリス 'Snow Cushion'（2002）、ブフタルムム 'Alpengold'（1991）、エリオゴヌム 'Little Rascal'（2009）、
#   ゴニオリモン 'Sea Spray'（2007）。アルンクス エスシフォリウスは 1984年に Jelitto が初めて種子を売った、との記述。
# 種のページを当てたもの: ヘレボルス アーグティフォリウス（Hb01）、ヘレボルス オリエンタリスの交配の混合（Hb02。花色は混合なので使わない）、ファラリス アルンディナセア（Pi01・Pi02。緑葉の種）、
#   ロジャーシア ピンナータ（Rg01）、パンパスグラス（Cd01。[White Feather, White Plume] は大型の系統）。
#   当てていないもの: イベリスの種そのもの（品種の種子だけ）、リリオペ、ロジャーシア ポドフィラ、ソリダゴ（rugosa・flexicaulis はなし）、アクタエア ヤポニカ、アンドロサセ ビローサ、
#   オーブリエタ（x cultorum の品種だけ）、ウェイリチー（Chrysanthemum の検索にもなかった）、エリカ カルネア、エリシマム（'Orange Flame' なし）、ヘリアンサス 'Happy Days'、ヘリクトトリコン。
# 日照の欄（Location）は記号で読めなかった。
# Jelitto の「Full sun in cool summer climates to semi-shade elsewhere」（アルンクス エスシフォリウス）、土の欄の「cool」（アスチルボイデス）・「warm」（アルテア、パンパスグラス）、
#   「need a warm summer to flower」（エラグロスティス）は暑さに関わる記述だが、Jelitto は耐暑性の判定に使わない（記録だけ）。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-20"
_FRU = "decorative fruit / medicinal plant / beneficial plant / tea herb / culinary herb / groundcover"
_LYO = "Selection. Species is native to Europe, Asia Minor to Turkestan, Himalayas: open woodlands, roadsides."
_LYJ = "ヨーロッパ・小アジア〜トルキスタン・ヒマラヤの明るい林、道ばた（種の原産地）"
_PHA = ("PHALARIS arundinacea", "species", None, "", "June - August", "Z3 - Z8", "stoloniferous / erect", "200 cm", "moist / boggy / along streamsides", "",
        "beneficial plant / groundcover; suitable for cutting / water or marshplant", None)
JELITTO = [
 (["Fr01"], "FRAGARIA vesca var. semperflorens 'Alexandria'", "cultivar", None, "white", "May - September", "Z4 - Z8", "", "20 cm", "average / humus rich, fertile", "",
  "Productive variety, mostly elongated red berries, without stolons. " + _FRU + "; honey-bee food plant", None),
 (["Fr02"], "FRAGARIA vesca var. semperflorens 'Alpine Yellow' [White Delight, White Solemacher …]", "cultivar", None, "white", "May - June", "Z4 - Z8", "", "20 cm",
  "average / humus rich, fertile", "", "White-yellow berries, without stolons. " + _FRU, None),
 (["Hb01"], "HELLEBORUS argutifolius (corsicus)", "species", "Corsica, Sardinia: open woodland.", "yellowish-green", "February - April", "Z6 - Z9", "evergreen / wintergreen", "50 cm",
  "dry / well-drained / average", "", "Evergreen foliage for cutting. toxic plant / groundcover; suitable for cutting", "コルシカ島・サルデーニャ島の明るい林（種の原産地）"),
 (["Hb02"], "HELLEBORUS orientalis New Hybr. (x hybridus)", "species", "Garden origin", "mixture of yellow, white, pink, red, that also includes some spotted and striped",
  "February - April", "Z3 - Z8", "clumping / wintergreen", "35 cm", "average", "",
  "Jelitto's special blend of its newest hybrids. Long-lasting cut flower. Plant in a favorable winter location. Early spring flowering. toxic plant / groundcover; suitable for cutting",
  "園芸で作られたもの"),
 (["Ib02"], "IBERIS sempervirens 'Snow Cushion'", "cultivar", "Garden origin", "snow-white", "April - May", "Z3 - Z9",
  "stoloniferous / cushion-forming / compact / evergreen / wintergreen", "15 cm", "well-drained / average", "",
  "First reliable dwarf Candytuft seed strain, only one-half the size of the typical Candytuft, large and abundant flowering. Densely crowded corymbs of snow-white flowers. "
  "First choice for container production in smaller pots (9 cm). Could be easily used in mixed container plantings or in the rock garden. Early spring flowering. "
  "Introduced by JELITTO PERENNIAL SEED in 2002. groundcover; honey-bee food plant / for the rock garden / flowering pot plant", "園芸で作られたもの"),
 (["Lc01"], "LYCHNIS coronaria 'Alba' (AGROSTEMMA, SILENE)", "cultivar", _LYO, "pure white", "July - August", "Z4 - Z8", "erect / richly branched / evergreen", "70 cm",
  "dry / average / undemanding", "",
  "Mostly biennial, might be perennial after an early pruning. Pure white selection of the well known Rose Campion. The bright white flowers are very nice for shady, dark places. "
  "Decorative white and silvery foliage. For natural and cottage gardens. Sows at a matching location itself. Easy to grow! ornamental foliage plant / groundcover", _LYJ),
 (["Lc02"], "LYCHNIS coronaria 'Oculata' (AGROSTEMMA, SILENE) [Angel's Blush]", "cultivar", _LYO, "white, later with red eye", "July - August", "Z4 - Z8",
  "erect / richly branched / evergreen", "70 cm", "dry / average", "",
  "Mostly biennial, might be perennial after an early pruning. Variable white with red eye selection of the well known Rose Campion. Decorative white and silvery foliage. "
  "For natural and cottage gardens. Sows at a matching location itself. Easy to grow! ornamental foliage plant / groundcover", _LYJ),
 (["Lc03"], "LYCHNIS x haageana 'Molten Lava'", "cultivar", None, "brilliant red", "June - July", "Z5 - Z8", "compact", "30 cm", "well-drained / average", "",
  "Abundant flowering. groundcover; for the rock garden / flowering pot plant", None),
 (["Pi01", "Pi02"],) + _PHA,
 (["Rg01"], "RODGERSIA pinnata", "species", None, "pink-white", "June - July", "Z5 - Z8", "", "80 cm", "moist / average", "", "suitable for cutting", None),
 (["Ai01"], "ASTILBOIDES tabularis (RODGERSIA)", "cultivar", "Manchuria, Northern Korea, Northern China: woodlands, along streams.", "white", "May - July", "Z4 - Z8",
  "rhizomatous / tall / bushy", "100 cm", "moist / along streamsides / cool", "",
  "ASTILBOIDES tabularis is an imposing ornamental foliage plant. With uniform moisture, the leaves of the panel sheet form an excellent background for smaller floriferous perennials "
  "in the foreground. Forms an underground rhizome, but not running. ornamental foliage plant / decorative fruit / groundcover; suitable for cutting / water or marshplant",
  "満州・朝鮮半島北部・中国北部の林、流れのそば"),
 (["Ax01"], "ALTHAEA officinalis", "cultivar", "West Europe, Central Asia", "pink", "May - September", "Z3 - Z10", "", "180 cm",
  "lime-loving, calcareous / average / humus rich, fertile / warm", "", "medicinal plant / beneficial plant / tea herb / culinary herb; honey-bee food plant", "西ヨーロッパ・中央アジア"),
 (["Au01"], "ARUNCUS aethusifolius [Noble Spirit]", "cultivar", "South Korea", "white", "May - July", "Z3 - Z9", "clumping / low-growing", "30 cm", "moist / well-drained", "",
  "Lovely feathery foliage. Flowers with partially red stems. Perennial Plant of the Year 2010 in Sweden. Full sun in cool summer climates to semi-shade elsewhere. "
  "In 1984 Jelitto were then the first seed company in a position to sell this species of aruncus seeds. groundcover", "韓国"),
 (["Bi01"], "BIGELOWIA nuttallii", "cultivar", "North America, South and Southeast United States: on sandstone and on the edge of pine forests.", "yellow umbels",
  "August - October", "Z4 - Z10", "stoloniferous / erect / evergreen", "30 cm", "dry / average", "",
  "Dense yellow umbels, persistent flowering groundcover. Upright and very stable. White, yellow flowers, very closely set, form an unusual, planar impression. Drought-tolerant. "
  "Easy to care for and undemanding. groundcover; honey-bee food plant / for the rock garden / suitable for cutting", "北アメリカ（アメリカ南部・南東部）の砂岩の上、マツ林のふち"),
 (["Bu01"], "BUPHTHALMUM salicifolium 'Alpengold'", "cultivar", "Cultivar. Alps, Southeastern Europe: calcareous and low nutrient meadows.", "golden", "June - August", "Z3 - Z9",
  "cushion-forming", "50 cm", "dry / lime-loving, calcareous / average / poor, lean", "",
  "Larger flowers than the species, double ray of petals. Introduced by JELITTO PERENNIAL SEEDS in 1991. honey-bee food plant / suitable for cutting",
  "アルプス・南東ヨーロッパの石灰質でやせた草地（種の原産地）"),
 (["Cd01"], "CORTADERIA selloana (argentea) [White Feather, White Plume]", "species", "South America - Argentinia, Brazil, Chile, Paraguay and Uruguay", "mostly silver-white",
  "September - October", "Z7 - Z10", "erect / clumping / tall / wintergreen", "200 cm", "well-drained / average / humus rich, fertile / warm", "",
  "Dense tufts with arching leaves and decorative mostly silver-white plumes, variable. Excellent cut flower - fresh or dried. solitary plant; suitable for cutting",
  "南アメリカ（アルゼンチン・ブラジル・チリ・パラグアイ・ウルグアイ。種の原産地）"),
 (["Da01"], "PELTIPHYLLUM peltatum (DARMERA)", "cultivar", None, "pink", "April - May", "Z5 - Z8", "stoloniferous", "100 cm", "moist / boggy / average", "",
  "Decorative leaves appear after flowers. water or marshplant", None),
 (["Es01"], "ELSHOLTZIA stauntonii", "cultivar", "China", "rose-purple", "September - October", "Z4 - Z9", "erect", "150 cm", "dry / well-drained", "",
  "Aromatic foliage and flowering panicles of rose-purple. Leaves smell minty when rubbed. Drought resistant candidate for cut flowers. "
  "medicinal plant; honey-bee food plant / suitable for cutting", "中国"),
 (["Et01"], "ERAGROSTIS spectabilis", "cultivar", "USA", "bright rose-red", "August - October", "Z5 - Z10", "erect / clumping", "50 cm", "dry / sandy / well-drained / poor, lean", "",
  "Extremely drought tolerant grass. The bright rose-red colored inflorescence glows when backlit. Plant en masse in an open meadow or natural garden. "
  "Spreading slowly by rhizomes, and seeding where happy. One of the most attractive late flowering ornamental grasses, need a warm summer to flower. "
  "for the rock garden / suitable for cutting", "アメリカ"),
 (["Eo01"], "ERIOGONUM allenii 'Little Rascal'", "cultivar", "Virginia and West Virginia (USA)", "bright golden", "June - September", "Z5 - Z10", "erect / rosettes-forming", "40 cm",
  "dry / well-drained", "",
  "Astoundingly beautiful, rare, long flowering, drought-tolerant, durable species. Golden parasols. Great plant for bees and cut flowers. Plant in the rock garden, dry areas or "
  "mixed containers. Introduced by JELITTO PERENNIAL SEEDS in 2009. honey-bee food plant / for the rock garden / suitable for cutting",
  "アメリカ（バージニア・ウェストバージニア。種の原産地）"),
 (["Go01"], "GONIOLIMON collinum 'Sea Spray' (incanum)", "cultivar", "Balkan Peninsula and Eastern Romania", "white", "July - August", "Z5 - Z9",
  "rosettes-forming / clumping / vigorous", "40 cm", "dry / well-drained", "",
  "Lovely basal leaves of light bluish-green and sturdy sprays of tiny star-shaped white blooms. White umbels, richly branched, healthy foliage, strong habit. "
  "Introduced by JELITTO PERENNIAL SEEDS in 2007. for the rock garden / suitable for cutting", "バルカン半島・ルーマニア東部（種の原産地）"),
]
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes（試験地は USDA 5b）。pdftotext -raw で読んだ。
#   no20 Barrenworts（https://www.chicagobotanic.org/downloads/planteval_notes/no20_barrenworts.pdf）Table 1・Table 2 と本文。総合評価の星は記号が落ちて読めなかった。
#   no15 Goldenrods（no15_goldenrods.pdf）Table 1 と本文。'Gold Spangles' は試験に入っていない（斑入りの flexicaulis 'Variegata' は別の名前なので当てていない）。
#   no40 Rodgersias and Astilboides（no40_rodgersias_astilboides.pdf）Table 1 と本文。総合評価は星5つ（excellent）〜1つ（very poor）。
#     ロジャーシアの 'Scarlet'・'Bronze Beauty' は試験に入っていない（podophylla 'Bronze Form' は別の名前なので当てていない）。
#   no23 Lamiums（no23_lamiums.pdf）: Lamium galeobdolon は本文で名前が挙がるだけで、'Hermann's Pride' は試験に入っていない。
#   ほかの属の号は一覧（no1〜no40）にない。
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {
 "Em01": ("Epimedium ×rubrum", "cultivar", 14, 24, None, None, None,
          "花は赤（距は白）、花つき 20〜40%、花期は4月中旬〜5月中旬。春の葉は赤。本文で good の評価を受けた品種の1つに挙げられている。総合評価の星は読み取れなかった（no20）"),
 "Em02": ("Epimedium ×versicolor 'Sulphureum'", "cultivar", 13, 28, None, None, None,
          "花は黄、花つき 20〜40%、花期は4月下旬〜5月下旬。試験の間に、冬の傷みで1株が枯れた（近縁の 'Neosulphureum' は冬の強さが excellent、との比較の記述）。"
          "総合評価の星は読み取れなかった（no20）"),
 "So02": ("Solidago rugosa 'Fireworks'", "cultivar", 54, 76, None, None, None,
          "ソリダゴの試験で総合評価が最もよかった。花つき 80〜100%、花期は9月中旬〜10月下旬。茎は弓なりで株元は締まり、ゆっくり広がる。倒れなかった。"
          "うどんこ病は minor（1994・96・97年に出たが、葉の20%未満）、さび病なし、冬の傷みなし。春の葉はバーガンディ色（no15）"),
 "Ai01": ("Astilboides tabularis", "cultivar", 57, 30, None, None, None,
          "総合評価 ★3（fair）。花はクリーム白、花期は6月中旬〜7月中旬。葉の高さ 16 in・花茎を含めて 57 in。4月の第2週ごろに芽が出るので、"
          "2004・06・08・10・13年に新葉が遅霜で中〜重く傷んだ（50〜100%）。葉の幅は、ふつうの年は約12 in、春に雨の多い年は2フィートを超えた。試験全体で、冬に枯れた株はなかった（no40）"),
}
