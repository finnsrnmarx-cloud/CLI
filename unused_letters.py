"""Compute which grid cells are covered by the solver's 12 verified D-pairs
and print the remaining unused letters in reading order — those are the
'drawn a blank' clue candidates.

Then try plugging in NEW candidate words found by find_more_words.py to
see whether any of them removes 'noise' letters and leaves a cleaner clue.
"""
from __future__ import annotations

GRID = [
    list("rsdifindthsart"),
    list("ehresodaeetgna"),
    list("netrhalxhgowip"),
    list("egedauyueaenrp"),
    list("ptnnmllmxidnee"),
    list("ohuinkthanacsm"),
    list("alnpfyldebsttn"),
    list("uumjarebemehrw"),
    list("mithdceigiugts"),
    list("tlamibftoteget"),
    list("sailniitniapen"),
    list("nstoagrniiobrt"),
    list("ietiryeesprayw"),
    list("tunenty-tessix"),
]

def cell(code):
    # 'A6' -> (5, 0) ; row is 1-based number, col is letter A..N
    col = ord(code[0]) - ord('A')
    row = int(code[1:]) - 1
    return (row, col)

def path_cells(codes):
    return [cell(c) for c in codes]

# Solver's 12 verified pairs — paths use CORRECT cell traversals
# matching the arrows shown in the user's image.
PAIRS = {
    # aluminum: H2->A9 is a diagonal SW
    "aluminum":    "H2,G3,F4,E5,D6,C7,B8,A9".split(","),
    # hexadecimal: I3-I6 (down), then down-left diagonal to B10
    "hexadecimal": "I3,I4,I5,I6,H7,G8,F9,E10,D10,C10,B10".split(","),
    # can: L6->J6 is 3 cells horizontal
    "can":         "L6,K6,J6".split(","),
    # thumb: L7,L8,K9,J8,J7
    "thumb":       "L7,L8,K9,J8,J7".split(","),
    # end: M5->K5 -> so M5,L5,K5
    "end":         "M5,L5,K5".split(","),
    # ring toe: M4->M2->K2->K4 (three-segment)
    "ringtoe":     "M4,M3,M2,L2,K2,K3,K4".split(","),
    # fire: G10->G13 (vertical down)
    "fire":        "G10,G11,G12,G13".split(","),
    # binary: F10->E10->E13->F13 (4-letter? no binary=6)
    # b-i-n-a-r-y: F10=b,E10=i,E11=n,E12=a,E13=r,F13=y → confirmed
    "binary":      "F10,E10,E11,E12,E13,F13".split(","),
    # jar: D8->F8 = D8,E8,F8
    "jar":         "D8,E8,F8".split(","),
    # pinky: D7->D6->F6->F7  (p-i-n-k-y) → D7=p,D6=i... wait let me check
    # Actually pinky=5 letters. Path D7,D6,E6,F6,F7 earlier — more likely
    "pinky":       "D7,D6,E6,F6,F7".split(","),
    # opener: A6->A1 (vertical up)
    "opener":      "A6,A5,A4,A3,A2,A1".split(","),
    # hundreds: B6->C6,D5->D2,C1->B1
    # h-u-n-d-r-e-d-s = 8 letters
    "hundreds":    "B6,C6,D5,D4,D3,D2,C1,B1".split(","),
    # paint: L11->H11 (horizontal)
    "paint":       "L11,K11,J11,I11,H11".split(","),
    # base ten: L12->L13,K14->I14,H13->H12 (7 letters: b-a-s-e-t-e-n)
    "baseten":     "L12,L13,K14,J14,I14,H13,H12".split(","),
    # soda: E2->H2 (horizontal)
    "soda":        "E2,F2,G2,H2".split(","),
    # hallux: E3->E4,F5->G5,H4->H3 (6 letters h-a-l-l-u-x)
    "hallux":      "E3,E4,F5,G5,H4,H3".split(","),
    # spray: I13->M13 (horizontal)
    "spray":       "I13,J13,K13,L13,M13".split(","),
    # integer: I12->I11,J10->L10,M11->M12 (7 letters i-n-t-e-g-e-r)
    "integer":     "I12,I11,J10,K10,L10,M11,M12".split(","),
    # tin: A14->A12 (vertical up)
    "tin":         "A14,A13,A12".split(","),
    # units: B14->C14,D13,C12->B12 (5 letters u-n-i-t-s)
    "units":       "B14,C14,D13,C12,B12".split(","),
    # trash: N1->J1 (horizontal)
    "trash":       "N1,M1,L1,K1,J1".split(","),
    # appendage: N2->N4,M5->K5,J4->J2 (9 letters a-p-p-e-n-d-a-g-e)
    "appendage":   "N2,N3,N4,M5,L4,K5,J4,J3,J2".split(","),
    # oil: D12->B10 (diagonal)
    "oil":         "D12,C11,B10".split(","),
    # tens: C13->B13->A12->A11 — but A12 overlaps with tin!
    # t-e-n-s = 4 letters. Let me use C13,B13,A12,A11 for the literal path
    "tens":        "C13,B13,A12,A11".split(","),
}

# Track coverage (only include paths where cells are actually valid)
covered = set()
for w, codes in PAIRS.items():
    for (r, c) in path_cells(codes):
        covered.add((r, c))
