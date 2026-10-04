"""versions.json from versions/<patch>/{info,mapdata}.json.

The README no longer carries a per-patch table (the owner 2026-10-04: removed); the counts live in
versions.json, and Sloppy's Terrain Stats page draws them.

info.json: {"patch", "date" (YYYY-MM-DD), "map_sha1", "manifest"} — optionally "same_as": the patch whose map file
this one shipped unchanged (then the folder holds only info.json).

    python build_index.py
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))


def _key(v):
    m = re.match(r"(\d+)\.(\d+)([a-z]?)", v)
    return int(m.group(1)), int(m.group(2)), m.group(3)


def load():
    rows = []
    vdir = os.path.join(HERE, "versions")
    for ver in sorted(os.listdir(vdir), key=_key):
        info = json.load(open(os.path.join(vdir, ver, "info.json"), encoding="utf-8"))
        md_path = os.path.join(vdir, ver, "mapdata.json")
        counts = json.load(open(md_path, encoding="utf-8"))["counts"] if os.path.exists(md_path) else None
        rows.append({**info, "counts": counts})
    by = {r["patch"]: r for r in rows}
    for r in rows:                                             # a patch with the same map file shows that map's counts
        if r.get("same_as") and r["counts"] is None:
            r["counts"] = by[r["same_as"]]["counts"]
    return rows


def main():
    rows = load()
    with open(os.path.join(HERE, "versions.json"), "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=1)
        f.write("\n")
    print(len(rows), "patches")


if __name__ == "__main__":
    main()
