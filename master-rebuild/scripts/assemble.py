import json, glob, re, sys, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
sys.path.insert(0, '/tmp/claude-0/scripts')
import ias

T = '/tmp/claude-0/-home-user-sukkongrass-app/40078efc-ec4a-5210-9a53-642e54c6f0c7/scratchpad/trial'
OUT = sys.argv[1]

wb0 = openpyxl.load_workbook('/tmp/claude-0/x/m.xlsx', read_only=True)
ws0 = wb0['Sheet1']; R = list(ws0.iter_rows(values_only=True)); H = R[0]
M = {r[1]: dict(zip(H, r)) for r in R[1:] if r[1]}
kewd = json.load(open(T + '/kew.json'))

FAM = {'Asteraceae': 'キク科', 'Ranunculaceae': 'キンポウゲ科', 'Lamiaceae': 'シソ科', 'Caryophyllaceae': 'ナデシコ科',
       'Rosaceae': 'バラ科', 'Poaceae': 'イネ科', 'Asparagaceae': 'キジカクシ科', 'Asphodelaceae': 'ススキノキ科',
       'Plumbaginaceae': 'イソマツ科', 'Crassulaceae': 'ベンケイソウ科', 'Saxifragaceae': 'ユキノシタ科',
       'Primulaceae': 'サクラソウ科', 'Fabaceae': 'マメ科', 'Caprifoliaceae': 'スイカズラ科', 'Liliaceae': 'ユリ科',
       'Geraniaceae': 'フウロソウ科', 'Polemoniaceae': 'ハナシノブ科', 'Hydrangeaceae': 'アジサイ科', 'Cornaceae': 'ミズキ科',
       'Valerianaceae': 'オミナエシ科（旧）'}
SRCNAME = {'s01': 'RHS', 's06': 'NC State', 's07': 'ミネソタ大', 's08': 'シカゴ植物園', 's09': 'Wildflower Center',
           's10': 'perennials.com／Walters', 's12': '育種会社', 'Kew': 'Kew（WCVP）', 's05': '環境省 外来種リスト'}

def fmt_name(s):
    if not s: return s
    s = s.replace('\n', ' ').replace('　', ' ')
    s = re.sub(r"[‘’‛`]", "'", s)
    s = re.sub(r'\s+', ' ', s).strip()
    s = re.sub(r"\s*（", "（", s)
    i = s.find("'")
    if i > 0 and s[i-1] != ' ': s = s[:i] + ' ' + s[i:]
    return s

SEASON = {'早春': (3, 3), '晩冬': (2, 2), '冬': (12, 2), '晩春': (5, 5), '春': (4, 5), '初夏': (6, 6), '盛夏': (7, 8),
          '晩夏': (8, 9), '夏': (7, 8), '晩秋': (11, 11), '秋': (9, 10)}
def bloom(s):
    if not s or s in ('ー', 'None'): return None, None
    s = str(s).replace('〜', '～')
    m = re.search(r'[（(](\d+)月?[^\d]*?(\d+)?月?', s)
    nums = re.findall(r'(\d+)\s*月?', s[s.find('（') if '（' in s else s.find('('):] if ('（' in s or '(' in s) else '')
    if nums:
        n = [int(x) for x in nums]; return n[0], n[-1]
    parts = s.split('～')
    def look(w, first):
        for k in sorted(SEASON, key=len, reverse=True):
            if w.startswith(k): return SEASON[k][0 if first else 1]
        return None
    return look(parts[0].strip(), True), look(parts[-1].strip(), False)

def height(s):
    if s is None: return None, None, None
    s = str(s).replace('（', '(').replace('）', ')').replace('〜', '～')
    paren = None
    m = re.search(r'\(([^)]*)\)', s)
    if m: paren = m.group(1); s = s[:m.start()]
    n = [int(x) for x in re.findall(r'\d+', s)]
    if not n: return None, None, paren
    return n[0], n[-1], paren

def months_after(end, add):
    if not end: return '花後'
    m = (end + add - 1) % 12 + 1
    return f'花後（{m}月頃）'
PR = {'早春': ('雪解け後（4月下旬〜5月上旬）', '2〜3月'), '秋': ('10月', '11〜12月'),
      '初夏': ('6月下旬〜7月上旬', '5月下旬〜6月上旬'), '不要': ('不要', '不要')}

def v(f, k):
    x = f.get(k) or {}
    return x.get('value')

