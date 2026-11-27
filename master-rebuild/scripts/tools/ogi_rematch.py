"""2026-11-27 おぎはら植物図鑑の全掲載名（all_names.json。空の検索で取った 3201件）と、おぎはらをまだ当てていない品種を名前で照らし合わせ、候補を出す。
使い方（master-rebuild で）: ogi_rematch.py <all_names.json> <出力.json>
- 品種名のある商品: マスターの植物名の '…' の中（カタカナ）と、図鑑の ‘…’ の中を比べる（似ている度 0.8 以上）。属の名前（カタカナの最初の語）も見る
- 品種名のない商品: 植物名全体（かっこの中も別に）と、図鑑の掲載名を比べる
- 候補を出すだけ。当てるかどうかは、図鑑のページの学名を読んで決める
"""
import difflib, glob, importlib.util, json, os, re, sys, unicodedata

names = json.load(open(sys.argv[1], encoding="utf-8"))["names"]
done = {}  # (フォルダ, 試行ID) → (図鑑ID, level)
for p in sorted(glob.glob("batch_*/ogihara_data.py")) + ["scripts/pilot/ogihara_data.py"]:
    sp = importlib.util.spec_from_file_location("o", p)
    mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(mod)
    folder = "pilot" if "scripts" in p.replace("\\", "/") else os.path.dirname(p).replace("\\", "/")
    for rec in mod.OGIHARA:
        for k in rec[0]:
            done[(folder, k)] = (rec[1], rec[3])


def norm(s):
    s = unicodedata.normalize("NFKC", s or "")
    s = re.sub(r"[\s・\-‐－—―=＝.．,、]", "", s)
    s = s.replace("ヴァ", "バ").replace("ヴィ", "ビ").replace("ヴェ", "ベ").replace("ヴォ", "ボ").replace("ヴ", "ブ")
    s = s.replace("ー", "").replace("ッ", "").replace("ィ", "イ").replace("ェ", "エ").replace("ァ", "ア").replace("ォ", "オ").replace("ュ", "ユ").replace("ャ", "ヤ").replace("ョ", "ヨ")
    return s


def cv(s):
    m = re.search(r"['‘’`´＇\"“”]\s*(.+?)\s*['‘’`´＇\"“”]", unicodedata.normalize("NFKC", s or ""))
    return m.group(1) if m else None


Z = []
for zid, nm in names.items():
    c = cv(nm)
    Z.append((zid, nm, norm(c) if c else None, norm(re.sub(r"['‘’].*", "", nm)), norm(re.sub(r"\(.*?\)|（.*?）", "", nm))))
out = []
for p in sorted(glob.glob("batch_*/input/*.json") + glob.glob("pilot/input/*.json")):
    it = json.load(open(p, encoding="utf-8"))
    folder = p.replace("\\", "/").split("/input/")[0]
    k = it.get("id") or os.path.basename(p)[:-5]
    if (folder, k) in done and done[(folder, k)][1] == "cultivar":
        continue
    nm = it["植物名"]
    c = cv(nm)
    genus = norm(unicodedata.normalize("NFKC", nm).split()[0]) if nm.split() else ""
    cands = []
    if c:
        nc = norm(c)
        for zid, znm, zc, zhead, zall in Z:
            if not zc:
                continue
            r = difflib.SequenceMatcher(None, nc, zc).ratio()
            if r >= 0.8 or (len(nc) >= 4 and (nc in zc or zc in nc) and r >= 0.6):
                g = difflib.SequenceMatcher(None, genus, zhead[:len(genus) + 2]).ratio() if genus else 0
                cands.append((round(r, 2), round(g, 2), zid, znm))
    else:
        base = unicodedata.normalize("NFKC", nm)
        keys = [norm(re.sub(r"\(.*?\)", "", base))] + [norm(x) for x in re.findall(r"\((.*?)\)", base)]
        for zid, znm, zc, zhead, zall in Z:
            if zc:
                continue
            zkeys = [zall] + [norm(x) for x in re.findall(r"[\(（](.*?)[\)）]", unicodedata.normalize("NFKC", znm))]
            r = max(difflib.SequenceMatcher(None, a, b).ratio() for a in keys for b in zkeys if a and b) if keys and zkeys else 0
            if r >= 0.85:
                cands.append((round(r, 2), 1.0, zid, znm))
    cands.sort(reverse=True)
    if cands:
        out.append({"商品番号": it["商品番号"], "フォルダ": folder, "ID": k, "植物名": nm, "学名": it.get("学名"), "在庫": it.get("在庫あり"),
                    "今の当て": done.get((folder, k)), "候補": cands[:5]})
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("図鑑", len(names), "当て済み（品種のページ）", sum(1 for v in done.values() if v[1] == "cultivar"), "種のページ", sum(1 for v in done.values() if v[1] != "cultivar"), "候補のある品種", len(out))
