#!/usr/bin/env node
/* Renders each slide to a pixel-exact PNG (1080×1080 square,
   1080×1620 portrait) by screenshotting the un-scaled slide element. */
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const outDir = path.join(__dirname, 'png');
  fs.mkdirSync(outDir, { recursive: true });

  // the pre-installed browser predates this playwright build, so point at it directly
  const browser = await chromium.launch({
    executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  });
  const page = await browser.newPage({ viewport: { width: 1400, height: 1200 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'exam-health-carousel.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(() => {
    document.documentElement.classList.add('export');
    // drop the preview scaling the page applied on load
    document.querySelectorAll('.stage').forEach(st => {
      st.style.height = '';
      st.style.removeProperty('--s');
    });
  });
  await page.waitForTimeout(400);

  const slides = await page.$$('.slide');
  const report = [];
  for (const slide of slides) {
    const meta = await slide.evaluate(el => {
      const frame = el.querySelector('.frame');
      const main = el.querySelector('.main');
      return {
        idx: el.dataset.idx,
        fmt: el.dataset.fmt,
        w: el.offsetWidth,
        h: el.offsetHeight,
        // does the content actually fit the fixed canvas?
        overflow: Math.max(0, frame.scrollHeight - frame.clientHeight),
        mainOverflow: Math.max(0, main.scrollHeight - main.clientHeight),
      };
    });
    const name = `${meta.fmt}-${String(meta.idx).padStart(2, '0')}.png`;
    await slide.screenshot({ path: path.join(outDir, name) });
    report.push({ ...meta, name });
  }

  // contact sheets: the whole deck at preview scale, for reviewing at a glance
  await page.evaluate(() => document.documentElement.classList.remove('export'));
  await page.setViewportSize({ width: 1180, height: 1000 });
  await page.evaluate(() => window.dispatchEvent(new Event('resize')));
  await page.waitForTimeout(300);
  for (const [id, name] of [['deck-square', 'sheet-square'], ['deck-portrait', 'sheet-portrait']]) {
    const el = await page.$('#' + id);
    await el.screenshot({ path: path.join(outDir, name + '.png') });
  }

  await browser.close();

  let bad = 0;
  for (const r of report) {
    const flag = (r.overflow > 0 || r.mainOverflow > 0) ? '  <-- OVERFLOW' : '';
    if (flag) bad++;
    console.log(`${r.name}  ${r.w}x${r.h}  frame+${r.overflow}  main+${r.mainOverflow}${flag}`);
  }
  console.log(bad ? `\n${bad} slide(s) overflow the canvas` : '\nall slides fit');
})();
