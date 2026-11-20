# おぎはら植物園「おぎはら植物図鑑」（s20）: 在庫のある1品種の属20（レオントポディウムからウンキニアまで）と、
#   在庫のない2〜3品種の属12（アムソニアからビオラまで）。batch_17/input の32属。
# 2026-11-20 に読んだ（curl。scripts/tools/ogi_search.py と ogi_page2.py）。図鑑を、属の学名32個と Cotula・Bistorta・Ficaria・Persicaria virginiana／filiformis、
#   日本語（エーデルワイス・ルエリア・スポディオポゴン・フィソステギア・ハナトラノオ・アストラット・ガラハッド・ブラックナイト・スミレ・アマドコロ・フェンネル）で検索。
# 一致は24ページ（26品種に当てた。ほかに同じ種・同じ属の別品種のページを13読んだ）。
# 図鑑の書き方がマスターと違うもの: 'Superbum' は「ペルシカリア ‘スーパーバ’ Persicaria bistorta ‘Superba’」、トバラは「ポリゴナム バージニアナム Polygonum virginianum」、
#   サーモプシスは「センダイハギ ヴィロサ Thermopsis villosa」、セセリは「セセリ ‘ムーンキャロット’ Seseli gummiferum 'Moon Carrot'」（Jelitto は [Moon Carrot] を種の流通名としている）、
#   セスレリアは「セスレリア オータムナリス (セスレリア アルゲンティア) Sesleria autumnalis ssp. argentea」、'Blue Ice' は Amsonia 'Blue Ice'（種小名なし）、
#   ビオラ ラブラドリカは Viola labradorica 'Purpura'（紫葉。マスターの葉色も パープル／ブラック系 なので、売っている商品のページとして当てた）、
#   バプティシアは「バプテシア」「ムラサキセンダイハギ」、コクリュウは「黒竜(コクリュウ) Ophiopogon planiscapus 'Nigrescens'」。
# 種のページを当てたもの: トバラの2品種（To01 'Compton's Form'・To02 'Variegata'。図鑑の Polygonum virginianum は葉に模様の入る種そのもの）、
#   バプティシア オーストラリス var. minor（Ba02。ムラサキセンダイハギのページ）。
# 載っていないもの・当てていないもの: レモンバームの緑葉（図鑑は 'Gold Leaf' の1ページだけ。強）、アマドコロ（図鑑は斑入りの var. pluriflorum の1ページだけ。強）、
#   ラチビダ ピンナータ（図鑑は columnifera の品種）、アムソニア タバーナエモンタナの種そのもの（同じ種は 'Storm Cloud' の1ページだけ。チョウジソウ〔elliptica〕は別の種）、
#   緑葉のフェンネル（ブロンズフェンネルの1ページだけ）、ヘリオプシス 'Summer Nights'（下の SIBLING）、ラシラス 'Heavenly Blue'（同じ種は 'Rosenelfe' の1ページだけ。中）、
#   バーノニア 'White Lightning'（同じ種は種そのものの1ページだけ）、デルフィニウムの3品種（図鑑は New Millennium シリーズなど別の品種）、
#   エーデルワイス・ポア・ルエリア・スポディオポゴン・フィソステギア・リモニウム 'Blue Diamond'・ロサ・ビオラ 'Mars'（掲載なし）。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-20"
S2 = "日向～やや半日陰"
HS = "やや半日陰"
_TOV = (2279, "ポリゴナム バージニアナム Polygonum virginianum", "species", "強", HS,
        [("habit", "広がりのある姿になるので半日陰のカバーに良い"), ("habit", "花は白で日本のミズヒキに似るが、より小型で扱いやすい")])
