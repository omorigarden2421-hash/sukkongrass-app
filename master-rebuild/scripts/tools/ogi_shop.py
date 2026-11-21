"""おぎはら植物園の楽天のお店（item.rakuten.co.jp/ogis/）の商品ページを、図鑑のページの「カタログ品番」から開いて読む。

使い方（master-rebuild で）: python -X utf8 scripts/tools/ogi_shop.py <保存先フォルダ（リポジトリの外）> <出力.json>
- 対象: 各 batch と scripts/pilot の ogihara_data.py に書いてある図鑑のID（品種のページも、種のページも）
- 図鑑のページ https://www.ogis.co.jp/gallery/page01.php?id=<ID> の中の「カタログ品番；31L」→ https://item.rakuten.co.jp/ogis/31l/
  （売り切れの品種もページが残っていることがある。ないものは 404）
- 2.5秒おき。取得済みは飛ばす。ページ全体は保存先だけに置き、リポジトリには入れない。出力は短い項目だけ
- 商品ページの共通の説明（2026-11-21 に確認）:
  耐暑性「強・強い」は暑さに強い植物です「中・普通」は暖地では涼しいところで夏越しを行うなど工夫が必要「弱」は暖地では夏越し困難で寒冷地向きです。
"""
import glob
import html
import importlib.util
import json
import os
import re
import subprocess
import sys
import time

OUT, RES = sys.argv[1], sys.argv[2]
os.makedirs(OUT + "/gallery", exist_ok=True)
os.makedirs(OUT + "/shop", exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
ids = {}  # 図鑑のID → [(データのフォルダ, 試行ID, level, 図鑑の表記)]
for p in sorted(glob.glob("batch_*/ogihara_data.py")) + ["scripts/pilot/ogihara_data.py"]:
    sp = importlib.util.spec_from_file_location("o", p)
    mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(mod)
    folder = os.path.dirname(p).replace("\\", "/")
    for rec in mod.OGIHARA:
        for k in rec[0]:
            ids.setdefault(int(rec[1]), []).append((folder, k, rec[3], rec[2]))


def text(t):
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))


def g(p, s):
    m = re.search(p, s)
    return m.group(1).strip() if m else None


res = {}
for n, gid in enumerate(sorted(ids)):
    gf = f"{OUT}/gallery/p{gid}.html"
    if not os.path.exists(gf) or os.path.getsize(gf) < 3000:
        subprocess.run(["curl", "-sS", "-m", "40", "-A", "Mozilla/5.0", f"https://www.ogis.co.jp/gallery/page01.php?id={gid}", "-o", gf])
        time.sleep(1.0)
    gt = open(gf, encoding="utf-8", errors="replace").read()
    no = g(r"カタログ品番；\s*([0-9A-Za-z-]+)", gt)
    link = g(r'(https://item\.rakuten\.co\.jp/ogis/[^"/]+/)', gt)
    rec = {"used_by": ids[gid], "catalog_no": no, "on_sale_link": bool(link)}
    res[str(gid)] = rec
    url = link or (f"https://item.rakuten.co.jp/ogis/{no.lower()}/" if no else None)
    if not url:
        rec["status"] = "品番なし"
        continue
    rec["url"] = url
    sf = f"{OUT}/shop/{gid}.html"
    if not os.path.exists(sf):
        r = subprocess.run(["curl", "-sSL", "-m", "40", "-A", UA, "-w", "\n%{http_code}", url], capture_output=True)
        time.sleep(2.5)
        body, _, code = r.stdout.rpartition(b"\n")
        if code.strip() not in (b"200", b"404"):
            rec["status"] = "取得できず " + code.decode("ascii", "replace")
            print(gid, rec["status"], flush=True)
            if code.strip() in (b"403", b"429", b"503"):
                print("止めます（アクセス制限の可能性）", flush=True)
                break
            continue
        open(sf, "wb").write(code.strip() + b"\n" + body)
    raw = open(sf, "rb").read()
    code, _, body = raw.partition(b"\n")
    if code != b"200":
        rec["status"] = "ページなし（404）"
        continue
    x = text(body.decode("euc-jp", "replace"))
    a = x.find("■ 学 名")
    if a < 0:
        rec["status"] = "形の違うページ"
        continue
    b = x.find("基本的な管理", a)
    k = x[b:b + 700] if b > 0 else ""
    rec.update({
        "status": "ok",
        "name": g(r"学 名 : (.{0,80}?) ■", x[a:]),
        "heat": g(r"耐暑性 : (.{0,60}?) ■", x[a:]),
        "cold": g(r"耐寒性 : (.{0,60}?) ■", x[a:]),
        "spread": g(r"株張り : (.{0,60}?) ■", x[a:]),
        "sun": g(r"日 照 : (.{0,40}?) ■", x[a:]),
        "sun_cool": g(r"寒冷地 (.+?) 暖 地", k),
        "sun_warm": g(r"暖 地 (.+?) 土 壌", k),
        "moisture": g(r"乾燥地 ※(.+?) 耐乾性", k),
        "dry": g(r"耐乾性 (.+?) 耐湿性", k),
        "wet": g(r"耐湿性 (.+?) 剪 定", k),
        "pruning": g(r"剪 定 (.+?) 肥 料", k),
        "propagation": g(r"増 殖 (.+?) 消 毒", k),
        "pests": g(r"消 毒 (.+?) お届けする苗について", k),
    })
    if n % 25 == 0:
        print(n, "/", len(ids), gid, rec["status"], flush=True)
        json.dump({"checked": time.strftime("%Y-%m-%d"), "pages": res}, open(RES, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
json.dump({"checked": time.strftime("%Y-%m-%d"), "pages": res}, open(RES, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
import collections
print("図鑑のID", len(ids), collections.Counter(r.get("status") for r in res.values()))
print("done")
