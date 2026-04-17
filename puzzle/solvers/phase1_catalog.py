"""Phase 1 — exhaustive grid cataloguing.

Emits:
  findings/letter_positions.json
  findings/hyphen_neighborhood.md
  findings/hex_digit_map.md
  findings/straight_line_words.csv
  findings/king_path_words.csv
  findings/diagonals.md
  findings/spirals_border.md
  findings/columns.md

No conclusions, just data.

Requires a dictionary at /usr/share/dict/words or DICT env var. Falls back
to a tiny builtin list (unsuitable for real runs) if not found.
"""

from __future__ import annotations

import csv
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from grid_utils import (  # noqa: E402
    COLS, ROWS, STRAIGHT_DIRS, HYPHEN, alphabet_pos, cell, cell_neighbors,
    col_string, diagonal_strings, find_straight_line_starts, hex_value,
    king_path_exists, load, reading_order_cells, row_string,
)

ROOT = Path(__file__).parent.parent
FINDINGS = ROOT / "findings"
FINDINGS.mkdir(exist_ok=True)

FALLBACK_WORDS = [
    "find", "start", "hexadecimal", "step", "date", "wire", "last",
    "entry", "integer", "digit", "aluminum", "tin", "dig", "the", "is",
    "there", "entire", "add", "six", "can", "you",
]


def load_words(min_len: int = 4) -> list[str]:
    path = os.environ.get("DICT", "/usr/share/dict/words")
    if Path(path).exists():
        words = []
        for line in Path(path).read_text().splitlines():
            w = line.strip().lower()
            if len(w) >= min_len and w.isalpha():
                words.append(w)
        return sorted(set(words))
    return [w for w in FALLBACK_WORDS if len(w) >= min_len]


def letter_positions(grid):
    out: dict[str, list[list[int]]] = defaultdict(list)
    for r, c in reading_order_cells():
        ch = cell(grid, r, c)
        out[ch].append([r, c])
    return dict(sorted(out.items()))


def hyphen_report(grid) -> str:
    lines = ["# Hyphen analysis\n"]
    found = [(r, c) for r, c in reading_order_cells() if cell(grid, r, c) == HYPHEN]
    lines.append(f"Hyphen cells: {found}\n")
    for r, c in found:
        lines.append(f"## ({r}, {c})\n")
        neigh = []
        for nr, nc in cell_neighbors(r, c):
            ch = cell(grid, nr, nc)
            ap = alphabet_pos(ch)
            neigh.append(f"({nr},{nc})={ch!r} alpha={ap}")
        lines.append("Neighbors: " + "; ".join(neigh) + "\n")
        lines.append(
            f"Arithmetic: r+c={r+c}, r*c={r*c}, r^2+c={r*r+c}, "
            f"r*c+r+c={r*c+r+c}\n"
        )
    return "\n".join(lines)


def hex_digit_map(grid) -> str:
    total = 0
    per_row = [0] * ROWS
    per_col = [0] * COLS
    hits = []
    for r, c in reading_order_cells():
        ch = cell(grid, r, c)
        if hex_value(ch) is not None:
            total += 1
            per_row[r - 1] += 1
            per_col[c - 1] += 1
            hits.append((r, c, ch))
    lines = [
        "# Hex-digit cell map",
        f"Total hex cells (a-f): {total}",
        f"Per row: {per_row}",
        f"Per col: {per_col}",
        "",
        "Cells:",
    ]
    for r, c, ch in hits:
        lines.append(f"  ({r:2d},{c:2d}) = {ch}")
    return "\n".join(lines)


def straight_line_scan(grid, words):
    rows = []
    for w in words:
        for r, c, d in find_straight_line_starts(grid, w):
            rows.append((len(w), w, r, c, d))
    rows.sort(reverse=True)
    return rows


def king_path_scan(grid, words, cap: int = 12):
    rows = []
    for w in words:
        if len(w) > cap:
            continue
        if king_path_exists(grid, w):
            rows.append((len(w), w))
    rows.sort(reverse=True)
    return rows


def diagonals_report(grid) -> str:
    diags = diagonal_strings(grid)
    lines = ["# Diagonals", ""]
    for label, s in diags.items():
        lines.append(f"{label}: {s}  (reversed: {s[::-1]})")
    return "\n".join(lines)


def spiral_cw(grid):
    top, bot, lft, rgt = 0, ROWS - 1, 0, COLS - 1
    out = []
    while top <= bot and lft <= rgt:
        for c in range(lft, rgt + 1):
            out.append(grid[top][c])
        top += 1
        for r in range(top, bot + 1):
            out.append(grid[r][rgt])
        rgt -= 1
        if top <= bot:
            for c in range(rgt, lft - 1, -1):
                out.append(grid[bot][c])
            bot -= 1
        if lft <= rgt:
            for r in range(bot, top - 1, -1):
                out.append(grid[r][lft])
            lft += 1
    return "".join(out)


def border_cw(grid) -> str:
    out = []
    for c in range(COLS):
        out.append(grid[0][c])
    for r in range(1, ROWS):
        out.append(grid[r][COLS - 1])
    for c in range(COLS - 2, -1, -1):
        out.append(grid[ROWS - 1][c])
    for r in range(ROWS - 2, 0, -1):
        out.append(grid[r][0])
    return "".join(out)


def columns_report(grid) -> str:
    lines = ["# Columns (top-to-bottom)", ""]
    for c in range(1, COLS + 1):
        lines.append(f"c{c:2d}: {col_string(grid, c)}")
    lines.append("\n# Columns (bottom-to-top)\n")
    for c in range(1, COLS + 1):
        lines.append(f"c{c:2d}: {col_string(grid, c)[::-1]}")
    return "\n".join(lines)


def main() -> None:
    grid = load()
    words = load_words(min_len=4)
    print(f"Loaded {len(words)} dictionary words")

    (FINDINGS / "letter_positions.json").write_text(
        json.dumps(letter_positions(grid), indent=2)
    )
    (FINDINGS / "hyphen_neighborhood.md").write_text(hyphen_report(grid))
    (FINDINGS / "hex_digit_map.md").write_text(hex_digit_map(grid))

    sl_rows = straight_line_scan(grid, words)
    with (FINDINGS / "straight_line_words.csv").open("w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["length", "word", "row", "col", "direction"])
        wr.writerows(sl_rows)

    kp_rows = king_path_scan(grid, [w for w in words if len(w) >= 5])
    with (FINDINGS / "king_path_words.csv").open("w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["length", "word"])
        wr.writerows(kp_rows)

    (FINDINGS / "diagonals.md").write_text(diagonals_report(grid))
    (FINDINGS / "spirals_border.md").write_text(
        "# Spirals and border\n\n"
        f"CW spiral:  {spiral_cw(grid)}\n"
        f"CCW spiral: {spiral_cw(grid)[::-1]}\n"
        f"Border CW:  {border_cw(grid)}\n"
        f"Border CCW: {border_cw(grid)[::-1]}\n"
    )
    (FINDINGS / "columns.md").write_text(columns_report(grid))
    print("Phase 1 complete → findings/")


if __name__ == "__main__":
    main()
