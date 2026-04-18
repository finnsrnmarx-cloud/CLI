# Introduction — Jane Street April 2026 "Can U Dig It?"

## What the puzzle is

Jane Street, a quantitative trading firm, publishes a puzzle every
month. Their April 2026 entry is titled **"Can U Dig It?"** — a
reference to the 1989 Pop Will Eat Itself song which itself samples
the 1979 film *The Warriors*. The puzzle's capitalised **U** is
visually emphasised.

The puzzle page gives you a 14×14 grid of lowercase letters with
exactly one hyphen, and a single line of text:

> *"(Apologies, but we've drawn a blank with this puzzle's
> instructions. One thing we do know is that the answer is a
> positive integer…)"*

That's the whole prompt. No rules, no target, no grid legend —
just the grid and a positive-integer constraint. The solver has to
figure out both **what the puzzle is asking** AND **how to compute
the answer** from the grid alone.

## The grid

```
 1  r s d i f i n d t h s a r t
 2  e h r e s o d a e e t g n a
 3  n e t r h a l x h g o w i p
 4  e g e d a u y u e a e n r p
 5  p t n n m l l m x i d n e e
 6  o h u i n k t h a n a c s m
 7  a l n p f y l d e b s t t n
 8  u u m j a r e b e m e h r w
 9  m i t h d c e i g i u g t s
10  t l a m i b f t o t e g e t
11  s a i l n i i t n i a p e n
12  n s t o a g r n i i o b r t
13  i e t i r y e e s p r a y w
14  t u n e n t y - t e s s i x
```

The one hyphen sits at position **(14, 8)** — the 8th cell of the
bottom row. The grid has 195 letters + 1 hyphen = 196 cells.

## First impressions

Several things jump out immediately:

1. **The bottom row** (`tunenty-tessix`) visually resembles
   "twenty-six" — a wink at the year 2026.
2. The grid **excludes three letters**: Q, V, and Z.
3. Two letters appear only once: **J** at (8,4) and **K** at (6,6).
4. The title emphasises **U** — and there are exactly 7 U's in the grid.
5. The answer must be a positive integer, but we're given no
   arithmetic operation.

The rest of this introduction explains how the solver's community
(and this analysis) unpacked the puzzle.

---

## The core mechanic — king-path tracing

The grid contains hidden English sentences that trace as **king-move
paths**: you can walk 8 directions (horizontal, vertical, diagonal),
one cell at a time, without reusing any cell. Chess-king rules on a
14×14 board.

When you search the grid that way, five long phrases emerge that
look like operational instructions. They are not random — their
length and grammatical coherence makes incidental occurrence
astronomically unlikely.

## The 5 hidden instruction "axioms"

### 1. FIND THE START (12 letters, 1 unique king-path)

Path: (1,5)→(1,6)→(1,7)→(1,8)→(1,9)→(1,10)→(2,10)→(1,11)→(2,11)
→(1,12)→(1,13)→(1,14). Mostly runs along row 1, reading the
letters `findthestart` directly.

### 2. ADD THE HEXADECIMALS (18 letters, 4 king-paths)

Path example: (2,8)→(2,7)→(1,8)→(1,9)→(1,10)→(2,9)→(3,9)→(4,9)
→(5,9)→(6,9)→(7,8)→(8,7)→(9,6)→(10,5)→(10,4)→(10,3)→(10,2)
→(11,1). Sweeps diagonally across the grid from top-right to
bottom-left.

### 3. STEP BY SIX (9 letters, 3 king-paths)

Path: (9,14)→(9,13)→(10,13)→(11,12)→(12,12)→(13,13)→(14,12)
→(14,13)→(14,14). Lives entirely in the bottom-right corner and
ends with the word `six` in the last row.

### 4. THERE IS A DATE ON WIRE (18 letters, 2 king-paths)

Path: (3,3)→(2,2)→(3,2)→(2,3)→(2,4)→(1,4)→(2,5)→(3,6)→(2,7)
→(2,8)→(1,9)→(2,10)→(3,11)→(4,12)→(3,12)→(3,13)→(4,13)→(5,13).
Wanders through the top five rows of the grid.

### 5. LAST ENTRY ENTIRE INTEGER (22 letters, 1 unique king-path)

Path: (10,2)→(11,2)→(12,2)→(13,3)→(14,4)→(14,5)→(14,6)→(13,5)
→(13,6)→(13,7)→(12,8)→(11,8)→(11,7)→(12,7)→(13,8)→(12,9)
→(11,9)→(10,10)→(10,11)→(10,12)→(11,13)→(12,13). A 22-cell
complex path through the bottom half. The longest and most
convincing of the five.

