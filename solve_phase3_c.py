"""Phase 3c — Visualize axiom path shapes.

Draw each axiom king-path on the grid to check for visual patterns.
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


def find_first_path(word):
    def dfs(r, c, i, seen, path):
        if i == len(word):
            return path
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in seen and G[nr][nc] == word[i]:
                res = dfs(nr, nc, i + 1, seen | {(nr, nc)}, path + [(nr, nc)])
                if res:
                    return res
        return None
    for r in range(H):
        for c in range(W):
            if G[r][c] == word[0]:
                res = dfs(r, c, 1, frozenset({(r, c)}), [(r, c)])
                if res:
                    return res
    return None


AXIOMS = ["findthestart", "addthehexadecimals", "stepbysix",
          "thereisadateonwire", "lastentryentireinteger"]

# Draw all 5 paths on a single grid — use different markers per axiom
marker = {"findthestart": "F", "addthehexadecimals": "A",
          "stepbysix": "S", "thereisadateonwire": "D",
          "lastentryentireinteger": "L"}

display = [[". " for _ in range(W)] for _ in range(H)]
# overlay: if a cell is in multiple paths, mark with *
path_hits = [[[] for _ in range(W)] for _ in range(H)]
for ax in AXIOMS:
    p = find_first_path(ax)
    for r, c in p:
        path_hits[r][c].append(marker[ax])

for r in range(H):
    for c in range(W):
        if G[r][c] == "-":
            display[r][c] = "- "
        elif len(path_hits[r][c]) == 0:
            display[r][c] = ". "
        elif len(path_hits[r][c]) == 1:
            display[r][c] = path_hits[r][c][0] + " "
        else:
            display[r][c] = "* "

print("All 5 axiom paths overlaid:")
print("F=findthestart  A=addthehex  S=stepbysix  D=dateonwire  L=lastentry")
print("* = multi-axiom cell    . = uncovered\n")
for r in range(H):
    print("  " + "".join(display[r]))

# Count cells by category
counts = {"F": 0, "A": 0, "S": 0, "D": 0, "L": 0, "*": 0, ".": 0, "-": 0}
for r in range(H):
    for c in range(W):
        counts[display[r][c][0]] += 1
print(f"\nCounts: {counts}")

# Statistics: axiom 1-only cells, axiom 2-only, etc.
print(f"\nCells unique to each axiom:")
single_cells = {ax: 0 for ax in AXIOMS}
for r in range(H):
    for c in range(W):
        hits = path_hits[r][c]
        if len(hits) == 1:
            # map back from marker to axiom
            for ax, m in marker.items():
                if m == hits[0]:
                    single_cells[ax] += 1
for ax in AXIOMS:
    print(f"  {ax:30s}  {single_cells[ax]} cells")

# Highlight the LAST cell of LASTENTRYENTIREINTEGER
print("\n" + "=" * 60)
print("The 167-target cell: LAST cell of LASTENTRYENTIREINTEGER")
print("=" * 60)
last = find_first_path("lastentryentireinteger")[-1]
print(f"  Cell: ({last[0]+1}, {last[1]+1}) = '{G[last[0]][last[1]]}'")
print(f"  Flat position (1-based): 167")

# Trace which axioms pass through that cell
cells_overlap = path_hits[last[0]][last[1]]
print(f"  Other axioms touching this cell: {cells_overlap}")
