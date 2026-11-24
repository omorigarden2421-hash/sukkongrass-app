"""3属の試行: 集めた文献から、品種ごとの値の下書きを作る（Excel。リポジトリの外に出す）。

使い方: python3 -X utf8 scripts/pilot/assemble_pilot.py <input フォルダ> <digest.json> <生データのフォルダ> <出力.xlsx> [属ごとのデータのフォルダ]
例（アスター）: … batch_aster/input <digest> <raw> <出力.xlsx> batch_aster
考え方
- 品種のページがあればそれを使い、なければ同じ種のページ、それもなければ同じ属で最も多い書き方（属レベル）を使う。
  どの階層の記述かを「レベル」に残す（品種／種／属）。
- 耐暑性・蒸れ耐性・西日耐性は、RULES.md の決め方を言い回しの照合で下書きする（PATTERNS）。根拠の文を横に出すので、人が確認する。
- 花色・葉色・株張りは品種のページからだけ取る（種のページからは入れない）。
- 文献にない値は空欄のまま。
"""
import glob
import html
import json
import os
import re
import sys
from collections import Counter

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

# 属ごとのデータ（ogihara_data.py・gaissmayer_data.py・rhs_ids.py・jelitto_cbg_data.py）のフォルダ。省略時は3属の試行（scripts/pilot）
sys.path.insert(0, sys.argv[5] if len(sys.argv) > 5 else os.path.dirname(os.path.abspath(__file__)))
import gaissmayer_data as GA  # noqa: E402
import ogihara_data as OG  # noqa: E402
import rhs_ids as RH  # noqa: E402
import jelitto_cbg_data as JC  # noqa: E402
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from extra_cols import extra as extra_columns, prune_extra, prune_all, six as six_columns, sdb_lv  # noqa: E402

IN, DIGEST, RAW, OUT = sys.argv[1:5]
D = json.load(open(DIGEST, encoding="utf-8"))
# 2026-11-24 耐暑性・蒸れ耐性の総当たりの読み直し（商品番号 → 欧米耐暑・欧米蒸れ・決め手）
_RR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "heat_reread.json")
REREAD = json.load(open(_RR, encoding="utf-8")) if os.path.exists(_RR) else {}
ITEMS = [json.load(open(f, encoding="utf-8")) for f in sorted(glob.glob(IN + "/*.json"))]
OGI = {i: rec for rec in OG.OGIHARA for i in rec[0]}
JEL = {i: rec for rec in JC.JELITTO for i in rec[0]}
# おぎはら植物園の楽天の商品ページから読んだ項目（scripts/tools/ogi_shop.py が作る。図鑑のID → 項目）。2026-11-21 の決定で、蒸れ耐性・西日耐性・乾燥耐性にも使う
_SHOP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "ogihara_shop.json")
SHOP = json.load(open(_SHOP, encoding="utf-8"))["pages"] if os.path.exists(_SHOP) else {}
R3 = {"弱": 0, "中": 1, "強": 2}
RW = {"×": 0, "△": 1, "○": 2, "◎": 3}


def _nz(x):
    return (x or "").replace(" ", "")


def _lvl(x):
    x = _nz(x)
    return next((a for a in ("やや強い", "やや弱い", "強い", "弱い", "普通") if x.startswith(a)), None)


def shop_heat(sh):
    x = _nz(sh.get("heat"))
    return "強" if x.startswith("強") else "中" if x.startswith(("普通", "中")) else "弱" if x.startswith("弱") else None


def shop_muggy(sh):
    """耐湿性の説明に「高温多湿を嫌う」があれば、耐湿性が やや弱い・弱い なら 弱、それ以外は 中。
    耐暑性の補足が「暖地では夏に風とおし、水はけよく」だけなら 中。どちらもなければ None（書いていないことから 強 とはしない）"""
    # 2026-11-24 読み直し: 「高温時には多湿に注意」「湿気の多い環境を嫌います」も同じ意味（空気の湿気）として拾う
    if re.search("高温多湿|蒸れ|高温時[^。]*多湿|湿気の多い", _nz(sh.get("wet"))):
        return ("弱" if _lvl(sh.get("wet")) in ("やや弱い", "弱い") else "中"), "耐湿性: " + sh["wet"]
    if "風とおし" in _nz(sh.get("heat")):
        return "中", "耐暑性: " + sh["heat"]
    return None, None


def shop_west(sh):
    """暖地の日照。寒冷地と暖地で違うときだけ使う。西日は避ける → ×、暖地が半日陰・日陰だけ → ×、
    昼過ぎから（夏場は）半日陰が理想 → △、寒冷地は日向で暖地は 日向〜やや半日陰 → ○"""
    c, w = _nz(sh.get("sun_cool")), _nz(sh.get("sun_warm"))
    if not w or c == w:
        return None
    if "西日" in w:
        return "×"
    if re.search("昼過ぎ|夏場|午後", w):
        return "△"
    return "○" if "日向" in w else "×"


def shop_dry(sh):
    return {"強い": "強", "やや強い": "強", "普通": "中", "やや弱い": "弱", "弱い": "弱"}.get(_lvl(sh.get("dry")))


def _low(a, b, rank):
    if a is None or b is None:
        return a or b
    return a if rank[a] <= rank[b] else b


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower().replace("'", "")).strip("-")


def sentences(t):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t or "") if s.strip()]


# ---------- 言い回しの照合（RULES.md の heat / muggy / west_sun） ----------
P_HEAT_WEAK = r"intolerant of (the )?hot|(performs?|grows?) poorly in [^.]*hot|dislike[s]? (the |high )?(hot|heat)|for cool summer climates|dislike[s]? [^.]*hot, humid summer|intolerant of (the )?(high |extreme )?heat|cool weather plant|not recommended for planting south|do(es)? not (grow|perform|do) well in the deep south|don.t do well in heat|does not tolerate hot|will not do well in the hot|not recommended for growing south|require[s]? a cool|prefer[s]? cool[- ](summer|weather|climate|temperature|night|condition|growing condition)|best performance (occurs |is seen )?in (cool|climates with cool)|best in cool summer|struggles? in (the )?heat|does not (do well|tolerate) .*heat|do(es)? not (do|perform) well [^.]*(night ?time temperatures|night temperatures|hot and humid|hot summer)|(decline|suffer) in summer heat south of|not (terribly |very |particularly )?tolerant of [^.]*(hot|heat)|struggles? in (the )?hot|sensitive to (high )?heat|intolerant of [^.]*hot and humid|will not perform well [^.]*hot|not recommended for the southeastern|intolerant of (high )?summer heat|did not do well [^.]*hot and humid|(does|do) poorly in hot|poorly in hot climates|will not do well in hot|best in regions with cool summers|in hot, humid summer regions, plants do not usually last|less successful in the high summer heat|struggles? in our hot|thrive in cool summer climates|prefers cooler weather"
P_HEAT_MID = r"hot summer weather[^.]*dormant|full sun in cooler climates|from hot summer temperatures|foliage may wilt in the heat|hot afternoon sun|depreciates in the heat|shade is helpful if summers are hot|stress in hot|foliage (tends to|will|can) (decline|burn)|heat of the summer sets in|some tolerance for hot|afternoon shade|decline[s]? .*hot summer|interrupts? in the heat|foliage may (decline|scorch|burn)|scorch|in hot summer climates|best in cool northern summer|full sun is best in cool|leaf burn|in the south it is best|shade at the heat of the day|in hot summer locations|moderately resistant to [^.]*heat|flop in [^.]*hot (summer )?temperatures|dormant in hot weather"
P_HEAT_STRONG = r"adaptable to [^.]*hot, humid|heat-tolerant|bears up under hot|good heat tolerance|tolerates?,? (the |high |summer )?(hot|heat)|heat tolerant|(?<!in)tolerant of [^.]*(heat|hot)|tolerates hot and humid|good heat and drought tolerance|grows? well in hot|good tolerance for heat|tolerates [a-z ]+, heat\b|perform beautifully in the piedmont and coastal plain|heat and frost-tolerant|ground cover for hot, dry areas|loves hot, sunny sites"
P_MUGGY_WEAK = r"intolerant of (the )?hot and humid|(performs?|grows?) poorly in [^.]*hot,? (and )?humid|dislike[s]? (the )?hot and humid|dislike[s]? [^.]*hot, humid|intolerant of (the )?(high )?heat and humidity|dislike[s]? .*humidity|melt[s]? out|not .*tolerant of .*humid|do(es)? not (do|perform) well in [^.]*hot and humid|don.t do well in heat and humidity|does not tolerate hot or humid|not do well in the hot humid|because of winter stresses and high summer humidity|high summer humidity in the st\b|struggles? in (the )?heat and humidity|struggles? in (the )?hot and humid|sensitive to (high )?heat and humidity|intolerant of [^.]*hot and humid|will not perform well in [^.]*hot and humid|intolerant of (high )?summer heat and humidity|did not do well [^.]*hot and humid|in hot, humid summer regions, plants do not usually last|challenge to grow [^.]*humid summer|less successful in the high summer heat and humidity|does not perform well in climates with high humidity"
P_MUGGY_MID = r"decline [^.]*high humidity|stress in hot and humid|bothered by humidity|some tolerance for hot and humid|(mildew|rust|leaf spot)[^.]*humid|humid[^.]*(mildew|rust|leaf spot|flop)|good air circulation|prefer[s]? .*dry air|tolerates humidity better than|blight[^.]*hot and humid"
P_MUGGY_STRONG = r"tolerates? heat, humidity|adaptable to [^.]*hot, humid|bears up under hot, humid|tolerates? hot and humid|(?<!in)tolerant of [^.]*hot and humid|(?<!in)tolerant of .*humidity|tolerates? .*heat and humidity|tolerance for heat, humidity|tolerates hot, humid|(?<!in)tolerant of [^.]*hot, humid|good selection for humid climates"
# 2026-11-20: 「intolerant of high heat and humidity」が tolerant of … heat に当たって 強 になっていた（スカビオサ）。in- の付く形を 強 から外し、弱 の言い回しに足した。
#   トロリウスの「cool weather plant」「dislikes dry soils and hot, humid summers」「not recommended for planting south of …」も 弱 に足した。
#   タリクトラムの「Performs poorly in hot and humid summer climates」「Intolerant of hot and humid conditions」「May grow poorly in climates with hot, humid summers」を 弱、
#   「Some tolerance for hot and humid summer weather」を 中 に足した（2026-11-20）。
#   2026-11-20（batch_09）: 「Foliage tends to burn in hot, dry, sunny summer conditions」（シュウメイギク）、「As the heat of the summer sets in, foliage tends to decline」
#   「the foliage will decline」（トラデスカンティア）を 中、「good heat tolerance」（シモツケ）を 強、「may be bothered by humidity」（ネペタ）を蒸れ 中 に足した。
#   2026-11-20（batch_10）: 「drought- and heat-tolerant」「bears up under hot, humid summers」（ルドベキア フルギダ）を 強、
#   「Light shade is helpful if summers are hot」（クニフォフィア）「may show some stress in hot and humid summers」（ユーフォルビア）を 中 に足した。
#   2026-11-20（batch_11）: 「Plants dislike high heat and humidity」（デスカンプシア フレクシオーサ）「shrub for cool summer climates」（ロニセラ ペリクリメナム）を 弱、
#   「Flowering may decline and foliage may wilt in the heat of the summer」（フクシア）「protect from hot afternoon sun」（シベリアアヤメ）
#   「foliage typically depreciates in the heat」（プリムラ ベリス）を 中 に足した。「more tolerant of heat and humidity than other types of primroses」のような
#   ほかとの比較は 強 にしない（「better than most」と同じ扱いで 中）。フクシアの「does best in cool moist conditions」は気候ではなく場所の条件とも読めるので当てていない。
#   2026-11-20（batch_12）: 「Best performance occurs in cool summer climates」（アストランティア）「Best performance in climates with cool summers」（リグラリア デンタータ）
#   「Best performance occurs in cool climates」（プルサティラ）「prefers cool growing conditions」（ヤマアジサイ・エゾアジサイ。試作の P25 と同じ 弱）を 弱、
#   「protection … from hot summer temperatures」（ヘデラ）を 中、「Tolerates high heat and humidity」（アンドロポゴン スコパリウス）
#   「Tolerant of hot and humid summers」（オミナエシ・オトコエシ。試作の P19 と同じ 強）「tolerates, heat, humidity」（ノリウツギ）を 強 に足した。
#   2026-11-20（batch_17）: 「Somewhat intolerant of high summer heat and humidity」「did not do well … in the hot and humid St. Louis」（セスレリア オータムナリス）
#   「It does poorly in hot, dry sites」「grows slowly and poorly in hot climates」「will not do well in hot, dry sites」（スポディオポゴン）
#   「Best in regions with cool summers」（Walters のエーデルワイス）「In hot, humid summer regions, plants do not usually last more than 2 to 3 years」
#   （Walters のデルフィニウム。蒸れも 弱）を 弱、「Stems tend to flop in … hot summer temperatures」（フィソステギア）を 中、
#   「perform beautifully in the Piedmont and coastal plain, where true Lupines don't grow well because of the heat」（サーモプシス）
#   「Roses are heat and frost-tolerant」（NC State のバラの属のページ）を 強 に足した。蒸れ 弱:「It can be a challenge to grow them in humid summer climates
#   south of USDA Zone 7」（NC State のデルフィニウムの属のページ）。蒸れ 強:「Tolerant of hot, humid summer regions」（Walters のアムソニア フブリヒティ）
#   「a particularly good selection for humid climates」（MBG のバラ 'Sir Thomas Lipton'）。
#   2026-11-20（batch_18）: 「less successful in the high summer heat and humidity of the deep South」「Does not perform well in climates with high humidity」
#   （NC State のセラスチウム。蒸れも 弱）「It can struggle in our hot southern summers」（NC State のヤナギラン）「Plants generally thrive in cool summer climates」
#   「prefers cooler weather」（バレリアン）を 弱、「may go partially dormant in hot weather」（コエレリア）を 中、「Ground cover for hot, dry areas」（スポロボルス）
#   「loves hot, sunny sites」（Walters のロシアンセージ）を 強 に足した。ヤナギランの「It is absent from the hot and humid southeastern U.S.」は分布の説明なので当てていない。
P_AFTERNOON = r"shade is helpful if summers are hot|foliage (tends to|can) burn|afternoon shade|afternoon sun|scorch|leaf burn|protected from hot sun"


