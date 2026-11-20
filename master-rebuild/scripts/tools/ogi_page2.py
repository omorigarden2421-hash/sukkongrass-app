"""おぎはら植物図鑑のページを取得して、1行にまとめて出す。使い方: ogi_page2.py <保存先> <ID> ..."""
import html
import os
import re
import subprocess
import sys
import time

out = sys.argv[1]
for i in sys.argv[2:]:
    f = f"{out}/p{i}.html"
    if not os.path.exists(f) or os.path.getsize(f) < 3000:
        subprocess.run(["curl", "-sS", "-m", "40", "-A", "Mozilla/5.0", f"https://www.ogis.co.jp/gallery/page01.php?id={i}", "-o", f])
        time.sleep(1)
    t = open(f, encoding="utf-8", errors="replace").read()
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    x = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))
    a = x.find("おぎはら植物図鑑", x.find("HOME"))
    m = x.find("Memo", a)
    d = x.find("Data", m)
    e = x.find("Memo", d)
    head = re.sub(r"カタログ品番；\S+ -->", "", x[a + 9:m]).strip()
    half = len(head) // 2
    name = head[half:].strip() if head[:half].strip() and head[:half].strip()[:8] == head[half:].strip()[:8] else head
    data = x[d + 4:e if e > 0 else d + 200]
    heat = re.search(r"耐暑性；(\S+)", data)
    sun = re.search(r"日照；(\S+)", data)
    ev = re.search(r"(常緑\S*|落葉\S*|半常緑\S*)", data)
    print(i, "|", name[:90], "|暑", heat.group(1) if heat else None, "|", sun.group(1) if sun else None, "|", ev.group(1) if ev else "", "|", x[m + 4:d].strip()[:int(os.environ.get("MEMO", "150"))])
