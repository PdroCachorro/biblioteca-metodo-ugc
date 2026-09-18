// Scrapes fastmoss.com's public (no-login) top-5 rankings for Brazil across
// 3 rank types x 3 categories, then enriches each unique product with its
// own detail-page images + real stats. Outputs ../ranking_data.json in the
// exact shape build.py expects.
//
// NOTE on the detail page's "Estrategia de Marketing" pie/donut charts:
// they show the EXACT SAME canned percentages (18/34/48%, 71/11/18%,
// 0/100%) on every product -- verified by hand across a dozen products.
// That's a fake/demo overlay for logged-out visitors, not real data, so
// this scraper does not collect it.

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const https = require('https');
const crypto = require('crypto');

const RANK_TYPES = [
  ['vendas', 'Ranking de vendas', 'saleslist'],
  ['novos', 'Ranking de novos produtos', 'newProducts'],
  ['video', 'Ranking de produtos em vídeo', 'hotvideo'],
];
const CATEGORIES = [
  ['todos', 'Todos', null],
  ['roupas', 'Roupas femininas', 2],
  ['beleza', 'Beleza e cuidados pessoais', 14],
];

const OUT_DIR = path.join(__dirname, '..');
const IMG_DIR = path.join(OUT_DIR, 'images', 'products');
fs.mkdirSync(IMG_DIR, { recursive: true });

function listUrl(slug, cid) {
  let url = `https://www.fastmoss.com/pt/e-commerce/${slug}?region=BR`;
  if (cid) url += `&l1_cid=${cid}`;
  return url;
}

async function extractListRows(page) {
  return page.evaluate(() => {
    const headers = Array.from(document.querySelectorAll('main thead th')).map(th => th.innerText.trim());
    const rows = Array.from(document.querySelectorAll('main tr.ant-table-row')).slice(0, 5);
    return rows.map(r => {
      const tds = Array.from(r.querySelectorAll('td'));
      const img = r.querySelector('img');
      const a = r.querySelector('a');
      const cells = tds.map(td => td.innerText.trim());
      const obj = {};
      headers.forEach((h, i) => { if (h) obj[h] = cells[i] || ''; });
      obj.__img = img ? img.src : null;
      obj.__href = a ? a.href : null;
      return obj;
    });
  });
}

// Maps a raw row (shape varies by rank type) into {title, price, store, img, metrics, detail_url}
function normalizeRow(rankId, raw) {
  if (rankId === 'vendas') {
    const [title, price] = raw['Produtos'].split('\nPreço de venda:');
    const store = (raw['Loja associada'] || '').split('\n')[0];
    return {
      title: title.trim(), price: (price || '').trim(), store,
      img: raw.__img, detail_url: raw.__href,
      metrics: [
        ['Vendas/dia', raw['Volume de Vendas'] || ''],
        ['Variação', raw['Variação percentual de vendas'] || ''],
        ['Receita', raw['Receita de Vendas'] || ''],
        ['GMV total', raw['GMV total'] || ''],
      ],
    };
  }
  if (rankId === 'novos') {
    const [title, rest] = raw['Produtos'].split('\nPreço de venda:');
    const price = (rest || '').split('\n')[0];
    const store = (raw['Loja associada'] || '').split('\n')[0];
    return {
      title: title.trim(), price: (price || '').trim(), store,
      img: raw.__img, detail_url: raw.__href,
      metrics: [
        ['Vendas 3d', raw['Vendas de três dias'] || ''],
        ['Receita 3d', raw['Receita de três dias'] || ''],
        ['Vendas totais', raw['Vendas totais'] || ''],
        ['GMV total', raw['GMV total'] || ''],
      ],
    };
  }
  // video
  const prodCol = raw['Produtos vendidos em transmissão ao vivo'] || '';
  const [title, rest] = prodCol.split('\nPreço de venda:');
  const price = (rest || '').split('\n')[0];
  const contentCol = raw['Conteúdo do vídeo'] || '';
  const store = contentCol.split('\n')[0];
  return {
    title: title.trim(), price: (price || '').trim(), store,
    img: raw.__img, detail_url: raw.__href,
    metrics: [
      ['Vendas', raw['Vendas totais'] || ''],
      ['GMV', raw['GMV total'] || ''],
      ['Views', raw['Total de reproduções'] || ''],
      ['Curtidas', raw['Total de curtidas'] || ''],
    ],
  };
}