# MBG の品種ページの文を「属の記述」として同じ属のほかの種に広げない属。
# カンパニュラは MBG にページがあるのがホタルブクロの仲間（punctata・takesimana とその交配種）だけで、
# その文をラクティフローラやポルテンシュラギアナなど性質の違う種に当てると、推測で埋めることになるため。
# ペルシカリアも同じ（MBG の品種ページはアンプレクシカウリスだけで、アフィニスやミクロセファラに当てない）。
# セダムも同じ（MBG の品種ページは背の高いベンケイソウの仲間だけで、ミセバヤやウスリーの仲間に当てない）。
# カラマグロスティスも同じ（MBG の品種ページは × アクティフローラだけで、エピジジョスに当てない）。
GENUS_MBG_SKIP = {"Campanula", "Persicaria", "Sedum", "Calamagrostis", "Festuca", "Trifolium"}

# 学名で、ユーザーが個別に決めたもの（2026-11-19 のチェックリスト）
NAME_OVERRIDE = {
 "G05": ("Geranium 'Blogold'", "流通名 Blue Sunrise。RHS の表記に合わせた"),
 "G24": ("Geranium sanguineum 'New Hampshire Purple'", "RHS・MBG・シカゴ植物園の表記に合わせた"),
 "V05": ("Veronica spicata subsp. incana", "RHS の表記に合わせた。商品名はそのまま"),
 "V10": ("Veronica spicata", "RHS のページは亜種 subsp. spicata。種として売っているので今の学名のまま"),
}
NAME_OVERRIDE.update({
 "Lu02": ("Lupinus 'Fräulein'", "2026-11-19 の決定（試作のとき）。RHS は 'Noble Maiden' (Band of Nobles Series)"),
 "To02": ("Persicaria virginiana (Variegated Group) 'Painter's Palette'", "2026-11-21 ユーザーの回答: 売っているのは 'Painter's Palette' と同じ。RHS の表記"),
 "D10": ("Sedum reflexum", "2026-11-21 ユーザーの回答: マスターの学名（Sedum 'Vera Jameson'）は誤り。RHS では Sedum reflexum はシノニム扱い（Sedum rupestre の仲間）"),
 "Pq01": ("Physostegia virginiana", "2026-11-21 ユーザーの回答: 'Deep pink' は花色の意味で、品種名ではない"),
 "Ep01": ("Eupatorium album L.", "2026-11-21 ユーザーの回答: この種ではなく、フジバカマの白花など別のもの。種は未確定で、学名は直していない"),
 "Fu05": ("Fuchsia magellanica 'Variegata'", "RHS に同じ名前が2つあり（var. gracilis と var. macrostema）、どちらか分からない（2026-11-21 ユーザーの回答）"),
})
# 自社の観察（文献の値とは別に持つ）
OWN_NOTES = {"V04": "越冬：傷む年がある（2026-11-19 ユーザーの回答。シカゴ植物園の冬の傷みの記録と合う）"}


def yl_pick(rows, sp, sci=None):
    """YList の行から和名を選ぶ。種そのものの行（変種・亜種・品種でない）を先に採る（標準 → 広義 → synonym の順）。
    2026-11-20（batch_17・18）: 前は「標準」の最初の行を採っていたので、アマドコロがオオアマドコロ（var. maximowiczii）、
    ヤナギランがヤエザキヤナギラン（f. pleniflorum）、テンニンソウがミカエリテンニンソウ、イブキトラノオがオホーツクイブキトラノオになっていた。"""
    g, e = sp.split()[:2]
    # マスターの学名に変種・亜種・品種の名前があるときは、その行を先に採る（Athyrium niponicum var. pictum → ニシキシダ）
    inf = re.search(r"\b(?:var|subsp|ssp|f)\.\s*([a-z-]+)", sci or "")
    if inf and inf.group(1) != e:
        c = [x for x in rows if (x["sci"] + " ").startswith(f"{g} {e} ") and re.search(r" (var|subsp|ssp|f)\. " + inf.group(1) + r"\b", x["sci"])]
        c.sort(key=lambda x: x["status"] != "標準")
        if c:
            return c[0]
    # 引用符のある行（Hosta sieboldiana … 'Hypophylla' のような品種の行）は、種そのものの行にしない（2026-11-21）
    plain = [x for x in rows if (x["sci"] + " ").startswith(f"{g} {e} ") and "'" not in x["sci"] and not re.search(r" (var|subsp|ssp|f)\. ", x["sci"] + " ")]
    for st in ("標準", "広義", "synonym"):
        c = [x for x in plain if x["status"] == st]
        if c:
            return c[0]
    # 2026-11-23: 種そのものの行がないときは、基本変種・基本亜種（Campanula punctata var. punctata → ホタルブクロ）の行を採る。
    #   それもなければ空欄（前は最初の「標準」の行を採っていて、別の変種〔ヤマホタルブクロ〕や別の種〔Aster ericoides → Aster pilosus のキダチコンギク〕になっていた）
    auto = [x for x in rows if re.match(rf"{g} {e} .*?\b(?:var|subsp|ssp)\. {e}\b", x["sci"])
            and not re.search(rf"\b(?:var|subsp|ssp)\. {e}\b.*\b(?:var|subsp|ssp|f)\. ", x["sci"]) and "'" not in x["sci"]]
    auto.sort(key=lambda x: x["status"] != "標準")
    return auto[0] if auto else None


