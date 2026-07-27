/* ------------------------------------------------------------------
   Illustration system — Nnamdi Azikiwe University Medical Center
   Flat 2D vector. No outlines. Fixed 7-fill palette. The same student
   — same build, same coily hair, same teal shirt, no facial features —
   appears in all eight scenes, and every scene shares the same teal
   ground line at y=450 with the figure standing on it.
   Fills resolve through CSS vars so one drawing reads on both the
   paper-ground and the ink-ground slides.
------------------------------------------------------------------ */

const SKIN = '#7B4B2E';
const HAIR = '#37220F';
const TEAL = '#2F8F7E';
const MARI = '#E9A13B';
const CLAY = '#C8604A';
const LIGHT = 'var(--o-light)'; // near-white on paper slides, chart stock on ink slides
const DARK = 'var(--o-dark)';   // ink on paper slides, lifted pine on ink slides

const GROUND_Y = 450;

/* Round skull, short coily hair from one cap plus four coils.
   Deliberately featureless — it keeps eight drawings on-style and
   lets any student see themselves in the figure. */
function head(cx, cy, r) {
  const c = r * 0.31;
  return `
    <circle cx="${cx}" cy="${cy}" r="${r}" fill="${SKIN}"/>
    <path d="M${cx - r} ${cy - r * 0.12} a${r} ${r} 0 0 1 ${r * 2} 0 z" fill="${HAIR}"/>
    <circle cx="${cx - r * 0.74}" cy="${cy - r * 0.46}" r="${c}" fill="${HAIR}"/>
    <circle cx="${cx + r * 0.74}" cy="${cy - r * 0.46}" r="${c}" fill="${HAIR}"/>
    <circle cx="${cx - r * 0.36}" cy="${cy - r * 0.94}" r="${c}" fill="${HAIR}"/>
    <circle cx="${cx + r * 0.36}" cy="${cy - r * 0.94}" r="${c}" fill="${HAIR}"/>`;
}

/* The standing student, built from the ground up so every figure
   lands on the same baseline. `arms` picks the pose. */
function student(cx, arms = 'down') {
  const legH = 54, torsoH = 118, torsoW = 108, r = 46;
  const torsoBottom = GROUND_Y - legH;
  const torsoTop = torsoBottom - torsoH;
  const headCy = torsoTop - 26;

  /* arms hang just clear of the torso edge (half-width 54) so they
     read as arms rather than disappearing behind the shirt */
  const A = {
    down: `
      <rect x="${cx - 80}" y="${torsoTop + 14}" width="26" height="88" rx="13" fill="${SKIN}"/>
      <rect x="${cx + 54}" y="${torsoTop + 14}" width="26" height="88" rx="13" fill="${SKIN}"/>`,
    up: `
      <rect x="${cx - 86}" y="${torsoTop - 70}" width="26" height="104" rx="13" fill="${SKIN}"
            transform="rotate(-28 ${cx - 73} ${torsoTop - 18})"/>
      <rect x="${cx + 60}" y="${torsoTop - 70}" width="26" height="104" rx="13" fill="${SKIN}"
            transform="rotate(28 ${cx + 73} ${torsoTop - 18})"/>`,
    raise: `
      <rect x="${cx - 80}" y="${torsoTop + 14}" width="26" height="88" rx="13" fill="${SKIN}"/>
      <rect x="${cx + 58}" y="${torsoTop - 74}" width="26" height="104" rx="13" fill="${SKIN}"
            transform="rotate(18 ${cx + 71} ${torsoTop - 22})"/>`,
    hold: `
      <rect x="${cx - 82}" y="${torsoTop + 30}" width="26" height="76" rx="13" fill="${SKIN}"
            transform="rotate(-30 ${cx - 69} ${torsoTop + 68})"/>
      <rect x="${cx + 56}" y="${torsoTop + 30}" width="26" height="76" rx="13" fill="${SKIN}"
            transform="rotate(30 ${cx + 69} ${torsoTop + 68})"/>`,
  }[arms];

  return `
    ${A}
    <rect x="${cx - 46}" y="${torsoBottom}" width="30" height="${legH}" rx="14" fill="${DARK}"/>
    <rect x="${cx + 16}" y="${torsoBottom}" width="30" height="${legH}" rx="14" fill="${DARK}"/>
    <rect x="${cx - torsoW / 2}" y="${torsoTop}" width="${torsoW}" height="${torsoH}" rx="42" fill="${TEAL}"/>
    ${head(cx, headCy, r)}`;
}

