"""3属の試行: クラウドからも読める文献（stauden.de・MBG・NC State・YList）を、種と品種の単位で取得して生データを保存する。

使い方: python3 -I scripts/pilot/fetch_all.py pilot/input <保存先フォルダ（リポジトリの外）>
- 種のまとまり（input の species）ごとに1回: NC State の種／属のページ、YList、MBG の種のページ、stauden.de の種のページ
- 品種ごとに1回: MBG の品種ページ、stauden.de の品種ページ、NC State の品種ページ（あれば）
取得は curl（1.2秒おき）。ページ全体は保存先だけに置き、リポジトリには入れない。途中で止めても、取得済みは飛ばして再開できる。
"""
import glob
import html
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse

IN, OUT = sys.argv[1], sys.argv[2]
for d in ("mbg", "sdb", "ncsu", "yl"):
    os.makedirs(f"{OUT}/{d}", exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"


def get(url, binary=False):
    for _ in range(3):
        r = subprocess.run(["curl", "-sSL", "-m", "45", "-A", UA, "-w", "\n%{http_code}", url], capture_output=True)
        body = r.stdout.decode("utf-8", "replace")
        time.sleep(1.2)
        if r.returncode == 0 and "\n" in body:
            text, code = body.rsplit("\n", 1)
            return code.strip(), text
        time.sleep(3)
    return "ERR", ""


def norm(s):
    return re.sub(r"[^a-z]", "", s.lower())


def cached(path):
    return os.path.exists(path) and os.path.getsize(path) > 2


def save(path, obj):
    json.dump(obj, open(path, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)


# ---------- stauden.de ----------
def sdb_search(q):
    code, t = get("https://www.stauden.de/staudendatenbank/api.php?" + urllib.parse.urlencode({"action": "search", "q": q}))
    try:
        return [(i["relid"], i["bona_1"]) for i in json.loads(t).get("items", []) if i.get("type") == "plant"]
    except Exception:
        return []


def sdb(key, queries, want):
    """want(name) が真の最初の候補を選び、plant を保存する"""
    path = f"{OUT}/sdb/{key}.json"
    if cached(path):
        return
    res = {"tries": [], "pick": None}
    for q in dict.fromkeys(queries):
        items = sdb_search(q)
        res["tries"].append({"q": q, "names": items[:40]})
        hit = sorted((i for i in items if want(i[1])), key=lambda i: -int(want(i[1])))  # 品種名がぴったり一致する候補を先に
        if hit:
            res["pick"] = hit[0]
            code, t = get("https://www.stauden.de/staudendatenbank/api.php?" + urllib.parse.urlencode({"action": "plant", "relid": hit[0][0]}))
            try:
                res["plant"] = json.loads(t)
            except Exception:
                res["plant_error"] = code
            break
    save(path, res)


# ---------- MBG ----------
def mbg_search(q):
    code, t = get("https://plantfinder.mobot.org/PlantFinderProfileResults.aspx?basic=" + urllib.parse.quote(q))
    out = []
    for m in re.findall(r'href="/PlantFinderDetails\.aspx\?taxonid=(\d+)[^"]*"[^>]*>(.*?)</a>', t, re.S):
        nm = html.unescape(re.sub(r"<[^>]+>", "", m[1])).strip()
        if nm:
            out.append((m[0], nm))
    return list(dict.fromkeys(out))


def mbg(key, queries, want):
    path = f"{OUT}/mbg/{key}.json"
    if cached(path):
        return
    res = {"tries": [], "pick": None}
    for q in dict.fromkeys(queries):
        items = mbg_search(q)
        res["tries"].append({"q": q, "names": items[:20]})
        hit = sorted((i for i in items if want(i[1])), key=lambda i: -int(want(i[1])))  # 品種名がぴったり一致する候補を先に
        if hit:
            res["pick"] = hit[0]
            url = f"https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderDetails.aspx?taxonid={hit[0][0]}"
            code, t = get(url)
            res["url"] = url
            open(f"{OUT}/mbg/{key}.html", "w", encoding="utf-8").write(t)
            break
    save(path, res)


# ---------- NC State ----------
def ncsu(key, slugs):
    path = f"{OUT}/ncsu/{key}.json"
    if cached(path):
        return
    res = {"tries": [], "url": None}
    for s in dict.fromkeys(slugs):
        url = f"https://plants.ces.ncsu.edu/plants/{s}/"
        code, t = get(url)
        res["tries"].append({"slug": s, "code": code})
        if code == "200" and "Plant Toolbox" in t:
            res["url"] = url
            open(f"{OUT}/ncsu/{key}.html", "w", encoding="utf-8").write(t)
            break
    save(path, res)


# ---------- YList ----------
def ylist(key, q):
    path = f"{OUT}/yl/{key}.json"
    if cached(path):
        return
    u = "http://ylist.info/ylist_simple_search.php?" + urllib.parse.urlencode(
        {"any_field": q, "capital": "0", "family_order": "2", "family_disp_type": "1", "family_header": "0", "spec_order": "0",
         "list_type": "0", "search": "検索"})
    code, t = get(u)
    rows = []
    for m in re.finditer(r"<span class = 'list_all'>.*?pass=(\d+)'><span class = 'gakumei'>(.*?)</span>(.*?)</(?:span|a)>", t, re.S):
        rest = html.unescape(m.group(3)).replace("　", " ").split()
        rows.append({"pass": m.group(1), "sci": re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))).strip(),
                     "ja": rest[0] if rest else "", "status": rest[1] if len(rest) > 1 else ""})
    save(path, {"q": q, "url": u, "code": code, "rows": rows})


