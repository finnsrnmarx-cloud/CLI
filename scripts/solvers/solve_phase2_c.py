"""Phase 2c — Self-referential convergence on 167.

The LAST cell of LASTENTRYENTIREINTEGER is at flat-index 167 (1-based).
The step-6-hex-sum from first hex letter is also 167.

This suggests 167 is self-consistent: the path sum itself equals the
target's position. A beautifully cyclic puzzle.

This script:
  1. Verifies 167 convergence from both directions
  2. Computes the actual path the algorithm traverses
  3. Checks whether 167 or 2193 is the intended final value
  4. Cross-checks with all-metal-sums (82 Pb, 79 Au, 33 etc.)
"""

from __future__ import annotations

GRID_RAW = """
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
""".strip()

G = [r.split() for r in GRID_RAW.splitlines()]
H, W = 14, 14
HEX = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}

# Build flat string (skipping hyphen)
flat = []
flat_pos = []
for r in range(H):
    for c in range(W):
        if G[r][c] != "-":
            flat.append(G[r][c])
            flat_pos.append((r+1, c+1))
flat_str = "".join(flat)

# Start position: first hex letter in grid = 'd' at (1,3) = flat index 2 (0-based)
start = flat_str.find("d")
print(f"First hex letter in grid: flat[{start}] = '{flat_str[start]}' at {flat_pos[start]}")

# Step by 6, collect hex letters
letters_visited = []
hex_letters = []
positions_visited = []
for i in range(start, len(flat_str), 6):
    letters_visited.append(flat_str[i])
    positions_visited.append(i)
    if flat_str[i] in HEX:
        hex_letters.append(flat_str[i])

hex_sum = sum(HEX[c] for c in hex_letters)
print(f"\nStep-6 from flat[{start}]:")
print(f"  Positions visited: {len(letters_visited)}")
print(f"  Last position: {positions_visited[-1]} (0-based) / {positions_visited[-1]+1} (1-based)")
print(f"  Last letter: '{letters_visited[-1]}' at {flat_pos[positions_visited[-1]]}")
print(f"  All visited letters: {''.join(letters_visited)}")
print(f"  Hex letters: {''.join(hex_letters)} (count={len(hex_letters)})")
print(f"  HEX SUM = {hex_sum}")

# Now compare: last cell of LASTENTRYENTIREINTEGER path (flat index 1-based 167 = 0-based 166)
# That cell is (12, 13) = 'r' per Phase 2b
target_r, target_c = 11, 12  # 0-based (12, 13) 1-based
target_flat = -1
for i, (r, c) in enumerate(flat_pos):
    if r == 12 and c == 13:
        target_flat = i
        break

print(f"\nLast cell of LASTENTRYENTIREINTEGER path: (12,13) = '{G[target_r][target_c]}'")
print(f"  Flat index (1-based): {target_flat + 1}")
print(f"  Matches hex_sum? {hex_sum == target_flat + 1}")

print("\n" + "=" * 60)
print("INTERPRETATION:")
print("=" * 60)
print("  'FIND THE START' -> first hex letter 'd' at flat index 3 (1-based)")
print("  'STEP BY SIX' -> stride 6 forward")
print("  'ADD THE HEXADECIMALS' -> sum hex-values of a-f cells = 167")
print("  'LAST ENTRY ENTIRE INTEGER' -> the SUM itself equals the position of")
print("     the last cell of the LAST ENTRY axiom (flat-pos 167)")
print("  'THERE IS A DATE ON WIRE' -> decorative nudge / confirmation")
print()
print("  -> ANSWER = 167")

# Also test: what if "entire integer" means read something else at that cell?
# e.g., the row's hex sum, or the column's
print("\n--- If LAST ENTRY points to 'r' at (12,13): ---")
row_12_hex = sum(HEX.get(G[11][c], 0) for c in range(W))
col_13_hex = sum(HEX.get(G[r][12], 0) for r in range(H))
print(f"  Row 12 hex sum: {row_12_hex}")
print(f"  Col 13 hex sum: {col_13_hex}")
print(f"  Letter 'r' alphabet pos: 18")

# Summarize all new candidates
print("\n" + "=" * 60)
print("FRESH CANDIDATES FROM PHASE 2")
print("=" * 60)
candidates = [
    (45, "Main diagonal hex sum = Rhodium (Rh, dig metal)"),
    (77, "Anti-diagonal hex sum = Iridium (Ir, dig metal)"),
    (82, "Corners alphabet sum = Lead (Pb, dig metal)"),
    (167, "Step-6 hex from first hex letter = LAST cell flat-pos"),
    (141, "Perimeter hex sum (52 cells)"),
    (549, "Interior 12×12 hex sum"),
    (371, "Uncovered cells hex sum (124 cells not in any axiom)"),
    (369, "All 5 axiom paths hex sum total"),
    (2395, "369 + 2026"),
    (2541, "1-letter element-symbol weighted total"),
    (79, "Axiom-length sum / TUNES / Gold — ★★★★★"),
    (33, "Col 6 / vanadium / U-col-sum — ★★★★★"),
    (23, "Dig count / V atomic number"),
]
for val, desc in sorted(candidates):
    print(f"  {val:>6}  {desc}")
