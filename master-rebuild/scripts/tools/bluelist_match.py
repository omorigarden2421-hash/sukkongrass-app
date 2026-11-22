"""北海道ブルーリスト2010（植物）と、まとめの表の品種を照らし、hokkaido_bluelist.json を作る。

使い方（master-rebuild で）: python -X utf8 scripts/tools/bluelist_match.py <まとめの表.xlsx>

- 一覧は scripts/tools/data/hokkaido_bluelist2010_plants.tsv（北海道庁「北海道ブルーリスト2010選定結果」の PDF の
  植物の表 639 種を書き写したもの。PDF は文字が取り出せないので、画面で読んで書き写した。国外 586・国内 49・不明 4 で PDF の数と一致）
- 一覧は和名だけ。照らし方は2つ:
  1. 表の「和名」（YList の標準和名）が、一覧の種名と同じ。一覧の異名と同じときは、下の SYN_OK で同じ種と確かめたものだけ
  2. 和名が違う・ないが、学名で同じ種と分かるもの（SCI。学名の属＋種小名で当てる）
- 種として当てる。品種・変種の違いは見ない（環境省のリストと同じ）。変種が違うときは note に書く
"""
import csv, json, os, re, sys
import openpyxl

XLSX = sys.argv[1]
HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "..", "..", "hokkaido_bluelist.json")

# 一覧の異名で当たったときに、同じ種と確かめたもの（表の和名 → 一覧の種名）
SYN_OK = {
    "セイヨウジュウニヒトエ": "セイヨウキランソウ",  # Ajuga reptans
    "スイセンノウ": "フランネルソウ",  # Lychnis coronaria
    "ジギタリス": "キツネノテブクロ",  # Digitalis purpurea
    "ミドリハッカ": "オランダハッカ",  # Mentha spicata
    "ルリタマアザミ": "ルリタマアザミ",
}
# 異名で当たるが、別の種なので当てないもの（記録）
SYN_NG = {
    "ヤグルマソウ": "一覧の「ヤグルマギク」の異名。表の ヤグルマソウ はロジャーシア（Rodgersia podophylla）で別の植物",
    "ヤグルマハッカ": "一覧の「タイマツバナ」（Monarda didyma）の異名に載っている。表の品種は Monarda fistulosa で別の種",
}
# 学名で同じ種と分かるもの（属＋種小名 → 一覧の種名, note）
SCI = {
    "Crocosmia × crocosmiiflora": ("ヒメヒオウギズイセン", "一覧の異名 モントブレチア"),
    "Melissa officinalis": ("セイヨウハッカ", "一覧の異名 レモンバーム。表の和名は コウスイハッカ"),
    "Mentha × piperita": ("コショウハッカ", "一覧の異名 ペパーミント"),
    "Phalaris arundinacea": ("クサヨシ", "斑入りの変種（シマヨシ）も種として当てた"),
    "Glechoma hederacea": ("コバノカキドオシ", "一覧の異名 セイヨウカキドオシ。表の和名は カキドオシ（日本の亜種）。種として当てた"),
    "Prunella vulgaris": ("セイヨウウツボグサ", "表の和名は ウツボグサ（日本の亜種）。種として当てた"),
    "Campanula punctata": ("ホタルブクロ", "表の和名は ヤマホタルブクロ（変種）。種として当てた"),
    "Iris ensata": ("ハナショウブ", "表の和名は ノハナショウブ（野生の変種）。種として当てた"),
    "Arrhenatherum elatius": ("オオカニツリ", "一覧の異名 トールオートグラス。表の和名は チョロギガヤ（変種）。種として当てた"),
}


def species(sci):
    s = re.sub(r"[‘’'\"].*$", "", sci or "").replace("×", " × ")
    s = re.sub(r"\s+x\s+", " × ", s)
    w = s.split()
    if len(w) >= 3 and w[1] == "×":
        return " ".join(w[:3])
    return " ".join(w[:2])


def main():
    bl, by = [], {}
    with open(os.path.join(HERE, "data", "hokkaido_bluelist2010_plants.tsv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            bl.append(r)
            by.setdefault(r["種名"], r)
    syn = {}
    for r in bl:
        for n in [x for x in r["異名"].split("、") if x]:
            syn.setdefault(n, r)

    ws = openpyxl.load_workbook(XLSX, read_only=True)["マスター（下書き916品種）"]
    R = list(ws.iter_rows(values_only=True)); h = R[1]
    ino, iw, ig = h.index("商品番号"), h.index("和名"), h.index("学名（正名）")
    out = {}
    for r in R[2:]:
        no, w, sci = str(r[ino]), (r[iw] or "").strip(), r[ig] or ""
        hit = None
        if w in by:
            hit = (by[w], "表の和名が一覧の種名と同じ", "")
        elif w in SYN_OK and SYN_OK[w] in by:
            hit = (by[SYN_OK[w]], "表の和名が一覧の異名と同じ（同じ種と確かめた）", "")
        else:
            sp = species(sci)
            if sp in SCI:
                name, note = SCI[sp]
                hit = (by[name], "学名で同じ種", note)
        if hit:
            b, how, note = hit
            out[no] = {"学名": sci, "和名": w, "一覧の種名": b["種名"], "カテゴリー": b["カテゴリー"],
                       "原産地の区分": b["原産地の区分"], "照らし方": how, "note": note}
        elif w in SYN_NG:
            out[no] = {"学名": sci, "和名": w, "当てない": SYN_NG[w]}
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    n = [v for v in out.values() if "カテゴリー" in v]
    from collections import Counter
    print("当たった品種:", len(n), Counter(v["カテゴリー"] for v in n))


if __name__ == "__main__":
    main()
