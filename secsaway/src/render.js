const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const root = path.resolve(__dirname, '..');
  const out = path.join(root, 'export'); fs.mkdirSync(path.join(out, 'jpeg'), { recursive: true });
  const names = fs.readFileSync(path.join(root, 'pages.txt'), 'utf8').trim().split('\n');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.join(root, 'brand-book.html'));
  await page.evaluate(() => document.fonts.ready);
  const fonts = await page.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight));
  console.log('fonts loaded:', fonts.join(', '));
  await page.pdf({ path: path.join(out, 'Secsaway_Brand_Guidelines_v1.0.pdf'), width: '1920px', height: '1080px', printBackground: true, preferCSSPageSize: true });
  for (let i = 0; i < names.length; i++) {
    const el = await page.$('#p' + (i + 1));
    await el.screenshot({ path: path.join(out, 'jpeg', `Secsaway_${String(i + 1).padStart(2, '0')}_${names[i]}.jpg`), type: 'jpeg', quality: 92 });
  }
  // logo PNGs, 2000px wide, transparent
  const lp = path.join(root, 'logo-pack');
  for (const f of fs.readdirSync(lp).filter(f => f.endsWith('.svg'))) {
    const svg = fs.readFileSync(path.join(lp, f), 'utf8');
    const m = svg.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/); const w = +m[1], h = +m[2];
    const H = Math.round(2000 * h / w);
    const p2 = await browser.newPage({ viewport: { width: 2000, height: H }, deviceScaleFactor: 1 });
    await p2.setContent(`<html><body style="margin:0;background:transparent">${svg.replace(/width="[\d.]+" height="[\d.]+"/, 'width="2000" height="' + H + '"')}</body></html>`);
    await p2.screenshot({ path: path.join(lp, f.replace('.svg', '.png')), omitBackground: true, clip: { x: 0, y: 0, width: 2000, height: H } });
    await p2.close();
  }
  await browser.close();
})();
