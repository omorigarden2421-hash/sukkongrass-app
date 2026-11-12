# 候補のRHSページと、NC州立大学のページを保存して、品種ごとの要点（原文）を digest.jsonl にまとめる。
# 使い方: python3 -I fetch_all.py マスター.xlsx match.csv 保存先フォルダ digest.jsonl [rhs|nc]
import sys, re, csv, json, html, os, subprocess, time, unicodedata, pandas as pd
src, match, out, dig, mode = sys.argv[1:6]
os.makedirs(out, exist_ok=True)
def get(u, f, pause=1.0):
    if not os.path.exists(f):
        subprocess.run(['curl', '-sS', '-L', '-m', '40', '-o', f, '-w', '%{http_code}', u], capture_output=True); time.sleep(pause)
    return open(f, encoding='utf-8', errors='replace').read() if os.path.exists(f) else ''
def text(t):
    t = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', t, flags=re.S)
    t = html.unescape(re.sub(r'<[^>]+>', '|', t))
    return re.sub(r'\s+', ' ', re.sub(r'[\s|]*\|[\s|]*', ' | ', t))
def seg(t, a, b, n=300):
    i = t.find(a)
    if i < 0: return ''
    j = t.find(b, i + len(a))
    return t[i + len(a): j if j > 0 else i + len(a) + n].strip(' |')[:n]
def rhs(u):
    f = os.path.join(out, re.sub(r'[^A-Za-z0-9]+', '_', u.split('/plants/')[-1])[:80] + '.html')
    t = text(get(u, f))
    nm = seg(t, 'RHS Home | Plants |', '| Save to My Plants', 240).split(' | RHS | Plant Profile | ')
    fix = lambda s: re.sub(r'\s+', ' ', s.replace(' | ', ' ').replace('[ ', '[').replace(' ]', ']')).strip()
    d = {'url': u, 'name': fix(nm[0]), 'common': fix(nm[1]) if len(nm) > 1 else '',
         'status': seg(t, '| Name Status |', '|', 30), 'desc': '', 'position': '', 'height': '', 'spread': '', 'foliage': ''}
    i = t.find('| Position |')
    if i > 0:
        last = t[:i].rstrip(' |').split(' | ')[-1]
        if len(last) >= 40: d['desc'] = last
        d['position'] = seg(t, '| Position |', '| Soil Types', 80); d['height'] = seg(t, '| Max Height |', '|', 40); d['spread'] = seg(t, '| Max Spread |', '|', 40)
    b = t[t.find('| Botanical Details |'):] if '| Botanical Details |' in t else ''
    if '| Foliage |' in b: d['foliage'] = seg(b, '| Foliage |', '|', 30)
    if '| Synonyms |' in t: d['syn'] = seg(t, '| Synonyms |', '| Buy', 200).split(' | Herbaceous')[0].split(' | RHS Recommended')[0].replace(' | ', ' ')
    if '= Hybrid Tea |' in t: d['group'] = seg(t, '= Hybrid Tea |', '| How to Grow', 260)
    return d
def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s.replace("'", '')).strip('-')
def nc(sci):
    s = re.sub(r'[‘’‛`´]', "'", unicodedata.normalize('NFKC', sci)); q = re.findall(r"'(.+?)'", s)
    head = slug(s.split("'")[0]); cands = []
    if q:
        cands = [head + '-' + slug(q[0]), head.split('-')[0] + '-' + slug(q[0])]
    elif re.search(r'\b(var|subsp|ssp|f)\.|\bsp\.', s): cands = []          # 変種・亜種・品種（f.）は、種のページを当てない
    else: cands = ['-'.join(head.split('-')[:2])]
    for c in dict.fromkeys(cands):
        f = os.path.join(out, 'nc_' + c[:80] + '.html'); raw = get('https://plants.ces.ncsu.edu/plants/' + c + '/', f)
        if '404 Not Found' in raw[:3000] or len(raw) < 5000: continue
        t = text(raw); d = {'url': 'https://plants.ces.ncsu.edu/plants/' + c + '/', 'cultivar_page': bool(q)}
        mm = re.search(r'<title>(.*?)\|', raw, re.S); d['name'] = html.unescape(re.sub(r'\s+', ' ', mm.group(1)).strip()) if mm else ''
        i = t.find('| Description |'); j = t.find('| Cultivars / Varieties', i); d['desc'] = t[i + 15: j if 0 < j < i + 2600 else i + 2600].strip(' |')
        for k in ('Height', 'Width'):
            mm = re.search(k + r': (\d+ ft\. \d+ in\. - \d+ ft\. \d+ in\.)', t)
            if mm: d[k] = mm.group(1)
        for k in ['Light:', 'Flower Color:', 'Flower Bloom Time:', 'Flower Description:', 'Woody Plant Leaf Characteristics:', 'Resistance To Challenges:']:
            i = t.find('| ' + k + ' |')
            if i >= 0:
                v = t[i + len(k) + 4: i + 420]; j = v.find(': |'); v = v[:j].rsplit(' | ', 1)[0] if 0 < j else v[:200]
                d[k.rstrip(':')] = v.split(' | Download')[0].strip(' |')
        return d
    return None
m = pd.read_excel(src, dtype=str).fillna(''); mt = {r[0]: r for r in csv.reader(open(match, encoding='utf-8-sig'))}
done = set()
if os.path.exists(dig): done = {json.loads(l)['pid'] for l in open(dig, encoding='utf-8')}
COLS = ['学名', '高さ(cm)', '広がり(cm)', '花時期', '花色', '日照条件', '耐暑性', '常緑性']
with open(dig, 'a', encoding='utf-8') as w:
    for _, r in m.iterrows():
        pid = r['商品番号']
        if pid in done: continue
        rec = {'pid': pid, 'name': r['植物名'].replace('\n', ' '), 'master': {c: r[c] for c in COLS}}
        if mode == 'rhs':
            c = mt.get(pid, [''] * 9); pages = []
            for k in (3, 5, 7):
                if not c[k + 1]: break
                d = rhs(c[k + 1]); d['match'] = c[k]; pages.append(d)
                if d['desc'] and d['status'] in ('Accepted', 'Correct', 'Trade'): break
            rec['rhs'] = pages
        else:
            rec['nc'] = nc(r['学名'])
        w.write(json.dumps(rec, ensure_ascii=False) + '\n'); w.flush()
