# Master Candidate List — Jane Street April 2026 "Can U Dig It?"

> Every number we've seriously considered, now re-ranked by literal
> axiom compliance. Last full rewrite: 2026-04-20 after the Mozart
> K.184 / Symphony No. 26 discovery.

---

## The five axioms and their alternate readings

The grid hides five imperative/declarative phrases as king-paths. Each
is listed with every interpretation that's been seriously proposed.

### AXIOM 1 — FIND THE START
Locate a starting position.
- **F-a** Top-left cell (1,1)
- **F-b** First hex letter (`d` at (1,3)) in reading order
- **F-c** The START king-path itself (cells (1,11) → (1,14))
- **F-d** First byte of JPEG (SOI marker `FF D8`, byte 0)
- **F-e** Second DQT marker (`FF DB 00 43 01`, byte 89-91)
- **F-f** Track 6 on the PWEI album (byte 6)
- **F-g** ALUMINUM diagonal anchor at (2,8)

### AXIOM 2 — STEP BY SIX
Stride by 6.
- **S-a** Stride 6 through flat-row-major grid (196 cells)
- **S-b** Stride 6 rows (rows 1, 7, 13)
- **S-c** Column index 6 (col 6 top-to-bottom)
- **S-d** Stride 6 image bytes
- **S-e** Track 6 on album (PWEI "Can U Dig It?")
- **S-f** Symphony "No. 6" (ruled out — K.184 is No. 26, not 6)
- **S-g** 14 − 8 = 6 (hyphen coords generate the stride)

### AXIOM 3 — ADD THE HEXADECIMALS
Sum values interpreted as hexadecimal.
- **H-a** Sum letter values a=10..f=15 for letters visited
- **H-b** Sum byte values of image bytes visited
- **H-c** Sum only bytes in 0x0A..0x0F range (strict-hex)
- **H-d** Concatenate hex digits to form a multi-digit hex integer
- **H-e** Sum hex-letter-positions weighted by frequency

### AXIOM 4 — THERE IS A DATE ON WIRE
A date is encoded at the hyphen/wire.
- **D-a** Row 14 spells "twenty-six" → **date = 26**
- **D-b** Publication year → **date = 2026**
- **D-c** 14 − 8 = 6 (hyphen as subtraction operator; already absorbed as stride)
- **D-d** Declarative only — date tells you WHERE to go (e.g. 26 indexes Köchel 184)
- **D-e** Entry "date on wire" as metadata, not an addition

### AXIOM 5 — LAST ENTRY ENTIRE INTEGER
The final value IS the answer.
- **I-a** Raw sum; no modification; the integer stands whole
- **I-b** Sum + 26 (date-on-wire additive)
- **I-c** Sum + 2026 (calendar-year additive; **rejected empirically** — see 2192, 2193 below)
- **I-d** Concatenate sum with date → `<sum><26>` or `<2026><sum>`

---

## Scoring conventions

Each candidate gets a row in the axiom grid with:

| Mark | Meaning |
|:---:|---|
| ✅ | Satisfies this axiom under a principled reading |
| 🟡 | Satisfies under a stretched reading |
| ❌ | Does not satisfy |
| — | Not applicable |

Candidates are ranked by count of ✅ first, then 🟡, then thematic
strength.

**End of Part 1 (definitions).**

---

## PART 2 — TOP TIER (5/5 axioms satisfied)

### ★★★★★★ #1: **184** — Mozart Köchel catalogue closure

**Axiom grid:**

| F (find) | S (step6) | H (hex) | D (date) | I (integer) |
|:---:|:---:|:---:|:---:|:---:|
| ✅ F-e (2nd DQT byte 91) | ✅ S-d (image stride 6) | ✅ H-b (sum image bytes) | ✅ D-d (26 → K.184) | ✅ I-a (raw integer) |

**Blurb — all connections:**

Start at byte 91 of the JPEG image header (the table-id byte of the
second DQT marker `FF DB 00 43 **01**`). This is the natural
"FIND THE START": the grid points at the image, and the image's
structural markers anchor position 91. Stride 6 through subsequent
bytes. The running hex-sum is **184**.

Row 14 of the grid phonetically spells **"twenty-six"** (letters 1-4
are `TUNE`, then `NTY-TESSIX` merges into "twenty-six"). The wire
(hyphen at (14,8)) bisects that "date". But **26 is not added** — it's
an **index**: Mozart's **Symphony No. 26** has the Köchel catalogue
number **K. 184**. Row 14 literally reads **"Tune 26"** = Symphony
No. 26 = K. 184.

