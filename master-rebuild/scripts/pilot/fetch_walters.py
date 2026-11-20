"""Walters（perennials.com）の品種ページを、品種名から URL を作って取得する。

使い方: python3 -I scripts/pilot/fetch_walters.py <input フォルダ> <保存先フォルダ（リポジトリの外）>
URL は https://www.perennials.com/plants/<属>-<種小名>-<品種名>.html または <属>-<品種名>.html の形。
アスターの仲間は、新しい属名（symphyotrichum など）でも試す。取得済みは飛ばす。
"""
import glob
import json
import os
import re
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
IN, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT + "/walters", exist_ok=True)
ALT = {"Aster novae-angliae": "symphyotrichum-novae-angliae", "Aster novi-belgii": "symphyotrichum-novi-belgii", "Aster dumosus": "symphyotrichum-dumosum",
       "Aster cordifolius": "symphyotrichum-cordifolium", "Aster ericoides": "symphyotrichum-ericoides", "Aster divaricatus": "eurybia-divaricata",
       "Aster macrophyllus": "eurybia-macrophylla", "Aster umbellatus": "doellingeria-umbellata",
       "Ageratina altissima": "eupatorium-rugosum", "Polygonum bistorta": "persicaria-bistorta", "Tovara virginiana": "persicaria-virginiana",
       "Thermopsis caroliniana": "thermopsis-villosa", "Limonium latifolium": "limonium-platyphyllum", "Ranunculus ficaria": "ficaria-verna"}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower().replace("'", "")).strip("-")


hits = []
for f in sorted(glob.glob(IN + "/*.json")):
    it = json.load(open(f, encoding="utf-8"))
    k = it["id"]
    out = f"{OUT}/walters/{k}.html"
    if os.path.exists(out) or os.path.exists(out + ".none"):
        if os.path.exists(out):
            hits.append(k)
        continue
    g = it["属"].lower()
    cv = it["品種名"] if it["品種名"] and re.search("[A-Za-z]", it["品種名"]) else None
    sp = None if it["species"].endswith("hybrid") else it["species"].split()[1]
    bases = [f"{g}-{sp}" if sp else g]
    if it["species"] in ALT:
        bases.append(ALT[it["species"]])
    if sp:
        bases.append(g)
    cands = [f"{b}-{slug(cv)}" for b in bases] if cv else bases[:2 if it["species"] in ALT else 1]
    ok = False
    for c in dict.fromkeys(cands):
        u = f"https://www.perennials.com/plants/{c}.html"
        r = subprocess.run(["curl", "-sSL", "-m", "40", "-A", "Mozilla/5.0", "-w", "\n%{http_code}", u], capture_output=True)
        time.sleep(1.0)
        body = r.stdout.decode("utf-8", "replace")
        t, code = body.rsplit("\n", 1) if "\n" in body else ("", "ERR")
        if code.strip() == "200" and "USDA Zone" in t and "Search Not Found" not in t:
            open(out, "w", encoding="utf-8").write(u + "\n" + t)
            ok = True
            hits.append(k)
            break
    if not ok:
        open(out + ".none", "w").write("")
print(len(hits), hits)
