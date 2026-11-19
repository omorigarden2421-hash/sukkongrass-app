"""MBG(s02)・YList(s04)・stauden.de 無料データベース(s18) の取得結果を trial/evidence/Pxx.json に追記する。

使い方: python3 -I scripts/sources/merge.py <取得結果のフォルダ> <trial フォルダ>
取得結果のフォルダには fetch_*.py が作る mbg/ yl/ sdb/ がある。
追記した記録には checked（確認日）を付ける。何度実行しても同じ結果になる（s02・s04・s18 の記録を入れ直す）。
Jelitto(s11)・Gaißmayer(s17) は merge_chrome.py が追記する（merge.py の後に実行する）。
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mbg_curated import CURATED  # noqa: E402

RAW, TRIAL = sys.argv[1], sys.argv[2]
CHECKED = "2026-11-19"
NEW_SOURCES = {"s02", "s04", "s18"}

# ---------- stauden.de の用語 → 日本語 ----------
MON = {"Januar": "1月", "Februar": "2月", "März": "3月", "April": "4月", "Mai": "5月", "Juni": "6月", "Juli": "7月",
       "August": "8月", "September": "9月", "Oktober": "10月", "November": "11月", "Dezember": "12月"}
G = {
 # Wuchsform
 "aufrechte Stängel mit grundständigem Blattschopf": "株元に葉が茂り、茎が直立する",
 "aufrechte, beblätterte Stängel ohne grundständigen Blattschopf": "葉の付いた茎が直立する（株元の葉の茂みはない）",
 "teppichartig, mattenartig": "じゅうたん状・マット状",
 "buschig, dichtbuschig bis lockerbuschig": "こんもり茂る（密〜やや粗）",
 "polsterartig bis polsterbildend": "クッション状（ポルスター）",
 "bogig": "弓なり", "ausladend bis breitausladend": "横に張り出す〜広く張り出す",
 "kissenartig bis kissenbildend": "クッション状", "geneigt": "傾く", "halbkugelig": "半球形",
 "aufrecht bis straff aufrecht": "直立〜まっすぐ直立",
 # Wuchsverhalten
 "horstig, lockerhorstig, horstbildend": "株立ち（株でまとまり、広がらない）",
 "kriechend, teils wurzelnd": "這い、一部は根を下ろす", "rhizombildend": "地下茎を作る",
 "ausläufertreibend": "ランナー（ほふく枝）を出す",
 # Blattphase
 "sommergrün": "夏緑（冬は葉が枯れる）", "wintergrün": "冬緑（冬も葉が残り、春に入れ替わる）", "immergrün": "常緑",
 # Licht
 "sonnig": "日なた", "absonnig": "明るい日陰（直射は当たらないが明るい）", "halbschattig": "半日陰", "schattig": "日陰",
 # Lage
 "anpassungsfähig": "適応力がある", "wärmeliebend": "暖かい場所を好む", "schutzbedürftig": "保護が必要",
 "kühleliebend": "涼しい場所を好む",
 # Bodenfeuchte
 "frisch": "適湿（frisch）", "trocken": "乾燥", "feucht": "湿り気", "nass": "湿地",
 # Sichtung
 "** (sehr gut)": "★★（とても良い）", "* (gut)": "★（良い）", "*** (ausgezeichnet)": "★★★（優秀）",
 "bisher ohne Bewertung": "まだ評価なし", "Li (Liebhabersorte)": "Li（愛好家向け品種）",
 "Ø (entbehrliche Sorte)": "Ø（なくてもよい品種）",
 # Eigenschaften
 "Blattschmuck": "葉が観賞対象", "Blatt- oder Blütenduft": "葉または花に香り", "Fruchtschmuck": "実・種の姿が観賞対象",
 "ganz oder in Teilen giftig": "全体または一部に毒",
 # Verwendung
 "Insektennährpflanze": "昆虫の蜜源・食草", "für Schnittzwecke, Floristik": "切り花・フラワーアレンジ向き",
 "Heil- und Medizinpflanzen": "薬用植物", "sonnige Beete an Gebäuden": "建物沿いの日なたの花壇",
 "absonnige Beete an Gebäuden": "建物沿いの明るい日陰の花壇", "für Grabstätten geeignet": "墓地の植栽向き",
 "extensive Dachbegrünung": "粗放型の屋上緑化",
 # MS
 "ja": "あり", "nein": "なし", "horstig": "株立ち", "versamend": "こぼれ種で増える", "nicht versamend": "こぼれ種で増えない",
 "mäßig versamend": "こぼれ種でほどほどに増える", "stark versamend": "こぼれ種でよく増える",
 # Blattschmuck
 "mehrfarbig": "多色", "ganzjährig wirkungsvoll": "一年中観賞できる", "zweifarbig": "二色", "herbstfärbend": "紅葉する",
 # Vermehrung
 "Teilung im Frühling": "春に株分け", "Stecklinge im Frühling": "春に挿し木", "Risslinge im Frühling": "春にかき取り挿し（Risslinge）",
 "Grundständige Stecklinge im Frühling bis Sommer": "春〜夏に株元の芽で挿し木", "Teilung im Winter bis Frühling": "冬〜春に株分け",
 "Teilung nach der Blüte": "花後に株分け", "Stecklinge im Frühling bis Sommer": "春〜夏に挿し木",
 "Nebenrosetten im Frühling bis Sommer": "春〜夏に子株（脇のロゼット）で", "Kopfstecklinge im Frühling bis Sommer": "春〜夏に天挿し",
 "Wurzelschnittlinge im Winter bis Frühling": "冬〜春に根伏せ",
 "Normalkeimer, die Samen keimen meist leicht und kurzzeitig": "ふつうに発芽する（種は容易に短期間で発芽）",
 "Aussaat im Frühling": "春まき", "Aussaat im Winter bis Vorfrühling": "冬〜早春まき",
 "Kaltkeimer, eine Wärme- und Kühlephase ist nötig": "低温発芽型（暖かい期間と寒い期間が必要）",
 "Aussaat sofort nach der Samenreife": "種が熟したらすぐまく（取りまき）", "Aussaat ist wärmebedürftig": "発芽に暖かさが必要",
 # Heimat
 "Europa": "ヨーロッパ", "Kaukasus": "コーカサス", "Japan": "日本", "Sachalin": "サハリン", "Naher Osten": "中近東",
 "Nordamerika mit USA und Kanada": "北米（米国・カナダ）", "Kurilen": "千島列島", "Zentral-USA": "米国中部",
 "N-Mexiko": "メキシコ北部", "N-Afrika": "北アフリカ", "Mittelamerika": "中米", "Mexiko": "メキシコ", "W-Alpen": "西アルプス",
 "Zentral-Alpen": "中央アルプス", "USA": "米国", "Iran": "イラン", "N-Deutschland": "ドイツ北部", "Zirkumpolar": "周極地域",
 "Armenien": "アルメニア", "Kurdistan": "クルディスタン", "N-Iran": "イラン北部", "China": "中国", "Korea": "朝鮮半島",
 "Mandschurei": "中国東北部（満州）", "O-Sibirien": "東シベリア",
 "Mitteleuropa: Deutschland, Schweiz, Österreich": "中欧（ドイツ・スイス・オーストリア）", "O-Europa": "東欧", "S-Europa": "南欧",
 "östliches Nordamerika": "北米東部", "Sibirien": "シベリア",
 # Funktionstyp / Wuchsstärke
 "Bodendecker": "グラウンドカバー", "Begleiter": "脇役（Begleiter）", "Gerüstbildner": "骨格になる植物（Gerüstbildner）",
 "stark": "強い", "schwach": "弱い",
}
# Pflegehinweis: (原文の先頭, field, 日本語)
CARE = [
 ("An optimalen Standorten kaum Pflege nötig", "care", "合った場所ならほとんど手入れ不要"),
 ("Rückschnitt der Stängel im Herbst bis Spätherbst", "pruning", "秋〜晩秋に茎を切り戻す"),
 ("Kein Rückschnitt im Herbst", "pruning", "秋は切り戻さない（冬の姿・葉・種の穂を残す、または株を守るため）"),
 ("Rückschnitt abgeblühter Stängel bis zum grundständigen Blattschopf", "pruning", "咲き終わった茎を株元の葉の上まで切り戻す"),
 ("Aufkeimende Selbstaussaat beachten und kontrollieren", "spread_mode", "こぼれ種の芽生えに注意し、管理する"),
 ("Rückschnitt nach der ersten Blühphase bewirkt meist eine Nachblüte", "pruning", "一番花の後に切り戻すと、たいてい二番花が咲く"),
 ("Winterschutz /Sonnenschutz bei Kahlfrost ratsam", "winter_care", "雪のない凍結時は防寒・日よけをすると良い"),
 ("Schutz vor Winternässe und Staunässe", "winter_care", "冬の過湿と滞水から守る"),
 ("Rückschnitt vor der Samenreife um Selbstaussaat zu vermeiden", "spread_mode", "こぼれ種を避けるため、種が熟す前に切り戻す"),
 ("Ausbreitung durch Ausläufer, Rhizome oder wurzelnde Triebe", "spread_mode", "ランナー・地下茎・根を下ろす茎で広がるので、必要に応じて範囲を抑える"),
 ("Langlebig, möglichst viele Jahre nicht umpflanzen", "lifespan", "長寿。できるだけ長年植え替えない"),
 ("Rückschnitt abgeblühter Blütenstände bis zu den oberen Stängelblättern", "pruning", "咲き終わった花穂を、茎の上の方の葉の上まで切る"),
 ("Einige Samenstände, teils kurzlebiger Pflanzen", "lifespan", "（短命なこともあるので）種の穂をいくつか残してこぼれ種で維持する"),
 ("Totaler oder teilweiser Rückschnitt im Frühjahr", "pruning", "春に全体または一部を切り戻す"),
 ("Einzelne, abgeblühte Blüten", "pruning", "咲き終わった花を一つずつ切るか摘み取る"),
]
ZONE = re.compile(r"^Z(\d+) \((.+?) °C\)$")


def tr(v):
    if v in G:
        return G[v]
    m = ZONE.match(v)
    if m:
        return f"ゾーン{m.group(1)}（{m.group(2).replace(' bis ', '〜')}℃）"
    return MON.get(v, v)


def level_of(werte):
    lv = {w["ebene"] for w in werte}
    for k in ("genus", "species", "cultivar"):  # 一番広い階層を採る（控えめに）
        if k in lv:
            return k
    return "cultivar"


# stauden.de の項目 → evidence の field
SDB_MAP = {
 "Wuchsform": "habit", "Wuchsverhalten": "spread_mode", "Blattphase": "evergreen", "Lichtansprüche": "sun",
 "Lage, Exposition": "exposure", "Winterhärtezone": "hardiness_zone_de", "Bodenfeuchte": "soil_moisture",
 "Heimatregionen, Verbreitung": "native_range", "Vermehrung vegetativ": "propagation", "Vermehrung generativ": "propagation",
 "MS-Vegetativer Ausbreitungsdrang": "spread_mode", "MS-Generativer Ausbreitungsdrang": "spread_mode",
 "MS-Herbstfärbung": "seasonal_foliage", "MS-Wintersteher/-aspekt": "seasonal_foliage", "Blattschmuck": "seasonal_foliage",
 "Funktionstyp": "function_type", "Wuchsstärke": "vigor",
}
LABEL_JA = {"MS-Vegetativer Ausbreitungsdrang": "株の広がり方", "MS-Generativer Ausbreitungsdrang": "こぼれ種",
            "MS-Herbstfärbung": "紅葉", "MS-Wintersteher/-aspekt": "冬も立ち姿が残る", "Blattschmuck": "葉の観賞性",
            "Vermehrung vegetativ": "栄養繁殖", "Vermehrung generativ": "種まき"}


def sdb_entries(pid):
    fs = glob.glob(f"{RAW}/sdb/{pid}_plant_*.json")
    if not fs:
        return None, []
    d = json.load(open(fs[0], encoding="utf-8"))
    relid = d["master"]["relid"]
    url = f"https://www.stauden.de/staudendatenbank.html?relid={relid}"
    name = max((d["master"].get(k) or "" for k in ("bona_lang", "bona_1", "bona_3")), key=len)
    og = {}
    for k in d["kriterien"]:
        for o in k["obergruppen"]:
            if o["werte"]:
                og[o["name"]] = o["werte"]
    ev = []

    def add(field, quote, ja, level):
        ev.append({"field": field, "value_ja": ja, "quote": quote, "source": "s18", "url": url, "level": level,
                   "from_master_source": False, "checked": CHECKED})

    add("accepted_name", f"Botanischer Name: {name}", f"stauden.de での学名表記：{name}", "cultivar")
    for a, b, field, ja in (("Blüten-Höhe von", "Blüten-Höhe bis", "height", "花の高さ"),
                            ("Blatt-Höhe von", "Blatt-Höhe bis", "height", "葉の高さ")):
        if a in og or b in og:
            lo = og.get(a, og.get(b))[0]["wert"]
            hi = og.get(b, og.get(a))[0]["wert"]
            rng = lo if lo == hi else f"{lo}–{hi}"
            add(field, f"{a.rsplit(' ', 1)[0]}: {rng} cm", f"{ja} {rng.replace('–', '〜')}cm", level_of(og.get(a, []) + og.get(b, [])))
    if "Blütezeit von" in og or "Blütezeit bis" in og:
        lo = og.get("Blütezeit von", og.get("Blütezeit bis"))[0]["wert"]
        hi = og.get("Blütezeit bis", og.get("Blütezeit von"))[0]["wert"]
        add("bloom_time", f"Blütezeit: {lo} bis {hi}", tr(lo) if lo == hi else f"{tr(lo)}〜{tr(hi)}",
            level_of(og.get("Blütezeit von", []) + og.get("Blütezeit bis", [])))
    for name_de, field in SDB_MAP.items():
        if name_de not in og:
            continue
        by_level = {}
        for w in og[name_de]:
            by_level.setdefault(w["ebene"], []).append(w["wert"])
        for lv, ws in by_level.items():
            pre = (LABEL_JA[name_de] + "：") if name_de in LABEL_JA else ""
            add(field, f"{name_de}: {'; '.join(ws)}", pre + "、".join(tr(w) for w in ws), lv)
    for w in og.get("Eigenschaften", []):
        f = {"ganz oder in Teilen giftig": "toxicity", "Blatt- oder Blütenduft": "fragrance"}.get(w["wert"], "ornamental")
        add(f, f"Eigenschaften: {w['wert']}", tr(w["wert"]), w["ebene"])
    for w in og.get("Allgemeine Verwendungsmöglichkeiten", []):
        f = {"Insektennährpflanze": "pollinators", "für Schnittzwecke, Floristik": "cut_flower"}.get(w["wert"], "uses")
        add(f, f"Allgemeine Verwendungsmöglichkeiten: {w['wert']}", tr(w["wert"]), w["ebene"])
    for w in og.get("Pflegehinweis", []):
        for head, f, ja in CARE:
            if w["wert"].startswith(head):
                add(f, f"Pflegehinweis: {w['wert']}", ja, w["ebene"])
                break
        else:
            raise SystemExit(f"訳のない Pflegehinweis: {w['wert']}")
    if "Sichtungswerte BdS" in og:
        v = og["Sichtungswerte BdS"][0]["wert"]
        yr = og.get("Jahr der letzten Sichtung", [{"wert": ""}])[0]["wert"]
        add("trial_rating", f"Sichtungswerte BdS: {v}" + (f"; Jahr der letzten Sichtung: {yr}" if yr else ""),
            f"品種評価（Staudensichtung）：{tr(v)}" + (f"、最後の評価年 {yr}" if yr else ""),
            og["Sichtungswerte BdS"][0]["ebene"])
    for e in ev:  # 訳し漏れの検出
        if re.search(r"[äöüß]|[a-z]{6,}", e["value_ja"]) and e["field"] not in ("accepted_name",):
            if not re.search(r"（(frisch|Risslinge|Begleiter|Gerüstbildner|Staudensichtung)）", e["value_ja"]):
                raise SystemExit(f"{pid}: 訳し漏れ {e['value_ja']}")
    return (url, name, relid), ev


# stauden.de で品種が見つからず、種のページを使ったもの
SDB_LEVEL_OVERRIDE = {"P14": "species", "P20": "species", "P23": "species", "P24": "species", "P26": "species"}
SDB_NOTE = {"P10": "stauden.de は Hosta × fortunei 'Gold Standard' として掲載", "P11": "stauden.de は Hemerocallis × cultorum 'Stella de Oro' として掲載",
            "P16": "stauden.de は Heuchera americana 'Green Spice' として掲載", "P18": "stauden.de は Lupinus polyphyllus 'Fräulein' として掲載",
            "P05": "stauden.de は var. camtschatica と表記", "P24": "stauden.de の Spiraea japonica のページは学名だけで、項目の記載がない",
            "P26": "stauden.de の表記は Lonicera periclyneum（つづり違い）。種のページ"}

# YList: 試作ID → 採用する学名の行（先頭一致）
YL_PICK = {"P01": "Artemisia schmidtiana Maxim.", "P02": "Aquilegia chrysantha A.Gray", "P03": "Ajuga reptans L.",
           "P05": "Achillea sibirica (Ledeb.) Regel subsp. camtschatica (Heimerl) Heimerl", "P09": "Miscanthus sinensis Andersson",
           "P12": "Echinacea purpurea (L.) Moench", "P14": "Armeria maritima (Mill.) Willd.", "P17": "Lysimachia nummularia L.",
           "P19": "Patrinia scabiosifolia Link", "P20": "Tricyrtis hirta (Thunb.) Hook.", "P21": "Geranium phaeum L.",
           "P22": "Phlox paniculata L.", "P23": "Anemone sylvestris L.", "P24": "Spiraea japonica L.f.",
           "P25": "Hydrangea serrata (Thunb.) Ser. var. yesoensis (Koidz.) H.Ohba", "P26": "Lonicera periclymenum L.",
           "P27": "Cornus alba L."}

MBG_NAME = {"P08": "Calamagrostis × acutiflora 'Karl Foerster'", "P09": "Miscanthus sinensis 'Morning Light'", "P10": "Hosta 'Gold Standard'",
            "P11": "Hemerocallis 'Stella de Oro'", "P12": "Echinacea purpurea 'Magnus'", "P15": "Sedum spurium 'Schorbuser Blut' DRAGON'S BLOOD",
            "P16": "Heuchera 'Green Spice'", "P18": "Lupinus × hybrida", "P20": "Tricyrtis 'Lightning Strike'",
            "P24": "Spiraea japonica 'Goldflame'", "P27": "Cornus alba 'Sibirica'"}
MBG_HEAD = (("Zone", "usda_zone", "USDAゾーン "), ("Height", "height", "草丈 "), ("Spread", "spread", "株張り "),
            ("BloomTime", "bloom_time", "花期 "), ("Sun", "sun", ""), ("Water", "soil_moisture", "水分 "))
SUN = {"Full sun": "日なた", "Full sun to part shade": "日なた〜半日陰", "Part shade to full shade": "半日陰〜日陰", "Part shade": "半日陰",
       "Full shade": "日陰"}
WATER = {"Dry to medium": "乾燥〜中", "Medium": "中", "Medium to wet": "中〜湿", "Dry": "乾燥", "Wet": "湿"}
TOL = {"Rabbit": "ウサギ", "Deer": "シカ", "Drought": "乾燥", "Dry Soil": "乾いた土", "Shallow-Rocky Soil": "浅い岩がちな土",
       "Urban Conditions": "都市環境（大気汚染）", "Black Walnut": "クログルミ", "Erosion": "土壌浸食", "Wet Soil": "湿った土",
       "Heavy Shade": "深い日陰", "Clay Soil": "粘土質", "Air Pollution": "大気汚染"}
EN_MON = dict(zip("January February March April May June July August September October November December".split(),
                  [f"{i}月" for i in range(1, 13)]))


def ft(s):
    def conv(m):
        a, b = float(m.group(1)), float(m.group(2))
        return f"{a:g}〜{b:g}フィート（約{round(a * 30.48)}〜{round(b * 30.48)}cm）"
    return re.sub(r"([\d.]+) to ([\d.]+) feet", conv, s)


def norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("”", '"').replace("“", '"')).strip()


def mbg_entries(pid):
    p = f"{RAW}/mbg/{pid}.json"
    j = json.load(open(p, encoding="utf-8"))
    if not j.get("pick"):
        return None, []
    F, url, lv = j["fields"], j["url"], j["level"]
    name = MBG_NAME.get(pid) or j["pick"][1]
    ev = []

    def add(field, quote, ja):
        ev.append({"field": field, "value_ja": ja, "quote": quote, "source": "s02", "url": url, "level": lv,
                   "from_master_source": False, "checked": CHECKED})

    add("accepted_name", name, f"MBG Plant Finder での表記：{name}")
    for key, field, pre in MBG_HEAD:
        if key not in F:
            continue
        q = F[key]
        v = q.split(": ", 1)[1]
        if key == "Sun":
            ja = SUN[v]
        elif key == "Water":
            ja = pre + WATER[v]
        elif key in ("Height", "Spread"):
            ja = pre + ft(v)
        elif key == "BloomTime":
            ja = pre + "".join(EN_MON.get(w, {"to": "〜"}.get(w, w)) for w in v.split())
        else:
            ja = pre + v.replace(" to ", "〜")
        add(field, q, ja)
    m = re.search(r"Tolerate: (.*?)(?: Garden locations| Interest:|$)", F.get("Maintenance", ""))
    if m:
        items = [x.strip() for x in m.group(1).split(",")]
        add("tolerate", "Tolerate: " + ", ".join(items), "耐えるもの：" + "、".join(TOL[x] for x in items))
        if "Drought" in items:
            add("drought", "Tolerate: " + ", ".join(items), "「耐えるもの」の欄に乾燥（Drought）がある")
    if "InvasiveLink" in F:
        add("invasive_note", F["InvasiveLink"], "MBG のページに侵略性の注意表示がある（地域の外来種情報を確認するよう案内）")
    body = norm(" ".join(F.get(k, "") for k in ("Culture", "Noteworthy", "Problems")))
    for cpid, field, quote, ja in CURATED:
        if cpid != pid:
            continue
        for part in quote.split(" ... "):
            if norm(part) not in body:
                raise SystemExit(f"{pid}: 原文に見つからない引用: {part}")
        add(field, quote, ja)
    return (url, name), ev


def main():
    for f in sorted(glob.glob(f"{TRIAL}/evidence/P*.json")):
        pid = os.path.basename(f)[:3]
        d = json.load(open(f, encoding="utf-8"))
        d["evidence"] = [e for e in d["evidence"] if e["source"] not in NEW_SOURCES]
        d["access_log"] = [a for a in d["access_log"] if a["source"] not in NEW_SOURCES]
        notes = []
        # --- MBG
        info, ev = mbg_entries(pid)
        if info:
            j = json.load(open(f"{RAW}/mbg/{pid}.json", encoding="utf-8"))
            d["access_log"].append({"source": "s02", "url": info[0], "status": "ok", "checked": CHECKED,
                                    "note": ("品種ページ" if j["level"] == "cultivar" else "種（または交配群）のページ") + f"：{info[1]}"})
            d["evidence"] += ev
            if pid == "P15":
                notes.append("MBG は 'Schorbuser Blut'（英名 DRAGON'S BLOOD）として掲載。（'Dragon's Blood' と 'Schorbuser Blut' が同じ品種かどうかは、学名の検討シートで確認する）")
            if pid == "P20":
                notes.append("MBG は Tricyrtis 'Lightning Strike'（種小名なし）として掲載")
        else:
            d["access_log"].append({"source": "s02", "url": "https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderSearch.aspx",
                                    "status": "not_found", "checked": CHECKED, "note": "Plant Finder を検索したが、品種・種とも該当ページなし"})
        # --- YList
        y = json.load(open(f"{RAW}/yl/{pid}.json", encoding="utf-8"))
        if pid in YL_PICK:
            row = next(r for r in y["rows"] if r["sci"] == YL_PICK[pid])
            url = f"http://ylist.info/ylist_detail_display.php?pass={row['pass']}"
            d["access_log"].append({"source": "s04", "url": url, "status": "ok", "checked": CHECKED, "note": f"{row['sci']}（{row['status']}）"})
            d["evidence"].append({"field": "common_name_ja", "value_ja": row["ja"], "quote": f"{row['sci']} {row['ja']} {row['status']}",
                                  "source": "s04", "url": url, "level": "species", "from_master_source": False, "checked": CHECKED})
            if row["status"] != "標準":
                notes.append(f"YList では {row['sci']} は synonym 扱い（和名 {row['ja']}）")
        elif "url" in y:
            d["access_log"].append({"source": "s04", "url": y["url"], "status": "not_found", "checked": CHECKED,
                                    "note": f"「{y['q']}」で検索、該当なし（YList は日本の野生植物と主な栽培植物が対象）"})
        else:
            d["access_log"].append({"source": "s04", "url": "http://ylist.info/", "status": "not_found", "checked": CHECKED,
                                    "note": "種が決まらない交配品種・属のみのため検索していない"})
        # --- stauden.de
        info, ev = sdb_entries(pid)
        if info:
            lv = SDB_LEVEL_OVERRIDE.get(pid)
            if lv:
                for e in ev:
                    e["level"] = "genus" if e["level"] == "genus" else "species"
            d["access_log"].append({"source": "s18", "url": info[0], "status": "ok", "checked": CHECKED,
                                    "note": ("種のページ（品種の掲載なし）" if lv else "品種ページ") + f"：{info[1]}。無料版（ログインなし）"})
            d["evidence"] += ev
            if pid in SDB_NOTE:
                notes.append(SDB_NOTE[pid])
        else:
            d["access_log"].append({"source": "s18", "url": "https://www.stauden.de/staudendatenbank.html", "status": "not_found",
                                    "checked": CHECKED, "note": "無料版を検索したが掲載なし"})
        # --- Jelitto(s11)・Gaißmayer(s17) はクラウドから読めない。merge_chrome.py が追記する
        found = {e["field"] for e in d["evidence"]}
        d["not_found"] = [x for x in d.get("not_found", []) if x not in found]
        chrome_mark = "\n\n【2026-11-19 追記：Jelitto・Gaißmayer（Chrome で確認）】"
        text, _, chrome = d.get("notes", "").partition(chrome_mark)
        base = re.split(r"\n\n【2026-11-19 追記】", text)[0]
        d["notes"] = base + ("\n\n【2026-11-19 追記】" + "。".join(notes) if notes else "") + (chrome_mark + chrome if chrome else "")
        json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        n = {s: sum(1 for e in d["evidence"] if e["source"] == s) for s in ("s02", "s04", "s18")}
        print(pid, n, "残りの not_found:", len(d["not_found"]))


main()
