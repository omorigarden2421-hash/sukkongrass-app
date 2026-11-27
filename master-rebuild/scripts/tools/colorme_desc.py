"""2026-11-27 カラーミーショップの商品説明（HTML）の 5つのまとまりを、新マスターの値で書き換える。
使い方: colorme_desc.py <新マスター.xlsx> <カラーミーの商品CSV> <出力フォルダ> [見本にする型番,型番,…|-] [一括更新用CSVの出力先]
- 書き換えるのは 基本情報・環境適正・生育特性・庭での使い方・管理 の <ul> の中だけ。ほかの文・画像・値段・在庫には触らない
- 商品番号・植物名・倒伏リスクは今の行をそのまま残す
- 出し方（ユーザーの決定 2026-11-27）: 品種で確かめた値はそのまま／種からの値・確かさ 低 は 値＋（目安）／空欄は「情報なし」
- 出力: stats.json（項目ごとの数）、sample.html（見本。今と新を並べる）
- 一括更新用CSV: マスターと合う行だけ。60列・見出し行なし・Shift-JIS(cp932)・全部の欄を " で囲む・行の終わりは CRLF。画像URLの列（商品画像URL・その他画像1〜9URL）は空（空なら画像は上書きされない）。商品説明のほかの列は、ダウンロードしたままの値
- Shift-JIS にない文字（学名の ö など）は、商品説明の中だけ &#数字; の形にする
- 「管理」のまとまりがない行（低木の5行）は、管理を足さない
- 商品CSV は値段と在庫を含むので、リポジトリに置かない。出力フォルダもリポジトリの外にする
"""
import csv, html, json, os, re, sys, collections
import openpyxl

MASTER, CSVP, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
SAMPLE = sys.argv[4].split(",") if len(sys.argv) > 4 and sys.argv[4] != "-" else []
CSVOUT = sys.argv[5] if len(sys.argv) > 5 else None
os.makedirs(OUT, exist_ok=True)
NA = "情報なし"
MEYASU = "（目安）"

PH = {
    "耐寒性": {"強": "北海道内の多くの地域で戸外越冬可", "中の強": "最低気温-15度以下が4～5日以上続かなければ越冬可",
            "中の中": "最低気温-10度以下が続く地域では注意が必要", "中の弱": "最低気温-5度以下になる地域では防寒が必要",
            "弱": "北海道では一年草扱い"},
    "耐暑性": {"強": "蒸し暑い夏にも強い", "中": "風通しが良ければ夏越ししやすい", "弱": "高温多湿が苦手"},
    "蒸れ耐性": {"強": "蒸れに強く夏も安定", "中": "風通しに気をつければ夏越し可", "弱": "夏は風通しの良い場所が必須"},
    "乾燥耐性": {"強": "水やりが少なくても育つ", "中": "適度な水分が必要", "弱": "乾燥に注意・水切れしやすい"},
    "西日耐性": {"◎": "西向き・西日の強い場所でも問題なし", "○": "短時間の西日なら耐えられる", "△": "西日は避けたほうが無難", "×": "西日は不可"},
    "土壌水分": {"湿潤寄り": "水持ちの良い土を好む", "適湿": "一般的な庭土で育つ", "排水必須": "水はけの良い土が必要", "乾燥寄り": "乾きやすい土向き"},
    "管理タイプ": {"放任型": "基本的に大きな手入れをしなくても育つ", "花後刈込型": "花後に刈り込むと整う", "夏前切戻型": "初夏に切り戻すと姿が整う",
              "隔離推奨型": "コンテナや仕切りで拡大を管理", "毎年株更新型": "毎年の株更新が必要"},
    "管理難易度": {"易": "初心者にも育てやすい", "中": "一般的", "難": "上級者向け"},
    "常緑性": {"落葉": "冬季落葉", "半常緑": "半常緑（暖地では常緑、寒冷地では落葉）", "常緑": "常緑"},
}
SECTIONS = {
    "基本情報": ["商品番号", "植物名", "学名", "花色", "葉色", "開花時期", "草丈", "広がり", "常緑性", "成株シルエット", "原産地"],
    "環境適正": ["日照条件", "耐寒性", "耐暑性", "蒸れ耐性", "乾燥耐性", "西日耐性", "土壌水分"],
    "生育特性": ["混植適性", "倒伏リスク", "増え方"],
    "庭での使い方": ["景観構成用途", "機能用途"],
    "管理": ["管理難易度", "管理タイプ", "病害虫リスク", "刈込時期"],
}
KEEP = {"商品番号", "植物名", "倒伏リスク"}


def s(v):
    return "" if v is None else str(v).strip()


def wave(t):
    return t.replace("〜", "～")


def tags(text):
    return re.findall(r"[・/](品種|種)(?=[\]）\s（。、・]|$)", s(text), flags=re.M)


def species_only(text):
    t = tags(text)
    return bool(t) and "品種" not in t


def low(text):
    return "確かさ 低" in s(text).split("]")[0]


