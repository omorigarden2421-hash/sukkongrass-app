# おぎはら植物園「おぎはら植物図鑑」（s20）: ポテンティラ・パニカム・アキレア・スタキス・ヒューケラ。2026-11-19 に読んだ（curl。やり方は batch_03/ogihara_data.py の冒頭）。
# 図鑑を ポテンティラ・パニカム・アキレア・ノコギリソウ・スタキス・ヒューケラ・ツボサンゴ・ラムズイヤー で検索。一致は17ページ（品種・種あわせて23品種に当てた）。
# 図鑑は 'Terracotta' を Achillea millefolium 'Terra Cotta'、'Noblessa' を Achillea fl.pl. 'Noblessa' と書いている。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-19"
OGIHARA = [
 (["Ac03"], 202, "アキレア ‘テラコッタ’ Achillea millefolium 'Terra Cotta'", "cultivar", "強", "日向～やや半日陰",
  [("heat_humidity", "暑さ寒さに強く土質も選ばない丈夫な性質で放任でも栽培可能")]),
 (["Ac06"], 2260, "アキレア ‘レッド ベルベット’ Achillea millefolium 'Red Velvet'", "cultivar", "強", "日向～やや半日陰",
  [("heat_humidity", "暑さ寒さに強く土質も選ばないので放任でも栽培可能")]),
 (["Ac07"], 200, "アキレア ‘ノブレッサ’ Achillea fl.pl. 'Noblessa'", "cultivar", "強", "日向～やや半日陰",
  [("heat_humidity", "暑さ寒さに強く、土質も選ばないとても丈夫な性質")]),
 (["He03"], 1196, "ツボサンゴ ‘ジンジャーエール’ Heuchera 'Ginger Ale'", "cultivar", "中", "やや半日陰", [("evergreen", "常緑～半常緑")]),
 (["He04"], 2241, "ツボサンゴ ‘グリーン スパイス’ Heuchera 'Green Spice'", "cultivar", "中", "やや半日陰", [("habit", "‘アメリカーナ’の選抜種で丈夫で育てやすい")]),
 (["He07"], 1239, "ツボサンゴ ‘サターン’ Heuchera 'Saturn'", "cultivar", "中", "やや半日陰", []),
 (["He11", "He12"], 1171, "赤花ツボサンゴ Heuchera sanguinea", "species", "中", "やや半日陰", [("sun", "半日陰で咲く鮮やかな花は少ないのでシェードガーデンに重宝します")]),
 (["Pa05"], 2930, "パニカム ‘ノースウインド' Panicum virgatum 'Northwind'", "cultivar", "強", "日向", [("habit", "数あるパニカムの中でも最も姿のまとまりが良く、円筒形を維持する")]),
 (["Pa06"], 1615, "パニカム ‘プレーリースカイ’ Panicum virgatum 'Prairie Sky'", "cultivar", "強", "日向", [("habit", "丈夫で育てやすいブルー系の大型グラス")]),
 (["Pa07"], 2319, "パニカム ‘シェナンドア’ Panicum virgatum 'Shenandoah'", "cultivar", "強", "日向",
  [("seasonal_foliage", "秋冬の紅葉は深い黒紫色からオレンジや赤く変わる"), ("habit", "性質も極めて丈夫")]),
 (["Po05"], 974, "ポテンティラ ‘ヘレンジェーン’ Potentilla nepalensis 'Helen Jane'", "cultivar", "強", "日向", [("heat_humidity", "暑さ、寒さに強い丈夫な多年草")]),
 (["Po08"], 977, "ポテンティラ ‘ロンマクベス’ Potentilla nepalensis 'Ron McBeath’", "cultivar", "強", "やや半日陰", []),
 (["Po09"], 976, "ポテンティラ ‘モナーク ベルベット’ Potentilla thurbere ‘Mnarch’s Velvet’", "cultivar", "強", "やや半日陰",
  [("heat_humidity", "イチゴに近縁のキンバイの一種で、暑さ、寒さに強くとても丈夫な多年草")]),
 (["St01"], 779, "ラムズイヤー Stachys byzantina", "cultivar", "中", "やや半日陰", [("spread_mode", "よく殖え、グランドカバーにも良い")]),
 (["St02", "St03"], 779, "ラムズイヤー Stachys byzantina", "species", "中", "やや半日陰", []),
 (["St04"], 783, "スタキス マクランサ Stachys macrantha", "cultivar", "強", "日向", [("habit", "性質も強健で育てやすい 花期以外は低く、広がるように生育する")]),
 (["St05"], 782, "スタキス ‘モーニングブラッシュ’ Stachys macrantha 'Morning Blush'", "cultivar", "強", "日向", [("habit", "性質も強健で育てやすい")]),
 (["St06", "St07"], 780, "スタキス モニエリ Stachys monieri", "species", "強", "日向",
  [("heat_humidity", "暑さ寒さに強く、丈夫で育てやすい花"), ("spread_mode", "広がるように生育するのでグランドカバーにも良い")]),
]
# 同じ種の別品種の値を、載っていない同種の品種に使う種（2026-11-19 のユーザーの決定に沿った試し。DECISIONS.md）。
# パニカム バーゲタムは3品種がどれも 強（対象は Pa01・Pa02・Pa03・Pa04・Pa08）。ポテンティラ ネパレンシスは2品種が 強（対象は Po06・Po07）。
SIBLING = {"Panicum virgatum": ("強", ["Pa05", "Pa06", "Pa07"]), "Potentilla nepalensis": ("強", ["Po05", "Po08"])}
