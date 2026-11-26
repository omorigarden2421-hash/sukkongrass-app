# 繁殖方法の読み直し（決め方）

宿根草916品種のマスター（北海道広尾町の生産者）。文献の値と文から、繁殖方法（どうやって増やすか）を1品種ずつ決め直す。
**推測で値を作らない。品種名や今のマスターの値だけで決めない。当てはまる文献の値も文もなければ null。**

## 値（次の語の並び。当てはまるものを全部、この順で）
- 株分け：division、divide、lift and divide、Teilung
- 挿し木：stem cuttings、basal cuttings、softwood / semi-ripe / hardwood cuttings、tip cuttings、Stecklinge（茎や芽の挿し木。草の芽挿しもここ）
- 根挿し：root cuttings、Wurzelschnittlinge
- 実生：seed、sow、Aussaat（下の「品種名のある商品の実生」に注意）
- その他：地下茎分割（rhizome division）、取り木（layering）、ランナー・子株（runners、offsets、plantlets、stolons）。値は「その他（ランナー）」のように中身を括弧で書く

## 入力（1行1品種の JSON）
- RHS・品種：Propagation（RHS の繁殖の欄。いちばん大事）と、そのほかの欄の関わる文
- NC State：段階と Recommended Propagation Strategy などの値・文
- MBG：段階と、Culture などの「Propagate by …」の文
- Walters・品種、Gaißmayer、stauden.de（段階と値）、おぎはら（段階と楽天の値・文）
- Jelitto（種子の会社）：その種・品種の種子を売っているページがある、という印だけ（段階）
- 今の値・今の値の文献・今のマスター：比べるためだけ

## 決め方
- 「どう増やすか」を書く文・値だけを使う。次は繁殖方法ではない：
  - self-seeds（こぼれ種で増える）、seed heads（花がら・種の穂）、cut back、deadhead、spreads by rhizomes（広がり方の説明）
  - ただし「Propagate by … or by seed」「can be grown from seed」「easily grown from seed」は実生
- 文献の段階：繁殖の方法は種でほぼ共通なので、品種のページを優先し、なければ**種のページも使ってよい**（trial/RULES.md の propagation と同じ）。属のページ・RHS の [Genus] の文は使わない
- **品種名のある商品の実生**：品種は種から育てると親と同じにならないことが多い。品種名のある商品には、次のときだけ 実生 を入れる
  - 品種のページ（RHS・品種、Walters、stauden.de の（cultivar）、Gaißmayer・品種など）が seed / sow / Aussaat を挙げている
  - または、文献が「comes true from seed」「seed strain」「seed-raised」とその品種について書いている
  - または、Jelitto の段階が「品種」（種子会社がその品種の種子を売っている＝種子系の品種）
  - 種のページだけが seed を挙げているときは入れない（メモに「種のページは実生も挙げる」と書く）
- 品種名のない商品（種の商品）は、種のページの seed も 実生 に入れる。Jelitto の段階「種」（その種の種子を売っている）も 実生 の根拠にしてよい
- 文献の順（DECISIONS.md の「その他」の順位）：RHS → NC State → MBG → Walters → Gaißmayer → stauden.de → Jelitto → おぎはら。方法は足し算でまとめる（どれか1つの文献が挙げていれば入れる）。ただし文献が「division is not recommended」「resents division」「does not divide well」など、その方法を勧めないと書くときは入れず、メモに書く
- 迷ったら、いちばんよい読みを書いて 確かさ を 低 にし、メモに理由

## 出力
1品種1行の JSON（JSON Lines）。全品種を書く（今と同じでも書く）。
{"商品番号": …, "繁殖": ["株分け", "挿し木", …] または null, "段階": "品種"|"種"|"品種と種"|null, "決め手": "[文献・段階] 原語（短く引用）／…", "今と違う": true|false, "食い違い": "勧めない・食い違う記述（なければ null）", "確かさ": "高|中|低", "メモ": "今と違う理由・迷った点（日本語、短く）"}
- 並びは 株分け → 挿し木 → 根挿し → 実生 → その他（…）の順
- 「今と違う」は 今の値（「株分け、挿し木（RHS）」の形）の方法の組と比べる（今のマスターとは比べない）
