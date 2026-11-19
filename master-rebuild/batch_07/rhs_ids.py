# RHS（s01）の植物ページの番号: スカビオサ・ポレモニウム・フィリペンデュラ・サンギソルバ・トロリウス。探し方は scripts/pilot/rhs_ids.py と同じ（2026-11-20。アプリ内のブラウザーで検索ページを順に開いた）。
# 候補63ページを curl で読み、Name Status（Accepted／Correct／Synonym／Unresolved）と栽培の項目の有無を見て選んだ。
# RHS はスカビオサ コーカシカの品種をどれも Synonym としている（正名は要確認。ほかの文献では Lomelosia caucasica）。オクロレウカは Scabiosa columbaria subsp. ochroleuca。
# 試行ID: (番号, RHS の表記, メモ)
RHS = {
 "Sc01": (79278, "Scabiosa caucasica 'Kompliment'", "RHS ではシノニム扱い（正名は要確認）。マスターは 'Compliment'。名前だけの登録"),
 "Sc02": (286941, "Scabiosa caucasica 'Perfecta Blue' (Perfecta Series)", "RHS ではシノニム扱い（正名は要確認）。マスターの学名は 'Blue Perfection'、商品名はパーフェクタ"),
 "Sc03": (52291, "Scabiosa caucasica 'Fama'", "RHS ではシノニム扱い（正名は要確認）。名前だけの登録。栽培の項目があるのは 'Fama Deep Blue'（316389）で、同じ品種かは未確認"),
 "Sc04": (76478, "Scabiosa caucasica 'Perfecta Alba' (Perfecta Series)", "RHS ではシノニム扱い（正名は要確認）"),
 "Sc05": (304927, "Scabiosa 'Vivid Vi'", "RHS は 'Vivid Vi' を採用名（Adopted）とし、'Vivid Violet'（281840）をその別名としている"),
 "Sc06": (68299, "Scabiosa columbaria subsp. ochroleuca", "RHS は columbaria の亜種としている（Scabiosa ochroleuca はシノニム扱い）"),
 "Sc07": (256456, "Scabiosa columbaria subsp. ochroleuca 'Moon Dance'", "RHS は columbaria の亜種の品種としている（マスターは Scabiosa ochroleuca）"),
 "Pl01": (152417, "Polemonium boreale 'Heavenly Habit'", ""),
 "Pl02": (343630, "Polemonium caeruleum subsp. caeruleum f. album", "RHS は品種ではなく品種群（f. album）として掲載。マスターは 'Album'"),
 "Pl03": (80465, "Polemonium carneum 'Apricot Delight'", "RHS は carneum の品種としている（caeruleum 'Apricot Delight' はシノニム扱い）"),
 "Pl04": (192947, "Polemonium viscosum 'Blue Whirl'", "RHS ではシノニム扱い（正名は要確認）。名前だけの登録。種は viscosum（マスターは caeruleum）"),
 "Pl05": (256393, "Polemonium caeruleum 'Filigree Clouds'", "名前だけの登録"), "Pl06": (256392, "Polemonium caeruleum 'Filigree Skies'", "名前だけの登録"),
 "Pl07": (115423, "Polemonium yezoense var. hidakanum 'Purple Rain'", ""),
 "Fi01": (215074, "Filipendula multijuga 'Fuji Haze' (v)", "名前だけの登録"), "Fi02": (7218, "Filipendula purpurea", ""),
 "Fi03": (96034, "Filipendula purpurea 'Elegans'", ""),
 "Fi04": (95088, "Filipendula rubra 'Venusta'", "RHS は 'Venusta' を正名とし、'Venusta Magnifica'・'Magnifica' をその別名としている"),
 "Fi05": (32871, "Filipendula ulmaria", ""), "Fi06": (75800, "Filipendula ulmaria 'Variegata' (v)", ""),
 "Sa01": (72832, "Sanguisorba albiflora", ""), "Sa02": (16402, "Sanguisorba hakusanensis", ""), "Sa03": (102853, "Sanguisorba menziesii", ""),
 "Sa04": (166635, "Sanguisorba officinalis 'Lemon Splash' (v)", "RHS は officinalis の品種としている（obtusa 'Lemon Splash' はシノニム扱い）"),
 "Sa05": (318232, "Sanguisorba 'Pink Tanna'", "RHS は種小名なし（officinalis 'Pink Tanna' はシノニム扱い）"),
 "Sa06": (345244, "Sanguisorba officinalis subsp. microcephala", "RHS で未確定（Unresolved）。名前だけの登録。マスターは var. microcephala"),
 "Sa07": (263267, "Sanguisorba tenuifolia var. alba", "RHS は変種（var. alba）として掲載。マスターは 'Alba'"),
 "Sa08": (336575, "Sanguisorba tenuifolia 'Bordeaux'", "RHS で未確定（Unresolved）"),
 "Tr01": (54725, "Trollius chinensis 'Golden Queen'", ""), "Tr02": (84184, "Trollius × cultorum 'Lemon Queen'", ""),
 "Tr03": (315949, "Trollius × cultorum 'New Moon'", ""), "Tr04": (297983, "Trollius europaeus 'Lemon Supreme'", "名前だけの登録"),
 "Tr06": (118464, "Trollius × cultorum 'Cheddar'", "RHS ではシノニム扱い（ページの英名は globeflower 'Taleggio'。'Taleggio' の別名とみられる。正名は要確認）"),
}
# 見つからなかったもの: Tr05 'Yellow Queen'（検索に出ない。種のページは 18449 Trollius europaeus）
