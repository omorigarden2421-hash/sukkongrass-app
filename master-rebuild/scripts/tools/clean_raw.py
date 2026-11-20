"""落ちたときに壊れた生データ（JSON として読めないもの・中身が空の HTML）を消す。使い方: clean_raw.py <raw フォルダ>"""
import glob
import json
import os
import sys

raw = sys.argv[1]
bad = []
for f in glob.glob(raw + "/*/*.json"):
    try:
        json.load(open(f, encoding="utf-8"))
    except Exception:
        bad.append(f)
for f in glob.glob(raw + "/*/*.html"):
    b = open(f, "rb").read()
    if len(b) < 500 or b.count(b"\x00") > 100:
        bad.append(f)
print(len(bad), [os.path.relpath(f, raw) for f in bad])
for f in bad:
    os.remove(f)
    other = f[:-5] + (".html" if f.endswith(".json") else ".json")
    if os.path.exists(other) and os.path.basename(os.path.dirname(f)) != "rhs":
        os.remove(other)
