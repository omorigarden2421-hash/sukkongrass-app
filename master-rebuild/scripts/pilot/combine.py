"""まとまりごとの下書き（19個・916品種）を、試作28品種のマスターと同じ列の並びの1つの表にまとめる。

使い方（master-rebuild で）: python -X utf8 scripts/pilot/combine.py <ClaudeWork> <元のマスター.xlsx> <試作マスター.xlsx> <出力.xlsx>
- 下書きは <ClaudeWork> の「下書き_*.json」「試行_3属*.json」のうち、まとまりごとに名前の末尾がいちばん新しいもの（scripts/tools/rediff.py の KEY と同じ探し方）
- 「今のマスター」の列（花期・草丈・耐寒性・流通名）は元のマスターから。価格・在庫数は写さない（在庫の有無だけ）
- 外来種リストは、試作マスターの「外来種リスト該当（全商品）」のシートから（環境省のリストとの照合は試作のときに全商品で済んでいる）
- 下書きにまだない列（科名・香り・管理タイプなど）は空欄にして、「まだ作っていない列」のシートに並べる
"""
import glob
import json
import os
import re
import sys

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

CW, MASTER, TRIAL, OUT = sys.argv[1:5]
src = open("scripts/tools/rediff.py", encoding="utf-8").read()
KEYS = ["試行_3属*.json", "下書き_アスター*.json"] + re.findall(r'\d+: "(下書き_[^"]+)"', src)
draft, files = {}, []
for k in KEYS:
    f = sorted(glob.glob(f"{CW}/{k}"))[-1]
    files.append(f)
    for r in json.load(open(f, encoding="utf-8")):
        draft[str(r["商品番号"])] = r
stock = {}
for f in glob.glob("batch_*/input/*.json") + glob.glob("pilot/input/*.json"):
    d = json.load(open(f, encoding="utf-8"))
    stock[str(d["商品番号"])] = d
ws0 = openpyxl.load_workbook(MASTER, read_only=True)["Sheet1"]
rows0 = list(ws0.iter_rows(values_only=True))
H0 = list(rows0[0])
master = [dict(zip(H0, r)) for r in rows0[1:] if r[H0.index("商品番号")] and r[H0.index("学名")]]
wt = openpyxl.load_workbook(TRIAL, read_only=True)
ias_rows = list(wt["外来種リスト該当（全商品）"].iter_rows(values_only=True))
IH = list(ias_rows[0])
ias = {}
for r in ias_rows[1:]:
    d = dict(zip(IH, r))
    if d.get("商品番号"):
        ias[str(d["商品番号"])] = d


def fmt_name(s):
    if not s:
        return s
    s = re.sub(r"[‘’‛`]", "'", str(s).replace("\n", " ").replace("　", " "))
    s = re.sub(r"\s*（", "（", re.sub(r"\s+", " ", s).strip())
    i = s.find("'")
    return s[:i] + " " + s[i:] if i > 0 and s[i - 1] != " " else s


SEASON = {"早春": (3, 3), "晩冬": (2, 2), "冬": (12, 2), "晩春": (5, 5), "春": (4, 5), "初夏": (6, 6), "盛夏": (7, 8), "晩夏": (8, 9), "夏": (7, 8), "晩秋": (11, 11), "秋": (9, 10)}


def bloom(s):  # scripts/assemble.py（試作）と同じ読み方
    if not s or s in ("ー", "None"):
        return None, None
    s = str(s).replace("〜", "～")
    if "（" in s or "(" in s:
        nums = re.findall(r"(\d+)\s*月?", s[s.find("（") if "（" in s else s.find("("):])
        if nums:
            return int(nums[0]), int(nums[-1])
    parts = s.split("～")

    def look(w, first):
        for k in sorted(SEASON, key=len, reverse=True):
            if w.startswith(k):
                return SEASON[k][0 if first else 1]
        return None
    return look(parts[0].strip(), True), look(parts[-1].strip(), False)


