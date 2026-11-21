"""暑さに弱い品種の確認ページ（非公開の Artifact）を作る。入力は heat_page_data.json（まとめの表から抜き出したもの。価格・在庫数は入っていない）"""
import html
import json
import os
import re

S = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(S + "/heat_page_data.json", encoding="utf-8"))
# 22品種を、同じ種・同じ根拠ごとにまとめる。(見出し, 下書きのID, おぎはらの値の出どころ, 欧米の文献の内容〔日本語の要約〕)
GROUPS = [
 ("カンパニュラ プンクタータ（ホタルブクロの仲間）", ["C22", "C18", "C21", "C19", "C17", "C20"],
  "おぎはらは 'ウェディングベル' と 'チェリーベル' を 強 としています。ほかの4品種は、おぎはらにページがなく、同じ種の値を使っています。",
  "MBG（米国ミズーリ植物園）：夏の暑い地域では半日陰を好む。夜の気温が21℃（華氏70度）を下回らない日が続く地域では、よく育たない。"),
 ("リグラリア デンタータ", ["Lg02", "Lg01"],
  "おぎはらにこの2品種のページはなく、同じ種の4品種（'ブリットマリー クロフォード' など）がどれも 強 なので、その値を使っています。",
  "MBG：夏が涼しい気候でいちばんよく育つ。高温多湿の夏の地域では、午後に日かげになる場所がよい。水が足りていても、暑い地域では日中に葉がしおれることがある。"),
 ("ロニセラ ペリクリメナム（ハニーサックル）", ["Lo04", "Lo03"],
  "おぎはらは 'セロチナ' を 強 としています。'ハニーベビー' はページがなく、同じ種の値を使っています。",
  "MBG：夏の暑い地域では、午後に日かげになる場所がよい。高温多湿の夏には、うどんこ病・斑点病が出やすい。夏が涼しい気候向きの低木。"),
 ("フェスツーカ グラウカ", ["Fe03", "Fe02"],
  "おぎはらは、種（フェスツーカ グラウカ）のページで 強 としています。",
  "MBG：高温多湿の夏には、葉がかなり傷むことがある。NC State（米国ノースカロライナ州立大）：短命で、暑さ・湿気に耐えない。（'ボルダーブルー' のページには「根づけば暑さと乾燥に耐える」とも書いてあります）"),
 ("クナウティア マケドニカ", ["Kt01", "Kt03"],
  "おぎはらにこの2つのページはなく、同じ種の2品種（'マース ミジェット' など）が 強 なので、その値を使っています。",
  "MBG：米国深南部の暑さと湿気では弱ることが多く、夏の暑さで茎がねじれて倒れやすい。"),
 ("モリニア カエルレア 'バリエガータ'", ["Mo06"], "おぎはらは、この品種を 強 としています。",
  "NC State：夏が涼しい気候でいちばんよく育つ。夏の暑い気候ではよく育たない。MBG：夏の暑い気候では花が減ることがある。"),
 ("バレリアナ オフィシナリス（バレリアン）", ["Va01"], "おぎはらは 強 としています。",
  "MBG：夏が涼しい気候でよく育つ。NC State：涼しい気候と多い雨を好み、米国では主に北部に広がっている。"),
 ("トロリウス チネンシス 'ゴールデンクィーン'", ["Tr01"], "おぎはらは、この品種を 強 としています。",
  "MBG：涼しい気候の植物。乾いた土と、高温多湿の夏を嫌う。USDA ゾーン7（6とする人もいる）より南には勧めない。"),
 ("カラミンサ ネペタ 'ブルークラウド'", ["Ca02"], "おぎはらは、種（カラミンサ ネペタ）のページで 強 としています。",
  "MBG：米国深南部（USDA ゾーン7より南）ではよく育たない。高温多湿の夏には葉が傷むことがある。"),
 ("ビバーナム 'オノンダガ'", ["Vu02"], "おぎはらは、この品種を 強 としています。",
  "NC State：いろいろな土に合うが、暑さには強くない。MBG：USDA ゾーン7より南には勧めない。"),
 ("ムクデニア 'カラスバ'（タンチョウソウ）", ["Mk02"], "おぎはらは、この品種を 強 としています（暖地の日照は「日向〜やや半日陰」）。",
  "MBG：米国深南部の高温多湿の夏では弱ることが多く、午後の日かげか木もれ日を好む。"),
 ("カレックス 'エバーゴールド'", ["X07"], "おぎはらは、この品種を 強 としています。", "MBG：高温多湿の夏の気候を嫌う。"),
 ("スティパ テヌイッシマ（エンジェルヘアー）", ["Su02"], "おぎはらは 強 としています。", "NC State：米国南東部の高温多湿の条件ではよく育たない。"),
]
by = {r["下書きのID"]: r for r in D["g23"]}
assert sorted(i for g in GROUPS for i in g[1]) == sorted(by), set(by) ^ {i for g in GROUPS for i in g[1]}
e = html.escape


