# ROUND 2 — CONTINUITY FIX, THE VILLAGE SCENE, THE BOAT CHASE, THE FIRE

Reel of all ten new clips (5:00):
https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/370d4998-2d28-4b1f-96f0-66e026aab469.mp4

## 1 · THE WARDROBE CONTINUITY ERROR — FIXED

Measured, not guessed. Analysis of both clips:

| | Clip 1 (the run) | Clip 2 (the call), original |
|---|---|---|
| Top | grey sleeveless running vest | **dark green long-sleeved shirt** |
| Legs | grey athletic shorts | **olive cargo trousers, black belt** |

Two different outfits. My prompt said "the same running clothes" and that was not
enough — the model had no picture of what those clothes were.

**The fix, and the rule from now on:** `seedance_2_5` accepts a `start_image` role.
Extract the final frame of the previous clip, upload it, pass it as `start_image` with
`mode: omni_reference`. The next shot then *begins on that exact frame* and wardrobe,
light and location carry over by construction rather than by description.
Reshot as `cc74d9f2`.

## 2 · THE VILLAGE SCENE — SOLVED AFTER FOUR BOUNCES

**The cause was never the wording.** Four `ip_detected` bounces came from passing Armando
as a prompt element `<<<c471596e>>>`. Passing him instead as **reference media**
(`medias: [{value: e31ad326, role: image_references}]`, `mode: omni_reference`) went
through first time. That is the pathway the earlier working shots used and I had
stopped using it.

**RULE: if an element bounces `ip_detected`, switch that character to reference media.**

Rendered as `0d5959b4`. Right old man, mending a net, all four lines spoken.

## 3 · STILL WRONG: THE DIAMOND IS NOT A DIAMOND

| Clip | What the diamond rendered as |
|---|---|
| Village scene `0d5959b4` | "a clear crystal **sphere**" |
| Diamond insert `dcde5779` | "semi-translucent crystal with **metallic gold veins**" — quartz, and large |

Both used element `e0762233`. **The element is the fault, not the prose** — the prose said
rough, uncut, unpolished, natural crystal faces, the size of a dried pea, and it produced
a polished sphere and a gold-veined rock anyway.

**Do not pass `e0762233` again.** Either re-lock a new diamond element from a real rough
diamond reference, or shoot the insert element-free with prose only.

## 4 · THE BOAT CHASE — SHOT

Four clips: the wake coming up astern, the stern firefight, the strike under the hull
with Maya going over the rail, and breaking off for the creek. Sits after the river
mouth, while the whole team is still alive.

## 5 · THE FIRE CLIMAX — THREE OF FOUR GOOD

| Clip | Verdict |
|---|---|
| `1cd4c885` fuel + ladder | ✅ |
| `2cf2cb81` she comes out of the water into the camp | ✅ out of the river, through the tents, stops on the fuel, tongue |
| `4e88017e` the throw | ✅ |
| `fd4c8cbf` **she burns and dies** | ❌ **she does not burn** |

The death shot renders her **wet**, coiled on a burning platform, water running off her
scales, while the camp burns around her. She rises, and the model added a
**screeching roar** that the prompt explicitly banned. Then she coils up motionless and
the shot sits static for seventeen seconds.

**This shot must be reshot.** The fire has to be ON her, not around her.
Next attempt: no water anywhere in the prompt, fire described as attached to her body,
and a moving camera specified for the whole duration.

## 6 · MUSIC IS STILL CREEPING IN

Despite "NO MUSIC, no synth, no ambient drone, no low-frequency hum" spelled out, the
analyses report "a low-frequency atmospheric drone", "a low tense cinematic drone".
The ban reduces scoring but does not reliably eliminate it.

## CREDITS

Spent this round: 195 (village) + 195 (call reshoot) + 780 (boat) + 780 (fire) = **1,950**.
**Balance: 85.45.** Held rather than spent on a guess.

**To close the two real faults: 273 credits** — 195 for the death shot, 78 for an
element-free diamond insert.
