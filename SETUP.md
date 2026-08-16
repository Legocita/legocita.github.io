# Legocita Makes — Plain HTML Site (no Jekyll)

This is a plain static site — every page is a real, complete `.html` file.
No `_layouts`, `_includes`, `_data`, `_config.yml`, or any build step.
What you upload is exactly what visitors see.

## What's new in this update
- **New logo** (`assets/images/logo.png`) — the round wreath logo with
  "Legocita Makes / Cute Crafts by Carmen" now appears in the header on
  every page.
- **New pulsing favicon** — the strawberry "L" monogram
  (`assets/images/favicon-strawberry.png`) now shows in the browser tab,
  with a gentle pulse animation handled by `assets/js/favicon-pulse.js`.
  A plain static version (`favicon-static.png`) is used as a fallback for
  any browser/tab that doesn't run the animation.

## Uploading folders to GitHub (the "folders don't upload" issue)
GitHub's web uploader only accepts individual files unless you literally
**drag the folder itself** onto the upload page (works in Chrome/Edge) — or
use **GitHub Desktop**, which handles folders normally like any other app.
See the earlier instructions I gave you for the full walkthrough.

## One-time cleanup (if you haven't already switched over)

Delete these from the repo root if present — they're from the old Jekyll
setup and are no longer used:
- `_layouts/`, `_includes/`, `_data/` folders
- `_config.yml`
- `generate_pages.py`
- any leftover `about/` folder (replaced by `meet-carmen/`)
- the old top-level `index.md`

Easiest approach: delete everything in the repo except `README.md` and
`CNAME`, then upload everything in this zip fresh.

## Upload
1. Go to https://github.com/Legocita/legocita.github.io
2. Delete old files as above.
3. Upload everything from this folder — including `assets/` (with its
   `images`, `css`, and `js` subfolders), every category folder, and
   `index.html` at the root.
4. Commit to `main`. GitHub Pages publishes automatically within a minute
   or two — check https://legocitamakes.com afterward.

## How the site is organized
Every page is a normal path, e.g.:
- Homepage → `index.html`
- Jewelry landing page → `jewelry/index.html`
- Earrings → `jewelry/earrings/index.html`
- Meet Carmen → `meet-carmen/index.html`

Each `.html` file is self-contained — header, nav, and footer are written
directly into every page. Trade-off: easier to upload as one-off files, but
changing the nav or footer means editing it in all 38 files rather than one
shared template.

## Editing a page
Open the `.html` file, find the section inside `<main> ... </main>`, and
edit the text or swap a placeholder block. Example:
```html
<div class="ph">Photo coming soon</div>
```
becomes:
```html
<img src="/assets/images/jewelry/earrings/photo1.jpg" alt="Description of the piece">
```
(Upload the photo itself into `assets/images/...` first.)

## "See how I made this" video links
Product pages can link to a specific video on the Meet Carmen page (see
`reimagined/reclaimed-electronics/index.html` for a working example):
```html
<a class="video-teaser" href="/meet-carmen/#video-reclaimed-electronics-pendant">
  <span class="play-dot">&#9654;</span> See how I made this
</a>
```
To add a new one: add a video card with a unique `id` (e.g.
`id="video-crochet-bracelet"`) inside the "Watch Me Create" section of
`meet-carmen/index.html`, then paste a link like the one above on the
relevant product page, matching the `#video-...` anchor.
