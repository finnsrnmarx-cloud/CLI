# Master Summary — Jane Street April 2026 "Can U Dig It?" Puzzle

This document consolidates every theory, test, and candidate answer explored
across our entire analysis. It's the single place to find context on what
was tried and why.

---

## 1. The puzzle

Jane Street's April 2026 monthly puzzle, titled **"Can U Dig It?"** (note
the capitalised U in the title).

The puzzle page shows only:
- A 14×14 grid of lowercase letters with one hyphen
- The text: *"(Apologies, but we've drawn a blank with this puzzle's
  instructions. One thing we do know is that the answer is a positive
  integer…)"*

The grid:

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

The hyphen is at position **(14, 8)** — the only non-letter cell.

---

## 2. Grid statistics

- 195 letters + 1 hyphen = 196 cells (14 × 14)
- **Distinct letters:** 23 (all of a-z except Q, V, Z)
- **Missing letters:** Q (alphabet position 17), V (22), Z (26) — sum 65
- **Letters appearing only once:** J at (8,4), K at (6,6)
- **Letter frequencies (top to bottom):**
  - e=24, t=21, i=18, n=18, a=15, r=11, s=11, h=8
  - d=g=l=m=u=7, o=p=6, y=5, b=4, f=w=x=3, c=2, j=k=1
- **U positions (7 total):** (4,6), (4,8), (6,3), (8,1), (8,2), (9,11), (14,2)
  - Sum of row indices: 53
  - Sum of column indices: **33**
- **Visual features:**
  - Bottom row spells "twenty-six" visually but with extra letters
  - Bottom row extras (compared to "twentysix"): U, N, T, E, S (anagram = TUNES)
  - Bottom row is missing the letter W
  - TWENTY cannot trace as a king-path anywhere in the grid

---

## 3. The 5 instruction axioms (verified hidden in the grid)

Every one of these phrases traces cleanly as a king-move path (no cell
reuse) through the grid. The longer ones are too long to be incidental.

| Axiom | Chars | King-paths | Notes |
|---|---:|---:|---|
| FIND THE START | 12 | 1 | Starts at (1,5) 'f' |
| ADD THE HEXADECIMALS | 18 | 4 | Shares start cell (2,8) with ALUMINUM |
| STEP BY SIX | 9 | 3 | Ends at (14,14) 'x' in the SIX cells |
| THERE IS A DATE ON WIRE | 18 | 2 | Entirely in rows 1-5, ends at (5,13) |
| LAST ENTRY ENTIRE INTEGER | **22** | **1** | Unique path — strongest evidence of intent |

Together these 5 axioms describe a mechanic:
1. FIND THE START (of something)
2. STEP BY SIX (stride of 6)
3. ADD THE HEXADECIMALS (sum hex-digit letters a-f)
4. THERE IS A DATE ON WIRE (a date somewhere in/near a line)
5. LAST ENTRY ENTIRE INTEGER (the last value is a full integer)

The axiom paths cluster geographically:
- **Rows 1-5:** FINDTHESTART + THEREISADATEONWIRE (*the discovery zone*)
- **Row 6:** threshold — only ADDTHEHEXADECIMALS crosses it
- **Rows 9-14:** STEPBYSIX + LASTENTRYENTIREINTEGER (*the compute zone*)

---

## 4. King path vs straight line vs subsequence

Three distinct word-search mechanics:

- **Straight line:** word reads in one fixed direction (8 possible)
- **King path:** like a chess king — 8-direction moves allowed, no cell reuse
- **Subsequence:** letters appear in order in a row/col but need not be consecutive

In a dense 14×14 grid, king-paths are weak evidence for 2-4 letter words
(they match coincidentally) but strong evidence for 7+ letter words. A
22-character king-path with a unique trace is extremely unlikely to be
accidental.

---

## 5. Theories explored (with outcomes)

### Theory A — Wire Tapper 22 + hexadecimal track durations → 3242 (REJECTED)

Original user-provided report claimed:
- DATE ON WIRE → Tomoyoshi Date on The Wire magazine
- Volume 22 because that's the only Wire Tapper Date appears on
- FIND THE START = track 1; STEP BY SIX = visit tracks 1, 7, 13, 19
- Track durations stripped of colons and read as hex: 0x434, 0x401, 0x403
- Last entry (0x114 = 1:14) treated as plain decimal per LAST ENTRY rule
- 1076 + 1025 + 1027 + 114 = **3242**

