"""Kew WCVP（一括データ）から原産地を引いて kew_native.json を作る。

使い方（master-rebuild で）:
  python -X utf8 scripts/tools/kew_native.py <統合表.xlsx> <wcvp を展開したフォルダ>

- 学名（正名）から品種名を外し、種（亜種・変種があればそれ）で WCVP を引く。
- 異名なら正名の分布を使う。
- 分布は wcvp_distribution.csv の「自生」（introduced=0、extinct=0、location_doubtful=0）だけ。
- 地域名は TDWG の地域区分（level 2）を日本語にする。東アジア（日本・朝鮮半島・台湾など）だけは国・島の単位まで書く。
- 交配種で分布がないときは、Kew の交配式（hybrid_formula）があれば「交配種（交配親：…）」とする。
- 推測では埋めない。引けないものは空のまま理由を残す。
"""
import csv, json, re, sys, os
import openpyxl

csv.field_size_limit(10**9)
XLSX, WD = sys.argv[1], sys.argv[2]
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "kew_native.json")

L2 = {
    "10": "北ヨーロッパ", "11": "中央ヨーロッパ", "12": "南西ヨーロッパ", "13": "南東ヨーロッパ", "14": "東ヨーロッパ",
    "20": "北アフリカ", "21": "マカロネシア（カナリア諸島など）", "22": "西アフリカ熱帯域", "23": "中西アフリカ熱帯域",
    "24": "北東アフリカ熱帯域", "25": "東アフリカ熱帯域", "26": "南アフリカ熱帯域", "27": "南部アフリカ",
    "28": "大西洋中部の島々", "29": "西インド洋の島々（マダガスカルなど）",
    "30": "シベリア", "31": "ロシア極東", "32": "中央アジア", "33": "コーカサス", "34": "西アジア", "35": "アラビア半島",
    "36": "中国", "37": "モンゴル", "38": "東アジア", "40": "インド亜大陸", "41": "インドシナ", "42": "マレーシア地域",
    "43": "パプア地域", "50": "オーストラリア", "51": "ニュージーランド", "60": "南西太平洋", "61": "中南部太平洋",
    "62": "北西太平洋", "63": "中北部太平洋", "70": "北米の亜寒帯（アラスカ・カナダ北部・グリーンランド）",
    "71": "カナダ西部", "72": "カナダ東部", "73": "アメリカ北西部", "74": "アメリカ中北部", "75": "アメリカ北東部",
    "76": "アメリカ南西部", "77": "アメリカ中南部", "78": "アメリカ南東部", "79": "メキシコ", "80": "中央アメリカ",
    "81": "カリブ海", "82": "南アメリカ北部", "83": "南アメリカ西部", "84": "ブラジル", "85": "南アメリカ南部",
    "90": "亜南極の島々", "91": "南極大陸",
}
# 東アジア（level 2 = 38）は国・島の単位まで
L3_EA = {"JAP": "日本", "KOR": "朝鮮半島", "TAI": "台湾", "KZN": "千島列島", "NNS": "南西諸島", "OGA": "小笠原諸島"}
EU = ["10", "11", "12", "13", "14"]
US = ["73", "74", "75", "76", "77", "78"]


def summarize(l2s, l3_ea):
    """level 2 の区分（順序つき）を日本語の短い文にする。"""
    s = set(l2s)
    parts = []
    done = set()
    for code in sorted(s):
        if code in done:
            continue
        if code in EU and all(c in s for c in EU):
            parts.append("ヨーロッパ全域"); done.update(EU); continue
        if code in US and all(c in s for c in US):
            parts.append("アメリカ合衆国の全域"); done.update(US); continue
        if code in ("71", "72") and "71" in s and "72" in s:
            parts.append("カナダ南部"); done.update(("71", "72")); continue
        if code == "38":
            names = [L3_EA[c] for c in ["JAP", "KZN", "KOR", "TAI", "NNS", "OGA"] if c in l3_ea]
            parts.append("・".join(names) if names else L2[code]); done.add(code); continue
        parts.append(L2.get(code, code)); done.add(code)
    return "、".join(parts)


def clean(s):
    s = re.sub(r"[‘’‛'\"].*$", "", s)  # 品種名を外す
    s = re.sub(r"\(.*?\)", " ", s)
    s = s.replace("×", " × ").replace(" x ", " × ")
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"var\.(\S)", r"var. \1", s); s = re.sub(r"subsp\.(\S)", r"subsp. \1", s)
    s = re.sub(r"\s+(sp|spp|hybrid|hybrids|group|Group)\.?$", "", s).strip()
    return s


