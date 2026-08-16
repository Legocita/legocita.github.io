# Setting up on legocita.github.io

This folder is a complete Jekyll site. GitHub Pages runs Jekyll automatically —
no build step needed on your end.

## 1. Remove the old files from the repo
Delete these two files from the root of `legocita.github.io`:
- `index.html` (the old single-page site)
- `legocita-makes-logo.png` (replaced by `assets/images/logo.jpg`)

## 2. Add everything in this folder
Copy every file and folder here into the root of the `legocita.github.io`
repository, keeping the folder structure exactly as-is (the `_` folders are
required — don't rename them).

Easiest way if you're not comfortable with git commands:
1. Go to https://github.com/Legocita/legocita.github.io
2. Delete the two old files (via the trash-can icon on each file's page).
3. Click "Add file" → "Upload files" and drag in everything from this folder
   (make sure folders like `_layouts`, `_includes`, `_data`, `assets`,
   `jewelry`, `watercolor`, etc. all come along — GitHub's uploader supports
   dragging whole folders in most browsers).
4. Commit directly to `main`.

GitHub Pages will rebuild automatically — the site is usually live again
within 1–2 minutes. You can check build status under the repo's
"Actions" tab.

## 3. What's here right now
- Every page from your requested structure (Home, Jewelry + 6 sub-pages,
  Watercolor + 3, Crochet & Fiber + 3, Reimagined + 3, Healing Hands + 7,
  Seasonal & Special + 5, Custom Orders, Gallery, About Carmen, Contact).
- Your logo, dropdown navigation matching that structure, and a soft
  blush/lavender/sage color palette pulled from the mood boards.
- "Photo coming soon" placeholder blocks everywhere a real product photo
  will eventually go.

## 4. Adding real photos later
Drop photos into `assets/images/` (make subfolders per category if you like,
e.g. `assets/images/jewelry/earrings/`), then in the relevant `.md` file
swap a placeholder block like:

```html
<div class="ph">Photo coming soon</div>
```

for:

```html
<img src="{{ '/assets/images/jewelry/earrings/photo1.jpg' | relative_url }}" alt="Description of the piece">
```

## 5. Editing text
Every page is a plain-text `.md` file — the header/nav/footer are shared
automatically from `_layouts/default.html` and `_data/nav.yml`, so you only
ever need to touch nav.yml once to change the menu everywhere.

## 6. Testing locally (optional)
If you want to preview changes before pushing, install Ruby + Jekyll and run:
```
bundle exec jekyll serve
```
from the repo root, then visit `http://localhost:4000`.
