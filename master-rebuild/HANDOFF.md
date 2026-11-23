# 引き継ぎ（2026-11-21 更新）

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
- 確認事項はユーザーが回答済み（DECISIONS.md「3属の試行」の回答）。残り：試作の rows と同じ JSON の形にはしていない（下書きは Excel と JSON の表）、ユーザーの確認（学名の検討42品種など）
- スマホ用の確認ページ（非公開の Artifact）を作った。作り方はユーザーのパソコンの一時フォルダのスクリプトで、リポジトリには入れていない
- 耐暑性の決め方を変更（2026-11-19 の最後の決定）：おぎはら植物園にページがあれば、その値を採る。試作では P08・P10・P21 が 強 に変わった（heat_trial.py の OGIHARA_HEAT）。3属では耐暑性の 弱 がなくなり、強 30・中 33・空欄 15。食い違いは根拠の文に「[食い違い]」として残る
- RHS の花色・葉色（Colour & scent の表）を取り込んだ：花色の空欄 34→16、葉色 37→16。自社の値が残るのは 花色 15・葉色 16・株張り 15 品種
- ベロニカの評価報告（Plant Evaluation Notes 33）：pdftotext の -raw で表が読めた。9品種の株幅と草姿、冬の傷みの記録を jelitto_cbg_data.py の CBG_V に入れた。「文献の注意」の列に 'Sunny Border Blue' の冬の傷み（5年中4年、試験の終わりまでに枯死）を出している。Table 3 の記号（c・d）の意味は未確認
- 学名の決定などを反映（2026-11-19、DECISIONS.md「学名・越冬・次の属」）：assemble_pilot.py に「学名（採用）」（RHS が Accepted／Correct なら RHS の表記、個別の決定は NAME_OVERRIDE）と「自社の観察」（OWN_NOTES）の列を追加

## 次の属：アスター（2026-11-19 に開始、作業中）
- ユーザーの決定：アスターから進め、確認は全部終わってからまとめて見る
- 入力は batch_aster/input（23品種、種のまとまり 12）。作り方：`python3 scripts/pilot/make_input.py <元のマスター.xlsx> batch_aster/input Aster=A`
- アスターは文献によって属名が違う（Symphyotrichum・Eurybia・Doellingeria）。fetch_all.py に GENUS_ALIAS・SPECIES_ALIAS を足した
- 下書きまで完了（2026-11-19）：データは batch_aster/（ogihara_data.py 3品種、gaissmayer_data.py 8品種、rhs_ids.py 18品種、jelitto_cbg_data.py：Jelitto は種のページ6つ、シカゴ植物園 Plant Evaluation Notes 36 Asters から8品種の総合評価・株幅・うどんこ病とさび病への強さ）
- 組み立て：`python3 -X utf8 scripts/pilot/assemble_pilot.py batch_aster/input <digest> <raw> <出力.xlsx> batch_aster`（最後の引数が属ごとのデータのフォルダ）。RHS の取得は scripts/pilot/fetch_rhs.py、Walters は scripts/pilot/fetch_walters.py（アスターは1品種しか当たらなかった）
- 結果（23品種）：日照・USDA・土壌水分・病害虫は全品種、切り戻しは20品種。耐暑性は4品種だけ（おぎはら3、NC State 1〔シオン〕）。欧米の文献はアスターの暑さをほとんど書いていない。蒸れ耐性は18品種が 中（「風通しを良くすると葉の病気が減る」という記述から）。品種のページがどの文献にもないのは5品種（A08・A10・A11・A13・A14）
- 学名の検討は17品種（RHS は多くを Symphyotrichum・Eurybia・Doellingeria に移している。デュモーサスの品種を novi-belgii としている文献がある）
- 出力はユーザーのパソコンの `ClaudeWork/下書き_アスター23品種_1119.xlsx`
- 次の属の候補（在庫の多い順）：ヘメロカリス、カンパニュラ、カレックス。ユーザーは「確認は全部終わってからまとめて」と回答済み

## 次の3属：ヘメロカリス・カンパニュラ・カレックス（2026-11-19 に開始、作業中）
- 入力は batch_02/input（55品種：M=ヘメロカリス17、C=カンパニュラ25、X=カレックス13。種のまとまり 22）。作り方：`python3 scripts/pilot/make_input.py <元のマスター.xlsx> batch_02/input Hemerocallis=M Campanula=C Carex=X`
- ブラウザーで読む分は済み。データは batch_02/（rhs_ids.py 50品種、ogihara_data.py 10品種、gaissmayer_data.py 7ページ、jelitto_cbg_data.py 9ページ）。シカゴ植物園の評価報告はこの3属では探していない
- 残りの手順（このとおり実行すれば下書きができる。<raw> は生データの保存先で、リポジトリの外の好きなフォルダでよい。消えていたら取り直せる）
  1. `python3 -I scripts/pilot/fetch_all.py batch_02/input <raw>`（stauden.de・MBG・NC State・YList。取得済みは飛ばす）
  2. `python3 -I scripts/pilot/fetch_walters.py batch_02/input <raw>`
  3. `python3 -I scripts/pilot/fetch_rhs.py batch_02 <raw>`（2026-11-19 に50ページ取得済み）
  4. `python3 -I scripts/pilot/digest.py <raw> <digest.json>`
  5. `python3 -X utf8 scripts/pilot/assemble_pilot.py batch_02/input <digest.json> <raw> <出力.xlsx> batch_02`
  6. 下書きの耐暑性・蒸れ・西日の根拠を見て、当たり違い（同名の別品種）や判定のおかしいものを直す
- 2026-11-19 の終わりに手順1〜5まで実行済み（最初の下書きは `ClaudeWork/下書き_ヘメロカリス・カンパニュラ・カレックス55品種_1119.xlsx`）
- 手順6（下書きの中身の確認）を実施（2026-11-19、ユーザーのパソコン）。直した下書きは `ClaudeWork/下書き_ヘメロカリス・カンパニュラ・カレックス55品種_1119b.xlsx`（前の `_1119.xlsx` は残してある）。生データは前のセッションの一時フォルダ（b2_raw・b2_digest.json）をそのまま使った
  - 同名の別品種への当たり違いは見つからなかった（stauden.de・MBG・Walters・おぎはら・RHS の掲載名を全品種で照合）
  - 直したこと（assemble_pilot.py）
    1. MBG の「夜温が 70°F（約21℃）を下回らない夏には向かない」という文（Does not do well／perform well …）が耐暑性に反映されていなかった。弱 の言い回しに追加。カンパニュラの耐暑性は 中 → 弱 が7品種（C07・C10・C15・C17・C19・C20・C21）。おぎはらにページがある5品種（C09・C18・C22・C24・C25）は 強 のままで、食い違いの記録が「弱 相当」になった。C24 は「hot and humid summer climates … do not perform well」で蒸れ耐性 弱
    2. カンパニュラでは、MBG の品種ページの文を「属の記述」としてほかの種に広げない（GENUS_MBG_SKIP）。ページがあるのはホタルブクロの仲間だけで、ラクティフローラ等に当てると推測になるため。C06・C08・C11・C12・C14・C16・C23 の耐暑性・西日耐性と、MBG・属 から入っていた USDA・土壌水分・病害虫・切り戻しは空欄に戻った
    3. 「品種ページのある文献」の数え方：RHS の名前だけの登録（栽培の項目がないページ。X11・X12 など）と、Gaißmayer の種のページ（X08・X09）は数えない。種のページからは花色を取らない
    4. 乾燥耐性の言い回しを追加（occasional drought → 中、must not be allowed to dry out → 弱。X04・X08・X09）。Walters の ™ の文字化けを直した
  - 直した後の結果（55品種）：耐暑性 強 26・中 5・弱 8・空欄 16、蒸れ耐性 強 18・弱 2・空欄 35、西日耐性 ◎5・○24・△8・×3・空欄 15。品種のページがどの文献にもないのは11品種（C06・C14・C15・C16・M11・M12・M15・X06・X08・X11・X12）
  - アスターと3属の試行を同じスクリプトで作り直して比べた：値の違いは「品種ページのある文献」の列だけ（RHS の名前だけの登録を数えなくなった分。アスター4品種、試行9品種）。ユーザーの手元の Excel は作り直していない
  - ユーザーに見てもらうもの（要注意）：耐暑性 弱 の8品種（上の7品種と C13 パーシシフォリア 'モーハイミ'）、蒸れ耐性 弱 の2品種（C24、X07 'エバーゴールド'）、おぎはらとの食い違い6品種（C09・C18・C22・C24・C25・X07）
  - （回答済み）ホタルブクロの C17・C19・C20・C21 は、おぎはらの同じ種の品種に合わせて 強 にした。耐暑性 弱 は4品種（C07・C10・C13・C15）になった
- 気づいた点：カレックスの一部（ブキャナニー、'フロステッドカール'、'エバーゴールド'）は、おぎはらが耐寒性「約 -12℃」、Jelitto がゾーン6〜9 としている。商品「カレックス 'バーグレニーアイ'」はマスターの学名が Carex talbotii だが、RHS・Jelitto には Carex berggrenii がある。カレックス 'Kiwi'・'Blue Ridge' は Jelitto が発表元
- シカゴ植物園の評価報告を追加（2026-11-19）：Plant Evaluation Notes 31 Bellflowers から8品種（C07・C08・C09・C12・C13・C22・C23・C24）の株幅と注意を batch_02/jelitto_cbg_data.py の CBG_V に入れた。'Sarastro' は試験で最高評価、'Moerheimii' は2年目の夏に根腐れで枯れた、という記録を「文献の注意」に出している。ヘメロカリスとカレックスの号はない

## その次の3属：フロックス・ペルシカリア・サルビア（2026-11-19 に開始、作業中）
- 入力は batch_03/input（52品種：F=フロックス19、R=ペルシカリア17、S=サルビア16。種のまとまり 14）。作り方：`python3 scripts/pilot/make_input.py <元のマスター.xlsx> batch_03/input Phlox=F Persicaria=R Salvia=S`（P は試作の ID で使っているので、フロックスは F、ペルシカリアは R）
- fetch_all.py に足したもの：ペルシカリアの別の属名（Bistorta・Koenigia など。GENUS_ALIAS・SPECIES_ALIAS）、品種名の別の書き方（CV_ALIAS：May Night＝Mainacht、Queen Blue＝Blue Queen／Blaukönigin、Norah Leigh＝Nora Leigh、David Lavender＝David's Lavender）、品種名がぴったり一致する候補を先に採る（'David' が 'David's Lavender' に当たらないように）、'White' はありふれた品種名として種小名も照合
- おぎはら植物園：batch_03/ogihara_data.py（27ページ、34品種に当てた）。図鑑の検索は curl でも読めた（やり方はそのファイルの冒頭）。ブラウザーは要らない
- RHS：batch_03/rhs_ids.py（45品種。アプリ内のブラウザーで検索ページを順に開いて番号を拾い、候補のページを curl で読んで正名のページを選んだ）。RHS はアンプレクシカウリスとアフィニスを Bistorta に移している
- シカゴ植物園：batch_03/jelitto_cbg_data.py の CBG_V（no35 宿根フロックス 5品種、no13 フロックス 2品種、no14 サルビア 3品種）。ペルシカリアの号はない。株幅が幅で書かれている報告のために、CBG_V の株幅は (下限, 上限) でも書けるようにした（assemble_pilot.py）
- Gaißmayer・Jelitto：ユーザーのパソコンの Chrome（Claude in Chrome）で読んだ（2026-11-19）。batch_03/gaissmayer_data.py（21ページ、26品種に当てた）、batch_03/jelitto_cbg_data.py の JELITTO（11ページ）。探し方は各ファイルの冒頭
  - 【ユーザーの指示】この2サイトは、次からも必ず Chrome で読む。アプリ内のブラウザーでは Cloudflare の確認画面から進まず、ユーザーが押しても通らなかった。Chrome では確認画面なしで開けた
  - Chrome の JavaScript の結果は約1,000字で切れ、URL の ? 以降を含む文字列は遮断される。1ページごとに「表の項目」と「本文」を短く切って返すと読める
- 下書きまで完了（2026-11-19）：`ClaudeWork/下書き_フロックス・ペルシカリア・サルビア52品種_1119.xlsx`。組み立ては `python3 -X utf8 scripts/pilot/assemble_pilot.py batch_03/input <digest> <raw> <出力.xlsx> batch_03`
  - 結果（52品種）：耐暑性 強 26・中 8・空欄 18（弱はなし）、蒸れ耐性 強 6・中 15・空欄 31、西日耐性 ◎12・○20・△1・×4・空欄 15。品種のページがどの文献にもないのは6品種（F04・F06・F10・F18・R02・R07）。学名の検討は32品種
  - 宿根フロックスの蒸れ耐性 中 は「風通しを良くするとうどんこ病が減る」という記述から（アスターと同じ）。宿根フロックスの耐暑性は、おぎはらにページのある2品種（'Blue Paradise'・'David'）だけ 強、ほかは空欄（欧米の文献に暑さの記述がない）
  - 根拠を確認して直したこと：(1) S07 'Madeline' の MBG がローズマリーの 'Madeline Hill' に当たっていた → fetch_all.py で、品種名の前半だけが合う候補は種小名も一致するときだけ採るようにした (2) S15 'Rhapsody in Blue' に、おぎはらのプラテンシスの同名品種を当てていた → 別の品種と見て外した（stauden.de・MBG に nemorosa／× sylvestris の 'Rhapsody in Blue' がある） (3) ペルシカリアも GENUS_MBG_SKIP に追加（MBG のアンプレクシカウリスの文を、アフィニスやミクロセファラに広げない）
  - ユーザーに伝えること：'Red Dragon' は Gaißmayer が Z8・「冬越ししない宿根草」の扱い（冬は落ち葉などで覆う、春植えを勧める）、RHS は H4。'Blue Paradise' は Gaißmayer が「涼しい地域で特によく育つことが多い」、シカゴ植物園が「葉の斑点病で下葉が落ちやすい」。斑入りの宿根フロックス（'Harlequin'・'Norah Leigh'）はシカゴ植物園で晩夏に葉焼け
  - ユーザーの回答（2026-11-19、DECISIONS.md に記録）：(a) 同じ種のおぎはらの値を使う（試し。見返せるように「耐暑性の決め方」「耐暑性（欧米の文献だけなら）」の2列を下書きの右端に追加。assemble_pilot.py と各 batch の ogihara_data.py の SIBLING）(b) S15 は × シルベストリス (c) S12 は 'Blue Queen' と同じ品種として扱う。反映後：batch_02 の耐暑性は 強 30・中 5・弱 4・空欄 16、batch_03 は 強 32・中 2・空欄 18
  - 宿根フロックス（paniculata）にも同じ扱いをする、と回答（'Blue Paradise'・'David' が根拠、ほか12品種を 強 に）。反映後の batch_03：耐暑性 強 44・中 2・空欄 6
- 名前で気づいた点（学名の検討に出る）：'Laura' は RHS では 'Uspekh' の別名（シカゴ植物園は別の品種として両方載せている）／'Red Riding Hood' は RHS では 'Miss Mary' の別名／'Merleau' の3品種は RHS では Salvia × digenea（マスターは nemorosa）／'Queen Blue' は 'Blue Queen'（'Blaukönigin'）の語順違いと見て当てた／'Rhapsody in Blue' はおぎはらでは pratensis の品種（マスターは × sylvestris）／'Brushstrokes' は RHS では Persicaria filiformis／'Silver Dragon' は RHS では種小名なし／ポリモーファは RHS ではシノニム扱い

## 4つ目のまとまり：セダム・エキナセア・アスチルベ（2026-11-19、下書きまで完了）
- 入力は batch_04/input（47品種：D=セダム〔Sedum 16・Hylotelephium 2〕、E=エキナセア15、B=アスチルベ14。種のまとまり 18）。作り方：`python3 scripts/pilot/make_input.py <元のマスター.xlsx> batch_04/input Sedum=D Echinacea=E Astilbe=B Hylotelephium=D`
- 文献：おぎはら 22ページ（どれも耐暑性 強）、RHS 40品種、Gaißmayer 14ページ・Jelitto 9ページ（どちらも Chrome。確認画面が一度出たが、待つと自動で通った）。シカゴ植物園の評価報告はこの3属にはない
- fetch_all.py に足したもの：セダムの別の属名（Hylotelephium・Phedimus）、'Autumn Joy'＝'Herbstfreude'、'Dragon's Blood'＝'Schorbuser Blut'、アスチルベ アレンジーの × 表記。'Mediovariegatum'・'Tricolor'・'Superba' などをありふれた品種名に追加（種小名も照合する）
- 下書き：`ClaudeWork/下書き_セダム・エキナセア・アスチルベ47品種_1119.xlsx`。耐暑性 強 31・中 10・空欄 6、蒸れ耐性 強 14・空欄 33、西日耐性 ◎13・○8・△6・×14・空欄 6。品種のページがどの文献にもないのは4品種（B03・B06・D18・E12）
- 根拠を確認して直したこと：D13 'Mediovariegatum' の MBG が別の種（erythrostictum）の同名品種に当たっていた → 種小名も照合するようにして外した。セダムも GENUS_MBG_SKIP に追加（背の高いベンケイソウの文を、ミセバヤなどに広げない）
- 同じ種のおぎはらの値：アスチルベ アレンジーの B03・B04・B05 を 強 にした（根拠は 'Color Flash Lime'・'Fanal'。batch_04/ogihara_data.py の SIBLING）
- アスチルベは全品種が 日照 半日陰・西日耐性 ×・乾燥耐性 弱（MBG：暑い夏や乾燥で、土が湿っていないと葉が傷む）。おぎはらは 強 なので、耐暑性は食い違いの記録つきで 強
- ユーザーに聞くこと・伝えること：(a) D10 は学名が Sedum 'Vera Jameson'、商品名が「セダム レフレクサム」で食い違う（今は学名のとおり 'Vera Jameson' の文献を当てている。D09 と同じ内容）(b) セダム 'Mediovariegatum' は Gaißmayer が Z7・「冬越ししない宿根草」の扱い、RHS は H3 (c) 'Autumn Joy' は RHS では Hylotelephium × mottramianum 'Herbstfreude'（マスターは Hylotelephium spectabile）

## 5つ目のまとまり：ミント・ゲウム・ビンカ・プルモナリア・ペンステモン（2026-11-19 に開始、作業中）
- 残りの属は1属あたり10品種前後なので、5属ずつ（約50品種）にまとめる。順番は在庫のある品種が多い属から（残りの上位：ポテンティラ、パニカム、アキレア、スタキス、ヒューケラ、スカビオサ、ポレモニウム、フィリペンデュラ、サンギソルバ、トロリウス…）。batch_05 までで 916品種中 355品種の下書きができた
- 入力は batch_05/input（50品種：Me=ミント11、Ge=ゲウム10、Vi=ビンカ9、Pu=プルモナリア11、Pe=ペンステモン9。ID は2文字の頭文字）
- 文献：おぎはら 16ページ（ミントは掲載なし）、RHS 46品種、Gaißmayer 16ページ・Jelitto 13ページ（Chrome）、シカゴ植物園 no17 Pulmonaria から6品種（batch_05/jelitto_cbg_data.py の CBG_V）
- 下書きまで完了（2026-11-19）：`ClaudeWork/下書き_ミント・ゲウム・ビンカ・プルモナリア・ペンステモン50品種_1119.xlsx`。耐暑性 強 21・中 16・空欄 13（ミント11品種とペンステモン バルバタス2品種は暑さの記述なし）、西日耐性 ◎2・○11・△10・×14・空欄 13。品種のページがどの文献にもないのは3品種（Me02・Vi06・Vi07）
- 根拠を確認して直したこと（assemble_pilot.py。前の batch にも効く）
  - 「Prefers cool, organically rich, humusy soils」（涼しい土を好む）を「涼しい気候を好む」と取り違えて、プルモナリア8品種が 弱 になっていた → cool の後ろが summer・weather・climate などのときだけ 弱 にする。8品種は 中 になった（おぎはらの 中 とそろった）
  - 属の代表（MBG の品種ページの文をほかの品種に広げる）は、同じ書き出しのページが2つ以上あるときだけ作る。ミントは1ページ（'Kentucky Colonel'）だけだったので、ほかのミントの USDA などは空欄に戻った。batch_04 の D01 'Mr Goodbud' も同じ理由で空欄に戻った（batch_02・03 は変化なし）
- プルモナリアは全品種が 日照 半日陰・西日耐性 ×・乾燥耐性 弱。シカゴ植物園では 'Blue Ensign'・'Lewis Palmer'・'Spilled Milk' が評価の低い一覧に入っている（うどんこ病、冬に全株が枯れた等。「文献の注意」に出している）
- ユーザーに聞くこと・伝えること：(a) Me05 は学名が Mentha × piperita だけで、商品名はグレープフルーツミント（RHS の 'Grapefruit' を当てた）(b) Me08 ストロベリーミントは RHS では × piperita 'Strawberry'（マスターは spicata subsp. citrata）(c) ビンカ マジョール 'Variegata' は Gaißmayer が Z7・「霜にやや弱い、厳しい土地では冬の保護が要る」(d) Vi03 と Vi04 は学名が同じ 'Atropurpurea'（商品名は別）

## 6つ目のまとまり：ポテンティラ・パニカム・アキレア・スタキス・ヒューケラ（2026-11-19、下書きまで完了）
- 入力は batch_06/input（49品種：Po=ポテンティラ12、Pa=パニカム8、Ac=アキレア9、St=スタキス8、He=ヒューケラ12）
- 文献：おぎはら 17ページ（23品種）、RHS 43品種、Gaißmayer 21ページ・Jelitto 24ページ（Chrome）、シカゴ植物園 no27 Stachys から5品種・no21 Coral bells から2品種（no5 Yarrow は PDF が画像だけで読めなかった）
- fetch_all.py に足したもの：スタキスの別の属名（Betonica）、ポテンティラ トライデンタータ＝Sibbaldiopsis、ベルナ＝neumanniana、'Walter Funcke'＝'Walther Funcke'、'Firefly'＝'Leuchtkäfer'、'Dallas Blue'＝'Dallas Blues'
- 下書き：`ClaudeWork/下書き_ポテンティラ・パニカム・アキレア・スタキス・ヒューケラ49品種_1119.xlsx`。耐暑性 強 24・中 15・空欄 10、蒸れ耐性 強 2・中 17・空欄 30、西日耐性 ◎11・○11・△6・×11・空欄 10。品種のページがどの文献にもないのは4品種（He09・Po06・Po11・St06）
- 根拠を確認した：同名の別品種への当たり違いは見つからなかった。直したところはない
- 同じ種のおぎはらの値：パニカム バーゲタムの5品種（Pa01〜Pa04・Pa08）とポテンティラ ネパレンシスの2品種（Po06・Po07）を 強 にした（batch_06/ogihara_data.py の SIBLING）
- ヒューケラは全品種が 耐暑性 中・西日耐性 ×（MBG：土が乾くと葉が焼けて傷む。おぎはらも 中）。パニカムとヒューケラの蒸れ耐性 中 は「高温多湿でさび病が出やすい」「乾いた空気を好む」から
- ユーザーに伝えること：スタキス 'Primrose Heron' はシカゴ植物園で冬の傷みが繰り返し出た／ヒューケラ 'Dale's Strain' は同じ試験で冬に株元が腐って枯れた／'Hummelo' と ヒューケラ 'White Cloud' は最高評価
- Gaißmayer は商品ページを1秒おきに続けて開くと、10ページほどで確認画面に切り替わった（待つと自動で通った）。1ページごとに6秒あけると出なかった

## 7つ目のまとまり：スカビオサ・ポレモニウム・フィリペンデュラ・サンギソルバ・トロリウス（2026-11-20、下書きまで完了）
- 入力は batch_07/input（34品種：Sc=スカビオサ7、Pl=ポレモニウム7、Fi=フィリペンデュラ6、Sa=サンギソルバ8、Tr=トロリウス6。種のまとまり 20）。マスターの「Scabiosa caucasia」はつづり違いなので、種のまとまりは caucasica にそろえた（make_input.py。学名の列はそのまま）
- 文献：おぎはら 15ページ（15品種）、RHS 31品種（候補63ページの Name Status を見て選んだ）、Gaißmayer 15ページ（19品種。Chrome、最初から6秒おき、確認画面は出なかった）。シカゴ植物園の一覧（no1〜no40）にこの5属の号はない
- Jelitto：17ページ（18品種。Chrome、6秒おき）。最初に検索ページを開いたとき Cloudflare の確認画面（チェックボックス）が出たまま1分待っても進まなかったので、操作せずにいったん飛ばした。15分ほど別の作業をしている間に、同じタブで確認が自動で通っていた（操作はしていない）。そのあとは出なかった。次も、出たら操作せずに別の作業を先にして、あとでタブを見直す
- Jelitto が発表した品種（育種会社 s12 と同じ扱いにできる）：ポレモニウム 'Purple Rain'（2006、'Purple Rain Strain'）、トロリウス 'Lemon Supreme'（2010）、'New Moon'（2011）。Jelitto は 'Perfecta' に [Blue Perfection] の別名を付けている（マスターの学名 'Blue Perfection' と商品名パーフェクタは同じ品種）。'Fama' は 'Fama Deep Blue' と 'Fama White' があり、どちらか決められないので当てていない
- fetch_all.py に足したもの：スカビオサの別の属名（Lomelosia）、'Compliment'＝'Kompliment'、'Blue Perfection'＝'Perfecta'、'Moon Dance'＝'Moondance'、'Venusta Magnifica'＝'Venusta'、トロリウス カルトラムの × 表記。'Elegans'・'Venusta' をありふれた品種名に追加
- 下書き：`ClaudeWork/下書き_スカビオサ・ポレモニウム・フィリペンデュラ・サンギソルバ・トロリウス34品種_1120.xlsx`。耐暑性 強 10・中 12・弱 5・空欄 7、蒸れ耐性 弱 11・空欄 23、西日耐性 ○13・△4・×11・空欄 6。品種のページがどの文献にもないのは4品種（Fi01・Pl04・Pl05・Tr05）。学名の検討は23品種（Jelitto を足して組み立て直した後も同じ）
- 根拠を確認して直したこと（assemble_pilot.py。前の batch にも効く）
  - MBG・NC State の「intolerant of high heat and humidity」（高温多湿に耐えない）が、tolerant of … heat の言い回しに当たって 強 になっていた（スカビオサ）。in- の付く形を 強 から外し、弱 に足した
  - MBG のトロリウスの文「cool weather plant」「dislikes dry soils and hot, humid summers」「not recommended for planting south of USDA Zone 7」が、どの言い回しにも当たっていなかった。弱 に足した
  - 前の batch を同じスクリプトで作り直して比べた：batch_02・03・04・06 は変化なし。batch_05 はゲウム5品種（Ge01・Ge02・Ge03・Ge05・Ge08）の耐暑性が 中 → 弱（MBG：深南部の夏の高温多湿では苦しむ。USDA ゾーン7より南には勧めない）。おぎはらにページのある Ge04・Ge06 は値は変わらず、食い違いの記録が「弱 相当」になった。作り直した下書きは `ClaudeWork/下書き_ミント・ゲウム・ビンカ・プルモナリア・ペンステモン50品種_1120.xlsx`（前の `_1119.xlsx` は残してある）。3属の試行とアスターは作り直していない（生データは前のセッションの一時フォルダにある）
