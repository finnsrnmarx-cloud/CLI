"""dash_wire.py — Test dash-is-the-wire interpretation.

Tests the hypothesis that the hyphen at (14,8) IS the 'wire' referenced
in axiom 4 (THERE IS A DATE ON WIRE), and the implications for the
other axioms (especially the starting position).
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
H, W = 14, 14
flat, flat_pos = [], []
for r in range(H):
    for c in range(W):
        if G[r][c] != "-":
            flat.append(G[r][c])
            flat_pos.append((r+1, c+1))
flat_str = "".join(flat)

HEX = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}


def step6_hex(start, step=6):
    total, letters, hex_letters = 0, [], []
    for i in range(start, len(flat_str), step):
        ch = flat_str[i]
        letters.append(ch)
        if ch in HEX:
            hex_letters.append(ch)
            total += HEX[ch]
    return total, "".join(letters), "".join(hex_letters)


print("=" * 70)
print("WIRE = DASH AT (14,8). The wire is vertical in column 8.")
print("=" * 70)

col8 = "".join(G[r][7] for r in range(H) if G[r][7] != "-")
print(f"\nColumn 8 (top to bottom, excluding dash): {col8!r}")
print(f"Length: {len(col8)}")

hex_in_col8 = [ch for ch in col8 if ch in HEX]
sum_col8 = sum(HEX[ch] for ch in hex_in_col8)
print(f"Hex letters in col 8: {hex_in_col8!r}  sum = {sum_col8}")
print(f"Col 8 hex sum + 2026 = {sum_col8 + 2026}")
print(f"Col 8 hex sum + 26   = {sum_col8 + 26}")

col8_rev = col8[::-1]
print(f"\nColumn 8 read bottom-up: {col8_rev!r}")


print("\n" + "=" * 70)
print("START AT (1,8) — TOP OF WIRE COLUMN — AND STEP BY 6")
print("=" * 70)
start_flat = 7
total, letters, hex_only = step6_hex(start_flat)
print(f"Starting at flat[{start_flat}] = {flat_str[start_flat]!r} at {flat_pos[start_flat]}")
print(f"Letters visited (step 6): {letters}")
print(f"Hex-only: {hex_only!r}")
print(f"Hex sum: {total}")
print(f"Hex sum + 2026: {total + 2026}")
print(f"Hex sum + 26:   {total + 26}")
print(f"Hex sum + 6:    {total + 6}")


print("\n" + "=" * 70)
print("ALTERNATIVE: WIRE = ROW 14 (row containing the dash)")
print("=" * 70)
row14 = "".join(G[13])
row14_letters = row14.replace("-", "")
print(f"Row 14 letters: {row14_letters!r}")
hex_in_r14 = [ch for ch in row14_letters if ch in HEX]
print(f"Hex letters: {hex_in_r14}")
print(f"Hex sum in row 14: {sum(HEX[c] for c in hex_in_r14)}")

print("\nStep by 6 within row 14:")
for offset in range(6):
    stepped = [row14_letters[i] for i in range(offset, len(row14_letters), 6)]
    hex_stepped = [c for c in stepped if c in HEX]
    s = sum(HEX[c] for c in hex_stepped)
    print(f"  offset {offset}: {stepped} → hex {hex_stepped} = {s}")


print("\n" + "=" * 70)
print("IF THE WIRE POINTS TO ROW 14 AS DATE=2026, THEN SEEK GRID HEX SUM")
print("=" * 70)

# Various hex totals across grid
total_all_hex = sum(HEX[c] for c in flat_str if c in HEX)
print(f"Sum of ALL hex letters in grid: {total_all_hex}")
print(f"  + 2026 = {total_all_hex + 2026}")
print(f"  - 2026 = {total_all_hex - 2026 if total_all_hex > 2026 else 2026 - total_all_hex}")
print(f"  * 6    = {total_all_hex * 6}")

# How many hex letters are in col 8 vs elsewhere
print(f"\nCol 8 hex sum:          {sum_col8}")
print(f"Row 14 hex sum:         {sum(HEX[c] for c in row14_letters if c in HEX)}")
print(f"Grid total hex sum:     {total_all_hex}")
print(f"Grid minus col 8:       {total_all_hex - sum_col8}")
print(f"Grid minus row 14:      {total_all_hex - sum(HEX[c] for c in row14_letters if c in HEX)}")


print("\n" + "=" * 70)
print("CANDIDATE ANSWERS (dash-as-wire hypothesis)")
print("=" * 70)
candidates = [
    (sum_col8, "Sum of hex letters in col 8 alone"),
    (sum_col8 + 2026, "Col 8 hex sum + 2026"),
    (sum_col8 + 26, "Col 8 hex sum + 26"),
    (total, "Step-6 from (1,8) hex sum alone"),
    (total + 2026, "Step-6 from (1,8) + 2026"),
    (total + 26, "Step-6 from (1,8) + 26"),
    (total + 6, "Step-6 from (1,8) + 6"),
    (total_all_hex, "Sum of ALL hex letters in grid"),
    (total_all_hex + 2026, "All hex + 2026"),
    (total_all_hex + 26, "All hex + 26"),
]
for v, d in sorted(set(candidates)):
    print(f"  {v:>6}  {d}")