def height(s):
    if s is None:
        return None, None, None
    s = str(s).replace("（", "(").replace("）", ")").replace("〜", "～")
    paren = None
    m = re.search(r"\(([^)]*)\)", s)
    if m:
        paren, s = m.group(1), s[:m.start()]
    n = [int(x) for x in re.findall(r"\d+", s)]
    return (n[0], n[-1], paren) if n else (None, None, paren)


def split_name(sci):
    """学名 → (属, 種小名, 品種名)。交配種・種小名なしは種小名を空欄にする"""
    cv = re.search(r"'(.+)'", sci)
    head = re.sub(r"\(.*?\)", " ", re.sub(r"'.*$", "", sci)).replace("×", " × ").split()
    g = head[0] if head else None
    rest = [w for w in head[1:] if w != "×"]
    ep = " ".join(rest) if rest and re.fullmatch(r"[a-z-]+", rest[0]) else None
    if ep and "×" in head[1:2]:
        ep = "× " + ep
    return g, ep, cv.group(1) if cv else None


COLS = [  # (列名, 出どころ)
 ("商品番号", "今のマスター"), ("植物名", "今のマスター"), ("学名（正名）", "文献"), ("属", "自動"), ("種小名", "自動"), ("品種名", "自動"), ("旧学名・別名", "文献"),
 ("科名", "まだ"), ("和名", "文献（YList）"), ("流通名・別名", "今のマスター"), ("花色（分類）", "文献"), ("花色（詳細）", "文献"),
 ("花期 開始月", "今のマスター"), ("花期 終了月", "今のマスター"), ("草丈 最小(cm)", "今のマスター"), ("草丈 最大(cm)", "今のマスター"), ("草丈 括弧内の値", "今のマスター"),
 ("株張り 最小(cm)", "文献"), ("株張り 最大(cm)", "文献"), ("葉色（分類）", "文献"), ("葉の特徴", "まだ"), ("紅葉・冬の葉", "文献"), ("香り", "まだ"), ("成株シルエット", "まだ"),
 ("日照", "文献"), ("耐寒性", "今のマスター"), ("USDA 下限", "文献"), ("USDA 上限", "文献"), ("RHS 耐寒性", "文献"), ("耐暑性", "文献（判定）"), ("蒸れ耐性", "文献（判定）"),
 ("暑さ・蒸れの注意", "文献"), ("西日耐性", "文献（判定。組み合わせ）"), ("夏越し実績（自社の実測）", "自社の実測（本州のお客様・卸先からの報告を記入）"), ("乾燥耐性", "文献"),
 ("土壌水分", "文献"), ("pH・土質", "まだ"), ("耐潮性", "まだ"), ("常緑性", "文献（温暖地の値）"), ("原産地", "文献"), ("増え方", "文献"), ("こぼれ種の量(0-3)", "まだ"),
 ("地下茎で広がる程度(0-3)", "まだ"), ("混植適性", "まだ"), ("広がりすぎの注意", "まだ"), ("外来種リスト", "文献（環境省）"), ("毒性", "まだ"), ("主な病害虫", "文献"),
 ("管理タイプ", "まだ"), ("管理難易度", "まだ"), ("切り戻しの方法", "文献"), ("切り戻し時期（広尾町）", "まだ"), ("切り戻し時期（関東）", "まだ"), ("株分けの間隔", "まだ"),
 ("繁殖方法", "文献"), ("景観構成用途", "自動"), ("切り花適性", "文献"), ("蜜源価値", "文献"), ("機能用途タグ", "まだ"), ("デザイン系タグ", "まだ"), ("リスクタグ", "まだ"),
 # ここから右は、下書きから持ってきた見返し用の列（試作マスターにはない）
 ("在庫あり", "今のマスター"), ("自社の観察", "自社"), ("花色（自社の値）", "今のマスター"), ("株張り（自社の値・cm）", "今のマスター"), ("葉色（自社の値）", "今のマスター"),
 ("耐暑性の信頼度", "見返し用"), ("耐暑性の決め方", "見返し用"), ("耐暑性（欧米の文献だけなら）", "見返し用"), ("蒸れ耐性（欧米の文献だけなら）", "見返し用"),
 ("乾燥耐性の出どころ", "見返し用"), ("暑さ・蒸れ・西日の根拠", "見返し用"), ("学名（マスター）", "今のマスター"), ("学名のメモ", "見返し用"), ("学名（RHS）", "見返し用"),
 ("品種ページのある文献", "見返し用"), ("使った文献", "見返し用"), ("空欄の数（下書き）", "見返し用"), ("下書きのID", "見返し用"),
]
NOT_YET = {
 "科名": "試作では Kew から取った。全品種ではまだ取っていない",
 "葉の特徴": "試作では文献の本文から人が書いた。下書きにはない",
 "香り": "同上（RHS の Fragrance、Gaißmayer の Duftend は読んであるが、表にしていない）",
 "成株シルエット": "試作では文献の草姿から決めた。下書きにはない",
 "pH・土質": "RHS の Soil・pH の欄は読んであるが、表にしていない",
 "耐潮性": "下書きにはない（おぎはら・MBG の本文に書いてある品種がある）",
 "こぼれ種の量(0-3)": "stauden.de・Gaißmayer の記述は集めてあるが、0〜3 の段階にしていない",
 "地下茎で広がる程度(0-3)": "同上",
 "混植適性": "下書きにはない",
 "広がりすぎの注意": "下書きにはない（「文献の注意」と根拠に一部ある）",
 "毒性": "Gaißmayer の Giftklasse、Jelitto の toxic plant は読んであるが、表にしていない",
 "管理タイプ": "試作では切り戻し・増え方から決めた。下書きにはない",
 "管理難易度": "管理タイプなどから自動で決める列。管理タイプがまだない",
 "切り戻し時期（広尾町）": "切り戻しの方法から自動で決める列。全品種ではまだ決めていない",
 "切り戻し時期（関東）": "同上",
 "株分けの間隔": "下書きにはない",
 "機能用途タグ": "ほかの列から自動で決める列。まだ決めていない",
 "デザイン系タグ": "同上",
 "リスクタグ": "同上",
}
rows, miss = [], []
for m in master:
    no = str(m["商品番号"])
    d = draft.get(no)
    if not d:
        miss.append(no)
        continue
    adopted = d.get("学名（採用）") or fmt_name(m["学名"])
    note = None
    mm = re.match(r"^(.*?)（(.*)）$", adopted, re.S)
    if mm:
        adopted, note = mm.group(1), mm.group(2)
    g, ep, cv = split_name(adopted)
    b0, b1 = bloom(m.get("花時期"))
    h0, h1, hp = height(m.get("高さ(cm)"))
    sp = [int(x) for x in re.findall(r"\d+", re.sub(r"（.*$", "", str(d.get("株張り(cm)") or "")))]
    z = re.match(r"(\d+)〜(\d+)", str(d.get("USDA") or ""))
    ia = ias.get(no)
    r = {
     "商品番号": m["商品番号"], "植物名": fmt_name(m["植物名"]), "学名（正名）": adopted, "属": g, "種小名": ep, "品種名": cv,
     "旧学名・別名": fmt_name(m["学名"]) if re.sub(r"[^a-z]", "", fmt_name(m["学名"]).lower()) != re.sub(r"[^a-z]", "", adopted.lower()) else None,
     "和名": re.sub(r"（種）$", "", d["和名"]) if d.get("和名") else None, "流通名・別名": fmt_name(m.get("別名")),
     "花色（分類）": d.get("花色（分類）"), "花色（詳細）": d.get("花色（文献の語）"), "花期 開始月": b0, "花期 終了月": b1,
     "草丈 最小(cm)": h0, "草丈 最大(cm)": h1, "草丈 括弧内の値": hp, "株張り 最小(cm)": sp[0] if sp else None, "株張り 最大(cm)": sp[-1] if sp else None,
     "葉色（分類）": d.get("葉色（分類）"), "紅葉・冬の葉": d.get("紅葉"), "日照": d.get("日照"), "耐寒性": m.get("耐寒性"),
     "USDA 下限": int(z.group(1)) if z else None, "USDA 上限": int(z.group(2)) if z else None, "RHS 耐寒性": d.get("RHS 耐寒性"),
     "耐暑性": d.get("耐暑性"), "蒸れ耐性": d.get("蒸れ耐性"), "暑さ・蒸れの注意": d.get("文献の注意"), "西日耐性": d.get("西日耐性"),
     "乾燥耐性": d.get("乾燥耐性"), "土壌水分": d.get("土壌水分"), "常緑性": d.get("常緑性"), "原産地": d.get("原産地"), "増え方": d.get("増え方"),
     "外来種リスト": (f"{ia.get('カテゴリ')}（{ia.get('リストの和名')}）" + (f"／特定外来生物: {ia['特定外来生物']}" if ia.get("特定外来生物") not in (None, "なし") else "")
                if ia else "掲載なし"),
     "主な病害虫": d.get("病害虫"), "切り戻しの方法": d.get("切り戻し"), "繁殖方法": d.get("繁殖"),
     "景観構成用途": (None if h1 is None else "前景" if h1 < 40 else "中景" if h1 < 90 else "後景"),
     "切り花適性": d.get("切り花"), "蜜源価値": d.get("蜜源"),
     "在庫あり": "○" if stock.get(no, {}).get("在庫あり") else None, "自社の観察": d.get("自社の観察"), "花色（自社の値）": d.get("花色（自社の値）"),
     "株張り（自社の値・cm）": d.get("株張り（自社の値・cm）"), "葉色（自社の値）": d.get("葉色（自社の値）"), "耐暑性の信頼度": d.get("耐暑性の信頼度"),
     "耐暑性の決め方": d.get("耐暑性の決め方"), "耐暑性（欧米の文献だけなら）": d.get("耐暑性（欧米の文献だけなら）"),
     "蒸れ耐性（欧米の文献だけなら）": d.get("蒸れ耐性（欧米の文献だけなら）"), "乾燥耐性の出どころ": d.get("乾燥耐性の出どころ"),
     "暑さ・蒸れ・西日の根拠": d.get("暑さ・蒸れ・西日の根拠"), "学名（マスター）": fmt_name(m["学名"]), "学名のメモ": note, "学名（RHS）": d.get("学名（RHS）"),
     "品種ページのある文献": d.get("品種ページのある文献"), "使った文献": d.get("使った文献"), "空欄の数（下書き）": d.get("空欄の数"), "下書きのID": d.get("ID"),
    }
    rows.append(r)
