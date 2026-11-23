"""まとめの表（combine.py の出力）を、試作と同じ形（trial/rows/Pxx.json）の品種ごとの JSON にする。

使い方（master-rebuild で）: python -X utf8 scripts/pilot/to_rows.py <まとめの表.xlsx> <出力フォルダ>
- 1品種1ファイル（<商品番号>.json）。形は trial/RULES.md の rows と同じ:
  {"id", "product_no", "name_ja", "fields": {<field>: {"value", "method", "sources", "level", "note"}}, "review": {...}}
- 文献の値だけを入れる。今のマスターの値（花期・草丈・耐寒性・流通名）、在庫、価格、自社の値は入れない（試作の rows と同じ）
- sources・level は、値の後ろの「（RHS）」「（MBG・種）」や、根拠の列の「[MBG・品種]」「[おぎはら/品種]」から読む。
  どちらもない項目は sources を null にして、note に「使った文献」の列を写す（組み立てのとき文献名を付けていない項目）
- method: まとめの表の1行目（出どころ）に「判定」があれば 判定、なければ 記載
"""
import json
import os
import re
import sys

import openpyxl

SRC = [  # (表の中の文献名, 文献ID)。長い名前から先に当てる
    ("おぎはら楽天", "s21"), ("おぎはら", "s20"), ("stauden.de", "s18"), ("Gaißmayer", "s17"), ("Jelitto", "s11"), ("Walters", "s10"),
    ("シカゴ植物園", "s08"), ("NC State", "s06"), ("YList", "s04"), ("Kew", "s03"), ("MBG", "s02"), ("RHS", "s01"), ("環境省", "s05"),
]
SRC_RE = re.compile("|".join(re.escape(n) for n, _ in SRC))
ID = dict(SRC)
# (field, 表の列, 値の形, 文献を探す根拠の列)。値の形: str・int・list（「、」で分ける）
FIELDS = [
    ("accepted_name", "学名（正名）", "str", None), ("synonyms", "旧学名・別名", "list", None), ("family", "科名", "str", None),
    ("common_name_ja", "和名", "str", None), ("flower_color_detail", "花色（詳細）", "str", None), ("flower_color_class", "花色（分類）", "list", None),
    ("spread_min", "株張り 最小(cm)", "int", None), ("spread_max", "株張り 最大(cm)", "int", None), ("foliage_class", "葉色（分類）", "str", None),
    ("foliage_features", "葉の特徴", "list", None), ("seasonal_foliage", "紅葉・冬の葉", "str", None), ("fragrance", "香り", "str", None),
    ("silhouette", "成株シルエット", "str", "成株シルエットの根拠"), ("sun", "日照", "str", None),
    ("usda_min", "USDA 下限", "int", None), ("usda_max", "USDA 上限", "int", None), ("rhs_h", "RHS 耐寒性", "str", None),
    ("heat", "耐暑性", "str", "暑さ・蒸れ・西日の根拠"), ("heat_note", "暑さ・蒸れの注意", "str", None),
    ("muggy", "蒸れ耐性", "str", "暑さ・蒸れ・西日の根拠"), ("west_sun", "西日耐性", "str", "暑さ・蒸れ・西日の根拠"),
    ("drought", "乾燥耐性", "str", None), ("soil_moisture", "土壌水分", "str", None), ("soil_ph_type", "pH・土質", "str", None),
    ("salt", "耐潮性", "str", "耐潮性の根拠"), ("evergreen_warm", "常緑性", "str", None), ("native_range", "原産地", "str", None),
    ("spread_modes", "増え方", "list", None), ("self_seed_level", "こぼれ種の量(0-3)", "int", "こぼれ種・地下茎の根拠"),
    ("rhizome_level", "地下茎で広がる程度(0-3)", "int", "こぼれ種・地下茎の根拠"), ("mixing", "混植適性", "str", "混植適性の根拠"),
    ("invasive_note", "広がりすぎの注意", "str", None), ("ias_list", "外来種リスト", "str", None), ("hokkaido_bluelist", "北海道ブルーリスト", "str", None), ("toxicity", "毒性", "str", None),
    ("pests", "主な病害虫", "list", None), ("pruning_codes", "切り戻しの方法", "list", "切り戻し・手入れの文（全部）"),
    ("management_type", "管理タイプ", "str", "管理タイプのメモ"), ("division_interval", "株分けの間隔", "str", "株分けの間隔の根拠"),
    ("propagation", "繁殖方法", "list", None), ("cut_flower", "切り花適性", "str", None), ("pollinator", "蜜源価値", "str", None),
]
TAIL = re.compile(r"（([^（）]*)）$")


