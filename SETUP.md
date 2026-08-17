# Legocita Makes — Plain HTML Site (no Jekyll)

Every page is a real, complete `.html` file — no build step.

## What's new in this update — and exactly what you need to upload
Only three things changed. You do NOT need to re-upload all 38 pages —
just these:

1. **`assets/css/style.css`** (updated) — added the botanical corner
   sprinkles that now show on every page's header automatically, plus the
   colorful icon-badge styling.
2. **`assets/images/decor/`** (new folder, 13 small SVG files) — the
   hand-drawn rose, shells, birds, strawberries, lavender, leaf sprigs, and
   the six category icon badges.
3. **`index.html`** (homepage only) — added the new "What We Create" row
   of colorful icon badges linking to each shop category.

Every other page (all 37 category and sub-pages) automatically picks up
the new corner sprinkles through the shared CSS file — you don't need to
touch them individually.

## What the sprinkles look like
- **Every page header** (all sub-pages) now has a small leaf sprig in the
  top-left corner, a tiny wildflower bottom-right, and a strawberry accent
  top-right — subtle, consistent, and automatic.
- **The homepage hero** has a fuller scattering: a rose, a shell, a
  lavender sprig, a little bird, a leaf sprig, and a wildflower, using
  colors from across your full palette.
- **The new "What We Create" row** uses six colored circle badges (like
  the one you liked from the moodboard) — sage green for Jewelry, ocean
  blue for Watercolor, wildflower purple for Crochet & Fiber, driftwood
  for Reimagined, strawberry for Healing Hands, sunflower gold for
  Seasonal & Special — each links straight to that category page.

## Uploading
Go to https://github.com/Legocita/legocita.github.io and upload just the
three items above (drag the `decor` folder in directly, or use GitHub
Desktop). Commit to `main`, then check https://legocitamakes.com after a
minute or two.

## Adding more sprinkles later
All the individual decoration SVGs are reusable — drop an `<img>` tag
referencing any file in `assets/images/decor/` anywhere you'd like on a
page, e.g.:
```html
<img src="/assets/images/decor/strawberry.svg" style="width:40px;">
```
