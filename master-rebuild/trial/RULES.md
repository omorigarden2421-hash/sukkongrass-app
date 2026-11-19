# 試作マスターの値の決め方（当てはめルール）

あなたの仕事は、集めた文献の記述（trial/evidence/Pxx.json）を、下のルールでマスターの値に当てはめることです。
**新しく文献を調べに行かない。** evidence にある記述だけを使う。推測で値を作らない。当てはまる記述がなければ空欄（null）。

## 入力
- trial/evidence/Pxx.json … 文献の記述（field, value_ja, quote, source, url, level）
- trial/input/Pxx.json … 今のマスターの一部（参考。値を写さない）
- trial/kew.json … Kew（英国王立植物園）の学名データの照合結果

## 文献の優先順位（文献どうしが食い違うとき）
- 文献ID: s01=RHS、s02=MBG（ミズーリ植物園）、s04=YList、s08=シカゴ植物園、s07=ミネソタ大、s06=NC State、s09=Wildflower Center、s10=perennials.com／Walters、s12=育種会社、s18=stauden.de 無料データベース（ドイツ宿根草生産者協会 BdS）、s17=Gaißmayer（ドイツのナーサリー）、s11=Jelitto（ドイツの種子会社）
- **耐寒・越冬に関わる項目**（usda）: s08 > s07 > s01 > s02 > s10 > s06 > その他
- **暑さ・蒸れに関わる項目**（heat、muggy、west_sun、heat_note、evergreen_warm）: s06 > s02 > s01 > s10 > s08 > その他
- **それ以外**: s01 > s08 > s06 > s02 > s07 > s09 > s10 > s12 > s18 > s17 > s11
- s02・s18 の位置は 2026-11-19 にユーザー確認済み。MBG はセントルイス（夏が高温多湿）の植物園なので、暑さの項目では NC State の次に置いた。
- s18（ドイツ）の耐寒ゾーン（hardiness_zone_de）・花の高さ・花期は値に使わない（耐寒性・草丈・花期は今のマスターの値を使う決定のため）。s18 の exposure・function_type・vigor・trial_rating・care・ornamental・uses も値には使わない（記録のみ）。
- s18 は用語を選ぶ形式のデータなので、他の文献に記述がない項目を埋めるのに使い、他の文献の文章による記述と食い違うときは文章の方を採って conflicts に書く。
- s17・s11 の扱い（2026-11-19 にユーザー確認済み）:
  - 順位は s18 の下（s18 > s17 > s11）。他の文献に記述がない項目を埋めるのに使う（増え方・こぼれ種・切り戻し・冬の保護・病害虫・毒・香り・切り花など）。
  - 耐寒ゾーン（s17 の hardiness_zone_de、s11 の usda_zone）・花期・高さは値に使わない（記録のみ。s18 と同じ）。usda_min／usda_max を決めるときも s11 のゾーンは使わない。
  - 暑さ・蒸れ（heat、muggy）の判定には使わない（記録のみ）。s11・s17 の heat_humidity の記録があっても heat・muggy は決めない。west_sun では、日なたで葉が色あせる・強い日なたの条件など、日差しについての記述は使ってよい。
  - 例外: Jelitto が発表元の品種（P05 アキレア 'ラブパレード'、P12 エキナセア 'マグナス'）では、s11 を育種会社の品種情報（s12）と同じ順位で扱う。ゾーン・花期・高さ・暑さを使わない点は変わらない。
  - s17 の質問への回答（Antwort）はナーサリー自身の文として使ってよい。s11・s17 の uses・exposure・vigor・trial_rating・care・function_type は値に使わない（記録のみ。s18 と同じ）。
- 数値（株張り）だけは例外: 品種レベルの具体的な数値（cm・インチ）を出している文献を優先（s10 > s08 > s06 > s12）。具体的な数値がなく RHS の幅（例 0.1〜0.5m）しかなければ RHS を使う。
- 採用しなかった食い違いは conflicts に書く。