COLS = ['商品番号', '植物名', '学名（正名）', '属', '種小名', '品種名', '旧学名・別名', '科名', '和名', '流通名・別名',
        '花色（分類）', '花色（詳細）', '花期 開始月', '花期 終了月', '草丈 最小(cm)', '草丈 最大(cm)', '草丈 括弧内の値',
        '株張り 最小(cm)', '株張り 最大(cm)', '葉色（分類）', '葉の特徴', '紅葉・冬の葉', '香り', '成株シルエット',
        '日照', '耐寒性', 'USDA 下限', 'USDA 上限', 'RHS 耐寒性', '耐暑性', '蒸れ耐性', '暑さ・蒸れの注意', '西日耐性',
        '乾燥耐性', '土壌水分', 'pH・土質', '耐潮性', '常緑性（寒冷地）', '常緑性（温暖地）', '原産地', '増え方',
        'こぼれ種の量(0-3)', '地下茎で広がる程度(0-3)', '混植適性', '広がりすぎの注意', '外来種リスト', '毒性', '主な病害虫',
        '管理タイプ', '管理難易度', '切り戻しの方法', '切り戻し時期（広尾町）', '切り戻し時期（関東）',
        '植え付け適期（広尾町）', '植え付け適期（関東）', '株分けの間隔', '繁殖方法',
        '景観構成用途', '切り花適性', '蜜源価値', '機能用途タグ', 'デザイン系タグ']
# column -> (field key in rows json or None, how)
LIT = {'旧学名・別名': 'synonyms', '花色（分類）': 'flower_color_class', '花色（詳細）': 'flower_color_detail',
       '株張り 最小(cm)': 'spread_min', '株張り 最大(cm)': 'spread_max', '葉色（分類）': 'foliage_class',
       '葉の特徴': 'foliage_features', '紅葉・冬の葉': 'seasonal_foliage', '香り': 'fragrance', '成株シルエット': 'silhouette',
       '日照': 'sun', 'USDA 下限': 'usda_min', 'USDA 上限': 'usda_max', 'RHS 耐寒性': 'rhs_h', '耐暑性': 'heat',
       '暑さ・蒸れの注意': 'heat_note', '乾燥耐性': 'drought', '土壌水分': 'soil_moisture', 'pH・土質': 'soil_ph_type',
       '耐潮性': 'salt', '常緑性（寒冷地）': 'evergreen_cold', '常緑性（温暖地）': 'evergreen_warm', '原産地': 'native_range',
       '増え方': 'spread_modes', 'こぼれ種の量(0-3)': 'self_seed_level', '地下茎で広がる程度(0-3)': 'rhizome_level',
       '混植適性': 'mixing', '広がりすぎの注意': 'invasive_note', '毒性': 'toxicity', '主な病害虫': 'pests',
       '管理タイプ': 'management_type', '切り戻しの方法': 'pruning', '株分けの間隔': 'division_interval',
       '繁殖方法': 'propagation', '切り花適性': 'cut_flower', '蜜源価値': 'pollinator', '学名（正名）': 'accepted_name'}
HOW = {}
for c in COLS: HOW[c] = '文献'
for c in ['商品番号', '植物名', '流通名・別名', '耐寒性', '花期 開始月', '花期 終了月', '草丈 最小(cm)', '草丈 最大(cm)', '草丈 括弧内の値']:
    HOW[c] = '今のマスター'
for c in ['属', '種小名', '品種名', '管理難易度', '切り戻し時期（広尾町）', '切り戻し時期（関東）', '植え付け適期（広尾町）',
          '植え付け適期（関東）', '景観構成用途', '機能用途タグ', 'デザイン系タグ']:
    HOW[c] = '自動'
HOW['科名'] = '文献（Kew）'; HOW['外来種リスト'] = '文献（環境省）'; HOW['和名'] = '文献（YList・未取得）'
HOW['蒸れ耐性'] = '保留（ルール待ち）'; HOW['西日耐性'] = '保留（ルール待ち）'

def j(x):
    if x is None: return None
    if isinstance(x, list): return '、'.join(str(i) for i in x) if x else None
    return x

