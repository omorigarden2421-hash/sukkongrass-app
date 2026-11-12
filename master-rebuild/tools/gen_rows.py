# digest（RHS・NC州立大学の原文の要点）と、人が読んで決めた judg.tsv から、台帳の行を作る。
# 使い方: python3 -I gen_rows.py digest_rhs.jsonl digest_nc.jsonl judg.tsv 出力フォルダ 確認日 [済みの商品番号…を書いたファイル]
# judg.tsv（タブ区切り）: 商品番号 / 判定(OK・NG・SP) / 高さの原文 / 花時期の原文 / 花色の原文 / 花色の日本語 / メモ
#   OK＝RHSのページはこの品種で合っている。NG＝別の植物なので使わない。SP＝種や群のページなので品種には使わない。
#   高さ・花時期・花色の原文は、RHSの説明文にあるままの語句（無ければ空）。説明文に含まれない語句はエラーで止まる。
import sys, re, json, csv, os
rhs_p, nc_p, judg_p, outdir, date = sys.argv[1:6]
skip = set(open(sys.argv[6]).read().split()) if len(sys.argv) > 6 else set()
RHS = 'RHS（英国王立園芸協会）'; NC = 'NC州立大学 Extension Plant Toolbox'
D = {}
for l in open(rhs_p, encoding='utf-8'): r = json.loads(l); D[r['pid']] = r
for l in open(nc_p, encoding='utf-8'): r = json.loads(l); D.setdefault(r['pid'], r)['nc'] = r.get('nc')
SEASON = [(r'early[- ]spring', '春', '春'), (r'mid[- ]?spring', '春', '春'), (r'late[- ]spring', '春', '春'), (r'spring', '春', '春'),
          (r'early[- ]summer', '初夏', '初夏'), (r'mid[- ]?summer', '盛夏', '盛夏'), (r'late[- ]summer', '晩夏', '晩夏'), (r'summer', '初夏', '晩夏'),
          (r'early[- ]autumn|early[- ]fall', '秋', '秋'), (r'mid[- ]?autumn', '秋', '秋'), (r'late[- ]autumn', '秋', '秋'), (r'autumn|fall', '秋', '秋'),
          (r'late[- ]winter', '冬', '冬'), (r'mid[- ]?winter', '冬', '冬'), (r'early[- ]winter', '冬', '冬'), (r'winter', '冬', '冬'),
          (r'january|february|december', '冬', '冬'), (r'march|april|may', '春', '春'), (r'june', '初夏', '初夏'), (r'july', '盛夏', '盛夏'),
          (r'august', '晩夏', '晩夏'), (r'september|october|november', '秋', '秋')]
def season(raw):
    s = raw.lower(); hits = []
    s = re.sub(r'(early|mid|late)[- ]*(?:to|and|or|-)[- ]*(early|mid|late)[- ]*(spring|summer|autumn|winter)', r'\1 \3 to \2 \3', s)   # mid to late summer → mid summer to late summer
    pos = 0
    while pos < len(s):
        for pat, a, b in SEASON:
            m = re.match(pat + r'\b', s[pos:])
            if m: hits.append((a, b)); pos += m.end(); break
        else: pos += 1
    if not hits: raise SystemExit('花時期を読み取れない: ' + raw)
    a, b = hits[0][0], hits[-1][1]
    return a if a == b else a + '～' + b
def band(v):
    v = v.strip()
    m = re.fullmatch(r'([\d.]+)-([\d.]+) metres', v)
    if m: return '%d～%d' % (round(float(m.group(1)) * 100), round(float(m.group(2)) * 100))
    m = re.fullmatch(r'Up to (\d+) ?cm', v)
    if m: return m.group(1)
    m = re.fullmatch(r'Higher than (\d+) metres', v)
    if m: return None
    return None
def height(raw):
    s = raw.lower().replace(' ', '')
    m = re.fullmatch(r'([\d.]+)(?:-|to)([\d.]+)(cm|m)', s)
    if m: k = 100 if m.group(3) == 'm' else 1; return '%d～%d' % (round(float(m.group(1)) * k), round(float(m.group(2)) * k))
    m = re.fullmatch(r'([\d.]+)(cm|m)', s)
    if m: return '%d' % round(float(m.group(1)) * (100 if m.group(2) == 'm' else 1))
    raise SystemExit('高さを読み取れない: ' + raw)