- 同名の別品種への当たり違いは見つからなかった
- 同じ種のおぎはらの値（batch_07/ogihara_data.py の SIBLING）：トロリウス カルトラムの 'Lemon Queen'（Tr02）を 強（根拠は 'New Moon'・'Cheddar'）。スカビオサ コーカシカの Sc01・Sc03・Sc04 を 中（根拠は 'Perfecta' と、扱いのない 'White Queen'。どちらも 中）。【見返すこと】同じ種の値を 中 で使ったのはここが初めて（これまではどれも 強）。欧米の文献だけなら 弱。耐暑性の最後の検討で見る
- 当てなかったもの：オクロレウカの種そのもの（Sc06。おぎはらのページは 'Moon Dance' だけ）、ナガボノワレモコウ 'Bordeaux'（Sa08。同じ種のページは var. alba だけ）
- おぎはらと欧米の文献の食い違い：スカビオサ コーカシカ（おぎはら 中／MBG・NC State は高温多湿に耐えない＝弱 相当）、トロリウス チネンシス・ユーロペウス（おぎはら 強／MBG は涼しい気候の植物・暑く湿った夏を嫌う＝弱 相当）、ポレモニウム 'Apricot Delight'（おぎはら 中／MBG の種の記述は 弱 相当）
- 耐暑性 弱 の5品種：ポレモニウム カエルレウムの4品種（Pl02・Pl04・Pl05・Pl06。MBG：深南部の夏の高温多湿に耐えない）とスカビオサ 'Vivid Violet'（Sc05。MBG：高温多湿に耐えず、ゾーン7より南ではよく育たない）
- ユーザーに聞くこと・伝えること（学名の検討に出る）：(a) ポレモニウム 'Apricot Delight' は RHS・おぎはらとも carneum の品種（マスターは caeruleum）。今はカエルレウムの種の記述を当てている (b) ポレモニウム 'Blue Whirl' は RHS では viscosum の品種（マスターは caeruleum）。同じく種の記述はカエルレウムのもの (c) 'Pink Tanna' は RHS が種小名なし、おぎはらが tenuifolia、マスターと Gaißmayer が officinalis (d) 'Lemon Splash' は RHS が officinalis の品種（マスターは obtusa） (e) トロリウス 'Cheddar' は RHS では 'Taleggio' の別名とみられる (f) フィリペンデュラ 'Venusta Magnifica' は RHS では 'Venusta' の別名 (g) スカビオサ オクロレウカは RHS では Scabiosa columbaria subsp. ochroleuca (h) Gaißmayer：オクロレウカと 'Moon Dance' は短命でこぼれ種でよく増える、ウルマリアは地下茎で強く広がる
- RHS の検索は、アプリ内のブラウザーで見えない枠（iframe）を1つ作り、36件の検索を順に開いた（1回の実行は45秒で切れるが、ページの中で動き続けるので、結果を window に置いて後から読む）

## 8つ目のまとまり：タリクトラム・コレオプシス・リアトリス・リシマキア・ベロニカストラム・エリンジウム・ミスカンサス・モリニア（2026-11-20、下書きまで完了）
- 入力は batch_08/input（54品種：Th=タリクトラム8、Co=コレオプシス7、Li=リアトリス7、Ly=リシマキア7、Vs=ベロニカストラム7、Er=エリンジウム6、Mi=ミスカンサス6、Mo=モリニア6。種のまとまり 22）
- 文献：おぎはら 22ページ（27品種）、RHS 51品種、Gaißmayer 26ページ（32品種）・Jelitto 27ページ（どちらも Chrome、6秒おき）、シカゴ植物園 no28 Meadow rues から5品種（no9 Blazing stars は PDF が画像だけで読めない）
- 途中でパソコンが落ちた。生データのうち2ファイルが壊れていた（JSON として読めない）ので、消して取り直した。再起動のあと Chrome は自分で起動した（`Start-Process chrome`）。拡張機能がつながるまで数分かかった
- 確認画面：再起動のあとは Jelitto も Gaißmayer も最初の1回で確認画面が出た。どちらも操作せずに1〜数分置いたら自動で通った（別のタブで別のサイトを読みながら待つとよい）
- fetch_all.py に足したもの：rochebrunianum＝rochebruneanum、モリニアの亜種の書き方、'Lavendelturm'＝'Lavender Towers'、'Erika'＝'Erica'、'Moorhex'＝'Moorhexe'、'Floristan Violet／White' のドイツ語の書き方
- 下書き：`ClaudeWork/下書き_タリクトラム・コレオプシス・リアトリス・リシマキア・ベロニカストラム・エリンジウム・ミスカンサス・モリニア54品種_1120.xlsx`。耐暑性 強 29・中 13・弱 8・空欄 4、蒸れ耐性 強 19・中 1・弱 5・空欄 29、西日耐性 ◎6・○20・△24・×1・空欄 3。品種のページがどの文献にもないのは1品種（Ly02）
- 根拠を確認して直したこと（assemble_pilot.py。前の batch にも効く）：MBG のタリクトラムの文が当たっていなかった。「Performs poorly in hot and humid summer climates」「Intolerant of hot and humid conditions」「May grow poorly in climates with hot, humid summers」を 弱、「Some tolerance for hot and humid summer weather」を 中 に足した
  - 前の batch を作り直して比べた：batch_02〜05・07 は変化なし。batch_06 はポテンティラ3品種（Po01・Po02・Po12）の耐暑性・蒸れ耐性が 空欄 → 弱、西日耐性が 空欄 → △（MBG：ゾーン7より南の高温多湿の夏ではよく育たないことが多い）。作り直した下書きは `ClaudeWork/下書き_ポテンティラ・パニカム・アキレア・スタキス・ヒューケラ49品種_1120.xlsx`（前の `_1119.xlsx` は残してある）
  - 【気づき】言い回しの照合は、新しい属のたびに拾い漏れが見つかる。各まとまりで、MBG・NC State の hot・heat・humid・cool・summer を含む文を全部出して、当たっていない文がないかを見る（やり方は下の手順）
- 同名の別品種への当たり違いは見つからなかった
- 同じ種のおぎはらの値（batch_08/ogihara_data.py の SIBLING）：西洋クガイソウの 'Adoration'・アルビフローラム（Vs03・Vs07）を 強、ススキの5品種（Mi01・Mi02・Mi03・Mi05・Mi06）を 強。Mi05 'Purpurascens' は RHS・MBG が sinensis の品種としていない（種小名なし）ので、ススキの値を当てたのは要確認
- 耐暑性 弱 の8品種：モリニアの5品種（Mo01〜Mo05。NC State：涼しい夏の気候で最もよく育ち、暑い夏の気候ではよく育たない。おぎはらにページのある 'Variegata' は 強 で食い違いの記録つき）、コレオプシス ロゼア 'American Dream'（MBG：涼しい夏の気候が最もよい。Walters は「暑さと湿気に耐える」で食い違い）、タリクトラム 'Thundercloud'・ロチブルニエナム（MBG）
- おぎはらと欧米の文献の食い違い：タリクトラム アキレジフォリウム・デラバイ（おぎはら 中／MBG 弱 相当）、モリニア 'Variegata'（強／弱 相当）、リシマキア・西洋クガイソウ（強／中 相当）
- ユーザーに聞くこと・伝えること（学名の検討に出る）：(a) Vs01「ベロニカストラム シビリクム（クガイソウ）」は、おぎはらのクガイソウ（Veronicastrum japonicum）のページを和名で当てた。売っているのがどちらかは要確認 (b) Vs02 エゾクガイソウは、おぎはらでは Veronicastrum sachalinense (c) ススキ 'Purpurascens' は RHS・MBG とも種小名なし、'Cosmopolitan' は RHS では var. condensatus の品種 (d) コレオプシス 'Star Cluster' は RHS・おぎはらとも種小名なし（マスターは × verticillata） (e) リアトリス 'Kobold' は、おぎはらでは 'Goblin'（英語名）(f) シカゴ植物園：デラバイは試験地（日なた）で根づきが悪く冬に枯れた、'Elin' は最高評価だがうどんこ病が2年出た (g) Gaißmayer：エリンジウム ユッキフォリウムは Z7、プンクタータは地下茎で広がりはびこる

## 9つ目のまとまり：モナルダ・トラデスカンティア・スピレア・ネペタ・アネモネ・アクイレギア・セントーレア・アジュガ（2026-11-20、下書きまで完了）
- 入力は batch_09/input（51品種：Mn=モナルダ6、Td=トラデスカンティア6、Sp=スピレア5、Ne=ネペタ11、An=アネモネ6、Aq=アクイレギア6、Ce=セントーレア6、Aj=アジュガ5。種のまとまり 25）。試作28品種と重なる品種（アジュガ 'Burgundy Glow'、スピレア 'Goldflame' など）も同じ形で入れてある
- 文献：おぎはら 24ページ（29品種）、RHS 50品種、Gaißmayer 14ページ（18品種）・Jelitto 23ページ（どちらも Chrome、6秒おき）、シカゴ植物園 no12 モナルダ 2品種・no34 トラデスカンティア 5品種・no29 ネペタ 5品種・no25 アネモネ 2品種
- 確認画面：Jelitto が途中で一度確認画面に戻った（気づかずに検索を8回続けて開いてしまった）。操作せずに10分ほど別の作業をしている間に自動で通った。まとめて開く前に、最初の1ページの題名で確認画面でないことを確かめる
- 裏で動かす取得（fetch_all.py）は10分で打ち切られることがある。止まっていたら、同じコマンドをもう一度実行すれば続きから取れる。そのあと fetch_walters.py も忘れずに実行する（最後の行が done になっているか、walters の一覧が出たかを見る）
- fetch_all.py に足したもの：アネモネ（Eriocapitella）・セントーレア（Psephellus）の別の属名、シュウメイギク・ネペタ・コデマリ・トラデスカンティアの × 表記、mussinii＝racemosa、'Blue Stocking'＝'Blaustrumpf'、'Genpei'＝'Shirobana' など。'Major' をありふれた品種名に追加
- 下書き：`ClaudeWork/下書き_モナルダ・トラデスカンティア・スピレア・ネペタ・アネモネ・アクイレギア・セントーレア・アジュガ51品種_1120.xlsx`。耐暑性 強 25・中 18・弱 3・空欄 5、蒸れ耐性 中 11・弱 6・空欄 34、西日耐性 ◎4・○21・△15・×6・空欄 5。品種のページがどの文献にもない品種はなし
- 根拠を確認して直したこと（assemble_pilot.py）：MBG・NC State の暑さの文を全部出して、当たっていない文を足した。「Foliage tends to burn in hot, dry, sunny summer conditions」（シュウメイギク）、「As the heat of the summer sets in, foliage tends to decline」「the foliage will decline」（トラデスカンティア）を 中、「good heat tolerance」（シモツケ 'Goldflame'）を 強、「may be bothered by humidity」（ネペタ）を蒸れ 中。前の batch（02〜08）を作り直して比べたが、変化はなかった
- 同名の別品種への当たり違いは見つからなかった。stauden.de はモナルダの交配品種を「Monarda fistulosa '…'」、'Pink Candy' を Nepeta subsessilis と書いているが、品種名は同じ
- 同じ種のおぎはらの値（batch_09/ogihara_data.py の SIBLING）：モナルダ ディディマの4品種（Mn01〜Mn04。根拠は図鑑の色別の「Monarda didyma×hybridus」4ページ。品種名のあるページではないので、ほかより根拠が弱い）、トラデスカンティア アンダーソニアナの Td01・Td02、シモツケの Sp01・Sp03 を 強、オダマキ 'Bordeaux Barlow'（Aq05）を 中
- 耐暑性 弱 の3品種：ネペタ ムッシーニアイ（Ne05）・'Alba'（Ne06）・'Blue Wonder'（Ne09）。MBG の文は「Somewhat intolerant of the heat and humidity of the deep South（深南部の高温多湿にはやや弱い）」で、「やや」が付く。同じ文のある 'Six Hills Giant'・'Walker's Low' は、おぎはらにページがあるので 強（食い違いの記録つき）。最後の検討で見る
- おぎはらと欧米の文献の食い違い：セントーレア ディールバータ（おぎはら 強／MBG：涼しい夏の気候を好み、ゾーン7より南ではよく育たない＝弱 相当）、ネペタ（上のとおり）、モナルダ ディディマ・トラデスカンティア（強／中 相当）
- 耐暑性が空欄の5品種：An05・Aq02・Ce02・Mn05・Ne08（暑さの記述がどの文献にもない）
- ユーザーに聞くこと・伝えること（学名の検討に出る）：(a) ネペタは文献ごとに種の扱いが違う。'Felix' は RHS・Jelitto とも racemosa（マスターは × faassenii）、'Blue Wonder' は RHS が × faassenii（マスターは racemosa）、'Walker's Low' は おぎはらが × faassenii、'Pink Candy' は RHS が種小名なし・おぎはらが hybrida（マスターは nervosa）、ムッシーニアイは RHS・Jelitto とも racemosa が正名 (b) モナルダ 'Blue Stocking'・'Fireball'・'Panorama Red Shades' は RHS では種小名なし、'Bee-Bright' は流通名で品種名は 'Monbebr' (c) 'Magic Carpet'・'Junior Walker'・'Black Scallop' も RHS では流通名（品種名は 'Walbuma'・'Novanepjun'・'Binblasca'） (d) アジュガ 'Chocolate Chip' は、おぎはらが Ajuga tenorii、RHS は reptans 'Chocolate Chip' をシノニム扱い (e) スピレア 'Goldflame' は、おぎはらが × bumalda（RHS は japonica が正名） (f) トラデスカンティアは RHS がどれも Andersoniana Group (g) シカゴ植物園：トラデスカンティア 'Little Doll' は葉の斑点病が最も重い区分、'Red Cloud' は勢いが強いが咲き始めに倒れやすい、モナルダ フィッツローサはうどんこ病に very poor、シュウメイギク 'Pamina' は冬の傷みで株を失い再試験

## 10個目のまとまり：ダイアンサス・ヘレニウム・ミューレンベルギア・アルメリア・ユーフォルビア・ヘリアンセマム・クニフォフィア・ペニセタム・ルドベキア・タイム（2026-11-20、下書きまで完了）
- 入力は batch_10/input（50品種：Di=ダイアンサス5、Hl=ヘレニウム5、Mu=ミューレンベルギア5、Ar=アルメリア4、Eu=ユーフォルビア4、Hm=ヘリアンセマム4、Kn=クニフォフィア4、Pn=ペニセタム4、Ru=ルドベキア4、Ty=タイム11。種のまとまり 30）
- 文献：おぎはら 17ページ（19品種）、RHS 44品種、Gaißmayer 16ページ（20品種）・Jelitto 23ページ（どちらも Chrome、6秒おき）。シカゴ植物園は no8 Rudbeckia だけ号があるが、PDF が画像だけで読めなかった
- 【未実施】Gaißmayer でミューレンベルギアを検索し忘れた（掲載があるかは未確認）。Jelitto の 'Goldsturm' のページは本文が長く、表の後半（ゾーン・高さ・土）を読み取れなかった
- 確認画面：Gaißmayer が最初の検索で確認画面になったが、操作せずに Jelitto を先に読んでいる間に自動で通った。Jelitto は出なかった
- fetch_all.py に足したもの：ペニセタムの別の属名（Cenchrus）、polychroma＝epithymoides、タイムの × 表記と Coccineus Group、'Mardi gras'＝'Helbro' など。'Aureus'・'Coccineus'・'Rubrifolia'・'French' をありふれた品種名に追加
- 下書き：`ClaudeWork/下書き_ダイアンサス・ヘレニウム・ミューレンベルギア・アルメリア・ユーフォルビア・ヘリアンセマム・クニフォフィア・ペニセタム・ルドベキア・タイム50品種_1120.xlsx`。耐暑性 強 21・中 4・弱 3・空欄 22、蒸れ耐性 強 1・中 11・空欄 38、西日耐性 ◎3・○11・△15・空欄 21。品種のページがどの文献にもないのは6品種（Ar01・Ar04・Di05・Eu01・Hm02・Kn01）
- 【このまとまりの特徴】耐暑性の空欄が22品種と多い。タイム9品種（ロンギカウリスとシトリオドラス以外）、アルメリア3品種、ペニセタム2品種、ミューレンベルギア2品種、ヘレニウム2品種など。欧米の文献に暑さの記述がなく、おぎはらにもページがない。ミューレンベルギア デュモーサ・リジェンスは MBG・stauden.de にもほとんど記述がなく、空欄の項目が特に多い（属の平均で12.6項目）
- 根拠を確認して直したこと（assemble_pilot.py）：MBG・NC State の暑さの文を全部出して、当たっていない文を足した。「drought- and heat-tolerant」「bears up under hot, humid summers」（ルドベキア フルギダ）を 強、「Light shade is helpful if summers are hot」（クニフォフィア）「may show some stress in hot and humid summers」（ユーフォルビア アミグダロイデス）を 中。前の batch（02〜09）を作り直して比べたが、変化はなかった
- 同名の別品種への当たり違いは見つからなかった。stauden.de は 'Blue Hills' を Dianthus gratianopolitanus、'Ice Queen' を Kniphofia uvaria、'Peter Davis' を Thymus richardii、ヘレニウムの交配品種を Helenium x cultorum と書いている
- 同じ種のおぎはらの値（batch_10/ogihara_data.py の SIBLING）：ヘレニウム オータムナーレの 'Salsa'・'Sombrero' を 強（根拠は 'Tie Dye' と、同じマリアッチのシリーズの 'Siesta'。図鑑は種小名を書いていないので、ほかより根拠が弱い）
- 耐暑性 弱 の3品種：ヘリアンセマム（Hm01・Hm03・Hm04。MBG：涼しい夏と暖かい冬を好む）
- おぎはらと欧米の文献の食い違い：ダイアンサス デルトイデス・ユーフォルビア ポリクロマ・クニフォフィア（おぎはら 強／欧米は「暑い夏の気候では午後の日陰」などで 中 相当）
- ユーザーに聞くこと・伝えること（学名の検討に出る）：(a) ユーフォルビア ポリクロマは RHS・Jelitto・Gaißmayer とも epithymoides が正名 (b) 'Mardi Gras'・'Undaunted' は RHS では流通名（品種名は 'Helbro'・'Pund01s'） (c) タイム 'Coccineus' は RHS では Coccineus Group、'Magic Carpet'・'Cheviot'・'Tie Dye' は RHS が種小名なし、フレンチタイムは RHS が「Thymus vulgaris French, summer」 (d) ルドベキア 'Goldsturm'・'Little Goldstar' は、おぎはら・Gaißmayer が var. sullivantii の品種（RHS は 'Little Goldstar' に変種名を付けない） (e) ペニセタム 'Fairy Tails' は、おぎはら・stauden.de が orientale の品種（マスターは種小名なし） (f) ダイアンサス sp. 'Lion Rock'・ヘリアンセマム 'St Mary's'・'Dazzler'・クニフォフィア 'Bees' Lemon'・ペニセタム 'Black Beauty'・ユーフォルビア 'Golden Glory' は RHS で見つからなかった (g) Gaißmayer：クニフォフィア 'Ice Queen' とレモンタイム 'Aureus' は Z7（'Aureus' は「いつも冬越しできるとは限らない」）、カシュジアノーラムは短命だがこぼれ種でよく増える、キパリシアスは地下茎で強く広がる（Jelitto も「はびこる」と注意）

## 11個目のまとまり：ジギタリス・プリムラ・ユーパトリウム・ベルゲニア・カラマグロスティス・デスカンプシア・フクシア・アイリス・ロニセラ（2026-11-20、下書きまで完了）
- 入力は batch_11/input（53品種：Dg=ジギタリス10、Pr=プリムラ7、Ep=ユーパトリウム6、Bg=ベルゲニア5、Cg=カラマグロスティス5、Ds=デスカンプシア5、Fu=フクシア5、Ir=アイリス5、Lo=ロニセラ5。種のまとまり 32）
- 文献：おぎはら 24ページ（24品種。デスカンプシア・フクシア・アイリスは掲載なし）、RHS 50品種、Gaißmayer 15ページ（17品種）・Jelitto 31ページ（38品種。どちらも Chrome、6秒おき）、シカゴ植物園 no37 Joe-Pye weeds から3品種（セレスチナム・'Ivory Towers'・'Gateway'）
- 確認画面：Gaißmayer も Jelitto も最初の1ページで確認画面が出た。どちらも操作せずに置き、1〜3分後に自動で通った（その間は RHS の結果を読んでいた）。そのあとは出なかった
- Jelitto の商品ページのアドレスは、商品ごとに置き場所が違う（/Seed/Perennials/…、/Seed/Ornamental+Grasses/…、/Jelitto+Perennial+Seeds/New+Varieties/… など）。名前から作ると Error になるものがあるので、検索結果のリンクから拾う（JavaScript の結果に = ? & を含めると遮断されるので、pathname だけを返す）
- fetch_all.py に足したもの：ユーパトリウムの別の属名（Eutrochium・Conoclinium）、デスカンプシア フレクシオーサ＝Avenella、アクティフローラ・マートネンシス・ロニセラ3種の × 表記、'Millers Crimson'＝'Miller's Crimson'、'Appleblossom'＝'Apple Blossom'、'Goldtau'＝'Golden Dew'、'Snow Time'＝'Snowtime'、'Apricot'＝'Sutton's Apricot' など
- 下書き：`ClaudeWork/下書き_ジギタリス・プリムラ・ユーパトリウム・ベルゲニア・カラマグロスティス・デスカンプシア・フクシア・アイリス・ロニセラ53品種_1120.xlsx`。耐暑性 強 15・中 20・弱 3・空欄 15、蒸れ耐性 中 6・弱 1・空欄 46、西日耐性 ○10・△15・×21・空欄 7。品種のページがどの文献にもないのは1品種（Fu02 'Enstone'）。学名の検討は27品種
- 根拠を確認して直したこと（assemble_pilot.py。前の batch にも効く）
  - 読む欄を増やした：MBG の「Uses」（GardenUses）、NC State の「Flower Description」「Leaf Description」。暑さの文がここにだけ書かれていることがあった
  - 弱 に足した：「Plants dislike high heat and humidity」（デスカンプシア フレクシオーサ。蒸れだけ 弱 で耐暑性が空欄だった）、「shrub for cool summer climates」（ロニセラ ペリクリメナム）
  - 中 に足した：「Flowering may decline and foliage may wilt in the heat of the summer」（フクシア）、「protect from hot afternoon sun」（シベリアアヤメ）、「foliage typically depreciates in the heat」（プリムラ ベリス）
  - 「more tolerant of heat and humidity than other types of primroses」のような、ほかとの比較は 強 にしない（「better than most」と同じ扱いで 中）。プリムラ ベリスの蒸れ耐性が 強 → 中
  - カラマグロスティスを GENUS_MBG_SKIP に追加（MBG の品種ページは × アクティフローラだけ。エピジジョスに当てない）。Cg05 の耐暑性・USDA は空欄に戻った
  - フクシアの「It does best in cool moist conditions with some shade」は、気候ではなく場所の条件とも読めるので当てていない（当てれば 弱）。最後の検討で見る
  - 前の batch（02〜10）を作り直して比べたが、変化はなかった
- 同名の別品種への当たり違いは見つからなかった。stauden.de は 'Gateway'・'Red Dwarf'・'Ivory Towers' を Eupatorium fistulosum、'Hawkshead' を Fuchsia magellanica var. gracilis と書いているが、品種名は同じ
- 同じ種のおぎはらの値（batch_11/ogihara_data.py の SIBLING）：ジギタリス プルプレアの 'Elsie Kelsey'・'Excelsior'（Dg06・Dg07）を 中（根拠の5ページがどれも 中）、ユーパトリウム マクラツム 'Gateway'（Ep05）・カラマグロスティス 'Avalanche'（Cg01）・ロニセラ 'Honey Baby'（Lo03）を 強。【見返すこと】同じ種の値を 中 で使ったのは batch_07 のスカビオサに続いて2回目
- 当てなかったもの：ベルゲニア コーディフォリアの Bg01〜Bg03（同じ種のページが 'Snow Time' の1つだけ。図鑑の「実生系」は Bergenia ×Hybrids）
- 耐暑性 弱 の3品種：デスカンプシア フレクシオーサ（Ds05。MBG：高温多湿を嫌い、ゾーン7より南ではよく育たないことが多い。蒸れ耐性も 弱）、プリムラ 'Primadiente Rose'（Pr01。Walters：涼しい夏の地域が最もよい）、プリムラ 'Green Lace'（Pr06。NC State のポリアンサの記述：涼しい気候が要る）
- おぎはらと欧米の文献の食い違い：ロニセラ ペリクリメナム（おぎはら 強／MBG：涼しい夏の気候向きのつる＝弱 相当）、カラマグロスティス・ユーパトリウム フィスツローサム・マクラツム（強／暑い夏の気候では午後の日陰、土が乾くと葉が焼ける＝中 相当）
- 耐暑性が空欄の15品種：ベルゲニア4（Bg01〜Bg03・Bg05）、デスカンプシア セスピトーサ4（Ds01〜Ds04）、アイリス4（Ir01〜Ir04）、Cg05・Ep01・Pr02。欧米の文献に暑さの記述がなく、おぎはらにもページがない。ベルゲニア エメイエンシス・ユーパトリウム アルブム・アイリスの4品種は、ほかの項目も空欄が多い
- ユーザーに聞くこと・伝えること（学名の検討に出る）：(a) 'Elsie Kelsey' は Jelitto が 'Pam's Choice' の別名として載せている（RHS は 'Elsie Kelsey' を独立した名前、種小名なしで掲載）。Jelitto の 'Pam's Choice' のページを当てたが、同じ品種として扱ってよいかは要確認 (b) 北米のユーパトリウムは RHS では Eutrochium（'Gateway'・'Red Dwarf'・'Ivory Towers'）と Conoclinium（セレスチナム）。'Pink Frost' は、おぎはらが Eupatorium × arakianum（サワフジバカマ）、RHS・Walters が fortunei (c) フクシア 'Genii'・'Hawkshead'、ロニセラ 'Honey Baby'、プリムラ 'Primadiente Rose'・'Green Lace' は RHS が種小名なし。'Enstone' は RHS が var. molinae の品種。'Variegata' は RHS に2つあり（var. gracilis と var. macrostema）、どちらを売っているかは要確認 (d) ロニセラ 'Harlequin' は RHS では流通名（品種名は 'Sherlite'）。ジギタリス 'Apricot' は RHS では 'Sutton's Apricot' が正名、'Excelsior' は Excelsior Group (e) アイリス 'Red Flare' は RHS でシベリアアヤメの品種として確かめられなかった（同名の丈の高いジャーマンアイリスがある）。'Black Form' は RHS では「黒花の系統」 (f) Bg02「ニューウィンターフラワリング Hybs」は Jelitto の 'New Hybrids' [New Winterflowering Hybrids]（実生の交配系統）。'Redstart' は Jelitto では 'Rotblum' [Red Beauty, Red Start] (g) Ep01「ユーパトリウム 白花」は学名が Eupatorium album。売っているものがこの種か（フジバカマの白花などではないか）は要確認 (h) Jelitto が発表した品種（育種会社と同じ扱いにできる）：'Monstrosa Purple'・'Monstrosa White'（2022）、'Blue Selection'（1994）、'Primadiente Rose'（2014）、'Ivory Towers'（2010）、'Rotblum'（1978）、'Snowtime'（2023）、'Pixie Fountain'（2010） (i) シカゴ植物園：'Gateway'・'Ivory Towers' はうどんこ病に poor、セレスチナムは冬にほとんど枯れたように見えても地下茎と実生で戻った (j) Gaißmayer：フクシア 'Hawkshead' は Z7・春植えを勧める、ジギタリス プルプレアは二年草でこぼれ種で続く・石灰の多い土ではだめ

