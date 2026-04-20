"""Jane Street April 2026 puzzle 'Can U Dig It?' — exploratory solver.

The puzzle presents a 14x14 grid with no instructions beyond a note that the
answer is a positive integer. Title hints at 'digging' and features a
capitalised U. Bottom row visually reads 'twenty-six' but the letters
don't literally spell twenty-six (no 'w' in row 14).

This script probes several hypotheses and reports raw data so a human can
judge which mechanic the puzzle is using. Run:

    pip install english-words
    python3 solve.py
"""

from __future__ import annotations

from collections import Counter
from itertools import chain

from english_words import get_english_words_set

ENGLISH = get_english_words_set(["web2"], lower=True)

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

NUM_BASIC = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
    50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
    100: "hundred", 1000: "thousand",
}


def num_word(n: int) -> str:
    if n in NUM_BASIC:
        return NUM_BASIC[n]
    if n < 100:
        return NUM_BASIC[(n // 10) * 10] + NUM_BASIC[n % 10]
    if n < 1000:
        s = NUM_BASIC[n // 100] + "hundred"
        if n % 100:
            s += num_word(n % 100)
        return s
    raise ValueError(n)


def find_straight(word: str) -> list[tuple[int, int, int, int]]:
    """Return all (r, c, dr, dc) for word as a straight 8-direction placement."""
    results = []
    L = len(word)
    for r in range(H):
        for c in range(W):
            for dr, dc in DIRS8:
                nr, nc = r + (L - 1) * dr, c + (L - 1) * dc
                if not (0 <= nr < H and 0 <= nc < W):
                    continue
                if all(G[r + i * dr][c + i * dc] == word[i] for i in range(L)):
                    results.append((r, c, dr, dc))
    return results


def count_king_paths(word: str, stop_at: int | None = None) -> int:
    """Count king-move no-reuse paths spelling word."""
    count = 0

    def dfs(r: int, c: int, i: int, seen: frozenset[tuple[int, int]]) -> None:
        nonlocal count
        if stop_at is not None and count >= stop_at:
            return
        if i == len(word):
            count += 1
            return
        for dr, dc in DIRS8:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < H and 0 <= nc < W
                and (nr, nc) not in seen
                and G[nr][nc] == word[i]
            ):
                dfs(nr, nc, i + 1, seen | {(nr, nc)})

    for r in range(H):
        for c in range(W):
            if G[r][c] == word[0]:
                dfs(r, c, 1, frozenset({(r, c)}))
                if stop_at is not None and count >= stop_at:
                    return count
    return count


def letter_stats() -> None:
    print("\n=== Letter stats ===")
    flat = "".join("".join(r) for r in G).replace("-", "")
    c = Counter(flat)
    print(f"Total letters: {sum(c.values())}")
    missing = sorted(set("abcdefghijklmnopqrstuvwxyz") - set(c))
    print(f"Missing letters: {missing}  (blocks any number-word containing Q/V/Z)")


def u_positions() -> None:
    us = [(r + 1, c + 1) for r in range(H) for c in range(W) if G[r][c] == "u"]
    print(f"\n=== U positions ({len(us)} total) ===")
    print(f"  (1-indexed): {us}")


def number_words_report() -> None:
    print("\n=== Number words present as king-move paths (no cell reuse) ===")
    present = []
    for n in range(1, 201):
        w = num_word(n)
        if count_king_paths(w, stop_at=1):
            present.append(n)
    print(f"  Numbers 1-200 that trace: {present}")
    print(f"  Single-digit present: {[n for n in present if n < 10]}")
    print(f"  Single-digit missing: {[n for n in range(1, 10) if n not in present]}")

    print("\n=== Number words as STRAIGHT-LINE placements (traditional word search) ===")
    for n in chain(range(1, 30), range(30, 101, 10), [100, 1000]):
        w = num_word(n)
        places = find_straight(w)
        if places:
            print(f"  {n:4d} {w!r:12s}: {len(places)} placements")


def thematic_report() -> None:
    themes = [
        "tune", "tunes", "tunnel", "dig", "digs", "digit", "digits",
        "dug", "date", "wire", "hex", "find", "start", "end", "add",
        "last", "integer", "answer", "sum", "count", "total", "mine",
        "earth", "bury", "hole", "pit", "path", "can", "you",
        "alan", "moore", "score",
    ]
    print("\n=== Thematic-word king-path counts ===")
    for w in themes:
        c = count_king_paths(w)
        if c:
            sp = find_straight(w)
            print(f"  {w!r:10s}: {c} king-paths, {len(sp)} straight")


def english_residual(min_len: int = 4) -> None:
    """Greedy longest-first cover, then report residual letters."""
    found: dict[str, list[tuple[tuple[int, int], ...]]] = {}
    for r in range(H):
        for c in range(W):
            for dr, dc in DIRS8:
                letters, cells = [], []
                rr, cc = r, c
                while 0 <= rr < H and 0 <= cc < W and G[rr][cc] != "-":
                    letters.append(G[rr][cc])
                    cells.append((rr, cc))
                    rr += dr
                    cc += dc
                for L in range(min_len, len(letters) + 1):
                    word = "".join(letters[:L])
                    if word in ENGLISH:
                        found.setdefault(word, []).append(tuple(cells[:L]))

    used: set[tuple[int, int]] = set()
    placed: list[tuple[str, tuple]] = []
    for w, pls in sorted(found.items(), key=lambda x: (-len(x[0]), x[0])):
        for pl in pls:
            if not (set(pl) & used):
                used.update(pl)
                placed.append((w, pl))
                break
    remaining = [
        (r, c, G[r][c])
        for r in range(H)
        for c in range(W)
        if (r, c) not in used and G[r][c] != "-"
    ]
    print(f"\n=== Greedy English cover (min_len={min_len}): placed {len(placed)} words ===")
    print(f"  Residual letters ({len(remaining)}): {''.join(ch for _, _, ch in remaining)!r}")


def bottom_row_dive() -> None:
    print("\n=== Bottom row ===")
    row = "".join(G[-1])
    print(f"  raw: {row!r}")
    letters = row.replace("-", "")
    counter = Counter(letters)
    target = "twentysix"
    diff = counter - Counter(target)
    missing = Counter(target) - counter
    print(f"  vs 'twentysix'  extras: {dict(diff)}  deficit: {dict(missing)}")
    print(f"  => bottom row has extra letters T, E, N, S, U (anagram: TUNES)")
    print(f"     and is MISSING a 'w' — so 'twenty' does NOT trace anywhere.")


def candidate_summary() -> None:
    print("\n" + "=" * 60)
    print("CANDIDATE ANSWERS (ranked, not verified)")
    print("=" * 60)
    lines = [
        "  26  : bottom row visually spells 'twenty-six'",
        "  17  : sum of straight-line digit words (ONE+SIX+TEN = 1+6+10)",
        "  60  : product of straight-line digit words (1*6*10)",
        "  21  : sum of king-path single-digit words {1,2,3,6,9}",
        " 324  : product of king-path single-digit words",
        " 339  : sum of all king-path numbers {1,2,3,6,9,10,19,90,99,100}",
        "  10  : count of distinct king-path numbers <= 100",
        "   7  : count of U's in the grid",
    ]
    for l in lines:
        print(l)
    print("\n  None of these is verified. Jane Street publishes the official")
    print("  solution in early May 2026 — that's the only way to be sure.")


if __name__ == "__main__":
    print("Grid:")
    for r in G:
        print("  " + " ".join(r))
    letter_stats()
    u_positions()
    bottom_row_dive()
    number_words_report()
    thematic_report()
    english_residual(min_len=4)
    candidate_summary()
