# おぎはら植物園「おぎはら植物図鑑」（s20）: スカビオサ・ポレモニウム・フィリペンデュラ・サンギソルバ・トロリウス。2026-11-20 に読んだ（curl。やり方は batch_03/ogihara_data.py の冒頭）。
# 図鑑を スカビオサ・松虫草・ポレモニウム・ハナシノブ・フィリペンデュラ・シモツケソウ・キョウガノコ・サンギソルバ・ワレモコウ・カライトソウ・トウチソウ・トロリウス・キンバイ で検索。一致は15ページ（15品種に当てた）。
# 図鑑の書き方がマスターと違うもの: 'Apricot Delight' は Polemonium carneum（マスターは caeruleum）、'Pink Tanna' は Sanguisorba tenuifolia（マスターは officinalis）、
#   'Cheddar' は Trollius x cultorum（マスターは種小名なし）、Fi04 は 'Venusta'（マスターは 'Venusta Magnifica'。RHS は同じ品種の別名としている）、
#   Sc02 は 'Perfecta'（マスターの学名は 'Blue Perfection'、商品名はパーフェクタ）、Sa07 は Sanguisorba tenuifolia var. alba。
# 載っていないもの: キョウガノコ、シモツケソウ 'Fuji Haze'、ウルマリア、カエルレウムのほかの品種、オクロレウカの種そのもの、ワレモコウのほかの種。'White Queen'（caucasica、耐暑性 中）は扱いのない品種。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-20"
OGIHARA = [
 (["Sc02"], 1116, "松虫草(スカビオサ) ‘パーフェクタ’ Scabiosa caucasica 'Perfecta'", "cultivar", "中", "日向～やや半日陰",
  [("habit", "日本の松虫草に比べ丈夫で宿根性なので育て易い")]),
 (["Sc07"], 1115, "松虫草(スカビオサ) ‘ムーンダンス’ Scabiosa ochroleuca 'Moon Dance'", "cultivar", "強", "日向～やや半日陰",
  [("habit", "コンパクトに育ち、ドーム状の美しい草姿になる"), ("cut_flower", "柔らかい色合いが切花にも人気")]),
 (["Pl03"], 909, "ハナシノブ ‘アプリコットデライト’ Polemonium carneum 'Apricot Delight'", "cultivar", "中", "やや半日陰", []),
 (["Pl07"], 914, "ハナシノブ ‘パープルレイン’ Polemonium yezoense 'Purple Rain'", "cultivar", "中", "やや半日陰",
  [("seasonal_foliage", "特に芽吹きや秋、冬は葉色が黒に近いほど濃く魅力的 気温が高くなるにつれ緑がかる")]),
 (["Pl01"], 913, "ハナシノブ ‘ヘブンリーハビット’ Polemonium boreale 'Heavenly Habit'", "cultivar", "中", "やや半日陰", [("habit", "コンパクトな草姿がかわいい小型のハナシノブ")]),
 (["Fi04"], 986, "フィリペンデュラ ‘ベヌスタ’ Filipendula rubra 'Venusta'", "cultivar", "中", "やや半日陰",
  [("habit", "大型で最終的に1m近い株張りになり、多数の花を上げ、とても見事")]),
 (["Sa07"], 989, "長穂シロワレモコウ(サンギソルバ アルバ) Sanguisorba tenuifolia var.alba", "cultivar", "強", "日向",
  [("pests", "性質は強健だがウドンコ病になりやすいので注意する")]),
 (["Sa05"], 987, "サンギソルバ ‘ピンクタンナ’ Sanguisorba tenuifolia 'Pink Tanna'", "cultivar", "強", "日向", [("heat_humidity", "寒さ暑さに強く丈夫で群生し、花立ちよくたくさん咲き美しい")]),
 (["Sa03"], 3337, "サンギソルバ メンジーシー Sanguisorba menziesii", "cultivar", "強", "日向～やや半日陰", [("habit", "性質は強健"), ("evergreen", "半常緑～落葉")]),
 (["Sa02"], 990, "カライトソウ Sanguisorba hakusanensis", "cultivar", "中", "やや半日陰", [("soil", "強乾燥に注意して育てる")]),
 (["Tr06"], 449, "トロリウス ‘チェダー’ Trollius x cultorum 'Cheddar'", "cultivar", "強", "やや半日陰", [("soil", "性質は強健だが、乾燥を嫌うのでやや湿った場所が良い")]),
 (["Tr03"], 450, "トロリウス ‘ニュームーン’ Trollius x cultorum 'New Moon'", "cultivar", "強", "やや半日陰", []),
 (["Tr05"], 2075, "トロリウス ヨーロパエウス Trollius europaeus", "species", "強", "やや半日陰", [("soil", "やや湿った場所を好み、場所が合うと一面に咲き揃い見事")]),
 (["Tr04"], 451, "トロリウス ‘レモンスプリーム’ Trollius europaeus 'Lemon Supreme'", "cultivar", "強", "やや半日陰", [("habit", "姿は小型で花は大輪の改良種で花つきも良く、草姿のまとまりが良い")]),
 (["Tr01"], 447, "カンムリキンバイ ‘ゴールデンクイーン’ Trollius chinensis 'Golden Queen'", "cultivar", "強", "やや半日陰", [("soil", "やや湿った場所を好む")]),
]
# 同じ種の別品種の値を、載っていない同種の品種に使う種（2026-11-19 のユーザーの決定に沿った試し。DECISIONS.md）。
# トロリウス カルトラムは 'New Moon'・'Cheddar' がどちらも 強（対象は Tr02 'Lemon Queen'）。
# スカビオサ コーカシカは 'Perfecta' と 'White Queen'（図鑑のID 1117。扱いのない品種）がどちらも 中（対象は Sc01・Sc03・Sc04）。
#   【見返すこと】これまでの対象はどれも 強 だった。中 を同じ扱いにしたのはここが初めて（耐暑性の最後の検討で見る）。
# オクロレウカの種そのもの（Sc06）は、同じ種のページが 'Moon Dance' の1つだけなので当てていない。
# ナガボノワレモコウ（tenuifolia）の 'Bordeaux'（Sa08）は、同じ種のページが変種 var. alba の1つだけなので当てていない。
SIBLING = {"Trollius cultorum": ("強", ["Tr03", "Tr06"]), "Scabiosa caucasica": ("中", ["Sc02", "図鑑の 'White Queen'"])}
