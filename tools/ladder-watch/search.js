// アルミラダー（アルミブリッジ）出品監視スクリプト
// 条件: 長さ3.6m以上・耐荷重3t以上
//   発送可 → 全国 / 引き取りのみ → 北海道のみ
// 使い方: node tools/ladder-watch/search.js [--all]
//   seen.json に記録済みのIDは「新着」から外す。--all で全件表示。
// 出力: result.json と result.md（同じフォルダ）
const fs = require('fs');
const path = require('path');

const DIR = __dirname;
const SEEN = path.join(DIR, 'seen.json');
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36';
const QUERIES = ['アルミブリッジ', 'アルミラダー', 'ラダーレール', '重機 ブリッジ', 'ユンボ ブリッジ', 'トラクター ブリッジ', 'アルミ 歩み板', '昭和ブリッジ', 'アルミブリッジ 3t', 'アルミブリッジ 360'];
const MIN_LEN_CM = 360;
const MIN_CAP_T = 3;
const MAX_PRICE = 100000; // 予算上限（円）。価格不明は通知対象に含める
const EXCLUDE_NEW = true; // 新品（業者の新品販売）は通知しない

const norm = (s) => (s || '').normalize('NFKC');

// 長さ(cm)と耐荷重(t)をタイトル・本文から読み取る。見つからなければ null。
function parseSpec(text) {
  const t = norm(text).replace(/,/g, '');
  const lens = [];
  for (const m of t.matchAll(/(\d{3})(?:\.\d+)?\s*(?:cm|センチ|㎝)/gi)) lens.push(+m[1]);
  for (const m of t.matchAll(/(?<![\d.])(\d(?:\.\d{1,2})?)\s*(?:m(?!m)|メートル|メ-トル|ｍ)/gi)) lens.push(Math.round(+m[1] * 100));
  for (const m of t.matchAll(/(?:全長|長さ|L)\s*[:=]?\s*(\d{4})\s*(?:mm|ミリ)/gi)) lens.push(Math.round(+m[1] / 10));
  const caps = [];
  for (const m of t.matchAll(/(\d+(?:\.\d+)?)\s*(?:t(?![a-z])|トン|噸)/gi)) caps.push(+m[1]);
  for (const m of t.matchAll(/(\d{3,5})\s*kg/gi)) caps.push(+m[1] / 1000);
  // 昭和ブリッジ等の型式 例: GP-360-45-3.0 / SBA-240-30-0.8 （長さ-幅-荷重）
  for (const m of t.matchAll(/[A-Z]{1,4}-?(\d{3})-(\d{2})-(\d{1,2}(?:\.\d)?)/g)) { lens.push(+m[1]); caps.push(+m[3]); }
  // 日軽パワーブリッジ等 例: PX40-360-45 （荷重×10-長さ-幅）
  for (const m of t.matchAll(/(?:PX|PXF|PF|NP|PK)(\d{2,3})-(\d{3})-(\d{2})/g)) { caps.push(+m[1] / 10); lens.push(+m[2]); }
  // アルーダ等「長さ360」（単位なし3桁）
  for (const m of t.matchAll(/(?:全長|長さ)\s*[:：]?\s*(\d{3})(?!\d)/g)) lens.push(+m[1]);
  // 「長さ3m60cm」
  for (const m of t.matchAll(/(\d)\s*m\s*(\d{2})\s*(?:cm|センチ)/gi)) lens.push(+m[1] * 100 + +m[2]);
  // 「3600x370mm」
  for (const m of t.matchAll(/(?<!\d)(\d{4})\s*[x×*]\s*\d{2,3}\s*mm/gi)) lens.push(Math.round(+m[1] / 10));
  // 「全長約3600mm」「3000mm」など
  for (const m of t.matchAll(/(?<!\d)(\d{4})\s*mm/gi)) { const v = +m[1]; if (v >= 1000 && v <= 8000) lens.push(Math.round(v / 10)); }
  // 「全長3,620」のように単位なしの4桁
  for (const m of t.matchAll(/全長\s*[:：]?\s*(\d{4})(?!\s*\d)/g)) lens.push(Math.round(+m[1] / 10));
  const plausibleLen = lens.filter((x) => x >= 100 && x <= 800);
  const plausibleCap = caps.filter((x) => x > 0 && x <= 30);
  return {
    len: plausibleLen.length ? Math.max(...plausibleLen) : null,
    cap: plausibleCap.length ? Math.max(...plausibleCap) : null,
  };
}

