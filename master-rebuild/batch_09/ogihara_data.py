# おぎはら植物園「おぎはら植物図鑑」（s20）: モナルダ・トラデスカンティア・スピレア・ネペタ・アネモネ・アクイレギア・セントーレア・アジュガ。2026-11-20 に読んだ（curl）。
# 図鑑を モナルダ・トラデスカンチア・ムラサキツユクサ・シモツケ・コデマリ・ネペタ・キャットミント・アネモネ・シュウメイギク・秋明菊・オダマキ・セントーレア・ヤグルマ・アジュガ で検索。
# 一致は24ページ（29品種に当てた）。
# 図鑑の書き方がマスターと違うもの: 'Goldflame' は Spiraea x bumalda（マスターは japonica）、'Pink Candy' は Nepeta hybrida（マスターは nervosa）、
#   'Walker's Low' は Nepeta x faassenii（マスターは racemosa）、'Six Hills Giant' は Nepeta×fassenii（マスターは種小名なし）、'Chocolate Chip' は Ajuga tenorii（マスターは reptans）、
#   'Nora Barlow'・'Black Barlow' は Aquilegia vulgaris plena。
# 載っていないもの・当てていないもの: モナルダの各品種（図鑑は色別の「Monarda didyma×hybridus」だけ）・フィッツローサ・'Bee-Bright'、トラデスカンティアの 'Blue and Gold' 以外、
#   'Genpei'・'Magic Carpet'、ムッシーニアイ（図鑑の「ブルーキャットミント Nepeta hybrid」「ホワイトキャットミント Nepeta × fassenii 'alba'」は同じものか分からない）、
#   'Pink Cat'・'Blue Wonder'・'Felix'・'Dropmore'（ファッシニアイは種のページを当てた）、シュウメイギクの3品種（図鑑にあるのはスワンのシリーズなど別の品種）、ムルチフィダ 'Major'、
#   'Pink Lanterns'（ページはあるが Data の欄がない）、マクロセファラ。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-20"
S2 = "日向～やや半日陰"
OGIHARA = [
 (["Td04"], 848, "ムラサキツユクサ ‘ブルーアンドゴールド’ Tradescantia 'Blue and Gold'", "cultivar", "強", "やや半日陰",
  [("habit", "有名な‘スイートケイト’に比べて葉色がやや淡いライム色で、花色は、より青い")]),
 (["Sp02"], 1984, "黄金シモツケ ‘ゴールドフレーム’ Spiraea x bumalda 'Goldflame'", "cultivar", "強", "日向",
  [("seasonal_foliage", "春のはっきりした芽吹き色、濃いピンクの花、秋には全体が赤く紅葉し、四季を通して長く楽しめる"), ("pruning", "剪定次第で形も自在"), ("evergreen", "落葉樹")]),
 (["Sp04"], 2099, "コデマリ ‘ゴールド ファウンテン’ Spiraea × vanhouttei 'Gold Fountain'", "cultivar", "強", "日向", [("pruning", "性質がとても強健で、剪定にも強く樹形も自在")]),
 (["Sp05"], 1976, "コデマリ ‘ピンクアイス’ Spiraea × vanhouttei 'Pink Ice'", "cultivar", "強", "日向",
  [("pruning", "剪定に強く形も自在で切る度に美しい芽吹きが楽しめる"), ("evergreen", "落葉樹")]),
 (["Ne11"], 751, "ネペタ ‘ブルードリームス’ Nepeta subsessilis 'Blue Dreams'", "cultivar", "強", S2,
  [("habit", "北海道から四国まで自生する日本のネペタ、ミソガワソウの選抜改良種で性質が特に強健で育て易い")]),
 (["Ne07"], 747, "キャットミント ‘ピンクキャンディ’ Nepeta hybrida 'Pink Candy'", "cultivar", "強", S2, [("pruning", "花後短くカットすると繰り返し花を咲かせ初夏から秋まで長く楽しめる")]),
 (["Ne10"], 746, "ブルーキャットミント ‘ウォーカーズロウ’ Nepeta x faassenii 'Walker's Low'", "cultivar", "強", S2,
  [("heat_humidity", "シナモンの香りがし、丈夫で暑さ寒さに強く良く育つ"), ("pruning", "花後短く切り戻すと姿良く繰り返し咲く")]),
 (["Ne04"], 749, "ブルーキャットミント ‘シックスヒルズジャイアント’ Nepeta×fassenii 'Six Hills Giant'", "cultivar", "強", S2,
  [("habit", "大型で背が高くなり花茎が立つので、すっきりとした草姿が美しい 丈夫で生育も早い")]),
 (["Ne03"], 2275, "ブルーキャットミント ‘ジュニア ウォーカー’ Nepeta x faassenii 'Junior Walker'", "cultivar", "強", S2,
  [("habit", "人気種‘ウォーカーズロウ’の小型改良種で丈が低く、花穂も短く密に咲く")]),
 # 2026-11-27 Ne09 'Blue Wonder' は種が × faassenii になったので、この種のページも当てた（図鑑に 'Blue Wonder' のページはない）
 (["Ne02", "Ne09"], 750,"ブルーキャットミント ファッシニー Nepeta × faassenii", "species", "強", "日向", [("pruning", "キャットミントは花後短く切り戻すと姿良く繰り返し花を咲かせる")]),
 (["An06"], 238, "アネモネ ムルチフィーダ ‘ルブラ’ Anemone multifida 'Rubra'", "cultivar", "中", S2, []),
 (["An04"], 243, "アネモネ レベイレイ Anemone leveillei", "cultivar", "中", S2, [("evergreen", "冬は完全に落葉する")]),
 (["Aq03"], 442, "オダマキ ‘イエロークイーン’ Aquilegia chrysantha 'Yerrow Queen'", "cultivar", "中", "やや半日陰", [("habit", "生育旺盛の早い強健種")]),
 (["Aq01"], 444, "オダマキ ‘コルベット' Aquilegia canadensis 'Corbett'", "cultivar", "中", "やや半日陰", [("habit", "カナダオダマキの小型改良種")]),
 (["Aq04"], 432, "オダマキ ‘ノラバロー’ Aquilegia vulgaris plena 'Nora Barlow'", "cultivar", "中", "やや半日陰", []),
 (["Aq06"], 431, "オダマキ ‘ブラックバロー’ Aquilegia vulgaris plena 'Black Barlow'", "cultivar", "中", "やや半日陰", [("self_seed", "各種こぼれ種でも殖える")]),
 (["Ce01"], 216, "セントーレア デルバータ Centaurea dealbata", "cultivar", "強", S2,
  [("heat_humidity", "暑さ、寒さに強く、とても丈夫で育てやすい"), ("habit", "長寿命の多年草で、株が劣化しにくく、年々株が大きく育ち、花数も増えていく")]),
 (["Ce06"], 2261, "セントーレア プルケリマ Centaurea pulcherrima", "cultivar", "中", S2, [("heat_humidity", "やや乾き気味の場所を好み、多湿に注意する")]),
 (["Ce03"], 208, "セントーレア モンタナ Centaurea montana", "cultivar", "中", "日向", [("drought", "乾燥にも耐える強健種")]),
 (["Ce04"], 209, "セントーレア モンタナ ‘アルバ’ Centaurea montana 'Alba'", "cultivar", "中", "日向", []),
 (["Ce05"], 208, "セントーレア モンタナ Centaurea montana", "species", "中", "日向", []),
 (["Aj01"], 761, "アジュガ ‘ブラックスカロップ’ Ajuga reptans 'Black Scallop'", "cultivar", "強", S2,
  [("spread_mode", "繁殖枝の伸びがコンパクトで徒長せず、まとまりのある姿")]),
 (["Aj02"], 758, "アジュガ ‘バーガンディグロー’ Ajuga reptans 'Burgundy Glow'", "cultivar", "強", S2, [("evergreen", "夏はシルバー、秋はピンクに変化し、冬も常緑で美しく周年楽しめる")]),
 (["Aj03"], 762, "アジュガ ‘チョコレートチップ’ Ajuga tenorii 'Chocolate Chip'", "cultivar", "強", S2, [("habit", "紫葉の小型種 株が密に茂り、花つき良く美しい")]),
 (["Aj05"], 764, "アジュガ ‘バニラチップ’ Ajuga reptans 'Vanilla Chip'", "cultivar", "強", S2, [("habit", "基本種に比べ生育は遅いので寄せ植えなどにも良い")]),
 (["Aj04"], 756, "アジュガ レプタンス Ajuga reptans", "species", "強", S2, [("spread_mode", "旺盛にほふく枝を出し地面を覆いグランドカバーに最適")]),
]
# 同じ種の別品種の値を、載っていない同種の品種に使う種（2026-11-19 のユーザーの決定に沿った試し。DECISIONS.md）。
# モナルダ ディディマ: 図鑑の「モナルダ レッド・パープル・ピンク・ホワイト」（Monarda didyma×hybridus。ID 789・790・791・793）がどれも 強（対象は Mn01〜Mn04）。
# トラデスカンティア アンダーソニアナ: 'Blue and Gold' と 'Sweet Kate'（ID 2963）がどちらも 強（対象は Td01・Td02。種小名なしの Td03・Td05・Td06 には当たらない）。
# シモツケ（japonica）: 'Goldflame'・'Limemound'（ID 1985）・'White Gold'（ID 1986）がどれも 強（対象は Sp01・Sp03）。
# オダマキ ブルガリス: 'Nora Barlow'・'Black Barlow'・'Blue Barlow'（ID 428）・'Rose Barlow'（ID 433）がどれも 中（対象は Aq05 'Bordeaux Barlow'）。
SIBLING = {"Monarda didyma": ("強", ["図鑑の モナルダ レッド・パープル・ピンク・ホワイト"]),
           "Tradescantia andersoniana": ("強", ["Td04", "図鑑の 'Sweet Kate'"]),
           "Spiraea japonica": ("強", ["Sp02", "図鑑の 'Limemound'・'White Gold'"]),
           "Aquilegia vulgaris": ("中", ["Aq04", "Aq06", "図鑑の 'Blue Barlow'・'Rose Barlow'"])}
