# 出典台帳（ledger.csv）から新しい品種マスターを作る。
# 使い方: python3 -I build_master.py 元マスター.xlsx ledger.csv 出力.xlsx
# - 対象列は台帳にある値だけを入れ、台帳に無いものは空欄（＝未確認）にする。
# - 対象外の列（耐寒性ほか）は元マスターのまま。
# - 「食い違い」シートに、元の値と台帳の値が違う箇所を出す。
import sys, pandas as pd

TARGET = ['学名', '高さ(cm)', '広がり(cm)', '花時期', '花色', '日照条件', '耐暑性', '常緑性']

src, ledger_path, out = sys.argv[1:4]
m = pd.read_excel(src, dtype=str)
lg = pd.read_csv(ledger_path, dtype=str).fillna('')
lg = lg[lg['項目'].isin(TARGET) & lg['区分'].isin(['C', 'B']) & (lg['値'] != '')]
bad = lg[(lg['区分'] == 'C') & (lg['URL'] == '')]
if len(bad):
    sys.exit(f'URLの無いC行があります: {len(bad)}件。台帳を直してください。')

# 出典として認めるサイト（出典ルール v1.2 の一次情報）。これ以外のURLのC行は受け付けない。
import os, re
from urllib.parse import urlparse
ALLOWED = [
    'missouribotanicalgarden.org',   # Missouri Botanical Garden
    'rhs.org.uk',                     # 英国王立園芸協会
    'plants.ces.ncsu.edu',            # NC州立大学 Extension Plant Toolbox
    'wildflower.org',                 # Lady Bird Johnson Wildflower Center
    'plants.usda.gov',                # USDA PLANTS
    'ylist.info',                     # YList
    'naro.go.jp', 'affrc.go.jp',      # 国内の公的研究機関
    'hinshu2.maff.go.jp',             # 農水省 品種登録
    'uspto.gov', 'patents.google.com' # 米国植物特許（育成元の公式記載）
]
# 米国の州立大学 Extension（.edu）。.edu なら何でもよいわけではないので、extension を含むものに限る
EDU_EXT = re.compile(r'(^|\.)(extension|ext)\.[a-z0-9.-]+\.edu$|extension\.[a-z0-9-]+\.edu$')
# 育成元の公式サイトや、上に無い大学Extensionは、大森さんが承認したものだけをこのファイルに1行1ドメインで追加する
APPROVED = os.path.join(os.path.dirname(os.path.abspath(__file__)), '追加承認_出典ドメイン.txt')
breeders = []
if os.path.exists(APPROVED):
    breeders = [l.strip() for l in open(APPROVED, encoding='utf-8') if l.strip() and not l.startswith('#')]

def ok(url):
    host = urlparse(url).hostname or ''
    if any(host == d or host.endswith('.' + d) for d in ALLOWED + breeders):
        return True
    return bool(EDU_EXT.search(host))

ng = lg[(lg['区分'] == 'C') & ~lg['URL'].apply(ok)]
if len(ng):
    print(ng[['商品番号', '項目', 'URL']].to_string())
    sys.exit(f'認められていない出典のC行があります: {len(ng)}件。一次情報に差し替えるか、行を消してください。')

done = set(lg['商品番号'])
new = m.copy()
diffs, status = [], []
for i, r in m.iterrows():
    pid = r['商品番号']
    for col in TARGET:
        hit = lg[(lg['商品番号'] == pid) & (lg['項目'] == col)]
        if len(hit):
            v = '／'.join(dict.fromkeys(hit['値']))
            new.at[i, col] = v
            if str(r[col]) != v:
                diffs.append({'商品番号': pid, '植物名': r['植物名'], '項目': col,
                              '元の値': r[col], '台帳の値': v,
                              '区分': '／'.join(hit['区分']), '出典': ' | '.join(hit['URL'])})
            st = 'C' if (hit['区分'] == 'C').any() else 'B'
        else:
            new.at[i, col] = ''
            st = '未確認'
        status.append({'商品番号': pid, '植物名': r['植物名'], '項目': col, '状況': st,
                       '照合済みの品種': '済' if pid in done else '未着手'})

st = pd.DataFrame(status)
with pd.ExcelWriter(out) as w:
    new.to_excel(w, sheet_name='マスター', index=False)
    pd.DataFrame(diffs).to_excel(w, sheet_name='食い違い', index=False)
    st[st['照合済みの品種'] == '済'].to_excel(w, sheet_name='照合状況', index=False)
    lg.to_excel(w, sheet_name='出典台帳', index=False)
print(f'照合済み品種 {len(done)} / {len(m)}、食い違い {len(diffs)} 件')
print(st[st['照合済みの品種'] == '済']['状況'].value_counts().to_string())
