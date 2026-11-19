"""おぎはら植物園「おぎはら植物図鑑」（s20。長野県の宿根草ナーサリー）の耐暑性などを trial/evidence/ に追記する。

使い方: python3 -I scripts/sources/add_ogihara.py <trial フォルダ>
2026-11-19 にユーザーのパソコンで読んだ（https://www.ogis.co.jp/ の検索で品種を探し、図鑑のページの DATA と MEMO を読んだ）。
みんなの趣味の園芸（shuminoengei.jp）は 403 と証明書エラーで読めなかったので、その代わり。
何度実行しても同じ結果になる（s20 の記録を入れ直す）。
"""
import json
import sys

TRIAL = sys.argv[1]
CHECKED = "2026-11-19"
URL = "https://www.ogis.co.jp/gallery/page01.php?id="
# 試作ID: (図鑑のID, 図鑑の表記, level, 耐暑性, 日照, MEMO から拾った文 [(field, 原文)])
PAGES = {
 "P01": (229, "朝霧草 Artemisia schmidtiana", "species", "中", "日向～やや半日陰", [("pruning", "伸びたら短く切り戻すと草姿良く作れる")]),
 "P02": (442, "オダマキ ‘イエロークイーン’ Aquilegia chrysantha 'Yerrow Queen'", "cultivar", "中", "やや半日陰", []),
 "P03": (758, "アジュガ ‘バーガンディグロー’ Ajuga reptans 'Burgundy Glow'", "cultivar", "強", "日向～やや半日陰",
         [("seasonal_foliage", "夏はシルバー、秋はピンクに変化し、冬も常緑で美しく周年楽しめる")]),
 "P08": (2890, "カラマグロスティス ‘カール フォースター’ Calamagrostis x acutiflora 'Karl Foerster'", "cultivar", "強", "日向", []),
 "P09": (1576, "ススキ ‘モーニングライト’ Miscanthus sinensis 'Morning Light'", "cultivar", "強", "日向", []),
 "P10": (1552, "ギボウシ(ホスタ) ‘ゴールドスタンダード’ Hosta ‘Goldstandard’", "cultivar", "強", "半日陰",
         [("sun", "日射はやや強めの方が発色良い")]),
 "P13": (681, "サルビア ネモローサ ‘カラドンナ’ Salvia nemorosa ‘Caradonna’", "cultivar", "強", "日向", []),
 "P15": (1092, "セダム(コーカサスキリンソウ) ‘ドラゴンズブラッド’ Sedum spurium 'Dragon's Blood'", "cultivar", "強", "日向",
         [("heat_humidity", "セダムの中でも特に性質が強健"), ("drought", "周年美しい色を保つので乾燥地のカバーに向く")]),
 "P19": (2776, "オミナエシ Patrinia scabiosifolia", "species", "強", "日向", []),
 "P21": (1043, "黒花フウロ (ファエウム) Geranium phaeum var. phaeum", "species", "強", "日向～やや半日陰",
         [("heat_humidity", "性質が強健で耐暑性があり、大株に育て易い"), ("evergreen", "冬季常緑種")]),
 "P23": (244, "アネモネ シルベストリス Anemone sylvestris", "species", "中", "日向～やや半日陰", []),
 "P24": (1984, "黄金シモツケ ‘ゴールドフレーム’ Spiraea x bumalda 'Goldflame'", "cultivar", "強", "日向", []),
}
NOT_FOUND = "図鑑を検索したが掲載なし（品種名・属名・和名で検索）"


def main():
    for n in range(1, 29):
        pid = f"P{n:02d}"
        path = f"{TRIAL}/evidence/{pid}.json"
        d = json.load(open(path, encoding="utf-8"))
        d["evidence"] = [e for e in d["evidence"] if e["source"] != "s20"]
        d["access_log"] = [a for a in d["access_log"] if a["source"] != "s20"]
        if pid in PAGES:
            gid, name, level, heat, sun, memo = PAGES[pid]
            url = URL + str(gid)
            kind = "品種のページ" if level == "cultivar" else "種のページ"
            d["access_log"].append({"source": "s20", "url": url, "status": "ok", "checked": CHECKED, "note": f"{kind}：{name}"})
            recs = [("heat_humidity", f"耐暑性 {heat}（日本のナーサリーの評価。値のみ）", f"耐暑性；{heat}"),
                    ("sun", sun.replace("～", "〜"), f"日照；{sun}")] + [(f, q, q) for f, q in memo]
            for field, ja, quote in recs:
                d["evidence"].append({"field": field, "value_ja": ja, "quote": quote, "source": "s20", "url": url, "level": level,
                                      "from_master_source": False, "checked": CHECKED})
        else:
            d["access_log"].append({"source": "s20", "url": "https://www.ogis.co.jp/gallery/search.php", "status": "not_found",
                                    "checked": CHECKED, "note": NOT_FOUND})
        json.dump(d, open(path, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    print("掲載あり", len(PAGES))


main()
