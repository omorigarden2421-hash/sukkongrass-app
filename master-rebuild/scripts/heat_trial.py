"""耐暑性・蒸れ耐性・西日耐性を分けて決める判定（2026-11-19。同日にユーザーが採用し、RULES.md に書いた）。
このファイルの D が28品種の判定で、scripts/sources/apply_heat_rows.py が trial/rows/ に反映する。

使い方: python3 scripts/heat_trial.py <出力.xlsx> <元のマスター.xlsx>
出力には元のマスターの値を並べる（答え合わせ用）。出力はリポジトリの外に置く。

ルール（RULES.md と同じ内容）
- 耐暑性（気温への強さ）: 弱＝暑さを嫌う・冷涼な気候が必要・暑い夏に弱る、の明記／中＝条件つき（暑い地域では午後の日陰、
  強い日なたで葉が焼ける、穏やかな夏を好む）／強＝heat tolerant の明記。文献が割れたら控えめな側。
- 蒸れ耐性（空気の湿気・株蒸れへの強さ。土の過湿とは別）: 弱＝高温多湿で溶ける・株腐れ・多湿の地域に向かない、の明記／
  中＝多湿で姿が乱れる・病気が出やすいが維持できる、風通しが必要／強＝humidity に耐える明記。
  「排水の悪い土で株腐れ」だけの記述は土の話なので使わない。
- 西日耐性: ×＝午後の日差しで葉が焼ける明記、または半日陰・日陰の植物／△＝暑い地域では午後の日陰を勧める記述、
  または耐暑性が弱／◎＝日なたで育ち、耐暑性 強・乾燥耐性 強で、午後の日陰を勧める記述がない／○＝それ以外で耐暑性が中以上。
- 耐暑性だけは、欧米の文献に暑さの記述がないとき、おぎはら植物園（s20。日本のナーサリー）の値を使う。蒸れ耐性・西日耐性には使わない。
- 文章の記述がないときは空欄。「補助」欄に、stauden.de の場所の区分・原産地・USDA 上限から見た目安を書く（値には入れない）。
"""
import glob
import json
import os
import sys

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, "..", "trial")

# 耐暑性を、おぎはら植物園（s20）の値から入れた品種。欧米の文献に暑さの記述がないときだけ使う（2026-11-19 決定）
OGIHARA_HEAT = ("P01", "P03", "P15", "P23")
# おぎはら植物園の耐暑性が、欧米の文献からの判定と違う品種（値は変えず conflicts に書く）
OGIHARA_CONFLICT = {
 "P08": "MBG は「暑い地域では午後の日陰を好む」（中）／おぎはら植物園は 強。欧米の文献に記述があるので 中 のまま",
 "P10": "NC State は「南部では葉焼けを防ぐため日陰に」（中）／おぎはら植物園は 強。欧米の文献に記述があるので 中 のまま",
 "P21": "MBG は「米国深南部の暑さと湿気に耐えない」「暑い夏に葉が傷む」（弱）／おぎはら植物園は 強（性質が強健で耐暑性があり）。欧米の文献に記述があるので 弱 のまま。差が大きいので要確認",
}

# 判定に使った記述が属のページだけの品種（rows の level に入れる）
LEVEL = {"P06": "genus"}

