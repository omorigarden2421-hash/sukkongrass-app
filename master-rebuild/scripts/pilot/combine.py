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
BL = json.load(open("hokkaido_bluelist.json", encoding="utf-8")) if os.path.exists("hokkaido_bluelist.json") else {}
KN = json.load(open("kew_native.json", encoding="utf-8")) if os.path.exists("kew_native.json") else {}
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
# リストの学名（種）ごと。品種名・変種の書き方の違いは見ない（種で当てる）
def sp_key(name):
    """学名 → 「属 種小名」（交配の印 x・× と品種名は除く）。種小名がなければ None"""
    w = [x for x in re.sub(r"'.*$", "", str(name or "")).split() if x not in ("x", "×")]
    return " ".join(w[:2]) if len(w) >= 2 and re.fullmatch(r"[a-z-]+", w[1]) else None


IAS_SP = {sp_key(d_["リストの学名"]): d_ for d_ in ias.values() if sp_key(d_["リストの学名"])}


# 管理タイプの見直し（2026-11-21）: 品種ごとに、切り戻し・手入れの文を読んで決め直した結果（mgmt_review.json。商品番号 → type・codes・confidence・reason・quote）。
# あれば、言い回しの照合で決めた値より優先する
REVIEW = {str(x["no"]): x for x in json.load(open("mgmt_review.json", encoding="utf-8"))} if os.path.exists("mgmt_review.json") else {}
# 確認ページへのユーザーの回答（scripts/tools/apply_answers.py が作る）。文献より優先する
ANS = json.load(open("user_answers.json", encoding="utf-8")) if os.path.exists("user_answers.json") else {"耐暑性": {}, "違うとの指摘": {}, "管理タイプ": {}}
# 食い違いの回答は {"商品番号": {項目: {...}}}、外したものの確認は "商品番号-項目" のキー。ここでタプルに直す
ANS.setdefault("食い違い", {})
ANS["外したものの確認"] = {tuple(k.split("-", 1)) for k in ANS.get("外したものの確認", {})}
# 未決の学名の確認（2026-11-24）。回答は user_answers.json の「未決」: {下書きのID: {選択, メモ, 日付}}
FU05 = {"A": "Fuchsia magellanica var. gracilis 'Variegata'", "B": "Fuchsia magellanica var. macrostema 'Variegata'"}
# Ep01 は選んだ和名を YList の標準（ヒヨドリバナは広義）の学名に当てる。2026-11-24 に YList（ylist.info の簡易検索）で確かめた。pass は YList の番号
EP01 = {"A": ("Eupatorium japonicum", "フジバカマ", "5590"), "B": ("Eupatorium × arakianum", "サワフジバカマ", "23975"),
        "C": ("Eupatorium makinoi", "ヒヨドリバナ", "7096。YList では広義")}


def rhs_name(s):
    """「学名（RHS）」の列の文字 → RHS の正名だけ（説明・[Accepted]・(v) などを除く）"""
    s = re.sub(r"（.*$", "", s or "", flags=re.S)
    s = re.sub(r"\s*\[[A-Za-z ]+\]\s*$", "", s).strip()
    return re.sub(r"\s*\((v|d|f|m|s)\)$", "", s).strip()


def name_answer(id_, a, adopted, note, ryu, wa, d, master_name):
    """未決の学名の確認の回答を当てる。返すのは (学名, 学名のメモ, 流通名・別名, 和名)"""
    v, memo, day = a.get("選択"), a.get("メモ"), a.get("日付")
    head = f"ユーザーの確認（{day}）：" + (f"{v}" if v else "選択なし") + (f"（メモ：{memo}）" if memo else "")

    def out(changed):
        # 学名を変えたときは、前のメモ（「今の学名のまま」など）を「前のメモ」として後ろに残す
        return "；".join(x for x in (head, note and (f"前のメモ：{note}" if changed else note)) if x)
    if id_ == "Fu05":
        if v in FU05:
            adopted = FU05[v]
            if v == "B":
                head += "。文献は RHS の var. gracilis のページを当てたまま【要見直し】"
        return adopted, out(v in FU05), ryu, wa
    if id_ == "Ep01":
        if v in EP01:
            adopted, wa, ps = EP01[v]
            head += f"。{wa}の白花。学名は YList の {wa}（{ps}）。種の文献はまだ当てていない【要見直し】"
        elif v == "D":
            head += "。種未確定"
        return adopted, out(v in EP01), ryu, wa
    if v in ("B", "C"):
        new = rhs_name(d.get("学名（RHS）"))
        if new:
            g0, ep0, _ = split_name(master_name)
            g1, ep1, cv1 = split_name(new)
            hyb = lambda e: re.sub(r"^[x×]\s*", "× ", e) if e else e  # 交配の印は x と × のどちらでも同じ
            if v == "C":
                q0 = re.findall(r"'([^']+)'", master_name)  # 'Pink Jewel'('Rosa Juwel') のような書き方もあるので、最初の引用だけ
                keep = q0[0] if q0 and q0[0] != cv1 else master_name  # 品種名が違えば今の品種名、種だけが違えば今の学名を流通名に残す
                ryu = "、".join(x for x in dict.fromkeys(((ryu or "").split("、") if ryu else []) + [keep]) if x)
            if (g0, hyb(ep0)) != (g1, hyb(ep1)):  # 種が変わった。和名と種の文献は前の種のものなので、当て直しが要る
                wa = None
                head += "。種が変わったので和名は空欄にした。種の文献は前の種のまま【要見直し】"
            adopted = new
            return adopted, out(True), ryu, wa
        head += "。RHS の正名が読めないので今のまま【要見直し】"
    return adopted, out(False), ryu, wa


MK = ANS.get("未決", {})
# 広がり方の総当たりの読み直し（2026-11-24。商品番号 → こぼれ種・地下茎・混植と決め手）。段階は下書き（assemble）で使い済み。ここでは混植適性の確かめに使う
SPREAD_RR = json.load(open("spread_reread.json", encoding="utf-8")) if os.path.exists("spread_reread.json") else {}
# 矛盾の洗い出しで、段階 3 なのに侵略的でなかった品種の読み直し（2026-11-24 ユーザー「おすすめでお願い」）。商品番号 → {列: (値, 理由)}
_MON = "NC State・種「地下の走出枝で急速に広がる」は速く広がる話で、侵略的・はびこるとは書いていない（RULES.md の 2：spreads／vigorous spreader）。3 → 2"
_SPI = "こぼれ種ではびこる記述（NC State・MBG）は種の記述だけ。品種がこぼれ種で増えるかは分からないので空欄（2026-11-19 のスピレア 'Goldflame' の決定と同じ）。3 → 空欄"
_PEN = "NC State・種の文は「種が風や衣服で運ばれて広がる」で、地下茎の話ではない（読み違い）。3 → 空欄"
LV_FIX = {
    "344": {"地下茎で広がる程度(0-3)": (2, _MON)}, "615": {"地下茎で広がる程度(0-3)": (2, _MON)},
    "1264": {"地下茎で広がる程度(0-3)": (2, _MON)}, "1265": {"地下茎で広がる程度(0-3)": (2, _MON)},
    "1202": {"地下茎で広がる程度(0-3)": (2, "NC State・種「マット状に速く広がる」は速く広がる話で、侵略的とは書いていない。3 → 2")},
    "1979": {"地下茎で広がる程度(0-3)": (None, _PEN)}, "1585": {"地下茎で広がる程度(0-3)": (None, _PEN)},
    "47": {"こぼれ種の量(0-3)": (None, _SPI)}, "805": {"こぼれ種の量(0-3)": (None, _SPI)}, "1484": {"こぼれ種の量(0-3)": (None, _SPI)},
}
# 広がり方の読み直しの決定（2026-11-24 ユーザー「おすすめ」）。問2: 段階 3 なのに E でなかった品種。
# 除外: 29 アルケミラ・1979 ペニセタム（ユーザーの決定で 強い）、種の記述だけの品種（スピレア 'Goldflame' の決定と同じ: 266, 351, 946, 1009, 1987, 47, 805, 1484）
MIX_E3 = {"79", "131", "675", "684", "894", "1480", "1564", "1625", "1627", "1684", "1685", "1781", "1822", "1974"}
MIX_STRONG_NOWAY = {
    "289": "RHS・品種「Can be invasive」とあるが、どう広がるかは書いていない。強い（配置注意）",
    "1135": "NC State・種「逃げ出した雑草（escaped weed）」とあるが、どう広がるかは書いていない。強い（配置注意）",
}
# 花色（分類）の総当たりの読み直し（2026-11-24。商品番号 → 花色・決め手・食い違い・確かさ・メモ。scripts/tools/color_reread_note.md）
SD_COLOR = [("白", "白"), ("ピンク", "ピンク|桃|ローズ|赤紫"), ("青・紫", "青|紫|藤|ラベンダー|すみれ"), ("黄", "黄|クリーム|レモン|ｸﾘｰﾑ"), ("赤", "赤|紅|緋|ワイン|ﾜｲﾝ"),
            ("オレンジ・アプリコット", "オレンジ|橙|アプリコット|杏|サーモン|銅")]
LEAF_PHOTO = json.load(open("leaf_photo_check.json", encoding="utf-8")) if os.path.exists("leaf_photo_check.json") else {}
LEAF_RR = json.load(open("leaf_reread.json", encoding="utf-8")) if os.path.exists("leaf_reread.json") else {}
DRY_RR = json.load(open("dry_reread.json", encoding="utf-8")) if os.path.exists("dry_reread.json") else {}
EVER_RR = json.load(open("ever_reread.json", encoding="utf-8")) if os.path.exists("ever_reread.json") else {}
SOIL_RR = json.load(open("soil_reread.json", encoding="utf-8")) if os.path.exists("soil_reread.json") else {}
CUT_RR = json.load(open("cut_reread.json", encoding="utf-8")) if os.path.exists("cut_reread.json") else {}
POLL_RR = json.load(open("poll_reread.json", encoding="utf-8")) if os.path.exists("poll_reread.json") else {}
PROP_RR = json.load(open("prop_reread.json", encoding="utf-8")) if os.path.exists("prop_reread.json") else {}
WINTER_RR = json.load(open("winter_reread.json", encoding="utf-8")) if os.path.exists("winter_reread.json") else {}
# 2026-11-26 ユーザー「読みやすく整えて」: winter_text() の下書きを、事実を足さず・落とさずに読みやすく整えた文（scripts/tools/winter_polish_note.md）
WINTER_POLISH = json.load(open("winter_polish.json", encoding="utf-8")) if os.path.exists("winter_polish.json") else {}
SPECIES_CHECK = json.load(open("species_check.json", encoding="utf-8")) if os.path.exists("species_check.json") else {}


