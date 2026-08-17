# Legocita Makes — Single-File Site

Everything is now ONE HTML file. Every "page" (all 38 of them — Home,
Jewelry, all 6 jewelry sub-pages, Meet Carmen, etc.) lives inside
`index.html` as a hidden/shown section, and a small bit of JavaScript
switches between them instantly when you click a nav link — no page
reloads, no separate files.

## What you upload from now on
Just **`index.html`**, almost always. The `assets/` folder (CSS, images,
fonts, decorations) rarely changes — you'll only touch it again if you add
new photos or I make a styling change that needs a new asset file.

## Important trade-off — please read
Because this is one file with JavaScript-driven navigation, the web
addresses changed shape:

- **Before:** `legocitamakes.com/jewelry/earrings/`
- **Now:** `legocitamakes.com/#jewelry-earrings`

If you've shared or printed any of the old-style links anywhere (business
cards, social bios, QR codes, Google listings), those specific addresses
will stop working — visitors would land on a blank/404 instead of the
Earrings page. The homepage (`legocitamakes.com`) is unaffected, and every
link *inside* the site (nav, buttons, "See how I made this") was updated
automatically, so browsing the site itself works exactly the same.

If discoverability in Google search for individual categories matters to
you long-term, the old multi-page version is better for that (each page
was its own crawlable address). Happy to keep both versions on hand if
you'd like — just say so.

## Uploading
Go to https://github.com/Legocita/legocita.github.io, upload `index.html`
(and `assets/` the first time, or whenever it changes), commit to `main`.
Check https://legocitamakes.com after a minute or two.

## Editing content later
Open `index.html` and search for the page you want, e.g. search for
`id="page-jewelry-earrings"` — everything between that section's opening
and closing `<section>` tag is that page's content, editable exactly like
before (swap `<div class="ph">Photo coming soon</div>` for a real
`<img>` tag, edit text, etc.).

## What's new in this update
- **Single file** — see above.
- **Social icons refreshed** — real Instagram, Facebook, Pinterest, TikTok,
  Etsy, and YouTube icons (glyphs, not text abbreviations), lined up in the
  footer with a slow, staggered pulse animation to draw the eye. Update the
  `href` on each one once you have your real profile URLs (TikTok, Etsy,
  and YouTube link to placeholder handles right now).
