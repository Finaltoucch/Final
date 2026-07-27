#!/usr/bin/env node
/* Renders every card to a 4K PNG.
 *
 * The card is authored at 1000 CSS px square; raising the device pixel ratio
 * to 3.84 makes the browser rasterise it at 3840 x 3840 natively. Nothing is
 * resampled — vector art and text are drawn at the output resolution.
 */
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const SIZE = Number(process.env.SIZE || 3840);
const ONLY = process.argv.slice(2);

(async () => {
  const outDir = path.join(__dirname, 'out', `${SIZE}`);
  fs.mkdirSync(outDir, { recursive: true });

  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage({
    viewport: { width: 1120, height: 1120 },
    deviceScaleFactor: SIZE / 1000,
  });
  page.on('pageerror', e => console.error('page error:', e.message));
  page.on('console', m => { if (m.type() === 'error') console.error('console:', m.text()); });
  await page.goto('file://' + path.join(__dirname, 'replica-deck.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(() => {
    document.documentElement.classList.add('export');
    document.querySelectorAll('.stage').forEach(s => { s.style.width = s.style.height = '1000px'; });
    document.querySelectorAll('.card').forEach(c => c.style.removeProperty('--s'));
  });
  await page.waitForTimeout(300);

  for (const el of await page.$$('.card')) {
    const slug = await el.evaluate(e => e.dataset.slug);
    if (ONLY.length && !ONLY.some(f => slug.includes(f))) continue;
    const file = path.join(outDir, `${slug}.png`);
    await el.screenshot({ path: file });
    console.log(`${slug}.png  ${SIZE}x${SIZE}  ${(fs.statSync(file).size / 1024).toFixed(0)} KB`);
  }

  await browser.close();
})();
