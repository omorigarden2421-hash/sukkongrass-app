"""下書きに足す列（2026-11-21）: 科名・香り・毒性・pH・土質・こぼれ種の量(0-3)・地下茎で広がる程度(0-3)。
assemble_pilot.py から呼ぶ。決め方は trial/RULES.md（fragrance・toxicity・soil_ph_type・self_seed_level・rhizome_level）に合わせた。
- 科名・毒性・pH・土質・こぼれ種・地下茎は、種のページの記述も使う（RULES.md）。香りは、品種のページ（品種名のない商品は種のページ）だけ
- こぼれ種・地下茎は言い回しの照合。根拠の文を「こぼれ種・地下茎の根拠」の列に出すので、人が確かめる。
  種の記述から決めた値は、品種でも同じとは限らない（不稔の品種など）。根拠の列にレベル（品種／種／属）を書いてある
"""
import re

FAMILY_JA = {
 "Asteraceae": "キク科", "Compositae": "キク科", "Lamiaceae": "シソ科", "Labiatae": "シソ科", "Rosaceae": "バラ科", "Ranunculaceae": "キンポウゲ科", "Poaceae": "イネ科",
 "Gramineae": "イネ科", "Cyperaceae": "カヤツリグサ科", "Asparagaceae": "キジカクシ科", "Fabaceae": "マメ科", "Leguminosae": "マメ科", "Papilionaceae": "マメ科",
 "Apiaceae": "セリ科", "Umbelliferae": "セリ科", "Caryophyllaceae": "ナデシコ科", "Brassicaceae": "アブラナ科", "Cruciferae": "アブラナ科", "Saxifragaceae": "ユキノシタ科",
 "Crassulaceae": "ベンケイソウ科", "Geraniaceae": "フウロソウ科", "Plantaginaceae": "オオバコ科", "Scrophulariaceae": "ゴマノハグサ科", "Campanulaceae": "キキョウ科",
 "Polemoniaceae": "ハナシノブ科", "Boraginaceae": "ムラサキ科", "Primulaceae": "サクラソウ科", "Polygonaceae": "タデ科", "Caprifoliaceae": "スイカズラ科",
 "Dipsacaceae": "マツムシソウ科", "Valerianaceae": "オミナエシ科", "Apocynaceae": "キョウチクトウ科", "Asclepiadaceae": "ガガイモ科", "Malvaceae": "アオイ科",
 "Onagraceae": "アカバナ科", "Iridaceae": "アヤメ科", "Amaryllidaceae": "ヒガンバナ科", "Liliaceae": "ユリ科", "Xanthorrhoeaceae": "ススキノキ科", "Asphodelaceae": "ススキノキ科",
 "Hemerocallidaceae": "ススキノキ科", "Convallariaceae": "キジカクシ科", "Ruscaceae": "キジカクシ科", "Agavaceae": "キジカクシ科", "Hostaceae": "キジカクシ科",
 "Hydrangeaceae": "アジサイ科", "Papaveraceae": "ケシ科", "Fumariaceae": "ケシ科", "Berberidaceae": "メギ科", "Euphorbiaceae": "トウダイグサ科", "Violaceae": "スミレ科",
 "Lythraceae": "ミソハギ科", "Plumbaginaceae": "イソマツ科", "Paeoniaceae": "ボタン科", "Ericaceae": "ツツジ科", "Cistaceae": "ハンニチバナ科", "Buxaceae": "ツゲ科",
 "Araliaceae": "ウコギ科", "Vitaceae": "ブドウ科", "Celastraceae": "ニシキギ科", "Cornaceae": "ミズキ科", "Adoxaceae": "ガマズミ科", "Viburnaceae": "ガマズミ科",
 "Verbenaceae": "クマツヅラ科", "Acanthaceae": "キツネノマゴ科", "Gentianaceae": "リンドウ科", "Rubiaceae": "アカネ科", "Commelinaceae": "ツユクサ科",
 "Athyriaceae": "メシダ科", "Woodsiaceae": "イワデンダ科", "Dryopteridaceae": "オシダ科", "Aspleniaceae": "チャセンシダ科", "Montiaceae": "ヌマハコベ科",
 "Portulacaceae": "スベリヒユ科", "Linaceae": "アマ科", "Globulariaceae": "オオバコ科", "Phrymaceae": "ハエドクソウ科", "Solanaceae": "ナス科", "Thymelaeaceae": "ジンチョウゲ科",
 "Hypericaceae": "オトギリソウ科", "Clusiaceae": "オトギリソウ科", "Nyctaginaceae": "オシロイバナ科", "Colchicaceae": "イヌサフラン科", "Melanthiaceae": "シュロソウ科",
 "Araceae": "サトイモ科", "Juncaceae": "イグサ科", "Tropaeolaceae": "ノウゼンハレン科", "Bignoniaceae": "ノウゼンカズラ科", "Oleaceae": "モクセイ科",
 "Calycanthaceae": "ロウバイ科", "Aizoaceae": "ハマミズナ科", "Resedaceae": "モクセイソウ科", "Urticaceae": "イラクサ科", "Cannabaceae": "アサ科", "Rutaceae": "ミカン科",
 "Menyanthaceae": "ミツガシワ科", "Nymphaeaceae": "スイレン科", "Typhaceae": "ガマ科", "Alismataceae": "オモダカ科", "Equisetaceae": "トクサ科", "Osmundaceae": "ゼンマイ科",
 "Onocleaceae": "コウヤワラビ科", "Pteridaceae": "イノモトソウ科", "Polypodiaceae": "ウラボシ科", "Tamaricaceae": "ギョリュウ科", "Elaeagnaceae": "グミ科",
 "Santalaceae": "ビャクダン科", "Zingiberaceae": "ショウガ科", "Cannaceae": "カンナ科", "Musaceae": "バショウ科", "Phytolaccaceae": "ヤマゴボウ科", "Amaranthaceae": "ヒユ科",
 "Chenopodiaceae": "ヒユ科", "Frankeniaceae": "フランケニア科", "Loganiaceae": "マチン科", "Buddlejaceae": "ゴマノハグサ科", "Stachyuraceae": "キブシ科", "Diervillaceae": "スイカズラ科",
 "Linnaeaceae": "スイカズラ科", "Morinaceae": "スイカズラ科", "Tofieldiaceae": "チシマゼキショウ科", "Xyridaceae": "トウエンソウ科", "Sapindaceae": "ムクロジ科",
}
PH = (("acid", "酸性"), ("neutral", "中性"), ("alkalin", "アルカリ性"))
SOIL = (("clay", "粘土"), ("sand", "砂質"), ("loam", "ローム"), ("chalk", "白亜質"), ("high organic", "腐植質"), ("rocky", "岩混じり"), ("normal", "普通の土"))
PARTS = (("leav", "葉"), ("leaf", "葉"), ("flower", "花"), ("root", "根"), ("seed", "種子"), ("fruit", "実"), ("sap", "汁液"), ("juice", "汁液"), ("stem", "茎"), ("bark", "樹皮"), ("bulb", "球根"))

