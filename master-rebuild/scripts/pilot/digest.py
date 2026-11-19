"""3属の試行: fetch_all.py が保存した生データから、判定に使う項目だけを取り出して1つの JSON にまとめる。

使い方: python3 -I scripts/pilot/digest.py <生データのフォルダ> <出力 digest.json（リポジトリの外）>
キーは種のまとまり（sp_...）または試行ID。値は文献ごとの項目（原文のまま。訳さない）。
- sdb（stauden.de）: 項目名 → [(値, 階層 cultivar/species/genus)]
- mbg: 見出しの項目（Zone, Sun, Water, Tolerate など）と本文（Culture, Noteworthy, Problems, Uses）
- ncsu: 定型の項目（dt → dd）と説明文
"""
import glob
import html
import json
import os
import re
import sys

RAW, OUT = sys.argv[1], sys.argv[2]


def clean(s):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))).strip()


def sdb(path):
    j = json.load(open(path, encoding="utf-8"))
    p = j.get("plant")
    if not p or "master" not in p:
        return None
    m = p["master"]
    out = {"name": max((m.get(k) or "" for k in ("bona_lang", "bona_1", "bona_3")), key=len), "relid": m["relid"],
           "url": f"https://www.stauden.de/staudendatenbank.html?relid={m['relid']}", "f": {}}
    for k in p.get("kriterien", []):
        for o in k["obergruppen"]:
            if o["werte"]:
                out["f"][o["name"]] = [(w["wert"], w["ebene"]) for w in o["werte"]]
    return out


def mbg(path):
    j = json.load(open(path, encoding="utf-8"))
    hp = path[:-5] + ".html"
    if not j.get("pick") or not os.path.exists(hp):
        return None
    t = open(hp, encoding="utf-8", errors="replace").read()
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    f = {}
    for m in re.finditer(r'id="ctl00_MainContentPlaceHolder_(\w+?)Row"[^>]*>(.*?)(?=<div id="ctl00_MainContentPlaceHolder_\w+Row"|<div class="clear-float">|$)', t, re.S):
        v = clean(m.group(2))
        if v:
            f[m.group(1)] = v
    return {"name": j["pick"][1], "url": j["url"], "f": f}


def ncsu(path):
    j = json.load(open(path, encoding="utf-8"))
    hp = path[:-5] + ".html"
    if not j.get("url") or not os.path.exists(hp):
        return None
    t = open(hp, encoding="utf-8", errors="replace").read()
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    title = clean(re.search(r"<title>(.*?)</title>", t, re.S).group(1)).split("|")[0].strip()
    f = {}
    for m in re.finditer(r"<dt[^>]*>(.*?)</dt>\s*((?:<dd[^>]*>.*?</dd>\s*)+)", t, re.S):
        k = clean(m.group(1)).rstrip(":")
        v = "; ".join(clean(x) for x in re.findall(r"<dd[^>]*>(.*?)</dd>", m.group(2), re.S))
        if k and v and len(v) < 9000:
            f[k] = v
    return {"name": title, "url": j["url"], "f": f}


def main():
    D = {}
    for src, fn in (("sdb", sdb), ("mbg", mbg), ("ncsu", ncsu)):
        for p in sorted(glob.glob(f"{RAW}/{src}/*.json")):
            key = os.path.basename(p)[:-5]
            r = fn(p)
            if r:
                D.setdefault(key, {})[src] = r
    for p in sorted(glob.glob(f"{RAW}/yl/*.json")):
        j = json.load(open(p, encoding="utf-8"))
        if j.get("rows"):
            D.setdefault(os.path.basename(p)[:-5], {})["yl"] = {"url": j["url"], "rows": j["rows"][:6]}
    json.dump(D, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    n = {s: sum(1 for v in D.values() if s in v) for s in ("sdb", "mbg", "ncsu", "yl")}
    print(len(D), n)


main()
