# おぎはら植物園「おぎはら植物図鑑」（s20）: アスクレピアス・クロコスミア・ガイラルディア・アガスタチ・カリオプテリス・クナウティア・レウイシア・ルピナス・オリガヌム・ペオニア・パルテノキッスス・
#   シダルセア・アラビス・カルーナ・カマエメルム・クリサンセマム・キミキフーガ・ドラコセファラム。
# 2026-11-20 に読んだ（curl。scripts/tools/ogi_search.py と ogi_page2.py）。
# 図鑑を、属の学名（Asclepias・Crocosmia・Gaillardia・Agastache・Caryopteris・Knautia・Lewisia・Lupinus・Origanum・Paeonia・Parthenocissus・Sidalcea・Arabis・Calluna・Chamaemelum・
#   Chrysanthemum・Cimicifuga・Actaea・Dracocephalum・Nipponanthemum・Tripora）と、和名・カタカナ名（カリガネソウ・ハマギク・コハマギク・サラシナショウマ・ムシャリンドウ・カモミール・ツタ・
#   シャクヤク・オレガノ・ルピナス・レウイシア・アラビス・カルーナ・クナウティア など）で検索。
# 一致は15ページ（15品種に当てた。ほかに同じ種・同じ属の別品種のページを24読んだ）。
# 図鑑の書き方がマスターと違うもの: 'Snow Fairy' は「カリガネソウ ‘スノー フェアリー’ Tripora divaricata 'Snow Fairy'」、'Black Negligee' は Cimicifuga simplex(=Actaea matsumurae) 'Black Negligee'、
#   'Lucifer' は Crocosmia 'Lucifer'（種小名なし）、斑入りのアメリカヅタは「斑入りアメリカヅタ Parthenocissus quinquefolia 'Variegata'」
#   （マスターの Px02 は学名に品種名がなく、商品名が「斑入り」。図鑑のこのページを品種のページとして当てた）。
# 載っていないもの・当てていないもの: レウイシア・ルピナス・アラビス・カルーナ・ドラコセファラム・ハマギク・コハマギク（掲載なし）、ガイラルディア（図鑑は別の種の2ページだけ）、
#   ペオニア（ヤマシャクヤクの3ページだけ。別の種）、アスクレピアス アスペルラ、アガスタチ 'Red Fortune'、クロコスミアの × crocosmiiflora の2品種と 'Ember Glow'
#   （図鑑は 'Lucifer' と 'Hellfire' の2ページ。どちらも種小名なしの交配品種で、同じ種とは言えない）、オレガノ ブルガレの2品種（'Norton's Gold' は種小名なし）、
#   緑葉のアメリカヅタ（同じ種は斑入りの1ページだけ）、シダルセア マルビフローラの2品種（図鑑は malviflora-Hybr. 'Purpetta' の1ページだけ。中）、
#   ローマンカモミールの一重（同じ種は八重の1ページだけ。中）。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-20"
S2 = "日向～やや半日陰"
HS = "やや半日陰"
OGIHARA = [
 (["Aa01"], 768, "アガスターシェ ‘ブラックアダー’ Agastache 'Black Adder'", "cultivar", "強", "日向", [("habit", "性質も特に丈夫で放任でも育つ花 花期も長い")]),
 (["Aa02"], 2872, "アガスターシェ ‘ブルー フォーチュン’ Agastache 'Blue Fortune'", "cultivar", "強", "日向",
  [("evergreen", "落葉"), ("seasonal_foliage", "花後の冬は種(シードヘッド)が残り、ウインターガーデンにも面白い")]),
 (["Ak02"], 2908, "アスクレピアス ‘シンデレラ’ Asclepias incarnata 'Cinderella'", "cultivar", "強", "日向",
  [("evergreen", "半常緑～落葉"), ("cut_flower", "四季咲きで花期も長く、切花にも向く"), ("habit", "株立ちになり、背も高いので庭の後方に良い")]),
 (["Ci02"], 462, "シミシフーガ ‘ブラックネグリジェ’ Cimicifuga simplex(=Actaea matsumurae) 'Black Negligee'", "cultivar", "中", HS, []),
 (["Cm02"], 126, "ダブルフラワーカモミール Chamaemelum nobile ‘Flore Pleno'", "cultivar", "中", "日向",
  [("habit", "普通種に比べ草丈が低くやや這性で芝生のような草姿となりグランドカバーにも向く"), ("fragrance", "良い香りも強くハーブとしての用途も多様")]),
 (["Cr01"], 2365, "クロコスミア ‘ルシファー’ Crocosmia 'Lucifer'", "cultivar", "強", "日向",
  [("evergreen", "半常緑～落葉"), ("heat_humidity", "暑さに強くとても丈夫で、夏によく咲く"), ("cut_flower", "海外では切り花としても人気が高い")]),
 (["Cy01"], 2271, "カリオプテリス ‘ダークナイト’ Caryopteris x clandonensis 'Dark Knight'", "cultivar", "強", "日向", [("pruning", "花後は短く切り、樹形を整えるとよい")]),
 (["Cy02"], 475, "カリオプテリス ‘ウォーセスターゴールド’ Caryopteris ×clandonensis 'Worcester Gold'", "cultivar", "強", "日向", []),
 (["Cy03"], 2798, "カリガネソウ ‘スノー フェアリー’ Tripora divaricata 'Snow Fairy'", "cultivar", "強", S2,
  [("evergreen", "落葉"), ("heat_humidity", "日陰や湿気に強く、細やかな斑入り葉が場所を明るくするので、暗くなりがちな半日陰の庭で重宝する")]),
 (["Kt02"], 1113, "クナウティア ‘マースミジェット’ Knautia macedonica 'Mars Midget'", "cultivar", "強", S2,
  [("heat_humidity", "宿根性の松虫草の一種で暑さに強く初夏から秋までよく咲く")]),
 (["Or01"], 739, "オレガノ ‘ヘレンハウゼン’ Origanum laevigatum 'Herrenhausen'", "cultivar", "強", S2,
  [("spread_mode", "とても生育旺盛な強健種で、よく殖えたくさんの花を立ち上げ咲く姿が見事"), ("seasonal_foliage", "秋冬は黒味を帯びた濃いブロンズ色に紅葉する")]),
 (["Px02"], 3321, "斑入りアメリカヅタ Parthenocissus quinquefolia 'Variegata'", "cultivar", "強", "日向",
  [("evergreen", "落葉性"), ("seasonal_foliage", "秋には赤く紅葉して見事"), ("habit", "ツルからも根を出し、壁面を登るが、野生のアメリカヅタに比べて成長が穏やかで扱いやすい")]),
 (["Px03"], 1994, "ナツヅタ ‘フェンウェイパーク’ Parthenocissus tricuspidata 'Fenway Park'", "cultivar", "強", "日向",
  [("evergreen", "落葉"), ("seasonal_foliage", "秋の鮮やかな紅葉も魅力"), ("habit", "普通種に比べ生育はやや遅く、ツルの長さは3m程でコンパクト")]),
 (["Sd01"], 1, "シダルセア ‘ビアンカ’ Sidalcea candida 'Bianca'", "cultivar", "強", "日向", [("habit", "小さな丸い葉が密生し広がるように生育する")]),
]
# 同じ種の別品種の値を、載っていない同種の品種に使う種（2026-11-19 のユーザーの決定に沿った試し。DECISIONS.md）。
# アスクレピアス インカルナータ（Asclepias incarnata）: 'Ice Ballet'（ID 2777）・'Cinderella'（ID 2908）がどちらも 強（対象は Ak03 'Milkmaid'・Ak04 'Soulmate'）。
# クナウティア マケドニカ（Knautia macedonica）: 'Mars Midget'（ID 1113）・'Thunder and Lightning'（ID 2495）がどちらも 強（対象は Kt01 種そのもの・Kt03 'Midget Mauves'）。
# サラシナショウマ（Cimicifuga simplex）: 'White Pearl'（ID 466）・'Black Negligee'（ID 462）・'Atropurpurea'（ID 461）・'Brunette'（ID 463）・'Pink Spike'（ID 464）がどれも 中
#   （対象は Ci01 種そのもの）。同じ種の値を 中 で使うのは batch_07・batch_11・batch_12・batch_14 に続いて5回目。
SIBLING = {"Asclepias incarnata": ("強", ["図鑑の 'Ice Ballet'", "図鑑の 'Cinderella'"]),
           "Knautia macedonica": ("強", ["図鑑の 'Mars Midget'", "図鑑の 'Thunder and Lightning'"]),
           "Cimicifuga simplex": ("中", ["図鑑の 'White Pearl'", "図鑑の 'Black Negligee'", "図鑑の 'Atropurpurea'", "図鑑の 'Brunette'", "図鑑の 'Pink Spike'"])}
