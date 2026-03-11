#!/usr/bin/env python3
"""Generate search/europe.svg from Europe GeoJSON. Run once; commit europe.svg."""
import json
import urllib.request
import sys
from pathlib import Path

GEOJSON_URL = "https://raw.githubusercontent.com/leakyMirror/map-of-europe/master/GeoJSON/europe.geojson"
# Europe bounds (approx) for equirectangular projection
LON_MIN, LON_MAX = -31, 50
LAT_MIN, LAT_MAX = 34, 72
WIDTH, HEIGHT = 420, 320


def project(lon, lat):
    x = (lon - LON_MIN) / (LON_MAX - LON_MIN) * WIDTH
    y = (LAT_MAX - lat) / (LAT_MAX - LAT_MIN) * HEIGHT
    return x, y


def ring_to_path(ring):
    pts = [project(c[0], c[1]) for c in ring]
    if not pts:
        return ""
    return "M " + " L ".join(f"{round(x,1)},{round(y,1)}" for x, y in pts) + " Z"


def geom_to_path(geom):
    if geom["type"] == "Polygon":
        return " ".join(ring_to_path(ring) for ring in geom["coordinates"])
    if geom["type"] == "MultiPolygon":
        return " ".join(
            ring_to_path(ring)
            for poly in geom["coordinates"]
            for ring in poly
        )
    return ""


def main():
    out_path = Path(__file__).resolve().parent / "europe.svg"
    print("Fetching GeoJSON...")
    with urllib.request.urlopen(GEOJSON_URL, timeout=30) as r:
        data = json.load(r)
    paths = []
    for f in data.get("features", []):
        props = f.get("properties", {})
        iso2 = (props.get("ISO2") or "").strip().upper()
        name = (props.get("NAME") or "").strip()
        if not iso2 or not name:
            continue
        geom = f.get("geometry")
        if not geom:
            continue
        d = geom_to_path(geom)
        if not d:
            continue
        paths.append((iso2, name, d))
    print(f"Writing {len(paths)} countries to {out_path}")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" class="europe-map-svg">\n')
        for iso2, name, d in paths:
            f.write(f'  <path id="{iso2}" data-name="{name}" d="{d}" />\n')
        f.write("</svg>\n")
    print("Done.")


if __name__ == "__main__":
    main()
