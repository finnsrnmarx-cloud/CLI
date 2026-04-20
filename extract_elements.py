"""Chunk 2 — Full chemical element names traceable in grid.

Tests: every element name (Z=1..103) as a king-path.
Only reports ones that actually trace.
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
DIRS = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]

def king_paths(word, stop=None):
    cnt = 0
    def dfs(r, c, i, seen):
        nonlocal cnt
        if stop and cnt >= stop: return
        if i == len(word): cnt += 1; return
        for dr, dc in DIRS:
            nr, nc = r+dr, c+dc
            if 0<=nr<H and 0<=nc<W and (nr,nc) not in seen and G[nr][nc]==word[i]:
                dfs(nr, nc, i+1, seen | {(nr, nc)})
    for r in range(H):
        for c in range(W):
            if G[r][c] == word[0]:
                dfs(r, c, 1, frozenset({(r, c)}))
                if stop and cnt >= stop: return cnt
    return cnt

def straight_lines(word):
    cnt = 0
    L = len(word)
    for r in range(H):
        for c in range(W):
            for dr, dc in DIRS:
                if not (0<=r+(L-1)*dr<H and 0<=c+(L-1)*dc<W): continue
                if all(G[r+i*dr][c+i*dc]==word[i] for i in range(L)):
                    cnt += 1
    return cnt

ELEMENTS = {
    1: "hydrogen", 2: "helium", 3: "lithium", 4: "beryllium",
    5: "boron", 6: "carbon", 7: "nitrogen", 8: "oxygen",
    9: "fluorine", 10: "neon", 11: "sodium", 12: "magnesium",
    13: "aluminum", 14: "silicon", 15: "phosphorus", 16: "sulfur",
    17: "chlorine", 18: "argon", 19: "potassium", 20: "calcium",
    21: "scandium", 22: "titanium", 23: "vanadium", 24: "chromium",
    25: "manganese", 26: "iron", 27: "cobalt", 28: "nickel",
    29: "copper", 30: "zinc", 31: "gallium", 32: "germanium",
    33: "arsenic", 34: "selenium", 35: "bromine", 36: "krypton",
    37: "rubidium", 38: "strontium", 39: "yttrium", 40: "zirconium",
    41: "niobium", 42: "molybdenum", 43: "technetium", 44: "ruthenium",
    45: "rhodium", 46: "palladium", 47: "silver", 48: "cadmium",
    49: "indium", 50: "tin", 51: "antimony", 52: "tellurium",
    53: "iodine", 54: "xenon", 55: "cesium", 56: "barium",
    57: "lanthanum", 58: "cerium", 63: "europium", 64: "gadolinium",
    65: "terbium", 66: "dysprosium", 67: "holmium", 68: "erbium",
    69: "thulium", 70: "ytterbium", 71: "lutetium", 72: "hafnium",
    73: "tantalum", 74: "tungsten", 75: "rhenium", 76: "osmium",
    77: "iridium", 78: "platinum", 79: "gold", 80: "mercury",
    81: "thallium", 82: "lead", 83: "bismuth", 84: "polonium",
    85: "astatine", 86: "radon", 87: "francium", 88: "radium",
    89: "actinium", 90: "thorium", 91: "protactinium", 92: "uranium",
}

print(f"{'Z':>4s}  {'Name':<14s}  {'King':>5s}  {'Straight':>8s}")
print("-" * 50)
found = []
for z, name in ELEMENTS.items():
    k = king_paths(name, stop=5)
    s = straight_lines(name)
    if k or s:
        found.append((z, name, k, s))
        marker = "★ STRAIGHT" if s > 0 else ""
        print(f"  {z:>3}   {name:<14s}  {k:>5}  {s:>5}  {marker}")
print(f"\n  Total element names traceable: {len(found)}")
print(f"  Sum of atomic numbers: {sum(z for z,_,_,_ in found)}")

# The missing-letter analysis
print("\n  NOT traceable (grid lacks required letter — note Q, V, Z absent):")
for z, name in ELEMENTS.items():
    if any(c in "qvz" for c in name.lower()):
        blocker = next(c for c in name.lower() if c in "qvz")
        print(f"    Z={z:<3} {name:<14s} blocked by '{blocker}'")