def snow_note(f, hk):
    """北海道の文に足す「雪が少ない年は」の一言（2026-11-27 のユーザーの決定）。
    雪のない寒さだけの防寒・雪の少ない地域の記録を、北海道の文の最後に一言で残す。"""
    if not f:
        return None
    rec = f.get("雪・寒冷地") or ""
    parts = [p for p in rec.split("。") if re.search(r"Kahlfrost|雪のない|雪がない|雪の少ない|雪が少ない|雪の覆いがない|雪に覆われない", p)]
    out = []
    def add(s):
        if s not in out:
            out.append(s)
    for p in parts:
        if "高植え" in p:
            add("高植えにするとよいという文献があります")
        elif "マルチ" in p:
            add("冬に株元をマルチで覆うと安心です")
        elif "葉が焼け" in p:
            add("雪に覆われないと、厳しい寒さで葉が焼けて傷みやすくなります")
        elif "−18℃" in p:
            add("雪の覆いがないまま −18℃ を下回ると冬を越せないことがある、という記録があります")
        elif "日差し" in p:
            add("冬の日差しと雪のない凍結から守ると安心です")
        elif re.search(r"傷む|弱い", p):
            add("雪のない強い冷え込みで傷みやすくなります")
        elif "日よけ" in p:
            add("雪のない強い冷え込みに備えて、防寒や冬の日よけをすると安心です")
        else:
            add("雪のない強い冷え込みに備えて、防寒をすると安心です")
    if not out and f.get("防寒") == "雪がない寒さで必要":
        add("雪のない強い冷え込みに備えて、防寒や冬の日よけをすると安心です" if "Sonnenschutz" in (f.get("決め手") or "") else "雪のない強い冷え込みに備えて、防寒をすると安心です")
    if not out or re.search(r"雪のない|雪が少ない", hk or ""):
        return None
    return "雪が少ない年は、" + "。また、".join(out) + "。"


WOODY_GENERA = set("Hydrangea Cornus Spiraea Lonicera Rosa Calluna Euonymus Parthenocissus Ampelopsis Hedera Physocarpus Viburnum".split())  # 2026-11-26 に文を直した低木・つるの属


def winter_text(f, ever, soil, cold, sci=None):
    """冬の手入れ（北海道）・（温暖地）の文を、文献から抜き出した事実（winter_reread.json）と、読み直した常緑性・土壌水分、
    今のマスターの耐寒性から作る（2026-11-26 の決定。DECISIONS.md）。推測の文は足さない"""
    f = f or {}
    ev = (ever or "").split("（")[0]
    hk, wm, why = [], [], []
    woody = bool(sci) and sci.split()[0] in WOODY_GENERA  # 低木・つるは「地上部が枯れる」「枯れた地上部を切る」と書かない
    if ev == "常緑":
        s = "冬も葉が残る常緑性です。"
    elif ev == "半常緑":
        s = "冬に葉の一部が残る半常緑性です。"
    elif ev == "落葉":
        s = "冬は葉を落とします。" if woody else "冬は地上部が枯れます。"
    else:
        s = None
    if s:
        hk.append(s); wm.append(s); why.append(f"常緑性：{ever}")
    fall = f.get("秋の地上部")
    if fall == "秋に切る":
        hk.append("晩秋、地上部が枯れたら地際で切ります。"); wm.append("晩秋、地上部が枯れたら地際で切ります。")
    elif fall == "春まで残す" and woody:
        hk.append("剪定は雪解け後、新芽が出る前に行います。"); wm.append("剪定は早春（2〜3月）、新芽が出る前に行います。")
    elif fall == "春まで残す":
        hk.append("枯れた地上部は冬のあいだ残し、雪解け後、新芽が出る前に切ります。")
        wm.append("枯れた地上部は冬のあいだ残し、早春（2〜3月）、新芽が出る前に切ります。")
    elif fall == "切らない":
        hk.append("秋に刈り込まず、葉はそのまま冬を越させます。"); wm.append("秋に刈り込まず、葉はそのまま冬を越させます。")
    elif fall == "どちらでも":
        hk.append("枯れた地上部は、晩秋か雪解け後に切ります。"); wm.append("枯れた地上部は、晩秋か早春に切ります。")
    if fall:
        why.append(f"秋の地上部：{fall}")
    spring = (f.get("春の手入れ") or "").rstrip("。")
    if spring:
        hk.append(f"春の手入れ：{spring}。"); wm.append(f"春の手入れ：{spring}。")
    look = re.sub(r"（Wintersteher）|（Winteraspekt）", "", f.get("冬の姿") or "").rstrip("。")
    if look:
        hk.append(f"冬の姿：{look}。"); wm.append(f"冬の姿：{look}。")
    prot = f.get("防寒")
    if prot == "必要":
        hk.append("文献では、冬に株元をマルチで覆うなどの防寒を勧めています。"); wm.append("文献では、冬に株元をマルチで覆うなどの防寒を勧めています。")
    elif prot == "寒冷地で必要":
        hk.append("寒い地域では、冬に株元をマルチで覆うなどの防寒を勧める文献があります。")
        wm.append("防寒を勧めるのは寒い地域だけで、温暖地では特に要りません。")
    elif cold in ("中の弱", "弱"):
        hk.append(f"寒さにやや弱い（耐寒性：{cold}）ので、冬は株元を覆うなどの防寒をします。")
    if prot:
        why.append(f"防寒：{prot}" + ("（北海道の文には「雪が少ない年は」の一言で書く。2026-11-27）" if prot == "雪がない寒さで必要" else ""))
    elif cold in ("中の弱", "弱"):
        why.append(f"防寒：文献に記述なし。今のマスターの耐寒性が {cold} なので北海道の文に書いた")
    if f.get("冬の過湿") == "注意":
        hk.append("冬の過湿に弱いので、水はけのよい場所に植え、雪解け水がたまる場所は避けます。")
        wm.append("冬の過湿に弱いので、水はけのよい場所に植えます。")
        why.append("冬の過湿：注意")
    elif soil == "排水必須":
        hk.append("水はけの悪い土では傷みやすいので、水はけのよい場所に植えます。")
        wm.append("水はけの悪い土では傷みやすいので、水はけのよい場所に植えます。")
        why.append("土壌水分：排水必須")
    cold_note = [x for x in re.split(r"[／;；]", f.get("雪・寒冷地") or "") if x.strip() and not re.search(r"Kahlfrost|雪のない|雪がない|雪の少ない|雪が少ない|雪の覆いがない|雪に覆われない", x)]
    if cold_note:
        hk.append("寒冷地での記録：" + "。".join(x.strip().rstrip("。") for x in cold_note) + "。")
    return "".join(hk) or None, "".join(wm) or None, why
LEAF_MASTER = {"① グリーン系": "グリーン系", "② ゴールド／ライム系": "ゴールド・ライム系", "③ ブルー系": "ブルー系", "④ シルバー系": "シルバー系",
               "⑤ パープル／ブラック系": "パープル・ブラック系", "⑥ ブロンズ／レッド系": "ブロンズ・レッド系", "⑦ 斑入り": "斑入り", "⑧ 季節変化型": "季節変化型"}