const GROUND = `<rect x="86" y="${GROUND_Y}" width="388" height="13" rx="6.5" fill="${TEAL}" opacity=".42"/>`;

function scene(inner) {
  return `<svg viewBox="0 0 560 560" role="img" xmlns="http://www.w3.org/2000/svg">
    <circle cx="280" cy="272" r="246" fill="var(--o-halo)"/>
    ${GROUND}
    ${inner}
  </svg>`;
}

/* 01 — Cover: the student reading, clinic cross standing over them */
const coverArt = scene(`
  <rect x="348" y="120" width="118" height="118" rx="32" fill="${MARI}"/>
  <rect x="392" y="148" width="30" height="62" rx="10" fill="${DARK}"/>
  <rect x="375" y="164" width="64" height="30" rx="10" fill="${DARK}"/>
  ${student(210, 'hold')}
  <path d="M210 392 l-92 -24 v-58 l92 24 z" fill="${LIGHT}"/>
  <path d="M210 392 l92 -24 v-58 l-92 24 z" fill="${LIGHT}"/>
  <rect x="205" y="334" width="10" height="58" rx="3" fill="${DARK}" opacity=".18"/>
`);

/* 02 — Realistic targets: the session broken into portions on a planner */
const targetsArt = scene(`
  ${student(148, 'down')}
  <rect x="272" y="196" width="216" height="254" rx="24" fill="${LIGHT}"/>
  <path d="M272 220 a24 24 0 0 1 24 -24 h168 a24 24 0 0 1 24 24 v28 h-216 z" fill="${TEAL}"/>
  <rect x="306" y="178" width="16" height="40" rx="8" fill="${DARK}"/>
  <rect x="438" y="178" width="16" height="40" rx="8" fill="${DARK}"/>
  <rect x="296" y="278" width="52" height="38" rx="10" fill="${MARI}"/>
  <rect x="354" y="278" width="52" height="38" rx="10" fill="${MARI}"/>
  <rect x="412" y="278" width="52" height="38" rx="10" fill="${DARK}" opacity=".13"/>
  <rect x="296" y="326" width="52" height="38" rx="10" fill="${MARI}"/>
  <rect x="354" y="326" width="52" height="38" rx="10" fill="${DARK}" opacity=".13"/>
  <rect x="412" y="326" width="52" height="38" rx="10" fill="${DARK}" opacity=".13"/>
  <rect x="296" y="374" width="52" height="38" rx="10" fill="${DARK}" opacity=".13"/>
  <rect x="354" y="374" width="52" height="38" rx="10" fill="${DARK}" opacity=".13"/>
  <rect x="412" y="374" width="52" height="38" rx="10" fill="${DARK}" opacity=".13"/>
`);

/* 03 — Study breaks: stand up, stretch, let the clock run */
const breaksArt = scene(`
  ${student(160, 'up')}
  <circle cx="374" cy="356" r="94" fill="${LIGHT}"/>
  <circle cx="374" cy="356" r="94" fill="none" stroke="${TEAL}" stroke-width="14"/>
  <rect x="367" y="292" width="14" height="70" rx="7" fill="${DARK}"/>
  <rect x="367" y="349" width="62" height="14" rx="7" fill="${MARI}"/>
  <circle cx="374" cy="356" r="10" fill="${DARK}"/>
`);

/* 04 — Sleep: the night the memory is actually consolidated */
const sleepArt = scene(`
  <path d="M414 128 a62 62 0 1 0 48 78 a49 49 0 0 1 -48 -78 z" fill="${MARI}"/>
  <rect x="292" y="214" width="20" height="20" rx="6" fill="${DARK}" opacity=".34"/>
  <rect x="322" y="168" width="30" height="30" rx="9" fill="${DARK}" opacity=".24"/>
  <rect x="100" y="368" width="360" height="82" rx="26" fill="${LIGHT}"/>
  <rect x="118" y="322" width="132" height="52" rx="22" fill="${LIGHT}"/>
  ${head(184, 330, 44)}
  <path d="M232 368 h202 a26 26 0 0 1 26 26 v30 a26 26 0 0 1 -26 26 h-202 z" fill="${TEAL}"/>
  <rect x="100" y="450" width="360" height="14" rx="7" fill="${DARK}" opacity=".22"/>
`);