async function extractDetail(page) {
  return page.evaluate(() => {
    const main = document.querySelector('main');
    const text = main.innerText;
    const lines = text.split('\n').map(s => s.trim()).filter(Boolean);
    function idx(l) { return lines.indexOf(l); }
    function after(l) { const i = idx(l); return i >= 0 ? lines[i + 1] : null; }
    function before(l) { const i = idx(l); return i > 0 ? lines[i - 1] : null; }
    const imgs = Array.from(new Set(
      Array.from(document.querySelectorAll('main img'))
        .map(i => i.src)
        .filter(s => s.indexOf('tt_product') > -1)
    ));
    return {
      imgs,
      rankRange: before('Ranking de Vendas no Brasil'),
      popularityIndex: before('Índice de popularidade'),
      vendasTotais: before('Vendas totais'),
      gmvTotal: before('GMV total'),
      numInfluencers: before('Número de influencers de vendas'),
      price: after('Preço:'),
      frete: after('Frete:'),
      tipoLogistica: after('Tipo de logística:'),
      comissao: after('Taxa de comissão:'),
      dataUpload: (after('Data estimada de upload:') || '').replace(/\s*\(GMT.*\)$/, ''),
    };
  });
}

function localName(url) {
  const h = crypto.createHash('md5').update(url).digest('hex').slice(0, 16);
  const ext = url.includes('.webp') ? '.webp' : '.jpg';
  return h + ext;
}

function download(url) {
  return new Promise((resolve, reject) => {
    const name = localName(url);
    const dest = path.join(IMG_DIR, name);
    if (fs.existsSync(dest)) return resolve('images/products/' + name);
    https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, (res) => {
      if (res.statusCode !== 200) { res.resume(); return reject(new Error('HTTP ' + res.statusCode + ' for ' + url)); }
      const chunks = [];
      res.on('data', (c) => chunks.push(c));
      res.on('end', () => {
        fs.writeFileSync(dest, Buffer.concat(chunks));
        resolve('images/products/' + name);
      });
    }).on('error', reject);
  });
}

async function main() {
  const browser = await chromium.launch();
  const page = await browser.newPage({ userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' });

  const rankings = {};
  const detailCache = new Map(); // detail_url -> detail object

  for (const [rankId] of RANK_TYPES) {
    rankings[rankId] = {};
    for (const [catId, , slugArg] of CATEGORIES) {
      const [, , slug] = RANK_TYPES.find(rt => rt[0] === rankId);
      const cid = CATEGORIES.find(c => c[0] === catId)[2];
      await page.goto(listUrl(slug, cid), { waitUntil: 'networkidle', timeout: 60000 });
      await page.waitForTimeout(1800);
      const raw = await extractListRows(page);
      const rows = raw.map(r => normalizeRow(rankId, r));
      rankings[rankId][catId] = rows;
      console.log(rankId, catId, rows.length, 'rows');
    }
  }

  // Enrich with detail pages (dedup by URL)
  const allRows = [];
  for (const rankId in rankings) for (const catId in rankings[rankId]) for (const row of rankings[rankId][catId]) allRows.push(row);
  const uniqueUrls = Array.from(new Set(allRows.map(r => r.detail_url).filter(Boolean)));
  console.log('unique detail pages:', uniqueUrls.length);

  for (const url of uniqueUrls) {
    try {
      await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
      await page.waitForTimeout(1500);
      const detail = await extractDetail(page);
      detailCache.set(url, detail);
    } catch (e) {
      console.error('detail failed', url, e.message);
      detailCache.set(url, null);
    }
  }

  await browser.close();

  // Download images (card thumb + gallery), rewrite to local paths
  for (const row of allRows) {
    try { row.img = await download(row.img); } catch (e) { console.error('img dl failed', row.img, e.message); }
    const detail = detailCache.get(row.detail_url);
    if (detail) {
      const localImgs = [];
      for (const u of detail.imgs) {
        try { localImgs.push(await download(u)); } catch (e) { console.error('gallery dl failed', u, e.message); }
      }
      detail.imgs = localImgs.length ? localImgs : [row.img];
    }
    row.detail = detail || null;
    const idMatch = (row.detail_url || '').match(/detail\/(\d+)/);
    row.tiktok_url = idMatch ? `https://shop.tiktok.com/view/product/${idMatch[1]}?region=BR&locale=en&source=agency` : null;
    delete row.detail_url;
  }

  const today = new Date().toLocaleDateString('pt-BR', { timeZone: 'America/Sao_Paulo' });
  const out = {
    rank_types: RANK_TYPES.map(([id, label]) => [id, label]),
    categories: CATEGORIES.map(([id, label]) => [id, label]),
    rankings,
    last_updated: today,
  };
  fs.writeFileSync(path.join(OUT_DIR, 'ranking_data.json'), JSON.stringify(out, null, 1), 'utf-8');
  console.log('wrote ranking_data.json');
}

main().catch((e) => { console.error(e); process.exit(1); });
