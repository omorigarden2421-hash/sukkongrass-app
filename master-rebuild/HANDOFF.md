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
1. （済）Jelitto・Gaißmayer の文献の順位と使い方は 2026-11-19 に決定し、DECISIONS.md と RULES.md に書いた（ゾーン・花期・高さ・暑さは記録だけ、順位は stauden.de > Gaißmayer > Jelitto、Jelitto が発表元の P05・P12 は s12 と同じ扱い）
2. （済）Jelitto・Gaißmayer の evidence を trial/rows/ に当てはめ、試作表と確認用ページを作り直した（2026-11-19、ユーザーのパソコン）
   - 当てはめは scripts/sources/apply_chrome_rows.py（`python3 -I scripts/sources/apply_chrome_rows.py trial`。空欄だけを埋め、値がある項目は変えずに食い違いを conflicts に書く）
   - 埋めた項目は8つ：P18 ルピナス（学名、花色の分類・詳細、別名）、P19 オミナエシ（香り）、P21 ゲラニウム（広がりすぎの注意）、P22 フロックス（旧表記、こぼれ種の量 1）。食い違いの記録は5つ（P08・P19・P21・P22・P23）
   - s02・s04・s18 の rows への当てはめと DECISIONS の反映は、前のクラウドのセッションですでに済んでいた（rows の changes_20261119）
   - 試作表はユーザーのパソコンの `ClaudeWork/試作マスター_28品種_1119b.xlsx`（リポジトリには入れない）。確認用ページは pages/master-trial-1119.html（今回の変更点は合計151件、うち今回の8件は理由が「Jelitto・Gaißmayer:」で始まる）
   - パソコンで assemble.py を動かすときは、環境省のリストの場所を環境変数 IAS_XLSX で渡す（ias.py）
   - 作り直した後の確認事項4つ（フロックスの増え方、食い違い4件、ルピナスの学名、アネモネ 'マドンナ' の扱い）はユーザーが回答済み（DECISIONS.md「試作表の確認」）。rows・試作表・ページに反映した
   - 耐暑性・蒸れ耐性・西日耐性（2026-11-19）：以前のルールのメモがユーザーのパソコンで見つかり、3項目を分けて判定するルールに決めた（DECISIONS.md、RULES.md の heat・muggy・west_sun）。28品種の判定は scripts/heat_trial.py、rows への反映は scripts/sources/apply_heat_rows.py（`python3 -I scripts/sources/apply_heat_rows.py trial`）。試作表は `ClaudeWork/試作マスター_28品種_1119c.xlsx`、元のマスターの値と並べた一覧は `ClaudeWork/試し判定_耐暑性・蒸れ・西日_28品種.xlsx`（どちらもリポジトリには入れない）
   - rows を作り直すときの順番：apply_chrome_rows.py → apply_heat_rows.py（逆でも値は同じ。changes_20261119 の並び順だけ変わる）
   - 暑さの記述がなかった7品種の読み直し（2026-11-19）：NC State の属のページと MBG を読み直し、見つけた記述を scripts/sources/add_reread.py で evidence に追記（P17 の MBG の1文は mbg_curated.py にも追加）。耐暑性が埋まったのは P06・P17。残り5品種は DECISIONS.md の未決
   - おぎはら植物園（s20）を耐暑性専用の文献として追加（2026-11-19）：28品種中12品種が掲載。evidence への追記は scripts/sources/add_ogihara.py。耐暑性が空欄だった P01・P03・P15・P23 に値を入れた（heat_trial.py の OGIHARA_HEAT）。全件に進むときは、図鑑の検索（POST gallery/search.php、mode=search、text=名前）→ page01.php?id= の DATA を読む
3. （済）未決事項は 2026-11-19 にチェックリストで回答済み（DECISIONS.md「未決事項」の回答）。残りはミントブッシュの種だけ（ユーザーの確認待ち）
4. 全件（916品種）へ進む。その前に、ホスタ・ゲラニウム・ベロニカの3属（約80品種）で試す（2026-11-19 にユーザーと決定。まだ着手していない）。単位は種、順番は在庫のある品種が多い属から
   - 文献の読める場所：RHS・NC State・シカゴ・Walters・MBG・YList・stauden.de はクラウドから。Jelitto・Gaißmayer はユーザーのパソコンの Chrome、おぎはら植物園はパソコンのブラウザー（クラウドから読めるかは未確認）
   - 手順の案：元のマスターを属・種で並べ、種ごとに「種のページを1回読む → 同じ種の全品種に種レベルの項目を入れる → 品種ページがあれば品種の項目を足す」。7月の作業指示書（ユーザーのパソコン ClaudeWork4/マスターリスト修正_作業指示書_v1.2.md）も同じ考え方
   - 試作の rows は手書きの判定（heat_trial.py の D など）を含む。全件では同じルールで判定を作る仕組みが要る

