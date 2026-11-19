# おぎはら植物園「おぎはら植物図鑑」（s20）: カンパニュラ・ヘメロカリス・カレックス。2026-11-19 にブラウザーで読んだ。
# 図鑑を カンパニュラ・ホタルブクロ・ヘメロカリス・カレックス・スゲ で検索（掲載名 74件）。一致は10品種。
# カレックスの耐寒性は「約 -12℃」と書かれている（ブキャナニー、'フロステッドカール'、'エバーゴールド'）。
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-19"
OGIHARA = [
 (["C05"], 72, "カンパニュラ ‘ツイスターベル’ Campanula glomerata 'Twister Bell'", "cultivar", "中", "やや半日陰", []),
 (["C09"], 86, "カンパニュラ ‘サラストロ’ Campanula 'Sarastro'", "cultivar", "強", "やや半日陰",
  [("heat_humidity", "強健なカンパニュラ トラケリウムとホタルブクロの交配種で原種のホタルブクロに比べ暑さにも強く丈夫でよく殖える"),
   ("spread_mode", "原種のホタルブクロに比べ暑さにも強く丈夫でよく殖える")]),
 (["C18"], 85, "ホタルブクロ ‘チェリーベルス’ Campanula punctata 'Cherry Bells'", "cultivar", "強", "やや半日陰", []),
 (["C22"], 87, "ホタルブクロ ‘ウエディングベル’ Campanula punctata 'Wedding Bells'", "cultivar", "強", "やや半日陰",
  [("spread_mode", "強健な改良種で広がるように生育する")]),
 (["C24"], 91, "ホタルブクロ ‘ビューティフルトラスト’ Campanula takesimana 'Beautiful Trust'", "cultivar", "強", "やや半日陰", []),
 (["C25"], 92, "ホタルブクロ ‘ピンクオクトパス’ Campanula takesimana 'Pink Octopus'", "cultivar", "強", "やや半日陰", []),
 (["M04"], 1348, "ヘメロカリス ‘シカゴアパッチ’ Hemerocallis 'Chicago Apache'", "cultivar", "強", "日向", []),
 (["X01"], 1596, "カレックス ブキャナニー Carex buchananii", "cultivar", "強", "日向", [("evergreen", "常緑で寄せ植えや花壇のアクセントに良い")]),
 (["X02"], 1593, "カレックス ‘フロステッドカール’ Carex comans 'Frosted Curls'", "cultivar", "強", "日向",
  [("pruning", "姿が乱れたら株元での強剪定により再び美しく芽吹く")]),
 (["X07"], 1591, "ベアグラス(カレックス ‘エバー ゴールド’) Carex oshimensis ‘Evergold’", "cultivar", "強", "日向", [("evergreen", "常緑性")]),
]
# 同じ種の別品種の値を、載っていない同種の品種に使う種（2026-11-19 ユーザーの決定。「強判定にしてみよう。あとで見返せるように」）。
# 種: (耐暑性, 根拠にした品種の試行ID)。対象は C17・C19・C20・C21（欧米の文献だけなら 弱）。下書きの「耐暑性の決め方」の列で見分けられる。
SIBLING = {"Campanula punctata": ("強", ["C18", "C22"])}
