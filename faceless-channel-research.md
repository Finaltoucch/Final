# Faceless YouTube Channel — Research Notes

Working notes from reviewing a viral X/Twitter thread on building a faceless,
AI-assisted YouTube channel, plus the adaptations for our own setup.

**Source:** `x.com/vampscally/status/2083711186051223694`
**Reviewed:** 2026-08-02
**Status:** Research complete. Niche not yet chosen — see [Open Items](#open-items).

---

## 1. The Claim

Author says: eight months in, no camera, no face, no team. Last month the channel
did **$9,400** — roughly 480,000 views at an **$18 RPM** ≈ $8,600 AdSense, plus
affiliate. Niche is finance. Monthly tool cost ~$57.

Presented as a repeatable six-step build with three pasteable prompts.

---

## 2. Verdict — What Holds Up

**Niche selection by RPM is the highest-leverage decision.**
Revenue per thousand views varies ~5–10x by topic because it's set by advertiser
bids, not by YouTube. Choosing on RPM before choosing on passion is correct and
most people get it backwards.

**Retention is the algorithm; the script is retention.**
Clean audio and stock footage are table stakes. Whether a video gets pushed to new
viewers is decided by whether people keep watching, and that's a writing problem.
His Step 2 script prompt is the strongest asset in the whole thread.

**The cost math is honest.**
~$57/mo is real, and it genuinely replaces work that costs money (scriptwriter,
VO, editor, SEO).

**Ship volume before judging results.**
Right advice. Wrong reason — see below.

---

## 3. Verdict — What's Inflated or Wrong

| Claim | Reality |
|---|---|
| "Finance: $15–50 RPM" | $50 is an outlier (US-audience tax/insurance/credit, Q4), not the top of a range. Realistic band is ~$8–25. His own $18 sits at healthy-but-not-magic. **Ceiling presented as spread.** |
| "Retention target 70%" | Exceptional, not a target. Solid 10-min performers land 40–50% average view percentage. Treating 70% as pass/fail makes you think you're failing while doing fine. |
| "Algorithm needs 20–30 videos to learn who to show you to" | Folklore. There is no channel-level warmup counter — videos are tested largely on their own merits. Ship 20–30 anyway: you get better at writing and you buy more lottery tickets. **Same conclusion, invented mechanism.** |
| "$9,400 last month" | Unverifiable, and shaped conveniently. 480k views in month 8 off ~30 videos, from a channel doing 200 views at video 5, means a couple of hard breakouts. That's survivorship presented as pipeline. |
| Channel never named | Standard for the genre. Keep one hand on your wallet. |

---

## 4. What the Thread Leaves Out

- **Monetization threshold.** 1,000 subs + 4,000 watch hours before a single cent.
  Months of unpaid work that the "$57/mo → $9,400" framing erases.
- **Platform risk.** YouTube has been tightening on mass-produced, templated,
  low-differentiation content. A channel that is *entirely* AI script → synthetic
  voice → stock B-roll sits squarely in the blast radius. This is the main risk to
  the business model, not a footnote.
- **Saturation.** "Faceless finance channel using AI" is among the most crowded
  corners of the platform right now. The edge available eight months ago is not the
  edge available today. Differentiation has to come from the writing or from a
  genuinely untapped sub-angle.
- **Disclosure.** Synthetic voice narration requires YouTube's altered-content
  toggle at upload. Not mentioned once in the thread.

---

## 5. The Tell

The thread is written to its own Step 2 formula — shocking number in line one,
problem amplification, credibility bridge ("that mistake cost me three weeks"),
body sections each with a takeaway, callback close, earn-the-follow.

Not a criticism: it's evidence the author can actually write to the structure he's
selling. It's also why it reads as so persuasive — you're inside the funnel while
reading about the funnel.

**Bottom line:** a good workflow with a fabricated income statement stapled to the
front. Keep the prompts, keep the strategy, discount the numbers.

---

## 6. The Six-Step Build

1. **Pick the niche by RPM**, not by interest. Run the math before committing.
2. **Write the script.** This is the actual business — everything else is assembly.
3. **Voice it once, keep that voice forever.** Channel identity depends on it.
4. **Assemble in CapCut.** Visual changes every 3–5 seconds. Auto-captions on
   (most viewers scroll with sound off).
5. **Generate the metadata layer** — title, description, tags, chapters, pinned
   comment.
6. **Post 20–30 videos before judging anything.** Same day, same time, weekly,
   for the first six months.

Claude carries steps 1, 2, 5 and most of 6's planning. Steps 3 and 4 are assembly.

---

## 7. Our Stack

We have a **cloned voice of our own** on Higgsfield — consent is not an issue,
rights are clean. This replaces the ElevenLabs line item entirely.

| Step | Thread's version | Ours |
|---|---|---|
| Script | Claude — $20/mo | Claude — $20/mo |
| Voice | ElevenLabs — $22/mo | Higgsfield (already held) |
| Edit | CapCut — free | CapCut — free |
| B-roll | Pexels / Pixabay — free | same |

**Advantage the thread doesn't have:** a clone of our own voice can be re-rendered
in eight months and still match. Stock voices get deprecated and retuned. Ours
won't drift.

### Voice production rules

- **Lock one settings combo and never touch it** — same voice ID, same speed, same
  stability, every video. If episode 12 sounds 10% off from episode 4, viewers
  notice without knowing why.
- **~0.9x speed** reads with more authority for finance/analytical content.
- **Punctuation carries the pacing.** Short sentences, em dashes, paragraph breaks.
  Add explicit `[pause]` markers only where a beat really matters — over-marking is
  what makes cloned voices sound stilted.
- **Fix numbers in the script, not in post.** Cloned voices mangle `$18,000` and
  `2026` inconsistently. Spell them as spoken.
- **Tick YouTube's altered-content disclosure** at upload, from video one, so it's
  routine. It's about synthetic audio, not about consent — it applies to us. No
  measurable reach penalty; skipping it is a policy violation on every video.

---

## 8. The Prompts

### 8.1 — Niche selection (Step 1)

```
Act as a YouTube channel strategist. I want to start a faceless channel.

Analyze these 5 niches: [LIST]

For each give me:
1. Estimated RPM range
2. Competition level (low / medium / high)
3. Content repeatability score (1-10)
4. Audience size potential
5. Monetization options beyond AdSense
6. One untapped content angle nobody is doing

Then build a 52-video title calendar for the winner. If you can't fill 52,
the niche is too narrow.

Final recommendation: which niche to start, and why.
```

**Our addition:** also demand a saturation read and a platform-risk read per niche.
The original prompt is blind to both, and both are the things that actually kill
these channels.

### 8.2 — Script (Step 2) — voice-ready version

Adapted from the thread, with narration constraints folded in for our cloned voice.

```
You are a senior YouTube scriptwriter for a faceless channel in [NICHE].

Write a full script for: "[TITLE]"
Length: 10 minutes (~1,500 words)
Audience: [WHO — be specific: age, situation, what they're stuck on]

STRUCTURE
1. Hook (0:00-0:30): open on a shocking number or counterintuitive
   claim. No intro, no greeting, no channel name.
2. Problem amplification (0:30-1:30): make them feel it with specific
   numbers. Use "you" constantly.
3. Credibility bridge (1:30-2:00): one reason to trust this. Under 30
   seconds. No résumé.
4. Body (2:00-9:00): 3-5 sections. Each = bold claim, real example with
   numbers, one usable takeaway, bridge to next. Pattern interrupt every
   90 seconds.
5. Close (9:00-10:00): call back to the hook, one action, earn the sub.

VOICE CONSTRAINTS (this is read aloud by a single narrator)
- Sentences under 20 words. Active voice. No filler.
- No parentheticals, no bullet lists, no "as you can see" or any
  reference to on-screen visuals.
- Spell numbers as spoken: "eighteen thousand dollars," "twenty
  twenty-six," "three percent."
- Line break at every natural breath point.
- No tongue-twisters or heavy sibilance runs.

OUTPUT
- Full script
- Estimated spoken runtime at 150 wpm
- 5 thumbnail concepts
- 3 titles: one curiosity, one SEO, one emotional
```

### 8.3 — Metadata (Step 5)

```
Act as a YouTube SEO specialist.

Video topic: [TOPIC]. Niche: [NICHE].
Script summary: [2-3 sentences]

Output:
1. Title under 60 characters, main keyword, triggers curiosity
2. Description, 200 words, SEO optimized, with timestamps and a CTA
3. 15 tags, broad and specific mixed
4. 5 chapter titles with timestamps
5. 3 pinned-comment options to boost engagement

Optimize for click-through rate and watch time.
```

---

## 9. Reference — RPM by Niche

Thread's figures alongside a corrected read. Treat all of these as directional;
actual RPM depends heavily on audience geography (US/UK/CA/AU pay far more),
season (Q4 peaks, January craters), and video length.

| Niche | Thread's claim | More realistic |
|---|---|---|
| Finance & investing | $15–50 | $8–25, spikes higher on tax/insurance/credit |
| Technology & AI | $12–30 | $8–20 |
| Health & longevity | $10–25 | $6–18, ad-restriction risk on medical claims |
| General & entertainment | $3–8 | $2–8 |

---

## Open Items

- [ ] Choose the niche — candidates not yet decided. Run 8.1 with the saturation
      and platform-risk additions once we have 3–5 to compare.
- [ ] Build the 52-video title calendar for whichever niche survives.
- [ ] Test a 30-second hook through the Higgsfield voice before committing to the
      full pipeline — confirm pacing and number pronunciation.
- [ ] Lock and document the exact Higgsfield voice settings (voice ID, speed,
      stability) so every future episode matches.
- [ ] Decide the weekly publish slot and hold it for six months.