COLOR_RR = json.load(open("color_reread.json", encoding="utf-8")) if os.path.exists("color_reread.json") else {}
MIX_FIX = {"1524": "環境省の外来種リスト（第２版）の防除検討外来種（シロガネヨシ）。MBG・種「暖かい冬の地域でこぼれ種で侵略的に増える」。侵略的・隔離推奨型"}
# 食い違いの印の仕分け（scripts/tools/kuichigai_classify.py）。外したものの理由
KR_DROP = {}
if os.path.exists("kuichigai_review.json"):
    for _x in json.load(open("kuichigai_review.json", encoding="utf-8")):
        for _i in _x["外す"]:
            KR_DROP[(str(_x["商品番号"]), _i["項目"])] = _i["外した理由"]


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
 ("科名", "文献"), ("和名", "文献（YList）"), ("流通名・別名", "今のマスター"), ("花色（分類）", "文献（読み直し）"), ("花色（詳細）", "文献"),
 ("花期 開始月", "今のマスター"), ("花期 終了月", "今のマスター"), ("草丈 最小(cm)", "今のマスター"), ("草丈 最大(cm)", "今のマスター"), ("草丈 括弧内の値", "今のマスター"), ("草丈（文献）", "文献（見比べ用）"), ("草丈の食い違い", "自動"), ("花期（文献）", "文献（見比べ用）"), ("花期の食い違い", "自動"),
 ("株張り 最小(cm)", "今のマスター（空欄は文献）"), ("株張り 最大(cm)", "今のマスター（空欄は文献）"), ("株張り（文献）", "文献（見比べ用）"), ("株張りの食い違い", "自動"), ("葉色（分類）", "文献（読み直し）"), ("葉の特徴", "文献（用語の照合）"), ("紅葉・冬の葉", "文献"), ("香り", "文献"), ("成株シルエット", "文献（判定）"),
 ("日照", "今のマスター（空欄は文献）"), ("日照（文献）", "文献（見比べ用）"), ("日照の食い違い", "自動"), ("耐寒性", "今のマスター"), ("耐寒性の食い違い", "自動"), ("USDA 下限", "文献"), ("USDA 上限", "文献"), ("RHS 耐寒性", "文献"), ("耐暑性", "文献（判定）"), ("蒸れ耐性", "文献（判定）"),
 ("暑さ・蒸れの注意", "文献"), ("西日耐性", "文献（判定。組み合わせ）"), ("夏越し実績（自社の実測）", "自社の実測（本州のお客様・卸先からの報告を記入）"), ("乾燥耐性", "文献"),
 ("土壌水分", "文献（読み直し）"), ("pH・土質", "文献"), ("耐潮性", "文献（判定）"), ("常緑性", "文献（温暖地の値・読み直し）"), ("原産地", "文献"), ("増え方", "文献"), ("こぼれ種の量(0-3)", "文献（判定）"),
 ("地下茎で広がる程度(0-3)", "文献（判定）"), ("混植適性", "文献（判定）"), ("広がりすぎの注意", "文献（決まった文に当てはめ）"), ("外来種リスト", "文献（環境省）"), ("北海道ブルーリスト", "文献（北海道庁）"), ("毒性", "文献"), ("主な病害虫", "文献"),
 ("管理タイプ", "文献（判定）"), ("管理難易度", "自動"), ("切り戻しの方法", "文献"), ("切り戻し時期（広尾町）", "自動"), ("切り戻し時期（関東）", "自動"), ("株分けの間隔", "文献"),
 ("繁殖方法", "文献（読み直し）"), ("冬の手入れ（北海道）", "文献（作り直し）"), ("冬の手入れ（温暖地）", "文献（作り直し）"), ("景観構成用途", "自動"), ("切り花適性", "文献（読み直し）"), ("蜜源価値", "文献（読み直し）"), ("機能用途タグ", "自動"), ("デザイン系タグ", "自動"), ("リスクタグ", "自動"),
 # ここから右は、下書きから持ってきた見返し用の列（試作マスターにはない）
 ("在庫あり", "今のマスター"), ("自社の観察", "自社"), ("花色（自社の値）", "今のマスター"), ("株張り（自社の値・cm）", "今のマスター"), ("葉色（自社の値）", "今のマスター"),
 ("耐暑性の信頼度", "見返し用"), ("耐暑性の決め方", "見返し用"), ("耐暑性（欧米の文献だけなら）", "見返し用"), ("蒸れ耐性（欧米の文献だけなら）", "見返し用"),
 ("乾燥耐性の出どころ", "見返し用"), ("暑さ・蒸れ・西日の根拠", "見返し用"), ("学名（マスター）", "今のマスター"), ("学名のメモ", "見返し用"), ("学名（RHS）", "見返し用"),
 ("花色の根拠", "見返し用"), ("葉色の根拠", "見返し用"), ("葉色の写真確認", "見返し用（写真）"), ("常緑性の根拠", "見返し用"), ("土壌水分の根拠", "見返し用"), ("切り花の根拠", "見返し用"), ("蜜源の根拠", "見返し用"), ("繁殖の根拠", "見返し用"), ("冬の手入れの根拠", "見返し用"), ("冬の手入れ（今のマスター・北海道）", "今のマスター"), ("冬の手入れ（今のマスター・温暖地）", "今のマスター"),("こぼれ種・地下茎の根拠", "見返し用"), ("管理タイプの決め方", "見返し用"), ("管理タイプのメモ", "見返し用"), ("管理タイプの決め手（原文）", "見返し用"), ("管理タイプ（言い回しの照合）", "見返し用"),
 ("切り戻し・更新の根拠", "見返し用"), ("切り戻し・手入れの文（全部）", "見返し用"), ("項目の文献", "見返し用"),
 ("成株シルエット（種の記述なら）", "見返し用"), ("成株シルエットの根拠", "見返し用"), ("葉の特徴（種の記述なら）", "見返し用"), ("耐潮性の根拠", "見返し用"),
 ("株分けの間隔の根拠", "見返し用"), ("混植適性の根拠", "見返し用"), ("品種ページのある文献", "見返し用"), ("使った文献", "見返し用"), ("空欄の数（下書き）", "見返し用"), ("下書きのID", "見返し用"),
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
    ryu = fmt_name(m.get("別名"))
    wa = re.sub(r"（種）$", "", d["和名"]) if d.get("和名") else None
    if d.get("ID") in MK:
        adopted, note, ryu, wa = name_answer(d["ID"], MK[d["ID"]], adopted, note, ryu, wa, d, fmt_name(m["学名"]))
    g, ep, cv = split_name(adopted)
    b0, b1 = bloom(m.get("花時期"))
    h0, h1, hp = height(m.get("高さ(cm)"))
    sp = [int(x) for x in re.findall(r"\d+", re.sub(r"（.*$", "", str(d.get("株張り(cm)") or "")))]
    z = re.match(r"(\d+)〜(\d+)", str(d.get("USDA") or ""))
    ia = ias.get(no)
    if not ia and g and ep:  # 2026-11-24（矛盾の洗い出し）: 学名を直した結果、リストの種と同じ種になった品種にも当てる（アスター 'Prof. Anton Kippenberg' → ユウゼンギク）
        ia = IAS_SP.get(sp_key(f"{g} {ep}"))
    ias_note = None
    if ia and sp_key(ia["リストの学名"]) != sp_key(adopted):
        # 2026-11-24: リストは元のマスターの学名で当ててあった。正名（RHS）の種がリストの種と違えば当てない（クロコスミア 'Lucifer'：RHS は種小名なしの Crocosmia 'Lucifer'）
        ias_note = f"掲載なし（元のマスターの学名ではリストの {ia['リストの学名']}（{ia.get('カテゴリ')}）に当たっていたが、正名 {adopted} はその種ではない。同じ属の園芸品種）"
        ia = None
    r = {
     "商品番号": m["商品番号"], "植物名": fmt_name(m["植物名"]), "学名（正名）": adopted, "属": g, "種小名": ep, "品種名": cv,
     "旧学名・別名": fmt_name(m["学名"]) if re.sub(r"[^a-z]", "", fmt_name(m["学名"]).lower()) != re.sub(r"[^a-z]", "", adopted.lower()) else None,
     "和名": wa, "流通名・別名": ryu,
     "花色（分類）": d.get("花色（分類）"), "花色（詳細）": d.get("花色（文献の語）"), "花期 開始月": b0, "花期 終了月": b1,
     "草丈 最小(cm)": h0, "草丈 最大(cm)": h1, "草丈 括弧内の値": hp, "株張り 最小(cm)": sp[0] if sp else None, "株張り 最大(cm)": sp[-1] if sp else None,
     "葉色（分類）": d.get("葉色（分類）"), "紅葉・冬の葉": d.get("紅葉"), "日照": d.get("日照"), "耐寒性": m.get("耐寒性"),
     "USDA 下限": int(z.group(1)) if z else None, "USDA 上限": int(z.group(2)) if z else None, "RHS 耐寒性": d.get("RHS 耐寒性"),
     "耐暑性": d.get("耐暑性"), "蒸れ耐性": d.get("蒸れ耐性"), "暑さ・蒸れの注意": d.get("文献の注意"), "西日耐性": d.get("西日耐性"),
     "乾燥耐性": d.get("乾燥耐性"), "土壌水分": d.get("土壌水分"), "常緑性": d.get("常緑性"), "原産地": d.get("原産地"), "増え方": d.get("増え方"),
     "外来種リスト": (f"{ia.get('カテゴリ')}（{ia.get('リストの和名')}）" + (f"／特定外来生物: {ia['特定外来生物']}" if ia.get("特定外来生物") not in (None, "なし") else "")
                if ia else ias_note or "掲載なし"),
     "主な病害虫": d.get("病害虫"), "切り戻しの方法": d.get("切り戻し"), "繁殖方法": d.get("繁殖"),
     "切り花適性": d.get("切り花"), "蜜源価値": d.get("蜜源"),
     "科名": d.get("科名"), "香り": d.get("香り"), "毒性": d.get("毒性"), "pH・土質": d.get("pH・土質"), "こぼれ種の量(0-3)": d.get("こぼれ種の量(0-3)"),
     "地下茎で広がる程度(0-3)": d.get("地下茎で広がる程度(0-3)"), "こぼれ種・地下茎の根拠": d.get("こぼれ種・地下茎の根拠"),
     "在庫あり": "○" if stock.get(no, {}).get("在庫あり") else None, "自社の観察": d.get("自社の観察"), "花色（自社の値）": d.get("花色（自社の値）"),
     "株張り（自社の値・cm）": d.get("株張り（自社の値・cm）"), "葉色（自社の値）": d.get("葉色（自社の値）"), "耐暑性の信頼度": d.get("耐暑性の信頼度"),
     "耐暑性の決め方": d.get("耐暑性の決め方"), "耐暑性（欧米の文献だけなら）": d.get("耐暑性（欧米の文献だけなら）"),
     "蒸れ耐性（欧米の文献だけなら）": d.get("蒸れ耐性（欧米の文献だけなら）"), "乾燥耐性の出どころ": d.get("乾燥耐性の出どころ"),
     "暑さ・蒸れ・西日の根拠": d.get("暑さ・蒸れ・西日の根拠"), "学名（マスター）": fmt_name(m["学名"]), "学名のメモ": note, "学名（RHS）": d.get("学名（RHS）"),
     "品種ページのある文献": d.get("品種ページのある文献"), "使った文献": d.get("使った文献"), "空欄の数（下書き）": d.get("空欄の数"), "下書きのID": d.get("ID"),
    }
    # 2026-11-21（続き）: 成株シルエット・葉の特徴・耐潮性・株分けの間隔・混植適性・広がりすぎの注意（下書きの列。決め方は scripts/pilot/extra_cols.py の six）
    for c in ("成株シルエット", "成株シルエット（種の記述なら）", "成株シルエットの根拠", "葉の特徴", "葉の特徴（種の記述なら）", "耐潮性", "耐潮性の根拠",
              "株分けの間隔", "株分けの間隔の根拠", "混植適性", "混植適性の根拠", "広がりすぎの注意"):
        r[c] = d.get(c)
    # 北海道の指定外来種（北海道生物の多様性の保全等に関する条例。指定一覧 R5.06.01 で確かめた。植物はこの2種だけ）。
    #   栽培は、野外に出ない施設（屋内、管理された庭園・公園等）で。地下茎・種子で外に出ないように、栽培土を野外に捨てない
    hk = {"Aegopodium podagraria": "イワミツバ", "Leucanthemum vulgare": "フランスギク"}.get(" ".join(adopted.split()[:2]))
    if ia:
        r["広がりすぎの注意"] = "。".join(x for x in (r["広がりすぎの注意"], f"環境省の外来種リストに掲載（{r['外来種リスト']}）") if x)
    if hk:
        r["外来種リスト"] = f"{r['外来種リスト']}／北海道の指定外来種（{hk}。条例。栽培は野外に出ない施設で）"
        r["広がりすぎの注意"] = "。".join(x for x in (r["広がりすぎの注意"], f"北海道の指定外来種（{hk}）。道内では、野外に出ない施設（屋内、管理された庭園・公園等）で育て、地下茎や種で外に出さない。地下茎の断片が入った土を野外に捨てない") if x)
    # 北海道ブルーリスト2010（2026-11-23。scripts/tools/bluelist_match.py → hokkaido_bluelist.json）。種として当てる
    BLM = {"A1": "緊急に防除が必要", "A2": "北海道の生態系に大きな影響。防除の必要性を検討する外来種", "A3": "定着していて、生態系への影響が報告・懸念されている",
           "B": "定着している（影響の報告はない）", "C": "定着ははっきりしないが、影響が報告・懸念されている", "D": "定着ははっきりしない（影響の報告はない）",
           "E": "定着していないが、影響が報告・懸念されている"}
    bl = BL.get(no, {})
    if bl.get("カテゴリー"):
        r["北海道ブルーリスト"] = (f"{bl['カテゴリー']}：{BLM[bl['カテゴリー']]}（{bl['一覧の種名']}。{bl['原産地の区分']}外来種"
                                 + ("" if bl["原産地の区分"] != "国内" else "＝道外の国内から入ったもの") + (f"。{bl['note']}" if bl.get("note") else "") + "）")
    else:
        r["北海道ブルーリスト"] = "掲載なし"
    # 2026-11-23 のユーザーの方針「耐寒性・花時期・高さ・広がり・日照条件は、基本的にマスターを尊重。明らかにマスターとほかの情報先の
    #   データが異なる場合は、再検討」（DECISIONS.md）。日照・株張りも今のマスターの値にし（空欄だけ文献）、文献の値は見比べ用の列へ。
    #   西日耐性は文献の日照から決めたまま（下書きの値）
    lsun = d.get("日照")
    msun = (str(m.get("日照条件")).replace("～", "〜") if m.get("日照条件") else None)
    r["日照"] = msun or lsun
    # 西日耐性は日照で変わる（半日陰・日陰なら ×、日向で耐暑性・乾燥耐性とも 強なら ◎）。2026-11-23 から、下書きの「西日耐性（日照ごと）」から
    #   マスターの日照の値を選ぶ（明るい日陰は 半日陰 と同じ扱い）。文献の日照のときと変わったら、根拠に書く
    wmap = dict(x.split(":", 1) for x in (d.get("西日耐性（日照ごと）") or "").split("；") if ":" in x)
    wkey = "半日陰" if msun in ("半日陰", "明るい日陰") else msun
    if msun and wkey in wmap:
        wnew = None if wmap[wkey] == "空欄" else wmap[wkey]
        if wnew != r["西日耐性"]:
            r["暑さ・蒸れ・西日の根拠"] = "\n".join(x for x in (f"[日照] 今のマスターの日照（{msun}）で西日耐性を決め直した（文献の日照 {lsun} なら {r['西日耐性'] or '空欄'}）", r.get("暑さ・蒸れ・西日の根拠")) if x)
            r["西日耐性"] = wnew
    pv = [l.split("=", 1)[1] for l in (d.get("項目の文献") or "").split("\n") if l.startswith("日照=")]
    r["日照（文献）"] = f"{lsun}（{pv[0]}）" if lsun and pv else lsun
    SR = {"日向": 0, "日向〜半日陰": 1, "半日陰": 2, "明るい日陰": 2, "日陰": 3}
    r["日照の食い違い"] = None
    if msun and lsun and abs(SR.get(msun, 1) - SR.get(lsun, 1)) >= 2:  # 日向 と 半日陰・日陰 のように2段以上違うとき
        r["日照の食い違い"] = f"大きく違う（文献 {lsun}／マスター {msun}）"
    mw0, mw1, _ = height(m.get("広がり(cm)"))
    r["株張り（文献）"] = d.get("株張り(cm)")
    r["株張りの食い違い"] = None
    if mw0 is not None:
        r["株張り 最小(cm)"], r["株張り 最大(cm)"] = mw0, mw1
        if sp:
            a, b = sp[0], sp[-1]
            gap = max(mw0 - b, a - mw1)
            if gap >= max(10, 0.25 * mw1):
                r["株張りの食い違い"] = f"重ならない（文献 {a}〜{b}cm／マスター {mw0}〜{mw1}cm）"
    # 耐寒性：今のマスターの区分は定義が書いてないので、はっきり違うときだけ印（強 なのに USDA 下限 7 以上か RHS H1〜H3、弱・中の弱 なのに USDA 下限 4 以下か RHS H6〜H7）
    r["耐寒性の食い違い"] = None
    mh = m.get("耐寒性")
    zl = int(z.group(1)) if z else None
    hh = re.match(r"H(\d)", str(d.get("RHS 耐寒性") or ""))
    hv = int(hh[1]) if hh else None
    if mh == "強" and ((zl and zl >= 7) or (hv and hv <= 3)):
        r["耐寒性の食い違い"] = f"マスターは 強、文献は USDA 下限 {zl}・RHS {d.get('RHS 耐寒性')}"
    elif mh in ("弱", "中の弱") and ((zl and zl <= 4) or (hv and hv >= 6)):
        r["耐寒性の食い違い"] = f"マスターは {mh}、文献は USDA 下限 {zl}・RHS {d.get('RHS 耐寒性')}"
    # 文献の草丈・花期（2026-11-23。ユーザーの指示「4を始める」）。今のマスターの値は変えない。見比べ用の列と、範囲が重ならないときの印
    r["草丈（文献）"], r["花期（文献）"] = d.get("草丈（文献）"), d.get("花期（文献）")
    lh = re.match(r"(\d+)(?:〜(\d+))?", r["草丈（文献）"] or "")
    r["草丈の食い違い"] = None
    if lh and h0 is not None:
        a, b = int(lh[1]), int(lh[2] or lh[1])
        m0, m1 = h0, h1 if h1 is not None else h0
        gap = max(m0 - b, a - m1)  # 範囲のすき間（cm）。小さな差は印にしない（10cm 以上、かつマスターの値の 25% 以上）
        if gap >= max(10, 0.25 * m1):
            r["草丈の食い違い"] = f"重ならない（文献 {a}〜{b}cm／マスター {m0}〜{m1}cm）"
    lb = re.match(r"(\d+)(?:〜(\d+))?月", r["花期（文献）"] or "")
    r["花期の食い違い"] = None
    if lb and b0:
        a, b = int(lb[1]), int(lb[2] or lb[1])
        c0, c1 = b0, b1 or b0
        # 月の集合で比べる（8〜2月 のように年をまたぐ範囲があるため。2026-11-23 修正）
        def mset(x, y):
            return {(x - 1 + i) % 12 + 1 for i in range((y - x) % 12 + 1)}
        if not (mset(a, b) & mset(c0, c1)):
            r["花期の食い違い"] = f"重ならない（文献 {a}〜{b}月／マスター {c0}〜{c1}月）"
    # 食い違いの確認ページ（2026-11-23）の回答。M＝マスターのまま、B＝文献に合わせる、C＝メモの値。
    #   回答がない印のうち、kuichigai_review.json で「外す」にしたものは、その理由を印の後ろに書く
    for kk in ("日照", "耐寒性", "花期", "草丈", "株張り"):
        col = kk + "の食い違い"
        if not r.get(col):
            continue
        why = KR_DROP.get((no, kk))
        if why:
            r[col] += f"。外した（マスターのまま）：{why}"
            if (no, kk) in ANS.get("外したものの確認", {}):
                r[col] += "。【要見直し】ユーザーが確認したいと回答"
        ua_ = ANS.get("食い違い", {}).get(no, {}).get(kk)
        if not ua_:
            continue
        sel, memo = ua_.get("選択"), ua_.get("メモ")
        tag = f"ユーザーの確認（{ua_['日付']}）"
        done = False
        if sel == "M":
            r[col] += f"。{tag}：マスターのまま"
            done = True
        elif sel in ("B", "C"):
            src = memo if sel == "C" else {"草丈": r["草丈（文献）"], "株張り": r["株張り（文献）"], "花期": r["花期（文献）"], "日照": r["日照（文献）"]}.get(kk)
            src = str(src or "")
            nums = [int(x) for x in re.findall(r"\d+", re.sub(r"（.*$", "", src))]
            if kk in ("草丈", "株張り") and nums:
                r[f"{kk} 最小(cm)"], r[f"{kk} 最大(cm)"] = nums[0], nums[-1]
                done = True
            elif kk == "花期" and nums and "月" in src:
                r["花期 開始月"], r["花期 終了月"] = nums[0], nums[-1] if len(nums) > 1 else nums[0]
                done = True
            elif kk == "耐寒性":
                cv_ = re.match(r"(中の強|中の弱|強|中|弱)", str(memo or ""))
                if cv_:
                    r["耐寒性"] = cv_[1]
                    done = True
            elif kk == "日照":
                sv = re.match(r"(日向〜半日陰|半日陰〜日陰|日向|半日陰|明るい日陰|日陰)", src)
                if sv:
                    r["日照"] = sv[1]
                    done = True
            r[col] += f"。{tag}：" + ("文献に合わせた" if sel == "B" and done and kk != "耐寒性" else f"{r['耐寒性']} にした" if kk == "耐寒性" and done else f"メモの値にした（{memo}）" if done else
                                       f"【要見直し】{'見直す' if sel == 'B' else '別の値'}と回答（自動では直せない）")
        if memo and sel != "C":
            r[col] += f"。備考：{memo}"
        if not done and sel not in ("B", "C"):
            r[col] += f"。【要見直し】回答：{sel or ''}（{memo}）"
    # 原産地（2026-11-23）: Jelitto の値がないときは Kew WCVP の自生地（kew_native.json。scripts/tools/kew_native.py）。
    #   種の分布なので、品種でも「種の原産地」。交配種は Kew の交配式
    kn = KN.get(no, {})
    if not r["原産地"] and kn.get("原産地"):
        r["原産地"] = kn["原産地"] + ("（Kew）" if kn["原産地"].startswith("交配種") else "（種の原産地）（Kew）")
    # ---------- ほかの列から決める列（試作の scripts/assemble.py・trial/RULES.md と同じ決め方。2026-11-21） ----------
    codes = [c for c in re.split(r"[、,]", re.sub(r"（.*$", "", d.get("切り戻し") or "")) if c]
    rz, sd = d.get("地下茎で広がる程度(0-3)"), d.get("こぼれ種の量(0-3)")
    why = d.get("こぼれ種・地下茎の根拠") or ""
    for col_, (val_, msg_) in LV_FIX.get(no, {}).items():  # 2026-11-24 段階の読み直し（ユーザー「おすすめでお願い」）
        r[col_] = val_
        r["こぼれ種・地下茎の根拠"] = "\n".join(x for x in (r.get("こぼれ種・地下茎の根拠"), f"[段階の読み直し 2026-11-24] {msg_}") if x)
        if col_.startswith("地下茎"):
            rz = val_
        else:
            sd = val_
    # 増え方を、こぼれ種・地下茎の段階にそろえる（2026-11-24。矛盾の洗い出し）。増え方は stauden.de（順位がいちばん下）の用語だけから作っていて、
    # 段階はほかの文献も使っているので、食い違っていた。段階のほうに合わせる（RULES.md: self-seeds → こぼれ種、rhizomes → 地下茎、stolons・runners → ランナー）
    m0 = [x for x in (r["増え方"] or "").split("、") if x]
    m1 = list(m0)
    if sd == 0:
        m1 = [x for x in m1 if x != "こぼれ種"]
    elif sd and "こぼれ種" not in m1:
        m1.append("こぼれ種")
    if rz == 0:
        m1 = [x for x in m1 if x not in ("地下茎", "ランナー")] or ["株立ち"]
    elif rz and not {"地下茎", "ランナー"} & set(m1):
        ev_ = " ".join(re.findall(r"\[(?:地下茎|こぼれ種) \d／[^\]]*\] ([^\n]*)", why)).lower()  # こぼれ種の行に地下茎の話があることもある（「self-seeds and spreads by rhizome」）
        add_ = (["地下茎"] if re.search(r"rhizom|sucker|underground|root(s|ing)? (that )?spread|wurzelausläufer|unterirdisch", ev_) else []) + \
               (["ランナー"] if re.search(r"stolon|runner|creeping stem|prostrate stem|roots? at (the )?nodes|ausläufer|kriechend|trailing stem", ev_) else [])
        m1 += add_
    if (rz or 0) >= 2 and {"地下茎", "ランナー"} & set(m1):
        m1 = [x for x in m1 if x != "株立ち"]  # 株立ちは「広がらない」の意味（RULES.md）
    m1 = [x for x in ("株立ち", "地下茎", "ランナー", "こぼれ種") if x in m1]
    if m1 != m0:
        r["増え方"] = "、".join(m1) or None
        r["こぼれ種・地下茎の根拠"] = "\n".join(x for x in (r.get("こぼれ種・地下茎の根拠"), f"[増え方] こぼれ種・地下茎の段階に合わせて直した（前：{'、'.join(m0) or '空欄'}）") if x)
    # 管理タイプ（上から順）: E 隔離推奨型＝地下茎かこぼれ種が 3（はびこる、と文献に明記）。B 花後刈込型＝切り戻しに「花後」。
    #   A 放任型＝切り戻しが「不要」「早春」「秋」だけ。切り戻しの記述がなければ空欄。
    #   D 毎年株更新型・C 夏前切戻型は、もとになる記述（毎年の株分け、初夏の切り戻し）を全品種では拾っていないので、今は付かない
    mt, mt_note = None, None
    # こぼれ種 3 が種の記述だけのとき、品種には当てない（品種がこぼれ種で増えるかは分からない。2026-11-19 のスピレア 'Goldflame' の決定と同じ）。
    # 地下茎 3 は株の広がり方なので、種の記述でも品種に当てる（アジュガ 'Burgundy Glow' の決定と同じ）
    seed3 = (sd or 0) >= 3 and not (cv and re.search(r"\[こぼれ種 3／[^\]]*・種\]", why))
    wide = (rz or 0) >= 3 or seed3
    inv_text = (d.get("混植適性") or "").startswith("侵略的") and not wide  # 文献に invasive／aggressive の明記（RULES.md: E は mixing が 侵略的）
    if (sd or 0) >= 3 and not seed3:
        mt_note = "種の記述では、こぼれ種ではびこる。この品種でも同じかは分からないので、隔離推奨型にしていない（要確認）"
    if wide or inv_text:
        mt = "E 隔離推奨型"
        if cv and re.search(r"\[地下茎 3／[^\]]*・種\]", why):
            mt_note = "地下茎の広がり方は種の記述から"
        if inv_text:
            mt_note = "文献に「侵略的・はびこる」の記述（混植適性の根拠の列）"
    elif d.get("毎年〜2年ごとの更新"):
        mt = "D 毎年株更新型"
    elif d.get("夏前の切り戻し"):
        mt = "C 夏前切戻型"
    elif "花後" in codes:
        mt = "B 花後刈込型"
    elif codes:
        mt = "A 放任型"
    mt_machine, mt_how, mt_quote = mt, ("言い回しの照合（目安）" if mt else None), None
    rv = REVIEW.get(no)
    if rv:
        mt = rv.get("type")
        mt_how = f"文を読んで見直し（確かさ：{rv.get('confidence')}）"
        mt_note = rv.get("reason")
        mt_quote = rv.get("quote")
        if rv.get("codes"):
            codes = list(rv["codes"])
    ua = ANS["管理タイプ"].get(no)
    if ua and ua["値"] in "AB":
        mt = {"A": "A 放任型", "B": "B 花後刈込型"}[ua["値"]]
        mt_how = f"ユーザーの確認（{ua['日付']}、{ua['ページ']}）"
        codes = [c for c in codes if c != "花後"] or ["不要"] if ua["値"] == "A" else list(dict.fromkeys(codes + ["花後"]))
    elif ua:
        mt_how = f"{mt_how or ''}。ユーザーの確認で保留（{ua['日付']}。あとで見直す）"
    if ua and ua.get("備考"):
        mt_note = "。".join(x for x in (mt_note, f"ユーザーの備考：{ua['備考']}") if x)
    # 混植適性を見直した管理タイプにそろえる: 文を読んで E にしなかった品種で、混植適性が「侵略的」なら「強い」に下げる
    #   （広がりやすいことは文献にあるので 強い は残す。見直しで、invasive／aggressive の明記ではない・種のこぼれ種の話・地域の話と読んだもの）
    if rv and not (mt or "").startswith("E") and (r.get("混植適性") or "").startswith("侵略的"):
        r["混植適性"] = "強い（周囲を圧迫、配置注意）"
        r["混植適性の根拠"] += "\n[管理タイプの見直し] 文を読んで隔離推奨型にしなかったので、侵略的 から 強い に下げた"
    # 逆向きもそろえる（2026-11-24。矛盾の洗い出し）: 文を読んで隔離推奨型（E）にした品種は、混植適性も 侵略的（RULES.md: E は mixing が 侵略的）
    if (mt or "").startswith("E") and not (r.get("混植適性") or "").startswith("侵略的"):
        r["混植適性の根拠"] = "\n".join(x for x in (r.get("混植適性の根拠"), f"[管理タイプの見直し] 文を読んで隔離推奨型にしたので、{r.get('混植適性') or '空欄'} から 侵略的 にそろえた") if x)
        r["混植適性"] = "侵略的（隔離推奨）"
    # 切り戻しの方法を、管理タイプを決めた切り戻しの区分（見直し・回答のあと）にそろえる（2026-11-24。矛盾の洗い出し）。
    # 前は下書きの値（言い回しの照合）のままで、見直した管理タイプ・切り戻し時期と食い違っていた。「不要」とほかの区分が両方あるときは、切る記述があるほうを残す
    if len(codes) > 1 and "不要" in codes:
        codes = [c for c in codes if c != "不要"]
    c0 = re.sub(r"（.*$", "", d.get("切り戻し") or "")
    if codes and "、".join(codes) != c0:
        r["切り戻しの方法"] = "、".join(codes) + ("（ユーザーの確認）" if ua and ua["値"] in "AB" else "（文献の文を読んで見直し。管理タイプの決め手の列）")
    # パンパスグラス 'Mini Pampas'（2026-11-24 ユーザー「おすすめでお願い」）: 環境省の外来種リスト（防除検討外来種）と、MBG・種「暖かい地域でこぼれ種で侵略的」から、侵略的・隔離推奨型
    if no in MIX_FIX:
        r["混植適性"], mt = "侵略的（隔離推奨）", "E 隔離推奨型"
        r["混植適性の根拠"] = "\n".join(x for x in (r.get("混植適性の根拠"), f"[ユーザーの決定 2026-11-24] {MIX_FIX[no]}") if x)
        mt_how = "ユーザーの決定（2026-11-24。矛盾の洗い出しのおすすめ）"
    # こぼれ種 2 の基準（2026-11-24 ユーザー「おすすめでお願い」）: 混植適性は 普通 のまま（「こぼれ種でよく増える」の注意は付く）。
    # ただし、こぼれ種 2 の根拠の文に「雑草化する」「大きな群落を作る」「野生化している」があれば 強い
    # 花色（分類）は総当たりの読み直しの値を使う（2026-11-24）。品種の文献の値だけ（商品が種そのものなら種の値も）。中心・喉の色、ほかの色と並ぶ Grey・Silver・Brown は数えない
    crr = COLOR_RR.get(no)
    if crr:
        cnew = "、".join(crr.get("花色") or []) or None
        cold_ = r.get("花色（分類）")
        cw = [f"[読み直し 2026-11-24・確かさ {crr.get('確かさ')}] {crr.get('決め手') or '品種の文献に花色の値がない'}"]
        if (cnew or "") != (cold_ or "") and set((cnew or "").split("、")) != set((cold_ or "").split("、")):
            cw.append(f"前の値：{cold_ or '空欄'}。{crr.get('メモ') or ''}")
        if crr.get("食い違い"):
            cw.append(f"[食い違い] {crr['食い違い']}")
        # stauden.de だけで決まり、今のマスターの花色と重ならないときは空欄（2026-11-24 ユーザー「おすすめ（空欄）」）。
        # stauden.de は種の色を品種に付けていることがあるため。グラスの穂などの「その他」は対象外
        if cnew and (crr.get("決め手") or "").startswith("[stauden") and set(crr["花色"]) != {"その他"}:
            ms_ = {c for c, pat in SD_COLOR if re.search(pat, r.get("花色（自社の値）") or "")}
            if ms_ and not ms_ & set(crr["花色"]):
                cw.append(f"[空欄に戻した] stauden.de だけの値（{cnew}）が今のマスターの花色と重ならないため（ユーザーの決定 2026-11-24）")
                cnew = None
        r["花色（分類）"] = cnew
        if cnew and not r.get("花色（詳細）") and crr.get("決め手"):
            mm_ = re.match(r"^\[([^\]]*)\]\s*(.*)$", crr["決め手"], re.S)
            r["花色（詳細）"] = f"{mm_.group(2)}（{mm_.group(1)}）" if mm_ else crr["決め手"]
        r["花色の根拠"] = "\n".join(cw)
    # 葉色（分類）は総当たりの読み直しの値を使う（2026-11-24）。生育期の主な葉の色・斑を優先・品種の値だけ（商品が種そのものなら種も）
    lrr = LEAF_RR.get(no)
    if lrr:
        lnew, lold = lrr.get("葉色"), r.get("葉色（分類）")
        lw = [f"[読み直し {lrr.get('読み直し2') or '2026-11-24'}・確かさ {lrr.get('確かさ')}] {lrr.get('決め手') or '品種の文献に葉色の値も文もない'}"]
        if (lnew or "") != (lold or ""):
            lw.append(f"前の値：{lold or '空欄'}。{lrr.get('メモ') or ''}")
        if lrr.get("食い違い"):
            lw.append(f"[食い違い] {lrr['食い違い']}")
        # stauden.de だけで決まり、今のマスターの葉色と違うときは空欄（2026-11-24 ユーザー「おすすめ（空欄）」。花色と同じ）。
        # 今のマスターが「⑧ 季節変化型」（分類にない）のときは比べない
        mlf = LEAF_MASTER.get(lrr.get("今のマスター") or "")
        if lnew and (lrr.get("決め手") or "").startswith("[stauden") and mlf and mlf != "季節変化型" and mlf != lnew:
            lw.append(f"[空欄に戻した] stauden.de だけの値（{lnew}）が今のマスターの葉色（{lrr.get('今のマスター')}）と違うため（ユーザーの決定 2026-11-24）")
            lnew = None
        # RHS の品種名に「(v)」（RHS が斑入りとしている）があれば斑入り（2026-11-25 ユーザー「3つともおすすめ」）
        # ただし、中心・葉脈の模様（ヒューケラ型）で地の色にした品種は除く（同じ日の決定。模様は斑入りにしない）
        if no == "1484":
            # スピレア 'Magic Carpet'：RHS の名前に (v) があるが、RHS の葉色は Bronze・Red・Yellow（新芽が赤く、のちに黄金色）。季節変化型にする（ユーザー「季節変化型に」2026-11-27）
            lw.append(f"[ユーザーの決定 2026-11-27] RHS の名前に (v) があるが、RHS の葉色は Bronze・Red・Yellow で、新芽の赤から黄金色に変わる品種なので季節変化型にした（読み直しの値：{lnew or '空欄'}。今のマスターも ⑧ 季節変化型）")
            lnew = "季節変化型"
        elif "(v)" in (r.get("学名（RHS）") or "") and lnew != "斑入り" and not re.search(r"中心|葉脈|中肋", lrr.get("メモ") or ""):
            lw.append(f"[RHS の名前の (v)] RHS が斑入りの品種としているので斑入りにした（読み直しの値：{lnew or '空欄'}。ユーザーの決定 2026-11-25）")
            lnew = "斑入り"
        r["葉色（分類）"] = lnew
        # 自社の値（今のマスターの葉色主分類）は、文献の値がないときと、文献の値と違うときに残す
        r["葉色（自社の値）"] = lrr.get("今のマスター") if (not lnew or LEAF_MASTER.get(lrr.get("今のマスター") or "") != lnew) else None
        r["葉色の根拠"] = "\n".join(lw)
    # 常緑性は総当たりの読み直しの値を使う（2026-11-25）。値の後ろに（決め手の文献・段階）
    err = EVER_RR.get(no)
    if err:
        enew, eold = err.get("常緑性"), r.get("常緑性")
        mm_ = re.match(r"\[([^\]]+)\]", err.get("決め手") or "")
        r["常緑性"] = f"{enew}（{mm_.group(1).replace('cultivar', '品種').replace('species', '種')}）" if enew and mm_ else enew
        ew = [f"[読み直し 2026-11-25・確かさ {err.get('確かさ')}] {err.get('決め手') or '文献に常緑性の値も文もない'}"]
        if (enew or "") != ((eold or "").split("（")[0]):
            ew.append(f"前の値：{eold or '空欄'}。{err.get('メモ') or ''}")
        if err.get("食い違い"):
            ew.append(f"[食い違い] {err['食い違い']}")
        r["常緑性の根拠"] = "\n".join(ew)
    # 乾燥耐性は総当たりの読み直しの値を使う（2026-11-25）。欧米の文献で決まらないときは、決まっている順（おぎはら楽天 → NC State・RHS の項目 → MBG の Water 推定）で埋めた値
    drr = DRY_RR.get(no)
    if drr:
        dold = r.get("乾燥耐性")
        r["乾燥耐性"] = drr.get("乾燥耐性")
        dw = [f"[読み直し 2026-11-25・確かさ {drr.get('確かさ')}] {drr.get('決め手') or '欧米の文献に乾燥への強さの値も文もない'}"]
        if drr.get("文献の値") is None and drr.get("出どころ"):
            dw.append(f"埋め方：{drr['出どころ']}")
        if (r["乾燥耐性"] or "") != (dold or ""):
            dw.append(f"前の値：{dold or '空欄'}。{drr.get('メモ') or ''}")
        if drr.get("食い違い"):
            dw.append(f"[食い違い] {drr['食い違い']}")
        if drr.get("おぎはらとの食い違い"):
            dw.append(f"[食い違い] {drr['おぎはらとの食い違い']}")
        r["乾燥耐性の出どころ"] = "\n".join(dw)
        # 西日耐性の ◎ は「日向・耐暑性 強・乾燥耐性 強」のとき（assemble_pilot.py の west_for）。乾燥耐性が変わったので合わせ直す
        hsun, wv = (r.get("日照") or ""), r.get("西日耐性")
        full = hsun.startswith("日向") and r.get("耐暑性") == "強" and r["乾燥耐性"] == "強"
        wnote = None
        if wv == "◎" and not full:
            r["西日耐性"], wnote = "○", f"[乾燥耐性の読み直し] 乾燥耐性が {r['乾燥耐性'] or '空欄'} になったので、西日耐性 ◎ → ○"
        elif wv == "○" and full and "（西日 ○ 相当）" not in (r.get("暑さ・蒸れ・西日の根拠") or ""):
            r["西日耐性"], wnote = "◎", "[乾燥耐性の読み直し] 乾燥耐性が 強 になり、日向・耐暑性 強 とそろったので、西日耐性 ○ → ◎"
        if wnote:
            r["暑さ・蒸れ・西日の根拠"] = "\n".join(x for x in (wnote, r.get("暑さ・蒸れ・西日の根拠")) if x)
    # 土壌水分は総当たりの読み直しの値を使う（2026-11-26。scripts/tools/soil_reread_note.md）
    srr = SOIL_RR.get(no)
    if srr:
        sold = r.get("土壌水分")
        r["土壌水分"] = srr.get("土壌水分")
        sw_ = [f"[読み直し 2026-11-26・確かさ {srr.get('確かさ')}] {srr.get('決め手') or '欧米の文献に土の湿りの値も文もない'}"]
        if (r["土壌水分"] or "") != (sold or ""):
            sw_.append(f"前の値：{sold or '空欄'}。{srr.get('メモ') or ''}")
        if srr.get("食い違い"):
            sw_.append(f"[食い違い] {srr['食い違い']}")
        r["土壌水分の根拠"] = "\n".join(sw_)
    # 切り花適性は総当たりの読み直しの値を使う（2026-11-26。scripts/tools/cut_reread_note.md）
    crr = CUT_RR.get(no)
    if crr:
        cold = r.get("切り花適性")
        r["切り花適性"] = crr.get("切り花")
        cw_ = [f"[読み直し 2026-11-26・確かさ {crr.get('確かさ')}] {crr.get('決め手') or '文献に切り花の記述がない'}"]
        if (r["切り花適性"] or "") != (cold or ""):
            cw_.append(f"前の値：{cold or '空欄'}。{crr.get('メモ') or ''}")
        if crr.get("食い違い"):
            cw_.append(f"[食い違い] {crr['食い違い']}")
        r["切り花の根拠"] = "\n".join(cw_)
    # 蜜源価値は総当たりの読み直しの値を使う（2026-11-26。scripts/tools/poll_reread_note.md）
    prr = POLL_RR.get(no)
    if prr:
        pold = r.get("蜜源価値")
        r["蜜源価値"] = prr.get("蜜源")
        pw_ = [f"[読み直し 2026-11-26・確かさ {prr.get('確かさ')}] {prr.get('決め手') or '文献に蜜源の記述がない'}"]
        if (r["蜜源価値"] or "") != (pold or ""):
            pw_.append(f"前の値：{pold or '空欄'}。{prr.get('メモ') or ''}")
        if prr.get("食い違い"):
            pw_.append(f"[食い違い] {prr['食い違い']}")
        r["蜜源の根拠"] = "\n".join(pw_)
    # 品種なのに種のページの値を使った切り花・蜜源の確かめ（2026-11-27。scripts/tools/species_value_check_note.md）
    # 外す：品種の性質（八重咲き・品種のページの逆の記述）で種の値が当てはまらない → 空欄。迷う：値は残し、根拠に書く
    for item_, col_, ev_ in (("切り花", "切り花適性", "切り花の根拠"), ("蜜源", "蜜源価値", "蜜源の根拠")):
        sc_ = SPECIES_CHECK.get(no, {}).get(item_)
        if sc_ and r.get(col_):
            if sc_["判断"] == "外す":
                r[ev_] = f"[品種の確かめ 2026-11-27] 種の値 {r[col_]} は品種に当てはまらないので外した：{sc_['理由']}\n" + (r.get(ev_) or "")
                r[col_] = None
            else:
                r[ev_] = (r.get(ev_) or "") + f"\n[品種の確かめ 2026-11-27・要確認] 種の値が品種に当てはまるか迷う：{sc_['理由']}"
    # 繁殖方法は総当たりの読み直しの値を使う（2026-11-26。scripts/tools/prop_reread_note.md）
    grr = PROP_RR.get(no)
    if grr:
        gold = r.get("繁殖方法")
        r["繁殖方法"] = "、".join(grr.get("繁殖") or []) or None
        gw_ = [f"[読み直し 2026-11-26・確かさ {grr.get('確かさ')}] {grr.get('決め手') or '文献に繁殖の記述がない'}"]
        if re.sub(r"（RHS）$", "", gold or "") != (r["繁殖方法"] or ""):
            gw_.append(f"前の値：{gold or '空欄'}。{grr.get('メモ') or ''}")
        if grr.get("食い違い"):
            gw_.append(f"[食い違い] {grr['食い違い']}")
        r["繁殖の根拠"] = "\n".join(gw_)
    # 冬の手入れ（北海道）・（温暖地）は文献から作り直す（2026-11-26 の決定）。今のマスターの文は見比べ用の列に残す
    wf = WINTER_RR.get(no)
    whk, wwm, wwhy = winter_text(wf, r.get("常緑性"), r.get("土壌水分"), r.get("耐寒性"), r.get("学名（正名）"))
    wpo = WINTER_POLISH.get(no)
    if wpo:
        whk, wwm = wpo.get("北海道"), wpo.get("温暖地")
    sn = snow_note(wf, whk)
    if sn:
        whk = (whk or "") + sn
        wwhy.append(f"[雪が少ない年の一言 2026-11-27] {sn}")
    r["冬の手入れ（北海道）"], r["冬の手入れ（温暖地）"] = whk, wwm
    r["冬の手入れ（今のマスター・北海道）"], r["冬の手入れ（今のマスター・温暖地）"] = m.get("冬の手入れ（北海道）"), m.get("冬の手入れ（温暖地）")
    if wf:
        wwhy.insert(0, f"[文献から抜き出し 2026-11-26・確かさ {wf.get('確かさ')}] {wf.get('決め手') or '文献に冬の手入れの記述がない'}")
        if wf.get("食い違い"):
            wwhy.append(f"[食い違い] {wf['食い違い']}")
    r["冬の手入れの根拠"] = "\n".join(wwhy) or None
    # 葉色の写真確認（2026-11-24。記録だけで値は変えない）
    lph = LEAF_PHOTO.get(no)
    r["葉色の写真確認"] = f"{lph['判断']}（{lph['写真']}の写真：{lph['見えた色']}）" if lph else None
    rrs = SPREAD_RR.get(no, {})
    if (r.get("混植適性") or "").startswith("普通") and sd == 2:
        ev2 = [l for l in why.split("\n") if l.startswith("[こぼれ種 2")]
        hit2 = next((l for l in ev2 if re.search(r"weedy|naturaliz|colonies|escaped|verwilder", l, re.I)), None)
        # 総当たりの読み直し（spread_reread.json）で、同じ基準で 強い と読んだもの（群落・野生化の文が、こぼれ種の決め手とは別の文にあるとき）
        if not hit2 and (rrs.get("混植") or "").startswith("強い"):
            hit2 = f"[読み直し] {rrs.get('混植の決め手') or ''}"
        if hit2:
            r["混植適性"] = "強い（周囲を圧迫、配置注意）"
            r["混植適性の根拠"] = "\n".join(x for x in (r.get("混植適性の根拠"), "[こぼれ種 2 の基準 2026-11-24] こぼれ種 2 で、雑草化・群落・野生化の記述があるので 強い：" + hit2[:160]) if x)
    # 株立ちの記述だけの品種（2026-11-24 総当たりの読み直し）: RULES.md の「普通（混植可）: clump-forming で上の記述なし」。
    # 前は stauden.de の horstig と地下茎 0〜1 しか見ていなかったので、RHS の Habit: Clump forming や MBG の clump-forming だけの品種が空欄だった
    if not r.get("混植適性") and (rrs.get("混植") or "").startswith("普通") and (rz or 0) < 2 and (sd or 0) < 3:
        r["混植適性"] = "普通（混植可）"
        r["混植適性の根拠"] = "\n".join(x for x in (r.get("混植適性の根拠"), f"[読み直し 2026-11-24] 株立ちの記述だけで、広がる記述がない：{rrs.get('混植の決め手') or ''}"[:220]) if x)
    # 2026-11-24 ユーザーの決定（広がり方の読み直しの3つの問い、すべておすすめどおり）
    # 問2: 読み直しで段階 3（はびこる・雑草化・取り除きにくいの明記）なのに、前の管理タイプの見直しで E にしなかった品種 → 侵略的・隔離推奨型
    if no in MIX_E3:
        if not (r.get("混植適性") or "").startswith("侵略的") or not (mt or "").startswith("E"):
            r["混植適性の根拠"] = "\n".join(x for x in (r.get("混植適性の根拠"), f"[ユーザーの決定 2026-11-24] 読み直しで段階 3（{(rrs.get('混植の決め手') or '')[:120]}）。植物の性質として書かれているので 侵略的・隔離推奨型") if x)
        r["混植適性"], mt = "侵略的（隔離推奨）", "E 隔離推奨型"
        mt_how = "ユーザーの決定（2026-11-24。広がり方の読み直しのおすすめ）"
    # 問1: 地下茎 2（根茎・ランナーで広がる。はびこるの明記なし）なのに混植適性が空欄 → 強い（RULES.md: 地下茎 2 は 強い）
    if not r.get("混植適性") and rz == 2:
        r["混植適性"] = "強い（周囲を圧迫、配置注意）"
        r["混植適性の根拠"] = "\n".join(x for x in (r.get("混植適性の根拠"), "[ユーザーの決定 2026-11-24] 地下茎 2（根茎・ランナーで広がる記述）なので 強い") if x)
    # 問3: 「侵略的になりうる」「逃げ出した雑草」とだけあり、広がり方が書いていない品種 → 強い
    if no in MIX_STRONG_NOWAY:
        r["混植適性"] = "強い（周囲を圧迫、配置注意）"
        r["混植適性の根拠"] = "\n".join(x for x in (r.get("混植適性の根拠"), f"[ユーザーの決定 2026-11-24] {MIX_STRONG_NOWAY[no]}") if x)
    cold = r["耐寒性"]  # 食い違いの確認の回答で変わることがある
    heat = d.get("耐暑性")
    uh = ANS["耐暑性"].get(no)
    if uh:
        heat = r["耐暑性"] = uh["値"]
        r["耐暑性の決め方"] = f"ユーザーの確認（{uh['日付']}、暑さの確認の問{uh['問題']}）" + (f"。備考：{uh['備考']}" if uh.get("備考") else "")
    for k, v in ANS["違うとの指摘"].get(no, {}).items():  # 値は変えず、見直しの印だけ付ける（「どう違うか」は自由記述なので）
        col = "耐暑性の決め方" if k == "耐暑性" else "暑さ・蒸れ・西日の根拠"
        r[col] = "。".join(x for x in (r.get(col), f"【要見直し】ユーザーが{k} 弱 は違うと指摘（{v['日付']}）" + (f"：{v['どう違うか']}" if v.get("どう違うか") else "")) if x)
    if (mt or "").startswith("E") or cold in ("中の弱", "弱", "一年草扱い"):
        diff = "難"
    elif mt is None:
        diff = None
    elif mt.startswith("A") and heat != "弱" and cold in ("強", "中の強"):
        diff = "易"
    else:
        diff = "中"
    PR = {"早春": ("雪解け後（4月下旬〜5月上旬）", "2〜3月"), "秋": ("10月", "11〜12月"), "初夏": ("6月下旬〜7月上旬", "5月下旬〜6月上旬"), "不要": ("不要", "不要"), "花後": ("花後", "花後")}
    hk = [PR[c][0] for c in codes if c in PR]
    kt = [PR[c][1] for c in codes if c in PR]
    modes = r.get("増え方") or ""
    smax = sp[-1] if sp else None
    use = []
    if h1:
        use.append("前景" if h1 <= 40 else "中景" if h1 < 90 else "後景")
    sil = d.get("成株シルエット")
    gc = sil == "マット" or bool(h1 and h1 <= 20 and ("ランナー" in modes or "地下茎" in modes))
    if gc:
        use.append("グラウンドカバー")
    if (sil in ("グラス", "アーチ") and h1 and h1 >= 60) or (smax and smax >= 90):
        use.append("主役（単植向き）")
    if smax and smax <= 40 and not gc:
        use.append("群植向き")
    sun, dr, fc = (r["日照"] or "").replace("明るい日陰", "半日陰"), r.get("乾燥耐性"), r.get("葉色（分類）")
    tags = []
    if sun in ("半日陰", "日陰"):
        tags.append("日陰庭向き")
    elif sun == "日向〜半日陰":
        tags.append("半日陰でも可")
    if dr == "強":
        tags.append("乾燥地向き")
    if r.get("蜜源価値") in ("◎", "○"):
        tags.append("蜜源")
    if r.get("切り花適性") in ("◎", "○"):
        tags.append("切り花")
    if fc and fc != "グリーン系":
        tags.append("カラーリーフ")
    if d.get("耐潮性") == "◎":
        tags.append("海辺向き")
    if sil in ("マット", "ドーム") and dr == "強" and r.get("土壌水分") in ("排水必須", "乾燥寄り"):
        tags.append("ロックガーデン向き")
    dz = []
    if fc == "シルバー系":
        dz.append("シルバーリーフ")
    if fc == "パープル・ブラック系":
        dz.append("黒葉アクセント")
    if fc == "斑入り":
        dz.append("斑入り葉")
    if re.search(r"Poaceae|Cyperaceae", d.get("科名") or "") or sil == "グラス":
        dz.append("グラス調")
    if cold == "強" and diff == "易":
        dz.append("北海道向き強健")
    risk = []
    if d.get("蒸れ耐性") == "弱":
        risk.append("管理難（高温多湿で崩れやすい）")
    # 要管理: 管理タイプが E か、混植適性が 侵略的・強い。言い回しの照合の「はびこる」(wide) は、文を読んで見直した品種では使わない（見直しで E から外したものに残さない）
    if (mt or "").startswith("E") or (wide and not rv) or (r.get("混植適性") or "").startswith(("侵略的", "強い")):
        risk.append("要管理（広がりやすい）")
    # 2026-11-24 ユーザー「おすすめでお願い」: 環境省の外来種リスト（第２版）に載っている種も 要管理（北海道ブルーリスト A2 と同じ扱い）
    if not (r.get("外来種リスト") or "掲載なし").startswith("掲載なし"):
        risk.append("要管理（環境省の外来種リスト）")
    # 2026-11-23 ユーザーの回答「A2だけ入れる」: 北海道ブルーリストの A2（A1 もあれば同じ）。A3・B・D は入れない
    if (BL.get(no, {}).get("カテゴリー") or "") in ("A1", "A2"):
        risk.append(f"要管理（北海道ブルーリスト {BL[no]['カテゴリー']}）")
    r.update({"管理タイプ": mt, "管理タイプのメモ": mt_note, "管理難易度": diff, "切り戻し時期（広尾町）": "、".join(dict.fromkeys(hk)) or None,
              "切り戻し時期（関東）": "、".join(dict.fromkeys(kt)) or None, "景観構成用途": "、".join(use) or None,
              "切り戻し・更新の根拠": d.get("切り戻し・更新の根拠"), "切り戻し・手入れの文（全部）": d.get("切り戻し・手入れの文（全部）"), "項目の文献": d.get("項目の文献"),
              "管理タイプの決め方": mt_how, "管理タイプの決め手（原文）": mt_quote, "管理タイプ（言い回しの照合）": mt_machine,
              "機能用途タグ": "、".join(tags) or None, "デザイン系タグ": "、".join(dz) or None, "リスクタグ": "、".join(risk) or None})
    rows.append(r)