master_rows, evid_rows, name_rows = [], [], []
inputs = {json.load(open(p))['id']: json.load(open(p)) for p in glob.glob(T + '/input/P*.json')}
for p in sorted(glob.glob(T + '/rows/P*.json')):
    d = json.load(open(p)); pid = d['id']; f = d['fields']; inp = inputs[pid]
    no = inp['商品番号']; no = int(no) if str(no).isdigit() else no; m = M.get(no) if isinstance(no, int) else None
    row = {c: None for c in COLS}
    row['商品番号'] = no
    row['植物名'] = fmt_name(m['植物名'] if m else inp['植物名'])
    row['流通名・別名'] = m['別名'] if m else None
    row['耐寒性'] = m['耐寒性'] if m else None
    b0, b1 = bloom(m['花時期']) if m else (None, None)
    row['花期 開始月'], row['花期 終了月'] = b0, b1
    h0, h1, hp = height(m['高さ(cm)']) if m else (None, None, None)
    row['草丈 最小(cm)'], row['草丈 最大(cm)'], row['草丈 括弧内の値'] = h0, h1, hp
    for c, k in LIT.items(): row[c] = j(v(f, k))
    acc = v(f, 'accepted_name') or inp['学名']
    mm = re.match(r"^\s*(×?\s*[A-Z][a-z]+)\s*(×?\s*[a-z][a-z\-]+)?(.*)$", acc)
    if mm:
        row['属'] = mm.group(1).strip(); row['種小名'] = (mm.group(2) or '').strip() or None
        cv = re.search(r"'([^']+)'", acc); row['品種名'] = cv.group(1) if cv else None
    k = kewd.get(pid) or {}
    if k.get('family'): row['科名'] = f"{FAM.get(k['family'], '')}（{k['family']}）"
    hits, gh = ias.check(inp['学名'])
    if hits: row['外来種リスト'] = '、'.join(f"{x['cat']}（{x['ja'].split('（')[0]}）" for x in hits)
    elif gh: row['外来種リスト'] = '掲載なし（同属の ' + '、'.join(f"{x['ja'].split('（')[0]}：{x['cat']}" for x in gh) + ' あり。要確認）'
    else: row['外来種リスト'] = '掲載なし'
    # auto
    mt = v(f, 'management_type') or ''
    heat = v(f, 'heat'); cold = row['耐寒性']
    if mt.startswith('E') or heat == '弱' or cold in ('中の弱', '弱', '一年草扱い'): diff = '難'
    elif mt.startswith('A') and heat in ('強', '中') and cold in ('強', '中の強'): diff = '易'
    else: diff = '中'
    row['管理難易度'] = diff
    codes = v(f, 'pruning_codes') or []
    hk, kt = [], []
    for c in codes:
        if c == '花後': hk.append(months_after(b1, 1)); kt.append(months_after(b1, 0))
        elif c in PR: hk.append(PR[c][0]); kt.append(PR[c][1])
    row['切り戻し時期（広尾町）'] = '、'.join(dict.fromkeys(hk)) or None
    row['切り戻し時期（関東）'] = '、'.join(dict.fromkeys(kt)) or None
    if cold in ('強', '中の強'): row['植え付け適期（広尾町）'] = '5月中旬〜6月、8月下旬〜9月上旬'
    elif cold: row['植え付け適期（広尾町）'] = '5月下旬〜6月（春植えのみ）'
    row['植え付け適期（関東）'] = '10〜11月（秋植え推奨）、3月' if heat == '弱' else '3〜4月、10〜11月'
    sil = v(f, 'silhouette'); modes = v(f, 'spread_modes') or []; smax = v(f, 'spread_max')
    use = []
    if h1:
        use.append('前景' if h1 <= 30 else '中景' if h1 <= 80 else '後景')
    gc = sil == 'マット' or (h1 and h1 <= 20 and any(x in modes for x in ('ランナー', '地下茎')))
    if gc: use.append('グラウンドカバー')
    if (sil in ('グラス', 'アーチ') and h1 and h1 >= 60) or (smax and smax >= 90): use.append('主役（単植向き）')
    if smax and smax <= 40 and not gc: use.append('群植向き')
    row['景観構成用途'] = '、'.join(use) or None
    tags = []
    sun = v(f, 'sun') or ''; dr = v(f, 'drought'); fc = v(f, 'foliage_class'); sm = v(f, 'soil_moisture')
    if '半日陰' in sun and not sun.startswith('日向〜') or sun == '日陰': tags.append('日陰庭向き')
    elif sun == '日向〜半日陰': tags.append('半日陰でも可')
    if dr == '強': tags.append('乾燥地向き')
    if v(f, 'pollinator'): tags.append('蜜源')
    if v(f, 'cut_flower'): tags.append('切り花')
    if fc and fc != 'グリーン系': tags.append('カラーリーフ')
    if v(f, 'salt') == '◎': tags.append('海辺向き')
    if sil in ('マット', 'ドーム') and dr == '強' and sm in ('排水必須', '乾燥寄り'): tags.append('ロックガーデン向き')
    row['機能用途タグ'] = '、'.join(tags) or None
    dz = []
    if fc == 'シルバー系': dz.append('シルバーリーフ')
    if fc == 'パープル・ブラック系': dz.append('黒葉アクセント')
    if fc == '斑入り': dz.append('斑入り葉')
    if k.get('family') in ('Poaceae', 'Cyperaceae') or sil == 'グラス': dz.append('グラス調')
    if cold == '強' and diff == '易': dz.append('北海道向き強健')
    row['デザイン系タグ'] = '、'.join(dz) or None
    master_rows.append(row)
    conf = {c['field']: c['detail'] for c in d.get('conflicts', []) if isinstance(c, dict)}
    for c, kk in LIT.items():
        x = f.get(kk) or {}
        if x.get('value') in (None, [], ''): continue
        srcs = x.get('sources') or []
        rel = '低（文献どうしが食い違い）' if kk in conf or c in conf else ('高（2つ以上の文献）' if len(set(srcs)) >= 2 else '中（1つの文献）')
        evid_rows.append([no, row['植物名'], c, j(x.get('value')), x.get('method'), '、'.join(SRCNAME.get(s, s) for s in srcs),
                          {'cultivar': '品種', 'species': '種', 'genus': '属'}.get(x.get('level'), x.get('level')), rel,
                          conf.get(kk) or conf.get(c), x.get('note')])
    nr = d.get('name_review')
    kacc = k.get('accepted') if k.get('status') == 'Synonym' or (k.get('matched') and k.get('accepted') and not k['accepted'].startswith(k['matched'])) else None
    if nr or kacc:
        nr = nr or {}
        if not nr.get('reason') and k.get('status') == 'Synonym':
            nr = {'proposed': None, 'reason': 'Kew では別の植物のシノニムとして照合された。同じ綴りで著者名の違う別の学名に当たった可能性が高い（RHS では正名）。要確認', 'source': 'Kew'}
        name_rows.append([no, row['植物名'], inp['学名'], nr.get('proposed'), nr.get('reason'), nr.get('source'),
                          k.get('accepted') if k else None, k.get('status') if k else None, None])

