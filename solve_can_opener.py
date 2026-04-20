"""solve_can_opener.py — Tests the 'TIN OPENER' / 'open the can' idea.

Column 1 reversed reads: 'tinstmuaopener' — contains TIN and OPENER.
The title 'Can U Dig It?' uses CAN = metal container. The column 1 cue
suggests you should 'open the can' by stripping the perimeter (the
metal shell) and working with the inner 12×12 (the contents).

Also verifies new numeric findings:
  - axiom-length sum = 79 (= TUNES alphabet sum = Au atomic number)
  - perimeter hex sum
  - inner 12×12 hex sum
  - various combinations with 2026, 33, 23
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

AXIOMS = {
    "findthestart": 12,
    "addthehexadecimals": 18,
    "stepbysix": 9,
    "thereisadateonwire": 18,
    "lastentryentireinteger": 22,
}


def hex_of(ch: str) -> int:
    return HEX.get(ch, 0)


def cells_in_perimeter() -> list[tuple[int, int]]:
    cells = []
    for c in range(W):
        cells.append((0, c))
        cells.append((H - 1, c))
    for r in range(1, H - 1):
        cells.append((r, 0))
        cells.append((r, W - 1))
    return cells


def cells_in_interior() -> list[tuple[int, int]]:
    return [(r, c) for r in range(1, H - 1) for c in range(1, W - 1)]


def sum_hex_of(cells: list[tuple[int, int]]) -> tuple[int, list[str]]:
    hex_letters = []
    total = 0
    for r, c in cells:
        ch = G[r][c]
        if ch in HEX:
            hex_letters.append(ch)
            total += HEX[ch]
    return total, hex_letters


print("=" * 70)
print("1. AXIOM LENGTH SUM (verified = 79 = TUNES = Gold Z)")
print("=" * 70)
total_len = sum(AXIOMS.values())
print(f"  {'axiom':30s} length")
print(f"  {'-' * 40}")
for name, n in AXIOMS.items():
    print(f"  {name:30s} {n}")
print(f"  {'-' * 40}")
print(f"  TOTAL:                         {total_len}")
print(f"\n  Match against:")
print(f"    TUNES alphabet sum:        {sum(ord(c)-96 for c in 'tunes')}")
print(f"    Gold (Au) atomic number:   79")

print("\n" + "=" * 70)
print("2. PERIMETER HEX SUM (the 'can' wall / shell)")
print("=" * 70)
perim = cells_in_perimeter()
p_sum, p_hex = sum_hex_of(perim)
print(f"  Perimeter cell count: {len(perim)}")
print(f"  Hex letters in perimeter: {p_hex}")
print(f"  Count: {len(p_hex)}")
print(f"  SUM: {p_sum}")
print(f"  + 2026: {p_sum + 2026}")

print("\n" + "=" * 70)
print("3. INTERIOR 12×12 HEX SUM (inside the 'can')")
print("=" * 70)
inter = cells_in_interior()
i_sum, i_hex = sum_hex_of(inter)
print(f"  Interior cell count: {len(inter)}")
print(f"  Hex letters in interior: {i_hex}")
print(f"  Count: {len(i_hex)}")
print(f"  SUM: {i_sum}")
print(f"  + 2026: {i_sum + 2026}")

print(f"\n  Perimeter + Interior = full grid hex: {p_sum + i_sum}")

print("\n" + "=" * 70)
print("4. WIRE COLUMN (col 8) HEX SUM")
print("=" * 70)
col8 = [(r, 7) for r in range(H) if G[r][7] != "-"]
c_sum, c_hex = sum_hex_of(col8)
print(f"  Col 8 hex letters (excluding dash): {c_hex}")
print(f"  SUM: {c_sum}")

print("\n" + "=" * 70)
print("5. HYPHEN-POSITION ARITHMETIC at (14,8)")
print("=" * 70)
print(f"  14 + 8 = {14 + 8}   (22, REJECTED)")
print(f"  14 - 8 = {14 - 8}   (matches STEP BY SIX!)")
print(f"  14 * 8 = {14 * 8}")
print(f"  14 / 8 = {14 / 8:.4f}")
print(f"  8^14 / 14^8 / etc — unlikely to yield small integer")

print("\n" + "=" * 70)
print("6. COMBINATION CANDIDATES")
print("=" * 70)
candidates = [
    (79, "axiom-length-sum / TUNES / Au (NEW top)"),
    (33, "col 6 hex / U col-sum / vanadium-hex-letters"),
    (23, "dig count / V / missing from grid"),
    (33 + 23, "33+23 = Ba (Barium)"),
    (79 - 33, "79-33 = Pd (Palladium)"),
    (79 + 33, "79+33 (no clean element)"),
    (33 + 23 + 79, "sum of three convergents"),
    (79 * 2, "2 × Au"),
    (33 * 2, "2 × 33 = 66 (Dy, Dysprosium)"),
    (23 * 2, "2 × 23 = 46 (Pd) same as 79-33"),
    (p_sum, "perimeter hex sum"),
    (i_sum, "interior 12×12 hex sum"),
    (p_sum + 2026, "perimeter + 2026"),
    (i_sum + 2026, "interior + 2026"),
]
seen = set()
for n, desc in sorted(candidates):
    if n in seen:
        continue
    seen.add(n)
    print(f"  {n:>6}  {desc}")

print("\n" + "=" * 70)
print("7. SUBMIT ORDER per plan")
print("=" * 70)
submit_order = [
    79, 33, 23, 2192, 2193, 56, 167, 166, 46, 135, 14, 63, 184, 89, 13
]
for i, n in enumerate(submit_order, 1):
    print(f"  {i:>2}.  {n}")
