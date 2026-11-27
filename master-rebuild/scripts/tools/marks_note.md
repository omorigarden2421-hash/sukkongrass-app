# 印の取り込み（2026-11-27）

RHS の詳細ページの「Plants for Pollinators」（For Biodiversity の印）と、植える場所（Suggested planting locations and garden types）の「Cut flowers」、
Gaißmayer の表の「Schnittgeeignet: ja」は、前は値を取り出すときに拾っていなかった。蜜源・切り花の読み直し（2026-11-26）の入力にも入っていなかった。
ユーザー「直す」（2026-11-27）。

## 取り出し
- scripts/pilot/assemble_pilot.py の rhs() で `_cutflowers`・`_pollinators` を取る。切り花の書き出し（DUMP_CUT）の Gaißmayer に表の Schnittgeeignet を足した
- 環境変数 DUMP_MARKS を付けて rediff.py を回すと、全品種の印を marks_dump.jsonl に書き出す（値は変えない）

## 読み直しの値に入れる（scripts/tools/apply_marks.py。決め方は poll_reread_note.md・cut_reread_note.md と同じ）
- 蜜源：RHS の Plants for Pollinators は ◎（段階 品種・確かさ 高）。読み直しが ◎ なら変えない。△ なら変えずに食い違いとして出す
- 切り花：読み直しが空欄のときだけ ○ にする（印だけなので ◎ にはしない。○・◎ は変えない。△ は変えずに食い違いとして出す）
  - RHS の Cut flowers、Gaißmayer の品種のページ（または品種名のない商品の種のページ）の Schnittgeeignet → ○・段階 品種（または種）・確かさ 中
  - 品種名のある商品に Gaißmayer の種のページだけ → ○・段階 種・確かさ 低（2026-11-26 の決定「種も使う（○まで）」）。草丈 最大 30cm 以下は当てない（2026-11-27 の決定「外す」）。species_check.json で 外す にした品種にも当てない
- メモの末尾に「（2026-11-27 印の取り込み：…。前の読み直し：…）」
- species_check.json（品種なのに種の値を使った項目の確かめ）で 外す・迷う にした蜜源でも、RHS の品種のページに印があれば、値は品種のページから決まるので 残す にする
