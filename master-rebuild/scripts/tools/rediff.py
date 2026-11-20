"""前の batch を今の assemble_pilot.py で作り直して、手元の下書き（JSON）と耐暑性・蒸れ・西日を比べる。
使い方（master-rebuild で）: rediff.py <ClaudeWork> <一時出力フォルダ>
"""
import glob
import json
import os
import subprocess
import sys

CW, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
T = "C:/Users/owner/AppData/Local/Temp/claude"
A = T + "/803dcd3d003c6b53/4b6386d0-6448-4907-be7f-4c2938beba51/scratchpad"
B = T + "/9eda375844c6e6aa/a4823c38-e78a-46f6-b54c-9f8733f815df/scratchpad"
C = T + "/5942321c1c0f279d/ea463099-8b77-426c-a604-bb613db7757b/scratchpad"
D = T + "/0f02706c790fef35/9e6508df-d005-4099-9883-c3e6eff4df83/scratchpad"
RAW = {2: A, 3: B, 4: B, 5: B, 6: B, 7: C, 8: C, 9: C, 10: C, 11: D}
KEY = {2: "下書き_ヘメロカリス*1119b.json", 3: "下書き_フロックス*.json", 4: "下書き_セダム*.json", 5: "下書き_ミント*.json", 6: "下書き_ポテンティラ*.json",
       7: "下書き_スカビオサ*.json", 8: "下書き_タリクトラム*.json", 9: "下書き_モナルダ*.json", 10: "下書き_ダイアンサス*.json",
       11: "下書き_ジギタリス*.json"}
for n in sorted(RAW):
    if len(sys.argv) > 3 and str(n) not in sys.argv[3:]:
        continue
    r = RAW[n]
    out = f"{OUT}/b{n}.xlsx"
    p = subprocess.run([sys.executable, "-X", "utf8", "scripts/pilot/assemble_pilot.py", f"batch_{n:02d}/input", f"{r}/b{n}_digest.json", f"{r}/b{n}_raw", out, f"batch_{n:02d}"],
                       capture_output=True, text=True, encoding="utf-8")
    if p.returncode:
        print("fail", n, p.stderr[-300:])
        continue
    old = sorted(glob.glob(f"{CW}/{KEY[n]}"))[-1]  # 一番新しい日付のもの
    o = {x["ID"]: x for x in json.load(open(old, encoding="utf-8"))}
    nw = {x["ID"]: x for x in json.load(open(out[:-5] + ".json", encoding="utf-8"))}
    ch = 0
    for k in nw:
        for c in ("耐暑性", "蒸れ耐性", "西日耐性", "耐暑性（欧米の文献だけなら）"):
            if o[k].get(c) != nw[k].get(c):
                ch += 1
                print(n, k, nw[k]["学名（マスター）"][:34], c, o[k].get(c), "→", nw[k].get(c))
    print("batch", n, "変化", ch, "（比べた下書き:", os.path.basename(old)[:22], "）")