# 試作ID: (耐暑性, 蒸れ耐性, 西日耐性, 補助の目安, 根拠, 文献)
D = {
 "P01": ("中", "弱", "○", "",
         "耐暑: 欧米の文献に暑さだけの記述がないので、おぎはら植物園の値（中、種のページ）を使った。蒸れ: 大雨と高湿度のあと株の中心が腐って溶ける（melt-out）、夏が多湿な地域では強く刈り込む。アルテミシア属は湿度の高い気候に耐えない（NC State、属）。西日: 日なたで育ち乾燥に強い。午後の日陰を勧める記述なし",
         "シカゴ植物園、Walters、NC State"),
 "P02": ("中", "弱", "△", "",
         "耐暑: 同属の中では暑さと日なたに耐える（MBG）、Heat tolerant（Wildflower）。一方、夏が暑い所で日が強すぎると弱って葉を落とす（NC State）。割れているので控えめに 中。蒸れ: 米国南東部の高温多湿の夏にはあまり耐えない。西日: 暑い夏に日が強すぎると弱る",
         "MBG、NC State、Wildflower Center"),
 "P03": ("強", "中", "×", "",
         "耐暑: 欧米の文献に暑さだけの記述がないので、おぎはら植物園の値（強、品種のページ）を使った。蒸れ: とても湿度が高い条件と重い土で株腐れ、高温多湿の地域では風通しを良くする。この品種は疫病・茎腐れへの抵抗性が良い。西日: 葉焼けを防ぐため半日陰がよい（RHS）",
         "MBG、NC State、RHS"),
 "P04": ("弱", "弱", "△", "",
         "耐暑: 強い暑さを嫌う（RHS）、涼しく湿った条件を好む（NC State）。蒸れ: 高温多湿の夏の地域では盛夏に溶けて見苦しくなり、秋に回復することが多い（Walters）。西日: 耐暑性が弱",
         "RHS、NC State、Walters"),
 "P05": ("強", "強", "◎", "",
         "耐暑: Heat tolerant、暑く乾いた日なたに最も向く宿根草の一つ（Walters）。蒸れ: 高温多湿の夏と乾燥に耐える（MBG）。西日: 暑く乾いた日なた向き、乾燥に強い",
         "MBG、Walters"),
 "P06": ("強", None, "○", "",
         "耐暑: アガスタチ属は暑さと乾燥に耐える（NC State、属のページ）。蒸れ: 同じページに「米国南東部の夏に最もよく耐える種類（'Blue Fortune' など）を選ぶ」とあり、種類によって差があるが、この品種についての記述はないので空欄。西日: 日なたで育ち耐暑性 強。乾燥耐性の値がまだないので ◎ にしない",
         "NC State"),
 "P07": ("中", None, "△", "原産はピレネーの高地（Jelitto）。以前の基準（冷涼地・高山原産は弱）なら 弱",
         "耐暑: 夏の気温が高い地域の日なたでは水やりが余分に必要（属）。シカゴの試験で夏に急に弱った年がある。蒸れの記述なし。西日: 暑い地域の日なたは水が余分に必要",
         "シカゴ植物園"),
 "P08": ("中", "中", "△", "",
         "耐暑: 夏が暑い地域では午後に少し日陰になる所を好む（MBG）。蒸れ: 高温多湿や雨の多い夏には弱り、さび病にかかりやすい（NC State）。枯れる記述はないので 中。西日: 午後の日陰を好む",
         "MBG、NC State"),
 "P09": ("強", "強", "○", "",
         "耐暑・蒸れ: 夏の暑さと湿気に耐える（MBG、NC State）。西日: 暖かい地域では午後の日陰が最もよい（Walters）ので ◎ にしない",
         "MBG、NC State、Walters"),
 "P10": ("中", None, "×", "",
         "耐暑: 南部では葉焼けを防ぐため日陰〜木もれ日に植える（NC State、属）。蒸れの記述なし（株腐れは排水の悪い土の話）。西日: 午後の強い日差しはホスタには致命的（Walters）、強い日なたで葉が色あせる（Gaißmayer）",
         "NC State、Walters、Gaißmayer"),
 "P11": ("強", "強", "○", "",
         "耐暑・蒸れ: 夏の暑さと湿気に耐える（MBG）。西日: 日なたで育つが、乾燥耐性が 中 なので ○",
         "MBG"),
 "P12": ("強", "強", "◎", "",
         "耐暑・蒸れ: 乾燥・暑さ・湿気に耐える（MBG、NC State）。西日: 暑く風の強い条件に適応、乾燥に強い",
         "MBG、NC State、Walters"),
 "P13": ("強", "中", "◎", "",
         "耐暑: 暑さと湿気に耐える（Walters）。蒸れ: 多湿な気候では夏が進むと倒れて株が開く（MBG）。割れているので控えめに 中。西日: 日なたで育ち乾燥に強い",
         "MBG、Walters"),
 "P14": ("弱", None, "△", "",
         "耐暑: 涼しい海岸の環境を好む（NC State、種）。蒸れの記述なし（湿って肥えた土・重い粘土で株の中心が腐る、は土の話）。西日: 耐暑性が弱",
         "NC State、MBG"),
 "P15": ("強", None, "◎", "stauden.de は「涼しい所を好む」とする（記録のみ）",
         "耐暑: 欧米の文献に暑さの記述がないので、おぎはら植物園の値（強、品種のページ。「セダムの中でも特に性質が強健」）を使った。蒸れの記述なし。西日: 日なたで育ち、耐暑性 強・乾燥耐性 強で、午後の日陰を勧める記述なし",
         ""),
 "P16": ("中", "中", "△", "",
         "耐暑: 暖かい地域では半日陰が最もよい（Walters）、南部では午後に日陰を好む（MBG）。蒸れ: この属の多くは比較的乾いた空気を好む（NC State、属）。西日: 高温乾燥時に日なたで葉焼け、午後の日陰を好む",
         "MBG、NC State、Walters"),
 "P17": ("中", None, "△", "",
         "耐暑: セントルイス（夏が高温多湿）では午後に少し日陰になる所を好む（MBG、種）。条件つきなので 中。蒸れの記述なし。西日: 午後の日陰を好む",
         "MBG"),
 "P18": ("弱", "弱", "△", "",
         "耐暑: 冷涼な気候が必要、ゾーン7〜8 では一年草扱い（NC State、属）。蒸れ: 米国深南部の暑さと湿気を嫌う（MBG、NC State）。西日: 夏が暑い地域では午後に少し日陰を好む",
         "MBG、NC State"),
 "P19": ("強", "強", "◎", "",
         "耐暑・蒸れ: 高温多湿の夏によく耐える（MBG、NC State、Walters）。西日: 乾燥に強く、午後の日陰を勧める記述なし",
         "MBG、NC State、Walters"),
 "P20": ("中", None, "×", "",
         "耐暑: 夏が暑い地域で日なたに植えると葉が焼けやすい（MBG）。蒸れの記述なし。西日: 半日陰の植物で、日なたで葉が焼ける",
         "MBG"),
 "P21": ("弱", "弱", "△", "",
         "耐暑: 夏が暑い地域では花後に葉が傷む（MBG、種）。蒸れ: 米国深南部の暑さと湿気に耐えない（MBG、種）。西日: 強い日なたは土が乾きすぎないときだけ（Gaißmayer）",
         "MBG、Gaißmayer"),
 "P22": ("中", "中", "△", "stauden.de: 涼しい所を好む",
         "耐暑・蒸れ: とても暑く多湿な条件より、夏が穏やかな気候を好む（MBG、種）。枯れる記述はないので 中（以前の基準の例でも Phlox paniculata は 中）。うどんこ病には強い品種。西日: 穏やかな夏を好む",
         "MBG"),
 "P23": ("中", None, "△", "",
         "耐暑: 欧米の文献に耐性の記述がないので、おぎはら植物園の値（中、種のページ）を使った。蒸れの記述なし。西日: 夏が涼しい地域では日なた、それ以外は半日陰（Jelitto。日差しについての記述として使った）",
         "Jelitto"),
 "P24": ("強", None, "◎", "",
         "耐暑: 'Goldflame' は暑さによく耐えることで知られる（MBG）。蒸れの記述なし。西日: 乾燥に強く、午後の日陰を勧める記述なし",
         "MBG"),
 "P25": ("弱", None, "×", "",
         "耐暑: 涼しい生育条件を好む（NC State、種）。蒸れの記述なし。西日: 暖かい地域では強い日差しを避けないと葉と花が早く色あせ、焼ける",
         "NC State"),
 "P26": ("中", "中", "△", "",
         "耐暑: 涼しい地域に向く（NC State）、夏が暑い地域では午後に日陰になる場所がよい（MBG）。蒸れ: 高温多湿の夏にうどんこ病・斑点病が出やすい（MBG）。西日: 午後の日陰がよい",
         "MBG、NC State"),
 "P27": ("弱", None, "△", "",
         "耐暑: 夏が暑い地域（ゾーン7 より南）では弱り、病気にかかりやすくなる（MBG、NC State）。湿気についての記述ではないので蒸れは空欄。西日: 耐暑性が弱",
         "MBG、NC State"),
 "P28": (None, None, None, "手がかりなし（種が決まっていない）", "文献の記述なし", ""),
}


