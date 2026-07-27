#!/usr/bin/env node
/* Assembles the self-contained carousel page: inlines the subsetted
   webfonts (the published page cannot reach a font CDN) and the
   illustration module into the template. */
const fs = require('fs');
const path = require('path');

const dir = __dirname;
const template = fs.readFileSync(path.join(dir, 'src/template.html'), 'utf8');
const fonts = fs.readFileSync(path.join(dir, 'fonts-inline.css'), 'utf8');
const art = fs.readFileSync(path.join(dir, 'src/illustrations.js'), 'utf8');

const out = template
  .replace('/*__FONTS__*/', () => fonts)
  .replace('/*__ART__*/', () => art);

const dest = path.join(dir, 'exam-health-carousel.html');
fs.writeFileSync(dest, out);
console.log('built', dest, (out.length / 1024).toFixed(1), 'KB');
