# WHAT THE HANDS LET GO — Assets and Spend

## Reference sheets (nano_banana_pro, 2K, 9:16) — 6.00 credits

| Sheet | Job ID | Status |
|---|---|---|
| The woman | `bc3490b3-726d-4b2e-a352-c8ea3893b7bf` | live |
| The clearing (two-panel, empty of people) | `47ec504a-5d61-4314-9eed-c33ae0cd41ad` | live |
| The kestrel (two-panel) | `a41a3582-771a-4c25-b6ef-410f06b060c1` | live |

## Keyframes (nano_banana_pro, 2K, 9:16) — 22.00 credits

All live. Each generated against 2–3 reference sheets via `image_references`.

| # | Job ID | References |
|---|---|---|
| 01 | `1fbc49ea-e4c2-467d-bf69-0a5cd24c1286` | clearing, woman |
| 02 | `13a4005e-b617-446d-bdb5-9159fbed3871` | clearing, woman |
| 03 | `ca057555-321c-4780-b387-d940bde8b90d` | clearing, woman |
| 04 | `5af98535-d4ca-4921-b183-16df86b42139` | woman, clearing |
| 05 | `c1ab1cfa-9384-45eb-be1f-4d109983547e` | kestrel, clearing |
| 06 | `da6662e2-2ec9-47cf-b3c3-df484379c204` | woman, kestrel, clearing |
| 07 | `7c81472f-bdcb-4933-8e3e-df6651ff3d52` | woman, kestrel, clearing |
| 08 | `8a406a81-95c4-4183-a638-3af76c3a68c4` | kestrel, clearing |
| 09 | `4d9a2965-0f7a-4085-8c61-ab54068bd53b` | woman, clearing |
| 10 | `8910a316-5fe2-422e-8058-868a8b8dac7e` | woman, clearing |
| 11 | `db5e5234-10c7-48ed-a3b6-8210956556e4` | clearing, woman |

## Clips — batch 1 (kling3_0) — 103.25 credits — **UNDERSIZED, PREVIEW ONLY**

| # | Job ID | # | Job ID |
|---|---|---|---|
| 01 | `840b3e53-632b-407e-9472-efef10a328ab` | 07 | `0254429e-8f62-4e32-9680-61d50af07c0f` |
| 02 | `c59ffcf4-c695-42e5-b125-8def8e8fe09c` | 08 | `d0e5f541-f328-427f-b1d2-a8e02bdf4735` |
| 03 | `0024ca8c-11b3-4a28-aa1b-efbf58b331b5` | 09 | `d981cb40-4b6c-4b95-977f-d94e4a743697` |
| 04 | `bd53ba26-584a-4b80-ae5f-522d789d2027` | 10 | `f366543d-bdbf-48bc-bc82-4e4dd4d345c7` |
| 05 | `86939ebf-b69c-4a45-afa1-a15f4c948173` | 11 | `f45f916f-5488-42be-9245-6724db7dd4b0` |
| 06 | `f1c677f4-01d4-48b5-917f-cd7d8383c027` | | |

All 11 returned **716×1284** — below the 1080×1920 floor. See the error note.

## Spend

| Item | Credits |
|---|---|
| 3 reference sheets | 6.00 |
| 11 keyframes | 22.00 |
| 11 clips (std, sound on — wrong) | 103.25 |
| **Spent** | **131.25** |
| 11 clips re-fire (pro, silent) — quoted | 88.50 |

Balance was 150.83 before clips (a 100-credit top-up had landed, and the
balance matched prediction exactly — no drain). Balance after: **47.58**.
The re-fire needs **40.92 more**.

## Preset bounces declined

`24bae836-2c4a-48e0-89b6-49fcc0b21612` — "IN THE DARK". Bounced 7 of the 11
clips on first submission. Nothing was charged for a bounced submission.

---

# ERROR NOTE — the undersized clip batch

**What happened.** I submitted all 11 clips with `quality: "pro"`. Kling's
resolution parameter is **`mode`**, not `quality`. The unknown key was
ignored, so every clip rendered in `mode: "std"` at 716×1284. I also left
`sound` at its default `on` instead of passing `off`.

**Cost of the mistake.** 103.25 credits instead of the 88.50 quoted — and the
overage is not the resolution, it is the audio: `std` with sound is 1.75
credits/second, while `pro` silent is 1.50. I paid more and got less.

**Why it was not caught before submission.** I quoted the price from memory
of previous projects instead of running a `get_cost` preflight, which is
free. A preflight would have returned 88.50 against my 103.25 actual and
exposed the mismatch before a single credit was spent.

**Rule taken from this.** Before any batch spend, run `get_cost` on one
representative item and reconcile it against the quote. A preflight is free;
a wrong batch is not. And read the model's own parameter list from
`models_explore` rather than reusing a remembered key — the key that is
wrong silently is more expensive than the one that errors.

**What is salvageable.** The 11 std clips are a complete, correctly cut film.
They were assembled into a full preview at no further cost so the shots and
the edit can be judged before the re-fire is paid for. The keyframes and
reference sheets are unaffected and will be reused unchanged.
