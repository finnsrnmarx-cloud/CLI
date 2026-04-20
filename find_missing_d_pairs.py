"""Hunt for missing D-pair candidates.

The solver has 12 pairs; the 73-letter unused string still contains
noise. Missing D-pairs would consume the noise and reveal the real
clue. Search for:

  - Things-in-a-can words (not yet used)
  - Digit words (body parts OR number systems) not yet used

as king-paths restricted to currently-UNUSED cells.
"""
from __future__ import annotations
from solve_d_pairs import PAIRS, parse_path, GRID

USED = set()
for _, p1, _, p2 in PAIRS:
    USED |= set(parse_path(p1))
    USED |= set(parse_path(p2))

# Unused cells -> letter lookup
UNUSED = {}
for r in range(1, 15):
    for c in range(1, 15):
        if (r, c) not in USED and GRID[r - 1][c - 1] != '-':
            UNUSED[(r, c)] = GRID[r - 1][c - 1]

print(f"Unused cells: {len(UNUSED)}")
print("Unused positions by letter:")
from collections import defaultdict
by_letter = defaultdict(list)
for (r, c), ch in UNUSED.items():
    by_letter[ch].append((r, c))
for ch in sorted(by_letter):
    print(f"  '{ch}': {by_letter[ch]}")


def king_neighbors(r, c):
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 1 <= nr <= 14 and 1 <= nc <= 14:
                yield nr, nc


def find_word_paths(word: str, restrict_to=None):
    """All king-paths spelling `word` using distinct cells.
    If restrict_to is given, only cells in that set are eligible.
    """
    word = word.lower()
    results = []
    # Starting cells must match first letter
    for (r, c), ch in (restrict_to or {}).items() if restrict_to else [((r, c), GRID[r-1][c-1]) for r in range(1,15) for c in range(1,15) if GRID[r-1][c-1] != '-']:
        if ch != word[0]:
            continue
        stack = [(r, c, [(r, c)])]
        while stack:
            cr, cc, path = stack.pop()
            if len(path) == len(word):
                results.append(path)
                continue
            needed = word[len(path)]
            for nr, nc in king_neighbors(cr, cc):
                if (nr, nc) in path:
                    continue
                if restrict_to and (nr, nc) not in restrict_to:
                    continue
                if GRID[nr - 1][nc - 1] != needed:
                    continue
                stack.append((nr, nc, path + [(nr, nc)]))
    return results


# Candidate words to test
CAN_WORDS = [
    "beer", "wine", "soup", "stew", "cola", "oil",
    "pork", "ham", "spam", "tuna", "peas", "beans",
    "corn", "jam", "mixer", "sauce", "broth",
    "tea", "water", "milk", "juice", "honey",
    "wax", "cork", "pail",
]
DIGIT_WORDS = [
    # Numeric bases
    "octal", "decimal", "ternary", "duodecimal", "dozenal",
    "thousands", "millions", "power",
    # Body digits
    "thumb", "index", "middle", "ring", "pinky", "little",
    "finger", "toe", "hallux", "pointer",
    "limb", "phalanx", "nail",
    # Number-related
    "whole", "prime", "integer",  # integer already used
    "odd", "even", "sum", "count",
]

print("\n\n=== Checking CAN_WORDS in unused cells ===")
for w in CAN_WORDS:
    paths = find_word_paths(w, UNUSED)
    if paths:
        print(f"  {w}: {len(paths)} path(s)")
        for p in paths[:3]:
            print(f"    {p}")

print("\n=== Checking DIGIT_WORDS in unused cells ===")
for w in DIGIT_WORDS:
    paths = find_word_paths(w, UNUSED)
    if paths:
        print(f"  {w}: {len(paths)} path(s)")
        for p in paths[:3]:
            print(f"    {p}")

# Also try long words that might be the clue "the smallest number"
print("\n=== Long clue-ish words in unused cells (might be missing pairs) ===")
for w in ["smallest", "largest", "number", "three", "nine", "eight",
          "digits", "totaling", "twenty", "subtract", "add", "multiply"]:
    paths = find_word_paths(w, UNUSED)
    if paths:
        print(f"  {w}: {len(paths)} path(s)")
        for p in paths[:2]:
            print(f"    {p}")