def judge(texts):
    """texts: [(文献名, レベル, 文)] → (耐暑性, 蒸れ, 午後の日陰の記述あり, 根拠)"""
    heat = muggy = None
    aft = False
    why = []
    hlv = set()
    rank = {"弱": 0, "中": 1, "強": 2}
    for src, lv, s in texts:
        low = s.lower().replace("\xa0", " ")  # 文献の文に改行しない空白が混じることがある（NC State のスティパ テヌイッシマ）
        h = "弱" if re.search(P_HEAT_WEAK, low) else "中" if re.search(P_HEAT_MID, low) else "強" if re.search(P_HEAT_STRONG, low) else None
        m = "弱" if re.search(P_MUGGY_WEAK, low) else "強" if re.search(P_MUGGY_STRONG, low) else "中" if re.search(P_MUGGY_MID, low) else None
        ws = "scorch" in low and "winter" in low and not re.search(r"hot|heat|summer", low)  # 冬の寒さ・日ざしによる葉の傷み（イベリス、ヘレボルス）は暑さ・西日の記述ではない
        if h == "中" and ws:
            h = None
        # 「Foliage tends to decline by late summer」（アスター コルディフォリウス）は、暑さの語がなく、葉の病気の話なので暑さの記述にしない（2026-11-21）
        if h == "中" and "decline by late summer" in low and not re.search(r"hot|heat", low):
            h = None
        if "better than most" in low or re.search(r"more tolerant of [^.]* than", low):  # 「同属の中では強い」という比較の書き方は 強 にしない
            h = "中" if h == "強" else h
            m = "中" if m == "強" else m
        if re.search(P_AFTERNOON, low) and not ws:
            aft = True
        if h or m or (re.search(P_AFTERNOON, low) and not ws):
            why.append(f"[{src}/{lv}] {s}")
        if h:
            hlv.add(lv)
        if h and (heat is None or rank[h] < rank[heat]):  # 割れたら控えめな側
            heat = h
        if m and (muggy is None or rank[m] < rank[muggy]):
            muggy = m
    return heat, muggy, aft, why, hlv


SUN_MODE = "fill"  # 日照の決め方（2026-11-23 ユーザーの回答「はい」で "fill"。下の「日照・USDA・水分」の説明。DECISIONS.md）
SUNR = {"日向": 0, "日向〜半日陰": 1, "半日陰": 2, "日陰": 3}
SUN_MBG = {"Full sun": "日向", "Full sun to part shade": "日向〜半日陰", "Part shade to full shade": "半日陰", "Part shade": "半日陰", "Full shade": "日陰"}
WATER_MBG = {"Dry to medium": "乾燥寄り", "Medium": "適湿", "Medium to wet": "湿潤寄り", "Dry": "乾燥寄り", "Wet": "湿潤寄り"}
LEAF_W = {"Blue": "ブルー系", "Yellow": "ゴールド・ライム系", "Gold": "ゴールド・ライム系", "Chartreuse": "ゴールド・ライム系", "Variegated": "斑入り",
          "Silvery Grey": "シルバー系", "Grey": "シルバー系", "Deep Green": "グリーン系", "Light Green": "グリーン系", "Green": "グリーン系",
          "Burgundy": "パープル・ブラック系", "Purple": "パープル・ブラック系", "Bronze": "ブロンズ・レッド系", "Red": "ブロンズ・レッド系"}
COLOR_W = {"Mauve/Lilac": "青・紫", "Deep Blue": "青・紫", "Light Blue": "青・紫", "Purple": "青・紫", "Deep Purple": "青・紫", "Blue": "青・紫",
           "Violet": "青・紫", "White": "白", "Cream": "白", "Light Pink": "ピンク", "Deep Pink": "ピンク", "Pink": "ピンク", "Rose": "ピンク",
           "Magenta": "ピンク", "Red": "赤", "Yellow": "黄", "Orange": "オレンジ・アプリコット", "Lavender": "青・紫"}
LICHT = {"sonnig": "日向", "absonnig": "半日陰", "halbschattig": "半日陰", "schattig": "日陰"}
PEST = [("slug", "ナメクジ"), ("snail", "カタツムリ"), ("leaf spot", "斑点病"), ("rust", "さび病"), ("powdery mildew", "うどんこ病"),
        ("downy mildew", "べと病"), ("root rot", "根腐れ"), ("crown rot", "株腐れ"), ("nematode", "葉センチュウ"), ("scale", "カイガラムシ"),
        ("virus", "ウイルス病"), ("deer", None), ("rabbit", None)]


MON_DE = {"Januar": 1, "Februar": 2, "März": 3, "April": 4, "Mai": 5, "Juni": 6, "Juli": 7, "August": 8, "September": 9,
          "Oktober": 10, "November": 11, "Dezember": 12}
MON_EN = {m: i for i, m in enumerate(["January", "February", "March", "April", "May", "June", "July", "August", "September",
                                      "October", "November", "December"], 1)}
SEASON_W = {"Early Spring": "早春", "Mid Spring": "春", "Late Spring": "晩春", "Early Summer": "初夏", "Mid Summer": "盛夏",
            "Late Summer": "晩夏", "Early Fall": "初秋", "Mid Fall": "秋", "Late Fall": "晩秋", "Winter": "冬"}


def lit_height_bloom(w, m, mlv, s, slv, rh, is_cv):
    """2026-11-23（ユーザーの指示「4を始める」）: 今のマスターの値と見比べる、文献の草丈・花期。値には使わない（見返し用の列）。
    草丈は品種の数値を優先（株張りと同じ。trial/RULES.md の数値の例外）: Walters（品種）→ MBG（品種）→ stauden.de（品種）→ MBG（種）→ stauden.de（種）→ RHS の幅。
    花期は月で書いてある stauden.de（ドイツ）→ MBG（セントルイス）。どちらもなければ Walters の季節。"""
    ht = bl = None
    hs = [x for x in (w["f"].get("Height", []) if w else []) if "cm" in x]
    mh = re.search(r"([\d.]+) to ([\d.]+) feet", m["f"].get("Height", "")) if m else None
    sh = (s["f"].get("Blüten-Höhe von") or s["f"].get("Wuchs-Höhe von"), s["f"].get("Blüten-Höhe bis") or s["f"].get("Wuchs-Höhe bis")) if s else (None, None)
    # stauden.de は品種のページにも、種・属から引き継いだ値が載る（値ごとに "cultivar"／"species"／"genus" の印）。
    #   2026-11-23：その印で文献の段階を決める（品種のページでも、印が species なら 種 の値として扱う）。
    #   "cultivar" はそのページ自身の値（種のページでも cultivar と付く）なので、ページの段階のまま
    LV = {"cultivar": slv, "species": "種", "genus": "属"}
    shl = slv
    if sh[0] or sh[1]:
        shl = LV.get((sh[0] or sh[1])[0][1], slv)
    sh = (sh[0][0][0] if sh[0] else None, sh[1][0][0] if sh[1] else None)
    cands = []
    if hs:
        cands.append((0, hs[0].replace(" cm", "").replace("-", "〜") + "（Walters・品種）"))
    if mh:
        cands.append((1 if mlv == "品種" else 3, f"{round(float(mh[1]) * 30.48)}〜{round(float(mh[2]) * 30.48)}（MBG・{mlv}）"))
    if sh[0] or sh[1]:
        cands.append((2 if shl == "品種" else 4, "〜".join(x for x in dict.fromkeys(sh) if x) + f"（stauden.de・{shl}）"))
    if rh and rh["f"].get("Max Height"):
        mm = re.search(r"([\d.]+)-([\d.]+) metre", rh["f"]["Max Height"].replace("–", "-"))
        if mm:
            cands.append((5, f"{round(float(mm[1]) * 100)}〜{round(float(mm[2]) * 100)}（RHS の幅）"))
    cands = [c for c in cands if "・属）" not in c[1]]  # 属のページの値は使わない
    if is_cv:  # 品種の商品には、種のページの草丈を使わない（DECISIONS.md の「種のページの情報」）
        cands = [c for c in cands if "・種）" not in c[1]]
    if cands:
        ht = min(cands)[1]
    sv = s["f"].get("Blütezeit von") if s else None
    sb = s["f"].get("Blütezeit bis") if s else None
    mb = re.search(r"Bloom Time: (\w+) to (\w+)", m["f"].get("BloomTime", "")) if m else None
    mb1 = re.search(r"Bloom Time: (\w+)$", m["f"].get("BloomTime", "").strip()) if m else None
    bc = []
    if sv and MON_DE.get(sv[0][0]):
        a = MON_DE[sv[0][0]]
        b = MON_DE.get(sb[0][0], a) if sb else a
        bl_ = LV.get(sv[0][1], slv)  # 花期も値ごとの印で段階を決める
        bc.append((0 if bl_ == "品種" else 2, f"{a}〜{b}月（stauden.de・{bl_}。ドイツ）" if a != b else f"{a}月（stauden.de・{bl_}。ドイツ）"))
    if mb and mb[1] in MON_EN and mb[2] in MON_EN:
        bc.append((1 if mlv == "品種" else 3, f"{MON_EN[mb[1]]}〜{MON_EN[mb[2]]}月（MBG・{mlv}。セントルイス）"))
    elif mb1 and mb1[1] in MON_EN:
        bc.append((1 if mlv == "品種" else 3, f"{MON_EN[mb1[1]]}月（MBG・{mlv}。セントルイス）"))
    if w and w["f"].get("Blooming Time"):
        ss = [v for k_, v in SEASON_W.items() if k_ in w["f"]["Blooming Time"]]
        if ss:
            bc.append((4, "・".join(ss) + "（Walters・品種。季節）"))
    bc = [c for c in bc if "・属。" not in c[1]]
    if bc:
        bl = min(bc)[1]
    return ht, bl


def walters(k):
    p = f"{RAW}/walters/{k}.html"
    if not os.path.exists(p):
        return None
    t = open(p, encoding="utf-8").read()
    url, t = t.split("\n", 1)
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    x = re.sub(r"[ \t\xa0]+", " ", html.unescape(re.sub(r"<[^>]+>", "\n", t)))
    lines = [s.strip() for s in x.split("\n") if s.strip()]
    r = {"url": url, "f": {}}
    try:
        i = next(n for n, s in enumerate(lines) if s.startswith("USDA Zone:"))
    except StopIteration:
        return None
    r["zone"] = lines[i].split(":")[1].strip()
    r["name"] = (lines[i - 2] if i >= 2 else "").replace("â„¢", "™").replace("Â®", "®")
    r["text"] = lines[i + 2] if "Plant number" in lines[i + 1] else lines[i + 1]
    labels = ["Sun Exposure", "Soil Type", "Soil pH", "Soil Moisture", "Care Level", "Flower Colour", "Blooming Time", "Foliage Color",
              "Plant Uses & Characteristics", "Flower Head Size", "Height", "Spread", "Foot Traffic", "Growth Rate", "Print this Plant"]
    cur = None
    for s in lines[i + 2:]:
        if s in labels:
            if s == "Print this Plant":
                break
            cur = s
            r["f"][cur] = []
        elif cur and s not in ("Optimal Growing Conditions", "Appearance and Characteristics"):
            r["f"][cur].append(re.sub(r"\s+or$", "", s))
    return r


