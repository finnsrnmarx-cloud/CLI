"""solve_snake.py — Combined-mechanic exploration.

Tests the following ideas end-to-end:

  A. Find each of the 5 axiom phrases as king-paths.
  B. Concatenate those paths (in several orderings).
  C. Step by 6 along the combined path and collect HEX digits (a-f → 10-15).
  D. Sum the hex values. Optionally add the 'bottom-row year' 2026 as the
     'LAST ENTRY ENTIRE INTEGER'.
  E. Also try PWEI track-6 interactions (multiply/add 6).
  F. Compute element atomic-number hex encodings.

All candidate integers are printed at the bottom.
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
DIRS = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]

HEX_DIGITS = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}


def find_all_king_paths(word: str, max_paths=200):
    results = []

    def dfs(r, c, i, seen, path):
        if len(results) >= max_paths:
            return
        if i == len(word):
            results.append(path.copy())
            return
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in seen and G[nr][nc] == word[i]:
                path.append((nr, nc))
                seen.add((nr, nc))
                dfs(nr, nc, i + 1, seen, path)
                seen.remove((nr, nc))
                path.pop()

    for r in range(H):
        for c in range(W):
            if G[r][c] == word[0]:
                dfs(r, c, 1, {(r, c)}, [(r, c)])
    return results


def find_first(word: str):
    paths = find_all_king_paths(word, max_paths=1)
    return paths[0] if paths else None


AXIOMS = [
    "findthestart",
    "addthehexadecimals",
    "stepbysix",
    "thereisadateonwire",
    "lastentryentireinteger",
]


# ----------------------------------------------------------------------
def path_letters(path):
    return "".join(G[r][c] for r, c in path)


def hex_sum_at_step(path: list, step: int = 6, start_offset: int = 0) -> tuple[int, str]:
    """Walk along path taking every `step`-th cell, sum hex values."""
    letters = []
    total = 0
    for i in range(start_offset, len(path), step):
        r, c = path[i]
        ch = G[r][c]
        letters.append(ch)
        if ch in HEX_DIGITS:
            total += HEX_DIGITS[ch]
    return total, "".join(letters)


def hex_sum_all(path: list) -> int:
    total = 0
    for r, c in path:
        ch = G[r][c]
        if ch in HEX_DIGITS:
            total += HEX_DIGITS[ch]
    return total


def as_hex_number(s: str) -> int | None:
    """If s is all hex digits, return its value. Else None."""
    try:
        return int(s, 16)
    except ValueError:
        return None


# ----------------------------------------------------------------------
def run():
    print("=" * 70)
    print("AXIOM PATHS — individual hex analysis")
    print("=" * 70)

    axiom_paths = {}
    for ax in AXIOMS:
        p = find_first(ax)
        if not p:
            print(f"  MISSING: {ax}")
            continue
        axiom_paths[ax] = p
        letters = path_letters(p)
        hs = hex_sum_all(p)
        hs6, sixletters = hex_sum_at_step(p, 6)
        hs6_1, sixletters1 = hex_sum_at_step(p, 6, start_offset=1)
        hex_only = "".join(ch for ch in letters if ch in HEX_DIGITS)
        hex_num = as_hex_number(hex_only) if hex_only else None
        print(f"\n  {ax}  ({len(p)} cells)")
        print(f"    letters:        {letters!r}")
        print(f"    hex digits only:{hex_only!r}  -> as hex value: {hex_num}")
        print(f"    sum(all hex cells in path):  {hs}")
        print(f"    step-6 letters: {sixletters!r}  sum={hs6}")
        print(f"    step-6 off1:    {sixletters1!r}  sum={hs6_1}")

    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("CONCATENATED-PATH (all 5 axioms end-to-end) hex analysis")
    print("=" * 70)
    concat_order = AXIOMS[:]
    concat_path = []
    for ax in concat_order:
        concat_path.extend(axiom_paths.get(ax, []))
    concat_letters = path_letters(concat_path)
    print(f"  Total cells: {len(concat_path)}")
    print(f"  Concat letters: {concat_letters}")
    hex_only = "".join(ch for ch in concat_letters if ch in HEX_DIGITS)
    print(f"  Hex-only letters: {hex_only!r} (length {len(hex_only)})")

    hs = hex_sum_all(concat_path)
    print(f"  Sum of ALL hex cells in concat path: {hs}")
    hs_step6, letters_6 = hex_sum_at_step(concat_path, 6)
    print(f"  Step-by-6 letters: {letters_6!r}  hex sum: {hs_step6}")
    for off in range(1, 6):
        hss, lls = hex_sum_at_step(concat_path, 6, off)
        print(f"  Step-by-6 offset {off}: {lls!r}  hex sum: {hss}")

    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("PLUS 2026 (bottom row as 'LAST ENTRY ENTIRE INTEGER')")
    print("=" * 70)
    print(f"  hex_sum_all + 2026 = {hs + 2026}")
    print(f"  hex_sum_all + 26   = {hs + 26}")
    print(f"  hex_sum_all + 2026 * 6 (PWEI track 6) = {hs + 2026 + 6}")

    # Try each step-6 offset + 2026
    for off in range(6):
        s, _ = hex_sum_at_step(concat_path, 6, off)
        print(f"  step6 off{off} sum + 2026 = {s + 2026}")

    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("STEP-6 over the WHOLE FLAT GRID (Gemini's hypothesis)")
    print("=" * 70)
    flat = "".join("".join(r) for r in G).replace("-", "")
    # Find first 't' of 'start' — start starts with s-t-a-r-t at row 1 cols 11-14
    # The 't' is at (1,14) flat position 14 (1-indexed). Let's try multiple starts.
    t_positions_in_start = []
    for idx, ch in enumerate(flat):
        if ch == "t":
            t_positions_in_start.append(idx)
    print(f"  All 't' positions in flat grid: {t_positions_in_start[:10]}... (total {len(t_positions_in_start)})")

    # Try stepping by 6 from each 't' and summing hex
    for start in t_positions_in_start[:8]:
        letters = [flat[i] for i in range(start, len(flat), 6)]
        hex_vals = [HEX_DIGITS.get(ch, 0) for ch in letters]
        total = sum(hex_vals)
        hex_letters = "".join(ch for ch in letters if ch in HEX_DIGITS)
        print(f"  start flat pos {start:3d} (char {flat[start]!r}): letters visited ({len(letters)}): {''.join(letters)}")
        print(f"      hex-only: {hex_letters}  sum: {total}  sum+2026: {total + 2026}")

    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("ELEMENT-NAME HEX encodings")
    print("=" * 70)
    for name, z in [("aluminum", 13), ("aluminium", 13), ("tin", 50),
                    ("iron", 26), ("neon", 10), ("argon", 18), ("holmium", 67)]:
        hex_only = "".join(ch for ch in name if ch in HEX_DIGITS)
        hex_num = as_hex_number(hex_only) if hex_only else None
        print(f"  {name!r:12s} Z={z:3d}  hex-digits only: {hex_only!r} -> {hex_num}")
    print(f"  Al+Sn = 13+50 = 63")
    print(f"  Al*Sn = 13*50 = 650")
    print(f"  (Al+Sn) + 2026 = 2089")
    print(f"  2026 + 50 + 13 = 2089")
    print(f"  2026 - 50 - 13 = 1963")

    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("PWEI 'Can U Dig It?' track 6 calculations")
    print("=" * 70)
    print(f"  2026 + 6 = 2032")
    print(f"  2026 * 6 = 12156")
    print(f"  2026 / 6 = 337.67 (not int)")
    print(f"  2026 - 6 = 2020")
    print(f"  (hex_sum_all={hs}) * 6 = {hs*6}")
    print(f"  {hs} + 6 = {hs + 6}")


if __name__ == "__main__":
    run()
