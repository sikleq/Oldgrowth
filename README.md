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
tiles/<patch>/<row>_<col>.webp the map at 8192 × 8192 in 16 × 16 tiles, for zooming in (Sloppy's Terrain pages
                               load them from https://sikleq.github.io/Oldgrowth/)
```

Full-size pictures (about 10000 × 10400, 2 game units per pixel) are attached to the
[releases](https://github.com/sikleq/Oldgrowth/releases), one per patch, to keep the repository small.

When a patch shipped the very same map file as an earlier one, its folder holds only `info.json`, and the table
says which patch it matches.

<!-- TABLE START -->
| Patch | Date | Map | Trees | Camps | Towers | Outposts | Watchers | Lotus pools | Wisdom shrines | Twin gates | What moved since the patch before |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 7.41f | 2026-09-15 | [picture](versions/7.41f/map.webp) | 2475 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | no object moved (the map file still changed) |
| 7.41e | 2026-07-30 | [picture](versions/7.41e/map.webp) | 2475 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | no object moved (the map file still changed) |
| 7.41d | 2026-06-04 | [picture](versions/7.41d/map.webp) | 2475 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | no object moved (the map file still changed) |
| 7.41c | 2026-05-06 | [picture](versions/7.41c/map.webp) | 2475 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | no object moved (the map file still changed) |
| 7.41b | 2026-04-07 | same file as 7.41a | 2475 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | the same map file |
| 7.41a | 2026-03-28 | [picture](versions/7.41a/map.webp) | 2475 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | trees +0 −1 |
| 7.41 | 2026-03-24 | [picture](versions/7.41/map.webp) | 2476 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | trees +324 −304; camps moved: 7; towers moved: 2; watchers moved: 3; lotus pools moved: 2; Tormentors moved: 2; twin gates moved: 2 |
| 7.40c | 2026-01-21 | [picture](versions/7.40c/map.webp) | 2456 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | no object moved (the map file still changed) |
| 7.40b | 2025-12-23 | same file as 7.40 | 2456 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | the same map file |
| 7.40 | 2025-12-15 | [picture](versions/7.40/map.webp) | 2456 | 28 | 22 | 2 | 10 | 2 | 2 | 2 | trees +239 −293; camps moved: 9; towers moved: 1; watchers +4 −8; wisdom shrines moved: 2 |
| 7.39e | 2025-10-02 | [picture](versions/7.39e/map.webp) | 2510 | 28 | 22 | 2 | 14 | 2 | 2 | 2 | no object moved (the map file still changed) |
| 7.39d | 2025-08-05 | [picture](versions/7.39d/map.webp) | 2510 | 28 | 22 | 2 | 14 | 2 | 2 | 2 | trees +0 −3 |
| 7.39c | 2025-06-24 | [picture](versions/7.39c/map.webp) | 2513 | 28 | 22 | 2 | 14 | 2 | 2 | 2 | watchers moved: 2 |
| 7.39b | 2025-05-29 | [picture](versions/7.39b/map.webp) | 2513 | 28 | 22 | 2 | 14 | 2 | 2 | 2 | trees +38 −27; camps moved: 2; towers moved: 1; watchers moved: 1 |
| 7.39 | 2025-05-21 | [picture](versions/7.39/map.webp) | 2502 | 28 | 22 | 2 | 14 | 2 | 2 | 2 | trees +290 −297; camps moved: 5; towers moved: 4; watchers moved: 1; lotus pools moved: 2; Roshan pits moved: 2; bounty runes moved: 1 |
| 7.38c | 2025-03-27 | [picture](versions/7.38c/map.webp) | 2509 | 28 | 22 | 2 | 14 | 2 | 2 | 2 | trees +152 −130; camps moved: 2; towers moved: 1; watchers moved: 1 |
| 7.38b | 2025-03-05 | [picture](versions/7.38b/map.webp) | 2487 | 28 | 22 | 2 | 14 | 2 | 2 | 2 | trees +2 −11 |
| 7.38 | 2025-02-19 | [picture](versions/7.38/map.webp) | 2496 | 28 | 22 | 2 | 14 | 2 | 2 | 2 | trees +1017 −1052; camps moved: 21; lotus pools moved: 2; twin gates moved: 2; Tormentors moved: 2; bounty runes moved: 2; wisdom shrines +2 −0; wisdom runes +0 −2; outposts +0 −2; watchers +14 −10; Roshan pits moved: 2 |
| 7.37e | 2024-11-19 | [picture](versions/7.37e/map.webp) | 2531 | 28 | 22 | 4 | 10 | 0 | 0 | 2 | no object moved (the map file still changed) |
| 7.37d | 2024-10-01 | [picture](versions/7.37d/map.webp) | 2531 | 28 | 22 | 4 | 10 | 0 | 0 | 2 | no object moved (the map file still changed) |
| 7.37c | 2024-08-28 | [picture](versions/7.37c/map.webp) | 2531 | 28 | 22 | 4 | 10 | 0 | 0 | 2 | no object moved (the map file still changed) |
| 7.37b | 2024-08-14 | same file as 7.36 | 2531 | 28 | 22 | 4 | 10 | 0 | 0 | 2 | the same map file |
| 7.37 | 2024-07-31 | same file as 7.36 | 2531 | 28 | 22 | 4 | 10 | 0 | 0 | 2 | the same map file |
| 7.36c | 2024-06-24 | same file as 7.36 | 2531 | 28 | 22 | 4 | 10 | 0 | 0 | 2 | the same map file |
| 7.36b | 2024-06-05 | same file as 7.36 | 2531 | 28 | 22 | 4 | 10 | 0 | 0 | 2 | the same map file |
| 7.36a | 2024-05-26 | same file as 7.36 | 2531 | 28 | 22 | 4 | 10 | 0 | 0 | 2 | the same map file |
| 7.36 | 2024-05-22 | [picture](versions/7.36/map.webp) | 2531 | 28 | 22 | 4 | 10 | 0 | 0 | 2 | no object moved (the map file still changed) |
| 7.35d | 2024-03-21 | same file as 7.35c | 2531 | 28 | 22 | 4 | 10 | 0 | 0 | 2 | the same map file |
| 7.35c | 2024-02-21 | [picture](versions/7.35c/map.webp) | 2531 | 28 | 22 | 4 | 10 | 0 | 0 | 2 | no object moved (the map file still changed) |
| 7.35b | 2023-12-21 | same file as 7.35 | 2531 | 28 | 22 | 4 | 10 | 0 | 0 | 2 | the same map file |
| 7.35 | 2023-12-14 | [picture](versions/7.35/map.webp) | 2531 | 28 | 22 | 4 | 10 | 0 | 0 | 2 | trees +0 −4; watchers +2 −0 |
| 7.34e | 2023-11-20 | same file as 7.34d | 2535 | 28 | 22 | 4 | 8 | 0 | 0 | 2 | the same map file |
| 7.34d | 2023-10-05 | [picture](versions/7.34d/map.webp) | 2535 | 28 | 22 | 4 | 8 | 0 | 0 | 2 | no object moved (the map file still changed) |
| 7.34c | 2023-09-08 | [picture](versions/7.34c/map.webp) | 2535 | 28 | 22 | 4 | 8 | 0 | 0 | 2 | no object moved (the map file still changed) |
| 7.34b | 2023-08-14 | same file as 7.34 | 2535 | 28 | 22 | 4 | 8 | 0 | 0 | 2 | the same map file |
| 7.34 | 2023-08-08 | [picture](versions/7.34/map.webp) | 2535 | 28 | 22 | 4 | 8 | 0 | 0 | 2 | trees +0 −1; outposts moved: 2; watchers moved: 4 |
| 7.33e | 2023-07-13 | same file as 7.33c | 2536 | 28 | 22 | 4 | 8 | 0 | 0 | 2 | the same map file |
| 7.33d | 2023-06-15 | same file as 7.33c | 2536 | 28 | 22 | 4 | 8 | 0 | 0 | 2 | the same map file |
| 7.33c | 2023-05-13 | [picture](versions/7.33c/map.webp) | 2536 | 28 | 22 | 4 | 8 | 0 | 0 | 2 | trees +57 −84 |
| 7.33b | 2023-04-25 | [picture](versions/7.33b/map.webp) | 2563 | 28 | 22 | 4 | 8 | 0 | 0 | 2 | no object moved (the map file still changed) |
| 7.33 | 2023-04-20 | [picture](versions/7.33/map.webp) | 2563 | 28 | 22 | 4 | 8 | 0 | 0 | 2 | trees +1838 −1578; camps +24 −12; camp tiers changed: 3; camp spawn boxes +24 −12; towers moved: 3; lotus pools +2 −0; twin gates +2 −0; Tormentors +2 −0; bounty runes moved: 2; wisdom runes +2 −0; outposts +4 −2; watchers +8 −0; Roshan pits +2 −1 |
| 7.32e | 2023-03-07 | [picture](versions/7.32e/map.webp) | 2303 | 16 | 22 | 2 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.32d | 2022-11-29 | same file as 7.32b | 2303 | 16 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.32c | 2022-09-27 | same file as 7.32b | 2303 | 16 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.32b | 2022-08-30 | rendering | 2303 | 16 | 22 | 2 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.32 | 2022-08-24 | rendering | 2303 | 16 | 22 | 2 | 0 | 0 | 0 | 0 | trees +57 −44; camps +0 −2; camp spawn boxes +1 −3; bounty runes moved: 1; outposts moved: 1 |
| 7.31d | 2022-06-08 | rendering | 2290 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.31c | 2022-05-04 | same file as 7.31 | 2290 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.31b | 2022-02-28 | same file as 7.31 | 2290 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.31 | 2022-02-23 | rendering | 2290 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | trees +4 −0; towers moved: 2; bounty runes moved: 2 |
| 7.30e | 2021-10-28 | same file as 7.29d | 2286 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.30d | 2021-09-25 | same file as 7.29d | 2286 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.30c | 2021-09-11 | same file as 7.29d | 2286 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.30b | 2021-08-23 | same file as 7.29d | 2286 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.30 | 2021-08-18 | same file as 7.29d | 2286 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.29d | 2021-05-24 | rendering | 2286 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.29c | 2021-04-29 | rendering | 2286 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | trees +6 −5 |
| 7.29b | 2021-04-16 | rendering | 2285 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | trees +5 −10 |
| 7.29 | 2021-04-09 | rendering | 2290 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | trees +734 −548; camps moved: 15; camp tiers changed: 2; camp spawn boxes changed: 16; towers moved: 5; bounty runes +1 −3; power runes moved: 2; outposts moved: 2 |
| 7.28c | 2021-02-19 | rendering | 2104 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.28b | 2021-01-10 | rendering | 2104 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.28a | 2020-12-22 | same file as 7.28 | 2104 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.28 | 2020-12-17 | rendering | 2104 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | trees +1 −3 |
| 7.27d | 2020-08-26 | same file as 7.27 | 2106 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.27c | 2020-07-17 | same file as 7.27 | 2106 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.27b | 2020-07-15 | same file as 7.27 | 2106 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.27a | 2020-07-04 | same file as 7.27 | 2106 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.27 | 2020-06-28 | rendering | 2106 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | trees +5 −6; camps moved: 1; camp tiers changed: 5; camp spawn boxes changed: 3 |
| 7.26c | 2020-05-02 | same file as 7.25 | 2107 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.26b | 2020-04-28 | same file as 7.25 | 2107 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.26a | 2020-04-21 | same file as 7.25 | 2107 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.26 | 2020-04-17 | same file as 7.25 | 2107 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.25c | 2020-04-06 | same file as 7.25 | 2107 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.25b | 2020-03-25 | same file as 7.25 | 2107 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.25a | 2020-03-18 | same file as 7.25 | 2107 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.25 | 2020-03-17 | rendering | 2107 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | trees moved: 4 |
| 7.24b | 2020-02-26 | rendering | 2107 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.24 | 2020-01-26 | rendering | 2107 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | trees +51 −46; camps moved: 1; camp spawn boxes changed: 1; bounty runes moved: 2; outposts moved: 2 |
| 7.23f | 2020-01-07 | rendering | 2102 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.23e | 2019-12-14 | rendering | 2102 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.23d | 2019-12-11 | same file as 7.23c | 2102 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.23c | 2019-12-06 | rendering | 2102 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.23b | 2019-11-29 | same file as 7.23 | 2102 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.23a | 2019-11-27 | same file as 7.23 | 2102 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | the same map file |
| 7.23 | 2019-11-26 | rendering | 2102 | 18 | 22 | 2 | 0 | 0 | 0 | 0 | trees +308 −414; camps moved: 9; camp tiers changed: 2; camp spawn boxes changed: 10; bounty runes moved: 4; power runes moved: 2; outposts +2 −0; Roshan pits moved: 1 |
| 7.22h | 2019-09-29 | same file as 7.22g | 2208 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.22g | 2019-09-06 | rendering | 2208 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.22f | 2019-07-28 | same file as 7.22 | 2208 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.22e | 2019-07-14 | same file as 7.22 | 2208 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.22d | 2019-06-30 | same file as 7.22 | 2208 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.22c | 2019-06-09 | same file as 7.22 | 2208 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.22b | 2019-05-27 | same file as 7.22 | 2208 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.22 | 2019-05-24 | rendering | 2208 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | trees +54 −53; camps moved: 3; camp spawn boxes changed: 5; towers moved: 1; bounty runes moved: 1 |
| 7.21d | 2019-03-24 | rendering | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.21c | 2019-03-02 | rendering | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.21b | 2019-02-16 | same file as 7.21 | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.21 | 2019-01-29 | rendering | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | camp tiers changed: 2 |
| 7.20e | 2018-12-09 | rendering | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.20d | 2018-11-30 | rendering | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.20c | 2018-11-24 | same file as 7.20b | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.20b | 2018-11-20 | rendering | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | camp spawn boxes changed: 1 |
| 7.20 | 2018-11-19 | rendering | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | trees +414 −412; camps moved: 11; camp tiers changed: 4; camp spawn boxes changed: 14; towers moved: 3; bounty runes moved: 2 |
| 7.19d | 2018-10-12 | same file as 7.19c | 2205 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.19c | 2018-09-14 | rendering | 2205 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.19b | 2018-09-01 | rendering | 2205 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.19 | 2018-07-29 | rendering | 2205 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | trees +2 −0 |
| 7.18 | 2018-06-25 | same file as 7.17 | 2203 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.17 | 2018-06-10 | rendering | 2203 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.16 | 2018-05-27 | same file as 7.15 | 2203 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.15 | 2018-05-10 | rendering | 2203 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | trees +1 −5; camp spawn boxes changed: 4; towers moved: 2; bounty runes moved: 1; power runes moved: 2 |
| 7.14 | 2018-04-26 | same file as 7.11 | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.13b | 2018-04-13 | same file as 7.11 | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.13 | 2018-04-12 | same file as 7.11 | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.12 | 2018-03-29 | same file as 7.11 | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.11 | 2018-03-15 | rendering | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | no object moved (the map file still changed) |
| 7.10 | 2018-03-01 | same file as 7.09 | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the same map file |
| 7.09 | 2018-02-15 | rendering | 2207 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | trees +2 −3; towers moved: 2 |
| 7.08 | 2018-02-01 | rendering | 2208 | 18 | 22 | 0 | 0 | 0 | 0 | 0 | the first map file of the history |
<!-- TABLE END -->

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
   object of interest is listed with its position; camp boxes come from their trigger hulls.

The scripts are in [sikleq/Sloppy](https://github.com/sikleq/Sloppy) — `scripts/gen/map_history.py`,
`scripts/gen/stitch_sfm.py`, `scripts/gen/mend_map.py`, `scripts/gen/extract_map_entities.py` — and the method is
written up in its `docs/terrain.md`. Sloppy's Terrain pages compare every patch's map with the one before it.

## Thanks

The idea and the inspiration come from the interactive maps of
[Leamare](https://github.com/leamare/dota-interactive-map) and
[devilesk](https://github.com/devilesk/dota-interactive-map). The renders, the data and the tooling here are our
own.

## License

Dota 2, its map and everything shown on it are © Valve Corporation. This is an unofficial fan project, not
affiliated with or endorsed by Valve. The tables and the scripts that build them may be used freely.
