# Legocita Makes — Plain HTML Site (no Jekyll)

## What's fixed/new in this update

**1. Header overlap bug — fixed.** The nav bar had 11 top-level items plus
the logo/brand text, and at most desktop widths they didn't actually fit
in the space they were given — the layout was quietly squeezing your logo
text until it wrapped and collided with "Home". Fixed by:
- Never letting the logo/brand shrink or wrap.
- Trimming the nav link size slightly so more items fit comfortably.
- Widening the header's available row and switching to the mobile-style
  slide-out menu a bit earlier (below ~1300px window width) so it never
  has to cram — a wide phone/tablet browser now gets the clean hamburger
  menu instead of a squeezed row.

**2. Each nav tab now hovers a different color**, pulled from across your
palette — Jewelry hovers leaf green, Watercolor hovers ocean blue, Crochet
& Fiber hovers lavender, Reimagined hovers driftwood, Healing Hands hovers
strawberry, Seasonal & Special hovers sunflower gold, and so on through
all 11 tabs. The current page's tab keeps that same color instead of
always being forest green.

**3. Flowers are bigger and there are more of them.** Every page now has:
- 5 flowers/leaves/shells around the page header (up from 2–3), sized
  noticeably larger.
- A *second*, smaller cluster of 2 flowers down near the bottom
  "custom order" call-to-action section, so the botanical touches carry
  through the page instead of only showing up at the top.
- The homepage hero now has 8, plus 2 more near the bottom CTA.

## What you need to upload
This is a full re-upload again (all 38 pages changed, since each page's
flower placement is baked into its HTML) — plus the updated CSS file:
- `assets/css/style.css` (header fix + hover colors + sizing)
- All 38 `.html` pages

## Uploading
Go to https://github.com/Legocita/legocita.github.io, upload everything in
this folder, commit to `main`. Check https://legocitamakes.com after a
minute or two — try resizing your browser window narrower to see the nav
switch cleanly to the hamburger menu instead of overlapping.
