"""まとめの表（全916品種）で、項目どうしの食い違い（矛盾）を総当たりで探す（2026-11-24）。
使い方（master-rebuild で）: python -X utf8 scripts/tools/mujun_check.py <まとめの表.xlsx> mujun.json
見るもの:
  A 決め方どおりか（ほかの列から決まる列が、決め方と合っているか。仕組みの誤りを見つける）
  B 意味の食い違い（別々の文献から来た列どうしが、ありえない組み合わせになっていないか）
  C 同じ種・同じ属の中でのばらつき（種や属で決まるはずの値が、品種ごとに違わないか）
  D 今のマスターの値との違い（花色・葉色）
出力: 調べ方ごとに、当たった品種（商品番号・植物名・関係する列の値）
"""
import collections
import json
import re
import sys

import openpyxl

SRC, OUT = sys.argv[1], sys.argv[2]
rows = list(openpyxl.load_workbook(SRC, read_only=True).worksheets[0].iter_rows(values_only=True))
H = rows[1]
R = [dict(zip(H, r)) for r in rows[2:] if r[0] is not None]


def v(x, c):
    s = x.get(c)
    return None if s in (None, "") else str(s)


def bare(s):
    """「落葉（RHS）」→「落葉」"""
    return re.sub(r"（.*$", "", s) if s else s


def lvl(x, c):
    s = v(x, c)
    return int(s) if s and s.isdigit() else None


checks = collections.OrderedDict()


def add(key, title, kind, x, cols, why=None):
    e = checks.setdefault(key, {"調べ方": title, "種類": kind, "品種": []})
    e["品種"].append({"商品番号": x["商品番号"], "植物名": x["植物名"], "学名": x["学名（正名）"],
                     "値": {c: v(x, c) for c in cols}, **({"メモ": why} if why else {})})


