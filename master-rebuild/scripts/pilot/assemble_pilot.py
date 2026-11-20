"""3属の試行: 集めた文献から、品種ごとの値の下書きを作る（Excel。リポジトリの外に出す）。

使い方: python3 -X utf8 scripts/pilot/assemble_pilot.py <input フォルダ> <digest.json> <生データのフォルダ> <出力.xlsx> [属ごとのデータのフォルダ]
例（アスター）: … batch_aster/input <digest> <raw> <出力.xlsx> batch_aster
考え方
- 品種のページがあればそれを使い、なければ同じ種のページ、それもなければ同じ属で最も多い書き方（属レベル）を使う。
  どの階層の記述かを「レベル」に残す（品種／種／属）。
- 耐暑性・蒸れ耐性・西日耐性は、RULES.md の決め方を言い回しの照合で下書きする（PATTERNS）。根拠の文を横に出すので、人が確認する。
- 花色・葉色・株張りは品種のページからだけ取る（種のページからは入れない）。
- 文献にない値は空欄のまま。
"""
import glob
import html
import json
import os
import re
import sys
from collections import Counter

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

# 属ごとのデータ（ogihara_data.py・gaissmayer_data.py・rhs_ids.py・jelitto_cbg_data.py）のフォルダ。省略時は3属の試行（scripts/pilot）
sys.path.insert(0, sys.argv[5] if len(sys.argv) > 5 else os.path.dirname(os.path.abspath(__file__)))
import gaissmayer_data as GA  # noqa: E402
import ogihara_data as OG  # noqa: E402
import rhs_ids as RH  # noqa: E402
import jelitto_cbg_data as JC  # noqa: E402

IN, DIGEST, RAW, OUT = sys.argv[1:5]
D = json.load(open(DIGEST, encoding="utf-8"))
ITEMS = [json.load(open(f, encoding="utf-8")) for f in sorted(glob.glob(IN + "/*.json"))]
OGI = {i: rec for rec in OG.OGIHARA for i in rec[0]}
JEL = {i: rec for rec in JC.JELITTO for i in rec[0]}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower().replace("'", "")).strip("-")


def sentences(t):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t or "") if s.strip()]


# ---------- 言い回しの照合（RULES.md の heat / muggy / west_sun） ----------
P_HEAT_WEAK = r"intolerant of (the )?hot|(performs?|grows?) poorly in [^.]*hot|dislike[s]? (the )?(hot|heat)|dislike[s]? [^.]*hot, humid summer|intolerant of (the )?(high |extreme )?heat|cool weather plant|not recommended for planting south|do(es)? not grow well in the deep south|not recommended for growing south|require[s]? a cool|prefer[s]? cool[- ](summer|weather|climate|temperature|night|condition)|best in cool summer|struggles? in (the )?heat|does not (do well|tolerate) .*heat|do(es)? not (do|perform) well [^.]*(night ?time temperatures|night temperatures|hot and humid|hot summer)"
P_HEAT_MID = r"some tolerance for hot|afternoon shade|decline[s]? .*hot summer|interrupts? in the heat|foliage may (decline|scorch|burn)|scorch|in hot summer climates|best in cool northern summer|full sun is best in cool|leaf burn|in the south it is best"
P_HEAT_STRONG = r"tolerates? (the )?(hot|heat)|heat tolerant|(?<!in)tolerant of [^.]*heat|tolerates hot and humid"
P_MUGGY_WEAK = r"intolerant of (the )?hot and humid|(performs?|grows?) poorly in [^.]*hot,? (and )?humid|dislike[s]? (the )?hot and humid|dislike[s]? [^.]*hot, humid|intolerant of (the )?(high )?heat and humidity|dislike[s]? .*humidity|melt[s]? out|not .*tolerant of .*humid|do(es)? not (do|perform) well in [^.]*hot and humid"
P_MUGGY_MID = r"some tolerance for hot and humid|(mildew|rust|leaf spot)[^.]*humid|humid[^.]*(mildew|rust|leaf spot|flop)|good air circulation|prefer[s]? .*dry air"
P_MUGGY_STRONG = r"tolerates? hot and humid|(?<!in)tolerant of .*humidity|tolerates? .*heat and humidity"
# 2026-11-20: 「intolerant of high heat and humidity」が tolerant of … heat に当たって 強 になっていた（スカビオサ）。in- の付く形を 強 から外し、弱 の言い回しに足した。
#   トロリウスの「cool weather plant」「dislikes dry soils and hot, humid summers」「not recommended for planting south of …」も 弱 に足した。
#   タリクトラムの「Performs poorly in hot and humid summer climates」「Intolerant of hot and humid conditions」「May grow poorly in climates with hot, humid summers」を 弱、
#   「Some tolerance for hot and humid summer weather」を 中 に足した（2026-11-20）。
P_AFTERNOON = r"afternoon shade|afternoon sun|scorch|leaf burn|protected from hot sun"


