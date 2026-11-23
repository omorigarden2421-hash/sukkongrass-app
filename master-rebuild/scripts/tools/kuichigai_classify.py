"""まとめの表の「…の食い違い」の印（耐寒性・花期・草丈・株張り・日照）を、確認が要るもの（残す）と、
測り方や地域の違いで説明できるもの（外す。マスターのまま）に分ける。2026-11-23（ユーザーの指示「先に調べてから確認ページ」）。
使い方: python -X utf8 scripts/tools/kuichigai_classify.py <まとめの表.xlsx> kuichigai_review.json
"""
import openpyxl, json, re, sys
wb = openpyxl.load_workbook(sys.argv[1], read_only=True)
ws = wb.active
rows = list(ws.iter_rows(values_only=True))
H = rows[1]
idx = {h: i for i, h in enumerate(H)}
F = ["草丈の食い違い", "花期の食い違い", "株張りの食い違い", "日照の食い違い", "耐寒性の食い違い"]
out = []
for r in rows[2:]:
    if not any(r[idx[f]] for f in F):
        continue
    d = {k: r[idx[k]] for k in ["商品番号", "植物名", "学名（正名）", "品種名", "草丈 最小(cm)", "草丈 最大(cm)", "草丈（文献）", "花期 開始月", "花期 終了月", "花期（文献）", "株張り 最小(cm)", "株張り 最大(cm)", "株張り（文献）", "日照", "日照（文献）", "耐寒性", "USDA 下限", "RHS 耐寒性", "草姿シルエット", "科名", "和名"] if k in idx}
    for f in F:
        if r[idx[f]]:
            d[f] = r[idx[f]]
    out.append(d)
d = out

from collections import Counter
# 根もとに葉が集まり、花茎や穂だけが高く伸びる仲間（葉の高さと花の高さが大きく違う）
BASAL = {"Heuchera", "× Heucherella", "Tiarella", "Ligularia", "Bergenia", "Hosta", "Pulmonaria", "Brunnera",
         "Yucca", "Astilbe", "Mukdenia"}
GRASS = ("Poaceae", "Cyperaceae")


def rng(s):
    m = re.search(r"文献 (\d+)(?:〜(\d+))?(?:cm|月)／マスター (\d+)〜(\d+)", s)
    return tuple(int(x) if x else None for x in m.groups())


res = []
cnt = Counter()
for x in d:
    sci = x["学名（正名）"] or ""
    genus = "× Heucherella" if sci.startswith("× Heucherella") else sci.split()[0]
    fam = x.get("科名") or ""
    keep, drop = [], []
    for k, lk in [("草丈の食い違い", "草丈（文献）"), ("株張りの食い違い", "株張り（文献）"), ("花期の食い違い", "花期（文献）"),
                  ("日照の食い違い", "日照（文献）"), ("耐寒性の食い違い", None)]:
        v = x.get(k)
        if not v:
            continue
        item = {"項目": k.replace("の食い違い", ""), "内容": v, "文献": x.get(lk) if lk else f"USDA 下限 {x.get('USDA 下限')}・RHS {x.get('RHS 耐寒性')}"}
        why = None
        if k in ("草丈の食い違い", "株張りの食い違い"):
            a, b, m0, m1 = rng(v)
            b = b or a
            big = a > m1
            src = item["文献"] or ""
            if k == "株張りの食い違い" and big:
                why = "文献は何年も育った後の株幅（" + ("シカゴ植物園の数年の試験" if "シカゴ" in src else "RHS の最終的な大きさの大まかな区分" if "RHS" in src else "Walters の成株") + "）。マスターより大きく出るのは測り方の違い"
            elif k == "草丈の食い違い" and big and ("Stachys byzantina" in sci or genus in BASAL or any(g in fam for g in GRASS)):
                why = "葉は低く、花茎や穂だけが高く伸びる植物。文献は花の高さ、マスターは葉の高さとみられる"
            elif k == "草丈の食い違い" and big and "RHS" in src:
                why = "RHS の値は最終的な大きさの大まかな区分（1〜1.5m など）"
        elif k == "花期の食い違い":
            a, b, c0, c1 = rng(v)
            b = b or a
            gap = (c0 - b) % 12
            if "ドイツ" in item["文献"] and gap <= 1:
                why = "文献はドイツの花期。寒い広尾では1か月ほど遅れて咲く"
            elif "セントルイス" in item["文献"] and gap <= 2:
                why = "文献はセントルイス（アメリカ中部の暖かい町）の花期。広尾では1〜2か月遅れて咲く"
        if why:
            item["外した理由"] = why
            drop.append(item)
            cnt["外す:" + item["項目"]] += 1
        else:
            keep.append(item)
            cnt["残す:" + item["項目"]] += 1
    res.append({"商品番号": x["商品番号"], "植物名": x["植物名"], "学名": sci, "和名": x.get("和名"), "残す": keep, "外す": drop,
                "マスター": {"草丈": f"{x['草丈 最小(cm)']}〜{x['草丈 最大(cm)']}cm", "株張り": f"{x['株張り 最小(cm)']}〜{x['株張り 最大(cm)']}cm",
                           "花期": f"{x['花期 開始月']}〜{x['花期 終了月']}月", "日照": x["日照"], "耐寒性": x["耐寒性"]}})
json.dump(res, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sorted(cnt.items()))
print("残る品種", sum(1 for r in res if r["残す"]), "全部外れる品種", sum(1 for r in res if not r["残す"]))
