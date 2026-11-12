const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
(async () => {
  const out = path.join(__dirname, 'export'); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1240, height: 1754 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'flyers.html'));
  await p.evaluate(() => document.fonts.ready);
  const names = ['Secsaway_Flyer_01_Every_Handover', 'Secsaway_Flyer_02_Track_Every_Handover'];
  const els = await p.$$('section.fl');
  for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: path.join(out, names[i] + '.jpg'), type: 'jpeg', quality: 95 });
  // A4 PDF: 1240px design width scaled to 210mm
  await p.pdf({ path: path.join(out, 'Secsaway_Flyers_A4.pdf'), width: '210mm', height: '297mm', printBackground: true,
    scale: 210 / (1240 * 25.4 / 96), margin: { top: 0, bottom: 0, left: 0, right: 0 } });
  await b.close();
})();
