# おぎはら植物園（楽天市場店）の商品ページから、項目欄（学名・花期・草丈・株張り・耐寒性・耐暑性・日照・原産地・分類）を原文のまま取り出す。
# 使い方: python3 -I ogihara_get.py 価格比較.xlsx マスター.xlsx 保存先フォルダ 出力.csv
import sys, re, html, os, subprocess, time, csv, pandas as pd
x, master, out, dst = sys.argv[1:5]
os.makedirs(out, exist_ok=True)
d = pd.read_excel(x, sheet_name='一致した全品種', dtype=str).fillna('')
m = pd.read_excel(master, dtype=str).fillna('')
pid = {u.split('pid=')[-1]: (r, n.replace('\n', ' '), s) for u, r, n, s in zip(m['通販サイトURL'], m['商品番号'], m['植物名'], m['学名'])}
KEYS = [('学名', r'学\s*名'), ('花期', r'花\s*期'), ('草丈', r'草\s*丈'), ('株張り', r'株張り'), ('耐寒性', r'耐寒性'), ('耐暑性', r'耐暑性'), ('日照', r'日\s*照'), ('原産地', r'原産地')]
rows = []
for _, r in d.iterrows():
    key = r['大森 商品ページ'].split('pid=')[-1]
    if key not in pid: continue
    u = r['おぎはら 商品ページ']; f = os.path.join(out, re.sub(r'[^A-Za-z0-9]+', '_', u.split('/ogis/')[-1]) + '.html')
    if not os.path.exists(f):
        subprocess.run(['curl', '-sS', '-L', '-m', '40', '-o', f, u], capture_output=True); time.sleep(2)
    t = open(f, 'rb').read().decode('euc-jp', 'replace') if os.path.exists(f) else ''
    t = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', t, flags=re.S)
    t = html.unescape(re.sub(r'<[^>]+>', '|', t)); t = re.sub(r'[\s|]*\|[\s|]*', ' | ', t)
    rec = {'商品番号': pid[key][0], '植物名': pid[key][1], 'マスターの学名': pid[key][2], 'おぎはらの商品名': r['おぎはら 商品名'], '照合のしかた': r['照合のしかた'], 'URL': u}
    seg = t[t.find('商品番号：'):]
    mm = re.search(r'■ \| ([^|■]*(?:宿根草|多年草|低木|球根|一年草|二年草|シダ|グラス|つる)[^|■]*) \| ■', seg[:1500]); rec['分類'] = mm.group(1).strip() if mm else ''
    for k, pat in KEYS:
        mm = re.search(r'■ \| ' + pat + r'\s*[:：]\s*([^|]*?) \|', seg[:2500]); rec[k] = mm.group(1).strip() if mm else ''
    rows.append(rec)
pd.DataFrame(rows).to_csv(dst, index=False, encoding='utf-8-sig')
print(len(rows), {k: sum(1 for r in rows if r[k]) for k, _ in KEYS}, sum(1 for r in rows if r['分類']))
