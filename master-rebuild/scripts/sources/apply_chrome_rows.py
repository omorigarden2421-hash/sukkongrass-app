"""Jelitto(s11)・Gaißmayer(s17) の evidence を、RULES.md の決定（2026-11-19）に沿って trial/rows/Pxx.json に当てはめる。

使い方: python3 -I scripts/sources/apply_chrome_rows.py <trial フォルダ>
決定: 順位は最下位（s18 > s17 > s11）。空欄を埋めるのに使い、すでに値がある項目は変えない。
ゾーン・花期・高さ・暑さは値に使わない。Jelitto が発表元の P05・P12 は s12 と同じ順位。
すでに値がある項目で s17・s11 が違うことを書いている場合は、値は変えずに conflicts に書く。
何度実行しても同じ結果になる（"by": "chrome" の印を付けた記録を入れ直す）。
"""
import json
import sys

TRIAL = sys.argv[1]
TAG = "chrome"
NOTE_MARK = " 2026-11-19（Jelitto・Gaißmayer）: "

# 空欄を埋める: (試作ID, field, 値, method, sources, level, note, 変更理由)
FILL = [
 ("P18", "flower_color_detail", "クリーム白", "記載", ["s17", "s11"], "cultivar",
  "Gaißmayer cremeweiß／Jelitto creamy-white（どちらも 'Fräulein' の品種ページ）",
  "Gaißmayer・Jelitto に 'Fräulein' の品種ページがあり、花色の記述が加わった"),
 ("P18", "flower_color_class", ["白"], "判定", ["s17", "s11"], "cultivar", "クリーム白を 白 に当てはめた",
  "Gaißmayer・Jelitto の品種ページの花色（クリーム白）から"),
 ("P18", "accepted_name", "Lupinus 'Fräulein'", "記載", ["s18", "s17", "s11"], "cultivar",
  "2026-11-19 ユーザー決定: 種小名を書かない形にする。品種名 'Fräulein'（ウムラウトあり）は stauden.de・Gaißmayer・Jelitto で一致。種の扱いは Lupinus polyphyllus（stauden.de）、Polyphyllus-Hybride（Gaißmayer、育種者 Benary 1958）、L. perennis Russell Band of Nobles Series（Jelitto）と割れている。RHS・Kew では確認できない",
  "3文献で品種名が一致。種の扱いが割れているため、種小名なしで書く（ユーザー決定）"),
 ("P18", "synonyms", ["'Noble Maiden'（Jelitto が併記する英名）"], "記載", ["s11"], "cultivar",
  "Jelitto の表記: LUPINUS perennis Russell Band of Nobles Series 'Fräulein' [Noble Maiden]",
  "Jelitto の品種ページに別名 [Noble Maiden] の併記があった"),
 ("P17", "waterside", True, "判定", ["s17"], "species",
  "Gaißmayer: 池の縁など湿った場所向きの丈夫なグラウンドカバー。Lebensbereich に WR4（水辺・湿地）を含む",
  "Gaißmayer に、池の縁・湿地に向く記述があった（景観構成用途の 水辺向き に使う）"),
 ("P19", "fragrance", "花", "判定", ["s17"], "species",
  "Gaißmayer: 花のにおいは好みが分かれる、という記述（良い香りという意味ではない）。商品が種そのものなので種の記述を使った",
  "Gaißmayer に花のにおいの記述があった"),
 ("P21", "invasive_note", "こぼれ種が多く、きちんと整った庭には勧められない。避けるには花後すぐに全体を切り戻す", "記載", ["s17"], "species",
  "Gaißmayer の種（Geranium phaeum）のページの記述。'Mourning Widow' でも同じかは品種の記述がなく未確認",
  "Gaißmayer（種のページ）に広がりすぎの注意があった"),
 ("P22", "synonyms", ["Phlox amplifolia 'David'"], "記載", ["s17"], "cultivar", "Gaißmayer: ehemals（以前の表記）Phlox amplifolia 'David'",
  "Gaißmayer の品種ページに以前の表記があった"),
 ("P22", "self_seed_level", 1, "判定", ["s17"], "cultivar",
  "Gaißmayer（品種への回答）: 花後に切り戻すと種が熟すのを防ぎ、望まない実生を防げる → 1（こぼれ種することがある）",
  "Gaißmayer の回答に、切り戻さないと実生が出る記述があった"),
]

