"""Jelitto(s11)・Gaißmayer(s17) の記述（chrome_curated.py）を trial/evidence/Pxx.json に追記する。

使い方: python3 -I scripts/sources/merge_chrome.py <trial フォルダ>
この2つの文献はクラウドから読めないので、ユーザーのパソコンの Chrome で読んで chrome_curated.py に書き写してある。
何度実行しても同じ結果になる（s11・s17 の記録を入れ直す）。merge.py（s02・s04・s18）とは別に実行できる。
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chrome_curated as C  # noqa: E402

TRIAL = sys.argv[1]
SOURCES = {"s11", "s17"}
MARK = "\n\n【2026-11-19 追記：Jelitto・Gaißmayer（Chrome で確認）】"

MON = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
       "September": 9, "October": 10, "November": 11, "December": 12}
BODEN = {"frisch": "frischer Boden", "trocken": "trockener Boden", "feucht": "feuchter Boden", "nass (Sumpf)": "nasser Boden (Sumpf)"}
ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12}


def terms(value, table, sep):
    return "、".join(table[t.strip()] for t in value.split(sep))


def rec(field, ja, quote, src, page):
    return {"field": field, "value_ja": ja, "quote": quote, "source": src, "url": page["url"], "level": page["level"],
            "from_master_source": False, "checked": C.CHECKED}


def jelitto(page):
    out = []

    def add(field, key, ja):
        out.append(rec(field, ja, f"{key}: {page[key]}", "s11", page))

    out.append(rec("accepted_name", f"Jelitto での学名表記：{page['name']}", page["name"], "s11", page))
    if "Family" in page:
        add("family", "Family", page["Family"])
    if "Origin" in page:
        add("native_range", "Origin", C.J_TERMS[page["Origin"]])
    if "Flower Colour" in page:
        add("flower_color", "Flower Colour", C.J_TERMS[page["Flower Colour"]])
    a, b = page["Natural Flowering Period"].split(" - ")
    add("bloom_time", "Natural Flowering Period", f"{MON[a]}月〜{MON[b]}月")
    z = re.fullmatch(r"Z(\d+) - Z(\d+)", page["Winter Hardiness Zones"])
    add("usda_zone", "Winter Hardiness Zones", f"ゾーン{z[1]}〜{z[2]}")
    if "Foliage" in page:
        add("foliage", "Foliage", C.J_TERMS[page["Foliage"]])
    if "Growth Habit" in page:
        parts = [t.strip() for t in page["Growth Habit"].split("/")]
        add("habit", "Growth Habit", "、".join(C.J_TERMS[t] for t in parts))
        if "stoloniferous" in parts:
            add("spread_mode", "Growth Habit", C.J_TERMS["stoloniferous"])
        if "clumping" in parts:
            add("spread_mode", "Growth Habit", C.J_TERMS["clumping"])
        if "evergreen" in parts:
            add("evergreen", "Growth Habit", "常緑")
    add("height", "Height with Flowers", "花を含む高さ " + page["Height with Flowers"].replace(" ", ""))
    soil = [t.strip() for t in page["Soil Requirements"].split("/")]
    moist = [t for t in soil if t in ("well-drained", "moist", "dry", "average")]
    other = [t for t in soil if t not in moist]
    add("soil_moisture", "Soil Requirements", "、".join(C.J_TERMS[t] for t in moist))
    if other:
        add("soil_type_ph", "Soil Requirements", "、".join(C.J_TERMS[t] for t in other))
    add("sun", "Location", terms(page["Location"], C.J_TERMS, ","))
    if "suitable for cutting" in page.get("Usage", ""):
        add("cut_flower", "Usage", "切り花に向く")
    return out


def gaiss(page):
    out = []

    def add(field, key, ja, quote=None):
        out.append(rec(field, ja, quote or f"{key}: {page[key]}", "s17", page))

    if page["name"].startswith(("Hosta Hybride", "Hemerocallis Hybride", "Calamagrostis x")):
        out.append(rec("accepted_name", f"Gaißmayer での学名表記：{page['name']}", page["name"], "s17", page))
    add("family", "Familie", page["Familie"])
    add("flower_color", "Blütenfarbe", C.G_TERMS[page["Blütenfarbe"]])
    if "Blattfarbe" in page:
        add("foliage", "Blattfarbe", "葉色：" + C.G_TERMS[page["Blattfarbe"]])
    m = re.fullmatch(r"([IVX]+)(–|\s\+\s)([IVX]+)(\s\(mittel–spät\))?", page["Blütezeit"])
    ja = f"{ROMAN[m[1]]}月{'〜' if m[2] == '–' else 'と'}{ROMAN[m[3]]}月" + ("（中〜遅咲き）" if m[4] else "")
    add("bloom_time", "Blütezeit", ja)
    add("height", "Höhe", "高さ " + page["Höhe"].replace(" ", "").replace("–", "〜"))
    add("sun", "Lichtverhältnisse", terms(page["Lichtverhältnisse"], C.G_TERMS, ","))
    add("soil_moisture", "Lebensbereich", "、".join(C.G_TERMS[t] for t in page["Boden"]),
        f"Lebensbereich: {page['Lebensbereich']}（{' / '.join(BODEN[t] for t in page['Boden'])}）")
    z = re.fullmatch(r"Z(\d) \((-[\d,]+) °C bis (-[\d,]+) °C\)", page["Winterhärtezone"])
    add("hardiness_zone_de", "Winterhärtezone", f"ゾーン{z[1]}（{z[2].replace(',', '.')}〜{z[3].replace(',', '.')}℃）")
    if "Wintergrün" in page:
        add("evergreen", "Wintergrün", "冬緑（冬も葉が残る）")
    if "Steril" in page:
        add("spread_mode", "Steril", "不稔（種ができない）")
    if "Schneckenfraß" in page:
        add("pests_diseases", "Schneckenfraß", "ナメクジの食害：" + C.G_TERMS[page["Schneckenfraß"]])
    if "Giftklasse" in page:
        add("toxicity", "Giftklasse", C.G_TERMS[page["Giftklasse"]])
    if "Duftend" in page:
        add("fragrance", "Duftend", "香りあり")
    if "Schnittgeeignet" in page:
        add("cut_flower", "Schnittgeeignet", "切り花に向く")
    if "Züchter" in page:
        add("group", "Züchter", "育種者：" + page["Züchter"])
    return out


def main():
    used = set()
    for f in sorted(glob.glob(f"{TRIAL}/evidence/P*.json")):
        pid = os.path.basename(f)[:3]
        d = json.load(open(f, encoding="utf-8"))
        d["evidence"] = [e for e in d["evidence"] if e["source"] not in SOURCES]
        d["access_log"] = [a for a in d["access_log"] if a["source"] not in SOURCES]
        for src, pages, build, search, label in (("s11", C.JELITTO, jelitto, C.J_SEARCH, "Jelitto"),
                                                 ("s17", C.GAISS, gaiss, C.G_SEARCH, "Gaißmayer")):
            page = pages.get(pid)
            if page:
                kind = "品種ページ" if page["level"] == "cultivar" else "種のページ"
                d["access_log"].append({"source": src, "url": page["url"], "status": "ok", "checked": C.CHECKED,
                                        "note": f"{kind}：{page['name']}。ユーザーのパソコンの Chrome で読んだ"})
                d["evidence"] += build(page)
                for i, (tp, ts, field, quote, ja) in enumerate(C.TEXT):
                    if (tp, ts) == (pid, src):
                        d["evidence"].append(rec(field, ja, quote, src, page))
                        used.add(i)
            else:
                d["access_log"].append({"source": src, "url": search, "status": "not_found", "checked": C.CHECKED,
                                        "note": C.NOT_FOUND[src][pid] + f"。ユーザーのパソコンの Chrome で {label} のサイト内検索を使った"})
        found = {e["field"] for e in d["evidence"]}
        d["not_found"] = [x for x in d.get("not_found", []) if x not in found]
        base = d.get("notes", "").split(MARK)[0]
        d["notes"] = base + (MARK + C.NOTES[pid] if pid in C.NOTES else "")
        json.dump(d, open(f, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
        n = {s: sum(1 for e in d["evidence"] if e["source"] == s) for s in ("s11", "s17")}
        print(pid, n, "残りの not_found:", len(d["not_found"]))
    left = [C.TEXT[i][:3] for i in range(len(C.TEXT)) if i not in used]
    if left:
        raise SystemExit(f"ページのない品種に記述がある: {left}")


main()