## 12個目のまとまり：シレネ・ゲンチアナ・プルサティラ・ティアレラ・アルケミラ・アンドロポゴン・ヘデラ・リグラリア・パトリニア・プルネラ・トリキルティス・ハイドランジア・アストランティア（2026-11-20、下書きまで完了）
- 入力は batch_12/input（51品種：Si=シレネ5、Gn=ゲンチアナ4、Ps=プルサティラ4、Ti=ティアレラ4、Al=アルケミラ3、Ad=アンドロポゴン3、Hd=ヘデラ3、Lg=リグラリア3、Pt=パトリニア3、Pv=プルネラ3、Tc=トリキルティス3、Hy=ハイドランジア7、As=アストランティア6。種のまとまり 28）。試作28品種と重なる品種（アルケミラ、オミナエシ、ホトトギス、エゾアジサイなど）も同じ形で入れてある
- 文献：おぎはら 21ページ（24品種。ゲンチアナ・プルサティラ・ヘデラ・ホトトギスは掲載なし）、RHS 44品種、Gaißmayer 15ページ（23品種）・Jelitto 27ページ（34品種。どちらも Chrome、6秒おき）、シカゴ植物園 no24 Lady's mantles から2品種・no16 Toad lilies から1品種（'Tojen'。総合評価の星は記号が落ちて読めなかった）
- 確認画面：Gaißmayer も Jelitto も、このまとまりの最初の1ページでまた確認画面が出た（前のまとまりから1時間ほどあいていた）。どちらも操作せずに置き、1〜2分で自動で通った。そのあとは出なかった
- fetch_all.py に足したもの：アンドロポゴン スコパリウス＝Schizachyrium scoparium、シレネ ユニフローラ＝Silene maritima、ティアレラ ウェリー＝cordifolia var. collina、ヤマアジサイ＝Hydrangea macrophylla subsp. serrata、'Togen'＝'Tojen'、'Robin Whitebreast'＝'Weißkehlchen'、'Sugar and Spice'＝'Sugar & Spice'。'Grandiflora'・'Albiflora' をありふれた品種名に追加
- 下書き：`ClaudeWork/下書き_シレネ・ゲンチアナ・プルサティラ・ティアレラ・アルケミラ・アンドロポゴン・ヘデラ・リグラリア・パトリニア・プルネラ・トリキルティス・ハイドランジア・アストランティア51品種_1120.xlsx`。耐暑性 強 13・中 22・弱 7・空欄 9、蒸れ耐性 強 5・弱 1・空欄 45、西日耐性 ○12・△7・×25・空欄 7。品種のページがどの文献にもないのは8品種（As04・Hd01・Hd03・Hy02・Hy04・Hy07・Pt02・Si01。RHS に名前だけの登録があるものを含む）。学名の検討は27品種
- 根拠を確認して直したこと（assemble_pilot.py。前の batch にも効く）
  - 弱 に足した：「Best performance occurs in cool summer climates」（アストランティア）、「Best performance in climates with cool summers」（リグラリア デンタータ）、「Best performance occurs in cool climates」（プルサティラ）、「prefers cool growing conditions」（ヤマアジサイ・エゾアジサイ。試作の P25 エゾアジサイと同じ 弱 になった）
  - 中 に足した：「protection … from hot summer temperatures」（ヘデラ）
  - 強 に足した：「Tolerates high heat and humidity」（アンドロポゴン スコパリウス）、「Tolerant of hot and humid summers」（オミナエシ・オトコエシ。試作の P19 と同じ 強・蒸れ 強 になった）、「tolerates, heat, humidity」（ノリウツギ）
  - 前の batch を作り直して比べた：batch_02〜04・07・09〜11 は変化なし。batch_05 はビンカ6品種の「欧米の文献だけなら」が 空欄 → 強（NC State：It tolerates high heat。耐暑性の値は、おぎはらの 強 のままで変わらない）。batch_06 はポテンティラ × トンゲイ（Po10）の耐暑性が 空欄 → 強、西日耐性が 空欄 → ◎（Walters：Tolerant of hot, dry locations once established）。batch_08 はエリンジウム プラナムの2品種（Er02・Er03）の「欧米の文献だけなら」が 空欄 → 強（Walters：Tolerant of hot, dry sites。値は おぎはらの 中 のままで、食い違いの記録が付いた）。作り直した下書きは `ClaudeWork/下書き_ミント…50品種_1120b.xlsx`・`下書き_ポテンティラ…49品種_1120b.xlsx`・`下書き_タリクトラム…54品種_1120b.xlsx`（前のものは残してある）
- 同名の別品種への当たり違いは見つからなかった。stauden.de はティアレラの交配品種を Tiarella laciniata、'Tojen' を Tricyrtis hirta と書いているが、品種名は同じ
- 同じ種のおぎはらの値（batch_12/ogihara_data.py の SIBLING）：アンドロポゴン ジェラルディ（Ad01。種そのもの。根拠は 'Red October'・'Blackhawks'）・スコパリウス 'Blaze'（Ad02）、リグラリア デンタータの2品種（Lg01・Lg02）、ノリウツギ 'Aurea'（Hy02）を 強、シレネ ユニフローラ 'Robin Whitebreast'（Si03）を 中
- Hy03 は、マスターの商品名に「ミナヅキ」とあるので、おぎはらの ノリウツギ ‘ミナヅキ’ を品種のページとして当てた（マスターの学名は 'Grandiflora'）
- 当てなかったもの：ヤマアジサイ 'Cheju-do' とエゾアジサイ2品種（おぎはらのヤマアジサイの品種はどれも 強 だが、エゾアジサイは変種が違うので、同じ種の値を使っていない。欧米の文献から 弱）、おぎはらの「菊葉大輪ウツボグサ」は Prunella grandiflora の種のページとして Pv01・Pv02 に当てた（葉の切れ込む系統の名前。要確認）
- 耐暑性 弱 の7品種：プルサティラ4品種（Ps01〜Ps04。MBG：涼しい気候で最もよく育つ）、ヤマアジサイ 'Cheju-do'・エゾアジサイ2品種（Hy04・Hy06・Hy07。NC State：涼しい環境を好む）
- おぎはらと欧米の文献の食い違い：アストランティア6品種（おぎはら 中／MBG：夜温が 70°F を下回る涼しい夏の気候で最もよく育つ＝弱 相当）、リグラリア デンタータ（強／涼しい夏の気候で最もよい＝弱 相当）・プルツェワルスキー（中／弱 相当。蒸れ耐性も 弱）、ヤマアジサイ 'Kurenai'（強／弱 相当）、アナベル・ノリウツギ（強／中 相当）、シレネ 'Robin Whitebreast'（中／MBG：涼しい気候を好む＝弱 相当）
- 耐暑性が空欄の9品種：ゲンチアナ4品種（暑さの記述がどの文献にもない。ほかの項目も空欄が多く、属の平均で15項目）、アルケミラ サクサティリス・'Gold Strike'、プルネラ ブルガリス、'Tojen'、ティアレラ 'Lacquer Leaf'
- ユーザーに聞くこと・伝えること（学名の検討に出る）：(a) アンドロポゴン スコパリウスは RHS・Gaißmayer・おぎはらとも Schizachyrium scoparium (b) ヘデラ 'Spetchley' は RHS では Hedera hibernica の品種（helix 'Spetchley' はシノニム扱い）、'Baltica' は RHS では品種名 (c) アストランティア 'Hadspen Blood'・'Roma' は RHS が種小名なし (d) プルサティラは Jelitto が 'Pearl Bells'＝'Perlen Glocke'、'Rose Bells'＝'Rosen Glocke'、'White Bells'＝'Alba' としている（RHS は 'White Bells' を未確定の別の名前として載せている） (e) シレネ 'Robin Whitebreast' は、RHS が八重咲き (d)、Jelitto の 'Weißkehlchen' [Robin White Breast] は一重（Flower: single）。売っているものがどちらかは要確認。Si05 は商品名が「'ダブル'（スワンレイク）」で、学名は 'Swan Lake' (f) ゲンチアナ 'Nikita' は Jelitto が種（dahurica）の流通名としている。'Blue Herald' は RHS では 'Blauer Herold' (g) エゾアジサイは RHS では Hydrangea serrata subsp. yezoensis（マスターのつづりは yesoensis）(h) ホトトギス 'Lightning Strike' は RHS・MBG とも種小名なし（マスターは hirta）、'Togen' は 'Tojen' が普通のつづり (i) ティアレラ ウェリーは Jelitto が cordifolia ssp. collina の別名を併記 (j) Jelitto が発表した品種：'Blue Herald'（1989）・'Blue Cross'（2009）・'Bella Alpinella'（2018）・'Perlen Glocke'（2010）・'Rosen Glocke'（2014） (k) シカゴ植物園：アルケミラ サクサティリスは試験の途中で急に衰え、冬に株元が傷んだ (l) Gaißmayer：プルネラ ブルガリスは非常によく広がる、ホトトギスは春植えと冬の落ち葉の覆いを勧める、アルケミラ モリスは花後に地際で切るとこぼれ種を防げる

## 13個目のまとまり：ガウラ・ジプソフィラ・アシリウム・コルヌス・フェスツーカ・ハコネクロア・パパベル・アンジェリカ・エノテラ・バーバスカム・バーベナ・アンスリスクス・アルテミシア・カラミンサ（2026-11-20、下書きまで完了）
- 入力は batch_13/input（51品種：Ga=ガウラ6、Gy=ジプソフィラ6、At=アシリウム5、Cn=コルヌス4、Fe=フェスツーカ4、Hk=ハコネクロア4、Pp=パパベル4、Ag=アンジェリカ3、Oe=エノテラ3、Vb=バーバスカム3、Vn=バーベナ3、Ah=アンスリスクス2、Am=アルテミシア2、Ca=カラミンサ2。種のまとまり 26）。試作28品種と重なる品種（アサギリソウ、コルヌス 'Sibirica' など）も同じ形で入れてある
- 文献：おぎはら 27ページ（36品種。ジプソフィラ・コルヌスは掲載なし）、RHS 49品種、Gaißmayer 21ページ（28品種）・Jelitto 28ページ（34品種。どちらも Chrome、6〜7秒おき）、シカゴ植物園 no39 シダ 5品種・no26 エノテラ 2品種・no19 アルテミシア 1品種
- 確認画面：Gaißmayer も Jelitto も最初の1ページで確認画面が出た。どちらも操作せずに置き、1〜2分で自動で通った（その間はもう一方のサイトと RHS を進めた）。そのあとは出なかった
- 【Chrome の道具の注意】1回の指示に20ページ（約2分半）を詰めたら、道具の返事が時間切れになった。ページは裏で開かれ続けたが結果が返らず、15ページを読み直した。1回の指示は6〜7ページ（1分以内）までにする。時間切れのあとは、前の指示がまだ動いていることがあるので、30秒ほど待ってから次を出す
- 読み方の工夫（次も使える）：検索結果のリンクの pathname を sessionStorage に入れておき、商品ページでは「読む → 次のページへ移る」を1つの JavaScript で行う（結果に ? = & を入れない。Gaißmayer は番号、Jelitto は名前の先頭60字を鍵にした）
- fetch_all.py に足したもの：ガウラ＝Oenothera lindheimeri、カラミンサ＝Clinopodium、フェスツーカ ガウティエリ＝scoparia、エノテラ マクロカルパ＝missouriensis、コルヌス セリセア＝stolonifera、オリエンタルポピー＝Papaver (Oriental Group)、ニシキシダの var. pictum、'Princess Victoria Louise'＝'Prinzessin Victoria Louise'、'Janlim'＝'Oriental Limelight'、'Snowflake'＝'Schneeflocke'、'All Gold'＝'Allgold'、'Brilliant'＝'Brillant' など。'Elegantissima'・'Brilliant'・'Snowflake'・'Metallicum' をありふれた品種名に追加
- 下書き：`ClaudeWork/下書き_ガウラ・ジプソフィラ・アシリウム・コルヌス・フェスツーカ・ハコネクロア・パパベル・アンジェリカ・エノテラ・バーバスカム・バーベナ・アンスリスクス・アルテミシア・カラミンサ51品種_1120.xlsx`。耐暑性 強 26・中 9・弱 4・空欄 12、蒸れ耐性 強 7・中 1・弱 6・空欄 37、西日耐性 ◎3・○21・△7・×9・空欄 11。品種のページがどの文献にもないのは4品種（Fe04・Ga06・Gy03・Gy06）。学名の検討は27品種
- 根拠を確認して直したこと（assemble_pilot.py。前の batch にも効く）
  - 弱 に足した：「Short-lived ornamental grass that does not tolerate hot or humid conditions」（フェスツーカ グラウカ。蒸れも 弱）、「They generally don't do well in heat and humidity or south of zone 7」（オリエンタルポピー。蒸れも 弱）、「Plants generally do not perform well in the deep South below USDA Zone 7」（カラミンサ ネペタ）
  - 強 に足した：「Tolerates summer heat and humidity」（エノテラ マクロカルパ）
  - 蒸れ 中 に足した：「General foliage decline often occurs in high humidity summer climates」（アルテミシア ブルガリス 'Janlim'）
  - フェスツーカを GENUS_MBG_SKIP に追加（MBG の品種ページはグラウカだけ。ガウティエリ・アイダホエンシスに当てない）
  - 前の batch（02〜12）を作り直して比べた：変わったのは batch_09 のシュウメイギク 'Honorine Jobert'（An03）だけで、耐暑性が 中 → 弱（MBG：Plants do not perform well in the deep South (south of USDA Zone 7)）。作り直した下書きは `ClaudeWork/下書き_モナルダ…51品種_1120b.xlsx`（前の `_1120.xlsx` は残してある）
- 同名の別品種への当たり違いは見つからなかった。stauden.de は 'Elijah Blue' を Festuca cinerea、ニシキシダを Athyrium niponicum '…'（var. pictum なし）と書いているが、品種名は同じ
- 同じ種のおぎはらの値（batch_13/ogihara_data.py の SIBLING）：バーベナ ハスタータの種そのもの（Vn02）を 強（根拠は 'Blue Spires'・'Pink Spires'・'White Spires'）
- 種のページを当てたもの（おぎはら）：ガウラの5品種（白蝶草のページ。図鑑のガウラ8ページはどれも 強）、フェスツーカ グラウカの2品種、カラミンサ 'Blue Cloud'（図鑑の「カラミンサ(ピンク)」が Calamintha nepeta）、ニシキシダ 'Metallicum'（図鑑の 'Pictum'。RHS は 'Metallicum' を var. pictum のシノニムとしている）
- フウチソウの4商品は、図鑑の4ページ（緑葉・紅・黄金・斑入り。学名はどれも Hakonechloa macra）を、マスターの商品名と照らして当てた。Hk01（緑葉）と Hk02（ベニフウチソウ）はマスターの学名が同じ Hakonechloa macra
- 当てなかったもの：アンジェリカ パキカルパ（図鑑は 'Summer Delight' の1ページだけ）・'Ebony'、バーバスカム 'Sixteen Candles'、エノテラ スペシオーサ 'Woodside White'（どれも同じ種のページが1つだけ）
- 耐暑性 弱 の4品種：オリエンタルポピー4品種（おぎはら：高温多湿に弱く暖地では夏越しが難しい。NC State も同じ向きで、食い違いなし）
- おぎはらと欧米の文献の食い違い：フウチソウ（おぎはら 強／MBG・NC State：涼しい夏の気候で最もよく育つ、米国南部の暑い夏には耐えないことがある＝弱 相当。'Aureola' だけ 中 相当）、フェスツーカ グラウカ（強／NC State：暑さや湿気に耐えない＝弱 相当。蒸れ耐性は 弱）、カラミンサ 'Blue Cloud'（強／MBG：ゾーン7より南の深南部ではよく育たない＝弱 相当）、フェスツーカ ガウティエリ（強／なし）
- 耐暑性が空欄の12品種：ジプソフィラ5品種（Gy01〜Gy04・Gy06。'Rosea' だけ Walters の「暑さに耐える」で 強）、アンジェリカ パキカルパ・'Ebony'、アルテミシア 'Janlim'、フェスツーカ アイダホエンシス、エノテラ 'Silver Wings'・'Woodside White'、バーバスカム 'Sixteen Candles'。フェスツーカ アイダホエンシスは、ほかの項目も空欄が多い
- ユーザーに聞くこと・伝えること（学名の検討に出る）：(a) ガウラは RHS では Oenothera lindheimeri（Jelitto も OENOTHERA を併記）。'Sunset Dreams'・'White Fountain' は RHS では名前だけのシノニム扱い、'Yuubae'（夕映え）は欧米の文献に名前がない (b) オリエンタルポピーは RHS では Papaver (Oriental Group)。Pp02 は 'Prinzessin Victoria Louise' がもとの名前（おぎはら：実生につき色幅がある） (c) カーペットカスミソウは RHS では Acanthophyllum cerastioides (d) Gy03 は商品名が「ジプソフィラ ローザス 'コーンヘッド'」、学名が Gypsophila paniculata 'Conehead'。'Conehead' はどの文献にも名前がなく、種の記述だけを当てている。売っているものが何かは要確認 (e) Gy06 レペンス 'White' は品種名ではなく白花の意味とみられる（RHS は「Gypsophila repens white-flowered」）(f) 'Snowflake' は RHS・Gaißmayer・Jelitto とも 'Schneeflocke'（種子で殖やす品種で、八重は6割ほど） (g) ニシキシダ 'Metallicum' は RHS では var. pictum のシノニム（変種そのもの） (h) アルテミシア 'Janlim' は RHS が種小名なし（Oriental Limelight は流通名）。RHS・MBG とも「広がりすぎることがある」と注意 (i) カラミンサ 'Blue Cloud' は RHS・Jelitto とも subsp. nepeta の品種。Jelitto は種子の系統（'Blue Cloud Strain'） (j) Hk02 ベニフウチソウに RHS の 'Beni-kaze' を当てた。同じ系統かは要確認 (k) フェスツーカ ガウティエリは、商品名が「スコパリア（ホビット）」。Jelitto は FESTUCA gautieri (scoparia) [Hobbit]、RHS には 'Hobbit' の名前だけの登録（未確定）がある。'Elijah Blue' は stauden.de・Gaißmayer が Festuca cinerea の交配品種 (l) 'Wedding Candles' は Jelitto が chaixii f. album の品種（RHS は f. album を付けない）。バーバスカムの3品種とガウラ 'Summer Breeze'・'Royal Wedding'・エノテラ 'Silver Wings' は Jelitto が発表した品種 (m) Gaißmayer：ガウラは Z7・「確実に冬越しするとは言えない、冬の過湿を避ける、春植えを勧める」、バーベナ ボナリエンシスは Z8・短命、フウチソウは Z7・春植えを勧める、アンジェリカ 'Vicar's Mead'・アンスリスクス 'Ravenswing' はふつう二年草（'Ravenswing' はこぼれ種でよく増える）、アサギリソウは冬の過湿を避ける (n) シカゴ植物園：ニシキシダ 'Burgundy Lace'・'Silver Falls' は午後の日が当たる区で乾燥・日の当たりすぎの傷みが2年以上、'Pewter Lace' は日かげで傷みなし（最高評価）。アサギリソウは晩夏に蒸れで株の中心があいた年が2年。エノテラ 'Woodside White' は冬に株元が傷んだ年が2年（すぐ回復）、スペシオーサの品種は地下茎で速く広がる

## 14個目のまとまり：チャスマンティウム・ケロネ・エキノプス・エリムス・エリゲロン・ガリウム・グレコマ・カリメリス・ラベンダー・レウカンセマム・リスラム・パキサンドラ・フロミス・サギナ・サポナリア・センペルビブム・シルフィウム・スティパ・シンフィオトリクム・ビバーナム・ユッカ・ヒューケレラ・トリフォリウム（2026-11-20、下書きまで完了）
- 入力は batch_14/input（51品種・23属：Ch=チャスマンティウム2、Cl=ケロネ2、Ec=エキノプス2、El=エリムス2、Eg=エリゲロン2、Gm=ガリウム2、Gc=グレコマ2、Ka=カリメリス2、La=ラベンダー2、Le=レウカンセマム2、Lt=リスラム2、Pc=パキサンドラ2、Ph=フロミス2、Sg=サギナ2、Sn=サポナリア2、Sm=センペルビブム2、Sl=シルフィウム2、Su=スティパ2、Sy=シンフィオトリクム2、Vu=ビバーナム2、Yu=ユッカ2、Hr=ヒューケレラ3、Tf=トリフォリウム6。種のまとまり 35）
- make_input.py を直した：学名が「× Heucherella …」のように × で始まる商品は、× を外した語を属とする（ヒューケレラは × のあるもの2つと、ないもの1つで3品種だった）。'Pink Jewel'('Rosa Juwel') のように別名が続く書き方は、最初の名前だけを品種名にする
- 文献：おぎはら 22ページ（31品種）、RHS 47品種、Gaißmayer 23ページ（33品種）・Jelitto 31ページ（40品種。どちらも Chrome、7秒おき、1回の指示は6ページまで）、シカゴ植物園 no30 レウカンセマム 1品種（'Snowdrift'）・no36 アスター 1品種（'Jenny'）
- 確認画面：Gaißmayer も Jelitto も、このまとまりの最初の1ページでまた確認画面が出た（前のまとまりから30分ほどあいていた）。どちらも操作せずに置き、RHS の結果を確かめている間（3分ほど）に自動で通った。そのあとは出なかった
- fetch_all.py に足したもの：シンフィオトリクム＝Aster、スティパ＝Nassella・Jarava、カリメリス インシサ＝Aster incisus、フロミス トゥベローサ＝Phlomoides、エリムス マジェラニカス＝Agropyron、クルマバソウ＝Asperula odorata、シャスターデージーの × 表記、'Pink Jewel'＝'Rosa Juwel'、'Broadway Lights'＝'Leumayel' など。'Atropurpureum'・'Alba Plena'・'Rosea Plena'・'Mariesii' をありふれた品種名に追加
- 下書き：`ClaudeWork/下書き_チャスマンティウム・ケロネ・エキノプス・エリムス・エリゲロン・ガリウム・グレコマ・カリメリス・ラベンダー・レウカンセマム・リスラム・パキサンドラ・フロミスほか51品種_1120.xlsx`（属が多いので、ファイル名は途中から「ほか」とした）。耐暑性 強 24・中 13・弱 1・空欄 13、蒸れ耐性 強 3・中 3・弱 5・空欄 40、西日耐性 ◎4・○24・△7・×5・空欄 11。品種のページがどの文献にもないのは4品種（Lt02・Sm01・Sy01・Tf04）。学名の検討は23品種
- 根拠を確認して直したこと（assemble_pilot.py。前の batch にも効く）
  - 文献の文に「改行しない空白」が混じっていると言い回しに当たらなかった（NC State のスティパ テヌイッシマ）。判定の前にふつうの空白に直すようにした
  - 弱 に足した：「This plant will not do well in the hot humid conditions of the southeast」（スティパ テヌイッシマ。蒸れも 弱）
  - 中 に足した：「In the hot summer weather, it tends to become dormant」（グレコマ）、「does best in full sun in cooler climates and partial shade in the southeast」（サギナ 'Aurea'）
  - 強 に足した：「adaptable to … hot, humid weather」（カリメリス インシサ。蒸れも 強）。蒸れ 強：「tolerates heat, humidity, drought」（ユッカ グロリオーサ）
  - 蒸れ 弱 に足した：「difficult to grow … because of winter stresses and high summer humidity」「High summer humidity in the St. Louis area is not appreciated」（ラベンダー。MBG の文は「St.」で切れて2つに分かれるので、切れた形で当てている）
  - トリフォリウムを GENUS_MBG_SKIP に追加（MBG の品種ページはレペンスだけ。ルーベンス・オクロレウカムに当てない）
  - 前の batch（02〜13）を作り直して比べたが、変化はなかった
- 同名の別品種への当たり違いは見つからなかった。stauden.de は 'Jenny' を Aster dumosus、ヒューケレラを x Heucherella tiarelloides、'Platinum Blue' を Echinops ritro と書いているが、品種名は同じ
- 同じ種のおぎはらの値（batch_14/ogihara_data.py の SIBLING）：エゾミソハギの種そのもの・'Happy Snow'（Lt01・Lt02）を 強（根拠は 'Happy Lights'・'Robert'）、ヤブデマリ 'Mariesii'（Vu01）を 強、シロツメクサの3品種（Tf02〜Tf04）を 中。【見返すこと】同じ種の値を 中 で使ったのは4回目（batch_07・11・12 に続く）
- 種のページを当てたもの（おぎはら）：ワイルドオーツ 'Little Tickler'、源平小菊（'Profusion'）、フロミス チューベロサ（'Bronze Flamingo'）、サポナリア オフィシナリスの八重の2品種。スティパ テヌイッシマは、マスターの商品名に「エンジェルヘアー」とあるので図鑑の 'Angel Hair' を品種のページとして当てた
- 当てなかったもの：フッキソウの緑葉（同じ種は斑入りの1ページだけ）、トリフォリウム ルーベンス・'Frosty Feathers'（'Red Feathers' の1ページだけ）、品種名のないセンペルビブム、アスターの2品種
- 耐暑性 弱 の1品種：サギナ サブラータ（Sg01。NC State：強い暑さや乾燥ではよく育たない。蒸れ耐性も 弱〔Walters：高温多湿の夏の地域では蒸れて傷むことがある〕）。'Aurea'（Sg02）は NC State の品種のページから 中（蒸れ耐性は 弱）
- 蒸れ耐性 弱 の5品種：ラベンダー2品種、サギナ2品種、スティパ テヌイッシマ
- おぎはらと欧米の文献の食い違い：スティパ テヌイッシマ（おぎはら 強／NC State：米国南東部の高温多湿ではよく育たない＝弱 相当）、ビバーナム 'Onondaga'（強／MBG：ゾーン7より南には勧めない、NC State：暑さに耐えない＝弱 相当）、フロミス ルッセリアナ・'Broadway Lights'（強／中 相当）
- 耐暑性が空欄の13品種：ケロネ2、ラベンダー2（蒸れ耐性は 弱）、シルフィウム2、アスター2、トリフォリウム オクロレウカム・ルーベンス・'Frosty Feathers'、クルマバソウ、フッキソウの緑葉。シルフィウム・センペルビブム・アスターは、ほかの項目も空欄が多い（属の平均で9〜11項目）
- ユーザーに聞くこと・伝えること（学名の検討に出る）：(a) Cl02 ケロネ オブリクア 'Alba' は、RHS が「Chelone obliqua var. alba」を Chelone glabra の白花のシノニムとしている（Jelitto は CHELONE obliqua var. alba で種子を売っている）。売っているものがどちらの種かは要確認。RHS のページは別の種になるので当てていない (b) エリゲロン 'Pink Jewel' は RHS が 'Rosa Juwel'（種小名なし）、おぎはら・Jelitto・stauden.de が speciosus の品種 (c) エリゲロン 'Profusion' は RHS が種のシノニム、Jelitto・Gaißmayer が 'Blütenmeer' の別名 (d) カリメリス インシサ 'Variegata' は RHS ではシノニム扱い（Kalimeris yomena 'Variegata' を併記）(e) 'Broadway Lights' は RHS・MBG で品種名 'Leumayel'（おぎはらは 'Broadway'）(f) フロミス 'Bronze Flamingo' は RHS がシノニム扱い、Jelitto が種の流通名 (g) トリフォリウム オクロレウカムは RHS のつづりが ochroleucon。レペンスの 'Atropurpureum'・'Dragon's Blood'、ルーベンス 'Frosty Feathers'、サポナリア 'Alba Plena' は RHS で未確定 (h) アスターの2品種（Sy01・Sy02）は、マスターの学名が新しい属名（Symphyotrichum）。アスターのまとまり（batch_aster）の品種は古い属名（Aster）のままなので、最後の学名の検討でそろえる。'Jolly Jumper' はどの文献にも名前がない (i) Gc01 は商品名が「グレコマ 散り斑」、学名は品種名なしの Glechoma hederacea（種の記述を当てている）。Sm01 は品種名のないセンペルビブム (j) スティパ イチュは Jelitto が (NASSELLA, JARAVA) を併記、テヌイッシマは Nassella tenuissima とも書かれる (k) Jelitto が発表した品種：エキノプス 'Star Frost'（2008）・'Snowdrift'（1996）・'Frosty Feathers'（2016） (l) シカゴ植物園：アスター 'Jenny' は総合評価 very poor（さび病に非常に弱く、最初の冬に枯れた）。'Snowdrift' は花つき excellent だが、冬に株元が傷んだ年がある (m) Gaißmayer：源平小菊は Z7・「暖かい土地や暖冬では多年草、それ以外は短命。こぼれ種でよく増える」、スティパ2種は Z7・春植えを勧める、カワラマツバは地下茎で強く広がる（植える場所に注意）、クルマバソウは地下茎で広がり涼しい土を好む、サギナは栄養繁殖の不稔の系統

