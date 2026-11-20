# おぎはら植物園「おぎはら植物図鑑」（s20）: ジギタリス・プリムラ・ユーパトリウム・ベルゲニア・カラマグロスティス・デスカンプシア・フクシア・アイリス・ロニセラ。
# 2026-11-20 に読んだ（curl。scripts/tools/ogi_search.py と ogi_page2.py）。
# 図鑑を ジギタリス・プリムラ・クリンソウ・サクラソウ・ユーパトリウム・フジバカマ・ヒヨドリ・ベルゲニア・ヒマラヤユキノシタ・カラマグロスティス・ノガリヤス・ヤマアワ・
#   デスカンプシア・デシャンプシア・フクシア・フクシャ・ホクシア・マゼラニカ・アイリス・アヤメ・イリス・シビリカ・ショウブ・ロニセラ・スイカズラ・ハニーサックル・エメイ で検索。
# 一致は24ページ（24品種に当てた。ほかに同じ種の別品種のページを6つ読んだ）。
# 図鑑の書き方がマスターと違うもの: 'Pink Frost' は Eupatorium × arakianum（サワフジバカマ。マスターは fortunei）、'Milk Chocolate' は品種名を学名に書かず Digitalis parviflora、
#   セレスチナムは Eupatorium coelestinum(=Conoclinium coelestinum)。
# 載っていないもの・当てていないもの: ジギタリス 'Elsie Kelsey'・'Excelsior'、プリムラ コルツソイデス・デンティキュラータ・'Green Lace'（'Gold Lace' は別の品種）、
#   ユーパトリウム アルブム、ベルゲニアの種そのもの・'Redstart'・エメイエンシス（図鑑の「実生系」は Bergenia ×Hybrids で、コーディフォリアのページではないので当てていない）、
#   カラマグロスティス エピジジョス、デスカンプシア・フクシア・アイリス（該当の掲載なし。アイリスは tuberosa だけ）、ロニセラ 'Honey Baby'。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-20"
S2 = "日向～やや半日陰"
HS = "やや半日陰"
OGIHARA = [
 (["Dg01"], 524, "ジギタリス グランデフロラ Digitalis grandiflora", "cultivar", "中", "日向", []),
 (["Dg02"], 2697, "ジギタリス ルテア Digitalis lutea", "cultivar", "中", S2, [("habit", "何年も宿根する長寿命な原種で毎年よく咲く")]),
 (["Dg03"], 519, "ジギタリス メルトネンシス Digitalis × mertonensis", "cultivar", "中", "日向",
  [("heat_humidity", "普通種(パープレア系)に比べ耐暑性もあり育て易い")]),
 (["Dg04"], 525, "ジギタリス ‘ミルクチョコレート’ Digitalis parviflora", "cultivar", "中", "日向", []),
 (["Dg05"], 512, "ジギタリス ‘アプリコット’ Digitalis purpurea 'Apricot'", "cultivar", "中", "日向", []),
 (["Dg08"], 3069, "ジギタリス ‘モンストローサ・パープル’ Digitalis purpurea 'Monstrosa Purple'", "cultivar", "中", "日向", [("evergreen", "常緑～半常緑")]),
 (["Dg09"], 3068, "ジギタリス ‘モンストローサ・ホワイト’ Digitalis purpurea 'Monstrosa White'", "cultivar", "中", "日向", [("evergreen", "常緑～半常緑")]),
 (["Dg10"], 513, "ジギタリス ‘スノーシンブル’ Digitalis purpurea 'Snow Thimble'", "cultivar", "中", "日向", [("self_seed", "冷涼地ではこぼれ種でもよく殖える")]),
 (["Pr03"], 592, "白花クリンソウ Primula japonica 'Alba'", "cultivar", "中", HS, []),
 (["Pr04"], 593, "クリンソウ ‘アップルブロッサム’ Primula japonica 'Appleblossom'", "cultivar", "中", HS, [("soil", "やや湿った場所を好む")]),
 (["Pr05"], 590, "クリンソウ Primula japonica", "species", "中", HS, []),
 (["Pr07"], 594, "プリムラ ベリス Primula veris", "cultivar", "中", HS, [("fragrance", "花には芳香がある"), ("habit", "強健でよく殖える野生の桜草")]),
 (["Ep02"], 204, "ユーパトリウム セレスチナム Eupatorium coelestinum(=Conoclinium coelestinum)", "cultivar", "強", "日向",
  [("heat_humidity", "暑さ寒さに強く丈夫で地下茎で広がるように生育する"), ("spread_mode", "地下茎で広がるように生育する 一面に咲きグランドカバーに良い")]),
 (["Ep03"], 2540, "ユーパトリウム ‘アイボリー タワー’ Eupatorium fistulosum f. albidum 'Ivory Towers'", "cultivar", "強", S2,
  [("pruning", "初夏に咲き、切り戻しておくと秋も咲く"), ("evergreen", "落葉性")]),
 (["Ep04"], 2541, "ユーパトリウム ‘ピンク フロスト’ Eupatorium × arakianum 'Pink Frost'", "cultivar", "強", S2,
  [("habit", "原種のフジバカマ同様に丈夫でよく育つ"), ("evergreen", "落葉性")]),
 (["Ep06"], 2684, "ユーパトリウム ‘レッド ドワーフ’ Eupatorium maculatum 'Red Dwarf'", "cultivar", "強", S2,
  [("habit", "大型の種類が多い中、本種は比較的小型の品種"), ("evergreen", "落葉")]),
 (["Bg04"], 3130, "ヒマラヤユキノシタ ‘スノー タイム’ Bergenia cordifolia 'Snow Time'", "cultivar", "強", HS,
  [("evergreen", "常緑性の厚い葉をもち、周年常緑"), ("spread_mode", "徐々に広がっていく多年草なので、半日陰のカバーなどに良い")]),
 (["Cg02"], 2890, "カラマグロスティス ‘カール フォースター’ Calamagrostis x acutiflora 'Karl Foerster'", "cultivar", "強", "日向",
  [("habit", "茎、穂が直立する、すっきりとした姿の品種"), ("evergreen", "落葉性")]),
 (["Cg03"], 2316, "カラマグロスティス ‘オーバーダム’ Calamagrostis x acutiflora 'Overdam'", "cultivar", "強", "日向",
  [("habit", "茎、穂が直立する、姿の美しいグラス シャープな葉には斑が入り、カラーリーフとして楽しめる"), ("evergreen", "落葉性")]),
 (["Cg04"], 2152, "カラマグロスティス ブラキトリカ Calamagrostis brachytricha", "cultivar", "強", "日向",
  [("habit", "耐寒性も強く寒冷地の植栽にも良い"), ("evergreen", "落葉性")]),
 (["Lo01"], 1906, "ハニーサックル アメリカーナ Lonicera ×americana", "cultivar", "強", "日向",
  [("habit", "ハニーサックルの中で最も強健と言われるほど丈夫"), ("fragrance", "花つき良く株全体を覆うように咲き見事で良い香りを漂わせる"), ("evergreen", "半常緑～落葉")]),
 (["Lo02"], 1916, "ハニーサックル ‘ハーレクイン’ Lonicera × italica 'Harlequin'", "cultivar", "強", "日向",
  [("fragrance", "花は外側が淡いピンクを帯び、内側が白で香りも良い"), ("evergreen", "常緑～半常緑")]),
 (["Lo04"], 1913, "ハニーサックル ‘セロティナ’ Lonicera periclymenum 'Serotina'", "cultivar", "強", "日向",
  [("fragrance", "ツルの伸びが早く、花の香りも良い"), ("evergreen", "半常緑～落葉")]),
 (["Lo05"], 1914, "ハニーサックル テルマニアナ Lonicera × tellmanniana", "cultivar", "強", "日向",
  [("fragrance", "香りは僅かだが、ツルの伸びが早く、性質がとても強健"), ("evergreen", "落葉")]),
]
# 同じ種の別品種の値を、載っていない同種の品種に使う種（2026-11-19 のユーザーの決定に沿った試し。DECISIONS.md）。
# ジギタリス プルプレア: 図鑑の 'Apricot'・'Monstrosa Purple'・'Monstrosa White'・'Snow Thimble'・'Monstrosa'（ID 2122）がどれも 中（対象は Dg06 'Elsie Kelsey'・Dg07 'Excelsior'）。
# ユーパトリウム マクラツム: 'Red Dwarf'・'Atropurpureum'（ID 2912）・'Phantom'（ID 2911）がどれも 強（対象は Ep05 'Gateway'）。
# カラマグロスティス アクティフローラ: 'Karl Foerster'・'Overdam'・'Waldenbuch'（ID 3218）がどれも 強（対象は Cg01 'Avalanche'）。
# ロニセラ ペリクリメナム: 'Serotina'・'Graham Thomas'（ID 1911）・'Belgica'（ID 1908）がどれも 強（対象は Lo03 'Honey Baby'）。
# 当てていないもの（同じ種のページが1つだけ）: ベルゲニア コーディフォリアの Bg01〜Bg03（ページは 'Snow Time' だけ。ほかのヒマラヤユキノシタは交配品種）。
SIBLING = {"Digitalis purpurea": ("中", ["Dg05", "Dg08", "Dg09", "Dg10", "図鑑の 'Monstrosa'"]),
           "Eupatorium maculatum": ("強", ["Ep06", "図鑑の 'Atropurpureum'", "図鑑の 'Phantom'"]),
           "Calamagrostis acutiflora": ("強", ["Cg02", "Cg03", "図鑑の 'Waldenbuch'"]),
           "Lonicera periclymenum": ("強", ["Lo04", "図鑑の 'Graham Thomas'", "図鑑の 'Belgica'"])}
