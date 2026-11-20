# RHS（s01）の植物ページの番号: チャスマンティウム・ケロネ・エキノプス・エリムス・エリゲロン・ガリウム・グレコマ・カリメリス・ラベンダー・レウカンセマム・リスラム・パキサンドラ・フロミス・サギナ・
#   サポナリア・センペルビブム・シルフィウム・スティパ・シンフィオトリクム・ビバーナム・ユッカ・ヒューケレラ・トリフォリウム。
# 探し方は scripts/pilot/rhs_ids.py と同じ（2026-11-20。アプリ内のブラウザーで検索ページ53件を順に開いた）。候補60ページを scripts/tools/rhs_check.py で読み、Name Status と栽培の項目の有無を見て選んだ。
# 試行ID: (番号, RHS の表記, メモ)
RHS = {
 "Ch01": (45715, "Chasmanthium latifolium", ""), "Ch02": (344841, "Chasmanthium latifolium 'Little Tickler'", "名前だけの登録"),
 "Cl01": (3715, "Chelone obliqua", ""),
 "Ec01": (273633, "Echinops bannaticus 'Star Frost'", ""), "Ec02": (194025, "Echinops ritro subsp. ruthenicus 'Platinum Blue'", ""),
 "Eg01": (114502, "Erigeron 'Rosa Juwel'", "RHS の正名はドイツ語の 'Rosa Juwel'、種小名なし（'Pink Jewel' はシノニム扱い）"),
 "Eg02": (32487, "Erigeron karvinskianus", "RHS は 'Profusion' を種（Erigeron karvinskianus）のシノニムとしている（品種として分けていない）"),
 "El01": (366838, "Elymus canadensis 'Icy Blue'", "名前だけの登録"), "El02": (54735, "Elymus magellanicus", ""),
 "Gc01": (8034, "Glechoma hederacea", ""), "Gc02": (71551, "Glechoma hederacea 'Variegata' (v)", ""),
 "Gm01": (7595, "Galium odoratum", ""), "Gm02": (7596, "Galium verum", ""),
 "Hr01": (219310, "× Heucherella 'Stoplight'", ""), "Hr02": (193754, "× Heucherella 'Sunspot' (v)", "名前だけの登録"), "Hr03": (281268, "× Heucherella 'Tapestry'", ""),
 "Ka01": (28154, "Kalimeris incisa", ""),
 "Ka02": (138635, "Kalimeris incisa 'Variegata'", "RHS ではシノニム扱い（別名に Kalimeris yomena 'Variegata' を併記。正名は要確認）"),
 "La01": (96353, "Lavandula angustifolia 'Hidcote'", ""), "La02": (99904, "Lavandula angustifolia 'Munstead'", ""),
 "Le01": (180315, "Leucanthemum × superbum 'Snowdrift'", ""),
 "Le02": (270116, "Leucanthemum × superbum [Broadway Lights] ('Leumayel')", "Broadway Lights は流通名、品種名は 'Leumayel'"),
 "Lt01": (10645, "Lythrum salicaria", ""),
 "Pc01": (12099, "Pachysandra terminalis", ""), "Pc02": (91844, "Pachysandra terminalis 'Variegata' (v)", ""),
 "Ph01": (12705, "Phlomis russeliana", ""),
 "Ph02": (210152, "Phlomis tuberosa 'Bronze Flamingo'", "RHS ではシノニム扱い（Jelitto は種の流通名としている。正名は要確認）"),
 "Sg01": (78129, "Sagina subulata", ""), "Sg02": (70509, "Sagina subulata var. glabrata 'Aurea'", ""),
 "Sl01": (17357, "Silphium laciniatum", ""), "Sl02": (369899, "Silphium mohrii", "栽培の項目が少ないページ"),
 "Sm02": (74195, "Sempervivum 'Bronco'", ""),
 "Sn01": (85076, "Saponaria officinalis 'Alba Plena' (d)", "名前だけの登録。RHS で未確定（Unresolved）"), "Sn02": (66191, "Saponaria officinalis 'Rosea Plena' (d)", ""),
 "Su01": (161388, "Stipa ichu", "RHS の正名は Stipa ichu（Jarava ichu はシノニム扱い）"), "Su02": (58857, "Stipa tenuissima", ""),
 "Sy02": (340276, "Symphyotrichum novi-belgii 'Jenny'", ""),
 "Tf01": (52266, "Trifolium ochroleucon", "RHS のつづりは ochroleucon（ochroleucum はシノニム扱い）"),
 "Tf02": (18369, "Trifolium repens 'Atropurpureum'", "名前だけの登録。RHS で未確定（Unresolved）"),
 "Tf03": (175583, "Trifolium repens 'Dragon's Blood'", "RHS で未確定（Unresolved）"), "Tf04": (55067, "Trifolium repens 'Wheatfen'", "名前だけの登録"),
 "Tf05": (41779, "Trifolium rubens", ""), "Tf06": (358920, "Trifolium rubens 'Frosty Feathers'", "RHS で未確定（Unresolved）"),
 "Vu01": (94896, "Viburnum plicatum f. tomentosum 'Mariesii'", ""), "Vu02": (70552, "Viburnum sargentii 'Onondaga'", ""),
 "Yu01": (44109, "Yucca filamentosa 'Bright Edge' (v)", ""), "Yu02": (65193, "Yucca gloriosa 'Variegata' (v)", ""),
}
# 見つからなかったもの・当てていないもの: Cl02 ケロネ オブリクア 'Alba'（RHS は Chelone obliqua var. alba を Chelone glabra の白花のシノニムとしている。別の種になるので当てていない）、
#   Lt02 'Happy Snow'、Sm01（品種名のないセンペルビブム）、Sy01 'Jolly Jumper'（RHS に名前がない）
