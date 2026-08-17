# Legocita Makes — Plain HTML Site (no Jekyll)

## What's fixed/new in this update

**The bug:** the botanical decorations were anchored to the full browser
width instead of your actual content column — on a wide monitor that put
them way out near the edge of the screen, far from the cards and text, and
sometimes clipped. Fixed: decorations are now positioned relative to the
1180px content column itself, so they sit close to the headline and cards
no matter how wide the browser window is.

**Floating motion:** every sprinkle now gently drifts (a slow rise/fall
with a little rotation, ~6-9 seconds per cycle, all slightly offset from
each other so they don't move in sync).

**Two new botanicals:** jasmine and baby's breath, added to the existing
set (rose, wildflower, lavender, leaf sprig, strawberry, shell, bird).

**Every page is genuinely different now:** each of the 38 pages gets its
own reproducible combination of 2–3 flowers/leaves/shells in different
corner positions — the homepage hero has the fullest set (6), sub-pages
get 2–3. Re-running the generator always produces the same result per
page (no shuffling every time you rebuild).

**Hidden on small screens** (phones) to avoid clutter — sprinkles show on
tablet/desktop widths only.

## What you need to upload
This one's a full re-upload of all 38 pages, since the per-page sprinkle
combinations are baked into each file's HTML (not just the shared CSS this
time):
- `assets/css/style.css` (updated — new sprinkle/float system)
- `assets/images/decor/` (2 new files: `jasmine.svg`, `baby-breath.svg`)
- All 38 `.html` pages (each has its own sprinkle set baked in)

## Uploading
Go to https://github.com/Legocita/legocita.github.io, upload everything in
this folder (drag the whole unzipped folder in, or use GitHub Desktop),
commit to `main`. Check https://legocitamakes.com after a minute or two.

## Adjusting a page's flowers later
Each page's sprinkles live near the top of its `<section class="page-header">`
(or `<section class="hero">` on the homepage), inside a `<div class="sprinkles">`
block. Each flower is one line:
```html
<span class="sprinkle" style="top:-10px; left:-30px; width:34px; height:40px;
  background-image:url('/assets/images/decor/rose.svg'); animation-delay:-2s;"></span>
```
Swap the file name in `background-image` for any icon in `assets/images/decor/`,
or nudge `top/left/right/bottom` to reposition it.