# 値は変えず、食い違いとして書く: (試作ID, field, detail)
CONFLICT = [
 ("P08", "drought", "NC State・Walters は乾燥に耐える（強）／Gaißmayer は「夏に土が乾きすぎると育たない、さび病が出やすくなる」。優先順位で 強 のまま"),
 ("P19", "self_seed_level", "NC State は 1（こぼれ種することがある）／Gaißmayer は「こぼれ種でよく増える」（2 相当）。優先順位で 1 のまま"),
 ("P21", "self_seed_level", "MBG・stauden.de は 1／Gaißmayer（種）は「こぼれ種が多い」（2 相当）。優先順位で 1 のまま"),
 ("P22", "spread_modes", "Walters・NC State は株立ち（clump）／stauden.de と Gaißmayer（どちらも品種ページ）は短いほふく枝を出すとする。優先順位で 株立ち のまま（2026-11-19 ユーザー決定。地下茎で広がる程度も空欄のまま）"),
 ("P23", "drought", "MBG は medium moisture（中）／Gaißmayer（種）は「乾燥と日なたにとてもよく耐える」。優先順位で 中 のまま"),
]

# フィールドの note に書き足す（値は null のまま）: (試作ID, field, 追記)
FIELD_NOTE = [
 ("P05", "spread_modes", "Jelitto（発表元。s12 と同じ順位）は Growth Habit: clumping（株立ち）。Walters（s10、上位）の「広がってパッチ状になる」との食い違いは残るため空欄のまま"),
 ("P17", "fragrance", "Gaißmayer の表に Duftend: ja（香りあり）とあるが、花か葉かの記載がないため空欄のまま"),
 ("P18", "fragrance", "Gaißmayer の表に Duftend: ja（香りあり）とあるが、花か葉かの記載がないため空欄のまま"),
 ("P22", "rhizome_level", "Gaißmayer（品種）は「短いほふく枝で少しずつ大きく密な株になる」とするが、増え方を上位の文献どおり株立ちにしたので空欄のまま（2026-11-19 ユーザー決定）"),
 ("P10", "rhizome_level", "Gaißmayer: 肥料が十分なら大きな株になる、とあるが、広がらないことの明記ではないため空欄のまま"),
]

# name_review の理由に書き足す
NAME_REVIEW = {
 "P18": "Jelitto は LUPINUS perennis Russell Band of Nobles Series 'Fräulein' [Noble Maiden]、Gaißmayer は Lupinus Polyphyllus-Hybride 'Fräulein' と表記。Band of Nobles Series の一色であること、ウムラウト付きの Fräulein であることは3文献（stauden.de・Jelitto・Gaißmayer）で一致。種の扱いは polyphyllus（交配種）が2文献、perennis が1文献。ユーザー決定で、学名は種小名なしの Lupinus 'Fräulein' とした",
 "P22": "Gaißmayer は以前 Phlox amplifolia 'David' と表記していた（今は Phlox paniculata 'David'）",
 "P23": "Jelitto は種（ANEMONE sylvestris）の種子に [Madonna] の別名を併記している。'Madonna' が種と区別できる品種かどうかの確認が必要",
}

# 学名の検討シートの「文献の正名（提案）」を置き換える（ユーザー決定）
PROPOSED = {"P18": "Lupinus 'Fräulein'（2026-11-19 ユーザー決定。種小名なし）"}

