# おぎはら植物園「おぎはら植物図鑑」（s20）: ダイアンサス・ヘレニウム・ミューレンベルギア・アルメリア・ユーフォルビア・ヘリアンセマム・クニフォフィア・ペニセタム・ルドベキア・タイム。
# 2026-11-20 に読んだ（curl。scripts/tools/ogi_search.py と ogi_page2.py）。
# 図鑑を ダイアンサス・ナデシコ・カルスシアノルム・ヘレニウム・ミューレンベルギア・アルメリア・ハマカンザシ・ユーフォルビア・ヘリアンセマム・クニフォフィア・トリトマ・ペニセタム・ルドベキア・タイム・ジャコウソウ・クリーピング で検索。
# 一致は17ページ（19品種に当てた）。
# 図鑑の書き方がマスターと違うもの: 'Fairy Tails' は Pennisetum orientale（マスターは種小名なし）、'Goldsturm'・'Little Goldstar' は Rudbeckia fulgida var. sullivantii、
#   'Tie Dye' は Helenium（種小名なし。マスターは autumnale）、Ar03 は「アルメリア ‘ルブリフロラ’」と書いて学名は 'Rubrifolia'、Mu04 は Muhlenbergia reverchonii Undaunted。
# 載っていないもの・当てていないもの: ダイアンサス 'Blue Hills'・'Lion Rock'、ヘレニウム 'Mardi Gras'・'Moerheim Beauty'、ミューレンベルギア デュモーサ・リジェンス、
#   アルメリアの種そのもの・'Alba'・'Variegata'（ページは 'Rubrifolia' だけ）、ユーフォルビアの 'Golden Glory'・'Clarice Howard'・'Fireglow'、ヘリアンセマム（掲載なし）、
#   クニフォフィア 'Bees' Lemon'・'Shining Sceptre'、ペニセタム 'Black Beauty'・マクロウルム、タイムのロンギカウリス以外
#   （イブキジャコウソウ〔Thymus quinquecostatus〕は別の種なので、セイヨウイブキジャコウソウ〔serpyllum〕には当てていない。'Red Carpet' は praecox で別の品種）。
# (試行ID のリスト, 図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
# level: cultivar＝その品種（または種そのものを売っている商品）のページ、species＝種のページを同じ種の品種に当てたもの
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
CHECKED = "2026-11-20"
S2 = "日向～やや半日陰"
OGIHARA = [
 (["Di01"], 2923, "ナデシコ カルスシアノルム(細葉ナデシコ) Dianthus carthusianorum", "cultivar", "強", S2, [("drought", "乾燥にも強く、丈夫な性質"), ("evergreen", "常緑～半常緑")]),
 (["Di02"], 2923, "ナデシコ カルスシアノルム(細葉ナデシコ) Dianthus carthusianorum", "species", "強", S2, []),
 (["Di03"], 901, "姫ナデシコ ‘アークティックファイヤー’ Dianthus deltoides 'Arctic Fire'", "cultivar", "強", S2,
  [("heat_humidity", "耐寒、耐暑性があり、こぼれダネでもよく殖えるのでグランドカバーに向く"), ("self_seed", "こぼれダネでもよく殖える")]),
 (["Hl03"], 2201, "ヘレニウム ‘タイ ダイ’ Helenium 'Tie Dye'", "cultivar", "強", "日向", []),
 (["Mu01"], 1587, "ミューレンベルギア カピラリス Muhlenbergia capillaris", "cultivar", "強", "日向", [("evergreen", "グリーンの葉は固さがあり冬も常緑で秋冬の枯れ姿にも風情がある")]),
 (["Mu03"], 2308, "ミューレンベルギア リンドヘイメリ Muhlenbergia lindheimeri", "cultivar", "強", "日向", [("evergreen", "常緑～半常緑"), ("habit", "大型で株いっぱいに穂を上げる様子は見応えがある")]),
 (["Mu04"], 2226, "ミューレンベルギア レバコニー Muhlenbergia reverchonii Undaunted", "cultivar", "強", "日向",
  [("habit", "カピラリスに似るが草丈が低く、赤茶色の穂を地上近くより広げる"), ("habit", "性質が強健で育てやすいグラス")]),
 (["Ar03"], 2857, "アルメリア ‘ルブリフロラ’ Armeria maritima 'Rubrifolia'", "cultivar", "強", "日向",
  [("evergreen", "常緑～半常緑"), ("habit", "本種は葉色がブロンズがかり、姿がよりコンパクトな品種")]),
 (["Eu04"], 867, "ユーフォルビア ポリクロマ Euphorbia polychroma", "cultivar", "強", S2, [("habit", "こんもりと茂り丈夫でよく殖え、グランドカバーや花壇の縁取りにおすすめ"), ("evergreen", "冬季落葉種")]),
 (["Kn02"], 2814, "トリトマ ‘アイスクイーン’ Kniphofia 'Ice Queen'", "cultivar", "強", "日向",
  [("heat_humidity", "性質が丈夫で、放任で冬も夏も越せるので育てやすい"), ("evergreen", "半常緑～落葉")]),
 (["Kn03"], 3072, "トリトマ ‘オレンジバニラ ホプシクル’ Kniphofia 'Orange Vanilla Popsicle'", "cultivar", "強", "日向",
  [("habit", "とてもコンパクトで場所を取らないため、様々な場所で使いやすい 性質も丈夫で放任でもよく育つ"), ("evergreen", "半常緑～落葉")]),
 (["Pn03"], 2314, "ペニセタム ‘フェアリー テール’ Pennisetum orientale 'Fairy Tails'", "cultivar", "強", "日向",
  [("heat_humidity", "アジアに広く自生するオリエンターレの品種で、寒さ、暑さに強いうえ、夏から秋にかけて長期間穂を楽しめる優良種"), ("evergreen", "半常緑～落葉")]),
 (["Pn02"], 2889, "ペニセタム アオチカラシバ Pennisetum alopecuroides f. viridescens", "cultivar", "強", "日向",
  [("self_seed", "こぼれ種で殖えるが花後に切ることでコントロールできる"), ("evergreen", "半常緑～落葉")]),
 (["Ru01"], 2861, "ルドベキア ‘ゴールドストラム’ Rudbeckia fulgida var. sullivantii 'Goldsturm'", "cultivar", "強", "日向",
  [("habit", "原種に比べてコンパクトで殖えすぎない特長がある 丈夫さはそのままで多少の荒地、痩せ地にも耐える"), ("evergreen", "落葉")]),
 (["Ru02"], 194, "ルドベキア ‘リトル ゴールドスター’ Rudbeckia fulgida var. sullivantii 'Little Goldstar'", "cultivar", "強", "日向",
  [("heat_humidity", "暑さ寒さに強く丈夫な宿根タイプのルドベキア")]),
 (["Ru03"], 2070, "ルドベキア ‘ヘンリーアイラーズ’ Rudbeckia subtomentosa 'Henry Eilers'", "cultivar", "強", "日向",
  [("heat_humidity", "暑さ寒さに耐え、乾燥にも強く丈夫"), ("fragrance", "花には甘い香りがある")]),
 (["Ru04"], 2860, "ルドベキア ‘リトルヘンリー’ Rudbeckia subtomentosa 'Little Henry'", "cultivar", "強", "日向",
  [("heat_humidity", "極めて丈夫な性質は変わらず、暑さ寒さに耐え、乾燥にも強い"), ("evergreen", "落葉")]),
 (["Ty03"], 2130, "タイム ロンギカウリス Thymus longicaulis", "cultivar", "強", S2,
  [("heat_humidity", "とても丈夫で、暑さに強く夏も青々とよく茂り、冬も葉が残る常緑性"), ("spread_mode", "タイムの中でも生育が抜群に早く、カーペット状に広がるので、グランドカバーに最適")]),
]
# 同じ種の別品種の値を、載っていない同種の品種に使う種（2026-11-19 のユーザーの決定に沿った試し。DECISIONS.md）。
# ヘレニウム オータムナーレ: 'Tie Dye' と、同じマリアッチのシリーズの 'Siesta'（図鑑のID 2200。Helenium Mariachi ‘Siesta’）がどちらも 強（対象は Hl01 'Salsa'・Hl02 'Sombrero'）。
#   図鑑はどちらにも種小名を書いていないので、ほかより根拠が弱い。
# 当てていないもの（同じ種のページが1つだけ、または値を読んでいない）: アルメリア マリティマの Ar01・Ar02・Ar04、ペニセタム 'Black Beauty'。
SIBLING = {"Helenium autumnale": ("強", ["Hl03", "図鑑の Mariachi 'Siesta'"])}
