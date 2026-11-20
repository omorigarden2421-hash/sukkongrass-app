# RHS（s01）の植物ページの番号: 在庫のない1品種の属19（アゲラティナからバレリアナまで）。
# 探し方は scripts/pilot/rhs_ids.py と同じ（2026-11-20。アプリ内のブラウザーで、17個目のまとまりの分と合わせて検索ページ78件を順に開いた）。
#   候補24ページを scripts/tools/rhs_check.py で読み、Name Status と栽培の項目の有無を見て選んだ。
# 試行ID: (番号, RHS の表記, メモ)
RHS = {
 "Af01": (257109, "Ageratina altissima 'Chocolate'", "Eupatorium rugosum 'Chocolate' は RHS でシノニム扱い"),
 "Tn01": (58882, "Anthemis tinctoria 'Alba'", "名前だけの登録。RHS ではシノニム扱い（種の正名は Cota tinctoria）"),
 "Cp01": (3382, "Cephalaria gigantea", ""), "Cz01": (3401, "Cerastium tomentosum", ""),
 "Cj01": (210071, "Chamaenerion angustifolium", "RHS の正名は Chamaenerion angustifolium（マスターは Chamerion）"),
 "Cv01": (114159, "Convallaria keiskei", "名前だけの登録"),
 "Cq01": (221912, "Corydalis leucanthema 'Silver Spectre' (v)", "RHS で未確定（Unresolved）"),
 "Gi01": (7989, "Gillenia trifoliata", ""), "Gb01": (8054, "Globularia trichosantha", "名前だけの登録"),
 "Ko01": (9771, "Koeleria glauca", ""),
 "Ls01": (255032, "Leucosceptrum japonicum 'Golden Angel'", "名前だけの登録。RHS に f. aureum の名前はない（Jelitto が f. aureum の流通名として 'Golden Angel' を書いているので当てた。要確認）"),
 "On01": (85496, "Oenanthe javanica 'Flamingo' (v)", ""), "Ol01": (24959, "Orlaya grandiflora", ""),
 "Pg01": (383623, "Salvia yangii (Pe)", "RHS の正名は Salvia yangii（Perovskia atriplicifolia はシノニム扱い）"),
 "Sj01": (16488, "Satureja spicigera", "Satureja repanda は RHS でシノニム扱い"),
 "Sx01": (120675, "Selinum wallichianum", "RHS ではシノニム扱い（Selinum tenuifolium・Cortia wallichiana もシノニム。正名は要確認）"),
 "Sb01": (108702, "Sporobolus heterolepis", ""), "Va01": (18738, "Valeriana officinalis", ""),
}
# 見つからなかったもの・当てていないもの: Pb01 プロスタンテラ（ミントブッシュ。種が未確定なので当てていない。RHS には cuneata・rotundifolia・ovalifolia・lasianthos などのページがある）。
