# 引き継ぎ（2026-11-20 更新）

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

## 次にやること（15個目のまとまりから）
- batch_14 までで 916品種中 749品種の下書きができた（試行78＋アスター23＋55＋52＋47＋50＋49＋34＋54＋51＋50＋53＋51＋51＋51）。残りは 167品種・108属
- 残りの属はどれも4品種以下で、在庫のある品種は1つ以下。1回 50品種前後にまとめる（次は18属。そのあとは1〜2品種の属ばかりで、1回に25属以上になる）
- 残りの属（在庫のある品種が多い順。在庫あり／全品種。2026-11-20 に元のマスターから数えた）：アスクレピアス 1/4、クロコスミア 1/4、ガイラルディア 1/4、アガスタチ 1/3、カリオプテリス 1/3、クナウティア 1/3、レウイシア 1/3、ルピナス 1/3、オリガヌム 1/3、ペオニア 1/3、パルテノキッスス 1/3、シダルセア 1/3、アラビス 1/2、カルーナ 1/2、カマエメルム 1/2、クリサンセマム 1/2、キミキフーガ 1/2、ドラコセファラム 1/2、エピメディウム 1/2、フラガリア 1/2、ヘレボルス 1/2、イベリス 1/2、リリオペ 1/2、リクニス 1/2、ムクデニア 1/2、ファラリス 1/2、フィソカルプス 1/2、ロジャーシア 1/2、ソリダゴ 1/2、そのあとは1品種だけの属（アクタエア、エゴポディウム、アルテア …）が続く（数え方：元のマスターの学名の最初の語〔× で始まるときは次の語〕を属とし、batch_*/input と pilot/input にある属を除いて、在庫のある品種の数・全品種の数の順に並べる）
- 15個目の案：アスクレピアス・クロコスミア・ガイラルディア・アガスタチ・カリオプテリス・クナウティア・レウイシア・ルピナス・オリガヌム・ペオニア・パルテノキッスス・シダルセア・アラビス・カルーナ・カマエメルム・クリサンセマム・キミキフーガ・ドラコセファラム（18属 51品種）。ID の頭文字は、これまでに使ったもの（H G V A M C X F R S D E B Me Ge Vi Pu Pe Po Pa Ac St He Sc Pl Fi Sa Tr Th Co Li Ly Vs Er Mi Mo Mn Td Sp Ne An Aq Ce Aj Di Hl Mu Ar Eu Hm Kn Pn Ru Ty Dg Pr Ep Bg Cg Ds Fu Ir Lo Si Gn Ps Ti Al Ad Hd Lg Pt Pv Tc Hy As Ga Gy At Cn Fe Hk Pp Ag Oe Vb Vn Ah Am Ca Ch Cl Ec El Eg Gm Gc Ka La Le Lt Pc Ph Sg Sn Sm Sl Su Sy Vu Yu Hr Tf、試作の P）と重ならないようにする。アガスタチ・ルピナス 'Fraulein' は試作28品種と重なる
- シカゴ植物園の評価報告がある属（一覧より）：no37 ユーパトリウム、no24 アルケミラ、no30 レウカンセマム、no32 プラティコドン、no18 アムソニア、no19 アルテミシア、no20 エピメディウム、no23 ラミウム、no26 オエノセラ、no15 ソリダゴ、no16 トリキルティス、no39 シダ、no40 ロジャーシア ほか。画像だけで読めない号：no5 アキレア、no8 ルドベキア、no9 リアトリス（古い号は読めないことが多い）
- 1つのまとまりの手順：make_input.py → fetch_all.py と fetch_walters.py（裏で。10分で切れるので、あとで同じコマンドをもう一度実行して done と Walters の一覧を確かめる）→ おぎはら（scripts/tools/ogi_search.py で検索、ogi_page2.py でページを1行ずつに）→ RHS の番号（アプリ内のブラウザーで検索を順に開く。50件で20分ほど → 候補を scripts/tools/rhs_check.py で読んで Name Status を見る）→ Gaißmayer・Jelitto（Chrome。1ページごとに6秒あける。最初の1ページの題名で確認画面でないことを確かめてからまとめて開く。確認画面が出たら操作せず、もう一方のサイトや別の作業を先にしてからタブを見直す。それでも出たままなら飛ばして、ここに書く）→ シカゴ植物園の号（pdftotext -raw）→ scripts/tools/clean_raw.py → fetch_rhs.py → digest.py → assemble_pilot.py → scripts/tools/show.py で当たり先と根拠を読む → MBG・NC State の hot・heat・humid・cool を含む文を全部出して拾い漏れを見る → scripts/tools/rediff.py で前の batch を作り直して比べる（新しい batch は rediff.py の RAW・KEY に足す）→ HANDOFF.md → コミット → GitHub に送る
- scripts/tools/ の補助スクリプトは、作業中に一時フォルダで使っていたものをそのまま入れた（生データの場所が書き込まれているものがある。別のパソコンやフォルダでは書き換えて使う）
- Jelitto・Gaißmayer を飛ばしたまとまり：なし（batch_10 の Gaißmayer のミューレンベルギアだけ検索していない）
- 生データ（b2_raw〜b14_raw と digest）はこのパソコンの一時フォルダ（AppData/Local/Temp/claude/ の下。b7〜b10 は 5942321c1c0f279d/ea463099-…/scratchpad、b11・b12 は 0f02706c790fef35/9e6508df-…/scratchpad、b13・b14 は 803dcd3d003c6b53/15533220-…/scratchpad。場所は scripts/tools/rediff.py にも書いてある）にあり、消えることがある。消えていたら fetch_all.py などで取り直せる
- Windows の Git Bash では、長い日本語と引用符を含むヒアドキュメントが「unexpected EOF」で失敗することがある。データのファイルやスクリプトは、ファイルを書く道具で直接書く
- 2026-11-20 のセッションは、7つ目から10個目まで（189品種）を1つの会話で進めた。会話が長くなると遅くなるので、2個ごとに新しいセッションに切り替えるとよい（13・14個目は1つのセッションで進めた）

## 新しいセッションで続けるとき
- 耐暑性は今の決め方のまま進め、全部の属が終わってから最後にもう一度検討する（2026-11-19 ユーザーの指示。DECISIONS.md）。新しい属でも「同じ種のおぎはらの値」を使うときは、その batch の ogihara_data.py の SIBLING に書く
- このファイルと DECISIONS.md・trial/RULES.md を読めば、決まったことと手順が分かる
- 文献ごとの読める場所：stauden.de・MBG・NC State・YList・Walters・RHS の詳細ページ・シカゴ植物園の PDF・おぎはら植物園は curl。RHS の検索はブラウザー（アプリ内のブラウザーでよい）。Gaißmayer と Jelitto はユーザーのパソコンの Chrome（Claude in Chrome）
- ユーザーはスマホで見ることがある。確認ページは非公開の Artifact で作り、チェックリストは選ぶと「1A、2B…」の文ができる形にして、チャットに貼ってもらう
- ユーザーは「確認は全部終わってからまとめて見る」と回答済み。判断が要ることだけ聞く

## 注意
- 文献にない値は推測で埋めない（空欄）。値ごとに文献ID・原文・URL・確認日を残す
- 文献値・自社の実測値・設計上の推奨値は分けて管理する
- 価格・在庫を含むデータは公開リポジトリにコミットしない
- 文献の本文そのもの（ページ全体）はリポジトリに入れない。短い引用だけを evidence に残す