# MBG の品種ページの文を「属の記述」として同じ属のほかの種に広げない属。
# カンパニュラは MBG にページがあるのがホタルブクロの仲間（punctata・takesimana とその交配種）だけで、
# その文をラクティフローラやポルテンシュラギアナなど性質の違う種に当てると、推測で埋めることになるため。
# ペルシカリアも同じ（MBG の品種ページはアンプレクシカウリスだけで、アフィニスやミクロセファラに当てない）。
# セダムも同じ（MBG の品種ページは背の高いベンケイソウの仲間だけで、ミセバヤやウスリーの仲間に当てない）。
GENUS_MBG_SKIP = {"Campanula", "Persicaria", "Sedum"}

# 学名で、ユーザーが個別に決めたもの（2026-11-19 のチェックリスト）
NAME_OVERRIDE = {
 "G05": ("Geranium 'Blogold'", "流通名 Blue Sunrise。RHS の表記に合わせた"),
 "G24": ("Geranium sanguineum 'New Hampshire Purple'", "RHS・MBG・シカゴ植物園の表記に合わせた"),
 "V05": ("Veronica spicata subsp. incana", "RHS の表記に合わせた。商品名はそのまま"),
 "V10": ("Veronica spicata", "RHS のページは亜種 subsp. spicata。種として売っているので今の学名のまま"),
}
# 自社の観察（文献の値とは別に持つ）
OWN_NOTES = {"V04": "越冬：傷む年がある（2026-11-19 ユーザーの回答。シカゴ植物園の冬の傷みの記録と合う）"}


def judge(texts):
    """texts: [(文献名, レベル, 文)] → (耐暑性, 蒸れ, 午後の日陰の記述あり, 根拠)"""
    heat = muggy = None
    aft = False
    why = []
    hlv = set()
    rank = {"弱": 0, "中": 1, "強": 2}
    for src, lv, s in texts:
        low = s.lower()
        h = "弱" if re.search(P_HEAT_WEAK, low) else "中" if re.search(P_HEAT_MID, low) else "強" if re.search(P_HEAT_STRONG, low) else None
        m = "弱" if re.search(P_MUGGY_WEAK, low) else "強" if re.search(P_MUGGY_STRONG, low) else "中" if re.search(P_MUGGY_MID, low) else None
        if "better than most" in low:  # 「同属の中では強い」という比較の書き方は 強 にしない
            h = "中" if h == "強" else h
            m = "中" if m == "強" else m
        if re.search(P_AFTERNOON, low):
            aft = True
        if h or m or re.search(P_AFTERNOON, low):
            why.append(f"[{src}/{lv}] {s}")
        if h:
            hlv.add(lv)
        if h and (heat is None or rank[h] < rank[heat]):  # 割れたら控えめな側
            heat = h
        if m and (muggy is None or rank[m] < rank[muggy]):
            muggy = m
    return heat, muggy, aft, why, hlv


SUN_MBG = {"Full sun": "日向", "Full sun to part shade": "日向〜半日陰", "Part shade to full shade": "半日陰", "Part shade": "半日陰", "Full shade": "日陰"}
WATER_MBG = {"Dry to medium": "乾燥寄り", "Medium": "適湿", "Medium to wet": "湿潤寄り", "Dry": "乾燥寄り", "Wet": "湿潤寄り"}
LEAF_W = {"Blue": "ブルー系", "Yellow": "ゴールド・ライム系", "Gold": "ゴールド・ライム系", "Chartreuse": "ゴールド・ライム系", "Variegated": "斑入り",
          "Silvery Grey": "シルバー系", "Grey": "シルバー系", "Deep Green": "グリーン系", "Light Green": "グリーン系", "Green": "グリーン系",
          "Burgundy": "パープル・ブラック系", "Purple": "パープル・ブラック系", "Bronze": "ブロンズ・レッド系", "Red": "ブロンズ・レッド系"}
COLOR_W = {"Mauve/Lilac": "青・紫", "Deep Blue": "青・紫", "Light Blue": "青・紫", "Purple": "青・紫", "Deep Purple": "青・紫", "Blue": "青・紫",
           "Violet": "青・紫", "White": "白", "Cream": "白", "Light Pink": "ピンク", "Deep Pink": "ピンク", "Pink": "ピンク", "Rose": "ピンク",
           "Magenta": "ピンク", "Red": "赤", "Yellow": "黄", "Orange": "オレンジ・アプリコット", "Lavender": "青・紫"}
LICHT = {"sonnig": "日向", "absonnig": "半日陰", "halbschattig": "半日陰", "schattig": "日陰"}
PEST = [("slug", "ナメクジ"), ("snail", "カタツムリ"), ("leaf spot", "斑点病"), ("rust", "さび病"), ("powdery mildew", "うどんこ病"),
        ("downy mildew", "べと病"), ("root rot", "根腐れ"), ("crown rot", "株腐れ"), ("nematode", "葉センチュウ"), ("scale", "カイガラムシ"),
        ("virus", "ウイルス病"), ("deer", None), ("rabbit", None)]


