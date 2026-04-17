"""Reusable grid primitives.

All coordinates are 1-indexed in public APIs (matches the plan's phrasing,
e.g. "hyphen at (14, 8)"). Internally we convert to 0-indexed arrays.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable, Iterator

sys.path.insert(0, str(Path(__file__).parent.parent / "data"))
from grid import HYPHEN, ROWS, COLS, load_grid  # noqa: E402

# 8-connected king moves (row_delta, col_delta)
KING_DELTAS: tuple[tuple[int, int], ...] = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
)

# 8 straight directions, labelled
STRAIGHT_DIRS: dict[str, tuple[int, int]] = {
    "E":  (0, 1),
    "W":  (0, -1),
    "S":  (1, 0),
    "N":  (-1, 0),
    "SE": (1, 1),
    "SW": (1, -1),
    "NE": (-1, 1),
    "NW": (-1, -1),
}


def in_bounds(r: int, c: int) -> bool:
    """1-indexed bounds check."""
    return 1 <= r <= ROWS and 1 <= c <= COLS


def cell(grid: list[list[str]], r: int, c: int) -> str:
    """1-indexed getter."""
    return grid[r - 1][c - 1]


def cell_neighbors(r: int, c: int) -> list[tuple[int, int]]:
    """King neighbors of (r, c), 1-indexed, in-bounds."""
    out = []
    for dr, dc in KING_DELTAS:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc):
            out.append((nr, nc))
    return out


def reading_order_cells(include_hyphen: bool = True) -> list[tuple[int, int]]:
    """Row-major (r, c) order for all 196 cells."""
    return [(r, c) for r in range(1, ROWS + 1) for c in range(1, COLS + 1)]


def straight_line_trace(
    grid: list[list[str]],
    word: str,
    r0: int,
    c0: int,
    dr: int,
    dc: int,
) -> bool:
    """Does `word` appear starting at (r0, c0) in direction (dr, dc)?"""
    w = word.lower()
    for i, ch in enumerate(w):
        r, c = r0 + i * dr, c0 + i * dc
        if not in_bounds(r, c) or cell(grid, r, c) != ch:
            return False
    return True


def find_straight_line_starts(
    grid: list[list[str]], word: str
) -> list[tuple[int, int, str]]:
    """All (start_r, start_c, direction_label) for straight-line hits."""
    hits: list[tuple[int, int, str]] = []
    for r in range(1, ROWS + 1):
        for c in range(1, COLS + 1):
            for label, (dr, dc) in STRAIGHT_DIRS.items():
                if straight_line_trace(grid, word, r, c, dr, dc):
                    hits.append((r, c, label))
    return hits


def king_paths(
    grid: list[list[str]], word: str, max_paths: int = 10_000
) -> list[list[tuple[int, int]]]:
    """Enumerate every king-connected (no-revisit) path spelling `word`."""
    w = word.lower()
    if not w:
        return []
    results: list[list[tuple[int, int]]] = []

    def dfs(path: list[tuple[int, int]]) -> None:
        if len(results) >= max_paths:
            return
        if len(path) == len(w):
            results.append(path.copy())
            return
        r, c = path[-1]
        next_ch = w[len(path)]
        for nr, nc in cell_neighbors(r, c):
            if (nr, nc) in path:
                continue
            if cell(grid, nr, nc) != next_ch:
                continue
            path.append((nr, nc))
            dfs(path)
            path.pop()

    for r in range(1, ROWS + 1):
        for c in range(1, COLS + 1):
            if cell(grid, r, c) == w[0]:
                dfs([(r, c)])
                if len(results) >= max_paths:
                    return results
    return results


def king_path_exists(grid: list[list[str]], word: str) -> bool:
    return bool(king_paths(grid, word, max_paths=1))


def subsequence_in_line(word: str, line: str) -> list[list[int]]:
    """All sets of column indices (0-based into `line`) where `word`
    appears as a subsequence. Returns list of index-lists."""
    w = word.lower()
    line = line.lower()
    results: list[list[int]] = []

    def dfs(wi: int, start: int, picks: list[int]) -> None:
        if wi == len(w):
            results.append(picks.copy())
            return
        for j in range(start, len(line)):
            if line[j] == w[wi]:
                picks.append(j)
                dfs(wi + 1, j + 1, picks)
                picks.pop()

    dfs(0, 0, [])
    return results


def row_string(grid: list[list[str]], r: int) -> str:
    return "".join(grid[r - 1])


def col_string(grid: list[list[str]], c: int) -> str:
    return "".join(grid[r - 1][c - 1] for r in range(1, ROWS + 1))


def diagonal_strings(grid: list[list[str]]) -> dict[str, str]:
    """All 8 diagonals (main + anti, both directions across offsets)."""
    out: dict[str, str] = {}
    # NE-SW and NW-SE diagonals by starting offset
    for offset in range(-(ROWS - 1), COLS):
        nw_se = []
        for i in range(max(0, -offset), min(ROWS, COLS - offset)):
            r = i + 1
            c = i + offset + 1
            if in_bounds(r, c):
                nw_se.append(grid[r - 1][c - 1])
        if nw_se:
            out[f"NW-SE@{offset}"] = "".join(nw_se)
    for offset in range(0, ROWS + COLS - 1):
        ne_sw = []
        for i in range(ROWS):
            r = i + 1
            c = offset - i + 1
            if in_bounds(r, c):
                ne_sw.append(grid[r - 1][c - 1])
        if ne_sw:
            out[f"NE-SW@{offset}"] = "".join(ne_sw)
    return out


def alphabet_pos(ch: str) -> int | None:
    """a->1, b->2, ..., z->26. Non-letter -> None."""
    ch = ch.lower()
    if "a" <= ch <= "z":
        return ord(ch) - ord("a") + 1
    return None


def hex_value(ch: str) -> int | None:
    """Hex digit value for a-f. Non-hex -> None."""
    ch = ch.lower()
    if ch in "abcdef":
        return int(ch, 16)
    return None


def flatten(grid: list[list[str]], include_hyphen: bool = True) -> str:
    cells = []
    for r in range(ROWS):
        for c in range(COLS):
            ch = grid[r][c]
            if ch == HYPHEN and not include_hyphen:
                continue
            cells.append(ch)
    return "".join(cells)


def load() -> list[list[str]]:
    return load_grid()


if __name__ == "__main__":
    g = load()
    print(f"Loaded {ROWS}x{COLS} grid")
    print("Row strings:")
    for r in range(1, ROWS + 1):
        print(f"  {r:2d}: {row_string(g, r)}")