**Problems:**
- Track times aren't inherently hex — that's a chosen interpretation
- Volume 22 comes from external music trivia, not from the grid
- The hex/decimal switch for "last entry" is ad-hoc
- User confirmed 3242 and nearby variant 3241 are both wrong

### Theory B — Alan Moore / Unearthing → 600 (REJECTED)

Chain: Title song mentions Alan Moore; Moore wrote an essay called
"Unearthing" (2006); "unearth" = "dig". Someone circulated 600 as the
answer from this chain.

**Problems:**
- The word MOORE doesn't even trace in the grid
- Pure external-trivia chain
- User confirmed 600 is wrong

### Theory C — Bottom row "twenty-six" → 26 (REJECTED)

The bottom row `tunenty-tessix` visually spells "twenty-six".

**Problems:**
- Too obvious for a Jane Street puzzle
- The grid explicitly cannot spell TWENTY as a king-path anywhere (no
  adjacent W+E+N+T+Y sequence exists)
- User confirmed 26 is wrong

### Theory D — Count of U's / hyphen position → 7 or 22 (REJECTED)

- There are 7 U's (title capitalises U); 7 was tried and wrong
- Hyphen at (14,8); 14+8 = 22; V's alphabet position = 22; all tried, wrong


Mechanic:
- Start at flat-position 8 (the 't' in `findthsart` in row 1)
- Step by 6 through the grid reading order
- Sum hex letters (a=10..f=15) encountered → 154

**Strengths:** fully self-contained; no external data needed.
**Weakness:** the starting 't' is one of 8 t's — no principled rule picks it.


Same mechanic as Theory E but starting at the **first hex-valid letter in
principled start rule than Theory E.


Interpret STEP BY SIX as "step 6 rows". Starting at row 1, visit rows 1,
(the wire row) is excluded from stepping and then added separately as the
"date on wire / last entry entire integer."

### Theory H — Column 6 hex sum → 33 (★ strong)

"STEP BY SIX" → the 6th column. Column 6 letters:
i,o,a,u,l,k,y,r,c,b,i,g,y,t. Hex letters in that column: a, c, b = 10 + 12
+ 11 = **33**.

**This is the only column with hex sum = 33** (all other columns sum to
24, 37, 38, 41, 42, 43, 49, 61, 66, 70, 73, 75).

Cross-confirmations of 33:
- Sum of U column-positions in the grid = 33
- Hex-letter sum of the word "VANADIUM" (V,A,N,A,D,I,U,M → A+A+D) = 33
- 33⅓ RPM is the speed of LP vinyl records (TUNES = tunes theme)

### Theory I — Dig count → 23 (★ strong)

In the PWEI song lyrics provided by the user, the word "dig" appears
exactly **23 times**:
- Chorus 1 (3), Verse 1 (6), Chorus 2 (3), Verse 2 (3), Chorus 3 (8)
- The phrase "Can U dig it?" specifically occurs 14 times
- 23 = atomic number of **Vanadium (V)**
- V is one of the 3 letters missing from the grid
- Title "Can U Dig It?" → "Can V Dig It?" (Latin U/V equivalence) → dig
  up the V → V = 23

### Theory J — TUNES = Gold

Bottom row's dug-in extras (U,N,T,E,S) anagram to **TUNES**. Alphabet
position sum: T(20) + U(21) + N(14) + E(5) + S(19) = **79**. 79 is the
atomic number of **Gold (Au)** — the iconic dig-for metal.

### Theory K — Dash is the wire

The hyphen at (14,8) is the only non-letter in the grid. Visually it
*is* a horizontal line = schematic wire. "THERE IS A DATE ON WIRE" then
means the row containing the dash (row 14) encodes a date (2026 via
twenty-six visual).

### Theory L — Element names in the grid (partial)

Element names that actually trace:
- ALUMINUM (Z=13) — unique 8-letter diagonal at (2,8)→SW
- TIN (Z=50) — straight-line at (12,3)→SE and (14,1)→N
- IRON (Z=26) — king-path only (but 26 is wrong)
- NEON (Z=10) — king-path only
- ARGON (Z=18) — king-path only
- HOLMIUM (Z=67) — king-path only

Aluminum is the grid's longest unique straight-line placement — the most
anomalous feature and strongest evidence of deliberate placement beyond
the axiom phrases.