def level_of(s):
    return "cultivar" if "品種" in s else "species" if "種" in s else "genus" if "属" in s else None


def cites(text):
    """文の中の文献名と階層 → (sources, level)。階層は、いちばん細かいもの（品種 → 種 → 属）"""
    srcs, lv = [], set()
    for m in re.finditer(r"(" + SRC_RE.pattern + r")(?:[・/／](品種|種|属))?", text or ""):
        i = ID[m.group(1)]
        if i not in srcs:
            srcs.append(i)
        if m.group(2):
            lv.add(level_of(m.group(2)))
    level = next((x for x in ("cultivar", "species", "genus") if x in lv), None)
    return srcs, level


# 「根拠」のシート（まとまりごとの下書きの根拠をつないだもの）の項目 → field。最後の列に文献名と階層があれば使う
EVMAP = {"USDA": ("usda_min", "usda_max"), "日照": ("sun",), "乾燥耐性": ("drought",), "土壌水分": ("soil_moisture",),
         "株張り(cm)": ("spread_min", "spread_max"), "花色（文献の語）": ("flower_color_detail", "flower_color_class"),
         "葉色（分類）": ("foliage_class",), "和名": ("common_name_ja",), "原産地": ("native_range",), "増え方": ("spread_modes",),
         "切り花": ("cut_flower",), "蜜源": ("pollinator",), "常緑性": ("evergreen_warm",), "病害虫": ("pests",), "繁殖": ("propagation",),
         "切り戻し": ("pruning_codes",), "紅葉": ("seasonal_foliage",)}
# 「項目の文献」の列（assemble_pilot.py が 2026-11-21 から残す。「日照=MBG・種」の行）の項目 → field
PROV = {"日照": ("sun",), "土壌水分": ("soil_moisture",), "乾燥耐性": ("drought",), "増え方": ("spread_modes",), "切り花": ("cut_flower",),
        "蜜源": ("pollinator",), "花色（文献の語）": ("flower_color_detail",), "花色（分類）": ("flower_color_class",),
        "株張り(cm)": ("spread_min", "spread_max"), "葉色（分類）": ("foliage_class",)}
FIXED = {"rhs_h": ["s01"], "common_name_ja": ["s04"], "ias_list": ["s05"], "hokkaido_bluelist": ["s22"]}  # 出どころが1つに決まっている列（RHS の H 値・YList の和名・環境省のリスト）


