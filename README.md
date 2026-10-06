# Oldgrowth

Top-down pictures of the Dota 2 map for every patch, and what stands on it — trees, neutral camps, towers, runes,
outposts, lotus pools, Roshan and Tormentors — counted from the game's own files.

It feeds the Terrain pages of [Sloppy](https://sikleq.github.io/Sloppy/) and is free for anyone to use.

## What is here

```
versions/<patch>/map.webp      the whole map, 4096 × 4096, top-down
versions/<patch>/mapdata.json  every map object with its position, read from the map file — and the map's layers:
                               lane creep paths, river currents (spline, radius and strength of each node), shop,
                               no-ward and Roshan pit zones, hero and courier spawn points
versions/<patch>/entities.json.gz  the map file's FULL entity list as decompiled, every class and key
versions/<patch>/info.json     the patch's date and the exact map file it shipped
versions.json                  all of the above in one table
tiles/<patch>/<row>_<col>.webp the map at 8192 × 8192 in 16 × 16 tiles, for zooming in (Sloppy's Terrain pages
                               load them from https://sikleq.github.io/Oldgrowth/)
```

Full-size pictures (about 10000 × 10400, 2 game units per pixel) are attached to the
[releases](https://github.com/sikleq/Oldgrowth/releases), one per patch, to keep the repository small.

When a patch shipped the very same map file as an earlier one, its folder holds only `info.json`, and
`versions.json` says which patch it matches (`same_as`).

## How it is made

1. **The map file of every patch.** `game/dota/maps/dota.vpk` lives in Steam depot 373301. For each patch the
   builds of its release days are looked up in the depot's manifest history; the manifest alone (DepotDownloader
   `-manifest-only`) gives the map file's SHA-1, so one map file is downloaded per distinct SHA-1. The first build
   after a patch date is now and then still the old map, so a patch's map is the last build of its first days.
2. **The picture.** Each map file is loaded in Source Filmmaker (Dota 2 Workshop Tools). A camera with a 1° lens
   flies over the map from 240 000 units up in a serpentine, 6 × 11 frames of 3840 × 2160; with so narrow a lens the
   frames are nearly orthographic, so each one is placed by the camera's own position and the borders are
   cross-faded — no feature matching. The land beyond the map's edge stays dark, as the game draws it (it lights
   nothing out there).
   Maps older than 7.41 are rendered on the game as it was before 7.41 (the build of 2026-03-16, every depot
   brought back to that day): 7.41 reworked the water, and today's game draws older maps' rivers as maroon
   triangles.
   7.39's map file holds two "templar gates" (`npc_dota_unit_templar_gate`, the Twin Gate model with another
   skin) that no patch note mentions and 7.39b removed; that build has no texture for them, so they came out
   pink. They are replaced by the ground of the 7.39b picture, which is unchanged there.
3. **The objects.** The map file's entity lumps are decompiled with
   [ValveResourceFormat](https://github.com/ValveResourceFormat/ValveResourceFormat) (Source2Viewer) and every
   object of interest is listed with its position; camp boxes and the other zones come from their trigger hulls.
   Lane paths follow each creep spawner's chain of `path_corner`s. A river current
   (`dota_movespeed_modifier_path`) is a spline of nodes in the entity's own frame (turned by its yaw), each with
   in / out tangents, a radius (the reach of its speed bonus, bank to bank) and a strength (2 strong, 1 moderate).
   `entities.json.gz` keeps everything else too, as Source2Viewer gives it (`_lump` names the entity lump).

The scripts are in [sikleq/Sloppy](https://github.com/sikleq/Sloppy) — `scripts/gen/map_history.py`,
`scripts/gen/stitch_sfm.py`, `scripts/gen/mend_map.py`, `scripts/gen/extract_map_entities.py`,
`scripts/gen/oldgrowth_mapdata.py` — and the method is
written up in its `docs/terrain.md`. Sloppy's Terrain pages compare every patch's map with the one before it.

## Thanks

The idea and the inspiration come from the interactive maps of
[Leamare](https://github.com/leamare/dota-interactive-map) and
[devilesk](https://github.com/devilesk/dota-interactive-map). The renders, the data and the tooling here are our
own.

## License

Dota 2, its map and everything shown on it are © Valve Corporation. This is an unofficial fan project, not
affiliated with or endorsed by Valve. The tables and the scripts that build them may be used freely.
