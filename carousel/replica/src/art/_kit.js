/* Shared drawing vocabulary for the replica scenes.
 *
 * Every scene draws into the same 1000 x 1000 user space as the card, so a
 * scene may bleed off any edge exactly as the source artwork does. Colours
 * are the values measured off the source grid (see replica/README.md).
 */

const C = {
  cream:      '#FDF7EB',
  creamDeep:  '#FBF0DD',
  navy:       '#11294A',
  navyLine:   '#1A334F',
  ink:        '#1A1A1A',
  outline:    '#2B2117',   // the warm near-black every shape is drawn with
  white:      '#FBF8F1',
  paper:      '#F7F2E4',
  paperEdge:  '#E4DCC8',

  skin:       '#B4661F',
  skinLit:    '#C8792F',
  skinShade:  '#8E4E19',
  hair:       '#1B1A17',
  hairLit:    '#37332C',

  blue:       '#35558A',
  blueDeep:   '#1E3A5C',
  blueLit:    '#4A6E9E',
  blueBlob:   '#C3D6E8',
  blueBlobLt: '#DCE7F2',

  gold:       '#F2B23C',
  goldDeep:   '#D8912A',
  goldBlob:   '#FAD99E',

  wood:       '#A0632A',
  woodLit:    '#B5763F',
  woodDark:   '#7E4A20',

  clay:       '#C0492E',
  clayDeep:   '#8E3320',
  orange:     '#C9743A',

  green:      '#587353',
  greenDeep:  '#3E5B3C',
  greenLeaf:  '#4F7346',
  olive:      '#7C8A50',

  grey:       '#B6B3AB',
  greyDeep:   '#6E6A63',
};

/* Stroke weights, in the 1000-unit space. The source outlines measure ~1.5px
 * on a 415px panel, which is 3.6 here. */
const W = { hair: 4.2, form: 3.6, detail: 2.6, fine: 1.9 };

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');

/** A filled shape with the house outline. */
const sh = (d, fill, sw = W.form, extra = '') =>
  `<path d="${d}" fill="${fill}" stroke="${C.outline}" stroke-width="${sw}" ${extra}/>`;

/** A fill with no outline — shading, blobs, background washes. */
const fl = (d, fill, extra = '') => `<path d="${d}" fill="${fill}" ${extra}/>`;

/** An unfilled stroke — creases, fold lines, rule lines. */
const ln = (d, sw = W.detail, stroke = C.outline, extra = '') =>
  `<path d="${d}" fill="none" stroke="${stroke}" stroke-width="${sw}" stroke-linecap="round" ${extra}/>`;

const circ = (cx, cy, r, fill, sw = W.form) =>
  `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fill}" stroke="${C.outline}" stroke-width="${sw}"/>`;

const dot = (cx, cy, r, fill) => `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fill}"/>`;

const rect = (x, y, w, h, fill, r = 0, sw = W.form) =>
  `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${r}" fill="${fill}" stroke="${C.outline}" stroke-width="${sw}"/>`;

/** Lettering inside the artwork (book spines, signage, packaging). */
const label = (x, y, text, size, fill, weight = 900, extra = '') =>
  `<text x="${x}" y="${y}" font-family="Lato" font-size="${size}" font-weight="${weight}" ` +
  `fill="${fill}" text-anchor="middle" ${extra}>${esc(text)}</text>`;

/** An arm, leg or neck: a round-capped stroke laid over a wider outline
 *  stroke, which is far easier to steer than a closed silhouette. */
const limb = (d, width, fill = C.skin, sw = W.form) =>
  `<path d="${d}" fill="none" stroke="${C.outline}" stroke-width="${width + sw * 2}" stroke-linecap="round" stroke-linejoin="round"/>` +
  `<path d="${d}" fill="none" stroke="${fill}" stroke-width="${width}" stroke-linecap="round" stroke-linejoin="round"/>`;

/** Same idea, but the outline is drawn separately so limbs can overlap the
 *  body without cutting a notch in it: call `limbUnder` for every limb first,
 *  then `limbOver` in the same order. */
const limbUnder = (d, width, sw = W.form) =>
  `<path d="${d}" fill="none" stroke="${C.outline}" stroke-width="${width + sw * 2}" stroke-linecap="round" stroke-linejoin="round"/>`;
const limbOver = (d, width, fill = C.skin) =>
  `<path d="${d}" fill="none" stroke="${fill}" stroke-width="${width}" stroke-linecap="round" stroke-linejoin="round"/>`;

/* ---- recurring props ------------------------------------------------- */

/** The soft pale-blue ground blob that sits behind most scenes. */
const blueWash = d => fl(d, C.blueBlob);

/** A sprig of leaves, used bottom-left on 04 and 07 and in the corners of 09. */
function sprig(x, y, scale, rot, leafFill, stemStroke) {
  const leaf = (lx, ly, lw, lh, a) =>
    `<ellipse cx="${lx}" cy="${ly}" rx="${lw}" ry="${lh}" fill="${leafFill}" ` +
    `transform="rotate(${a} ${lx} ${ly})"/>`;
  return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${scale})">
    ${ln('M0 0 C 20 -40 44 -78 70 -108', 4, stemStroke)}
    ${leaf(14, -26, 20, 9, 28)}${leaf(-8, -34, 19, 9, -34)}
    ${leaf(32, -58, 19, 9, 20)}${leaf(6, -64, 18, 8, -40)}
    ${leaf(52, -88, 17, 8, 14)}${leaf(28, -94, 16, 7, -46)}
    ${leaf(66, -114, 14, 7, 8)}
  </g>`;
}

/** Coily hair: a scalloped dome swept from the left temple over the crown to
 *  the right, closed with a shallow curve across the brow. `from`/`to` are
 *  angles in degrees measured anticlockwise from the right of the head, so a
 *  crop can be cut lower on one side than the other. */
function coilyHair(cx, cy, rx, ry, {
  fill = C.hair, bumps = 11, bulge = 1.13, from = 196, to = -16, brow = 0.30,
} = {}) {
  const at = (deg, k = 1) => [
    cx + rx * k * Math.cos((deg * Math.PI) / 180),
    cy - ry * k * Math.sin((deg * Math.PI) / 180),
  ];
  const [sx, sy] = at(from);
  let d = `M ${sx.toFixed(1)} ${sy.toFixed(1)}`;
  for (let i = 0; i < bumps; i++) {
    const a1 = from + ((to - from) * (i + 0.5)) / bumps;
    const a2 = from + ((to - from) * (i + 1)) / bumps;
    const [qx, qy] = at(a1, bulge);
    const [px, py] = at(a2);
    d += ` Q ${qx.toFixed(1)} ${qy.toFixed(1)} ${px.toFixed(1)} ${py.toFixed(1)}`;
  }
  d += ` Q ${cx.toFixed(1)} ${(cy + ry * brow).toFixed(1)} ${sx.toFixed(1)} ${sy.toFixed(1)} Z`;
  return sh(d, fill, W.hair);
}

module.exports = {
  C, W, sh, fl, ln, circ, dot, rect, label,
  limb, limbUnder, limbOver, blueWash, sprig, coilyHair, esc,
};