def window(desc, raw, n=13):
    i = desc.lower().find(raw.lower())
    if i < 0: return None
    words = desc.split(' '); c = len(desc[:i].split(' ')) - 1; k = len(raw.split(' '))
    a = max(0, c - (n - k) // 2); b = min(len(words), a + n); a = max(0, b - n)
    return ' '.join(words[a:b]).strip(' ,.;')
def light_rhs(p):
    s = {x.strip() for x in p.split(',') if x.strip()}
    o = [x for x in ['Full sun', 'Partial shade', 'Full shade'] if x in s]
    if not o or s - set(o): return None
    J = {'Full sun': '日向', 'Partial shade': '半日陰', 'Full shade': '日陰'}
    return J[o[0]] if len(o) == 1 else J[o[0]] + '～' + J[o[-1]]
FOL = {'Deciduous': '冬季落葉', 'Semi evergreen': '半常緑', 'Evergreen': '常緑'}
def sci_from(name):
    n = name
    n2 = re.sub(r"\[\s*[^\]]*\]\s*\('([^']+)'\)", r"'\1'", n)      # [商品名] ('品種名') → '品種名'
    codes = re.findall(r"\s\(([^()']*)\)", n2); n3 = re.sub(r"\s\([^()']*\)", '', n2)
    n3 = re.sub(r'\s*PBR\b', '', n3).replace(' × ', ' × ').strip()
    memo = []
    if n2 != n: memo.append('RHSでは [ ] 内は商品名で、品種名は引用符の中。')
    if codes: memo.append('RHSの記号・群の名前（%s）は値に入れていない。' % '、'.join(codes))
    return re.sub(r'\s+', ' ', n3), ' '.join(memo)
def ft(v):
    m = re.findall(r'(\d+) ft\. (\d+) in\.', v)
    if len(m) != 2: return None
    a, b = [int(f) * 30 + round(int(i) * 2.5) for f, i in m]
    return ('%d' % a) if a == b else '%d～%d' % (a, b)
NCCOL = {'Blue': '青', 'Purple/Lavender': '紫', 'Pink': 'ピンク', 'Red/Burgundy': '赤', 'White': '白', 'Gold/Yellow': '黄色', 'Orange': 'オレンジ', 'Green': '緑', 'Cream/Tan': 'クリーム色', 'Brown/Copper': '茶', 'Black': '黒', 'Gray/Silver': '灰色', 'Insignificant': '目立たない', 'Variegated': '複色'}
def light_nc(v):
    o = []
    if 'Full sun' in v: o.append('日向')
    if 'Partial Shade' in v or 'Dappled Sunlight' in v: o.append('半日陰')
    if 'Deep shade' in v: o.append('日陰')
    return None if not o else (o[0] if len(o) == 1 else o[0] + '～' + o[-1])
rows, asks, syn, stat = [], [], [], []
J = {}
for l in open(judg_p, encoding='utf-8'):
    if not l.strip() or l.startswith('#'): continue
    f = l.rstrip('\n').split('\t'); f += [''] * (7 - len(f)); J[f[0]] = f
for pid, f in J.items():
    if pid in skip: continue
    r = D[pid]; name = r['name']; got = {}
    def add(k, v, src, url, q, raw, memo):
        if k in got: return
        got[k] = v; rows.append([pid, name, sci, k, v, 'C', src, url, q, raw, date, memo])
    pg = next((p for p in r.get('rhs', []) if p.get('desc')), None) or (r.get('rhs') or [None])[0]
    sci = r['master']['学名']
    if f[1] == 'OK' and pg:
        u = pg['url']; desc = pg.get('desc', ''); st = pg.get('status', '')
        bot = pg['name']; sci, memo = sci_from(bot)
        if st == 'Synonym':
            syn.append([pid, name, r['master']['学名'], bot, pg.get('common', ''), u]); memo += ' RHSでは別名（Synonym）の扱い。'
        elif st not in ('Accepted', 'Correct'): memo += ' RHSの Name Status は %s。' % st
        if f[6]: memo += ' ' + f[6]
        add('学名', sci, RHS, u, (bot + ' / Name Status: ' + st)[:140], '', memo.strip())
        if f[2]:
            w = window(desc, f[2])
            if not w: raise SystemExit(f'{pid}: 高さの語句が説明文に無い: {f[2]}')
            add('高さ(cm)', height(f[2]), RHS, u, w, f[2], '区分表示は %s。' % pg.get('height', ''))
        elif band(pg.get('height', '')): add('高さ(cm)', band(pg['height']), RHS, u, 'Max Height ' + pg['height'], pg['height'], 'RHSの大きさは区分表示。')
        if band(pg.get('spread', '')): add('広がり(cm)', band(pg['spread']), RHS, u, 'Max Spread ' + pg['spread'], pg['spread'], 'RHSの大きさは区分表示。')
        if f[3] == '-':
            add('花時期', 'ー', RHS, u, window(desc, f[4]) or desc[:80], '', '花を観賞しない植物（シダなど）。'); add('花色', '花なし', RHS, u, window(desc, f[4]) or desc[:80], '', '花を観賞しない植物（シダなど）。')
        else:
            if f[3]:
                w = window(desc, f[3])
                if not w: raise SystemExit(f'{pid}: 花時期の語句が説明文に無い: {f[3]}')
                add('花時期', season(f[3]), RHS, u, w, f[3], '')
            if f[4]:
                w = window(desc, f[4])
                if not w or not f[5]: raise SystemExit(f'{pid}: 花色の語句が説明文に無い／日本語が無い: {f[4]}')
                add('花色', f[5], RHS, u, w, '', '')
        if light_rhs(pg.get('position', '')): add('日照条件', light_rhs(pg['position']), RHS, u, 'Position: ' + pg['position'], '', '')
        if pg.get('foliage') in FOL: add('常緑性', FOL[pg['foliage']], RHS, u, 'Foliage: ' + pg['foliage'], '', '')
    n = r.get('nc')
    is_cv = "'" in re.sub(r'[‘’‛]', "'", r['master']['学名'])
    if n and (n.get('cultivar_page') or not is_cv) and f[1] != 'NG':
        u = n['url']; note = 'RHSに記載が無いため NC州立大学 の値。'
        if '学名' not in got:
            sci = n['name'].split(' (')[0]; add('学名', sci, NC, u, n['name'][:120], '', 'RHSに使えるページが無いため NC州立大学 の名前。')
        if n.get('Height') and ft(n['Height']): add('高さ(cm)', ft(n['Height']), NC, u, 'Height: ' + n['Height'], n['Height'], note)
        if n.get('Width') and ft(n['Width']): add('広がり(cm)', ft(n['Width']), NC, u, 'Width: ' + n['Width'], n['Width'], note)
        if n.get('Flower Bloom Time') and f[3] != '-':
            order = [x for x in ['Winter', 'Spring', 'Summer', 'Fall'] if x in n['Flower Bloom Time']]
            if order and not ('Winter' in order and 'Fall' in order): add('花時期', season(order[0] + ' to ' + order[-1]) if len(order) > 1 else season(order[0]), NC, u, 'Flower Bloom Time: ' + n['Flower Bloom Time'], n['Flower Bloom Time'], note)
        if n.get('Flower Color') and f[3] != '-':
            cs = [NCCOL[x.strip()] for x in n['Flower Color'].split('|') if x.strip() in NCCOL]
            if cs: add('花色', '・'.join(cs), NC, u, 'Flower Color: ' + n['Flower Color'], '', note + 'NC州立大学の花色は大まかな分類。')
        if n.get('Light') and light_nc(n['Light']): add('日照条件', light_nc(n['Light']), NC, u, ('Light: ' + n['Light'])[:150], '', note)
        lf = n.get('Woody Plant Leaf Characteristics', '')
        for k, v in (('Semi-evergreen', '半常緑'), ('Deciduous', '冬季落葉'), ('Evergreen', '常緑')):
            if k in lf: add('常緑性', v, NC, u, 'Woody Plant Leaf Characteristics: ' + lf, '', note); break
        if 'Heat' in [x.strip() for x in n.get('Resistance To Challenges', '').split('|')]:
            add('耐暑性', '強', NC, u, 'Resistance To Challenges: ' + n['Resistance To Challenges'][:110], '', 'NC州立大学が「暑さに耐える」項目に挙げている。')
    if not got: asks.append([pid, name, '一次情報に記載なし' if f[1] != 'NG' else 'RHSに該当ページなし', '全項目', (f[6] or 'RHS・NC州立大学に、この品種のページが見つからない。') , (pg or {}).get('url', ''), '', ''])
    stat.append([pid, f[1], len(got)])
os.makedirs(outdir, exist_ok=True)
for fn, data in (('rows.csv', rows), ('asks.csv', asks), ('syn.csv', syn)):
    csv.writer(open(os.path.join(outdir, fn), 'w', newline='', encoding='utf-8')).writerows(data)
print('品種', len(stat), '行', len(rows), '記載なし', len(asks), '別名扱い', len(syn))