// 判定: ok=両方条件満たす / check=片方以上不明だが除外理由なし / ng=条件未満
function judge(spec) {
  if (spec.len !== null && spec.len < MIN_LEN_CM) return 'ng';
  if (spec.cap !== null && spec.cap < MIN_CAP_T) return 'ng';
  if (spec.len !== null && spec.cap !== null) return 'ok';
  return 'check';
}

const RELEVANT = /ブリッジ|ラダー|歩み板|あゆみ板|渡り板/;
// 重機・農機用らしさ（タイトルにどれか必要）
const HEAVY = /アルミ|重機|農機|トラクター|ユンボ|建機|コンバイン|バックホ|積載|昭和ブリッジ|日軽|パワーブリッジ|アルインコ|ピカ|PICA|ハセガワ|長谷川|ブリッジ\s*2本|2本\s*セット|\d(?:\.\d)?\s*(?:t|トン)/i;
const IRRELEVANT = /足場板|踏板|ステージ|シャツ|ニット|セーター|眼鏡|メガネ|サングラス|クレストブリッジ|タワーブリッジ|トレーニング|インレー|クラウン|コミック|キャンバス|ギター|ベース|ネックレス|指輪|プラスチック|カースロープ|ジャッキ|バイク用|自転車|車椅子|車いす|犬|ペット|ドッグ|脚立|はしご|梯子|キャンピング|スノーボード|ブリッジ\s*(?:ピン|ベース)|ラダーラック|ラダーフレーム|ルーフ|プラモデル|トミカ|ミニカー|ラダーテーブル|ラダーシェルフ|ハンガー/;
const NEW_ITEM = /新品|未使用|メーカー直送|法人様お届け|送料無料.*新品/;
const PICKUP_ONLY = /引き?取り?限定|引取限定|直接引き?取り?のみ|手渡し(?:のみ|限定)|発送不可|発送できません|配送不可/;
const HOKKAIDO = /北海道|十勝|帯広|広尾|札幌|旭川|釧路|函館|苫小牧|北見/;

// curl を使う（プロキシ環境変数をそのまま使えるため）
const { execFile } = require('child_process');
function get(url) {
  return new Promise((resolve, reject) => {
    execFile('curl', ['-sSL', '--fail', '--max-time', '40', '-A', UA, '-H', 'Accept-Language: ja-JP', url],
      { maxBuffer: 64 * 1024 * 1024, encoding: 'utf8' },
      (err, out) => (err ? reject(new Error(`${err.message.split('\n')[0]} ${url}`)) : resolve(out)));
  });
}

// ---------------- ヤフオク ----------------
async function yahoo() {
  const out = new Map();
  for (const q of QUERIES) {
    try {
      const html = await get(`https://auctions.yahoo.co.jp/search/search?p=${encodeURIComponent(q)}&n=100&s1=new&o1=d`);
      const m = html.match(/<script id="__NEXT_DATA__"[^>]*>([\s\S]*?)<\/script>/);
      if (!m) continue;
      const items = JSON.parse(m[1])?.props?.pageProps?.initialState?.search?.items?.listing?.items || [];
      for (const it of items) {
        if (out.has(it.auctionId)) continue;
        out.set(it.auctionId, {
          site: 'ヤフオク', id: 'y:' + it.auctionId, title: norm(it.title),
          price: it.buyNowPrice && it.isFixedPrice ? it.buyNowPrice : it.price,
          priceNote: it.isFixedPrice ? '定額' : `現在価格（入札${it.bidCount}件, 即決${it.buyNowPrice ?? 'なし'}）`,
          url: `https://auctions.yahoo.co.jp/jp/auction/${it.auctionId}`,
          area: it.prefectureCode === 1 ? '北海道' : `都道府県コード${it.prefectureCode}`,
          hokkaido: it.prefectureCode === 1,
          end: it.endTime, start: it.startTime, isNew: it.itemCondition === 'NEW',
        });
      }
    } catch (e) { console.error('yahoo', q, e.message); }
  }
  return [...out.values()];
}

async function yahooDetail(item) {
  try {
    const html = norm(await get(item.url));
    const text = html.replace(/<script[\s\S]*?<\/script>/g, ' ').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ');
    const loc = text.match(/発送元の地域\s*([^\s]+)/) || text.match(/発送元\s*([^\s]+)/);
    if (loc) { item.area = loc[1]; item.hokkaido = HOKKAIDO.test(loc[1]); }
    item.pickupOnly = PICKUP_ONLY.test(text) || /配送方法\s*(?:取りに来る|直接取引|引き取り)/.test(text);
    item.detailText = text.slice(0, 20000);
  } catch (e) { console.error('yahoo detail', item.url, e.message); }
}