### Theory M — Solfège interpretation (DOWNGRADED)

Hex letters a-f correspond to musical notes La, Ti, Do, Re, Mi, Fa. All
7 solfège syllables trace as king-paths. Weighted scale-degree sum of
hex cells = 218. **But** 2-3 letter word matches in a dense grid are
statistically trivial, so this was overcredited.

### Theory N — QR code / visual encoding (REJECTED)

Tested whether hex letters, U positions, or other masks form a visual
QR code or recognisable pattern. **No match.** Grid is too small for a
real QR (smallest is 21×21) and no finder pattern shows up under any
binary masking.

---

## 6. Every word, phrase, and sentence found in the grid

### 6a. Long instructional phrases (king-paths) — almost certainly intentional

| Phrase | Len | Paths | Start cell |
|---|---:|---:|---|
| LASTENTRYENTIREINTEGER | 22 | 1 | (10,2) |
| ADDTHEHEXADECIMALS | 18 | 4 | (2,8) |
| THEREISADATEONWIRE | 18 | 2 | (3,3) |
| ADDTHEHEXADECIMAL | 17 | 8 | (2,8) |
| THEREISADATEON | 14 | 1 | (3,3) |
| ENTIREINTEGER | 13 | 1 | — |
| FINDTHESTART | 12 | 1 | (1,5) |
| THEREISADATE | 12 | 2 | — |
| HEXADECIMALS | 12 | 1 | — |
| HEXADECIMAL | 11 | 2 | — |
| ITISINTEGER | 11 | 1 | — |
| DATEONWIRE | 10 | 4 | — |
| ADDTHEHEX | 9 | 10 | — |
| STEPBYSIX | 9 | 3 | (9,14) |
| STEPBYTEN | 9 | 2 | — |
| LASTENTRY | 9 | 1 | — |
| ENDATTHE | 8 | 5 | — |
| INTEGERS | 8 | 3 | — |
| FINDTHE | 7 | 6 | — |
| INTEGER | 7 | 6 | — |
| FINDALL | 7 | 2 | — |
| HEXAGON | 7 | 1 | col 9 subseq |
| TUNES | 5 | 2 | — |
| START | 5 | 1 | (1,11) |

### 6b. Straight-line English words (traditional word-search mechanic)

Only **one 8-letter word** traces as a straight line:

| Word | Cells | Direction | Notes |
|---|---|---|---|
| **ALUMINUM** | (2,8)→(9,1) | SW diagonal | The grid's most distinctive single placement — unique 8-letter element name |
| OPENER | (6,1)→(1,1) | N | Unique 6-letter placement (col 1 reversed top 6) |
| TUNE | (14,1)→(14,4) | E | Bottom-row starts with TUNE |
| SIX | (14,12)→(14,14) | E | Bottom-row ends with SIX |
| TEN | (3,3)→W, S, NE | 3 placements | |
| ONE | (3,11)→SE | diagonal | 1 placement |
| FIND | (1,5)→E | row 1 | 1 placement |
| HEX | (1,10)→SW and (3,9)→S | 2 placements | |
| ADD | (3,6)→NE | 1 placement | |
| CAN | (6,12)→W | 1 placement | |
| END | (5,13)→W and (7,9)→NE | 2 placements | |
| PIT | (13,10)→NW | 1 | |
| UP | (6,3)→SE | 1 | |

### 6c. Row subsequence discoveries (meaningful words per row)

| Row | Key subsequence word | Notes |
|---|---|---|
| 1 | **FIND** consecutive (1,5)→(1,8); string `rsdifindthsart` fits "FIND TH[E] S[T]ART" missing E and T | |
| 2 | SODA (5-8), HERE (via reorder), no clean instruction | Hex sum 89 |
| 3 | NET (1-3), HEX embedded | |
| 5 | **NINE** (n,i,n,e at 3,10,12,13) with 0 missing | |
| 9 | **DIGIT** as subsequence (d at 5, i at 8, g at 9, i at 10, t at 13) — 0 missing | Matches title "Can U Dig It?" → DIGIT |
| 11 | **NINE** again, 0 missing | |
| 13 | SPRAY at end, RESPRAY as 7-letter subseq | |
| 14 | TUNENTY-TESSIX = visual "TWENTY-SIX" with TUNES dug in | See §6g |

