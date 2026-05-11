#!/usr/bin/env python3
"""Re-generate manifest.json from the current directory contents."""

import json, os, sys

CDN_BASE = os.environ.get("CDN_BASE", "https://raw.githubusercontent.com/shommichatterjee/wscp-assets/main")
BASE = os.path.dirname(os.path.abspath(__file__))

LABEL_OVERRIDES = {
    # objects
    "anchor": "Anchor", "arrows": "Arrows", "axes": "Axes", "barrels": "Barrels",
    "baseball-ball-1": "Baseball", "baseball-ball-2": "Baseball Alt",
    "baseball-bats": "Baseball Bats", "basketball-ball": "Basketball",
    "bicycle": "Bicycle", "boat-wheel": "Ship Wheel", "boot": "Boot",
    "boots": "Cowboy Boots", "brown-bear": "Brown Bear", "buffallo": "Buffalo",
    "chicken": "Chicken", "chicken-2": "Rooster", "deer": "Deer", "duck": "Duck",
    "fish": "Fish", "hammers": "Hammers", "lightbulb": "Lightbulb",
    "motorcycle": "Motorcycle", "photo-camera": "Camera",
    "pig": "Pig", "pig-2": "Pig Alt", "polar-bear": "Polar Bear",
    "soccer-ball": "Soccer Ball",
    # overlays
    "coffee-stain-1": "Stain 1", "coffee-stain-2": "Stain 2",
    "coffee-stain-3": "Stain 3", "coffee-stain-4": "Stain 4",
    "coffee-stain-5": "Stain 5", "coffee-stain-6": "Stain 6",
    "coffee-stain-7": "Stain 7", "coffee-stain-8": "Stain 8",
    "coffee-stain-9": "Stain 9",
}

def label(slug):
    return LABEL_OVERRIDES.get(slug, slug.replace('-', ' ').title())

def scan(rel_folder):
    result = []
    path = os.path.join(BASE, rel_folder)
    if not os.path.exists(path):
        return result
    for f in sorted(os.listdir(path)):
        if f.startswith('.') or not os.path.isfile(os.path.join(path, f)):
            continue
        slug = f.rsplit('.', 1)[0]
        ext = f.rsplit('.', 1)[-1].lower()
        result.append({
            "id": slug,
            "label": label(slug),
            "url": f"{CDN_BASE}/{rel_folder}/{f}",
            "file": f,
            "type": "svg" if ext == "svg" else ("png" if ext == "png" else "jpg"),
        })
    return result

def num_label(prefix, n):
    return f"{prefix} {int(n):02d}"

def scan_numbered(rel_folder, prefix):
    items = scan(rel_folder)
    for item in items:
        try:
            n = item["id"].split("-")[-1]
            item["label"] = num_label(prefix, n)
        except:
            pass
    return items

manifest = {
    "version": "1.1.0",
    "cdnBase": CDN_BASE,
    "backgrounds": {
        "textures": {
            "gold":  {"label": "Gold Textures",    "description": "Premium gold foil & metallic textures",   "items": scan_numbered("backgrounds/textures/gold",  "Gold")},
            "black": {"label": "Black Textures",   "description": "Dark leather, carbon & matte textures",   "items": scan_numbered("backgrounds/textures/black", "Black")},
            "paper": {"label": "Paper & Grain",    "description": "Aged paper & grain overlay textures",     "items": scan_numbered("backgrounds/textures/paper", "Paper")},
        },
        "monogram": {"label": "Marble Backgrounds", "description": "Marble & stone backgrounds",             "items": scan_numbered("backgrounds/monogram", "BG")},
        "scenes":   {"label": "Studio Scenes",      "description": "Studio & stage photo backgrounds",       "items": scan("backgrounds/scenes")},
    },
    "elements": {
        "objects":  {"label": "Vintage Objects",    "description": "Hand-crafted vintage logo objects",       "items": scan("elements/objects")},
        "overlays": {"label": "Grunge Overlays",    "description": "Grunge & texture overlay elements",       "items": scan("elements/overlays")},
        "vectors":  {"label": "Premium Vectors",    "description": "SVG logo elements from Vecteezy",         "items": scan("elements/vectors")},
        "frames":   {"label": "Frames & Borders",   "description": "Decorative frames & borders",             "items": scan("elements/frames")},
        "badges":   {"label": "Badges & Crests",    "description": "Vintage badges & crest shapes",           "items": scan("elements/badges")},
    }
}

out = os.path.join(BASE, "manifest.json")
with open(out, "w") as f:
    json.dump(manifest, f, indent=2)

total = sum(
    len(cat.get("items", [])) if "items" in cat
    else sum(len(sub.get("items", [])) for sub in cat.values() if isinstance(sub, dict))
    for section in manifest.values() if isinstance(section, dict)
    for cat in section.values() if isinstance(cat, dict)
)
print(f"manifest.json updated — {total} assets across all categories")
