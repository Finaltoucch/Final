# Cherry Servers × Solana — Edit Spec (client corrections pass)

Source: `Cherry_Servers_Corrected_Final_copy_1.mp4`
1920×1080 · 30 fps · 32.97 s · H.264 + AAC 44.1 kHz stereo

This document records what the correction pass changes, where, and why — and what is
still blocked on assets only the client can supply.

---

## Governing constraint: the audio is not re-cut

Every change below is made **inside the existing 32.97 s duration**, as an overlay or a
patch on the picture. Nothing is trimmed, inserted, or slipped on the timeline.

That is deliberate. The voice-over and music are already mixed and timed; removing the
1 s `aramco` shot or appending an end card would push everything after it out of sync
with the VO and force a re-mix. Covering picture instead keeps the audio bit-identical
to the approved mix and keeps the VO landing exactly where it lands today.

---

## Shot map (measured, not estimated)

Scene-detect and black-detect on the source give:

| Region | TC | Note |
|--------|----|------|
| Racing body | 0.00 – 29.37 | ~30 cuts, fastest run 25.3–29.4 |
| `aramco` pit-straight shot | **16.30 – 17.33** | isolated 1.03 s shot |
| PIRELLI tyre shot | **7.13 – 8.53** | logo stable at x 860–1045, y 315–435 |
| Original end card | **29.37 – 32.93** | black + logo + wordmark, 3.57 s |

---

## 1. Opening three seconds

**Client:** *"the first three seconds should include the Cherry Servers logo and a direct
line such as 'Bare metal for Solana validators'. Captions should begin immediately."*

- **Brand lockup** — logo mark + `cherry servers` wordmark, top-left, fades up at 0.30 s
  and holds until 28.90 s. It persists through the whole film rather than flashing once:
  the client's stated risk is the asset reading as motorsport sponsorship, and a constant
  corner lockup is what makes it read as *Cherry's own ad* in a feed scroll.
- **Headline** — `BARE METAL FOR` (red, tracked) over `SOLANA VALIDATORS` (white, large),
  centred, 0.35 → 3.25 s with 0.35 s fades, on a soft top-and-bottom gradient scrim so it
  survives the busy racing plate.
- **Captions** — first cue starts at **0.15 s**.

The racing opening is kept intact underneath, as requested.

## 2. Mid-video portal insert

**Client:** *"a real, legible three-to-four-second recording of the Cherry portal showing
server configuration or deployment, timed to the infrastructure part of the voice-over."*

Slotted at **16.30 – 19.80 s (3.5 s)**.

That start point is chosen because it is a hard cut *and* it is the first frame of the
`aramco` shot — so the insert does double duty: it delivers the product proof and it
buries the single worst piece of third-party branding in the film.

**Blocked:** this needs a real screen recording. The cut currently carries a marked
holding slate (`PORTAL CAPTURE · 3.5 s · REPLACE WITH REAL SCREEN RECORDING`) so the
timing is reviewable now. A fabricated or mocked-up portal UI would be the one
credibility error this audience punishes, so none was generated.

**Capture spec:** 1920×1080 or larger, 30 fps, no cursor trails, no browser chrome or
personal account details, UI at ≥125 % zoom so the config fields survive the 9:16 crop.
Show configuration → deploy. Slow, deliberate pointer movement reads better than fast.

## 3. End frame

**Client:** *"'Solana servers by Cherry Servers' with a clear 'Explore Solana servers' action."*

The original end card (29.37 – 32.93) is replaced in place, same duration:

- logo mark + `cherry servers` wordmark
- headline **Solana servers by Cherry Servers**
- red CTA pill **Explore Solana servers**
- `cherryservers.com`

## 4. Third-party branding removal

| Mark | Where | Treatment |
|------|-------|-----------|
| **PIRELLI** | tyre sidewall, 7.08 – 8.58 | feathered patch: blur σ22 + desaturate to 0.20 + slight darken, so the red wordmark resolves to rubber tone while the sidewall stripe survives |
| **aramco** | trackside barrier, 16.26 – 17.38 | feathered patch, blur σ38 + desaturate — and covered outright by the portal insert |

Both use soft-edged alpha masks rather than hard boxes, so there is no visible rectangle.
The patches are applied to the master *before* reframing, so all three ratios inherit them.

**Note:** the car's own Cherry Servers livery, the red sidewall arc, and the trackside
`CHERRY SERVERS` boards are all kept — those are Cherry's own branding.

## 5. Three native ratios

| Ratio | Output | Reframe |
|-------|--------|---------|
| 16:9 | 1920×1080 | native |
| 9:16 | 1080×1920 | centre crop 608 px wide, Lanczos up |
| 1:1 | 1080×1080 | centre crop 1080 px wide |

Type is re-laid out per ratio — not scaled from the 16:9 comp. The 9:16 headline breaks to
two lines and its caption baseline sits 300 px up from the bottom to clear platform UI chrome.

---

## Blocked on client

1. **Portal screen recording** (§2) — the only genuinely missing asset.
2. **Voice-over script text** — captions must be typeset from the script, not guessed.
   Speech-model transcription is unavailable in this environment (model hosts are blocked
   by network policy), and for an ad the caption track should come from the approved script
   anyway so that *Solana*, *Cherry Servers* and any figures are spelled correctly.
   Drop the lines into `captions.srt` and the three caption tracks regenerate.
3. **Confirmation of the infrastructure VO beat.** The insert is parked at 16.30 s because
   that is a clean cut. If the infrastructure line actually lands elsewhere, move
   `PORT_IN` and the insert follows.
