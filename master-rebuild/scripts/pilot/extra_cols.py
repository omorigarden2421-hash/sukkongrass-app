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
    if s and ok(slv) and any("duft" in v.lower() for v, _ in s["f"].get("Eigenschaften", [])):
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
            for v, _ in s["f"].get(key, []):
                for kind, fn in (("seed", _de_seed), ("rhiz", _de_rhiz)):
                    lv = fn(v)
                    if lv is not None and not (kind == "rhiz" and key == "Pflegehinweis"):
                        cand[kind].append(("stauden.de", slv, lv, v))
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
    r["こぼれ種・地下茎の根拠"] = "\n".join(why) or None
    return r
