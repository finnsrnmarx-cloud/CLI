"""solve_solfege.py — Solfège / musical-note interpretations of the grid.

Tests the idea that 'ADD THE HEXADECIMALS' could be musical: the 6 hex
digits a-f are musical notes (La, Ti, Do, Re, Mi, Fa). Their values
could be scale degrees (1-7) or semitones (0-11).

Also searches for solfège syllables (do, re, mi, fa, sol, la, ti, si)
hidden in the grid.
"""

from __future__ import annotations

from collections import Counter

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
DIRS8 = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]

flat_str = "".join("".join(r) for r in G).replace("-", "")
counter = Counter(flat_str)

# Hex letters → solfège mappings
SCALE_DEGREE = {"c": 1, "d": 2, "e": 3, "f": 4, "a": 6, "b": 7}  # movable do
CHROMATIC    = {"c": 0, "d": 2, "e": 4, "f": 5, "a": 9, "b": 11}  # semitones from C
HEX_VAL      = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
# Include G (Sol) for music interpretation
SCALE_DEGREE_G = {**SCALE_DEGREE, "g": 5}
CHROMATIC_G    = {**CHROMATIC, "g": 7}


def sum_by(mapping):
    total = 0
    for letter, n in counter.items():
        if letter in mapping:
            total += mapping[letter] * n
    return total


print("=" * 70)
print("MUSICAL/HEX LETTER COUNTS IN GRID")
print("=" * 70)
for l in "abcdefg":
    print(f"  {l}: {counter.get(l, 0):2d} occurrences")

print("\n" + "=" * 70)
print("WEIGHTED SUMS UNDER DIFFERENT MAPPINGS")
print("=" * 70)

print(f"\nHEX values (a=10..f=15):")
s = sum_by(HEX_VAL)
print(f"  sum = {s}")
print(f"  + 2026 = {s + 2026}")

print(f"\nSOLFÈGE scale degrees (movable do, 1-7):")
s = sum_by(SCALE_DEGREE)
print(f"  without G: sum = {s}")
s2 = sum_by(SCALE_DEGREE_G)
print(f"  with G=5:  sum = {s2}")
print(f"  without G +2026 = {s + 2026}")
print(f"  with G +2026    = {s2 + 2026}")

print(f"\nCHROMATIC semitones (C=0..B=11):")
s = sum_by(CHROMATIC)
print(f"  without G: sum = {s}")
s2 = sum_by(CHROMATIC_G)
print(f"  with G=7:  sum = {s2}")
print(f"  without G +2026 = {s + 2026}")
print(f"  with G +2026    = {s2 + 2026}")


# Step-by-6 from various starts, using solfège degrees instead of hex values
print("\n" + "=" * 70)
print("STEP-BY-6 WITH SOLFÈGE MAPPING (movable do degrees)")
print("=" * 70)


def step_sum(start, step, mapping):
    total = 0
    for i in range(start, len(flat_str), step):
        ch = flat_str[i]
        if ch in mapping:
            total += mapping[ch]
    return total


for start in [2, 7, 8, 13, 0]:
    ch = flat_str[start]
    print(f"\nStart flat[{start}] = {ch!r}:")
    for mapname, m in [("HEX", HEX_VAL), ("SolfègeDeg", SCALE_DEGREE),
                       ("SolfègeG", SCALE_DEGREE_G), ("Chromatic", CHROMATIC),
                       ("ChromaticG", CHROMATIC_G)]:
        s = step_sum(start, 6, m)
        print(f"  {mapname:<14} sum = {s:>4}  +2026 = {s + 2026}")


# Search for solfège syllables as substrings / king paths
print("\n" + "=" * 70)
print("SOLFÈGE SYLLABLES — king-path counts")
print("=" * 70)


def count_king(word):
    c = 0

    def dfs(r, col, i, seen):
        nonlocal c
        if i == len(word):
            c += 1
            return
        for dr, dc in DIRS8:
            nr, nc = r + dr, col + dc
            if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in seen and G[nr][nc] == word[i]:
                dfs(nr, nc, i + 1, seen | {(nr, nc)})

    for r in range(H):
        for col in range(W):
            if G[r][col] == word[0]:
                dfs(r, col, 1, frozenset({(r, col)}))
    return c


syllables = [
    ("do", 1), ("re", 2), ("mi", 3), ("fa", 4),
    ("sol", 5), ("so", 5), ("la", 6), ("ti", 7), ("si", 7),
    ("doh", 1), ("ray", 2), ("mee", 3), ("fah", 4),
    ("soh", 5), ("lah", 6), ("tee", 7),
    # longer: full words?
    ("dore", 12), ("mifa", 34), ("sollati", 567),
]
print(f"{'syl':<10} {'deg':>4}  {'king-paths':>10}")
for syl, deg in syllables:
    k = count_king(syl)
    if k:
        print(f"{syl!r:<10} {deg:>4}  {k:>10}")


# Count only a-f (hex-only) but multiply by scale degrees
print("\n" + "=" * 70)
print("TUNES letter sum using different schemes")
print("=" * 70)
for label, m in [("alpha position", {l: i+1 for i, l in enumerate("abcdefghijklmnopqrstuvwxyz")}),
                 ("solfège (T/U/N/E/S non-musical)", {"t": 0, "u": 0, "n": 0, "e": 3, "s": 0})]:
    s = sum(m.get(c, 0) for c in "tunes")
    print(f"  {label:<40}: {s}")
# Just sum the single musical letter in TUNES
print(f"  TUNES has only one musical letter: E (Mi=3, or 14 in hex)")

# Final candidate dump
print("\n" + "=" * 70)
print("MUSICAL/SOLFÈGE CANDIDATE ANSWERS")
print("=" * 70)
cands = []
for n in [sum_by(HEX_VAL), sum_by(SCALE_DEGREE), sum_by(SCALE_DEGREE_G),
          sum_by(CHROMATIC), sum_by(CHROMATIC_G)]:
    cands.append(n)
    cands.append(n + 2026)
for n in sorted(set(cands)):
    print(f"  {n}")
