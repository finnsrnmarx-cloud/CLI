"""Test the SNAKE / MAZE interpretation.

Hypotheses:
  A. Concatenate all 5 axiom paths into one 79-cell super-path.
     Step by 6 through that. Or examine where position 6/12/18/... land.
  B. Start at the DASH (14,8) and walk — the dash is the true START.
  C. Each axiom's END cell points at the NEXT axiom's START cell.
  D. Follow each axiom's DIRECTION SEQUENCE from a new start point.
  E. The 5 axioms are a SEQUENCE of operations — walk each in order.
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


AXIOMS = ["findthestart", "addthehexadecimals", "stepbysix",
          "thereisadateonwire", "lastentryentireinteger"]

paths = {a: find_first(a) for a in AXIOMS}

# ============================================================
# IDEA A: Concatenate paths in order, step by 6, look at results
# ============================================================
print("=" * 60)
print("IDEA A: Concatenate all 5 axiom paths → 79-cell snake")
print("=" * 60)

concat_path = []
for ax in AXIOMS:
    concat_path.extend(paths[ax])
letters = [G[r][c] for r, c in concat_path]
print(f"Total concat path length: {len(concat_path)}")
print(f"All letters: {''.join(letters)}")

total_hex = sum(HEX.get(c, 0) for c in letters)
print(f"Total hex sum along entire path: {total_hex}")

# Step by 6 through the concatenation
print("\n--- Step 6 through concatenated path ---")
for off in range(6):
    stepped_letters = [letters[i] for i in range(off, len(letters), 6)]
    hex_only = [c for c in stepped_letters if c in HEX]
    s = sum(HEX[c] for c in hex_only)
    print(f"offset {off}: {''.join(stepped_letters)}  hex={''.join(hex_only)}  sum={s}")

# Look at positions 6, 12, 18, ... (1-based every 6th)
print("\n--- Letters at positions 6, 12, 18, ... (1-based every 6th) ---")
positions = list(range(5, len(concat_path), 6))  # 0-indexed position 5 = 1-based 6
for p in positions:
    r, c = concat_path[p]
    print(f"position {p+1}: ({r+1},{c+1}) = '{G[r][c]}'")
positional_letters = ''.join(G[r][c] for r, c in [concat_path[p] for p in positions])
print(f"Concat: '{positional_letters}'")
pos_hex = sum(HEX.get(c, 0) for c in positional_letters)
print(f"Hex sum: {pos_hex}")

# ============================================================
# IDEA B: Start at the DASH and walk axiom-style
# ============================================================
print("\n" + "=" * 60)
print("IDEA B: The DASH at (14,8) is the start")
print("=" * 60)

# What are the dash's 8 neighbors?
dash_r, dash_c = 13, 7  # 0-indexed (14,8)
print(f"Dash at ({dash_r+1}, {dash_c+1}). 8 neighbors:")
for dr, dc in DIRS:
    nr, nc = dash_r+dr, dash_c+dc
    if 0<=nr<H and 0<=nc<W:
        print(f"  {(dr,dc)}: ({nr+1},{nc+1}) = '{G[nr][nc]}'")

# Walk 6 cells from dash in each direction, sum hex letters
print("\n--- Walk 6 cells from dash in each of 8 directions ---")
for dr, dc in DIRS:
    letters_walk = []
    for step in range(1, 7):
        nr, nc = dash_r + dr*step, dash_c + dc*step
        if 0<=nr<H and 0<=nc<W:
            letters_walk.append(G[nr][nc])
        else:
            letters_walk.append("_")
    hex_only = [c for c in letters_walk if c in HEX]
    s = sum(HEX[c] for c in hex_only)
    print(f"dir {(dr,dc)}: {''.join(letters_walk)}  hex_sum={s}")

# ============================================================
# IDEA C: Do axioms chain?
# ============================================================
print("\n" + "=" * 60)
print("IDEA C: Do axioms chain (end of one = start of next)?")
print("=" * 60)
for ax in AXIOMS:
    p = paths[ax]
    print(f"{ax:30s}  start=({p[0][0]+1},{p[0][1]+1})='{G[p[0][0]][p[0][1]]}'  end=({p[-1][0]+1},{p[-1][1]+1})='{G[p[-1][0]][p[-1][1]]}'")

print("\nDo any axiom endpoints match starting cells of another axiom?")
for a in AXIOMS:
    for b in AXIOMS:
        if a == b: continue
        if paths[a][-1] == paths[b][0]:
            print(f"  {a} END matches {b} START at {paths[a][-1]}")
        # Also check adjacency
        ar, ac = paths[a][-1]
        br, bc = paths[b][0]
        if abs(ar-br) <= 1 and abs(ac-bc) <= 1 and (ar != br or ac != bc):
            print(f"  {a} END ({ar+1},{ac+1}) ADJACENT to {b} START ({br+1},{bc+1})")
