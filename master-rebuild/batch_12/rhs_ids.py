# RHS（s01）の植物ページの番号: シレネ・ゲンチアナ・プルサティラ・ティアレラ・アルケミラ・アンドロポゴン・ヘデラ・リグラリア・パトリニア・プルネラ・トリキルティス・ハイドランジア・アストランティア。
# 探し方は scripts/pilot/rhs_ids.py と同じ（2026-11-20。アプリ内のブラウザーで検索ページ54件を順に開いた）。候補60ページを scripts/tools/rhs_check.py で読み、Name Status と栽培の項目の有無を見て選んだ。
# RHS はアンドロポゴン スコパリウスを Schizachyrium scoparium として載せている。
# 試行ID: (番号, RHS の表記, メモ)
RHS = {
 "Ad01": (62079, "Andropogon gerardii", ""), "Ad02": (299798, "Schizachyrium scoparium 'Blaze'", "名前だけの登録。RHS の正名は Schizachyrium scoparium"),
 "Ad03": (271981, "Schizachyrium scoparium 'Prairie Blues'", "RHS の正名は Schizachyrium scoparium（Andropogon scoparius 'Prairie Blues' はシノニム扱い）"),
 "Al01": (774, "Alchemilla mollis", ""), "Al02": (45972, "Alchemilla saxatilis", "RHS で未確定（Unresolved）"), "Al03": (298071, "Alchemilla sericata 'Gold Strike'", ""),
 "As01": (164615, "Astrantia 'Hadspen Blood'", "RHS は種小名なし（major 'Hadspen Blood' はシノニム扱い）"),
 "As02": (180785, "Astrantia 'Roma'", "RHS は種小名なし（major 'Roma' はシノニム扱い）"),
 "As03": (90309, "Astrantia major 'Ruby Wedding'", ""), "As05": (272661, "Astrantia major 'Venice'", ""),
 "As06": (47807, "Astrantia major subsp. involucrata 'Shaggy'", ""),
 "Gn02": (7778, "Gentiana dahurica", "栽培の項目が少ないページ。RHS に 'Nikita' の名前はなく、種のページ（Jelitto は Nikita を種の流通名としている）"),
 "Gn03": (170942, "Gentiana paradoxa 'Blauer Herold'", "名前だけの登録。RHS はドイツ語の 'Blauer Herold' で掲載（マスターは 'Blue Herald'）"),
 "Gn04": (522026, "Gentiana septemfida var. lagodechiana 'Bella Alpinella'", "名前だけの登録"),
 "Hd01": (349083, "Hedera helix 'Henriette' (v)", "名前だけの登録"),
 "Hd02": (357640, "Hedera hibernica 'Spetchley'", "RHS の正名は Hedera hibernica 'Spetchley'（helix 'Spetchley' はシノニム扱い）"),
 "Hd03": (86524, "Hedera helix 'Baltica'", "名前だけの登録。RHS は品種 'Baltica' として掲載（var. baltica はシノニム扱い）"),
 "Hy01": (63034, "Hydrangea arborescens 'Annabelle'", ""), "Hy03": (98581, "Hydrangea paniculata 'Grandiflora'", ""),
 "Hy05": (178462, "Hydrangea serrata 'Kurenai' (L)", ""),
 "Hy06": (275591, "Hydrangea serrata subsp. yezoensis", "RHS は亜種 subsp. yezoensis（つづりは yezoensis。var. yezoensis はシノニム扱い）"),
 "Lg01": (116495, "Ligularia dentata 'Dark Beauty'", "名前だけの登録"), "Lg02": (167792, "Ligularia dentata 'Orange Queen'", ""), "Lg03": (23892, "Ligularia przewalskii", ""),
 "Ps01": (14184, "Pulsatilla vulgaris", ""),
 "Ps02": (298619, "Pulsatilla vulgaris 'Perlen Glocke'", "名前だけの登録。RHS の正名は 'Perlen Glocke'（'Pearl Bells' はシノニム扱い）"),
 "Ps03": (369130, "Pulsatilla 'Rose Bells'", "RHS ではシノニム扱い（正名は要確認。Jelitto は 'Rosen Glocke' の英語名としている）"),
 "Ps04": (285975, "Pulsatilla vulgaris 'White Bells'", "名前だけの登録。RHS で未確定（Unresolved）。Jelitto は 'Alba' の別名としている（RHS の 'Alba' は 92427）"),
 "Pt01": (82273, "Patrinia scabiosifolia", ""), "Pt03": (88825, "Patrinia villosa", "名前だけの登録"),
 "Pv01": (370985, "Prunella grandiflora 'Bella Blue'", "名前だけの登録"), "Pv02": (137142, "Prunella grandiflora 'Rubra'", ""), "Pv03": (13944, "Prunella vulgaris", ""),
 "Si01": (164001, "Silene dioica 'Jade Valley' (v)", "名前だけの登録"), "Si02": (85303, "Silene uniflora 'Druett's Variegated' (v)", ""),
 "Si03": (117393, "Silene uniflora 'Robin Whitebreast' (d)", "RHS は八重咲き (d) としている（Jelitto の 'Weißkehlchen' は一重。要確認）"),
 "Si04": (59446, "Silene uniflora 'Rosea'", ""), "Si05": (179058, "Silene uniflora 'Swan Lake' (d)", "名前だけの登録"),
 "Tc01": (175814, "Tricyrtis formosana 'Gilt Edge' (v)", ""),
 "Tc02": (163991, "Tricyrtis 'Lightning Strike' (v)", "名前だけの登録。RHS は種小名なし（マスターは hirta）"),
 "Tc03": (83140, "Tricyrtis 'Tojen'", "RHS のつづりは 'Tojen'（マスターは 'Togen'）"),
 "Ti02": (176933, "Tiarella 'Pink Skyrocket'", ""), "Ti03": (253778, "Tiarella 'Sugar and Spice'", ""), "Ti04": (18217, "Tiarella wherryi", ""),
}
# 見つからなかったもの・当てていないもの: Gn01 'Blue Cross'（種のページ 7776 だけ）、Hy02 'Aurea'・Hy04 'Cheju-do'・Hy07 エゾアジサイの白花、Pt02 'Nana'、Ti01 'Lacquer Leaf'、As04 'Vanilla Edge'