/* 05 — Meals and water: a balanced plate, and something to drink */
const mealsArt = scene(`
  ${student(146, 'down')}
  <circle cx="372" cy="350" r="100" fill="${LIGHT}"/>
  <circle cx="372" cy="350" r="80" fill="${DARK}" opacity=".07"/>
  <circle cx="344" cy="320" r="34" fill="${TEAL}"/>
  <circle cx="404" cy="326" r="27" fill="${MARI}"/>
  <rect x="326" y="366" width="94" height="46" rx="23" fill="${CLAY}"/>
  <rect x="240" y="286" width="72" height="164" rx="26" fill="${TEAL}" opacity=".34"/>
  <rect x="240" y="356" width="72" height="94" rx="26" fill="${TEAL}"/>
  <rect x="260" y="252" width="32" height="40" rx="10" fill="${DARK}"/>
`);

/* 06 — Quick fixes: the can and the extra coffee, ruled out */
const quickfixArt = scene(`
  ${student(140, 'down')}
  <rect x="266" y="256" width="94" height="194" rx="26" fill="${MARI}"/>
  <rect x="266" y="326" width="94" height="48" fill="${DARK}" opacity=".2"/>
  <rect x="289" y="232" width="48" height="28" rx="10" fill="${DARK}"/>
  <rect x="378" y="348" width="96" height="102" rx="20" fill="${LIGHT}"/>
  <path d="M474 370 h14 a27 27 0 0 1 0 54 h-14 z" fill="${LIGHT}"/>
  <rect x="378" y="348" width="96" height="27" rx="13" fill="${CLAY}"/>
  <circle cx="424" cy="238" r="54" fill="${CLAY}"/>
  <rect x="392" y="228" width="64" height="20" rx="10" fill="${LIGHT}"
        transform="rotate(-45 424 238)"/>
`);

/* 07 — Seek care early: the Medical Center, and the walk to its door */
const clinicArt = scene(`
  ${student(140, 'down')}
  <rect x="248" y="188" width="234" height="262" rx="22" fill="${LIGHT}"/>
  <path d="M248 210 a22 22 0 0 1 22 -22 h190 a22 22 0 0 1 22 22 v40 h-234 z" fill="${TEAL}"/>
  <rect x="352" y="278" width="26" height="76" rx="9" fill="${CLAY}"/>
  <rect x="327" y="303" width="76" height="26" rx="9" fill="${CLAY}"/>
  <path d="M334 450 v-56 a31 31 0 0 1 62 0 v56 z" fill="${DARK}" opacity=".82"/>
  <rect x="272" y="384" width="46" height="46" rx="11" fill="${MARI}"/>
  <rect x="412" y="384" width="46" height="46" rx="11" fill="${MARI}"/>
`);

/* 08 — Existing conditions: medication stocked, examiner told in time */
const conditionArt = scene(`
  ${student(140, 'raise')}
  <rect x="266" y="200" width="216" height="140" rx="22" fill="${LIGHT}"/>
  <rect x="266" y="200" width="216" height="32" rx="16" fill="${TEAL}"/>
  <circle cx="308" cy="272" r="21" fill="${MARI}"/>
  <circle cx="362" cy="272" r="21" fill="${MARI}"/>
  <circle cx="416" cy="272" r="21" fill="${MARI}"/>
  <circle cx="308" cy="316" r="21" fill="${DARK}" opacity=".15"/>
  <circle cx="362" cy="316" r="21" fill="${MARI}"/>
  <circle cx="416" cy="316" r="21" fill="${DARK}" opacity=".15"/>
  <rect x="300" y="392" width="128" height="58" rx="18" fill="${CLAY}"/>
  <rect x="322" y="366" width="40" height="30" rx="10" fill="${DARK}"/>
`);

const ART = {
  cover: coverArt,
  targets: targetsArt,
  breaks: breaksArt,
  sleep: sleepArt,
  meals: mealsArt,
  quickfix: quickfixArt,
  clinic: clinicArt,
  condition: conditionArt,
};
