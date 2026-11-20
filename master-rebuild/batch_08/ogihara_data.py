# おぎはら植物園「おぎはら植物図鑑」（s20）: タリクトラム・コレオプシス・リアトリス・リシマキア・ベロニカストラム・エリンジウム・ミスカンサス・モリニア。2026-11-20 に読んだ（curl）。
# 図鑑を タリクトラム・カラマツソウ・コレオプシス・ハルシャギク・リアトリス・リシマキア・クサレダマ・ベロニカストラム・クガイソウ・エリンジューム・ミスカンサス・ススキ・イトススキ・モリニア で検索。
# 一致は22ページ（27品種に当てた）。図鑑はエリンジウムを「エリンジューム」と書く（「エリンジウム」「エリンギウム」では出ない）。
# 図鑑の書き方がマスターと違うもの: Li07 'Kobold' は 'Goblin'（英語名）、Th04 は delavayi 'Alba'、Vs06 は 'Lavendeltrum'、Vs04 は 'Erica'、
#   Vs02 エゾクガイソウは Veronicastrum sachalinense（マスターは sibiricum var. yezoense）、Vs01 クガイソウは Veronicastrum japonicum（マスターは sibiricum。和名で当てた。要確認）。
# 載っていないもの: 'Thundercloud'・'Black Stockings'・'Elin'・ロチブルニエナム、'Firefly'・'Mercury Rising'・'American Dream'・'Moonbeam'・'Zagreb'（バーティシラータは種のページ）、
#   リアトリス ピクノスタキア・スピカータの種そのもの・'Floristan'、コンジェスティフロラ 'Variegata'・ヌンムラリアの種そのもの・クサレダマ、'Adoration'・アルビフローラム、
#   エリンジウム ユッキフォリウム、ススキの種そのもの・'Cosmopolitan'・'Little Zebra'・'Purpurascens'・イトススキ、モリニアの 'Variegata' 以外。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-20"
OGIHARA = [
 (["Th05"], 455, "黄花カラマツソウ (タリクトラム グラウカム) Thalictrum flavum ssp. glaucum", "cultivar", "中", "やや半日陰",
  [("habit", "背が高くなり茎も太く伸びるのでガーデンの背景におすすめ")]),
 (["Th01"], 2621, "カラマツソウ ‘パープレウム’ Thalictrum aquilegifolium ‘Purpureum’", "cultivar", "中", "やや半日陰", [("evergreen", "落葉")]),
 (["Th03"], 453, "カラマツソウ デラバイ Thalictrum delavayi", "cultivar", "中", "やや半日陰", [("cut_flower", "花もちがよく切り花にも向く")]),
 (["Th04"], 454, "カラマツソウ デラバイ ‘アルバ’ Thalictrum delavayi 'Alba'", "cultivar", "中", "やや半日陰", []),
 (["Co07"], 2543, "コレオプシス ‘スター クラスター’(PVP) Coreopsis 'Star Cluster'", "cultivar", "強", "日向～やや半日陰",
  [("heat_humidity", "暑さ、寒さに耐える宿根性の春車菊"), ("heat_humidity", "夏も冬も越す丈夫な性質"), ("evergreen", "落葉性")]),
 (["Co03"], 2688, "コレオプシス ‘レッド シフト’ Coreopsis 'Red Shift'", "cultivar", "強", "日向～やや半日陰",
  [("seasonal_foliage", "気温が下がり始める頃には、染物のように花全体を赤く変化させて季節感を楽しめる"), ("evergreen", "落葉")]),
 (["Co05", "Co06"], 228, "コレオプシス バーチキリアタ(糸葉春車菊) Coreopsis verticillata", "species", "強", "日向", [("spread_mode", "地下茎でよく殖え長期間咲く")]),
 (["Li02"], 3324, "リアトリス スカリオサ Liatris scariosa", "cultivar", "強", "日向", [("evergreen", "落葉性")]),
 (["Li03"], 3324, "リアトリス スカリオサ Liatris scariosa", "species", "強", "日向", []),
 (["Li07"], 2114, "リアトリス ‘ゴブリン’ Liatris spicata 'Goblin'", "cultivar", "強", "日向～やや半日陰",
  [("habit", "通常のリアトリスに比べ大きくならないドワーフタイプ"), ("cut_flower", "丈夫で放任でも毎年よく咲き、切り花にもできる")]),
 (["Ly06"], 2795, "リシマキア ‘アレキサンダー’ Lysimachia punctata 'Alexander'", "cultivar", "強", "日向～やや半日陰", [("evergreen", "落葉")]),
 (["Ly01"], 634, "リシマキア ‘ミッドナイトサン’ Lysimachia congestiflora 'Midnight Sun'", "cultivar", "強", "やや半日陰",
  [("spread_mode", "小さいブロンズ色の葉が這うように広がりグランドカバーに向く")]),
 (["Ly04"], 637, "リシマキア ヌムラリア ‘オーレア’ Lysimachia nummularia 'Aurea'", "cultivar", "強", "やや半日陰",
  [("spread_mode", "生育旺盛で、グランドカバーや雑草除けに良い"), ("soil", "特に多湿、日陰に強いので半日陰の湿気が多い場所など、他の植物が育ちにくい環境にも耐える")]),
 (["Ly05"], 639, "リシマキア プンクタータ Lysimachia punctata", "cultivar", "強", "やや半日陰", [("habit", "丈夫で土質も選ばないので、やや半日陰のグランドカバーに最適")]),
 (["Vs02"], 553, "エゾクガイソウ Veronicastrum sachalinense", "cultivar", "強", "日向", [("heat_humidity", "北海道産だが、耐暑性もあり強健な性質で育て易い")]),
 (["Vs01"], 552, "クガイソウ Veronicastrum japonicum", "cultivar", "強", "日向", [("native_range", "本州に広く分布し、山地や高原の日当たりの良い草地に生育する")]),
 (["Vs04"], 556, "西洋クガイソウ ‘エリカ’ Veronicastrum virginicum 'Erica'", "cultivar", "強", "日向", [("habit", "日本のクガイソウに比べてコンパクトに育ち、性質も丈夫")]),
 (["Vs05"], 554, "西洋クガイソウ ‘ファシネーション’ Veronicastrum virginicum 'Fascination'", "cultivar", "強", "日向",
  [("heat_humidity", "日本のクガイソウに比べ性質が強健で耐暑性に優れ、暖地でも栽培が可能")]),
 (["Vs06"], 555, "西洋クガイソウ ‘ラベンデルトルム’ Veronicastrum virginicum 'Lavendeltrum'", "cultivar", "強", "日向", [("habit", "性質も強健な優良品種")]),
 (["Er01"], 828, "エリンジューム プラナム Eryngium planum", "cultivar", "中", "日向～やや半日陰", [("evergreen", "寒さに強く冬も葉が残る"), ("self_seed", "こぼれ種でも殖える")]),
 (["Er02", "Er03", "Er04"], 828, "エリンジューム プラナム Eryngium planum", "species", "中", "日向～やや半日陰", []),
 (["Er05"], 836, "エリンジューム ‘ミスマーブル’(バリーフォリウム)", "cultivar", "中", "日向～やや半日陰", []),
 (["Mi04"], 1576, "ススキ ‘モーニングライト’ Miscanthus sinensis 'Morning Light'", "cultivar", "強", "日向",
  [("habit", "株が広がりすぎずコンパクトで植栽に使いやすい"), ("evergreen", "落葉性")]),
 (["Mo06"], 1585, "モリニア ‘バリエガータ’ Molinia caerulea 'Variegata'", "cultivar", "強", "日向",
  [("seasonal_foliage", "秋冬になると茎がさらに黄色く染まる"), ("evergreen", "落葉性")]),
]
# 同じ種の別品種の値を、載っていない同種の品種に使う種（2026-11-19 のユーザーの決定に沿った試し。DECISIONS.md）。
# 西洋クガイソウ（virginicum）は 'Erica'・'Fascination'・'Lavendeltrum' がどれも 強（対象は Vs03 'Adoration'・Vs07 アルビフローラム）。
# ススキ（sinensis）は 'Morning Light' と、扱いのない 'Purple Fall'（図鑑のID 1577）がどちらも 強（対象は Mi01・Mi02・Mi03・Mi05・Mi06）。
# 当てていないもの（同じ種のページが1つだけ）: アキレジフォリウム 'Thundercloud'、スピカータの Li04〜Li06（ページは 'Goblin' だけ）、
#   コンジェスティフロラ 'Variegata'、ヌンムラリアの種そのもの（ページは 'Aurea' だけ）、モリニアの Mo01〜Mo05（ページは 'Variegata' だけ）。
SIBLING = {"Veronicastrum virginicum": ("強", ["Vs04", "Vs05", "Vs06"]), "Miscanthus sinensis": ("強", ["Mi04", "図鑑の 'Purple Fall'"])}
