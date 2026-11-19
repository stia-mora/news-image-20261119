# The World in One Page — 19 November 2026

A one-page newspaper front page summarising the world news of **Thursday,
19 November 2026**, drawn entirely in code (Python + Pillow, vector-style
shapes and system fonts — no photos, no AI-generated art).

## The six stories

1. **Welcome back to Vice City** — after 13 years, Grand Theft Auto VI
   unlocks at midnight in each market, starting in New Zealand; early
   reviews give it 99 on Metacritic. (Reuters)
2. **One light-day from home** — NASA confirms on 19 November that Voyager 1,
   launched in 1977, is now 16 billion miles away: light takes a full day
   to reach it. (NASA)
3. **A Van Gogh for $190.4m** — *Châtaigniers en fleurs* (1890) sets a new
   auction record for the artist at Sotheby's in New York, after a Nazi-era
   ownership dispute was settled. (Sotheby's / Artnet)
4. **Cyclone Akvan nears India** — the severe storm is forecast to cross the
   Andhra Pradesh–Odisha coast by noon on 20 November, with winds of
   90–100 km/h and heavy rain. (India Meteorological Department)
5. **EU plans €45bn Ukraine loan** — Brussels proposes a €45 billion loan to
   support Kyiv, to be repaid once Russia pays war reparations.
6. **Trump, Xi and Putin to meet** — the three leaders are set for
   trilateral talks in Shenzhen today, on the sidelines of the APEC summit.

All facts were checked against reporting published on 19 November 2026
(or, for the overnight stories, the evening of 18 November); nothing is
invented and forecasts are labelled as forecasts.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (`/output` by default).

To redraw the image from scratch:

```sh
python3 draw.py
```

## Files

- `entry.png` — the 1024×1024 entry image (< 1 MiB)
- `draw.py` — the script that draws it
- `main.ts` — copies `entry.png` to the output directory
