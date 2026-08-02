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

## Recommendation

**Primary: A — Miniature Diorama.** Distinctive, technically the most reliable to
generate consistently, keeps authority intact, and the scale metaphor *is* the
channel's thesis.

**Wildcard worth testing: B — Claymation.** Higher ceiling, higher risk. It's the
one that could make the channel genuinely unmistakable, and it's the only
direction that turns the tooling's biggest weakness into an asset.

**Combine with the Sime Media layout system**, which still holds regardless of
which we pick: locked palette, quiet lowercase type, annotation lines, UI cards
for real numbers. Generated footage for the world, CapCut for every number and
word on screen — because generative video still cannot render text reliably, and
our numbers have to be exactly right.

---

## Production Model

Per 10-minute video:

- **12–20 generated hero shots**, 3–8 seconds each
- Reused across the video via reframing, different crops, and speed changes
- Text, numbers, UI cards, charts, captions: **all CapCut/Canva**, never generated
- One locked style prompt suffix appended to every single generation, saved on
  video one and never edited

That last point is the whole consistency mechanism. The style suffix is the
channel's visual identity in one string.

---

## Next Step

Generate the same subject in three styles — miniature, clay, paper — so the
choice is made on evidence rather than description. Also gives us a measured
credit cost per shot to budget the remaining 51 videos.

- [ ] Approve test generation
- [ ] Pick direction from the results
- [ ] Lock the style prompt suffix
- [ ] Build the palette into the suffix
