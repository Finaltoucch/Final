// Exports each v5 flyer as its own PDF (1080x1350 px page) with live text and vector logo.
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
(async () => {
  const out = path.join(__dirname, 'export-v5', 'editable-pdf'); fs.mkdirSync(out, { recursive: true });
  const names = ['Secsaway_Flyer_1_Never_Go_Off_Route', 'Secsaway_Flyer_2_Accounted_For', 'Secsaway_Flyer_3_December_In_Motion'];
  const b = await chromium.launch();
  for (let i = 0; i < names.length; i++) {
    const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
    await p.goto('file://' + path.join(__dirname, 'flyers_v5.html'));
    await p.waitForSelector('body[data-ready="1"]');
    // keep only flyer i
    await p.evaluate(k => { document.querySelectorAll('section.fl').forEach((s, j) => { if (j !== k) s.remove(); }); document.body.style.background = '#fff'; }, i);
    await p.addStyleTag({ content: '@page{size:1080px 1350px;margin:0} html,body{margin:0}' });
    await p.pdf({ path: path.join(out, names[i] + '.pdf'), width: '1080px', height: '1350px', printBackground: true, preferCSSPageSize: true });
    await p.close();
  }
  await b.close();
})();
