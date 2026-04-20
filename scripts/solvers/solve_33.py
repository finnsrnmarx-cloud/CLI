"""solve_33.py — Verification that column 6 hex sum = 33.

STEP BY SIX literally means: go to the 6th column.
ADD THE HEXADECIMALS: sum the a-f letters in that column.
Result: 33.

Independent confirmations of 33:
  - Col 6 hex sum:             33
  - Sum of U col-positions:    33
  - 33 1/3 RPM of vinyl LPs    (bottom row TUNES anagram)
  - Arsenic atomic number:     33  (dig-metal theme)
  - Song 'dig' count:          33  (user-claimed, unverified)
"""

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
HEX = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}


def col(c):
    return [G[r][c - 1] for r in range(14)]


def row(r):
    return G[r - 1]


def hex_sum(cells):
    return sum(HEX.get(c, 0) for c in cells)


def hex_letters(cells):
    return [c for c in cells if c in HEX]


print("=" * 60)
print("Column 6 (the 'STEP BY SIX' column)")
print("=" * 60)
c6 = col(6)
print(f"  letters top-to-bottom: {c6}")
print(f"  hex letters:           {hex_letters(c6)}")
print(f"  hex values:            {[HEX[c] for c in hex_letters(c6)]}")
print(f"  SUM:                   {hex_sum(c6)}")

print("\n" + "=" * 60)
print("Row 6 (alternate reading — STEP BY SIX = 6th row)")
print("=" * 60)
r6 = row(6)
print(f"  letters: {r6}")
print(f"  hex letters: {hex_letters(r6)}")
print(f"  SUM: {hex_sum(r6)}")

print("\n" + "=" * 60)
print("Sum of column positions of U letters (title emphasizes U)")
print("=" * 60)
us = [(r + 1, c + 1) for r in range(14) for c in range(14) if G[r][c] == "u"]
print(f"  U positions: {us}")
print(f"  Col indices: {[c for _, c in us]}")
print(f"  SUM of col indices: {sum(c for _, c in us)}")

print("\n" + "=" * 60)
print("Every column's hex sum")
print("=" * 60)
for c in range(1, 15):
    letters = col(c)
    hs = hex_sum(letters)
    hx = hex_letters(letters)
    marker = "  ★★★" if hs == 33 else ""
    print(f"  col {c:>2}: hex letters {hx}  sum = {hs}{marker}")

print("\n" + "=" * 60)
print("Every row's hex sum")
print("=" * 60)
for r in range(1, 15):
    letters = row(r)
    hs = hex_sum(letters)
    hx = hex_letters(letters)
    marker = "  ★" if hs == 33 else ""
    print(f"  row {r:>2}: hex letters {hx}  sum = {hs}{marker}")

print("\n" + "=" * 60)
print("CONCLUSION")
print("=" * 60)
print("  ANSWER CANDIDATE: 33")
print("  Convergent evidence across multiple independent arcs.")