SUN_SHADE = ("半日陰", "明るい日陰", "日陰")
for x in R:
    sun, heat, dr, west = v(x, "日照"), v(x, "耐暑性"), v(x, "乾燥耐性"), v(x, "西日耐性")
    muggy = v(x, "蒸れ耐性")
    rz, sd = lvl(x, "地下茎で広がる程度(0-3)"), lvl(x, "こぼれ種の量(0-3)")
    mix, mt = v(x, "混植適性") or "", v(x, "管理タイプ") or ""
    modes = v(x, "増え方") or ""
    risk, tags, dz = v(x, "リスクタグ") or "", v(x, "機能用途タグ") or "", v(x, "デザイン系タグ") or ""
    fc, sil = v(x, "葉色（分類）"), v(x, "成株シルエット")
    h1 = lvl(x, "草丈 最大(cm)")
    use = v(x, "景観構成用途") or ""
    soil = v(x, "土壌水分")
    cut = v(x, "切り戻しの方法") or ""
    # ---- A 決め方どおりか
    WC = ["日照", "耐暑性", "乾燥耐性", "西日耐性"]
    if sun in SUN_SHADE and west in ("◎", "○", "△"):
        add("A西日1", "日照が半日陰・日陰なのに、西日耐性が × でない", "A", x, WC)
    if west == "◎" and not (heat == "強" and dr == "強" and (sun or "").startswith("日向")):
        add("A西日2", "西日耐性 ◎ なのに、日向・耐暑性 強・乾燥耐性 強 がそろっていない", "A", x, WC)
    if heat == "弱" and west in ("◎", "○"):
        add("A西日3", "耐暑性 弱 なのに、西日耐性が ◎・○", "A", x, WC)
    if heat is None and west in ("◎", "○"):
        add("A西日4", "耐暑性が空欄なのに、西日耐性が ◎・○", "A", x, WC)
    if rz is not None and rz >= 3 or sd is not None and sd >= 3:
        if not mix.startswith("侵略的"):
            add("A混植1", "地下茎かこぼれ種が 3 なのに、混植適性が「侵略的」でない", "A", x, ["地下茎で広がる程度(0-3)", "こぼれ種の量(0-3)", "混植適性", "管理タイプ"])
    if mix.startswith("普通") and ((rz or 0) >= 2 or (sd or 0) >= 2):
        add("A混植2", "混植適性が「普通」なのに、地下茎かこぼれ種が 2 以上", "A", x, ["地下茎で広がる程度(0-3)", "こぼれ種の量(0-3)", "混植適性", "混植適性の根拠"])
    if mt.startswith("E") != mix.startswith("侵略的"):
        add("A管理1", "管理タイプ E（隔離推奨型）と、混植適性「侵略的」が合わない", "A", x, ["管理タイプ", "混植適性", "地下茎で広がる程度(0-3)", "こぼれ種の量(0-3)"])
    need_risk = mt.startswith("E") or mix.startswith(("侵略的", "強い"))
    if need_risk != ("要管理（広がりやすい）" in risk):
        add("A管理2", "リスクタグ「要管理（広がりやすい）」と、管理タイプ・混植適性が合わない", "A", x, ["リスクタグ", "管理タイプ", "混植適性"])
    if (muggy == "弱") != ("管理難" in risk):
        add("A管理3", "リスクタグ「管理難」と、蒸れ耐性 弱 が合わない", "A", x, ["リスクタグ", "蒸れ耐性"])
    if mt.startswith("B") and "花後" not in cut:
        add("A切戻1", "管理タイプ B（花後刈込型）なのに、切り戻しの方法に「花後」がない", "A", x, ["管理タイプ", "切り戻しの方法", "切り戻し時期（広尾町）"])
    if "不要" in cut and mt[:1] in ("B", "C"):
        add("A切戻2", "切り戻しの方法が「不要」なのに、管理タイプが B・C", "A", x, ["管理タイプ", "切り戻しの方法"])
    if cut and v(x, "切り戻し時期（広尾町）") is None:
        add("A切戻3", "切り戻しの方法があるのに、切り戻し時期（広尾町）が空欄", "A", x, ["切り戻しの方法", "切り戻し時期（広尾町）"])
    if h1:
        want = "前景" if h1 <= 40 else "中景" if h1 < 90 else "後景"
        if want not in use:
            add("A景観1", "草丈と、景観構成用途（前景〜40・中景〜90・後景）が合わない", "A", x, ["草丈 最大(cm)", "景観構成用途"])
    tsun = (sun or "").replace("明るい日陰", "半日陰")
    if (tsun in ("半日陰", "日陰")) != ("日陰庭向き" in tags) or (tsun == "日向〜半日陰") != ("半日陰でも可" in tags):
        add("Aタグ1", "日照と、機能用途タグ（日陰庭向き・半日陰でも可）が合わない", "A", x, ["日照", "機能用途タグ"])
    for f, t in (("シルバー系", "シルバーリーフ"), ("パープル・ブラック系", "黒葉アクセント"), ("斑入り", "斑入り葉")):
        if (fc == f) != (t in dz):
            add("Aタグ2", "葉色と、デザイン系タグ（シルバーリーフ・黒葉アクセント・斑入り葉）が合わない", "A", x, ["葉色（分類）", "デザイン系タグ"])
    if (dr == "強") != ("乾燥地向き" in tags):
        add("Aタグ3", "乾燥耐性 強 と、機能用途タグ「乾燥地向き」が合わない", "A", x, ["乾燥耐性", "機能用途タグ"])
    # 増え方と、こぼれ種・地下茎の段階
    if "こぼれ種" in modes and sd == 0:
        add("A増え方1", "増え方に「こぼれ種」があるのに、こぼれ種の量が 0", "A", x, ["増え方", "こぼれ種の量(0-3)", "こぼれ種・地下茎の根拠"])
    if (sd or 0) >= 2 and "こぼれ種" not in modes:
        add("A増え方2", "こぼれ種の量が 2 以上なのに、増え方に「こぼれ種」がない", "A", x, ["増え方", "こぼれ種の量(0-3)", "こぼれ種・地下茎の根拠"])
    if re.search("地下茎|ランナー", modes) and rz == 0:
        add("A増え方3", "増え方に「地下茎・ランナー」があるのに、地下茎で広がる程度が 0", "A", x, ["増え方", "地下茎で広がる程度(0-3)", "こぼれ種・地下茎の根拠"])
    if (rz or 0) >= 2 and modes and not re.search("地下茎|ランナー", modes):
        add("A増え方4", "地下茎で広がる程度が 2 以上なのに、増え方が「株立ち」だけ", "A", x, ["増え方", "地下茎で広がる程度(0-3)", "こぼれ種・地下茎の根拠"])
    # ---- B 意味の食い違い
    if soil == "乾燥寄り" and dr == "弱":
        add("B水1", "土壌水分が「乾燥寄り」なのに、乾燥耐性 弱", "B", x, ["土壌水分", "乾燥耐性", "乾燥耐性の出どころ"])
    if soil == "湿潤寄り" and dr == "強":
        add("B水2", "土壌水分が「湿潤寄り」なのに、乾燥耐性 強", "B", x, ["土壌水分", "乾燥耐性", "乾燥耐性の出どころ"])
    if heat == "弱" and muggy == "強":
        add("B暑1", "耐暑性 弱 なのに、蒸れ耐性 強", "B", x, ["耐暑性", "蒸れ耐性", "耐暑性の決め方", "暑さ・蒸れ・西日の根拠"])
    if heat == "強" and muggy == "弱":
        add("B暑2", "耐暑性 強 なのに、蒸れ耐性 弱（ありうるが、目立つ組み合わせ）", "B", x, ["耐暑性", "蒸れ耐性", "耐暑性の決め方", "暑さ・蒸れ・西日の根拠"])
    lo, hi = lvl(x, "USDA 下限"), lvl(x, "USDA 上限")
    if lo and hi and lo > hi:
        add("B寒1", "USDA 下限が上限より大きい", "B", x, ["USDA 下限", "USDA 上限"])
    rhs = v(x, "RHS 耐寒性")
    if lo and rhs and (rhs in ("H7", "H6") and lo >= 7 or rhs in ("H1a", "H1b", "H1c", "H2", "H3") and lo <= 5):
        add("B寒2", "USDA 下限と RHS 耐寒性が大きく食い違う", "B", x, ["USDA 下限", "RHS 耐寒性", "耐寒性"])
    ev = bare(v(x, "常緑性"))
    if ev == "常緑" and "落葉" in (v(x, "紅葉・冬の葉") or ""):
        add("B葉1", "常緑なのに、紅葉・冬の葉に落葉の記述", "B", x, ["常緑性", "紅葉・冬の葉"])
    if sil == "マット" and h1 and h1 >= 60:
        add("B形1", "成株シルエットが「マット」なのに、草丈が 60cm 以上", "B", x, ["成株シルエット", "草丈 最大(cm)", "成株シルエットの根拠"])
    if sil == "グラス" and not re.search(r"Poaceae|Cyperaceae|Juncaceae|Restionaceae|Typhaceae|Asparagaceae|Liliaceae|Iridaceae", v(x, "科名") or ""):
        add("B形2", "成株シルエットが「グラス」なのに、イネ科・カヤツリグサ科などではない", "B", x, ["成株シルエット", "科名", "成株シルエットの根拠"])
    if re.search(r"Poaceae|Cyperaceae", v(x, "科名") or "") and sil and sil not in ("グラス", "直立", "マット", "アーチ"):
        add("B形3", "イネ科・カヤツリグサ科なのに、成株シルエットが グラス・直立・マット・アーチ 以外", "B", x, ["成株シルエット", "科名", "成株シルエットの根拠"])
    if v(x, "外来種リスト") and v(x, "外来種リスト") != "掲載なし" and not (mt.startswith("E") or mix.startswith(("侵略的", "強い")) or "要管理" in risk):
        add("B外来1", "外来種リストに載っているのに、要管理・隔離推奨のどれでもない", "B", x, ["外来種リスト", "管理タイプ", "混植適性", "リスクタグ"])
    if v(x, "耐潮性") == "×" and "海辺向き" in tags:
        add("B潮1", "耐潮性 × なのに「海辺向き」", "B", x, ["耐潮性", "機能用途タグ"])

