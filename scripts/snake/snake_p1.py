"""Snake/maze interpretation — Part 1: step-6 through each axiom's cells.

For each of the 5 axioms individually, stride 6 through its cell
sequence and collect hex values.
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

print("=" * 60)
print("Step-6 through EACH axiom's cells individually")
print("=" * 60)

for ax in AXIOMS:
    p = paths[ax]
    letters = [G[r][c] for r, c in p]
    print(f"\n{ax} ({len(p)} cells):")
    print(f"  letters: {''.join(letters)}")
    for off in range(6):
        stepped = [letters[i] for i in range(off, len(letters), 6)]
        hex_only = [c for c in stepped if c in HEX]
        s = sum(HEX[c] for c in hex_only)
        if s > 0:
            print(f"    off {off}: {''.join(stepped)}  hex={s}")

# Sum across all 5 step-6 offsets per axiom
print("\n" + "=" * 60)
print("Summing step-6 at offset 0 across all 5 axioms")
print("=" * 60)
total_off0 = 0
for ax in AXIOMS:
    p = paths[ax]
    letters = [G[r][c] for r, c in p]
    stepped = [letters[i] for i in range(0, len(letters), 6)]
    s = sum(HEX.get(c, 0) for c in stepped)
    total_off0 += s
print(f"Total: {total_off0}")

# Each axiom's START cell, stepped
print("\n" + "=" * 60)
print("What if each axiom's start cell is a sequence and we stride 6?")
print("=" * 60)
starts = [paths[ax][0] for ax in AXIOMS]
print(f"Axiom start cells: {[(r+1,c+1) for r,c in starts]}")
start_letters = [G[r][c] for r, c in starts]
print(f"Start letters: {start_letters}  ({''.join(start_letters)})")
# 'fastl' — the first letters of each axiom
start_alpha = sum(ord(c)-96 for c in start_letters)
print(f"Alphabet sum: {start_alpha}")

# Ends
ends = [paths[ax][-1] for ax in AXIOMS]
end_letters = [G[r][c] for r, c in ends]
print(f"\nAxiom end cells: {[(r+1,c+1) for r,c in ends]}")
print(f"End letters: {end_letters}  ({''.join(end_letters)})")
# 'tsxer'
end_alpha = sum(ord(c)-96 for c in end_letters)
print(f"Alphabet sum: {end_alpha}")

# Is 'fastl' or 'tsxer' meaningful?
print(f"\nStart letters anagram candidates: fastl -> 'flats'")
print(f"End letters anagram: tsxer -> 'rexts'? 'rests'? 'strex'?")
