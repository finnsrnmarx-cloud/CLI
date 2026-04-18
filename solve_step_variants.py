"""solve_step_variants.py — Explore different 'step by six' mechanics
starting from principled start positions.

Key candidate starts:
  (1,11) = 's' — S of the word 'start' (king-path start)
  (1,14) = 't' — T at end of 'start' king-path
  (14,12) = 's' — S of 'six' in the bottom row
  (2,8) = 'a' — start of ALUMINUM straight diagonal
  (1,8) = 'd' — top of dash/wire column
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

flat = []
flat_pos = []
for r in range(H):
    for c in range(W):
        if G[r][c] != "-":
            flat.append(G[r][c])
            flat_pos.append((r + 1, c + 1))
flat_str = "".join(flat)


def flat_idx(row1, col1):
    """Return flat index for 1-indexed (row, col). Returns None if it's the dash."""
    if G[row1 - 1][col1 - 1] == "-":
        return None
    # Count non-dash cells up to (row1, col1)
    idx = 0
    for r in range(H):
        for c in range(W):
            if r == row1 - 1 and c == col1 - 1:
                return idx
            if G[r][c] != "-":
                idx += 1
    return None


# --- Mechanic A: step 6 in flat reading order ---------------------------
def mechanic_A(start_flat):
    letters, hex_letters, s = [], [], 0
    for i in range(start_flat, len(flat_str), 6):
        ch = flat_str[i]
        letters.append(ch)
        if ch in HEX:
            hex_letters.append(ch)
            s += HEX[ch]
    return s, "".join(letters), "".join(hex_letters)


# --- Mechanic B: move 6 king-cells in a direction -----------------------
DIRS = {"E": (0, 1), "S": (1, 0), "SE": (1, 1), "NE": (-1, 1), "W": (0, -1),
        "N": (-1, 0), "SW": (1, -1), "NW": (-1, -1)}


def mechanic_B(r0, c0, direction, step=6):
    """Move by step cells at a time in the given direction."""
    dr, dc = DIRS[direction]
    letters, hex_letters, s = [], [], 0
    r, c = r0 - 1, c0 - 1
    while 0 <= r < H and 0 <= c < W:
        ch = G[r][c]
        if ch != "-":
            letters.append(ch)
            if ch in HEX:
                hex_letters.append(ch)
                s += HEX[ch]
        r += step * dr
        c += step * dc
    return s, "".join(letters), "".join(hex_letters)


# --- Mechanic C: take every Nth row / col ------------------------------
def mechanic_row(step=6, start=0):
    cells = []
    s, hex_letters = 0, []
    for r in range(start, H, step):
        for c in range(W):
            ch = G[r][c]
            if ch != "-":
                cells.append(ch)
                if ch in HEX:
                    hex_letters.append(ch)
                    s += HEX[ch]
    return s, "".join(cells), "".join(hex_letters)


def mechanic_col(step=6, start=0):
    cells = []
    s, hex_letters = 0, []
    for c in range(start, W, step):
        for r in range(H):
            ch = G[r][c]
            if ch != "-":
                cells.append(ch)
                if ch in HEX:
                    hex_letters.append(ch)
                    s += HEX[ch]
    return s, "".join(cells), "".join(hex_letters)


# ===================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("MECHANIC A: step 6 in flat reading order, from principled starts")
    print("=" * 70)
    starts = [
        ((1, 1), "grid top-left, first cell"),
        ((1, 3), "first hex letter 'd'"),
        ((1, 5), "first letter of FINDTHESTART king path 'f'"),
        ((1, 8), "top of dash/wire column 'd'"),
        ((1, 11), "S of the word 'start' king-path"),
        ((1, 14), "T at end of 'start' king-path"),
        ((2, 8), "A of ALUMINUM diagonal"),
        ((14, 11), "S of 'six' in bottom row"),
        ((14, 12), "I of 'six' in bottom row"),
        ((14, 1), "T of bottom row"),
    ]
    for (r, c), label in starts:
        i = flat_idx(r, c)
        if i is None:
            continue
        s, _, hex_s = mechanic_A(i)
        print(f"  ({r:2d},{c:2d}) {G[r-1][c-1]!r} flat={i:3d}  {label}")
        print(f"         hex-letters: {hex_s}  sum={s}  +2026={s + 2026}")

    print("\n" + "=" * 70)
    print("MECHANIC B: move 6 cells per step in a direction")
    print("=" * 70)
    from_cells = [(1, 1), (1, 8), (1, 11), (2, 8), (14, 1)]
    for r, c in from_cells:
        print(f"\n  Start ({r},{c}) = {G[r-1][c-1]!r}:")
        for d in ["E", "S", "SE", "NE"]:
            s, cells, hex_s = mechanic_B(r, c, d, step=6)
            print(f"    dir {d:<2} (step 6): {cells!r:<20} hex={hex_s!r:<10} sum={s:<4} +2026={s + 2026}")

    print("\n" + "=" * 70)
    print("MECHANIC C: every Nth row (stepping by 6)")
    print("=" * 70)
    for start in range(6):
        s, cells, hex_s = mechanic_row(step=6, start=start)
        rows_used = [r + 1 for r in range(start, H, 6)]
        print(f"  rows {rows_used}: hex={hex_s}  sum={s}  +2026={s + 2026}")

    print("\n" + "=" * 70)
    print("MECHANIC D: every Nth col (stepping by 6)")
    print("=" * 70)
    for start in range(6):
        s, cells, hex_s = mechanic_col(step=6, start=start)
        cols_used = [c + 1 for c in range(start, W, 6)]
        print(f"  cols {cols_used}: hex={hex_s}  sum={s}  +2026={s + 2026}")

    print("\n" + "=" * 70)
    print("MECHANIC E: step 6 along a king-path of 'SIX'")
    print("=" * 70)
    # SIX king-path is (14,12)→(14,13)→(14,14) — only 3 cells
    six_path = [(13, 11), (13, 12), (13, 13)]
    print(f"  SIX king-path: {[(r+1, c+1) for r, c in six_path]}")
    letters = [G[r][c] for r, c in six_path]
    print(f"  Letters: {letters}")
    # Extend the path every 6-th cell? Not obvious.

    print("\n" + "=" * 70)
    print("ADDITIONAL IDEAS")
    print("=" * 70)
    # Row 6 + Col 6 — interesting rows
    row6 = "".join(G[5])
    col6 = "".join(G[r][5] for r in range(H))
    print(f"  Row 6:  {row6!r}")
    print(f"  Col 6:  {col6!r}")
    print(f"  Row 6 hex sum: {sum(HEX.get(c, 0) for c in row6)}")
    print(f"  Col 6 hex sum: {sum(HEX.get(c, 0) for c in col6)}")

    # Row 12 + Col 12
    row12 = "".join(G[11])
    col12 = "".join(G[r][11] for r in range(H))
    print(f"\n  Row 12:  {row12!r}")
    print(f"  Col 12:  {col12!r}")
    print(f"  Row 12 hex sum: {sum(HEX.get(c, 0) for c in row12)}")
    print(f"  Col 12 hex sum: {sum(HEX.get(c, 0) for c in col12)}")
