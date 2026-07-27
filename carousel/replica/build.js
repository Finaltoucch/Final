#!/usr/bin/env node
/* Assembles the self-contained replica page: inlines Lato, the nine scene
 * modules and the copy table into one HTML file with no external requests. */
const fs = require('fs');
const path = require('path');

const dir = __dirname;
const read = p => fs.readFileSync(path.join(dir, p), 'utf8');

const panels = require('./src/panels');

/* The scene modules are CommonJS so they can be linted and required from
 * node; for the page they are flattened into one object literal. */
/* the kit's export block is the last statement in the file — drop it whole */
const kitSrc = read('src/art/_kit.js');
const kit = kitSrc.slice(0, kitSrc.lastIndexOf('module.exports'));

const scenes = panels
  .filter(p => fs.existsSync(path.join(dir, `src/art/${String(p.n).padStart(2, '0')}.js`)))
  .map(p => {
    const src = read(`src/art/${String(p.n).padStart(2, '0')}.js`)
      .replace(/^const \{[^}]*\} = require\([^)]*\);$/gm, '')
      .replace(/^module\.exports = /m, '');
    return `  ${p.n}: (${src.trim().replace(/;$/, '')}),`;
  })
  .join('\n');

const art = `${kit}\nconst ART = {\n${scenes}\n};`;

const out = read('src/template.html')
  .replace('/*__FONTS__*/', () => read('src/fonts.css'))
  .replace('/*__ART__*/', () => art)
  .replace('/*__PANELS__*/', () => 'const PANELS = ' + JSON.stringify(panels, null, 2) + ';');

const dest = path.join(dir, 'replica-deck.html');
fs.writeFileSync(dest, out);
console.log('built', path.relative(process.cwd(), dest), (out.length / 1024).toFixed(1), 'KB');
