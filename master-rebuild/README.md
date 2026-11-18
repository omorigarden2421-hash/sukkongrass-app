# 宿根草マスター再作成

文献だけを根拠に宿根草マスターを作り直す作業の記録。

- `trial/SPEC.md` … 文献調査の仕様（使ってよい文献と集める項目）
- `trial/RULES.md` … 文献の記述をマスターの区分に当てはめるルール
- `trial/input/` … 試作28品種の対象（今のマスターの学名と出典）
- `trial/evidence/` … 文献から集めた記述（原文・URL付き）
- `trial/rows/` … ルールで当てはめた値
- `trial/kew.json` … Kew（WCVP）での学名照合結果
- `scripts/assemble.py` … 試作マスター（Excel）を組み立てる
- `scripts/kew.py` … Kew の学名データとの照合（データは https://sftp.kew.org/pub/data-repositories/WCVP/wcvp.zip を /tmp/claude-0/kew に展開）
- `scripts/ias.py` … 環境省 生態系被害防止外来種リスト（植物）との照合（https://www.env.go.jp/nature/intro/2outline/list/list_plants.xlsx を /tmp/claude-0/env に保存）
- `pages/` … 確認用チェックリストのページ

価格・在庫を含む元のマスターと試作の Excel は、このリポジトリが公開のため入れていない。
