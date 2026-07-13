# Bevmap — CSV-driven beverage map

Everything on the map now lives in one editable table, `places.csv`.
Edit it, run one script, and the GeoJSON files the map consumes are
regenerated. See `DESIGN.md` for the reasoning.

## Files

| File | What it is |
|---|---|
| `places.csv` | **Source of truth.** One row per place per map layer. |
| `build_geojson.py` | Converts the CSV into the three JSON files below; geocodes new addresses. |
| `bars.json`, `icedmocha.json`, `happyhour.json` | Generated — don't edit by hand anymore. |
| `index.html`, `js/` | The map page, unchanged from the live site. |
| `environment.yml` | Optional conda env (the script needs nothing beyond stock Python). |

## Adding a place

Add a row to `places.csv`. Columns:

```
name, type, neighborhood, address, lat, lon, score1, score2, score3
```

- `type` is one of `Bar`, `Coffee`, `happyHour` (case-insensitive). A place
  on two layers = two rows.
- **You don't need coordinates.** Leave `lat`/`lon` empty and put a street
  address (e.g. `171 E 92nd St, New York, NY`) in `address`. The script
  looks it up on OpenStreetMap's geocoder and writes the coordinates back
  into the CSV, so each address is only ever looked up once.
- If you already know the coordinates, fill `lat`/`lon` and leave
  `address` empty (or filled — filled coordinates always win).
- Scores are 0–5; `na` is allowed and shows as "na/5" in the popup.

Then:

```bash
python3 build_geojson.py
```

It validates every row and refuses to write anything if a row is broken
(bad type, missing both address and coordinates, non-numeric score), so a
typo can't take down the map. `--no-geocode` runs fully offline and errors
on rows that would need a lookup.

Editing in Excel/Numbers works fine — just keep saving as CSV.

## Requirements / reproducing on any machine

Python ≥ 3.8, **no packages** — the script is standard library only.
Geocoding needs internet; everything else runs offline. If you want a
pinned interpreter via conda:

```bash
conda env create -f environment.yml && conda activate bevmap
```

## Testing the whole Hugo site locally

From the `sukritsingh.github.io` folder:

```bash
hugo server
```

then open <http://localhost:1313/side-projects/bevmap/> (the embed page)
and <http://localhost:1313/bevmap/index.html> (the raw map). Click each
layer toggle and a few markers to check popups.

To preview *this* folder's map standalone before copying anything over:

```bash
cd claude-bevmap && python3 -m http.server 8000
# open http://localhost:8000/index.html
```

(The one path difference: `index.html` loads `/bevmap/js/leaflet.ajax.min.js`
by absolute path, so standalone preview needs the folder served at `/bevmap/`
or that one script tag temporarily changed to `js/leaflet.ajax.min.js`.
Inside Hugo it's correct as-is.)

## Copying into the real site

On a branch in `sukritsingh.github.io`, copy into `static/bevmap/`:

```bash
cp places.csv build_geojson.py bars.json icedmocha.json happyhour.json \
   ../sukritsingh.github.io/static/bevmap/
```

`index.html` and `js/` are already identical there. `places.csv` and the
script will be published as (harmless) static files; keep them in
`static/bevmap/` anyway so the data and its source stay together.

Note: this regeneration fixes one bug in the live data — "Le Cheile" in
`happyhour.json` was typed `Bar`, so it showed a blue whiskey-scored popup
on the happy-hour layer. It's now correctly `happyHour`.

`testgeo.json` and `ponybar.geojson` in the live folder are unreferenced
leftovers and can be deleted whenever (optional).
