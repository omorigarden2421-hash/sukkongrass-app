# マスターの学名を、RHSのサイトマップ（品種ページの一覧）と突き合わせて、ページの候補を出す。
# 使い方: python3 -I rhs_match.py マスター.xlsx rhs_urls.txt 出力.csv [rhs_overrides.csv]
# rhs_overrides.csv（商品番号, ページ番号, メモ）があれば、その品種は手で決めたページを使う（番号が空なら候補なし）。
import sys, re, csv, difflib, collections, unicodedata, pandas as pd
m = pd.read_excel(sys.argv[1], dtype=str).fillna('')
idx = collections.defaultdict(list); byid = {}
for u in open(sys.argv[2], encoding='utf-8'):
    u = u.strip(); mm = re.search(r'/plants/(\d+)/([^/]+)/details', u)
    if mm:
        byid[mm.group(1)] = u
        sl = mm.group(2); sl = sl[2:] if sl.startswith('x-') else sl
        idx[sl.split('-')[0]].append((sl, u))
def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    s = re.sub(r"(?<=[a-z])'(?=s\b)", '', s)
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')
CODES = {'d', 'v', 'pbr', 'f', 'm', 'series', 'group', 'x'}
out = []
for _, r in m.iterrows():
    sci = unicodedata.normalize('NFKC', r['学名']).replace('\n', ' ').strip()
    sci = re.sub(r'[‘’‛`´]', "'", sci)
    q = re.findall(r"'(.+?)'(?=\s|$|\))", sci + ' ')
    if not q and sci.count("'") >= 2: q = [sci[sci.index("'") + 1: sci.rindex("'")]]
    cv = slug(q[0]) if q else ''
    head = sci.split("'")[0] if q else sci
    head = re.sub(r'\([^)]*\)', ' ', head)                       # （命名者）や（別名）を外す
    head = re.sub(r'\s[A-Z][A-Za-z.]*\.?(\s[A-Z][A-Za-z.]*)*\s*$', '', ' ' + head.strip()).strip() if (not q and len(head.split()) > 2) else head
    head = re.sub(r'\b(sp|ssp|subsp|var|f)\.', lambda k: {'ssp': 'subsp'}.get(k.group(1), k.group(1)) + ' ', head)
    toks = slug(head).split('-'); genus = toks[0] if toks and toks[0] != 'x' else (toks[1] if len(toks) > 1 else '')
    sp = [t for t in toks[1:] if t not in ('x', genus)]
    cands = idx.get(genus, [])
    best = []
    for sl, u in cands:
        tail = sl[len(genus) + 1:] if sl.startswith(genus + '-') else ''
        tt = tail.split('-') if tail else []
        if cv:
            pad = '-' + tail + '-'
            if '-' + cv + '-' in pad:
                extra = [t for t in pad.replace('-' + cv + '-', '-', 1).strip('-').split('-') if t and t not in CODES]
                spm = sum(1 for t in sp if t in extra); other = len([t for t in extra if t not in sp])
                kind = '一致' if other == 0 else '一致＋余分'
                best.append((0 if other == 0 else 1, -spm, other, len(sl), kind, u))
            else:
                ratio = difflib.SequenceMatcher(None, cv, tail).ratio() if tail else 0
                tailcv = '-'.join(tt[-len(cv.split('-')):]) if tt else ''
                ratio = max(ratio, difflib.SequenceMatcher(None, cv, tailcv).ratio())
                if ratio >= 0.8: best.append((2, -ratio, 0, len(sl), 'あいまい%.2f' % ratio, u))
        else:
            want = '-'.join(sp)
            if tail == want: best.append((0, 0, 0, len(sl), '種で一致', u))
            elif want and tail.startswith(want + '-') and all(t in CODES for t in tail[len(want) + 1:].split('-')): best.append((1, 0, 0, len(sl), '種で一致＋記号', u))
            elif want and [x for x in tail.split('-') if x != 'x'] == [x for x in sp if x not in ('subsp', 'var', 'f')]: best.append((1, 0, 0, len(sl), '種で一致（×や階級の表記違い）', u))
    best.sort()
    row = [r['商品番号'], r['植物名'].replace('\n', ' '), sci]
    for b in best[:3]: row += [b[4], b[5]]
    out.append(row + [''] * (9 - len(row)))
if len(sys.argv) > 4:
    ov = {r[0]: r for r in list(csv.reader(open(sys.argv[4], encoding='utf-8')))[1:]}
    for row in out:
        if row[0] in ov:
            ids = ov[row[0]][1].split(); row[3:] = [''] * 6
            for k, i in enumerate(ids[:3]): row[3 + 2 * k] = '手で指定'; row[4 + 2 * k] = byid[i]
csv.writer(open(sys.argv[3], 'w', newline='', encoding='utf-8-sig')).writerows([['商品番号', '植物名', '学名', '判定1', 'URL1', '判定2', 'URL2', '判定3', 'URL3']] + out)
c = collections.Counter((r[3] or 'なし').rstrip('0123456789.') for r in out); print(dict(c))
