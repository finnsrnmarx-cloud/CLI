"""Phase 2b — LAST ENTRY ENTIRE INTEGER deep dive.

Tests:
  1. The LAST cells of each axiom path
  2. The literal LAST cell of LASTENTRYENTIREINTEGER path
  3. The letter / value AT the last cell treated as an 'entire integer'
  4. Various 'last' interpretations
  5. All single-letter 1-letter element symbols present in grid
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


def find_first_path(word):
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


AXIOMS = {
    "findthestart": "find the start",
    "addthehexadecimals": "add the hexadecimals",
    "stepbysix": "step by six",
    "thereisadateonwire": "there is a date on wire",
    "lastentryentireinteger": "last entry entire integer",
}

# 1. Last cell of each axiom
print("=" * 60)
print("LAST CELL of each axiom's king-path")
print("=" * 60)
for ax_key, ax_disp in AXIOMS.items():
    p = find_first_path(ax_key)
    last_r, last_c = p[-1]
    last_letter = G[last_r][last_c]
    print(f"  {ax_disp:30s} last=({last_r+1},{last_c+1})='{last_letter}' (hex={HEX.get(last_letter, '—')})")

# 2. LAST ENTRY ENTIRE INTEGER path's last cell
print("\n" + "=" * 60)
print("LAST ENTRY ENTIRE INTEGER — detailed path")
print("=" * 60)
p = find_first_path("lastentryentireinteger")
print(f"  Start: ({p[0][0]+1}, {p[0][1]+1}) = '{G[p[0][0]][p[0][1]]}'")
print(f"  End:   ({p[-1][0]+1}, {p[-1][1]+1}) = '{G[p[-1][0]][p[-1][1]]}'")
print(f"  Path length: {len(p)} cells")

# Show last 5 cells
print(f"\n  Last 5 cells of path:")
for r, c in p[-5:]:
    print(f"    ({r+1},{c+1})='{G[r][c]}' (hex={HEX.get(G[r][c], '—')}, alphabet={ord(G[r][c])-96})")

# 3. "last entry" could mean last cell of something specific
# Interpretations:
# - Last cell of LAST axiom path: the final 'r' at (12,13)
# - Last letter of the grid flat string: x at (14,14)
# - Last cell of the grid in reading order excluding hyphen: also x
# - Last entry as 'entire integer' = full alphabet position
last_r, last_c = p[-1]
last_letter = G[last_r][last_c]
alpha = ord(last_letter) - 96
print(f"\n  Last cell letter: '{last_letter}'  alphabet pos = {alpha}")
print(f"  As integer: {alpha}")

# 4. 'Entire integer' could be the POSITION number (like 14*14 = 196 position)
# Or the cell's flat index: (r * W + c)
flat_idx = last_r * W + last_c
print(f"  Flat index (0-based): {flat_idx}")
print(f"  Flat index (1-based): {flat_idx + 1}")

# 5. All 1-letter element symbols present in grid
print("\n" + "=" * 60)
print("1-letter element symbols in grid")
print("=" * 60)
ONE_LETTER = {"h": 1, "b": 5, "c": 6, "n": 7, "o": 8, "f": 9, "p": 15,
              "s": 16, "k": 19, "v": 23, "y": 39, "i": 53, "w": 74,
              "u": 92}
from collections import Counter
flat_str = "".join("".join(r) for r in G).replace("-", "")
letter_counts = Counter(flat_str)
print(f"{'letter':<8} {'Z':<5} {'count':<6} {'total Z':<10}")
grand_total_z = 0
for ltr, z in sorted(ONE_LETTER.items(), key=lambda x: x[1]):
    cnt = letter_counts.get(ltr, 0)
    tot = cnt * z
    grand_total_z += tot
    print(f"  {ltr:<6} {z:<5} {cnt:<6} {tot}")
print(f"\n  Grand total: {grand_total_z}")

# 6. Intersection: axiom-path hex sums
print("\n" + "=" * 60)
print("Hex sum along EACH axiom's king-path")
print("=" * 60)
for ax_key in AXIOMS:
    p = find_first_path(ax_key)
    letters = [G[r][c] for r, c in p]
    hex_sum = sum(HEX.get(ch, 0) for ch in letters)
    hex_ltrs = [ch for ch in letters if ch in HEX]
    print(f"  {AXIOMS[ax_key]:30s} sum={hex_sum}  (hex letters: {''.join(hex_ltrs)})")

# Total of all 5 paths summed
total = 0
for ax_key in AXIOMS:
    p = find_first_path(ax_key)
    letters = [G[r][c] for r, c in p]
    total += sum(HEX.get(ch, 0) for ch in letters)
print(f"\n  TOTAL across all 5 axiom paths: {total}")
print(f"    + 2026 = {total + 2026}")
print(f"    - 2026 = {total - 2026 if total > 2026 else 2026 - total}")