## 15個目のまとまり：アスクレピアス・クロコスミア・ガイラルディア・アガスタチ・カリオプテリス・クナウティア・レウイシア・ルピナス・オリガヌム・ペオニア・パルテノキッスス・シダルセア・アラビス・カルーナ・カマエメルム・クリサンセマム・キミキフーガ・ドラコセファラム（2026-11-20、下書きまで完了）
- 入力は batch_15/input（51品種・18属：Ak=アスクレピアス4、Cr=クロコスミア4、Gl=ガイラルディア4、Aa=アガスタチ3、Cy=カリオプテリス3、Kt=クナウティア3、Lw=レウイシア3、Lu=ルピナス3、Or=オリガヌム3、Py=ペオニア3、Px=パルテノキッスス3、Sd=シダルセア3、Ab=アラビス2、Cu=カルーナ2、Cm=カマエメルム2、Cs=クリサンセマム2、Ci=キミキフーガ2、Dr=ドラコセファラム2。種のまとまり 31）。試作28品種と重なる品種（アガスタチ 'Black Adder'、ルピナス 'Fraulein'）も同じ形で入れてある
- 文献：おぎはら 15ページ（15品種。レウイシア・ルピナス・アラビス・カルーナ・ドラコセファラム・ハマギク・コハマギク・ペオニアの園芸品種は掲載なし）、RHS 48品種、Gaißmayer 17ページ（20品種）・Jelitto 26ページ（31品種。どちらも Chrome、7秒おき、1回の指示は6ページまで）。シカゴ植物園の一覧（no1〜no40）にこの18属の号はない
- 確認画面：Gaißmayer も Jelitto も、最初の1ページで確認画面が出た。どちらも操作せずに置き、RHS とシカゴ植物園の一覧を見ている間（3分ほど）に自動で通った。そのあとは出なかった
- 読み方の工夫（次も使える）：Gaißmayer の商品ページは、番号さえ合っていれば途中の語が違っても開いた（/web/shop/a/b/384/x/<番号>/?static）。検索結果からは番号と名前だけ拾えばよい。検索も商品ページも「読む → 次へ移る」の関数を sessionStorage に入れておき、2つのサイトを交互に、7秒おきで進めた
- fetch_all.py に足したもの：キミキフーガ＝Actaea、ハマギク＝Nipponanthemum nipponicum、コハマギク＝Dendranthema yezoense、カリオプテリス ディバリカータ＝Tripora divaricata、× clandonensis・× crocosmiiflora・× grandiflora の × 表記、アラビス アルピナ＝Arabis caucasica、フェルディナンディコブルギ＝Arabis procurrens、ローマンカモミール＝Anthemis nobilis、'Goblin'＝'Kobold'、'Burgundy'＝'Burgunder'、'Fraulein'＝'Fräulein'、'Chandelier'＝'Kronleuchter'、'Kinlochrue'＝'Kinlochruel'
- 下書き：`ClaudeWork/下書き_アスクレピアス・クロコスミア・ガイラルディア・アガスタチ・カリオプテリス・クナウティア・レウイシア・ルピナス・オリガヌムほか51品種_1120.xlsx`（ファイル名が長すぎると保存できないので、途中から「ほか」とした）。耐暑性 強 20・中 12・弱 9・空欄 10、蒸れ耐性 中 1・弱 9・空欄 41、西日耐性 ◎5・○20・△13・×3・空欄 10。品種のページがどの文献にもない品種はなかった。学名の検討は27品種
- 根拠を確認して直したこと（assemble_pilot.py。前の batch にも効く）
  - 【誤りを直した】Walters の「Not terribly tolerant of hot humid summers」（シダルセア 'Rosaly'）が tolerant of … hot に当たって 強 になっていた。not (terribly／very／particularly) tolerant of … を 弱 に足した（弱 を先に見るので 強 にならない）
  - 弱 に足した：「Plants tend to decline／suffer in summer heat south of Zone 6」（アラビス。MBG は同じページで「Tolerates hot dry conditions」とも書いているが、割れたら控えめな側）
  - 中 に足した：「Provide some shade at the heat of the day for golden and variegated leaf forms」（オレガノ ブルガレの黄葉・斑入り）、「in hot summer locations (USDA Zones 8 and 9), this vine may do best if planted on eastern or northern walls」（ナツヅタ）、「moderately resistant to … heat」（アメリカヅタ）
  - 強 に足した：「Good heat and drought tolerance」（オレガノ）、「grows well in hot, dry sites」（ガイラルディア アリスタータ）
  - 蒸れ 弱 に足した：「often struggle in the heat and humidity of the deep South」（クナウティア）。蒸れ 中 に足した：「tolerates humidity better than some hyssops」（アガスタチ 'Blue Fortune'。比べる書き方なので 強 にしない）
  - 前の batch（02〜14）を作り直して比べたが、変化はなかった
- 同名の別品種への当たり違いは見つからなかった。stauden.de・MBG・Gaißmayer はガイラルディアの 'Burgunder'・'Kobold'・'Amber Wheels' を × grandiflora、stauden.de はアガスタチを Agastache rugosa、ルピナスを Lupinus polyphyllus、ペオニアの交配種を Paeonia x hybrida と書いているが、品種名は同じ
- 同じ種のおぎはらの値（batch_15/ogihara_data.py の SIBLING）：アスクレピアス インカルナータの 'Milkmaid'・'Soulmate'（Ak03・Ak04）を 強（根拠は 'Ice Ballet'・'Cinderella'）、クナウティア マケドニカの種そのもの・'Midget Mauves'（Kt01・Kt03）を 強（根拠は 'Mars Midget'・'Thunder and Lightning'）、サラシナショウマの種そのもの（Ci01）を 中（根拠は 'White Pearl' など5品種）。【見返すこと】同じ種の値を 中 で使ったのは5回目（batch_07・11・12・14 に続く）
- 当てなかったもの（おぎはら）：クロコスミアの × crocosmiiflora の2品種と 'Ember Glow'（図鑑は 'Lucifer'・'Hellfire' の2ページで、どちらも種小名なし）、オレガノ ブルガレの2品種、緑葉のアメリカヅタ・シダルセア マルビフローラ・一重のローマンカモミール（どれも同じ種のページが1つだけ）、アスクレピアス アスペルラ、アガスタチ 'Red Fortune'
- Px02（斑入りのアメリカヅタ）は、マスターの学名に品種名がない。図鑑の「斑入りアメリカヅタ Parthenocissus quinquefolia 'Variegata'」を品種のページとして当てた。RHS の斑入り（[Star Showers] 'Monham'）は同じ品種か分からないので当てていない
- 耐暑性 弱 の9品種：カルーナ2品種（MBG・NC State：高温多湿を嫌う、ゾーン6より南には勧めない。蒸れも 弱）、ルピナス3品種（NC State の属のページ：涼しい気候が要る、米国南部の高温多湿を嫌う。ペレニスは種のページ：夏の暑さで地上部が枯れることがある）、シダルセア 'Party Girl'（MBG：涼しい夏を好む）・'Rosaly'（Walters）、ローマンカモミールの一重（MBG：涼しい夏の気候で最もよい）、アラビス 'Pixie Cream'
- 蒸れ耐性 弱 の9品種：カルーナ2、クナウティア3、ルピナスの交配種2、シダルセア マルビフローラ2
- おぎはらと欧米の文献の食い違い：クナウティア3品種（おぎはら 強／MBG：夏の夜が涼しい気候で最もよく育つ、米国南部の高温多湿では苦しむ＝弱 相当）、ローマンカモミールの八重（中／弱 相当）、クロコスミア 'Lucifer'（強／暑い夏の地域では半日陰を好む＝中 相当）、ナツヅタ 'Fenway Park'・斑入りのアメリカヅタ（強／中 相当）
- 耐暑性が空欄の10品種：アラビス 'Variegata'、アスクレピアス アスペルラ、ハマギク・コハマギク、ドラコセファラム2品種、ガイラルディア 'Mesa Peach'、レウイシア 'Little Snowberry'、ペオニア 'Coral Sunset'・'Paula Fay'。ハマギク・コハマギク・ドラコセファラム・パルテノキッススは、ほかの項目も空欄が多い（属の平均で9〜11項目）
- ガイラルディアの3品種（Gl01〜Gl03）は、マスターの学名が aristata なので、MBG・NC State のアリスタータ（種）の記述を当てている（耐暑性 強 は NC State の種のページから）。RHS などは × grandiflora の品種としている
- ユーザーに聞くこと・伝えること（学名の検討に出る）：(a) ガイラルディア 'Amber Wheels'・'Burgundy'・'Goblin' は、RHS・stauden.de・Gaißmayer・MBG が × grandiflora の品種（Jelitto は aristata）。RHS の品種名はドイツ語の 'Burgunder'・'Kobold'。'Mesa Peach' は RHS では流通名（品種名は 'Pas907056'） (b) ルピナス 'Fraulein' は RHS が 'Noble Maiden' (Band of Nobles Series)・種小名なし、Jelitto が 'Fräulein' [Noble Maiden]、'Chandelier' は Jelitto・Gaißmayer が 'Kronleuchter'。試作のときの決定（学名は Lupinus 'Fräulein'）と合う (c) キミキフーガは RHS が Actaea simplex（'Black Negligee' は Atropurpurea Group）、おぎはらは Cimicifuga simplex(=Actaea matsumurae) (d) ハマギクは RHS・Jelitto とも Nipponanthemum nipponicum (e) カリガネソウ 'Snow Fairy' は、おぎはらが Tripora divaricata、RHS は Caryopteris・Tripora のどちらの名前もシノニム扱い（名前だけの登録） (f) アラビス 'Pixie Cream' は RHS・Jelitto・stauden.de が Arabis caucasica の品種（RHS で未確定）。フェルディナンディコブルギ 'Variegata' は RHS の正名が Arabis procurrens 'Variegata' (g) アガスタチ 'Black Adder' は RHS のつづりが 'Blackadder'。'Red Fortune' は RHS の耐寒性が H2（寒さに弱い扱い）、'Black Adder' は H4 (h) クロコスミア 'Lucifer' は RHS・MBG・おぎはらが種小名なし、Gaißmayer が Crocosmia masoniorum の品種（マスターは × crocosmiiflora）。'Ember Glow' は RHS のつづりが 'Emberglow' (i) アスクレピアス 'Milkmaid' は、Jelitto が 'Iceballet' の別名として載せている（ASCLEPIAS incarnata 'Iceballet' [Milkmaid, Ice Follies]）。RHS・MBG・おぎはらに 'Milkmaid' の名前はない。Jelitto のこのページを当てたが、同じ品種として扱ってよいかは要確認。'Cinderella' は RHS でシノニム扱い（名前だけの登録） (j) シダルセア 'Party Girl'・'Rosaly' とレウイシアの3品種は RHS が種小名なし (k) カルーナ 'Kinlochrue' は RHS のつづりが 'Kinlochruel' (l) 八重のローマンカモミールは RHS・おぎはらが 'Flore Pleno'、Gaißmayer が 'Plenum' (m) ドラコセファラム 'Fuji White'・レウイシア 'Little Snowberry' は RHS で未確定。'Jim Best' は RHS に名前がない（MBG に品種のページがある） (n) Jelitto が発表した品種：アスクレピアス 'Iceballet'（1992）、ガイラルディア 'Amber Wheels'（2009）、クナウティア 'Mars Midget'（2002）・'Midget Mauves'（2019）、シダルセア 'Bianca'（1989）・'Rosaly'（1990）、アラビス 'Pixie Cream'（2007）、ドラコセファラム 'Fuji Blue'・'Fuji White'（2001）、レウイシア 'Little Mango'（2012）・'Little Raspberry'（2015）・'Little Snowberry'（2018） (o) Gaißmayer：クロコスミア 'Lucifer' は Z7・「いちばん寒さに強い品種とされるが、厳しい土地では冬の保護を勧める。春植えがよい」、ルピナスは毒性が「強い」の区分、オレガノ ブルガレはこぼれ種でよく増える、'Herrenhausen' は花後に全体を切り戻すとこぼれ種を防げる、シダルセア カンディダは過湿の重い土にも長い乾燥にも耐えない、八重・一重のローマンカモミールは花後に強く切り戻す (p) Jelitto：シダルセア 'Rosaly' は「夏の涼しい気候では日なた、ほかでは半日陰」、ハマギクはゾーン7〜10、レウイシアは石灰を避ける

## 16個目のまとまり：エピメディウム・フラガリア・ヘレボルス・イベリス・リリオペ・リクニス・ムクデニア・ファラリス・フィソカルプス・ロジャーシア・ソリダゴと、1品種の属27（2026-11-20、下書きまで完了）
- 入力は batch_16/input（50品種・38属：Em=エピメディウム2、Fr=フラガリア2、Hb=ヘレボルス2、Ib=イベリス2、Lr=リリオペ2、Lc=リクニス3、Mk=ムクデニア2、Pi=ファラリス2、Pz=フィソカルプス2、Rg=ロジャーシア2、So=ソリダゴ2、1品種ずつ：Ae=アクタエア、Ao=エゴポディウム、Ax=アルテア、Ap=アンペロプシス、Ay=アンドロサセ、Aw=アレナセルム、Au=アルンクス、Ai=アスチルボイデス、Az=オーブリエタ、Bi=ビゲロウィア、Br=ブルネラ、Bu=ブフタルムム、Ct=ケラトスティグマ、Cd=コルタデリア、Da=ダルメラ、De=デンドランセマ、Es=エルショルチア、Et=エラグロスティス、Ei=エリカ、Eo=エリオゴヌム、Ey=エリシマム、En=ユーオニマス、Go=ゴニオリモン、Hn=ヘリアンサス、Hc=ヘリクトトリコン、Im=インペラータ、Lm=ラミアストラム。種のまとまり 44）
- make_input.py を直した：学名が「Lychnis×haageana」のように × が属名にくっついている商品は、× の前を属とする（リクニスが3品種になった。input の学名は「Lychnis × haageana 'Molten Lava'」と、× の前後に空白が入る）
- 文献：おぎはら 15ページ（16品種）、RHS 48品種、Gaißmayer 17ページ（17品種。ほかに、当てなかった種のページを1つ読んだ）・Jelitto 21ページ（22品種。どちらも Chrome、7秒おき、1回の指示は6ページまで）、シカゴ植物園 no20 エピメディウム 2品種・no15 ソリダゴ 1品種（'Fireworks'）・no40 ロジャーシアとアスチルボイデス 1品種（アスチルボイデス）
- 確認画面：batch_15 を読み終えてから40分ほどあいていた。検索の6〜7ページ目で、Gaißmayer も Jelitto も確認画面が出た。どちらも操作せずに置き、RHS とシカゴ植物園の報告を読んでいる間（4分ほど）に自動で通った。そのあとは出なかった
- 【気をつけること】確認画面のページをそのまま読むと「0件」と読み違える（Gaißmayer の Lychnis で起きた。あとで検索し直した）。読む前にページの題名（Gaißmayer は「Produkt-Suche」「Produkt |」、Jelitto は「Hits for」と本文の「Plant Description」）を確かめ、違えば読まずに止める形にした
- fetch_all.py に足したもの：リクニス＝Silene、デンドランセマ＝Chrysanthemum、ラミアストラム＝Lamium、アクタエア＝Cimicifuga、× rubrum・× versicolor・× haageana の × 表記、ヘレボルス オリエンタリス＝× hybridus（種のページがないときだけ）、ノブドウ＝Ampelopsis brevipedunculata、アレナセルムの subsp.／var. bulbosum、ファラリスの var. picta、ムクデニア＝Aceriphyllum、アスチルボイデス＝Rodgersia tabularis、'Diabolo'＝'Monlo'、'Summer Wine'＝'Seward'、'Gin-ryū'＝'Silver Dragon'、'Herman's Pride'＝'Hermann's Pride'、'Vivelli'＝'Vivellii'、'Rubra'＝'Red Baron'、'Karasuba'＝'Crimson Fans'
- 下書き：`ClaudeWork/下書き_エピメディウム・フラガリア・ヘレボルス・イベリス・リリオペ・リクニス・ムクデニア・ファラリス・フィソカルプス・ロジャーシア・ソリダゴほか50品種_1120.xlsx`。耐暑性 強 19・中 5・弱 4・空欄 22、蒸れ耐性 強 3・中 1・弱 6・空欄 40、西日耐性 ◎5・○7・△7・×16・空欄 15。品種のページがどの文献にもないのは5品種（Ae01・Cd01・Pi01・Rg01・Rg02）。学名の検討は31品種
- 根拠を確認して直したこと（assemble_pilot.py。前の batch にも効く）
  - 【誤りを直した】「冬の寒さ・日ざしで常緑の葉が傷む（sun scorch … in cold winter climates）」という文が scorch に当たって、暑さ 中・西日 × になっていた（イベリス、ヘレボルス アーグティフォリウス）。scorch と winter があり、hot・heat・summer がない文は、暑さ・西日の判定に使わないようにした。イベリスの西日耐性は × → ◎
  - 弱 に足した：「often struggle in the hot and humid summers of the deep South」（ムクデニア。蒸れも 弱）、「sensitive to high heat and humidity」（ヘリクトトリコン。蒸れも 弱）、「intolerant of our hot and humid climate」「will not perform well in the hot and humid summer conditions」「not recommended for the southeastern United States」（ブルネラ。蒸れも 弱）
  - 強 に足した：「good tolerance for heat, humidity and drought」（ヤブラン。蒸れも 強）、「tolerates salt spray, heat and drought」（リリオペ スピカータ）。蒸れ 強：「Tolerates hot, humid summer regions」（Walters のソリダゴ 'Fireworks'）
  - 蒸れ 中 に足した：「Leaf blight … particularly troublesome in hot and humid summer climates」（エゴポディウム）
  - 前の batch（02〜15）を作り直して比べた：変わったのは batch_06 のアキレア 'Coronation Gold'（Ac02）だけで、蒸れ耐性が 空欄 → 強（MBG：'Coronation Gold' tolerates hot, humid summers and drought）。作り直した下書きは `ClaudeWork/下書き_ポテンティラ…49品種_1120c.xlsx`（前の `_1120b.xlsx` は残してある）
- 同名の別品種への当たり違いは見つからなかった。stauden.de は 'Orange Flame' を Erysimum linifolium、'Happy Days' を Helianthus decapetalus、ベニチガヤを Imperata cylindrica var. major 'Rubra'、MBG は斑入りノブドウを Ampelopsis brevipedunculata var. maximowiczii 'Elegans' と書いているが、品種名は同じ
- 同じ種のおぎはらの値（batch_16/ogihara_data.py の SIBLING）：ヤブラン 'Okina'（Lr01）を 強（根拠は 'Variegated White' など4品種）、リクニス コロナリア 'Alba'（Lc01）を 強（'Angel's Blush' など3品種）、パンパスグラス 'Mini Pampas'（Cd01）を 強（'Evita' など4品種）、ロジャーシア ピンナータ 'Scarlet'（Rg01）を 中（'Chocolate Wing' など4品種）。【見返すこと】同じ種の値を 中 で使ったのは6回目（batch_07・11・12・14・15 に続く）
- 種のページを当てたもの（おぎはら）：ヘレボルス アーグティフォリウス（'Janet Starnes'）、イベリス センパービレンス（'Snow Cushion'）、ブルネラ マクロフィラ（'Silver Spear'）
- 【要確認】ベニチガヤ（Im01）は、図鑑の「紅チガヤ Imperata koenigii」を和名で当てた（学名の書き方がマスターと違う）。Gaißmayer は 'Red Baron' のページを当てた（RHS が 'Red Baron' を 'Rubra' のシノニムとしている）
- 当てなかったもの（おぎはら）：エピメディウムの2品種（図鑑は別の交配の4ページ。どれも 中）、ワイルドストロベリーの2品種（'Golden Alexandria' の1ページだけ）、ヘレボルス オリエンタリス（図鑑の実生は × hybridus）、リリオペ スピカータ、× haageana 'Molten Lava'、ムクデニアの種そのもの（'Karasuba' の1ページだけ）、ファラリス（図鑑は Phalaris karka）、ロジャーシア ポドフィラ、アルテア・エラグロスティス・エリカ・エリオゴヌム（図鑑は同じ属の別の種）、ユーオニマス 'Emerald Gaiety'・ラミアストラム（同じ種のページが1つだけ）
- Gaißmayer の種のページ（Fragaria vesca）は「ランナーでよく広がる」野生型の説明なので、ランナーを出さない四季なりの 'Alpine Yellow' には当てていない
- 耐暑性 弱 の4品種：アレナセルム 'Variegatum'（NC State：夜が涼しく夏が乾く気候を好み、暑いと病気になるか休眠する）、エリカ カルネア 'Vivelli'（NC State：涼しい夏を好み、米国南部では難しい）、ヘリクトトリコン（NC State：高温多湿に弱い）、ムクデニアの種そのもの（MBG）
- 蒸れ耐性 弱 の6品種：アルンクス 'Noble Spirit'、ブルネラ 'Silver Spear'、ダルメラ、ヘリクトトリコン、ムクデニア2品種
- おぎはらと欧米の文献の食い違い：ダルメラ（おぎはら 強／MBG：涼しい夏の気候を好み、米国南部の高温多湿ではよく育たない＝弱 相当）、ムクデニア 'Karasuba'（強／弱 相当）、アルンクス 'Noble Spirit'（中／MBG：ゾーン8〜10の高温多湿ではよく育たない＝弱 相当）、ブルネラ 'Silver Spear'（中／弱 相当）、アスチルボイデス・エゴポディウム・ルリマツリモドキ・フィソカルプス2品種（強／中 相当）、ヘレボルス 'Janet Starnes'（強／Walters：午前の日と午後の日かげがよい＝中 相当）
- 耐暑性が空欄の22品種：アクタエア、アルテア、アンドロサセ、オーブリエタ、ビゲロウィア、ブフタルムム、デンドランセマ、エピメディウム2、ユーオニマス、エリオゴヌム、エルショルチア、エリシマム、ゴニオリモン、ヘレボルス オリエンタリス、ヘリアンサス、× haageana、ラミアストラム、ファラリス2、ロジャーシア ポドフィラ、ソリダゴ 'Gold Spangles'。ビゲロウィア・エリシマム・エリオゴヌム・アクタエア・ブフタルムム・ソリダゴ 'Gold Spangles'・ファラリス 'Tricolor' は、ほかの項目も空欄が多い（12〜17項目）
- ユーザーに聞くこと・伝えること（学名の検討に出る）：(a) リクニスは RHS の正名が Silene（Silene coronaria 'Alba'）。'Angel's Blush' は Jelitto が 'Oculata' [Angel's Blush]、RHS ではシノニム扱い (b) デンドランセマ ウェイリチーは RHS の正名が Chrysanthemum weyrichii (c) ラミアストラムは RHS・MBG が Lamium galeobdolon、品種名のつづりは 'Hermann's Pride' (d) ベニチガヤは RHS の正名が 'Rubra'（'Red Baron' はシノニム扱い） (e) フィソカルプス 'Summer Wine' は RHS・MBG とも流通名（品種名は 'Seward'）、'Diabolo' は 'Monlo' の別名つき (f) 斑入りノブドウは RHS の正名が Ampelopsis brevipedunculata 'Elegans'（マスターは glandulosa var. brevipedunculata） (g) アレナセルムは RHS が var. bulbosum（マスターは ssp.）、エリカは 'Vivellii'、エリオゴヌムは RHS のつづりが alleni (h) エリシマム 'Orange Flame'・ソリダゴ 'Gold Spangles'・アルンクス 'Noble Spirit' は RHS が種小名なし。'Orange Flame' は stauden.de が linifolium の品種（マスターは kotschyanum） (i) オーブリエタ 'Variegata' は RHS では Variegata Group (j) ヘレボルス オリエンタリス（Hb02）は、マスターの花色が「白系他」。種（orientalis）の文献を当てているが、売っているのが交配種（× hybridus）の実生なら当て先が変わる。要確認 (k) ロジャーシア 'Scarlet'・'Bronze Beauty'、アクタエア 'Silver Dance'（RHS は名前だけ）はどの文献にも品種のページがない。パンパスグラス 'Mini Pampas' は RHS で名前だけのシノニム扱い (l) ヘリアンサス 'Happy Days' は商品名に「ヤナギバヒマワリ」とあるが、RHS・MBG は種小名なし、stauden.de は decapetalus の品種 (m) Jelitto が発表した品種：イベリス 'Snow Cushion'（2002）、ブフタルムム 'Alpengold'（1991）、エリオゴヌム 'Little Rascal'（2009）、ゴニオリモン 'Sea Spray'（2007） (n) Gaißmayer：ベニチガヤは Z6・「よく冬の保護をしたときだけ冬越しする。浅い鉢植え向き。地植えは春に日当たりのよい守られた場所へ、冬は落ち葉と枝で覆う」、リクニス コロナリアは短命（2〜3年）でこぼれ種で続く、斑入りのエゴポディウムは「種より広がり方は穏やかだが、こぼれ種の前に花を摘む」、ルリマツリモドキ・ヤブラン・エルショルチアは春植えを勧める、ダルメラは遅霜で花が傷むことがある、アスチルボイデスは過湿を避ける (o) シカゴ植物園：エピメディウム 'Sulphureum' は試験の間に冬の傷みで1株が枯れた、アスチルボイデスは芽出しが早く、5年で新葉が遅霜に中〜重く傷んだ（総合評価 ★3）、ソリダゴ 'Fireworks' は試験で最高評価 (p) MBG はチガヤ（Imperata cylindrica）を、米国のいくつかの州で有害な雑草に指定されていると書いている（種の記述。同じページに「涼しいゾーン5〜6では広がり方が穏やか」とも）

