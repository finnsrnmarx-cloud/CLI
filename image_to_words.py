"""Try to transform the image hex bytes into words/letters.

Approaches:
  1. Raw ASCII decode of each byte
  2. Bytes mod 26 -> A..Z
  3. Hex-letter-only bytes (0x0A..0x0F) -> 'a'..'f' — read as hex string
  4. Nibble pairs -> letter lookup in grid by (row,col)
  5. Byte value -> grid position (row = byte//14, col = byte%14)
"""
from __future__ import annotations

RAW = """
FF D8 FF E0 00 10 4A 46 49 46 00 01 01 01 00 90 00 90 00 00 FF DB 00 43 00 03 02 02 03 02 02 03 03 03
04 03 03 04 05 08 05 05 04 04 05 0A 07 07 06 08 0C 0A 0C 0C 0B 0A 0B 0B 0D 0E 12 10 0D 0E 11 0E 0B 0B 10
16 10 11 13 14 15 15 15 0C 0F 17 18 16 14 18 12 14 15 14 FF DB 00 43 01 03 04 04 05 04 05 09 05 09 14
0D 0B 0D 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14
""".strip()
bs = [int(t, 16) for t in RAW.split()]
n = len(bs)

GRID = [
    "rsdifindthsart",
    "ehreSodaeetgna",
    "nEtrhalxhgowip",
    "egeDauyueAnrpp",
    "ptnNmllmxidnee",
    "ohuinkthAnacsm",
    "alnPfyldebsttn",
    "uumjarebEmehrw",
    "mithDceigiugts",
    "tlamIbftoteget",
    "sailnIiTniapen",
    "nsToaGrniiobrt",
    "ieTirYeesprayw",
    "tunentY-tessix",
]
g = [row.lower() for row in GRID]

# 1. ASCII decode (print only printable)
ascii_str = "".join(chr(b) if 32 <= b < 127 else "." for b in bs)
print("=== 1. ASCII decode of all bytes ===")
print(ascii_str)
print()

# 2. Bytes mod 26 -> letter
print("=== 2. byte % 26 -> A..Z ===")
mod26 = "".join(chr(ord('A') + (b % 26)) for b in bs)
print(mod26)
print()

# 3. Only the "hex letter" bytes (0x0A..0x0F)  -> a..f
print("=== 3. Only hex-letter bytes (0x0A..0x0F) as a..f ===")
hexlets = "".join("abcdef"[b - 10] for b in bs if 10 <= b <= 15)
print(f"  ({len(hexlets)} chars): {hexlets}")
print()

# 4. Byte value as grid index (row-major, 14x14 = 196 cells)
print("=== 4. Byte value -> grid cell (row-major, byte < 196) ===")
letters = []
for b in bs:
    if b < 196:
        r, c = divmod(b, 14)
        letters.append(g[r][c])
    else:
        letters.append(".")
print("".join(letters))
print()

# 5. Nibble -> row, nibble -> col (both nibbles < 14)
print("=== 5. High nibble=row, low nibble=col (both <14) ===")
letters = []
for b in bs:
    hi, lo = b >> 4, b & 0xF
    if hi < 14 and lo < 14:
        letters.append(g[hi][lo])
    else:
        letters.append(".")
print("".join(letters))
print()

# 6. Step-6 bytes -> grid cells
print("=== 6. Step-6 bytes as grid lookups (byte<196, row-major) ===")
for off in range(6):
    out = []
    for i in range(off, n, 6):
        b = bs[i]
        if b < 196:
            r, c = divmod(b, 14)
            out.append(g[r][c])
        else:
            out.append(".")
    print(f"  off {off}: {''.join(out)}")
print()

# 7. Bytes interpreted as alphabet positions (1..26)
print("=== 7. Bytes in range 1..26 -> letter ===")
out = "".join(chr(ord('a') + b - 1) if 1 <= b <= 26 else "." for b in bs)
print(out)
