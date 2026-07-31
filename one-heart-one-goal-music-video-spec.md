# "One Heart, One Goal" — 30s Music Video / Lipsync Spec

Production sheet for the Higgsfield build. Everything here is locked and ready to
execute; only the generation calls remain.

## Locked inputs

| Item | Value |
| --- | --- |
| Audio media_id | `4a9bcda8-f81a-4c0e-b8ac-900086185a7d` |
| Audio filename | `One_Heart_One_Goal_30s_context_for_finalist_pilots (1).mp3` |
| Duration | 30s |
| Performer | `@Aurelia-Vega` — element `b2ed2007-0767-4931-b912-99e37c2beee4` |
| Fallback element | `@aurelia` — `50a2a681-afea-4996-bb1d-da121ab2ea92` |
| Video model | Seedance 2.0 (image-to-video, native audio-driven lipsync) |
| Resolution | **720p** |
| Aspect | 16:9 |

## Performance direction (applies to every shot)

She must show **facial passion** — this is the primary note, not a garnish. In each
shot the face carries the song:

- Eyes open and locked to lens on every hook line; no neutral or "pretty-blank" gaze.
- Brows engaged — lifting on the rises, drawing in on the low lines.
- Full jaw movement on sustained vowels; teeth visible on the belted notes.
- Cords visible in the neck on the peak; genuine physical effort, not mimed singing.
- Micro-beats between lines: a swallow, a breath, a flash of a smile — never a
  frozen face between phrases.
- Emotion arc across the 30s: resolve → lift → open joy → defiant belt → warmth.

Negative direction for every prompt: no closed mouth during vocals, no slack or
deadpan expression, no stiff head, no lip-sync drift, no extra fingers, no
warping around the jawline.

## Shot list — 6 × 5s = 30s

| # | Time | Frame | Camera | Face beat |
| --- | --- | --- | --- | --- |
| 1 | 0:00–0:05 | Medium close, stadium tunnel mouth, emerald + gold rim light | Slow push in | Head lowers, then lifts into lens — resolve hardening into a smile |
| 2 | 0:05–0:10 | Close-up, floodlights flaring behind her | Slight handheld drift | Brows lift on the rise; eyes widen, mouth opens fully on the hook |
| 3 | 0:10–0:15 | Wide-to-medium on the pitch, crowd bokeh, gold confetti | Arc around her | Open joy — laughing into the line, chin up, arms opening |
| 4 | 0:15–0:20 | Tight close-up, low angle, hard key from below | Locked off, subtle breathe | Peak belt — neck cords, teeth visible, eyes half-closed with effort |
| 5 | 0:20–0:25 | Medium, crowd in front of her, hands reaching in frame | Slow crane up | Defiance turning to connection; direct hard eye contact to lens |
| 6 | 0:25–0:30 | Close, centre pitch, floodlights blooming into flare | Slow pull back | Warm resolve — softening smile, one last sustained note, breath out |

## Per-shot prompt template

```
@Aurelia-Vega singing directly to camera, {FRAME}, {CAMERA}.
Her face is full of passion: {FACE BEAT}, brows fully engaged, eyes alive and
locked to lens, jaw moving fully on every vowel, visible breath and effort.
Emerald and gold stadium palette, anthemic festival lighting, cinematic
shallow depth of field, 720p, 16:9.
Negative: closed mouth while singing, blank or deadpan expression, stiff head,
lipsync drift, warped jaw, extra fingers.
```

## Execution order

1. Generate the 6 anchor stills with the `@Aurelia-Vega` element, one per shot,
   each already showing the target expression — the still sets the face, and
   Seedance carries it through the clip.
2. Slice the 30s audio into six 5s segments matched to the table above.
3. Run each still + its audio slice through Seedance 2.0 image-to-video at 720p
   with lipsync enabled.
4. Assemble in order, cut on the beat, grade emerald/gold, master to 30s.

## Status

Steps 1–4 are blocked on the Higgsfield MCP connection, which dropped mid-session.
Audio is already uploaded and confirmed; no re-upload needed when it returns.
