# DIAMOND ANACONDA — 60-SECOND TRAILER

**https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/bad0571d-91ef-4a01-8f7f-495b9175d60b.mp4**

**60.0 seconds · 19 shots · cut from the finished film. Zero credits — editing only.**

No title cards, no tagline, no type of any kind, per the standing instruction.

## THE CUT

Shots get shorter as it runs — 6s at the open, 2s by the deaths. That acceleration
is the whole trick: the audience feels the film speeding up without being told.

| At | Len | Shot | Source |
|---|---|---|---|
| 0:00 | 6.0 | Armando by the fire — *"And that is the smallest one."* | `0d5959b4` |
| 0:06 | 5.0 | The dealer's back room — the number | `2e59db9a` |
| 0:11 | 4.0 | The chart — *"Nobody has lived there since nineteen seventy-four"* | `f3f60ec0` |
| 0:15 | 3.5 | Upriver at dawn, the island coming out of the haze | `3336ce1b` |
| 0:18 | 4.0 | The wake astern — *"That is not the current."* | `50408f67` |
| 0:22 | 3.5 | The stern firefight | `2d7e2003` |
| 0:26 | 3.0 | The strike under the hull, Maya over the rail | `b336e3af` |
| 0:29 | 3.0 | Mateo taken | `2eab3b2e` |
| 0:32 | 2.5 | The riverbank — *"MATEO!"* | `f94fec33` |
| 0:34 | 3.0 | The argument | `0240ab06` |
| 0:37 | 3.0 | The drone screen | `07f6af63` |
| 0:40 | 2.5 | The crossing, waist deep | `e5eb0cd5` |
| 0:43 | 2.0 | Liam taken | `899e0a7c` |
| 0:45 | 2.0 | Daniel running | `a7830ffd` |
| 0:47 | 2.0 | The passages, muzzle flash | `59e492a7` |
| 0:49 | 2.0 | The gate takes her | `605814e1` |
| 0:51 | 3.0 | She comes out of the river into the camp | `2cf2cb81` |
| 0:54 | 3.0 | The throw, the ground goes up | `4e88017e` |
| 0:57 | 3.0 | She burns | `fd4c8cbf` |

## WHY THIS SHAPE

- **Opens on the quietest thing in the film.** An old man, a fire, one line. It sells the
  premise without a single explosion, which is what buys the next fifty seconds.
- **The number at 0:06** tells the audience what six people are about to die for. Without
  it the rest is just jungle.
- **Three lines of dialogue total**, all in the first fifteen seconds. After that it is
  picture and sound only.
- **The creature is held back until 0:51.** She appears twice, at the very end, both times
  already on fire or about to be. Nothing in the first fifty seconds shows her.
- **Ends on the burn, not on a card.** No title, no date, no logo.

## TECHNIQUE

Each shot carries its own original audio with a 0.10s fade in and 0.12s fade out, so the
hard cuts do not click. Every segment re-encoded to 1280x720 / 24fps / aac 32000 /
timescale 90000, then concat-copied.

**Two bugs worth remembering:**
1. `ffmpeg` without `-nostdin` **eats the loop's input file**. A `while read ... done < spec`
   loop dies after the first iteration with *"Invalid duration specification for ss"*.
   Always pass `-nostdin`, or drive the loop from an array.
2. The sandbox is discarded seconds after a call returns. Chain download, cut, concat and
   the upload PUT into ONE command, with the presigned URL fetched beforehand.
