# 台帳・確認リスト・MBG未確認リストに行を足すための共通の関数（属ごとの追記スクリプトから使う）
import csv, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RHS = 'RHS（英国王立園芸協会）'; NC = 'NC州立大学 Extension Plant Toolbox'
def _append(name, header, rows):
    p = os.path.join(D, name); new = not os.path.exists(p)
    with open(p, 'a', newline='', encoding='utf-8-sig' if new else 'utf-8') as f:
        w = csv.writer(f)
        if new: w.writerow(header)
        w.writerows(rows)
def ledger(pid, name, sci, src, url, date, items):
    # items: (項目, 値, 原文抜粋, 換算前の値, メモ)
    _append('ledger.csv', [], [[pid, name, sci, k, v, 'C', src, url, q, raw, date, memo] for k, v, q, raw, memo in items])
def ask(pid, name, kind, item, body, urls, req):
    _append('大森さんへの確認リスト.csv', [], [[pid, name, kind, item, body, urls, req, '']])
def mbg(pid, name, sci, url, memo=''):
    _append('MBG_未確認リスト.csv', ['商品番号', '植物名', '学名', 'MBGのURL', 'メモ'], [[pid, name, sci, url, memo]])