def name(r):
    return re.sub(r"\s+", " ", str(r["植物名"]))


def chip(label, v, cls=""):
    return f'<span class="chip {cls}"><i>{label}</i>{e(str(v)) if v else "—"}</span>'


out = []
for n, (title, ids, ogi, west) in enumerate(GROUPS, start=1):
    items = "".join(
        f'<li><b>{e(name(by[i]))}</b><span class="no">商品番号 {by[i]["商品番号"]}{"・在庫あり" if by[i]["在庫あり"] else "・在庫なし"}・信頼度 {by[i]["耐暑性の信頼度"]}</span></li>' for i in ids)
    r0 = by[ids[0]]
    chips = chip("蒸れ", r0["蒸れ耐性"], "warn" if r0["蒸れ耐性"] == "弱" else "") + chip("西日", r0["西日耐性"])
    radios = "".join(
        f'<label class="opt"><input type="radio" name="q{n}" id="q{n}{k}" value="{k}"><span><b>{k}</b>{t}</span></label>'
        for k, t in (("A", "強 のまま"), ("B", "中 にする"), ("C", "弱 にする")))
    out.append(f'''<section class="q" data-q="{n}">
<h3><span class="num">{n}</span>{e(title)}</h3>
<ul class="plants">{items}</ul>
<div class="chips">{chip("耐暑性（今の値）", "強", "now")}{chip("欧米の文献だけなら", "弱", "warn")}{chips}</div>
<dl class="ev"><dt>おぎはら植物園</dt><dd>{e(ogi)}</dd><dt>欧米の文献</dt><dd>{e(west)}</dd></dl>
<div class="opts" role="radiogroup" aria-label="{e(title)} の耐暑性">{radios}</div>
<label class="memo"><span>備考（自由に）</span><textarea id="m{n}" rows="1" placeholder="例：うちでは夏も問題ない"></textarea></label>
</section>''')
QHTML = "\n".join(out)


def rows(lst, kind):
    lst = sorted(lst, key=lambda r: (str(r["学名（正名）"]), r["商品番号"]))
    o = []
    for r in lst:
        no = r["商品番号"]
        ev = [x for x in str(r["暑さ・蒸れ・西日の根拠"] or "").split("\n") if x.strip()][:5]
        evh = "".join(f"<li>{e(x[:260])}</li>" for x in ev) or "<li>（根拠の文は記録なし）</li>"
        both = r["耐暑性"] == "弱" and r["蒸れ耐性"] == "弱"
        o.append(f'''<li class="row" data-no="{no}" data-kind="{kind}" data-stock="{1 if r["在庫あり"] else 0}">
<div class="rowhead"><div class="nm"><b>{e(name(r))}</b><span class="no">{e(str(r["学名（正名）"]))}・商品番号 {no}{"" if r["在庫あり"] else "・在庫なし"}</span></div>
<label class="flag"><input type="checkbox" id="f{kind}{no}"><span>違う</span></label></div>
<div class="chips">{chip("耐暑性", r["耐暑性"], "warn" if r["耐暑性"] == "弱" else "")}{chip("蒸れ", r["蒸れ耐性"], "warn" if r["蒸れ耐性"] == "弱" else "")}{chip("西日", r["西日耐性"])}{'<span class="chip both">暑さも蒸れも弱</span>' if both else ""}</div>
<details><summary>根拠の文（{e(str(r["耐暑性の決め方"] or "欧米の文献"))}）</summary><ul class="src">{evh}</ul></details>
<label class="memo" hidden><span>どう違うか（例：中でよい）</span><textarea id="n{kind}{no}" rows="1"></textarea></label>
</li>''')
    return "\n".join(o)


HW, MW = rows(D["hw"], "h"), rows(D["mw"], "m")
PAGE = open(S + "/heat_page_template.html", encoding="utf-8").read()
PAGE = PAGE.replace("{{QUESTIONS}}", QHTML).replace("{{HW}}", HW).replace("{{MW}}", MW)
PAGE = PAGE.replace("{{NQ}}", str(len(GROUPS))).replace("{{N22}}", str(len(by))).replace("{{NH}}", str(len(D["hw"]))).replace("{{NM}}", str(len(D["mw"])))
PAGE = PAGE.replace("{{NHS}}", str(sum(1 for r in D["hw"] if r["在庫あり"]))).replace("{{NMS}}", str(sum(1 for r in D["mw"] if r["在庫あり"])))
open(S + "/atsusa_kakunin.html", "w", encoding="utf-8", newline="\n").write(PAGE)
print(len(PAGE), "文字")