## 3属の試行（ホスタ・ゲラニウム・ベロニカ。2026-11-19 に開始、作業中）
- 対象：78品種（ホスタ 32、ゲラニウム 28、ベロニカ 18）、種のまとまり 25。入力は pilot/input/（価格・在庫数なし）。作り方は scripts/pilot/make_input.py
- 取得：scripts/pilot/fetch_all.py（stauden.de・MBG・NC State・YList。生データはリポジトリの外）→ scripts/pilot/digest.py で1つの JSON にまとめる
- ブラウザーで読んだ分：scripts/pilot/ogihara_data.py（おぎはら植物園、42品種に耐暑性）、scripts/pilot/gaissmayer_data.py（Gaißmayer、19品種）
- 掲載率（途中）：stauden.de は品種ページ 44／78・種のページあり 41、おぎはら 42、Gaißmayer 21、MBG は取得のやり直し中
- 分かった問題：品種名にアポストロフィがあると切れる（修正済み）。'Album' のような同名の品種が別の種に当たる（fetch_all.py の照合を厳しくした。G12・G17 の MBG、H05 の MBG、V14・V17 の stauden.de は取り直しが必要）
- Walters（perennials.com）は品種名から URL を作って取得（78中42）。scripts/pilot/assemble_pilot.py が下書きの表を作る（出力はユーザーのパソコンの `ClaudeWork/試行_3属78品種_1119.xlsx`）
- 下書きの結果（78品種）：空欄は 日照 2、USDA 4、土壌水分 8、病害虫 8、耐暑性 15、西日耐性 15、常緑性 17、増え方 17、乾燥耐性 20、花色 34、株張り 36、葉色 37、切り戻し 45、切り花 49、蜜源 60、和名 63、蒸れ耐性 69。品種のページがどの文献にもないのは18品種
- 耐暑性の根拠の内訳：NC State の属のページ 30（ホスタ）、MBG 17、おぎはら 10、NC State の種 5、なし 15。おぎはらと食い違うのは21品種（ほとんどがホスタ：NC State の属の記述では 中、おぎはらは品種ごとに 強）
- 耐暑性・蒸れ・西日は言い回しの照合（assemble_pilot.py の P_HEAT_* など）で下書きし、根拠の文を横に出して人が確認する形にした
- まだ：RHS（品種のIDを調べる方法が要る）・シカゴ植物園・Jelitto の取得、試作と同じ形（rows・根拠・学名の検討）への統合、ユーザーの確認
- RHS を追加（2026-11-19）：検索結果は JavaScript で描かれるので、ブラウザーで rhs.org.uk を開き、見えない枠（iframe）で検索ページを順に開いて番号を拾った（78中68品種で該当ページあり。番号は scripts/pilot/rhs_ids.py）。詳細ページは curl で読める。表の項目（Aspect＝向き、Hardiness、Foliage、Habit、Moisture、Max Spread）と How to grow（Pruning・Pests・Diseases・Propagation）を assemble_pilot.py に取り込んだ。空欄は 株張り 36→16、切り戻し 45→10、常緑性 17→7、病害虫 8→2 に減った。Aspect に西向き・南向きがない品種は西日耐性を × にしている
- Jelitto とシカゴ植物園を追加（2026-11-19）：scripts/pilot/jelitto_cbg_data.py。Jelitto は11ページ（品種のページは V02・V11 だけ。原産地と蜜源に使用）。シカゴはゲラニウムの評価報告（Plant Evaluation Notes 22）の表から14品種（株幅・秋の葉色・花後の切り戻し）。ベロニカの報告（no33）は表が文字として崩れて取り出せず未使用。ホスタの報告はなし
- 自社の値：文献で埋まらなかった花色（33品種）・株張り（16）・葉色（37）に、今のマスターの値を別の列で入れた（pilot/input に 花色・広がり・葉色主分類 を追加）
- 下書きの Excel に「根拠」（1,137行）と「学名の検討」（42品種）のシートを付けた
- 確認事項はユーザーが回答済み（DECISIONS.md「3属の試行」の回答）。残り：試作の rows と同じ JSON の形にはしていない（下書きは Excel と JSON の表）、RHS の花色の欄は未取り込み、ベロニカの評価報告は PDF を目で読む必要がある、ユーザーの確認（食い違いと 弱 の品種）
- スマホ用の確認ページ（非公開の Artifact）を作った。作り方はユーザーのパソコンの一時フォルダのスクリプトで、リポジトリには入れていない

## 注意
- 文献にない値は推測で埋めない（空欄）。値ごとに文献ID・原文・URL・確認日を残す
- 文献値・自社の実測値・設計上の推奨値は分けて管理する
- 価格・在庫を含むデータは公開リポジトリにコミットしない
- 文献の本文そのもの（ページ全体）はリポジトリに入れない。短い引用だけを evidence に残す