# 属が分けられて、文献によって別の属名で載っているもの（アスターの仲間）
GENUS_ALIAS = {"Aster": ["Aster", "Symphyotrichum", "Eurybia", "Doellingeria", "Galatella"],
               "Persicaria": ["Persicaria", "Bistorta", "Koenigia", "Aconogonon", "Polygonum"],
               "Sedum": ["Sedum", "Hylotelephium", "Phedimus"], "Hylotelephium": ["Hylotelephium", "Sedum"]}
SPECIES_ALIAS = {
 "Aster novae-angliae": ["Symphyotrichum novae-angliae"], "Aster novi-belgii": ["Symphyotrichum novi-belgii"],
 "Aster dumosus": ["Symphyotrichum dumosum"], "Aster cordifolius": ["Symphyotrichum cordifolium"],
 "Aster ericoides": ["Symphyotrichum ericoides"], "Aster divaricatus": ["Eurybia divaricata"],
 "Aster macrophyllus": ["Eurybia macrophylla"], "Aster umbellatus": ["Doellingeria umbellata"],
 "Aster frikartii": ["Aster x frikartii"],
 "Persicaria amplexicaulis": ["Bistorta amplexicaulis", "Polygonum amplexicaule"], "Persicaria affinis": ["Bistorta affinis", "Polygonum affine"],
 "Persicaria polymorpha": ["Koenigia x fennica", "Aconogonon speciosum", "Polygonum polymorphum"],
 "Persicaria virginiana": ["Persicaria filiformis", "Polygonum virginianum"],
 "Salvia superba": ["Salvia x superba"], "Salvia sylvestris": ["Salvia x sylvestris"],
 "Sedum spectabile": ["Hylotelephium spectabile"], "Hylotelephium spectabile": ["Sedum spectabile"], "Sedum telephium": ["Hylotelephium telephium"],
 "Sedum cauticola": ["Hylotelephium cauticola"], "Sedum erythrostictum": ["Hylotelephium erythrostictum"], "Sedum sieboldii": ["Hylotelephium sieboldii"],
 "Sedum ussuriense": ["Hylotelephium ussuriense"], "Sedum kamtschaticum": ["Phedimus kamtschaticus"], "Sedum spurium": ["Phedimus spurius"],
 "Astilbe arendsii": ["Astilbe x arendsii"],
}
# 品種名の別の書き方（ドイツ語の元の名前、つづりの違い）。マスターの品種名 → 文献での書き方
CV_ALIAS = {"May Night": ["Mainacht"], "Norah Leigh": ["Nora Leigh"], "Queen Blue": ["Blue Queen", "Blaukönigin"], "David Lavender": ["David's Lavender"],
            "Autumn Joy": ["Herbstfreude"], "Dragon's Blood": ["Schorbuser Blut"],}
