"""3属の試行（ホスタ・ゲラニウム・ベロニカ）の入力ファイルを、元のマスターから作る。

使い方: python3 scripts/pilot/make_input.py <元のマスター.xlsx> pilot/input
価格・在庫数は写さない（在庫の有無だけ）。ID は属の頭文字＋連番（H01…、G01…、V01…）。
species は「種のページを1回読む」単位（交配種・種小名なしは "<属> hybrid"）。
"""
import json
import os
import re
import sys

import openpyxl

src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
ws = openpyxl.load_workbook(src, read_only=True)["Sheet1"]
rows = list(ws.iter_rows(values_only=True))
H = list(rows[0])
GENERA = {"Hosta": "H", "Geranium": "G", "Veronica": "V"}


def clean(s):
    s = str(s).replace("\n", " ").replace("　", " ")
    s = re.sub(r"[‘’‛`]", "'", s)
    return re.sub(r"\s+", " ", s).strip()


items = []
for r in rows[1:]:
    d = dict(zip(H, r))
    if not d.get("商品番号") or not d.get("学名"):
        continue
    sci = clean(d["学名"])
    sci = re.sub(r"^(\w+)'", r"\1 '", sci)  # Hosta'Gold Standard'
    g = sci.split()[0]
    if g not in GENERA:
        continue
    cv = re.search(r"'(.+)'", sci)  # 品種名の中のアポストロフィ（Cat's Eyes など）を切らない
    head = re.sub(r"'.*$", "", sci)
    head = re.sub(r"\(.*?\)", "", head).replace("×", " x ").split()
    words = [w for w in head[1:] if w != "x"]
    hybrid = "x" in head[1:] or not words
    species = f"{g} {words[0]}" if words and re.fullmatch(r"[a-z\-]+", words[0]) else f"{g} hybrid"
    items.append({"商品番号": d["商品番号"], "植物名": clean(d["植物名"]), "学名": sci, "属": g, "species": species,
                  "交配種": hybrid, "品種名": cv.group(1) if cv else None, "別名": clean(d["別名"]) if d.get("別名") else None,
                  "在庫あり": isinstance(d.get("在庫数"), (int, float)) and d["在庫数"] > 0,
                  "花時期": d.get("花時期"), "高さ(cm)": d.get("高さ(cm)"), "耐寒性": d.get("耐寒性")})
items.sort(key=lambda x: (x["属"], x["species"], x["学名"]))
n = {}
for it in items:
    k = GENERA[it["属"]]
    n[k] = n.get(k, 0) + 1
    it["id"] = f"{k}{n[k]:02d}"
    json.dump(it, open(f"{out}/{it['id']}.json", "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
sp = sorted({it["species"] for it in items})
print(len(items), n, "種のまとまり", len(sp))
for s in sp:
    print(" ", s, [it["id"] for it in items if it["species"] == s])
