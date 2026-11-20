import subprocess, sys, re, urllib.parse, time, html
out = {}
for term in sys.argv[1:]:
    data = "mode=search&text=" + urllib.parse.quote(term)
    r = subprocess.run(["curl", "-sS", "-m", "40", "-A", "Mozilla/5.0", "-c", "ck.txt", "-b", "ck.txt", "-d", data, "https://www.ogis.co.jp/gallery/search.php"], capture_output=True)
    t = r.stdout.decode("utf-8", "replace")
    n = re.search(r"検索結果\s*(\d+)件", re.sub(r"<!--.*?-->", "", t, flags=re.S))
    pages = [t]
    total = int(n.group(1)) if n else 0
    p = 1
    while p * 20 < total and p < 15:
        time.sleep(1)
        r = subprocess.run(["curl", "-sS", "-m", "40", "-A", "Mozilla/5.0", "-c", "ck.txt", "-b", "ck.txt", f"https://www.ogis.co.jp/gallery/search.php?index=&catalog=&p={p}"], capture_output=True)
        pages.append(r.stdout.decode("utf-8", "replace")); p += 1
    tt = "".join(pages)
    print("##", term, total)
    seen = set()
    for m in re.finditer(r'page01\.php\?gallery=search&p=\d+&id=(\d+)".*?<figcaption[^>]*>(.*?)</figcaption>', tt, re.S):
        nm = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(2)))).strip()
        if nm and (m.group(1), nm) not in seen:
            seen.add((m.group(1), nm)); print(m.group(1), nm)
    time.sleep(1)
