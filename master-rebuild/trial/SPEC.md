# 試作調査の仕様（宿根草マスター再作成）

あなたは宿根草生産者のマスターデータ再作成のため、決められた文献だけから品種の情報を集める調査員です。
値を「決める」のではなく、**文献に書いてあることを原文付きで集める**のが仕事です。区分への当てはめは後で別に行います。

## 使ってよい文献（これ以外は使わない）
| ID | 文献 | 取得方法 |
|---|---|---|
| s01 | RHS Plant Finder (www.rhs.org.uk/plants/...) | curl -sSL で取得可 |
| s06 | NC State Extension Plant Toolbox (plants.ces.ncsu.edu/plants/...) | curl 可 |
| s07 | University of Minnesota Extension (extension.umn.edu) | curl 可 |
| s08 | Chicago Botanic Garden (www.chicagobotanic.org/plantinfo/...、品種評価 plant evaluation の報告) | curl 可 |
| s09 | Lady Bird Johnson Wildflower Center (www.wildflower.org/plants/...) 北米原産種のみ | curl 可 |
| s10 | Walters Gardens (www.perennials.com/plants/... と www.waltersgardens.com) | curl 可 |
| s12 | 品種を作った育種会社の品種情報（例 www.provenwinners.com） | curl 可 |

- 次は **使わない**: 一般の園芸店・ナーサリーの商品ページ、gardenia.net、Wikipedia、botanic.jp、ブログ、Plant Delights、Bluestone、Hillier、prairiemoon、heathersociety など。
- 2026-11-19 更新：MBG(s02)・YList(s04)・stauden.de 無料データベース(s18) はクラウドから読める（取得方法は scripts/sources/）。Jelitto(s11)・Gaißmayer(s17) は Cloudflare の確認画面で止まるため、クラウドからは読めない（ユーザーのパソコンの Chrome で読む）。Kew POWO(s03) は scripts/kew.py で照合済み。
- 2026-11-19 追記：Jelitto(s11)・Gaißmayer(s17) はユーザーのパソコンの Chrome で読んだ（scripts/sources/chrome_curated.py）。記録には `checked` を付ける。Gaißmayer の耐寒ゾーンは hardiness_zone_de、Jelitto のゾーンは usda_zone に入れた。
- s02・s04・s18 の記録には `checked`（確認日）を付ける。s18 では SPEC の表にない field（exposure, hardiness_zone_de, function_type, vigor, trial_rating, care, winter_care, ornamental, uses）、s02 では tolerate も使う。
- 外来種リスト(s05)は別途調べるので不要。

## 取得方法
- ページ本文は Bash の `curl -sSL -m 30 -A 'Mozilla/5.0' URL` で取得し、`python3 -I` でタグを除いて読む。WebFetch はこの環境ではネットワーク許可が古く失敗することがあるので curl を優先。
- URL を探すには WebSearch を使ってよい（検索結果のページの中身は読まない。上の文献のURLを見つけるためだけ）。RHS のURLは `https://www.rhs.org.uk/plants/<数字>/<名前>/details` の形。
- 入力ファイル（trial/input/Pxx.json）には今のマスターの値と、マスターが使った出典URLがある。**出典URLのうち、上の表の文献に当てはまるものだけ**読んでよい（ユーザー承認済み）。読んだら `from_master_source: true` を付ける。マスターの値そのものを答えとして写してはいけない。
- 品種のページがなく、種や属のページにしか情報がない場合も記録してよいが、`level` を "species" または "genus" にする。品種のページなら "cultivar"。

## 集める項目（field キー）
| field | 内容 | 例（原文の語） |
|---|---|---|
| accepted_name | 文献が示す正しい学名（品種名含む） | Artemisia schmidtiana 'Nana' |
| synonyms | 旧学名・シノニム | Anemone sylvestris → Anemonoides sylvestris |
| family | 科 | Asteraceae |
| common_name_ja | 日本語名が文献にあれば | |
| group | 品種群・シリーズ・交配親 | Band of Nobles Series |
| flower_color | 花色（文献の言葉） | lemon-yellow |
| bloom_time | 花期（参考。文献の言葉そのまま） | June to August |
| height | 草丈（参考。単位そのまま、花茎込みか葉か分かれば記す） | 30-45cm |
| spread | 株張り | 45-60cm |
| foliage | 葉の色・斑・毛など | silver, finely divided |
| seasonal_foliage | 紅葉・冬の葉色 | burgundy in winter |
| fragrance | 花や葉の香り | aromatic foliage |
| habit | 形の記述 | upright, clump-forming, mounded, mat-forming |
| sun | 日照 | full sun to part shade |
| usda_zone | USDAゾーン | 4-8 |
| rhs_hardiness | RHS H値 | H5 |
| heat_humidity | 暑さ・高温多湿・夏の蒸れ・株腐れの記述 | does not tolerate hot humid summers |
| drought | 乾燥耐性 | drought tolerant once established |
| soil_moisture | 土の湿り具合・排水 | moist, well-drained |
| soil_type_ph | pH、粘土・砂質 | tolerates clay; acid to alkaline |
| salt | 耐塩・潮風 | salt tolerant / seaside |
| evergreen | 常緑・半常緑・落葉 | semi-evergreen |
| native_range | 原産地 | Japan |
| spread_mode | 増え方（地下茎・ランナー・こぼれ種・株が広がらない） | spreads by stolons; self-seeds |
| lifespan | 寿命 | short-lived |
| staking | 支柱・倒伏 | may need staking |
| toxicity | 毒性（人・ペット） | toxic to cats |
| pests_diseases | 病害虫 | powdery mildew, slugs |
| pruning | 切り戻し・刈り込みの方法と時期 | cut back after flowering |
| division | 株分けの間隔・時期 | divide every 3-4 years in spring |
| propagation | 繁殖方法 | division, seed, cuttings |
| cut_flower | 切り花 | good cut flower |
| pollinators | 蜂・蝶・ハチドリなど | attracts butterflies; RHS Plants for Pollinators |
| invasive_note | 文献の侵略性・広がりすぎの注意 | can be invasive |

## 出力
`trial/evidence/<Pxx>.json` に UTF-8 で書く:
```json
{
 "id": "P01",
 "searched_name": "Artemisia schmidtiana 'Nana'",
 "access_log": [{"source":"s01","url":"...","status":"ok|404|blocked|not_found","note":""}],
 "evidence": [
  {"field":"habit","value_ja":"低いクッション状に茂る","quote":"forms a dense, low cushion","source":"s01","url":"https://...","level":"cultivar","from_master_source":false}
 ],
 "not_found": ["toxicity","salt"],
 "notes": "調べていて気づいたこと（学名の誤り、品種の特定が難しい等）を日本語で"
}
```
- 1つの項目に複数の文献があれば、それぞれ1件ずつ記録する（文献どうしの食い違いを後で見るため）。
- quote は原文をそのまま短く（英語のまま）。value_ja はその日本語訳。推測で書かない。
- 見つからなかった項目は not_found に入れる。
- 1品種あたり、文献の取得は最大8ページ程度にとどめる。
