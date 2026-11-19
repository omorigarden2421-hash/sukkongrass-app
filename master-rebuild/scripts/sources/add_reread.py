"""2026-11-19 の読み直し（暑さの記述がなかった品種の、種・属のページ）で見つけた記述を trial/evidence/ に追記する。

使い方: python3 -I scripts/sources/add_reread.py <trial フォルダ>
何度実行しても同じ結果になる（"added": "reread-20261119" の印を付けた記録を入れ直す）。
MBG（s02）の1件は mbg_curated.py にも入れてあるので、merge.py を実行し直しても残る。
"""
import json
import sys

TRIAL = sys.argv[1]
TAG = "reread-20261119"
CHECKED = "2026-11-19"
NC_AGA = "https://plants.ces.ncsu.edu/plants/agastache/"
NC_ART = "https://plants.ces.ncsu.edu/plants/artemisia/"
MBG_P17 = "https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderDetails.aspx?taxonid=285553"
# (試作ID, field, 日本語訳, 原文, 文献, URL, level)
REC = [
 ("P06", "heat_humidity", "アガスタチ属は暑さと乾燥に耐える", "They are also heat and drought tolerant.", "s06", NC_AGA, "genus"),
 ("P06", "drought", "アガスタチ属は暑さと乾燥に耐える", "They are also heat and drought tolerant.", "s06", NC_AGA, "genus"),
 ("P06", "heat_humidity", "米国南東部の夏に最もよく耐える種類（'Blue Fortune'、'Blue Boa'、Acapulco 群など）を選ぶ",
  "Choose a species that tolerates southeast summers best such as 'Blue Fortune', 'Blue Boa' or the Acapulco® group.", "s06", NC_AGA, "genus"),
 ("P06", "soil_moisture", "水はけの良い土が必須。排水の悪い土で冬に根が濡れると枯れる",
  "Well-drained soils are essential for these plants and wet winter feet in poorly drained soil will do them in.", "s06", NC_AGA, "genus"),
 ("P01", "heat_humidity", "アルテミシア属は、湿った土、冬の過湿、湿度の高い気候に耐えない。湿った条件では腐りやすい",
  "They will not tolerate wet soils, wet winter conditions, or climates with high humidity. Plants are prone to rot in moist conditions.",
  "s06", NC_ART, "genus"),
 ("P17", "heat_humidity", "セントルイス（夏が高温多湿）では午後に少し日陰になる所を好む",
  "Plants prefer some part afternoon shade in the St. Louis area", "s02", MBG_P17, "species"),
]
LOG = [
 ("P06", "s06", NC_AGA, "ok", "属 Agastache のページ（A. mexicana の種のページは 404）。暑さの記述を探すための読み直し"),
 ("P01", "s06", NC_ART, "ok", "属 Artemisia のページ。暑さの記述を探すための読み直し"),
 ("P03", "s02", "https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderDetails.aspx?taxonid=243536", "ok",
  "読み直し。暑さだけの記述はなし（湿気と株腐れの記述のみ）"),
 ("P15", "s06", "https://plants.ces.ncsu.edu/plants/sedum/", "ok", "属 Sedum のページと Phedimus spurius の種のページを読み直し。暑さの記述なし"),
 ("P23", "s06", "https://plants.ces.ncsu.edu/plants/anemone/", "ok", "属 Anemone のページ。属全体の一般的な説明だけで、この種の暑さの記述なし"),
]


def main():
    for n in range(1, 29):
        pid = f"P{n:02d}"
        path = f"{TRIAL}/evidence/{pid}.json"
        d = json.load(open(path, encoding="utf-8"))
        d["evidence"] = [e for e in d["evidence"] if e.get("added") != TAG]
        d["access_log"] = [a for a in d["access_log"] if a.get("added") != TAG]
        for p, field, ja, quote, src, url, level in REC:
            if p != pid:
                continue
            if any(e["source"] == src and e["field"] == field and e["quote"] == quote for e in d["evidence"]):
                continue  # merge.py がすでに入れている
            d["evidence"].append({"field": field, "value_ja": ja, "quote": quote, "source": src, "url": url, "level": level,
                                  "from_master_source": False, "checked": CHECKED, "added": TAG})
        for p, src, url, status, note in LOG:
            if p == pid:
                d["access_log"].append({"source": src, "url": url, "status": status, "checked": CHECKED, "note": note, "added": TAG})
        found = {e["field"] for e in d["evidence"]}
        d["not_found"] = [x for x in d.get("not_found", []) if x not in found]
        json.dump(d, open(path, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    print("追記", len(REC), "件")


main()
