# RHS（s01）の植物ページの番号: アスクレピアス・クロコスミア・ガイラルディア・アガスタチ・カリオプテリス・クナウティア・レウイシア・ルピナス・オリガヌム・ペオニア・パルテノキッスス・
#   シダルセア・アラビス・カルーナ・カマエメルム・クリサンセマム・キミキフーガ・ドラコセファラム。
# 探し方は scripts/pilot/rhs_ids.py と同じ（2026-11-20。アプリ内のブラウザーで検索ページ66件を順に開いた）。候補70ページを scripts/tools/rhs_check.py で読み、Name Status と栽培の項目の有無を見て選んだ。
# 試行ID: (番号, RHS の表記, メモ)
RHS = {
 "Aa01": (313009, "Agastache 'Blackadder'", "RHS のつづりは 'Blackadder'（1語）"), "Aa02": (109004, "Agastache 'Blue Fortune'", ""),
 "Aa03": (164191, "Agastache mexicana 'Red Fortune'", ""),
 "Ab01": (251964, "Arabis caucasica 'Pixie Cream'", "名前だけの登録。RHS で未確定（Unresolved）。Arabis alpina subsp. caucasica 'Pixie Cream' はシノニム扱い"),
 "Ab02": (105670, "Arabis procurrens 'Variegata' (v)", "RHS の正名は Arabis procurrens 'Variegata'（ferdinandi-coburgi 'Variegata' はシノニム扱い）"),
 "Ak01": (189392, "Asclepias asperula", ""),
 "Ak02": (270359, "Asclepias incarnata 'Cinderella'", "名前だけの登録。RHS ではシノニム扱い（Asclepias 'Cinderella' は未確定。正名は要確認）"),
 "Ak04": (137522, "Asclepias incarnata 'Soulmate'", ""),
 "Ci01": (143107, "Cimicifuga simplex var. simplex", "RHS では Cimicifuga はシノニム扱い（正名は Actaea の側）"),
 "Ci02": (227224, "Actaea simplex (Atropurpurea Group) 'Black Negligee'", "RHS の正名は Actaea simplex (Atropurpurea Group) 'Black Negligee'（Cimicifuga simplex 'Black Negligee' はシノニム扱い）"),
 "Cm01": (29189, "Chamaemelum nobile", ""), "Cm02": (91879, "Chamaemelum nobile 'Flore Pleno' (d)", ""),
 "Cr01": (91289, "Crocosmia 'Lucifer'", "RHS は種小名なし"), "Cr02": (141459, "Crocosmia × crocosmiiflora 'Solfatare'", ""),
 "Cr03": (109469, "Crocosmia × crocosmiiflora 'Constance'", ""), "Cr04": (95011, "Crocosmia 'Emberglow'", "RHS のつづりは 'Emberglow'（1語）"),
 "Cs01": (29279, "Nipponanthemum nipponicum", "名前だけの登録。RHS の正名は Nipponanthemum nipponicum"),
 "Cs02": (122802, "Chrysanthemum yezoense", ""),
 "Cu01": (95685, "Calluna vulgaris 'Kinlochruel' (d)", "RHS のつづりは 'Kinlochruel'"), "Cu02": (90959, "Calluna vulgaris 'Loch Turret'", ""),
 "Cy01": (101641, "Caryopteris × clandonensis 'Dark Knight'", ""), "Cy02": (89405, "Caryopteris × clandonensis 'Worcester Gold'", ""),
 "Cy03": (215073, "Caryopteris divaricata 'Snow Fairy'", "名前だけの登録。RHS ではシノニム扱い（Tripora divaricata 'Snow Fairy' もシノニム扱い。正名は要確認）"),
 "Dr01": (170646, "Dracocephalum argunense 'Fuji Blue'", ""),
 "Dr02": (180987, "Dracocephalum argunense 'Fuji White'", "名前だけの登録。RHS で未確定（Unresolved）"),
 "Gl01": (243359, "Gaillardia × grandiflora 'Amber Wheels'", "名前だけの登録。RHS は × grandiflora の品種（aristata 'Amber Wheels' はシノニム扱い）"),
 "Gl02": (234000, "Gaillardia × grandiflora 'Burgunder'", "RHS は × grandiflora の品種、品種名はドイツ語の 'Burgunder'"),
 "Gl03": (234001, "Gaillardia × grandiflora 'Kobold'", "RHS は × grandiflora の品種、品種名はドイツ語の 'Kobold'（'Goblin' はシノニム扱い）"),
 "Gl04": (345598, "Gaillardia × grandiflora [Mesa Peach] ('Pas907056') (Mesa Series)", "Mesa Peach は流通名、品種名は 'Pas907056'"),
 "Kt01": (61000, "Knautia macedonica", ""), "Kt02": (180972, "Knautia macedonica 'Mars Midget'", ""),
 "Kt03": (384660, "Knautia macedonica 'Midget Mauves'", "名前だけの登録"),
 "Lu01": (85006, "Lupinus 'Chandelier' (Band of Nobles Series)", ""),
 "Lu02": (90760, "Lupinus 'Noble Maiden' (Band of Nobles Series)", "RHS の表記は英語名の 'Noble Maiden'（Jelitto は 'Fräulein' [Noble Maiden]）。種小名なし"),
 "Lu03": (57482, "Lupinus perennis", ""),
 "Lw01": (311035, "Lewisia 'Little Mango' (Little Series)", "RHS は種小名なし"), "Lw02": (345162, "Lewisia 'Little Raspberry' (Little Series)", "RHS は種小名なし"),
 "Lw03": (362024, "Lewisia 'Little Snowberry' (Little Series)", "RHS は種小名なし。RHS で未確定（Unresolved）"),
 "Or01": (79410, "Origanum laevigatum 'Herrenhausen'", ""), "Or02": (89773, "Origanum vulgare 'Aureum'", ""),
 "Px01": (12349, "Parthenocissus quinquefolia", ""), "Px03": (107238, "Parthenocissus tricuspidata 'Fenway Park'", ""),
 "Py01": (219551, "Paeonia 'Coral Sunset'", ""), "Py02": (72217, "Paeonia 'Paula Fay'", ""), "Py03": (91077, "Paeonia lactiflora 'Sarah Bernhardt'", ""),
 "Sd01": (64966, "Sidalcea candida 'Bianca'", ""), "Sd02": (71986, "Sidalcea 'Party Girl'", "RHS は種小名なし"),
 "Sd03": (50547, "Sidalcea 'Rosaly'", "名前だけの登録。RHS は種小名なし（malviflora 'Rosaly' はシノニム扱い）"),
}
# 見つからなかったもの・当てていないもの: Ak03 'Milkmaid'（RHS に名前がない）、Or03 'Jim Best'（RHS に名前がない）、
#   Px02 斑入りのアメリカヅタ（マスターの学名に品種名がない。RHS の斑入りは [Star Showers] ('Monham') だが、同じ品種かは分からない）。