def main():
    out, master = sys.argv[1], sys.argv[2]
    ws0 = openpyxl.load_workbook(master, read_only=True)["Sheet1"]
    rows = list(ws0.iter_rows(values_only=True))
    head = rows[0]
    m = {r[1]: dict(zip(head, r)) for r in rows[1:] if r[1]}
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "試し判定（28品種）"
    cols = ["商品番号", "植物名", "耐暑性（試し）", "耐暑性（元）", "蒸れ耐性（試し）", "蒸れ耐性（元）", "西日耐性（試し）", "西日耐性（元）",
            "今の試作表の耐暑性", "元と違う項目", "根拠（文献の記述の要約）", "文献", "補助の目安（値には入れていない）", "御社の判断（記入）"]
    ws.append(cols)
    diff_n = {"耐暑性": 0, "蒸れ耐性": 0, "西日耐性": 0}
    both_n = dict(diff_n)
    for p in sorted(glob.glob(T + "/input/P*.json")):
        i = json.load(open(p, encoding="utf-8"))
        pid = i["id"]
        r = json.load(open(p.replace("input", "rows"), encoding="utf-8"))["fields"]
        no = i["商品番号"]
        o = m.get(int(no)) if str(no).isdigit() else None
        heat, muggy, west, aux, why, src = D[pid]
        old = [o and o.get(k) for k in ("耐暑性", "蒸れ耐性", "西日耐性")]
        diffs = []
        for name, new, ov in zip(diff_n, (heat, muggy, west), old):
            if new and ov:
                both_n[name] += 1
                if new != ov:
                    diff_n[name] += 1
                    diffs.append(name)
        ws.append([no, i["植物名"].replace("　", " "), heat, old[0], muggy, old[1], west, old[2], r["heat"].get("value"),
                   "、".join(diffs) or None, why, src or None, aux or None, None])
    fill = PatternFill("solid", fgColor="2F6B4A")
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = fill
        c.alignment = Alignment(wrap_text=True, vertical="center")
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    for col, w in zip("ABCDEFGHIJKLMN", (9, 32, 9, 9, 9, 9, 9, 9, 10, 16, 70, 22, 44, 20)):
        ws.column_dimensions[col].width = w
    ws.freeze_panes = "C2"
    ws2 = wb.create_sheet("試しのルール")
    for line in __doc__.strip().split("\n"):
        ws2.append([line])
    ws2.column_dimensions["A"].width = 120
    wb.save(out)
    print({k: f"{diff_n[k]}/{both_n[k]}" for k in diff_n})


if __name__ == "__main__":
    main()
