"""versions.json and the README table from versions/<patch>/{info,mapdata}.json.

info.json: {"patch", "date" (YYYY-MM-DD), "map_sha1", "manifest"} — optionally "same_as": the patch whose map file
this one shipped unchanged (then the folder holds only info.json).

    python build_index.py
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
COLUMNS = (("Trees", "ent_dota_tree"), ("Camps", "npc_dota_neutral_spawner"), ("Towers", "npc_dota_tower"),
           ("Outposts", "npc_dota_watch_tower"), ("Watchers", "npc_dota_lantern"), ("Lotus pools", "npc_dota_lotus_pool"),
           ("Wisdom shrines", "npc_dota_xp_fountain"), ("Twin gates", "npc_dota_unit_twin_gate"))


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


def table(rows):
    head = "| Patch | Date | Map | " + " | ".join(c for c, _ in COLUMNS) + " | What moved since the patch before |"
    sep = "|" + "---|" * (4 + len(COLUMNS))
    lines = [head, sep]
    for r in reversed(rows):
        c = r["counts"] or {}
        if r.get("same_as"):
            pic, moved = f"same file as {r['same_as']}", "the same map file"
        else:
            has = os.path.exists(os.path.join(HERE, "versions", r["patch"], "map.webp"))
            pic = f"[picture](versions/{r['patch']}/map.webp)" if has else "rendering"
            moved = r.get("changes", "")
        lines.append(f"| {r['patch']} | {r['date']} | {pic} | " + " | ".join(str(c.get(k, "")) for _, k in COLUMNS)
                     + f" | {moved} |")
    return "\n".join(lines)


def main():
    rows = load()
    with open(os.path.join(HERE, "versions.json"), "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=1)
        f.write("\n")
    readme = os.path.join(HERE, "README.md")
    s = open(readme, encoding="utf-8").read()
    a, b = s.index("<!-- TABLE START -->"), s.index("<!-- TABLE END -->")
    s = s[:a] + "<!-- TABLE START -->\n" + table(rows) + "\n" + s[b:]
    open(readme, "w", encoding="utf-8", newline="\n").write(s)
    print(len(rows), "patches")


if __name__ == "__main__":
    main()