def walters(k):
    p = f"{RAW}/walters/{k}.html"
    if not os.path.exists(p):
        return None
    t = open(p, encoding="utf-8").read()
    url, t = t.split("\n", 1)
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    x = re.sub(r"[ \t\xa0]+", " ", html.unescape(re.sub(r"<[^>]+>", "\n", t)))
    lines = [s.strip() for s in x.split("\n") if s.strip()]
    r = {"url": url, "f": {}}
    try:
        i = next(n for n, s in enumerate(lines) if s.startswith("USDA Zone:"))
    except StopIteration:
        return None
    r["zone"] = lines[i].split(":")[1].strip()
    r["name"] = (lines[i - 2] if i >= 2 else "").replace("â„¢", "™").replace("Â®", "®")
    r["text"] = lines[i + 2] if "Plant number" in lines[i + 1] else lines[i + 1]
    labels = ["Sun Exposure", "Soil Type", "Soil pH", "Soil Moisture", "Care Level", "Flower Colour", "Blooming Time", "Foliage Color",
              "Plant Uses & Characteristics", "Flower Head Size", "Height", "Spread", "Foot Traffic", "Growth Rate", "Print this Plant"]
    cur = None
    for s in lines[i + 2:]:
        if s in labels:
            if s == "Print this Plant":
                break
            cur = s
            r["f"][cur] = []
        elif cur and s not in ("Optimal Growing Conditions", "Appearance and Characteristics"):
            r["f"][cur].append(re.sub(r"\s+or$", "", s))
    return r


RHS_PEST = [("slug", "ナメクジ"), ("snail", "カタツムリ"), ("vine weevil", "キンケクチブトゾウムシ"), ("capsid", "カスミカメ"), ("sawfl", "ハバチ"),
            ("aphid", "アブラムシ"), ("virus", "ウイルス病"), ("leaf spot", "斑点病"), ("powdery mildew", "うどんこ病"), ("downy mildew", "べと病"),
            ("rust", "さび病"), ("honey fungus", "ナラタケ病"), ("leafhopper", "ヨコバイ"), ("caterpillar", "イモムシ"), ("eelworm", "線虫"),
            ("root rot", "根腐れ"), ("crown rot", "株腐れ")]


def rhs(k):
    """RHS の詳細ページから、表の項目（dt/dd）と How to grow の文を取る"""
    if k not in RH.RHS:
        return None
    pid, name, memo = RH.RHS[k]
    p = f"{RAW}/rhs/{pid}.html"
    if not os.path.exists(p):
        return None
    t = open(p, encoding="utf-8", errors="replace").read()

    def cl(x):
        x = re.sub(r"<button.*?</button>|<dialog.*?</dialog>|<svg.*?</svg>|<script.*?</script>", "", x, flags=re.S)
        return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).strip()
    f = {}
    for a, b in re.findall(r"<dt[^>]*>(.*?)</dt>\s*<dd[^>]*>(.*?)</dd>", t, re.S):
        key = cl(a).split(" (function")[0].strip()
        if key and key not in f:
            f[key] = cl(b)
    for lab in ("Cultivation", "Propagation", "Pruning", "Pests", "Diseases"):
        m = re.search(lab + r"\s*</h\d>\s*(.*?)</(?:div|section)>", t, re.S)
        if m:
            f[lab] = cl(m.group(1))
    # 「Colour & scent」の表（季節ごとの 花・葉 の色）
    i = t.find("Colour &")
    m = re.search(r"<table.*?</table>", t[i:] if i >= 0 else "", re.S)
    if m:
        fl, fo = [], []
        for row in re.findall(r"<tr[^>]*>(.*?)</tr>", m.group(0), re.S)[1:]:
            c = [cl(x) for x in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.S)]
            if len(c) >= 4:
                fl += [x.strip() for x in c[2].split(",") if x.strip()]
                fo += [x.strip() for x in c[3].split(",") if x.strip()]
        f["FlowerColour"] = list(dict.fromkeys(fl))
        f["FoliageColour"] = list(dict.fromkeys(fo))
    return {"name": name, "memo": memo, "url": f"https://www.rhs.org.uk/plants/{pid}/x/details", "f": f}


def pick(k, sk, gk, src):
    """品種 → 種 → 属 の順に、その文献のページを探す"""
    for key, lv in ((k, "品種"), (sk, "種"), (gk, "属")):
        if key and src in D.get(key, {}):
            return D[key][src], lv
    return None, None