RHS_PEST = [("slug", "ナメクジ"), ("snail", "カタツムリ"), ("vine weevil", "キンケクチブトゾウムシ"), ("capsid", "カスミカメ"), ("sawfl", "ハバチ"),
            ("aphid", "アブラムシ"), ("virus", "ウイルス病"), ("leaf spot", "斑点病"), ("powdery mildew", "うどんこ病"), ("downy mildew", "べと病"),
            ("rust", "さび病"), ("honey fungus", "ナラタケ病"), ("leafhopper", "ヨコバイ"), ("caterpillar", "イモムシ"), ("eelworm", "線虫"),
            ("root rot", "根腐れ"), ("crown rot", "株腐れ")]


def _species_alias():
    """fetch_all.py の SPECIES_ALIAS（同じ種の別の書き方）を読む。fetch_all.py は読み込むと動き出すので、辞書の部分だけ取り出す"""
    import ast
    t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fetch_all.py"), encoding="utf-8").read()
    a = t.index("SPECIES_ALIAS = {") + len("SPECIES_ALIAS = ")
    return ast.literal_eval(t[a:t.index("\n}\n", a) + 2])


SPECIES_ALIAS = _species_alias()


def adopt_name(it, rh, others):
    """学名（採用）を決める（2026-11-21 のチェックリスト 21〜24 の回答）。返すのは (採用する学名, メモ)。
    RHS が正名（Accepted／Correct）のときは RHS の表記にする: 別の属名が正名（Lychnis → Silene など）、流通名（[流通名] ('品種名') → 品種名にして流通名を残す）、つづりの違い。
    RHS の種がマスターと違う種のとき（同じ種の別の書き方ではないとき）は、ほかの文献（others）にも同じ種小名があるときだけ直す。
    マスターに品種名があるのに RHS の名前に品種名がないとき（Group、種のページ、ambig. など）は直さない。"""
    master = it["学名"]
    if not rh or rh["f"].get("Name Status") not in ("Accepted", "Correct"):
        return master, None
    name = re.sub(r"\s+", " ", re.sub(r"\((v|d|F|Pe|[a-z ]+)\)", "", rh["name"])).strip()
    name = re.sub(r" (L\.|Lam\.|Schrank \[\d+\])$", "", name)
    if re.search(r"ambig\.|misapplied", name):
        return master, None
    note = None
    m = re.match(r"^(.*?)\s*\[(.+?)\]\s*\('(.+)'\)", name)
    if m:
        name, note = f"{m.group(1)} '{m.group(3)}'", f"流通名 {m.group(2)}"
    if "'" in master and "'" not in name:
        return master, None
    if "'" in name:
        # 品種名のあとの付け足し（著者名、(G)・(Pf) のような区分の記号）は落とす。シリーズ名だけ残す
        last = name.rindex("'")
        ser = re.findall(r"\([^)]*Series\)", name[last + 1:])
        name = name[:last + 1] + (" " + ser[0] if ser else "")
        mc, rc = re.search(r"'(.+?)'(?!\w)", master), re.search(r"'(.+)'", name)
        if mc and rc and not m:
            import difflib
            import unicodedata
            nrm = lambda x: re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode().lower())
            if difflib.SequenceMatcher(None, nrm(mc.group(1)), nrm(rc.group(1))).ratio() < 0.8:
                return master, f"RHS の正名は {name}（品種名が違う。今の学名のまま）"
    else:
        # 品種名のない名前は、属・種小名・亜種／変種／品種までにする（著者名や説明の語を落とす）
        g = re.match(r"^([A-Z][a-z]+(?: ×)? [a-z-]+(?: (?:subsp\.|var\.|f\.) [a-z-]+)*)", name)
        if not g:
            return master, None
        name = g.group(1)
    low = lambda x: re.findall(r"\b[a-z][a-z-]{2,}\b", re.sub(r"'.*", "", x).replace("×", " "))
    rw = [w for w in low(name) if w not in ("subsp", "var", "ssp")]
    sp = it["species"]
    if not sp.endswith("hybrid") and rw:
        me = sp.split()[1]
        same = [me] + [w for a in SPECIES_ALIAS.get(sp, []) for w in low(a)]
        if rw[0] not in same and rw[0][:5] != me[:5]:  # 語尾だけの違い（caucasica／caucasia、-us／-um）は同じ種とみる
            if not any(rw[0] in (o or "").lower() for o in others):
                return master, f"RHS は {name}（種が違う。ほかの文献で確かめられないので今の学名のまま）"
            note = (note + "。" if note else "") + "RHS とほかの文献が同じ種"
    return name, note


def rhs(k):
    """RHS の詳細ページから、表の項目（dt/dd）と How to grow の文を取る"""
    if k not in RH.RHS:
        return None
    pid, name, memo = RH.RHS[k]
    p = f"{RAW}/rhs/{pid}.html"
    if not os.path.exists(p):
        return None
    t = open(p, encoding="utf-8", errors="replace").read()

    def cl(x):
        x = re.sub(r"<button.*?</button>|<dialog.*?</dialog>|<svg.*?</svg>|<script.*?</script>", "", x, flags=re.S)
        return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).strip()
    f = {}
    for a, b in re.findall(r"<dt[^>]*>(.*?)</dt>\s*<dd[^>]*>(.*?)</dd>", t, re.S):
        key = cl(a).split(" (function")[0].strip()
        if key and key not in f:
            f[key] = cl(b)
    # 日照（Position の見出しの下の Full sun・Partial shade・Full shade。表の項目 dt/dd にはない。2026-11-23 に追加）
    a = t.find(">Aspect</dt")
    i = t.rfind(">Position</h2>", 0, a if a >= 0 else len(t))
    if i >= 0:
        sp = re.findall(r"<span[^>]*>\s*(Full sun|Partial shade|Full shade)\s*</span>", t[i:a if a >= 0 else i + 5000])
        if sp:
            f["Position"] = "・".join(dict.fromkeys(sp))
    for lab in ("Cultivation", "Propagation", "Pruning", "Pests", "Diseases"):
        m = re.search(lab + r"\s*</h\d>\s*(.*?)</(?:div|section)>", t, re.S)
        if m:
            f[lab] = cl(m.group(1))
    # 土の種類（Growing Conditions の Chalk・Clay・Loam・Sand）と香り（Colour & Scent の Fragrance）は表の項目（dt/dd）にないので、本文から拾う
    x = cl(t)
    sm = re.search(r"Growing Conditions (.{0,40}?) Moisture", x)
    if sm and re.search(r"Chalk|Clay|Loam|Sand", sm.group(1)):
        f["_soil"] = sm.group(1)
    fm = re.search(r"Colour & Scent Fragrance (.{0,30}?) ?Season", x)
    if fm and re.search(r"Flower|Foliage", fm.group(1)):
        f["_frag"] = fm.group(1)
    # 「Suggested planting locations and garden types」に Coastal があるか（耐潮性の ○ のもと。2026-11-21）
    cm = re.search(r"Suggested planting locations and garden types (.{0,400}?)(?: Pruning | Pests | Diseases |$)", x)
    if cm and "Coastal" in cm.group(1):
        f["_coastal"] = "Coastal"
    # 「Colour & scent」の表（季節ごとの 花・葉 の色）
    i = t.find("Colour &")
    m = re.search(r"<table.*?</table>", t[i:] if i >= 0 else "", re.S)
    if m:
        fl, fo = [], []
        for row in re.findall(r"<tr[^>]*>(.*?)</tr>", m.group(0), re.S)[1:]:
            c = [cl(x) for x in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.S)]
            if len(c) >= 4:
                fl += [x.strip() for x in c[2].split(",") if x.strip()]
                fo += [x.strip() for x in c[3].split(",") if x.strip()]
        f["FlowerColour"] = list(dict.fromkeys(fl))
        f["FoliageColour"] = list(dict.fromkeys(fo))
    return {"name": name, "memo": memo, "url": f"https://www.rhs.org.uk/plants/{pid}/x/details", "f": f}


def pick(k, sk, gk, src):
    """品種 → 種 → 属 の順に、その文献のページを探す"""
    for key, lv in ((k, "品種"), (sk, "種"), (gk, "属")):
        if key and src in D.get(key, {}):
            return D[key][src], lv
    return None, None