# ---------- write workbook ----------
wb = openpyxl.Workbook()
HF = Font(bold=True, color='FFFFFF'); HFILL = PatternFill('solid', fgColor='2F6B4A')
SUB = PatternFill('solid', fgColor='E1EFE6')
def sheet(title, header, rows, widths=None, first=False):
    ws = wb.active if first else wb.create_sheet()
    ws.title = title
    ws.append(header)
    for c in ws[1]: c.font = HF; c.fill = HFILL; c.alignment = Alignment(wrap_text=True, vertical='center')
    for r in rows: ws.append(r)
    ws.freeze_panes = 'C2' if title.startswith('マスター') else 'A2'
    for i, h in enumerate(header, 1):
        ws.column_dimensions[get_column_letter(i)].width = (widths or {}).get(h, max(10, min(28, len(str(h)) * 2 + 2)))
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = Alignment(wrap_text=True, vertical='top')
    return ws

ws = sheet('マスター（試作28品種）', COLS, [[r[c] for c in COLS] for r in master_rows],
           {'植物名': 34, '学名（正名）': 32, '旧学名・別名': 28, '暑さ・蒸れの注意': 40, '切り戻しの方法': 40, '原産地': 24,
            '広がりすぎの注意': 30, '主な病害虫': 24, '葉の特徴': 24, '外来種リスト': 26}, first=True)
ws.insert_rows(1)
for i, c in enumerate(COLS, 1):
    ws.cell(row=1, column=i, value=HOW[c]).fill = SUB
ws.freeze_panes = 'C3'
sheet('根拠', ['商品番号', '植物名', '項目', '値', '決め方', '文献', '情報のレベル', '信頼度', '文献どうしの食い違い', 'メモ'], evid_rows,
      {'植物名': 30, '値': 36, '文献どうしの食い違い': 44, 'メモ': 40, '文献': 24})
sheet('学名の検討', ['商品番号', '植物名', '今の学名', '文献の正名（提案）', '理由', '文献', 'Kew の正名', 'Kew での扱い', '御社の判断（記入）'], name_rows,
      {'植物名': 30, '今の学名': 30, '文献の正名（提案）': 32, '理由': 44, 'Kew の正名': 32, '御社の判断（記入）': 24})