def main():
    wb = openpyxl.load_workbook(XLSX, read_only=True)
    ws = wb["マスター（下書き916品種）"]
    R = list(ws.iter_rows(values_only=True)); h = R[1]
    ino, ig = h.index("商品番号"), h.index("学名（正名）")
    ctxc = [h.index(c) for c in ("学名（RHS）", "旧学名・別名", "学名のメモ") if c in h]
    plants = [(str(r[ino]), r[ig] or "", " ".join(str(r[i]) for i in ctxc if r[i])) for r in R[2:] if r[ino] is not None]
    CTX = {"": ""}

    rows, byname = {}, {}
    with open(os.path.join(WD, "wcvp_names.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="|"):
            if r["taxon_rank"] not in ("Species", "Variety", "Subspecies", "Form"):
                continue
            rows[r["plant_name_id"]] = r
            key = re.sub(r"\s+", " ", r["taxon_name"].replace("×", " ")).strip()  # × は外して引く
            byname.setdefault(key, []).append(r["plant_name_id"])
    dist = {}
    with open(os.path.join(WD, "wcvp_distribution.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="|"):
            if r["introduced"] != "0" or r["extinct"] != "0" or r["location_doubtful"] != "0":
                continue
            dist.setdefault(r["plant_name_id"], []).append((r["region_code_l2"], r["area_code_l3"]))

    order = {"Accepted": 0, "Artificial Hybrid": 1, "Synonym": 2, "Illegitimate": 3}

    amb = {}

    def find1(q, hyb):
        pids = [p for p in byname.get(q, []) if rows[p]["taxon_status"] in order]
        if hyb:  # 交配種として書かれた名前は、Kew でも交配種のものだけに当てる
            pids = [p for p in pids if rows[p]["species_hybrid"] or rows[p]["hybrid_formula"]]
        if not pids:
            return None, None
        acc_ids = {p if rows[p]["taxon_status"] in ("Accepted", "Artificial Hybrid") else rows[p]["accepted_plant_name_id"] for p in pids}
        acc_rec = [p for p in pids if rows[p]["taxon_status"] in ("Accepted", "Artificial Hybrid")]
        if acc_rec:
            pid = acc_rec[0]
        elif len(acc_ids) == 1:
            pid = sorted(pids, key=lambda p: order[rows[p]["taxon_status"]])[0]
        else:  # 同じ名前が別々の正名を指す（同名異物）。表の RHS の学名・旧学名・メモに、
            # 行き先の正名か「名前＋命名者」が書かれていればそれに決める。なければ空ける
            t = CTX[""]
            hit = [p for p in pids if (rows[p]["taxon_name"] + " " + rows[p]["taxon_authors"]) in t
                   or " ".join(rows.get(rows[p]["accepted_plant_name_id"], {}).get("taxon_name", "?").split()[:2]) in t]
            if len({rows[p]["accepted_plant_name_id"] for p in hit}) == 1:
                r = dict(rows[hit[0]]); r["_決め方"] = "同名の別種あり。表の RHS の学名・旧学名で決めた"
                return r, rows[r["accepted_plant_name_id"]]
            amb[q] = sorted(rows[p]["taxon_name"] + " " + rows[p]["taxon_authors"] + "→" + rows.get(rows[p]["accepted_plant_name_id"], {}).get("taxon_name", "?") for p in pids)
            return None, None
        r = rows[pid]
        acc = r if r["taxon_status"] in ("Accepted", "Artificial Hybrid") else rows.get(r["accepted_plant_name_id"])
        if not acc:
            return None, None
        return r, acc

    def find(q, loose=False):
        # 交配種の印（×）は WCVP の名前に入っていないので、外した形で引き、交配種の記録だけに当てる。
        # 種小名の綴りの揺れ（-ii と -i）も試す。
        hyb = "×" in q
        q0 = q
        q = q.replace("× ", "")
        vs = [q]
        for v in list(vs):
            w = v.split()
            if len(w) >= 2:
                e = w[-1]
                alt = e[:-1] if e.endswith("ii") else e + "i" if e.endswith("i") else None
                if alt:
                    vs.append(" ".join(w[:-1] + [alt]))
        # 小文字の x で書かれた名前（loose）は、交配種で当たらなければ普通の種でも引く
        for h in ([hyb, False] if (loose and hyb) else [hyb]):
            for v in vs:
                r, acc = find1(v, h)
                if r:
                    if v != q:
                        r = dict(r); r["_綴り"] = v
                    return r, acc
        return None, None

    out = {}
    for no, sci, ctx in plants:
        CTX[""] = ctx
        q = clean(sci)
        parts = q.split()
        cands = [q]
        if len(parts) > 2 and parts[1] != "×":
            cands.append(" ".join(parts[:2]))
        if len(parts) > 3 and parts[1] == "×":
            cands.append(" ".join(parts[:3]))
        rec = {"学名": sci, "照合": None}
        for c in cands:
            r, acc = find(c, loose=" x " in sci and "×" not in sci)
            if not r:
                continue
            d = dist.get(acc["plant_name_id"], [])
            lvl = "infra" if acc["taxon_rank"] in ("Variety", "Subspecies", "Form") else "species"
            if not d and lvl == "infra":
                sp = find(acc["genus"] + " " + acc["species"])[1]
                if sp and dist.get(sp["plant_name_id"]):
                    acc, d, lvl = sp, dist[sp["plant_name_id"]], "species"
            rec.update({"照合": r.get("_綴り", c), "状態": r["taxon_status"], "正名": acc["taxon_name"] + " " + acc["taxon_authors"],
                        "単位": lvl, "決め方": r.get("_決め方", ""), "途中まで": c != q, "英語の分布": acc["geographic_area"],
                        "交配式": acc.get("hybrid_formula") or r.get("hybrid_formula") or ""})
            if "×" in c and rec["交配式"] and (r["species_hybrid"] or r["hybrid_formula"]):
                rec["原産地"] = "交配種（交配親：" + rec["交配式"] + "）"
            elif d:
                l2 = sorted({a for a, _ in d}); l3 = sorted({b for a, b in d if a == "38"})
                rec["地域コード"] = l2; rec["東アジアの国"] = l3
                rec["原産地"] = summarize(l2, l3)
            elif rec["交配式"]:
                rec["原産地"] = "交配種（交配親：" + rec["交配式"] + "）"
            break
        if not rec["照合"]:
            a = [amb[c] for c in cands if c.replace("× ", "") in amb]
            if a:
                rec["理由"] = "同じ名前が Kew で別々の種を指すため決めない：" + " ／ ".join(a[0])
        out[no] = rec

    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=False)
    n = sum(1 for v in out.values() if v.get("原産地"))
    print("照合できた:", sum(1 for v in out.values() if v["照合"]), "/ 原産地あり:", n, "/", len(out))


if __name__ == "__main__":
    main()