## 種・属レベルの情報を品種に使ってよい項目
- **使ってよい**（level が species／genus でも採用。level をそのまま記録）: accepted_name の種部分、synonyms、common_name_ja、native_range、sun、usda、rhs_h、heat、muggy、west_sun、heat_note、drought、soil_moisture、soil_ph_type、salt、evergreen_warm、spread_modes、self_seed_level、rhizome_level、mixing、invasive_note、toxicity、pests、pruning、pruning_codes、management_type、division_interval、propagation、pollinator
- **使わない**（品種レベルの記述がなければ null）: flower_color_detail、flower_color_class、spread_min/max、foliage_class、foliage_features、seasonal_foliage、fragrance、silhouette、cut_flower
- ただし商品が種そのもの（品種名なし。例 Sagina subulata、Alchemilla saxatilis、Lysimachia nummularia、Patrinia scabiosifolia、Geranium phaeum）なら、種レベルの記述は「品種レベル」と同じ扱いでよい。

## 出力: trial/rows/Pxx.json
```json
{"id":"P01","fields":{
  "<field>":{"value":<値>,"method":"記載|判定","sources":["s01","s10"],"level":"cultivar|species|genus","note":"任意"}
 },
 "conflicts":[{"field":"spread","detail":"RHS 0.1-0.5m／Walters 45-60cm。Walters を採用"}],
 "name_review":{"current":"マスターの学名","proposed":"文献の正名（RHS優先、Kew で種名を確認）","reason":"日本語で","source":"s01 / Kew"},
 "notes":"日本語"}
```
- method: 文献の言葉をそのまま値にした → 記載。下の対応表で区分に当てはめた → 判定。
- 値がないときは {"value":null}。

