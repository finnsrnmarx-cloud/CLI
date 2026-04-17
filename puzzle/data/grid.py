"""Grid loader. Reads data/grid.txt into a 14x14 list-of-lists.

A filled cell is a single lowercase letter. The hyphen `-` represents the
non-letter cell (expected at row 14 col 8, i.e. index [13][7]). `#` marks
unfilled placeholder cells — if any remain at solve time, the loader
raises so we never silently analyze the skeleton.
"""

from __future__ import annotations

from pathlib import Path

GRID_TXT = Path(__file__).parent / "grid.txt"
ROWS = 14
COLS = 14
HYPHEN = "-"
PLACEHOLDER = "#"


def load_grid() -> list[list[str]]:
    text = GRID_TXT.read_text().rstrip("\n")
    lines = text.split("\n")
    if len(lines) != ROWS:
        raise ValueError(f"expected {ROWS} rows, got {len(lines)}")
    grid: list[list[str]] = []
    for r, line in enumerate(lines, start=1):
        if len(line) != COLS:
            raise ValueError(f"row {r}: expected {COLS} cols, got {len(line)}")
        grid.append(list(line))
    return grid


def assert_filled(grid: list[list[str]]) -> None:
    unfilled = [
        (r + 1, c + 1)
        for r, row in enumerate(grid)
        for c, ch in enumerate(row)
        if ch == PLACEHOLDER
    ]
    if unfilled:
        raise RuntimeError(
            f"grid.txt still has {len(unfilled)} placeholder cells "
            f"(first at {unfilled[0]}); paste real letters before solving"
        )


if __name__ == "__main__":
    g = load_grid()
    try:
        assert_filled(g)
    except RuntimeError as e:
        print(f"WARN: {e}")
    print(f"Loaded grid: {ROWS}x{COLS}")
    for row in g:
        print("".join(row))
