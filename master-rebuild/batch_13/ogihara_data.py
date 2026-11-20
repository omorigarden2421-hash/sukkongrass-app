# おぎはら植物園「おぎはら植物図鑑」（s20）: ガウラ・ジプソフィラ・アシリウム・コルヌス・フェスツーカ・ハコネクロア・パパベル・アンジェリカ・エノテラ・バーバスカム・バーベナ・アンスリスクス・アルテミシア・カラミンサ。
# 2026-11-20 に読んだ（curl。scripts/tools/ogi_search.py と ogi_page2.py）。
# 図鑑を ガウラ・ハクチョウソウ・ジプソフィラ・カスミソウ・宿根カスミソウ・Gypsophila・アシリウム・ニシキシダ・メシダ・コルヌス・サンゴミズキ・ミズキ・Cornus・フェスツカ・フウチソウ・
#   オリエンタルポピー・オニゲシ・アンジェリカ・エノテラ・ツキミソウ・Oenothera・バーバスカム・バーベナ・Anthriscus・チャービル・アルテミシア・アサギリソウ・ヨモギ・カラミンサ で検索。
# 一致は27ページ（36品種に当てた。ほかに同じ種の別品種のページを12読んだ）。
# 図鑑の書き方がマスターと違うもの: ニシキシダは Athyrium niponicum '…'（var. pictum を書かない）、'Ravenswing' は「ワイルドチャービル Anthriscus sylvestris 'Raven's Wing'」、
#   フェスツーカ ガウティエリは Festuca scoparia、'Princess Victoria Louise' は 'Prinzessin Victoria Louise'（実生につき色幅がある、と書いている）、
#   フウチソウの4つは学名がどれも Hakonechloa macra で、名前は 緑葉フウチ草・紅フウチソウ・黄金フウチ草・斑入りフウチ草（マスターの商品名と照らして当てた）。
# 種のページを当てたもの: ガウラ（白蝶草。Ga01・Ga03〜Ga06）、フェスツカ グラウカ（Fe02・Fe03）、ニシキシダ 'Pictum'（At03 'Metallicum'。変種 pictum のページとして）、
#   カラミンサ ネペタ（Ca02 'Blue Cloud'。図鑑の「カラミンサ(ピンク)」が Calamintha nepeta）。
# 載っていないもの・当てていないもの: ジプソフィラ・コルヌス（掲載なし）、フェスツーカ アイダホエンシス、アルテミシア ブルガリス 'Janlim'、エノテラ マクロカルパ、
#   アンジェリカ パキカルパ（図鑑は 'Summer Delight' の1ページだけ。強）・シルベストリス 'Ebony'（同じ種は 'Vicar's Mead' の1ページだけ）、
#   バーバスカム 'Sixteen Candles'（同じ種は 'Wedding Candles' の1ページだけ）、エノテラ スペシオーサ 'Woodside White'（同じ種は 'Silky' の1ページだけ。強）。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-20"
S2 = "日向～やや半日陰"
HS = "やや半日陰"
_GAU = [("self_seed", "初夏から初冬まで長期間咲き続けとても丈夫でこぼれ種でもよく殖え次々と咲く")]
_NIS = [("evergreen", "落葉性"), ("heat_humidity", "充実した株で、春夏の気温が涼しいほど発色が良い")]
_PAP = [("heat_humidity", "高温多湿に弱く暖地では夏越しが難しく、1年草扱いの場合もあるが、花後に種を保管し、涼しくなった頃に蒔くと苗が作れる")]
OGIHARA = [
 (["Ga02"], 2068, "ガウラ ‘サマー エモーション’ Gaura lindheimeri 'Summer Emotions'", "cultivar", "強", "日向",
  [("habit", "コンパクトタイプで普通種の半分ほどの草丈にまとまり、びっしりと咲き揃う"), ("heat_humidity", "普通種同様に長期間咲き続け、性質も丈夫で放任でもよく咲く")]),
 (["Ga01", "Ga03", "Ga04", "Ga05", "Ga06"], 42, "白蝶草(ガウラ) Gaura lindheimeri", "species", "強", "日向", _GAU),
 (["At01"], 1338, "西洋メシダ ‘ドレス ダガー’ Athyrium filix-femina 'Dre's Dagger'", "cultivar", "強", "半日陰", [("evergreen", "落葉性")]),
 (["At02"], 1333, "ニシキシダ ‘バーガンディレース’ Athyrium niponicum 'Burgundy Lace'", "cultivar", "強", "半日陰", _NIS),
 (["At04"], 1334, "ニシキシダ ‘ピューターレース’ Athyrium niponicum 'Pewter Lace'", "cultivar", "強", "半日陰", _NIS),
 (["At05"], 1335, "ニシキシダ ‘シルバーフォールズ’ Athyrium niponicum 'Silver Falls'", "cultivar", "強", "半日陰", _NIS),
 (["At03"], 1337, "ニシキシダ ‘ピクタム’ Athyrium niponicum 'Pictum'", "species", "強", "半日陰",
  [("evergreen", "落葉性"), ("spread_mode", "小型で地下茎でふえるので半日陰のグランドカバーや鉢植え、寄せ植えに")]),
 (["Fe01"], 2640, "フェスツカ スコパリア Festuca scoparia", "cultivar", "強", "日向", [("evergreen", "常緑性"), ("habit", "超小型のフェスツカで、短い葉が密生するボール状の姿")]),
 (["Fe02", "Fe03"], 1583, "フェスツカ グラウカ Festuca glauca", "species", "強", "日向", [("evergreen", "常緑性"), ("drought", "乾燥に強くロックガーデンやコンテナにも良い")]),
 (["Hk01"], 1579, "緑葉フウチ草 Hakonechloa macra", "cultivar", "強", HS, [("evergreen", "落葉性")]),
 (["Hk02"], 1582, "紅フウチソウ Hakonechloa macra", "cultivar", "強", HS, [("evergreen", "落葉性"), ("seasonal_foliage", "特に初夏頃によく発色し、秋の紅葉も美しい")]),
 (["Hk03"], 1581, "黄金フウチ草 Hakonechloa macra", "cultivar", "強", HS, [("evergreen", "落葉性")]),
 (["Hk04"], 1580, "斑入りフウチ草 Hakonechloa macra", "cultivar", "強", HS, [("evergreen", "落葉性"), ("seasonal_foliage", "特に秋は赤みが強く紅葉し美しい")]),
 (["Pp01"], 2429, "オリエンタルポピー ‘ブリリアント’ PAPAVER orientale 'Brilliant'", "cultivar", "弱", HS, _PAP),
 (["Pp02"], 3444, "オリエンタルポピー ‘ビクトリア ルイーズ’ Papaver orientale 'Prinzessin Victoria Louise'", "cultivar", "弱", "日向",
  [("heat_humidity", "寒さに強い宿根ポピーで夏の高温多湿を嫌うが、水はけよくすると夏越しも可能")]),
 (["Pp03"], 483, "オリエンタルポピー ‘ロイヤルウエディング’ Papaver orientale 'Royal Wedding'", "cultivar", "弱", HS, _PAP),
 (["Pp04"], 3123, "オリエンタルポピー ‘メイ クイーン’ Papaver orientale 'May Queen'", "cultivar", "弱", "日向", [("evergreen", "半常緑")]),
 (["Ag03"], 2277, "アンジェリカ ‘ビカーズ ミード’ Angelica sylvestris 'Vicar's Mead'", "cultivar", "強", HS, []),
 (["Vb02"], 579, "バーバスカム ‘ウエディングキャンドルズ’ Verbascum chaixii 'Wedding Candles'", "cultivar", "中", HS, []),
 (["Vb03"], 577, "バーバスカム ‘ビオレッタ’ Verbascum phoeniceum 'Violetta'", "cultivar", "中", HS, []),
 (["Vn01"], 479, "バーベナ ボナリエンシス(三尺バーベナ) Verbena bonariensis", "cultivar", "強", "日向",
  [("heat_humidity", "とても強健な性質で寒冷地から暖地まで幅広く植えられる宿根タイプのバーベナ"), ("self_seed", "株も越冬するうえ、こぼれ種でとても殖え群生する")]),
 (["Vn03"], 476, "バーベナ ハスタータ ‘ブルースパイヤー’ Verbena hastata 'Blue Spires'", "cultivar", "強", "日向",
  [("pruning", "花後切り戻すと再び開花し、秋遅くまで長く楽しめる"), ("self_seed", "こぼれ種でもよく殖える")]),
 (["Ah01"], 2217, "ワイルドチャービル ‘ゴールデン フリース’ Anthriscus sylvestris 'Golden Fleece'", "cultivar", "中", HS, [("self_seed", "多年草でこぼれダネでも殖える")]),
 (["Ah02"], 838, "ワイルドチャービル ‘レイヴァンズ ウィング’ Anthriscus sylvestris 'Raven's Wing'", "cultivar", "中", HS, [("self_seed", "多年草でこぼれダネでも殖える")]),
 (["Am01"], 229, "朝霧草 Artemisia schmidtiana", "cultivar", "中", S2, [("pruning", "伸びたら短く切り戻すと草姿良く作れる")]),
 (["Ca01"], 742, "カラミンサ ‘バリエガータ’ Calamintha grandiflora 'Variegata'", "cultivar", "強", "日向", [("fragrance", "淡いミントのような爽やかな香りを持つ")]),
 (["Ca02"], 743, "カラミンサ(ピンク) Calamintha nepeta", "species", "強", "日向", []),
]
# 同じ種の別品種の値を、載っていない同種の品種に使う種（2026-11-19 のユーザーの決定に沿った試し。DECISIONS.md）。
# バーベナ ハスタータ: 'Blue Spires'・'Pink Spires'（ID 478）・'White Spires'（ID 477）がどれも 強（対象は Vn02。種そのものを売っている商品）。
SIBLING = {"Verbena hastata": ("強", ["Vn03", "図鑑の 'Pink Spires'", "図鑑の 'White Spires'"])}