// ---------------- ジモティー ----------------
async function jimoty() {
  const out = new Map();
  const urls = [];
  for (const q of QUERIES) {
    urls.push(['hokkaido', `https://jmty.jp/hokkaido/sale?keyword=${encodeURIComponent(q)}`]);
    urls.push(['all', `https://jmty.jp/all/sale?keyword=${encodeURIComponent(q)}`]);
  }
  for (const [scope, url] of urls) {
    try {
      const html = await get(url);
      for (const m of html.matchAll(/p-item-title[^>]*>\s*<a[^>]*href="(https:\/\/jmty\.jp\/([a-z]+)\/[^"]*article-([a-z0-9]+))"[^>]*>([^<]+)/g)) {
        const [, link, pref, id, title] = m;
        if (out.has(id)) continue;
        // 直後の価格
        const after = html.slice(m.index, m.index + 3000);
        const pm = after.match(/p-item-most-important[^>]*>\s*([\d,]+)\s*円/) || after.match(/([\d,]+)\s*円/);
        out.set(id, {
          site: 'ジモティー', id: 'j:' + id, title: norm(title).trim(), url: link,
          price: pm ? +pm[1].replace(/,/g, '') : null, priceNote: '',
          area: pref, hokkaido: pref === 'hokkaido', scope,
        });
      }
    } catch (e) { console.error('jimoty', url, e.message); }
  }
  return [...out.values()];
}

async function jimotyDetail(item) {
  try {
    const html = norm(await get(item.url));
    const text = html.replace(/<script[\s\S]*?<\/script>/g, ' ').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ');
    item.detailText = text.slice(0, 20000);
    // 一覧のタイトルは途中で切れるので、ページの<title>から全文と地域を取る
    const tt = html.match(/<title[^>]*>([^<]+)<\/title>/);
    if (tt) {
      const full = tt[1].replace(/｜ジモティー.*$/, '');
      const mm = full.match(/^(.*)\s\(([^)]*)\)\s*(\S+?)の/);
      if (mm) { item.title = mm[1].trim(); item.area = mm[3]; }
    }
    // ジモティーは基本手渡し。配送対応の記載がある場合のみ発送可扱い
    item.shipOk = /(?:配送|発送)(?:可|可能|対応|します|いたします)|ジモティーで配送|ジモティー便|宅配便で/.test(text) && !PICKUP_ONLY.test(text);
    item.pickupOnly = !item.shipOk;
  } catch (e) { console.error('jimoty detail', item.url, e.message); }
}

