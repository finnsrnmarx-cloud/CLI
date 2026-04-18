"""Chunk 3 — Long/meaningful modern English words as king-paths.

Filters aggressively for common modern English. Groups by length.
"""
from __future__ import annotations
import sys
from english_words import get_english_words_set

ALL_ENG = get_english_words_set(["web2"], lower=True)

# Filter for common-looking modern English
# Reject archaic/scientific/obscure affixes
ARCHAIC_ENDINGS = ("ine", "ite", "oid", "ism", "ium", "ose", "ase",
                   "olic", "ish", "ist", "ial", "orial", "arian")
ARCHAIC_PREFIXES = ("inter", "intra", "semi", "pre", "ecto",
                    "hyper", "hypo", "anti", "dia", "poly")

def looks_modern(w):
    if len(w) < 6 or len(w) > 12: return False
    if not w.isalpha(): return False
    # Basic heuristics for common English
    if w.endswith(ARCHAIC_ENDINGS):
        # Allow some common ones
        if w in {"define", "divine", "machine", "routine", "favorite",
                 "dynamite", "satellite", "site", "spite",
                 "stationary", "sensational", "emotional", "national",
                 "tradition", "mission", "passion", "session"}:
            pass
        else:
            return False
    # Exclude most proper-noun-looking things
    if w.endswith("ian") or w.endswith("ese"): return False
    if w.endswith("ology") or w.endswith("ography"): return False
    return True

ENG = {w for w in ALL_ENG if looks_modern(w)}

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
        if ch == "-" or ch not in node: return
        nxt = node[ch]
        if TERMINAL in nxt:
            found.add(nxt[TERMINAL])
        for dr, dc in DIRS:
            nr, nc = r+dr, c+dc
            if 0<=nr<H and 0<=nc<W and (nr,nc) not in seen:
                dfs(nr, nc, nxt, seen | {(nr, nc)})
    for r in range(H):
        for c in range(W):
            if G[r][c] != "-":
                dfs(r, c, TRIE, frozenset({(r, c)}))
    return found

sys.setrecursionlimit(20000)
words = search()

by_len = {}
for w in words:
    by_len.setdefault(len(w), []).append(w)

print(f"Total modern words (6-12 chars): {len(words)}\n")
for L in sorted(by_len.keys(), reverse=True):
    ws = sorted(by_len[L])
    print(f"--- Length {L} ({len(ws)} words) ---")
    for w in ws:
        print(f"  {w}")
    print()