## 項目と当てはめ方
| field | 値の形 | ルール |
|---|---|---|
| accepted_name | 文字列 | RHS の正名（品種名含む）。RHS で Unresolved／なしなら Kew の正名＋品種名。品種名の大文字小文字・引用符（半角 '）を正しく |
| synonyms | 配列 | 文献にある旧学名・別名（品種の別名も） |
| flower_color_detail | 日本語文字列 | 優先文献の花色を日本語で（例 レモンイエロー、淡いラベンダー） |
| flower_color_class | 配列 | 赤／ピンク／青・紫／オレンジ・アプリコット／黄／白／その他 から。花が目立たない・観賞しないなら ["その他"] |
| spread_min, spread_max | 数値(cm) | インチ×2.54、フィート×30.48、m×100 で cm に。整数に丸める |
| foliage_class | 文字列 | グリーン系／ゴールド・ライム系／ブルー系／シルバー系／パープル・ブラック系／ブロンズ・レッド系／斑入り／季節変化型 のどれか1つ。斑入りは斑入りを優先。季節で大きく色が変わる（新芽と夏で違う等）は季節変化型 |
| foliage_features | 配列(日本語) | 斑の入り方、毛、切れ込み、光沢など。葉色以外の特徴 |
| seasonal_foliage | 日本語文字列 | 紅葉・冬の葉色・新芽の色など |
| fragrance | 文字列 | 花／葉／花と葉。「香りがない」と明記されていれば なし。記述なしは null |
| silhouette | 文字列 | 直立（upright, erect, columnar）／ドーム（mounded, mounding, dome, cushion, rounded）／株立ち（clump-forming で茎が複数立つ、bushy, shrub, vase-shaped）／アーチ（arching, fountain で草本・低木）／グラス（イネ科・カヤツリグサ科で葉が噴水状に広がる）／ロゼット（basal rosette）／マット（mat-forming, creeping, carpet, trailing groundcover）／つる（climber, twining, vine）。複数当てはまれば成株の全体の形に最も近いもの1つ |
| sun | 文字列 | 日向（full sun のみ）／日向〜半日陰（full sun to part shade）／半日陰（part shade, partial shade, dappled）／日陰（full shade）。RHS の Full sun + Partial shade は 日向〜半日陰 |
| usda_min, usda_max | 整数 | 3a などは数字部分。食い違いは優先順位で1つ選び conflicts へ |
| rhs_h | 文字列 | H1a〜H7 |
| common_name_ja | 文字列 | YList（s04）の和名。種レベルでよい。YList が synonym とする学名に付いた和名は note にその旨を書く。YList にない → null |
| heat | 強／中／弱 | 耐暑性＝気温への強さ（2026-11-19 決定。蒸れとは分ける）。弱: 暑さを嫌う・冷涼な気候が必要・冷涼な夏を好む・暑い夏に弱る、の明記。中: 条件つきで育つ記述だけ（暑い地域では午後の日陰を好む、暑い所で日なただと葉が焼ける、穏やかな夏を好むが枯れる記述はない）。強: heat tolerant の明記。文献が割れたら控えめな側（強と条件つきが両方あれば 中）。暑さだけを書いた記述がなければ null（USDA上限・原産地・s18 の exposure からは決めない。目安として note に書くのはよい） |
| muggy | 強／中／弱 | 蒸れ耐性＝夏の高温多湿・空気の湿気・株蒸れへの強さ（2026-11-19 決定。定義は以前のメモ「■耐暑性などの説明」）。弱: 高温多湿で溶ける（melt-out）・多湿で株腐れ・高温多湿の地域に向かない／耐えない、の明記。中: 多湿で姿が乱れる・病気が出やすいが維持できる、風通しが必要、乾いた空気を好む。強: humidity に耐える明記。割れたら控えめな側。土の話（排水の悪い土・湿った土・粘土で腐る）だけの記述は使わない。「湿った土を好む」も蒸れに強い根拠にしない。記述なし→null |
| west_sun | ◎／○／△／× | 西日耐性（2026-11-19 決定。文献に直接の記述はないので組み合わせで判定。method は必ず 判定）。×: 午後の日差し・強い日差しで葉が焼ける明記、または sun が 半日陰／日陰。△: 暑い地域では午後の日陰を勧める記述、暑い時期の日なたで弱る記述、または heat が 弱。◎: 日なたで育ち（sun が 日向 または 日向〜半日陰）、heat 強・drought 強で、午後の日陰を勧める記述がない。○: それ以外で heat が 中 以上。heat が null で日差しの記述もない→null |
| heat_note | 日本語文字列 | 暑さ・蒸れ・株腐れに関する記述の要約（1〜2文） |
| drought | 強／中／弱 | drought tolerant（定着後含む）→強。average／medium moisture→中。乾かさない・水切れに弱い→弱 |
| soil_moisture | 文字列 | 乾燥寄り（dry, dry to medium）／適湿（moist but well-drained, medium, average）／湿潤寄り（moist to wet, consistently moist, boggy）／排水必須（sharp drainage, must be well-drained, rots in wet/winter wet）／幅広く適応（wet から dry まで幅広く） |
| soil_ph_type | 日本語文字列 | pH（酸性／中性／アルカリ性）と土質（粘土／砂質／ローム／白亜質）を列挙。例「酸性〜アルカリ性、粘土・砂質・ローム」 |
| salt | ◎／○／△／× | salt tolerant・tolerates salt spray・seaside の明記→◎。moderate／some salt tolerance→○。RHS の植栽場所に Coastal があるだけ→○（note に「RHS Coastal のみ」）。low／poor→△。not salt tolerant→×。記述なし→null |
| evergreen_warm | 常緑／半常緑／落葉 | 常緑性は1列（温暖地の値。2026-11-18 決定）。RHS（英国）・NC State・MBG・「温暖地では常緑」等の記述。s18 の Blattphase は immergrün→常緑、wintergrün→半常緑、sommergrün→落葉 と読む（他の文献に記述がないときだけ使う）。evergreen_cold は廃止（rows に残っていたら消す） |
| native_range | 日本語文字列 | 原種の原産地。交配種は「園芸品種（交配親：…）」。Kew の geographic_area を日本語に訳してよい（source は "Kew"） |
| spread_modes | 配列 | 株立ち（広がらない）／地下茎／ランナー／こぼれ種。rhizomes, suckers→地下茎。stolons, runners, roots at nodes→ランナー。self-seeds→こぼれ種。clump-forming で広がる記述がない→株立ち（広がらない） |
| self_seed_level | 0〜3 | 0: 不稔・種ができない・こぼれ種しないと明記。1: may self-seed、少し。2: self-seeds freely／readily。3: aggressively、weedy、種で侵略的。記述なし→null |
| rhizome_level | 0〜3 | 0: clump-forming で広がらない明記。1: slowly spreading。2: spreads／vigorous spreader。3: aggressive, invasive spreading, 隔離推奨。記述なし→null |
| mixing | 文字列 | 侵略的（隔離推奨）: invasive／aggressive の明記。強い（周囲を圧迫、配置注意）: vigorous spreader、can crowd out。普通（混植可）: clump-forming で上の記述なし。弱い（埋もれやすい）: weak grower, easily overwhelmed |
| invasive_note | 日本語文字列 | 侵略性・広がりすぎの注意の要約 |
| toxicity | 日本語文字列 | 例「猫に有毒（全草）」。食用の記述は毒性ではないので入れない。記述なし→null |
| pests | 配列(日本語) | 主な病害虫の名前。例 うどんこ病、さび病、ナメクジ、アブラムシ。「特になし」と明記されていれば ["特になし"] |
| pruning | 日本語文字列 | 切り戻しの方法の要約（いつ・どこまで） |
| pruning_codes | 配列 | 花後（花が終わったら切る・花がら摘み）／早春（冬〜早春に枯れた茎葉を地際で刈る）／秋（秋に刈る）／初夏（初夏に草丈を詰める・チェルシーチョップ・夏前に刈り込む）／不要（剪定不要の明記）。木本の剪定もこれに当てはめる |
| management_type | 文字列 | E 隔離推奨型: mixing が 侵略的。D 毎年株更新型: 毎年〜2年ごとの株分け・植え替え・更新が必要と明記。C 夏前切戻型: pruning_codes に 初夏、または夏に葉が傷むので切り戻す記述。B 花後刈込型: pruning_codes に 花後（返り咲き・姿を整える）。A 放任型: 上のどれでもなく、low maintenance や早春の刈り取りだけの記述。記述が全くなければ null。上から順に判定 |
| division_interval | 日本語文字列 | 例「3〜4年ごと、春」 |
| propagation | 配列 | 株分け／挿し木／実生／その他（日本語） |
| cut_flower | ◎／○ | good／excellent cut flower→◎。can be used／dried flowers／cut stems の記述→○。記述なし→null |
| pollinator | ◎／○ | RHS Plants for Pollinators のバッジ、または bee/butterfly magnet、highly attractive →◎。attracts bees／butterflies／pollinators →○。記述なし→null |

## 2026-11-18 の決定でマスターから外した項目
寿命、支柱の要否、品種群、合わせやすい植物、ポット規格、出荷時期、植え付け適期。rows には作らない。
蒸れ耐性（muggy）・西日耐性（west_sun）は 2026-11-19 に決め方を決定（上の表）。28品種の判定は scripts/heat_trial.py、rows への反映は scripts/sources/apply_heat_rows.py。
切り戻し時期は pruning_codes から assemble.py が作る（「花後」は月を入れない）。管理難易度も assemble.py が作る（耐暑性が弱だけでは「難」にしない）。

## 注意
- 侵略性・こぼれ種の量を種の記述だけから決めるときは、品種でも同じと言えるかを note に書く。ユーザーが個別に決めた例：アジュガ 'Burgundy Glow' は種の記述で隔離推奨型、スピレア 'Goldflame' は品種で確認できないため空欄（DECISIONS.md）。
- 文献の言葉は意味で判断する（キーワードの一致だけで決めない）。
- 迷ったら null にして note に理由を書く。
- name_review は学名・品種名が今のマスターと違う（つづり・別名扱い・種小名違い・属の変更など）ときだけ書く。違わなければ null。
- JSON は python3 -I -c "import json;json.load(open(...))" で必ず検証する。
