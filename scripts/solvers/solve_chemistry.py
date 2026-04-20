"""Phase 5 — Chemistry deep dive.

Hypothesis: the grid points to a CHEMICAL REACTION whose product is the answer.

Key clue: ALUMINUM is the most distinctive element name in the grid. The
aluminothermic process uses Al to industrially produce VANADIUM from V2O5:
  V2O5 + 10 Al -> 2 V + 5 Al2O3

VANADIUM (V) is also the missing letter from the grid (Q, V, Z absent).
This creates a beautiful self-consistent loop:
  - Grid contains ALUMINUM (the reagent)
  - Grid is missing V (the product you must EXTRACT)
  - Title 'Can U Dig It?' = can you DIG OUT the missing element?
  - Answer = 23 (Vanadium atomic number)
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
DIRS = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]


def king_adjacent_pairs(sym):
    """Find all king-adjacent letter pairs spelling sym."""
    if len(sym) != 2:
        return []
    pairs = []
    for r in range(H):
        for c in range(W):
            if G[r][c] != sym[0]:
                continue
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and G[nr][nc] == sym[1]:
                    pairs.append(((r+1, c+1), (nr+1, nc+1)))
    return pairs


# 1-letter symbols present in grid
ONE_LETTER_ELEMENTS = {
    "h": ("H", 1), "b": ("B", 5), "c": ("C", 6), "n": ("N", 7),
    "o": ("O", 8), "f": ("F", 9), "p": ("P", 15), "s": ("S", 16),
    "k": ("K", 19), "y": ("Y", 39), "i": ("I", 53), "w": ("W", 74),
    "u": ("U", 92),
}

# 2-letter symbols (case-insensitive lowercase)
TWO_LETTER_ELEMENTS = {
    "he": ("He", 2), "li": ("Li", 3), "be": ("Be", 4), "ne": ("Ne", 10),
    "na": ("Na", 11), "mg": ("Mg", 12), "al": ("Al", 13), "si": ("Si", 14),
    "cl": ("Cl", 17), "ar": ("Ar", 18), "ca": ("Ca", 20),
    "sc": ("Sc", 21), "ti": ("Ti", 22), "cr": ("Cr", 24), "mn": ("Mn", 25),
    "fe": ("Fe", 26), "co": ("Co", 27), "ni": ("Ni", 28), "cu": ("Cu", 29),
    "zn": ("Zn", 30), "ga": ("Ga", 31), "ge": ("Ge", 32), "as": ("As", 33),
    "se": ("Se", 34), "br": ("Br", 35), "kr": ("Kr", 36), "rb": ("Rb", 37),
    "sr": ("Sr", 38), "zr": ("Zr", 40), "nb": ("Nb", 41), "mo": ("Mo", 42),
    "tc": ("Tc", 43), "ru": ("Ru", 44), "rh": ("Rh", 45), "pd": ("Pd", 46),
    "ag": ("Ag", 47), "cd": ("Cd", 48), "in": ("In", 49), "sn": ("Sn", 50),
    "sb": ("Sb", 51), "te": ("Te", 52), "xe": ("Xe", 54), "cs": ("Cs", 55),
    "ba": ("Ba", 56), "la": ("La", 57), "ce": ("Ce", 58), "pr": ("Pr", 59),
    "nd": ("Nd", 60), "pm": ("Pm", 61), "sm": ("Sm", 62), "eu": ("Eu", 63),
    "gd": ("Gd", 64), "tb": ("Tb", 65), "dy": ("Dy", 66), "ho": ("Ho", 67),
    "er": ("Er", 68), "tm": ("Tm", 69), "yb": ("Yb", 70), "lu": ("Lu", 71),
    "hf": ("Hf", 72), "ta": ("Ta", 73), "re": ("Re", 75), "os": ("Os", 76),
    "ir": ("Ir", 77), "pt": ("Pt", 78), "au": ("Au", 79), "hg": ("Hg", 80),
    "tl": ("Tl", 81), "pb": ("Pb", 82), "bi": ("Bi", 83), "po": ("Po", 84),
    "at": ("At", 85), "rn": ("Rn", 86), "fr": ("Fr", 87), "ra": ("Ra", 88),
    "ac": ("Ac", 89), "th": ("Th", 90), "pa": ("Pa", 91), "np": ("Np", 93),
    "pu": ("Pu", 94), "am": ("Am", 95), "cm": ("Cm", 96), "bk": ("Bk", 97),
    "cf": ("Cf", 98), "es": ("Es", 99), "fm": ("Fm", 100),
}

print("=" * 70)
print("ALL 2-letter element symbols as king-adjacent pairs in grid")
print("=" * 70)
elements_found = {}
for sym_lower, (sym_disp, z) in TWO_LETTER_ELEMENTS.items():
    pairs = king_adjacent_pairs(sym_lower)
    if pairs:
        elements_found[sym_disp] = (z, len(pairs))
        # show first 3 placements
        cells = pairs[:3]
        print(f"  {sym_disp:4s} (Z={z:3d})  {len(pairs):3d} placement(s)  e.g. {cells}")

# Sum and analyse
print(f"\nTotal distinct 2-letter elements found as adjacent pairs: {len(elements_found)}")
print(f"Sum of all atomic numbers: {sum(z for z, _ in elements_found.values())}")

# Critical: V (Vanadium, Z=23) — does its symbol 'v' exist? No, V is missing!
print("\n" + "=" * 70)
print("THE VANADIUM HYPOTHESIS")
print("=" * 70)
print(f"  V (Vanadium, Z=23) — CANNOT be found in grid because letter 'v' is absent")
print(f"  Industrial production of V: aluminothermic reduction")
print(f"  V2O5 + 10 Al -> 2 V + 5 Al2O3")
print()
print(f"  ALUMINUM is in the grid (8-letter diagonal at (2,8)→SW)")
print(f"  Aluminum (Z=13) + Vanadium pentoxide -> Vanadium (Z=23)")
print()
print(f"  Mechanism interpretation:")
print(f"    - Grid contains the REAGENT (Al)")
print(f"    - Grid is MISSING the PRODUCT (V)")
print(f"    - Title 'Can U Dig It?' = can you EXTRACT the missing V?")
print(f"    - ANSWER = 23")

# Additional reactions worth noting
print("\n" + "=" * 70)
print("Other thermite-style reactions where Al reduces a metal oxide")
print("=" * 70)
reactions = [
    ("Iron",       "Fe2O3", "Al + Fe2O3 -> Al2O3 + 2 Fe", 26),
    ("Vanadium",   "V2O5",  "10 Al + 3 V2O5 -> 5 Al2O3 + 6 V", 23),
    ("Chromium",   "Cr2O3", "2 Al + Cr2O3 -> Al2O3 + 2 Cr", 24),
    ("Manganese",  "MnO2",  "4 Al + 3 MnO2 -> 2 Al2O3 + 3 Mn", 25),
    ("Titanium",   "TiO2",  "4 Al + 3 TiO2 -> 2 Al2O3 + 3 Ti", 22),
    ("Copper",     "CuO",   "2 Al + 3 CuO -> Al2O3 + 3 Cu", 29),
    ("Nickel",     "NiO",   "2 Al + 3 NiO -> Al2O3 + 3 Ni", 28),
    ("Niobium",    "Nb2O5", "10 Al + 3 Nb2O5 -> 5 Al2O3 + 6 Nb", 41),
    ("Tungsten",   "WO3",   "2 Al + WO3 -> Al2O3 + W", 74),
    ("Molybdenum", "MoO3",  "2 Al + MoO3 -> Al2O3 + Mo", 42),
]
print(f"  {'Product':<12s} {'Z':<4s} {'oxide':<10s} reaction")
for name, oxide, rxn, z in reactions:
    print(f"  {name:<12s} {z:<4d} {oxide:<10s} {rxn}")

# Check which of these PRODUCTS' letters are missing from the grid
print("\n  PRODUCTS whose ELEMENT NAME letters include a letter MISSING from the grid:")
print("    (V=missing, Q=missing, Z=missing)")
for name, oxide, rxn, z in reactions:
    name_lower = name.lower()
    missing_in_name = [c for c in name_lower if c in "qvz"]
    if missing_in_name:
        print(f"    {name} (Z={z}) — contains missing letter(s): {missing_in_name}")

# Sn smelting
print("\n" + "=" * 70)
print("Tin smelting (carbothermic reduction)")
print("=" * 70)
print("  SnO2 + 2C -> Sn + 2CO2")
print("  Cassiterite (SnO2, tin oxide) + carbon -> Tin + carbon dioxide")
print("  Sn is in the grid; carbon (C) is also a 1-letter symbol present")
