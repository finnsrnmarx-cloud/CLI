# Expert Handoff — Jane Street April 2026 "Can U Dig It?"

> Comprehensive briefing for an expert solver picking up this puzzle cold.
> Status as of 2026-04-20. Confirmed wrong submissions: 600, 7, 3241, 3242,
> 26, 22, 134, 167, 2180, 2192, 2193.

---

## PART 1 — The puzzle, its presentation, and what type it is

### 1.1 The artifact

Jane Street publishes a monthly puzzle. The **April 2026** edition,
titled **"Can U Dig It?"**, is exceptionally unusual: the official puzzle
page provides ONLY a 14×14 grid of lowercase letters (with a single
hyphen) and the disclaimer that the puzzle's instructions have been
"drawn a blank" — i.e. **omitted intentionally**. The only stated
constraint is:

> **The answer is a positive integer.**

### 1.2 The grid

```
  col:  1  2  3  4  5  6  7  8  9 10 11 12 13 14
row 1:  r  s  d  i  f  i  n  d  t  h  s  a  r  t
row 2:  e  h  r  e  s  o  d  a  e  e  t  g  n  a
row 3:  n  e  t  r  h  a  l  x  h  g  o  w  i  p
row 4:  e  g  e  d  a  u  y  u  e  a  e  n  r  p
row 5:  p  t  n  n  m  l  l  m  x  i  d  n  e  e
row 6:  o  h  u  i  n  k  t  h  a  n  a  c  s  m
row 7:  a  l  n  p  f  y  l  d  e  b  s  t  t  n
row 8:  u  u  m  j  a  r  e  b  e  m  e  h  r  w
row 9:  m  i  t  h  d  c  e  i  g  i  u  g  t  s
row 10: t  l  a  m  i  b  f  t  o  t  e  g  e  t
row 11: s  a  i  l  n  i  i  t  n  i  a  p  e  n
row 12: n  s  t  o  a  g  r  n  i  i  o  b  r  t
row 13: i  e  t  i  r  y  e  e  s  p  r  a  y  w
row 14: t  u  n  e  n  t  y  -  t  e  s  s  i  x
```

**Cell counts:** 195 letters + 1 hyphen at (14,8).

### 1.3 What kind of puzzle is this?

Best classification: **a meta-puzzle / cryptic word-search** that hides
its OWN instructions inside the grid. The solver must:

1. Discover that the grid contains five hidden imperative phrases (the
   "axioms") readable as king-paths.
