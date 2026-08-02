# Animation Direction

Sime Media gave us a *layout* system — palette discipline, metaphor objects,
quiet type, annotation lines. It did not give us an *animation* system, because
it doesn't have one. It's still images with slow push-ins.

We want real motion. This is how to get it without a studio.

---

## The Governing Principle

**Choose a style where generative video's failure modes read as intentional.**

Higgsfield's video models produce a characteristic set of artifacts: slight
temporal jitter between frames, textures that drift and re-form, edges that
breathe, physics that isn't quite right.

In a **photorealistic** shot, every one of those is a defect. The viewer can't
name it, but they feel it, and in a niche whose entire product is credibility
that feeling is expensive. This is the trap most AI channels fall into — they
chase realism, land in the uncanny valley, and look cheap.

In a **stylised, handmade-looking** shot, those exact same artifacts read as
craft. Stop-motion is *supposed* to jitter. Paper is *supposed* to have
irregular edges. A miniature set is *supposed* to have slightly strange scale.

So the rule is: **never generate photoreal.** Pick a style that was already
imperfect before we got there. That's the whole trick, and it's the difference
between "beefy unique animation" and "obviously AI."

---

## Four Directions

### A — Miniature Diorama / Tilt-Shift 🏆

Every concept built as a tiny physical set. A miniature warehouse for logistics.
A tiny bank branch with tiny customers queuing. A doll's-house living room stacked
with unopened parcels. Shot with product lighting and shallow depth of field, the
camera drifting slowly through.

**Why it works with our stack:**
- Image models are exceptionally good at miniature sets — it's a heavily
  represented aesthetic
- "Miniature diorama, tilt-shift, seamless background, studio lighting" is a
  strong enough style anchor to stay consistent across 52 videos
- Shallow depth of field hides artifacts in the blur, for free
- Slow camera drift is the motion type generative video handles most reliably

**Why it fits the content:** the channel is about scale — what things actually
cost, how big a number really is. Making the whole visual language literally
about scale is not decoration, it's argument.

**Risk:** low. This is the safe distinctive choice.

---

### B — Claymation / Stop-Motion 🎯

Everything modelled in plasticine. Chunky clay figures, visible thumbprints, a
slightly wobbly world. Aardman-adjacent.

**Why it works with our stack — and this is the clever part:**

Stop-motion's defining characteristic is **temporal jitter**. It's shot frame by
frame, so things pop and shift between frames. That is *precisely* the artifact
generative video cannot avoid producing.

Every other channel is fighting that artifact. In this style it's the aesthetic.
The weakness becomes the signature.

**Why it fits the content:** the tonal contrast is the hook. Warm, tactile,
almost childlike visuals explaining ruthless corporate economics. Nobody in
finance is doing this. It's disarming, it's memorable, and it makes a video about
airline pricing feel like something you'd send to a friend.

**Risk:** medium. Could undercut authority in a niche that trades on credibility —
though the contrast is also exactly what makes it travel.

---

### C — Paper Craft / Cut-Out Collage

Layered paper with visible fibre texture, hard drop shadows, elements sliding and
folding. Editorial — the aesthetic of a broadsheet's explainer desk.

**Why it works:** paper edges are supposed to be irregular, so artifacts vanish.
Flat layered motion is easy to fake in CapCut too, meaning we can mix generated
shots with hand-built ones and nobody can tell which is which.

**Why it fits:** reads serious, designed, and expensive. Strongest authority
signal of the four.

**Risk:** low, but least distinctive — closest to what design-forward channels
already do.

---

### D — Isometric Systems

Clean isometric 3D. Money as machinery — conveyor belts, pipes, sorting
mechanisms, little cubes moving through a system.

**Why it works:** perfect for "how does this actually work" mechanics, which is
half our calendar.

**Risk:** high, but not technical — it's the generic corporate-explainer look.
Every SaaS landing page uses it. We'd be distinctive in the niche and invisible
everywhere else.

---

### E — Stick Figures 🏆 **RECOMMENDED**

Bold black stick figures on a flat coloured ground. Circle head, straight limbs,
no face. Expressive through posture and motion alone.

**This is the one currently blowing up, and the data is real.** New channels
reporting 3.5M views and 160K subscribers inside three months; one channel at
20M views from 14 videos. Treat the "$4,000 per video" and "$11,000 a month"
figures in those write-ups with the same skepticism we applied to the original
thread — they come from tutorial blogs, which is the genre that inflates. **The
view counts and growth curves are the credible part; the earnings claims are
not.**

**Why it beats every other option for our constraints:**

1. **It has no fidelity to lose.** Every other style fights the uncanny valley.
   A stick figure has no face to render wrong, no hands to mangle, no skin to
   look plastic. The single biggest technical risk of AI video simply doesn't
   apply. This is the cleanest possible answer to "the AI must be invisible."
2. **It stops scrolls.** Bold black shapes on flat colour read at any size,
   including a 168-pixel-wide phone thumbnail. Most business thumbnails are
   cluttered photo composites that turn to mush at that size.