# こぼれ種（英語）
S0 = r"\bsterile (hybrid|cultivar|variety|plant|triploid|selection|seed)|\b(is|are) (seed[- ])?sterile|does not self-?seed|will not self-?seed|does not (set|produce) (viable )?seed|seedless|non-seeding|produces? no (viable )?seed"
S3 = r"(aggressive|rampant|invasive|weedy)(ly)? (self-?(seed|sow)|reseed)|self-?(seed|sow)s? (so )?(aggressively|invasively|rampantly)|(self-?seeding|reseeding) can be (a problem|invasive|aggressive|weedy)|weedy (through|by|from) self-?seeding|can (be|become) (invasive|weedy|aggressive) (by|through|from|via) (self-?seeding|seed)"
S2 = r"(freely|readily|easily|abundantly|vigorously|prolifically) (self-?(seed|sow)|reseed)|(self-?(seed|sow)|reseed)s? (itself )?(freely|readily|easily|abundantly|vigorously|prolifically|generously|profusely)|prolific (self-?seeder|reseeder)|freely by (self-?seeding|seed)"
S1 = r"self-?(seed|sow)|(will|may|can|often|readily|freely) reseed|reseeds? (itself|in|around|where)|naturaliz(e|es|ing) by seed|seeds? (itself )?around"
# 地下茎・ランナー（英語）
RW = r"rhizom|stolon|runner|underground|sucker|creeping root|root(s|ing) at the nodes|spread"
R0 = r"does not spread|doesn.t spread|non-spreading|not (considered )?(to be )?(invasive|aggressive)|non-invasive|will not spread|non-running|not a spreader|stays? in (a )?(tight |neat )?clumps?|clumps? do(es)? not spread|without (being|becoming) (invasive|aggressive)|(does|do|will) not (spread|run)(?! (aggressively|rapidly|quickly|as|very))"
R3 = r"(spreads?|spreading|spread) (very |quite )?(aggressively|rapidly|invasively|rampantly)|aggressive(ly)? (spread|rhizom|stolon|runner|sucker|coloniz|ground ?cover)|invasive (spreader|rhizom|runner|stolon)|(can|may|tends? to) (be|become) (quite |very |somewhat )?(invasive|aggressive)|rampant|difficult to contain|aggressive spreader|spreads? to the point of"
R1 = r"(does|do|will) not spread (aggressively|rapidly|quickly|very)|less (apt|likely|prone|inclined) to spread|less (aggressive|invasive)|(spreads?|spreading|creeps?|creeping|expands?|expanding) (very |quite )?(slowly|gradually)|(slowly|gradually) (spread|creep|expand|coloniz|form)|slow(ly)?[- ](spreading|creeping)|short (rhizomes|stolons|runners)|slow to spread|not (overly|too|very) aggressive|slowly forming"
R2 = r"spreads? (by|via|through|from) (creeping |underground |short |slender |its )?(rhizom|stolon|runner|sucker|root|stem)|spreading by|rhizomatous|stoloniferous|(by|via) (creeping |underground )?(rhizomes|stolons|runners|suckers)|form(s|ing)? (large |dense |extensive |sizable )?colon|coloniz|suckers? (freely|to form)|root(s|ing) at the nodes|vigorous(ly)? spread|spreads? (quickly|widely|freely|readily|indefinitely|vigorously)|running (rhizom|habit)"


import json as _json
import os as _os
_SRR = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "spread_reread.json")
SPREAD_RR = _json.load(open(_SRR, encoding="utf-8")) if _os.path.exists(_SRR) else {}

SDB_LV = {"species": "種", "genus": "属"}
LV_RANK = {"品種": 0, "種": 1, "属": 2}


def sdb_tag(tag, slv):
    """stauden.de の値ごとの印 → 段階。"cultivar" の印は、そのページの段階（種のページなら 種）"""
    return SDB_LV.get(tag, slv)


def sdb_lv(s, keys, slv, use=None):
    """stauden.de の値の段階（2026-11-24）。品種のページにも、種・属から引き継いだ値が載る（値ごとの "cultivar"／"species"／"genus" の印）。
    keys の値（use を渡したら、use(値) が真の値だけ）のうち、いちばん広い段階を返す。値がなければ slv"""
    lvs = [slv]
    for key in ([keys] if isinstance(keys, str) else keys):
        for v, tag in s["f"].get(key, []):
            if use is None or use(v):
                lvs.append(sdb_tag(tag, slv))
    return max(lvs, key=lambda x: LV_RANK.get(x, 0))


def _family(rh, m, n, s):
    for src, val in (("RHS", rh and rh["f"].get("Family")), ("MBG", m and m["f"].get("Family", "").replace("Family:", "")),
                     ("NC State", n and n["f"].get("Family")), ("stauden.de", s and s["f"].get("Familienname") and s["f"]["Familienname"][0][0])):
        x = re.search(r"[A-Z][a-z]+(aceae|ae)\b", str(val or ""))
        if x:
            lat = x.group(0)
            return (f"{FAMILY_JA[lat]}（{lat}）" if lat in FAMILY_JA else lat) + f"（{src}）"
    return None


def _ph_soil(rh, n, nl, w):
    def fmt(ph_text, soil_text, src):
        ph = [ja for en, ja in PH if en in ph_text.lower()]
        so = list(dict.fromkeys(ja for en, ja in SOIL if en in soil_text.lower()))
        a = "酸性〜アルカリ性" if len(ph) == 3 else "〜".join(ph) if len(ph) == 2 and ph != ["酸性", "アルカリ性"] else "・".join(ph)
        out = "、".join(x for x in (a, "・".join(so)) if x)
        return f"{out}（{src}）" if out else None
    if rh and (rh["f"].get("pH") or rh["f"].get("_soil")):
        return fmt(rh["f"].get("pH", ""), rh["f"].get("_soil", ""), "RHS")
    if n and (n["f"].get("Soil pH") or n["f"].get("Soil Texture")):
        return fmt(n["f"].get("Soil pH", ""), n["f"].get("Soil Texture", ""), f"NC State・{nl}")
    if w and (w["f"].get("Soil pH") or w["f"].get("Soil Type")):
        return fmt(" ".join(w["f"].get("Soil pH", [])), " ".join(w["f"].get("Soil Type", [])), "Walters・品種")
    return None


def _fragrance(it, rh, m, mlv, n, nl, s, slv, w, ga, ga_own):
    ok = lambda lv: lv == "品種" or not it.get("品種名")
    parts, src, vague = [], [], []
    if rh and rh["f"].get("_frag"):
        f = rh["f"]["_frag"].lower()
        parts += [p for en, p in (("flower", "花"), ("foliage", "葉")) if en in f]
        src.append("RHS")
    if m and ok(mlv):
        mt = m["f"].get("Maintenance", "")
        fl = re.search(r"Flower: (.*?)(?= (?:Leaf|Attracts|Fruit|Other|Tolerate|Invasive):|$)", mt)
        lf = re.search(r"Leaf: (.*?)(?= (?:Attracts|Fruit|Other|Tolerate|Invasive):|$)", mt)
        got = [p for mm, p in ((fl, "花"), (lf, "葉")) if mm and "Fragrant" in mm.group(1)]
        if got:
            parts += got
            src.append("MBG")
    if n and ok(nl):
        got = [p for key, p in (("Flower Value To Gardener", "花"), ("Leaf Value To Gardener", "葉")) if "Fragrant" in n["f"].get(key, "")]
        if got:
            parts += got
            src.append("NC State")
    if w and any("Fragrant" in x for x in w["f"].get("Plant Uses & Characteristics", [])):
        vague.append("Walters")
    if ga and ga_own and ga[11].get("Duftend") == "ja":
        vague.append("Gaißmayer")
    if s and any("duft" in v.lower() for v, _ in s["f"].get("Eigenschaften", [])) and ok(sdb_lv(s, "Eigenschaften", slv, lambda v: "duft" in v.lower())):
        vague.append("stauden.de")
    parts = list(dict.fromkeys(parts))
    if parts:
        return ("花と葉" if len(parts) == 2 else parts[0]) + "（" + "・".join(dict.fromkeys(src)) + "）"
    if vague:
        return "あり（部位の記述なし。" + "・".join(vague) + "）"
    return None