## 17個目のまとまり：在庫のある1品種の属20（レオントポディウムからウンキニアまで）と、在庫のない2〜3品種の属12（アムソニアからビオラまで）（2026-11-20、下書きまで完了）
- 入力は batch_17/input（47品種・32属。1品種ずつ：Ln=レオントポディウム、Lp=レプティネラ、Ms=メリッサ、Ml=ミリウム、Op=オフィオポゴン、Pm=パルテニウム、Pf=フィテウマ、Pj=ピンピネラ、Pw=ポア、Pd=ポリゴナツム、Pk=ポリゴヌム、Rn=ラナンキュラス、Rt=ラティビダ、Rl=ルエリア、Ss=セセリ、Se=セスレリア、Sq=スポディオポゴン、Sk=スクシサ、Tm=テルモプシス、Un=ウンキニア。在庫のない属：Av=アムソニア3、Ba=バプティシア3、Dl=デルフィニウム3、Fo=フォエニクルム2、Hp=ヘリオプシス2、Lh=ラティルス2、Lj=リモニウム2、Pq=フィソステギア2、Ro=ロサ2、To=トバラ2、Vr=ベルノニア2、Vo=ビオラ2。種のまとまり 36）
- 【input を手で直した】To01 トバラ 'Compton's Form' は、マスターの学名に種小名がない（Tovara 'Compton's Form'）ので make_input.py では「Tovara hybrid」になる。RHS が Persicaria virginiana 'Compton's Form' と書いているので、input の species だけ「Tovara virginiana」に直した（学名の列はそのまま）。make_input.py を作り直すと元に戻る
- 文献：おぎはら 24ページ（26品種）、RHS 44品種、Gaißmayer 18ページ（19品種）・Jelitto 36ページ（38品種。どちらも Chrome）、シカゴ植物園 no18 アムソニア 3品種・no11 シュラブローズ 1品種（'Adelaide Hoodless'。'Sir Thomas Lipton' は入っていない）。Gaißmayer・Jelitto・RHS の番号・おぎはらは、18個目のまとまりの分も同じときに続けて読んだ
- 確認画面と読み方（Gaißmayer・Jelitto）
  - 最初はどちらも確認画面なしで開いた
  - 【やってはいけないこと】開いてあるページの中から fetch で検索結果を順に読む形（7秒おき）を試したら、どちらのサイトも数ページで確認画面（403・Just a moment）になった。この読み方はやめた
  - そのあとタブで開くと、どちらも確認画面（「しばらくお待ちください...」）が出た。操作せずに置き、おぎはら図鑑と RHS を進めている間（10分ほど）に自動で通った。そのあとは最後まで出なかった
  - タブを1ページずつ開く読み方（「読む → 次へ移る」の関数を sessionStorage に入れ、2つのタブを交互に、1つのサイトにつき7秒おき。1回の指示は10ステップ＝各サイト5ページ、40秒ほど）で、検索58語＋61語、商品ページ28＋51を読んだ
  - Jelitto は検索の途中で一度「525: SSL handshake failed」（サーバー側のエラー）になった。同じページを開き直すと読めた
  - Chrome の JavaScript の結果は約1,000字で切れるので、読んだ内容は sessionStorage にためて、最後に950字ずつ取り出した（結果に = ? & を入れない）
- fetch_all.py に足したもの：トバラ＝Persicaria・Polygonum、ポリゴヌム ビストルタ＝Bistorta officinalis・Persicaria bistorta、ラナンキュラス フィカリア＝Ficaria verna、サーモプシス カロリニアナ＝Thermopsis villosa、リモニウム ラティフォリウム＝Limonium platyphyllum、エーデルワイス＝Leontopodium nivale subsp. alpinum、レプティネラ＝Cotula、× variicolor の × 表記、'Twilite'＝'Twilite Prairieblues'、'Rosenelfe'＝'Rose Fairy'、'Superbum'＝'Superba'、'Purpureum'＝'Bronze'・'Rubrum'。'Purpureum'・'Aureum'・'Superbum'・'Chocolate' などをありふれた品種名に追加。18個目の分（アゲラティナ＝Eupatorium rugosum、アンテミス＝Cota、カメリオン＝Epilobium・Chamaenerion、ギレニア＝Porteranthus、ペロフスキア＝Salvia yangii、レウコスケプトルム＝Comanthosphace など）も同じときに足した。fetch_walters.py にも別の属名の URL を足した
- 下書き：`ClaudeWork/下書き_レオントポディウム・レプティネラ・メリッサ・ミリウム・オフィオポゴン・パルテニウム・フィテウマ・ピンピネラ・ポアほか47品種_1120.xlsx`。耐暑性 強 24・中 9・弱 6・空欄 8、蒸れ耐性 強 2・中 3・弱 5・空欄 37、西日耐性 ◎6・○18・△10・×7・空欄 6。品種のページがどの文献にもないのは1品種（Pq01 フィソステギア 'Deep pink'）。学名の検討は26品種
- 根拠を確認して直したこと（assemble_pilot.py。前の batch にも効く）
  - 弱 に足した：「Somewhat intolerant of high summer heat and humidity」「did not do well … in the hot and humid St. Louis」（MBG のセスレリア オータムナリス。蒸れも 弱）、「It does poorly in hot, dry sites」「grows slowly and poorly in hot climates」「will not do well in hot, dry sites」（スポディオポゴン）、「Best in regions with cool summers」（Walters のエーデルワイス）、「In hot, humid summer regions, plants do not usually last more than 2 to 3 years」（Walters のデルフィニウム。蒸れも 弱）
  - 中 に足した：「Stems tend to flop in rich soils, too much shade or hot summer temperatures」（フィソステギア）
  - 強 に足した：「perform beautifully in the Piedmont and coastal plain, where true Lupines don't grow well because of the heat」（NC State のサーモプシス）、「Roses are heat and frost-tolerant」（NC State のバラの属のページ。属の記述なので信頼度は低）
  - 蒸れ 弱 に足した：「It can be a challenge to grow them in humid summer climates south of USDA Zone 7」（NC State のデルフィニウムの属のページ）。蒸れ 強 に足した：「Tolerant of hot, humid summer regions」（Walters のアムソニア フブリヒティ）、「a particularly good selection for humid climates」（MBG のバラ 'Sir Thomas Lipton'。同じページの「風通しを良くすると葉の病気が減る」とで割れるので、値は 中）
  - おぎはら図鑑の耐暑性の欄が空欄のページ（18個目のオルラヤ。1〜2年草扱い）は、耐暑性には使わないようにした
  - 【誤りを直した】和名（YList）の拾い方。前は「標準」の最初の行を採っていたので、変種・品種の行を拾うことがあった（アマドコロが「オオアマドコロ」、イブキトラノオが「オホーツクイブキトラノオ」、18個目のヤナギランが「ヤエザキヤナギラン」、テンニンソウが「ミカエリテンニンソウ」）。種そのものの行（変種・亜種・品種でない行）を先に採り、マスターの学名に変種・亜種・品種の名前があるときはその行を先に採るようにした（assemble_pilot.py の yl_pick）
  - 前の batch（02〜16）を作り直して比べた：耐暑性・蒸れ耐性・西日耐性の変化はなかった。和名は9つのまとまりの26品種で変わったので、下書きを作り直した（前のファイルは残してある）
    - batch_04 `下書き_セダム…47品種_1120.xlsx`：キリンソウ2品種（ホソバエゾキリンソウ → キリンソウ）、ミセバヤ 'Mediovariegatum'（カガノベンケイソウ → ミセバヤ）、セダム テレフィウム 'Munstead Dark Red'（カラフトミセバヤ → ムラサキベンケイソウ）、アスチルベ チネンシス var. taquetii 'Superba'（オオチダケサシ → タンナトリアシ）
    - batch_05 `下書き_ミント…50品種_1120c.xlsx`：ニホンハッカ（ヨウシュハッカ → ハッカ）
    - batch_08 `下書き_タリクトラム…54品種_1120c.xlsx`：タリクトラム アクイレギフォリウム2品種（ダイセンカラマツ → カラマツソウ）、ミスカンサス f. gracillimus（ススキ → イトススキ）
    - batch_09 `下書き_モナルダ…51品種_1120c.xlsx`：シモツケ3品種（オヤマシモツケ → シモツケ）
    - batch_10 `下書き_ダイアンサス…50品種_1120b.xlsx`：ペニセタム f. viridescens（チカラシバ → アオチカラシバ）
    - batch_11 `下書き_ジギタリス…53品種_1120b.xlsx`：カラマグロスティス ブラキトリカ（サイシュウノガリヤス → ノガリヤス）、アイリス エンサータ 'Variegata'（ハナショウブ → ノハナショウブ。YList は Iris ensata そのものをノハナショウブ、var. hortensis をハナショウブとしている）
    - batch_13 `下書き_ガウラ…51品種_1120b.xlsx`：ニシキシダの4品種（ニシキシダ → イヌワラビ。YList はニシキシダを f. metallicum の和名としていて、マスターの var. pictum の行はないので、種の和名になった）
    - batch_15 `下書き_アスクレピアス…ほか51品種_1120b.xlsx`：ドラコセファラム2品種（シロバナムシャリンドウ → ムシャリンドウ）、シャクヤク 'Sarah Bernhardt'（シベリアシャクヤク → シャクヤク）
    - batch_16 `下書き_エピメディウム…ほか50品種_1120b.xlsx`：斑入りノブドウ（ケノブドウ → ノブドウ）、アレナセルム ssp. bulbosum（オオカニツリ → チョロギガヤ）、リリオペ スピカータ 'Gin-ryū'（ヤブラン → コヤブラン）、ファラリス var. picta（クサヨシ → シマヨシ）
    - 3属の試行（78品種）とアスター（23品種）の下書きは、rediff.py の対象に入っていないので作り直していない。最後にまとめて作り直すときに和名を見直す
- 同名の別品種への当たり違いは見つからなかった。stauden.de はデルフィニウムを Delphinium x cultorum Pacific 'Astolat'、ブロンズフェンネルを Foeniculum vulgare 'Rubrum'、ビオラ 'Mars' を Viola grypoceras 'Mars'、MBG は 'Superbum' を Bistorta officinalis 'Superbum' と書いているが、品種名は同じ
- 同じ種のおぎはらの値（batch_17/ogihara_data.py の SIBLING）：ヘリオプシス 'Summer Nights'（Hp01）を 強（根拠は 'Burning Hearts'・'Asahi'・'Summer Pink'・'Bleeding Hearts'・'Loraine Sunshine' の5品種）
- 種のページを当てたもの（おぎはら）：トバラの2品種（図鑑の「ポリゴナム バージニアナム Polygonum virginianum」）、バプティシア オーストラリス var. minor（ムラサキセンダイハギのページ）
- 売っている商品そのもののページとして当てたもの：セセリ グミフェラム（図鑑は 'Moon Carrot'。Jelitto は [Moon Carrot] を種の流通名としている）、ビオラ ラブラドリカ（図鑑は Viola labradorica 'Purpura'、Jelitto は VIOLA labradorica hort. 'Purpurea' (riviniana Purpurea-Group)。どちらも紫葉で、マスターの葉色も パープル／ブラック系）、サーモプシス カロリニアナ（図鑑・Jelitto・RHS とも Thermopsis villosa）
- 当てなかったもの（おぎはら）：レモンバームの緑葉（図鑑は 'Gold Leaf' の1ページだけ）、アマドコロ（斑入りの var. pluriflorum の1ページだけ）、ラチビダ ピンナータ（図鑑は columnifera の品種）、アムソニア タバーナエモンタナの種そのもの（同じ種は 'Storm Cloud' の1ページだけ）、緑葉のフェンネル、ラシラス 'Heavenly Blue'、バーノニア 'White Lightning'（どれも同じ種のページが1つだけ）、デルフィニウムの3品種（図鑑は別の品種）
- 【要確認】セスレリア（Se01）。マスターの学名は Sesleria autumnalis ssp. argentea。Jelitto は SESLERIA argentea (autumnalis ssp. argentea)、RHS は Sesleria argentea と Sesleria autumnalis を別の種として載せている。おぎはらは「セスレリア オータムナリス (セスレリア アルゲンティア)」。MBG・NC State・stauden.de・Gaißmayer は Sesleria autumnalis のページしかなく、それを種の記述として当てている（耐暑性の「欧米の文献だけなら 弱」と蒸れ耐性 弱 は、MBG の autumnalis の記述から）。売っているものがどちらかで当て先が変わる
- 【要確認】デルフィニウムの3品種。Jelitto のページは Pacific-Premium-Series の 'Astolat Premium'・'Black Knight Premium'・'Galahad Premium'（名前に Premium が付く Jelitto の選抜）。同じ色の系統として当てた。RHS は Astolat Group・Black Knight Group（品種ではなくグループ）
- 耐暑性 弱 の6品種：デルフィニウム3品種（NC State の属のページ：涼しい夏を好む。Walters：高温多湿の夏の地域では2〜3年しかもたないことが多い。蒸れも 弱）、エーデルワイス（MBG：暑さと湿気を嫌う。Walters：夏の涼しい地域がよい。蒸れも 弱）、アマドコロ（MBG：暑い夏を嫌う）、スポディオポゴン（MBG・NC State：暑い気候ではよく育たない）
- 蒸れ耐性 弱 の5品種：デルフィニウム3、エーデルワイス、セスレリア
- おぎはらと欧米の文献の食い違い：セスレリア（おぎはら 強／MBG：夏の高い暑さと湿気にやや耐えない＝弱 相当）、アムソニア フブリヒティ・'Blue Ice'（強／MBG：暑い地域では午後の日かげで花が長もちする＝中 相当）、コクリュウ（強／NC State：暖かい気候では午後の日かげがよい＝中 相当）
- 耐暑性が空欄の8品種：アムソニア タバーナエモンタナ、緑葉のフェンネル、ラシラス 'Heavenly Blue'、ポア 'Blue Hills'、ルエリア、ラチビダ ピンナータ、ビオラ 'Mars'、バーノニア 'White Lightning'。ポア（17項目）・ロサ（平均12.5項目）・ルエリア・サーモプシス（12項目）は、ほかの項目も空欄が多い（ポアは MBG・NC State・stauden.de・Walters にページがなく、RHS も名前だけ。ルエリアとサーモプシスは RHS が名前だけ）
- ロサの2品種は、MBG に 'Sir Thomas Lipton' の品種のページがあるだけで、RHS・stauden.de・おぎはら・Gaißmayer・Jelitto にはない。'Adelaide Hoodless' の耐暑性 強 は、NC State のバラの属のページの1文（Roses are heat and frost-tolerant）だけが根拠（信頼度は低）
- ユーザーに聞くこと・伝えること（学名の検討に出る）：(a) トバラは RHS・MBG が Persicaria virginiana。'Compton's Form' は RHS でシノニム扱い（Persicaria virginiana var. filiformis 'Compton's Red' を併記）。'Variegata' は RHS では品種ではなく Variegated Group（未確定）で、'Painter's Palette' は別の名前。Jelitto は POLYGONUM virginianum 'Variegatum' … [Painter's Palette] と1つにしている（当てていない）。売っているのがどちらかは要確認 (b) ポリゴナム ビストルタ 'Superbum' は RHS の正名が Bistorta officinalis 'Superba'（おぎはらは Persicaria bistorta 'Superba'） (c) カラスバ ヒメリュウキンカは RHS の正名が Ficaria verna 'Brazen Hussy' (d) コクリュウは RHS の正名が Ophiopogon planiscapus 'Kokuryū'（'Nigrescens' はシノニム扱い） (e) サーモプシス カロリニアナは RHS・Jelitto・おぎはら・MBG とも Thermopsis villosa (f) リモニウム ラティフォリウムは MBG が Limonium platyphyllum（RHS はどちらもシノニム扱い）。'Blue Diamond' は Jelitto が LIMONIUM species 'Blue Diamond'（1987年に Jelitto が発表）、RHS は名前だけのシノニム扱い (g) エーデルワイスは RHS に Leontopodium alpinum subsp. alpinum と Leontopodium nivale subsp. alpinum の2つのページがある（どちらも Correct） (h) ウンキニア ルブラは RHS でシノニム扱い、耐寒性は H3。Jelitto はゾーン6〜10 (i) アムソニア 'Blue Ice' は RHS・MBG・おぎはらが種小名なし（マスターは tabernaemontana。シカゴ植物園の報告は、'WFF Select' として入手し 2000年に名前が付いた、と書いている） (j) バプティシア 'Twilite' は RHS が Baptisia × variicolor 'Twilite' (Prairieblues Series) (k) ラシラス 'Heavenly Blue' は RHS・Jelitto のつづりが 'Heavenly Blues'（2022年に Jelitto が発表。RHS の耐寒性は H3）、'Rosenelfe' は RHS で未確定 (l) フィソステギア 'Variegata' は RHS が var. speciosa の品種。'Deep pink' はどの文献にも名前がなく、種の記述だけを当てている。品種名ではなく花色の意味かは要確認 (m) ビオラ ラブラドリカは、RHS が「Viola labradorica ambig.」（あいまいな名前）とし、紫葉のものを riviniana Purpurea Group の側のシノニムとしている。ビオラ 'Mars' は RHS が種小名なし（Viola mandshurica 'Mars' はシノニム扱い）、stauden.de は Viola grypoceras 'Mars' (n) ブロンズフェンネルは stauden.de・Gaißmayer が 'Rubrum'（RHS・Jelitto は 'Purpureum' のシノニムとしている）。Gaißmayer：フェンネルはふつう二年草で、こぼれ種でよく増える (o) Jelitto が発表した品種：ヘリオプシス 'Summer Nights'（2004）・'Burning Hearts'（2016）、ラシラス 'Heavenly Blues'（2022）、リモニウム 'Blue Diamond'（1987）、バーノニア 'White Lightning'（2014）、ポア 'Blue Hills'（2009） (p) Gaißmayer：ビストルタ 'Superba' は「種とちがって広がりすぎない。涼しく湿った土向き」、レプティネラは Z6、コクリュウは Z6・短いランナーでゆっくり広がる、ミリウム 'Aureum' は夏に葉色が黄緑になる・こぼれ種で増える（じゃまにはならない）、ビオラ ラブラドリカはこぼれ種と短いランナーでよく増える、レモンバームは「雪のない厳しい凍結だけが苦手」 (q) Jelitto：セセリは短命（short living）、ミリウム 'Aureum' は「黄金色は涼しい温帯でいちばんよく保たれる」、エーデルワイスとビオラ ラブラドリカは「夏の涼しい気候では日なた、ほかでは半日陰」 (r) シカゴ植物園：アムソニアの3種類は6年間の試験で冬の傷みなし。タバーナエモンタナは9〜10月に株の中心があく。バラ 'Adelaide Hoodless' は黒星病に強くない・冬の傷みが少しある（冬の保護なしの試験）が、本文で Parkland のバラのうち良いものの1つとされている

## 18個目のまとまり（最後）：在庫のない1品種の属19（アゲラティナからバレリアナまで）（2026-11-20、下書きまで完了）
- 入力は batch_18/input（19品種・19属。Af=アゲラティナ、Tn=アンテミス、Cp=セファラリア、Cz=セラスチウム、Cj=カメリオン、Cv=コンバラリア、Cq=コリダリス、Gi=ギレニア、Gb=グロブラリア、Ko=コエレリア、Ls=レウコスケプトルム、On=オエナンテ、Ol=オルラヤ、Pg=ペロフスキア、Pb=プロスタンテラ、Sj=サツレヤ、Sx=セリナム、Sb=スポロボルス、Va=バレリアナ。種のまとまり 19）
- 文献：おぎはら 12ページ（12品種）、RHS 18品種、Gaißmayer 10ページ（10品種）・Jelitto 14ページ（14品種。どちらも Chrome）、シカゴ植物園 no37 ジョーパイウィードとその仲間 1品種（Ageratina altissima 'Chocolate'）。おぎはら・RHS の番号・Gaißmayer・Jelitto は、17個目のまとまりと同じときに続けて読んだ（読み方と確認画面のことは 17個目の節）。このまとまりの分を読んでいる間は、確認画面は出なかった
- 【プロスタンテラ（ミントブッシュ）】Pb01 は種が未確定（DECISIONS.md の未決。マスターの学名は Prostanthera sp.）。種が分からないまま入力に入れ、文献は何も当てていない。下書きは、花色・株張り・葉色の「自社の値」のほかは全部空欄（空欄 18項目）。おぎはら・Gaißmayer・Jelitto には属ごと掲載がない。RHS には cuneata・rotundifolia・ovalifolia・lasianthos などのページがあるので、種が分かれば当てられる
- 下書き：`ClaudeWork/下書き_アゲラティナ・アンテミス・セファラリア・セラスチウム・カメリオン・コンバラリア・コリダリス・ギレニア・グロブラリアほか19品種_1120.xlsx`。耐暑性 強 9・中 3・弱 1・空欄 6、蒸れ耐性 弱 2・空欄 17、西日耐性 ◎2・○7・△4・×1・空欄 5。品種のページがどの文献にもないのは2品種（Cv01 スズラン、Pb01 ミントブッシュ）。学名の検討は10品種
- 根拠を確認して直したこと（assemble_pilot.py。前の batch にも効く。17個目のコミットに入っている）
  - 弱 に足した：「less successful in the high summer heat and humidity of the deep South」「Does not perform well in climates with high humidity」（NC State のセラスチウム。蒸れも 弱）、「It can struggle in our hot southern summers」（NC State のヤナギラン）、「Plants generally thrive in cool summer climates」「prefers cooler weather」（バレリアン）
  - 中 に足した：「may go partially dormant in hot weather」（NC State のコエレリア）
  - 強 に足した：「Ground cover for hot, dry areas」（MBG のスポロボルス）、「loves hot, sunny sites」（Walters のロシアンセージ）
  - ヤナギランの「It is absent from the hot and humid southeastern U.S.」は分布の説明なので当てていない
  - 前の batch（02〜17）を作り直して比べた：耐暑性・蒸れ耐性・西日耐性の変化はなかった（和名の変化は 17個目の節）
- 同名の別品種への当たり違いは見つからなかった。Walters は 'Chocolate' を Eupatorium rugosum 'Chocolate'、stauden.de はヤナギランを Epilobium angustifolium と書いているが、同じもの
- 同じ種のおぎはらの値（SIBLING）：このまとまりでは使っていない
- 売っている商品そのもののページとして当てたもの：コエレリア グラウカ（図鑑は 'Blue Sprite'。Jelitto は [Coolio, Blue Sprite] を種の流通名としている）、オルラヤ（図鑑は 'White Lace'。Jelitto は [White Lace, White Finch] を種の流通名としている。図鑑の耐暑性の欄は空欄なので、耐暑性は空欄のまま）、セラスチウム トメントサム（図鑑は「シルバー カーペット」を併記）
- 【要確認】テンニンソウの黄金葉（Ls01。マスターは Leucosceptrum japonicum f. aureum）に、おぎはら・Gaißmayer・RHS の 'Golden Angel' のページを当てた。Jelitto が LEUCOSCEPTRUM japonicum f. aureum [Golden Angel] と、f. aureum の流通名として 'Golden Angel' を書いているため。売っているものが 'Golden Angel' かどうかは要確認（違うなら、耐暑性 強 と花色などは空欄に戻る）
- 当てなかったもの：アンテミス 'Alba' のおぎはら（同じ種は 'Dwarf form' の1ページだけ）、スズラン（おぎはら・Gaißmayer は Convallaria majalis とその品種だけで、種が違う。RHS の Convallaria keiskei は名前だけの登録）、コリダリス 'Silver Spectre'（RHS のページだけ。未確定）、グロブラリア トリコサンタ（おぎはら・Gaißmayer は別の種だけ。RHS は名前だけ）、セラスチウム・ヤナギラン・ペロフスキアの Gaißmayer（品種のページだけ）
- 耐暑性 弱 の1品種：アンテミス ティンクトリア 'Alba'（MBG の種のページ：米国深南部の高温多湿に耐えない。蒸れ耐性も 弱）
- 蒸れ耐性 弱 の2品種：アンテミス 'Alba'、セラスチウム トメントサム
- おぎはらと欧米の文献の食い違い：バレリアン（おぎはら 強／MBG：夏の涼しい気候でよく育つ＝弱 相当）、ヤナギラン（中／NC State：暑い南部の夏では苦しむ＝弱 相当）、セラスチウム（中／MBG・NC State：高温多湿の夏の気候ではよく育たない＝弱 相当）、'Chocolate'（強／NC State：米国南東部では午後の日かげを好む＝中 相当）、コエレリア（強／NC State：暑い時期は半ば休眠することがある＝中 相当）
- 耐暑性が空欄の6品種：コリダリス 'Silver Spectre'、スズラン、グロブラリア、オルラヤ、ミントブッシュ、クリーピングセボリー。スズラン（17項目）・グロブラリア（15項目）・テンニンソウの黄金葉（14項目）・コリダリス（10項目）は、ほかの項目も空欄が多い
- ユーザーに聞くこと・伝えること（学名の検討に出る）：(a) 'Chocolate' は、商品名が「ユーパトリム ルゴサム」、マスターの学名は Ageratina altissima 'Chocolate'（RHS・MBG・stauden.de・Gaißmayer と同じ。おぎはら・Walters・Jelitto は Eupatorium rugosum）。ユーパトリウムのまとまり（batch_11）とは別の属名になっている (b) アンテミス ティンクトリアは RHS の正名が Cota tinctoria（'Alba' は名前だけの登録）。'Alba' は 2006年に Jelitto が発表 (c) ヤナギランは RHS の正名が Chamaenerion angustifolium、おぎはら・Jelitto・stauden.de は Epilobium (d) ロシアンセージは RHS の正名が Salvia yangii (e) セリナム ウォリキアナムは RHS でシノニム扱い (f) コリダリス 'Silver Spectre' は RHS で未確定。MBG・stauden.de・おぎはら・Gaißmayer・Jelitto に名前がない (g) スズラン（Convallaria keiskei）は、YList の和名がスズラン。RHS は Convallaria majalis var. keiskei をシノニムとしている (h) オルラヤは1〜2年草の扱い（おぎはら：基本的に1〜2年草扱いで、こぼれ種でよく増える。Jelitto：Biennial。Gaißmayer：一年草で、こぼれ種で続く） (i) シカゴ植物園：'Chocolate' は総合評価 ★5（26種類のうち最高評価の4つの1つ）。夏のいちばん暑い日や土が乾いたときは、しおれることが多かった。こぼれ種で増えたが雑草になるほどではない。同じ試験で、緑葉の種そのものは ★2 (j) Gaißmayer：アンテミス 'Alba' は Z6・「花後に半分まで切ると株が長もちし、こぼれ種も抑えられる」、セファラリアは「合う場所ではこぼれ種でよく増える。早めの切り戻しで抑えられる」、コエレリアは「肥えた土では短命」、クリーピングセボリーは Z6・冬のあと地際まで切り戻す・芽出しが遅い、バレリアンは Z6 (k) Jelitto：ヤナギランは地下のランナーと種子で速く増える、ロシアンセージは「暑さと乾燥に強い」（記録だけ）、クリーピングセボリーはゾーン6〜9、セリナムはゾーン6〜9

