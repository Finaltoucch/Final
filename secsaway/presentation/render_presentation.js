// One PDF page per module (each at its own height), merged into a single PDF; plus a long JPEG for Behance.
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs'), { execFileSync } = require('child_process');
(async () => {
  const out = path.join(__dirname, 'export'); const tmp = path.join(out, 'pages'); fs.mkdirSync(tmp, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + path.join(__dirname, 'presentation.html'));
  await p.waitForSelector('body[data-ready="1"]');
  const mods = await p.$$eval('section.m', els => els.map(e => [e.dataset.name, e.offsetHeight]));
  const files = [];
  for (let i = 0; i < mods.length; i++) {
    const [name, h] = mods[i];
    await p.evaluate(k => document.querySelectorAll('section.m').forEach((s, j) => s.style.display = j === k ? '' : 'none'), i);
    const f = path.join(tmp, String(i + 1).padStart(2, '0') + '_' + name + '.pdf');
    await p.pdf({ path: f, width: '1920px', height: h + 'px', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 }, pageRanges: '1' });
    files.push(f);
  }
  execFileSync('pdfunite', [...files, path.join(out, 'Secsaway_Brand_Identity_Presentation.pdf')]);
  await p.evaluate(() => document.querySelectorAll('section.m').forEach(s => s.style.display = ''));
  const lp = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await lp.goto('file://' + path.join(__dirname, 'presentation.html'));
  await lp.waitForSelector('body[data-ready="1"]');
  await lp.screenshot({ path: path.join(out, 'Secsaway_Brand_Identity_Presentation_long.jpg'), type: 'jpeg', quality: 90, fullPage: true });
  await b.close();
  fs.rmSync(tmp, { recursive: true });
})();
