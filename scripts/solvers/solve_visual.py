"""solve_visual.py — Visualize the grid as binary patterns to look for
QR codes, finder patterns, or other visual encodings.
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
H = W = 14

HEX = set("abcdef")
VOWELS = set("aeiouy")


def visualize(predicate, label):
    print(f"\n{label}")
    print("  " + " ".join(str(c % 10) for c in range(1, W + 1)))
    for r in range(H):
        marks = ["█" if predicate(G[r][c]) else "·" for c in range(W)]
        print(f"{r+1:>2} " + " ".join(marks))


def visualize_letters(letters_set, label):
    visualize(lambda ch: ch in letters_set, label)


# 1. Hex letters (a-f)
visualize_letters(HEX, "HEX LETTERS (a-f) = █")

# 2. Vowels
visualize_letters(VOWELS, "VOWELS (a,e,i,o,u,y) = █")

# 3. U only
visualize_letters({"u"}, "U ONLY = █")

# 4. Letter T only (most common after E)
visualize_letters({"t"}, "T ONLY = █")

# 5. Letter E only (most common)
visualize_letters({"e"}, "E ONLY = █")

# 6. Specific pattern: "musical" letters a-g
visualize_letters(set("abcdefg"), "MUSICAL LETTERS (a-g) = █")

# 7. Letters that are hex AND vowels (a, e)
visualize_letters({"a", "e"}, "HEX-VOWELS (a, e) = █")

# 8. Letters of "VANADIUM" (v, a, n, d, i, u, m)
visualize_letters({"v", "a", "n", "d", "i", "u", "m"}, "VANADIUM LETTERS (vanadium) = █")

# 9. Letters of "DIG" only
visualize_letters({"d", "i", "g"}, "DIG LETTERS = █")

# 10. ASCII binary: each letter -> 0/1 based on (alphabet pos % 2)
visualize(lambda ch: ch != "-" and (ord(ch) - 96) % 2 == 1, "ALPHABET-POSITION ODD = █")

# Look for 7x7 finder-pattern-like structures
print("\n\n=== QR FINDER PATTERN CHECK ===")
print("A QR finder pattern (7x7) looks like:")
print("  ███████")
print("  █·····█")
print("  █·███·█")
print("  █·███·█")
print("  █·███·█")
print("  █·····█")
print("  ███████")
print("\nThe 14x14 grid is too small to contain even one finder pattern (7x7)")
print("at any standard QR position. Smallest QR code is Version 1 = 21x21.")
print("So a literal QR code is not possible. Could be a custom 14x14 encoding.")

# Compute each row as a 14-bit binary number under hex-vs-not interpretation
print("\n\n=== ROWS AS 14-BIT BINARY NUMBERS (hex letter = 1) ===")
for r in range(H):
    bits = "".join("1" if G[r][c] in HEX else "0" for c in range(W))
    val = int(bits, 2)
    hexv = f"0x{val:04X}"
    print(f"  row {r+1:>2}: {bits}  = {val:>5}  ({hexv})")

# Sum of all such numbers
total = sum(int("".join("1" if G[r][c] in HEX else "0" for c in range(W)), 2)
            for r in range(H))
print(f"\n  Sum of all row binary numbers: {total}")
print(f"  Sum + 2026: {total + 2026}")

# Same for columns
print("\n\n=== COLS AS 14-BIT BINARY NUMBERS (hex letter = 1) ===")
for c in range(W):
    bits = "".join("1" if G[r][c] in HEX else "0" for r in range(H))
    val = int(bits, 2)
    print(f"  col {c+1:>2}: {bits}  = {val:>5}  (0x{val:04X})")

# Look at U placement - count and unique pattern
print("\n\n=== U PLACEMENT FINGERPRINT ===")
u_positions = [(r + 1, c + 1) for r in range(H) for c in range(W) if G[r][c] == "u"]
print(f"  U positions: {u_positions}")
# As bit positions in 14*14=196 grid
bit_positions = [(r * 14 + c) for r in range(H) for c in range(W) if G[r][c] == "u"]
print(f"  As 0-indexed flat positions: {bit_positions}")
print(f"  Sum of bit positions: {sum(bit_positions)}")

# What 7-bit/8-bit/etc binary do U positions form if we read in raster order?
flat_bits = "".join("1" if G[r][c] == "u" else "0" for r in range(H) for c in range(W))
print(f"  Flat U bitmap (196 bits): {flat_bits[:80]}...")
print(f"  As big int: {int(flat_bits, 2)}")
