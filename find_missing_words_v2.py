"""Exhaustive search: what words/phrases can we king-path-trace
through the 24 extras that remain after matching the base sentence?"""
from solve_d_pairs import PAIRS, parse_path, GRID

used = set()
for _, p1, _, p2 in PAIRS:
    used |= set(parse_path(p1))
    used |= set(parse_path(p2))

letters = ''.join(GRID[r-1][c-1] for r in range(1,15) for c in range(1,15)
                  if (r,c) not in used and GRID[r-1][c-1] != '-')

# Extras after matching base sentence
h = "ifindthesmallestnumberwithdigitstotalingtwentysix"
unused_positions = [(r,c, GRID[r-1][c-1]) for r in range(1,15) for c in range(1,15)
                    if (r,c) not in used and GRID[r-1][c-1] != '-']
matched = [False] * len(letters)
j = 0
for i in range(len(letters)):
    if j < len(h) and letters[i] == h[j]:
        matched[i] = True; j += 1

EXTRA_CELLS = {(unused_positions[k][0], unused_positions[k][1]): unused_positions[k][2]
               for k in range(len(letters)) if not matched[k]}
print(f"Extras ({len(EXTRA_CELLS)} cells):\n  {dict(sorted(EXTRA_CELLS.items()))}\n")

# King-neighbor helper
def king_neighbors(r, c):
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if not (dr == dc == 0):
                nr, nc = r+dr, c+dc
                if 1 <= nr <= 14 and 1 <= nc <= 14:
                    yield nr, nc

# Find king-paths for a word (within restricted cell set)
def find_paths(word, cells_set, allow_letter_map):
    """Returns list of paths (each a list of (r,c)). `allow_letter_map`
    maps (r,c) -> letter."""
    word = word.lower()
    results = []
    for (r,c), ch in allow_letter_map.items():
        if ch != word[0]: continue
        stack = [(r, c, [(r,c)])]
        while stack:
            cr, cc, path = stack.pop()
            if len(path) == len(word):
                results.append(path); continue
            needed = word[len(path)]
            for nr, nc in king_neighbors(cr, cc):
                if (nr, nc) in path or (nr, nc) not in cells_set: continue
                if allow_letter_map.get((nr, nc)) != needed: continue
                stack.append((nr, nc, path + [(nr, nc)]))
    return results

# Try a LOT of candidate words (can / digit themes)
CANDIDATE_WORDS = [
    # Can things
    "beef", "ham", "wax", "foam", "seltzer", "ginger", "syrup",
    "wine", "rum", "gin", "port",
    "gravy", "honey", "tea", "milk",
    "oats", "flour", "meat", "corn", "yeast",
    "wet", "dry", "mist",
    # Digit things
    "ring", "little", "middle", "index", "pinkie",
    "great toe", "second toe", "third toe", "fourth toe",
    "fingers", "toes",
    "nail", "pad", "tip",
    "digit", "limb",
    # Numeric systems / sizes
    "ones", "tens", "hundreds", "thousand", "thousands", "millions",
    "mantissa", "fraction",
    "metric",
    "big", "small", "large", "tiny",
    # Generic short words for testing
    "regent", "retina", "eighty", "weight", "wight", "tight",
    "eight", "nine", "ten", "twelve", "thirty",
    "went", "north", "south", "east", "west",
    # Pairs expected
    "fig", "ether", "ether", "meter", "timer", "meter",
    "fret", "fret", "gnat",
    "yearn", "earn",
    "game", "tame", "name",
]

print("=== Words traceable as king-paths within the 24 extras ===\n")
for w in sorted(set(CANDIDATE_WORDS)):
    p = find_paths(w, set(EXTRA_CELLS.keys()), EXTRA_CELLS)
    if p:
        print(f"  '{w}' ({len(w)}): {len(p)} path(s)")
        for path in p[:2]:
            print(f"    {path}")

# Specifically look at compact clusters
print("\n=== Cluster analysis ===")
# Visualise extras as a dense subgrid
extras_sorted = sorted(EXTRA_CELLS.keys())
print("Top-left cluster (rows 2-5, cols 2-3):")
tl = [(r,c) for (r,c) in extras_sorted if 2<=r<=5 and 2<=c<=3]
print(f"  cells: {tl}")
print(f"  letters: {[EXTRA_CELLS[p] for p in tl]}")

print("\nRow 3-4 col 6-7:")
mid = [(r,c) for (r,c) in extras_sorted if 3<=r<=4 and 6<=c<=7]
print(f"  cells: {mid}")
print(f"  letters: {[EXTRA_CELLS[p] for p in mid]}")

print("\nRow 3-5 col 12-14:")
right = [(r,c) for (r,c) in extras_sorted if 3<=r<=5 and 12<=c<=14]
print(f"  cells: {right}")
print(f"  letters: {[EXTRA_CELLS[p] for p in right]}")