## How the 5 axioms are spatially organised

When you draw all five paths on the grid at once, they cluster
into three zones:

- **Rows 1-5 (top)** — FIND THE START + THERE IS A DATE ON WIRE.
  This is the "setup / discovery" zone.
- **Row 6 is a threshold** — only ADD THE HEXADECIMALS crosses it.
- **Rows 9-14 (bottom)** — STEP BY SIX + LAST ENTRY ENTIRE INTEGER.
  This is the "compute / output" zone.

The axioms are laid out like a workflow: read the header (top),
flow through the hex-adding operation (diagonal), then finalise at
the bottom.

---

## Other meaningful phrases and words found

### Variant instruction phrases (also trace as king-paths)

Beyond the five core axioms, several substrings and related
phrases also appear:

- ADD THE HEXADECIMAL (17 chars, 8 paths)
- ADD THE HEX (9 chars, 10 paths)
- FIND THE HEX (10 chars, 5 paths)
- FIND THE HEX DAY (13 chars, 3 paths) — potentially suggests the
  "date" is a "hex day"
- FIND THE HEXADECIMAL (17 chars, 4 paths)
- DATE ON WIRE (10 chars, 4 paths)
- NO DATE ON WIRE (11 chars, 2 paths) — an inverse reading
- THE DATE ON WIRE (12 chars, 2 paths)
- LAST TEN (7 chars, 5 paths)
- FINAL TEN ENTRY (15 chars, 1 unique path)
- STEP BY TEN (9 chars, 2 paths)
- ENTIRE INTEGER (13 chars, 1 path)
- IT IS INTEGER (11 chars, 1 path)
- END AT THE (8 chars, 5 paths)

These confirm the grid is saturated with instruction-style
phrases — the core five are just the cleanest / longest / unique.

### Unique lone-placement words

Some words trace in a single remarkable way:

- **ALUMINUM** — 8-letter element name, traces as a diagonal
  straight line from (2,8) going SW to (9,1). This is the grid's
  **only 8-letter English word** that traces as a pure straight
  line. Its uniqueness is the strongest single-word signal.
- **OPENER** — 6-letter straight line on column 1 reversed. The
  top 6 cells of column 1 read from bottom to top spell OPENER.
  Combined with TIN nearby, this creates a **"tin opener"** pun —
  a can-opener — tying back to the title "Can U Dig It?".
- **DIGIT** — Row 9 hides the word DIGIT as a perfect subsequence
  (d at column 5, i at 8, g at 9, i at 10, t at 13). "Can U Dig It?"
  phonetically contains "dig + it" = digit. Row 9 confirms this.

### The bottom row decomposed

Row 14 reads `tunenty-tessix`. Compared to the target spelling
"twentysix", the row has:

- **W removed** (intentionally absent — grid has no 'w' near
  where it would need to be for TWENTY to trace)
- **5 letters inserted**: U, N, T, E, S — which anagram to **TUNES**

So the bottom row visually spells "twenty-six" but is *actually*
a twenty-six with the word TUNES dug into it. The grid is literally
showing you music tunes inside a year.

### Chemistry layer

Seven element names trace in the grid:

| Z | Element | How it traces |
|---:|---|---|
| 10 | Neon | King-path |
| 13 | Aluminum | **Straight-line diagonal** (unique) |
| 18 | Argon | King-path |
| 26 | Iron | King-path |
| 50 | Tin | Straight-line (2 placements) |
| 67 | Holmium | King-path |

The two conspicuously **missing** elements are both dug-for metals:

- **Vanadium (V, Z=23)** — the letter 'v' is absent from the grid
- **Silver (Ag)** — needs 'v' too

This matters because **aluminum's main industrial use is
aluminothermic reduction** — the reaction `V₂O₅ + 10 Al → 2 V + 5
Al₂O₃`. The grid contains aluminum (reagent) and even ALUMINA (the
oxide byproduct, 2 paths) but NOT vanadium. It looks like the grid
depicts the reaction *with the product removed*, inviting you to
"dig out" the missing element.

### Pop Will Eat Itself connection

The puzzle title is the exact title of track 6 on PWEI's 1989
album *This Is the Day… This Is the Hour… This Is This!*. The
song is a pop-culture litany mentioning Alan Moore, Optimus Prime,
Bruce Wayne, Dirty Harry, and so on. The phrase "Can U Dig It?" is
repeated many times (count unclear across versions).

