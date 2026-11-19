# おぎはら植物園「おぎはら植物図鑑」（s20）: セダム・エキナセア・アスチルベ。2026-11-19 に読んだ（curl。やり方は batch_03/ogihara_data.py の冒頭）。
# 図鑑を セダム・ミセバヤ・キリンソウ・ベンケイソウ・エキナセア・アスチルベ で検索（掲載名 約170件）。一致は22ページ（品種・種あわせて26品種に当てた）。
# 図鑑は 'Dark Side of the Moon' を Astilbe chinensis、'Peach Blossom' を Astilbe rosea の品種と書いている（マスターはどちらも種小名なし）。
# D10（学名は 'Vera Jameson'、商品名は「セダム レフレクサム」）は、どちらの植物か分からないので当てていない（図鑑に「セダム レフレクサム」2881 はある）。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-19"
OGIHARA = [
 (["B01"], 3420, "アスチルベ ‘カラーフラッシュ ライム’ Astilbe 'Color Flash Lime'", "cultivar", "強", "やや半日陰",
  [("foliage", "夏以降は緑葉に変わるが、春の色の華やかさは一見の価値がある品種")]),
 (["B02"], 2145, "アスチルベ ‘ファナル’ Astilbe × arendsii 'Fanal'", "cultivar", "強", "日向～やや半日陰", [("habit", "株姿はコンパクトにまとまり、花つきが良い")]),
 (["B07"], 2807, "アスチルベ ‘スポットライト’ Astilbe 'Spotlight'", "cultivar", "強", "日向～やや半日陰", [("sun", "半日陰の場所でも咲く")]),
 (["B12"], 3315, "アスチルベ ‘ダークサイド オブザムーン’ Astilbe chinensis 'Dark Side of the Moon'", "cultivar", "強", "やや半日陰",
  [("habit", "成長はゆっくりだが、丈夫で着実に育つタイプ")]),
 (["B13"], 2715, "アスチルベ ‘デルフト レース’ Astilbe 'Delft Lace'", "cultivar", "強", "日向～やや半日陰", []),
 (["B14"], 2146, "アスチルベ ‘ピーチブロッサム’ Astilbe rosea'Peach Blossom'", "cultivar", "強", "日向～やや半日陰", [("habit", "性質も丈夫で育てやすい品種")]),
 (["D02"], 3344, "セダム(ベンケイソウ) ‘オータム ジョイ’ Sedum spectabile ‘Autumn Joy’", "cultivar", "強", "日向",
  [("heat_humidity", "弁慶の名のとおり強健で、暑さ寒さに耐え、肉厚な葉姿は乾燥にも強く、他の植物が育ちにくい環境下でも元気に育つ")]),
 (["D04"], 1079, "セダム(ミセバヤ) ‘バートラムアンダーソン’ Sedum(Hylotelephium) 'Bertram Anderson'", "cultivar", "強", "日向",
  [("drought", "乾燥に強いので乾燥地のカバーや吊り鉢などハンギング、寄せ植えもおすすめ"), ("seasonal_foliage", "特に低温の季節は葉色が黒っぽくなり美しい")]),
 (["D05"], 1081, "セダム(ベンケイソウ) ‘フロスティモーン’ Sedum(Hylotelephium) erythrostictum'Frosty Morn'", "cultivar", "強", "日向", []),
 (["D08"], 1083, "セダム(ベンケイソウ) ‘マトロナ’ Sedum telephium(Hylotelephium pallescens) 'Matrona'", "cultivar", "強", "日向",
  [("habit", "生育はとても早く強健で、特に育て易い")]),
 (["D13"], 3127, "ミセバヤ 斑入り Hylotelephium sieboldii 'Mediovariegatum'", "cultivar", "強", "日向",
  [("drought", "極めて乾燥に強く丈夫で多用途"), ("seasonal_foliage", "ピンクの花、秋冬の紅葉と楽しみも多く")]),
 (["D15"], 1092, "セダム(コーカサスキリンソウ) ‘ドラゴンズブラッド’ Sedum spurium 'Dragon's Blood'", "cultivar", "強", "日向",
  [("habit", "茎はよく分岐しカーペット状に地面を覆い、周年美しい色を保つので乾燥地のカバーに向く")]),
 (["D16"], 1094, "セダム(コーカサスキリンソウ) ‘トリカラー’ Sedum(Phedimus) spurium 'Tricolor'", "cultivar", "強", "日向",
  [("habit", "生育はゆっくりだが丈夫で、小スペースのグランドカバーや寄せ植えなどにおすすめ")]),
 (["E02"], 167, "エキナセア ‘オレンジパッション’ Echinacea purpurea 'Orange Passion'", "cultivar", "強", "日向", [("habit", "性質も強健")]),
 (["E04"], 156, "エキナセア パリダ Echinacea pallida", "cultivar", "強", "日向", [("cut_flower", "切花にも向く")]),
 (["E05"], 157, "エキナセア ‘フラダンサー’ Echinacea pallida 'Hula Dancer'", "cultivar", "強", "日向", []),
 (["E06"], 159, "エキナセア パラドクサ Echinacea paradoxa", "cultivar", "強", "日向", []),
 (["E08"], 161, "エキナセア ‘ファタル アトラクション’ Echinacea purpurea 'Fatal Attraction'", "cultivar", "強", "日向", []),
 (["E09"], 162, "エキナセア ‘グリーンエンビー’ Echinacea purpurea 'Green Envy'", "cultivar", "強", "日向", []),
 (["E10"], 163, "エキナセア ‘グリーンジュエル’ Echinacea purpurea 'Green Jewel'", "cultivar", "強", "日向", [("cut_flower", "夏の切花にとてもおしゃれ")]),
 (["E14"], 173, "エキナセア ‘バージン’ Echinacea purpurea 'Virgin'", "cultivar", "強", "日向", []),
 (["E07", "E11", "E12", "E13", "E15"], 152, "エキナセア パープレア Echinacea purpurea", "species", "強", "日向", [("heat_humidity", "暑さに強く夏によく咲く")]),
]
# 同じ種の別品種の値を、載っていない同種の品種に使う種（2026-11-19 のユーザーの決定に沿った試し。DECISIONS.md）。
# アレンジー（arendsii）は 'Color Flash Lime'・'Fanal' の2品種が 強。対象は B03・B04・B05。宿根フロックス（根拠2品種）と同じ形。
# チネンシスは根拠にできる品種が1つ（'Spotlight'）だけなので入れていない。
SIBLING = {"Astilbe arendsii": ("強", ["B01", "B02"])}