## 2026-11-21：耐暑性の指針と、おぎはらの楽天の商品ページ（全品種に反映済み）
- 決まったことは DECISIONS.md「2026-11-21 の決定」。ここには、確かめたことと手順を書く
- おぎはらの耐暑性の定義は、図鑑のサイト（ogis.co.jp の図鑑・Q&A・コラム・会社案内）にはなく、楽天のお店の商品ページに共通の説明として書いてある（原文は DECISIONS.md）。会社案内には「栽培場は高冷地ながら、栽培施設内は40℃を超える日もありますが、冷房は使用しておりません」とある
- 楽天の商品ページの読み方：図鑑のページ（page01.php?id=）の中に「カタログ品番；31L」があり、https://item.rakuten.co.jp/ogis/31l/ で開ける（curl で読める。文字コードは EUC-JP）。図鑑から楽天へのリンクがあるのは販売中の品種だけだが、売り切れの品種もページが残っていることが多い
  - scripts/tools/ogi_shop.py が、各 batch と scripts/pilot の ogihara_data.py にある図鑑のIDを順に読む（2.5秒おき。取得済みは飛ばす）。結果は ogihara_shop.json（図鑑のID → 耐暑性・株張り・日照〔寒冷地／暖地〕・土の水分・耐乾性・耐湿性・剪定・増殖・消毒。価格・在庫は入れていない）
  - 2026-11-21 に読んだ結果：図鑑のページ 363 のうち、楽天にページあり 294・なし（404）69。品種では 412 のうち 323。アクセス制限のような応答は出なかった
  - ogihara_data.py の376件で、ogihara_data.py に書いた耐暑性と、今の図鑑の値を照らした。違いは 0
- 楽天のページで分かったこと（323品種）：耐暑性は図鑑とほぼ同じ（違いは3品種：Th04 タリクトラム デラバイ 'Album' は図鑑 中・楽天「弱い（夏期冷涼な地域に向く）」、Rn01 カラスバ ヒメリュウキンカは図鑑 強・楽天「普通（暖地では夏に風とおし、水はけよく）」、G02 ゲラニウム エンドレッシーは図鑑 中・楽天「強い」。控えめな側を採った）。「高温多湿を嫌う」などの一言がある品種 141、寒冷地と暖地で日照が違う品種 143（うち暖地が日かげ寄り 137。多いのは「昼過ぎから半日陰が理想」49）、耐乾性は全品種に5段階で書いてある
- assemble_pilot.py に入れたこと：ogihara_shop.json を読み、DECISIONS.md の決め方で耐暑性・蒸れ耐性・西日耐性・乾燥耐性に当てる（shop_heat・shop_muggy・shop_west・shop_dry）。列を3つ足した（「蒸れ耐性（欧米の文献だけなら）」「西日耐性（おぎはらの暖地の日照を入れる前）」「乾燥耐性の出どころ」）。根拠の行は6行から9行までに増やした。西日耐性の ◎（日向・耐暑性 強・乾燥耐性 強）は、おぎはらで乾燥耐性を埋める前の値で決めている
- 同じときに直したこと：(1) 「Foliage tends to decline by late summer」（アスター コルディフォリウス）が暑さ 中 に当たっていたので、暑さの語がないときは使わないようにした (2) 和名の拾い方で、引用符のある行（Hosta sieboldiana … 'Hypophylla'）を種そのものの行にしないようにした。どちらも、今の下書きの値は変わらない（直す前の組み立てで、3属の試行とアスターを作り直したときにだけ出た）
- scripts/tools/rediff.py を作り直した：3属の試行（pilot）とアスター（aster）も対象に入れ、耐暑性・蒸れ耐性・西日耐性・乾燥耐性・「欧米の文献だけなら」・和名を比べる。`--save 1121` を付けると、作り直した Excel と JSON を、末尾を _1121 に替えた名前で ClaudeWork に置く
- 確かめたこと：楽天のデータを入れる前の組み立てで、19個のまとまり（916品種）すべてが手元の下書きと同じ値になった（3属の試行とアスターは「欧米の文献だけなら」の列が増えただけ）。入れたあとに作り直した下書きは、試しの一覧（`ClaudeWork/試し_おぎはら楽天_蒸れ・西日・乾燥_323品種_1121.xlsx`）の案と同じ値になった。違いは耐暑性の6品種だけ：G02（上の「控えめな側」）と、ゲラニウム ファエウムの5品種（G16〜G20。試しの一覧を作ったとき、3属の試行の下書きに「欧米の文献だけなら」の列がなかったため。今の決め方では 強 → 中）
- 反映した結果（916品種。かっこ内は反映する前）：耐暑性 強 399（420）・中 234（214）・弱 68（67）・空欄 215（215）、蒸れ耐性 強 74（83）・中 175（91）・弱 118（68）・空欄 549（674）、西日耐性 ◎77・○246・△203・×209・空欄 181、乾燥耐性 強 202・中 199・弱 119・空欄 396（572）。変わった数：耐暑性 22、蒸れ耐性 138、西日耐性 54、乾燥耐性 176（どれも空欄を埋めたか、控えめな側に動いた）
- 耐暑性が 強 → 中 になった20品種は、下書きの「耐暑性の決め方」が「…＋楽天のページの注意（強 → 中）」の行
- 下書き：19個のまとまりすべてを、末尾 _1121 の名前で作り直した（`ClaudeWork/試行_3属78品種_1121.xlsx`、`下書き_アスター23品種_1121.xlsx`、`下書き_…_1121.xlsx`。前のファイルは残してある）。3属の試行とアスターも、今の照合で作り直してある
- まだ使っていない楽天の項目：株張り（今が空欄で、品種のページに値があるのは20品種）、土の水分、剪定、増殖、消毒
- 楽天にページがなかった89品種は、今までどおり（図鑑の耐暑性だけ）

- 残っていた4つの判断もユーザーが回答した（DECISIONS.md「耐暑性で残っていた判断」）。耐暑性の決め方はこれで確定
  - assemble_pilot.py に「耐暑性の信頼度」の列を足した。916品種で 高 106・中 457・低 138・空欄 215（低 の内訳は、同じ種の別品種から 82、欧米の属の記述だけ 56）
  - 「耐暑性 強・欧米だけなら 弱」のまま残る23品種：ロニセラ ペリクリメナム2、リグラリア デンタータ2、カラミンサ 'Blue Cloud'、フェスツーカ グラウカ2、スティパ テヌイッシマ、ビバーナム 'Onondaga'、クナウティア マケドニカ2、ムクデニア 'Karasuba'、セスレリア、バレリアン、ホタルブクロの仲間6、カレックス 'Evergold'、トロリウス チネンシス 'Golden Queen'、モリニア1（ID は Lo03・Lo04・Lg01・Lg02・Ca02・Fe02・Fe03・Su02・Vu02・Kt01・Kt03・Mk02・Se01・Va01・C17〜C22・X07・Tr01・Mo06）
  - 下書きは、列を足した形で末尾 _1121b の名前で作り直した（値は _1121 と同じ。最新は _1121b）

## 2026-11-21：「現物と学名の確認」の回答を反映
- チェックリスト（非公開の Artifact。24件。備考欄つき）の回答は DECISIONS.md「現物と学名の確認」の回答。ここには、調べたことと直した場所を書く
- 【input を手で直した】4品種。どれも学名の列はマスターのままで、JSON に「手で直した」の欄を足してある。make_input.py で作り直すと元に戻る
  - batch_04/input/D10.json：species を Sedum reflexum、品種名なしに
  - batch_11/input/Ep01.json：species を「Eupatorium hybrid」に（種が未確定で、種の文献を当てないため）
  - batch_17/input/Se01.json：species を Sesleria argentea に
  - batch_17/input/Pq01.json：品種名なしに
  （前からの1品種：batch_17/input/To01.json の species を Tovara virginiana に）
- セダム レフレクサム（D10）で読んだ文献：おぎはら「セダム レフレクサム Sedum reflexum(rupestre)」（図鑑のID 2881。耐暑性 強）、RHS「Sedum reflexum L.」（番号 16983。シノニム扱い）、MBG「Sedum rupestre」、NC State（sedum-rupestre）、stauden.de「Sedum reflexum」、Walters（sedum-reflexum）、Gaißmayer「Sedum rupestre（Tripmadam）」（商品 9235。Z4）、Jelitto「SEDUM reflexum (rupestre, PETROSEDUM)」。Gaißmayer と Jelitto は Chrome で4ページだけ読んだ（最初の1ページで確認画面が出たが、数秒で通った）。fetch_all.py にセダム レフレクサム＝Sedum rupestre・Petrosedum を足した。D10 の耐暑性は 中 → 強（'Vera Jameson' の文献が外れ、おぎはらの値になった）
- ミスカンサス 'Purpurascens'（Mi05）で確かめたこと：MBG は「Miscanthus sinensis 'Purpurascens' と同じもので、その名前で売られることもある。ただし、sinensis の品種でも変種でもなく、親の分からない交配種で、M. 'Purpurascens' と書くべきだとする専門家もいる」と書いている。RHS は Miscanthus 'Purpurascens'（種小名なし）で、シノニムに Miscanthus oligostachyus 'Purpurascens'・Miscanthus sinensis 'Purpureus' などを挙げている。マスターの学名（Miscanthus sinensis 'Purpurascens'）は流通している書き方の1つ。ユーザーの回答どおり、ススキの仲間として扱う（耐暑性は同じ種の別品種から。信頼度：低）。学名（採用）は RHS の表記の Miscanthus 'Purpurascens'
- ジプソフィラ「ローザス コーンヘッド」（Gy03）：Web で「Rosa's Conehead」「Rosas Conehead」「ローザス コーンヘッド」を検索したが、この名前の品種のページは見つからなかった（2026-11-21）。種の記述だけを当てたまま
- アスクレピアス 'Milkmaid'（Ak03）：ユーザーが指定したページ（plantlust。Select Seeds の説明を載せている）は、Asclepias incarnata 'Milkmaid' を白花・香りのある品種として載せている（高さ 36〜60 in、花期は夏）。'Ice Ballet' と同じかどうかは書いていない。Jelitto は 'Iceballet' の別名に Milkmaid を挙げている。当て方は変えていない
- セスレリア（Se01）：Sesleria argentea として、MBG・NC State・stauden.de・YList を探したがページはなかった。使っている文献は、おぎはら（図鑑と楽天）・Jelitto（SESLERIA argentea）・RHS（名前だけ）。蒸れ耐性 弱 と「欧米の文献だけなら 弱」は消えた（どちらも autumnalis の記述だった）
- 値が変わったのは3品種：D10（耐暑性 中 → 強、西日 ○ → ◎）、Vs01（耐暑性 強 → 空欄、西日 ○ → 空欄、乾燥耐性 弱 → 空欄。おぎはらのクガイソウを外したため）、Se01（蒸れ耐性 弱 → 空欄、西日 ◎ → ○、乾燥耐性 強 → 中）
- 学名（採用）の決め方を変えた（assemble_pilot.py の adopt_name。チェックリスト 21〜24）。前は、RHS が正名でも rhs_ids.py にメモのある品種は直していなかった。今は直す
  - 学名（採用）が変わったのは 126品種（RHS の表記にしたもの：属が変わる、種小名を付けない、流通名 → 品種名、つづり、× の書き方など。ユーザーの回答で直した D10・Pq01・To02 を含む）
  - 直さずに検討に残したのは 22品種（学名（採用）の列に理由を書いてある）：RHS が別の品種名を正名としているもの（Dg05・Dg08・Dg09・Ps02・Gy04・Eg01・Gl03・Op01・F14・S14・Fi04・Li06・Mn01）、RHS の種がマスターと違い、ほかの文献で確かめられないもの（Hd02・S04・D02・Me08・Sa04・Ne09・A05・A07）、フクシア 'Variegata'（Fu05）。ユーパトリウム 白花（Ep01）は学名を直さず、種が未確定と書いてある
  - 「2つ以上の文献がそろえば直す」で種が変わったのは8品種：ガイラルディア3（aristata → × grandiflora）、カレックス X12（talbotii → berggrenii）、ポレモニウム 'Apricot Delight'（caeruleum → carneum）、スカビオサ オクロレウカ2（→ columbaria subsp. ochroleuca）、ネペタ 'Felix'（× faassenii → racemosa）。文献の当て直しは下の項目
- 種が変わった品種の文献を当て直した（2026-11-21。ユーザー：「当て直す」）
  - 【input を手で直した】6品種の species（学名の列はマスターのまま。JSON の「手で直した」に理由）：batch_02 X12（Carex berggrenii）、batch_07 Pl03（Polemonium carneum）、batch_09 Ne01（Nepeta racemosa）、batch_15 Gl01・Gl02・Gl03（Gaillardia grandiflora）
  - スカビオサ オクロレウカ（Sc06・Sc07）は、RHS の書き方（Scabiosa columbaria subsp. ochroleuca）が同じ種の別の書き方なので、種は変えていない（fetch_all.py の SPECIES_ALIAS に足した）
  - ネペタ 'Felix'（Ne01）：おぎはらの × faassenii の種のページを外した。耐暑性は 強 → 弱（MBG の Nepeta racemosa：米国深南部の暑さと湿気にやや耐えない。暑い夏の気候では午後の軽い日かげを好む）、西日 ◎ → △
  - ガイラルディア3品種（Gl01〜Gl03）：耐暑性 強 → 空欄、西日 → 空欄、乾燥耐性は 中（NC State の × grandiflora：根づけばいくらかの乾燥に耐える）。前の 強 は、MBG・NC State のアリスタータ（種）の記述（暑く乾いた場所でよく育つ）から来ていた。× grandiflora の種のページ（NC State・stauden.de。MBG はなし）には暑さの記述がない
  - ポレモニウム 'Apricot Delight'（Pl03）：カエルレウムの記述が外れ、「欧米の文献だけなら 弱」が空欄、蒸れ耐性 弱 → 中、西日 × → △、和名（ヨウシュハナシノブ）が空欄になった。耐暑性 中（おぎはら）は同じ
  - カレックス X12：stauden.de に Carex berggrenii のページがあった（MBG・NC State の種のページはなし）。値の変化はなく、空欄は15項目のまま
- 下書きは末尾 _1121d の名前で作り直した（最新は _1121d）

## 2026-11-21：全916品種を1つの表にまとめた
- scripts/pilot/combine.py が、まとまりごとの下書き（19個。名前の末尾がいちばん新しいもの）を、試作28品種のマスター（`ClaudeWork/試作マスター_28品種_1119c.xlsx`）と同じ列の並びの1つの表にする
  - 実行：`python -X utf8 scripts/pilot/combine.py <ClaudeWork> <元のマスター.xlsx> <試作マスター.xlsx> <出力.xlsx>`
  - 出力：`ClaudeWork/新マスター_下書き_916品種_1121.xlsx`（リポジトリには入れない）。並びは元のマスターの順。価格・在庫数は入れていない（在庫の有無だけ）
  - シート：マスター（下書き916品種）・根拠（13,655行）・学名の検討（503品種）・列ごとの埋まり具合・まだ作っていない列・この表について
  - 花期・草丈・耐寒性・流通名は今のマスターから（花期と草丈の読み方は試作の scripts/assemble.py と同じ）。景観構成用途は草丈の最大から（前景 〜40、中景 40〜90、後景 90以上）。外来種リストは試作マスターの「外来種リスト該当（全商品）」のシートから（該当15品種）
  - 「暑さ・蒸れの注意」には、下書きの「文献の注意」（シカゴ植物園の試験の記録など）を入れた
- 値のある品種の数（916品種中）：学名（正名）916、日照 863、土壌水分 855、主な病害虫 841、常緑性 839、USDA 759、株張り 743、西日耐性 731、葉色 729、増え方 725、耐暑性 697、花色 690、切り戻しの方法 690、繁殖方法 687、乾燥耐性 521、蜜源 513、和名 460、切り花 380、蒸れ耐性 366、原産地 271（2026-11-23 に Kew で 728）
- 【まだ作っていない列】試作マスターにはあるが、全品種の下書きにはない19列（表では空欄。理由は表の「まだ作っていない列」のシート）：科名、葉の特徴、香り、成株シルエット、pH・土質、耐潮性、こぼれ種の量、地下茎で広がる程度、混植適性、広がりすぎの注意、毒性、管理タイプ、管理難易度、切り戻し時期（広尾町・関東）、株分けの間隔、機能用途タグ、デザイン系タグ、リスクタグ
  - このうち、読んだ文献にもとの情報があるもの：香り・毒性（Gaißmayer の Duftend・Giftklasse、Jelitto の toxic plant、RHS）、pH・土質（RHS）、こぼれ種・地下茎（stauden.de・Gaißmayer の記述）、科名（RHS の Family、Gaißmayer の Familie）
- ミントブッシュの種は「分からない」で確定（DECISIONS.md）

## 2026-11-21：科名・香り・毒性・pH・土質・こぼれ種・地下茎の列を作った
- ユーザーの指示（「5つを先に作る」）。scripts/pilot/extra_cols.py に決め方をまとめ、assemble_pilot.py から呼ぶ。下書きに7列が増えた（科名・香り・毒性・pH・土質・こぼれ種の量(0-3)・地下茎で広がる程度(0-3)・こぼれ種・地下茎の根拠）。決め方は trial/RULES.md に合わせた
  - 科名：RHS の Family → MBG → NC State → stauden.de の順。和名の科名は extra_cols.py の対応表（APG の科。Hosta・Liriope などはキジカクシ科、Sedum はベンケイソウ科）
  - pH・土質：RHS（pH の欄と、Growing Conditions の Chalk・Clay・Loam・Sand）→ NC State（Soil pH・Soil Texture）→ Walters の順
  - 香り：RHS（Colour & Scent の Fragrance）・MBG（Flower／Leaf の Fragrant）・NC State（Flower／Leaf Value To Gardener）から「花／葉／花と葉」。Walters・Gaißmayer・stauden.de は部位が分からないので「あり（部位の記述なし）」。品種のページ（品種名のない商品は種のページ）だけ使う
  - 毒性：RHS（Potentially harmful）→ NC State（Poison Severity・Poison Part）→ Gaißmayer（Giftklasse）→ Jelitto（toxic plant）の順。種のページも使う
  - こぼれ種・地下茎：言い回しの照合（英語は NC State → MBG → Walters、ドイツ語は stauden.de の Wuchsverhalten・Pflegehinweis と Gaißmayer の本文）。最初に記述のあった文献の値を採り、ほかの文献が違う値のときは根拠の列に「食い違い」と出す。属のページの記述は使わない。0＝広がらない・種ができないと明記、1＝少し、2＝よく、3＝はびこる
- 値のある品種（916品種中）：科名 911、pH・土質 857、地下茎 363（0：26、1：91、2：168、3：78）、こぼれ種 362（0：22、1：288、2：47、3：5）、香り 183（葉 73・花 57・花と葉 19・部位の記述なし 34）、毒性 148
- 【人が確かめること】こぼれ種・地下茎は言い回しの照合なので、取り違えがありうる。何度か抜き出して直した（害虫の「difficult to eradicate」、属の一般的な注意、「does not spread aggressively」、手でまき直す意味の reseeding、「ohne lästig zu werden」）。根拠の文を「こぼれ種・地下茎の根拠」の列に出してある。種のページから決めた値は、品種でも同じとは限らない（不稔の品種など）。こぼれ種 1 の多くは「花後に切るとこぼれ種を防げる」という文から
- 【見つけたこと・まだ使っていない】NC State のページには「Resistance To Challenges」という項目があり、Heat・Humidity・Drought などが並んでいる（例：レモンバームは Deer; Drought; Dry Soil; Heat; Humidity; …）。RHS には「Drought Resistance: Yes」の項目がある。試しの一覧（`ClaudeWork/試し_NC Stateの強い項目_1121.xlsx`。336品種）をユーザーが見て、乾燥耐性の空欄だけ 中 で埋めると決めた（DECISIONS.md）。耐暑性・蒸れ耐性には使わない。項目は下書きの2つの列（NC State の Resistance To Challenges・RHS の Drought Resistance）に記録してある
- 乾燥耐性の空欄 91品種に 中 が入った（NC State の種のページ 72・品種のページ 2、RHS 17）。乾燥耐性は 強 200・中 294・弱 118・空欄 304 になった。ほかの値は変わっていない
- 下書きは末尾 _1121f の名前で作り直した（最新は _1121f。_1121e は列を足しただけで、耐暑性などの値は _1121d と同じ）。まとめの表 `ClaudeWork/新マスター_下書き_916品種_1121.xlsx` も作り直した（まだ作っていない列は13）

## 2026-11-21：ほかの列から決める列を、まとめの表に作った
- ユーザーの指示（「6列を作る」）。scripts/pilot/combine.py の中で、試作の scripts/assemble.py・trial/RULES.md と同じ決め方で作る（下書きの列は増やしていない）：管理タイプ、管理難易度、切り戻し時期（広尾町・関東）、機能用途タグ、デザイン系タグ、リスクタグ。景観構成用途にも「グラウンドカバー」「主役（単植向き）」「群植向き」を足した
  - 管理タイプ：E 隔離推奨型＝地下茎かこぼれ種が 3。B 花後刈込型＝切り戻しに「花後」。A 放任型＝切り戻しが「不要」「早春」「秋」だけ。切り戻しの記述がなければ空欄
  - こぼれ種 3 が種の記述だけのときは、品種を E にしない（スピレア 'Goldflame' の決定と同じ考え方）。地下茎 3 は種の記述でも品種に当てる（アジュガ 'Burgundy Glow' の決定と同じ考え方）。どちらも「管理タイプのメモ」の列に書く
- 【精度が低い】管理タイプは、試作28品種（人が文献を読んで決めた）と比べると、同じだったのは25品種中14品種。主な理由：(1) C 夏前切戻型・D 毎年株更新型は、もとになる記述（初夏の切り戻し、毎年の株分け）を全品種では拾っていないので付かない（試作では C が4、D が1）(2) 切り戻しの「花後」「不要」は RHS の Pruning の欄からの照合で、試作のときの読み方と違うことがある (3) 地下茎・こぼれ種の 3 が言い回しの照合。管理難易度は 25品種中17品種、リスクタグは 22品種が同じ
- 結果（916品種）：管理タイプ B 452・A 183・E 約80・空欄 約200、管理難易度 中・易・難、機能用途タグは 831品種、デザイン系タグは 298品種に値がある。数は表の「列ごとの埋まり具合」のシート
- 付いていないタグ：成株シルエットと耐潮性がまだないので、「ロックガーデン向き」「海辺向き」「水辺向き」と、シルエットから決める分
- まとめの表でまだ空欄の列は6つ：葉の特徴、成株シルエット、耐潮性、混植適性、広がりすぎの注意、株分けの間隔（どれも、文献の本文を読んで人が書く列）

## 2026-11-21：切り戻しと株の更新の記述を読み直した（管理タイプ C・D）
- ユーザーの指示（「読み直す」）。scripts/pilot/extra_cols.py の prune_extra が、MBG・NC State・Walters の本文、RHS の Pruning・Cultivation、Gaißmayer の切り戻しの文、おぎはら（図鑑と楽天の「剪定」）から、次の2つを言い回しの照合で拾う。下書きに3列が増えた（夏前の切り戻し・毎年〜2年ごとの更新・切り戻し・更新の根拠）
  - 夏前の切り戻し（C のもと）：夏に葉が傷んだら／倒れたら切り戻す、切り戻すと新しい葉が出る、初夏に草丈を詰める、梅雨前・夏前・蒸れ対策の切り戻し。209品種 → 決まった文を外して 150品種前後
  - 毎年〜2年ごとの更新（D のもと）：divide every year／every two years、each year に地際まで切る、など。4品種（セラスチウム、ゲウム 'Fireball'、アンテミス 'Alba'、エルショルチア）
  - 外したもの：おぎはらの楽天の「伸びすぎて姿が乱れたら株元まで短く切ると、再び芽吹き、姿が整う」（多くのグラスに付いている決まった文）、RHS の「mulch annually or lift and replant」（annually はマルチにかかる）
- combine.py の管理タイプは、上から E・D・C・B・A の順で決める。結果（916品種）：B 351、A 156、C 142、E 79、D 4、空欄 184。管理難易度は 中 522・易 120・難 93・空欄 181
- 【精度は上がっていない】試作28品種と同じだったのは、管理タイプが25品種中14品種のまま（管理難易度は18品種）。C が付くようになって合った品種（アキレジア 'Yellow Queen'、サルビア 'Caradonna' など）がある一方、試作では B だったのに C になった品種（ヒューケラ 'Green Spice'、アルケミラ サクサティリス、アキレア 'Love Parade'）が出た。「花後に切り戻すと新しい葉が出る」を C と読むか B と読むかの線が、試作のときの人の読み方と機械の照合で違う。コルヌス 'Sibirica'（試作は D）、ホトトギス（試作は A）、スピレア（試作は B）は、切り戻しの記述を拾えていない
- 管理タイプは「目安」として扱い、根拠（切り戻し・更新の根拠、こぼれ種・地下茎の根拠、管理タイプのメモ）を見て直す前提。試作のような精度にするには、品種ごとに文を読んで決める必要がある
- 下書きは末尾 _1121g の名前で作り直した（最新は _1121g。耐暑性などの値は変わっていない）。まとめの表も作り直した

## 2026-11-21：まだ空欄だった6列を作った（成株シルエット・葉の特徴・耐潮性・株分けの間隔・混植適性・広がりすぎの注意）
- ユーザーの指示（「上から三つを行いたい、上から順番に」の1つ目）。scripts/pilot/extra_cols.py の six() に決め方をまとめ、assemble_pilot.py から呼ぶ。下書きに12列が増えた（6列と、根拠・参考の列）。決め方は trial/RULES.md（silhouette・foliage_features・salt・division_interval・mixing・invasive_note）に合わせた。新しく文献は読んでいない（読んである文献だけ）
  - 成株シルエット：RHS の Habit（Climbing・Matforming・Trailing・Columnar upright）→ NC State の Habit/Form → MBG・Walters の本文の語（mound・upright・arching・mat-forming など）→ stauden.de の Wuchsform → RHS の Habit（Clump forming・Bushy など → 株立ち）の順。イネ科・カヤツリグサ科は、直立・マットと書かれていなければ グラス。品種のページ（品種名のない商品は種のページ）だけ（RULES.md）。種のページからの値は「成株シルエット（種の記述なら）」の列に参考として出す
  - 葉の特徴：stauden.de の Blatteigenschaften・Blattrand・Blattspreite・Blattform・Blattschmuck と、NC State の Leaf Feel・Leaf Margin・Leaf Type・Leaf Shape の用語を日本語に置きかえて並べた（対応表は extra_cols.py の LEAF_DE・LEAF_NC）。品種のページだけ。斑の入り方の細かい説明（Walters の本文など）は拾っていない
  - 耐潮性：本文の記述（salt tolerant・salt spray・seaside gardens など → ◎、slightly／moderately → ○、low → △、not → ×。割れたら控えめな側）。本文になく、項目だけのとき（RHS の植える場所の Coastal、NC State の Resistance To Challenges の Salt・Landscape Location の Coastal）は ○ で、根拠に「項目だけ」と書く。属のページは使わない
  - 株分けの間隔：RHS（Propagation・Cultivation）→ NC State → MBG → Walters の順に「every 3-4 years」などの文を探し、なければ株分けの時期だけ（「春または秋（間隔の記載なし）」）。stauden.de の Pflegehinweis の2つの決まった文（2〜4年ごとに分けて植え直す／長生きで、長年植え替えない方がよい）も使う
  - 混植適性：侵略的＝地下茎かこぼれ種が 3、または文献に invasive／aggressive の明記（庭での広がり方として）。強い＝「somewhat aggressive」「in optimum conditions」など条件つきの書き方、vigorous spreader・crowd out、吸枝で取り除きにくい、stauden.de の Wuchsstärke: wuchernd。弱い＝weak grower など（当たった品種はなし）。普通＝地下茎が 0〜1、または stauden.de の Wuchsverhalten が株立ち（horstig）だけで、上の記述がない。どれでもなければ空欄
  - 広がりすぎの注意：決まった文に当てはめた（地下茎・ランナーでよく広がる／強く広がり、はびこることがある、こぼれ種でよく増える、MBG の注意書き（Notice・Invasive の表示）、NC State の表示（Invasive Species・Weedy）、stauden.de の wuchernd、おぎはら楽天の注意書き、環境省の外来種リスト）。種の記述から品種に当てた分には「この品種で同じかは未確認」と付く
