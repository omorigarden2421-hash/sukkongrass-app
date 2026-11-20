# RHS（s01）の植物ページの番号: タリクトラム・コレオプシス・リアトリス・リシマキア・ベロニカストラム・エリンジウム・ミスカンサス・モリニア。
# 探し方は scripts/pilot/rhs_ids.py と同じ（2026-11-20。アプリ内のブラウザーで検索ページ49件を順に開いた）。候補70ページを curl で読み、Name Status と栽培の項目の有無を見て選んだ。
# RHS はモリニアの品種を亜種（subsp. caerulea／subsp. arundinacea）の下に置いている。'Purpurascens' は種小名なし（sinensis ではない）。
# 試行ID: (番号, RHS の表記, メモ)
RHS = {
 "Th01": (73814, "Thalictrum aquilegiifolium 'Purpureum'", "RHS で未確定（Unresolved）"),
 "Th02": (117489, "Thalictrum aquilegiifolium 'Thundercloud'", ""), "Th03": (18077, "Thalictrum delavayi", ""),
 "Th04": (74143, "Thalictrum delavayi 'Album'", ""), "Th05": (98203, "Thalictrum flavum subsp. glaucum", ""),
 "Th06": (221893, "Thalictrum 'Black Stockings'", ""), "Th07": (143574, "Thalictrum 'Elin'", ""),
 "Th08": (68901, "Thalictrum rochebruneanum", "マスターのつづりは rochebrunianum"),
 "Co01": (357584, "Coreopsis 'Firefly'", "名前だけの登録"), "Co02": (342583, "Coreopsis 'Mercury Rising' (Big Bang Series)", ""),
 "Co03": (285381, "Coreopsis 'Redshift'", ""), "Co04": (71026, "Coreopsis rosea 'American Dream'", ""),
 "Co05": (4370, "Coreopsis verticillata 'Moonbeam'", ""), "Co06": (89827, "Coreopsis verticillata 'Zagreb'", ""),
 "Co07": (316205, "Coreopsis 'Star Cluster' (Big Bang Series)", "RHS で未確定（Unresolved）。RHS は種小名なし（マスターは × verticillata）"),
 "Er02": (249929, "Eryngium planum 'Blue Glitter'", ""),
 "Er03": (248909, "Eryngium planum 'Blue Hobbit'", "RHS には 'Blauer Zwerg'（114505）も別のページとしてある"),
 "Er04": (307375, "Eryngium planum 'White Glitter'", ""),
 "Er05": (353689, "Eryngium variifolium 'Miss Marble'", "RHS ではシノニム扱い（正名は要確認）"), "Er06": (25532, "Eryngium yuccifolium", ""),
 "Li01": (10063, "Liatris pycnostachya", ""), "Li02": (181865, "Liatris scariosa", "名前だけの登録"), "Li03": (103721, "Liatris scariosa 'Alba'", ""),
 "Li04": (10064, "Liatris spicata", ""), "Li05": (56246, "Liatris spicata 'Floristan Violett'", "マスターは 'Floristan Violet'"),
 "Li06": (84510, "Liatris spicata 'Floristan Weiss'", "マスターは 'Floristan White'（RHS では [Floristan White] はこの品種の別名）"),
 "Li07": (83847, "Liatris spicata 'Kobold'", ""),
 "Ly01": (270732, "Lysimachia congestiflora 'Midnight Sun'", ""), "Ly03": (10632, "Lysimachia nummularia", ""),
 "Ly04": (47321, "Lysimachia nummularia 'Aurea'", ""), "Ly05": (10634, "Lysimachia punctata L.", ""),
 "Ly06": (61125, "Lysimachia punctata 'Alexander' (v)", ""), "Ly07": (10637, "Lysimachia vulgaris", ""),
 "Mi02": (118613, "Miscanthus sinensis var. condensatus 'Cosmopolitan' (v)", "RHS は変種 var. condensatus の品種としている（sinensis 'Cosmopolitan' はシノニム扱い）"),
 "Mi03": (189436, "Miscanthus sinensis 'Little Zebra' (v)", ""), "Mi04": (54584, "Miscanthus sinensis 'Morning Light' (v)", ""),
 "Mi05": (155419, "Miscanthus 'Purpurascens'", "RHS は種小名なし（sinensis var. purpurascens は誤用の名前としてシノニム扱い）"),
 "Mi06": (80383, "Miscanthus sinensis 'Gracillimus'", "RHS は品種 'Gracillimus' として掲載（マスターは f. gracillimus）"),
 "Mo01": (129087, "Molinia caerulea subsp. caerulea 'Dauerstrahl'", ""), "Mo02": (49857, "Molinia caerulea subsp. caerulea 'Heidebraut'", ""),
 "Mo03": (84915, "Molinia caerulea subsp. arundinacea 'Transparent'", ""), "Mo04": (118189, "Molinia caerulea subsp. caerulea 'Moorflamme'", ""),
 "Mo05": (47257, "Molinia caerulea subsp. caerulea 'Moorhexe'", "マスターは 'Moorhex'"), "Mo06": (86082, "Molinia caerulea subsp. caerulea 'Variegata' (v)", ""),
 "Vs01": (177034, "Veronicastrum sibiricum", ""), "Vs02": (156003, "Veronicastrum sibiricum var. yezoense", "名前だけの登録"),
 "Vs03": (511863, "Veronicastrum virginicum 'Adoration'", ""), "Vs04": (228380, "Veronicastrum virginicum 'Erica'", "RHS で未確定（Unresolved）。マスターは 'Erika'"),
 "Vs05": (109381, "Veronicastrum virginicum 'Fascination'", ""), "Vs06": (111539, "Veronicastrum virginicum 'Lavendelturm'", ""),
 "Vs07": (114022, "Veronicastrum virginicum 'Album'", "RHS は品種 'Album' を正名とし、f. albiflorum をその別名としている"),
}
# 番号を確かめていないもの: Er01 Eryngium planum・Mi01 Miscanthus sinensis（種のページ。検索では品種しか出なかった）、Ly02 congestiflora 'Variegata'（品種のページなし。種は 55037 で名前だけ）