GENERIC = {"album", "alba", "rose", "rosea", "nana", "variegated", "variegata", "albomarginata", "aurea", "rubra", "white",
           "mediovariegatum", "variegatum", "tricolor", "superba", "atropurpurea", "aureovariegata"}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower().replace("'", "")).strip("-")


def main():
    items = [json.load(open(f, encoding="utf-8")) for f in sorted(glob.glob(IN + "/*.json"))]
    species = sorted({it["species"] for it in items})
    for sp in species:
        key = "sp_" + slug(sp)
        g, e = sp.split()
        if e == "hybrid":
            ncsu(key, [g.lower()])
            continue
        names = [sp] + SPECIES_ALIAS.get(sp, [])
        ok = lambda n, names=names: norm(n) in [norm(x) for x in names]
        ncsu(key, [slug(x) for x in names] + [g.lower()])
        ylist(key, sp)
        mbg(key, names, ok)
        sdb(key, names, ok)
        print("species", sp, flush=True)
    for it in items:
        cv = it["品種名"]
        if not cv or not re.search(r"[A-Za-z]", cv):
            continue
        g = it["属"]
        sp = it["species"] if not it["species"].endswith("hybrid") else g
        ep = None if it["species"].endswith("hybrid") else it["species"].split()[1]

        def want(n, cv=cv, g=g, ep=ep, it=it):
            # 品種名が一致すること。引用符の中の名前か、大文字の流通名（'Rotfuchs' RED FOX など）で照合する。
            # 'Album'・'Nana' のようなありふれた品種名は、種小名も一致するときだけ採る（同名の別種を避ける）。
            n = n.replace("’", "'").replace("‘", "'")
            if not any(norm(a) in norm(n) for a in GENUS_ALIAS.get(g, [g])):
                return False
            m = re.search(r"'(.+)'", n)
            quoted = norm(m.group(1)) if m else ""
            trade = norm(" ".join(re.findall(r"[A-Z]{2,}", re.sub(r"'.*'", "", n))))
            generic = norm(cv) in GENERIC
            cvs = [norm(cv)] + [norm(a) for a in CV_ALIAS.get(cv, [])]
            exact = quoted in cvs or trade in cvs
            ok = exact or (not generic and quoted.startswith(norm(cv)))
            if not ok:
                return False
            words = [w for w in re.sub(r"'.*$", "", n).split()[1:] if re.fullmatch(r"[a-z-]+", w) and w not in ("x", "ssp", "subsp", "var")]
            eps = [ep] + [x.split()[-1] for x in SPECIES_ALIAS.get(it["species"], [])] if ep else []
            if generic and ep and not any(e in words for e in eps):
                return False
            # 品種名の前半だけが合っている候補（'Madeline' と 'Madeline Hill' など）は、種小名も一致するときだけ採る
            if not exact and ep and words and not any(e in words for e in eps):
                return False
            return 2 if exact else 1

        al = CV_ALIAS.get(cv, [])
        mbg(it["id"], [cv, f"{g} {cv}"] + al, want)  # MBG の検索は品種名だけの方が当たる
        sdb(it["id"], [f"{sp} {cv}", f"{g} {cv}", cv] + al, want)
        ncsu(it["id"], [slug(f"{sp} {cv}"), slug(f"{g} {cv}")])
        print(it["id"], it["学名"], flush=True)
    print("done")


main()