Three-arc convergence:
1. **Image mechanic** → step-6 hex sum from byte 91 = 184
2. **Grid referent** → "Tune twenty-six" → Köchel 184
3. **Grid element-sum** → sum of atomic numbers of elements mentioned
   in the grid lands at 184

"LAST ENTRY ENTIRE INTEGER" = 184 is clean, whole, and an actual
catalogue number (so it IS an integer identifying a real entity).

PWEI cross-check: "Can U Dig It?" is a pop-culture-reference song
("Alan Moore knows the score"); the grid works the same way — the
answer is only findable if you "dig" the cross-reference from "tune
26" to Köchel. The song is also *Track 6* on its album, reinforcing
STEP BY SIX.

**This is the current top recommendation.**

---

### ★★★★★ #2: **210** — Image closure + wire-date 26

**Axiom grid:**

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ✅ F-e | ✅ S-d | ✅ H-b | ✅ D-a (+26 additive) | ✅ I-b |

**Blurb:**

Same mechanic as 184, but treats D-a (adding 26) literally rather than
as an index. `184 + 26 = 210`. This is the fallback if the Köchel
interpretation is over-clever and the puzzle wanted a simple additive.
Weaker than 184 because 210 has no thematic self-reference, but
mechanically all 5 axioms are obeyed.

---

### ★★★★★ #3: **333** — Track-6 + Al-Z convergence + 26

**Axiom grid:**

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ✅ F-f (Track 6) | ✅ S-d | ✅ H-b | ✅ D-a | ✅ I-b |

**Blurb:**

Image step-6 starting at byte 6 (Track 6 = PWEI song position) gives
one sum; starting at byte 13 (Aluminum Z, the anomalous diagonal
anchor) gives another; they converge at **307**. Add 26 → **333**.

Additional resonance: **3×111 = 333**, and **33⅓ RPM × 10s = 333** —
TUNES theme (vinyl records). Column 6 hex sum = 33 is already a
known anchor; 333 amplifies it. 10/10 thematic but the math is
coincidence-adjacent.

---

### ★★★★★ #4: **115** — DATEONWIRE king-path hex + 26

**Axiom grid:**

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ✅ F-c (START king-path) | 🟡 S-g (14−8=6) | ✅ H-a | ✅ D-a | ✅ I-b |

**Blurb:**

The THERE-IS-A-DATE-ON-WIRE king-path has hex-letter sum **89**
(Actinium Z, incidentally). Add the date 26 → **115**. Satisfies all
axioms via a fully grid-internal reading; weakest axiom is STEP BY SIX
(the 6 comes from the hyphen operator 14−8=6, not a literal stride).

---

### ★★★★★ #5: **2210** — Image closure + calendar year

**Axiom grid:**

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ✅ F-e | ✅ S-d | ✅ H-b | 🟡 D-b | 🟡 I-c |

**Blurb:**

`184 + 2026 = 2210`. Same base mechanic as 184, but treats the date
as calendar year (D-b) additively (I-c). **Empirically weakened** by
the rejection of 2192/2193 (which were analogous +2026 constructs);
but 184 base is stronger than 167 base, so this version might still
land if the additive theory holds.

**End of Part 2 (top tier).**

---

## PART 2½ — NEW MOZART-EXTENSION CANDIDATES (2026-04-20 late)

After the Symphony 26 / K.184 discovery, `image_mozart_extended.py`
surfaced five more candidates that tighten the closure. All satisfy
the axioms if you accept the Köchel interpretation of row-14.

### ★★★★★ NEW #A: **626** — K.626 Requiem (Mozart's LAST composition)

**Axiom grid:**

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ✅ F-e (via K.184 start) | ✅ S-e (stride 6 K-numbers) | 🟡 H-d | ✅ D-d (26 as index) | ✅ I-a (the LAST entry) |

**Blurb — why this is possibly the solve:**

"LAST ENTRY ENTIRE INTEGER" is the single axiom most perfectly
satisfied by **K.626 — the Requiem**, Mozart's unfinished final work
and the actual **last numbered entry** in the Köchel catalogue. If
row-14 points at Mozart (via "tune 26" → Symphony 26 → K.184), then
the "LAST ENTRY" instruction may literally mean: ignore 184, jump to
the catalogue's last entry → 626.

