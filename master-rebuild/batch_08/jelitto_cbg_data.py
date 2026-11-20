# Jelitto（s11）とシカゴ植物園（s08）: タリクトラム・コレオプシス・リアトリス・リシマキア・ベロニカストラム・エリンジウム・ミスカンサス・モリニア。
# 【Jelitto は読みかけ】2026-11-20 に Chrome で検索まで済ませた（Thalictrum 13件・Coreopsis 15件・Liatris 11件・Lysimachia 12件・Veronicastrum 6件・Eryngium 21件・Miscanthus 4件・Molinia 2件）。
#   読むページ（/Seed/Perennials/<属の大文字>+<名前>+Portion+s.html。グラスは /Seed/Ornamental+Grasses/）:
#   THALICTRUM aquilegiifolium・delavayi・delavayi Album・flavum ssp glaucum・rochebruneanum、COREOPSIS rosea・verticillata、
#   LIATRIS pycnostachya・scariosa・scariosa Alba・spicata・spicata Floristan Violet・spicata Floristan White・spicata Kobold Strain、LYSIMACHIA punctata・vulgaris、
#   VERONICASTRUM sibiricum・virginicum f albiflorum（/Seed/Herbs/）、ERYNGIUM planum・planum Blue Glitter・planum Blue Hobbit・planum White Glitter・variifolium・yuccifolium、
#   MISCANTHUS sinensis、MOLINIA caerulea ssp arundinacea・caerulea ssp caerulea
# (試行ID のリスト, 表記, level, 原産地, 花色, 花期, ゾーン, 草姿, 花を含む高さ, 土, 日照, 特徴・用途, 原産地の日本語訳)
CHECKED = "2026-11-20"
JELITTO = []
AUTUMN = {}
CBG = {}
# シカゴ植物園 Plant Evaluation Notes（試験地は USDA 5b、日なた）。pdftotext -raw で読んだ。
#   no28 Meadow rues（https://www.chicagobotanic.org/downloads/planteval_notes/no28_meadowrues.pdf）Table 1 と本文。総合評価は4つ星 good・3つ星 fair・2つ星 poor
#   no9 Blazing stars（リアトリス）は PDF が画像だけで、文字として読めなかった（no5 Yarrow と同じ）
#   コレオプシス・リシマキア・ベロニカストラム・エリンジウム・ミスカンサス・モリニアの号は一覧（no1〜no40）にない
#   'Thundercloud'・delavayi 'Album'・'Black Stockings' は試験に入っていない
# 試行ID: (報告での表記, level, 草丈 in, 株幅 in, 秋の葉色, 切り戻し, 草姿, メモ)
CBG_V = {
 "Th01": ("aquilegiifolium 'Purpureum'", "cultivar", 42, 20, None, None, None,
          "総合評価 good（4つ星）。花つき 60〜80%。種や var. album より丈夫で花が多い。花色は株によって幅があり、種よりわずかに濃い程度。試験地の条件（土の水分が一定でない・日なた）でアキレジフォリウムは草勢が弱った（no28）"),
 "Th03": ("delavayi", "species", 33, 14, None, None, None,
          "総合評価 poor（2つ星）。植え付け後の根づきが悪く、8株中7株が最初の冬（1998-99）に枯れ、残る1株も2000-01の冬に枯れた。再試験はしていない（no28）"),
 "Th05": ("flavum ssp. glaucum", "species", 72, 30, None, None, None, "総合評価 good（4つ星）。花つき 60〜80%（no28）"),
 "Th07": ("'Elin'", "cultivar", 96, 42, None, None, None,
          "総合評価 good（4つ星）。花つき 60〜80%。草勢は両親をしのぎ、茎は8フィート（約2.4m）に達した。夏の間も葉を落とさずよく茂った。2001年と2003年にひどいうどんこ病が出た（no28）"),
 "Th08": ("rochebruneanum", "species", 72, 30, None, None, None, "総合評価 good（4つ星）。花つき 60〜80%。夏に葉を落として株がすく（'Elin' との比較の記述）（no28）"),
}
