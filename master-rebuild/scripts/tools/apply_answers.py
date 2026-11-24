"""確認ページ（暑さ・剪定・文献との食い違い）の「回答の文」を読み、user_answers.json に入れる。combine.py がこれを読んで、まとめの表に反映する。

使い方: 回答の文をテキストファイルに貼って保存し、
  python scripts/tools/apply_answers.py 回答.txt   （master-rebuild で実行）
同じ品種の回答が前にもあれば、新しい回答で上書きする。日付も残す。
"""
import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "user_answers.json")
QMAP = json.load(open(os.path.join(HERE, "heat_page_map.json"), encoding="utf-8"))  # 暑さのページの問題番号 → 商品番号
HEAT = {"A": "強", "B": "中", "C": "弱"}  # A 強 のまま・B 中 にする・C 弱 にする
today = datetime.date.today().isoformat()


def split_top(s):
    """読点で切る。全角の括弧の中の読点では切らない"""
    out, depth, cur = [], 0, ""
    for ch in s:
        depth += ch == "（"
        depth -= ch == "）"
        if ch == "、" and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    out.append(cur.strip())
    return [x for x in out if x]


def items(s):
    """「70（メモ）、71」→ [(70, "メモ"), (71, None)]。全角の括弧の中の読点では切らない"""
    out, depth, cur = [], 0, ""
    for ch in s:
        depth += ch == "（"
        depth -= ch == "）"
        if ch == "、" and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    res = []
    for x in (y.strip() for y in out):
        m = re.match(r"^(\d+)(?:→([ABH]))?(?:（(.*)）)?$", x)
        if m:
            res.append((m.group(1), m.group(2), m.group(3)))
    return res


def line(text, head):
    m = re.search(r"^" + re.escape(head) + r"[：:](.*)$", text, re.M)
    return m.group(1).strip() if m and m.group(1).strip() not in ("なし", "") else ""


def main(path):
    raw = open(path, encoding="utf-8").read()
    heads = [h for h in ("暑さの確認の回答", "剪定不要と花茎切りの回答") if h in raw]
    part = {}  # 2つのページの回答をまとめて貼っても、備考が混ざらないように分ける
    for h in heads:
        i = raw.index(h)
        j = min([raw.index(k) for k in heads if raw.index(k) > i] or [len(raw)])
        part[h] = raw[i:j]
    db = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {"耐暑性": {}, "違うとの指摘": {}, "管理タイプ": {}}
    n = 0
    if "暑さの確認の回答" in part:
        text = part["暑さの確認の回答"]
        memos = {q: t for q, _, t in items(line(text, "備考"))}
        for q, v in re.findall(r"(\d+)([ABC])", line(text, "暑さの確認の回答")):
            for no in QMAP[q]:
                db["耐暑性"][str(no)] = {"値": HEAT[v], "問題": int(q), "備考": memos.get(q), "日付": today}
                n += 1
        for head, key in (("耐暑性 弱 で違うと思う品種（商品番号）", "耐暑性"), ("蒸れ耐性 弱 で違うと思う品種（商品番号）", "蒸れ耐性")):
            for no, _, t in items(line(text, head)):
                db["違うとの指摘"].setdefault(no, {})[key] = {"どう違うか": t, "日付": today}
                n += 1
    if "剪定不要と花茎切りの回答" in part:
        text = part["剪定不要と花茎切りの回答"]
        memos = {no: t for no, _, t in items(line(text, "備考"))}
        for head, v in (("A 放任型", "A"), ("B 花後刈込型", "B"), ("保留", "H")):
            for no, _, _ in items(line(text, head)):
                db["管理タイプ"][no] = {"値": v, "備考": memos.get(no), "日付": today, "ページ": "剪定不要と花茎切りの確認"}
                n += 1
    if "食い違いの確認の回答" in raw:  # 文献との食い違いの確認（2026-11-23）。「25-草丈M、45-株張りC（40〜50）」
        text = raw[raw.index("食い違いの確認の回答"):]
        body = line(text, "食い違いの確認の回答")
        if not body.startswith("（まだ"):
            for x in split_top(body):
                m = re.match(r"^(\d+)-(日照|耐寒性|花期|草丈|株張り)([MBC])?(?:（(.*)）)?$", x)
                if m:
                    db.setdefault("食い違い", {}).setdefault(m[1], {})[m[2]] = {"選択": m[3], "メモ": m[4], "日付": today}
                    n += 1
        for x in split_top(line(text, "外したもののうち確認したいもの")):
            if re.match(r"^\d+-(日照|耐寒性|花期|草丈|株張り)$", x):
                db.setdefault("外したものの確認", {})[x] = {"日付": today}
                n += 1
    if "未決の確認の回答" in raw:  # 未決の学名の確認（2026-11-23）。「Fu05=C、Ep01=A（メモ）、Dg05=B」。表への反映は回答を見てから作る
        body = line(raw[raw.index("未決の確認の回答"):], "未決の確認の回答")
        if not body.startswith("（まだ"):
            for x in split_top(body):
                m = re.match(r"^(\w+)=([A-D])?(?:（(.*)）)?$", x)
                if m:
                    db.setdefault("未決", {})[m[1]] = {"選択": m[2], "メモ": m[3], "日付": today}  # combine.py の name_answer が学名・流通名・和名に当てる
                    n += 1
    if not n:
        sys.exit("回答の文が見つかりません（「暑さの確認の回答：」「剪定不要と花茎切りの回答」「食い違いの確認の回答：」「未決の確認の回答：」で始まる文を貼ってください）")
    json.dump(db, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    print("入れた件数:", n, {k: len(v) for k, v in db.items()})


if __name__ == "__main__":
    main(sys.argv[1])
