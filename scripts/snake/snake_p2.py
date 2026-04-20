"""Part 2: Dash as start. Follow axiom direction sequences.

For each axiom, extract its DIRECTION VECTOR SEQUENCE from the
king-path. Apply that same vector sequence starting at the dash
(14,8) and see where you end up and what you collect.
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


def find_first(word):
    def dfs(r, c, i, seen, path):
        if i == len(word): return path
        for dr, dc in DIRS:
            nr, nc = r+dr, c+dc
            if 0<=nr<H and 0<=nc<W and (nr,nc) not in seen and G[nr][nc]==word[i]:
                res = dfs(nr, nc, i+1, seen | {(nr, nc)}, path + [(nr, nc)])
                if res: return res
        return None
    for r in range(H):
        for c in range(W):
            if G[r][c] == word[0]:
                res = dfs(r, c, 1, frozenset({(r, c)}), [(r, c)])
                if res: return res
    return None


def path_to_directions(p):
    """Convert a path into its sequence of (dr, dc) movements."""
    dirs = []
    for i in range(1, len(p)):
        dr = p[i][0] - p[i-1][0]
        dc = p[i][1] - p[i-1][1]
        dirs.append((dr, dc))
    return dirs


AXIOMS = ["findthestart", "addthehexadecimals", "stepbysix",
          "thereisadateonwire", "lastentryentireinteger"]

paths = {a: find_first(a) for a in AXIOMS}

dash = (13, 7)  # (14,8) 0-indexed

print("=" * 60)
print("Apply each axiom's direction-sequence starting from the DASH")
print("=" * 60)

for ax in AXIOMS:
    dirs = path_to_directions(paths[ax])
    # Walk from dash applying these directions in order
    r, c = dash
    letters = ["-"]  # dash itself
    valid = True
    for dr, dc in dirs:
        r, c = r+dr, c+dc
        if 0 <= r < H and 0 <= c < W:
            letters.append(G[r][c])
        else:
            letters.append("_")
            valid = False
    hex_only = [c for c in letters if c in HEX]
    hex_sum = sum(HEX.get(c, 0) for c in letters if c in HEX)
    path_str = ''.join(letters)
    print(f"\n{ax}:")
    print(f"  directions: {dirs[:10]}{'...' if len(dirs)>10 else ''}")
    print(f"  letters from dash: {path_str}")
    print(f"  hex_sum: {hex_sum}  {'(off-grid at some point)' if not valid else ''}")
    print(f"  end cell: ({r+1}, {c+1}) {'off-grid' if not valid else ''}")

# Direction SUMS: each axiom's movement vector totaled
print("\n" + "=" * 60)
print("Total movement vector per axiom")
print("=" * 60)
for ax in AXIOMS:
    dirs = path_to_directions(paths[ax])
    total_dr = sum(d[0] for d in dirs)
    total_dc = sum(d[1] for d in dirs)
    print(f"  {ax}: Δrow={total_dr}, Δcol={total_dc}")

# If we combine all 5 axiom displacement vectors
total_dr = sum(sum(d[0] for d in path_to_directions(paths[ax])) for ax in AXIOMS)
total_dc = sum(sum(d[1] for d in path_to_directions(paths[ax])) for ax in AXIOMS)
print(f"\nCombined displacement if all 5 axioms walked: Δ=({total_dr}, {total_dc})")

# Applied from (1,1)
if 1 + total_dr - 1 >= 0 and 1 + total_dc - 1 >= 0:
    final_r = total_dr
    final_c = total_dc
    if 0 <= final_r < H and 0 <= final_c < W:
        print(f"  If walked from (1,1), end: ({final_r+1}, {final_c+1}) = '{G[final_r][final_c]}'")

# Applied from dash
final_r = dash[0] + total_dr
final_c = dash[1] + total_dc
print(f"  If walked from dash, end: ({final_r+1}, {final_c+1})")
if 0 <= final_r < H and 0 <= final_c < W:
    print(f"     cell letter: '{G[final_r][final_c]}'")
else:
    print(f"     OFF-GRID")