# ---- C 同じ種・同じ属の中でのばらつき
by_sp, by_g = collections.defaultdict(list), collections.defaultdict(list)
for x in R:
    g, ep = v(x, "属"), v(x, "種小名")
    if g:
        by_g[g].append(x)
    if g and ep:
        by_sp[(g, ep)].append(x)


def spread(groups, col, key, title, norm=bare):
    for k, xs in groups.items():
        vals = {norm(v(x, col)) for x in xs if v(x, col)}
        if len(vals) > 1:
            e = checks.setdefault(key, {"調べ方": title, "種類": "C", "品種": []})
            e["品種"].append({"まとまり": " ".join(k) if isinstance(k, tuple) else k,
                             "値ごと": {val: [f"{x['商品番号']} {x['植物名']}" for x in xs if norm(v(x, col)) == val] for val in sorted(vals)}})


spread(by_g, "科名", "C科名", "同じ属で科名が違う", norm=lambda s: re.sub(r"（RHS）|（[^（）]*）$", "", s or "").strip())
spread(by_sp, "原産地", "C原産地", "同じ種で原産地が違う", norm=lambda s: re.sub(r"（[^（）]*）$", "", s or "").strip())
spread(by_sp, "和名", "C和名", "同じ種で和名が違う", norm=lambda s: s)
spread(by_sp, "常緑性", "C常緑", "同じ種で常緑性が違う（品種で違うこともある）")
spread(by_sp, "毒性", "C毒性", "同じ種で毒性が違う")
spread(by_sp, "外来種リスト", "C外来", "同じ種で外来種リストが違う", norm=lambda s: s)
spread(by_sp, "北海道ブルーリスト", "Cブルー", "同じ種で北海道ブルーリストが違う", norm=lambda s: s)
spread(by_sp, "耐暑性", "C耐暑", "同じ種で耐暑性が違う（品種で違うこともある）", norm=lambda s: s)
spread(by_sp, "蒸れ耐性", "C蒸れ", "同じ種で蒸れ耐性が違う（品種で違うこともある）", norm=lambda s: s)
spread(by_sp, "乾燥耐性", "C乾燥", "同じ種で乾燥耐性が違う（品種で違うこともある）", norm=lambda s: s)
spread(by_sp, "土壌水分", "C土", "同じ種で土壌水分が違う", norm=lambda s: s)
spread(by_sp, "混植適性", "C混植", "同じ種で混植適性が違う", norm=lambda s: s)
spread(by_sp, "地下茎で広がる程度(0-3)", "C地下茎", "同じ種で地下茎で広がる程度が違う", norm=lambda s: s)

