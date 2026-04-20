"""Phase 2a — Paths, diagonals, corners.

Tests:
  1. The 5 axiom king-paths: which grid cells do they cover collectively?
  2. Cells NOT touched by any axiom — "answer cells"?
  3. Cells touched by MULTIPLE axioms (overlap / wire junctions)
  4. Main diagonal + anti-diagonal hex sums (candidate for 'WIRE')
  5. Corner letters as alphabet positions
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
DIRS = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]


def find_first_path(word: str):
    def dfs(r, c, i, seen, path):
        if i == len(word):
            return path
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in seen and G[nr][nc] == word[i]:
                res = dfs(nr, nc, i + 1, seen | {(nr, nc)}, path + [(nr, nc)])
                if res:
                    return res
        return None
    for r in range(H):
        for c in range(W):
            if G[r][c] == word[0]:
                res = dfs(r, c, 1, frozenset({(r, c)}), [(r, c)])
                if res:
                    return res
    return None


AXIOMS = ["findthestart", "addthehexadecimals", "stepbysix",
          "thereisadateonwire", "lastentryentireinteger"]

# 1. Path coverage
paths = {a: find_first_path(a) for a in AXIOMS}
all_cells = set()
cell_hits = {}  # (r,c) -> count
for a, p in paths.items():
    for cell in p:
        all_cells.add(cell)
        cell_hits[cell] = cell_hits.get(cell, 0) + 1

print(f"Total unique cells covered by all 5 axioms: {len(all_cells)}")
print(f"Cells hit by multiple axioms: {sum(1 for c in cell_hits if cell_hits[c] > 1)}")

# 2. Uncovered cells
uncovered = [(r, c) for r in range(H) for c in range(W) if (r, c) not in all_cells and G[r][c] != "-"]
print(f"\nUncovered cells (not touched by any axiom): {len(uncovered)}")
print(f"  Letters at uncovered cells: {''.join(G[r][c] for r, c in uncovered)}")
hex_uncov = [G[r][c] for r, c in uncovered if G[r][c] in HEX]
print(f"  Hex letters in uncovered: {hex_uncov}  sum={sum(HEX[c] for c in hex_uncov)}")

# 3. Multi-hit cells
multi = [(c, cell_hits[c]) for c in cell_hits if cell_hits[c] > 1]
multi.sort(key=lambda x: -x[1])
print(f"\nCells touched by multiple axioms (top 10):")
for cell, count in multi[:10]:
    r, c = cell
    print(f"  ({r+1},{c+1})='{G[r][c]}' hit {count} times")

# 4. Main + anti-diagonals
print("\n--- Diagonals ---")
main_diag = [G[i][i] for i in range(H)]
anti_diag = [G[i][H-1-i] for i in range(H)]
print(f"Main diag (1,1)→(14,14): {''.join(main_diag)}")
print(f"  Hex letters: {[c for c in main_diag if c in HEX]}")
print(f"  Hex sum: {sum(HEX.get(c,0) for c in main_diag)}")

print(f"Anti-diag (1,14)→(14,1): {''.join(anti_diag)}")
print(f"  Hex letters: {[c for c in anti_diag if c in HEX]}")
print(f"  Hex sum: {sum(HEX.get(c,0) for c in anti_diag)}")

# 5. Corner letters
print("\n--- Corners ---")
corners = [(0,0), (0,W-1), (H-1,0), (H-1,W-1)]
corner_letters = [G[r][c] for r, c in corners]
corner_vals = [ord(c)-96 for c in corner_letters]
print(f"Corners: {corner_letters}  (alphabet positions: {corner_vals})")
print(f"Sum of corner alphabet positions: {sum(corner_vals)}")
print(f"  82 = Lead (Pb) atomic number — another dig-metal!")

# Corner letters as hex if possible
corner_hex = [HEX.get(c, 0) for c in corner_letters]
print(f"Corner letters as hex: {corner_hex}  sum={sum(corner_hex)}")
