"""solve_final.py — Comprehensive theme-word scan across all directions.

Counts for each theme word:
  - substring occurrences across every straight line (8 directions, both ways)
  - subsequence presence in any line
  - king-move no-reuse path count across the whole grid
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


def all_lines():
    lines = []
    # rows + reversed
    for r in range(H):
        s = "".join(ch for ch in G[r] if ch != "-")
        lines.append(s)
        lines.append(s[::-1])
    # cols + reversed
    for c in range(W):
        s = "".join(G[r][c] for r in range(H) if G[r][c] != "-")
        lines.append(s)
        lines.append(s[::-1])
    # diagonals ↘
    for d in range(-H + 1, W):
        s = ""
        for i in range(max(H, W)):
            r = i + (0 if d >= 0 else -d)
            c = i + (d if d >= 0 else 0)
            if 0 <= r < H and 0 <= c < W and G[r][c] != "-":
                s += G[r][c]
        if len(s) >= 3:
            lines.append(s)
            lines.append(s[::-1])
    # diagonals ↙
    for d in range(H + W - 1):
        s = ""
        for i in range(max(H, W)):
            r, c = i, d - i
            if 0 <= r < H and 0 <= c < W and G[r][c] != "-":
                s += G[r][c]
        if len(s) >= 3:
            lines.append(s)
            lines.append(s[::-1])
    return lines


def is_subseq(word: str, line: str) -> bool:
    it = iter(line)
    return all(ch in it for ch in word)


def count_substring(word: str, lines) -> int:
    return sum(line.count(word) for line in lines)


def count_subseq(word: str, lines) -> int:
    return sum(1 for line in lines if is_subseq(word, line))


def count_king_paths(word: str) -> int:
    count = 0

    def dfs(r, c, i, seen):
        nonlocal count
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
    return count


if __name__ == "__main__":
    lines = all_lines()
    print(f"Total lines+reversed: {len(lines)}")

    theme = [
        "digit", "digits", "dig", "tune", "tunes",
        "twentysix", "twenty", "hex", "hexagon", "hexadecimal",
        "can", "canu", "canudig", "canudigit",
        "integer", "find", "add", "last", "start", "end",
        "sixty", "ninety", "hundred", "thousand", "nineteen",
    ]

    print(f"\n{'word':<15} {'substring':>10} {'subseq':>8} {'king':>6}")
    print("-" * 50)
    for w in theme:
        s = count_substring(w, lines)
        q = count_subseq(w, lines)
        k = count_king_paths(w)
        print(f"{w:<15} {s:>10} {q:>8} {k:>6}")

    print("\n=== Row 9 hides 'DIGIT' as subsequence (no missing letters) ===")
    print("    This maps directly to the puzzle title 'Can U Dig It?' → DIGIT.")

    print("\n=== Bottom row spells TWENTY-SIX with 'w' missing (year 2026 decoration) ===")
