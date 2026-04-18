"""Phase 2d — Uniqueness check for self-referential 167.

For every possible starting cell in the grid, compute step-6 hex sum.
Also compute flat-index (1-based) of every cell.
Find all pairs (start, target) where step_6_hex_sum(start) equals the
flat position of some MEANINGFUL cell (e.g., last cell of an axiom).

This verifies 167 is uniquely self-referential or reveals other hits.
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

# flat string
flat = []
flat_pos = []
for r in range(H):
    for c in range(W):
        if G[r][c] != "-":
            flat.append(G[r][c])
            flat_pos.append((r+1, c+1))
flat_str = "".join(flat)


def step6_hex(start):
    total = 0
    last_pos = start
    for i in range(start, len(flat_str), 6):
        if flat_str[i] in HEX:
            total += HEX[flat_str[i]]
        last_pos = i
    return total, last_pos + 1  # 1-based last position


# All starts that yield self-referential (sum == last_pos_visited)
print("=" * 60)
print("All starts where step-6 hex sum equals position of last cell visited")
print("=" * 60)
for start in range(len(flat_str)):
    s, last = step6_hex(start)
    if s == last:
        print(f"  flat[{start}]='{flat_str[start]}' at {flat_pos[start]}: sum={s}, last_pos={last} MATCH")

# Find if hex_sum from any start matches the flat-pos of an axiom's last cell
print("\n" + "=" * 60)
print("Axiom last cell flat positions (1-based):")
print("=" * 60)

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


AXIOMS = ["findthestart", "addthehexadecimals", "stepbysix",
          "thereisadateonwire", "lastentryentireinteger"]

axiom_last_flat = {}
for ax in AXIOMS:
    p = find_first_path(ax)
    last_r, last_c = p[-1]
    # compute flat position
    flat_idx = sum(1 for r in range(H) for c in range(W)
                   if G[r][c] != "-" and (r < last_r or (r == last_r and c < last_c)))
    axiom_last_flat[ax] = flat_idx + 1  # 1-based
    print(f"  {ax:30s} last cell ({last_r+1},{last_c+1})='{G[last_r][last_c]}'  flat={flat_idx+1}")

print("\n" + "=" * 60)
print("Which step-6 starts yield a hex sum matching ANY axiom's last flat position?")
print("=" * 60)
for start in range(len(flat_str)):
    s, _ = step6_hex(start)
    for ax, target in axiom_last_flat.items():
        if s == target:
            print(f"  flat[{start}]='{flat_str[start]}' at {flat_pos[start]}: hex_sum={s} matches {ax} last_flat_pos={target}")

# Also: find any OTHER starting cell that gives 167
print("\n" + "=" * 60)
print("All starts that give step-6 hex sum = 167")
print("=" * 60)
for start in range(len(flat_str)):
    s, _ = step6_hex(start)
    if s == 167:
        print(f"  flat[{start}]='{flat_str[start]}' at {flat_pos[start]}")

# And the counterpart: which TARGET cells can be hit with 167?
print(f"\n167 as a flat position (1-based) = {flat_pos[166]}  letter='{flat_str[166]}'")