assert not miss, miss
wb = openpyxl.Workbook()
ws = wb.active
ws.title = f"マスター（下書き{len(rows)}品種）"
ws.append([k for _, k in COLS])
ws.append([c for c, _ in COLS])
for r in rows:
    ws.append([r.get(c) for c, _ in COLS])
FILL = {"今のマスター": "E2EFDA", "まだ": "D9D9D9", "見返し用": "FFF2CC", "自動": "DDEBF7"}
for i, (c, k) in enumerate(COLS, start=1):
    for row in (1, 2):
        cell = ws.cell(row, i)
        cell.font = Font(bold=row == 2, size=9 if row == 1 else 11)
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        cell.fill = PatternFill("solid", fgColor=FILL.get(k, "FCE4D6" if k.startswith("自社") else "FFFFFF"))
    ws.column_dimensions[get_column_letter(i)].width = 36 if c in ("植物名", "学名（正名）", "暑さ・蒸れの注意", "暑さ・蒸れ・西日の根拠", "学名のメモ", "学名（RHS）") else 22 if "学名" in c or c in ("原産地", "主な病害虫", "切り戻しの方法", "外来種リスト", "耐暑性の決め方", "乾燥耐性の出どころ", "使った文献") else 11
ws.freeze_panes = "C3"


def sheet(title, header, data, widths):
    s = wb.create_sheet(title)
    s.append(header)
    for x in data:
        s.append(x)
    for c in s[1]:
        c.font = Font(bold=True)
        c.fill = PatternFill("solid", fgColor="DDEBF7")
    for i, w in enumerate(widths, start=1):
        s.column_dimensions[get_column_letter(i)].width = w
    s.freeze_panes = "A2"


