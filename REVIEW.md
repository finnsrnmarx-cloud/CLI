# Comprehensive Review — Jane Street April 2026 "Can U Dig It?" Puzzle

## The puzzle (facts)

- 14×14 grid of lowercase letters plus **one hyphen at (14,8)**
- Title: "Can U Dig It?" (capital U emphasized)
- Stated: "the answer is a positive integer"
- No other instructions given on the page

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

## Grid statistics (established)

- 195 letters + 1 hyphen
- Missing from alphabet: **Q, V, Z** (alphabet positions 17, 22, 26)
- Letters appearing only once: **J at (8,4)**, **K at (6,6)**
- Frequencies: e=24, t=21, i=18, n=18, a=15, r=11, s=11, h=8, d=g=l=m=u=7, o=p=6, y=5, b=4, f=w=x=3, c=2, j=k=1

## Confirmed rejected answers

| # | Derivation | Why it failed |
|---|---|---|
| **600** | Alan Moore's *Unearthing* essay (2006/2010), claimed via title → PWEI song → "Alan Moore knows the score" | MOORE doesn't trace in the grid; depends on external music-trivia chain |
| **7** | Count of U's in the grid | Too trivial; doesn't use the 14×14 structure |
| **3241 / 3242** | Wire Tapper 22 tracks 1/7/13/19 hex durations summed with one decimal exception | Track times aren't inherently hex; hex/decimal switch for "last entry" is ad-hoc; Vol-22 is external trivia |
| **26** | Bottom row visually reads "twenty-six" | Too obvious; the grid doesn't literally spell TWENTY as a subseq anywhere; bottom row is decoration |
| **22** | V's alphabet position or hyphen (14,8) → 14+8 | No supporting structure |

## Theories evaluated

### Theory A — 5 Axioms + Wire Tapper 22 (rejected family)

The 5 instruction phrases all trace in the grid as king-move paths:

| Phrase | Cells | Paths |
|---|---|---|
| FIND THE START | 12 | 1 |
| ADD THE HEXADECIMALS | 18 | 4 |
| STEP BY SIX | 9 | 3 |
| THERE IS A DATE ON WIRE | 18 | 2 |
| LAST ENTRY ENTIRE INTEGER | **22** | **1** |

The 22-character phrase tracing as a single unique king path is strong evidence of intent. Applying them to **WT22** as dataset produced 3242 (wrong).

**Conclusion:** the mechanic is real, the dataset is wrong.

### Theory B — Self-contained hex chain (2180 / 2193)

Start somewhere, step by 6 through the flat grid, sum hex-digit letters (a–f → 10–15), add 2026 (bottom row as year).

**Exhaustive verification of all starting positions:**

| Start | Cell | Hex letters hit | Hex sum | +2026 |
|---|---|---|---:|---:|
| flat[2] | d (1,3) — **FIRST HEX LETTER in grid** | — | **167** | **2193** |
| flat[8] | t (1,9) | edeeeaeedaea | **154** | **2180** |
| flat[14] | e (2,1) | — | 154 | 2180 |
| flat[24] | t (2,11) | edaaaefeae | 124 | 2150 |
| flat[30] | t (3,3) | edaaaefeae | 124 | 2150 |
| flat[57] | t (5,2) | ecbbcab | 81 | 2107 |
| flat[76] | t (6,7) | feeee | 71 | 2097 |
| flat[114] | t (9,3) | feae | 53 | 2079 |
| flat[167] | t (12,14) | ae | 24 | 2050 |

**Key principled interpretation:**
- "FIND THE START" → start of *the hexadecimals* → first a-f letter in reading order = `d` at (1,3)
- "STEP BY SIX" → stride 6 through the flat grid
- "ADD THE HEXADECIMALS" → sum a-f letter values along the way → 167
- "LAST ENTRY ENTIRE INTEGER" → add 2026 (bottom row year)
- **Answer: 167 + 2026 = 2193**

2193 is arguably more defensible than 2180 because its starting position has a rule ("first hex letter"), not an arbitrary t-choice.

**Total hex letters (a-f) in entire grid: 55, sum = 690.** If FIND THE START means "sum ALL hex letters":
- 690 + 2026 = **2716**
- 690 + 26 = 716

### Theory C — Element / metal ("dig for metals")

