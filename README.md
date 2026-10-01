# Oldgrowth

Top-down pictures of the Dota 2 map for every patch, and what stands on it — trees, neutral camps, towers, runes,
outposts, lotus pools, Roshan and Tormentors — counted from the game's own files.

It feeds the Terrain pages of [Sloppy](https://sikleq.github.io/Sloppy/) and is free for anyone to use. The name is a
nod to Nature's Prophet's Curse of the Oldgrowth.

## What is here

```
versions/<patch>/map.webp      the whole map, 4096 × 4096, top-down
versions/<patch>/mapdata.json  every map object with its position, read from the map file
versions/<patch>/info.json     the patch's date and the exact map file it shipped
versions.json                  all of the above in one table
```

Full-size pictures (about 10000 × 10400, 2 game units per pixel) are attached to the
[releases](https://github.com/sikleq/Oldgrowth/releases), one per patch, to keep the repository small.

When a patch shipped the very same map file as an earlier one, its folder holds only `info.json`, and the table
says which patch it matches.

<!-- TABLE START -->
| Patch | Date | Map | Trees | Camps | Towers | Outposts | Watchers | Lotus pools | Wisdom shrines | Twin gates | What moved since the patch before |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 7.41f | 2026-09-15 | [picture](versions/7.41f/map.webp) | 2475 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | no object moved (the map file still changed) |
| 7.41e | 2026-07-30 | rendering | 2475 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | no object moved (the map file still changed) |
| 7.41d | 2026-06-04 | rendering | 2475 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | no object moved (the map file still changed) |
| 7.41c | 2026-05-06 | rendering | 2475 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | no object moved (the map file still changed) |
| 7.41b | 2026-04-07 | same file as 7.41a | 2475 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | the same map file |
| 7.41a | 2026-03-28 | rendering | 2475 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | trees +0 −1 |
| 7.41 | 2026-03-24 | rendering | 2476 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | trees +324 −304; camps moved: 7; towers moved: 2; watchers moved: 3; lotus pools moved: 2; Tormentors moved: 2; twin gates moved: 2 |
| 7.40c | 2026-01-21 | rendering | 2456 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | no object moved (the map file still changed) |
| 7.40b | 2025-12-23 | same file as 7.40 | 2456 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | the same map file |
| 7.40 | 2025-12-15 | rendering | 2456 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | trees +239 −293; camps moved: 9; towers moved: 1; watchers +4 −8; wisdom shrines moved: 2 |
| 7.39e | 2025-10-02 | rendering | 2510 | 28 | 22 | 2 | 14 | 2 | 2 | 2 | no object moved (the map file still changed) |
| 7.39d | 2025-08-05 | rendering | 2510 | 28 | 22 | 2 | 14 | 2 | 2 | 2 | trees +0 −3 |
| 7.39c | 2025-06-24 | rendering | 2513 | 28 | 22 | 2 | 14 | 2 | 2 | 2 | watchers moved: 2 |
| 7.39b | 2025-05-29 | rendering | 2513 | 28 | 22 | 2 | 14 | 2 | 2 | 2 | trees +38 −27; camps moved: 2; towers moved: 1; watchers moved: 1 |
| 7.39 | 2025-05-21 | rendering | 2502 | 28 | 22 | 2 | 14 | 2 | 2 | 2 | trees +290 −297; camps moved: 5; towers moved: 4; watchers moved: 1; lotus pools moved: 2; Roshan pits moved: 2; bounty runes moved: 1 |
| 7.38c | 2025-03-27 | rendering | 2509 | 28 | 22 | 2 | 14 | 2 | 2 | 2 | trees +152 −130; camps moved: 2; towers moved: 1; watchers moved: 1 |
| 7.38b | 2025-03-05 | rendering | 2487 | 28 | 22 | 2 | 14 | 2 | 2 | 2 | trees +2 −11 |
| 7.38 | 2025-02-19 | rendering | 2496 | 28 | 22 | 2 | 14 | 2 | 2 | 2 |  |
<!-- TABLE END -->

## How it is made

1. **The map file of every patch.** `game/dota/maps/dota.vpk` lives in Steam depot 373301. For each patch the
   builds of its release days are looked up in the depot's manifest history; the manifest alone (DepotDownloader
   `-manifest-only`) gives the map file's SHA-1, so one map file is downloaded per distinct SHA-1. The first build
   after a patch date is now and then still the old map, so a patch's map is the last build of its first days.
2. **The picture.** Each map file is loaded in Source Filmmaker (Dota 2 Workshop Tools). A camera with a 1° lens
   flies over the map from 240 000 units up in a serpentine, 6 × 11 frames of 3840 × 2160; with so narrow a lens the
   frames are nearly orthographic, so each one is placed by the camera's own position and the borders are
   cross-faded — no feature matching. The corners beyond the map's edge, where nothing renders, get plain ground
   quilted from the map's own plainest ground.
3. **The objects.** The map file's entity lumps are decompiled with
   [ValveResourceFormat](https://github.com/ValveResourceFormat/ValveResourceFormat) (Source2Viewer) and every
   object of interest is listed with its position; camp boxes come from their trigger hulls.

The scripts are in [sikleq/Sloppy](https://github.com/sikleq/Sloppy) — `scripts/gen/map_history.py`,
`scripts/gen/stitch_sfm.py`, `scripts/gen/extract_map_entities.py` — and the method is written up in its
`docs/terrain.md`.

## Thanks

The idea and the inspiration come from the interactive maps of
[Leamare](https://github.com/leamare/dota-interactive-map) and
[devilesk](https://github.com/devilesk/dota-interactive-map). The renders, the data and the tooling here are our
own.

## License

Dota 2, its map and everything shown on it are © Valve Corporation. This is an unofficial fan project, not
affiliated with or endorsed by Valve. The tables and the scripts that build them may be used freely.