Three confirmations:
1. **K.626 IS Mozart's last entry** — the Köchel catalogue ends here
2. **Requiem = "dig" theme** — literally a mass for the dead / burial
3. **626 = 6 × 104 + 2 × 1** — note `6² × (something)` won't resolve
   cleanly but "STEP BY SIX → 626" stride from K.2 (176 steps × 6 − 50)
   doesn't work cleanly either. The mechanic is: start = K.184,
   step by 6 until end of catalogue, take LAST.

**Sequence from K.184 stepping +6**: 184, 190, 196, 202, ..., 622, 628
(exceeds 626). Last valid ≤ 626 would be **K.622** (Clarinet Concerto),
but the LAST Köchel number *period* is **K.626**.

### ★★★★★ NEW #B: **622** — K.622 Clarinet Concerto (last step-6 entry)

**Axiom grid:**

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ✅ F-e (K.184) | ✅ S-e (+6 per step) | ✅ H-b | ✅ D-a | ✅ I-a |

**Blurb:**

Exactly what the axioms prescribe: start at K.184 (Tune 26), step by
6 through Köchel numbers (184, 190, 196, 202, 208, …), stop at the
LAST stride ≤ 626. That's K.622 — the Clarinet Concerto, Mozart's
second-to-last work, composed during his final illness. Most
rigorously axiom-compliant "last entry" reading after 184 itself.

The sequence 184 → 190 → 196 → … → 622 has exactly **74 terms**
(184 + 73×6 = 622). Interesting: 74 = count of king-moves between
axiom-spelled-out words.

### ★★★★ NEW #C: **551** — K.551 Jupiter Symphony (last SYMPHONY)

**Axiom grid:**

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ✅ F-e | 🟡 S-e | ✅ H-b | ✅ D-a | ✅ I-a |

**Blurb:**

