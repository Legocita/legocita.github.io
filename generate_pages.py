#!/usr/bin/env python3
"""
Generates every section-landing page and sub-page for the Legocita Makes
site from the DATA structure below. Run once from /home/claude/build.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

def slugify(path):
    return path.strip("/")

def write(path, content):
    full = os.path.join(ROOT, path.lstrip("/"), "index.md")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    print("wrote", full)

SECTION_TPL = """---
title: {title}
description: "{description}"
permalink: {url}
---

<section class="page-header">
  <div class="container">
    <div class="breadcrumbs"><a href="{{{{ '/' | relative_url }}}}">Home</a> / {title}</div>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    <p class="lede">{intro}</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid">
{cards}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container" style="text-align:center;">
    <span class="eyebrow">Don't see exactly what you're picturing?</span>
    <h2>Every piece can be made custom.</h2>
    <p class="section-sub">{custom_note}</p>
    <a class="btn btn-primary" href="{{{{ '/custom-orders/' | relative_url }}}}">Start a Custom Order</a>
  </div>
</section>
"""

CARD_TPL = """      <div class="card">
        <div class="ph {phclass}">Photo coming soon<br><span>{title}</span></div>
        <div class="card-body">
          <h3>{title}</h3>
          <p>{blurb}</p>
          <a class="card-link" href="{{{{ '{url}' | relative_url }}}}">View {title} →</a>
        </div>
      </div>
"""

SUB_TPL = """---
title: {title}
description: "{description}"
permalink: {url}
---

<section class="page-header">
  <div class="container">
    <div class="breadcrumbs"><a href="{{{{ '/' | relative_url }}}}">Home</a> / <a href="{{{{ '{parent_url}' | relative_url }}}}">{parent_title}</a> / {title}</div>
    <span class="eyebrow">{parent_title}</span>
    <h1>{title}</h1>
    <p class="lede">{intro}</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="notice">Photos of {title_lower} pieces are coming soon — check back for the full collection!</div>
    <div class="grid">
{photo_cards}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container" style="text-align:center;">
    <span class="eyebrow">Want one made just for you?</span>
    <h2>Custom {title} welcome.</h2>
    <p class="section-sub">Tell Carmen your colors, occasion, or inspiration and she'll bring it to life.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{{{{ '/custom-orders/' | relative_url }}}}">Request a Custom Piece</a>
      <a class="btn btn-outline" href="{{{{ '{parent_url}' | relative_url }}}}">Back to {parent_title}</a>
    </div>
  </div>
