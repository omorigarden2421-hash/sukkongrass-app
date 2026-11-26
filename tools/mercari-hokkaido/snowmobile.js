// メルカリ: 北海道から出品されたスノーモービル本体を探す
// メルカリは出品地域で検索できないため、検索結果の新着を1件ずつ開いて「発送元の地域」を確認する。
// 使い方: node tools/mercari-hokkaido/snowmobile.js [--all]
//   seen.json に確認済みIDを記録し、新着だけを result.json / result.md に出す。--all で記録を無視。
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const DIR = __dirname;
const SEEN = path.join(DIR, 'seen.json');
const QUERIES = ['スノーモービル', 'スノーモビル', 'スノーモービル 本体', 'スノーモービル 実働'];
const MIN_PRICE = 30000; // 部品・小物を除くための下限（円）

const norm = (s) => (s || '').normalize('NFKC');
// 本体以外（部品・用品・おもちゃ等）を除く
const NOT_BODY = /パーツ|部品|ベルト|カバー|シート(?!付)|スキー板|ソリ|そり|トレーラー|ヘルメット|ウェア|ジャケット|ブーツ|グローブ|ゴーグル|ミニカー|模型|プラモ|ラジコン|おもちゃ|トミカ|ステッカー|マフラー|キャブ|ピストン|プラグ|ライト|ミラー|ハンドル|スプロケット|トラック\s*ベルト|カタログ|マニュアル|本$|DVD|ゲーム|キーホルダー|スタンド|ドリー|スキッド|クラッチ/;
const BODY_HINT = /本体|実働|不動|始動|エンジン|cc|CC|スキードゥ|ski-?doo|ヤマハ|YAMAHA|ポラリス|POLARIS|アークティック|ARCTIC|Arctic|BRP|リンクス|Lynx|LYNX|SNOSCOOT|スノースクート|VK|フェーザー|ベンチャー|SRX|PZ|MXZ|サミット|Summit|RMK|インディ|Indy/i;

(async () => {
  const showAll = process.argv.includes('--all');
  const seen = fs.existsSync(SEEN) ? JSON.parse(fs.readFileSync(SEEN, 'utf8')) : {};
  const browser = await chromium.launch();
  const page = await browser.newPage({ locale: 'ja-JP' });

  // 1. 検索
  const found = new Map();
  let batch = [];
  page.on('response', async (r) => {
    if (r.url().includes('/v2/entities:search')) { try { batch.push(...((await r.json()).items || [])); } catch {} }
  });
  for (const q of QUERIES) {
    batch = [];
    const url = `https://jp.mercari.com/search?keyword=${encodeURIComponent(q)}&status=on_sale&price_min=${MIN_PRICE}&sort=created_time&order=desc`;
    await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
    await page.waitForTimeout(3000);
    for (const it of batch) {
      if (found.has(it.id)) continue;
      const shop = it.itemType === 'ITEM_TYPE_BEYOND';
      found.set(it.id, {
        id: it.id, title: norm(it.name), price: +it.price, shop,
        url: shop ? `https://jp.mercari.com/shops/product/${it.id}` : `https://jp.mercari.com/item/${it.id}`,
      });
    }
  }
  page.removeAllListeners('response');
  const all = [...found.values()];
  const candidates = all.filter((it) => /スノーモ(?:ー)?ビル|スノーモビール|snowmobile|スノースクート/i.test(it.title) && !NOT_BODY.test(it.title) && it.price >= MIN_PRICE);
  const toCheck = candidates.filter((it) => showAll || !seen[it.id]);
  console.error(`検索結果 ${all.length} / 本体候補 ${candidates.length} / 未確認 ${toCheck.length}`);

  // 2. 新着だけ開いて発送元の地域を確認
  let detail = null;
  page.on('response', async (r) => {
    if (r.url().includes('items/get')) { try { detail = (await r.json()).data; } catch {} }
  });
  for (const it of toCheck) {
    detail = null;
    await page.goto(it.url, { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
    await page.waitForTimeout(1500);
    const text = norm(await page.evaluate(() => document.body.innerText).catch(() => '')).replace(/\s+/g, ' ');
    it.area = detail?.shipping_from_area?.name || (text.match(/発送元の地域\s*(\S+)/) || [])[1] || '';
    it.shippingPayer = detail?.shipping_payer?.name || '';
    it.shippingMethod = detail?.shipping_method?.name || '';
    it.condition = detail?.item_condition?.name || '';
    const desc = norm(detail?.description || (text.match(/商品の説明\s*(.{0,600})/) || [])[1] || '');
    it.desc = desc.replace(/\s+/g, ' ').slice(0, 300);
    it.hokkaido = /北海道/.test(it.area);
    it.bodyLikely = BODY_HINT.test(it.title + ' ' + desc) && !/(?:部品取り?用?の?み|パーツのみ)/.test(it.title);
    seen[it.id] = new Date().toISOString();
  }
  await browser.close();

  const hits = toCheck.filter((it) => it.hokkaido);
  fs.writeFileSync(SEEN, JSON.stringify(seen, null, 1));
  fs.writeFileSync(path.join(DIR, 'result.json'), JSON.stringify({ at: new Date().toISOString(), checked: toCheck.length, fresh: hits }, null, 1));
  const md = `# メルカリ 北海道のスノーモービル ${new Date().toISOString().slice(0, 10)}\n\n新着 ${hits.length} 件（確認 ${toCheck.length} 件）\n\n` +
    (hits.map((it) => `- ${it.title}\n  ${it.price.toLocaleString()}円 / ${it.shippingPayer || '送料不明'} / ${it.condition}\n  ${it.desc}\n  ${it.url}`).join('\n') || '新着なし') + '\n';
  fs.writeFileSync(path.join(DIR, 'result.md'), md);
  console.log(md);
})();
