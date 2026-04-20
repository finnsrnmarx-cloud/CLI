"""Show the spatial organization of each axiom king-path.

For each axiom, display:
  - Starting cell
  - Ending cell
  - Direction of each step (compass)
  - Overall shape (straight, zigzag, diagonal, etc.)
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
DIR_NAME = {(-1,-1):"NW",(-1,0):"N",(-1,1):"NE",(0,-1):"W",(0,1):"E",
            (1,-1):"SW",(1,0):"S",(1,1):"SE"}
ARROW = {(-1,-1):"↖",(-1,0):"↑",(-1,1):"↗",(0,-1):"←",(0,1):"→",
         (1,-1):"↙",(1,0):"↓",(1,1):"↘"}


def find_first(word):
    def dfs(r, c, i, seen, path):
        if i == len(word): return path
        for dr, dc in DIRS:
            nr, nc = r+dr, c+dc
            if 0<=nr<H and 0<=nc<W and (nr,nc) not in seen and G[nr][nc]==word[i]:
                res = dfs(nr, nc, i+1, seen | {(nr, nc)}, path + [(nr, nc)])
                if res: return res
        return None
    for r in range(H):
        for c in range(W):
            if G[r][c]==word[0]:
                res = dfs(r, c, 1, frozenset({(r, c)}), [(r, c)])
                if res: return res
    return None


AXIOMS = [
    ("findthestart", "FIND THE START"),
    ("addthehexadecimals", "ADD THE HEXADECIMALS"),
    ("stepbysix", "STEP BY SIX"),
    ("thereisadateonwire", "THERE IS A DATE ON WIRE"),
    ("lastentryentireinteger", "LAST ENTRY ENTIRE INTEGER"),
]


def analyse_path(path, name):
    print(f"\n{'='*60}")
    print(f"{name}  ({len(path)} cells)")
    print(f"{'='*60}")

    # Directions between consecutive cells
    directions = []
    for i in range(1, len(path)):
        dr = path[i][0] - path[i-1][0]
        dc = path[i][1] - path[i-1][1]
        directions.append((dr, dc))

    # Summary
    start = (path[0][0]+1, path[0][1]+1)
    end = (path[-1][0]+1, path[-1][1]+1)
    print(f"  Start:  ({start[0]:>2},{start[1]:>2}) = '{G[path[0][0]][path[0][1]]}'")
    print(f"  End:    ({end[0]:>2},{end[1]:>2}) = '{G[path[-1][0]][path[-1][1]]}'")

    # Direction frequency
    from collections import Counter
    dir_freq = Counter(directions)
    print(f"  Direction frequency:")
    for (dr, dc), cnt in sorted(dir_freq.items(), key=lambda x: -x[1]):
        print(f"    {DIR_NAME[(dr,dc)]:<3} {ARROW[(dr,dc)]} : {cnt}")

    # Arrow sequence
    arrows = "".join(ARROW[d] for d in directions)
    print(f"  Arrows: {arrows}")

    # Row/col ranges
    rows = [r for r, c in path]
    cols = [c for r, c in path]
    print(f"  Row span: {min(rows)+1}-{max(rows)+1}")
    print(f"  Col span: {min(cols)+1}-{max(cols)+1}")

    # Is it straight-line? (all directions equal)
    unique_dirs = set(directions)
    if len(unique_dirs) == 1:
        print(f"  Shape: STRAIGHT LINE ({DIR_NAME[list(unique_dirs)[0]]})")
    elif len(unique_dirs) == 2:
        print(f"  Shape: ZIGZAG / 2-direction")
    else:
        print(f"  Shape: COMPLEX ({len(unique_dirs)} distinct directions)")

    # Visual on mini-grid (only show cells on path)
    print(f"  Path on grid:")
    cell_to_idx = {cell: i for i, cell in enumerate(path)}
    min_r = max(0, min(rows) - 1)
    max_r = min(H, max(rows) + 2)
    min_c = max(0, min(cols) - 1)
    max_c = min(W, max(cols) + 2)
    for r in range(min_r, max_r):
        row_str = "    "
        for c in range(min_c, max_c):
            if (r, c) in cell_to_idx:
                idx = cell_to_idx[(r, c)]
                if idx == 0:
                    row_str += " S"  # start
                elif idx == len(path) - 1:
                    row_str += " E"  # end
                else:
                    row_str += " " + G[r][c].upper()
            else:
                row_str += " " + G[r][c].lower() if G[r][c] != "-" else " -"
        print(row_str)


for key, name in AXIOMS:
    path = find_first(key)
    analyse_path(path, name)