def _toxicity(rh, n, nl, ga, je):
    if rh and rh["f"].get("Potentially harmful"):
        t = rh["f"]["Potentially harmful"]
        out = []
        for who, ja in (("Humans/Pets", "人・ペット"), ("Humans", "人"), ("Pets", "ペット")):
            mm = re.search(who + r"[^:]*: (.*?)(?=Humans|Pets|Wear|$)", t)
            if mm and not any(o.startswith(ja.split("・")[0]) for o in out if who != "Pets"):
                eff = [j for e, j in (("harmful if eaten", "食べると有害"), ("toxic if eaten", "食べると有毒"), ("skin", "皮膚にかぶれ・刺激"), ("eye", "目に刺激")) if e in mm.group(1).lower()]
                if eff:
                    out.append(f"{ja}：" + "、".join(eff))
        if out:
            return "／".join(dict.fromkeys(out)) + "（RHS）"
    if n and n["f"].get("Poison Severity"):
        sev = {"low": "弱い", "medium": "中くらい", "high": "強い"}.get(n["f"]["Poison Severity"].strip().lower(), n["f"]["Poison Severity"])
        parts = list(dict.fromkeys(p for e, p in PARTS if e in n["f"].get("Poison Part", "").lower()))
        return f"毒性 {sev}" + (f"（部位：{'・'.join(parts)}）" if parts else "") + f"（NC State・{nl}）"
    if ga and ga[11].get("Giftklasse"):
        g = ga[11]["Giftklasse"]
        return ("強い毒" if "stark" in g or "++" in g else "弱い毒" if "schwach" in g else "有毒") + f"（Gaißmayer の区分: {g}）"
    if je and "toxic plant" in je[11]:
        return "有毒（Jelitto）"
    return None


def _de_seed(x):
    x = x.lower()
    if re.search(r"keine selbstaussaat|steril", x):
        return 0
    if re.search(r"ohne (dabei |jemals )?lästig|nie lästig", x):  # 「じゃまにならない程度に」
        return 1 if re.search(r"selbstaussaat|versam|sät sich|aussaat|verwilder", x) else None
    if re.search(r"moderat|gelegentlich|mäßig", x) and re.search(r"selbstaussaat|versam|sät sich|aussaat", x):
        return 1
    if re.search(r"lästig|starke selbstaussaat|stark versam|versamt sich stark", x):
        return 3
    if re.search(r"oft selbstaussaat|reichlich|üppig|gut versamend|versamt sich (gern|gut|reich|willig)|reiche selbstaussaat|sät sich (gern|reich|stark)", x) and re.search(r"selbstaussaat|versam|sät sich|aussaat", x):
        return 2
    if re.search(r"selbstaussaat|versam|sät sich", x):
        return 1
    return None


def _de_rhiz(x):
    x = x.lower()
    if re.search(r"(nicht|kaum|ohne zu) wucher|wuchert (sie |er |es )?(aber |jedoch )?nicht|keine ausläufer|nicht ausläufer", x):
        return 0
    if re.search(r"wuchert weniger|kurze[nr]? (ausläufer|rhizom)|allmählich|langsam (ausbreitend|wachsend)", x) and re.search(r"ausläufer|rhizom|bestände|horst|wucher", x):
        return 1
    if re.search(r"wuchernd|wuchert|starker? ausbreitung|stark ausläufer|invasiv", x):
        return 3
    if re.search(r"ausläufer|rhizom(e|en)? |kriechend|bestände", x):
        return 2
    return None


def _en(sent):
    """英語の1文 → (こぼれ種のレベル, 地下茎のレベル)"""
    x = sent.lower().replace("\xa0", " ")
    sd = 0 if re.search(S0, x) else 3 if re.search(S3, x) else 2 if re.search(S2, x) else 1 if re.search(S1, x) else None
    rz = None
    seedy = bool(re.search(r"self-?(seed|sow)|reseed", x))
    under = bool(re.search(r"rhizom|stolon|runner|sucker|underground|creeping", x))
    if re.search(R1, x):
        rz = 1
    elif re.search(R0, x) and re.search(RW + r"|invasive|aggressive|clump", x) and not re.search(r"thought to be|once considered", x):
        # 「地下茎で広がるが、はびこらない」のように広がり方も書いてある文は 1、広がらないとだけ書いてある文は 0
        rz = 1 if re.search(R2, x) else 0
    elif re.search(R3, x) and not (seedy and not under):
        # 「can be invasive／aggressive」だけの文は、広がり方の語（spread・rhizome など）があるときだけ採る（属の一般的な注意や害虫の話を拾わない）
        if re.search(r"spread|rhizom|stolon|runner|sucker|underground|creeping|coloniz|ground ?cover|rampant", x):
            rz = 3
    elif re.search(R2, x) and not (seedy and not under):
        # 「rhizomatous, clump-forming」のように、地下茎はあるが株立ちと書いてある文は 1
        only_adj = not re.search(R2.replace("rhizomatous|stoloniferous|", ""), x)
        if only_adj and re.search(r"rhizomatous (crown|rootstock|root system|roots)", x) and not re.search(r"spread|coloniz|stolon", x):
            rz = None  # 2026-11-21: 「central rhizomatous crown」は株の中心の形の説明で、広がり方の記述ではない（ホスタ）
        else:
            rz = 1 if only_adj and re.search(r"clump", x) else 2
    if rz == 3 and sd is None and seedy:
        sd, rz = 3, None
    return sd, rz


def extra(it, rh, m, mlv, n, nl, s, slv, w, ga, ga_own, je, texts):
    r = {"科名": _family(rh, m, n, s), "pH・土質": _ph_soil(rh, n, nl, w), "香り": _fragrance(it, rh, m, mlv, n, nl, s, slv, w, ga, ga_own),
         "毒性": _toxicity(rh, n, nl, ga, je)}
    # こぼれ種・地下茎: 文献の順（NC State → MBG → Walters → stauden.de → Gaißmayer）で、最初に記述のあった文献の値を採る。同じ文献の中では大きい方
    cand = {"seed": [], "rhiz": []}
    for src in ("NC State", "MBG", "Walters"):
        for a, lv, sent in texts:
            if a == src and lv != "属":  # 属のページの一般的な記述は、広がり方の項目には使わない（RULES.md）
                sd, rz = _en(sent)
                if sd is not None:
                    cand["seed"].append((src, lv, sd, sent))
                if rz is not None:
                    cand["rhiz"].append((src, lv, rz, sent))
    if s:
        for key in ("Wuchsverhalten", "Pflegehinweis"):
            for v, tg in s["f"].get(key, []):
                for kind, fn in (("seed", _de_seed), ("rhiz", _de_rhiz)):
                    lv = fn(v)
                    if lv is not None and not (kind == "rhiz" and key == "Pflegehinweis"):
                        cand[kind].append(("stauden.de", sdb_tag(tg, slv), lv, v))
    if ga:
        glv = "品種" if ga_own else "種"
        for field, v in ga[12]:
            if field in ("self_seed", "spread_mode", "lifespan", "habit", "pruning"):
                sd = _de_seed(v) if field != "spread_mode" or "versam" in v.lower() or "aussaat" in v.lower() else None
                rz = _de_rhiz(v) if field in ("spread_mode", "habit") else None
                if sd is not None:
                    cand["seed"].append(("Gaißmayer", glv, sd, v))
                if rz is not None:
                    cand["rhiz"].append(("Gaißmayer", glv, rz, v))
    why = []
    for kind, col, lab in (("seed", "こぼれ種の量(0-3)", "こぼれ種"), ("rhiz", "地下茎で広がる程度(0-3)", "地下茎")):
        r[col] = None
        if cand[kind]:
            first = cand[kind][0][0]
            same = [c for c in cand[kind] if c[0] == first]
            best = max(same, key=lambda c: c[2])
            r[col] = best[2]
            why.append(f"[{lab} {best[2]}／{best[0]}・{best[1]}] {best[3][:220]}")
            other = sorted({(c[0], c[2]) for c in cand[kind] if c[0] != first and c[2] != best[2]})
            if other:
                why.append(f"[{lab}の食い違い] " + "、".join(f"{a} は {b} 相当" for a, b in other))
    # 2026-11-24 総当たりの読み直し（spread_reread.json。scripts/tools/spread_reread_note.md）: こぼれ種・地下茎の段階は、全916品種の文を読み直した値を使う。
    # 言い回しの照合の値と違えば、根拠に残す
    rr = SPREAD_RR.get(str(it.get("商品番号")))
    if rr:
        for col, lab, key in (("こぼれ種の量(0-3)", "こぼれ種", "こぼれ種"), ("地下茎で広がる程度(0-3)", "地下茎", "地下茎")):
            new = rr.get(key)
            if new != r[col]:
                why.append(f"[読み直し 2026-11-24] {lab}：言い回しの照合では {r[col] if r[col] is not None else '空欄'}、文を読み直して {new if new is not None else '空欄'}（{rr.get(key + 'の決め手') or '記述なし'}）")
            if new is not None:
                # 「[こぼれ種 3／NC State・種] 原文」の形にする（combine.py・six() が文献と段階〔種の記述か〕をここから読む）
                q = rr.get(key + "の決め手") or ""
                mq = re.match(r"\[([^・\]]+)・([^\]]+)\]\s*(.*)$", q, re.S)
                src_, lv_ = (mq[1], {"cultivar": "品種", "species": "種", "genus": "属"}.get(mq[2], mq[2])) if mq else ("読み直し", "不明")
                why.insert(0, f"[{lab} {new}／{src_}・{lv_}] {(mq[3] if mq else q)}（読み直し）"[:300])
            r[col] = new
    r["こぼれ種・地下茎の根拠"] = "\n".join(why) or None
    return r


