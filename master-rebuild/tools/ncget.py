# 使い方: python3 -I ncget.py 保存先フォルダ URL...   NC州立大学 Plant Toolbox のページを保存し、要点の原文を表示する
import sys, re, html, subprocess, time, os
out = sys.argv[1]
KEYS = ['Height:', 'Width:', 'Light:', 'Flower Color:', 'Flower Bloom Time:', 'Flower Description:', 'Woody Plant Leaf Characteristics:', 'Leaf Description:', 'USDA Plant Hardiness Zone:', 'Resistance To Challenges:', 'Problems:']
for u in sys.argv[2:]:
    f = os.path.join(out, 'nc_' + re.sub(r'[^A-Za-z0-9]+', '_', u.split('/plants/')[-1])[:80] + '.html')
    if not os.path.exists(f):
        subprocess.run(['curl', '-sS', '-L', '-m', '40', '-o', f, u]); time.sleep(1)
    t = open(f, encoding='utf-8', errors='replace').read()
    t = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', t, flags=re.S)
    t = html.unescape(re.sub(r'<[^>]+>', '|', t))
    t = re.sub(r'[\s|]*\|[\s|]*', ' | ', t); t = re.sub(r'\s+', ' ', t)
    print('=====', u)
    m = re.search(r'<title>(.*?)</title>', open(f, encoding='utf-8', errors='replace').read(), re.S)
    print('名前:', re.sub(r'\s+', ' ', m.group(1)).strip() if m else '')
    i = t.find('| Description |'); j = t.find('| Cultivars / Varieties', i)
    d = t[i + 15: j if j > 0 else i + 2500]
    print('説明:', d[:2200])
    for k in KEYS:
        i = t.find('| ' + k + ' |')
        if i >= 0:
            j = t.find(': |', i + len(k) + 4); seg = t[i + 2: j if 0 < j < i + 500 else i + 300]
            seg = seg.rsplit(' | ', 1)[0] if 0 < j < i + 500 else seg
            print(' ', seg)
