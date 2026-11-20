import json,sys
d=json.load(open(sys.argv[1],encoding='utf-8'))
ids=sys.argv[2:]
for r in d:
    if ids:
        if r['ID'] in ids:
            print(r['ID'],(r.get('暑さ・蒸れ・西日の根拠') or '')[:700]); print('  注意:',(r.get('文献の注意') or '')[:200]); print()
        continue
    n=(r.get('文献での表記') or '').replace('おぎはら: ','O:').replace('stauden.de: ','S:').replace('Walters: ','W:').replace('Gaißmayer: ','G:')
    print(r['ID'],'|',r['学名（マスター）'][:46],'|',n[:170])
    print('   暑',r.get('耐暑性'),'/欧米',r.get('耐暑性（欧米の文献だけなら）'),'/',(r.get('耐暑性の決め方') or '')[:9],'|蒸',r.get('蒸れ耐性'),'|西',r.get('西日耐性'),'|',r.get('日照'),'|',r.get('USDA'))