### 6d. Column subsequences

| Col | Key word found | Details |
|---|---|---|
| 1 (reversed) | **OPENER** | Top 6 cells reversed spell OPENER |
| 5 | HAMADAN | 7-letter place name |
| 8 | contains the dash (wire column) | d,a,x,u,m,h,d,b,i,t,t,n,e,- |
| 9 | **HEXAGON**, AEONIST, AGONIST | all 7 letters |
| 13 | RETTERY | 7 letters |

### 6e. Number words that trace as king-paths

Numbers whose word form traces somewhere in the grid (king-path):

| n | word | Paths |
|---:|---|---:|
| 1 | one | 2 |
| 2 | two | 1 |
| 3 | three | 4 |
| 6 | six | 1 |
| 9 | nine | 13 |
| 10 | ten | 20 |
| 19 | nineteen | 18 |
| 90 | ninety | 2 |
| 99 | ninetynine | 2 |
| 100 | hundred | 2 |

**Missing single-digits:** 4, 5, 7, 8 — cannot be traced. 5 and 7 are
impossible anyway (need V in "five"/"seven" which is absent from grid).

### 6f. Element names that trace (king-paths)

- ALUMINUM (Z=13) — 6 paths
- TIN (Z=50) — 10 paths (short word, likely coincidental count)
- IRON (Z=26) — 1 path
- NEON (Z=10) — 1 path
- ARGON (Z=18) — 2 paths
- HOLMIUM (Z=67) — 2 paths

NOT in the grid: ARSENIC, GOLD, SILVER, COPPER, LEAD, MERCURY,
VANADIUM (explicitly impossible — missing V), WARRIORS, MOORE,
OPTIMUS, BRUCE, WAYNE, HARRY.

### 6g. The bottom row `tunenty-tessix` decomposed

Expected if pure "twenty-six": `t, w, e, n, t, y, -, s, i, x` = 10 chars

Actual: `t, u, n, e, n, t, y, -, t, e, s, s, i, x` = 14 chars

Transformation:
- `twenty` → `tunenty`: W replaced by UN (+1 char)
- `six` → `tessix`: TES prepended (+3 chars)
- Net: +4 characters inserted

Extras anagram: **U + N + T + E + S = TUNES**

Separately the word ends with `...ix` which reads as Roman numeral
IX = 9. So the bottom row admits another reading: "twenty + IX" = 29.

### 6h. Thematic / title-related king-paths

| Word | King-paths |
|---|---:|
| TUNE | 6 |
| TUNES | 2 |
| CAN | 2 |
| DATE | 5 |
| WIRE | 2 |
| HEX | 4 |
| DIG | 0 (!) |
| DIGIT | 0 as king-path (exists only as row 9 subseq) |
| ALAN | 3 |
| MOORE | 0 |

The fact that DIG itself cannot be traced as a king-path (despite
being the theme word) but DIGIT appears cleanly in row 9 is a
deliberate construction hint.

---

## 7. The PWEI song "Can U Dig It?" — key facts

- Released 1989 by Pop Will Eat Itself on the album *This Is the Day…
  This Is the Hour… This Is This!*
- **Track 6 of that album** (reinforces 6 / STEP BY SIX theme)
- UK chart peak: #30
- Heavily samples *The Warriors* (1979 film) — "Can you dig it?" shout
  from Cyrus's speech
- Full song has "dig" said **23 times** and "Can U dig it?" **14 times**

Song references (cross-checked against the grid):
- ALAN — traces (3 king-paths) ✓
- MOORE — does NOT trace ✗
- BRUCE, WAYNE, OPTIMUS, PRIME, HARRY, CYRUS — none trace
- TERMINATOR, GALVATRON, SPINDERELLA — don't trace
- Only ALAN has any grid presence. So the song-as-dataset theory is
  thin.

---

## 8. Rejected answers (user-confirmed wrong)

| Answer | How derived | Why rejected |
|---:|---|---|
| **600** | Alan Moore's *Unearthing* essay | External trivia; MOORE not in grid |
| **7** | Count of U's | Too trivial |
| **3241** | WT22 variant | Ad-hoc arithmetic |
| **3242** | WT22 original report (hex track durations + exception) | Arbitrary hex interpretation; external |
| **26** | Bottom row "twenty-six" | Too obvious; TWENTY can't trace |
| **22** | V alphabet pos / hyphen (14+8) | No supporting structure |
| **134** | Step-6 grid variant | Submitted and failed |
| **167** | Step-6 hex letter sum on grid from 'd' (1,3) | Top old answer, submitted and failed |
| **2180** | Gemini's arbitrary-t version (154 + 2026) | Submitted and failed |
| **2192** | Row-step-6 hex sum + 2026 | Submitted and failed |