print(f"Covered cells: {len(covered)} / 196")

# Unused cells in reading order
unused = []
for r in range(14):
    for c in range(14):
        if (r, c) not in covered and GRID[r][c] != '-':
            unused.append((r, c, GRID[r][c]))
unused_str = "".join(x[2] for x in unused)
print(f"\nUnused letter stream ({len(unused)} letters):")
print("  " + unused_str)

# Dump per-row uncovered cells
print("\nUncovered cells per row (A=col1..N=col14):")
for r in range(14):
    row_unused = [(c, GRID[r][c]) for c in range(14) if (r, c) not in covered and GRID[r][c] != '-']
    if row_unused:
        cells = ", ".join(f"{chr(ord('A')+c)}{r+1}={L}" for c, L in row_unused)
        letters = "".join(L for _, L in row_unused)
        print(f"  Row {r+1:>2} [{letters:>15}]  {cells}")

# Now plug in new candidate words to see what they'd remove
NEW_CANDIDATES = {
    # from find_more_words.py
    "case":    "L6,K6,K7,K8".split(","),
    "base":    "J7,K6,K7,K8".split(","),
    "tray":    "N12,M12,L13,M13".split(","),
    "bag":     "L12,K11,L10".split(","),
    "bin":     "F10,E10,E11".split(","),
    "mug":     "J8,K9,L9".split(","),
    "pan":     "N3,N2,M2".split(","),
    "pot":     "A5,A6,B5".split(","),
    "decimal": "H7,G8,F9,E10,D10,C10,B10".split(","),
    "pointer": "L11,K12,J11,I11,H10,G9,F8".split(","),
    "finger":  "E7,D6,C5,B4,B3,C2".split(","),
    "index":   "F1,G1,H1,I2,H3".split(","),
    "hand":    "E3,E4,D5,D4".split(","),
    "nail":    "A12,B11,C11,B10".split(","),
    "ones":    "K3,L4,M5,M6".split(","),
    "ring":    "M4,M3,M2,L2".split(","),
    "hex":     "J1,I2,H3".split(","),
    "toe":     "K2,K3,J2".split(","),
    "nineteen":"C5,D6,D5,C4,C3,B3,A2,A3".split(","),
    "ninth":   "D5,D6,C5,B5,B6".split(","),
    "tenth":   "C3,C4,C5,B5,B6".split(","),
    "find":    "E1,F1,G1,H1".split(","),
    "six":     "L14,M14,N14".split(","),
    "to":      "K2,K3".split(","),
    "three":   "C3,B2,A1,A2,B3".split(","),
    "nine":    "M2,M3,L4,K4".split(","),
    "one":     "K3,L4,K4".split(","),
    "ten":     "C3,B3,A3".split(","),
    "two":     "K2,L3,K3".split(","),
}

print(f"\nNew candidate words: {len(NEW_CANDIDATES)}")
print("Each one's cells and which are ALREADY covered:\n")
for w, codes in NEW_CANDIDATES.items():
    cells = path_cells(codes)
    overlapping = [c for c in cells if c in covered]
    new_cells = [c for c in cells if c not in covered]
    print(f"  {w:<10} len={len(cells):<2} already_covered={len(overlapping)}  new={len(new_cells)}")

# What happens to the unused stream if we add each NEW word individually
print("\n=== Effect of adding each new word ===")
for w, codes in NEW_CANDIDATES.items():
    cells = set(path_cells(codes))
    new_covered = covered | cells
    new_unused = []
    for r in range(14):
        for c in range(14):
            if (r, c) not in new_covered and GRID[r][c] != '-':
                new_unused.append(GRID[r][c])
    removed = len(unused) - len(new_unused)
    if removed > 0:
        stream = "".join(new_unused)
        print(f"  +{w:<10} (-{removed:<2} letters)  unused -> {stream}")

# Try several cumulative combinations
print("\n=== CUMULATIVE: add the strongest new candidates ===")
# Strongest: pointer, finger, index, case, nineteen, tenth, tray, nail, ones, mug, pot
for combo_name, combo_words in [
    ("+pointer",                     ["pointer"]),
    ("+finger",                      ["finger"]),
    ("+pointer +finger",             ["pointer","finger"]),
    ("+index +case +base",           ["index","case","base"]),
    ("+nineteen +tenth",             ["nineteen","tenth"]),
    ("ALL NEW",                      list(NEW_CANDIDATES.keys())),
    ("ordinals_only",                ["ninth","tenth","nineteen","three","nine","ten","one","two"]),
    ("containers_only",              ["case","tray","bag","bin","mug","pan","pot"]),
    ("digits_only",                  ["decimal","pointer","finger","index","base","hand","nail","ones","ring","hex","toe"]),
]:
    new_covered = set(covered)
    for w in combo_words:
        if w in NEW_CANDIDATES:
            new_covered.update(path_cells(NEW_CANDIDATES[w]))
    new_unused = []
    for r in range(14):
        for c in range(14):
            if (r, c) not in new_covered and GRID[r][c] != '-':
                new_unused.append(GRID[r][c])
    stream = "".join(new_unused)
    print(f"  {combo_name:<28} ({len(new_unused):>2} letters)  {stream}")