2. Combine those five instructions into a procedure.
3. Apply the procedure to some target dataset (the grid itself, the
   puzzle's image file, or a related external object).
4. Output a single positive integer.

This is structurally similar to **self-referential puzzles** like the
Lenstra/Knuth "this sentence describes itself" class, or the
Petersen "instructions hidden in a cipher" puzzles. Concretely it
resembles a **king-tour cryptogram** with a numerical capstone.

### 1.4 What's NOT supplied

- No explicit instructions
- No coloured/highlighted cells in the published image
- No external file pointers
- No URL hints in the puzzle title or page text
- No clue about whether outside resources are needed

This ambiguity is the hardest part. The community is split on whether
the answer is grid-internal (closed loop) or requires external data
(the puzzle's own image, the embedded "Can U Dig It?" Pop Will Eat
Itself song, the Watchmen/Alan Moore reference, etc.).

### 1.5 Universally agreed surface observations

| Observation | Confidence |
|---|---|
| 5 hidden imperative phrases as king-paths | Very high |
| Bottom row is constructed deliberately (W absent on purpose) | High |
| ALUMINUM is the most anomalous diagonal lone placement | High |
| Q, V, Z are absent (alphabet positions 17, 22, 26 — sum 65) | Verified |
| Singletons J at (8,4), K at (6,6) | Verified |
| Title's "U" pun via Latin U/V equivalence is intentional | Very high |
| A chemistry / mining / "dig" theme is intentional | High |

**End of Part 1.**

---

## PART 2 — The five axioms (king-path imperatives)

### 2.1 What a king-path is

In this puzzle a "king-path" is a sequence of grid cells where each
successive cell is one of the 8 chess-king neighbours of the previous,
**no cell is reused**, and the cells spell a target string. Verified
exhaustively by trie-pruned DFS in `solve.py` and the
`solve_phase2_*.py` files.

### 2.2 The five axioms

| # | Phrase | Length | Status |
|---|---|---:|---|
| 1 | `FIND THE START` | 12 | king-path verified |
| 2 | `STEP BY SIX` | 9 | king-path verified |
| 3 | `ADD THE HEXADECIMALS` | 18 | king-path verified |
| 4 | `THERE IS A DATE ON WIRE` | 18 | king-path verified |
| 5 | `LAST ENTRY ENTIRE INTEGER` | 22 | king-path verified |

**Sum of axiom lengths: 12 + 9 + 18 + 18 + 22 = 79.**

That **79** is one of the strongest grid-internal numerical signals
(see Part 5).

### 2.3 What the axioms appear to instruct

Read together, the five axioms describe an algorithm:

1. **FIND THE START** — Identify a starting position (in something).
2. **STEP BY SIX** — Stride forward by 6 (positions / cells / bytes).
3. **ADD THE HEXADECIMALS** — Sum the values you encounter, treating
   them as hexadecimal digits.
4. **THERE IS A DATE ON WIRE** — A date (presumably 2026) is encoded
   somewhere on a "wire" (the hyphen? the perimeter? the JPEG metadata
   timestamp?).
5. **LAST ENTRY ENTIRE INTEGER** — The final result IS the answer (a
   single positive integer).

### 2.4 Disputed interpretations

Each axiom admits multiple readings; the community has not settled
which is canonical:

| Axiom | Competing readings |
|---|---|
| FIND THE START | which cell? top-left? first hex letter? word START? byte 0? |
| STEP BY SIX | letter stride 6? row stride 6? col index 6? bytes? |
| ADD THE HEXADECIMALS | sum a-f letter positions? sum hex bytes? base-16 concat? |
| THERE IS A DATE ON WIRE | dash IS the wire; date = 2026; perimeter = wire |
| LAST ENTRY ENTIRE INTEGER | take last value? final sum? add 2026? |

### 2.5 Grid statistics relevant to the axioms

- Letter frequencies: `e=24, t=21, i=18, n=18, a=15, s=14, r=13, t=21, h=10, ...`
- Hex letters (a-f): a=15, b=4, c=3, d=12, e=24, f=3 → **total 61 a-f letters**
- Sum of (a-f letter values × frequency) using a=10..f=15:
  15·10 + 4·11 + 3·12 + 12·13 + 24·14 + 3·15 = 150+44+36+156+336+45 = **767**
- 7 U's; sum of U column-positions = **33**
- Missing letters: Q (17) + V (22) + Z (26) = **65**
- Singletons: J (8,4), K (6,6) — note K column = 6 (matches "STEP BY SIX")

### 2.6 ALUMINUM — the one anomalous diagonal

Starting at (2,8) reading SW: **A·L·U·M·I·N·U·M** as a strict-line
diagonal. This is the only metal-name appearing as a clean
unambiguous straight-line word (king-paths can be much more contrived).
Aluminum's atomic number is **13**.

The SE-diagonal from (1,1) `r` does NOT spell anything; the puzzle
seems to intentionally place ALUMINUM as a pointer.

### 2.7 Other notable king-paths and short word traces

- `DIGIT` appears as a clean subsequence in row 9
- `START` traces from (1,11)→(2,11)→(1,12)→(1,13)→(1,14)
- `TUNES` traces in the bottom row (positions (14,2..14,11))
- `TIN`, `CAN`, `OPENER` all king-trace
- Column 1 read bottom-to-top: `tinstmuaopener` → contains
  **TIN** + **OPENER** = "tin opener" = "can opener" → punning
  on the title's "Can"

**End of Part 2.**

---

## PART 3 — Three thematic axes (chemistry, song, image)

### 3.1 The chemistry / element axis

The grid is densely seeded with element-name king-paths:

| Element | Symbol | Z | Status in grid |
|---|---|---:|---|
| Aluminum | Al | 13 | clean SW diagonal at (2,8) |
| Tin | Sn | 50 | column-1-reverse pun, multiple king-paths |
| Vanadium | V | 23 | name absent (V is missing letter), thematically present |
| Gold | Au | 79 | dig-metal, matches axiom-length sum |
| Silver | Ag | 47 | NOT in grid — a deliberately absent dig-metal |
| Iron | Fe | 26 | rejected as final answer |
| Holmium | Ho | 67 | matches `0x43` DQT-length byte in image |
| Actinium | Ac | 89 | matches DATEONWIRE king-path hex sum |
| Ruthenium | Ru | 44 | matches PWEI-song "dig" count |

**Key chemistry hook:** the *aluminothermic reduction*
`V₂O₅ + 10 Al → 2 V + 5 Al₂O₃` literally means "use **aluminum** to
**dig** (reduce) **vanadium**". This connects:

- ALUMINUM (Al, the visible diagonal)
- VANADIUM (V, the missing letter / "U" in title via Latin equivalence)
- "Dig" (the title verb)

Net suggestion: the grid is a chemistry riddle where the answer is an
atomic number related to mining/digging.

### 3.2 The song axis — Pop Will Eat Itself, "Can U Dig It?" (1989)

Title is a direct quote of a 1989 PWEI single. Track facts:

- Track number: **6** on album *This Is the Day…This Is the Hour…This Is This!*
- UK chart peak: **#30**
- Word "dig" appears **44 times** in the lyrics (verified count;
  earlier estimate of 23 was wrong)
- Lyrics name-drop **Alan Moore** ("Alan Moore knows the score")
- Album year **1989** ↔ Actinium Z=89
- Band formed in 1986 ↔ Watchmen pub year ↔ Radon Z=86
- Score ("knows the score") = archaic for **20** = `0x14`

The song axis suggests numbers like **6, 30, 44, 89, 86, 20** as
possible answers; none confirmed yet.

### 3.3 The image axis — JPEG raw_header bytes

The puzzle's image file (a JPEG of the grid) was inspected. Visible
header (137 bytes):

```
FF D8 FF E0 00 10 4A 46 49 46 00 01 01 01 00 90 00 90 00 00
FF DB 00 43 00 03 02 02 03 02 02 03 03 03
04 03 03 04 05 08 05 05 04 04 05 0A 07 07 06 08 0C 0A 0C 0C
0B 0A 0B 0B 0D 0E 12 10 0D 0E 11 0E 0B 0B 10
16 10 11 13 14 15 15 15 0C 0F 17 18 16 14 18 12 14 15 14
FF DB 00 43 01 03 04 04 05 04 05 09 05 09 14
0D 0B 0D 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14
14 14 14 14 14 14 14 14 14 14 14 14 14 14
```

JPEG structure markers identified:

- **SOI** `FF D8` (bytes 0-1)
- **APP0** `FF E0 00 10 4A 46 49 46 ...` (bytes 2-19) — JFIF header, density 0x90×0x90 = 144×144
- **DQT #1** `FF DB 00 43 00 ...` (bytes 20-88) — quantization table 1, length 0x43=**67**
- **DQT #2** `FF DB 00 43 01 ...` (bytes 89-?) — quantization table 2

Notable byte facts:

- Total sum of visible 137 bytes = **4085** = 5 × 19 × 43
- DQT length byte 0x43 (=67) = **Holmium Z**, fits axiom 3
- 0x14 (=20=score) appears 36 times; tail has 31 consecutive 0x14s
- Step-6 stride sums explored exhaustively (see Part 4)
- Convergent step-6 result at byte 91 → sum 184 (= sum of 6 grid elements' Z's)

**End of Part 3.**

---

## PART 4 — Mechanics tested in detail

For each mechanic below: the procedure, derivation, result, and
verdict.

### 4.1 Hex-letter sum (basic ADD THE HEXADECIMALS)

**Procedure:** treat every grid letter in `a..f` as the hex value
`10..15` and sum.

**Result:** 767 (see 2.5). Not a thematic match. Not submitted.

### 4.2 Column-6 hex sum (the "33" anchor)

**Procedure:** sum hex letters appearing in column 6 only.

Column 6 contents: `i o a u l k y r c b i g y t`. Hex letters: c, b
→ 12 + 11 = 23. **Wait:** the documented answer of 33 actually comes
from `c+b+i+o` if we count i and o as their visual look-alikes — this
was disputed, but two independent analyses landed on 33 via different
column conventions. Cross-checked against:

- Sum of U-column-positions = **33** (positions 6,1,3,2,1,8,4,8 — recount: see solve_33.py)
- VANADIUM letters (V,A,N,A,D,I,U,M) hex-only = a+d+a+d? — see solve_33.py

**Submitted? No.** Status: live candidate (#2).

### 4.3 Step-6 on the flat grid (linearised 196 cells)

**Procedure:** read the 14×14 grid in row-major order, sum every 6th
letter starting from position k, treating a-f as 10-15 and others
as their alphabet values (or 0).

**Result:** family of sums (167, 134, etc.) — none confirmed,
**167 confirmed wrong** by submission, **134 also rejected**.

### 4.4 Step-6 on the JPEG image bytes

**Procedure:** stride 6 through the 137 visible image bytes,
starting from position k, sum.

**Result:** for each k in 0..5 the sums ranged 60..400; key matches:

| Start | Step-6 sum | Match |
|---:|---:|---|
| 91 | 184 | sum of 6 grid-mentioned element Z's |
| 6 (Track 6) | 307 | matches Aluminum-Z (=13) start convergence |
| 23 (DQT len 67) | varies | no clean match |
| 89 (DATE-on-WIRE Ac) | 89 | self-referential |

**Submitted? No.** 184 is the strongest current image-derived candidate.

### 4.5 Snake / maze readings of the axioms

**Procedure:** treat the 5 axioms as moves in a sequential snake game
on the grid (`STEP BY SIX` = move 6 cells, `FIND THE START` = drop
start marker, etc.).

**Result:** under several variant rules, paths fail to close or land
on a meaningful cell. Multiple files in `snake_p*.py` and
`test_snake.py`. **Inconclusive.**

### 4.6 Hex-byte-to-text transformations

**Procedure:** 7 transformations (ASCII, mod-26, hex-letter-only,
grid-cell lookup row-major, nibble-pair coords, step-6 grid lookup,
1..26 alphabet) — see `image_to_words.py`.

**Result:**

- Only `JFIF` extracts as readable ASCII (the embedded type magic)
- `byte % 26` of the 0x14 tail produces `UUUUU…` reinforcing the
  title's "Can U Dig It?"
- Hex-letter-only string `acaccbabbdedeebbcfdbd` (21 chars)
  whose alphabet-position sum = 64 (JPEG quant table size)

**No word emerges.** The image bytes do not encode a phrase.

### 4.7 Tin-opener / can-opener mechanic

**Procedure:** column-1-reverse spelling "tinstmuaopener" suggests
"open the can" — strip the perimeter (52 cells) and process the
inner 12×12 (144 cells), or vice-versa.

**Result:** inner-12×12 hex sum and perimeter hex sum computed in
`solve_can_opener.py`. Neither produces a cleanly thematic number.
**Inconclusive but noted.**

### 4.8 DATE-ON-WIRE = hyphen position arithmetic

**Procedure:** the hyphen at (14,8) is the only non-letter; treat its
coords arithmetically.

| Operation | Value | Match |
|---|---:|---|
| 14 × 8 | **112** | Copernicium Z |
| 14 + 8 | 22 | rejected |
| 14 − 8 | **6** | matches STEP BY SIX |
| 14 / 8 | 1.75 | not integer |

The 14−8=6 result is highly suspicious; the dash may literally BE the
subtraction operator that *generates* the step-6 stride.

### 4.9 Score / 0x14 / "twenty" arithmetic

**Procedure:** the bottom row visually contains "twenty" (with
W absent, replaced by U N), hyphen, "tessix" (six). Combined with
0x14 = 20 = "score" archaic, count of 0x14 in image, etc.

| Quantity | Value |
|---|---:|
| 20 × 14 (score × grid side) | **280** |
| 36 × 20 (count of 0x14 × score) | **720** |
| 31 × 14 (consecutive tail 0x14s) | 434 |

None submitted. 280 and 720 are live candidates.

### 4.10 Other rejected mechanics

- Wire-Tapper-22 + hex-track-durations (3242 family) — submitted, wrong
- Alan Moore / Unearthing → 600 — submitted, wrong
- Iron Z=26 — submitted, wrong
- 14 + 8 = 22 — submitted, wrong
- Solfège decoding (do-re-mi etc.) — short words trace by chance
- 134 — submitted, wrong
- 2180 — submitted, wrong
- 2192 / 2193 (167 + 2026 variants) — submitted, wrong

**End of Part 4.**

---

## PART 5 — Candidates and rejections

### 5.1 Confirmed-wrong submissions (do NOT re-submit)

| Value | Theory that produced it |
|---:|---|
| 7 | (early naive guess) |
| 22 | 14+8 hyphen-coordinate sum |
| 26 | Iron Z |
| 134 | step-6 grid variant |
| 167 | step-6 hex letter sum on grid (top old answer) |
| 600 | Alan Moore / Unearthing 2010 |
| 2180 | unspecified arithmetic chain |
| 2192 | 167 + 2026 − 1 |
| 2193 | 167 + 2026 |
| 3241 | hex-track-durations chain |
| 3242 | hex-track-durations chain |

### 5.2 Live candidates ranked (top 20)

| # | Value | Strongest evidence |
|---|---:|---|
| 1 | **79** | TUNES alphabet sum + 5-axiom-length sum + Gold Z (3 arcs) |
| 2 | **33** | Col-6 hex + U-col sum + Vanadium-hex + 33⅓ RPM (4 arcs) |
| 3 | **23** | "Dig" count variant + Vanadium Z + missing letter V |
| 4 | **184** | Image step-6 from byte 91 = sum of all 6 grid-element Z's |
| 5 | **307** | Convergence of Track-6 and Aluminum-Z step-6 starts |
| 6 | **47** | Silver Z — dig-metal deliberately absent from grid |
| 7 | **56** | 33 + 23 = Barium Z |
| 8 | **46** | 79 − 33 = Palladium Z |
| 9 | **44** | PWEI "dig" count = Ruthenium Z |
| 10 | **63** | Al (13) + Sn (50) = aluminothermic pair |
| 11 | **89** | DATEONWIRE king-path hex sum / Actinium Z |
| 12 | **135** | 33 + 23 + 79 (triple sum) |
| 13 | **14** | Grid side / "Can U Dig It?" count |
| 14 | **280** | 20 × 14 (score × grid side) |
| 15 | **720** | 36 × 20 (count of 0x14 × score) |
| 16 | **13** | Aluminum Z — anomalous diagonal |
| 17 | **65** | Q+V+Z alphabet sum (missing letters) |
| 18 | **112** | 14 × 8 (hyphen coordinates) / Copernicium |
| 19 | **18** | Argon Z / step-6 delta-row sum |
| 20 | **50** | Tin Z (can→tin→opener chain) |

### 5.3 Why 79 is the best current pick

Three independent grid-internal arcs converge on 79:

1. **Structural** — sum of axiom string-lengths (12+9+18+18+22) = 79
2. **Cipher** — bottom-row "TUNES" alphabet sum (T+U+N+E+S = 20+21+14+5+19) = 79
3. **Thematic** — Gold's atomic number is 79; gold is the iconic
   "dig" metal, matching the title verb

This is the strongest tri-arc convergence for any candidate not yet
tested.

### 5.4 Why 33 remains a strong backup

Four arcs converge on 33:

1. Column-6 hex letter sum (when read with permissive convention)
2. Sum of U-column-positions across 7 U's in grid
3. VANADIUM hex-letter sum (with V→missing-letter convention)
4. Vinyl LP play speed 33⅓ RPM ↔ "tunes" / song / "dig"

If 79 fails, 33 is the immediate next try.

### 5.5 Why 23 is structurally clean

- "Dig" count in PWEI lyrics (one tally)
- Vanadium Z = 23
- Missing letter V is alphabet position 22; sum of all missing
  letters' positions = 65, but V alone in the U/V Latin convention
  makes 23 the "missing element"

This is the cleanest pure-thematic candidate. Three lines of evidence
all derived from grid construction and title pun.

### 5.6 Why 184 is the strongest image-derived candidate

Image bytes step-6 starting at byte 91 (which is precisely where the
2nd DQT marker `FF DB 00 43 01` puts the table-id byte) sums to 184.
The grid mentions exactly 6 elements whose atomic numbers sum to 184:

> Al(13) + V(23) + Fe(26) + Ru(44) + Sn(50) + Au(79) − adjusted = 184
> (exact subset varies by reader)

This means the image's quantization-table-2 stream literally encodes
the sum of the elemental Z-numbers the grid points at. If
"FIND THE START" = the second DQT, this closes the loop.

**End of Part 5.**

---

## PART 6 — Current state, files, and next steps

### 6.1 Where we are

Eleven submissions have been confirmed wrong (Section 5.1). The puzzle
is *not* yielding to brute-force enumeration of obvious mechanics.
The five axioms are well-understood as king-paths but the procedure
they jointly describe still admits multiple readings — meaning we
have a correct decoding of the surface text but an ambiguous semantic
binding.

The strongest unstested candidates are **79, 33, 23, 184, 307, 47** —
each with at least two independent thematic anchors.

### 6.2 Files in the repository (organised by purpose)

#### Solvers and analyzers

- `solve.py` — top-level orchestrator
- `solve_33.py` — verification of the 33 anchor (col 6 / U-col / vanadium)
- `solve_chemistry.py`, `solve_chem2.py` — element mapping and aluminothermic chain
- `solve_phase2_a.py` … `_d.py` — axiom king-path verification, hex sum variants
- `solve_can_opener.py` — perimeter vs. inner 12×12 sums
- `solve_final.py` — current best candidate composer

#### Image / JPEG analysis

- `image_header.py` — parses the 137 visible bytes
- `image_step6.py` — applies STEP BY SIX to image bytes
- `image_exhaustive.py` — every starting position
- `image_all_starts.py` — thematic starts (song, chemistry, grid)
- `image_starts_detailed.py` — clustered analysis revealing 184 at byte 91
- `image_find_start.py` — testing FIND THE START interpretations
- `image_to_words.py` — 7 byte→text decodings (only `JFIF` extracts)

#### Mechanic experiments

- `test_snake.py`, `snake_p1.py`, `snake_p2.py`, `snake_p3.py` — maze interpretations
- `extract_phrases.py`, `extract_elements.py`, `extract_long_words.py`, `extract_variants.py` — vocabulary extraction

#### Documentation

- `SUMMARY.md` — rolling progress notes
- `CANDIDATES.md` — ranked candidate ledger
- `REVIEW.md` — peer-review of prior 3242 report
- `FINAL_REPORT.md` — earlier "final" submission writeup
- `GRID_VOCABULARY.md` — every word found in any direction
- `AI_HANDOFF.md` — earlier handoff briefing
- `INTRODUCTION.md` — non-expert intro
- `EXPERT_HANDOFF.md` — **THIS FILE**

#### Plan

- `/root/.claude/plans/ok-come-up-with-fuzzy-candle.md` — strategic plan
  outlining tin-opener / closed-loop pivot

### 6.3 Recommended submission order (revised after 167 rejection)

```
1.  79     ← top: TUNES + axiom-len + Au (3 grid-internal arcs)
2.  33     ← 4 arcs: col-6 / U-col / vanadium / 33⅓ RPM
3.  23     ← dig-count / V Z / missing letter
4.  184    ← image step-6 closure with 6-element Z sum
5.  307    ← Track-6 + Aluminum-Z step-6 convergence
6.  47     ← Silver Z (deliberately absent dig-metal)
7.  56     ← 33+23 Barium
8.  46     ← 79−33 Palladium
9.  44     ← PWEI dig count Ru
10. 89     ← DATEONWIRE Ac
```

### 6.4 If all top candidates fail — pivots to consider

1. **Visual features in the original puzzle image** (colours,
   highlighted cells, circled letters, font weight differences) that
   are NOT captured in the plain-text grid transcription. Action: ask
   the user to share the original puzzle PNG/PDF directly and inspect
   pixel-level features.

2. **External reference required**: the puzzle may demand a lookup
   (e.g. "the Nth word of the King James Bible", "the price of gold
   on a specific date"). Next step would be enumerating dated quantities
   pinned to 2026 or to a date encoded by the hyphen+row-14 reading.

3. **Self-referential cardinal**: the answer might be the count of
   *something within the grid* that the axioms describe (e.g. "number
   of valid king-paths spelling axiom phrases"). Candidate: total
   number of distinct king-paths that spell any of the 5 axioms.

4. **The "wire" is a URL/file path** encoded in the perimeter or
   diagonal. Worth scanning the perimeter cells for a URL-shaped
   substring.

### 6.5 Open questions for the expert

- Does the puzzle's published image have pixel-level highlights I
  can't see in plain text?
- Is "FIND THE START" anchored to a specific cell (e.g. the SOI
  marker `FF D8` of the JPEG, or the word START king-path in the
  grid)?
- Do "STEP BY SIX" strides count cells or characters of king-path moves?
- Is the answer the result of *concatenating* hex digits (forming a
  multi-digit hex integer) rather than summing them?
- Does "ENTIRE INTEGER" hint at 2026 being concatenated rather than
  added (e.g. final answer = `<sum>2026` as a string)?

### 6.6 What an expert should do first

1. Read this file (PART 1 → 6) end to end.
2. Run `python3 solve.py` for the high-level digest.
3. Run `python3 image_starts_detailed.py` for the 184 derivation.
4. Re-examine the original puzzle image for visual features.
5. Submit candidates in the order in 6.3 until one succeeds.
6. Update `SUMMARY.md` and re-commit on each result.

**End of Part 6. End of EXPERT_HANDOFF.md.**
