"""全部のまとまり（3属の試行・アスター・batch_02〜18）を今の assemble_pilot.py で作り直して、手元の下書き（JSON）と比べる。
使い方（master-rebuild で）: rediff.py <ClaudeWork> <一時出力フォルダ> [まとまり ...] [--save <末尾>]
  まとまりは pilot・aster・2〜18（省略すると全部）。
  --save 1121 のように付けると、作り直した Excel と JSON を、前の下書きの名前の末尾（_1119・_1120b など）を _1121 に替えた名前で ClaudeWork に置く
  （同じ名前がすでにあれば止まる。前のファイルは消さない）。
比べる列: 耐暑性・蒸れ耐性・西日耐性・乾燥耐性・耐暑性（欧米の文献だけなら）・和名。
"""
import collections
import glob
import json
import os
import re
import shutil
import subprocess
import sys

args = sys.argv[1:]
save = None
if "--save" in args:
    i = args.index("--save")
    save = args[i + 1]
    del args[i:i + 2]
CW, OUT = args[0], args[1]
only = args[2:]
os.makedirs(OUT, exist_ok=True)
T = "C:/Users/owner/AppData/Local/Temp/claude"
A = T + "/803dcd3d003c6b53/4b6386d0-6448-4907-be7f-4c2938beba51/scratchpad"
B = T + "/9eda375844c6e6aa/a4823c38-e78a-46f6-b54c-9f8733f815df/scratchpad"
C = T + "/5942321c1c0f279d/ea463099-8b77-426c-a604-bb613db7757b/scratchpad"
D = T + "/0f02706c790fef35/9e6508df-d005-4099-9883-c3e6eff4df83/scratchpad"
E = T + "/803dcd3d003c6b53/15533220-637a-4fd6-bea9-bf815c2d2368/scratchpad"
F = T + "/803dcd3d003c6b53/664da7c4-4721-4a49-8cb6-4c6efaf3c08a/scratchpad"
G = T + "/803dcd3d003c6b53/26b2b1f1-e379-4b33-8d33-fd862d2fee3c/scratchpad"
RAW = {2: A, 3: B, 4: B, 5: B, 6: B, 7: C, 8: C, 9: C, 10: C, 11: D, 12: D, 13: E, 14: E, 15: F, 16: F, 17: G, 18: G}
KEY = {2: "下書き_ヘメロカリス*.json", 3: "下書き_フロックス*.json", 4: "下書き_セダム*.json", 5: "下書き_ミント*.json", 6: "下書き_ポテンティラ*.json",
       7: "下書き_スカビオサ*.json", 8: "下書き_タリクトラム*.json", 9: "下書き_モナルダ*.json", 10: "下書き_ダイアンサス*.json",
       11: "下書き_ジギタリス*.json", 12: "下書き_シレネ*.json", 13: "下書き_ガウラ*.json", 14: "下書き_チャスマンティウム*.json",
       15: "下書き_アスクレピアス*.json", 16: "下書き_エピメディウム*.json",
       17: "下書き_レオントポディウム*.json", 18: "下書き_アゲラティナ*.json"}
# (名前, input, データのフォルダ〔None は scripts/pilot〕, digest, raw, 下書きの名前)
SETS = [("pilot", "pilot/input", None, A + "/pilot_digest.json", A + "/pilot_raw", "試行_3属*.json"),
        ("aster", "batch_aster/input", "batch_aster", A + "/aster_digest.json", A + "/aster_raw", "下書き_アスター*.json")]
SETS += [(str(n), f"batch_{n:02d}/input", f"batch_{n:02d}", f"{RAW[n]}/b{n}_digest.json", f"{RAW[n]}/b{n}_raw", KEY[n]) for n in sorted(RAW)]
COLS = ("耐暑性", "蒸れ耐性", "西日耐性", "乾燥耐性", "耐暑性（欧米の文献だけなら）", "和名")
tot = collections.Counter()
for name, inp, folder, dig, raw, key in SETS:
    if only and name not in only:
        continue
    out = f"{OUT}/b{name}.xlsx"
    cmd = [sys.executable, "-X", "utf8", "scripts/pilot/assemble_pilot.py", inp, dig, raw, out] + ([folder] if folder else [])
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if p.returncode:
        print("fail", name, p.stderr[-300:])
        continue
    old = sorted(glob.glob(f"{CW}/{key}"))[-1]  # 一番新しい日付のもの
    o = {x["ID"]: x for x in json.load(open(old, encoding="utf-8"))}
    nw = {x["ID"]: x for x in json.load(open(out[:-5] + ".json", encoding="utf-8"))}
    ch = collections.Counter()
    for k in nw:
        for c in COLS:
            if o[k].get(c) != nw[k].get(c):
                ch[c] += 1
                if os.environ.get("REDIFF_QUIET") != "1":
                    print(name, k, nw[k]["学名（マスター）"][:34], c, o[k].get(c), "→", nw[k].get(c))
    tot.update(ch)
    print("まとまり", name, "変化", sum(ch.values()), dict(ch), "（比べた下書き:", os.path.basename(old)[:22], "）")
    if save:
        stem = os.path.basename(old)[:-5]
        new = re.sub(r"_\d{4}[a-z]?$", "", stem) + "_" + save
        for ext in (".xlsx", ".json"):
            assert not os.path.exists(f"{CW}/{new}{ext}"), new
            shutil.copy(out[:-5] + ext, f"{CW}/{new}{ext}")
        print("   置いた:", new[:20], "…", new[-14:])
print("合計", dict(tot))
