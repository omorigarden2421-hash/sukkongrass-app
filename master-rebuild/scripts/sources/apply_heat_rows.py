"""耐暑性・蒸れ耐性・西日耐性の判定（scripts/heat_trial.py の D。2026-11-19 にユーザーが採用）を trial/rows/ に反映する。

使い方: python3 -I scripts/sources/apply_heat_rows.py <trial フォルダ>
heat（耐暑性）を入れ直し、muggy（蒸れ耐性）と west_sun（西日耐性）を新しく作る。
何度実行しても同じ結果になる（"by": "heat" の印を付けた記録を入れ直す）。
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from heat_trial import D, LEVEL, OGIHARA_CONFLICT, OGIHARA_HEAT  # noqa: E402

TRIAL = sys.argv[1]
TAG = "heat"
SID = {"MBG": "s02", "NC State": "s06", "Wildflower Center": "s09", "RHS": "s01", "Walters": "s10", "シカゴ植物園": "s08",
       "Gaißmayer": "s17", "Jelitto": "s11"}
FIELDS = (("heat", "耐暑性"), ("muggy", "蒸れ耐性"), ("west_sun", "西日耐性"))


def main():
    for pid, (heat, muggy, west, aux, why, src) in sorted(D.items()):
        path = f"{TRIAL}/rows/{pid}.json"
        d = json.load(open(path, encoding="utf-8"))
        f = d["fields"]
        for c in [c for c in d.get("changes_20261119", []) if c.get("by") == TAG]:
            if c["prev"] is None:
                f.pop(c["field"], None)
            else:
                f[c["field"]] = c["prev"]
        d["changes_20261119"] = [c for c in d.get("changes_20261119", []) if c.get("by") != TAG]
        d["conflicts"] = [c for c in d.get("conflicts", []) if not (isinstance(c, dict) and c.get("by") == TAG)]
        if pid in OGIHARA_CONFLICT:
            d["conflicts"].append({"field": "heat", "detail": OGIHARA_CONFLICT[pid], "by": TAG})
        sources = [SID[s] for s in src.split("、")] if src else []
        level = LEVEL.get(pid) or (f.get("heat") or {}).get("level") or "species"
        for (key, label), value in zip(FIELDS, (heat, muggy, west)):
            prev = f.get(key)
            old = (prev or {}).get("value")
            note = why + ("。目安（値には入れていない）: " + aux if aux and value is None else "")
            new = {"value": value, "note": note}
            if value is not None:
                srcs, method = sources, "判定"
                if pid in OGIHARA_HEAT and key == "heat":
                    srcs, method = ["s20"], "記載"
                elif pid in OGIHARA_HEAT and key == "west_sun":
                    srcs = sources + ["s20"]
                new = {"value": value, "method": method, "sources": srcs, "level": level, "note": note}
            f[key] = new
            if old != value or prev is None:
                reason = "耐暑性・蒸れ耐性・西日耐性を分けて判定するルール（2026-11-19 決定）: " + why
                d["changes_20261119"].append({"field": key, "old": old, "new": value, "reason": reason, "by": TAG, "prev": prev})
        json.dump(d, open(path, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    print("反映", len(D))


main()