NOTES = {
 "P03": "Jelitto・Gaißmayer は種のページのみ。値の変更なし（耐寒ゾーンの食い違いは記録だけ）",
 "P09": "Jelitto は種の種子のページ、Gaißmayer は品種ページ。値の変更なし（最初の冬の保護、ドイツではほとんど咲かない、は該当する項目がなく記録だけ）",
 "P12": "Jelitto は発表元（s12 と同じ順位）。上位の文献と食い違う記述はなく、値の変更なし",
 "P20": "Jelitto・Gaißmayer は Tricyrtis hirta（種）のページのみ。値の変更なし",
}


def main():
    done = set()
    for n in range(1, 29):
        pid = f"P{n:02d}"
        path = f"{TRIAL}/rows/{pid}.json"
        d = json.load(open(path, encoding="utf-8"))
        f = d["fields"]
        # 前回この処理で入れた分を取り消す
        for c in [c for c in d.get("changes_20261119", []) if c.get("by") == TAG]:
            f[c["field"]] = c["prev"]
        d["changes_20261119"] = [c for c in d.get("changes_20261119", []) if c.get("by") != TAG]
        d["conflicts"] = [c for c in d.get("conflicts", []) if not (isinstance(c, dict) and c.get("by") == TAG)]
        for k, x in f.items():
            if isinstance(x.get("note"), str):
                x["note"] = x["note"].split(NOTE_MARK)[0]
                if not x["note"]:
                    del x["note"]
        if (d.get("name_review") or {}).get("by") == TAG:
            d["name_review"] = None
        if d.get("name_review") and "proposed_prev" in d["name_review"]:
            d["name_review"]["proposed"] = d["name_review"].pop("proposed_prev")
        if d.get("name_review") and isinstance(d["name_review"].get("reason"), str):
            d["name_review"]["reason"] = d["name_review"]["reason"].split(NOTE_MARK)[0]
        d["notes"] = (d.get("notes") or "").split(NOTE_MARK)[0]

        for i, (p, field, value, method, sources, level, note, why) in enumerate(FILL):
            if p != pid:
                continue
            prev = f.get(field) or {"value": None}
            if prev.get("value") not in (None, [], ""):
                raise SystemExit(f"{pid} {field}: すでに値がある（{prev['value']}）。空欄だけを埋める決まり")
            f[field] = {"value": value, "method": method, "sources": sources, "level": level, "note": note}
            d["changes_20261119"].append({"field": field, "old": None, "new": value, "reason": "Jelitto・Gaißmayer: " + why,
                                          "by": TAG, "prev": prev})
            done.add(("F", i))
        for i, (p, field, detail) in enumerate(CONFLICT):
            if p == pid:
                if f.get(field, {}).get("value") in (None, [], ""):
                    raise SystemExit(f"{pid} {field}: 値がないのに食い違いを書こうとしている")
                d["conflicts"].append({"field": field, "detail": detail, "by": TAG})
                done.add(("C", i))
        for i, (p, field, text) in enumerate(FIELD_NOTE):
            if p == pid:
                x = f.setdefault(field, {"value": None})
                x["note"] = (x.get("note") or "") + NOTE_MARK + text
                done.add(("N", i))
        if pid in NAME_REVIEW:
            nr = d.get("name_review")
            if nr:
                nr["reason"] = (nr.get("reason") or "") + NOTE_MARK + NAME_REVIEW[pid]
                if pid in PROPOSED:
                    nr.setdefault("proposed_prev", nr.get("proposed"))
                    nr["proposed"] = PROPOSED[pid]
            else:
                d["name_review"] = {"current": None, "proposed": None, "reason": NOTE_MARK.strip() + " " + NAME_REVIEW[pid],
                                    "source": "s17 / s11", "by": TAG}
        if pid in NOTES:
            d["notes"] += NOTE_MARK + NOTES[pid]
        json.dump(d, open(path, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    n = len(FILL) + len(CONFLICT) + len(FIELD_NOTE)
    if len(done) != n:
        raise SystemExit("当てはめ先のない記録がある")
    print("埋めた項目", len(FILL), "食い違い", len(CONFLICT), "メモ", len(FIELD_NOTE))


main()
