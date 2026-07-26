# I Made a 44-Second Anime Film in an Afternoon. Here's the Full Receipt.

Yesterday I sat down with two tools and came out with a finished animated short. Eleven shots, an original character who stays the same person across every cut, ambient sound on all of them, 44 seconds end to end.

No camera. No animator. No studio. No render farm.

Total generation cost: about 200 credits.

Let me show you exactly how, including the parts that went wrong — because the "AI can do anything" posts you scroll past never show you the receipt.

## The stack

Two things.

**Claude** — the agent. It writes the shot list, holds the story straight across eleven shots, and calls the tools.

**Higgsfield through MCP** — the generator. MCP is the part most people miss. It isn't Claude *describing* how to make a video. It's Claude *operating* the video tool directly: submitting jobs, polling them, pulling results, assembling the final cut. You talk. It builds.

That distinction is the whole story. The gap between AI that gives advice and AI that does the work is exactly where the money is.

## What it actually cost

- One character reference still: **2 credits**
- Each 4-second shot at 720p with generated ambient audio: **18 credits**
- Stitching eleven clips into one MP4: **free**

Eleven shots is 198 credits. Add the reference still and call it 200 for a finished 44-second film.

Including my mistakes and re-runs, the entire session came to roughly 253 credits.

## The workflow that actually holds a character together

This is the part worth stealing.

My first attempt failed. I generated one good shot of a character, then tried to produce six more that matched by describing her again in every prompt. You get six different girls. Every prompt is a fresh roll of the dice.

The fix is a reference. Generate one still of your character — one image, 2 credits — then pass that image into every shot as a reference input. Now the model isn't inventing her each time. It's matching her.

Better still: once you have a video clip you love, use *that clip* as the reference for the next ones. Motion, palette, line weight, face — it all carries.

Lock the character first. Then shoot.

## The two mistakes

I passed a video clip's ID into a slot that expects an image. Rejected. There was a separate slot for video references and I hadn't read the model's spec properly. Read your tool's actual inputs before you burn credits guessing.

Second: the platform kept suggesting a stylistic preset instead of running my prompts literally. Accepting it would have restyled half my shots and broken continuity with the rest. I declined and resubmitted. Know when to refuse the tool's suggestion — consistency across shots beats one shot looking cooler in isolation.

## What this actually means

The barrier that just fell isn't technical skill. It's capital and headcount.

What's left — and what's now scarce — is knowing what to ask for. The model will happily render a boring shot. It has no opinion about whether your story works, whether cut three should be a close-up, or whether your ending is earned.

I spent maybe fifteen minutes writing prompts and two hours on the shot list.

That ratio is the job now. The tools are cheap. Taste isn't.
