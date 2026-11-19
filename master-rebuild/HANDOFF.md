# 引き継ぎ（2026-11-19 更新）

## 目的
宿根草の生産者（北海道広尾町）の通販・卸用マスターデータを、文献だけを根拠に作り直している。
28品種で試作済み。試作を固めてから全件（約1,000品種）に進む。

## まず読むもの（このフォルダ内）
- DECISIONS.md … これまでの決定事項（最優先）
- trial/SPEC.md … 文献調査の仕様（集める項目・出力形式）
- trial/RULES.md … 文献の記述をマスターの区分に当てはめるルール（DECISIONS.md の変更が優先）
- trial/evidence/ … 試作28品種で集めた文献の記述（原文・URL付き）
- trial/rows/ … 当てはめた値
- scripts/assemble.py … 試作マスター（Excel）を組み立てる。元のマスター（価格・在庫を含む Excel）はユーザーの手元にあり、リポジトリには入れていない（公開リポジトリのため）
- scripts/sources/ … MBG・YList・stauden.de の取得と evidence への追記。Jelitto・Gaißmayer は chrome_curated.py（Chrome で読んで書き写したもの）と merge_chrome.py

## 2026-11-19 にやったこと（クラウドのセッション。ユーザーのパソコンにはつながっていない）
文献が読めるかの確認結果：

| 文献 | 結果 | 補足 |
|---|---|---|
| s02 MBG | 読める | サーバーが中間証明書を送らないので、http://cacerts.digicert.com/GeoTrustTLSRSACAG1.crt を足した CA ファイルで取得する。本体は plantfinder.mobot.org に転送される。検索は PlantFinderProfileResults.aspx?basic=（1ページ6件。品種名だけ、または「属 種」で検索する） |
| s04 YList | 読める | http のみ。簡易検索の結果ページから和名と標準／synonym が取れる |
| s18 stauden.de 無料版 | 読める | 接続許可リストに www.stauden.de を追加した。ログインなしで品種ごとの項目が読める（staudendatenbank/api.php の search と plant。ページ自身が使っている公開の検索） |
| s11 Jelitto | クラウドからは読めない | Cloudflare の確認画面（403）。回避はしない。ユーザーのパソコンの Chrome では読める（下の「パソコンの Chrome でやったこと」） |
| s17 Gaißmayer | クラウドからは読めない | 同上 |

試作28品種への追記（trial/evidence/、`checked: 2026-11-19`）：
- MBG：24品種（品種ページ15、種・交配群のページ9）。なし：P04 サギナ、P06 アガスタチ、P07 アルケミラ、P28 ミントブッシュ
- YList：17品種で和名あり（種レベル）。交配品種や日本に縁の薄い種は該当なし
- stauden.de：25品種（品種ページ20、種のページ5。P24 スピレアは学名だけで中身なし）。なし：P25 エゾアジサイ、P27 コルヌス、P28 ミントブッシュ

stauden.de 無料版で読める主な項目：花の高さ・葉の高さ、花期、草姿、増え方（株立ち／地下茎／ランナー、こぼれ種の程度）、葉の時期（夏緑・冬緑・常緑）、日照、場所（暖かい所を好む／涼しい所を好む 等）、耐寒ゾーン（Z3〜Z9 と温度）、土の湿り、原産地、手入れ（切り戻しの時期、こぼれ種の注意、冬の保護）、繁殖方法、毒・香り、用途（切り花・蜜源）、Lebensbereich（植栽環境の区分）、品種評価（Staudensichtung の星と評価年）。
読めないもの：暑さ・蒸れの文章、病害虫、株張り（あるのは植え付け間隔）。

## 2026-11-19 パソコンの Chrome でやったこと（Claude in Chrome。ユーザーのパソコンのセッション）
Jelitto(s11)・Gaißmayer(s17) を Chrome で読み、試作28品種の trial/evidence/ に追記した（`checked: 2026-11-19`、計405件）。
- 読み方：Chrome でサイトを開くと Cloudflare の確認は自動で通った（Jelitto は十数秒かかった。チェックボックスが出たままなら、ユーザーに押してもらう）。サイト内検索で品種を探し、商品ページを開いて本文を読んだ。Gaißmayer は URL の末尾に `?static` を付けると「Mehr lesen」の続きと質問への回答まで1ページで読める
- 書き写した内容は scripts/sources/chrome_curated.py、evidence への追記は scripts/sources/merge_chrome.py（`python3 -I scripts/sources/merge_chrome.py trial`。何度実行しても同じ結果。merge.py とは別に動く）
- Jelitto：12品種（品種ページ4：P02 イエロークィーン、P05 ラブパレード、P12 マグナス、P18 フローレイン。種のページ8：P03・P04・P07・P09・P19・P20・P21・P23）。種子の会社なので、栄養繁殖の品種・低木は掲載なし
- Gaißmayer：15品種（品種ページ8：P01・P08・P09・P10・P11・P13・P18・P22。種のページ7：P03・P04・P17・P19・P20・P21・P23）
- どちらにもなし：P06 アガスタチ、P14 アルメリア、P15 セダム、P16 ヒューケラ、P24〜P28（低木・ミントブッシュ）
- 読める主な項目：Jelitto＝科、原産地、花色、花期、耐寒ゾーン（USDA）、葉、草姿、花を含む高さ、土、日照、用途。Gaißmayer＝花色、花期、高さ、日照、Lebensbereich（土の湿り）、耐寒ゾーン、ナメクジの食害、毒、香り、切り花、育種者、本文（増え方・こぼれ種・切り戻し・冬の保護など）と質問への回答
- Gaißmayer の質問への回答は、ナーサリー自身の回答文だけを使った（客の質問文は使っていない）
- 気づいたこと：P03 の耐寒ゾーンが Jelitto Z3-Z9 と Gaißmayer Z6 で食い違う。P12 は Gaißmayer にあるのが 'Magnus Superior' で別名なので使っていない。P23 は Jelitto が種の種子に [Madonna] の別名を付けている。P20 は両方とも Tricyrtis hirta（種）のページ。詳しくは各 evidence の notes
- trial/rows/ と試作表（Excel・確認用ページ）にはまだ反映していない

## 次にやること
1. Jelitto・Gaißmayer の文献の順位と使い方を決める（ゾーン・花期・高さを値に使うか、stauden.de と同じく記録だけにするか）。RULES.md にはまだ s11・s17 の扱いがない
2. DECISIONS.md の決定を RULES.md と assemble.py に反映し、新しい evidence（s02・s04・s18・s11・s17）を trial/rows/ に当てはめて試作表を作り直す。assemble.py は元のマスター（Excel）が必要。クラウドのセッションにはユーザーのパソコンのフォルダ（ClaudeWork）がつながらなかったので、元のマスターをセッションに渡してもらう（リポジトリには入れない）
3. 未決事項をユーザーに確認する（DECISIONS.md の「未決」）。ユーザーは確認事項をチェックリスト形式で答えるのを好む
4. 試作が固まったら、全件へ進む手順をユーザーと決める

## 注意
- 文献にない値は推測で埋めない（空欄）。値ごとに文献ID・原文・URL・確認日を残す
- 文献値・自社の実測値・設計上の推奨値は分けて管理する
- 価格・在庫を含むデータは公開リポジトリにコミットしない
- 文献の本文そのもの（ページ全体）はリポジトリに入れない。短い引用だけを evidence に残す
