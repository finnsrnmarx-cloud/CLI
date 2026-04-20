"""Phase 4a — Exhaustive king-path word search with length-weighted significance.

Find every English word (length >= 5) traceable as a king-path. Group by
length to evaluate by meaningfulness:
  >= 9 letters : almost certainly intentional
  7-8 letters  : very strong signal
  6 letters    : moderate signal
  5 letters    : weak (incidental in dense grid)

Ignore words below 5 chars entirely (too noisy).
"""

from __future__ import annotations
import sys
from english_words import get_english_words_set

ENG = get_english_words_set(["web2"], lower=True)
ENG = {w for w in ENG if w.isalpha() and 5 <= len(w) <= 15}

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

TERMINAL = "$"


def build_trie(words):
    trie = {}
    for w in words:
        node = trie
        for ch in w:
            node = node.setdefault(ch, {})
        node[TERMINAL] = w
    return trie


TRIE = build_trie(ENG)


def search():
    found = set()

    def dfs(r, c, node, seen):
        ch = G[r][c]
        if ch == "-" or ch not in node:
            return
        nxt = node[ch]
        if TERMINAL in nxt:
            found.add(nxt[TERMINAL])
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in seen:
                dfs(nr, nc, nxt, seen | {(nr, nc)})

    for r in range(H):
        for c in range(W):
            if G[r][c] != "-":
                dfs(r, c, TRIE, frozenset({(r, c)}))
    return found


sys.setrecursionlimit(20000)
words = search()

# Group by length
by_len = {}
for w in words:
    by_len.setdefault(len(w), []).append(w)

print(f"Total distinct king-path English words (5-15 chars): {len(words)}\n")
for L in sorted(by_len.keys(), reverse=True):
    ws = sorted(by_len[L])
    print(f"--- Length {L} ({len(ws)} words) ---")
    for w in ws:
        print(f"  {w}")
    print()