# ---------- 夏前の切り戻し（管理タイプ C）と、毎年〜2年ごとの更新（管理タイプ D）。2026-11-21 ----------
# trial/RULES.md: C 夏前切戻型＝初夏に草丈を詰める・夏前に刈り込む、または夏に葉が傷むので切り戻す記述。D 毎年株更新型＝毎年〜2年ごとの株分け・植え替え・更新が必要と明記。
_BAD = r"declin|flop|sprawl|leggy|ragged|unsightly|tired|depreciat|scorch|tatter|untidy|open up|lodg|rangy|shabby|brown"
_NEW = r"rejuvenat|refresh|fresh (new )?(foliage|growth|leaves)|new (foliage|growth|leaves)|second flush of (foliage|leaves)|tidy"
_CUT = r"(shear(ed|ing)?|cut(ting)?|trim(med|ming)?|mow(ed|ing)?|clip(ped|ping)?)( them| it| plants?| foliage| stems| clumps)?( back| down| to the ground| to basal| hard| by (one-|a )?(half|third))"
C_EN = [
 _CUT + r"[^.]*(" + _BAD + "|" + _NEW + ")",
 r"(" + _BAD + r")[^.]*" + _CUT,
 r"chelsea chop|pinch(ed|ing)? (back|out)[^.]*(late spring|early summer|may|june)|" + _CUT + r"[^.]*(in|by|before|until) (late spring|early summer|may|june|mid-?summer|early july)[^.]*(height|compact|bush|flop|staking|delay|shorter|sturdier)",
 r"(in|by|before) (late spring|early summer|may|june)[^.]*" + _CUT + r"[^.]*(height|compact|bush|flop|staking|delay|shorter|sturdier)",
]
C_DE = r"vorblütenschnitt|chelsea chop|pinzier|(juni|juli|sommer|frühsommer)[^.]*(rückschnitt|zurückschneiden|zurückgeschnitten|einkürzen)|(rückschnitt|zurückschneiden|einkürzen)[^.]*(juni|juli|frühsommer|im sommer)"
C_JA = r"梅雨前|梅雨入り前|夏前|初夏に[^。]*切り|蒸れ[^。]*(切り戻|刈り込|透か)|(切り戻|刈り込)[^。]*(蒸れ|夏越し)"
D_EN = (r"(divid(e|ed|ing)|replac(e|ed|ing)|renew(ed|ing)?|replant(ed|ing)?|lift(ed|ing)? and divid\w+|coppic(e|ed|ing)|cut(ting)? (back )?(hard |all stems )?to (the |near (the )?)?ground)[^.]*"
        r"(every (year|1-2 years|1 to 2 years|one to two years|two years|2 years|other year|spring)|each (year|spring)|annually|yearly)"
        r"")
D_JA = r"(毎年|1〜2年ごと|1～2年ごと|2年ごと)[^。]*(株分け|植え替え|更新|挿し木で更新)|(株分け|植え替え|更新)[^。]*(毎年|1〜2年ごと|1～2年ごと)"


PRUNE_ANY = (r"cut(ting)? (back|down|to)|shear|deadhead|dead-head|prun(e|ing)|trim|remov\w+ (the )?(spent|faded|old|dead|flower)|spent flower|pinch|\bmow|low maintenance|"
             r"little (care|maintenance)|clean ?up|tidy|after (flowering|bloom)|divid|replant|renew|rejuvenat|coppic|rückschnitt|schneiden|schnitt|teilen|umpflanzen|pflege")


def prune_all(texts, rh, ga, ga_own, og, sh, s, slv):
    """管理タイプを人が読んで決めるための列: 切り戻し・手入れ・株分けに触れている文を、文献ごとに全部並べる（属のページは除く）"""
    out = []
    if rh:
        for key in ("Pruning", "Cultivation", "Propagation"):
            if rh["f"].get(key):
                out.append(f"[RHS・品種／{key}] " + rh["f"][key][:300])
    for a, lv, x in texts:
        if lv != "属" and re.search(PRUNE_ANY, x.lower().replace("\xa0", " ")):
            out.append(f"[{a}・{lv}] {x[:300]}")
    if s:
        for v, tg in s["f"].get("Pflegehinweis", []):
            if sdb_tag(tg, slv) != "属":  # 属のページの文は並べない（ほかの文献と同じ）
                out.append(f"[stauden.de・{sdb_tag(tg, slv)}] {v}")
    if ga:
        out += [f"[Gaißmayer・{'品種' if ga_own else '種'}／{field}] {v[:300]}" for field, v in ga[12] if field in ("pruning", "division", "lifespan", "self_seed", "spread_mode")]
    if og:
        olv = "品種" if og[3] == "cultivar" else "種"
        out += [f"[おぎはら・{olv}／{field}] {v}" for field, v in og[6] if field in ("pruning", "spread_mode", "self_seed", "lifespan")]
        if sh and sh.get("status") == "ok":
            out += [f"[おぎはら楽天・{olv}／{lab}] {sh[key]}" for key, lab in (("pruning", "剪定"), ("propagation", "増殖")) if sh.get(key)]
    return "\n".join(dict.fromkeys(out)) or None