If "LAST ENTRY" specifically means the last **Symphony** (because
the title's TUNE = symphony), then the answer is K.551 — the Jupiter
Symphony, Mozart's final numbered symphony (#41). Symphony-only
interpretation. 551 is also a prime number.

### ★★★★ NEW #D: **345** — K.184 + K.161a (alt-catalogue sum)

**Axiom grid:**

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ✅ F-e | ❌ | ❌ | ✅ D-d | ✅ I-a |

**Blurb:**

Wikipedia lists Symphony No. 26 as "K.184 / 161a" — it has **two
Köchel numbers**. Sum 184 + 161 = **345**. Elegant "digital identity"
but doesn't invoke step-6 or hex. Thematic interest: 345 is
consecutive digits 3-4-5.

### ★★★★★ NEW #E: **47** (reinforced) — Silver Z, strict-hex from Symphony-26 byte

**Axiom grid:**

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ✅ F-d (byte 26 = Symphony 26 index) | ✅ S-d | ✅ H-c (strict-hex) | ✅ D-d | ✅ I-a |

**Blurb:**

**Major new finding.** Step-6 through image bytes starting at **byte
26** (= Symphony 26 index from row-14), summing ONLY bytes in the
0x0A-0x0F range (H-c, strict hex letters) → sum = **47**. That's
**Silver (Ag)**, the deliberately-absent dig-metal.

This is NOW the strongest 5/5 candidate after 184:
- FIND THE START → start at byte 26 (Symphony 26 index from row 14)
- STEP BY SIX → stride 6 through bytes
- ADD THE HEXADECIMALS → strict interpretation: only 0x0A-0x0F bytes
- THERE IS A DATE ON WIRE → the date (26) gave us the start position
- LAST ENTRY ENTIRE INTEGER → 47

Plus: Silver is THE archetypal dig-metal and its absence from the
grid was previously a dangling clue.

### ★★★ NEW #F: **1006** — Symphonies 26,32,38 K-sum

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ✅ F-d | ✅ S-e (+6 symphonies) | ❌ | ✅ D-d | ✅ I-a |

**Blurb:**

Step by 6 through symphony **numbers** starting at 26: 26, 32, 38,
44 (doesn't exist — Mozart wrote 41). Take K-numbers of the first
three valid: K.184 + K.318 + K.504 = **1006**. Discards 41 because
it breaks the stride.

### ★★★ NEW #G: **1557** — Symphonies 26,32,38,41 K-sum

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ✅ F-d | 🟡 S-e | ❌ | ✅ D-d | ✅ I-a |

**Blurb:**

Same as #F but includes K.551 (Symphony 41, the Jupiter, the LAST):
1006 + 551 = **1557**. Satisfies "LAST ENTRY" by including the final
symphony.

**End of Part 2½ (Mozart extensions).**

---

## PART 3 — MID TIER (3-4 axioms satisfied)

### ★★★★ #6: **307** — Track-6 / Al-Z step-6 convergence (raw)

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ✅ F-f | ✅ S-d | ✅ H-b | ❌ | ✅ I-a |

**Blurb:** Image step-6 from byte 6 or byte 13 both land on 307 for the
hex-byte sum. Misses DATE ON WIRE entirely. Structurally elegant but
doesn't close with row 14's "twenty-six" signal.

---

### ★★★★ #7: **89** — DATEONWIRE king-path hex (raw)

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ✅ F-c | 🟡 S-g | ✅ H-a | ✅ D-a | ✅ I-a |

**Blurb:** King-path spelling THERE IS A DATE ON WIRE has hex-letter
sum 89 (= Actinium Z, incidentally a radioactive element). Scores 4/5
on strict axiom-count. Matches Actinium's thematic "dig deep" quality
(rare-earth extraction).

---

### ★★★★ #8: **79** — TUNES / axiom-length / Gold

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ⚠ F-c | ❌ | 🟡 H-e | ❌ | ✅ I-a |

**Blurb:** **Three independent grid-internal arcs** — (a) TUNES
alphabet sum (T+U+N+E+S = 20+21+14+5+19 = 79), (b) sum of all 5 axiom
string-lengths = 79, (c) atomic number of Gold (Au), the iconic
dig-for metal. Extremely strong thematically but does NOT follow the
literal procedure (no stride-6, no wire-date). The "answer" theory
here is that the axioms are decorative and 79 is the grid's actual
numerical output.

---

### ★★★★ #9: **33** — Col-6 hex / U-col / Vanadium / vinyl RPM

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| 🟡 F-a | ✅ S-c (col 6) | ✅ H-a | ❌ | ✅ I-a |

**Blurb:** Four arcs — (a) col 6 letter hex-sum = 33, (b) sum of U
column-positions across 7 U's = 33, (c) VANADIUM hex-letter sum (under
one convention) = 33, (d) vinyl LP play speed 33⅓ RPM ties to TUNES
theme. Satisfies STEP BY SIX via column-6 reading. Misses
DATE ON WIRE. Historically strong but not axiom-complete.

---

### ★★★★ #10: **59** — Col-6 hex + 26

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| 🟡 F-a | ✅ S-c | ✅ H-a | ✅ D-a | ✅ I-b |

**Blurb:** `33 + 26 = 59` — takes the well-supported 33 anchor and
adds the wire-date 26 (D-a additive). Satisfies 4-5 axioms depending
on how strict FIND THE START is read.

---

### ★★★★ #11: **105** — TUNES/axiom/Au + 26

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ⚠ F-c | ❌ | 🟡 | ✅ D-a | ✅ I-b |

**Blurb:** `79 + 26 = 105`. The 79 anchor plus the wire-date additive.
Only works if 79 is really the pre-date answer. 3/5 axioms.

---

### ★★★ #12: **49** — Dig-count + 26

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ❌ | ❌ | ❌ | ✅ D-a | ✅ I-b |

**Blurb:** `23 + 26 = 49`. 23 is the "dig count / missing V" anchor.
Only satisfies DATE ON WIRE. Weak.

---

### ★★★ #13: **23** — Dig count / Vanadium Z / missing V

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ❌ | ❌ | ❌ | ❌ | ✅ I-a |

**Blurb:** Zero axiom support procedurally. Pure thematic: "dig"
count in PWEI lyrics (one reading) = Vanadium Z = missing letter V's
alphabet position (22) plus 1, etc. Included because its thematic
density is unusually high (three cross-references) even though it
ignores the axioms.

**End of Part 3 (mid tier).**

---

## PART 4 — LOW TIER (0-1 axioms satisfied; thematic-only)

### ★★ #14: **47** — Silver Z (deliberately absent dig-metal)

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ❌ | ❌ | ❌ | ❌ | ✅ I-a |

**Blurb:** Silver's atomic number is 47. Silver is an archetypal
dig-metal but SILVER doesn't trace as a king-path in the grid — it's
conspicuously absent. Theory: the answer is the dig-metal you have to
*discover* by its absence. Zero axiom support; pure thematic guess.

---

### ★★ #15: **56** — Barium Z (33 + 23)

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ❌ | ❌ | ❌ | ❌ | ✅ I-a |

**Blurb:** `33 + 23 = 56`, which is Barium's Z. Barium is used in
drilling mud ("dig" theme). Combines the two strongest non-axiom
anchors. Arithmetic is post-hoc.

---

### ★★ #16: **46** — Palladium Z (79 − 33)

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ❌ | ❌ | ❌ | ❌ | ✅ I-a |

**Blurb:** `79 − 33 = 46` = Palladium Z. Pd is mined; fits the theme.
Subtraction feels post-hoc.

---

### ★★ #17: **44** — Ruthenium Z / PWEI dig count

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ❌ | ❌ | ❌ | ❌ | ✅ I-a |

**Blurb:** PWEI lyrics say "dig" 44 times (verified count; earlier
23 was wrong). Ruthenium Z = 44. Song-theme anchor only.

---

### ★ #18: **63** — Al + Sn (aluminothermic)

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ❌ | ❌ | ❌ | ❌ | ✅ I-a |

**Blurb:** Aluminum (13) + Tin (50) = 63. Both elements have strong
grid presence. Aluminothermic pair but arbitrary sum.

---

### ★ #19: **135** — 33 + 23 + 79

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ❌ | ❌ | ❌ | ❌ | ✅ I-a |

**Blurb:** Triple-sum of the three thematic anchors. Post-hoc; weak.

---

### ★ #20: **14** — Grid side

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ❌ | ❌ | ❌ | ❌ | ✅ I-a |

**Blurb:** The grid is 14×14. "Can U dig it?" is 14 characters. Also
= 20−6 (score minus six). Too trivial.

---

### ★ #21: **280** — 20 × 14

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ❌ | ❌ | ❌ | ❌ | ✅ I-a |

**Blurb:** Score (20) × grid side (14) = 280. Invokes "Alan Moore
knows the score" (PWEI lyric) × grid dimension. Arithmetic thematic
only.

---

### ★ #22: **720** — 36 × 20

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ❌ | ❌ | ❌ | ❌ | ✅ I-a |

**Blurb:** 36 (count of 0x14 bytes in image) × 20 (score) = 720. Very
speculative.

---

### ★ #23: **13** — Aluminum Z (anomalous diagonal)

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| 🟡 F-g | ❌ | ❌ | ❌ | ✅ I-a |

**Blurb:** The ALUMINUM diagonal at (2,8) is the grid's most anomalous
feature. Al's Z = 13. Pure thematic anchor.

---

### ★ #24: **65** — Q + V + Z missing letters

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ❌ | ❌ | ❌ | ❌ | ✅ I-a |

**Blurb:** Alphabet positions of the three missing letters
(17+22+26) = 65. Grid-internal but no axiom support.

---

### ★ #25: **112** — 14 × 8 (hyphen coords)

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ✅ F-c | ❌ | ❌ | 🟡 D-c | ✅ I-a |

**Blurb:** Hyphen at (14,8); product = 112 = Copernicium Z (rarely
dug, short half-life, less thematic). Uses the wire position.

---

### ★ #26: **18** — Argon Z

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ❌ | ❌ | 🟡 | ❌ | ✅ I-a |

**Blurb:** Step-6 on delta-rows gives 18 in one variant. Argon isn't
mined (it's a noble gas) — poor thematic fit.

---

### ★ #27: **50** — Tin Z

| F | S | H | D | I |
|:---:|:---:|:---:|:---:|:---:|
| ❌ | ❌ | ❌ | ❌ | ✅ I-a |

**Blurb:** Tin's Z = 50. Tin ties to "tin opener" pun in col 1
reversed. Pure thematic anchor.

**End of Part 4 (low tier).**

---

## PART 5 — REJECTED CORPUS (submitted and confirmed wrong)

These numbers have been tried and rejected. **Do NOT re-submit any of
them.** Each entry explains what derivation produced it and — where
possible — why the theory behind it fails.

### ✗ **600** — Alan Moore / Unearthing

**Theory:** Alan Moore's book *Unearthing* was published around 2006/2010;
the song name-drops "Alan Moore knows the score". Some chain produced
600 (likely 20 × 30, score × chart peak, or similar).

**Post-mortem:** Relies on external biographical trivia (book pub date,
chart peak) with no grid-internal derivation. MOORE doesn't king-path
trace. Rejected — external trivia is not the answer pathway.

---

### ✗ **7** — Count of U's

**Theory:** 7 U's in the grid; title says "Can **U** Dig It?" so count
U's.

**Post-mortem:** Too trivial; ignores the 14×14 structure, the axioms,
and row 14. A 7-letter single-datum answer is almost never the solution
to a meta-puzzle.

---

### ✗ **3241** — WT22 variant

**Theory:** Variant of the Wire-Tapper-22 hex-track-durations chain
(the original 3242 AI report).

**Post-mortem:** Invalidates by being one-off ad-hoc arithmetic on
top of an already ad-hoc chain. External music-trivia dependency.

---

### ✗ **3242** — Wire-Tapper-22 hex track durations

**Theory:** Sum of Wire Tapper Vol. 22 compilation track durations,
with tracks 1/7/13/19 read in hex and the rest decimal, plus various
adjustments.

**Post-mortem:** The original AI-generated "answer". Rejected by the
community for being unmotivated (why those track numbers? why switch
bases?). External data + arbitrary rules. Classic overfitting.

---

### ✗ **26** — Row-14 phonetic

**Theory:** Row 14 spells "twenty-six" → answer is 26.

**Post-mortem:** Too direct. Also, 26 = Iron's Z, but Iron isn't
thematically central. **However**, this rejection IS the clue that led
to the Mozart K.184 discovery: 26 isn't the answer *directly*, it's an
INDEX into the Köchel catalogue → Symphony No. 26 → K. 184.

---

### ✗ **22** — V alphabet-position / hyphen 14+8

**Theory:** V is alphabet letter 22; hyphen at (14,8), 14+8=22.

**Post-mortem:** Coincidental convergence. The V-alphabet reading
requires external knowledge; the 14+8 is a pure coord arithmetic with
no axiom backing.

---

### ✗ **134** — Unspecified step-6 variant

**Theory:** Some step-6 starting cell yields 134.

**Post-mortem:** Arbitrary start cell; no FIND THE START principle
justifies it.

---

### ✗ **167** — Step-6 hex from first hex-letter

**Theory:** Start at first hex letter (`d` at (1,3)) in reading order,
step 6 through flat grid, sum a-f values = 167. Claimed all-5-axioms
satisfaction; also 167 was supposedly the flat-position of the last
cell of the LAST-ENTRY-ENTIRE-INTEGER king-path.

**Post-mortem:** The self-referential story was compelling but WRONG.
Lesson: multiple "axiom-satisfying" mechanics can coincide on the same
wrong number. This rejection demoted all 167-derivatives (2192, 2193)
and made us suspect **the grid isn't the correct dataset — the image
is**. The discovery pivot to image step-6 (yielding 184) followed
this failure.

---

### ✗ **2180** — Gemini's step-6 from flat-pos 8 + 2026

**Theory:** Step-6 hex from flat position 8 (`t` at (1,9)) yields
154; add 2026 = 2180.

**Post-mortem:** Arbitrary start (pos 8); +2026 mechanic unsupported.
Gemini's attempt at a self-contained chain, but the start position
was not principled.

---

### ✗ **2192** — 167 + 2025

**Theory:** Step-6 hex from first hex letter → 167; add 2026−1 = 2192
(off-by-one on year).

**Post-mortem:** 167 base is wrong; any additive on it fails.

---

### ✗ **2193** — 167 + 2026

**Theory:** 167 + 2026 (full year addition).

**Post-mortem:** Same base failure as 2192. **Crucial empirical
finding:** the fact that this fails is strong evidence that **adding
2026 calendar-year is NOT the correct DATE ON WIRE mechanic**. This
result specifically motivated the pivot to treating the date as 26
(not 2026) or as an index (not an additive).

---

### Pattern observed across failures

1. **Adding 2026 to anything has never worked.** 2180, 2192, 2193 all
   failed. This narrows the DATE ON WIRE interpretation toward either
   26-additive, 26-as-index, or date-as-metadata-only.
2. **Step-6 on the grid (flat) has consistently failed.** 167 and
   its relatives. This motivated the pivot to step-6 on the image
   bytes (yielding 184).
3. **External-trivia chains have all failed.** 600, 3241, 3242.
   The answer is either fully grid-internal or grid+image-internal.
4. **Single-number trivial answers have failed.** 7, 22, 26. The
   answer is probably a multi-digit number that genuinely composes
   multiple anchors.

**End of Part 5 (rejected corpus).**

---

## PART 6 — Final recommendation and submission order

### Scorecard summary

| Rank | Value | Axioms ✅ | Thematic | Submit priority |
|---:|---:|:---:|:---:|:---:|
| 1 | **184** | 5/5 | ★★★★★★ | **SUBMIT FIRST** |
| 2 | 210 | 5/5 | ★★★ | 2nd |
| 3 | 333 | 5/5 | ★★★★ | 3rd (if +26 additive) |
| 4 | 115 | 4/5 | ★★★ | 4th |
| 5 | 2210 | 4/5 (🟡 on 2) | ★★★ | 5th (+2026 fallback) |
| 6 | 307 | 3/5 | ★★★ | 6th |
| 7 | 89 | 4/5 | ★★★ | 7th |
| 8 | 79 | 1/5 | ★★★★★ | 8th (thematic gold-std) |
| 9 | 33 | 3/5 | ★★★★ | 9th |
| 10 | 59 | 4/5 | ★★★ | 10th (33 + 26) |
| 11 | 105 | 2/5 | ★★★ | 11th (79 + 26) |
| 12 | 49 | 1/5 | ★★ | 12th |
| 13 | 23 | 0/5 | ★★★★ | 13th |

### Suggested submission order (REVISED after Mozart extensions)

```
1.  184    ← K.184 Symphony 26 "Tune 26" (image step-6 + Köchel)
2.  47     ← Strict-hex step-6 from byte 26 = Silver (absent dig-metal)
3.  626    ← K.626 Requiem (LAST ENTRY of Köchel catalogue)
4.  622    ← K.622 Clarinet Concerto (last step-6 entry from K.184)
5.  551    ← K.551 Jupiter (last symphony)
6.  210    ← 184 + 26 additive
7.  345    ← K.184 + K.161a (dual catalogue sum)
8.  333    ← Track6+Al step-6 + 26
9.  115    ← DATEONWIRE hex + 26
10. 1006   ← Symphonies 26,32,38 K-sum
```

### If all top 10 fail — pivots

1. **Return to the original puzzle image** (PNG/PDF) and check for
   visual features not captured in the plain-text grid (colored cells,
   highlights, circled letters).

2. **Interpret STEP BY SIX as the Köchel index**: if "Tune 26" →
   K.184 worked for Symphony 26, maybe other hidden "Tune N" references
   exist and the axioms pick one. Look for other embedded tune/symphony
   numbers.

3. **Re-examine "LAST ENTRY ENTIRE INTEGER"**: could mean "the last
   K-number in the Mozart Symphony list" (K.551, the Jupiter Symphony).
   That would make the answer 551 rather than 184.

4. **Check the PWEI album position**: "Can U Dig It?" is Track 6; the
   album is *This Is the Day*. What's its catalog number in the band's
   discography? A matching cross-reference.

### Why 184 first

1. ✅ Literally satisfies all 5 axioms under principled readings
2. ✅ Has three independent closure arcs (image mechanic, Köchel
   catalogue, element-sum)
3. ✅ Explains the row-14 "twenty-six" signal as an INDEX, not an
   additive (consistent with 2192/2193 failures)
4. ✅ Explains the "tune" prefix in row 14 (TUNE + 26 = Symphony 26)
5. ✅ The K.184 target is itself a clean integer pointing to a real,
   unique cultural entity (a Mozart symphony)
6. ✅ Mozart symphony theme closes the loop with "TUNES" in row 14

### Why the prior #1 (167) was wrong (lesson learned)

The 167 theory satisfied all 5 axioms via a self-referential closure
(final cell position = sum). But it relied on STEP BY SIX on the grid
bytes, and the sum was purely grid-internal. The puzzle almost
certainly wanted the procedure applied to the IMAGE bytes (the raw
JPEG `raw_header` — which is why the image was even embedded with
visible hex). 167 was a siren song: elegant math on the wrong dataset.
184 corrects the dataset choice and adds the Köchel cultural layer.

### Final notes

- **Never re-submit** any number from Part 5.
- After each submission update this file (add failed number to Part 5,
  re-rank remaining candidates) and re-commit.
- If 184 succeeds, document the full solve path in `SUMMARY.md` so
  future Jane Street puzzles benefit from the Mozart-cross-reference
  lesson.

**End of CANDIDATES.md — latest rewrite 2026-04-20.**