_BAP = [("habit", "株立ちになり美しい青い花をたくさん咲かせるので、国内でも古くから親しまれている人気種 植えっぱなし、放任でよい丈夫な花")]
OGIHARA = [
 (["Lp01"], 206, "レプティネラ ‘プラッツ ブラック’ Leptinella squalida 'Platt's Black'", "cultivar", "中", HS,
  [("habit", "細かいシダのような葉が密生して育つキク科の多年草 葉色が黒や茶色で、とても個性的 小スペースのグランドカバーや寄せ植えにおもしろい")]),
 (["Ml01"], 1612, "ミリウム ‘オーレウム’ Milium effusum 'Aureum'", "cultivar", "強", "日向",
  [("heat_humidity", "高温になると葉色はやや浅くなるが、寒冷地では夏季も発色良く、美しい"), ("self_seed", "こぼれ種でも殖える"),
   ("pruning", "姿が乱れたら短く切り戻すと再び美しく芽吹く")]),
 (["Op01"], 1320, "黒竜(コクリュウ) Ophiopogon planiscapus 'Nigrescens'", "cultivar", "強", HS,
  [("evergreen", "冬も常緑"), ("habit", "リュウノヒゲに近縁で性質が似てとても丈夫")]),
 (["Pm01"], 2733, "パルテニウム インテグリフォリウム Parthenium integrifolium", "cultivar", "強", S2,
  [("cut_flower", "切り花、ドライフラワーにも向き、楽しみ方もいろいろ"), ("habit", "野趣のある草姿で草原などに自生し、メドウガーデンなどに向く")]),
 (["Pf01"], 103, "玉シャジン Phyteuma scheuchzeri", "cultivar", "強", HS,
  [("heat_humidity", "性質は強健で暑さにも強い"), ("habit", "這うように生育し、真っ直ぐに伸びる花茎の先にボール状のユニークな花を咲かせる")]),
 (["Pj01"], 811, "ピンピネラ マヨール ‘ロゼア’ Pimpinella major 'Rosea'", "cultivar", "中", HS, [("cut_flower", "切花にもおすすめ")]),
 (["Pk01"], 2921, "ペルシカリア ‘スーパーバ’ Persicaria bistorta ‘Superba’", "cultivar", "中", S2,
  [("evergreen", "半常緑～落葉"), ("habit", "本種は丈夫で育てやすい改良種で、株姿のまとまりも良い")]),
 (["To01"],) + _TOV, (["To02"],) + _TOV,
 (["Rn01"], 471, "カラス葉リュウキンカ Ranunculus ficaria 'Brazen Hussy'", "cultivar", "強", HS,
  [("evergreen", "花後から夏、冬は落葉し休眠する"), ("habit", "小さく野草の趣ある花だが、性質は強健でとても育て易い")]),
 (["Ss01"], 809, "セセリ ‘ムーンキャロット’ Seseli gummiferum 'Moon Carrot'", "cultivar", "中", HS, [("cut_flower", "切り花にも向く")]),
 (["Se01"], 3252, "セスレリア オータムナリス (セスレリア アルゲンティア) Sesleria autumnalis ssp. argentea", "cultivar", "強", "日向",
  [("evergreen", "常緑～半常緑"), ("seasonal_foliage", "明るい若緑色の葉は秋には黄色く鮮やかに、冬にはオレンジ色に変わり、冬も常緑")]),
 (["Sk01"], 2574, "サクシサ プラテンシス Succisa pratensis", "cultivar", "強", S2,
  [("evergreen", "常緑～半常緑"), ("habit", "花期が長く、夏から秋まで次々と花枝を上げよく咲く 性質も強健")]),
 (["Tm01"], 3454, "センダイハギ ヴィロサ(サーモプシス ヴィロサ) Thermopsis villosa", "cultivar", "強", "日向", [("heat_humidity", "寒さにも暑さにも耐える多年草")]),
 (["Un01"], 1607, "ウンシニア ルブラ Uncinia rubra", "cultivar", "強", "日向", [("evergreen", "常緑性"), ("habit", "草姿がコンパクトで乱れない")]),
 (["Av01"], 2264, "糸葉丁字草(アムソニア フブリヒティ) Amsonia hubrichtii", "cultivar", "強", HS,
  [("seasonal_foliage", "晩秋になると葉が鮮やかに紅葉し、色が少なくなってきた頃の庭でよく目立つ")]),
 (["Av03"], 2262, "丁字草 ‘ブルー アイス’ Amsonia 'Blue Ice'", "cultivar", "強", HS,
  [("seasonal_foliage", "葉は秋冬に鮮やかな黄色に紅葉する"), ("habit", "驚くほどコンパクトな品種で、大株になると、低いドーム状に咲き揃う")]),
 (["Ba01"], 2239, "ムラサキセンダイハギ Baptisia australis", "cultivar", "強", "日向", _BAP),
 (["Ba02"], 2239, "ムラサキセンダイハギ Baptisia australis", "species", "強", "日向", _BAP),
 (["Ba03"], 2803, "バプテシア ‘トワイライト プレーリーブルース’ Baptisia × variicolor 'Twilite Prairieblues'", "cultivar", "強", "日向",
  [("evergreen", "落葉"), ("habit", "性質が極めて丈夫で放任でよく育つ")]),
 (["Fo02"], 2874, "ブロンズ フェンネル Foeniculum vulgare 'Purpureum'", "cultivar", "強", S2, [("evergreen", "半常緑～落葉")]),
 (["Hp02"], 2118, "ヘリオプシス ‘バーニングハーツ’ Heliopsis helianthoides var. scabra 'Burning Hearts'", "cultivar", "強", "日向",
  [("heat_humidity", "ヘリオプシスは耐寒耐暑性に優れ丈夫で、夏秋の庭を飾る数少ない宿根草のひとつ")]),
 (["Lh02"], 1137, "ラシルス ‘ローゼンエルフ’ Lathyrus vernus 'Rosenelfe'", "cultivar", "中", "日向",
  [("habit", "スイートピーの仲間だがツルにならず、とてもコンパクトな株立ちになる"), ("habit", "生育はゆっくりだが、性質が強健で育てやすい")]),
 (["Lj02"], 2668, "スターチス ラティフォリウム Limonium latifolium", "cultivar", "強", S2,
  [("heat_humidity", "乾燥や暑さにも強い"), ("salt", "耐潮性があり、別名はシーラベンダー")]),
 (["Vr01"], 207, "バーノニア ノベボラセンシス Vernonia noveboracensis", "cultivar", "強", S2, [("pruning", "花後に切り戻すと繰り返し開花する")]),
 (["Vo01"], 799, "ビオラ ラブラドリカ Viola labradorica 'Purpura'", "cultivar", "中", HS,
  [("evergreen", "冬も常緑で深い葉色と花のシックでおしゃれな色合いが楽しめる")]),
]
# 同じ種の別品種の値を、載っていない同種の品種に使う種（2026-11-19 のユーザーの決定に沿った試し。DECISIONS.md）。
# ヘリオプシス ヘリアンソイデス（Heliopsis helianthoides）: 'Burning Hearts'（ID 2118）・'Asahi'（ID 3283）・'Summer Pink'（ID 3397）・'Bleeding Hearts'（ID 2686）・
#   'Loraine Sunshine'（ID 2071）がどれも 強（対象は Hp01 'Summer Nights'）。
SIBLING = {"Heliopsis helianthoides": ("強", ["図鑑の 'Burning Hearts'", "図鑑の 'Asahi'", "図鑑の 'Summer Pink'", "図鑑の 'Bleeding Hearts'", "図鑑の 'Loraine Sunshine'"])}