def main():
    # 属レベルの代表: その属の MBG 品種ページでいちばん多い Culture の書き出し
    genus_mbg = {}
    for g in sorted({it["属"] for it in ITEMS}):
        c = Counter()
        for it in ITEMS:
            if it["属"] == g and "mbg" in D.get(it["id"], {}):
                c[D[it["id"]]["mbg"]["f"].get("Culture", "")[:80]] += 1
        if g not in GENUS_MBG_SKIP and c and c.most_common(1)[0][1] >= 2 and c.most_common(1)[0][1] >= 0.7 * sum(c.values()):  # 属のどの品種ページもほぼ同じ文のときだけ、属の記述として使う
            top = c.most_common(1)[0][0]
            for it in ITEMS:
                if it["属"] == g and D.get(it["id"], {}).get("mbg", {}).get("f", {}).get("Culture", "")[:80] == top:
                    genus_mbg[g] = D[it["id"]]["mbg"]
                    break
    for g, m in genus_mbg.items():
        D.setdefault("ge_" + g, {})["mbg"] = m
    rows = []
    cols = ["ID", "商品番号", "植物名", "学名（マスター）", "学名（採用）", "学名（RHS）", "文献での表記", "和名", "花色（分類）", "花色（文献の語）", "株張り(cm)", "葉色（分類）", "日照",
            "USDA", "RHS 耐寒性", "原産地", "耐暑性", "蒸れ耐性", "西日耐性", "暑さ・蒸れ・西日の根拠", "乾燥耐性", "土壌水分", "常緑性", "増え方", "病害虫", "切り戻し", "繁殖", "紅葉", "文献の注意", "自社の観察", "切り花", "蜜源", "花色（自社の値）", "株張り（自社の値・cm）", "葉色（自社の値）",
            "品種ページのある文献", "使った文献", "空欄の数", "耐暑性の決め方", "耐暑性（欧米の文献だけなら）"]
    for it in ITEMS:
        k = it["id"]
        sk = "sp_" + slug(it["species"])
        gk = "ge_" + it["属"]
        own = D.get(k, {})
        w = walters(k)
        og = OGI.get(k)
        ga = GA.GAISS.get(k)
        ga_own = bool(ga) and (ga[2] == "cultivar" or not it.get("品種名"))  # 種のページを品種に当てた分は、品種ページに数えず花色も取らない
        rh = rhs(k)
        r = dict.fromkeys(cols)
        r.update({"ID": k, "商品番号": it["商品番号"], "植物名": it["植物名"], "学名（マスター）": it["学名"]})
        names = [f"{lab}: {x['name']}" for lab, x in (("stauden.de", own.get("sdb")), ("MBG", own.get("mbg")), ("Walters", w)) if x]
        if ga:
            names.append("Gaißmayer: " + ga[1] + ("" if ga_own else "（種のページ）"))
        if og:
            names.append("おぎはら: " + og[2])
        r["文献での表記"] = " ／ ".join(names) or None
        y = D.get(sk, {}).get("yl")
        if y:
            std = [x for x in y["rows"] if x["status"] == "標準"]
            r["和名"] = (std or y["rows"])[0]["ja"] + "（種）"
        used, cv_src = set(), []
        if rh:
            # 名前だけの登録（栽培・色の項目が1つもないページ）は品種ページに数えない
            if set(k2 for k2, v2 in rh["f"].items() if v2) - {"Time to Maturity", "Family", "Native to GB/Ireland", "Genus", "Name Status", "Plant Range"}:
                cv_src.append("RHS")
            r["学名（RHS）"] = rh["name"] + (f"（{rh['memo']}）" if rh["memo"] else "") + (f" [{rh['f']['Name Status']}]" if rh["f"].get("Name Status") else "")
        for lab, x in (("stauden.de", own.get("sdb")), ("MBG", own.get("mbg")), ("Walters", w), ("Gaißmayer", ga_own), ("おぎはら", og and og[3] == "cultivar")):
            if x:
                cv_src.append(lab)
        # --- 品種のページからだけ取る項目
        if w:
            fc = w["f"].get("Flower Colour", [])
            r["花色（文献の語）"] = "、".join(fc) or None
            r["花色（分類）"] = "、".join(dict.fromkeys(COLOR_W[c] for c in fc if c in COLOR_W)) or None
            sp_cm = next((s for s in w["f"].get("Spread", []) if "cm" in s), None)
            r["株張り(cm)"] = sp_cm.replace(" cm", "").replace("-", "〜") if sp_cm else None
            lf = [LEAF_W[c] for c in w["f"].get("Foliage Color", []) if c in LEAF_W]
            r["葉色（分類）"] = "斑入り" if "斑入り" in lf else (lf[0] if lf else None)
            used.add("Walters")
        if ga_own and not r["花色（文献の語）"]:
            r["花色（文献の語）"] = ga[3]
            used.add("Gaißmayer")
        # --- 日照・USDA・水分（品種 → 種 → 属）
        m, mlv = pick(k, sk, gk, "mbg")
        s, slv = pick(k, sk, None, "sdb")
        if m:
            f = m["f"]
            r["日照"] = SUN_MBG.get(f.get("Sun", "")[5:].strip())
            z = re.search(r"(\d+) to (\d+)", f.get("Zone", ""))
            r["USDA"] = f"{z[1]}〜{z[2]}（MBG・{mlv}）" if z else None
            r["土壌水分"] = WATER_MBG.get(f.get("Water", "")[7:].strip())
            used.add("MBG")
        if not r["日照"] and w and w["f"].get("Sun Exposure"):
            se = w["f"]["Sun Exposure"]
            r["日照"] = "日向〜半日陰" if "Full Sun" in se and "Partial Shade" in se else "日向" if "Full Sun" in se else "半日陰" if "Partial Shade" in se else "日陰"
        if not r["日照"] and s and "Lichtansprüche" in s["f"]:
            L = [LICHT.get(v) for v, _ in s["f"]["Lichtansprüche"]]
            r["日照"] = "日向〜半日陰" if "日向" in L and "半日陰" in L else "日向" if "日向" in L else "半日陰" if "半日陰" in L else "日陰"
            used.add("stauden.de")
        if not r["USDA"] and w:
            r["USDA"] = w["zone"].replace("-", "〜") + "（Walters・品種）"
        # --- 暑さ・蒸れ・西日
        texts = []
        if m:
            for sct in ("Culture", "Problems", "Noteworthy"):
                texts += [("MBG", mlv, x) for x in sentences(m["f"].get(sct, ""))]
        n, nlv = pick(k, sk, None, "ncsu")
        if n:
            nl = "属" if n["url"].rstrip("/").split("/")[-1] == it["属"].lower() else nlv
            for key in ("Description", "Insects, Diseases, and Other Plant Problems"):
                texts += [("NC State", nl, x) for x in sentences(n["f"].get(key, ""))]
            used.add("NC State")
        if w:
            texts += [("Walters", "品種", x) for x in sentences(w["text"])]
        heat, muggy, aft, why, hlv = judge(texts)
        r["耐暑性（欧米の文献だけなら）"] = heat
        r["耐暑性の決め方"] = "欧米の文献" if heat else None
        sib = getattr(OG, "SIBLING", {}).get(it["species"])
        if og:
            r["耐暑性の決め方"] = "おぎはら（" + ("品種" if og[3] == "cultivar" else "種") + "のページ）"
            # 2026-11-19 の最後の決定: おぎはら植物園にページがあれば、耐暑性はおぎはらの値を採る（日本の条件での評価）
            lab = "品種" if og[3] == "cultivar" else "種"
            if heat and og[4] != heat:
                why.append(f"[食い違い] 欧米の文献（{'・'.join(sorted(hlv))}の記述）は {heat} 相当。おぎはら植物園の値を採った")
            why.insert(0, f"[おぎはら/{lab}] 耐暑性；{og[4]}")
            heat = og[4]
            used.add("おぎはら")
        elif sib:
            # 2026-11-19 のユーザーの決定: おぎはらが同じ種の別品種をどれも同じ値にしているとき、載っていない同種の品種にもその値を使う。
            # あとで見返せるように、決め方と「欧米の文献だけなら」の値を別の列に残す（信頼度は低）。対象の種は <データのフォルダ>/ogihara_data.py の SIBLING
            if heat and sib[0] != heat:
                why.append(f"[食い違い] 欧米の文献（{'・'.join(sorted(hlv))}の記述）は {heat} 相当。おぎはら植物園の同じ種の品種の値を採った")
            why.insert(0, f"[おぎはら/同じ種の別品種（{'・'.join(sib[1])}）] 耐暑性；{sib[0]}（この品種のページはない。信頼度：低）")
            heat = sib[0]
            r["耐暑性の決め方"] = "おぎはら（同じ種の別品種から。信頼度：低）"
            used.add("おぎはら")
        r["耐暑性"], r["蒸れ耐性"] = heat, muggy
        drought = None
        alltext = " ".join(x for _, _, x in texts).lower()
        if m and "Drought" in m["f"].get("Tolerate", ""):
            drought = "強"
        elif re.search(r"some drought|occasional drought|tolerance for (some )?dry", alltext) and not re.search(r"intolerant of dry", alltext):
            drought = "中"
        elif re.search(r"intolerant of dry|never be allowed to dry out|(should|must) not be allowed to dry", alltext):
            drought = "弱"
        elif re.search(r"tolerates drought|drought tolerant", alltext) or (w and "Drought Tolerant" in w["f"].get("Plant Uses & Characteristics", [])):
            drought = "強"
        elif re.search(r"some drought|tolerance for (some )?dry", alltext):
            drought = "中"
        r["乾燥耐性"] = drought
        sun = r["日照"]
        if sun in ("半日陰", "日陰") or re.search(r"scorch|leaf burn|afternoon sun is", alltext):
            west = "×"
        elif aft or heat == "弱":
            west = "△"
        elif sun and sun.startswith("日向") and heat == "強" and drought == "強":
            west = "◎"
        elif heat in ("中", "強"):
            west = "○"
        else:
            west = None
        if rh and rh["f"].get("Aspect"):
            asp = rh["f"]["Aspect"].replace("–", "-")
            if "West-facing" not in asp and "South-facing" not in asp:
                west = "×"
                why.append(f"[RHS/品種] Aspect: {asp}（西向き・南向きが入っていない）")
            elif "West-facing" not in asp and west in (None, "○", "◎"):
                west = "△"
                why.append(f"[RHS/品種] Aspect: {asp}（西向きが入っていない）")
            else:
                why.append(f"[RHS/品種] Aspect: {asp}")
            used.add("RHS")
        r["西日耐性"] = west
        r["暑さ・蒸れ・西日の根拠"] = "\n".join(why[:6]) or None
        # --- 常緑性・増え方（stauden.de）
        if s:
            f = s["f"]
            ph = [v for v, _ in f.get("Blattphase", [])]
            r["常緑性"] = {"immergrün": "常緑", "wintergrün": "半常緑", "sommergrün": "落葉"}.get(ph[0]) + f"（stauden.de・{slv}）" if ph and ph[0] in ("immergrün", "wintergrün", "sommergrün") else None
            wv = [v for v, _ in f.get("Wuchsverhalten", [])]
            modes = []
            if any("horst" in v for v in wv):
                modes.append("株立ち")
            if any("rhizom" in v for v in wv):
                modes.append("地下茎")
            if any("ausläufer" in v or "kriechend" in v for v in wv):
                modes.append("ランナー")
            gen = [v for v, _ in f.get("MS-Generativer Ausbreitungsdrang", [])]
            if gen and "nicht" not in gen[0] and "steril" not in gen[0]:
                modes.append("こぼれ種")
            r["増え方"] = "、".join(dict.fromkeys(modes)) or None
            used.add("stauden.de")
            uses = [v for v, _ in f.get("Allgemeine Verwendungsmöglichkeiten", [])]
            if any("Schnitt" in v for v in uses):
                r["切り花"] = "○"
            if any("Insekten" in v for v in uses):
                r["蜜源"] = "○"
        if w:
            u = w["f"].get("Plant Uses & Characteristics", [])
            if "Cut Flower" in u:
                r["切り花"] = "○"
            if any("Attracts" in x for x in u):
                r["蜜源"] = "○"
        # --- 病害虫・切り戻し（MBG の Problems / Culture）
        if m:
            pr = m["f"].get("Problems", "").lower()
            ps = [ja for en, ja in PEST if ja and en in pr]
            r["病害虫"] = ("、".join(dict.fromkeys(ps)) or ("特になし" if "no serious" in pr else None))
            if r["病害虫"]:
                r["病害虫"] += f"（MBG・{mlv}）"
            cu = m["f"].get("Culture", "").lower()
            codes = []
            if re.search(r"after flowering|spent flower|deadhead|after bloom", cu):
                codes.append("花後")
            if re.search(r"do not need to be cut back", cu):
                codes = ["不要"]
            r["切り戻し"] = "、".join(codes) + f"（MBG・{mlv}）" if codes else None
        if rh:
            f = rh["f"]
            r["RHS 耐寒性"] = f.get("Hardiness")
            fo = f.get("Foliage", "")
            ev = "半常緑" if "Semi" in fo else "常緑" if "Evergreen" in fo else "落葉" if "Deciduous" in fo else None
            if ev:
                r["常緑性"] = ev + "（RHS）"
            mo = f.get("Moisture", "").replace("–", "-")
            if mo:
                r["土壌水分"] = "湿潤寄り" if "Poorly-drained" in mo else "適湿" if "Moist but well-drained" in mo else "排水必須" if "Well-drained" in mo else r["土壌水分"]
            if not r["株張り(cm)"] and f.get("Max Spread"):
                mm = re.search(r"([\d.]+)-([\d.]+) metre", f["Max Spread"])
                if mm:
                    r["株張り(cm)"] = f"{round(float(mm[1]) * 100)}〜{round(float(mm[2]) * 100)}（RHS の幅）"
            pd = (f.get("Pests", "") + " " + f.get("Diseases", "")).lower()
            ps = [ja for en, ja in RHS_PEST if en in pd]
            if ps:
                r["病害虫"] = "、".join(dict.fromkeys(ps)) + "（RHS）"
            elif "pest-free" in pd or "pest free" in pd:
                r["病害虫"] = "特になし（RHS）"
            pr = f.get("Pruning", "").lower()
            codes = []
            if re.search(r"after flowering|flowered stems|spent flower|deadhead|faded flower", pr):
                codes.append("花後")
            if re.search(r"end of the growing season|in autumn|dies back", pr):
                codes.append("秋")
            if re.search(r"late winter|early spring|in spring", pr):
                codes.append("早春")
            if "no pruning" in pr:
                codes = ["不要"]
            if codes:
                r["切り戻し"] = "、".join(codes) + "（RHS）"
            # 花色・葉色（RHS の Colour & scent の表）。Walters・Gaißmayer で入っていないときに使う
            RC = {"Blue": "青・紫", "Purple": "青・紫", "Pink": "ピンク", "White": "白", "Cream": "白", "Red": "赤", "Yellow": "黄", "Orange": "オレンジ・アプリコット"}
            if f.get("FlowerColour"):
                if not r["花色（文献の語）"]:
                    r["花色（文献の語）"] = "、".join(f["FlowerColour"]) + "（RHS）"
                if not r["花色（分類）"]:
                    r["花色（分類）"] = "、".join(dict.fromkeys(RC[c] for c in f["FlowerColour"] if c in RC)) or None
            fo = f.get("FoliageColour") or []
            if fo and not r["葉色（分類）"]:
                lc = ("斑入り" if "Variegated" in fo else "ブルー系" if "Blue" in fo else "ゴールド・ライム系" if ("Yellow" in fo or "Gold" in fo)
                      else "シルバー系" if ("Grey" in fo or "Silver" in fo) else "パープル・ブラック系" if "Purple" in fo
                      else "ブロンズ・レッド系" if ("Bronze" in fo or "Red" in fo) else "グリーン系" if "Green" in fo else None)
                if lc:
                    r["葉色（分類）"] = lc
                    r["_leaf_src"] = "RHS: " + ", ".join(fo)
            pg = f.get("Propagation", "").lower()
            ways = [ja for en, ja in (("division", "株分け"), ("cutting", "挿し木"), ("seed", "実生")) if en in pg]
            r["繁殖"] = "、".join(ways) + "（RHS）" if ways else None
            used.add("RHS")
        # --- シカゴ植物園の評価報告（ゲラニウム）: 品種ごとの株幅・秋の葉色・花後の切り戻し
        cb = JC.CBG.get(k) or JC.CBG_V.get(k)
        if cb:
            if cb[3] and not (w and w["f"].get("Spread")):
                wd = cb[3] if isinstance(cb[3], (tuple, list)) else (cb[3],)  # 幅で書かれている報告は (下限, 上限) のインチ
                r["株張り(cm)"] = "〜".join(str(round(x * 2.54)) for x in wd) + "（シカゴ植物園の試験での株幅）"
            if cb[4] and cb[4] != "none observed":
                r["紅葉"] = "秋に" + "・".join(JC.AUTUMN.get(c.strip(), c.strip()) for c in cb[4].split(",")) + "（シカゴ植物園）"
            if len(cb) > 7 and cb[7]:
                r["文献の注意"] = "シカゴ植物園: " + cb[7]
            if cb[5] == "Yes+" and not r["切り戻し"]:
                r["切り戻し"] = "花後（シカゴ植物園: 花後に切り戻すと姿が良くなった）"
            used.add("シカゴ植物園")
            if cb[1] == "cultivar":
                cv_src.append("シカゴ植物園")
        # --- Jelitto: 原産地と蜜源（種のページでも使える項目）。ゾーン・花期・高さ・暑さは使わない
        je = JEL.get(k)
        if je:
            if je[12]:
                r["原産地"] = je[12] + "（Jelitto・" + ("品種" if je[2] == "cultivar" else "種") + "）"
            if "honey-bee food plant" in je[11] and not r["蜜源"]:
                r["蜜源"] = "○"
            used.add("Jelitto")
            if je[2] == "cultivar":
                cv_src.append("Jelitto")
        # --- 自社の値: 文献で埋まらなかった花色・株張り・葉色に、今のマスターの値を別の列で残す（2026-11-19 決定）
        if not r["花色（文献の語）"] and it.get("花色"):
            r["花色（自社の値）"] = it["花色"]
        if not r["株張り(cm)"] and it.get("広がり(cm)"):
            r["株張り（自社の値・cm）"] = str(it["広がり(cm)"])
        if not r["葉色（分類）"] and it.get("葉色主分類"):
            r["葉色（自社の値）"] = it["葉色主分類"]
        # --- 学名（採用）: 2026-11-19 決定。RHS が正名（Accepted／Correct）としていれば RHS の表記に合わせる。
        #     RHS で未確定・シノニム・掲載なしのときは今の学名のまま（学名の検討シートに残す）
        adopted, note = it["学名"], None
        if k in NAME_OVERRIDE:
            adopted, note = NAME_OVERRIDE[k]
        elif rh and rh["f"].get("Name Status") in ("Accepted", "Correct") and not rh["memo"]:
            adopted = re.sub(r"\s+", " ", re.sub(r"\((v|[a-z ]+)\)", "", rh["name"])).strip()
        r["学名（採用）"] = adopted + (f"（{note}）" if note else "")
        if k in OWN_NOTES:
            r["自社の観察"] = OWN_NOTES[k]
        r["品種ページのある文献"] = "、".join(cv_src) or "なし"
        r["使った文献"] = "、".join(sorted(used)) or None
        core = ["花色（文献の語）", "株張り(cm)", "葉色（分類）", "日照", "USDA", "耐暑性", "蒸れ耐性", "西日耐性", "乾燥耐性", "土壌水分", "常緑性", "増え方", "病害虫",
                "切り戻し", "繁殖", "切り花", "蜜源", "和名"]
        r["空欄の数"] = sum(1 for c in core if r[c] in (None, ""))
        r["_core"] = core
        rows.append(r)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "下書き"
    ws.append(cols)
    for r in rows:
        ws.append([r[c] for c in cols])
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="2F6B4A")
    for row in ws.iter_rows(min_row=1):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    for i, wd in enumerate([6, 8, 30, 30, 40, 16, 10, 16, 9, 12, 12, 16, 7, 7, 7, 70, 7, 10, 16, 16, 24, 14, 6, 6, 22, 22, 7], 1):
        ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = wd
    ws.freeze_panes = "D2"

    def sheet(title, header, data, widths):
        w2 = wb.create_sheet(title)
        w2.append(header)
        for row in data:
            w2.append(row)
        for c in w2[1]:
            c.font = Font(bold=True, color="FFFFFF")
            c.fill = PatternFill("solid", fgColor="2F6B4A")
        for row in w2.iter_rows(min_row=1):
            for c in row:
                c.alignment = Alignment(wrap_text=True, vertical="top")
        for i, wd in enumerate(widths, 1):
            w2.column_dimensions[openpyxl.utils.get_column_letter(i)].width = wd
        w2.freeze_panes = "A2"

    # --- 根拠: 値ごとに、どの文献のどの階層（品種／種／属）から来たか
    ev = []
    for r in rows:
        for c in ("日照", "USDA", "RHS 耐寒性", "原産地", "乾燥耐性", "土壌水分", "常緑性", "増え方", "病害虫", "切り戻し", "繁殖", "紅葉", "株張り(cm)",
                  "花色（文献の語）", "葉色（分類）", "切り花", "蜜源", "和名"):
            v = r[c]
            if v in (None, ""):
                continue
            m = re.search(r"（([^（）]*)）$", str(v))
            ev.append([r["ID"], r["商品番号"], r["植物名"], c, v, m.group(1) if m else "（組み立て時に文献名を付けていない項目。使った文献の列を参照）"])
        for c in ("耐暑性", "蒸れ耐性", "西日耐性"):
            if r[c]:
                ev.append([r["ID"], r["商品番号"], r["植物名"], c, r[c], r["暑さ・蒸れ・西日の根拠"]])
        for c in ("花色（自社の値）", "株張り（自社の値・cm）", "葉色（自社の値）"):
            if r[c]:
                ev.append([r["ID"], r["商品番号"], r["植物名"], c, r[c], "今のマスターの値（文献に品種の記述がないため、自社の値として残した）"])
    sheet("根拠", ["ID", "商品番号", "植物名", "項目", "値", "文献・階層・根拠の文"], ev, [6, 8, 30, 18, 30, 90])

    # --- 学名の検討: マスターの学名と、文献での表記が違うもの
    def nz(x):
        x = re.sub(r"\(.*?\)|\[.*?\]|（.*?）", " ", x or "")
        x = x.replace("×", " ").replace("‘", "'").replace("’", "'")
        return re.sub(r"[^a-z]", "", re.sub(r"\bx\b", " ", x.lower()))
    nm = []
    for r in rows:
        k = r["ID"]
        own = D.get(k, {})
        rh = RH.RHS.get(k)
        cand = [("RHS", rh[1] if rh else None), ("stauden.de", own.get("sdb", {}).get("name")), ("MBG", own.get("mbg", {}).get("name"))]
        diff = [f"{lab}: {x}" for lab, x in cand if x and nz(x) != nz(r["学名（マスター）"])]
        status = re.search(r"\[(\w+)\]$", r["学名（RHS）"] or "")
        if diff or (status and status.group(1) not in ("Accepted", "Correct")) or (rh and rh[2]):
            nm.append([k, r["商品番号"], r["植物名"], r["学名（マスター）"], rh[1] if rh else None, status.group(1) if status else None,
                       " ／ ".join(diff) or None, rh[2] if rh else None, None])
    sheet("学名の検討", ["ID", "商品番号", "植物名", "今の学名", "RHS の表記", "RHS での扱い", "今の学名と違う表記", "メモ", "御社の判断（記入）"], nm,
          [6, 8, 30, 32, 36, 12, 60, 40, 24])
    wb.save(OUT)
    print("根拠", len(ev), "行 / 学名の検討", len(nm), "品種")
    core = rows[0]["_core"]
    print("品種", len(rows))
    print("項目ごとの空欄:", {c: sum(1 for r in rows if r[c] in (None, "")) for c in core})
    gen = {it["id"]: it["属"] for it in ITEMS}
    avg = {}
    for g in sorted(set(gen.values())):
        v = [r["空欄の数"] for r in rows if gen[r["ID"]] == g]
        avg[g] = round(sum(v) / len(v), 1)
    print("属ごとの平均空欄:", avg)
    print("耐暑", Counter(str(r["耐暑性"]) for r in rows), "蒸れ", Counter(str(r["蒸れ耐性"]) for r in rows), "西日", Counter(str(r["西日耐性"]) for r in rows))
    print("品種ページのある文献がない:", [r["ID"] for r in rows if r["品種ページのある文献"] == "なし"])
    json.dump([{c: r[c] for c in cols} for r in rows], open(OUT[:-5] + ".json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)


main()