assert not miss, miss
# 原産地を同じ種の中でそろえる（2026-11-24 ユーザー：「jelittoに合わせて」）。同じ種（属＋種小名）の商品のどれかに Jelitto の原産地があれば、
# その種の全部の商品を Jelitto の値にする（いちばん多い値。種のページの値を先に。「園芸で作られた」「交配」など品種の生まれの話は種の原産地ではないので使わない）。
# Jelitto の値がない種は今のまま（Kew の自生地）
_grp = {}
for r in rows:
    k = sp_key(f"{r['属']} {r['種小名']}") if r.get("種小名") else None
    if k:
        _grp.setdefault(k, []).append(r)
for k, rs in _grp.items():
    cand = [(0 if "Jelitto・種" in r["原産地"] else 1, re.sub(r"（Jelitto・(品種|種)）$", "", r["原産地"])) for r in rs
            if r.get("原産地") and re.search(r"（Jelitto・(品種|種)）$", r["原産地"]) and not re.search(r"園芸|交配", r["原産地"])]
    if not cand:
        continue
    best = min(cand, key=lambda c: (c[0], -sum(1 for c2 in cand if c2[1] == c[1])))
    for r in rs:
        if re.sub(r"（Jelitto・(品種|種)）$", "", r.get("原産地") or "") != best[1]:
            r["項目の文献"] = "\n".join(x for x in (r.get("項目の文献"), f"原産地=Jelitto（同じ種の別の商品のページから。前：{r.get('原産地') or '空欄'}）") if x)
            r["原産地"] = best[1] + "（Jelitto・種。同じ種の別の商品のページから）"
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
sheet("まだ作っていない列", ["列", "今の状態"], [[c, NOT_YET.get(c, "")] for c, k in COLS if k == "まだ"], [30, 90])
sheet("この表について", ["説明"], [[x] for x in [
    f"全{len(rows)}品種の下書きを、試作28品種のマスターと同じ列の並びにまとめたもの。並びは元のマスターの順。価格・在庫数は入れていない（在庫の有無だけ）。",
    "1行目は列の出どころ。緑＝今のマスターの値、白＝文献、青＝自動、灰色＝まだ作っていない列（空欄）、黄色＝見返し用の列（試作マスターにはない）。",
    "花期・草丈・耐寒性は今のマスターの値（2026-11-18 の決定）。耐暑性・蒸れ耐性・西日耐性・乾燥耐性の決め方は DECISIONS.md の 2026-11-21 の決定。",
    "「暑さ・蒸れの注意」には、下書きの「文献の注意」（シカゴ植物園の試験の記録など）を入れてある。通販ページには出さない（2026-11-19 の決定）。",
    "管理タイプ: E 隔離推奨型＝地下茎かこぼれ種が 3（はびこる、と文献に明記）。B 花後刈込型＝切り戻しに「花後」。A 放任型＝切り戻しが「不要」「早春」「秋」だけ。切り戻しの記述がなければ空欄。"
    "D 毎年株更新型＝毎年〜2年ごとの株分け・更新の記述。C 夏前切戻型＝夏に葉が傷んだら切り戻す、初夏に草丈を詰める、切り戻すと新しい葉が出る、などの記述（言い回しの照合。根拠は「切り戻し・更新の根拠」の列）。上から E・D・C・B・A の順。",
    "管理タイプの見直し（2026-11-21）: 在庫のある品種は、切り戻し・手入れの文を1品種ずつ読んで決め直した（「管理タイプの決め方」が「文を読んで見直し」の行。理由は「管理タイプのメモ」、決め手の原文は「管理タイプの決め手（原文）」）。"
    "在庫のない品種は、言い回しの照合のまま（目安）。見直した品種は、切り戻し時期も、読んで決めた区分（花後・早春・秋・初夏・不要）から作っている。",
    "管理難易度: E か、耐寒性が 中の弱・弱・一年草扱い → 難。A で、耐暑性が 弱 でなく、耐寒性が 強・中の強 → 易。ほかは 中。管理タイプが空欄なら空欄。",
    "タグ: 試作と同じ決め方。「水辺向き」だけは、もとになる列（水辺に向くという明記）がまだないので付いていない。",
    "成株シルエット・葉の特徴・耐潮性・株分けの間隔・混植適性・広がりすぎの注意（2026-11-21）: 文献の用語・言い回しの照合で作った目安。根拠は右の見返し用の列。"
    "成株シルエットと葉の特徴は品種のページ（品種名のない商品は種のページ）だけから。種のページからの値は「…（種の記述なら）」の列に参考として出してある。"
    "耐潮性の ○ の多くは、文献の項目だけ（RHS の植える場所の Coastal、NC State の Salt・Coastal）から。混植適性の 普通 は、地下茎が 0〜1 か、stauden.de で株立ちだけのとき。"
    "広がりすぎの注意は、決まった文に当てはめたもの（もとの文は、こぼれ種・地下茎の根拠と混植適性の根拠の列）。",
    "「夏越し実績（自社の実測）」は空欄で始め、本州のお客様・卸先からの報告を記入する。文献の値より優先する。",
    "もとにした下書き: " + "、".join(os.path.basename(f)[:16] + "…" + os.path.basename(f)[-11:-5] for f in files),
]], [160])
wb.save(OUT)
print("品種", len(rows), "/ 元のマスター", len(master), "根拠", len(ev), "学名の検討", len(nm))
print("値のある品種（主な列）:", {c: filled[c] for c in ("学名（正名）", "和名", "花色（分類）", "株張り 最小(cm)", "葉色（分類）", "日照", "USDA 下限", "耐暑性", "蒸れ耐性", "西日耐性", "乾燥耐性", "土壌水分", "常緑性", "原産地", "増え方", "主な病害虫", "切り戻しの方法", "繁殖方法", "切り花適性", "蜜源価値", "花期 開始月", "草丈 最大(cm)", "景観構成用途")})
print("外来種リスト: 掲載なし以外", sum(1 for r in rows if not r["外来種リスト"].startswith("掲載なし")))
