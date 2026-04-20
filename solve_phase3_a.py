"""Phase 3a — Alternative hex/cipher interpretations.

Tests:
  1. What if "HEXADECIMALS" means sum as 16-base number rather than decimal?
  2. What if we READ the entire 167 path as a hex string?
  3. Sum of ALL letters (not just a-f) using some alphabet-to-digit cipher
  4. The 5 axioms' LAST LETTERS alphabet sum
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

flat = [G[r][c] for r in range(H) for c in range(W) if G[r][c] != "-"]
flat_str = "".join(flat)

# Step-6 from 'd' (flat index 2)
start = 2
step6_chars = [flat_str[i] for i in range(start, len(flat_str), 6)]
step6_hex_only = [c for c in step6_chars if c in HEX]

print("=" * 60)
print("Alternative: read the step-6 hex letters AS a hex string")
print("=" * 60)
hex_str = "".join(step6_hex_only)
print(f"  Hex string: '{hex_str}' ({len(hex_str)} chars)")
try:
    as_number = int(hex_str, 16)
    print(f"  As hex number: {as_number}")
except ValueError:
    print("  Not parseable")

print(f"\n  Hex sum (a+b+c…): {sum(HEX[c] for c in step6_hex_only)}")

# Is 167 (0xA7) itself hex?
print(f"\n  167 in hex: 0x{167:X}")
print(f"  Reverse: hex 'A7' = {int('a7', 16)} = 167  ✓ cute")

# 1-letter element symbols sum using positions
print("\n" + "=" * 60)
print("Path cell alphabet positions (for the 167 path):")
print("=" * 60)
path_alpha = [ord(c) - 96 for c in step6_chars]
print(f"  Letters: {''.join(step6_chars)}")
print(f"  Alphabet positions: {path_alpha}")
print(f"  Sum: {sum(path_alpha)}")
print(f"  Product: small-ish: {1 if not path_alpha else eval('*'.join(str(x) for x in path_alpha))}")

# 5 axioms' LAST LETTERS alphabet sum
print("\n" + "=" * 60)
print("Sum of alphabet positions of LAST LETTERS of each axiom")
print("=" * 60)
last_letters = {"findthestart": "t", "addthehexadecimals": "s",
                "stepbysix": "x", "thereisadateonwire": "e",
                "lastentryentireinteger": "r"}
total_alpha = 0
for ax, ltr in last_letters.items():
    a = ord(ltr) - 96
    total_alpha += a
    print(f"  {ax:30s}  last='{ltr}'  alpha={a}")
print(f"\n  Sum: {total_alpha}")
print(f"  Concatenated last letters: {''.join(last_letters.values())}")

# First letter of each axiom
print("\n" + "=" * 60)
print("Sum of alphabet positions of FIRST LETTERS of each axiom")
print("=" * 60)
first_letters = {"findthestart": "f", "addthehexadecimals": "a",
                 "stepbysix": "s", "thereisadateonwire": "t",
                 "lastentryentireinteger": "l"}
total_first = 0
for ax, ltr in first_letters.items():
    a = ord(ltr) - 96
    total_first += a
    print(f"  {ax:30s}  first='{ltr}'  alpha={a}")
print(f"\n  Sum: {total_first}")
print(f"  First letters concat: {''.join(first_letters.values())}")