def rng(a, b, unit):
    a, b = s(a), s(b)
    if not a and not b:
        return ""
    if not b or a == b:
        return f"{a or b}{unit}"
    if not a:
        return f"{b}{unit}"
    return f"{a}～{b}{unit}"


def phrase(key, v):
    p = PH[key].get(v)
    return f"{v}（{p}）" if p else v


def values(m):
    """m: マスターの1行（見出し→値）。戻り値: {項目: (値, 目安かどうか)}。値が '' なら空欄"""
    cv = bool(s(m["品種名"]))
    o = {}
    o["学名"] = (s(m["学名（正名）"]), False)
    o["花色"] = (s(m["花色（自社の値）"]) or s(m["花色（分類）"]), False)
    leaf = re.sub(r"^[①-⑳]\s*", "", s(m["葉色（自社の値）"])) or s(m["葉色（分類）"])
    o["葉色"] = (leaf.replace("・", "／"), False)
    o["開花時期"] = (rng(m["花期 開始月"], m["花期 終了月"], "月"), False)
    o["草丈"] = (rng(m["草丈 最小(cm)"], m["草丈 最大(cm)"], "cm"), False)
    o["広がり"] = (rng(m["株張り 最小(cm)"], m["株張り 最大(cm)"], "cm"), False)
    ev = s(m["常緑性"])
    evv = re.sub(r"（.*", "", ev)
    o["常緑性"] = (PH["常緑性"].get(evv, evv), bool(evv) and ((cv and "・種）" in ev) or low(m["常緑性の根拠"])))
    sil, sil2 = s(m["成株シルエット"]), s(m["成株シルエット（種の記述なら）"])
    o["成株シルエット"] = ((sil or sil2) + "型" if (sil or sil2) else "", bool(not sil and sil2))
    o["原産地"] = (re.sub(r"（(Kew|Jelitto)[^（）]*）$", "", s(m["原産地"])), False)
    o["日照条件"] = (s(m["日照"]), False)
    v = s(m["耐寒性"])
    o["耐寒性"] = (phrase("耐寒性", v) if v else "", False)
    v = s(m["耐暑性"])
    o["耐暑性"] = (phrase("耐暑性", v) if v else "", s(m["耐暑性の信頼度"]) == "低")
    sp = cv and species_only(m["暑さ・蒸れ・西日の根拠"])
    for k in ("蒸れ耐性", "西日耐性"):
        v = s(m[k])
        o[k] = (phrase(k, v) if v else "", bool(v) and sp)
    v = s(m["乾燥耐性"])
    o["乾燥耐性"] = (phrase("乾燥耐性", v) if v else "", bool(v) and (low(m["乾燥耐性の出どころ"]) or (cv and species_only(m["乾燥耐性の出どころ"]))))
    v = s(m["土壌水分"])
    o["土壌水分"] = (phrase("土壌水分", v) if v else "", bool(v) and (low(m["土壌水分の根拠"]) or (cv and species_only(m["土壌水分の根拠"]))))
    o["混植適性"] = (s(m["混植適性"]), False)
    o["増え方"] = (s(m["増え方"]), False)
    o["景観構成用途"] = (s(m["景観構成用途"]), False)
    o["機能用途"] = (s(m["機能用途タグ"]), False)
    v = re.sub(r"^[A-E]\s*", "", s(m["管理タイプ"]))
    o["管理タイプ"] = (phrase("管理タイプ", v) if v else "", False)
    v = s(m["管理難易度"])
    o["管理難易度"] = (phrase("管理難易度", v) if v else "", False)
    o["病害虫リスク"] = (re.sub(r"（[^（）]*）$", "", s(m["主な病害虫"])), False)
    a, b = s(m["切り戻し時期（広尾町）"]), s(m["切り戻し時期（関東）"])
    o["刈込時期"] = (f"北海道：{a} / 本州：{b}" if a and b else "", False)
    return {k: (wave(v), f) for k, (v, f) in o.items()}


LI = re.compile(r"<li><b>(.*?)：</b>(.*?)</li>", re.S)


def rewrite(desc, m, stat):
    val = values(m)
    for sec, items in SECTIONS.items():
        mm = re.search(r"(<h3>■ " + sec + r"</h3>\s*<ul>)(.*?)(</ul>)", desc, re.S)
        if not mm:
            stat["まとまりがない:" + sec] += 1
            continue
        old = dict(LI.findall(mm.group(2)))
        lines = []
        for k in items:
            if k in KEEP:
                if k in old:
                    lines.append(f"<li><b>{k}：</b>{old[k]}</li>")
                continue
            v, f = val[k]
            if not v:
                new = NA
                stat["情報なし:" + k] += 1
            else:
                new = html.escape(v, quote=False) + (MEYASU if f else "")
                if f:
                    stat["目安:" + k] += 1
            if k not in old:
                stat["行を足す:" + k] += 1
            elif old[k].strip() != new:
                stat["変わる:" + k] += 1
            lines.append(f"<li><b>{k}：</b>{new}</li>")
        desc = desc[:mm.start(2)] + "\n" + "\n".join(lines) + "\n" + desc[mm.end(2):]
    return desc


