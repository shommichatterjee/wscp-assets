# WorkSyncPro Assets CDN

Static asset server for the WorkSyncPro Logo Maker. Served via GitHub Pages.

## Setup (one-time)

1. Create a new GitHub repo named `wscp-assets`
2. Push this folder:
   ```
   cd wscp-assets
   git remote add origin https://github.com/shommichatterjee/wscp-assets.git
   git add .
   git commit -m "Initial asset upload"
   git push -u origin main
   ```
3. Go to repo Settings → Pages → Source: `main` branch, `/ (root)` folder → Save
4. Your CDN base URL will be: `https://shommichatterjee.github.io/wscp-assets`
5. Update `ASSETS_CDN_BASE` in `LogoMakerNative.html`

## Directory Structure

```
backgrounds/
  textures/
    gold/       ← 29 gold foil textures (JPG, 1200px)
    black/      ← 30 dark/carbon textures (JPG, 1200px)
    paper/      ← 10 grain/paper textures (PNG, 1200px)
  monogram/     ← 6 marble/stone backgrounds (JPG, 1200px)
  scenes/       ← Studio & stage photo backgrounds (add from Vecteezy)

elements/
  objects/      ← 27 vintage logo objects & animals (PNG, 512px)
  overlays/     ← 9 grunge/coffee stain overlays (PNG, 800px)
  vectors/      ← SVG logo elements (add from Vecteezy — see VECTEEZY_DOWNLOADS.md)
  frames/       ← Decorative frames (add from Vecteezy)
  badges/       ← Vintage badges & crests (add from Vecteezy)

manifest.json   ← Auto-generated catalog (re-run generate-manifest.py to update)
```

## Adding New Assets

1. Drop optimized files into the appropriate folder
2. Run `python3 generate-manifest.py` to rebuild the manifest
3. Commit and push — GitHub Pages auto-deploys in ~30 seconds

## Vecteezy Downloads

See `VECTEEZY_DOWNLOADS.md` for the curated download list.
