# おぎはら植物園「おぎはら植物図鑑」（s20）: シレネ・ゲンチアナ・プルサティラ・ティアレラ・アルケミラ・アンドロポゴン・ヘデラ・リグラリア・パトリニア・プルネラ・トリキルティス・ハイドランジア・アストランティア。
# 2026-11-20 に読んだ（curl。scripts/tools/ogi_search.py と ogi_page2.py）。
# 図鑑を シレネ・ゲンチアナ・ゲンチアン・リンドウ・竜胆・プルサティラ・パルサティラ・プルサチラ・オキナグサ・翁草・ティアレラ・アルケミラ・アンドロポゴン・スキザクリウム・ジェラルディ・
#   ヘデラ・アイビー・キヅタ・リグラリア・メタカラコウ・オミナエシ・オトコエシ・プルネラ・ウツボグサ・ホトトギス・トリキルティス・杜鵑・アナベル・ノリウツギ・ミナヅキ・ヤマアジサイ・エゾアジサイ・アストランティア で検索。
# 一致は21ページ（24品種に当てた。ほかに同じ種の別品種のページを10読んだ）。
# 図鑑の書き方がマスターと違うもの: 'Prairie Blues' は Schizachyrium scoparius（マスターは Andropogon scoparius）、'Roma' は Astrantia major 'Rome'、
#   'Sugar and Spice' は Tiarella 'Suger and Spice'、'Annabelle' は Hydrangea arborescens 'Anabelle'、ヤマアジサイは Hydrangea macrophylla serrata、
#   Si02 は「シレネ ユニフロラ ‘バリエガータ’」と書いて学名は 'Druett's Variegated'、ウツボグサは「菊葉大輪ウツボグサ Prunella grandiflora」（葉の切れ込む系統の名前で載っている）。
# Hy03 はマスターの商品名に「ミナヅキ」とあるので、図鑑の ノリウツギ ‘ミナヅキ’（Hydrangea paniculata ‘Minazuki’）を品種のページとして当てた（マスターの学名は 'Grandiflora'）。
# 種のページを当てたもの: シレネ ディオイカ（Si01 'Jade Valley'）、オミナエシ（Pt02 'Nana'）、プルネラ グランディフローラ（Pv01・Pv02）、アストランティア マヨール（As04・As06）。
# 載っていないもの・当てていないもの: ゲンチアナ・プルサティラ・ヘデラ・ホトトギス（掲載なし）、ティアレラ 'Lacquer Leaf'、アルケミラ サクサティリス・'Gold Strike'、
#   プルネラ ブルガリス、'Cheju-do'・エゾアジサイ（ヤマアジサイの別の品種のページはどれも 強 だが、エゾアジサイは変種が違い、'Cheju-do' も含めて当てていない）。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-20"
S2 = "日向～やや半日陰"
HS = "やや半日陰"
_AST = (814, "アストランティア マヨール Astrantia major")
_ASM = [("heat_humidity", "暖地では水はけ良い土で植え夏は強乾燥に注意する 寒冷地では花期も長く放任でも大株に育て易い")]
OGIHARA = [
 (["Si01"], 880, "レッドキャンピオン(シレネ ディオイカ) Silene dioica", "species", "強", S2,
  [("heat_humidity", "とても丈夫で暑さ寒さに強く、株も残り、こぼれ種でも殖えるので放任でも群生し、たくさんの花を咲かせる"), ("self_seed", "こぼれ種でも殖えるので放任でも群生し")]),
 (["Si02"], 879, "シレネ ユニフロラ ‘バリエガータ’ Silene uniflora 'Druett's Variegated'", "cultivar", "中", HS,
  [("drought", "乾燥に強く砂礫地などのグランドカバーに有効"), ("pruning", "花後短く剪定すると姿良く咲き蒸れにくい")]),
 (["Si04"], 877, "シレネ ユニフロラ ‘ロゼア’ Silene uniflora 'Rosea'", "cultivar", "中", HS,
  [("pruning", "花がある程度咲き進んだら株元まで剪定すると姿良く次の花もきれいに咲き、繰り返し楽しめる")]),
 (["Si05"], 878, "シレネ ‘スワンレイク’ Silene uniflora 'Swan Lake'", "cultivar", "中", HS, [("habit", "ユニフロラの八重咲き種 シルバーの葉がコンパクトに生育する")]),
 (["Ti02"], 1275, "ティアレラ ‘ピンクスカイロケット’ Tiarella 'Pink Skyrocket'", "cultivar", "中", HS, []),
 (["Ti03"], 1278, "ティアレラ ‘シュガーアンドスパイス’(PVP) Tiarella 'Suger and Spice'", "cultivar", "中", HS, []),
 (["Ti04"], 1279, "ティアレラ ウェリー Tiarella wherryi", "cultivar", "中", HS, [("fragrance", "花には淡い香りがある")]),
 (["Al01"], 960, "アルケミラ モリス Alchemilla mollis", "cultivar", "中", HS, [("seasonal_foliage", "秋の紅葉も楽しめる")]),
 (["Ad03"], 1589, "スキザクリウム ‘プレーリーブルース’ Schizachyrium scoparius 'Prairie Blues'", "cultivar", "強", "日向",
  [("heat_humidity", "暑さ寒さに強く暖地から寒冷地まで植えられるブルー系の大型グラスは少なく貴重"), ("seasonal_foliage", "柔らかな穂と秋の赤い紅葉もきれい"), ("evergreen", "落葉性")]),
 (["Lg03"], 227, "リグラリア プルツェワルスキー Ligularia przewalskii", "cultivar", "中", "半日陰", [("soil", "やや湿った場所を好む")]),
 (["Pt01"], 2776, "オミナエシ Patrinia scabiosifolia", "cultivar", "強", "日向", [("evergreen", "落葉")]),
 (["Pt02"], 2776, "オミナエシ Patrinia scabiosifolia", "species", "強", "日向", []),
 (["Pt03"], 3009, "オトコエシ Patrinia villosa", "cultivar", "強", "日向", [("evergreen", "半常緑～落葉")]),
 (["Pv01", "Pv02"], 776, "菊葉大輪ウツボグサ Prunella grandiflora", "species", "中", "日向", [("spread_mode", "這うように広がり良く殖えるので、広い場所のグランドカバーによい")]),
 (["Hy01"], 1960, "アジサイ ‘アナベル’ Hydrangea arborescens 'Anabelle'", "cultivar", "強", HS,
  [("heat_humidity", "寒冷地でも暖地でも花つき良く強健"), ("pruning", "その年伸びた枝の先に花を付けるので、剪定は春芽吹くまで可能"), ("evergreen", "落葉樹")]),
 (["Hy03"], 1965, "ノリウツギ ‘ミナヅキ’ Hydrangea paniculata ‘Minazuki’", "cultivar", "強", HS,
  [("pruning", "新枝咲きで花後から冬まで剪定可能"), ("evergreen", "落葉樹")]),
 (["Hy05"], 2185, "ヤマアジサイ 紅(クレナイ) Hydrangea macrophylla serrata", "cultivar", "強", "半日陰",
  [("heat_humidity", "寒さ、暑さに強く日本中で栽培可能"), ("evergreen", "落葉樹")]),
 (["As01"], 817, "アストランティア ‘ハドスペンブラッド’ Astrantia major 'Hadspen Blood'", "cultivar", "中", HS, []),
 (["As02"], 821, "アストランティア ‘ローマ’ Astrantia major 'Rome'", "cultivar", "中", HS, [("habit", "生育が早く、大株に育てやすいので初心者の方にもおすすめの優良種")]),
 (["As03"], 823, "アストランティア ‘ルビーウエディング’ Astrantia major 'Ruby Wedding'", "cultivar", "中", HS, [("habit", "生育はゆっくり")]),
 (["As05"], 827, "アストランティア ‘ベニス’ Astrantia major 'Venice'", "cultivar", "中", HS, []),
 (["As04", "As06"], _AST[0], _AST[1], "species", "中", HS, _ASM),
]
# 同じ種の別品種の値を、載っていない同種の品種に使う種（2026-11-19 のユーザーの決定に沿った試し。DECISIONS.md）。
# シレネ ユニフローラ: 'Druett's Variegated'・'Rosea'・'Swan Lake'・'Alba'（ID 876）がどれも 中（対象は Si03 'Robin Whitebreast'）。
# アンドロポゴン スコパリウス: 'Prairie Blues'・'Chameleon'（ID 2824）・'Ha Ha Tonka'（ID 3460）がどれも 強（対象は Ad02 'Blaze'）。
# アンドロポゴン ジェラルディ: 'Red October'（ID 3045）・'Blackhawks'（ID 3461）がどちらも 強（対象は Ad01。種そのものを売っている商品）。
# リグラリア デンタータ: 'Britt-Marie Crawford'（ID 225）・'Midnight Lady'（ID 226）・'Pandora'（ID 2204）・'Garden Confetti'（ID 2527）がどれも 強（対象は Lg01 'Dark Beauty'・Lg02 'Orange Queen'）。
# ノリウツギ: 'Minazuki'・'Limelight'（ID 1966）がどちらも 強（対象は Hy02 'Aurea'）。
SIBLING = {"Silene uniflora": ("中", ["Si02", "Si04", "Si05", "図鑑の 'Alba'"]),
           "Andropogon scoparius": ("強", ["Ad03", "図鑑の 'Chameleon'", "図鑑の 'Ha Ha Tonka'"]),
           "Andropogon gerardii": ("強", ["図鑑の 'Red October'", "図鑑の 'Blackhawks'"]),
           "Ligularia dentata": ("強", ["図鑑の 'Britt-Marie Crawford'", "図鑑の 'Midnight Lady'", "図鑑の 'Pandora'", "図鑑の 'Garden Confetti'"]),
           "Hydrangea paniculata": ("強", ["Hy03", "図鑑の 'Limelight'"])}
