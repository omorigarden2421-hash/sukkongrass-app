# 3属の試行: Jelitto（s11）とシカゴ植物園の評価報告（s08）から読んだ内容。2026-11-19。
CHECKED = "2026-11-19"

# ---------- Jelitto ----------
# ユーザーのパソコンの Chrome で読んだ。サイト内検索の掲載名は Geranium 20件・Veronica 28件・Hosta 3件。
# 試行の品種と一致したのは下の11ページ（品種のページは V02 と V11 だけ、あとは種のページ）。Hosta は一致なし。
# キー: 試行ID のリスト。値: (Jelitto の表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
J_URL = "https://www.jelitto.com/Seed/Perennials/"
JELITTO = [
 (["G02"], "GERANIUM endressii", "species", None, "pink", "May - September", "Z4 - Z7", None, "30 cm", "average",
  "full sun, semi-shade, light shade", "groundcover", None),
 (["G12", "G13", "G14"], "GERANIUM macrorrhizum wild form", "species", "Central Europe to the Balkan peninsula", "purple-red", "May - August", "Z3 - Z8",
  "stoloniferous", "30 cm", "dry / alkaline / average / undemanding", "full sun, semi-shade, light shade",
  "groundcover; for the rock garden; sticky leaves turn red in autumn; A durable groundcover for tough conditions or the woodland garden.",
  "中央ヨーロッパ〜バルカン半島"),
 (["G17"], "GERANIUM phaeum f. albiflorum (Album)", "species", None, "pure white", "May - September", "Z5 - Z8", None, "60 cm", "moist / average",
  "semi-shade", "groundcover", None),
 (["G21"], "GERANIUM pratense", "species", None, "violet-red", "June - August", "Z4 - Z8", None, "50 cm", "well-drained / average",
  "full sun, semi-shade", "groundcover", None),
 (["V03"], "VERONICA chamaedrys", "species", None, "brilliant blue", "May - July", "Z5 - Z8", "stoloniferous / repent", "25 cm", "dry / average",
  "full sun, semi-shade", "medicinal plant; honey-bee food plant; for the rock garden", None),
 (["V05"], "VERONICA incana (spicata ssp. incana)", "species", "Eastern Europe to Central Asia: steppes.", "blue", "June - July", "Z3 - Z9",
  "stoloniferous / mat-forming", "40 cm", "dry / well-drained / average / poor, lean", "full sun",
  "ornamental foliage plant; groundcover; honey-bee food plant; for the rock garden; Foliage: silver-gray", "東ヨーロッパ〜中央アジアの草原（ステップ）"),
 (["V06"], "VERONICA longifolia (maritima, PSEUDOLYSIMACHION)", "species",
  "North, East and Central Europe, Siberia and East Asia: damp meadows, riparian forests.", "deep blue", "June - August", "Z4 - Z9", None, "80 cm",
  "moist / average", "full sun", "honey-bee food plant; suitable for cutting", "北・東・中央ヨーロッパ、シベリア、東アジアの湿った草地・河畔林"),
 (["V07", "V08", "V09"], "VERONICA prostrata", "species", None, "light blue, rarely pink", "May - June", "Z3 - Z8", "stoloniferous", "15 cm", "average",
  "full sun, semi-shade", "groundcover; for the rock garden", None),
 (["V10", "V12", "V13", "V14", "V15", "V16", "V17"], "VERONICA spicata", "species", "Europe, Eastern and Central Asia: grassland, rocky steppes.", "blue",
  "July - September", "Z3 - Z8", None, "60 cm", "dry / well-drained", "full sun", "groundcover; honey-bee food plant; suitable for cutting",
  "ヨーロッパ、東・中央アジアの草地・岩の多い草原"),
 (["V11"], "VERONICA spicata 'Alba'", "cultivar", "Europe, Eastern and Central Asia: grassland, rocky steppes.", "pure white", "July - September", "Z3 - Z8",
  None, "60 cm", "dry / well-drained", "full sun", "groundcover; honey-bee food plant; for the rock garden; suitable for cutting",
  "ヨーロッパ、東・中央アジアの草地・岩の多い草原"),
 (["V02"], "VERONICA teucrium 'Royal Blue' (austriaca ssp. teucrium) [Königsblau]", "cultivar",
  "Central Europe, Balkans, Eastern Europe to Eastern Siberia: nutrient poor meadows, woodland edges, open woodland.", "bright blue", "June - August",
  "Z4 - Z8", "clumping / bushy", "40 cm", "dry / well-drained / average / poor, lean", "full sun, semi-shade",
  "groundcover; honey-bee food plant; patio plant; suitable for cutting", "中央ヨーロッパ、バルカン、東ヨーロッパ〜東シベリアのやせた草地・林縁"),
]
# Jelitto にあるが、同じ品種か分からないので使っていない: spicata f. nana 'Blauteppich'（V14 'Nana' の候補）、spicata 'Pink Goblin' [Rosenrot]（V17 'Rose' の候補）
# 試作で読み済み: GERANIUM phaeum（種。試作 P21）

