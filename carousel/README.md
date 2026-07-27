# Exam-period health advisory — carousel

Eight-slide social carousel for the Nnamdi Azikiwe University Medical Center,
Awka, built from the Medical Team's exam-period health advisory.

Two sets are produced from one source: **square 1:1 (1080 × 1080)** and
**portrait 2:3 (1080 × 1620)**.

## Design system

**Concept — "The Health Chart."** Each slide is a leaf from a clinic chart
crossed with an exam answer booklet: a typewritten header strip, a marigold
margin rule down the left carrying the tip number, text on the left, and a flat
2D illustration in a square specimen window on the right.

**Colour**

| Token | Hex | Role |
| --- | --- | --- |
| `--ink` | `#10312B` | deep pine ground, near-black with a green bias |
| `--paper` | `#EDF1E7` | pale sage chart stock |
| `--marigold` | `#E9A13B` | the signal colour — numerals, margin rule, index |
| `--teal` | `#2F8F7E` | clinical mid-green |
| `--clay` | `#C8604A` | warm counterpoint, used sparingly |

**Type** — Zilla Slab 700 for display, Karla 400/700 for body, DM Mono 500
(uppercase, tracked) for the chart labels and slide index. All three are
subsetted to Latin and inlined as base64 `@font-face` data URIs, because the
published page cannot reach a font CDN.

**Numbering** — the source advisory is a genuine ordered list of seven tips, so
`01`–`07` encodes real sequence. The closing slide drops the numeral to signal
the end and carries the sign-off band instead. Ink-ground cover and closer
bookend six paper-ground tips.

**Illustrations** — flat vector, no outlines, seven fills. The same student —
same build, same coily hair, same teal shirt, no facial features — appears in
all eight scenes, standing on a shared ground line. Fills resolve through CSS
custom properties so one drawing reads correctly on both the paper and ink
grounds.

Line length on the square set runs deliberately short (~32 characters); social
carousels are read at a swipe, not at reading distance. The portrait set opens
the measure back up by running body copy full width beneath the illustration.

## Files

```
src/template.html      layout, design tokens, slide copy, render logic
src/illustrations.js   the eight scenes and the shared figure builder
fonts-inline.css       subsetted Zilla Slab / Karla / DM Mono as data URIs
build.js               inlines fonts + illustrations into the page
export.js              renders each slide to a pixel-exact PNG
exam-health-carousel.html   built, self-contained page
png/                   16 exported slides + 2 contact sheets
```

## Build

```sh
npm install playwright
node build.js     # -> exam-health-carousel.html
node export.js    # -> png/square-01..08.png, png/portrait-01..08.png
```

`export.js` toggles an `export` class that drops the preview scaling so each
slide screenshots at its exact pixel size, and reports any slide whose content
overflows the fixed canvas.

Edit copy in the `SLIDES` array in `src/template.html`; both formats regenerate
from it, so the two sets cannot drift apart.