def main(xlsx, out):
    wb = openpyxl.load_workbook(xlsx, read_only=True)
    evs = {}
    for e in wb["根拠"].iter_rows(min_row=2, values_only=True):
        for k in EVMAP.get(e[3], ()):
            s, lv = cites(e[5])
            if s:
                cur = evs.setdefault((e[1], k), [[], set()])
                cur[0] += [x for x in s if x not in cur[0]]
                cur[1].add(lv)
    ws = wb.worksheets[0]
    it = ws.iter_rows(values_only=True)
    origin = list(next(it))
    head = list(next(it))
    col = {c: i for i, c in enumerate(head)}
    os.makedirs(out, exist_ok=True)
    n, stats = 0, {"with_sources": 0, "no_sources": 0}
    for r in it:
        g = lambda c: r[col[c]]
        used = g("使った文献")
        prov = {}
        for line in (g("項目の文献") or "").splitlines():
            c, _, lab = line.partition("=")
            for k in PROV.get(c, ()):
                prov[k] = cites(lab)
        fields = {}
        for key, c, kind, evcol in FIELDS:
            v = g(c)
            method = "判定" if "判定" in (origin[col[c]] or "") else "記載"
            srcs, level, note = [], None, None
            if isinstance(v, str) and key in ("division_interval", "invasive_note", "foliage_features", "heat_note"):
                srcs, level = cites(v)  # 文の中に文献名がある。値はそのまま
            elif isinstance(v, str):
                m = TAIL.search(v)
                if m and SRC_RE.search(m.group(1)):  # 値の後ろの「（RHS）」などを外して、文献に
                    srcs, level = cites(m.group(1))
                    v = v[:m.start()].strip()
            if v is not None and not srcs and key in prov:
                srcs, level = prov[key]
            if v is not None and not srcs and evcol and g(evcol):
                srcs, level = cites(g(evcol))
            if v is not None and not srcs and key == "mixing" and "こぼれ種・地下茎の根拠の列" in (g("混植適性の根拠") or ""):
                srcs, level = cites(g("こぼれ種・地下茎の根拠"))  # 地下茎・こぼれ種の程度から決めた混植適性
            if v is not None and not srcs and key == "west_sun" and fields["sun"]["sources"]:
                srcs, level = fields["sun"]["sources"], fields["sun"]["level"]  # 日照が半日陰・日陰なので ×
                note = "日照（半日陰・日陰）から"
            if v is not None and not srcs and (g("商品番号"), key) in evs:
                s, lv = evs[(g("商品番号"), key)]
                srcs, level = s, next((x for x in ("cultivar", "species", "genus") if x in lv), None)
            if v is not None and key in FIXED:
                srcs = FIXED[key]
            if key == "heat" and v is not None:
                how = g("耐暑性の決め方") or ""
                if how.startswith("おぎはら"):
                    srcs, level = ["s20"], ("cultivar" if "品種のページ" in how else "species")
                note = "。".join(x for x in (how, f"信頼度：{g('耐暑性の信頼度')}" if g("耐暑性の信頼度") else None) if x) or None
            if key == "management_type":
                note = g("管理タイプの決め方")
            if key == "invasive_note" and v:
                srcs, level = cites(v)
            if kind == "list" and isinstance(v, str):
                v = [x.strip() for x in re.split(r"[、,]", v) if x.strip()] or None
                if v:  # 最後の要素の後ろの「（stauden.de・品種）」などは文献なので外す
                    m = TAIL.search(v[-1])
                    if m and SRC_RE.search(m.group(1)):
                        v[-1] = v[-1][:m.start()].strip()
            if kind == "int" and v is not None:
                v = int(v)
            if v is not None and not srcs and key not in ("accepted_name",):
                note = "。".join(x for x in (note, f"組み立てのとき文献名を付けていない項目（使った文献：{used}）") if x)
            stats["with_sources" if srcs else "no_sources"] += v is not None
            # 2026-11-23 の決定: MBG の Water: Medium から推定した乾燥耐性は、判定・信頼度 低 と分かるようにする
            if key == "drought" and str(g("乾燥耐性の出どころ") or "").startswith("推定"):
                method = "判定"
                note = "。".join(x for x in (note, g("乾燥耐性の出どころ")) if x)
            fields[key] = {"value": v, "method": method, "sources": srcs or None, "level": level}
            if note:
                fields[key]["note"] = note
        rn = g("学名（RHS）") or ""
        an = fields["accepted_name"]
        an["note"] = "。".join(x for x in (f"RHS：{rn}" if rn else None, g("学名のメモ")) if x) or None
        # 学名（採用）は、RHS が正名（Accepted／Correct）としていれば RHS の表記（assemble_pilot.py の adopt_name）。そのときだけ s01
        if re.search(r"\[(Accepted|Correct)", rn) and re.sub(r"[^a-z]", "", rn.split("[")[0].split("（")[0].lower()) == re.sub(r"[^a-z]", "", (an["value"] or "").lower()):
            an["sources"], an["level"] = ["s01"], "cultivar" if "'" in an["value"] else "species"
        else:
            an["note"] = "。".join(x for x in ("今のマスターの学名か、検討で決めた学名（RHS の正名と同じ表記ではない）", an.get("note")) if x)
        if fields["synonyms"]["value"]:
            fields["synonyms"]["note"] = "今のマスターの学名（正名と表記が違うもの）"
        row = {
            "id": g("下書きのID"), "product_no": g("商品番号"), "name_ja": g("植物名"),
            "fields": fields,
            "review": {
                "management_type_reason": g("管理タイプのメモ"), "management_type_quote": g("管理タイプの決め手（原文）"),
                "management_type_by_matching": g("管理タイプ（言い回しの照合）"), "heat_west_only": g("耐暑性（欧米の文献だけなら）"),
                "muggy_west_only": g("蒸れ耐性（欧米の文献だけなら）"), "heat_muggy_west_evidence": g("暑さ・蒸れ・西日の根拠"),
                "spread_evidence": g("こぼれ種・地下茎の根拠"), "mixing_evidence": g("混植適性の根拠"), "silhouette_evidence": g("成株シルエットの根拠"),
                "sources_with_cultivar_page": g("品種ページのある文献"), "sources_used": used,
            },
        }
        with open(os.path.join(out, f"{g('商品番号')}.json"), "w", encoding="utf-8", newline="\n") as f:
            json.dump(row, f, ensure_ascii=False, indent=1)
        n += 1
    print("品種", n, stats)


if __name__ == "__main__":
    main(*sys.argv[1:3])
