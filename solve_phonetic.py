"""solve_phonetic.py — Phonetic/cipher readings of the bottom row and
element-hex connections.

Hypotheses tested:
  1. 'tunenty-tessix' contains hidden Roman numerals (tess-IX → IX=9)
  2. Extras letters TUNES summed as alphabet positions
  3. Element symbols interpreted as hex (Fe=0xFE=254, etc.)
  4. Combinations with the 2180 family of results
"""

from __future__ import annotations

# Alphabet position (1-indexed) lookup
def alpha_val(s: str) -> int:
    return sum(ord(c) - ord('a') + 1 for c in s.lower() if c.isalpha())


# --- 1. Bottom row phonetic decomposition --------------------------------
print("=" * 70)
print("BOTTOM ROW PHONETIC / HIDDEN-ROMAN ANALYSIS")
print("=" * 70)

bottom = "tunentytessix"  # hyphen removed
print(f"Bottom row letters: {bottom!r} ({len(bottom)} letters)")

# Roman numeral interpretation: find IX, XI, IV, VI, etc. as substrings
roman_substrings = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xx", "xxx"]
print("\n--- Roman numerals as substrings of bottom row ---")
for r in roman_substrings:
    if r in bottom:
        idx = bottom.find(r)
        print(f"  {r!r:6s} found at position {idx}  -> value {int(r, ...) if False else 'roman'}")
        # manual roman conversion
        roman_map = {"i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5, "vi": 6,
                     "vii": 7, "viii": 8, "ix": 9, "x": 10, "xi": 11,
                     "xii": 12, "xx": 20, "xxx": 30}
        print(f"        value = {roman_map.get(r, '?')}")

# Specifically: 'ix' is at position 11-12 of bottom (last two chars before x-at-13)
# Actually: bottom = t u n e n t y t e s s i x (pos 0..12)
# 'ix' = positions 11, 12
print(f"\n  Last 3 chars of bottom: {bottom[-3:]!r}  (s, i, x = literally 'six', also ends in 'IX' = roman 9)")

# --- 2. Interpret 'twentysix' as '20 + IX' = 29 ---------------------------
print("\n--- If the last 'ix' is Roman 9 instead of part of 'six' ---")
print(f"  twenty + IX (9) = 29")
print(f"  twenty - IX (9) = 11")
print(f"  2020 + 9 = 2029")
print(f"  2026 - IX = 2017")

# --- 3. TUNES anagram → atomic values ------------------------------------
print("\n" + "=" * 70)
print("TUNES (anagram of extras U,N,T,E,S) — alphabet / element links")
print("=" * 70)
TUNES = "tunes"
print(f"  letters: {list(TUNES)}")
print(f"  alphabet-position values: t=20 u=21 n=14 e=5 s=19")
s = alpha_val(TUNES)
print(f"  SUM  = {s}  ← striking: atomic number of GOLD (Au) is 79")
print(f"  GOLD is the iconic 'dig for' metal ← puzzle theme")
print(f"  Product: 20*21*14*5*19 = {20*21*14*5*19}")

# --- 4. Element symbols in hex --------------------------------------------
print("\n" + "=" * 70)
print("ELEMENT SYMBOLS as hex-digit strings")
print("=" * 70)
# Hex-valid letters: a, b, c, d, e, f (plus 0-9)
HEX_SET = set("abcdef0123456789")
elements = [
    ("H", 1), ("He", 2), ("Li", 3), ("Be", 4), ("B", 5), ("C", 6),
    ("N", 7), ("O", 8), ("F", 9), ("Ne", 10), ("Na", 11), ("Mg", 12),
    ("Al", 13), ("Si", 14), ("P", 15), ("S", 16), ("Cl", 17), ("Ar", 18),
    ("K", 19), ("Ca", 20), ("Fe", 26), ("Ni", 28), ("Cu", 29), ("Zn", 30),
    ("Ba", 56), ("Ce", 58), ("Dy", 66), ("Ho", 67), ("Au", 79), ("Pb", 82),
    ("U", 92), ("Ac", 89), ("Cd", 48), ("Cf", 98), ("Db", 105), ("Sn", 50),
    ("Ag", 47), ("Bi", 83),
]
print(f"  Symbol  Z    hex?   hex value (if valid)")
full_hex_elements = []
for sym, z in elements:
    ls = sym.lower()
    is_hex = all(c in HEX_SET for c in ls)
    if is_hex and len(ls) == 2:
        try:
            hv = int(ls, 16)
            full_hex_elements.append((sym, z, hv))
            print(f"  {sym:<3}     {z:<3}  ALL-HEX  0x{sym.lower()} = {hv}")
        except ValueError:
            print(f"  {sym:<3}     {z:<3}  partial")
    else:
        # Still show if single hex letter
        if is_hex and len(ls) == 1:
            try:
                hv = int(ls, 16)
                print(f"  {sym:<3}     {z:<3}  single-hex  0x{sym.lower()} = {hv}")
            except:
                pass