# 根拠と学名の検討は、まとまりごとの下書き（Excel）のシートをつなぐ
ev, nm, evh, nmh = [], [], None, None
for f in files:
    w = openpyxl.load_workbook(f[:-5] + ".xlsx", read_only=True)
    for name, acc in (("根拠", ev), ("学名の検討", nm)):
        if name in w.sheetnames:
            rr = list(w[name].iter_rows(values_only=True))
            if name == "根拠":
                evh = evh or list(rr[0])
            else:
                nmh = nmh or list(rr[0])
            acc += [list(x) for x in rr[1:] if any(x)]
sheet("根拠", evh, ev, [8, 8, 30, 14, 14, 90])
sheet("学名の検討", nmh, nm, [6, 8, 30, 32, 36, 12, 60, 40, 24])
filled = {c: sum(1 for r in rows if r.get(c) not in (None, "")) for c, _ in COLS}
sheet("列ごとの埋まり具合", ["列", "出どころ", "値のある品種", "空欄の品種"], [[c, k, filled[c], len(rows) - filled[c]] for c, k in COLS], [34, 40, 14, 14])
sheet("まだ作っていない列", ["列", "今の状態"], [[c, NOT_YET[c]] for c, k in COLS if k == "まだ"], [30, 90])
sheet("この表について", ["説明"], [[x] for x in [
    f"全{len(rows)}品種の下書きを、試作28品種のマスターと同じ列の並びにまとめたもの。並びは元のマスターの順。価格・在庫数は入れていない（在庫の有無だけ）。",
    "1行目は列の出どころ。緑＝今のマスターの値、白＝文献、青＝自動、灰色＝まだ作っていない列（空欄）、黄色＝見返し用の列（試作マスターにはない）。",
    "花期・草丈・耐寒性は今のマスターの値（2026-11-18 の決定）。耐暑性・蒸れ耐性・西日耐性・乾燥耐性の決め方は DECISIONS.md の 2026-11-21 の決定。",
    "「暑さ・蒸れの注意」には、下書きの「文献の注意」（シカゴ植物園の試験の記録など）を入れてある。通販ページには出さない（2026-11-19 の決定）。",
    "「夏越し実績（自社の実測）」は空欄で始め、本州のお客様・卸先からの報告を記入する。文献の値より優先する。",
    "もとにした下書き: " + "、".join(os.path.basename(f)[:16] + "…" + os.path.basename(f)[-11:-5] for f in files),
]], [160])
wb.save(OUT)
print("品種", len(rows), "/ 元のマスター", len(master), "根拠", len(ev), "学名の検討", len(nm))
print("値のある品種（主な列）:", {c: filled[c] for c in ("学名（正名）", "和名", "花色（分類）", "株張り 最小(cm)", "葉色（分類）", "日照", "USDA 下限", "耐暑性", "蒸れ耐性", "西日耐性", "乾燥耐性", "土壌水分", "常緑性", "原産地", "増え方", "主な病害虫", "切り戻しの方法", "繁殖方法", "切り花適性", "蜜源価値", "花期 開始月", "草丈 最大(cm)", "景観構成用途")})
print("外来種リスト: 掲載なし以外", sum(1 for r in rows if r["外来種リスト"] != "掲載なし"))
