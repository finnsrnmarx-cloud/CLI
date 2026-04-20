"""Cleaner output — unambiguous unused letter extraction."""
from solve_d_pairs import PAIRS, parse_path, GRID

used = set()
for _, p1, _, p2 in PAIRS:
    used |= set(parse_path(p1))
    used |= set(parse_path(p2))

print(f"Total cells used: {len(used)} / 196")
print(f"Unused letter cells: {196 - len(used) - 1} (excluding hyphen)\n")

print("=== GRID — uppercase = USED in D-pairs, lowercase = UNUSED (drawn a blank) ===\n")
for r in range(1, 15):
    line = []
    for c in range(1, 15):
        ch = GRID[r - 1][c - 1]
        if ch == '-':
            line.append('─')
        elif (r, c) in used:
            line.append(ch.upper())
        else:
            line.append(ch.lower())
    print(f"row {r:2d}:  {' '.join(line)}")

# Dump unused letters in reading order
print("\n=== UNUSED letters (the hidden clue) ===\n")
by_row = []
for r in range(1, 15):
    row_unused = [GRID[r - 1][c - 1] for c in range(1, 15)
                  if (r, c) not in used and GRID[r - 1][c - 1] != '-']
    by_row.append(''.join(row_unused))

for r, letters in enumerate(by_row, 1):
    print(f"  row {r:2d}: '{letters}'")

full = ''.join(by_row)
print(f"\nConcatenated ({len(full)} letters):")
print(f"  '{full}'")

# Print with spaces inserted between words guess
print("\nSearching for common phrases...")
for phrase in ["find the", "smallest number", "with digits",
               "totaling twenty", "twenty six", "twenty-six",
               "number with", "three",
               "largest", "prime", "perfect", "square",
               "odd", "even", "sum", "total"]:
    # Check if phrase appears as subsequence in unused letters
    p_clean = phrase.replace(" ", "").replace("-", "").lower()
    f_clean = full.lower()
    if p_clean in f_clean:
        idx = f_clean.index(p_clean)
        print(f"  ✓ '{phrase}' found as CONTIGUOUS substring at pos {idx}")
    else:
        # As subsequence
        i = j = 0
        while i < len(f_clean) and j < len(p_clean):
            if f_clean[i] == p_clean[j]:
                j += 1
            i += 1
        if j == len(p_clean):
            print(f"  ~ '{phrase}' found as subsequence")
        else:
            print(f"  ✗ '{phrase}' NOT found (missing chars)")