</section>
"""

PHCLASSES = ["", "sage", "gold"]

def photo_cards(n, title):
    out = []
    for i in range(n):
        cls = PHCLASSES[i % len(PHCLASSES)]
        out.append(f'      <div class="card"><div class="ph {cls} ph-square">Photo coming soon<br><span>{title}</span></div></div>')
    return "\n".join(out)

DATA = {
    "jewelry": {
        "title": "Jewelry",
        "url": "/jewelry/",
        "eyebrow": "Wire-wrapped & hand-finished",
        "intro": "From everyday earrings to statement wearable art, every piece is wire-wrapped, beaded, or assembled by hand — designed to feel as good as it looks.",
        "custom_note": "Bridal sets, birthstone pieces, and one-of-a-kind commissions are always welcome.",
        "children": [
            ("Earrings", "earrings", "Lightweight, hand-finished earrings for everyday wear or special occasions."),
            ("Bracelets", "bracelets", "Wire-wrapped and beaded bracelets, from delicate stacks to statement cuffs."),
            ("Necklaces & Pendants", "necklaces-pendants", "Pendants, chokers, and layering necklaces built one wire loop at a time."),
            ("Rings", "rings", "Hand-formed rings in wire, wrapped stones, and mixed metals."),
            ("Wearable Art", "wearable-art", "Sculptural, unusual, statement pieces for the person who wants something no one else has."),
            ("Sets", "sets", "Matching earring, necklace, and bracelet sets — ready to gift or wear together."),
        ],
    },
    "watercolor": {
        "title": "Watercolor",
        "url": "/watercolor/",
        "eyebrow": "Painted by hand, one wash at a time",
        "intro": "Soft, storybook watercolor paintings and paper goods — from framed originals to greeting cards you'll want to keep instead of send.",
        "custom_note": "Pet portraits, house paintings, and custom color palettes are always an option.",
        "children": [
            ("Original Watercolors", "original-watercolors", "One-of-a-kind painted originals, ready to frame."),
            ("Cards & Paper Goods", "cards-paper-goods", "Greeting cards, prints, and paper goods painted with the same care as the originals."),
            ("Watercolor + Mixed Media", "mixed-media", "Watercolor paired with ink, thread, pressed botanicals, and other textures."),
        ],
    },
    "crochet-fiber": {
        "title": "Crochet & Fiber",
        "url": "/crochet-fiber/",
        "eyebrow": "Stitched with patience",
        "intro": "Tiny stitches turned into wearable and decorative pieces — from crochet jewelry to miniature keepsakes you can hold in one hand.",
        "custom_note": "Custom color combinations and made-to-order sizing are always available.",
        "children": [
            ("Crochet Jewelry", "crochet-jewelry", "Delicate crocheted earrings, necklaces, and accents."),
            ("Miniatures & Decorative Pieces", "miniatures-decorative", "Tiny crocheted keepsakes and decorative pieces made to bring a smile."),
            ("Fiber Accessories", "fiber-accessories", "Wearable fiber accessories built for everyday softness."),
        ],
    },
    "reimagined": {
        "title": "Reimagined",
        "url": "/reimagined/",
        "eyebrow": "Given a second life",
        "intro": "Circuit boards, hardware, and found objects — reclaimed and reworked into jewelry and art with a story behind every piece.",
        "custom_note": "Have a meaningful object you'd love reimagined into jewelry? Let's talk.",
        "children": [
            ("Reclaimed Electronics", "reclaimed-electronics", "Circuit boards and computer parts transformed into wearable art."),
            ("Found-Object Jewelry", "found-object-jewelry", "Hardware, keys, and small treasures repurposed into one-of-a-kind pieces."),
            ("One-of-a-Kind Assemblages", "one-of-a-kind-assemblages", "Mixed-material assemblages that can never quite be made the same way twice."),
        ],
    },
    "healing-hands": {
        "title": "Healing Hands / Medical Collection",
        "url": "/healing-hands/",
        "eyebrow": "For the people who take care of everyone else",
        "intro": "Jewelry and gifts designed for nurses, therapists, pharmacists, and every healthcare professional who could use a little something made just for them.",
        "custom_note": "Custom pieces for graduations, pinning ceremonies, and retirement gifts are a specialty.",
        "children": [
            ("Nursing", "nursing", "Stethoscope charms, caduceus pieces, and gifts for the nurse in your life."),
            ("Occupational Therapy", "occupational-therapy", "Meaningful pieces celebrating OT professionals."),
            ("Physical Therapy", "physical-therapy", "Gifts and jewelry for physical therapists and PTAs."),
            ("Pharmacy", "pharmacy", "Rx-inspired jewelry and gifts for pharmacists and pharmacy techs."),
            ("Rehab", "rehab", "Gifts for the rehabilitation team, from techs to specialists."),
            ("Other Healthcare Professions", "other-healthcare-professions", "Custom pieces for the many healthcare roles that keep everything running."),
            ("Healthcare Gifts & Custom Orders", "healthcare-gifts-custom-orders", "Graduation, pinning, and retirement gifts made to order."),
        ],
    },
    "seasonal": {
        "title": "Seasonal & Special Collections",
        "url": "/seasonal/",
        "eyebrow": "Made for the moment",
        "intro": "Limited-run collections inspired by strawberry season in Plant City, the changing seasons, holidays, and the plants and animals Carmen loves.",
        "custom_note": "Ask about custom holiday orders or a themed collection for your next event.",
        "children": [
            ("Strawberry / Plant City", "strawberry-plant-city", "A sweet tribute to Florida's strawberry capital."),
            ("Botanical & Nature", "botanical-nature", "Florals, leaves, and nature-inspired pieces."),
            ("Holidays", "holidays", "Seasonal collections for every holiday on the calendar."),
            ("Animals & Wildlife", "animals-wildlife", "Cardinals, critters, and creatures Carmen loves to paint and craft."),
            ("Limited Collections", "limited-collections", "Small-batch, once-and-done runs — when they're gone, they're gone."),
        ],
    },
}

for key, sec in DATA.items():
    cards = "".join(
        CARD_TPL.format(
            phclass=PHCLASSES[i % len(PHCLASSES)],
            title=child_title,
            blurb=blurb,
            url=f"/{key}/{slug}/",
        )
        for i, (child_title, slug, blurb) in enumerate(sec["children"])
    )
    content = SECTION_TPL.format(
        title=sec["title"],
        description=sec["intro"],
        url=sec["url"],
        eyebrow=sec["eyebrow"],
        intro=sec["intro"],
        cards=cards,
        custom_note=sec["custom_note"],
    )
    write(sec["url"], content)

    for child_title, slug, blurb in sec["children"]:
        sub_url = f"/{key}/{slug}/"
        content = SUB_TPL.format(
            title=child_title,
            description=blurb,
            url=sub_url,
            parent_url=sec["url"],
            parent_title=sec["title"],
            title_lower=child_title.lower(),
            intro=blurb,
            photo_cards=photo_cards(6, child_title),
        )
        write(sub_url, content)

print("Done.")
