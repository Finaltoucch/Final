# RAID — ALEXATOR, "Never Let Go" (release 019)

Project 13. Delivered 28 September 2026.

## Concept

A three-man tactical team fast-ropes into a forest clearing at dusk, stacks on a
cabin, breaches it, and brings a hostage out alive. Eleven shots. The film is built
so that the single loudest musical event in the section — the kick returning after a
bar of near-silence — is the moment the door comes off its latch.

This is the first film in the engagement built on an action structure rather than
the one-protagonist-performing-an-activity form that the previous twelve shared and
that the client rejected three times running.

## Form

| | |
|---|---|
| Shots | 11 |
| Length | 45.375 s (26 bars) |
| Cut rhythm | 7 shots x 2 bars (approach), 4 shots x 3 bars (after the drop) |
| Turn | Shot 08, the breach, lands exactly on the drop at 131.652 s of the track |

The seven approach shots run two bars each over the track's driving section. Shot 07
— a macro of a gloved hand closing on the door handle — sits on the bar where the
kick drops out entirely. Shot 08 lands on the returning kick. The four shots after
the drop run three bars each and open the film out.

## Continuity architecture

Three reference sheets were generated before any keyframe:

1. **Operator turnaround** — four views (front, three-quarter, side profile, back) at
   identical pose and scale. A single front-on view is not a character lock: it leaves
   the back, the sides and every undescribed attribute undefined, and each keyframe
   then invents its own answer. Identity is locked by **costume, not face** — balaclava,
   eye protection and helmet cover the face completely in all four views, so there is
   no face available to drift. Three operators appear together in several shots and
   none of them drifted.
2. **Helicopter** — matte black, entirely unmarked. No roundels, registration,
   insignia or readable text anywhere.
3. **Cabin** — generated empty of people, so the interior geometry stays fixed across
   shots 08, 09 and 10.

## Prompt discipline applied

Three rules, all earned from specific failures on earlier projects:

- **One motion instruction per shot, stated once.** Two motion verbs in one prompt is
  how RIDE THE STORM shot 11 ended up with the bike travelling backwards.
- **Describe the surface you want rather than negating what you don't.** "Opaque mirror
  visor", not "NO face".
- **Pin the camera and pin the positions.** The action then has only one way to read.

Shots 08 and 09 are the direct product of the third rule — see the fault table in
`02_ASSETS_AND_VERIFICATION.md`.

A fourth rule came out of the client's review of the first assembly:

- **Name a formation and you get a formation.** "Shoulder to shoulder", "single file",
  "press tight" are group nouns, and the model renders the group, tidily and
  symmetrically. Three people written as three separate bodies with three separate
  postures is what reads as real. Shots 02 and 06 both failed this way and both were
  rebuilt.

And a fifth, from the same review:

- **A fragment with nothing attached to it reads as unreal.** Shot 05 was a macro of
  boots with the body cropped out; shot 10 was a bullet in open air with no cause in
  frame. Both were rebuilt to include what the fragment belonged to — the whole man
  landing, and the finger that pulls the trigger.

## Deliverables

- `01_FINAL_ALEXATOR_NEVER_LET_GO.mp4` — 1080 x 1920, 24 fps, 45.375 s, AAC stereo 48 kHz
- `02_USED_AI_SOURCES.zip` — 3 reference sheets, 11 keyframes, 11 untrimmed source clips, full prompt and job-ID record
- `03_ORIGIN_PROOF.pdf` — 8 pages, delivered inside `03_ORIGIN_PROOF.zip`

## Spend

| Item | Credits |
|---|---|
| 3 reference sheets (nano_banana_pro 2K) | 6.00 |
| 11 keyframes (nano_banana_pro 2K) | 22.00 |
| 2 keyframe corrections, round 1 (shots 08, 09) | 4.00 |
| 7 clips x 5 s (kling3_0 pro, sound off) | 52.50 |
| 4 clips x 6 s (kling3_0 pro, sound off) | 36.00 |
| 4 keyframe corrections, round 2 (shots 02, 05, 06, 10) | 8.00 |
| 3 clips x 5 s + 1 clip x 6 s, round 2 | 31.50 |
| **Total** | **160.00** |

Round 1 video stage quoted at 88.50 and charged exactly 88.50 (266.08 -> 177.58).
Round 2 quoted at 39.50 and charged exactly 39.50 (177.58 -> 138.08).

## Revision history

| Round | Shots rebuilt | Found by |
|---|---|---|
| 1 | 08, 09 (keyframes only, before any clip was rendered) | Client review of pasted keyframes |
| 2 | 02, 05, 06, 10 (keyframe and clip) | Client review of the first assembled film |

The contact sheets originally embedded in the origin proof were removed at the
client's instruction; they had not been asked for. The proof is text and tables only.
