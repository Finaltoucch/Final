# Exam-period health advisory — replica deck

The nine advisory cards rebuilt from scratch as code, so they render at any
resolution instead of being resampled. `out/3840/` holds the 4K set
(3840 × 3840 each).

The source for this rebuild is `../source/grid.webp`, a 1254 × 1254 raster of
all nine cards. Everything here — layout, palette, type, artwork — was measured
off that image and re-authored; no pixels are carried over.

## What is measured, and what is drawn

**Measured from the source and reproduced exactly:** every word of copy, the
line breaks, the layout geometry, and the palette. Colours were taken by
eroding each shape's mask and reading the median of the interior pixels, so
they are the true fills rather than anti-aliased edges:

| Token | Hex | Role |
| --- | --- | --- |
| cream | `#FDF7EB` | card ground |
| navy | `#11294A` | badge, headings, sign-off ground |
| ink | `#1A1A1A` | body copy |
| skin | `#B4661F` | with `#C8792F` lit and `#8E4E19` shaded |
| hair / outline | `#1B1A17` / `#2B2117` | the warm near-black every shape is drawn with |
| wood | `#A0632A` | `#B5763F` lit, `#7E4A20` dark |
| gold / clay / green | `#F2B23C` / `#C0492E` / `#587353` | accents |

**Type is Lato** — Black for the headings and the badge numeral, Regular for
body copy. The source's single-storey `g` with an open tail, the angled cut on
the `t` ascender and the straight `y` descender identify it unambiguously. It
is subsetted to latin and inlined as base64, so the page needs no network.

**The illustrations are re-drawn, not copied.** The source artwork is generated
raster; these are hand-authored SVG in the same flat-illustration idiom — same
scene, same composition, same props, same fills, drawn with the house outline
weight. They read as the same pictures and they are genuinely resolution
independent, but they are not pixel-facsimiles of the originals, which is not
attainable by hand-authoring paths.

## Three deliberate departures

1. **Square canvases.** The source rows are 445 / 403 / 398 px tall against a
   uniform 414 px width, so the nine cards are three different shapes. That is
   an artefact of how the grid was generated. Everything here is 1:1, which is
   what a carousel wants.
2. **A consistent page indicator.** The source shows 5, 5, 5, 7, 6, 5, 6 and 6
   dots on cards 1–8, and the active dot is not always in the right place. This
   deck carries eight dots throughout, with the active one matching the card.
   The sign-off keeps none, as in the source.
3. **No hairline frame.** Each source tile has a 1 px grey edge where it was cut
   out of the grid. At 4K that would be a 10 px band, so it is dropped.

## Files

```
src/panels.js       copy, per-card type sizes and measures
src/template.html   card layout, design tokens, render logic
src/art/_kit.js     shared palette, stroke weights and drawing helpers
src/art/01..09.js   one scene per card
src/fonts.css       Lato 400/700/900, latin subset, base64
build.js            inlines fonts + scenes + copy -> replica-deck.html
render.js           rasterises each card at any size
out/3840/           the 4K set
out/contact-sheet.png
```

## Build

```sh
npm install                  # from ../ — playwright and @fontsource/lato
node build.js                # -> replica-deck.html (self-contained)
node render.js               # -> out/3840/*.png
SIZE=1080 node render.js     # any other size
node render.js 03 07         # only cards whose slug matches
```

`render.js` keeps the card at its authored 1000 CSS px and raises the device
pixel ratio instead (3.84 for 4K), so the browser rasterises vectors and text
at the output resolution — nothing is ever scaled up from a smaller bitmap.
There is no practical ceiling; `SIZE=7680` works the same way.

Copy lives in the `PANELS` array in `src/panels.js`. Body text is stored as
running prose and wrapped by the browser against a per-card `measure`, set so
it breaks on the same words the source does — so an edit reflows instead of
needing the line breaks rebuilt by hand.
