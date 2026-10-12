# @finaltoucch — Weekly Content System

**Account:** [instagram.com/finaltoucch](https://www.instagram.com/finaltoucch/)

**Positioning:** *I use AI to design, make videos, and land remote clients, and I show you exactly how.*

The page sits where four things meet: **design**, **AI video**, **remote freelancing**
(Upwork, Contra) and **faceless YouTube with AI**. Every post should leave the viewer with
either a skill they can use or a way to earn money from it.

---

## Profile Setup

- **Display name:** `Final Touch | AI Design & Video`. Instagram search reads this field, so it needs keywords.
- **Bio (pick one):**
  - `AI video • Design • Remote work 💻 I show you the tools & how to get paid with them ⬇️`
  - `Turning AI tools into income 🎬 Higgsfield • Upwork • Contra • Faceless YT`
  - `Designer using AI to work from anywhere 🌍 Free prompts & guides ⬇️`
- **Link in bio:** a link page with your portfolio (Contra profile works well), free prompt pack, and YouTube.
- **Highlights:** `AI Video 🎬` · `Design 🎨` · `Upwork 💼` · `Contra ⚡` · `Faceless YT ▶️` · `Results 📈`
- **Look:** dark background, one accent color (electric lime `#C6FF00` or yellow `#FFD60A`),
  bold sans-serif (Montserrat / Inter Bold). Small `@finaltoucch` watermark top-left on everything.

---

## The 5 Content Pillars

| Pillar | What it covers | Formats that work |
|---|---|---|
| 🎬 **AI Video** | Higgsfield and other generators: workflows, prompt breakdowns, before/after, camera-motion tricks | Screen-record Reels, "made this in 10 min" Reels |
| 🎨 **Design** | Design fixes, before/after, brand kits, thumbnails, AI + design workflow | Before/after Reels, tip carousels |
| 💼 **Freelance & Remote** | Upwork proposals, Contra profiles, pricing, finding clients, remote setup | Carousels (high saves), talking-text Reels |
| ▶️ **Faceless YouTube** | Storytelling niches, script → voice → visuals pipeline, retention, monetization rules | Carousels, workflow Reels |
| 📈 **Proof / BTS** | Your real projects, client wins, numbers, mistakes, "day in the life" | POV Reels, Stories |

**Mix per week:** about 40% tutorials, 30% freelancing and money, 20% showcase, 10% proof and personal.
Proof posts are what make people trust the tutorials.

---

## Weekly Rhythm (5 feed posts + daily Stories)

| Day | Slot | Pillar |
|---|---|---|
| **Mon** | Tutorial Reel | 🎬 AI Video (Higgsfield workflow) |
| **Tue** | Carousel | 💼 Upwork / Contra / remote work |
| **Wed** | Before/After Reel | 🎨 Design |
| **Thu** | Carousel or Reel | ▶️ Faceless YouTube with AI |
| **Fri** | POV / BTS Reel | 📈 Proof, results, day in the life |
| **Sat** | Stories only | Q&A box, polls, reply to DMs |
| **Sun** | Batch day (no post) | Plan and produce next week from `topic-bank.md` |

**Comment-keyword CTA:** end tutorials with *"Comment PROMPT and I'll DM it to you."* It brings
in comments and DMs, which the algorithm rewards. Automate it with ManyChat, or reply by hand to start.

---

## Sunday Batch Workflow (about 3–4 hours)

1. Pick 5 topics from `topic-bank.md`, one per pillar slot.
2. Duplicate the latest `week-XX.md` and fill it in.
3. Generate visuals: AI clips in Higgsfield, carousels in Canva or Figma.
4. Record screen captures and voiceovers in one sitting.
5. Edit all Reels in CapCut with burned-in captions and the watermark.
6. Schedule everything in Meta Business Suite.
7. Write down what last week's best post was, then make a variation of it.

---

## Hashtag Banks (use 5–8 per post: 1 brand, 2 broad, 3–5 niche)

- **Brand:** `#finaltoucch`
- **AI video:** `#aivideo #higgsfield #aifilm #aitools #aiart #generativeai #aianimation`
- **Design:** `#graphicdesign #designtips #brandidentity #designinspiration #canva #figma`
- **Freelance:** `#upwork #upworkfreelancer #contra #freelancing #remotework #workfromanywhere #freelancetips`
- **Faceless YT:** `#facelessyoutube #youtubeautomation #contentcreator #youtubetips #aistorytelling`

---

## Rules That Keep the Account Trustworthy

- **Never fake income screenshots.** Share real numbers or none. Proof is the brand.
- **Fees and policies change.** Check Upwork's current service fee and Connects pricing,
  Contra's current terms, and YouTube's monetization policy before posting about them.
- **Faceless YouTube:** YouTube does not monetize mass-produced or repetitive "inauthentic" content.
  Always teach adding real storytelling, editing, and originality, not "spam AI videos for money."
- **Disclose AI** where Instagram's "AI info" label applies to realistic AI-generated video.

---

## Branded Templates

All slides and covers are generated from code, so every post looks consistent:

- `design/brand.css`: colors, fonts, logo mark, layout pieces
- `design/content.mjs`: the text for each slide and cover. Edit this to make a new week.
- `design/build.mjs`: renders everything to PNG (1080×1350 carousels, 1080×1920 covers)

Rebuild: `npm i playwright-core` in `design/`, then `node design/build.mjs`.
Slide layouts available: `cover`, `vs`, `item`, `callout`, `steps`, `cta`.

## Files

- `README.md`: this strategy
- `topic-bank.md`: 60 post ideas across the pillars, enough for 12 weeks
- `week-01.md`: first full week, ready to produce
- `week-01/`: rendered carousels and Reel covers for week 1
- `brand/`: profile picture and 6 highlight covers
- `../instagram-content-pack-01.md`: earlier general-facts pack, now off-niche. Keep it as a format reference.
