// Renders every branded asset in content.mjs to PNG.
// Usage: node instagram/design/build.mjs   (needs playwright-core; Chromium from /opt/pw-browsers)
import { chromium } from "playwright-core";
import { mkdir, readFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { assets } from "./content.mjs";

const here = dirname(fileURLToPath(import.meta.url));
const outRoot = join(here, "..");
const css = await readFile(join(here, "brand.css"), "utf8");

const PILLARS = {
  ai: { label: "AI Video", color: "var(--ai)" },
  design: { label: "Design", color: "var(--design)" },
  freelance: { label: "Freelance", color: "var(--freelance)" },
  youtube: { label: "Faceless YT", color: "var(--youtube)" },
  proof: { label: "Behind the scenes", color: "var(--proof)" },
};

const header = (pillar, i, total) => `
  <div class="header">
    <div class="brand"><div class="mark">FT</div>@finaltoucch</div>
    ${pillar ? `<div class="tag" style="color:${PILLARS[pillar].color}">${PILLARS[pillar].label}</div>` : ""}
    ${total ? `<div class="count">${String(i).padStart(2, "0")}/${String(total).padStart(2, "0")}</div>` : ""}
  </div>`;

const footer = (i, total, last) => `
  <div class="footer">
    <div class="dots">${Array.from({ length: total }, (_, k) => `<i class="${k + 1 === i ? "on" : ""}"></i>`).join("")}</div>
    ${last ? `<div class="handle">Follow for more →</div>` : `<div class="swipe">Swipe →</div>`}
  </div>`;

const glow = (color, pos = "top:-300px;right:-300px") =>
  `<div class="glow" style="background:${color};${pos}"></div>`;

// ---------- slide layouts ----------
const layouts = {
  cover: (s) => `
    <div class="kicker">${s.kicker}</div>
    <div class="display" style="font-size:${s.size || 128}px">${s.title}</div>
    ${s.sub ? `<div class="sub">${s.sub}</div>` : ""}`,

  vs: (s) => `
    <div class="kicker">${s.kicker}</div>
    <div class="display" style="font-size:88px;margin-bottom:56px">${s.title}</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:28px">
      ${[s.left, s.right].map((c) => `
        <div class="card" style="border-top:8px solid ${c.color}">
          <div style="font-size:30px;font-weight:900;color:${c.color};letter-spacing:.06em;text-transform:uppercase;margin-bottom:22px">${c.name}</div>
          <div class="p" style="font-size:34px">${c.text}</div>
        </div>`).join("")}
    </div>
    ${s.note ? `<div style="margin-top:36px;font-size:26px;color:var(--muted)">${s.note}</div>` : ""}`,

  item: (s) => `
    <div class="big-num" style="${s.color ? `-webkit-text-stroke-color:${s.color}` : ""}">${s.num}</div>
    <div class="display" style="font-size:96px;margin:48px 0 40px">${s.title}</div>
    <div class="p">${s.text}</div>`,

  callout: (s) => `
    <div class="card" style="padding:64px;border-color:${s.color || "var(--accent)"};border-width:3px">
      <div style="font-size:30px;font-weight:900;letter-spacing:.1em;text-transform:uppercase;color:${s.color || "var(--accent)"};margin-bottom:28px">${s.kicker}</div>
      <div class="display" style="font-size:92px;margin-bottom:40px">${s.title}</div>
      <div class="p">${s.text}</div>
    </div>`,

  steps: (s) => `
    <div class="kicker">${s.kicker}</div>
    <div class="display" style="font-size:96px;margin-bottom:56px">${s.title}</div>
    <div style="display:flex;flex-direction:column;gap:20px">
      ${s.steps.map((t, k) => `
        <div style="display:flex;align-items:center;gap:30px">
          <div style="flex:none;width:76px;height:76px;border-radius:50%;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;font-weight:900;font-size:34px">${k + 1}</div>
          <div class="card" style="flex:1;padding:26px 34px;border-radius:24px"><div class="p" style="font-size:34px">${t}</div></div>
        </div>`).join("")}
    </div>`,

  cta: (s) => `
    <div class="display" style="font-size:120px">${s.title}</div>
    <div class="sub">${s.text}</div>
    <div style="display:flex;gap:22px;margin-top:64px;flex-wrap:wrap">
      ${["Save", "Share", "Follow"].map((b, k) => `
        <div style="font-size:32px;font-weight:800;padding:22px 40px;border-radius:999px;${k === 2 ? "background:var(--accent);color:var(--accent-ink)" : "border:2px solid rgba(255,255,255,.3)"}">${b}</div>`).join("")}
    </div>`,
};

// ---------- full-canvas assets ----------
function carouselSlide(c, s, i, total) {
  const color = PILLARS[c.pillar].color;
  const pos = i % 2 ? "top:-350px;right:-350px" : "bottom:-400px;left:-350px";
  return `<div class="canvas post">
    ${glow(s.glow || color, pos)}
    ${header(c.pillar, i, total)}
    <div class="body">${layouts[s.layout](s)}</div>
    ${footer(i, total, i === total)}
  </div>`;
}

function reelCover(a) {
  const color = PILLARS[a.pillar].color;
  return `<div class="canvas story">
    ${glow(color, "top:-200px;right:-400px")}
    ${glow("var(--accent)", "bottom:-600px;left:-500px;opacity:.18")}
    ${header(a.pillar)}
    <div class="body">
      <div class="kicker">${a.kicker}</div>
      <div class="display" style="font-size:${a.size || 150}px">${a.title}</div>
      ${a.sub ? `<div class="sub" style="font-size:46px">${a.sub}</div>` : ""}
    </div>
    <div class="footer"><div class="swipe">▶ Watch</div><div class="handle">@finaltoucch</div></div>
  </div>`;
}

function highlight(h) {
  return `<div class="canvas story" style="padding:0;align-items:center;justify-content:center">
    <div style="width:760px;height:760px;border-radius:50%;background:radial-gradient(circle at 30% 25%, #1f1f27, var(--bg));border:6px solid ${h.color};display:grid;place-items:center;position:relative;z-index:2">
      <svg width="340" height="340" viewBox="0 0 24 24" fill="none" stroke="${h.color}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">${h.icon}</svg>
    </div>
  </div>`;
}

function avatar() {
  return `<div class="canvas square" style="align-items:center;justify-content:center;background:radial-gradient(circle at 30% 25%, #1c1c24, var(--bg))">
    <div style="width:640px;height:640px;border-radius:150px;background:var(--accent);display:grid;place-items:center;position:relative;z-index:2;box-shadow:0 40px 160px rgba(198,255,0,.35)">
      <div class="display" style="font-size:360px;color:var(--accent-ink);letter-spacing:-0.07em">FT</div>
    </div>
  </div>`;
}

// ---------- render ----------
const page = (inner, w, h) => `<!doctype html><html><head><meta charset="utf-8">
<style>${css} html,body{width:${w}px;height:${h}px}</style></head><body>${inner}</body></html>`;

const browser = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const ctx = await browser.newContext({ deviceScaleFactor: 1 });
const tab = await ctx.newPage();
let count = 0;

async function shoot(html, w, h, file) {
  await mkdir(dirname(file), { recursive: true });
  await tab.setViewportSize({ width: w, height: h });
  await tab.setContent(page(html, w, h), { waitUntil: "load" });
  await tab.evaluate(() => document.fonts.ready);
  await tab.screenshot({ path: file, clip: { x: 0, y: 0, width: w, height: h } });
  count++;
}

for (const c of assets.carousels) {
  for (const [k, s] of c.slides.entries()) {
    await shoot(carouselSlide(c, s, k + 1, c.slides.length), 1080, 1350,
      join(outRoot, c.dir, `${String(k + 1).padStart(2, "0")}.png`));
  }
}
for (const r of assets.reelCovers) await shoot(reelCover(r), 1080, 1920, join(outRoot, r.file));
for (const h of assets.highlights) await shoot(highlight(h), 1080, 1920, join(outRoot, "brand/highlights", `${h.name}.png`));
await shoot(avatar(), 1080, 1080, join(outRoot, "brand/profile-picture.png"));

await browser.close();
console.log(`rendered ${count} images`);
