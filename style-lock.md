# Style Lock — Channel Visual Identity

**Locked 2026-08-02.** Confirmed against reference generation
`780d2125-9aca-42c5-87c7-e48a69a3378a`.

This file is the channel's visual identity. **Do not edit it after video 1
ships.** Consistency across 52 videos is worth more than any individual
improvement, and the moment this drifts the library stops looking like one show.

---

## Generation Parameters — Never Change These

| Parameter | Value |
|---|---|
| Model | `recraft_v4_1` |
| `model_type` | `vector` ← **outputs SVG, not raster. This is the point.** |
| `colors` | `["#1A1A1A", "#7B2233"]` |
| `background_color` | `#F2EBE0` |
| `resolution` | `2k` |
| `aspect_ratio` | `1:1` for library figures · `16:9` for full scenes |

**Cost:** 2.5 credits per image.

---

## The Palette

| Role | Hex | Use |
|---|---|---|
| Ground | `#F2EBE0` | Every background. Warm receipt paper. |
| Line | `#1A1A1A` | All figures, all linework, all type. |
| Signal | `#7B2233` | Oxblood. **One element per frame, never two.** |

The signal colour is the whole attention system. If everything is red, nothing
is. One red object per frame tells the viewer exactly where to look.

---

## The Style Suffix

Append this to **every** generation prompt, verbatim. It follows the subject
description.

```
Simple bold black line work, perfect circle head with no facial features,
straight clean limbs, thick confident uniform strokes. Flat cream paper
background, no gradient, no shading, no texture. Centered, generous negative
space, minimal editorial infographic style.
```

**Why each clause is load-bearing:**

- `perfect circle head with no facial features` — no face means nothing to render
  wrong. This is the clause that kills the uncanny valley.
- `thick confident uniform strokes` — prevents stroke weight drifting between
  generations, which is the fastest way to break consistency.
- `no gradient, no shading, no texture` — keeps output flat, which keeps SVG
  clean and editable.
- `generous negative space` — leaves room for the CapCut text layer without
  recomposing.

---

## Figure Library

Generate once. Reuse across all 52 videos. **After roughly video 5 the marginal
generation cost approaches zero** — this is the core economic argument for the
whole approach.

### Batch 1 — core poses (generated 2026-08-02, 15 credits)

| Pose | Use | Job ID |
|---|---|---|
| Standing neutral | Default anchor, establishing shots | `1335e6ff-f671-46b8-ba45-40fd23ebedb0` |
| Pointing right | Explaining, directing attention | `40afb908-72ea-4f98-a85b-1599a3cf7634` |
| Slumped / defeated | Loss, bad news, the problem | `a8be61de-77f5-45ea-8a27-79197cb54fd1` |
| Arms raised / celebrating | Win, payoff, resolution | `7061b385-5578-46bb-b5d1-2db547ff9eed` |
| Pushing red cube | Effort, burden, debt | `c583bd61-c751-4661-aeaf-a895f8a929bb` |
| Running | Chasing, fleeing, urgency | `2bccdf0c-47e9-40e0-a385-8cdb9060d2a5` |

### Batch 2 — to generate next

- Sitting at a desk
- Handing an object to another figure (transaction)
- Crowd / queue of figures (market, consumers)
- Climbing a staircase (progress, tiers)
- Holding an oversized object (scale metaphor)
- Falling (collapse)

### Reference scene

`780d2125-...` — figure vs. giant champagne bottle, scale comparison, 16:9.
This is the composition template for hero shots.

---

## Why SVG Changes the Workflow

Recraft's `vector` mode returns real `.svg` files. Consequences:

1. **Animate, don't regenerate.** A limb can be rotated on a keyframe in CapCut
   or After Effects. We are not generating a new figure per shot and hoping it
   matches — we are moving the same figure.
2. **One asset, every resolution.** 4K master and a phone thumbnail from the
   same file, no quality loss.
3. **Editable.** Recolour, reposition, delete the background, fix a limb. We are
   not stuck with the model's output.
4. **Identical, not similar.** The figure in video 52 is the same file as the
   figure in video 1.

This is what makes a genuine channel identity possible rather than a series of
loosely related generations.

---

## Division of Labour — Absolute Rule

| Element | Where it's made |
|---|---|
| Figures, objects, scenes | **Higgsfield** (Recraft vector) |
| Motion, transitions, timing | **CapCut** (keyframed vectors) |
| **All text, all numbers, all charts, all captions** | **CapCut / Canva — NEVER generated** |
| Hero motion shot (max 1 per video) | Higgsfield (Kling, 10 credits) |
| Voice | Higgsfield cloned voice, locked settings |

**The text rule is not negotiable.** Generative models still render text
unreliably, and this channel's entire product is numbers being exactly right. A
single mangled figure on screen costs more credibility than the animation earns.

---

## Production Budget

| Approach | Per video | Videos from ~1,093 credits |
|---|---|---|
| **Vector-led** ✅ | ~72 credits | ~15 |

And falling, as the figure library fills out.
