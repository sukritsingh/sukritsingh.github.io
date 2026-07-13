# Bevmap update — design spec

## Goal

Make adding/editing map entries easy: edit one CSV, run one script, get the
GeoJSON files the existing map already consumes. Addresses get converted to
lat/lon automatically. Zero changes to the map page itself.

## Current state

- `static/bevmap/index.html` — Leaflet map, loads three GeoJSON files by
  relative path: `bars.json` (Type=Bar), `icedmocha.json` (Type=Coffee),
  `happyhour.json` (Type=happyHour).
- Each feature: point coordinates + properties `name`, `Neighborhood`,
  `Type`, `Score1..3` (strings).
- Embedded in Hugo via iframe from `content/side-projects/bevmap.md`.
- `testgeo.json` / `ponybar.geojson` are unreferenced leftovers (not copied
  here; delete from the live site whenever convenient — optional).

## Design decisions (minimal-change principles)

1. **One CSV is the source of truth** (`places.csv`). Columns:
   `name, type, neighborhood, address, lat, lon, score1, score2, score3`.
   A place appearing on two maps (e.g. Pony Bar) is simply two rows.
2. **The script generates the three existing JSON filenames** so
   `index.html` needs no edits at all. The HTML in this folder is a
   byte-identical copy of the live one.
3. **Geocoding**: rows with an `address` but empty `lat`/`lon` are geocoded
   via OSM's Nominatim API (same data source as the map tiles). The
   resolved coordinates are **written back into the CSV**, so geocoding
   happens once per new row and every later run is fully deterministic and
   offline. Rows with lat/lon filled are never re-geocoded.
4. **No dependencies**: the script uses only the Python standard library
   (any Python ≥ 3.8). Reproducing the environment on any machine =
   having Python. An optional `environment.yml` is included for conda
   users who want a pinned interpreter.
5. **Validation**: the script fails loudly on unknown `type` values, rows
   missing both coordinates and address, and non-numeric scores — so a bad
   CSV can't silently produce a broken map.

## Out of scope (deliberately)

- No visual/UI changes to the map. It works. Suggestions if you ever want
  them, in rough order of value-per-line-of-code:
  - Distinct marker icons per layer (coffee cup / cocktail glass) instead of
    colored circles — Leaflet `divIcon` with an emoji is ~10 lines.
  - Pin the Leaflet version's SRI hashes or self-host it (currently 1.7.1
    from unpkg).
  - Drop `leaflet.ajax.min.js` and use `fetch()` + `L.geoJSON` (removes the
    plugin file); only worth it if the plugin ever breaks.
- No build integration with Hugo — the JSONs stay committed artifacts,
  which keeps the site build untouched.

## Workflow after copying over

```
edit places.csv  →  python3 build_geojson.py  →  git add/commit/push
```
