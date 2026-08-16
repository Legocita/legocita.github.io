# Legocita Makes — Plain HTML Site (no Jekyll)

Every page is a real, complete `.html` file — no build step. What you
upload is exactly what visitors see.

## What's new in this update
- **New color system** — replaced the pink/lavender palette with a natural
  landscape palette: warm cream/sand/stone as the quiet foundation (~70-75%
  of the page), sage/forest greens for navigation and structure, sky and
  ocean blue for fine accent lines, and strawberry, sunflower gold, and
  wildflower purple used sparingly as single accent moments (a button here,
  a photo frame there) rather than all at once.
- All of this lives in **one file**: `assets/css/style.css`. You don't need
  to touch any of the 38 page files to see it — just re-upload that one CSS
  file (and the rest of the folder, to be safe) and every page updates.
- Added a small reusable "botanical divider" (a fine line with a leaf) used
  under a few section headings on the homepage and Meet Carmen page — easy
  to sprinkle onto other pages later if you like it.

## Uploading folders to GitHub
GitHub's web uploader only accepts individual files unless you drag the
**folder itself** onto the upload page (works in Chrome/Edge), or use
**GitHub Desktop**, which handles folders like any other app.

## Upload
1. Go to https://github.com/Legocita/legocita.github.io
2. Delete old files if this is your first time switching to this static
   version (see prior notes) — otherwise just overwrite existing files.
3. Upload everything from this folder, including `assets/`.
4. Commit to `main`. Check https://legocitamakes.com after a minute or two.

## How the site is organized
Every page is a normal path, e.g. `jewelry/earrings/index.html`,
`meet-carmen/index.html`. Header, nav, and footer are written directly into
each page — colors and fonts are the one shared thing, via
`assets/css/style.css`.

## Editing a page
Open the `.html` file, find the section inside `<main> ... </main>`, and
edit text or swap a placeholder block:
```html
<div class="ph">Photo coming soon</div>
```
becomes:
```html
<img src="/assets/images/jewelry/earrings/photo1.jpg" alt="Description of the piece">
```

## Using the new accent classes
- `.frame-gold` — wraps a photo in a soft gold border, for a special/featured
  image (use on one photo at a time, not every photo).
- `.botanical-divider` — the small leaf-and-line divider under a heading:
  ```html
  <div class="botanical-divider"><svg viewBox="0 0 24 24" fill="none"><path d="M12 2c-1 4-4 6-8 6 4 4 4 9 8 14 4-5 4-10 8-14-4 0-7-2-8-6z" fill="var(--leaf)"/></svg></div>
  ```

## "See how I made this" video links
Product pages can link to a specific video on the Meet Carmen page (see
`reimagined/reclaimed-electronics/index.html` for a working example).
