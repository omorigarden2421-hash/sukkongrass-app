# -*- coding: utf-8 -*-
"""タグ列(38/61/62/63) 再導出プレビュー（xlsxは書き換えない）"""
import openpyxl, re, sys
from collections import Counter

SRC = '納品_最終版/宿根草マスタ_検証済み_最終版.xlsx'
wb = openpyxl.load_workbook(SRC, read_only=True)
ws = wb.active
rows = list(ws.iter_rows(min_row=2, values_only=True))
def C(r, i): return r[i-1]

def maxh(v):
    if v is None: return None
    n = [int(x) for x in re.findall(r'\d+', str(v))]
    return max(n) if n else None

def toks(v):
    s = '' if v is None else str(v).strip()
    out = []
    for t in re.split(r'[、,／/・\n]+', s):
        t = t.strip()
        if t: out.append(t)
    return out

KEEP62 = ['ナチュラルガーデン向き', '強健（放置向き）', 'ドライフラワー', 'リーフ観賞']
ORD62  = ['蜜源', '切り花', '日陰庭向き', 'ロックガーデン向き', '乾燥地向き', 'カラーリーフ'] + KEEP62
KEEP63 = ['北海道向き強健', 'モダン庭向き']
ORD63  = ['シルバーリーフ', '斑入り葉', '黒葉アクセント', 'グラス調'] + KEEP63

def derive(r):
    h    = maxh(C(r,12))
    sun  = str(C(r,14) or '').strip()
    dry  = str(C(r,24) or '').strip()
    wet  = str(C(r,23) or '').strip()
    hab  = str(C(r,35) or '').strip()
    cut  = str(C(r,37) or '').strip()
    leaf = str(C(r,40) or '').strip()
    mel  = str(C(r,55) or '').strip()
    sil  = str(C(r,57) or '').strip()
    cur38, cur61, cur62, cur63 = C(r,38), C(r,61), C(r,62), C(r,63)

    # 61 景観 (3区分)
    if h is None:
        n61 = str(cur61 or '').strip()
    elif h <= 30: n61 = '前景'
    elif h <= 80: n61 = '中景'
    else:         n61 = '後景'

    # 38 用途区分
    base = {'前景':'前景・縁取り','中景':'中景構成','後景':'後景・背景'}.get(n61)
    gc = hab in ('マット型','ランナー型')
    if base is None:
        n38 = str(cur38 or '').strip()
    else:
        n38 = base + ('、グラウンドカバー' if gc else '')

    # 62 機能用途タグ
    s = set()
    if mel in ('◎','○'): s.add('蜜源')
    if cut in ('◎','○'): s.add('切り花')
    if '日陰' in sun:     s.add('日陰庭向き')          # 日向単独のみ除外
    if dry == '強' or wet in ('排水必須','乾燥寄り'):
        s.add('ロックガーデン向き'); s.add('乾燥地向き')
    if leaf[:1] in ('②','③','④','⑤','⑥','⑦'): s.add('カラーリーフ')
    for t in KEEP62:
        if t in toks(cur62): s.add(t)
    n62 = '、'.join(t for t in ORD62 if t in s)

    # 63 デザイン系タグ
    d = set()
    if leaf.startswith('④'): d.add('シルバーリーフ')
    if leaf.startswith('⑦'): d.add('斑入り葉')
    if leaf.startswith('⑤'): d.add('黒葉アクセント')
    if sil == 'グラス':       d.add('グラス調')
    for t in KEEP63:
        if t in toks(cur63): d.add(t)
    n63 = '、'.join(t for t in ORD63 if t in d)

    return n38, n61, n62, n63

def norm(v): return str(v or '').strip()

diffcnt = {38:0,61:0,62:0,63:0}
tok_add = {62:Counter(),63:Counter()}
tok_del = {62:Counter(),63:Counter()}
samples = {38:[],61:[],62:[],63:[]}
new_vals = []

for r in rows:
    name = str(C(r,3) or '').replace('\n',' ')
    n38,n61,n62,n63 = derive(r)
    new_vals.append((n38,n61,n62,n63))
    for col,new in [(38,n38),(61,n61),(62,n62),(63,n63)]:
        old = norm(C(r,col))
        if new != old:
            diffcnt[col]+=1
            if len(samples[col])<12:
                samples[col].append((name[:30], old[:40], new[:40]))
    for col,new in [(62,n62),(63,n63)]:
        old_t=set(toks(C(r,col))); new_t=set(toks(new))
        for t in new_t-old_t: tok_add[col][t]+=1
        for t in old_t-new_t: tok_del[col][t]+=1

print('=== 変更件数（現行→再導出）全916品種 ===')
for col in (38,61,62,63):
    nm={38:'用途区分',61:'景観構成用途タグ',62:'機能用途タグ',63:'デザイン系タグ'}[col]
    print(f'  col{col} {nm}: {diffcnt[col]} 件変更')

for col in (62,63):
    nm={62:'機能用途タグ',63:'デザイン系タグ'}[col]
    print(f'\n=== col{col} {nm} トークン別 増減 ===')
    print('  [追加]', tok_add[col].most_common())
    print('  [削除]', tok_del[col].most_common())

for col in (61,38,62,63):
    nm={38:'用途区分',61:'景観',62:'機能',63:'デザイン'}[col]
    print(f'\n--- col{col} {nm} 変更サンプル (品種 | 旧 | 新) ---')
    for a,b,c in samples[col]:
        print(f'   {a:30s} | {b:40s} | {c}')
