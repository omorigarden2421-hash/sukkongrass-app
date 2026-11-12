# 使い方: python3 -I rhsget.py 保存先フォルダ URL...   RHSの品種ページを保存し、要点の原文を表示する
import sys, re, html, subprocess, time, os
out = sys.argv[1]
def seg(t, a, b, n=600):
    i = t.find(a)
    if i < 0: return ''
    j = t.find(b, i + len(a)) if b else -1
    return t[i + len(a): j if j > 0 else i + len(a) + n].strip(' |')[:n]
for u in sys.argv[2:]:
    f = os.path.join(out, re.sub(r'[^A-Za-z0-9]+', '_', u.split('/plants/')[-1])[:80] + '.html')
    if not os.path.exists(f):
        subprocess.run(['curl', '-sS', '-L', '-m', '40', '-o', f, u]); time.sleep(1)
    t = open(f, encoding='utf-8', errors='replace').read()
    t = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', t, flags=re.S)
    t = html.unescape(re.sub(r'<[^>]+>', '|', t))
    t = re.sub(r'[\s|]*\|[\s|]*', ' | ', t); t = re.sub(r'\s+', ' ', t)
    print('=====', u)
    print('名前:', seg(t, 'RHS Home | Plants |', '| Save to My Plants', 200))
    print('別名:', seg(t, '| Synonyms |', '| Herbaceous', 300) if '| Synonyms |' in t else '')
    m = re.search(r'\| (?:\d+ Suppliers?|Herbaceous Perennial|RHS Recommended|Buy online[^|]*|Alpine/Rockery|Ferns?|Grass Like|Bogs|Climber Wall Shrub|Shrubs|Conservatory Greenhouse|Bulbs|Annual Biennial|Bedding)(?: \| [^|]{0,40})*? \| ([^|]{60,}(?:\| [^|]+ )*?)\| Position \|', t)
    print('説明:', m.group(1).strip() if m else seg(t, 'Suppliers |', '| Position |', 900))
    print('日照:', seg(t, '| Position |', '| Soil Types', 80), '/ 高さ:', seg(t, '| Max Height |', '|', 40), '/ 広がり:', seg(t, '| Max Spread |', '|', 40))
    print('葉:', seg(t, 'Native to GB/Ireland |', '| Habit', 60), '/ 名前の扱い:', seg(t, '| Name Status |', '|', 30))
    print('群:', seg(t, '= Hybrid Tea |', '| How to Grow', 300) if '= Hybrid Tea |' in t else '')
