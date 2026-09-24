# EXIT — canonical asset list

**This file is the single source of truth for which job IDs go into the film.**
Anything not on the LIVE list is dead and must never be used as a `start_image`,
an `image_reference`, or included in the delivery ZIP.

Last updated 24 September 2026.

## LIVE — reference sheets

| Ref | Job ID |
|---|---|
| The jumper | `ca7d8430-71b6-4304-9582-d69afa398fa1` |
| Location A — cabin | `7a188194-2a89-45c0-b99c-ef8bc6db29bc` |
| Location B — coastline | `52628d89-0e1c-43d2-a0b3-d6f6899f4c07` |
| The aircraft **(v2)** | `43ced53a-3e12-4717-a04c-77db19da91a9` |

## LIVE — keyframes

| # | Shot | Job ID |
|---|---|---|
| 01 | altimeter **(v2)** | `05ad0b55-38f1-4cbc-a81e-e76c29a54642` |
| 02 | five jumpers on the bench | `0ceb234f-793f-4ce6-885a-9cd8b3aa69fd` |
| 03 | his face, waiting | `9284fc86-a717-4eb8-9b93-1328668382ca` |
| 04 | the door rolls open | `4cf394c1-fc46-47ef-83df-91fb6ab45555` |
| 05 | boots on the sill **(v2)** | `71a87a97-702b-4512-a5f9-911a5e44c1d6` |
| 06 | fingers leaving the frame | `d95dc4d5-9d61-4446-9aa2-d2235b3ac33e` |
| 07 | the exit, aircraft above **(v2)** | `c9c10eca-df92-4775-9982-e0621ec3ec23` |
| 08 | free fall over the bay | `e35d1d12-94b6-47cd-9a43-d0e347ca7d76` |
| 09 | face at terminal velocity | `7afc5ebc-6ac1-47e8-b526-2753c43bebf6` |
| 10 | under canopy | `bed0685b-178f-4805-bef7-53d845a3dd28` |
| 11 | landing on the beach | `6e8e76de-3c70-4b90-bffd-469683b29dfc` |

## DEAD — superseded, never use

| Was | Job ID | Why it was killed |
|---|---|---|
| Aircraft ref v1 | `e37daaab-3abc-4c29-8834-a5935279d736` | "LEFT PANEL" / "RIGHT PANEL" captions burned into the image; two aircraft in one view; airstair door with fold-down steps instead of a roll-up jump door |
| Keyframe 01 v1 | `5722d62e-8915-41fd-a9e3-f54c08b74f65` | Altimeter dial numbered with gibberish (0, 1000, 2000, 4000, 500, 800, 900, 10000, 11,000…), junk "300ft" text, dial oversized to the wrist |
| Keyframe 05 v1 | `0456c8ff-7c96-4329-af52-2d40b306a1e1` | Full-face visor helmet instead of open-face + goggles; altimeter on the wrong wrist plus a second instrument on the right hand; street shoes instead of skydiving boots |
| Keyframe 07 v1 | `7e666f5c-141c-4026-b490-f479092216fc` | Generated an invented aircraft — produced before the aircraft reference sheet existed, so the plane matched nothing |

## Why this file exists

On the previous project (SATURDAY) a superseded keyframe was shipped in v1
because the live/dead tracking existed only in conversation. Before the clip
batch and before the ZIP is packed, every ID gets checked against this file.

## Root-cause note on the four failures

All four were the same mistake: **leaving a surface where unwanted content
could appear and trusting a negative prompt to suppress it.**

- The word "panel" in a prompt invites a printed caption.
- "No numbers except on the dial" invites numbers on the dial.
- Not pinning the helmet type lets it drift to whatever the model prefers.

Negatives do not reliably suppress these. **Remove the surface, or crop past
it.** Same rule that fixed the branded speaker on SATURDAY.

## Surfaces still carrying that risk in the live set

Not yet confirmed clean — need visual check before clips:

- **02** — four extra sets of gear and helmets that could carry markings
- **04** — cabin interiors carry placards and safety notices in reality
- **07, 10, 11** — aircraft fuselage and canopy fabric are prime branding surfaces
- **the character sheet itself** — if the helmet or altimeter is wrong there,
  every frame inherits it and patching frames one at a time is the wrong fix
