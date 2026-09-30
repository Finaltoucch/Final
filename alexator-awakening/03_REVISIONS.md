# Awakening — revision rounds, and what each one taught

Every rule at the bottom of this file was paid for. None of it is theory.

---

## Round 1 — the extra arm

Client pasted the shot 05 frame: three shoulder-strap structures, a third bare
arm crossing to her face attached to no plausible body, fused fingers, and she
was standing in the middle of the road.

Cause: the prompt said *"lifts one hand to smooth a loose strand of hair back
from her cheek"* in a **waist-cropped** frame, with a clutch already in the other
arm. A raised hand near the face in a waist-cropped shot is a limb generator —
the model invents the shoulder that has to connect it, and the clutch had already
consumed the one arm it could see.

Fix: both hands down at her sides, hands below the waist, nothing crossing the
body. Pinned to the pavement, not the road.

---

## Round 2 — "why is an empty car moving without the man inside"

The car reference sheet carried `NO people, NO driver` — entirely correct for a
product sheet, which should show the car and nothing else. Shots 01 and 03 then
never put him back in, so the sheet's negative became a property of the car.

**A sheet-level exclusion is not a property of the thing.**

---

## Round 2 — the stopping car

Shot 11 sat still for a beat, then drove off. The prompt said where the car goes
but never said it was **already at speed in frame one**, so the model eased into
motion out of the still keyframe, which is the physically obvious reading of a
static first frame.

---

## Round 3 — "why is the steering in the left in some and on the right in some"

The car sheet specified paint, chrome, wheels, leather and the wood rim, and
**never said which side the steering wheel was on**. Six shots each decided
independently, so the car changed hands mid-film.

Shot 08 made it worse by writing the driver's position *against the lens* —
*"the NEAR seat closest to the camera"* — which cannot hold still across a shot
where the camera moves.

Fix: sheet rebuilt as explicitly left-hand drive, stated four ways plus a
dedicated cockpit view; all six affected shots rebuilt on the new sheet.

---

## Round 4 — "the girl appears suddenly"

Client: *"instead of the camera smoothly shifting and revealing her already
standing there"*.

Measured evidence: frame 259, the 03→04 cut, was the **only** cut in the film
that fell below the 0.30 scene-detection threshold, because shots 03 and 04
shared framing, palette and content. In the previous origin proof I had written
that off as a harmless detector quirk. It was not a quirk — it was the detector
telling me the cut did not read as a cut, which is exactly what the client saw.

Fix: shot 04 rebuilt as a camera reveal — a plane tree trunk fills the
foreground and the camera glides sideways to uncover her, **stationary
throughout**. After the fix all ten cuts detect, each on its planned frame.

---

## The seven prompt rules

Earned across this project and the raid.

1. **Undefined is not neutral.** It is a fresh decision the model makes every
   single time it renders.
2. **A specification must travel with every prompt that shows the subject, and a
   sheet-level exclusion is not a property of the thing.** `NO driver` was right
   for the car sheet and wrong for the shot.
3. **State position and direction against the world, never against the lens.**
   "Toward the lens", "the near seat closest to the camera" — these cannot hold
   still.
4. **Naming a formation gets you a formation.** "Shoulder to shoulder", "single
   file", "press tight" all render as drill.
5. **A fragment with nothing attached reads as unreal.** Boots with no body. A
   bullet with no shooter.
6. **A raised hand near the face in a waist-cropped frame is a limb generator.**
   The model invents the shoulder that connects it.
7. **A cut has to look like a cut.** Two shots sharing framing, palette and
   content read as one shot with something appearing in it.

## And one process rule

**Do not file a measurement you cannot explain as a quirk.** The frame-259
anomaly was visible and dismissed one round before the client caught it.