- 【こちらで置いた線引き。ユーザーの確認はまだ】
  - 「米国の州・オーストラリアなどで侵略的外来種とされている」という地域の話（MIX_ECO）は、庭での広がり方ではないので、混植適性は決めず、広がりすぎの注意にだけ書く（試作のススキ 'Morning Light' は 普通、スピレア 'Goldflame' は空欄だった）
  - こぼれ種によるもの、または種のページの「侵略的」で広がり方の語（rhizome・stolon・sucker など）がない文は、品種には当てない（注意にだけ書く）。地下茎・ランナーによるものは、種の記述でも品種に当てる（アジュガ 'Burgundy Glow' の決定と同じ考え方）
  - 「weedy」だけの文は 侵略的 にしない
  - combine.py の管理タイプ E は、今までの「地下茎かこぼれ種が 3」に、混植適性が 侵略的（文献に明記）を足した（RULES.md の「E: mixing が 侵略的」）。E は 79 → 90。足されたのは11品種：ヘデラ3、リシマキア ヌンムラリア2、エキナセア パリダ、バレリアン、ユーパトリウム コエレスティナム、アルテミシア ブルガリス、ススキ（種）、イトススキ。ススキは米国での話（風で飛ぶ種で侵略的）がもとなので、日本では見直しの候補
- 値のある品種（916品種中。かっこ内は在庫のある634品種）：成株シルエット 791（547）、混植適性 601（406）、株分けの間隔 598（420。うち「○年ごと」の記述あり 154、時期だけ 401）、葉の特徴 579（400）、広がりすぎの注意 334（241）、耐潮性 298（208。◎ 51・○ 245・× 2。○ のほとんどは項目だけ）
  - 成株シルエット：株立ち 278、ドーム 189、直立 126、マット 105、グラス 51、ロゼット 17、アーチ 16、つる 9。混植適性：普通 488、侵略的 90、強い 23
- 【精度】試作28品種（人が文献を読んで決めた）と比べると：成株シルエットは 23品種中18品種が同じ、混植適性は 20品種中18品種、耐潮性は 13品種中6品種
  - 成株シルエットの違い：アルテミシア 'Nana'（試作 ドーム。RHS の Habit は Matforming で、試作では全体の形から人が ドーム と判断）、アキレア（試作 直立／今 株立ち）、オミナエシ（試作 株立ち／今 直立）、スピレア・エゾアジサイ（試作 株立ち／今 ドーム）
  - 耐潮性の違いは、試作のときに読んだ Walters の「Salt Tolerant」の項目が、今の生データのページにない（3ページだけ）ことと、ホスタの属の記述を今回は使っていないことによる。試作 ◎ が今は ○ か空欄になる向き（控えめな側）
  - どの列も言い回し・用語の照合で作った目安。直したもの：花の説明（domed umbels・pincushion・upright stems of flowers）を株の形と読んでいた、「not inclined to be invasive」「without becoming weedy」など打ち消しの文を 侵略的 と読んでいた、「becomes difficult to remove」（壁に付いたツタ）
- 同じときに直したこと：地下茎の照合で、ホスタの MBG のページに共通の文「central rhizomatous crown」（株の中心の形の説明）は広がり方の記述にしない（_en）。今の下書きの地下茎の値は変わらなかった（同じ文のほかの語で当たっているため。ホスタの地下茎 2 は見直しの候補のまま）
- combine.py：6列を下書きから入れ、見返し用の列を6つ足した（成株シルエット（種の記述なら）・成株シルエットの根拠・葉の特徴（種の記述なら）・耐潮性の根拠・株分けの間隔の根拠・混植適性の根拠）。試作と同じ決め方のタグも付くようになった：グラウンドカバー（マット）、主役（グラス・アーチで草丈60cm以上）、海辺向き（耐潮性 ◎）、ロックガーデン向き（マット・ドームで乾燥耐性 強、土が排水必須・乾燥寄り）、リスクタグの 要管理（混植適性が 侵略的・強い）。「水辺向き」だけは、もとになる列がまだない
- 下書きは末尾 _1121h の名前で作り直した（最新は _1121h。耐暑性など今までの列の値は変わっていない）。まとめの表は `ClaudeWork/新マスター_下書き_916品種_1121b.xlsx`（前の _1121.xlsx は残してある）。まとめの表でまだ空欄の列はなくなった（夏越し実績（自社の実測）を除く）
- 【見つけたこと・ユーザーに伝える】おぎはらの楽天のページ（エゴポディウム 'バリエガータ'。商品番号 38、在庫あり）に「本種は北海道内のみ特定外来種の指定があります。私有地内で園芸用に育てることは問題ありませんが、自然界に放つと罰則があります」という注意書きがある。北海道の条例の指定かどうかは、まだ確かめていない（広がりすぎの注意の列に、おぎはらの文として入れてある）

## 2026-11-21：暑さに弱い品種の確認ページ（回答待ち）
- ユーザーの指示（「上から三つ」の2つ目）。非公開の Artifact「暑さに弱い品種の確認」 https://claude.ai/artifact/ETSmHmKSM416TBqk2PpmGZ （スマホ向け。備考欄つき。選ぶと回答の文ができるので、チャットに貼ってもらう）
  - 上の13問：耐暑性が「強のまま・欧米の文献だけなら 弱」の品種を、同じ種・同じ根拠ごとにまとめた（A 強のまま／B 中にする／C 弱にする）。欧米の文献の内容は日本語の要約を付けた
  - 下の一覧：耐暑性 弱 の69品種（在庫あり 47）と、蒸れ耐性 弱 の116品種（在庫あり 78。両方 弱 は34品種）。見るだけで、違うと思う品種だけ「違う」を押す形
- 「強のまま・欧米だけなら 弱」は、今の下書きでは 22品種（前の記録では 23。セスレリア〔Se01〕は、アルゲンティアとして当て直したときに「欧米だけなら 弱」が消えた）
- 作り方：まとめの表から3つの一覧を JSON に抜き出し（商品番号・植物名・学名・在庫の有無・耐暑性・蒸れ耐性・西日耐性・根拠。価格・在庫数は入れない）、scripts/tools/make_heat_page.py と heat_page_template.html で HTML にする（13問のまとめ方と日本語の要約は make_heat_page.py の GROUPS）
- 回答が来たら：DECISIONS.md に書き、品種ごとの上書き（assemble_pilot.py に、耐暑性・蒸れ耐性の手での上書きを足す）で反映する。まだ反映の仕組みは作っていない

## 2026-11-21：管理タイプを、在庫のある634品種で1品種ずつ見直した
- ユーザーの指示（「上から三つ」の3つ目。在庫のある品種から）。新しく文献は読んでいない
- 手順：(1) 下書きに「切り戻し・手入れの文（全部）」の列を足した（extra_cols.py の prune_all。RHS の Pruning・Cultivation・Propagation、MBG・NC State・Walters の本文のうち切り戻し・手入れ・株分けに触れている文、stauden.de の Pflegehinweis、Gaißmayer、おぎはら〔図鑑と楽天の剪定・増殖〕。属のページは除く）(2) 在庫のある634品種を学名の順に11組に分け、組ごとに補助のエージェントがその文を読んで、trial/RULES.md の management_type の決め方（上から E・D・C・B・A）で決めた。決め方の指示は一時フォルダの mt/BRIEF.md（要点：地域の話だけの「侵略的」は E にしない、種の記述のこぼれ種は品種に当てない、「花後に切ると新しい葉が出る」だけで夏の話がなければ B、stauden.de の決まった文の読み方、おぎはら楽天のグラスの決まった文だけでは C にしない）(3) 結果を master-rebuild/mgmt_review.json にまとめた（商品番号・type・codes〔切り戻しの区分〕・confidence・reason・quote。価格・在庫は入っていない）(4) combine.py が mgmt_review.json を読み、見直した品種はその値を優先する
- 確かめたこと：634品種すべてに結果があり、商品番号は組と一致。決め手の原文（quote）は全件、下書きの文の中にあった
- 結果（在庫のある634品種）：B 花後刈込型 320、A 放任型 132、E 隔離推奨型 79、C 夏前切戻型 70、D 毎年株更新型 3、空欄 30（手入れの文がない品種）。確かさは 高 337・中 228・低 69。言い回しの照合の値から変わったのは 257品種（うち、照合では空欄だったものに値が入ったのが 99）
  - 多かった変更：C → B（「花後に切り戻すと葉が新しくなる」だけで、夏の傷み・夏前の話がない。アキレア、プルモナリア、サルビア ネモローサ、ポレモニウム、ベロニカストラムなど）、B → A（グラス。花後の話は穂の色の説明の取り違えで、早春の刈り取りだけ。ススキ、モリニア、パニカムなど）、A → B（ホスタなど、花後に花茎を切る記述）
- 916品種では：B 437、A 175、C 117、E 97、D 5、空欄 85。在庫のない282品種は言い回しの照合のまま（目安。「管理タイプの決め方」の列で見分けられる）
- 【試作28品種との一致】見直した中に試作の品種が22あり、22品種とも試作と同じ値。ただし、エージェントには試作の28品種の値を線引きの参考として渡してあり、渡した文に決め手がないのに試作に合わせた品種がある（アルテミシア 'Nana' の C、コルヌス 'Sibirica'・'Elegantissima' の D、サルビア 'Caradonna' の C）。独立に確かめた精度ではない
- 【線引きがそろっていないところ。ユーザーに聞く】RHS が「剪定不要（No pruning required）」と書き、ほかの文献（stauden.de の決まった文、おぎはら楽天の「花後に花茎を切る程度」など）が花後の花茎切りを書いている品種。A にした組と B にした組がある（A 15品種・B 14品種。mgmt_review.json の no_prune_and_deadhead が true の行）。試作でも、アルメリア 'Variegata' は A、ホスタ 'Gold Standard' は B だった
- ほかに迷いが残るもの（確かさ 低 の69品種。理由は「管理タイプのメモ」の列）：RHS だけに「はびこるおそれがあるので容器で根域を制限」とあるミント5品種（E にした）、モナルダ3品種（「走出枝で急速に広がる」だけなので E → B）、ススキ（種）とネペタ ラセモサ（種）の E、摘心（pinch）を「初夏に草丈を詰める」と読んで C にしたカリメリス・ケロネ、同じ種で文の有無により値が分かれた品種（ベロニカストラム 'Album' だけ C、サポナリア、ヘレニウム）
- まだそろえていないこと：リスクタグの「要管理」と混植適性は言い回しの照合のままなので、見直しで E から外した品種（アルケミラ モリス、モナルダ、ペニセタム 'Black Beauty' など）にも付いている。逆に、見直しで E にした品種（ミントなど）の混植適性は変えていない
- 下書きは末尾 _1121i の名前で作り直した（最新は _1121i。「切り戻し・手入れの文（全部）」の列が増えただけ）。まとめの表は `ClaudeWork/新マスター_下書き_916品種_1121c.xlsx`（見返し用の列：管理タイプの決め方・管理タイプのメモ〔理由〕・管理タイプの決め手（原文）・管理タイプ（言い回しの照合）・切り戻し・手入れの文（全部））。見直した品種は、切り戻し時期も、読んで決めた区分から作っている

## 2026-11-21（夜）：確認ページの回答を表に入れる仕組みと、リスクタグ・混植適性のそろえ
- ユーザーの指示「取り掛かってください」（候補の 1〜3 のうち、2 と 3 をここに書く。1 は次の節）
- 回答を入れる仕組み：`python -X utf8 scripts/tools/apply_answers.py <回答の文を保存したファイル>`（master-rebuild で）。2つの確認ページの「回答の文」を読み、master-rebuild/user_answers.json に入れる（まだ回答がないので、このファイルはない）。combine.py がこれを読んで、文献より優先する
  - 暑さのページ：問題の番号から商品番号へは scripts/tools/heat_page_map.json（13問・22品種）。A＝強 のまま、B＝中、C＝弱。「耐暑性の決め方」に「ユーザーの確認（日付・問の番号）」と備考を書く。耐暑性が変わると管理難易度も作り直される
  - 暑さのページの「違うと思う品種」：値は変えない（「どう違うか」が自由に書く欄なので）。「耐暑性の決め方」か「暑さ・蒸れ・西日の根拠」に【要見直し】の印と、ユーザーの書いたことを足す
  - 剪定のページ：A・B はそのまま管理タイプにする（A なら切り戻しの区分から「花後」を除く、B なら「花後」を足す）。保留は値を変えず、「管理タイプの決め方」に「保留（あとで見直す）」と書く。備考は「管理タイプのメモ」に足す
  - 確かめたこと：試しの回答（暑さ・剪定の両方をまとめて貼ったもの）で、耐暑性・管理タイプ・管理難易度・切り戻し時期・決め方の列が書き換わり、ほかの列は変わらないことを見た。試しの回答のファイルは消した
- リスクタグと混植適性のそろえ（combine.py）
  - 「要管理（広がりやすい）」：管理タイプが E の品種にも付ける。言い回しの照合の「はびこる」（地下茎・こぼれ種が 3）は、文を読んで見直した品種では使わない。→ 見直しで E にしたミント5品種・プルネラ・リシマキア 'Alexander'・レプティネラ・サポナリア 'Rosea Plena' の9品種に新しく付いた
  - 混植適性：文を読んで E にしなかった品種で、「侵略的」が地下茎・こぼれ種の 3 だけによるものは「強い（周囲を圧迫、配置注意）」に下げた（アルケミラ モリス、モナルダ3品種、ペニセタム 'Black Beauty' の5品種。根拠の列に理由を書いた）。広がりやすいことは文献にあるので「要管理」のタグは残る
  - 見直しで E にした9品種の混植適性は空欄のまま（混植適性の文献の文がない。管理タイプの理由は「管理タイプのメモ」の列）

## 2026-11-21（夜）：在庫のない282品種の管理タイプも、1品種ずつ見直した（これで916品種すべて）
- ユーザーの指示「取り掛かってください」（候補の 1）。在庫のある634品種と同じ手順・同じ指示（mt/BRIEF.md）。新しく文献は読んでいない。学名の順に5組（chunk_12〜16）に分け、補助のエージェントが読んだ。同じ種で文が同じ品種は、在庫のある品種の結果（out_01〜11）と同じ値にするよう指示した
- 確かめたこと：282品種すべてに結果があり、商品番号は組と一致。決め手の原文（quote）は全件、渡した文の中にあった（1件は空白の違いだけ）。mgmt_review.json は916件・重複なし
- 結果（在庫のない282品種）：B 171、A 41、C 36、E 18、D 3、空欄 13（手入れの文がない）。確かさは 高 147・中 114・低 21。言い回しの照合の値から変わったのは 127品種
- 916品種では：B 491、A 173、C 106、E 97、D 6、空欄 43。管理難易度は 中 648・易 117・難 110・空欄 41。「要管理」のタグは125品種
- 混植適性のそろえ（combine.py）を広げた：見直しで E にしなかった品種の「侵略的」は、根拠が何でも「強い」に下げる（新しく当たったのはイトススキ 'Gracillimus' の1品種。こぼれ種の種の記述と「一部の地域で侵略的」だけ）。これで、E でないのに混植適性が 侵略的 の品種はない。E なのに混植適性が空欄の品種は12
- 【ユーザーに聞くこと】「剪定不要＋花後の花茎切り」の品種は、在庫のない品種にも17ある（mgmt_review.json の no_prune_and_deadhead が true の行は全部で46）。確認ページ（29品種）には入れていない（ページの選んだ値の保存が問題の番号で結び付いているので、途中で足すと、選んである値がずれる）。29品種の答えと同じ線引きで決めるか、あとで別のページで聞く
- エージェントが迷ったと書いたもの（確かさ 低 のほか）：ヤナギラン（MBG「庭で aggressive になりうる」で E。混植適性は空欄）、セラスチウム（「必要なら毎年株分け」を条件つきと読んで D にしない）、コルヌス セリセア 'Flaviramea'・アルバ 'Aurea'（文だけなら A だが、試作のコルヌスに合わせて D）、ツタ 'Fenway Park'（MBG「近くの管理されていない場所に侵略的に広がることがある」で E、広がり方は書いていない）、イベリス センペルビレンス（RHS「侵略的になりうる」だけで、広がり方がないので E にしない）、ビオラ ラブラドリカ（「ときに aggressive」で E にしない）、ニッポノキク・ネペタ 'Blue Dreams'・アガスターシェ 'Blue Fortune'（春の摘心・切り戻しを C と読んだ）
- まとめの表は `ClaudeWork/新マスター_下書き_916品種_1121d.xlsx`（「管理タイプの決め方」は916品種とも「文を読んで見直し」）

## 2026-11-21（夜）：エゴポディウムの「北海道の指定」を確かめた
- ユーザーの指示「次へ」（候補の 4）。おぎはら楽天のページの注意書き「本種は北海道内のみ特定外来種の指定」を、北海道庁の資料で確かめた
- 資料：北海道庁「指定外来種」のページ https://www.pref.hokkaido.lg.jp/ks/skn/shiteigairaishu01.html と、そこにある「指定外来種の指定一覧（R5.06.01）」の PDF。北海道生物の多様性の保全等に関する条例による指定（平成27年12月18日指定、平成28年6月19日施行、令和5年6月1日一部改正）。11種（動物9種・植物2種）
- 植物の2種は **イワミツバ【セリ科】** と **フランスギク【キク科】**。おぎはらの書いた「特定外来種」は、正しくは北海道の「指定外来種」（国の外来生物法の「特定外来生物」ではない）
- 一覧に書いてある栽培の仕方（イワミツバ）：特定飼養等施設は「個体が野外に逸出しないような施設（屋内、管理された庭園・公園等）」。飼養等の状況の確認と施設の点検を定期的に行う。地下茎の伸長や種子の飛散で野外に出ないよう留意する。地下茎の断片が入った栽培土を野外に捨てない。指定の理由は、本道の生物の多様性に著しい影響を及ぼす、またはそのおそれがあるため
- 当たる商品：エゴポディウム 'バリエガータム'（商品番号 38、在庫あり）。フランスギク（Leucanthemum vulgare）の商品はない。シャスターデージー（Leucanthemum × superbum。商品番号 934・1174）は別の種なので当てていない
- combine.py：学名の種（属＋種小名）が上の2種なら、「外来種リスト」の後ろに「／北海道の指定外来種（…）」を足し、「広がりすぎの注意」に上の栽培の仕方を足す。商品番号 38 の管理タイプは E 隔離推奨型のまま（見直しのときから）
- 北海道ブルーリスト（北海道の外来種リスト）は、選定結果の PDF の文字が取り出せず、イワミツバの区分は確かめていない。ブルーリストのページには、改訂作業中と書いてある → 2026-11-23 に確かめた（下の節。イワミツバは A2）
- まとめの表は `ClaudeWork/新マスター_下書き_916品種_1121e.xlsx`（最新）

## 2026-11-21（夜）：916品種を試作と同じ形（rows の JSON）にした
- ユーザーの指示「ア」（試作と同じ形にまとめる作業）
- `python -X utf8 scripts/pilot/to_rows.py <まとめの表.xlsx> rows`（master-rebuild で）。まとめの表（combine.py の出力。今は 1121e）から、master-rebuild/rows/<商品番号>.json を916個作る。形は trial/rows と同じ（fields の各項目に value・method・sources・level・note）。trial と同じ field 名に、family（科名）と ias_list（外来種リスト）を足した。review には、管理タイプの理由・決め手の原文、欧米の文献だけの耐暑性・蒸れ耐性、根拠の列を入れた
- 入れていないもの：今のマスターの値（花期・草丈・耐寒性・流通名）、在庫、価格、自社の値（試作の rows と同じ）。heat_note 以外の文の列（pruning の文）は、まだ作っていない
- 文献ID は trial/RULES.md と同じ（s01 RHS・s02 MBG・s04 YList・s05 環境省・s06 NC State・s08 シカゴ植物園・s10 Walters・s11 Jelitto・s17 Gaißmayer・s18 stauden.de・s20 おぎはら図鑑）。おぎはらの楽天の商品ページは、新しく s21 にした
- sources の読み方：値の後ろの「（RHS）」「（MBG・種）」、根拠の列の「[MBG・品種]」、「根拠」のシートの最後の列。RHS の H 値は s01、和名は s04、外来種リストは s05。耐暑性は「耐暑性の決め方」がおぎはらなら s20
- 文献名の付け直し（同じ日の夜。ユーザーの指示「あ」＝付け直す）：最初は値のある項目のうち 7693 件（約3割）に文献名がなかった（日照・土壌水分・葉色・増え方・乾燥耐性・切り花・蜜源・花色・株張りなど。組み立てのとき文献名を残していなかった）
  - assemble_pilot.py に「項目の文献」の列を足した（「日照=MBG・種」の行。値を入れたところで、どの文献の値かを残す。乾燥耐性は、決め手の言い回しが出てくる文の文献）。値の決め方は変えていない
  - 19個の下書きを末尾 _1121j で作り直し、前の _1121i と全部の列を比べて、916品種とも値が同じことを確かめた（896品種に「項目の文献」が付いた）。combine.py はこの列を見返し用の列として写す。まとめの表は `ClaudeWork/新マスター_下書き_916品種_1121f.xlsx`（最新）
  - to_rows.py：「項目の文献」の列を使うようにした。混植適性は、地下茎・こぼれ種の程度から決めたものは、その根拠の列の文献。西日耐性の × で文献がないもの（日照が半日陰のため）は日照の文献。学名は、RHS が正名としていてその表記と同じなら s01
  - 残り：文献名がないのは、学名 364（今のマスターの学名か、検討で決めた学名。RHS の正名と同じ表記ではない）と、旧学名 188（今のマスターの学名）だけ。どちらも note に書いてある
- 【試作28品種との照らし合わせ】（試作の X001〜X003 の3品種は商品番号がなく照らせない）。一致：管理タイプ 24/24（独立の確かめではない。前の節）、耐潮性以外の判定の列では 学名 24/25・RHS の H 値 22/23・USDA 上限 21/24・常緑性 20/25・耐暑性 20/24・成株シルエット 18/23・混植適性 18/20・株張り 18/23・葉色 16/23・土壌水分 16/24・日照 13/24・蒸れ耐性 12/14・西日耐性 12/24・乾燥耐性 10/24。文の項目（花色の詳細・葉の特徴・株分けの間隔・広がりすぎの注意など）は書き方が違うので一致しない。違いの一覧は作業用の一時フォルダの trial_diff.json

## 2026-11-23：原産地を Kew（WCVP）で埋めた
- ユーザーの指示「原産地を埋める」。原産地は 271 品種（Jelitto だけ）→ 728 品種
- データ：Kew の World Checklist of Vascular Plants の一括データ（sftp.kew.org/pub/data-repositories/WCVP/wcvp.zip、2026-06-04 版、約88MB）。リポジトリには入れていない（作業用の一時フォルダ）。消えていたら取り直す
- `python -X utf8 scripts/tools/kew_native.py <まとめの表.xlsx> <wcvp を展開したフォルダ>`（master-rebuild で）→ master-rebuild/kew_native.json（商品番号ごとに、照合した名前・Kew の状態・正名・英語の分布・地域コード・日本語の原産地・決め方）
- 決め方：
  - 学名（正名）から品種名を外し、種（亜種・変種があればそれ）で引く。異名なら Kew の正名の分布。綴りの揺れ（-ii と -i）も試す（例：Andropogon gerardii → gerardi、Eriogonum alleni → allenii）
  - 分布は wcvp_distribution.csv の自生だけ（introduced・extinct・location_doubtful が 0）。地域名は Kew の地域区分（TDWG level 2）を日本語にした。東アジアだけは 日本・朝鮮半島・台湾 などの単位まで。ヨーロッパの5区分がそろえば「ヨーロッパ全域」、アメリカの6区分なら「アメリカ合衆国の全域」、カナダ東西なら「カナダ南部」
  - 「×」の付いた交配種は、Kew でも交配種の記録だけに当てる。Kew に交配式があれば「交配種（交配親：…）」（例：Gaillardia × grandiflora → G. aristata × G. pulchella）
  - 同じ名前が Kew で別々の種を指すとき（命名者の違う同名）：表の「学名（RHS）」「旧学名・別名」「学名のメモ」に、行き先の正名か「名前＋命名者」が書かれていればそれに決めた（4品種：39 Leontopodium、294 Calamintha grandiflora、1202 Sedum reflexum、1470 Aster cordifolius）。決まらない4品種は空欄（1 Sagina subulata、362 Limonium latifolium、1191 Calamintha nepeta、1979 Pennisetum alopecuroides。理由は kew_native.json）
  - 属と品種名だけの交配種（Hosta 'Patriot' など）は種が決まらないので空欄
- combine.py：Jelitto の原産地があればそれを使い、なければ Kew（値の後ろに「（種の原産地）（Kew）」。交配種は「（Kew）」）。まとめの表 `ClaudeWork/新マスター_下書き_916品種_1123a.xlsx`（最新）。1121f と全部の列を比べて、変わったのは原産地の 457 品種だけ
- rows：to_rows.py を作り直した。native_range の sources は s03
- Jelitto の値がある品種で Kew と見比べた（25品種を抜き出し）。地域は食い違いなし（Kew のほうが広く書く）

