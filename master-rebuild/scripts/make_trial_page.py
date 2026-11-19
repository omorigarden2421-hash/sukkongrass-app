"""試作表（assemble.py の出力）から、価格・在庫を載せない確認用ページを作る。
使い方: python3 scripts/make_trial_page.py <試作.xlsx> pages/master-trial-1119.html
"""
import json, sys, re, openpyxl
src, out = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(src)  # 試作表は価格・在庫を含むのでリポジトリの外に置く
ws = wb.worksheets[0]
how = [c.value for c in ws[1]]; H = [c.value for c in ws[2]]
rows = [[c.value for c in r] for r in ws.iter_rows(min_row=3)]
FIELD2COL = {'synonyms': '旧学名・別名', 'flower_color_class': '花色（分類）', 'flower_color_detail': '花色（詳細）', 'spread_min': '株張り 最小(cm)',
 'spread_max': '株張り 最大(cm)', 'foliage_class': '葉色（分類）', 'foliage_features': '葉の特徴', 'seasonal_foliage': '紅葉・冬の葉', 'fragrance': '香り',
 'silhouette': '成株シルエット', 'sun': '日照', 'usda_min': 'USDA 下限', 'usda_max': 'USDA 上限', 'rhs_h': 'RHS 耐寒性', 'heat': '耐暑性',
 'heat_note': '暑さ・蒸れの注意', 'drought': '乾燥耐性', 'soil_moisture': '土壌水分', 'soil_ph_type': 'pH・土質', 'salt': '耐潮性', 'evergreen_warm': '常緑性',
 'common_name_ja': '和名', 'native_range': '原産地', 'spread_modes': '増え方', 'self_seed_level': 'こぼれ種の量(0-3)', 'rhizome_level': '地下茎で広がる程度(0-3)',
 'mixing': '混植適性', 'invasive_note': '広がりすぎの注意', 'toxicity': '毒性', 'pests': '主な病害虫', 'management_type': '管理タイプ', 'pruning': '切り戻しの方法',
 'pruning_codes': '切り戻し時期（広尾町）', 'division_interval': '株分けの間隔', 'propagation': '繁殖方法', 'cut_flower': '切り花適性', 'pollinator': '蜜源価値',
 'accepted_name': '学名（正名）'}
changes = {}
for no, name, field, old, new, reason in ([c.value for c in r] for r in wb['今回の変更点'].iter_rows(min_row=2)):
    changes.setdefault(str(no), []).append({'col': FIELD2COL.get(field, field), 'old': old, 'new': new, 'why': reason})
GROUPS = [['名前', ['学名（正名）', '旧学名・別名', '科名', '和名', '流通名・別名']],
 ['花と姿', ['花色（分類）', '花色（詳細）', '花期', '草丈(cm)', '株張り(cm)', '葉色（分類）', '葉の特徴', '紅葉・冬の葉', '香り', '成株シルエット', '常緑性']],
 ['環境', ['日照', '耐寒性', 'USDA', 'RHS 耐寒性', '耐暑性', '暑さ・蒸れの注意', '乾燥耐性', '土壌水分', 'pH・土質', '耐潮性', '原産地']],
 ['増え方と注意', ['増え方', 'こぼれ種の量(0-3)', '地下茎で広がる程度(0-3)', '混植適性', '広がりすぎの注意', '外来種リスト', '毒性', '主な病害虫']],
 ['管理', ['管理タイプ', '管理難易度', '切り戻しの方法', '切り戻し時期（広尾町）', '切り戻し時期（関東）', '株分けの間隔', '繁殖方法']],
 ['用途', ['景観構成用途', '切り花適性', '蜜源価値', '機能用途タグ', 'デザイン系タグ']]]
def rng(a, b, unit=''):
    if a is None and b is None: return None
    return f'{a}{unit}' if a == b or b is None else f'{a}〜{b}{unit}'
plants = []
for r in rows:
    d = dict(zip(H, r))
    d['花期'] = rng(d['花期 開始月'], d['花期 終了月'], '月')
    d['草丈(cm)'] = rng(d['草丈 最小(cm)'], d['草丈 最大(cm)']) and (rng(d['草丈 最小(cm)'], d['草丈 最大(cm)']) + (f"（{d['草丈 括弧内の値']}）" if d['草丈 括弧内の値'] else ''))
    d['株張り(cm)'] = rng(d['株張り 最小(cm)'], d['株張り 最大(cm)'])
    d['USDA'] = rng(d['USDA 下限'], d['USDA 上限'])
    plants.append({'no': str(d['商品番号']), 'name': d['植物名'], 'v': {k: d.get(k) for g in GROUPS for k in g[1]}, 'ch': changes.get(str(d['商品番号']), [])})
HOW = dict(zip(H, how)); HOW.update({'花期': '今のマスター', '草丈(cm)': '今のマスター', '株張り(cm)': '文献', 'USDA': '文献'})
data = json.dumps({'plants': plants, 'groups': GROUPS, 'how': HOW}, ensure_ascii=False).replace('</', '<\\/')
tpl = open(__file__.replace('make_trial_page.py', 'trial_page_template.html'), encoding='utf-8').read()
open(out, 'w', encoding='utf-8').write(tpl.replace('/*__DATA__*/null', data))
print(len(plants), sum(len(p['ch']) for p in plants))