def main():
    ws = openpyxl.load_workbook(MASTER, read_only=True).active
    rows = list(ws.iter_rows(values_only=True))
    head = [s(x) for x in rows[1]]
    master = {s(r[0]): dict(zip(head, r)) for r in rows[2:]}
    rs = list(csv.reader(open(CSVP, encoding="cp932", newline="")))
    H = rs[0]
    iD, iK, iN = H.index("商品説明"), H.index("型番"), H.index("商品名")
    stat = collections.Counter()
    res = []
    bad = collections.Counter()
    outrows = []
    IMG = [i for i, x in enumerate(H) if x == "商品画像URL" or re.fullmatch(r"その他画像.+URL", x)]
    assert len(H) == 60 and len(IMG) == 10, (len(H), IMG)
    for r in rs[1:]:
        k = r[iK].strip()
        if k not in master or "plant-info" not in r[iD]:
            continue
        st = collections.Counter()
        new = rewrite(r[iD], master[k], st)
        stat.update(st)
        stat["行"] += 1
        bad_here = set()
        for ch in new:
            try:
                ch.encode("cp932")
            except UnicodeEncodeError:
                bad_here.add(ch)
        for ch in bad_here:
            bad[ch] += new.count(ch)
            new = new.replace(ch, f"&#{ord(ch)};")
        res.append((k, r[iN], r[iD], new, st))
        if CSVOUT:
            rr = list(r)
            rr[iD] = new
            for i in IMG:
                rr[i] = ""
            outrows.append(rr)
    if CSVOUT:
        with open(CSVOUT, "w", encoding="cp932", newline="") as f:
            csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator=chr(13) + chr(10)).writerows(outrows)
    json.dump({"数": dict(sorted(stat.items())), "Shift-JISにない文字": dict(bad),
               "商品ごと": {k: {"目安": sum(v for a, v in st.items() if a.startswith("目安")), "情報なし": sum(v for a, v in st.items() if a.startswith("情報なし"))} for k, nm, old, new, st in res}},
              open(OUT + "/stats.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if SAMPLE:
        sample_html([x for x in res if x[0] in SAMPLE])
    print("書き換える行", stat["行"], "Shift-JISにない文字", dict(bad))


def part(desc):
    """5つのまとまりだけを取り出す"""
    out = []
    for sec in SECTIONS:
        mm = re.search(r"<h3>■ " + sec + r"</h3>\s*<ul>(.*?)</ul>", desc, re.S)
        out.append((sec, LI.findall(mm.group(1)) if mm else []))
    return out


def sample_html(items):
    css = """<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>商品説明の見本</title>
<style>body{font-family:sans-serif;margin:0;padding:16px;background:#fafaf7;color:#222;line-height:1.6}
h1{font-size:1.2em}h2{font-size:1.05em;margin:28px 0 6px;border-left:5px solid #5a8a2e;padding-left:8px}
h3{font-size:.95em;margin:14px 0 4px;color:#3d6b1c}
table{border-collapse:collapse;width:100%;background:#fff;font-size:.9em}
th,td{border:1px solid #ddd;padding:5px 7px;text-align:left;vertical-align:top}
th{background:#f0f7ea}td.k{white-space:nowrap;font-weight:bold;width:6.5em}
tr.chg td.n{background:#fff6d6}tr.na td.n{background:#eee;color:#666}tr.me td.n{background:#e3f0ff}
.leg span{display:inline-block;padding:2px 8px;margin:2px 6px 2px 0;border:1px solid #ddd;font-size:.85em}
.w{overflow-x:auto}</style>"""
    b = [css, "<h1>商品説明の見本（5つのまとまりだけ）</h1>",
         '<p class="leg"><span style="background:#fff6d6">黄：値が変わる</span><span style="background:#e3f0ff">青：（目安）が付く</span><span style="background:#eee">灰：情報なし</span><span>白：今と同じ</span></p>']
    for k, nm, old, new, st in items:
        b.append(f"<h2>{html.escape(k)}　{html.escape(nm)}</h2>")
        for (sec, o), (_, n) in zip(part(old), part(new)):
            od = dict(o)
            b.append(f'<h3>■ {sec}</h3><div class="w"><table><tr><th>項目</th><th>今のページ</th><th>新しいページ</th></tr>')
            for key, v in n:
                ov = od.get(key, "（行なし）").strip()
                cls = "na" if v == NA else ("me" if v.endswith(MEYASU) else ("chg" if ov != v else ""))
                b.append(f'<tr class="{cls}"><td class="k">{key}</td><td>{ov}</td><td class="n">{v}</td></tr>')
            b.append("</table></div>")
    open(OUT + "/sample.html", "w", encoding="utf-8").write("\n".join(b))


main()
