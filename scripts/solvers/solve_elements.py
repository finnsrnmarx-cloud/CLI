"""solve_elements.py — Search the grid for periodic-table element names.

Hypothesis: ALUMINUM traces as a 'lone' straight-line diagonal. What if
the grid hides a specific set of element names, and the answer is derived
from their atomic numbers?
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

G = [row.split() for row in GRID_RAW.splitlines()]
H, W = len(G), len(G[0])
DIRS8 = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]
DIR_NAMES = {
    (-1, -1): "NW", (-1, 0): "N", (-1, 1): "NE",
    (0, -1): "W", (0, 1): "E",
    (1, -1): "SW", (1, 0): "S", (1, 1): "SE",
}

# Atomic number → element name (standard English)
ELEMENTS = {
    1: "hydrogen", 2: "helium", 3: "lithium", 4: "beryllium",
    5: "boron", 6: "carbon", 7: "nitrogen", 8: "oxygen",
    9: "fluorine", 10: "neon", 11: "sodium", 12: "magnesium",
    13: "aluminum", 14: "silicon", 15: "phosphorus", 16: "sulfur",
    17: "chlorine", 18: "argon", 19: "potassium", 20: "calcium",
    21: "scandium", 22: "titanium", 23: "vanadium", 24: "chromium",
    25: "manganese", 26: "iron", 27: "cobalt", 28: "nickel",
    29: "copper", 30: "zinc", 31: "gallium", 32: "germanium",
    33: "arsenic", 34: "selenium", 35: "bromine", 36: "krypton",
    37: "rubidium", 38: "strontium", 39: "yttrium", 40: "zirconium",
    41: "niobium", 42: "molybdenum", 43: "technetium", 44: "ruthenium",
    45: "rhodium", 46: "palladium", 47: "silver", 48: "cadmium",
    49: "indium", 50: "tin", 51: "antimony", 52: "tellurium",
    53: "iodine", 54: "xenon", 55: "cesium", 56: "barium",
    57: "lanthanum", 58: "cerium", 59: "praseodymium", 60: "neodymium",
    61: "promethium", 62: "samarium", 63: "europium", 64: "gadolinium",
    65: "terbium", 66: "dysprosium", 67: "holmium", 68: "erbium",
    69: "thulium", 70: "ytterbium", 71: "lutetium", 72: "hafnium",
    73: "tantalum", 74: "tungsten", 75: "rhenium", 76: "osmium",
    77: "iridium", 78: "platinum", 79: "gold", 80: "mercury",
    81: "thallium", 82: "lead", 83: "bismuth", 84: "polonium",
    85: "astatine", 86: "radon", 87: "francium", 88: "radium",
    89: "actinium", 90: "thorium", 91: "protactinium", 92: "uranium",
    93: "neptunium", 94: "plutonium", 95: "americium", 96: "curium",
    97: "berkelium", 98: "californium", 99: "einsteinium", 100: "fermium",
    101: "mendelevium", 102: "nobelium", 103: "lawrencium",
}


def find_straight(word: str):
    """Return list of (r, c, dr, dc) for word as a straight placement."""
    results = []
    L = len(word)
    for r in range(H):
        for c in range(W):
            for dr, dc in DIRS8:
                nr = r + (L - 1) * dr
                nc = c + (L - 1) * dc
                if not (0 <= nr < H and 0 <= nc < W):
                    continue
                if all(G[r + i * dr][c + i * dc] == word[i] for i in range(L)):
                    results.append((r, c, dr, dc))
    return results


def count_king_paths(word: str, stop_at=None) -> int:
    count = 0

    def dfs(r, c, i, seen):
        nonlocal count
        if stop_at is not None and count >= stop_at:
            return
        if i == len(word):
            count += 1
            return
        for dr, dc in DIRS8:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in seen and G[nr][nc] == word[i]:
                dfs(nr, nc, i + 1, seen | {(nr, nc)})

    for r in range(H):
        for c in range(W):
            if G[r][c] == word[0]:
                dfs(r, c, 1, frozenset({(r, c)}))
                if stop_at is not None and count >= stop_at:
                    return count
    return count


def find_first_king_path(word: str):
    """Return a single king-path that spells `word`, or None."""

    def dfs(r, c, i, seen, path):
        if i == len(word):
            return path
        for dr, dc in DIRS8:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in seen and G[nr][nc] == word[i]:
                result = dfs(nr, nc, i + 1, seen | {(nr, nc)}, path + [(nr, nc)])
                if result:
                    return result
        return None

    for r in range(H):
        for c in range(W):
            if G[r][c] == word[0]:
                result = dfs(r, c, 1, frozenset({(r, c)}), [(r, c)])
                if result:
                    return result
    return None


def report_all_elements():
    print("=" * 72)
    print("Periodic table element search — checking all standard names")
    print("=" * 72)
    found_straight = []
    found_king_only = []
    for z, name in ELEMENTS.items():
        straight = find_straight(name)
        if straight:
            found_straight.append((z, name, straight))
            r, c, dr, dc = straight[0]
            path = [(r + i * dr, c + i * dc) for i in range(len(name))]
            print(f"  ★ STRAIGHT  Z={z:<3d} {name!r:15s} at ({r+1},{c+1})→{DIR_NAMES[(dr, dc)]}  cells={path[:4]}...")
        elif count_king_paths(name, stop_at=1) > 0:
            found_king_only.append((z, name))
            k = count_king_paths(name)
            print(f"    king-only Z={z:<3d} {name!r:15s} ({k} king-path(s), no straight)")

    print(f"\n  {'Elements found STRAIGHT:':<30} {len(found_straight)}")
    print(f"  {'Elements found only king:':<30} {len(found_king_only)}")
    return found_straight, found_king_only


def report_symbols_too():
    """Check if 1- or 2-letter element symbols are placed in specific cells."""
    print("\n" + "=" * 72)
    print("Element symbols as grid cells / pairs")
    print("=" * 72)
    SYMBOLS = {
        1: "h", 2: "he", 3: "li", 4: "be", 5: "b", 6: "c", 7: "n", 8: "o",
        9: "f", 10: "ne", 11: "na", 12: "mg", 13: "al", 14: "si",
        15: "p", 16: "s", 17: "cl", 18: "ar", 19: "k", 20: "ca",
        21: "sc", 22: "ti", 23: "v", 24: "cr", 25: "mn", 26: "fe",
        27: "co", 28: "ni", 29: "cu", 30: "zn", 31: "ga", 32: "ge",
        33: "as", 34: "se", 35: "br", 36: "kr", 37: "rb", 38: "sr",
        39: "y", 40: "zr", 41: "nb", 42: "mo", 43: "tc", 44: "ru",
        45: "rh", 46: "pd", 47: "ag", 48: "cd", 49: "in", 50: "sn",
        53: "i", 54: "xe", 55: "cs", 56: "ba", 79: "au", 80: "hg",
        81: "tl", 82: "pb", 83: "bi", 92: "u",
    }
    flat = "".join("".join(r) for r in G).replace("-", "")
    counts = {}
    for z, sym in SYMBOLS.items():
        if len(sym) == 1:
            c = flat.count(sym)
        else:
            # find as king-path or substring in any line
            c = count_king_paths(sym)
        counts[z] = (sym, c)
    # Print only interesting ones
    print(f"  {'Z':>3}  {'sym':<4}  {'count':>5}")
    for z, (sym, c) in sorted(counts.items()):
        print(f"  {z:>3}  {sym:<4}  {c:>5}")


def full_atomic_number_sum():
    """Sum of atomic numbers for all element names found as straight-line placements."""
    print("\n" + "=" * 72)
    print("Potential ANSWER derivations")
    print("=" * 72)
    found_straight, found_king_only = [], []
    for z, name in ELEMENTS.items():
        if find_straight(name):
            found_straight.append(z)
        elif count_king_paths(name, stop_at=1) > 0:
            found_king_only.append(z)

    print(f"  Elements found STRAIGHT-LINE: {found_straight}")
    print(f"    sum  of atomic #s: {sum(found_straight)}")
    print(f"    product: {eval('*'.join(str(x) for x in found_straight)) if found_straight else '-'}")
    print(f"    count: {len(found_straight)}")
    print(f"    concat: {''.join(str(z) for z in found_straight)}")

    print(f"\n  Elements found king-path only: {found_king_only}")
    print(f"    sum: {sum(found_king_only)}")
    print(f"    count: {len(found_king_only)}")

    union = sorted(set(found_straight) | set(found_king_only))
    print(f"\n  Union (any direction): {union}")
    print(f"    sum: {sum(union)}")


if __name__ == "__main__":
    report_all_elements()
    report_symbols_too()
    full_atomic_number_sum()
