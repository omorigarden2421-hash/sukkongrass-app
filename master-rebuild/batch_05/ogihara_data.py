# おぎはら植物園「おぎはら植物図鑑」（s20）: ミント・ゲウム・ビンカ・プルモナリア・ペンステモン。2026-11-19 に読んだ（curl。やり方は batch_03/ogihara_data.py の冒頭）。
# 図鑑を ミント・メンタ・ゲウム・ダイコンソウ・ビンカ・ツルニチニチソウ・プルモナリア・ペンステモン で検索。一致は16ページ（品種・種あわせて24品種に当てた）。
# ミント（Mentha）は掲載なし（マウンテンミント・キャットミントは別の属）。
# 図鑑は 'Flames of Passion' を Geum rivale、'Blazing Sunset' を Geum quellyon の品種と書いている。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-19"
OGIHARA = [
 (["Ge04"], 3191, "ゲウム ‘ブレイジング サンセット’ Geum quellyon ‘Blazing Sunset’", "cultivar", "強", "日向",
  [("heat_humidity", "寒さ、暑さに耐え、大株になると無数の花が咲き、庭の主役級の華やかさがある")]),
 (["Ge06"], 2570, "ゲウム ‘フレームオブパッション’ Geum rivale 'Flames of Passion'", "cultivar", "強", "日向",
  [("habit", "リバレの改良品種なので、性質は極めて丈夫で草姿もコンパクトにまとまる"), ("evergreen", "半常緑～落葉")]),
 (["Ge07"], 968, "ゲウム ‘マイタイ’ Geum 'Maitai'", "cultivar", "強", "日向～やや半日陰", []),
 (["Ge09"], 969, "ゲウム リバレ Geum rivale", "cultivar", "強", "日向", [("habit", "低く広がるように生育し花茎をすっと伸ばし、うなずくように咲く")]),
 (["Ge10"], 970, "ゲウム リバレ ‘アルバ’ Geum rivale 'Alba'", "cultivar", "強", "日向", []),
 (["Pe03"], 569, "ペンステモン ‘ダーク タワーズ’ Penstemon digitalis 'Dark Towers'", "cultivar", "強", "日向",
  [("heat_humidity", "‘ハスカーレッド’によく似るが、高温時でも葉色がより濃く、花色がピンクで鮮やかな品種")]),
 (["Pe04"], 568, "ペンステモン ‘ハスカーレッド’ Penstemon digitalis 'Husker Red'", "cultivar", "強", "日向",
  [("heat_humidity", "数あるペンステモンの品種の中でも群を抜いて強健で暑さ寒さに強く、こぼれ種でも殖える")]),
 (["Pe05"], 567, "ペンステモン ヒルスタス Penstemon hirsutus", "cultivar", "強", "日向", [("soil", "水はけよく育てれば丈夫で長生きする")]),
 (["Pe06"], 3445, "ペンステモン ピグメウス Penstemon hirsutus var. pygmaeus", "cultivar", "強", "日向", [("habit", "小型のペンステモンで低く広がるように成長する")]),
 (["Pe07"], 3445, "ペンステモン ピグメウス Penstemon hirsutus var. pygmaeus", "species", "強", "日向", []),
 (["Pe08"], 564, "ペンステモン ‘サンバーストルビー’ Penstemon × mex.'Sunburst Ruby'", "cultivar", "強", "日向", []),
 (["Pe09"], 566, "ペンステモン ピニフォリウス Penstemon pinifolius", "cultivar", "強", "日向", [("heat_humidity", "暑さ寒さに強く丈夫で暖地では冬も常緑")]),
 (["Pu02"], 1162, "プルモナリア ‘ブルーエンサイン’ Pulmonaria 'Blue Ensign'", "cultivar", "中", "半日陰", []),
 (["Pu05"], 1160, "プルモナリア ‘ラズベリースプラッシュ’ Pulmonaria 'Raspberry Splash’", "cultivar", "中", "半日陰",
  [("habit", "ロンギフォリアの交配種でプルモナリアの中でも特に強健で育て易い")]),
 (["Pu11"], 3128, "プルモナリア オフィシナリス Pulmonaria officinalis", "species", "中", "半日陰", []),
 (["Vi01"], 236, "ツル日々草 ‘バリエガータ’ Vinca major 'Variegata'", "cultivar", "強", "日向～やや半日陰",
  [("habit", "生育旺盛で、ツルが横によく広がり、庭の下草やグランドカバーに良い")]),
 (["Vi02", "Vi03", "Vi04", "Vi05", "Vi06", "Vi07", "Vi08", "Vi09"], 2863, "姫ツル日々草(ビンカ ミノール) Vinca minor", "species", "強", "日向～やや半日陰",
  [("habit", "よく伸びるツルからも根を下ろし、広範囲のカバー、雑草除けに適している"), ("sun", "日陰にも耐え植木の下草にも良い"), ("evergreen", "半常緑")]),
]
# プルモナリアの交配品種（種小名なし）は、'Blue Ensign'・'Raspberry Splash' がどちらも 中。交配品種は「同じ種」とは言えないので SIBLING には入れていない。