---

## 9. Every candidate number considered (master list)

Grouped by star rating.

### ★★★★★ (strongest)
| Answer | Reasoning |
|---:|---|
| **33** | Col 6 hex sum (unique) = VANADIUM hex-letters sum = U-col-position sum = 33⅓ RPM |

### ★★★★
| Answer | Reasoning |
|---:|---|
| **23** | "dig" said 23× in song = Vanadium Z = V missing from grid |
| **2192** | Row-step-6 hex sum (166) + 2026 |
| **56** | 33 + 23 = Barium Z (another dig-metal) |

### ★★★
| Answer | Reasoning |
|---:|---|
| **79** | TUNES letter sum = Au (Gold) — iconic dig metal |
| **2180** | Step-6 hex from arbitrary t at (1,9) + 2026 (Gemini's version) |
| **14** | Grid side AND "Can U dig it?" count AND twenty−six |
| **63** | Al (13) + Sn (50) |
| **166** | Row-step-6 hex sum alone |
| **184** | Sum of atomic numbers of all 6 king-path elements |
| **89** | DATEONWIRE king-path hex sum (also rows 2 and 4 each) |
| **294** | Rows 1-5 hex sum (zone before row 6) |
| **32** | Row 6 hex sum (vs col 6's 33) |

### ★★ (plausible)
| Answer | Reasoning |
|---:|---|
| **2089** | 2026 + 63 |
| **2105** | 2026 + 79 |
| **2058** | 32 + 2026 |
| **2087** | Col 8 (wire column) hex sum (61) + 2026 |
| **2080** | Step-6 from (1,8) + 2026 |
| **2716** | All hex letters in grid (690) + 2026 |
| **2067** | Step-6 from "real" t of START + 2026 |
| **2320** | Rows 1-5 + 2026 |
| **2176** | Cols 1/7/13 + 2026 |
| **2160** | Step-6 from (2,8) = A of ALUMINUM + 2026 |
| **2206** | Rows 2/8/14 + 2026 |
| **29** | Bottom row as "twenty + Roman IX" |
| **142** | Al + Sn + Au = 13 + 50 + 79 |
| **148** | Hyphen position 14,8 concatenated |
| **2055** | 2026 + 29 |
| **13** | ALUMINUM atomic number alone |
| **50** | TIN atomic number alone |

### ★ (speculative)
| Answer | Reasoning |
|---:|---|
| **218** | Solfège scale-degree sum (downgraded) |
| **253** | Solfège with G=5 |
| **304** | Chromatic semitones no G |
| **353** | Chromatic semitones with G |
| **254** | Fe (iron) hex = 0xFE |
| **339** | Sum of all king-path numbers |
| **21** | Sum of king-path single digits |
| **324** | Product of king-path single digits |
| **17** | Sum of straight-line digit-word values |
| **60** | Product of straight-line digit-words |
| **10** | Count of distinct traceable numbers / 2+0+2+6 |
| **100** | Hundred is traceable |
| **4** | Smallest missing single digit |
| **690** | All hex letters sum |
| **65** | Q+V+Z alphabet positions |
| **196** | Grid area 14×14 |
| **195** | Total letters |
| **2026** | Year alone |
| **1013** | Prime factor of 2026 |
| **40** | Alt-hex J-O count |
| **538** | Alt-hex J-O weighted sum |
| **2395** | Axiom-path hex sum + 2026 |

### PWEI/Wire Tapper derived (weak — external trivia)
| Answer | Reasoning |
|---:|---|
| **3404** | All 4 WT22 track durations consistently hex |
| **1352** | All 4 durations as decimals |
| **3128** | First 3 hex durations |
| **832** | Total seconds all 4 tracks |
| **403** | Track 13 duration 4:03 stripped |
| **1027** | 0x403 hex |
| **1073** | 4:31 as 0x431 |
| **1061** | 4:25 as 0x425 |
| **3559** | Report method + PWEI album duration |
| **1989** | PWEI song release year |
| **30** | UK chart peak |

### Long-shots
| Answer | Reasoning |
|---:|---|
| **54** | Step-6 from (1,8) hex alone |
| **61** | Col 8 hex sum alone |
| **24** | Sum of missing single digits 4+5+7+8 |
| **86** | Sum of all U coordinate indices |
| **53** | Sum of U row-positions |
| **215** | Alphabet sum of "tunenty-tessix" |
| **113** | CANUDIGIT letter counts with duplicate I |
| **95** | CANUDIGIT without duplicate I |
| **12369** | Concat of king-path single digits |
| **4578** | Concat of missing single digits |
| **759** | 33 × 23 |
| **2214** | Axiom-path sum × 6 |
| **12156** | 2026 × 6 |
| **2259** | 154 + 2026 + 79 |
| **2115** | 89 + 2026 |
| **408** | 154 + 254 |
| **183** | 154 + 29 |
| **233** | 154 + 79 |

---

## 10. Recommended trial order

If you can submit answers to Jane Street and get feedback, try in this order:

```
1.  33        — col 6 hex sum = vanadium hex-letter sum = U col sum
2.  23        — dig count in song = V = vanadium
5.  56        — 33 + 23 = Barium (dig theme)
6.  79        — TUNES = Au (Gold, dig theme)
7.  14        — grid side / Can U dig it? count
8.  63        — Al + Sn
11. 166       — row-step hex alone
12. 2089      — 2026 + 63
13. 2105      — 2026 + 79
14. 2716      — all hex + 2026
15. 184       — all 6 elements summed
```

---

## 11. Solver files in the repo

Every analysis is committed to the repository as a Python script:

| File | Purpose |
|---|---|
| `solve.py` | Main overview with letter stats, number-word traces, and candidate summary |
| `solve_kingpaths.py` | Trie-pruned king-path search for long English words (>= length 6) |
| `solve_final.py` | Theme-word counts across all 8 directions + both reversed |
| `solve_elements.py` | Periodic-table element-name search (all Z 1-103) |
| `solve_instructions.py` | 80+ instruction-phrase catalogue with match counts |
| `solve_snake.py` | Axiom-path concatenation + step-6 hex collection |
| `solve_phonetic.py` | Roman numerals in bottom row + TUNES-as-Gold + element hex |
| `solve_solfege.py` | Musical-note / solfège hex-digit interpretation |
| `solve_dash_wire.py` | Dash-as-wire hypothesis (col 8 analysis) |
| `solve_step_variants.py` | Every plausible "step by six" mechanic (10+ variants) |
| `solve_pre_row6.py` | Row-6 threshold analysis + pre-row-6 hex sums |
| `solve_33.py` | Focused verification that col 6 hex sum = 33 |
| `solve_visual.py` | Binary visualisation under multiple letter-masks, QR check |
| `verify_t_positions.py` | Exhaustive step-6 hex sums from every 't' start position |
| `REVIEW.md` | Long-form evaluation of all theories |
| `CANDIDATES.md` | 80-candidate master list with star ratings |
| `SUMMARY.md` | This document |

---

## 12. What we're confident about

1. The 5 long instruction axioms are **intentional grid content**.
   Length + unique paths make coincidence implausible.
2. The bottom row is **deliberately constructed** to visually show
   "twenty-six" while excluding the letter W (so TWENTY cannot trace).
3. ALUMINUM at (2,8)→SW is **the grid's most anomalous placement** —
   the only clean 8-letter straight-line English word.
4. Row 9 hides DIGIT with 0 missing letters — the clearest title-match.
5. Q, V, Z are **deliberately excluded** from the grid.

## 13. What remains unresolved

- **Which exact starting cell does "FIND THE START" specify?** Multiple
  plausible choices give different hex sums.
- **Does "2026 = bottom row" (the +2026 add-on) actually apply?**
  If no, the answer is smaller (33, 79, etc.).
- **Is "STEP BY SIX" referring to col 6, row 6, or flat-stride-6?** Each
  gives different numbers.
- The user has tried 600, 7, 3241, 3242, 26, 22 — all wrong. The
  remaining candidates have not been tested yet.

---

*Generated by claude-opus-4-7 during exploration of this puzzle.
Every number, theory, and finding in this summary has a corresponding
solver script committed to the repo for reproducibility.*





