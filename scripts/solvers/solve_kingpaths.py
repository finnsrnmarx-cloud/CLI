"""solve_v4.py — Trie-pruned king-path English word search.

Build a prefix trie from the English dictionary, then DFS on the grid
only following paths whose chars form a valid prefix. Prints all
traceable English words >= min_len, sorted by length.
"""

from __future__ import annotations

import sys

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

# Build trie
TERMINAL = "$"


def build_trie(words, min_len=3, max_len=12):
    trie: dict = {}
    for w in words:
        if len(w) < min_len or len(w) > max_len or "-" in w or "'" in w:
            continue
        node = trie
        for ch in w:
            node = node.setdefault(ch, {})
        node[TERMINAL] = w
    return trie


MIN_LEN = 6
MAX_LEN = 12
TRIE = build_trie(ENGLISH, MIN_LEN, MAX_LEN)


def search() -> set[str]:
    found: set[str] = set()

    def dfs(r: int, c: int, node: dict, seen: frozenset):
        ch = G[r][c]
        if ch not in node:
            return
        next_node = node[ch]
        if TERMINAL in next_node:
            found.add(next_node[TERMINAL])
        for dr, dc in DIRS8:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < H and 0 <= nc < W
                and (nr, nc) not in seen
                and G[nr][nc] != "-"
            ):
                dfs(nr, nc, next_node, seen | {(nr, nc)})

    for r in range(H):
        for c in range(W):
            if G[r][c] != "-":
                dfs(r, c, TRIE, frozenset({(r, c)}))
    return found


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    words = sorted(search(), key=lambda w: (-len(w), w))
    print(f"Found {len(words)} distinct English words of length {MIN_LEN}..{MAX_LEN} as king paths:\n")
    for w in words:
        print(f"  {len(w):2d}  {w}")