Only **two** element names trace as clean straight lines:
- **ALUMINUM (Z=13)** at (2,8)→SW — the grid's single 8-letter unique placement
- **TIN (Z=50)** at (12,3)→SE

Others trace only as king paths: **IRON (26), NEON (10), ARGON (18), HOLMIUM (67)**.

Key candidate: **63 = 13 + 50**

### Theory D — TUNES = GOLD (★ strongest thematic fit)

The bottom row `tunenty-tessix` visually = "twenty-six" with 5 extra letters inserted that anagram to **TUNES**:

- T(20) + U(21) + N(14) + E(5) + S(19) = **79**
- **Atomic number of Gold (Au) is exactly 79**
- Gold is the iconic metal humans **dig** for
- Ties together: title ("dig"), grid theme (metals), bottom row (TUNES extras)

### Theory E — Hidden Roman numerals

"tessix" ends in `ix` = **Roman IX = 9**. Bottom row reads as "twenty + IX" = **29**.

### Theory F — Alternate hex cipher

If "hexadecimal" means converting alphabet position to hex, J–O become the "teen" digits (10–15):
- J=1, K=1, L=7, M=7, N=18, O=6 in grid → **40** total cells

### Grid-internal cross-checks

| Observation | Where | Interpretation |
|---|---|---|
| DIGIT in row 9 as clean subseq | title match | thematic anchor |
| OPENER in col 1 reversed (top 6) | corner | striking but unused |
| HEXAGON in col 9 | supports HEX theme | |
| TWENTY doesn't trace anywhere | no matching W adjacency | bottom row is decoration |
| Only J at (8,4), only K at (6,6) | unique letters | candidate markers |

## Ranked candidate answers (not yet rejected)

| Rank | Answer | Derivation | Confidence |
|---:|---:|---|:---:|
| 1 | **2193** | 167 + 2026; start at FIRST HEX LETTER in grid (most principled) | ★★★★ |
| 2 | **79** | TUNES = Au (Gold) atomic number; self-contained dig-theme | ★★★★ |
| 3 | **2180** | Gemini's verified step-6 from t@(1,9) + 2026 | ★★★ |
| 4 | **63** | Al + Sn (only two straight-line elements) | ★★★ |
| 5 | **2105** | 2026 + 79 (year + Gold) | ★★★ |
| 6 | **2716** | 690 + 2026 (sum of ALL hex letters + year) | ★★★ |
| 7 | **2089** | 2026 + 63 (year + Al+Sn) | ★★ |
| 8 | **29** | Roman IX reading ("twenty + 9") | ★★ |
| 9 | **2150** | step-6 from other t-positions + 2026 | ★★ |
| 10 | **167** | hex sum alone, no year add | ★★ |
| 11 | **154** | hex sum alone, t-start | ★★ |
| 12 | **254** | Fe (iron) hex symbol 0xFE | ★ |
| 13 | **142** | Al+Sn+Au triad (13+50+79) | ★ |
| 14 | **2055** | 2026 + 29 | ★ |
| 15 | **690** | Sum of all a-f letters in grid | ★ |
| 16 | **40** | Alt-hex J–O count | ★ |
| 17 | **538** | Alt-hex J–O weighted sum | ★ |
| 18 | **2395** | Axiom-path hex sum + 2026 | ★ |
| 19 | **14** | T in alt hex / grid size | — |
| 20 | **50, 13** | TIN alone / Al alone | — |

## Recommended trial order

```
2193 → 79 → 2180 → 63 → 2105 → 2716 → 2089 → 29 → 167 → 154 → 2150
```

## Fallback plan if all fail

If all grid-internal candidates fail, the issue is likely that the original puzzle image has visual features not captured in the text transcription — highlighted cells, colour differences, circled letters, or an overlay. At that point, we'd need the original image.

## Solver files in this repo

- `solve.py` — main overview solver with candidates summary
- `solve_kingpaths.py` — trie-pruned king-path English word search
- `solve_final.py` — theme-word counts across all 8 directions
- `solve_elements.py` — periodic-table element name search
- `solve_instructions.py` — exhaustive instruction-phrase catalogue
- `solve_snake.py` — combined-mechanic (axiom paths + step-6 + hex)
- `solve_phonetic.py` — Roman-numeral / TUNES-as-Gold / element-hex analysis