# ---- D 今のマスターの値との違い（花色・葉色）
COLOR = [("白", "白"), ("ピンク", "ピンク|桃|ローズ|赤紫"), ("青・紫", "青|紫|藤|ラベンダー|すみれ"), ("黄", "黄|クリーム|レモン"), ("赤", "赤|紅|緋|ワイン"),
         ("オレンジ・アプリコット", "オレンジ|橙|アプリコット|杏|サーモン|銅")]
LEAF = {"① グリーン系": "グリーン系", "② ゴールド／ライム系": "ゴールド・ライム系", "③ ブルー系": "ブルー系", "④ シルバー系": "シルバー系",
        "⑤ パープル／ブラック系": "パープル・ブラック系", "⑥ ブロンズ／レッド系": "ブロンズ・レッド系", "⑦ 斑入り": "斑入り", "⑧ 季節変化型": None}
for x in R:
    mine, lit = v(x, "花色（自社の値）"), v(x, "花色（分類）")
    if mine and lit:
        ms = {c for c, pat in COLOR if re.search(pat, mine)}
        ls = set(re.split("[、・,/／]", lit)) | ({"青・紫"} if "青・紫" in lit else set()) | ({"オレンジ・アプリコット"} if "オレンジ" in lit else set())
        if ms and not (ms & ls):
            add("D花色", "花色が、今のマスターの値と重ならない", "D", x, ["花色（自社の値）", "花色（分類）", "花色（詳細）"])
    mine, lit = v(x, "葉色（自社の値）"), v(x, "葉色（分類）")
    if mine and lit and LEAF.get(mine) and LEAF[mine] != lit:
        add("D葉色", "葉色が、今のマスターの値と違う", "D", x, ["葉色（自社の値）", "葉色（分類）", "葉の特徴"])

json.dump(list(checks.values()), open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
for k, e in checks.items():
    print(f"{k:8s} {e['種類']} {len(e['品種']):4d}  {e['調べ方']}")