Only ONE lyric name (ALAN) traces in the grid. So the song is
thematic dressing, not a data source.

---

## Answers ruled out

Through submission attempts, these answers have been **confirmed
wrong** by the puzzle:

| Answer | How it was derived | Why it failed |
|---:|---|---|
| **600** | Alan Moore's "Unearthing" essay external reference | MOORE doesn't trace in grid; too associative |
| **7** | Count of U's in the grid | Too trivial |
| **3241** | Wire Tapper 22 variant arithmetic | Ad-hoc |
| **3242** | Wire Tapper 22 hex track durations + decimal last | Arbitrary hex interpretation; external trivia |
| **26** | Bottom row "twenty-six" literal reading | Too obvious; grid can't spell TWENTY |
| **22** | V alphabet position / hyphen (14+8) | No supporting mechanism |
| **134** | Step-6 hex sum from ALUMINUM's start cell | Mechanism wrong |
| **167** | Step-6 hex sum from first hex letter (self-referential match to LAST ENTRY's end cell) | Despite being a unique self-closing loop, still wrong |
| **2180** | 154 + 2026 (step-6 from arbitrary t + year) | +2026 variant of step-6 mechanic |

The pattern is striking: **every "step by six through the flat
grid, sum hex digits" answer has been rejected**. That family of
mechanisms is dead. So is any answer involving adding the year
2026 to a small sum.

## Where the solve currently stands

After all the above, the strongest remaining candidates are the
**multi-arc grid-internal convergences**:

### Top remaining: **33** (triple internal convergence)

- Column 6 hex-letter sum = 33 (unique across all 14 columns)
- Sum of column-positions of the 7 U's = 33
- Hex-letter sum of the word "VANADIUM" = 33

Reading: STEP BY SIX → the 6th column → ADD THE HEXADECIMALS on
that column → sum = 33. No external data, no year addition. Three
grid-internal paths produce the same value.

### Second: **79** (double internal convergence)

- TUNES letter alphabet sum = 79
- Sum of the 5 axiom phrase lengths (12+18+9+18+22) = 79
- (79 = Gold atomic number, thematic but external)

### Third: **23** (chemistry)

- Vanadium Z = 23
- Letter V is absent from the grid
- Rejected answers 22 (Ti) and 26 (Fe) bracket V on the periodic
  table — all three are aluminothermic products, and V is the
  one whose symbol is missing

### Other live candidates

- 89 (DATEONWIRE path hex sum = row 2 hex = row 4 hex — triple)
- 14 (grid side)
- 166 (rows 1/7/13 hex sum, no +2026)
- 44 (Ruthenium, if song dig-count is 44)
- 56 (33 + 23 = Barium)
- 46 (79 − 33 = Palladium)
- 82 (corners alphabet sum = Lead)
- 32 (row 6 hex sum)
- 63 (Al + Sn)

## Current recommended submission order

```
1.  33    ← triple internal convergence
2.  79    ← double internal convergence
3.  89    ← triple internal (DATEONWIRE = row 2 = row 4)
4.  23    ← V missing + chemistry
5.  14    ← grid side / end of FINDTHESTART
6.  166   ← row-step hex sum alone
7.  44    ← Ruthenium
8.  56    ← Barium
9.  46    ← Palladium
10. 82    ← Lead
```

---

## What we've learned about the puzzle

1. **The grid is carefully authored.** The 5 long instruction
   phrases are real. They're too long and too grammatical to be
   random.

2. **The "+2026" and "step-6" mechanics are probably red herrings.**
   Both have been ruled out by multiple rejections.

3. **The puzzle likely has a closed-loop, grid-internal solution.**
   External chemistry trivia (metal atomic numbers) and external
   music trivia (PWEI album, Wire magazine, track durations) have
   all been tried and rejected.

4. **The most promising route forward** is treating STEP BY SIX as
   a column index ("the 6th column") rather than a stride, and
   ADD THE HEXADECIMALS as summing the hex-valued letters found
   in that column. This gives **33**.

5. **If the puzzle author wanted you to walk the grid in step-6
   strides and sum hex digits, the answer would have been one of
   the values we already tried. It wasn't.** So that family of
   mechanics is off the table.

The puzzle's ultimate answer is probably a small (2-3 digit)
positive integer derivable from a single purely-grid-internal
operation. **33 is the current best guess.**

---

*Introduction complete. For full technical analysis see
`FINAL_REPORT.md`, `REVIEW.md`, `CANDIDATES.md`, `SUMMARY.md`, or
`AI_HANDOFF.md` in the same repository.*