## 2026-11-23：北海道ブルーリスト2010と照らした（新しい列「北海道ブルーリスト」）
- ユーザーの指示「北海道ブルーリスト」
- 資料：北海道庁「北海道の外来種リスト（ブルーリスト）」https://www.pref.hokkaido.lg.jp/ks/skn/alien/bluelist/bluelist_top.html の「北海道ブルーリスト2010選定結果」の PDF（21ページ）。植物の改訂版はまだない（改訂検討のページにあるのは哺乳類・鳥類・両生爬虫類の2019年版だけ）。カテゴリーの意味は改訂検討のページの「カテゴリー区分」の PDF（表1・表2）
- PDF は文字が取り出せない（pdftotext で文字化け）。3ページずつに分けて画面で読み、植物の表 639 種（国外 586・国内 49・不明 4。PDF の数と一致）を scripts/tools/data/hokkaido_bluelist2010_plants.tsv に書き写した（種名・異名・カテゴリー・原産地の区分）。一覧は和名だけで学名はない
- 植物で A1 はなし。A2 は17種（オオハンゴンソウ・オオアワダチソウ・セイヨウタンポポ・ヘラオオバコ・フランスギク・イワミツバ〔フイリイワミツバを含む〕・シロツメクサ・ムラサキツメクサ・キショウブ・オランダガラシ・セイタカアワダチソウ など）
- カテゴリーの意味：A＝定着していて影響が報告・懸念（A1 緊急に防除が必要、A2 大きな影響があり防除の必要性を検討、A3 それ以外）。B＝定着している・影響の報告なし。C＝定着がはっきりしない・影響あり。D＝定着がはっきりしない・影響の報告なし。E＝定着していない・影響あり。庭や花壇など人の管理下で栽培されている植物は選定の対象外（野外に出たものが対象）
- `python -X utf8 scripts/tools/bluelist_match.py <まとめの表.xlsx>` → master-rebuild/hokkaido_bluelist.json。照らし方：(1) 表の「和名」（YList の標準和名）が一覧の種名と同じ (2) 一覧の異名と同じで、同じ種と確かめたもの（SYN_OK。例：セイヨウジュウニヒトエ＝セイヨウキランソウ、ジギタリス＝キツネノテブクロ） (3) 和名が違う・ないが、学名で同じ種と分かるもの（SCI。例：Crocosmia × crocosmiiflora＝ヒメヒオウギズイセン、Melissa officinalis＝セイヨウハッカ〔異名 レモンバーム〕、Mentha × piperita＝コショウハッカ）。種として当て、変種・亜種の違い（カキドオシ・ウツボグサ・ヤマホタルブクロ・ノハナショウブ・チョロギガヤ）は値の中に書いた
- 当てなかったもの：ヤグルマソウ（ロジャーシア。一覧ではヤグルマギクの異名）、ヤグルマハッカ（Monarda fistulosa。一覧ではタイマツバナの異名）。ルピナス（一覧は Lupinus polyphyllus 系）・クロコスミアの交配品種（'Lucifer' など）・ソリダゴの品種は種が決まらないので当てていない
- 結果：113品種。A2 4（イワミツバ 38、シロツメクサ 317・393・582）、A3 17（ジギタリス・プルプレア 6、ネバリノギク 4、ユウゼンギク 3、クサヨシ 2、セイヨウノコギリソウ 2）、B 87、D 5（シュウメイギク・キバナノコギリソウ・ムラサキモウズイカ・ハナショウブ）。ほかは「掲載なし」
- combine.py：新しい列「北海道ブルーリスト」（外来種リストの右）。値は「A2：（意味）（一覧の種名。国外外来種）」の形。まとめの表 `ClaudeWork/新マスター_下書き_916品種_1123b.xlsx`（最新）。1123a と比べて、ほかの列は変わっていない
- rows：field「hokkaido_bluelist」。文献ID は新しく s22（北海道庁 北海道ブルーリスト2010）
- リスクタグ（同じ日。ユーザーの回答「A2だけ入れる」、DECISIONS.md）：A2 の4品種（38・317・393・582）に「要管理（北海道ブルーリスト A2）」を足した。4品種とも前から「要管理（広がりやすい）」が付いていた。管理タイプは変えていない。まとめの表 `ClaudeWork/新マスター_下書き_916品種_1123c.xlsx`（最新）。1123b と比べて変わったのはこの4品種のリスクタグだけ。rows にはリスクタグの項目がないので変わらない

## 2026-11-23：試作との食い違いの見直し・和名の当て方・シカゴ植物園の3号
- ユーザーの指示「1.2.3を順番で」（1 試作との食い違い、2 和名、3 シカゴ植物園の読めなかった号。4〔花期・草丈・耐寒性を文献の値で作る〕は始める前に必ず確認）
- 19個の下書きを末尾 _1123d で作り直した（1121j と比べて、変わったのは乾燥耐性・西日耐性・和名・文献の注意・株張りの一部だけ。日照は変えていない）。まとめの表 `ClaudeWork/新マスター_下書き_916品種_1123d.xlsx`（最新）、rows も作り直した
- 【1 試作との食い違い（日照 13/24・乾燥耐性 10/24・西日耐性 12/24）の原因】
  - 日照：試作のルール（trial/RULES.md「それ以外」の順位 s01 RHS が最優先）と違い、組み立ては MBG → Walters → stauden.de の順で、RHS を使っていなかった。RHS の日照はページの「Position」の見出しの下（表の項目 dt/dd ではない）にあり、1122ページ中 934 ページで読める。assemble_pilot.py の rhs() で取り出し、見返し用の列「日照（RHS）」に入れた（700品種）。決め方は SUN_MODE（"mbg" 今まで／"rhs" RHS 最優先／"shade" 両方あって違うときは日陰寄り）で切り替える。今は "mbg"（ユーザーの回答待ち）。RHS 最優先なら 265品種、日陰寄りなら 155品種の日照が変わる。RHS はイギリスの夏を前提に日照を広めに書く（例：クルマバソウ Galium odoratum を Full sun・Partial shade）
  - 乾燥耐性：(a) 読み落とし。ハイフン付きの drought-tolerant と tolerant of drought を拾っていなかった → 直した（強）。moderately／somewhat drought-tolerant は 中。intolerant of drought は 弱（tolerant of drought に当たらないようにした）。(b) 試作のルールにある「MBG の Water: Medium／Walters の Average → 中」が組み立てに入っていない（P07・P17・P18・P25・P27）。入れるかはユーザーの回答待ち。乾燥耐性が空欄の 281品種のうち、土壌水分が MBG の Medium は 39、RHS の Moist but well-drained は 136。(c) 2026-11-21 のユーザーの決定（RHS の Drought Resistance: Yes・NC State の項目は 中、おぎはら楽天で空欄を埋める）による違い（P14・P16・P19・P24）は直さない。(d) 文献が割れている（P11：MBG は Water: Medium、Walters は Drought Tolerant → 今は 強）
  - 変わった数（1121j → 1123d）：乾燥耐性 中→強 29、空欄→弱 15（フィリペンデュラなど。intolerant of drought）、空欄→強 8、強→中 4（スタキス ビザンティナ3・エリムス。moderately）、強→弱 2、弱→強 1（ベルゲニア 'Snowtime'。NC State「drought-tolerant とされる」「can tolerate drought」）、中→弱 1。西日耐性 ○→◎ 11、◎→○ 3（乾燥耐性に連動）
  - 西日耐性は日照・耐暑性・乾燥耐性から決まるので、上の2つが決まれば一緒に動く
- 【2 和名】yl_pick（YList の行から和名を選ぶ）で、種そのものの行がないときに「最初の標準の行」を採っていたため、別の変種や別の種の和名になっていた（21種）。例：Campanula punctata → ヤマホタルブクロ（var. hondoensis）、Aster ericoides → キダチコンギク（YList では Aster pilosus の和名）。基本変種・基本亜種の行（var. punctata → ホタルブクロ）を採り、なければ空欄にした。30品種の和名が変わった（ホタルブクロ6、オオバナノコギリソウ、セイヨウクサレダマ、シベリアクガイソウ、シャク2 など。空欄になったもの：Hosta sieboldiana・sieboldii、Thymus serpyllum 5、Hydrangea serrata 4、Glechoma hederacea 2、Galium verum、Viburnum plicatum、Androsace villosa、Persicaria virginiana、Achillea sibirica、Aster ericoides）。和名は 460 → 441。エゾアジサイ・ヤブデマリなどは、取ってある YList の検索結果にその行がない（検索し直せば入るかもしれない）
  - 北海道ブルーリストの照合はやり直した（113品種のまま。ホタルブクロは学名ではなく和名で当たるようになった）
- 【3 シカゴ植物園】no5 Yarrow（1994）・no8 Rudbeckia（1995）・no9 Blazing stars（1996）の PDF（画像だけ、4ページずつ）を画面で読み、batch_06・08・10 の jelitto_cbg_data.py の CBG_V に入れた（文献の注意・株幅）。アキレア 'Coronation Gold'・'Parker's Variety'、プタルミカ（種：品種はどれもうどんこ病）、トメントーサ（種：試験地の湿りすぎで不調）／リアトリス スピカータ（種）・ピクノスタキア（種）・'Floristan Violet'・'Floristan White'・'Kobold'／ルドベキア 'Goldsturm'、サブトメントーサ（種）。株幅は品種の数値（Walters）があればそちらが優先（RULES のとおり）。サブトメントーサの種の株幅（94cm）は品種に使わない
- 【日照と乾燥耐性の空欄（同じ日。DECISIONS.md の決定）】今のマスターと比べた：日照は RHS と 66%、MBG と 67% 一致（RHS と MBG が違う 196品種では、マスターは MBG 側 105・RHS 側 86）。乾燥耐性の空欄で MBG が Medium の品種は、今のマスターでも 中 が約半分
  - SUN_MODE = "fill"（空欄だけ RHS）：日照の空欄 28品種が埋まった（863 → 891）
  - MBG の Water: Medium → 中（推定・信頼度 低）：109品種（635 → 744）。前に「39品種」と伝えたのは数え違い（土壌水分の列の出どころが MBG のものだけ数えていた。RHS の値で土壌水分が上書きされた品種が 70 あった）。109品種のうち今のマスターも 中 は 63、弱 26、強 20
  - 下書きは末尾 _1123e、まとめの表 `ClaudeWork/新マスター_下書き_916品種_1123e.xlsx`（最新）。1123d と比べて変わったのは、日照 28（空欄→値）・乾燥耐性 109（空欄→中）・西日耐性 3 だけ。rows も作り直した（推定の乾燥耐性は method 判定・note つき）

## 2026-11-23：文献の草丈・花期の列（見比べ用）
- ユーザーの指示「4を始める」（今のマスターから写している花期・草丈・耐寒性を、文献の値で作って見比べる）。今のマスターの値の列（花期 開始月・終了月、草丈 最小・最大）は変えていない（2026-11-19 の「耐寒性・草丈・花期は今のマスターの値を使う」決定のまま）
- assemble_pilot.py の lit_height_bloom：下書きに「草丈（文献）」「花期（文献）」の列。下書きは末尾 _1123g。まとめの表 `ClaudeWork/新マスター_下書き_916品種_1123g.xlsx`（最新）に、草丈（文献）・草丈の食い違い・花期（文献）・花期の食い違いの4列を足した（今のマスターの草丈・花期の右）。1123e と比べて、ほかの列は変わっていない
  - 草丈：品種の数値を優先（株張りと同じ考え）。Walters（品種）→ MBG（品種）→ stauden.de（品種）→ MBG（種）→ stauden.de（種）→ RHS の幅（0.1〜0.5m のような区分）。品種の商品には種のページの草丈を使わない（DECISIONS.md「種のページの情報」）。属のページは使わない。stauden.de は花を含む高さ（Blüten-Höhe）、なければ Wuchs-Höhe。802品種（Walters 365・stauden.de 品種 141・RHS の幅 94・MBG 品種 93・MBG 種 75・stauden.de 種 34）
  - 花期：月で書いてある stauden.de（ドイツ）→ MBG（セントルイス）。どちらもなければ Walters の季節（初夏・盛夏など）。属のページは使わない。ドイツを先にしたのは、夏が涼しく広尾に近いと見たため（ユーザーが表を見て変えてよい）。833品種
  - 食い違いの印：草丈は、範囲が重ならず、すき間が 10cm 以上かつマスターの値の 25% 以上のときだけ（63品種。小さな差まで入れると 130）。花期は、月の範囲が重ならないとき（42品種）。今のマスターの花期は季節の言葉（初夏〜盛夏など）を月に直した値
- 耐寒性：文献の値は前から「USDA 下限・上限」「RHS 耐寒性（H 値）」の列にある。今のマスターの耐寒性は 強・中の強・中の中・中の弱・弱 で、定義が書いてないので、文献の値から同じ区分は作っていない（区分の決め方が要る）
- rows（試作の形）には、文献の草丈・花期の項目を入れていない（試作の field にない）

## 2026-11-23：5項目は今のマスターを尊重（日照・株張りもマスターの値に）
- ユーザーの方針（DECISIONS.md）。combine.py：日照は今のマスターの「日照条件」（～ は 〜 に。「明るい日陰」はそのまま。タグの判定では 半日陰 と同じ扱い）、株張りは「広がり(cm)」。マスターが空欄のときだけ文献の値。見比べ用の列「日照（文献）」「株張り（文献）」と、印の列「日照の食い違い」「株張りの食い違い」「耐寒性の食い違い」を足した
- 印の付け方：日照は2段以上違うとき（日向 と 半日陰・日陰）。株張りは草丈と同じ（範囲が重ならず、すき間が 10cm 以上かつマスターの値の 25% 以上）。耐寒性は、マスターが 強 なのに USDA 下限 7 以上か RHS H1〜H3、マスターが 弱・中の弱 なのに USDA 下限 4 以下か RHS H6〜H7
- 印の数（1123h）：日照 4、株張り 101、耐寒性 5、草丈 63、花期 42。どれかに印があるのは 202品種
- 西日耐性は、文献の日照から決めたまま（下書きの値）。マスターの日照に合わせて決め直してはいない
- rows：日照・株張りがマスターの値のときは sources を空にし、note に「今のマスターの値。文献：…」と【要見直し】の印を書く
- まとめの表 `ClaudeWork/新マスター_下書き_916品種_1123h.xlsx`。1123g と比べて変わったのは、株張り・日照・機能用途タグ（日照から決まる「日陰庭向き」など）だけ

## 2026-11-23：食い違いの印を仕分けて、確認ページを作った
- ユーザーの指示「先に調べてから確認ページ」。combine.py の花期の比べ方を直した（年をまたぐ範囲〔8〜2月 など。イネ科の穂〕を月の集合で比べる）。これで 939・1442 の印が消え、印は 200品種。まとめの表 `ClaudeWork/新マスター_下書き_916品種_1123i.xlsx`（最新）
- `scripts/tools/kuichigai_classify.py <まとめの表> kuichigai_review.json`：印を「残す（確認が要る）」と「外す（マスターのまま。理由つき）」に分ける。外す決まり：
  - 株張り：文献のほうが大きいとき（RHS の最終的な大きさの区分・シカゴ植物園の数年の試験・Walters の成株は、何年も育った後の幅）。88か所
  - 草丈：文献のほうが高く、葉が低く花茎や穂だけが伸びる植物（イネ科・カヤツリグサ科、Heuchera・× Heucherella・Tiarella・Ligularia・Bergenia・Hosta・Pulmonaria・Brunnera・Yucca・Astilbe・Mukdenia、Stachys byzantina）。または文献が RHS の大まかな区分で、文献のほうが高いとき。20か所
  - 花期：文献のほうが早く、ドイツ（stauden.de）なら1か月以内、セントルイス（MBG）なら2か月以内の遅れのとき（広尾は春が遅い）。19か所
  - 日照・耐寒性は全部残す
- 結果：残る 83品種（86か所。日照 4、耐寒性 5、花期 21、草丈 43、株張り 13）、全部外れる 117品種
- 確認ページ「文献との食い違いの確認」https://claude.ai/artifact/1epUhjEQEseqtxtLPM9z6j （非公開）。1か所ずつ M（マスターのまま）・B（文献に合わせる。耐寒性は「見直す」）・C（別の値。メモ）。外した127か所も理由ごとに折りたたみで載せ、「確認する」で戻せる。回答の文は「食い違いの確認の回答：<商品番号>-<項目><M/B/C>（メモ）、…」と「外したもののうち確認したいもの：…」。回答を表に入れる仕組みはまだ作っていない（→ 次の節で作った）

## 2026-11-23：食い違いの回答を入れる仕組み・stauden.de の値の段階の直し
- apply_answers.py：「食い違いの確認の回答：」の行を読み、user_answers.json の「食い違い」（{商品番号: {項目: {選択, メモ, 日付}}}）に入れる。「外したもののうち確認したいもの：」は「外したものの確認」（"商品番号-項目" のキー）
- combine.py：M はマスターのまま。B は文献の値（草丈・株張り・花期・日照）に置きかえる。C はメモの数字（草丈・株張り・花期）か日照のことばを使う。耐寒性は B・C どちらもメモが 強／中の強／中／中の弱／弱 ならその値、そうでなければ【要見直し】。印の列の後ろに「ユーザーの確認（日付）：…」を書く。回答のない印で kuichigai_review.json で外したものは、印の後ろに「外した（マスターのまま）：理由」。管理難易度の判定は回答後の耐寒性を使う。試しの回答で確かめた（試しの user_answers.json は消した）
- stauden.de の直し（assemble_pilot.py の lit_height_bloom）：stauden.de の値には、値ごとに "cultivar"（そのページ自身の値。種のページでも cultivar）／"species"（種から引き継いだ値）／"genus" の印がある。これまで品種のページの値を全部「品種」としていたので、種の値（例：アスター 'Vibrant Dome' の 100〜180cm）を品種の草丈として使っていた。印が species・genus なら 種・属 として扱うようにした（品種の商品では種の草丈を使わない決まりどおり）。草丈（文献）が 40品種、花期（文献）が 85品種で変わった。ほかの列（日照・常緑性など）の stauden.de の値は、まだ印を見ていない
- 印を付け直した結果（1123j）：残る 67品種（70か所。日照 4、耐寒性 5、花期 20、草丈 28、株張り 13）、全部外れる 116品種。確認ページ（同じ URL）も作り直した。まとめの表 `ClaudeWork/新マスター_下書き_916品種_1123j.xlsx`、下書きは末尾 1123j
- RHS の株張り「0〜10cm」（720・753・1912）は RHS の区分「0–0.1 metres」そのもので、読み違いではない

## 2026-11-23：西日耐性をマスターの日照で決め直した
- 西日耐性の決め方（DECISIONS.md 2026-11-19）は日照を使う（半日陰・日陰なら ×、日向で耐暑性・乾燥耐性とも 強なら ◎）。日照をマスターの値にしたので、西日耐性もマスターの日照で決め直した
- assemble_pilot.py：西日の判定を west_for(日照) にまとめ、新しい列「西日耐性（日照ごと）」（日向・日向〜半日陰・半日陰 のそれぞれの値。おぎはらの値で控えめにしたあと）を出す。下書きの「西日耐性」は文献の日照のまま（作り直して変化 0 を確かめた）
- combine.py：マスターの日照（明るい日陰は 半日陰 扱い）の値を選ぶ。変わったら「暑さ・蒸れ・西日の根拠」の先頭に「[日照] 今のマスターの日照（…）で西日耐性を決め直した（文献の日照 … なら …）」
- 変わったのは 74品種：× → ○ 23、× → 空欄 12、空欄 → × 12、△ → × 11、× → △ 10、○ → × 6。× → 空欄 は、耐暑性がわからないので決まらないもの
- kuichigai_classify.py：combine.py が印の後ろに足す文（外した理由・ユーザーの確認）を読み飛ばすようにした
- まとめの表 `ClaudeWork/新マスター_下書き_916品種_1123k.xlsx`（最新）、下書きは末尾 1123k

## 次にやること（全部の属の下書きが終わった）
- 【2026-11-21 の終わりの時点】6列・暑さの確認ページ・管理タイプの見直し（在庫あり）まで済み。待っているのは、(1) 確認ページ「暑さに弱い品種の確認」の回答 (2) 「剪定不要＋花後の花茎切り」を A にするか B にするか。（夜に、回答を表に入れる仕組み〔scripts/tools/apply_answers.py〕と、在庫のない282品種の管理タイプの見直しも済んだ。上の2つの節）。残っているのは、未決（DECISIONS.md）、試作と同じ形（rows・根拠の JSON）への統合
- batch_18 までで、全916品種の下書きができた（試行78＋アスター23＋55＋52＋47＋50＋49＋34＋54＋51＋50＋53＋51＋51＋51＋51＋50＋47＋19＝916）。2026-11-20 に、batch_*/input と pilot/input の商品番号（916件・重複なし）を元のマスターの商品番号（916件）と照らし、もれ・重複がないことを確かめた
- 耐暑性の決め方は 2026-11-21 に確定し、全品種に反映した（上の節）。次は、ユーザーの確認（各節の「ユーザーに聞くこと・伝えること」「要確認」。ユーザーは「確認は全部終わってからまとめて見る」と回答済み）
- 耐暑性の最終検討で見るもの：各下書きの「耐暑性の決め方」と「耐暑性（欧米の文献だけなら）」の列、根拠の「[食い違い]」、各 batch の ogihara_data.py の SIBLING（同じ種の別品種の値を使った試し。中 で使ったのは batch_07・11・12・14・15・16 の6回）
- 残っている未決は DECISIONS.md の「未決」（ミントブッシュの種〔保留〕、フクシア 'Variegata'、ユーパトリウム 白花の種、RHS が別の品種名を正名としている15品種）。種が変わった品種の文献の当て直しは 2026-11-21 に済み
- 下書きは、まとまりごとに別の Excel（ClaudeWork の「下書き_….xlsx」。同じまとまりに複数あるときは、名前の末尾が新しいものが最新。どれが最新かは scripts/tools/rediff.py の KEY で探せる）。1つの表にまとめる作業は 2026-11-21 に済み（上の節。scripts/pilot/combine.py）。まだ作っていない19列と、試作と同じ形（rows・根拠の JSON）への統合は残っている
- 3属の試行（78品種）とアスター（23品種）の下書きも、2026-11-21 に今の assemble_pilot.py で作り直した（rediff.py の対象に入れた）
- まとまりを作り直す手順：`python -X utf8 scripts/pilot/assemble_pilot.py batch_NN/input <digest.json> <raw> <出力.xlsx> batch_NN`。前の下書きと比べるのは scripts/tools/rediff.py（耐暑性・蒸れ耐性・西日耐性・乾燥耐性・「欧米の文献だけなら」・和名を比べる。ほかの列は比べない）
- 1つのまとまりの手順（記録。新しい属が増えたときに使う）：make_input.py → fetch_all.py と fetch_walters.py（裏で。あとで同じコマンドをもう一度実行して done と Walters の一覧を確かめる）→ おぎはら（scripts/tools/ogi_search.py で検索、ogi_page2.py でページを1行ずつに）→ RHS の番号（アプリ内のブラウザーで検索を順に開く → 候補を scripts/tools/rhs_check.py で読んで Name Status を見る）→ Gaißmayer・Jelitto（Chrome。タブで1ページずつ、1つのサイトにつき7秒おき。fetch で読まない。確認画面が出たら操作せず、別の作業を先にしてからタブを見直す）→ シカゴ植物園の号（pdftotext -raw）→ scripts/tools/clean_raw.py → fetch_rhs.py → digest.py → assemble_pilot.py → scripts/tools/show.py で当たり先と根拠を読む → MBG・NC State・Walters の hot・heat・humid・cool を含む文を全部出して拾い漏れを見る → scripts/tools/rediff.py で前の batch を作り直して比べる → HANDOFF.md → コミット → GitHub に送る
- ID の頭文字（使ったもの）：H G V A M C X F R S D E B Me Ge Vi Pu Pe Po Pa Ac St He Sc Pl Fi Sa Tr Th Co Li Ly Vs Er Mi Mo Mn Td Sp Ne An Aq Ce Aj Di Hl Mu Ar Eu Hm Kn Pn Ru Ty Dg Pr Ep Bg Cg Ds Fu Ir Lo Si Gn Ps Ti Al Ad Hd Lg Pt Pv Tc Hy As Ga Gy At Cn Fe Hk Pp Ag Oe Vb Vn Ah Am Ca Ch Cl Ec El Eg Gm Gc Ka La Le Lt Pc Ph Sg Sn Sm Sl Su Sy Vu Yu Hr Tf Ak Cr Gl Aa Cy Kt Lw Lu Or Py Px Sd Ab Cu Cm Cs Ci Dr Em Fr Hb Ib Lr Lc Mk Pi Pz Rg So Ae Ao Ax Ap Ay Aw Au Ai Az Bi Br Bu Ct Cd Da De Es Et Ei Eo Ey En Go Hn Hc Im Lm Ln Lp Ms Ml Op Pm Pf Pj Pw Pd Pk Rn Rt Rl Ss Se Sq Sk Tm Un Av Ba Dl Fo Hp Lh Lj Pq Ro To Vr Vo Af Tn Cp Cz Cj Cv Cq Gi Gb Ko Ls On Ol Pg Pb Sj Sx Sb Va、試作の P
- シカゴ植物園の評価報告（一覧 no1〜no40）で、画像だけで読めない号：no5 アキレア、no8 ルドベキア、no9 リアトリス（古い号は読めないことが多い）
- scripts/tools/ の補助スクリプトは、作業中に一時フォルダで使っていたものをそのまま入れた（生データの場所が書き込まれているものがある。別のパソコンやフォルダでは書き換えて使う）
- Jelitto・Gaißmayer を飛ばしたまとまり：なし（batch_10 の Gaißmayer のミューレンベルギアだけ検索していない）
- 生データ（b2_raw〜b18_raw と digest）はこのパソコンの一時フォルダ（AppData/Local/Temp/claude/ の下。b7〜b10 は 5942321c1c0f279d/ea463099-…/scratchpad、b11・b12 は 0f02706c790fef35/9e6508df-…/scratchpad、b13・b14 は 803dcd3d003c6b53/15533220-…/scratchpad、b15・b16 は 803dcd3d003c6b53/664da7c4-…/scratchpad、b17・b18 は 803dcd3d003c6b53/26b2b1f1-…/scratchpad。場所は scripts/tools/rediff.py にも書いてある）にあり、消えることがある。消えていたら fetch_all.py などで取り直せる
- Windows の Git Bash では、長い日本語と引用符を含むヒアドキュメントが「unexpected EOF」で失敗することがある。データのファイルやスクリプトは、ファイルを書く道具で直接書く
- 会話が長くなると遅くなるので、2個ごとに新しいセッションに切り替えて進めた（17・18個目は1つのセッション）

## 新しいセッションで続けるとき
- 全部の属の下書きが終わった（2026-11-20）。耐暑性は今の決め方（おぎはら優先、同じ種の別品種の値を使う試し）のまま全品種を下書きしてある。次は、耐暑性の決め方の最終検討とユーザーの確認（上の「次にやること」）
- このファイルと DECISIONS.md・trial/RULES.md を読めば、決まったことと手順が分かる
- 文献ごとの読める場所：stauden.de・MBG・NC State・YList・Walters・RHS の詳細ページ・シカゴ植物園の PDF・おぎはら植物園は curl。RHS の検索はブラウザー（アプリ内のブラウザーでよい）。Gaißmayer と Jelitto はユーザーのパソコンの Chrome（Claude in Chrome）
- ユーザーはスマホで見ることがある。確認ページは非公開の Artifact で作り、チェックリストは選ぶと「1A、2B…」の文ができる形にして、チャットに貼ってもらう
- ユーザーは「確認は全部終わってからまとめて見る」と回答済み。判断が要ることだけ聞く

## 注意
- 文献にない値は推測で埋めない（空欄）。値ごとに文献ID・原文・URL・確認日を残す
- 文献値・自社の実測値・設計上の推奨値は分けて管理する
- 価格・在庫を含むデータは公開リポジトリにコミットしない
- 文献の本文そのもの（ページ全体）はリポジトリに入れない。短い引用だけを evidence に残す
