# おぎはら植物園「おぎはら植物図鑑」（s20）: エピメディウム・フラガリア・ヘレボルス・イベリス・リリオペ・リクニス・ムクデニア・ファラリス・フィソカルプス・ロジャーシア・ソリダゴと、
#   アクタエアからラミアストラムまでの1品種の属27（batch_16/input の38属）。
# 2026-11-20 に読んだ（curl。scripts/tools/ogi_search.py と ogi_page2.py）。図鑑を、属の学名38個と Lamium で検索。
# 一致は15ページ（16品種に当てた。ほかに同じ種・同じ属の別品種のページを42読んだ）。
# 図鑑の書き方がマスターと違うもの: 'Karasuba' は「カラスバ タンチョウソウ Mukdenia rossii 'Karasuba'」、エゴポディウムは Aegopodium podagraria 'Variegata'、
#   斑入りノブドウは Ampelopsis glandulosa 'Elegans'、アスチルボイデスは「タブラリス」、ベニチガヤは「紅チガヤ Imperata koenigii」（学名が違うが、和名で当てた）、
#   フィソカルプスは「アメリカコデマリ」、ヘレボルス アーグティフォリウスは「クリスマスローズ(原種) アーグティフォリウス (コルシカス)」。
# 種のページを当てたもの: ヘレボルス アーグティフォリウス（Hb01 'Janet Starnes'）、イベリス センパービレンス（Ib02 'Snow Cushion'）、ブルネラ マクロフィラ（Br01 'Silver Spear'）。
# 載っていないもの・当てていないもの: エピメディウム × rubrum・× versicolor（図鑑は別の交配の4ページ。どれも 中）、ワイルドストロベリーの2品種（'Golden Alexandria' の1ページだけ。強）、
#   ヘレボルス オリエンタリス（図鑑の実生は Helleborus × hybridus。中。マスターは orientalis なので当てていない）、
#   リリオペ（'Okina'・'Gin-ryū' はなし。ムスカリは下の SIBLING。スピカータは掲載なし）、リクニス コロナリア 'Alba'（下の SIBLING）・× haageana 'Molten Lava'、
#   ムクデニアの種そのもの（同じ種は 'Karasuba' の1ページだけ）、ファラリス（図鑑の2ページは Phalaris karka で、種が違う）、
#   ロジャーシア ピンナータ 'Scarlet'（下の SIBLING）・ポドフィラ 'Bronze Beauty'、ソリダゴ 'Gold Spangles'、アクタエア ヤポニカ、アルテア オフィシナリス（図鑑は cannabina）、
#   コルタデリア 'Mini Pampas'（下の SIBLING）、エラグロスティス スペクタビリス（図鑑は trichoides）、エリカ カルネア（図鑑は × griffithsii）、エリオゴヌム アレニー（図鑑は umbellatum）、
#   ユーオニマス 'Emerald Gaiety'（図鑑の fortunei は 'Dan's Delight' の1ページだけ）、ラミアストラム 'Herman's Pride'（図鑑の Lamium galeobdolon は別の系統の1ページだけ）、
#   アンドロサセ・アレナセルム・オーブリエタ・ビゲロウィア・ブフタルムム・デンドランセマ・エルショルチア・エリシマム・ゴニオリモン・ヘリアンサス・ヘリクトトリコン（掲載なし）。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-20"
S2 = "日向～やや半日陰"
HS = "やや半日陰"
OGIHARA = [
 (["Ai01"], 2143, "アスチルボイデス タブラリス Astilboides tabularis", "cultivar", "強", "半日陰", [("habit", "インパクトの強い超大型植物 フキに似た傘状の葉は、テーブルのように大きい")]),
 (["Ao01"], 804, "エゴポディウム ‘バリエガータ’ Aegopodium podagraria 'Variegata'", "cultivar", "強", HS,
  [("spread_mode", "極めて性質強健で地下茎で広がるようにふえる")]),
 (["Ap01"], 1995, "斑入りノブドウ ‘エレガンス’ Ampelopsis glandulosa 'Elegans'", "cultivar", "強", S2,
  [("evergreen", "落葉"), ("habit", "ツル性で3mぐらいまで伸び、フェンスなどにからませると良い")]),
 (["Au01"], 979, "アルンクス ‘ノーブルスピリット’ Aruncus aethusifolius 'Noble Spirit'", "cultivar", "中", HS,
  [("habit", "葉の切れ込みが細かく、コンパクトにこんもりと密生するので草姿だけでも充分に美しい")]),
 (["Br01"], 1163, "ブルネラ マクロフィラ Brunnera macrophylla", "species", "中", "半日陰", [("spread_mode", "地下茎で広がるように生育し半日陰のグランドカバーに良い")]),
 (["Ct01"], 69, "ルリマツリモドキ Ceratostigma plumbaginoides", "cultivar", "強", HS,
  [("evergreen", "落葉"), ("pruning", "花後に短く切り戻すと姿よく咲き繰り返し楽しめる"), ("spread_mode", "生育旺盛で育て易く地下茎で横に広がりグランドカバーに良い")]),
 (["Da01"], 1282, "ダルメラ ペルタータ Darmera peltata", "cultivar", "強", HS, [("soil", "やや湿ったところを好む")]),
 (["Hb01"], 371, "クリスマスローズ(原種) アーグティフォリウス (コルシカス) Helleborus argutifolius", "species", "強", "日向",
  [("evergreen", "常緑"), ("habit", "コルシカスとも呼ばれる木立ち性種(茎がある)")]),
 (["Ib01"], 2618, "イベリス センパービレンス Iberis sempervirens", "cultivar", "強", "日向",
  [("evergreen", "半常緑～落葉"), ("habit", "低くふんわりとした花姿で、グランドカバーや花壇の前方に最適 性質も強健で育てやすい")]),
 (["Ib02"], 2618, "イベリス センパービレンス Iberis sempervirens", "species", "強", "日向",
  [("evergreen", "半常緑～落葉"), ("habit", "低くふんわりとした花姿で、グランドカバーや花壇の前方に最適 性質も強健で育てやすい")]),
 (["Im01"], 1603, "紅チガヤ Imperata koenigii", "cultivar", "強", HS,
  [("evergreen", "落葉性"), ("spread_mode", "やや湿った場所に植えるとよく殖え、群生する様はとても美しい"), ("seasonal_foliage", "秋はさらに赤味を増し美しい")]),
 (["Lc02"], 886, "リクニス ‘エンジェルス ブラッシュ’ Lychnis coronaria 'Angel's Blush'", "cultivar", "強", "日向", [("habit", "フランネルソウの覆輪咲き")]),
 (["Mk02"], 2295, "カラスバ タンチョウソウ Mukdenia rossii 'Karasuba'", "cultivar", "強", HS,
  [("evergreen", "冬は落葉し、早春にいち早く花を咲かせる"), ("seasonal_foliage", "新葉が赤く、花も赤みを帯びる品種で、秋の紅葉も真っ赤になる"),
   ("heat_humidity", "暑さ、寒さ、乾燥、ある程度の湿気にも耐え、極めて丈夫")]),
 (["Pz01"], 2022, "アメリカコデマリ ‘ディアボロ’ Physocarpus opulifolius ‘Diabolo’", "cultivar", "強", "日向",
  [("evergreen", "落葉樹"), ("cut_flower", "花後に赤い実がつき、きれいなので切花用にも栽培される"), ("pruning", "剪定に強く形も自在で性質も強健")]),
 (["Pz02"], 2184, "アメリカコデマリ ‘サマーワイン’ Physocarpus opulifolius 'Summer Wine'", "cultivar", "強", "日向",
  [("evergreen", "落葉樹"), ("parentage", "本種は‘ディアボロ’の葉色が濃い個体と‘ナナ’という矮性種の交配種")]),
 (["So02"], 2671, "ソリダゴ ‘ファイヤーワークス’ Solidago rugosa 'Fireworks'", "cultivar", "強", S2, [("evergreen", "落葉"), ("habit", "背が高く、株立ちになり、晩夏から花穂を水平に伸ばして、次第に下垂する")]),
]
# 同じ種の別品種の値を、載っていない同種の品種に使う種（2026-11-19 のユーザーの決定に沿った試し。DECISIONS.md）。
# ヤブラン（Liriope muscari）: 'Variegated White'（ID 1316）・'Pure Blonde'（ID 1319）・'Peedee Ingot'（ID 3032）・'Monroe White'（ID 3200）がどれも 強（対象は Lr01 'Okina'）。
# リクニス コロナリア（Lychnis coronaria）: 'Angel's Blush'（ID 886）・'Gardeners World'（ID 888）・'Private Heaven'（ID 887）がどれも 強（対象は Lc01 'Alba'）。
# ロジャーシア ピンナータ（Rodgersia pinnata）: 'Chocolate Wing'（ID 1291）・'Bronze Peacock'（ID 2296）・'Die Schone'（ID 1292）・'Fireworks'（ID 1293）がどれも 中
#   （対象は Rg01 'Scarlet'）。同じ種の値を 中 で使うのは batch_07・11・12・14・15 に続いて6回目。
# パンパスグラス（Cortaderia selloana）: 'Evita'（ID 2929）・'Tiny Pampa'（ID 3341）・'Rosea'（ID 2827）・'White Feather'（ID 2828）がどれも 強（対象は Cd01 'Mini Pampas'）。
SIBLING = {"Liriope muscari": ("強", ["図鑑の 'Variegated White'", "図鑑の 'Pure Blonde'", "図鑑の 'Peedee Ingot'", "図鑑の 'Monroe White'"]),
           "Lychnis coronaria": ("強", ["図鑑の 'Angel's Blush'", "図鑑の 'Gardeners World'", "図鑑の 'Private Heaven'"]),
           "Rodgersia pinnata": ("中", ["図鑑の 'Chocolate Wing'", "図鑑の 'Bronze Peacock'", "図鑑の 'Die Schone'", "図鑑の 'Fireworks'"]),
           "Cortaderia selloana": ("強", ["図鑑の 'Evita'", "図鑑の 'Tiny Pampa'", "図鑑の 'Rosea'", "図鑑の 'White Feather'"])}
