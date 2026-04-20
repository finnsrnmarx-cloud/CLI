"""Part 3: Deeper dash-walk analysis.

Starting at the dash, apply each axiom's direction SEQUENCE and
see what letters get collected BEFORE going off-grid. Look for
patterns where a walk-from-dash stays in grid and spells meaning.

Also: try reading each axiom path BACKWARDS from dash, and in
truncated form.
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

def dirs_of(p):
    return [(p[i][0]-p[i-1][0], p[i][1]-p[i-1][1]) for i in range(1, len(p))]

AXIOMS = ["findthestart", "addthehexadecimals", "stepbysix",
          "thereisadateonwire", "lastentryentireinteger"]

paths = {a: find_first(a) for a in AXIOMS}
dash = (13, 7)  # (14,8) 0-indexed

# Apply each axiom's REVERSED direction sequence from dash
print("=" * 60)
print("Walking REVERSED axiom directions from dash")
print("=" * 60)

for ax in AXIOMS:
    dirs_rev = [(-dr, -dc) for dr, dc in dirs_of(paths[ax])][::-1]
    r, c = dash
    letters = []
    in_grid = 0
    for dr, dc in dirs_rev:
        r, c = r+dr, c+dc
        if 0 <= r < H and 0 <= c < W:
            letters.append(G[r][c])
            in_grid += 1
        else:
            letters.append("_")
    hex_sum = sum(HEX.get(ch, 0) for ch in letters if ch in HEX)
    print(f"{ax:30s}  walked {in_grid}/{len(dirs_rev)}  letters: {''.join(letters)[:30]}")
    print(f"    hex sum: {hex_sum}")

# Start at dash, apply each axiom's DIRECTIONS one by one in series
print("\n" + "=" * 60)
print("Walk ALL 5 axioms in sequence from the dash")
print("=" * 60)
r, c = dash
collected = ['-']
for ax in AXIOMS:
    for dr, dc in dirs_of(paths[ax]):
        r, c = r+dr, c+dc
        if 0 <= r < H and 0 <= c < W:
            collected.append(G[r][c])
        else:
            collected.append(f"[off:{r+1},{c+1}]")
            break
    else:
        continue
    break

print(f"Collected from dash: {''.join(collected)[:60]}")
print(f"End cell: ({r+1}, {c+1})")
hex_sum = sum(HEX.get(ch, 0) for ch in collected if ch in HEX)
print(f"Hex sum so far: {hex_sum}")

# What if axiom directions get APPLIED to themselves (cycling)?
print("\n" + "=" * 60)
print("Just the first 6 moves of each axiom from dash (stride-6 aware)")
print("=" * 60)
for ax in AXIOMS:
    dirs6 = dirs_of(paths[ax])[:6]
    r, c = dash
    letters = ['-']
    for dr, dc in dirs6:
        r, c = r+dr, c+dc
        if 0 <= r < H and 0 <= c < W:
            letters.append(G[r][c])
        else:
            letters.append("_")
            break
    hex_sum = sum(HEX.get(ch, 0) for ch in letters if ch in HEX)
    print(f"  {ax}: {''.join(letters)}  hex_sum={hex_sum}")

# Every 6th direction from each axiom's path, starting from dash
print("\n" + "=" * 60)
print("Apply every 6th direction of each axiom from dash")
print("=" * 60)
for ax in AXIOMS:
    every6 = dirs_of(paths[ax])[::6]  # every 6th direction
    r, c = dash
    letters = ['-']
    for dr, dc in every6:
        r, c = r+dr, c+dc
        if 0 <= r < H and 0 <= c < W:
            letters.append(G[r][c])
        else:
            letters.append("_")
    hex_sum = sum(HEX.get(ch, 0) for ch in letters if ch in HEX)
    print(f"  {ax}: dirs={every6}  letters={''.join(letters)}  hex_sum={hex_sum}")