def prune_extra(texts, rh, ga, ga_own, og, sh):
    """返すのは {"夏前の切り戻し", "毎年〜2年ごとの更新", "切り戻し・更新の根拠"}。属のページの記述は使わない"""
    c_hit, d_hit = [], []
    sents = [(a, lv, x) for a, lv, x in texts if lv != "属"]
    if rh:
        for key in ("Pruning", "Cultivation"):
            for x in re.split(r"(?<=[.;])\s+", rh["f"].get(key, "")):
                if x.strip():
                    sents.append(("RHS", "品種", x.strip()))
    for a, lv, x in sents:
        low = x.lower().replace("\xa0", " ")
        if any(re.search(pat, low) for pat in C_EN) and not re.search(r"in (late )?(fall|autumn|winter)|late winter|early spring|after (the first )?frost", low):
            c_hit.append((a, lv, x))
        if re.search(D_EN, low):
            d_hit.append((a, lv, x))
    if ga:
        glv = "品種" if ga_own else "種"
        for field, v in ga[12]:
            if field == "pruning" and re.search(C_DE, v.lower()):
                c_hit.append(("Gaißmayer", glv, v))
    ja = []
    if og:
        olv = "品種" if og[3] == "cultivar" else "種"
        ja += [("おぎはら", olv, v) for field, v in og[6] if field in ("pruning", "heat_humidity")]
        if sh and sh.get("status") == "ok" and sh.get("pruning"):
            ja.append(("おぎはら楽天", olv, sh["pruning"]))
    for a, lv, v in ja:
        if re.search(C_JA, v):
            c_hit.append((a, lv, v))
        if re.search(D_JA, v):
            d_hit.append((a, lv, v))
    why = [f"[夏前の切り戻し／{a}・{lv}] {x[:230]}" for a, lv, x in c_hit[:2]] + [f"[毎年〜2年ごとの更新／{a}・{lv}] {x[:230]}" for a, lv, x in d_hit[:2]]
    return {"夏前の切り戻し": ("あり（" + "・".join(dict.fromkeys(a for a, _, _ in c_hit)) + "）") if c_hit else None,
            "毎年〜2年ごとの更新": ("あり（" + "・".join(dict.fromkeys(a for a, _, _ in d_hit)) + "）") if d_hit else None,
            "切り戻し・更新の根拠": "\n".join(why) or None}


# ---------- 2026-11-21（続き）: 成株シルエット・葉の特徴・耐潮性・株分けの間隔・混植適性・広がりすぎの注意 ----------
# 決め方は trial/RULES.md（silhouette・foliage_features・salt・division_interval・mixing・invasive_note）。どれも言い回し・用語の照合なので、根拠の列を見て人が確かめる。
# 成株シルエット・葉の特徴は、品種のページ（品種名のない商品は種のページ）だけ（RULES.md）。種のページからの値は、別の列（…種の記述なら）に参考として出す。
SIL_ORDER = ("つる", "マット", "ドーム", "アーチ", "直立", "ロゼット", "株立ち")
SIL_EN = (
 ("つる", r"\bclimber|\bclimbing|\btwining|\bvine\b|\bvining"),
 ("マット", r"mat[- ]forming|forms? (a |an |dense |low |tight |thick |flat |spreading |evergreen |attractive )*(mat|carpet)s?\b|carpet(ing|-forming)|ground-?hugging|\bprostrate|trailing (stems|habit|perennial|ground ?cover|plant)|creeping (perennial|habit|ground ?cover|stems|evergreen|mat|plant|herb|shrub|thyme|form)|low,? spreading (mat|carpet|ground ?cover)"),
 ("ドーム", r"\bmound(s|ed|ing)?\b|cushion[- ](forming|plant|shaped)|(low|dense|tight|compact|neat|evergreen|rounded) cushion|forms? an? (\w+,? )*cushion|dome-?shaped (plant|clump|mound|habit|shrub)|domed? (habit|mound|clump|shrub|bush|form)|forms? a (neat |low |tight |dense |compact )*dome|rounded (clump|habit|mound|shrub|bush|form|plant|shape)|hummock|\bbun\b"),
 ("アーチ", r"arching (habit|stems|mound|clump|foliage|leaves|form|branches|canes|blades)|gracefully arch|fountain|cascading (habit|mound|stems|foliage)|weeping (habit|form|foliage)"),
 ("直立", r"upright (habit|clump|perennial|grower|growth|form|plant|shrub|grass|, (clump|bushy|narrow|vase|columnar))|upright[- ]growing|(stiffly|strongly|strictly|narrowly|very|rigidly) upright|erect (habit|perennial|clump|plant|form|growth)|columnar|narrow,? upright|upright,? narrow"),
 ("ロゼット", r"rosette"),
 ("株立ち", r"clump-?forming|\bbushy|\bshrub|vase-shaped|forms? (a |an |dense |tidy |large |upright |loose |tight |neat |compact |slowly[- ]spreading |bushy )*clumps?\b|multi-stemmed|\bclumping"),
)
SIL_NC = (("つる", ("Climbing",)), ("マット", ("Creeping", "Prostrate")), ("ドーム", ("Mounding", "Rounded")), ("アーチ", ("Arching", "Cascading", "Weeping")),
          ("直立", ("Erect", "Columnar")), ("株立ち", ("Clumping", "Multi-stemmed", "Vase", "Dense")))
SIL_DE = (("つる", r"kletternd"), ("マット", r"teppichartig|mattenartig|flächig|flach, ausgebreitet"), ("ドーム", r"kissenartig|polsterartig|halbkugelig"),
          ("直立", r"aufrecht bis straff aufrecht"), ("ロゼット", r"rosettenartig"), ("株立ち", r"buschig"))
SIL_RHS_SURE = (("つる", "Climbing"), ("マット", "Matforming"), ("マット", "Trailing"), ("直立", "Columnar upright"))
GRASS = r"Poaceae|Cyperaceae|Gramineae"


def sentences_(t):
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", t or "") if x.strip()]


def _sil_text(sent):
    low = sent.lower().replace("\xa0", " ")
    return [k for k, pat in SIL_EN if re.search(pat, low)]


def _silhouette(rh, m, mlv, n, nl, s, slv, w, family, cultivar_ok):
    """返すのは (値, 根拠)。cultivar_ok(lv) が真のページだけ使う。文献の順は RHS（はっきりした語）→ NC State → MBG → Walters → stauden.de → RHS（Clump forming・Bushy など）"""
    grass = bool(re.search(GRASS, family or ""))

    def fin(v, why):
        if grass and v in ("株立ち", "ドーム", "アーチ"):  # イネ科・カヤツリグサ科で、直立・マットと書かれていないものは グラス
            return "グラス", why + "／イネ科・カヤツリグサ科"
        return v, why
    hab = rh["f"].get("Habit", "") if rh else ""
    for v, word in SIL_RHS_SURE:
        if word in hab:
            return fin(v, f"[RHS・品種] Habit: {hab}")
    if n and cultivar_ok(nl):
        hf = [x.strip() for x in re.split(r"[;,]", n["f"].get("Habit/Form", "")) if x.strip()]
        for v, words in SIL_NC:
            if any(x in words for x in hf):
                return fin(v, f"[NC State・{nl}] Habit/Form: {'; '.join(hf)}")
    for lab, page, lv, keys in (("MBG", m, mlv, ("Noteworthy", "Culture")), ("Walters", w, "品種", None)):
        if not page or not cultivar_ok(lv):
            continue
        sents = sentences_(page["text"]) if keys is None else [x for key in keys for x in sentences_(page["f"].get(key, ""))]
        hits = [(k, x) for x in sents for k in _sil_text(x)]
        for v in SIL_ORDER:
            for k, x in hits:
                if k == v:
                    return fin(v, f"[{lab}・{lv}] {x[:200]}")
    if s and cultivar_ok(sdb_lv(s, "Wuchsform", slv)):
        wf = " / ".join(v for v, _ in s["f"].get("Wuchsform", []))
        for v, pat in SIL_DE:
            if re.search(pat, wf):
                return fin(v, f"[stauden.de・{sdb_lv(s, 'Wuchsform', slv)}] Wuchsform: {wf}")
    if hab:
        if grass:
            return "グラス", f"[RHS・品種] Habit: {hab}／イネ科・カヤツリグサ科"
        if re.search(r"Clump forming|Bushy|Tufted|Suckering|Spreading branched", hab):
            return "株立ち", f"[RHS・品種] Habit: {hab}"
    return None, None


