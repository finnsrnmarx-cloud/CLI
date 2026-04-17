"""Phase 2 — axiom verification and search for further instruction phrases.

Input: the five known axioms plus starting cells.
Output: findings/PHASE2_AXIOMS.md
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from grid_utils import (  # noqa: E402
    COLS, ROWS, cell, king_paths, load, reading_order_cells,
)

FINDINGS = Path(__file__).parent.parent / "findings"

AXIOMS: dict[str, tuple[int, int]] = {
    "FINDTHESTART":         (1, 5),
    "ADDTHEHEXADECIMALS":   (2, 8),
    "STEPBYSIX":            (9, 14),
    "THEREISADATEONWIRE":   (3, 3),
    "LASTENTRYENTIREINTEGER": (10, 2),
}

CANDIDATE_PHRASES = [
    "FINDTHEEND", "ENDATTHE", "STARTATTHE", "READTHEGRID",
    "COUNTTHE", "MULTIPLYTHE", "SUMTHE", "TAKETHE",
    "DIGTHE", "DIGITOUT", "DIGFOR", "LOOKFOR",
    "BASETEN", "BASESIX", "BASESIXTEEN",
    "IGNORETHE", "SKIPTHE", "REMOVETHE",
    "TWOTHOUSANDTWENTYSIX", "YEARTWOTHOUSAND", "DIGIT", "DIGITS",
    "FINDTHEINTEGER", "ADDTHEDIGITS", "ENTIREINTEGER",
]


def monotonicity_score(path):
    """Lower = fewer direction reversals = more canonical-looking."""
    if len(path) < 3:
        return 0
    reversals = 0
    prev_d = None
    for (r1, c1), (r2, c2) in zip(path, path[1:]):
        d = (r2 - r1, c2 - c1)
        if prev_d is not None and d != prev_d:
            reversals += 1
        prev_d = d
    return reversals


def canonical_path(grid, word, start):
    paths = [p for p in king_paths(grid, word) if p[0] == start]
    if not paths:
        return None, []
    paths.sort(key=monotonicity_score)
    return paths[0], paths


def main() -> None:
    grid = load()
    lines = ["# Phase 2 — axiom verification\n"]

    axiom_paths = {}
    used_cells: set[tuple[int, int]] = set()
    for phrase, start in AXIOMS.items():
        canonical, all_paths = canonical_path(grid, phrase, start)
        lines.append(f"## {phrase}  starts at {start}")
        lines.append(f"  total king-paths from this start: {len(all_paths)}")
        if canonical is None:
            lines.append(f"  **NO PATH FOUND** — check grid or start.")
        else:
            lines.append(f"  canonical path: {canonical}")
            axiom_paths[phrase] = canonical
            used_cells.update(canonical)
        lines.append("")

    lines.append("## Residual cells (in reading order) — unused by any axiom\n")
    residual = []
    for r, c in reading_order_cells():
        if (r, c) not in used_cells:
            ch = cell(grid, r, c)
            residual.append((r, c, ch))
    lines.append(f"Count: {len(residual)}")
    residual_str = "".join(ch for _, _, ch in residual)
    lines.append(f"As a single string: {residual_str}\n")

    lines.append("## Search for additional instruction phrases\n")
    for phrase in CANDIDATE_PHRASES:
        paths = king_paths(grid, phrase, max_paths=5)
        if paths:
            lines.append(f"- **{phrase}** — {len(paths)} king-path(s); first: {paths[0]}")
    lines.append("")

    (FINDINGS / "PHASE2_AXIOMS.md").write_text("\n".join(lines))
    print("Phase 2 complete → findings/PHASE2_AXIOMS.md")


if __name__ == "__main__":
    main()
