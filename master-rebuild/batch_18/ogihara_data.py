# おぎはら植物園「おぎはら植物図鑑」（s20）: 在庫のない1品種の属19（アゲラティナからバレリアナまで）。batch_18/input の19属。
# 2026-11-20 に読んだ（curl。scripts/tools/ogi_search.py と ogi_page2.py）。図鑑を、属の学名19個と Eupatorium・Cota・Epilobium・Chamaenerion・Porteranthus・Comanthosphace、
#   日本語（ミントブッシュ・テンニンソウ・スズラン）で検索。一致は12ページ（12品種に当てた。ほかに同じ属の別の種・別品種のページを9読んだ）。
# 図鑑の書き方がマスターと違うもの: 'Chocolate' は「ユーパトリウム ‘チョコレート’ Eupatorium rugosum(=Ageratina altissima) 'Chocolate'」、ヤナギランは Epilobium angustifolium、
#   コエレリアは「コエレリア グラウカ(‘ブルー スプライト’) Koeleria glauca 'Blue Sprite'」（Jelitto は [Coolio, Blue Sprite] を種の流通名としている）、
#   オルラヤは「オルラヤ ‘ホワイトレース’ Orlaya grandiflora 'White Lace'」（Jelitto は [White Lace, White Finch] を種の流通名としている。図鑑の耐暑性の欄は空欄〔1〜2年草扱い〕）、
#   セラスチウムは「セラスチューム トメントーサム(シルバー カーペット)」。
# 【要確認】テンニンソウの黄金葉（Ls01。マスターは Leucosceptrum japonicum f. aureum）に、図鑑の「天人草 ‘ゴールデン エンジェル’ Leucosceptrum japonicum 'Golden Angel'」を当てた。
#   Jelitto が LEUCOSCEPTRUM japonicum f. aureum [Golden Angel] と、f. aureum の流通名として 'Golden Angel' を書いているため。売っているものが 'Golden Angel' かどうかは要確認。
# 載っていないもの・当てていないもの: アンテミス ティンクトリア 'Alba'（同じ種は 'Dwarf form' の1ページだけ。強。'Susanna Mitchell' は交配種）、
#   スズラン（図鑑は Convallaria majalis の八重咲きだけで、種が違う）、コリダリス 'Silver Spectre'（図鑑の6ページは別の種・別の品種）、
#   グロブラリア トリコサンタ（図鑑は punctata と salicina）、プロスタンテラ（ミントブッシュ）・サツレヤ・スポロボルス（掲載なし）。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-20"
S2 = "日向～やや半日陰"
HS = "やや半日陰"
OGIHARA = [
 (["Af01"], 203, "ユーパトリウム ‘チョコレート’ Eupatorium rugosum(=Ageratina altissima) 'Chocolate'", "cultivar", "強", "日向",
  [("habit", "フジバカマの仲間で強健"), ("habit", "春～夏は褐色の葉がカラーリーフとして楽しめる")]),
 (["Cp01"], 1112, "セファラリア ギガンティア Cephalaria gigantea", "cultivar", "強", "日向",
  [("self_seed", "性質も強健でこぼれダネでも殖える"), ("cut_flower", "切花にもおすすめ")]),
 (["Cz01"], 3291, "セラスチューム トメントーサム(シルバー カーペット) Cerastium tomentosum", "cultivar", "中", "日向",
  [("heat_humidity", "乾燥に強く、高温多湿を嫌うので乾きやすい日向へ植えるとよい"), ("pruning", "花後は短く切り戻して姿を整える"),
   ("habit", "柔らかな白い葉がカーペット状に広がり、晩春から初夏に白い花を一面に咲かせる")]),
 (["Cj01"], 50, "ヤナギラン Epilobium angustifolium", "cultivar", "中", "日向",
  [("heat_humidity", "特に夏涼しい地方では群生し見事になる 風通しの良いところで暖地でも夏越しは可能")]),
 (["Gi01"], 991, "ミツバシモツケ Gillenia trifoliata", "cultivar", "強", S2, [("seasonal_foliage", "秋の紅葉もきれい")]),
 (["Ko01"], 3135, "コエレリア グラウカ(‘ブルー スプライト’) Koeleria glauca 'Blue Sprite'", "cultivar", "強", "日向",
  [("evergreen", "常緑性"), ("heat_humidity", "性質が強健で、乾燥に強く高温多湿に注意すれば暖地でも育てやすい")]),
 (["Ls01"], 2563, "天人草 ‘ゴールデン エンジェル’ Leucosceptrum japonicum 'Golden Angel'", "cultivar", "強", HS,
  [("evergreen", "落葉性"), ("habit", "本種はその黄金葉の品種で、芽吹きから落葉まであざやかな葉色を保つ")]),
 (["On01"], 805, "セリ ‘フラミンゴ’ Oenanthe javanica 'Flamingo'", "cultivar", "強", HS,
  [("spread_mode", "繁殖枝で広がるように生育し、グランドカバーや寄せ植えに良い")]),
 (["Ol01"], 807, "オルラヤ ‘ホワイトレース’ Orlaya grandiflora 'White Lace'", "cultivar", None, S2,
  [("lifespan", "基本的に1～2年草扱いだが、こぼれダネでよく殖えるので毎年楽しめる"), ("cut_flower", "多花性でたくさんの花を上げ春から真夏近くまで長く咲き、切り花にも良い")]),
 (["Pg01"], 713, "ロシアンセージ Perovskia atriplicifolia", "cultivar", "強", S2,
  [("heat_humidity", "水はけ良く植えると夏越しも容易"), ("pruning", "花後と冬は短くカットすると姿が美しく育つ")]),
 (["Sx01"], 810, "セリナム ウォリキアナム Selinum wallichianum", "cultivar", "中", HS, [("habit", "細かく柔らかい葉が美しく背が高くなりワイルドに茂る")]),
 (["Va01"], 3008, "バレリアン(バレリアナ オフィシナリス) Valeriana officinalis", "cultivar", "強", S2,
  [("habit", "背が高くすらっと伸びた先に白い毬状の花を咲かせる")]),
]
# 同じ種の別品種の値を使う種: このまとまりにはない（どの属も1品種で、同じ種の別品種が2ページ以上あって当て先のない品種はなかった）。
SIBLING = {}