def main():
    # 属レベルの代表: その属の MBG 品種ページでいちばん多い Culture の書き出し
    genus_mbg = {}
    for g in sorted({it["属"] for it in ITEMS}):
        c = Counter()
        for it in ITEMS:
            if it["属"] == g and "mbg" in D.get(it["id"], {}):
                c[D[it["id"]]["mbg"]["f"].get("Culture", "")[:80]] += 1
        if g not in GENUS_MBG_SKIP and c and c.most_common(1)[0][1] >= 2 and c.most_common(1)[0][1] >= 0.7 * sum(c.values()):  # 属のどの品種ページもほぼ同じ文のときだけ、属の記述として使う
            top = c.most_common(1)[0][0]
            for it in ITEMS:
                if it["属"] == g and D.get(it["id"], {}).get("mbg", {}).get("f", {}).get("Culture", "")[:80] == top:
                    genus_mbg[g] = D[it["id"]]["mbg"]
                    break
    for g, m in genus_mbg.items():
        D.setdefault("ge_" + g, {})["mbg"] = m
    rows = []
    cols = ["ID", "商品番号", "植物名", "学名（マスター）", "学名（採用）", "学名（RHS）", "文献での表記", "和名", "花色（分類）", "花色（文献の語）", "株張り(cm)", "葉色（分類）", "日照",
            "USDA", "RHS 耐寒性", "原産地", "耐暑性", "蒸れ耐性", "西日耐性", "暑さ・蒸れ・西日の根拠", "乾燥耐性", "土壌水分", "常緑性", "増え方", "病害虫", "切り戻し", "繁殖", "紅葉", "文献の注意", "自社の観察", "切り花", "蜜源", "花色（自社の値）", "株張り（自社の値・cm）", "葉色（自社の値）",
            "品種ページのある文献", "使った文献", "空欄の数", "耐暑性の決め方", "耐暑性（欧米の文献だけなら）",
            "蒸れ耐性（欧米の文献だけなら）", "西日耐性（おぎはらの暖地の日照を入れる前）", "乾燥耐性の出どころ", "耐暑性の信頼度", "日照（RHS）", "草丈（文献）", "花期（文献）", "西日耐性（日照ごと）",
            "科名", "香り", "毒性", "pH・土質", "こぼれ種の量(0-3)", "地下茎で広がる程度(0-3)", "こぼれ種・地下茎の根拠",
            "NC State の Resistance To Challenges", "RHS の Drought Resistance", "夏前の切り戻し", "毎年〜2年ごとの更新", "切り戻し・更新の根拠",
            "成株シルエット", "成株シルエット（種の記述なら）", "成株シルエットの根拠", "葉の特徴", "葉の特徴（種の記述なら）", "耐潮性", "耐潮性の根拠",
            "株分けの間隔", "株分けの間隔の根拠", "混植適性", "混植適性の根拠", "広がりすぎの注意", "切り戻し・手入れの文（全部）", "項目の文献"]
    for it in ITEMS:
        k = it["id"]
        sk = "sp_" + slug(it["species"])
        gk = "ge_" + it["属"]
        own = D.get(k, {})
        w = walters(k)
        og = OGI.get(k)
        ga = GA.GAISS.get(k)
        ga_own = bool(ga) and (ga[2] == "cultivar" or not it.get("品種名"))  # 種のページを品種に当てた分は、品種ページに数えず花色も取らない
        rh = rhs(k)
        r = dict.fromkeys(cols)
        r.update({"ID": k, "商品番号": it["商品番号"], "植物名": it["植物名"], "学名（マスター）": it["学名"]})
        # 項目の文献（2026-11-21）: 値の後ろに文献名を付けていない項目について、どの文献の値かを残す（列名 → 「MBG・種」など）。値は変えない
        prov = {}

        def src(cols_, lab):
            for c in cols_:
                if r[c] not in (None, ""):
                    prov[c] = lab
        names = [f"{lab}: {x['name']}" for lab, x in (("stauden.de", own.get("sdb")), ("MBG", own.get("mbg")), ("Walters", w)) if x]
        if ga:
            names.append("Gaißmayer: " + ga[1] + ("" if ga_own else "（種のページ）"))
        if og:
            names.append("おぎはら: " + og[2])
        r["文献での表記"] = " ／ ".join(names) or None
        y = D.get(sk, {}).get("yl")
        if y:
            yp = yl_pick(y["rows"], it["species"], it["学名"])
            r["和名"] = yp["ja"] + "（種）" if yp else None
        used, cv_src = set(), []
        if rh:
            # 名前だけの登録（栽培・色の項目が1つもないページ）は品種ページに数えない
            if set(k2 for k2, v2 in rh["f"].items() if v2) - {"Time to Maturity", "Family", "Native to GB/Ireland", "Genus", "Name Status", "Plant Range"}:
                cv_src.append("RHS")
            r["学名（RHS）"] = rh["name"] + (f"（{rh['memo']}）" if rh["memo"] else "") + (f" [{rh['f']['Name Status']}]" if rh["f"].get("Name Status") else "")
        for lab, x in (("stauden.de", own.get("sdb")), ("MBG", own.get("mbg")), ("Walters", w), ("Gaißmayer", ga_own), ("おぎはら", og and og[3] == "cultivar")):
            if x:
                cv_src.append(lab)
        # --- 品種のページからだけ取る項目
        if w:
            fc = w["f"].get("Flower Colour", [])
            r["花色（文献の語）"] = "、".join(fc) or None
            r["花色（分類）"] = "、".join(dict.fromkeys(COLOR_W[c] for c in fc if c in COLOR_W)) or None
            sp_cm = next((s for s in w["f"].get("Spread", []) if "cm" in s), None)
            r["株張り(cm)"] = sp_cm.replace(" cm", "").replace("-", "〜") if sp_cm else None
            lf = [LEAF_W[c] for c in w["f"].get("Foliage Color", []) if c in LEAF_W]
            r["葉色（分類）"] = "斑入り" if "斑入り" in lf else (lf[0] if lf else None)
            used.add("Walters")
            src(("花色（文献の語）", "花色（分類）", "株張り(cm)", "葉色（分類）"), "Walters・品種")
        if ga_own and not r["花色（文献の語）"]:
            r["花色（文献の語）"] = ga[3]
            used.add("Gaißmayer")
            src(("花色（文献の語）",), "Gaißmayer・" + ("品種" if ga[2] == "cultivar" else "種"))
        # --- 日照・USDA・水分（品種 → 種 → 属）
        m, mlv = pick(k, sk, gk, "mbg")
        s, slv = pick(k, sk, None, "sdb")
        # 2026-11-23: RHS の日照（Position）。SUN_MODE で決め方を切り替える（ユーザーの回答待ち。DECISIONS.md）
        #   "mbg": 今まで（MBG → Walters → stauden.de。RHS は使わない） "rhs": RHS を最優先（trial/RULES.md の順位 s01 > … > s02）
        #   "shade": RHS と MBG の両方があって違うときは、日陰寄りの側
        rsun = None
        if rh and rh["f"].get("Position"):
            ps = rh["f"]["Position"]
            rsun = ("日向〜半日陰" if "Full sun" in ps and "Partial shade" in ps else "日向" if "Full sun" in ps
                    else "半日陰" if "Partial shade" in ps else "日陰")
        r["日照（RHS）"] = rsun
        if rsun and SUN_MODE == "rhs":
            r["日照"] = rsun
            src(("日照",), "RHS・品種")
        if m:
            f = m["f"]
            if not r["日照"]:
                r["日照"] = SUN_MBG.get(f.get("Sun", "")[5:].strip())
                src(("日照",), f"MBG・{mlv}")
                if rsun and SUN_MODE == "shade" and r["日照"] and SUNR[rsun] > SUNR[r["日照"]]:
                    r["日照"] = rsun
                    src(("日照",), "RHS・品種")
            z = re.search(r"(\d+) to (\d+)", f.get("Zone", ""))
            r["USDA"] = f"{z[1]}〜{z[2]}（MBG・{mlv}）" if z else None
            r["土壌水分"] = WATER_MBG.get(f.get("Water", "")[7:].strip())
            used.add("MBG")
            src(("土壌水分",), f"MBG・{mlv}")
        if not r["日照"] and w and w["f"].get("Sun Exposure"):
            se = w["f"]["Sun Exposure"]
            r["日照"] = "日向〜半日陰" if "Full Sun" in se and "Partial Shade" in se else "日向" if "Full Sun" in se else "半日陰" if "Partial Shade" in se else "日陰"
            src(("日照",), "Walters・品種")
        if not r["日照"] and s and "Lichtansprüche" in s["f"]:
            L = [LICHT.get(v) for v, _ in s["f"]["Lichtansprüche"]]
            r["日照"] = "日向〜半日陰" if "日向" in L and "半日陰" in L else "日向" if "日向" in L else "半日陰" if "半日陰" in L else "日陰"
            used.add("stauden.de")
            src(("日照",), f"stauden.de・{sdb_lv(s, 'Lichtansprüche', slv)}")
        #   "fill": 今まで（MBG → Walters → stauden.de）で空欄のときだけ RHS
        if not r["日照"] and rsun and SUN_MODE == "fill":
            r["日照"] = rsun
            src(("日照",), "RHS・品種")
        r["草丈（文献）"], r["花期（文献）"] = lit_height_bloom(w, m, mlv, s, slv, rh, "'" in (it["学名"] or ""))
        if not r["USDA"] and w:
            r["USDA"] = w["zone"].replace("-", "〜") + "（Walters・品種）"
        # --- 暑さ・蒸れ・西日
        texts = []
        if m:
            for sct in ("Culture", "Problems", "Noteworthy", "GardenUses"):  # GardenUses は 2026-11-20（batch_11）に追加: ロニセラの「shrub for cool summer climates」
                texts += [("MBG", mlv, x) for x in sentences(m["f"].get(sct, ""))]
        n, nlv = pick(k, sk, None, "ncsu")
        nl = None
        if n:
            nl = "属" if n["url"].rstrip("/").split("/")[-1] == it["属"].lower() else nlv
            # Flower Description・Leaf Description は 2026-11-20（batch_11）に追加: フクシアの「Flowering may decline and foliage may wilt in the heat of the summer」
            for key in ("Description", "Insects, Diseases, and Other Plant Problems", "Flower Description", "Leaf Description"):
                texts += [("NC State", nl, x) for x in sentences(n["f"].get(key, ""))]
            used.add("NC State")
        if w:
            texts += [("Walters", "品種", x) for x in sentences(w["text"])]
        heat, muggy, aft, why, hlv = judge(texts)
        # 2026-11-24 総当たりの読み直し（ユーザー「総当たりで調べなおす」）: 欧米の文献だけでの耐暑性・蒸れ耐性は、全916品種の文を読み直した値
        # （heat_reread.json。scripts/tools/heat_reread_note.md）を使う。言い回しの照合（judge）の値と違えば根拠に残す。おぎはら以降の決め方は今までどおり
        rr = REREAD.get(str(it["商品番号"]))
        if rr:
            for lab_, old_, new_, q_ in (("耐暑性", heat, rr["欧米耐暑"], rr.get("欧米耐暑の決め手")), ("蒸れ耐性", muggy, rr["欧米蒸れ"], rr.get("欧米蒸れの決め手"))):
                if old_ != new_:
                    why.append(f"[読み直し 2026-11-24] 欧米の文献だけの{lab_}：言い回しの照合では {old_ or '空欄'}、文を読み直して {new_ or '空欄'}（{q_ or '記述なし'}）")
            heat, muggy = rr["欧米耐暑"], rr["欧米蒸れ"]
            if heat and not hlv:
                hlv = {re.sub(r"^\[[^・\]]*・([^\]]*)\].*$", r"\1", rr.get("欧米耐暑の決め手") or "") or "種"}
        r["耐暑性（欧米の文献だけなら）"] = heat
        r["耐暑性の決め方"] = "欧米の文献" if heat else None
        sib = getattr(OG, "SIBLING", {}).get(it["species"])
        if og and og[4]:  # 図鑑の耐暑性の欄が空欄のページ（1〜2年草扱いのオルラヤなど）は、耐暑性には使わない
            r["耐暑性の決め方"] = "おぎはら（" + ("品種" if og[3] == "cultivar" else "種") + "のページ）"
            # 2026-11-19 の最後の決定: おぎはら植物園にページがあれば、耐暑性はおぎはらの値を採る（日本の条件での評価）
            lab = "品種" if og[3] == "cultivar" else "種"
            if heat and og[4] != heat:
                why.append(f"[食い違い] 欧米の文献（{'・'.join(sorted(hlv))}の記述）は {heat} 相当。おぎはら植物園の値を採った")
            why.insert(0, f"[おぎはら/{lab}] 耐暑性；{og[4]}")
            heat = og[4]
            used.add("おぎはら")
        elif sib:
            # 2026-11-19 のユーザーの決定: おぎはらが同じ種の別品種をどれも同じ値にしているとき、載っていない同種の品種にもその値を使う。
            # あとで見返せるように、決め方と「欧米の文献だけなら」の値を別の列に残す（信頼度は低）。対象の種は <データのフォルダ>/ogihara_data.py の SIBLING
            if heat and sib[0] != heat:
                why.append(f"[食い違い] 欧米の文献（{'・'.join(sorted(hlv))}の記述）は {heat} 相当。おぎはら植物園の同じ種の品種の値を採った")
            why.insert(0, f"[おぎはら/同じ種の別品種（{'・'.join(sib[1])}）] 耐暑性；{sib[0]}（この品種のページはない。信頼度：低）")
            heat = sib[0]
            r["耐暑性の決め方"] = "おぎはら（同じ種の別品種から。信頼度：低）"
            used.add("おぎはら")
        r["耐暑性"], r["蒸れ耐性"] = heat, muggy
        drought = None
        alltext = " ".join(x for _, _, x in texts).lower()

        def hit(p):  # その言い回しが出てくる文献（どの文の言い回しで決めたか）
            return "・".join(dict.fromkeys(f"{lab}・{lv}" for lab, lv, x in texts if re.search(p, x.lower()))) or None
        if m and "Drought" in m["f"].get("Tolerate", ""):
            drought = "強"
            dsrc = f"MBG・{mlv}"
        elif re.search(r"some drought|occasional drought|tolerance for (some )?dry|(moderately|somewhat) drought[- ]tolerant", alltext) and not re.search(r"intolerant of (dry|drought)", alltext):
            drought = "中"
            dsrc = hit(r"some drought|occasional drought|tolerance for (some )?dry|(moderately|somewhat) drought[- ]tolerant")
        elif re.search(r"intolerant of (dry|drought)|never be allowed to dry out|(should|must) not be allowed to dry", alltext):
            drought = "弱"
            dsrc = hit(r"intolerant of (dry|drought)|never be allowed to dry out|(should|must) not be allowed to dry")
        # 2026-11-23: ハイフン付き（drought-tolerant）と tolerant of drought も拾う（前は拾えていなかった）
        elif re.search(r"tolerates drought|drought[- ]tolerant|(?<!in)tolerant of drought", alltext) or (w and "Drought Tolerant" in w["f"].get("Plant Uses & Characteristics", [])):
            drought = "強"
            dsrc = hit(r"tolerates drought|drought[- ]tolerant|(?<!in)tolerant of drought") or "Walters・品種"
        elif re.search(r"some drought|tolerance for (some )?dry", alltext):
            drought = "中"
            dsrc = hit(r"some drought|tolerance for (some )?dry")
        r["乾燥耐性"] = drought
        if drought and dsrc:
            prov["乾燥耐性"] = dsrc
        sun = r["日照"]
        # 冬の寒さ・日ざしによる葉の傷み（scorch … winter）は西日の判定に使わない
        hot_text = " ".join(x.lower() for _, _, x in texts
                            if not ("scorch" in x.lower() and "winter" in x.lower() and not re.search(r"hot|heat|summer", x.lower())))
        # 2026-11-23：日照ごとの西日耐性も出す（日照は今のマスターの値を使うので、combine.py がマスターの日照で選び直す）
        def west_for(sun_, heat_=heat, drought_=drought, aspect=True):
            if sun_ in ("半日陰", "日陰") or re.search(r"scorch|leaf burn|afternoon sun is", hot_text):
                w_ = "×"
            elif aft or heat_ == "弱":
                w_ = "△"
            elif sun_ and sun_.startswith("日向") and heat_ == "強" and drought_ == "強":
                w_ = "◎"
            elif heat_ in ("中", "強"):
                w_ = "○"
            else:
                w_ = None
            if aspect and rh and rh["f"].get("Aspect"):
                asp_ = rh["f"]["Aspect"].replace("–", "-")
                if "West-facing" not in asp_ and "South-facing" not in asp_:
                    w_ = "×"
                elif "West-facing" not in asp_ and w_ in (None, "○", "◎"):
                    w_ = "△"
            return w_
        west_by_sun = {x: west_for(x) for x in ("日向", "日向〜半日陰", "半日陰")}
        west = west_for(sun)
        if rh and rh["f"].get("Aspect"):
            asp = rh["f"]["Aspect"].replace("–", "-")
            if "West-facing" not in asp and "South-facing" not in asp:
                why.append(f"[RHS/品種] Aspect: {asp}（西向き・南向きが入っていない）")
            elif "West-facing" not in asp and west_for(sun, aspect=False) in (None, "○", "◎"):
                why.append(f"[RHS/品種] Aspect: {asp}（西向きが入っていない）")
            else:
                why.append(f"[RHS/品種] Aspect: {asp}")
            used.add("RHS")
        r["西日耐性"] = west
        # --- おぎはら植物園の楽天の商品ページ（2026-11-21 の決定。DECISIONS.md）
        #   耐暑性は図鑑の値（楽天のページと違うときは控えめな側）。おぎはら 強・欧米 弱 で、おぎはら自身も蒸れか暖地の日かげの注意を書いているときは 中。
        #   蒸れ耐性・西日耐性は、欧米の文献からの値と、おぎはらの文からの値のうち控えめな側。乾燥耐性は、空欄のときだけおぎはらの値を入れる。
        r["蒸れ耐性（欧米の文献だけなら）"] = muggy
        r["西日耐性（おぎはらの暖地の日照を入れる前）"] = west
        sh = SHOP.get(str(og[1])) if og else None
        if sh and sh.get("status") == "ok":
            lab = "品種" if og[3] == "cultivar" else "種"
            extra = []
            ho = shop_heat(sh)
            if ho and og[4] and ho != heat:
                if R3[ho] < R3[heat]:
                    extra.append(f"[おぎはら楽天/{lab}] 耐暑性: {sh['heat']}（図鑑は {heat}。控えめな側を採った）")
                    heat = ho
                else:
                    extra.append(f"[食い違い] おぎはらの楽天のページは 耐暑性: {sh['heat']}（図鑑は {heat}。控えめな側のまま）")
            mo, mwhy = shop_muggy(sh)
            wo = shop_west(sh)
            do = shop_dry(sh)
            if og[4] and heat == "強" and r["耐暑性（欧米の文献だけなら）"] == "弱" and (mo or wo in ("×", "△")):
                heat = "中"
                extra.append("[おぎはら 強・欧米 弱] おぎはら自身も楽天のページで蒸れ・暖地の日かげの注意を書いているので、中 にした")
                r["耐暑性の決め方"] += "＋楽天のページの注意（強 → 中）"
            if mo:
                extra.append(f"[おぎはら楽天/{lab}] {mwhy}（蒸れ {mo} 相当）")
                if muggy == "強":
                    extra.append("[食い違い] 蒸れ: 欧米の文献は 強 相当。控えめな側を採った")
                muggy = _low(muggy, mo, R3)
            if do and not drought:
                drought = do
                r["乾燥耐性の出どころ"] = f"おぎはら楽天・{lab}（耐乾性: {sh['dry']}）"
                prov["乾燥耐性"] = f"おぎはら楽天・{lab}"
            elif do and do != drought:
                r["乾燥耐性の出どころ"] = f"[食い違い] おぎはら楽天・{lab}は 耐乾性: {sh['dry']}（{do} 相当）。欧米の文献の値のまま"
            # 2026-11-24（矛盾の洗い出し）: 楽天のページで耐暑性・乾燥耐性が変わったあとの値で、西日耐性を決め直す
            # （前は変わる前の値で決めていたので、耐暑性 中 なのに西日 ◎ の品種があった。アルメリア 'Rubrifolia'）
            west = west_for(sun, heat_=heat, drought_=drought)
            west_by_sun = {x: west_for(x, heat_=heat, drought_=drought) for x in ("日向", "日向〜半日陰", "半日陰")}
            if wo:
                extra.append(f"[おぎはら楽天/{lab}] 日照 寒冷地: {sh['sun_cool']}／暖地: {sh['sun_warm']}（西日 {wo} 相当）")
                west = _low(west, wo, RW)
                west_by_sun = {k_: _low(v_, wo, RW) for k_, v_ in west_by_sun.items()}
            at = 1 if why and why[0].startswith("[おぎはら") else 0
            why[at:at] = extra
            r["耐暑性"], r["蒸れ耐性"], r["西日耐性"], r["乾燥耐性"] = heat, muggy, west, drought
            used.add("おぎはら")
        r["西日耐性（日照ごと）"] = "；".join(f"{k_}:{v_ or '空欄'}" for k_, v_ in west_by_sun.items())
        # --- 耐暑性の信頼度（2026-11-21 の決定。マスターだけに持ち、通販ページには出さない）
        #   高＝おぎはらのページの値と欧米の文献の値が同じ、低＝同じ種の別品種から・属の記述だけ、中＝それ以外（品種か種のページが1つ、または両方あって値が違う）
        dm = r["耐暑性の決め方"] or ""
        if not r["耐暑性"]:
            r["耐暑性の信頼度"] = None
        elif "同じ種の別品種" in dm or (dm == "欧米の文献" and hlv == {"属"}):
            r["耐暑性の信頼度"] = "低"
        elif dm.startswith("おぎはら") and r["耐暑性（欧米の文献だけなら）"] == r["耐暑性"]:
            r["耐暑性の信頼度"] = "高"
        else:
            r["耐暑性の信頼度"] = "中"
        r["暑さ・蒸れ・西日の根拠"] = "\n".join(why[:9]) or None
        # 2026-11-24 総当たりの読み直し用: 環境変数 DUMP_HEAT（フォルダ）があれば、暑さ・蒸れに関わりそうな文を文献ごとに全部書き出す（値は変えない）
        if os.environ.get("DUMP_HEAT"):
            HEATW = r"heat|hot|humid|summer|cool|warm|melt|rot\b|rots|swelter|afternoon|scorch|wilt|south|climate|zone|tropic|muggy|sultry|wet|drain"
            rtx = [("RHS", "品種", x) for key in ("Cultivation", "Pruning", "Propagation") for x in sentences(rh["f"].get(key, ""))] if rh else []
            dump = {"商品番号": it["商品番号"], "植物名": it.get("植物名"), "学名": it.get("学名"), "ID": k, "品種名あり": "'" in (it["学名"] or ""),
                    "文": [f"[{a}・{lv}] {x}" for a, lv, x in texts + rtx if re.search(HEATW, x.lower())],
                    "おぎはら図鑑": ({"耐暑性": og[4], "段階": "品種" if og[3] == "cultivar" else "種"} if og else None),
                    "おぎはら同じ種の別品種": sib, "おぎはら楽天": ({k_: v_ for k_, v_ in sh.items() if k_ not in ("html",)} if sh else None),
                    "今の値": {c: r.get(c) for c in ("耐暑性", "蒸れ耐性", "耐暑性（欧米の文献だけなら）", "蒸れ耐性（欧米の文献だけなら）", "耐暑性の決め方")}}
            with open(os.path.join(os.environ["DUMP_HEAT"], "heat_dump.jsonl"), "a", encoding="utf-8") as fh:
                fh.write(json.dumps(dump, ensure_ascii=False, default=str) + "\n")
        # --- 常緑性・増え方（stauden.de）
        if s:
            f = s["f"]
            ph = [v for v, _ in f.get("Blattphase", [])]
            r["常緑性"] = {"immergrün": "常緑", "wintergrün": "半常緑", "sommergrün": "落葉"}.get(ph[0]) + f"（stauden.de・{sdb_lv(s, 'Blattphase', slv, lambda v: v == ph[0])}）" if ph and ph[0] in ("immergrün", "wintergrün", "sommergrün") else None
            wv = [v for v, _ in f.get("Wuchsverhalten", [])]
            modes = []
            if any("horst" in v for v in wv):
                modes.append("株立ち")
            if any("rhizom" in v for v in wv):
                modes.append("地下茎")
            if any("ausläufer" in v or "kriechend" in v for v in wv):
                modes.append("ランナー")
            gen = [v for v, _ in f.get("MS-Generativer Ausbreitungsdrang", [])]
            if gen and "nicht" not in gen[0] and "steril" not in gen[0]:
                modes.append("こぼれ種")
            r["増え方"] = "、".join(dict.fromkeys(modes)) or None
            used.add("stauden.de")
            uses = [v for v, _ in f.get("Allgemeine Verwendungsmöglichkeiten", [])]
            if any("Schnitt" in v for v in uses):
                r["切り花"] = "○"
            if any("Insekten" in v for v in uses):
                r["蜜源"] = "○"
            src(("増え方",), f"stauden.de・{sdb_lv(s, ('Wuchsverhalten', 'MS-Generativer Ausbreitungsdrang'), slv)}")
            src(("切り花", "蜜源"), f"stauden.de・{sdb_lv(s, 'Allgemeine Verwendungsmöglichkeiten', slv)}")
        if w:
            u = w["f"].get("Plant Uses & Characteristics", [])
            if "Cut Flower" in u:
                r["切り花"] = "○"
                prov["切り花"] = "・".join(dict.fromkeys(x for x in (prov.get("切り花"), "Walters・品種") if x))
            if any("Attracts" in x for x in u):
                r["蜜源"] = "○"
                prov["蜜源"] = "・".join(dict.fromkeys(x for x in (prov.get("蜜源"), "Walters・品種") if x))
        # --- 病害虫・切り戻し（MBG の Problems / Culture）
        if m:
            pr = m["f"].get("Problems", "").lower()
            ps = [ja for en, ja in PEST if ja and en in pr]
            r["病害虫"] = ("、".join(dict.fromkeys(ps)) or ("特になし" if "no serious" in pr else None))
            if r["病害虫"]:
                r["病害虫"] += f"（MBG・{mlv}）"
            cu = m["f"].get("Culture", "").lower()
            codes = []
            if re.search(r"after flowering|spent flower|deadhead|after bloom", cu):
                codes.append("花後")
            if re.search(r"do not need to be cut back", cu):
                codes = ["不要"]
            r["切り戻し"] = "、".join(codes) + f"（MBG・{mlv}）" if codes else None
        if rh:
            f = rh["f"]
            r["RHS 耐寒性"] = f.get("Hardiness")
            fo = f.get("Foliage", "")
            ev = "半常緑" if "Semi" in fo else "常緑" if "Evergreen" in fo else "落葉" if "Deciduous" in fo else None
            if ev:
                r["常緑性"] = ev + "（RHS）"
            mo = f.get("Moisture", "").replace("–", "-")
            if mo:
                r["土壌水分"] = "湿潤寄り" if "Poorly-drained" in mo else "適湿" if "Moist but well-drained" in mo else "排水必須" if "Well-drained" in mo else r["土壌水分"]
                if re.search(r"Poorly-drained|Moist but well-drained|Well-drained", mo):
                    prov["土壌水分"] = "RHS・品種"
            if not r["株張り(cm)"] and f.get("Max Spread"):
                mm = re.search(r"([\d.]+)-([\d.]+) metre", f["Max Spread"])
                if mm:
                    r["株張り(cm)"] = f"{round(float(mm[1]) * 100)}〜{round(float(mm[2]) * 100)}（RHS の幅）"
            pd = (f.get("Pests", "") + " " + f.get("Diseases", "")).lower()
            ps = [ja for en, ja in RHS_PEST if en in pd]
            if ps:
                r["病害虫"] = "、".join(dict.fromkeys(ps)) + "（RHS）"
            elif "pest-free" in pd or "pest free" in pd:
                r["病害虫"] = "特になし（RHS）"
            pr = f.get("Pruning", "").lower()
            codes = []
            if re.search(r"after flowering|flowered stems|spent flower|deadhead|faded flower", pr):
                codes.append("花後")
            if re.search(r"end of the growing season|in autumn|dies back", pr):
                codes.append("秋")
            if re.search(r"late winter|early spring|in spring", pr):
                codes.append("早春")
            if "no pruning" in pr:
                codes = ["不要"]
            if codes:
                r["切り戻し"] = "、".join(codes) + "（RHS）"
            # 花色・葉色（RHS の Colour & scent の表）。Walters・Gaißmayer で入っていないときに使う
            RC = {"Blue": "青・紫", "Purple": "青・紫", "Pink": "ピンク", "White": "白", "Cream": "白", "Red": "赤", "Yellow": "黄", "Orange": "オレンジ・アプリコット"}
            if f.get("FlowerColour"):
                if not r["花色（文献の語）"]:
                    r["花色（文献の語）"] = "、".join(f["FlowerColour"]) + "（RHS）"
                if not r["花色（分類）"]:
                    r["花色（分類）"] = "、".join(dict.fromkeys(RC[c] for c in f["FlowerColour"] if c in RC)) or None
                    src(("花色（分類）",), "RHS・品種")
            fo = f.get("FoliageColour") or []
            if fo and not r["葉色（分類）"]:
                lc = ("斑入り" if "Variegated" in fo else "ブルー系" if "Blue" in fo else "ゴールド・ライム系" if ("Yellow" in fo or "Gold" in fo)
                      else "シルバー系" if ("Grey" in fo or "Silver" in fo) else "パープル・ブラック系" if "Purple" in fo
                      else "ブロンズ・レッド系" if ("Bronze" in fo or "Red" in fo) else "グリーン系" if "Green" in fo else None)
                if lc:
                    r["葉色（分類）"] = lc
                    r["_leaf_src"] = "RHS: " + ", ".join(fo)
                    prov["葉色（分類）"] = "RHS・品種"
            pg = f.get("Propagation", "").lower()
            ways = [ja for en, ja in (("division", "株分け"), ("cutting", "挿し木"), ("seed", "実生")) if en in pg]
            r["繁殖"] = "、".join(ways) + "（RHS）" if ways else None
            used.add("RHS")
        # --- シカゴ植物園の評価報告（ゲラニウム）: 品種ごとの株幅・秋の葉色・花後の切り戻し
        cb = JC.CBG.get(k) or JC.CBG_V.get(k)
        if cb:
            if cb[3] and not (w and w["f"].get("Spread")):
                wd = cb[3] if isinstance(cb[3], (tuple, list)) else (cb[3],)  # 幅で書かれている報告は (下限, 上限) のインチ
                r["株張り(cm)"] = "〜".join(str(round(x * 2.54)) for x in wd) + "（シカゴ植物園の試験での株幅）"
            if cb[4] and cb[4] != "none observed":
                r["紅葉"] = "秋に" + "・".join(JC.AUTUMN.get(c.strip(), c.strip()) for c in cb[4].split(",")) + "（シカゴ植物園）"
            if len(cb) > 7 and cb[7]:
                r["文献の注意"] = "シカゴ植物園: " + cb[7]
            if cb[5] == "Yes+" and not r["切り戻し"]:
                r["切り戻し"] = "花後（シカゴ植物園: 花後に切り戻すと姿が良くなった）"
            used.add("シカゴ植物園")
            if cb[1] == "cultivar":
                cv_src.append("シカゴ植物園")
        # --- Jelitto: 原産地と蜜源（種のページでも使える項目）。ゾーン・花期・高さ・暑さは使わない
        je = JEL.get(k)
        if je:
            if je[12]:
                r["原産地"] = je[12] + "（Jelitto・" + ("品種" if je[2] == "cultivar" else "種") + "）"
            if "honey-bee food plant" in je[11] and not r["蜜源"]:
                r["蜜源"] = "○"
                prov["蜜源"] = "Jelitto・" + ("品種" if je[2] == "cultivar" else "種")
            used.add("Jelitto")
            if je[2] == "cultivar":
                cv_src.append("Jelitto")
        # --- 自社の値: 文献で埋まらなかった花色・株張り・葉色に、今のマスターの値を別の列で残す（2026-11-19 決定）
        if not r["花色（文献の語）"] and it.get("花色"):
            r["花色（自社の値）"] = it["花色"]
        if not r["株張り(cm)"] and it.get("広がり(cm)"):
            r["株張り（自社の値・cm）"] = str(it["広がり(cm)"])
        if not r["葉色（分類）"] and it.get("葉色主分類"):
            r["葉色（自社の値）"] = it["葉色主分類"]
        # --- 記録だけの列（2026-11-21）: NC State の「Resistance To Challenges」（Heat・Humidity・Drought など）と RHS の「Drought Resistance」。
        #     判定には使っていない。属のページの分は入れない
        if n and nl != "属" and n["f"].get("Resistance To Challenges"):
            r["NC State の Resistance To Challenges"] = n["f"]["Resistance To Challenges"] + f"（{nl}）"
        if rh and rh["f"].get("Drought Resistance"):
            r["RHS の Drought Resistance"] = rh["f"]["Drought Resistance"]
        # 2026-11-21 の決定: 乾燥耐性が空欄のときだけ、NC State の項目（Drought・Dry Soil）か RHS の Drought Resistance: Yes から 中 を入れる。
        #   強 にしないのは、本文から 中 と決めた品種の多くにもこの項目が付いているため。耐暑性・蒸れ耐性には使わない（Heat・Humidity は本文と食い違う例が多い）
        if not r["乾燥耐性"]:
            tags = [t.strip() for t in re.sub(r"（.*?）$", "", r["NC State の Resistance To Challenges"] or "").split(";")]
            if "Drought" in tags or "Dry Soil" in tags:
                r["乾燥耐性"] = "中"
                r["乾燥耐性の出どころ"] = f"NC State・{nl} の Resistance To Challenges（{'・'.join(t for t in tags if t in ('Drought', 'Dry Soil'))}）"
                prov["乾燥耐性"] = f"NC State・{nl}"
            elif (r["RHS の Drought Resistance"] or "").strip().lower().startswith("yes"):
                r["乾燥耐性"] = "中"
                r["乾燥耐性の出どころ"] = "RHS の Drought Resistance: Yes"
                prov["乾燥耐性"] = "RHS・品種"
        # 2026-11-23 の決定（ユーザー「はい」）: まだ空欄で、MBG の Water が Medium なら 中。乾燥への強さの記述ではなく土の湿りからの推定なので、
        #   出どころに「推定」と信頼度 低 を書く（あとでこの印の品種だけ空欄に戻せる）。RHS の Moist but well-drained は使わない
        if not r["乾燥耐性"] and m and m["f"].get("Water", "")[7:].strip() == "Medium":
            r["乾燥耐性"] = "中"
            r["乾燥耐性の出どころ"] = f"推定（MBG・{mlv} の Water: Medium から。乾燥の記述ではない。信頼度：低）"
            prov["乾燥耐性"] = f"MBG・{mlv}"
        # --- 科名・香り・毒性・pH・土質・こぼれ種・地下茎（2026-11-21。scripts/pilot/extra_cols.py）
        r.update(extra_columns(it, rh, m, mlv, n, nl, s, slv, w, ga, ga_own, JEL.get(k), texts))
        # --- 夏前の切り戻し・毎年〜2年ごとの更新（管理タイプ C・D のもと。2026-11-21）
        r.update(prune_extra(texts, rh, ga, ga_own, og, SHOP.get(str(og[1])) if og else None))
        # --- 成株シルエット・葉の特徴・耐潮性・株分けの間隔・混植適性・広がりすぎの注意（2026-11-21。scripts/pilot/extra_cols.py の six）
        r["切り戻し・手入れの文（全部）"] = prune_all(texts, rh, ga, ga_own, og, SHOP.get(str(og[1])) if og else None, s, slv)
        r.update(six_columns(it, rh, m, mlv, n, nl, s, slv, w, ga, ga_own, og, SHOP.get(str(og[1])) if og else None, texts, r))
        # --- 学名（採用）: 2026-11-19 決定。RHS が正名（Accepted／Correct）としていれば RHS の表記に合わせる。
        #     RHS で未確定・シノニム・掲載なしのときは今の学名のまま（学名の検討シートに残す）
        #     2026-11-21: メモのある品種も RHS の正名に合わせる。決め方は adopt_name()
        adopted, note = it["学名"], None
        if k in NAME_OVERRIDE:
            adopted, note = NAME_OVERRIDE[k]
        else:
            je0 = JEL.get(k)
            adopted, note = adopt_name(it, rh, [r["文献での表記"], je0[1] if je0 else None])
        r["学名（採用）"] = adopted + (f"（{note}）" if note else "")
        if k in OWN_NOTES:
            r["自社の観察"] = OWN_NOTES[k]
        r["品種ページのある文献"] = "、".join(cv_src) or "なし"
        r["使った文献"] = "、".join(sorted(used)) or None
        r["項目の文献"] = "\n".join(f"{c}={v}" for c, v in prov.items() if r.get(c) not in (None, "")) or None
        core = ["花色（文献の語）", "株張り(cm)", "葉色（分類）", "日照", "USDA", "耐暑性", "蒸れ耐性", "西日耐性", "乾燥耐性", "土壌水分", "常緑性", "増え方", "病害虫",
                "切り戻し", "繁殖", "切り花", "蜜源", "和名"]
        r["空欄の数"] = sum(1 for c in core if r[c] in (None, ""))
        r["_core"] = core
        rows.append(r)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "下書き"
    ws.append(cols)
    for r in rows:
        ws.append([r[c] for c in cols])
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="2F6B4A")
    for row in ws.iter_rows(min_row=1):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    for i, wd in enumerate([6, 8, 30, 30, 40, 16, 10, 16, 9, 12, 12, 16, 7, 7, 7, 70, 7, 10, 16, 16, 24, 14, 6, 6, 22, 22, 7], 1):
        ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = wd
    ws.freeze_panes = "D2"

    def sheet(title, header, data, widths):
        w2 = wb.create_sheet(title)
        w2.append(header)
        for row in data:
            w2.append(row)
        for c in w2[1]:
            c.font = Font(bold=True, color="FFFFFF")
            c.fill = PatternFill("solid", fgColor="2F6B4A")
        for row in w2.iter_rows(min_row=1):
            for c in row:
                c.alignment = Alignment(wrap_text=True, vertical="top")
        for i, wd in enumerate(widths, 1):
            w2.column_dimensions[openpyxl.utils.get_column_letter(i)].width = wd
        w2.freeze_panes = "A2"

    # --- 根拠: 値ごとに、どの文献のどの階層（品種／種／属）から来たか
    ev = []
    for r in rows:
        for c in ("日照", "USDA", "RHS 耐寒性", "原産地", "乾燥耐性", "土壌水分", "常緑性", "増え方", "病害虫", "切り戻し", "繁殖", "紅葉", "株張り(cm)",
                  "花色（文献の語）", "葉色（分類）", "切り花", "蜜源", "和名"):
            v = r[c]
            if v in (None, ""):
                continue
            m = re.search(r"（([^（）]*)）$", str(v))
            ev.append([r["ID"], r["商品番号"], r["植物名"], c, v, m.group(1) if m else "（組み立て時に文献名を付けていない項目。使った文献の列を参照）"])
        for c in ("耐暑性", "蒸れ耐性", "西日耐性"):
            if r[c]:
                ev.append([r["ID"], r["商品番号"], r["植物名"], c, r[c], r["暑さ・蒸れ・西日の根拠"]])
        for c in ("花色（自社の値）", "株張り（自社の値・cm）", "葉色（自社の値）"):
            if r[c]:
                ev.append([r["ID"], r["商品番号"], r["植物名"], c, r[c], "今のマスターの値（文献に品種の記述がないため、自社の値として残した）"])
    sheet("根拠", ["ID", "商品番号", "植物名", "項目", "値", "文献・階層・根拠の文"], ev, [6, 8, 30, 18, 30, 90])

    # --- 学名の検討: マスターの学名と、文献での表記が違うもの
    def nz(x):
        x = re.sub(r"\(.*?\)|\[.*?\]|（.*?）", " ", x or "")
        x = x.replace("×", " ").replace("‘", "'").replace("’", "'")
        return re.sub(r"[^a-z]", "", re.sub(r"\bx\b", " ", x.lower()))
    nm = []
    for r in rows:
        k = r["ID"]
        own = D.get(k, {})
        rh = RH.RHS.get(k)
        cand = [("RHS", rh[1] if rh else None), ("stauden.de", own.get("sdb", {}).get("name")), ("MBG", own.get("mbg", {}).get("name"))]
        diff = [f"{lab}: {x}" for lab, x in cand if x and nz(x) != nz(r["学名（マスター）"])]
        status = re.search(r"\[(\w+)\]$", r["学名（RHS）"] or "")
        if diff or (status and status.group(1) not in ("Accepted", "Correct")) or (rh and rh[2]):
            nm.append([k, r["商品番号"], r["植物名"], r["学名（マスター）"], rh[1] if rh else None, status.group(1) if status else None,
                       " ／ ".join(diff) or None, rh[2] if rh else None, None])
    sheet("学名の検討", ["ID", "商品番号", "植物名", "今の学名", "RHS の表記", "RHS での扱い", "今の学名と違う表記", "メモ", "御社の判断（記入）"], nm,
          [6, 8, 30, 32, 36, 12, 60, 40, 24])
    wb.save(OUT)
    print("根拠", len(ev), "行 / 学名の検討", len(nm), "品種")
    core = rows[0]["_core"]
    print("品種", len(rows))
    print("項目ごとの空欄:", {c: sum(1 for r in rows if r[c] in (None, "")) for c in core})
    gen = {it["id"]: it["属"] for it in ITEMS}
    avg = {}
    for g in sorted(set(gen.values())):
        v = [r["空欄の数"] for r in rows if gen[r["ID"]] == g]
        avg[g] = round(sum(v) / len(v), 1)
    print("属ごとの平均空欄:", avg)
    print("耐暑", Counter(str(r["耐暑性"]) for r in rows), "蒸れ", Counter(str(r["蒸れ耐性"]) for r in rows), "西日", Counter(str(r["西日耐性"]) for r in rows))
    print("品種ページのある文献がない:", [r["ID"] for r in rows if r["品種ページのある文献"] == "なし"])
    json.dump([{c: r[c] for c in cols} for r in rows], open(OUT[:-5] + ".json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)


main()