# ---------- シカゴ植物園 Plant Evaluation Notes 22（2004）Hardy Geraniums for Northern Gardens ----------
# https://www.chicagobotanic.org/downloads/planteval_notes/no22_geraniums.pdf の Table 1 から。試験地は USDA 5b。
# 総合評価（星）は記号で、文字として取り出せなかったので入れていない。
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 花後の切り戻し)
# 切り戻し: Yes+＝花後に切り戻し、2〜3週間で姿と健康が良くなった／Yes-＝切り戻したが改善なし／No+・No-＝切り戻していない／NR＝記録なし
CBG_URL = "https://www.chicagobotanic.org/downloads/planteval_notes/no22_geraniums.pdf"
CBG = {
 "G01": ("×cantabrigiense 'Biokovo'", "cultivar", None, None, "red, burgundy", None),
 "G02": ("endressii", "species", None, None, "none observed", None),
 "G03": ("himalayense", "species", 15, 20, None, "Yes-"),
 "G05": ("'Blue Sunrise' ('Verguld Saffier')", "cultivar", 24, 36, "none observed", "Yes+"),
 "G07": ("×oxonianum 'Katherine Adele'", "cultivar", 14, 22, "none observed", "Yes+"),
 "G11": ("'Johnson's Blue'", "cultivar", 24, 33, "red", "Yes+"),
 "G14": ("macrorrhizum 'Spessart'", "cultivar", 10, 27, "orange", "NR"),
 "G15": ("×oxonianum 'Wargrave Pink'", "cultivar", 14, 20, "red, orange", "No-"),
 "G20": ("phaeum 'Samobor'", "cultivar", 12, 45, "red, purple", "Yes+"),
 "G22": ("sanguineum 'Album'", "cultivar", 8, 15, "purplish", "No-"),
 "G23": ("sanguineum 'Max Frei'", "cultivar", 21, 32, "red, purple", "No+"),
 "G24": ("sanguineum 'New Hampshire Purple'", "cultivar", 20, 31, "red", "No+"),
 "G25": ("sanguineum var. striatum", "cultivar", 6, 17, "red", "No+"),
 "G26": ("sanguineum var. striatum", "cultivar", 6, 17, "red", "No+"),
}
AUTUMN = {"red": "赤", "burgundy": "バーガンディ", "orange": "オレンジ", "purple": "紫", "purplish": "紫がかる", "yellow": "黄", "golden-yellow": "黄金色"}
# ベロニカの報告（Plant Evaluation Notes 33, no33_veronica.pdf）もあるが、表が文字として崩れて取り出せなかった。PDF を目で読む必要がある。
# ホスタの評価報告は見つからなかった。'Bevan's Variety' は報告で「incorrect plant（別の植物だった）」とされ、値がない。