LEAF_DE = {
 "Blatteigenschaften": (("glänzend", "光沢がある"), ("fein behaart", "細かい毛がある"), ("flaumig", "綿毛がある（フェルト状）"), ("wollig", "羊毛状の毛がある"), ("borstig", "剛毛がある"),
                        ("rauh", "ざらつく"), ("runzelig", "しわがある"), ("ledrig", "革質"), ("bereift", "白い粉をふく"), ("weich", "柔らかい"), ("starr", "硬い"), ("hart", "硬い"),
                        ("aromatisch", "葉に香りがある"), ("gefleckt", "斑点がある")),
 "Blattrand": (("tief eingeschnitten", "深く切れ込む"), ("eingeschnitten", "切れ込みがある"), ("spitzlappig", "浅く裂ける"), ("gelappt", "浅く裂ける"), ("gewellt", "縁が波打つ"),
               ("dornig", "縁にとげ状の鋸歯"), ("gesägt", "縁に鋸歯"), ("gezähnt", "縁に鋸歯"), ("gekerbt", "縁に丸い鋸歯"), ("bewimpert", "縁に毛がある")),
 "Blattspreite": (("gefiedert", "羽状の葉"), ("fiederteilig", "羽状に裂ける"), ("fingerförmig", "掌状の葉"), ("handförmig", "掌状の葉"), ("feinzerteilt", "細かく裂ける"),
                  ("fleischig", "多肉質")),
 "Blattform/-Umriss": (("grasartig", "草状の細い葉"), ("nadelartig", "針状の葉"), ("haarförmig", "糸状の葉"), ("herzförmig", "ハート形"), ("nierenförmig", "腎臓形"),
                       ("rund bis rundlich", "丸い葉"), ("schwertförmig", "剣状の葉"), ("schildförmig", "盾形"), ("riemen", "帯状の葉"), ("lineal", "線形の葉")),
 "Blattschmuck": (("zweifarbig", "2色の葉"), ("mehrfarbig", "多色の葉"), ("buntblättrig", "斑入り")),
}
LEAF_NC = {
 "Leaf Feel": (("Glossy", "光沢がある"), ("Velvety", "ビロード状"), ("Leathery", "革質"), ("Fleshy", "多肉質"), ("Waxy", "ろう質"), ("Rough", "ざらつく"), ("Soft", "柔らかい"), ("Prickly", "とげがある")),
 "Leaf Margin": (("Lobed", "裂ける"), ("Serrate", "縁に鋸歯"), ("Dentate", "縁に鋸歯"), ("Denticulate", "縁に鋸歯"), ("Crenate", "縁に丸い鋸歯"), ("Undulate", "縁が波打つ")),
 "Leaf Type": (("Compound", "複葉"), ("Needles", "針状の葉"), ("Fronds", "シダの葉")),
 "Leaf Shape": (("Cordate", "ハート形"), ("Linear", "線形の葉"), ("Orbicular", "丸い葉"), ("Palmatifid", "掌状に裂ける"), ("Palmasect", "掌状に裂ける"), ("Pinnatifid", "羽状に裂ける"),
                ("Pinnatisect", "羽状に裂ける"), ("Filiform", "糸状の葉"), ("Acicular", "針状の葉")),
}


def _leaf(n, nl, s, slv, cultivar_ok):
    out, src = [], []
    if s and cultivar_ok(sdb_lv(s, list(LEAF_DE), slv)):  # 葉の語の値に、種・属から引き継いだものが1つでもあれば、種（属）の記述として扱う
        got = []
        for key, pairs in LEAF_DE.items():
            vals = " / ".join(v for v, _ in s["f"].get(key, []))
            for de, ja in pairs:
                if de not in vals:
                    continue
                if de == "eingeschnitten" and "深く切れ込む" in got and "eingeschnitten" not in vals.replace("tief eingeschnitten", ""):
                    continue
                if de == "lineal" and "grasartig" in vals:
                    continue
                got.append(ja)
        if got:
            out += got
            src.append(f"stauden.de・{sdb_lv(s, list(LEAF_DE), slv)}")
    if n and cultivar_ok(nl):
        got = []
        for key, pairs in LEAF_NC.items():
            val = n["f"].get(key, "")
            got += [ja for en, ja in pairs if en in val]
        if got:
            out += got
            src.append(f"NC State・{nl}")
    out = list(dict.fromkeys(out))
    return ("、".join(out) + "（" + "／".join(src) + "）") if out else None


SALT_NO = r"not (very |particularly )?salt[- ]tolerant|intolerant of [^.]*salt|no salt tolerance|does not tolerate [^.]*salt|sensitive to [^.]*salt"
SALT_LOW = r"(low|poor|little|limited) (salt|tolerance (to|of|for) salt)|salt tolerance is (low|poor)"
SALT_MID = r"(slightly|moderately|somewhat|fairly|mildly) (salt|tolerant of salt)|(some|moderate|slight|medium) (salt|tolerance (to|of|for) salt)|low levels of salt|salt tolerance is moderate"
SALT_YES = (r"salt[- ]tolerant|tolerat\w+ [^.]*\bsalt|tolerant of [^.]*\bsalt|salt[- ](spray|resistant|tolerance)|resist\w+ [^.]*\bsalt|withstands? [^.]*\bsalt|seaside (garden|planting|location|condition)|"
            r"coastal (garden|planting|condition|exposure|site)|cope in coastal|sea-salt|road salt|salzverträglich")


def _salt(texts, rh, n, nl, w, ga, ga_own, og):
    """RULES.md の salt。◎＝塩に耐える・海辺に向くと明記、○＝ある程度、または項目だけ（NC State の Resistance の Salt・植える場所の Coastal、RHS の植える場所の Coastal）、△＝弱い、×＝耐えない"""
    hits = []
    sents = [(a, lv, x) for a, lv, x in texts if lv != "属"]
    if rh:
        sents += [("RHS", "品種", x) for x in sentences_(rh["f"].get("Cultivation", ""))]
    if ga:
        sents += [("Gaißmayer", "品種" if ga_own else "種", v) for _, v in ga[12]]
    for a, lv, x in sents:
        low = x.lower().replace("\xa0", " ")
        g = "×" if re.search(SALT_NO, low) else "△" if re.search(SALT_LOW, low) else "○" if re.search(SALT_MID, low) else "◎" if re.search(SALT_YES, low) else None
        if g:
            hits.append((g, a, lv, x))
    if og:
        for field, v in og[6]:
            if field == "salt" or re.search(r"耐潮性があ|潮風に強|海辺に向|海岸でも", v):
                hits.append(("◎", "おぎはら", "品種" if og[3] == "cultivar" else "種", v))
    if hits:
        for g in ("×", "△", "○", "◎"):  # 文が割れたら控えめな側
            for h in hits:
                if h[0] == g:
                    return g, f"[{h[1]}・{h[2]}] {h[3][:220]}"
    tags = []
    if n and nl != "属":
        if "Salt" in [t.strip() for t in n["f"].get("Resistance To Challenges", "").split(";")]:
            tags.append(f"NC State・{nl} の Resistance To Challenges: Salt")
        if "Coastal" in n["f"].get("Landscape Location", ""):
            tags.append(f"NC State・{nl} の Landscape Location: Coastal")
    if rh and rh["f"].get("_coastal"):
        tags.append("RHS の植える場所: Coastal")
    if w and any("salt" in x.lower() for x in w["f"].get("Plant Uses & Characteristics", [])):
        tags.append("Walters の項目: " + "・".join(x for x in w["f"]["Plant Uses & Characteristics"] if "salt" in x.lower()))
    if tags:
        return "○", "[項目だけ。本文の記述はない] " + "／".join(tags)
    return None, None


NUM = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "other": 2}
_N = r"(\d+|one|two|three|four|five|six)"
DIV_INT = (r"every " + _N + r"(?:\s*(?:-|–|to|or)\s*" + _N + r")? years", r"every (second|third|fourth|fifth|other) year", r"every (few|several|couple of) years")
DIV_WORD = r"divid|division|lift and|replant"
SEASON = (("early spring", "早春"), ("late spring", "晩春"), ("spring", "春"), ("late summer", "晩夏"), ("early fall", "初秋"), ("early autumn", "初秋"), ("fall", "秋"), ("autumn", "秋"),
          ("after flowering", "花後"), ("after bloom", "花後"))


