"""2026-11-28 カラーミーショップの「特性が1枚でわかる画像」（その他画像1。550×550 PNG）を、新マスターから作り直す。
使い方: colorme_card.py <新マスター.xlsx> <カラーミーの商品CSV> <出力フォルダ> <型番,型番,…>
- 見た目と決まりは、今の画像12枚（2026-11-28 に見た）から読み取った。作った元の道具は残っていない
- 画像は Edge（headless）で HTML を写して作る。字は Noto Serif JP / Noto Sans JP（パソコンに入っているもの）
- 植物名は、今の商品説明の「植物名」の行のまま
- 寒冷地：耐寒性 強・中の強＝◎／中の中＝○／中の弱＝△／弱・一年草扱い＝×／空欄＝データなし（今の画像と同じ）
- 温暖地：耐暑性と蒸れ耐性の組み合わせ（今の画像と同じ）。強＋強＝◎／強＋中＝◎／強＋弱＝○／中＋強・中＝○／中＋弱＝△／弱＋強・中＝△／弱＋弱＝×
  蒸れ耐性が空欄のとき（今の画像にはない場合。新しく決めた）：耐暑性だけで 強＝◎／中＝○／弱＝△。耐暑性が空欄＝データなし
  耐暑性の信頼度が 低 のときは（目安）を付ける
- 大きさの呼び名（草丈の最大）：〜19 超小型／〜44 小型／〜69 中型／〜149 大型／150〜 超大型（境い目は今の画像からの推定）
- 出力フォルダはリポジトリの外にする
"""
import csv, html, os, re, subprocess, sys, time
import openpyxl

MASTER, CSVP, OUT, NOS = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4].split(",")
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
os.makedirs(OUT, exist_ok=True)


def s(v):
    return "" if v is None else str(v).strip()


def rng(a, b, unit=""):
    a, b = s(a), s(b)
    if not a and not b:
        return ""
    if not b or a == b:
        return f"{a or b}{unit}"
    return f"{a}～{b}{unit}"


COLD = {"強": ("◎", "北海道でも安心して<br>越冬可能"), "中の強": ("◎", "北海道でも安心して<br>越冬可能"),
        "中の中": ("○", "防寒対策があれば<br>越冬可能"), "中の弱": ("△", "寒さにやや弱い<br>品種です"),
        "弱": ("×", "寒冷地では越冬が<br>難しい品種"), "一年草扱い": ("×", "寒冷地では越冬が<br>難しい品種")}
T_A = "暑さ・蒸れにも<br>強く育ちます"
T_B = "暑さに強く夏も<br>安定して育ちます"
T_C = "夏の蒸れに注意すれば<br>育ちます"
T_D = "暑さ・蒸れに弱く<br>夏越しが難しい"
T_E = "温暖地での栽培は<br>難しい品種です"
WARM = {("強", "強"): ("◎", T_A), ("強", "中"): ("◎", T_B), ("強", "弱"): ("○", T_C), ("強", ""): ("◎", T_B),
        ("中", "強"): ("○", T_C), ("中", "中"): ("○", T_C), ("中", "弱"): ("△", T_D), ("中", ""): ("○", T_C),
        ("弱", "強"): ("△", T_D), ("弱", "中"): ("△", T_D), ("弱", "弱"): ("×", T_E), ("弱", ""): ("△", T_D)}
TIP = {"A": "大きな手入れをしなくても育ちます", "B": "花が終わったら刈り込むだけ", "C": "梅雨前に切り戻すと夏を乗り越えます",
       "D": "毎年植え替えや株更新が必要です", "E": "広がりを抑える工夫が必要です"}


def mark(m, c1, c2):
    if m == "◎":
        return f'<svg width="76" height="76" viewBox="0 0 76 76"><circle cx="38" cy="38" r="34" fill="none" stroke="{c1}" stroke-width="4"/><circle cx="38" cy="38" r="20" fill="none" stroke="{c1}" stroke-width="4"/></svg>'
    if m == "○":
        return f'<svg width="76" height="76" viewBox="0 0 76 76"><circle cx="38" cy="38" r="33" fill="none" stroke="{c2}" stroke-width="4"/></svg>'
    if m == "△":
        return f'<svg width="76" height="76" viewBox="0 0 76 76"><path d="M38 8 L72 68 L4 68 Z" fill="none" stroke="{c2}" stroke-width="4" stroke-linejoin="round" opacity=".55"/></svg>'
    if m == "×":
        return '<svg width="76" height="76" viewBox="0 0 76 76"><path d="M14 14 L62 62 M62 14 L14 62" stroke="#b9b9b9" stroke-width="7"/></svg>'
    return '<svg width="76" height="76" viewBox="0 0 76 76"><rect x="10" y="33" width="56" height="8" fill="#c4c4c4"/></svg>'


CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:550px;height:550px;overflow:hidden;background:#fff;font-family:'Noto Sans JP',sans-serif;color:#333}
.hd{height:88px;background:#3b5b2a;color:#fff;font-family:'Noto Serif JP',serif;font-weight:700;padding:0 24px;display:flex;align-items:center;line-height:1.3;letter-spacing:.04em}
.two{display:flex;height:232px}
.two>div{width:275px;text-align:center;padding-top:22px}
.cold{background:#e9f0fa}.warm{background:#fbeee3}
.lab{font-size:16px;color:#666;margin-bottom:12px}
.txt{font-size:19.5px;font-weight:500;line-height:1.45;margin-top:6px;color:#3a3a3a}
.me{font-size:13px;color:#777;font-weight:400}
.three{display:flex;height:150px;border-top:1px solid #e6e6e6}
.three>div{flex:1;text-align:center;padding-top:20px;border-left:1px solid #e6e6e6}
.three>div:first-child{border-left:0}
.ic{font-size:28px;line-height:1;height:34px}
.k{font-size:15px;color:#666;margin-top:6px}
.v{font-weight:700;color:#222;margin-top:2px;white-space:nowrap}
.sub{font-size:11.5px;color:#555;margin-top:1px}
.ft{height:80px;background:#f3f0e8;border-top:1px solid #e3dfd3;display:flex;align-items:center;justify-content:space-between;padding:0 24px}
.tip{font-family:'Noto Serif JP',serif;font-size:13.5px;color:#444}
.pill{border:2px solid #3b5b2a;color:#3b5b2a;font-weight:700;font-size:13.5px;padding:9px 16px;background:#fff;white-space:nowrap}
"""


def fit(text, base, limit):
    n = max(len(x) for x in text.split("<br>")) or 1
    return min(base, int(limit / n))


def card(m, name):
    cold = COLD.get(s(m["耐寒性"]), ("―", "データなし"))
    heat, mure = s(m["耐暑性"]), s(m["蒸れ耐性"])
    warm = WARM.get((heat, mure), ("―", "データなし"))
    me = '<div class="me">（目安）</div>' if heat and s(m["耐暑性の信頼度"]) == "低" else ""
    bloom = rng(m["花期 開始月"], m["花期 終了月"], "月") or "情報なし"
    h = rng(m["草丈 最小(cm)"], m["草丈 最大(cm)"], "cm") or "情報なし"
    w = rng(m["株張り 最小(cm)"], m["株張り 最大(cm)"], "cm")
    hmax = s(m["草丈 最大(cm)"]) or s(m["草丈 最小(cm)"])
    size = ""
    if re.fullmatch(r"\d+(\.\d+)?", hmax):
        x = float(hmax)
        size = "超小型" if x < 20 else "小型" if x < 45 else "中型" if x < 70 else "大型" if x < 150 else "超大型"
    sun = s(m["日照"]).replace("〜", "～") or "情報なし"
    tip = TIP.get(s(m["管理タイプ"])[:1], "")
    pos = re.search(r"前景|中景|後景", s(m["景観構成用途"]))
    lines = [html.escape(x.strip()) for x in re.split(r"[\r\n]+", name.strip()) if x.strip()]
    title = "<br>".join(lines[:2])
    tsize = fit(title, 26, 500)
    sub = "　".join(x for x in ((f"広がり {w}" if w else ""), size) if x)
    return f"""<!doctype html><meta charset="utf-8"><style>{CSS}</style>
<div class="hd" style="font-size:{tsize}px"><div>{title}</div></div>
<div class="two">
<div class="cold"><div class="lab">🌸 寒冷地（北海道・東北）</div>{mark(cold[0], "#2f6fb7", "#5b9bd5")}<div class="txt">{cold[1]}</div></div>
<div class="warm"><div class="lab">☀️ 温暖地（関東～九州）</div>{mark(warm[0], "#c8571b", "#e07b39")}<div class="txt">{warm[1]}</div>{me}</div>
</div>
<div class="three">
<div><div class="ic">🌸</div><div class="k">開花時期</div><div class="v" style="font-size:{fit(bloom, 27, 165)}px">{bloom}</div></div>
<div><div class="ic" style="color:#555">✥</div><div class="k">草丈 / 広がり</div><div class="v" style="font-size:{fit(h, 27, 300)}px">{h}</div><div class="sub">{sub}</div></div>
<div><div class="ic">☀️</div><div class="k">日照</div><div class="v" style="font-size:{fit(sun, 27, 150)}px">{sun}</div></div>
</div>
<div class="ft"><div class="tip">{"🌿　" + tip if tip else ""}</div>{f'<div class="pill">お庭の{pos.group(0)}向き</div>' if pos else ""}</div>"""


def main():
    ws = openpyxl.load_workbook(MASTER, read_only=True).active
    rows = list(ws.iter_rows(values_only=True))
    head = [s(x) for x in rows[1]]
    master = {s(r[0]): dict(zip(head, r)) for r in rows[2:]}
    rs = list(csv.reader(open(CSVP, encoding="cp932", newline="")))
    H = rs[0]
    iD, iK = H.index("商品説明"), H.index("型番")
    for r in rs[1:]:
        k = r[iK].strip()
        if k not in NOS or k not in master:
            continue
        mm = re.search(r"<li><b>植物名：</b>(.*?)</li>", r[iD], re.S)
        name = html.unescape(re.sub(r"<[^>]+>", "\n", mm.group(1))) if mm else r[H.index("商品名")]
        hp = os.path.abspath(f"{OUT}/{r[0]}_{k}.html")
        pp = os.path.abspath(f"{OUT}/{r[0]}_{k}.png")
        open(hp, "w", encoding="utf-8").write(card(master[k], name))
        if os.path.exists(pp):
            os.remove(pp)
        subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                        "--window-size=550,550", f"--screenshot={pp}", "file:///" + hp.replace("\\", "/")],
                       capture_output=True, timeout=90)
        for _ in range(60):  # Edge は書き終わる前に戻ることがあるので待つ
            if os.path.exists(pp) and os.path.getsize(pp) > 1000:
                break
            time.sleep(0.5)
        print(k, r[0], os.path.exists(pp))


main()
