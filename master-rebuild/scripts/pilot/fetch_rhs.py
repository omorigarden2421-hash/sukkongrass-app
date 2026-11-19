"""RHS の詳細ページを取得する（番号は <データのフォルダ>/rhs_ids.py。番号の探し方はそのファイルの冒頭を参照）。

使い方: python3 -I scripts/pilot/fetch_rhs.py <データのフォルダ> <保存先フォルダ（リポジトリの外）>
"""
import os
import subprocess
import sys
import time

sys.path.insert(0, sys.argv[1])
import rhs_ids  # noqa: E402

OUT = sys.argv[2] + "/rhs"
os.makedirs(OUT, exist_ok=True)
ok = 0
for k, (pid, name, _) in rhs_ids.RHS.items():
    out = f"{OUT}/{pid}.html"
    if not os.path.exists(out) or os.path.getsize(out) < 20000:
        subprocess.run(["curl", "-sSL", "-m", "40", "-A", "Mozilla/5.0", f"https://www.rhs.org.uk/plants/{pid}/x/details", "-o", out])
        time.sleep(1.0)
    ok += os.path.exists(out) and os.path.getsize(out) > 20000
print("RHS pages", ok, "/", len(rhs_ids.RHS))
