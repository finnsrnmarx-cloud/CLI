"""MAJOR PIVOT — 'Can U Dig It' literal reading.

  Can     = a literal metal CAN (soda, oil, spray, tin, aluminum, ...)
  U Dig It = U-shaped DIGIT — either a numeric digit system (hex, binary,
            base-ten) OR a body digit (thumb, pinky, ring toe, hallux).

Each pair of "Can" + "Digit" words traces a **D-shape** in the grid
(one word = the straight back of the D, the other = the curve).

The letters NOT used in any D-pair form a sentence ("drawn a blank" —
literally the blanks in the grid form the clue). The sentence ends in
"twenty-six". The answer is an integer decoded from that sentence.

This script:
  1. Parses all 12 D-pairs from the solver's path notation
  2. Computes the set of USED cells
  3. Prints UNUSED cells in row-major order (the clue)
"""
from __future__ import annotations
from typing import Iterable

GRID = [
    "rsdifindthsart",  # row 1
    "ehresodaeetgna",  # row 2
    "netrhalxhgowip",  # row 3
    "egedauyueaenrp",  # row 4
    "ptnnmllmxidnee",  # row 5
    "ohuinkthanacsm",  # row 6
    "alnpfyldebsttn",  # row 7
    "uumjarebemehrw",  # row 8
    "mithdceigiugts",  # row 9
    "tlamibftotegeet"[:14],  # row 10 ("tlamibftotegeet" -> trim) actually: tlamibftotegeEt
    "sailniitniapen",  # row 11
    "nstoagrniiobrt",  # row 12
    "ietiryeesprayw",  # row 13
    "tunenty-tessix",  # row 14
]
# Fix row 10 from the grid image: t l a m i b f t o t e g e t
GRID[9] = "tlamibftotegeT".lower()  # ends in 't' (col 14)
assert all(len(r) == 14 for r in GRID), [len(r) for r in GRID]


def col_letter_to_idx(L: str) -> int:
    """Excel-style A=1 .. N=14."""
    return ord(L.upper()) - ord('A') + 1


def parse_cell(token: str) -> tuple[int, int]:
    """e.g. 'H2' -> (row=2, col=8)"""
    token = token.strip()
    # col letters are [A-Z]+, rest is row digits
    i = 0
    while i < len(token) and token[i].isalpha():
        i += 1
    col_s, row_s = token[:i], token[i:]
    return (int(row_s), col_letter_to_idx(col_s))


def cells_between(a: tuple[int, int], b: tuple[int, int]) -> list[tuple[int, int]]:
    """All grid cells on the straight king-line from a to b (inclusive)."""
    (r1, c1), (r2, c2) = a, b
    dr = (r2 > r1) - (r2 < r1)
    dc = (c2 > c1) - (c2 < c1)
    steps = max(abs(r2 - r1), abs(c2 - c1))
    out = []
    for k in range(steps + 1):
        out.append((r1 + k * dr, c1 + k * dc))
    return out


def parse_path(path_s: str) -> list[tuple[int, int]]:
    """Parse solver notation like 'H2->A9' or 'L7->L8,K9,J8->J7'.

    Commas separate disjoint SEGMENTS; arrows join endpoints of
    straight king-moves.
    """
    cells: list[tuple[int, int]] = []
    for segment in path_s.split(','):
        segment = segment.strip()
        if '->' in segment:
            pts = [parse_cell(x) for x in segment.split('->')]
            for a, b in zip(pts, pts[1:]):
                seg_cells = cells_between(a, b)
                # avoid duplicating the junction point when chained
                if cells and cells[-1] == seg_cells[0]:
                    cells.extend(seg_cells[1:])
                else:
                    cells.extend(seg_cells)
        else:
            cells.append(parse_cell(segment))
    return cells


# The solver's 12 D-pairs
PAIRS = [
    ("aluminum",    "H2->A9",                "hexadecimal", "I3->I6->E10->B10"),
    ("can",         "L6->J6",                "thumb",       "L7->L8,K9,J8->J7"),
    ("end",         "M5->K5",                "ring toe",    "M4->M2->K2->K4"),
    ("fire",        "G10->G13",              "binary",      "F10->E10->E13->F13"),
    ("jar",         "D8->F8",                "pinky",       "D7->D6->F6->F7"),
    ("opener",      "A6->A1",                "hundreds",    "B6->C6,D5->D2,C1->B1"),
    ("paint",       "L11->H11",              "base ten",    "L12->L13,K14->I14,H13->H12"),
    ("soda",        "E2->H2",                "hallux",      "E3->E4,F5->G5,H4->H3"),
    ("spray",       "I13->M13",              "integer",     "I12->I11,J10->L10,M11->M12"),
    ("tin",         "A14->A12",              "units",       "B14->C14,D13,C12->B12"),
    ("trash",       "N1->J1",                "appendage",   "N2->N4,M5->K5,J4->J2"),
    ("oil",         "D12->B10",              "tens",        "C13->B13->A12->A11"),
]


def show_grid_with_letters(cells: Iterable[tuple[int, int]], label: str = ""):
    marked = set(cells)
    print(f"\n=== {label} ({len(marked)} cells marked) ===")
    for r in range(1, 15):
        row_s = ""
        for c in range(1, 15):
            ch = GRID[r - 1][c - 1]
            row_s += (f" [{ch}]" if (r, c) in marked else f"  {ch} ")
        print(f"row {r:2d}:{row_s}")


def verify_word(word: str, cells: list[tuple[int, int]]) -> str:
    letters = "".join(GRID[r - 1][c - 1] for r, c in cells)
    word_clean = word.replace(" ", "").lower()
    ok = "✓" if letters == word_clean else "✗"
    return f"  {ok} {word:<12} {len(cells)} cells → {letters!r}  (expected {word_clean!r})"


def main():
    all_used: set[tuple[int, int]] = set()

    print("PAIR-BY-PAIR VERIFICATION")
    for can_word, p1, dig_word, p2 in PAIRS:
        c1 = parse_path(p1)
        c2 = parse_path(p2)
        print(f"\n[{can_word} / {dig_word}]")
        print(verify_word(can_word, c1))
        print(verify_word(dig_word, c2))
        all_used |= set(c1)
        all_used |= set(c2)

    print(f"\n\nTotal USED cells: {len(all_used)} / 196")

    # Unused cells in row-major order
    unused = []
    for r in range(1, 15):
        for c in range(1, 15):
            if (r, c) not in all_used and GRID[r - 1][c - 1] != '-':
                unused.append((r, c, GRID[r - 1][c - 1]))

    print(f"UNUSED cells: {len(unused)}")
    print("Unused letters in reading order:")
    print("  " + "".join(x[2] for x in unused))

    show_grid_with_letters([(r, c) for r, c, _ in unused], "UNUSED (drawn a blank)")
    show_grid_with_letters(all_used, "USED (in D-pairs)")

    # Also print with spaces between row boundaries
    print("\nUnused by row:")
    for r in range(1, 15):
        row_letters = "".join(GRID[r - 1][c - 1] for c in range(1, 15) if (r, c) not in all_used and GRID[r - 1][c - 1] != '-')
        print(f"  row {r:2d}: {row_letters}")


if __name__ == "__main__":
    main()
