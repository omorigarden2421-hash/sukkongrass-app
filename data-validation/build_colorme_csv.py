# -*- coding: utf-8 -*-
"""カラーミー商品CSVに、今セッションで更新した列(景観61/機能62/管理難易度51/おすすめ65,66/一言キャッチ64)を
   案A=ピンポイント置換で反映。商品説明HTMLの該当箇所のみ差し替え、簡易説明を一言キャッチで補完。
   出力: 再アップロード用CSV(cp932, 全行)。"""
import csv, re, openpyxl, sys

APPLY='--apply' in sys.argv
SRC='/root/.claude/uploads/67bbf729-0108-5a33-b967-d4b309b67090/aac882ef-product_22.csv'
OUT='data-validation/カラーミー_商品CSV_反映版.csv'

# master(適用済み最新)
wb=openpyxl.load_workbook('data-validation/納品_最終版/宿根草マスタ_検証済み_最終版.xlsx', read_only=True)
ws=wb.active; data=list(ws.iter_rows(min_row=2,values_only=True))
def col(i): return [r[i-1] for r in data]
pid2i={}; num2i={}
for i,u in enumerate(col(1)):
    m=re.search(r'pid=(\d+)', str(u or ''))
    if m: pid2i[m.group(1)]=i
for i,n in enumerate(col(2)):
    num2i[str(n).strip()]=i
M={'land':col(61),'func':col(62),'star':col(51),'env':col(65),'gard':col(66),'catch':col(64)}
STAR2TXT={'★':'易（初心者にも育てやすい）','★★':'中（一般的）','★★★':'難（上級者向け）','★★★★':'難（上級者向け）'}

def li_list(text):
    items=[x.strip() for x in str(text or '').split('\n') if x.strip()]
    return '\n'+''.join(f'<li>{x}</li>\n' for x in items)

def transform(html, i):
    land=str(M['land'][i] or '').strip()
    func=str(M['func'][i] or '').strip() or '—'
    diff=STAR2TXT.get(str(M['star'][i] or '').strip(),'')
    # 1) 景観構成用途
    html=re.sub(r'(景観構成用途：</b>).*?(</li>)', lambda m:m.group(1)+land+m.group(2), html, count=1)
    # 2) 機能用途
    html=re.sub(r'(機能用途：</b>).*?(</li>)', lambda m:m.group(1)+func+m.group(2), html, count=1)
    # 3) 管理難易度
    if diff:
        html=re.sub(r'(管理難易度：</b>).*?(</li>)', lambda m:m.group(1)+diff+m.group(2), html, count=1)
    # 4) 育てる環境 <ul>
    html=re.sub(r'(<p><b>育てる環境</b></p>\s*<ul>).*?(</ul>)',
                lambda m:m.group(1)+li_list(M['env'][i])+m.group(2), html, count=1, flags=re.S)
    # 5) 庭づくり <ul>
    html=re.sub(r'(<p><b>庭づくり</b></p>\s*<ul>).*?(</ul>)',
                lambda m:m.group(1)+li_list(M['gard'][i])+m.group(2), html, count=1, flags=re.S)
    return html

with open(SRC, encoding='cp932') as f:
    cm=list(csv.reader(f))
hdr=cm[0]; rows=cm[1:]
ix={h:j for j,h in enumerate(hdr)}
C_ID=ix['商品ID']; C_KATA=ix['型番']; C_DESC=ix['商品説明']; C_SHORT=ix['簡易説明']

matched=0; changed_html=0; changed_short=0; enc_err=[]
preview=[]
for r in rows:
    i=pid2i.get(r[C_ID].strip())
    if i is None: i=num2i.get(r[C_KATA].strip())
    if i is None: continue
    matched+=1
    old=r[C_DESC]; new=transform(old, i)
    if new!=old:
        changed_html+=1
        if len(preview)<3:
            preview.append((r[ix['商品名']], old, new, i))
    r[C_DESC]=new
    catch=str(M['catch'][i] or '').strip()
    if catch and r[C_SHORT].strip()!=catch:
        r[C_SHORT]=catch; changed_short+=1

print(f'突合 {matched} / 商品説明変更 {changed_html} / 簡易説明補完 {changed_short}')

# プレビュー: 変更断片のみ抽出表示
def frag(h):
    out=[]
    for pat in [r'景観構成用途：</b>.*?</li>', r'機能用途：</b>.*?</li>', r'管理難易度：</b>.*?</li>']:
        m=re.search(pat,h)
        if m: out.append(m.group(0))
    m=re.search(r'<p><b>育てる環境</b></p>\s*<ul>.*?</ul>', h, re.S)
    if m: out.append(m.group(0).replace('\n',''))
    return out
if not APPLY:
    for nm,o,n,i in preview:
        print('\n===',nm,'===')
        of=frag(o); nf=frag(n)
        for a,b in zip(of,nf):
            if a!=b:
                print('  旧:',a[:90]); print('  新:',b[:90])
else:
    # cp932エンコード検査
    for r in rows:
        for cell in r:
            try: cell.encode('cp932')
            except: enc_err.append(cell[:20]); break
    with open(OUT,'w',encoding='cp932',newline='') as f:
        w=csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(hdr); w.writerows(rows)
    print('出力:',OUT)
    if enc_err: print('WARN cp932非対応セル:',len(enc_err),enc_err[:5])
    else: print('cp932エンコード OK（全セル）')
