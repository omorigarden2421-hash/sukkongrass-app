# おぎはら植物園「おぎはら植物図鑑」（s20）: フロックス・ペルシカリア・サルビア。2026-11-19 に読んだ。
# 図鑑を フロックス・ペルシカリア・サルビア・セージ・ポリゴナム・ミズヒキ・タデ で検索（掲載名 約190件）。一致は26ページ（品種・種あわせて33品種に当てた）。
# 検索は curl でも読めた（POST gallery/search.php、mode=search、text=名前（UTF-8 を % で符号化）。2ページ目以降は同じクッキーで search.php?index=&catalog=&p=1…）。
# 宿根フロックス（paniculata）とアンプレクシカウリスには種のページがない（品種のページだけ）。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-19"
OGIHARA = [
 (["F02"], 923, "フロックス ‘モントローザトリカラー’ Phlox divaricata 'Montrose Tricolor'", "cultivar", "強", "日向～やや半日陰",
  [("habit", "広がりのある草姿になる這性のフロックス"), ("seasonal_foliage", "気温が低い時期はピンクを帯びて紅葉し一層美しい"), ("fragrance", "芳香花")]),
 (["F05"], 934, "宿根フロックス ‘ブルーパラダイス’ Phlox paniculata 'Blue Paradise'", "cultivar", "強", "日向",
  [("fragrance", "満開頃は香りもすばらしく")]),
 (["F08"], 928, "宿根フロックス ‘ダビット’ Phlox paniculata 'David'", "cultivar", "強", "日向", [("pests", "性質は強健で育て易くウドンコ病にも強い")]),
 (["F19"], 924, "フロックス ピロサ Phlox pilosa", "cultivar", "強", "日向～やや半日陰", [("habit", "広がるように生育する這うタイプのフロックス"), ("fragrance", "芳香花")]),
 (["R01"], 843, "ポリゴナム アフィネ Polygonum affine", "cultivar", "中", "日向",
  [("soil", "水はけ良い場所を好み乾燥地のグランドカバーやロックガーデンにも向く"), ("seasonal_foliage", "秋冬は葉の赤い紅葉も楽しめる")]),
 (["R02"], 843, "ポリゴナム アフィネ Polygonum affine", "species", "中", "日向", []),
 (["R03"], 2132, "ペルシカリア ‘アルバ’ Persicaria amplexicaulis 'Alba'", "cultivar", "強", "日向",
  [("heat_humidity", "暑さ、寒さに強く、丈夫で花期も長いアンプレキシカウリス"), ("sun", "耐陰性があり、半日陰でも咲くのでシェードガーデンにも使用できる")]),
 (["R05"], 844, "ペルシカリア ‘ブラックフィールド’ Persicaria amplexicaulis 'Blackfield'", "cultivar", "強", "日向",
  [("heat_humidity", "性質は丈夫で暑さにも強く、株立ちになる")]),
 (["R09"], 2080, "ペルシカリア ‘ゴールデンアロー’ Persicaria amplexicaulis 'Golden Arrow'", "cultivar", "強", "日向",
  [("heat_humidity", "性質は丈夫で暑さにも強く、株立ちになる"), ("pruning", "夏から咲き始める花は切り戻しで繰り返し開花し")]),
 (["R11"], 2567, "ペルシカリア ‘オレンジ フィールド’ Persicaria amplexicaulis 'Orange Field'", "cultivar", "強", "日向",
  [("heat_humidity", "暑さ、寒さに強く性質がとても丈夫なアンプレキシカウリスの品種"), ("pruning", "花後切り戻すことで初冬まで繰り返し花を楽しめる")]),
 (["R12"], 2706, "ペルシカリア ‘ロゼア’ Persicaria amplexicaulis 'Rosea'", "cultivar", "強", "日向",
  [("heat_humidity", "暑さ、寒さに強く、丈夫で花期も長いアンプレキシカウリス"), ("sun", "半日陰でも咲きシェードガーデンにも良い")]),
 (["R14"], 2740, "ペルシカリア ‘レッド ドラゴン’ Persicaria microcephala 'Red Dragon'", "cultivar", "強", "日向～やや半日陰", [("evergreen", "半常緑～落葉")]),
 (["R16"], 2218, "ペルシカリア ポリモルファ Perisicaria polymorpha", "cultivar", "強", "日向", [("habit", "株張り、高さとも2mほどになる超大型の多年草")]),
 (["R17"], 2279, "ポリゴナム バージニアナム Polygonum virginianum", "species", "強", "やや半日陰", [("habit", "広がりのある姿になるので半日陰のカバーに良い")]),
 (["S01"], 681, "サルビア ネモローサ ‘カラドンナ’ Salvia nemorosa ‘Caradonna’", "cultivar", "強", "日向", []),
 (["S05"], 682, "サルビア ネモローサ ‘ローゼンウェイン Salvia nemorosa ’Rosenwein'", "cultivar", "強", "日向～やや半日陰",
  [("pruning", "各種ネモローサの系統は花後株元まで短く切り戻すと再び開花する")]),
 (["S02", "S03", "S04"], 680, "サルビア ネモローサ Salvia nemorosa", "species", "強", "日向～やや半日陰", [("pruning", "花後短く切り戻すと繰り返し咲く")]),
 (["S06"], 703, "コモンセージ Salvia officinalis", "cultivar", "強", "日向～やや半日陰", []),
 (["S07"], 697, "サルビア プラテンシス ‘メイドリーン’ Salvia pratensis 'Madeline'", "cultivar", "強", "日向～やや半日陰",
  [("heat_humidity", "暑さ寒さに強く、花期の長い人気のサルビア プラテンシスの新色"), ("pruning", "花後の切り戻しにより長期間次々と開花する")]),
 (["S08"], 690, "サルビア プラテンシス ‘ローズラプソディ’ Salvia pratensis 'Rose Rhapsody'", "cultivar", "強", "日向～やや半日陰", [("evergreen", "半常緑～落葉")]),
 (["S09"], 696, "サルビア プラテンシス ‘スカイダンス’ Salvia pratensis 'Sky Dance'", "cultivar", "強", "やや半日陰", []),
 (["S10"], 694, "サルビア プラテンシス ‘スイートエスメラルダ’ Salvia pratensis 'Sweet Esmeralda'", "cultivar", "強", "日向～やや半日陰", []),
 (["S11"], 695, "サルビア プラテンシス ‘トワイライトセレナーデ’ Salvia pratensis 'Twilight Serenade'", "cultivar", "強", "日向～やや半日陰", []),
 # マスターは 'Queen Blue'。図鑑は 'Blue Queen'。2026-11-19 ユーザーの決定で同じ品種として扱う（マスターの 濃い紫・45〜60cm・初夏〜盛夏 と、
 #   'Blaukönigin' の 青紫・シカゴ植物園の草丈 18〜24 in〔46〜61cm〕・初夏〜夏 が合う。Jelitto のサルビア73件に 'Queen Blue' はなく、その検索語では 'Blaukönigin' だけが出る）
 (["S12"], 723, "サルビア ‘ブルークイーン’ Salvia x superba 'Blue Queen'", "cultivar", "強", "日向",
  [("pruning", "花後に短く地際まで剪定すると姿良く繰り返し花をつける")]),
 # 図鑑の 693「サルビア プラテンシス ‘ラプソディ イン ブルー’ Salvia pratensis 'Rhapsody in Blue'」は、マスターの S15（Salvia × sylvestris 'Rhapsody in Blue'）とは
 #   別の品種と見て当てていない（stauden.de と MBG に nemorosa／× sylvestris の 'Rhapsody in Blue' が別にある）。ユーザーの回答（2026-11-19）: 売っているのは × シルベストリスの方
 (["S16"], 2796, "サルビア バーチキリアタ Salvia verticillata", "species", "強", "日向～やや半日陰", [("drought", "乾いた場所や痩せ地にも強く、丈夫で咲かせやすい")]),
]
# 同じ種の別品種の値を、載っていない同種の品種に使う種（2026-11-19 ユーザーの決定。「強判定にしてみよう。あとで見返せるように」）。
# 種: (耐暑性, 根拠にした品種の試行ID)。対象は R04・R06・R07・R08・R10・R13（欧米の文献だけなら 中）。下書きの「耐暑性の決め方」の列で見分けられる。
# 宿根フロックス（paniculata）も同じ扱いにする（2026-11-19 ユーザーの回答「強にする」）。根拠は 'Blue Paradise'・'David' の2品種、
#   対象は F06・F07・F09〜F18 の12品種（欧米の文献だけなら空欄）。
SIBLING = {"Persicaria amplexicaulis": ("強", ["R03", "R05", "R09", "R11", "R12"]),
           "Phlox paniculata": ("強", ["F05", "F08"])}
