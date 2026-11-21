# RHS（s01）の植物ページの番号: ジギタリス・プリムラ・ユーパトリウム・ベルゲニア・カラマグロスティス・デスカンプシア・フクシア・アイリス・ロニセラ。
# 探し方は scripts/pilot/rhs_ids.py と同じ（2026-11-20。アプリ内のブラウザーで検索ページ57件を順に開いた）。候補68ページを scripts/tools/rhs_check.py で読み、Name Status と栽培の項目の有無を見て選んだ。
# RHS は北米のユーパトリウムを Eutrochium・Conoclinium に移している（'Gateway'・'Red Dwarf' は Eutrochium maculatum (Atropurpureum Group)、'Ivory Towers' は Eutrochium fistulosum (Albidum Group)）。
# 試行ID: (番号, RHS の表記, メモ)
RHS = {
 "Bg01": (2209, "Bergenia cordifolia", ""), "Bg03": (58916, "Bergenia cordifolia 'Redstart'", ""),
 "Bg04": (534700, "Bergenia cordifolia 'Snowtime'", "RHS のつづりは 'Snowtime'（マスターは 'Snow Time'）"), "Bg05": (114345, "Bergenia emeiensis", ""),
 "Cg01": (198923, "Calamagrostis × acutiflora 'Avalanche'", ""), "Cg02": (72074, "Calamagrostis × acutiflora 'Karl Foerster'", ""),
 "Cg03": (93664, "Calamagrostis × acutiflora 'Overdam' (v)", ""), "Cg04": (129801, "Calamagrostis brachytricha", ""), "Cg05": (2602, "Calamagrostis epigejos", ""),
 "Dg01": (5856, "Digitalis grandiflora", ""), "Dg02": (20080, "Digitalis lutea", ""), "Dg03": (97206, "Digitalis × mertonensis", ""),
 "Dg04": (194142, "Digitalis parviflora 'Milk Chocolate'", ""),
 "Dg05": (96171, "Digitalis purpurea 'Sutton's Apricot'", "RHS の正名は 'Sutton's Apricot'（'Apricot' はシノニム扱い。126013）"),
 "Dg06": (180606, "Digitalis 'Elsie Kelsey'", "RHS は種小名なし（マスターは purpurea）"),
 "Dg07": (113840, "Digitalis purpurea Excelsior Group", "RHS は品種ではなく Excelsior Group として掲載"),
 "Dg08": (141842, "Digitalis purpurea 'Monstrosa'", "名前だけの登録。RHS にあるのは 'Monstrosa' だけ（'Monstrosa Purple' のページはない）"),
 "Dg09": (141842, "Digitalis purpurea 'Monstrosa'", "名前だけの登録。RHS にあるのは 'Monstrosa' だけ（'Monstrosa White' のページはない）"),
 "Dg10": (183828, "Digitalis purpurea 'Snow Thimble'", ""),
 "Ds01": (5638, "Deschampsia cespitosa", ""), "Ds02": (114437, "Deschampsia cespitosa 'Goldtau'", ""),
 "Ds03": (152204, "Deschampsia cespitosa 'Northern Lights' (v)", "名前だけの登録"), "Ds04": (297976, "Deschampsia cespitosa 'Pixie Fountain'", ""),
 "Ds05": (5640, "Deschampsia flexuosa", ""),
 "Ep02": (158038, "Conoclinium coelestinum", "名前だけの登録。RHS の正名は Conoclinium coelestinum（Eupatorium coelestinum はシノニム扱い）"),
 "Ep03": (501158, "Eutrochium fistulosum (Albidum Group) 'Ivory Towers'", "RHS の正名は Eutrochium（マスターは Eupatorium fistulosum f. albidum）"),
 "Ep04": (270953, "Eupatorium fortunei 'Pink Frost' (v)", ""),
 "Ep05": (500931, "Eutrochium maculatum (Atropurpureum Group) 'Gateway'", "RHS の正名は Eutrochium（Eupatorium maculatum … 'Gateway' はシノニム扱い）"),
 "Ep06": (501173, "Eutrochium maculatum (Atropurpureum Group) 'Red Dwarf'", "RHS の正名は Eutrochium（Eupatorium maculatum … 'Red Dwarf' はシノニム扱い）"),
 "Fu01": (7494, "Fuchsia magellanica", ""),
 "Fu02": (102906, "Fuchsia magellanica var. molinae 'Enstone' (v)", "名前だけの登録。RHS は var. molinae の品種としている"),
 "Fu03": (99790, "Fuchsia 'Genii'", "RHS は種小名なし（マスターは magellanica）"),
 "Fu04": (87155, "Fuchsia 'Hawkshead'", "RHS は種小名なし（マスターは magellanica）"),
 "Fu05": (82107, "Fuchsia magellanica var. gracilis 'Variegata' (v)",
          "RHS には 'Variegata' が2つある（var. gracilis 'Variegata' と、名前だけの var. macrostema 'Variegata' 70057）。栽培の項目がある gracilis の方を採った。売っているのがどちらかは要確認"),
 "Ir01": (96505, "Iris chrysographes black-flowered", "RHS は品種ではなく「黒花の系統」として掲載（マスターは 'Black Form'）"),
 "Ir02": (99775, "Iris ensata 'Variegata' (v)", ""), "Ir03": (9336, "Iris pumila", ""), "Ir04": (9352, "Iris sanguinea", ""),
 "Lo01": (90218, "Lonicera × americana (Mill.) K. Koch", "RHS には同名の誤用（misapplied。94143）と、あいまいな用法（218008）のページもある"),
 "Lo02": (108066, "Lonicera × italica [Harlequin] ('Sherlite') (v)", "RHS では Harlequin は流通名で、品種名は 'Sherlite'"),
 "Lo03": (129344, "Lonicera 'Honey Baby'", "RHS は種小名なし（マスターは periclymenum）"),
 "Lo04": (93077, "Lonicera periclymenum 'Serotina'", ""), "Lo05": (92648, "Lonicera × tellmanniana", ""),
 "Pr01": (369889, "Primula 'Primadiente Rose' (Co)", "名前だけの登録。RHS は種小名なし（マスターは cortusoides）"),
 "Pr03": (75168, "Primula japonica 'Alba' (Pf)", ""), "Pr04": (70481, "Primula japonica 'Apple Blossom' (Pf)", "RHS のつづりは 'Apple Blossom'"),
 "Pr05": (48146, "Primula japonica 'Miller's Crimson' (Pf)", "RHS のつづりは 'Miller's Crimson'"),
 "Pr06": (198564, "Primula 'Green Lace' (Pr/Poly)", "名前だけの登録。RHS は種小名なし（マスターは × polyanthus）"),
 "Pr07": (13892, "Primula veris (Pr)", ""),
}
# 見つからなかったもの・当てていないもの: Bg02（「ニューウィンターフラワリング Hybs」。品種名のない実生の交配系統）、Pr02 'Blue Selection'（種のページ 13740 だけ）、
#   Ir05 'Red Flare'（RHS には Iris 'Red Flare'〔Not established。名前だけ〕、'Red Flare' (TB)〔丈の高いジャーマンアイリスで別の品種〕、
#   'Redflare'〔シノニム扱い。どの名前の別名かを確かめていない〕がある。シベリアアヤメの品種と確かめられなかったので当てていない）
