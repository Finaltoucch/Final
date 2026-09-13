# DIAMOND ANACONDA — CUT TO THE SCREENPLAY

**https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/ed19af6e-1719-4a8b-8112-56a309bf4903.mp4**

**23:32 · 55 clips.** Ordered against `diamond-anaconda-screenplay.fountain` scene by
scene, not against my own running order.

## WHAT WAS ACTUALLY WRONG

The previous cut was not just loosely ordered. It had four structural faults.

### 1 · The 1974 camp was in the wrong act
I had it at 9:45, before Mateo dies. The screenplay puts `EXT. 1974 CAMP` at line 811 —
**after the flooded crossing**, with five people left. I had put it before the crossing
with seven. Moved.

### 2 · Liam died twice
`56728e79` (far bank) and `899e0a7c` (the new death) are the same event, thirty seconds
apart. **`56728e79` dropped.**

### 3 · Maya died twice
`28850dca` (sluice gate) and `605814e1` (the new gate death) are the same event.
**`28850dca` dropped.**

### 4 · Liam's line contradicted the footage
`0914ab84` has Liam saying *"He was right here, he was talking, I turned around"* — a line
written for a script where Mateo is taken **off-screen**. We now SHOW the snatch, with two
men hauling on his arm. The line makes the audience think they missed something.
**`0914ab84` dropped.**

### 5 · The cold open was at the front
Finaltouch: *"forget the cold open, just start from the run."* I had it at 0:00 anyway.
It is now at its real place in the story — `INT. UNDERGROUND TUNNEL - CONTINUOUS`
(line 1581), *"matches the cold open exactly"* — just before he gets out of the tunnel
and runs for the camp. **The film opens on the run.**

## THE ORDER

| At | Scene | Script |
|---|---|---|
| 0:00 | The morning run | *new opening* |
| 0:30 | The call | *new* |
| 1:00 | Fishing settlement — Armando, the diamond | l.138 |
| 1:30 | The valuation | *new* |
| 2:00 | The decision | *new* |
| 2:30 | The plan | *new* |
| 3:00 | Mateo says goodbye | *new* |
| 3:30 | Boatyard day — Mateo + Liam | l.239 |
| 3:45 | Boatyard day — Daniel + Marcus | l.239 |
| 4:00 | Boatyard day — Maya + Ryan | l.239 |
| 4:15 | Boatyard night — "Say it back to me" | l.370 |
| 4:45 | Upriver | *new* |
| 5:15 | River mouth — the engine dies | l.417 |
| 5:30 | **Boat chase — the wake** | *new* |
| 6:00 | **Boat chase — the stern firefight** | *new* |
| 6:30 | **Boat chase — the strike** | *new* |
| 7:00 | **Boat chase — breaking off** | *new* |
| 7:30 | Totem Creek — the shed skins | — |
| 8:00 | Abandoned settlement — "there is charge in it" | l.501 |
| 8:15 | Settlement — "the needle's moving" | l.501 |
| 8:30 | Settlement — "don't go underground" | l.501 |
| 8:45 | Settlement fire — night one | l.562 |
| 9:15 | Mateo goes to the water | l.562 |
| 9:45 | They lose him | l.562 |
| 10:15 | Riverbank — the rifle in the shallows | l.620 |
| 10:30 | Riverbank — the trough, "MATEO!" | l.620 |
| 10:45 | Riverbank — "that boat is thirty feet" | l.620 |
| 11:00 | The argument | *new* |
| 11:30 | Deep jungle — the drone sees her | l.688 |
| 12:00 | Crossing — going in | l.713 |
| 12:15 | Crossing — Kofi stops | l.713 |
| 12:30 | Crossing — the only thing moving | l.713 |
| 12:45 | Crossing — waist deep | l.713 |
| 13:00 | **Liam is taken** | l.713 |
| 13:30 | **The 1974 camp — the bones** | l.811 |
| 14:00 | **The 1974 camp — the torn log** | l.893 |
| 14:30 | The cavern — the walls answer | l.1024 |
| 15:00 | Carving chamber — "she lays them" | l.1066 |
| 15:30 | Daniel runs | l.1108 |
| 16:00 | Daniel stops | l.1108 |
| 16:30 | Side passage — the sock, the diamond | l.1118 |
| 17:00 | Cavern camp — "open your packs" | l.1167 |
| 17:30 | The passages — the hatchlings | l.1254 |
| 18:00 | Kofi holds the corridor | l.1308 |
| 18:30 | The gate takes her | l.1331 |
| 19:00 | Deep chamber — Marcus fires | l.1474 |
| 19:30 | After Marcus | l.1474 |
| 20:00 | **Tunnel — heat POV** *(was the cold open)* | l.1581 |
| 20:15 | **Tunnel — the scream** *(was the cold open)* | l.1581 |
| 20:30 | The fuel and the ladder | *new climax* |
| 21:00 | She comes out of the water into the camp | *new* |
| 21:30 | The throw | *new* |
| 22:00 | She burns | *new* |
| 22:30 | The doorway — "Where is my husband?" | l.1663 |
| 23:00 | The room — the line moves | l.1690 |

## GAP

`EXT. RIVER - MORNING` (l.1637) — Ryan reaching the boat, opening the pack, three
diamonds, his hands shaking — **has no usable clip.** It was one of the recorded cosmetic
faults. The cut currently goes from the fire straight to the doorway. It works, but that
beat is the film's last breath before the consequence and it is missing.

## TIMEBASE

Two clips needed re-encoding to match: `3f1c7d96` (2560x1440) and `8c8a8538`
(time_base 1/12288). **Always `-video_track_timescale 90000`** — the concat demuxer
adopts the first file's timebase and a mismatch silently inflates the whole film.

## STILL OUTSTANDING

1. The diamond renders as a polished sphere — element `e0762233` must not be used again.
2. She does not burn in the death shot.
3. The boat / three diamonds beat has no clip.
