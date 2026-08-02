# Production Spec — Vintage Newspaper Style

**Locked 2026-08-02.** This is the channel's visual style. It replaces the stick
figure direction in `style-lock.md` and `animation-direction.md`, both of which
are superseded.

---

## Why This Style

Four earlier directions failed. This one works for reasons worth recording so we
don't drift back:

1. **Texture hides the artifacts.** Halftone dots, paper fibre, ink bleed and
   foxing are noise by design. Generative models produce noise as a defect —
   here it lands as authenticity. Flat vector had nowhere to hide; aged newsprint
   is all hiding place.
2. **Kling handles it.** Cinematic video models add depth, grain, raking light
   and dust. On flat vector that destroyed the art. On a photographed antique
   print it *is* the art.
3. **One still is already a shot.** An engraved front page is worth looking at
   without any footage behind it. This was the fatal flaw of the chart-card
   approach — nothing to look at between the numbers.
4. **It earns the history angle.** "There was a year, and there was a meeting"
   plays completely differently over a period newspaper than over a chart.

---

## Image Generation — Locked Parameters

| Parameter | Value |
|---|---|
| Model | `nano_banana_pro` |
| `aspect_ratio` | `16:9` |
| `resolution` | `2k` |
| Cost | **2 credits** per image |

### The style suffix

Append to every image prompt, after the subject description:

```
Fine crosshatched engraving, dense stippling, coarse halftone dot texture,
ink bleed into paper fibre, foxing spots, slight misregistration of one muted
oxblood plate. Sepia, bone white, deep black. Flat archival photograph, even
museum light, extremely detailed.
```

### The subject formula

Every frame is **an aged newspaper page carrying a Victorian steel engraving of
a modern thing.** The comedy and the argument both come from that collision — a
printer drawn with the reverence of an 1890s scientific plate.

Always include:
- `Aged [decade] newspaper page on yellowed newsprint`
- A **bold letterpress headline in caps** — this is the on-screen text, and the
  model renders it reliably at this size
- `Heavy ornamental border` or `thin column rules and small body type`

---

## Video Generation — Locked Parameters

| Parameter | Value |
|---|---|
| Model | `kling3_0` |
| `duration` | `10` |
| `mode` | `std` |
| `sound` | `off` |
| `medias` | `start_image` = the still's job ID |
| Cost | **15 credits** per clip |

### The motion suffix

Append to every video prompt:

```
Archival footage of a real antique print, nothing new appears, the engraving
stays exactly as drawn, no morphing, no distortion.
```

That clause is load-bearing. Without it Kling invents detail and the page starts
mutating.

### Motion vocabulary — vary across shots

| Move | Use |
|---|---|
| Slow push in, dust in raking light | Establishing, opening shot |
| Lateral drift with parallax | Comparisons, "this versus that" |
| Hard fast push | The turn, the punchline |
| Track sideways along a row | Lists, multiple items |
| Dramatic push with shadow closing in | The close |

Never repeat the same move twice in a row.

---

## Cost Per Video

| Item | Unit | 60s video | 10-min video |
|---|---|---|---|
| Stills | 2 cr | 6 = 12 | ~40 = 80 |
| Clips | 15 cr | 6 = 90 | ~40 = 600 |
| Voiceover | 0.1 cr | 0.1 | ~0.5 |
| **Total** | | **~102** | **~680** |

**This is expensive.** A 10-minute video at ~680 credits means roughly one and a
half full videos on a 1,113 credit balance.

Options if the cost bites:
- Hold shots longer — 6s of screen time per 10s clip, cut for pace
- Reuse clips across videos where the subject is generic (a printing press, a
  balance scale, a shelf of bottles work in many episodes)
- Build a **stock library** of ~40 generic engraved newspaper clips once, reuse
  across the whole calendar. This is the single biggest saving available.
- Use stills with a CapCut push for filler shots, spend Kling only on hero moments

---

## Video 1 — Assets Built

**Why Printer Ink Costs More Than Champagne** · 60s · 6 shots

| # | Still | Clip | Motion | Narration beat |
|---|---|---|---|---|
| 1 | `80d6edf9` | `e9f7099d` | Slow push, dust | "A litre of printer ink costs more than Dom Pérignon…" |
| 2 | `fb631a38` | `ce3de924` | Lateral drift | "Not slightly more. Up to twelve times more." |
| 3 | `71655e20` | `52000db7` | Push to coins | "Seventy-nine dollars… some models they lose money." |
| 4 | `dcf161cc` | `3e094bce` | Hard push to blades | "Sell the handle at cost, the blades forever." |
| 5 | `fab06504` | `b21d196c` | Track along shelf | "HP. Canon. Epson." |
| 6 | `07c3d03f` | `142cf3e7` | Push, shadow closing | "Thirteen to ninety-five an ounce. Twice Dom Pérignon." |

**Voiceover:** `2e821e55` · voice `Finaltouch-` (`f20af7a3-2416-4cb8-b394-688e71bcc43d`)

### Headlines used

Each still carries its own on-screen text — no CapCut titling needed:

- `INK NOW DEARER THAN CHAMPAGNE`
- `THE SEVENTY-NINE DOLLAR TRAP`
- `THE HANDLE AT COST / THE BLADES FOREVER`
- `HOUSES OF THE TRADE`
- `WEIGHTS AND MEASURES`

This is a real advantage over every earlier direction: **the text is part of the
artwork**, in period type, rather than a modern overlay fighting the image.

---

## Assembly

Done in CapCut, by hand. **The sandbox running Claude cannot download generated
files** — the egress gateway returns 403 for Higgsfield's CDN, so clips and audio
can be created from here but not retrieved, concatenated or muxed.

Steps:
1. Download the six clips and the VO from Higgsfield
2. Lay clips 1–6 in order, ten seconds each
3. VO on the track beneath — paced to the same beats
4. Auto-captions on
5. Tick the altered-content disclosure at upload

To have Claude assemble instead, the files must be **attached in chat** — uploads
land on local disk and are readable.

---

## The Script — 60 seconds

> A litre of printer ink costs more than a litre of Dom Pérignon. Not slightly
> more. Up to twelve times more. And about half of what you buy will never touch
> paper.
>
> Here's how it gets you. You need a printer. You find one for seventy-nine
> dollars. That feels like a deal. It is a deal. The manufacturer is barely
> making anything on it. Some models, they lose money. That's not a mistake.
> That's the plan.
>
> It's the razor and blades model. Sell the handle at cost, make your money
> forever on the blades. HP. Canon. Epson. The hardware is the hook. The
> cartridge is the business.
>
> Consumer Reports measured it. Brand-name ink runs from thirteen dollars an
> ounce, to ninety-five. The cheapest ink you can buy costs more than twice as
> much as Dom Pérignon. Ounce for ounce.

### Sources

- Per-ounce range and the waste finding — [Consumer Reports](https://www.consumerreports.org/printers/the-high-cost-of-wasted-printer-ink)
- Pricing structure — [razor and blades model](https://en.wikipedia.org/wiki/Razor_and_blades_model)

---

## Superseded

`style-lock.md` and `animation-direction.md` describe the stick figure direction,
which was rejected. Kept for the reasoning about why generative video destroys
flat vector art — that lesson is what led here — but **do not use their
parameters.**
