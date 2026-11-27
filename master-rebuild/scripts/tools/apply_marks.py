"""2026-11-27 印の取り込み: RHS の「Plants for Pollinators」「Cut flowers」と Gaißmayer の表の「Schnittgeeignet: ja」を、
蜜源・切り花の読み直し（poll_reread.json・cut_reread.json）に入れる。前は取り出しで拾っていなかった（HANDOFF 1127i）。
使い方（master-rebuild で）: apply_marks.py <marks_dump.jsonl> <新マスター.xlsx> [--write]
  --write なしは数えるだけ。決め方は scripts/tools/marks_note.md
  （species_check.json の 1391・846 を 残す にしたのは手で直した。marks_note.md の最後の行）
"""
import json
import sys

import openpyxl

marks_p, xlsx = sys.argv[1], sys.argv[2]
write = "--write" in sys.argv
TAG = "（2026-11-27 印の取り込み：{}）"

marks = {}
for line in open(marks_p, encoding="utf-8"):
    d = json.loads(line)
    marks[str(d["商品番号"])] = d
wb = openpyxl.load_workbook(xlsx, read_only=True)
ws = wb.worksheets[0]
rows = list(ws.iter_rows(values_only=True))
h = rows[1]  # 1行目は列のまとまり、2行目が見出し
ih = h.index("草丈 最大(cm)")
height = {str(r[0]): r[ih] for r in rows[2:] if r[0] is not None}
cut = json.load(open("cut_reread.json", encoding="utf-8"))
poll = json.load(open("poll_reread.json", encoding="utf-8"))
spc = {(no, item): d for no, items in json.load(open("species_check.json", encoding="utf-8")).items() for item, d in items.items()}
log = {"蜜源": [], "切り花": [], "食い違い": [], "品種の確かめで外した": []}


def put(store, no, key, val, lv, by, conf, note):
    e = store.setdefault(no, {key: None, "段階": None, "決め手": None, "食い違い": None, "確かさ": "高", "メモ": None, "前の値": None, "今のマスター": None})
    old = e.get(key)
    e[key], e["段階"], e["決め手"], e["確かさ"] = val, lv, by, conf
    e["メモ"] = ((e.get("メモ") or "") + TAG.format(f"{note}。前の読み直し：{old if old else '空欄'}")).strip()
    return old


for no, m in sorted(marks.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 0):
    # 蜜源: RHS の Plants for Pollinators は ◎（poll_reread_note.md の ◎ の例）。RHS は文献の順の1番目
    if m["RHS_poll"]:
        e = poll.get(no) or {}
        v = e.get("蜜源")
        if v == "△":
            log["食い違い"].append(f"{no} 蜜源 △ のまま（RHS は Plants for Pollinators）: {e.get('決め手')}")
        elif v != "◎":
            if (no, "蜜源") in spc and spc[(no, "蜜源")]["判断"] == "外す":
                log["品種の確かめで外した"].append(f"{no} 蜜源（種の値を外した品種。RHS の品種のページに印がある）: {spc[(no, '蜜源')]['理由']}")
            old = put(poll, no, "蜜源", "◎", "品種", "[RHS・品種] For Biodiversity: Plants for Pollinators", "高",
                      "RHS の品種のページに Plants for Pollinators の印")
            log["蜜源"].append(f"{no} {old} → ◎")
    # 切り花: RHS の Cut flowers・Gaißmayer の品種のページの Schnittgeeignet は ○（印だけ。◎ にはしない）
    e = cut.get(no) or {}
    v = e.get("切り花")
    src = []
    if m["RHS_cut"]:
        src.append(("品種", "[RHS・品種] Suggested planting locations and garden types: Cut flowers"))
    if m["Gai_cut"] and (m["Gai_段階"] == "品種" or not m["品種名あり"]):
        src.append(("品種" if m["Gai_段階"] == "品種" else "種", f"[Gaißmayer・{m['Gai_段階']}] Schnittgeeignet: ja"))
    sp_only = False
    if not src and m["Gai_cut"] and m["Gai_段階"] == "種" and m["品種名あり"]:
        # 品種名のある商品に種のページ: 2026-11-26 の決定で ○ まで・確かさ 低。草丈 30cm 以下は当てない（2026-11-27 の決定「外す」）
        hh = height.get(no)
        if hh is not None and float(hh) > 30:
            src.append(("種", f"[Gaißmayer・種] Schnittgeeignet: ja（{m['Gai']}）"))
            sp_only = True
    if not src:
        continue
    if v == "△":
        log["食い違い"].append(f"{no} 切り花 △ のまま（{src[0][1]}）: {e.get('決め手')}")
    elif v is None:
        lv, by = src[0]
        if (no, "切り花") in spc and spc[(no, "切り花")]["判断"] == "外す" and sp_only:
            continue
        put(cut, no, "切り花", "○", lv, " ／ ".join(b for _, b in src), "低" if sp_only else "中",
            "種のページの印（品種名のある商品なので ○ まで・確かさ 低）" if sp_only else "切り花の印")
        log["切り花"].append(f"{no} 空欄 → ○（{lv}）")

for k, v in log.items():
    print("##", k, len(v))
    for x in v:
        print("  ", x)
if write:
    for p, d in (("cut_reread.json", cut), ("poll_reread.json", poll)):
        with open(p, "w", encoding="utf-8", newline="\r\n") as fh:  # 今のファイルと同じ形（indent=0・CRLF・末尾の改行なし）
            json.dump(d, fh, ensure_ascii=False, indent=0)
    print("書いた")