# invasive (whole master)
inv = []
for no, r in M.items():
    if not r.get('学名'): continue
    h, g = ias.check(r['学名'])
    for x in h:
        inv.append([no, fmt_name(r['植物名']), r['学名'], x['ja'], x['sci'], x['cat'], '指定あり' if x['tokutei'] else 'なし', x['area'], r.get('在庫数'), None])
sheet('外来種リスト該当（全商品）', ['商品番号', '植物名', '学名', 'リストの和名', 'リストの学名', 'カテゴリ', '特定外来生物', '特に問題となる地域や環境', '在庫数', '販売の見直し（記入）'], inv,
      {'植物名': 30, 'リストの和名': 30, 'リストの学名': 26, '特に問題となる地域や環境': 36, '販売の見直し（記入）': 24})
sales = []
for r in master_rows:
    m = M.get(r['商品番号']) if isinstance(r['商品番号'], int) else None
    if m:
        w = m.get('卸単価（税抜）')
        sales.append([r['商品番号'], r['植物名'], m.get('通販サイトURL'), m.get('在庫数'), w, int(w / 0.6) if isinstance(w, (int, float)) else None])
    else:
        sales.append([r['商品番号'], r['植物名'], None, None, None, None])
sheet('販売', ['商品番号', '植物名', '通販サイトURL', '在庫数', '卸単価（税抜）', '小売単価（税抜・卸÷0.6 切り捨て）'], sales, {'植物名': 30, '通販サイトURL': 40})
own = []
for r in master_rows:
    m = M.get(r['商品番号']) if isinstance(r['商品番号'], int) else None
    own.append([r['商品番号'], r['植物名'], m.get('特徴') if m else None, m.get('コメント') if m else None, None])
sheet('自社の文章', ['商品番号', '植物名', '特徴（専務作成）', 'コメント', '文献との食い違い（全件作成時に記入）'], own, {'植物名': 30, '特徴（専務作成）': 70, 'コメント': 30, '文献との食い違い（全件作成時に記入）': 40})
srcs = [['s01', 'RHS（英国王立園芸協会）Plant Finder', '公的機関DB', 'rhs.org.uk', '使用'],
        ['s02', 'Missouri Botanical Garden Plant Finder', '植物園DB', 'missouribotanicalgarden.org', 'この環境では読めず（パソコン側で対応予定）'],
        ['s03', 'Kew World Checklist of Vascular Plants（WCVP）', '植物園DB', 'sftp.kew.org（一括データ）', '使用（学名・科名・原産地）'],
        ['s04', 'YList', '公的機関DB', 'ylist.info', 'この環境では読めず（パソコン側で対応予定）'],
        ['s05', '環境省 生態系被害防止外来種リスト（植物）', '公的機関', 'env.go.jp', '使用'],
        ['s06', 'NC State Extension Plant Toolbox', '大学', 'plants.ces.ncsu.edu', '使用'],
        ['s07', 'University of Minnesota Extension', '大学', 'extension.umn.edu', '使用'],
        ['s08', 'Chicago Botanic Garden（Plant Finder・品種評価）', '植物園DB', 'chicagobotanic.org', '使用'],
        ['s09', 'Lady Bird Johnson Wildflower Center', '大学', 'wildflower.org', '使用'],
        ['s10', 'perennials.com（Valleybrook／Perennial Resource）・Walters Gardens', '生産・品種情報会社', 'perennials.com／waltersgardens.com', '使用'],
        ['s11', 'Jelitto カタログ', '種苗会社', 'jelitto.com', 'この環境では読めず（パソコン側で対応予定）'],
        ['s12', '育種会社の品種情報（Proven Winners など）', '育種会社', '各社', '使用'],
        ['s13', 'Beth Chatto', '育種・生産会社', 'bethchatto.co.uk', 'この環境では読めず']]
sheet('文献リスト', ['文献ID', '文献', '種類', 'サイト', '状態'], srcs, {'文献': 50, 'サイト': 30, '状態': 40})
rules = [[c, HOW[c]] for c in COLS]
sheet('列の決め方', ['列', '決め方'], rules, {'列': 30, '決め方': 30})
wb.save(OUT)
print('rows', len(master_rows), 'evid', len(evid_rows), 'names', len(name_rows), 'inv', len(inv))