// ---------------- メルカリ ----------------
async function mercari() {
  const { chromium } = require('playwright');
  const browser = await chromium.launch();
  const out = new Map();
  try {
    const page = await browser.newPage({ locale: 'ja-JP' });
    let batch = [];
    page.on('response', async (r) => {
      if (r.url().includes('/v2/entities:search')) { try { batch.push(...((await r.json()).items || [])); } catch {} }
    });
    for (const q of QUERIES) {
      batch = [];
      await page.goto(`https://jp.mercari.com/search?keyword=${encodeURIComponent(q)}&status=on_sale&sort=created_time&order=desc`, { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
      await page.waitForTimeout(3000);
      for (const it of batch) {
        if (out.has(it.id)) continue;
        const shop = it.itemType === 'ITEM_TYPE_BEYOND';
        out.set(it.id, {
          site: 'メルカリ', id: 'm:' + it.id, title: norm(it.name), price: +it.price, priceNote: '',
          url: shop ? `https://jp.mercari.com/shops/product/${it.id}` : `https://jp.mercari.com/item/${it.id}`,
          area: '', hokkaido: false, created: it.created ? new Date(+it.created * 1000).toISOString() : '',
        });
      }
    }
    out.page = page;
  } catch (e) { console.error('mercari', e.message); }
  return { items: [...out.values()], browser, page: out.page };
}

async function mercariDetail(item, page) {
  try {
    await page.goto(item.url, { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
    await page.waitForTimeout(2000);
    const text = norm(await page.evaluate(() => document.body.innerText)).replace(/\s+/g, ' ');
    item.detailText = text.slice(0, 20000);
    const loc = text.match(/発送元の地域\s*([^\s]+)/);
    if (loc) { item.area = loc[1]; item.hokkaido = HOKKAIDO.test(loc[1]); }
    item.pickupOnly = PICKUP_ONLY.test(item.title + ' ' + text);
  } catch (e) { console.error('mercari detail', item.url, e.message); }
}

// ---------------- アルーダ（ホクレン中古農機・北海道のみ） ----------------
async function aruda(browser) {
  const out = new Map();
  const page = await browser.newPage({ locale: 'ja-JP' });
  try {
    await page.goto('https://www.hokuren.or.jp/aruda/', { waitUntil: 'networkidle', timeout: 60000 });
    for (const q of ['ブリッジ', 'ラダー', '歩み板', 'あゆみ板']) {
      await page.goto('https://www.hokuren.or.jp/aruda/machine/search?init=1', { waitUntil: 'networkidle', timeout: 60000 });
      let box = page.locator('input[name="where[anyword]"]').last();
      if (!(await box.isVisible().catch(() => false))) {
        // 防御ページに当たった場合はトップを経由してやり直す
        await page.goto('https://www.hokuren.or.jp/aruda/', { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
        await page.waitForTimeout(3000);
        await page.goto('https://www.hokuren.or.jp/aruda/machine/search?init=1', { waitUntil: 'networkidle', timeout: 60000 });
        box = page.locator('input[name="where[anyword]"]').last();
      }
      await box.fill(q, { timeout: 15000 });
      await box.press('Enter');
      await page.waitForLoadState('networkidle').catch(() => {});
      for (let pg = 1; pg <= 10; pg++) {
        if (pg > 1) await page.goto(`https://www.hokuren.or.jp/aruda/machine/search?page=${pg}`, { waitUntil: 'networkidle', timeout: 60000 });
        const cards = await page.evaluate(() => [...document.querySelectorAll('#grid a.c-card')].map((a) => ({
          url: a.href,
          name: a.querySelector('.c-card__name')?.innerText || '',
          model: a.querySelector('.c-card__id')?.innerText || '',
          maker: a.querySelector('.c-card__manufacturer')?.innerText || '',
          price: a.querySelector('.c-card__price')?.innerText || '',
          shop: a.querySelector('.c-card__shop')?.innerText || '',
        })));
        if (!cards.length) break;
        let added = 0;
        for (const c of cards) {
          const id = c.url.split('/').pop();
          if (out.has(id)) continue;
          added++;
          out.set(id, {
            site: 'アルーダ', id: 'a:' + id, title: norm(`${c.name} ${c.maker} ${c.model}`).trim(), url: c.url,
            price: +(c.price.replace(/[^\d]/g, '')) || null, priceNote: '税込', area: c.shop, hokkaido: true, pickupOnly: true,
          });
        }
        if (!added) break;
      }
    }
  } catch (e) { console.error('aruda', e.message); }
  return { items: [...out.values()], page };
}

async function arudaDetail(item, page) {
  try {
    await page.goto(item.url, { waitUntil: 'networkidle', timeout: 60000 });
    const text = norm(await page.evaluate(() => document.body.innerText)).replace(/\s+/g, ' ');
    const i = text.indexOf('照会No');
    item.detailText = text.slice(i, i + 400);
    const addr = text.match(/〒\d{3}-\d{4}\s*北海道(\S+?[市町村])/);
    if (addr) item.area += `（${addr[1]}）`;
    const spec = item.detailText.match(/規格\s*(.*?)\s*年式/);
    if (spec) item.title += ` [規格: ${spec[1]}]`;
  } catch (e) { console.error('aruda detail', item.url, e.message); }
}

// ---------------- メイン ----------------
(async () => {
  const showAll = process.argv.includes('--all');
  const seen = fs.existsSync(SEEN) ? JSON.parse(fs.readFileSync(SEEN, 'utf8')) : {};

  const [y, j] = await Promise.all([yahoo(), jimoty()]);
  const m = await mercari();
  const a = await aruda(m.browser);
  const all = [...y, ...j, ...m.items, ...a.items];
  console.error(`取得: ヤフオク${y.length} / ジモティー${j.length} / メルカリ${m.items.length} / アルーダ${a.items.length}`);

  // 1次判定（タイトル）
  const stage1 = all.filter((it) => it.site === 'アルーダ' ? !IRRELEVANT.test(it.title) : RELEVANT.test(it.title) && HEAVY.test(norm(it.title)) && !IRRELEVANT.test(it.title) && judge(parseSpec(it.title)) !== 'ng');
  console.error(`タイトルで候補: ${stage1.length}`);

  // 2次判定（詳細ページ）
  await m.browser.close().catch(() => {});

  // 詳細ページを開くのは見込みのあるものだけ（未通知で、タイトルに寸法か荷重の条件を満たす記載がある / 北海道の引き取り物件）
  const promising = (it) => {
    const s = parseSpec(it.title);
    return s.len !== null || s.cap !== null || it.site === 'アルーダ' || (it.site === 'ジモティー' && it.hokkaido);
  };
  const toCheck = stage1.filter((it) => (showAll || !seen[it.id]) && promising(it));
  console.error(`詳細確認: ${toCheck.length}`);

  // ブラウザが落ちても作り直して続行する
  const { chromium } = require('playwright');
  let br = null, pg = null, arudaWarm = false;
  const page = async () => {
    if (!br || !br.isConnected() || !pg || pg.isClosed()) {
      await br?.close().catch(() => {});
      br = await chromium.launch();
      pg = await br.newPage({ locale: 'ja-JP' });
      arudaWarm = false;
    }
    return pg;
  };

  for (const it of toCheck) {
    if (it.site === 'ヤフオク') await yahooDetail(it);
    else if (it.site === 'ジモティー') await jimotyDetail(it);
    else if (it.site === 'アルーダ') {
      const p = await page();
      if (!arudaWarm) { await p.goto('https://www.hokuren.or.jp/aruda/', { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {}); arudaWarm = true; }
      await arudaDetail(it, p);
    } else await mercariDetail(it, await page());
    const tSpec = parseSpec(it.title);
    const dSpec = parseSpec(it.detailText || '');
    it.len = tSpec.len ?? dSpec.len;
    it.cap = tSpec.cap ?? dSpec.cap;
    it.verdict = judge({ len: it.len, cap: it.cap });
    it.isNew = it.isNew || NEW_ITEM.test(it.title);
    if (it.pickupOnly === undefined) it.pickupOnly = PICKUP_ONLY.test(it.title);
    // 地域条件: 引き取りのみ → 北海道のみ
    it.areaOk = !it.pickupOnly || it.hokkaido;
    delete it.detailText;
  }
  await br?.close().catch(() => {});
  await a.page?.context().browser()?.close().catch(() => {});

  // 長さ・荷重とも不明なものは通知しない（ノイズが多いため）。片方だけ不明なものは「要確認」で通知。
  const matched = toCheck.filter((it) => it.verdict !== 'ng' && it.areaOk && (it.len !== null || it.cap !== null)
    && !(EXCLUDE_NEW && it.isNew) && !(it.price != null && it.price > MAX_PRICE));
  matched.sort((a, b) => (a.isNew - b.isNew) || ((a.verdict === 'ok' ? 0 : 1) - (b.verdict === 'ok' ? 0 : 1)) || ((a.price ?? 1e9) - (b.price ?? 1e9)));
  const fresh = matched.filter((it) => showAll || !seen[it.id]);

  const now = new Date().toISOString();
  // 確認済みのものは条件外でも記録（毎日同じ物を開き直さないため）
  for (const it of toCheck) if (!seen[it.id]) seen[it.id] = now;
  fs.writeFileSync(SEEN, JSON.stringify(seen, null, 1));
  fs.writeFileSync(path.join(DIR, 'result.json'), JSON.stringify({ at: now, matched, fresh }, null, 1));

  const fmt = (it) => {
    const spec = `長さ${it.len ? it.len + 'cm' : '不明'}・耐荷重${it.cap ? it.cap + 't' : '不明'}`;
    const how = it.pickupOnly ? `引き取りのみ（${it.area || '北海道'}）` : `発送可/発送元:${it.area || '不明'}`;
    return `- [${it.verdict === 'ok' ? '条件一致' : '要確認'}]${it.isNew ? '[新品]' : '[中古]'} ${it.site} ${it.title}\n  ${it.price != null ? it.price.toLocaleString() + '円' : '価格不明'} ${it.priceNote || ''} / ${spec} / ${how}${it.end ? ' / 終了 ' + it.end.slice(0, 16).replace('T', ' ') : ''}\n  ${it.url}`;
  };
  const md = `# アルミラダー検索結果 ${now.slice(0, 10)}\n\n新着 ${fresh.length} 件（候補合計 ${matched.length} 件）\n\n${fresh.map(fmt).join('\n') || '新着なし'}\n`;
  fs.writeFileSync(path.join(DIR, 'result.md'), md);
  console.log(md);
})();
