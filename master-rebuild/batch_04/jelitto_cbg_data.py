# Jelitto（s11）とシカゴ植物園（s08）: セダム・エキナセア・アスチルベ。
# Jelitto は 2026-11-19 にユーザーのパソコンの Chrome（Claude in Chrome）で読んだ。探し方は batch_03/jelitto_cbg_data.py と同じ
#   （英語のサイト内検索: Echinacea 37件・Sedum 51件・Astilbe 6件）。一致は9ページ。確認画面が一度出たが、待つと自動で通った。
# 'Hula Dancer'（2006）は Jelitto が発表した品種（育種会社 s12 と同じ扱いにできる）。'Magnus' は試作 P12 と同じ品種。
# アスチルベ チネンシスの5品種には種のページを、'Superba' には変種 taquetii のページを当てた。'Showstar' は種子系の品種（混合色）。
# 読んでいないもの: SEDUM ussuriense（D18 'Pink Beacon' の種のページ）。背の高いセダム・スプリウムの品種は掲載なし。日照の欄は記号で読めなかった。
# シカゴ植物園: Plant Evaluation Notes の一覧（no1〜no40）に、セダム・エキナセア・アスチルベの号はない（no38 は屋上緑化の植物で、対象の品種は未確認）。
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-19"
JELITTO = [
 (["B04"], "ASTILBE arendsii 'Showstar'", "cultivar", None, "red, pink, cream to white", "June - August", "Z4 - Z8", "compact / bushy", "35 cm",
  "avoid lime / average / humus rich, fertile", "", "decorative fruit / groundcover; suitable for cutting / flowering pot plant", None),
 (["B06", "B07", "B08", "B09", "B10"], "ASTILBE chinensis", "species", "China, Japan", "lilac-rose", "July - September", "Z3 - Z8", "erect / rhizomatous / richly branched", "60 cm",
  "avoid lime / average / humus rich, fertile", "", "decorative fruit / groundcover; suitable for cutting", "中国、日本"),
 (["B11"], "ASTILBE chinensis var. taquetii", "species", None, "lilac shades", "", "Z3 - Z8", "erect / rhizomatous / richly branched", "100 cm",
  "avoid lime / moist / average / humus rich, fertile", "", "Tolerates dryness better than other Astilbes. decorative fruit / groundcover; suitable for cutting", None),
 (["D11", "D12"], "SEDUM kamtschaticum", "species", None, "orange-yellow", "August - September", "Z4 - Z9", "stoloniferous", "15 cm", "dry / average", "",
  "Award of Garden Merit (A.G.M.) from the Royal Horticultural Society. groundcover; honey-bee food plant / for the rock garden", None),
 (["E04"], "ECHINACEA pallida", "species", "Midwestern United States", "pale rose", "July - September", "Z3 - Z8", "erect", "80 cm", "well-drained / average", "",
  "Unusual narrow drooping pale-pink petals. With whitish pollen. Cutflowers keep well. medicinal plant; honey-bee food plant", "アメリカ中西部"),
 (["E05"], "ECHINACEA pallida 'Hula Dancer'", "cultivar", "Great Plains (Central USA)", "white with pink tinge", "July - September", "Z3 - Z8", "erect / slender, narrow", "80 cm",
  "well-drained / average", "",
  "Introduced by JELITTO PERENNIAL SEEDS in 2006. Slender upright stems - without branching. Cut flower candidate, deer and drought resistant, attract butterflies. honey-bee food plant / suitable for cutting",
  "アメリカ中部のグレートプレーンズ（種の原産地）"),
 (["E06"], "ECHINACEA paradoxa var. paradoxa", "species", "Rocky slopes in Missouri, Arkansas, Kansas, Oklahoma and Texas.", "bright yellow", "July - October", "Z4 - Z9", "erect", "80 cm",
  "well-drained / average", "", "honey-bee food plant / suitable for cutting", "ミズーリ・アーカンソー・カンザス・オクラホマ・テキサスの岩の多い斜面"),
 (["E07", "E08", "E09", "E10", "E12", "E13", "E14", "E15"], "ECHINACEA purpurea", "species", None, "purple-rose", "July - September", "Z3 - Z8", "", "100 cm", "well-drained / average", "",
  "medicinal plant; honey-bee food plant", None),
 (["E11"], "ECHINACEA purpurea 'Magnus'", "cultivar", "North America (Ohio and Michigan south to Georgia, west to Oklahoma and northeast to Texas)", "", "", "", "", "", "", "",
  "Award of Garden Merit (A.G.M.). Perennial Plant of the Year 1998 (PPA). The rose-purple flowers are arranged more horizontally than the pendulous, or drooping, habit of the wild species. Durable, low maintenance perennial. Very long lasting as cut-flower. The result of over ten years of careful selection by Swedish nurseryman, Magnus B. Nilsson.",
  "北アメリカ（オハイオ・ミシガンからジョージア、西はオクラホマ、テキサス北東部。種の原産地）"),
]
AUTUMN = {}
CBG = {}
CBG_V = {}
