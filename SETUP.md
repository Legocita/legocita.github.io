# Legocita Makes — Plain HTML Site (no Jekyll)

This is a plain static site now — every page is a real, complete `.html`
file. No `_layouts`, `_includes`, `_data`, `_config.yml`, or any build step.
What you upload is exactly what visitors see.

## One-time cleanup: remove the old Jekyll files

Since the last version used Jekyll, first delete these from the repo root
(if present) — they're no longer used and having them there could confuse
things:
- `_layouts/` (whole folder)
- `_includes/` (whole folder)
- `_data/` (whole folder)
- `_config.yml`
- `generate_pages.py`
- Any leftover `about/` folder from before (now replaced by `meet-carmen/`)
- The old top-level `index.md` (replaced by `index.html` in this build)

The easiest way to do this cleanly: delete every file/folder in the repo
except `README.md` and `CNAME` (if you already have one), then upload
everything in this zip fresh.

## Upload

1. Go to https://github.com/Legocita/legocita.github.io
2. Delete the old files as above.
3. Click **Add file → Upload files**, then drag in **everything** from this
   folder — including the `assets` folder, every category folder
   (`jewelry`, `watercolor`, etc.), `index.html`, and `CNAME`.
4. Commit directly to `main`.

GitHub Pages will publish automatically, usually within a minute or two.
Check **https://legocitamakes.com** afterward.

## How the site is organized

Every page lives at a normal, readable path — for example:
- Homepage → `index.html`
- Jewelry landing page → `jewelry/index.html`
- Earrings → `jewelry/earrings/index.html`
- Meet Carmen → `meet-carmen/index.html`

Each `.html` file is self-contained: the header, dropdown navigation, and
footer are written directly into every single page. That's the trade-off
of going plain-HTML — easier to upload as one-off files, but if you want to
change something in the nav or footer, you now have to make that change in
all 38 files rather than one shared template.

## Editing a page

Open the relevant `.html` file, find the section you want to change inside
`<main> ... </main>`, and edit the text or swap a placeholder block. Example
placeholder to replace with a real photo:

```html
<div class="ph">Photo coming soon</div>
```
becomes:
```html
<img src="/assets/images/jewelry/earrings/photo1.jpg" alt="Description of the piece">
```
(Upload the photo itself into `assets/images/...` first.)

## Changing the nav or footer everywhere

Because there's no shared template anymore, updating the navigation menu or
footer means editing that same block in every `.html` file. If that becomes
a hassle down the road, the Jekyll version (with one shared header/footer
file) is easy to bring back — just say the word.

## "See how I made this" video links

Product pages that want to link to a specific video on the Meet Carmen page
already have this pattern baked in (see `reimagined/reclaimed-electronics/index.html`
for a working example):

```html
<a class="video-teaser" href="/meet-carmen/#video-reclaimed-electronics-pendant">
  <span class="play-dot">&#9654;</span> See how I made this
</a>
```

To add a new one:
1. In `meet-carmen/index.html`, find the "Watch Me Create" section and add a
   new video card with a unique `id`, e.g. `id="video-crochet-bracelet"`.
2. On the relevant product page, paste a link like the one above, changing
   the `#video-...` anchor to match.