3. **It's a pattern interrupt in this niche.** Nobody in high-RPM finance is
   using it. It's currently concentrated in entertainment and story content.
4. **Consistency is trivial.** "Black stick figure, circle head, no face, flat
   background" is such a tight constraint that the model can barely deviate.
   Fifty-two videos will match.
5. **It's expressive.** Posture alone carries emotion. A slumped stick figure in
   front of a rising red line needs no dialogue.
6. **The documented workflow is our stack.** The tutorials describe image
   generation into Kling image-to-video. We have both, inside Higgsfield.

**Why it fits business explainers specifically:** stick figures are the *native*
language of economic explanation. "Here's you. Here's the bank. Here's where your
money goes." Every economics lecturer on earth already draws this on a
whiteboard. We're not forcing a trend onto the niche — we're using the niche's
oldest visual grammar, executed well.

**Risk:** the style is trending, which means saturation is coming. Our protection
is that we're taking it *into* a different niche than where it's saturating, and
that our moat was always the writing.

---

## Recommendation

**Primary: E — Stick Figures.**

The strategic play is arbitrage: **take the visual style that's proven to stop
scrolls and put it in the niche that's proven to pay.** Stickman is exploding in
entertainment, which pays $3–8 RPM. Business explainers pay $12–22. Nobody is
combining them.

**Backup: A — Miniature Diorama**, if the stick figure tests come back weak.

**Rejected: B — Claymation.** Still the cleverest technical fit (its jitter
problem is stop-motion's aesthetic), but stick figures beat it on thumbnail
legibility, and legibility is what stops a stranger.

**Combine with the Sime Media layout system**, which still holds regardless of
which we pick: locked palette, quiet lowercase type, annotation lines, UI cards
for real numbers. Generated footage for the world, CapCut for every number and
word on screen — because generative video still cannot render text reliably, and
our numbers have to be exactly right.

---

## Test Results — 2026-08-02

Generated two stick-figure test frames on Recraft V4.1 in `vector` mode, palette
pinned to the receipt scheme (`#F2EBE0` ground, `#1A1A1A` + `#7B2233`).

Job IDs: `780d2125-9aca-42c5-87c7-e48a69a3378a`,
`4a5cfa82-af98-4441-bdfa-9063515b6d35`

### The finding that changes the economics

**Recraft `vector` mode returns actual SVG files, not raster images.**

Output was `.svg` at 1344×756. That is a genuine vector asset, and it changes the
production model completely:

- **Infinitely scalable.** One asset serves a 4K master and a thumbnail with no
  quality loss.
- **Directly editable.** Open in any vector editor and recolour, reposition a
  limb, or move an element. We are not stuck with what the model gave us.
- **Animatable without generative video.** Vector shapes can be keyframed in
  CapCut or After Effects with perfectly clean edges. A stick figure's arm can
  be *actually rotated* rather than re-generated and hoped for.
- **Perfect consistency.** The same figure asset is reused across all 52 videos.
  Not "similar" — identical.

This is the difference between animating a character and generating a new one
every shot and praying it matches. It removes the single biggest failure mode of
AI video work, and it means the style holds across a whole library.

### Measured costs

| Item | Credits |
|---|---|
| Recraft V4.1 vector image, 2K | **2.5** |
| Kling 3.0 Turbo video, 5s @ 1080p | **10** |
| Nano Banana image (budget raster) | 1 |

Balance at time of test: **1,113 credits.**

---

## Production Model

Per 10-minute video, three approaches costed against real numbers:

| Approach | Composition | Credits | Videos from 1,113 |
|---|---|---|---|
| All generated video | 15 Kling clips | 150 | ~7 |
| Hybrid | 20 SVGs + 4 Kling clips | 90 | ~12 |
| **Vector-led** ✅ | 25 SVGs, animated in CapCut + 1 Kling hero clip | **~72** | **~15** |

**Go vector-led.** It's the cheapest *and* the best-looking, because keyframed
vector motion is cleaner than generated motion, not a compromise for it. Spend
Kling credits only on the one hero moment per video that genuinely needs
generated motion.

Rules that hold regardless:

- Text, numbers, UI cards, charts, captions: **all CapCut/Canva**, never
  generated — the models still cannot render text reliably and our numbers must
  be exact
- One locked style prompt suffix appended to every generation, saved on video one
  and never edited
- Build a **reusable figure library** — standing, walking, slumped, pointing,
  celebrating, falling. Generate once, reuse across all 52 videos. After roughly
  video 5 the per-video generation cost approaches zero.

That last point is the real unlock. This isn't 52 videos of generation cost. It's
one asset library plus incremental additions.

---

## Next Step

Generate the same subject in three styles — miniature, clay, paper — so the
choice is made on evidence rather than description. Also gives us a measured
credit cost per shot to budget the remaining 51 videos.

- [ ] Approve test generation
- [ ] Pick direction from the results
- [ ] Lock the style prompt suffix
- [ ] Build the palette into the suffix
