# 広がり方（こぼれ種の量・地下茎で広がる程度・混植適性）の読み直し（決め方）

宿根草916品種のマスター（北海道広尾町の生産者）。文献の文から、こぼれ種の量・地下茎で広がる程度・混植適性を決め直す。
**文献の文は意味で読む（キーワードの一致だけで決めない）。推測で値を作らない。当てはまる記述がなければ null。**

## 入力（1行1品種の JSON）
- 文: 広がり方に関わりそうな文を全部。頭の [文献・段階]（段階: 品種／種／属）。文献: NC State（ノースカロライナ州立大）、MBG（ミズーリ植物園）、Walters（米国の生産者）、RHS（英国王立園芸協会。Habit は株の形の項目）
- stauden.de（値（印））: ドイツの宿根草生産者協会のデータ。値の後ろの（cultivar／species／genus）は、その値がこの品種のもの／種から引き継いだもの／属から引き継いだもの。Wuchsverhalten＝広がり方、Wuchsstärke＝生育の強さ、MS-Generativer Ausbreitungsdrang＝種で広がる強さ、Pflegehinweis＝手入れの注意
- Gaißmayer: ドイツのナーサリーの欄（[欄名] 文）。self_seed＝こぼれ種、spread_mode＝広がり方 など
- 今の値: 今のマスターの値（比べるため）

## 段階の定義（trial/RULES.md）
- こぼれ種の量（0〜3）
  - 0：不稔・種ができない・こぼれ種しない、の明記（sterile、does not produce viable seed、keine Selbstaussaat、steril）
  - 1：may self-seed・少しこぼれ種する・こぼれ種を防ぐため種ができる前に切る（Rückschnitt vor der Samenreife um Selbstaussaat zu vermeiden）・mäßig／gelegentlich
  - 2：self-seeds freely／readily／easily／prolifically、oft Selbstaussaat、reichlich、versamt sich gern
  - 3：aggressively self-seeds、weedy、こぼれ種で侵略的・はびこる、lästig、starke Selbstaussaat
- 地下茎で広がる程度（0〜3）
  - 0：clump-forming で広がらない・地下茎を出さない、の明記（does not spread、non-spreading、keine Ausläufer、wuchert nicht）。「clump-forming」だけでは 0 にしない（null）
  - 1：slowly spreading・ゆっくり広がる・短い地下茎（kurze Ausläufer）・広がるがはびこらない
  - 2：spreads by rhizomes／stolons／runners／suckers、vigorous spreader、spreads rapidly／quickly（速く広がる）、forms colonies、ausläufertreibend、kriechend
  - 3：invasive、aggressive spreader、thug、はびこる・隔離が必要・手に負えない、wuchernd、invasiv（侵略的・攻撃的・はびこるの明記があるときだけ。「速く広がる」だけなら 2）
  - **種で広がる話（seeds carried by wind など）は地下茎ではなく、こぼれ種**
- 文献の使い方
  - 属のページの記述（段階＝属、stauden.de の genus 印）は使わない（RULES.md）
  - 文献の順：NC State → MBG → Walters → stauden.de → Gaißmayer。最初に記述のある文献の値を採り、同じ文献の中では大きい方。RHS の本文にはっきり書いてあれば、RHS を最初に採る。採らなかった文献と食い違えばメモに書く
  - 種の記述を品種に使ってよい（段階をそのまま書く）
  - 「地域によっては侵略的外来種」（法律・州の指定の話）は段階に使わず、メモに書く
- 混植適性（文献の記述から。この欄は参考で、最終の値は別の決まりとも合わせる）
  - 侵略的（隔離推奨）：invasive／aggressive／はびこるの明記、または地下茎かこぼれ種が 3
  - 強い（周囲を圧迫、配置注意）：vigorous spreader、can crowd out、spreads rapidly、地下茎 2。こぼれ種 2 は、雑草化・大きな群落・野生化の記述があるときだけ 強い（2026-11-24 の決定）
  - 普通（混植可）：株立ちで上の記述がない（こぼれ種 2 は、上の記述がなければ 普通）
  - 弱い（埋もれやすい）：weak grower、easily overwhelmed
  - 記述がなければ null

## 出力
1品種1行の JSON（JSON Lines）。全品種を書く（今と同じでも書く）。
{"商品番号": …, "こぼれ種": 0-3|null, "こぼれ種の決め手": "[文献・段階] 原文の短い引用", "地下茎": 0-3|null, "地下茎の決め手": …,
 "混植": "侵略的（隔離推奨）|強い（周囲を圧迫、配置注意）|普通（混植可）|弱い（埋もれやすい）|null", "混植の決め手": …,
 "今と違う": ["こぼれ種", "地下茎", "混植" のうち今の値と違うもの], "確かさ": "高|中|低", "メモ": "今と違う理由・迷った点（日本語、短く）"}
- 今の値の「こぼれ種の量(0-3)」「地下茎で広がる程度(0-3)」「混植適性」と比べる
- 迷ったら、いちばんよい読みを書いて 確かさ を 低 にし、メモに理由
