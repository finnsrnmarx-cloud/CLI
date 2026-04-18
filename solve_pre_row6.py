"""solve_pre_row6.py — Hex sums for row 6, rows 1-5 (before), and
king-path analysis of words leading to row 6.
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
DIRS = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]


def hex_sum_row(r):
    return sum(HEX.get(c, 0) for c in G[r - 1])


def hex_letters_row(r):
    return [c for c in G[r - 1] if c in HEX]


def hex_sum_col(c):
    return sum(HEX.get(G[r][c - 1], 0) for r in range(14))


def hex_letters_col(c):
    return [G[r][c - 1] for r in range(14) if G[r][c - 1] in HEX]


print("=" * 66)
print("ROW-BY-ROW HEX SUMS")
print("=" * 66)
totals = []
for r in range(1, 15):
    s = hex_sum_row(r)
    totals.append(s)
    print(f"  row {r:>2}: {G[r-1]}  hex letters: {hex_letters_row(r)}  sum = {s}")

print(f"\nRow 6 alone:        sum = {totals[5]}")
print(f"Rows 1-5 (before):  sum = {sum(totals[0:5])}")
print(f"Rows 1-6 (through): sum = {sum(totals[0:6])}")
print(f"Rows 7-14 (after):  sum = {sum(totals[6:])}")
print(f"All 14 rows:        sum = {sum(totals)}")

print(f"\nWith +2026 added:")
print(f"  row 6 + 2026           = {totals[5] + 2026}")
print(f"  rows 1-5 + 2026        = {sum(totals[0:5]) + 2026}")
print(f"  rows 1-6 + 2026        = {sum(totals[0:6]) + 2026}")

print("\n" + "=" * 66)
print("COLUMN-BY-COLUMN HEX SUMS (for reference)")
print("=" * 66)
for c in range(1, 15):
    s = hex_sum_col(c)
    marker = "  ★ = 33" if s == 33 else ""
    print(f"  col {c:>2}: sum = {s}{marker}")


# --- King paths that pass through or terminate in row 6 ---
print("\n" + "=" * 66)
print("Which axiom king-paths touch row 6?")
print("=" * 66)


def first_king_path(word):
    def dfs(r, c, i, seen, path):
        if i == len(word):
            return path
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 14 and 0 <= nc < 14 and (nr, nc) not in seen and G[nr][nc] == word[i]:
                res = dfs(nr, nc, i + 1, seen | {(nr, nc)}, path + [(nr, nc)])
                if res:
                    return res
        return None

    for r in range(14):
        for c in range(14):
            if G[r][c] == word[0]:
                res = dfs(r, c, 1, frozenset({(r, c)}), [(r, c)])
                if res:
                    return res
    return None


AXIOMS = ["findthestart", "addthehexadecimals", "stepbysix",
          "thereisadateonwire", "lastentryentireinteger"]

for ax in AXIOMS:
    path = first_king_path(ax)
    rows = set(r + 1 for r, c in path)
    touches_6 = 6 in rows
    rows_before_6 = sorted(r for r in rows if r < 6)
    rows_after_6 = sorted(r for r in rows if r > 6)
    print(f"\n  {ax}")
    print(f"    rows touched: {sorted(rows)}")
    print(f"    touches row 6: {touches_6}")
    if touches_6:
        # cells in row 6
        cells_in_6 = [(r + 1, c + 1) for r, c in path if r + 1 == 6]
        print(f"    cells in row 6: {cells_in_6}")


# --- Summing hex cells ALONG each axiom path ---
print("\n" + "=" * 66)
print("Hex-cell sums along each axiom king-path (up to / through row 6)")
print("=" * 66)

for ax in AXIOMS:
    path = first_king_path(ax)
    letters = [G[r][c] for r, c in path]
    # entire path
    full_sum = sum(HEX.get(c, 0) for c in letters)
    # path cells up to and including row 6
    through_r6 = [(r, c) for r, c in path if r + 1 <= 6]
    sum_through6 = sum(HEX.get(G[r][c], 0) for r, c in through_r6)
    # cells BEFORE row 6 (r+1 < 6 → r+1 <= 5)
    before_r6 = [(r, c) for r, c in path if r + 1 <= 5]
    sum_before6 = sum(HEX.get(G[r][c], 0) for r, c in before_r6)
    print(f"  {ax}")
    print(f"    full path hex sum:     {full_sum}")
    print(f"    through row 6 hex sum: {sum_through6}")
    print(f"    before row 6 hex sum:  {sum_before6}")


# --- What hex letters exist BEFORE the col-6 hex letters ---
print("\n" + "=" * 66)
print("Hex letters in col 6 by position")
print("=" * 66)
for r in range(14):
    ch = G[r][5]  # col 6, 0-indexed 5
    marker = "  ★ HEX" if ch in HEX else ""
    print(f"  ({r+1}, 6): {ch!r}{marker}")


print("\n" + "=" * 66)
print("FINAL CANDIDATES FROM ROW-6 ANALYSIS")
print("=" * 66)
candidates = [
    (32, "Row 6 hex sum alone"),
    (33, "Col 6 hex sum (the 'step by six' column)"),
    (51+89+24+89+41, "Rows 1-5 (before row 6) hex sum"),
    (51+89+24+89+41+32, "Rows 1-6 hex sum"),
    (sum(totals), "All rows hex sum (= col sum too)"),
]
for v, d in sorted(set(candidates)):
    print(f"  {v:>5}  {d}")