def _seasons(low):
    out, rest = [], low
    for en, ja in SEASON:
        if re.search(r"\b" + en + r"\b", rest):
            out.append(ja)
            rest = re.sub(r"\b" + en + r"\b", " ", rest)
    order = ["早春", "春", "晩春", "花後", "晩夏", "初秋", "秋"]
    return "または".join(sorted(dict.fromkeys(out), key=order.index))


def _division(texts, rh, w, s, slv):
    """RULES.md の division_interval。「○年ごと」の記述のある文を先に採り、なければ株分けの時期だけ（間隔の記載なし）。文献の順は RHS → NC State → MBG → Walters → stauden.de"""
    sents = []
    if rh:
        for key in ("Propagation", "Cultivation"):
            sents += [("RHS", "品種", x) for x in re.split(r"(?<=[.;])\s+", rh["f"].get(key, "")) if x.strip()]
    for src in ("NC State", "MBG", "Walters"):
        sents += [(a, lv, x) for a, lv, x in texts if a == src and lv != "属"]
    season_only = None
    for a, lv, x in sents:
        low = x.lower().replace("\xa0", " ")
        if not re.search(r"divid|division", low):
            continue
        val = None
        m1 = re.search(DIV_INT[0], low)
        m2 = re.search(DIV_INT[1], low)
        m3 = re.search(DIV_INT[2], low)
        if m1:
            a1 = int(m1.group(1)) if m1.group(1).isdigit() else NUM[m1.group(1)]
            b1 = m1.group(2) and (int(m1.group(2)) if m1.group(2).isdigit() else NUM[m1.group(2)])
            val = f"{a1}〜{b1}年ごと" if b1 else f"{a1}年ごと"
        elif m2:
            val = f"{NUM[m2.group(1)]}年ごと"
        elif m3:
            val = "数年ごと"
        elif re.search(r"divid\w* [^.]*(every|each) (year|spring)|divid\w* (annually|yearly)", low):
            val = "毎年"
        se = _seasons(low)
        if val:
            return val + (f"、{se}" if se else "") + f"（{a}・{lv}）", f"[{a}・{lv}] {x[:220]}"
        if se and not season_only:
            season_only = (f"{se}（間隔の記載なし。{a}・{lv}）", f"[{a}・{lv}] {x[:220]}")
    if s:
        for v, tg in s["f"].get("Pflegehinweis", []):
            if "zwei- bis vierjährigem" in v:
                return f"2〜4年ごと（stauden.de・{sdb_tag(tg, slv)}）", f"[stauden.de・{sdb_tag(tg, slv)}] {v}"
        for v, tg in s["f"].get("Pflegehinweis", []):
            if "nicht umpflanzen" in v:
                return ((season_only[0] + "。" if season_only else "") + f"長生きで、長年植え替えない方がよい（stauden.de・{sdb_tag(tg, slv)}）",
                        f"[stauden.de・{sdb_tag(tg, slv)}] {v}" + ("\n" + season_only[1] if season_only else ""))
    return season_only or (None, None)


MIX_STRONG = (r"vigorous(ly)? spread|spreads? (vigorously|quickly|rapidly)|rapid(ly)? spread|can (crowd|overwhelm|overrun|smother|out-?compete|choke)|(crowd|choke)s? out (other|neighbo|native|less)|"
              r"overwhelm (other|neighbo|small|less)|smother (other|neighbo|small|less)|(needs?|give it|given) (plenty of |lots of |ample )?(room|space) to spread")
# invasive／aggressive の明記（RULES.md の mixing: 侵略的）。打ち消し（not invasive、less aggressive など）と、ほかの植物の話は外す
MIX_INV = (r"(is|are|be|become|becoming|considered|regarded as|listed as|classed as|labeled it|classified as) (an? |highly |very |quite |extremely |potentially |somewhat |a bit |too |both persistent and )*\"?(invasive|aggressive|noxious)|(is|are) an? (\w+, )+(aggressive|invasive)|"
           r"(spreads?|spread|naturalizes|reseeds?|self-seeds?)(,| to| can)? (too |somewhat |sometimes |very |so )*(aggressively|invasively)|(aggressively|invasively) (spread|self-seed|reseed)|"
           r"aggressive (spread|weed|nature|plant|grower|colon)|invasive (species|weed|spread|plant|nature)|noxious weed|too aggressive|weedy and invasive|point of being (somewhat )?(aggressive|invasive)")
# 「weedy」だけの文は 侵略的 にしない（NC State の表示 Weedy は、注意に書く）
MIX_NEG = (r"not (considered |be |become |as |too |overly |terribly |generally |a |try )*(to be )?(invasive|aggressive|weedy|to take over)|non-(invasive|aggressive)|less (aggressive|invasive|weedy)|without being invasive|"
           r"not a threat|isn.t considered|does not spread (as )?aggressively|not spread aggressively|although not invasive|than the weedy|aggressive harvesting|as (are|is) some other|as is the (case|related)|"
           r"unlike some|is not invasive|not aggressive|invasive plant resources|many species are|green-leaved species|red form is not|the green form|like liriope spicata|infamous|"
           r"without becoming|not inclined to|not to be confused|threat is low|not (generally )?considered")
# 地域の話（米国の州・オーストラリアなどで侵略的外来種とされている、という記述）。庭での広がり方ではないので、混植適性は決めず、注意にだけ書く
#   （試作のススキ 'Morning Light' は 普通、スピレア 'Goldflame' は空欄だった）
MIX_ECO = (r"\bstates?\b|north carolina|australia|new zealand|\bareas\b|regions?\b|parts of|council|listed|u\.s\.|united states|climates|virginia|great lakes|natural areas|"
           r"native (plants|species|vegetation)|some sources|federal|usda|worst weed")
MIX_HEDGE = r"somewhat|a bit|a little|sometimes|potentially|\bmay\b|perhaps|probably|optimum|optimal|at times|under the right conditions|if (grown|planted) in"
SEEDY = r"self-?seed|reseed|\bseeds?\b"
ROOTY = r"rhizom|stolon|runner|sucker|creeping|underground|stems? root|vin(e|ing)|climb"
MIX_WEAK = r"weak grower|easily (overwhelmed|crowded out|out-?competed|overrun|swamped)|poor competitor|does not compete well|konkurrenzschwach|resents competition"
MBG_NOTICE = (("Federal Noxious Weed", "米国の連邦有害雑草法の指定種（MBG の注意書き）"), ("Missouri Noxious Weed", "米国ミズーリ州で有害雑草に指定され、栽培・販売できない（MBG の注意書き）"),
              ("noxious weed in one or more Midwestern", "米国中西部の州で有害雑草に指定（MBG の注意書き）"),
              ("weedy and potentially invasive", "雑草化しやすく侵略的になるおそれがあり、米国中西部の庭には勧めない（MBG の注意書き）"))


def _ev(why, lab, n_):
    """こぼれ種・地下茎の根拠の文字列から、[地下茎 3／MBG・種] の (文献, レベル) を取り出す"""
    g = re.search(r"\[" + lab + " " + str(n_) + r"／([^\]・]*)・([^\]]*)\]", why)
    return (g.group(1), g.group(2)) if g else ("", "")


