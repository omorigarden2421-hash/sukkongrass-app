# おぎはら植物園「おぎはら植物図鑑」（s20）: チャスマンティウム・ケロネ・エキノプス・エリムス・エリゲロン・ガリウム・グレコマ・カリメリス・ラベンダー・レウカンセマム・リスラム・パキサンドラ・
#   フロミス・サギナ・サポナリア・センペルビブム・シルフィウム・スティパ・シンフィオトリクム・ビバーナム・ユッカ・ヒューケレラ・トリフォリウム。
# 2026-11-20 に読んだ（curl。scripts/tools/ogi_search.py と ogi_page2.py）。
# 図鑑を、属のカタカナ名と学名（Chasmanthium・Chelone・Erigeron・Elymus・Galium・Glechoma・Kalimeris・Lavandula・Leucanthemum・Lythrum・Pachysandra・Phlomis・Sagina・Silphium・Sempervivum・
#   Saponaria・Stipa・Trifolium・Viburnum・Yucca）、和名（ルリタマアザミ・カキドオシ・クルマバソウ・カワラマツバ・ヨメナ・シャスターデージー・ミソハギ・フッキソウ・クローバー など）で検索。
# 一致は22ページ（31品種に当てた。ほかに同じ種の別品種のページを19読んだ）。
# 図鑑の書き方がマスターと違うもの: 'Pink Jewel' は「エリゲロン ‘ローザ ジュエル’ Erigeron speciosus 'Rosa Jewel'」、'Platinum Blue' は Echinops ruthenicus 'Platinum Blue'、
#   'Broadway Lights' は「シャスターデージー ‘ブロードウェイ’ Leucanthemum x superbum 'Broadway'」、'Snowdrift' は 'Snow Drift'、
#   スティパ テヌイッシマは「スティパ ‘エンジェル ヘアー’ Stipa(Nassella) tenuissima 'Angel Hair'」（マスターの商品名に「エンジェルヘアー」とあるので品種のページとして当てた）。
# 種のページを当てたもの: ワイルドオーツ（Ch02 'Little Tickler'）、源平小菊（Eg02 'Profusion'）、フロミス チューベロサ（Ph02 'Bronze Flamingo'）、サポナリア オフィシナリス（Sn01・Sn02）。
# 載っていないもの・当てていないもの: ケロネ・ガリウム・グレコマ・カリメリス・サギナ・シルフィウム（掲載なし）、ラベンダー（図鑑は 'Grosso' だけ。別の種の交配）、
#   フッキソウの緑葉（同じ種は斑入りの1ページだけ）、センペルビブムの品種名のない商品（Sm01）、アスター エリコイデス 'Jolly Jumper'・ノビベルギ 'Jenny'、
#   トリフォリウム オクロレウカム・ルーベンス・'Frosty Feathers'（ルーベンスは 'Red Feathers' の1ページだけ。強）。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-20"
S2 = "日向～やや半日陰"
HS = "やや半日陰"
_WO = (1609, "ワイルドオーツ Chasmanthium latifolium")
_SAP = (2568, "サポナリア オフィシナリス Saponaria officinalis")
OGIHARA = [
 (["Ch01"], _WO[0], _WO[1], "cultivar", "強", S2, [("evergreen", "落葉性"), ("seasonal_foliage", "冬に葉が枯れても残る穂の風情が美しく、ウインターガーデンの素材にも良い")]),
 (["Ch02"], _WO[0], _WO[1], "species", "強", S2, [("evergreen", "落葉性")]),
 (["Ec01"], 151, "エキノプス ‘スターフロスト’ Echinops bannaticus 'Star Frost'", "cultivar", "強", "日向", [("cut_flower", "切花やドライフラワーにも")]),
 (["Ec02"], 149, "エキノプス ‘プラチナムブルー’ Echinops ruthenicus 'Platinum Blue'", "cultivar", "強", "日向", [("cut_flower", "切花やドライフラワーに利用できる")]),
 (["Eg01"], 2672, "エリゲロン ‘ローザ ジュエル’ Erigeron speciosus 'Rosa Jewel'", "cultivar", "強", S2, [("pruning", "花後に切り戻しを行うと、繰り返し開花する")]),
 (["Eg02"], 139, "源平小菊(エリゲロン) Erigeron Karvinskianus", "species", "強", "日向",
  [("spread_mode", "広がるようによく殖え、初夏から初冬まで長い間よく咲く"), ("pruning", "伸びながら咲き続けるので、ある程度で短めに切り戻すと姿が整い、再びよく咲く")]),
 (["El01"], 2317, "エリムス ‘アイシー ブルー’ Elymus canadensis 'Icy Blue'", "cultivar", "強", "日向", [("evergreen", "落葉性")]),
 (["El02"], 1608, "エリムス マジェラニカス Elymus magellanicus", "cultivar", "中", "日向", [("heat_humidity", "葉が密生し草姿は乱れにくいが、蒸れに注意し水はけ良く育てる")]),
 (["Hr01"], 1256, "ヒューケレラ ‘ストップライト‘ Heucherella 'Stoplight'", "cultivar", "中", HS, [("evergreen", "常緑～半常緑"), ("habit", "サンスポットの改良種 より強健で生育も早く斑もはっきり入る")]),
 (["Hr02"], 1258, "ヒューケレラ ‘サンスポット‘ Heucherella 'Sunspot'", "cultivar", "中", HS, []),
 (["Hr03"], 1260, "ヒューケレラ ‘タペストリー’(PVP) Heucherella 'Tapestry'", "cultivar", "中", HS, []),
 (["Le01"], 123, "シャスターデージー ‘スノードリフト’ Leucanthemum x superbum 'Snow Drift'", "cultivar", "強", "日向",
  [("heat_humidity", "普通種同様に寒さ暑さに強く、とても丈夫で土質も選ばない育てやすい花")]),
 (["Le02"], 120, "シャスターデージー ‘ブロードウェイ’ Leucanthemum x superbum 'Broadway'", "cultivar", "強", "日向",
  [("heat_humidity", "普通種同様に寒さ暑さに強く、丈夫で放任でも毎年よく咲く")]),
 (["Pc02"], 2707, "斑入りフッキソウ Pachysandra terminalis 'Variegata'", "cultivar", "強", "半日陰", [("evergreen", "常緑～半常緑"), ("spread_mode", "性質は穏やかでゆっくりと生え進む")]),
 (["Ph01"], 729, "フロミス ルッセリアナ Phlomis russeliana", "cultivar", "強", S2, [("evergreen", "冬に落葉する宿根性"), ("spread_mode", "地下茎で殖えて群生し大きな花がたくさん咲き")]),
 (["Ph02"], 2274, "フロミス チューベロサ Phlomis tuberosa", "species", "強", S2, [("evergreen", "冬に落葉する宿根性")]),
 (["Sm02"], 2085, "センペルビブム ‘ブロンコ’ Sempervivum 'Bronco'", "cultivar", "中", "日向", [("seasonal_foliage", "冬は赤みを帯びたブロンズ色に紅葉する")]),
 (["Sn01", "Sn02"], _SAP[0], _SAP[1], "species", "強", S2, [("self_seed", "こぼれ種で殖えて、毎年あちこちから咲く")]),
 (["Su01"], 2826, "スティパ イチュー Stipa ichu", "cultivar", "強", "日向", [("evergreen", "半常緑～落葉"), ("heat_humidity", "乾燥気味の痩せ地を好み、多湿を嫌う")]),
 (["Su02"], 2505, "スティパ ‘エンジェル ヘアー’ Stipa(Nassella) tenuissima 'Angel Hair'", "cultivar", "強", "日向",
  [("evergreen", "半常緑～落葉"), ("heat_humidity", "蒸れに注意し水はけ良く育てる")]),
 (["Vu02"], 1989, "ビバーナム ‘オノンダガ’ Viburnum sargentii 'Onondaga'", "cultivar", "強", "日向", [("evergreen", "落葉樹")]),
 (["Yu01"], 1342, "ユッカラン ‘ブライトエッジ’ Yucca filamentosa 'Bright Edge'", "cultivar", "強", "日向",
  [("heat_humidity", "暑さ乾燥にも強く土質も選ばない強健な性質"), ("evergreen", "冬も常緑で約-25℃まで耐える")]),
 (["Yu02"], 3037, "ユッカ グロリオサ ‘バリエガータ’ Yucca gloriosa 'Variegata'", "cultivar", "強", "日向",
  [("heat_humidity", "寒さ、暑さ、乾燥に強くとても丈夫で放任でもよく育つ"), ("evergreen", "常緑")]),
]
# 同じ種の別品種の値を、載っていない同種の品種に使う種（2026-11-19 のユーザーの決定に沿った試し。DECISIONS.md）。
# エゾミソハギ（Lythrum salicaria）: 'Happy Lights'（ID 3456）・'Robert'（ID 3415）がどちらも 強（対象は Lt01 種そのもの・Lt02 'Happy Snow'）。
# ヤブデマリ（Viburnum plicatum）: 'Pink Beauty'（ID 1991）・'Watanabei'（ID 1990）・'Kilimanjaro Sunrise'（ID 2651）がどれも 強（対象は Vu01 'Mariesii'）。
# シロツメクサ（Trifolium repens）: 'Purpurascens'（ID 1125）・'Tint Rouge'（ID 2883）・'Tint Wine'（ID 2884）・'Pink&Silver'（ID 2882）がどれも 中
#   （対象は Tf02 'Atropurpureum'・Tf03 'Dragon's Blood'・Tf04 'Wheatfen'）。同じ種の値を 中 で使うのは batch_07・batch_11・batch_12 に続いて4回目。
SIBLING = {"Lythrum salicaria": ("強", ["図鑑の 'Happy Lights'", "図鑑の 'Robert'"]),
           "Viburnum plicatum": ("強", ["図鑑の 'Pink Beauty'", "図鑑の 'Watanabei'", "図鑑の 'Kilimanjaro Sunrise'"]),
           "Trifolium repens": ("中", ["図鑑の 'Purpurascens'", "図鑑の 'Tint Rouge'", "図鑑の 'Tint Wine'", "図鑑の 'Pink&Silver'"])}
