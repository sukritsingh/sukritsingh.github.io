#!/usr/bin/env python3
"""Build the bevmap GeoJSON files from places.csv.

Usage:
    python3 build_geojson.py [--csv places.csv] [--no-geocode]

Reads places.csv (columns: name, type, neighborhood, address, lat, lon,
score1, score2, score3), geocodes any row that has an address but no
lat/lon via OSM Nominatim, writes the resolved coordinates back into the
CSV, then writes bars.json, icedmocha.json and happyhour.json next to it.

Standard library only; works on any Python >= 3.8.
"""

import argparse
import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

# CSV "type" value (lowercased) -> (canonical Type property, output file)
TYPES = {
    "bar": ("Bar", "bars.json"),
    "coffee": ("Coffee", "icedmocha.json"),
    "happyhour": ("happyHour", "happyhour.json"),
}

FIELDS = ["name", "type", "neighborhood", "address", "lat", "lon",
          "score1", "score2", "score3"]

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
# Nominatim usage policy: identify your app, max 1 request/second.
USER_AGENT = "sukritsingh-bevmap/1.0 (https://sukritsingh.github.io)"


def geocode(address):
    """Return (lat, lon) strings for an address via Nominatim, or None."""
    query = urllib.parse.urlencode({"q": address, "format": "json", "limit": 1})
    req = urllib.request.Request(f"{NOMINATIM_URL}?{query}",
                                 headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        results = json.load(resp)
    if not results:
        return None
    return results[0]["lat"], results[0]["lon"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", default="places.csv",
                        help="input CSV (default: places.csv)")
    parser.add_argument("--no-geocode", action="store_true",
                        help="fail on missing coordinates instead of "
                             "calling the geocoding API")
    args = parser.parse_args()

    csv_path = Path(args.csv)
    out_dir = csv_path.parent
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    errors = []
    geocoded = 0
    for i, row in enumerate(rows, start=2):  # start=2: header is line 1
        where = f"line {i} ({row.get('name', '?')})"

        if row.get("type", "").strip().lower() not in TYPES:
            errors.append(f"{where}: unknown type {row.get('type')!r}, "
                          f"expected one of: {', '.join(sorted(TYPES))}")
            continue
        for col in ("score1", "score2", "score3"):
            if row.get(col, "").strip().lower() == "na":
                continue  # shows up as "na/5" in the popup
            try:
                float(row[col])
            except (ValueError, KeyError):
                errors.append(f"{where}: {col} is not a number (or 'na'): "
                              f"{row.get(col)!r}")

        if row.get("lat", "").strip() and row.get("lon", "").strip():
            continue
        address = row.get("address", "").strip()
        if not address:
            errors.append(f"{where}: needs either lat+lon or an address")
            continue
        if args.no_geocode:
            errors.append(f"{where}: missing lat/lon and --no-geocode is set")
            continue

        if geocoded:
            time.sleep(1.1)  # Nominatim rate limit
        result = geocode(address)
        geocoded += 1
        if result is None:
            errors.append(f"{where}: no geocoding match for {address!r} — "
                          f"try a fuller address or fill lat/lon by hand")
            continue
        row["lat"], row["lon"] = result
        print(f"geocoded {row['name']}: {row['lat']}, {row['lon']}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(f"aborted: {len(errors)} problem(s), no files written")

    if geocoded:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        print(f"updated {csv_path} with {geocoded} geocoded coordinate(s)")

    for type_key, (type_name, filename) in TYPES.items():
        features = [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(r["lon"]), float(r["lat"])],
                },
                "properties": {
                    "name": r["name"],
                    "Neighborhood": r["neighborhood"],
                    "Type": type_name,
                    "Score1": r["score1"],
                    "Score2": r["score2"],
                    "Score3": r["score3"],
                },
            }
            for r in rows if r["type"].strip().lower() == type_key
        ]
        out_path = out_dir / filename
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump({"type": "FeatureCollection", "features": features},
                      f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"wrote {out_path} ({len(features)} places)")


if __name__ == "__main__":
    main()
