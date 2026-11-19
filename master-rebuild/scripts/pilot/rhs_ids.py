# RHS（s01）の植物ページの番号。3属の試行用。
# 探し方（2026-11-19）: RHS の検索結果は JavaScript で描かれるので curl では読めない。ブラウザーで rhs.org.uk を開き、
# ページの中に見えない枠（iframe）を作って /plants/search-results?query=<属 品種名> を順番に開き、結果のリンクから番号を拾った。
# その後、候補の名前を見て人が選んだ（同名の別品種を避けるため）。詳細ページ https://www.rhs.org.uk/plants/<番号>/x/details は curl で読める。
# 試行ID: (番号, RHS の表記, メモ)
RHS = {
 "G01": (92274, "Geranium × cantabrigiense 'Biokovo'", ""), "G02": (7877, "Geranium endressii", ""),
 "G03": (7885, "Geranium himalayense", ""), "G04": (319810, "Geranium 'Azure Rush'", ""),
 "G05": (241922, "Geranium [Blue Sunrise] ('Blogold')", "品種名は 'Blogold'、Blue Sunrise は流通名"),
 "G06": (236965, "Geranium wallichianum 'Jolly Bee'", ""), "G07": (197528, "Geranium × oxonianum 'Katherine Adele'", ""),
 "G08": (137507, "Geranium 'Orion'", ""), "G09": (180971, "Geranium 'Tiny Monster'", ""),
 "G11": (95458, "Geranium × johnsonii 'Johnson's Blue'", ""), "G12": (94759, "Geranium macrorrhizum 'Album'", ""),
 "G13": (93462, "Geranium macrorrhizum 'Bevan's Variety'", ""), "G14": (74692, "Geranium macrorrhizum 'Spessart'", ""),
 "G15": (91252, "Geranium × oxonianum 'Wargrave Pink'", ""), "G17": (95015, "Geranium phaeum 'Album'", ""),
 "G18": (155261, "Geranium phaeum 'Margaret Wilson' (v)", ""), "G19": (180970, "Geranium phaeum 'Raven'", ""),
 "G20": (65850, "Geranium phaeum var. phaeum 'Samobor'", ""), "G21": (122459, "Geranium pratense striatum 'Splish-splash'", ""),
 "G22": (92120, "Geranium sanguineum 'Album'", ""), "G23": (85308, "Geranium sanguineum 'Max Frei'", ""),
 "G24": (141223, "Geranium sanguineum 'New Hampshire Purple'", "マスターは 'New Hampshire'。同じ品種か要確認"),
 "G25": (89025, "Geranium sanguineum var. striatum", ""), "G26": (89025, "Geranium sanguineum var. striatum", ""),
 "G27": (227334, "Geranium soboliferum 'Starman'", ""), "G28": (306605, "Geranium 'Fay Anna'", ""),
 "H01": (116494, "Hosta 'Abiqua Drinking Gourd'", ""), "H02": (94408, "Hosta 'August Moon'", ""), "H03": (89694, "Hosta 'Blue Cadet'", ""),
 "H04": (95375, "Hosta 'Bressingham Blue'", ""), "H05": (162009, "Hosta 'Cat's Eyes' (venusta) (v)", ""),
 "H06": (201512, "Hosta 'Christmas Candy'", ""), "H07": (238115, "Hosta 'Christmas Pageant' (v)", ""),
 "H08": (44888, "Hosta 'Christmas Tree' (v)", ""), "H09": (45620, "Hosta 'Diamond Tiara' (v)", ""),
 "H11": (169519, "Hosta 'Diana Remembered'", ""), "H12": (82812, "Hosta 'Gold Standard' (fortunei) (v)", ""),
 "H13": (96811, "Hosta 'Golden Tiara' (v)", ""), "H14": (115334, "Hosta 'Guacamole' (v)", ""), "H15": (169526, "Hosta 'Harvest Dandy'", ""),
 "H16": (92800, "Hosta 'Little Aurora' (tokudama hybrid)", ""), "H17": (116797, "Hosta 'Night before Christmas' (v)", ""),
 "H18": (64893, "Hosta 'Patriot' (v)", ""), "H19": (92830, "Hosta 'Pearl Lake'", ""), "H21": (343820, "Hosta 'Silver Halo' (v)", ""),
 "H23": (137011, "Hosta 'White Christmas' (undulata) (v)", "RHS には同名で (fortunei) の別ページ 166270 もある。stauden.de とおぎはらが undulata 系としているのでこちらを採った"),
 "H24": (40754, "Hosta 'Wide Brim' (v)", ""), "H25": (167610, "Hosta 'Wolverine' (v)", ""),
 "H26": (316812, "Hosta 'Yellow Polka Dot Bikini' (v)", ""), "H27": (91303, "Hosta (Tardiana Group) 'Halcyon'", ""),
 "H28": (51451, "Hosta (Tardiana Group) 'June' (v)", ""), "H29": (90814, "Hosta 'Frances Williams' (sieboldiana) (v)", ""),
 "H30": (85092, "Hosta sieboldii var. sieboldii f. kabitan (v)", "'Silver Kabitan' そのものではなく、カビタンギボウシのページ。要確認"),
 "H31": (81909, "Hosta undulata var. albomarginata (v)", ""),
 "V02": (51477, "Veronica austriaca subsp. teucrium 'Royal Blue'", ""), "V03": (60063, "Veronica chamaedrys 'Miffy Brute' (v)", ""),
 "V04": (47057, "Veronica 'Sunny Border Blue'", ""), "V05": (74889, "Veronica spicata subsp. incana", "マスターは Veronica incana"),
 "V06": (296874, "Veronica longifolia 'Pink Eveline'", ""), "V07": (194598, "Veronica prostrata 'Aztec Gold'", ""),
 "V09": (54910, "Veronica prostrata 'Mrs Holt'", ""), "V10": (18867, "Veronica spicata subsp. spicata", ""),
 "V11": (74788, "Veronica spicata 'Alba'", ""), "V12": (313176, "Veronica 'Atomic Amethyst Ray' (Atomic Ray Series)", ""),
 "V13": (180159, "Veronica spicata 'Blue Bouquet'", ""), "V14": (80549, "Veronica spicata subsp. spicata 'Nana'", ""),
 "V15": (50967, "Veronica 'Pink Damask'", "RHS には Veronica longifolia 'Pink Damask'（153465）のページもある"),
 "V16": (103959, "Veronica spicata 'Red Fox'", ""), "V18": (248883, "Veronica umbrosa 'Georgia Blue'", ""),
}
# 見つからなかったもの: G10 '夢サンシャイン'、G16 Geranium phaeum（種のページが検索の上位に出ない）、H10 'Diana Remembered Select'、
# H20 'Reiho'、H22 'Uchibane'、H32 Hosta venusta 'Variegated'、V01 Veronica austriaca（種）、V08 'Heavenly Blue'、
# V17 Veronica spicata 'Rose'（'Rosenrot' はあるが同じ品種か不明）