def six(it, rh, m, mlv, n, nl, s, slv, w, ga, ga_own, og, sh, texts, base):
    """base は extra() の結果（科名・こぼれ種・地下茎の値と根拠）。返すのは、6列とその根拠・参考の列"""
    own = lambda lv: lv == "品種" or not it.get("品種名")
    anyl = lambda lv: lv in ("品種", "種")
    r = {}
    sil, sil_why = _silhouette(rh, m, mlv, n, nl, s, slv, w, base.get("科名"), own)
    r["成株シルエット"] = sil
    ref = ref_why = None
    if not sil:
        ref, ref_why = _silhouette(None, m, mlv, n, nl, s, slv, None, base.get("科名"), anyl)
    r["成株シルエット（種の記述なら）"] = ref
    r["成株シルエットの根拠"] = sil_why or (ref_why and "（種の記述）" + ref_why)
    r["葉の特徴"] = _leaf(n, nl, s, slv, own)
    r["葉の特徴（種の記述なら）"] = None if r["葉の特徴"] else _leaf(n, nl, s, slv, anyl)
    r["耐潮性"], r["耐潮性の根拠"] = _salt(texts, rh, n, nl, w, ga, ga_own, og)
    r["株分けの間隔"], r["株分けの間隔の根拠"] = _division(texts, rh, w, s, slv)
    # --- 混植適性・広がりすぎの注意
    why = base.get("こぼれ種・地下茎の根拠") or ""
    rz, sd = base.get("地下茎で広がる程度(0-3)"), base.get("こぼれ種の量(0-3)")
    cv = bool(it.get("品種名"))
    notes, mix, mix_why = [], None, []
    sp_note = "（種についての記述。この品種で同じかは未確認）"
    if rz is not None and rz >= 2:
        a, lv = _ev(why, "地下茎", rz)
        notes.append(("地下茎・ランナーで強く広がり、はびこることがある" if rz == 3 else "地下茎・ランナーでよく広がる") + f"（{a}・{lv}）" + (sp_note if cv and lv == "種" else ""))
    if sd is not None and sd >= 2:
        a, lv = _ev(why, "こぼれ種", sd)
        notes.append(("こぼれ種で強く増え、雑草化することがある" if sd == 3 else "こぼれ種でよく増える") + f"（{a}・{lv}）" + (sp_note if cv and lv == "種" else ""))
    seed3 = (sd or 0) >= 3 and not (cv and _ev(why, "こぼれ種", 3)[1] == "種")
    strong = weak = inv = inv_seed = eco = None
    pool = [(a, lv, x) for a, lv, x in texts if lv != "属"] + ([("Gaißmayer", "品種" if ga_own else "種", v) for _, v in ga[12]] if ga else [])
    for a, lv, x in pool:
        low = x.lower().replace("\xa0", " ")
        if re.search(MIX_INV, low) and not re.search(MIX_NEG, low):
            if re.search(MIX_ECO, low):
                eco = eco or f"[{a}・{lv}] {x[:200]}"
            elif cv and not re.search(ROOTY, low) and (re.search(SEEDY, low) or lv == "種"):
                # 種のページの「侵略的」で、地下茎・ランナーなど広がり方の語がない文も同じ扱い（ススキの品種。試作の 'Morning Light' は 普通 だった）
                # こぼれ種によるもの: 品種でも同じかは分からないので、混植適性は決めず、注意にだけ書く（スピレア 'Goldflame' の決定と同じ考え方。品種のページでも、種についての文のことが多い）
                inv_seed = inv_seed or f"[{a}・{lv}] {x[:200]}"
            elif re.search(MIX_HEDGE, low):
                strong = strong or f"[{a}・{lv}] {x[:200]}"
            else:
                inv = inv or f"[{a}・{lv}] {x[:200]}"
        if not strong and re.search(MIX_STRONG, low) and not re.search(r"crowds? out (most |garden )*weeds|not spread|" + MIX_NEG, low):
            strong = f"[{a}・{lv}] {x[:200]}"
        if not strong and re.search(r"difficult to (remove|eradicate|contain)", low) and re.search(r"sucker|rhizom|stolon|runner", low):
            strong = f"[{a}・{lv}] {x[:200]}"
        if not weak and re.search(MIX_WEAK, low):
            weak = f"[{a}・{lv}] {x[:200]}"
    if inv:
        notes.append("文献に「侵略的・はびこる」という記述がある（" + inv[1:inv.index("]")] + "）" + (sp_note if cv and "・種]" in inv[:inv.index("]") + 1] else ""))
    elif strong and re.search(MIX_INV, strong.lower()):
        notes.append("文献に「条件によっては、はびこる」という記述がある（" + strong[1:strong.index("]")] + "）" + (sp_note if cv and "・種]" in strong[:strong.index("]") + 1] else ""))
    if inv_seed:
        notes.append("こぼれ種などではびこる、という記述がある（" + inv_seed[1:inv_seed.index("]")] + "）。この品種で同じかは未確認")
    if eco:
        notes.append("地域によっては侵略的外来種とされている、という記述がある（" + eco[1:eco.index("]")] + "）" + (sp_note if cv and "・種]" in eco[:eco.index("]") + 1] else ""))
    if n and nl != "属":
        ptag = [x.strip() for x in n["f"].get("Problems", "").split(";")]
        got = [ja for en, ja in (("Invasive Species", "Invasive Species（米国ノースカロライナ州で侵略的外来種）"), ("Weedy", "Weedy（雑草化しやすい）")) if en in ptag]
        if got:
            notes.append(f"NC State・{nl} の表示: " + "・".join(got) + (sp_note if cv and nl == "種" else ""))
    wv = [v for v, _ in s["f"].get("Wuchsverhalten", [])] if s else []
    ws = [v for v, _ in s["f"].get("Wuchsstärke", [])] if s else []
    if "wuchernd" in ws:
        wlv = sdb_lv(s, "Wuchsstärke", slv, lambda v: v == "wuchernd")
        strong = strong or f"[stauden.de・{wlv}] Wuchsstärke: wuchernd"
        notes.append(f"生育が強く、はびこる（stauden.de・{wlv} の Wuchsstärke: wuchernd）" + (sp_note if cv and wlv == "種" else ""))
    horst_only = bool(wv) and any("horst" in v for v in wv) and not any(re.search("ausläufer|rhizom|kriechend", v) for v in wv)
    if (rz or 0) >= 3 or seed3:
        mix = "侵略的（隔離推奨）"
        mix_why.append("地下茎かこぼれ種が 3（こぼれ種・地下茎の根拠の列）")
    elif inv:
        mix = "侵略的（隔離推奨）"
        mix_why.append(inv)
    elif strong:
        mix = "強い（周囲を圧迫、配置注意）"
        mix_why.append(strong)
    elif weak:
        mix = "弱い（埋もれやすい）"
        mix_why.append(weak)
    elif (rz in (0, 1) or (rz is None and horst_only)) and (sd or 0) < 3 and not inv_seed:
        mix = "普通（混植可）"
        mix_why.append("地下茎 0〜1（こぼれ種・地下茎の根拠の列）" if rz in (0, 1) else f"[stauden.de・{sdb_lv(s, 'Wuchsverhalten', slv)}] Wuchsverhalten: " + " / ".join(wv))
    if m and m["f"].get("Notice"):
        for en, ja in MBG_NOTICE:
            if en in m["f"]["Notice"]:
                notes.append(ja + (sp_note if cv and mlv == "種" else ""))
                break
    elif m and m["f"].get("InvasiveLink"):
        notes.append("米国内に侵略的とされている地域がある（MBG の表示）" + (sp_note if cv and mlv == "種" else ""))
    if sh and sh.get("status") == "ok" and "外来" in (sh.get("pests") or ""):
        notes.append("おぎはら楽天の注意書き: " + re.sub(r"^.*?ご注意\s*", "", sh["pests"])[:120])
    r["混植適性"] = mix
    r["混植適性の根拠"] = "\n".join(mix_why + [x for x in (inv_seed, eco) if x]) or None
    r["広がりすぎの注意"] = "。".join(notes) or None
    return r
