# マスターの機械的な矛盾チェック。使い方: python3 -I check_master.py マスター.xlsx 出力.csv
import sys, re, pandas as pd

m = pd.read_excel(sys.argv[1], dtype=str).fillna('')
out = []
def add(r, kind, detail):
    out.append({'商品番号': r['商品番号'], '植物名': r['植物名'].replace('\n', ' '), '種類': kind, '内容': detail})

dup = m[m['学名'] != ''].groupby('学名')['商品番号'].apply(list)
dup = dup[dup.str.len() > 1]
for i, r in m.iterrows():
    sci = r['学名']
    if sci in dup.index:
        add(r, '学名の重複（品種名が抜けている可能性）', f'{sci} → 商品番号 {dup[sci]}')
    if re.search(r'[Ａ-Ｚａ-ｚ　]', sci):
        add(r, '学名に全角文字', sci)
    name = r['植物名']
    if re.search(r"[‘'’]", name) and sci and not re.search(r"'|‘|’|var\.|f\.|subsp\.", sci):
        add(r, '商品名は品種なのに学名に品種名が無い', f'{name.replace(chr(10)," ")} / {sci}')
    for col in ['高さ(cm)', '広がり(cm)']:
        v = r[col]
        if v and not re.fullmatch(r'\d+(～\d+)?', v):
            add(r, f'{col}の書式', v)
    if r['花時期'] in ('', 'ー'):
        add(r, '花時期が空', r['花時期'])
pd.DataFrame(out).to_csv(sys.argv[2], index=False, encoding='utf-8-sig')
print(pd.DataFrame(out)['種類'].value_counts().to_string())