print(f"\n  Fe (iron) = 0xFE = 254  ← iron Z=26, hex symbol = 254")
print(f"  Au (gold) = 0xA? — u isn't hex")
print(f"  Be (beryl) = 0xBE = 190")
print(f"  Ce (cerium) = 0xCE = 206")
print(f"  Ac (actinium) = 0xAC = 172")

# --- 5. Element atomic numbers in hex -------------------------------------
print("\n--- Atomic numbers → hex ---")
for z in [13, 26, 50, 79]:
    print(f"  Z={z}  -> hex 0x{z:X}")
print(f"  2026 -> hex 0x{2026:X}  = 0x7EA")
print(f"  2180 -> hex 0x{2180:X}  = 0x884")

# --- 6. Combine with 2180 family ------------------------------------------
print("\n" + "=" * 70)
print("COMBINATIONS")
print("=" * 70)
combos = {
    "2180 (Gemini base)": 2180,
    "154 + 79 (TUNES = Au)": 154 + 79,
    "2026 + 79 (year + Au)": 2026 + 79,
    "2026 + 63 (year + Al+Sn)": 2026 + 63,
    "2026 + 29 (twenty-IX)": 2026 + 29,
    "2026 + 13 + 50 + 79 (Al+Sn+Au)": 2026 + 13 + 50 + 79,
    "2026 + 254 (year + iron-hex)": 2026 + 254,
    "154 + 254 (innersum + iron-hex)": 154 + 254,
    "154 + 63 (innersum + Al+Sn)": 154 + 63,
    "154 + 29 (innersum + 20+IX)": 154 + 29,
    "154 + 2026 + 79 (full chain +Au)": 154 + 2026 + 79,
    "154 + 2026 + 29 (full + 20+IX)": 154 + 2026 + 29,
}
for label, val in sorted(combos.items(), key=lambda x: x[1]):
    print(f"  {label:<40s} = {val}")

# --- 7. Just the straight-line elements (Al + Sn) + year ------------------
print("\n--- Just the CONFIRMED straight-line elements ---")
print(f"  Al ({13}) + Sn ({50}) = 63")
print(f"  Al*Sn = 650")
print(f"  year 2026 + 63 = 2089")
print(f"  year 2026 + 650 = 2676")
print(f"  year 2026 - 63 = 1963")

# --- 8. Final ranked candidates -------------------------------------------
print("\n" + "=" * 70)
print("RANKED FRESH CANDIDATES (not previously rejected)")
print("=" * 70)
fresh = [
    (79, "TUNES letter sum = Au (Gold) atomic number; GOLD = the 'dig' metal"),
    (29, "twenty + IX (Roman 9) reading of bottom row"),
    (254, "Fe (iron) symbol as hex = 0xFE"),
    (2055, "2026 + 29 (twenty + Roman IX)"),
    (2105, "2026 + 79 (year + Gold)"),
    (2180, "Gemini verified self-contained hex computation"),
    (2089, "2026 + Al+Sn (63)"),
    (2168, "2026 + Al+Sn+Au = 63 + 79 = 142; 2026+142 = 2168"),
    (2280, "2026 + 254 (year + Fe-hex)"),
    (233, "154 inner-sum + 79 (TUNES/Au)"),
    (183, "154 + 29 (inner + twenty-IX)"),
    (142, "Al + Sn + Au = 13+50+79 (triad of dig-metals)"),
    (408, "154 + 254 (inner + Fe-hex)"),
]
for val, desc in fresh:
    print(f"  {val:>6}  {desc}")
