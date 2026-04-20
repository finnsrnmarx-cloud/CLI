# Can U Dig It? — Jane Street April 2026

An exploration archive for the April 2026 Jane Street monthly puzzle:
a 14×14 letter grid with one hyphen and instructions deliberately
*"drawn a blank"*.

> **Spoiler policy** — this repo intentionally does **not** contain the
> final numeric answer or the narrowed-down clue phrasing. It preserves
> the dead-ends and misleads so other solvers can enjoy the puzzle.

## Repo layout

```
.
├── LICENSE
├── README.md          (this file)
├── assets/            Official puzzle images
│   ├── can-u-dig-it.jpg
│   └── puzzle.png
├── docs/              Research notes, theories, candidate lists
│   ├── AI_HANDOFF.md
│   ├── CANDIDATES.md
│   ├── EXPERT_HANDOFF.md
│   ├── EXPLORATION_SUMMARY.md
│   ├── FINAL_REPORT.md
│   ├── GRID_VOCABULARY.md
│   ├── INTRODUCTION.md
│   ├── Jules_Findings_1.md
│   ├── Jules_Findings_2.md
│   ├── REVIEW.md
│   └── SUMMARY.md
├── web/               Interactive theory mindmaps
│   ├── mindmap.html   2D force-directed graph (vis-network)
│   └── mindmap3d.html 3D force-directed graph (Three.js)
└── scripts/           Exploratory Python analyses
    ├── exploration/   General grid analysis
    ├── image/         JPEG header / hex-byte experiments
    ├── snake/         Maze / snake-game interpretations
    ├── extract/       Word & phrase extraction
    └── solvers/       Theory-specific solvers
```

## The grid

```
r s d i f i n d t h s a r t
e h r e s o d a e e t g n a
n e t r h a l x h g o w i p
e g e d a u y u e a e n r p
p t n n m l l m x i d n e e
o h u i n k t h a n a c s m
a l n p f y l d e b s t t n
u u m j a r e b e m e h r w
m i t h d c e i g i u g t s
t l a m i b f t o t e g e t
s a i l n i i t n i a p e n
n s t o a g r n i i o b r t
i e t i r y e e s p r a y w
t u n e n t y - t e s s i x
```

## Theories explored (all ultimately rejected in this archive)

Each of the following was investigated in depth and documented in
`docs/`. All were dead-ends or partial misleads.

- **Axiom king-paths** — FIND THE START, STEP BY SIX, ADD THE
  HEXADECIMALS, THERE IS A DATE ON WIRE, LAST ENTRY ENTIRE INTEGER.
  Produced candidates 167, 2180, 2192, 2193 — all rejected.
- **Column-6 / U-column / Vanadium hex** — candidate 33.
- **TUNES / axiom-length / Gold** — candidate 79.
- **Dig count / missing V** — candidate 23.
- **Chemistry / aluminothermic reduction** — Al (13) + V (23) = 36.
- **Mozart / Köchel bridge** — row-14 "Tune 26" → K.184 / K.551 / K.626.
- **PWEI song** — Track 6, Alan Moore lyric, "dig" count.
- **JPEG image header hex analysis** — step-6 from various byte starts.
- **Snake / maze interpretations** — five axioms as moves.
- **Can-opener / perimeter strip** — inner 12×12 vs. border cells.
- **Solfège / phonetic decoding** — do-re-mi mappings.

## Failed submissions (do NOT re-submit)

```
600, 7, 3241, 3242, 26, 22, 134, 167, 2180, 2192, 2193
```

## Scripts

The Python scripts under `scripts/` are self-contained (no external
dependencies) and print their findings to stdout. Run any with:

```
python3 scripts/<subfolder>/<script>.py
```

## Web

`web/mindmap.html` and `web/mindmap3d.html` are single-file interactive
theory visualizers. Open either in a browser (they load vis-network /
three.js from CDN). Drag to pan/rotate, scroll to zoom, click a node
for details, use the star filter to hide low-confidence candidates.

## License

See `LICENSE`.
