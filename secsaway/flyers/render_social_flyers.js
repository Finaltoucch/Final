const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
(async () => {
  const out = path.join(__dirname, 'export-social'); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'social_flyers.html'));
  await p.waitForSelector('body[data-ready="1"]');
  const names = ['Secsaway_Flyer_A_On_Time', 'Secsaway_Flyer_B_Ready_To_Ship', 'Secsaway_Flyer_C_Safe_Hands'];
  const els = await p.$$('section.fl');
  for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: path.join(out, names[i] + '.jpg'), type: 'jpeg', quality: 95 });
  await b.close();
})();
