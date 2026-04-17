"""Phase 3 — apply the five axioms to the grid itself.

The axioms say: FIND THE START / ADD THE HEXADECIMALS / STEP BY SIX /
THERE IS A DATE ON WIRE / LAST ENTRY ENTIRE INTEGER.

This script runs every reasonable interpretation and records every
candidate integer it produces. Nothing is committed to being the answer.

Output: findings/PHASE3_SELF_CONTAINED.md  and phase3_candidates.csv
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from grid_utils import (  # noqa: E402
    COLS, ROWS, HYPHEN, alphabet_pos, cell, col_string, diagonal_strings,
    flatten, hex_value, load, reading_order_cells, row_string,
)

FINDINGS = Path(__file__).parent.parent / "findings"

REJECTED = {600, 3241, 3242, 26, 22, 7}


def all_hex_cells(grid):
    return [(r, c, cell(grid, r, c))
            for r, c in reading_order_cells()
            if hex_value(cell(grid, r, c)) is not None]


def step_sequence(start_idx: int, step: int, n: int, length: int):
    """Generate up to n indices starting at start_idx by `step`,
    wrapping around modulo length."""
    out = []
    idx = start_idx
    for _ in range(n):
        out.append(idx % length)
        idx += step
    return out


def interpret_as_hex(cells):
    """Filter to hex-digit cells and sum."""
    total = 0
    digits = []
    for ch in cells:
        v = hex_value(ch)
        if v is not None:
            total += v
            digits.append(ch)
    return total, "".join(digits)


def date_on_wire_scan(grid):
    """For each 'wire' (row, col, diagonal), extract hex chars and
    check if they encode a 4-digit year. Return list of hits."""
    hits = []
    lines: list[tuple[str, str]] = []
    for r in range(1, ROWS + 1):
        lines.append((f"row{r}", row_string(grid, r)))
    for c in range(1, COLS + 1):
        lines.append((f"col{c}", col_string(grid, c)))
    for label, s in diagonal_strings(grid).items():
        lines.append((label, s))
    for label, s in lines:
        hex_chars = [ch for ch in s if hex_value(ch) is not None]
        if len(hex_chars) >= 4:
            hex_str = "".join(hex_chars)
            try:
                val = int(hex_str, 16)
            except ValueError:
                continue
            # also try first 4 hex chars as year
            year = int(hex_chars[0] + hex_chars[1] + hex_chars[2] + hex_chars[3], 16)
            hits.append((label, hex_str, val, year))
    return hits


def main() -> None:
    grid = load()
    lines = ["# Phase 3 — self-contained mechanic\n"]
    candidates: list[tuple[str, int, str]] = []  # (method, value, note)

    flat = flatten(grid, include_hyphen=False)
    hex_cells = all_hex_cells(grid)
    lines.append(f"Flat grid length (letters only): {len(flat)}")
    lines.append(f"Hex-digit cells: {len(hex_cells)}\n")

    # 1. Pure hex-only extraction (reading order)
    hex_stream = "".join(ch for _, _, ch in hex_cells)
    lines.append(f"Hex stream (reading order): {hex_stream}")
    sum_all_hex = sum(hex_value(ch) for ch in hex_stream)
    lines.append(f"Sum of all hex cells: {sum_all_hex}")
    candidates.append(("sum_all_hex_cells", sum_all_hex, "ADDTHE over reading-order hex cells"))
    try:
        candidates.append(("hex_stream_as_bigint", int(hex_stream, 16), "whole stream as one hex number"))
    except ValueError:
        pass

    # 2. STEP BY SIX starting from each possible "start"
    flat_full = flatten(grid, include_hyphen=True)
    starts = {
        "cell(1,1)": 0,
        "hyphen":    flat_full.index(HYPHEN) if HYPHEN in flat_full else None,
        "first_hex": next(
            (i for i, ch in enumerate(flat_full) if hex_value(ch) is not None),
            None,
        ),
    }
    for name, start in starts.items():
        if start is None:
            continue
        for step in (6,):
            stepped_idx = step_sequence(start, step, 33, len(flat_full))
            stepped = [flat_full[i] for i in stepped_idx]
            total, pulled = interpret_as_hex(stepped)
            candidates.append((
                f"step6_from_{name}_addhex",
                total,
                f"stepped={''.join(stepped)} hex={pulled}",
            ))
            # LAST ENTRY ENTIRE INTEGER: replace last hex contribution
            if pulled:
                last_entry = stepped[-1]
                if last_entry.isdigit() or hex_value(last_entry) is not None:
                    alt_total = total - (hex_value(last_entry) or 0)
                    # interpret last entry as its position-index instead
                    alt_total += stepped_idx[-1]
                    candidates.append((
                        f"step6_from_{name}_lastentry_is_position",
                        alt_total,
                        "last hex replaced with final cell index",
                    ))

    # 3. DATE ON WIRE — hex reads across each line
    wire_hits = date_on_wire_scan(grid)
    lines.append("\n## DATE ON WIRE (hex extractions per line)")
    for label, hex_str, val, year in wire_hits:
        lines.append(f"  {label}: hex={hex_str} → {val} (first-4 year={year})")
    # if any line has exactly "2026" in hex, flag it
    for label, hex_str, val, year in wire_hits:
        if year == 2026 or hex_str.startswith("7ea"):  # 0x7EA = 2026
            candidates.append((f"wire_year2026_{label}", val, hex_str))

    # 4. Alphabet-sum of residual cells (after removing those in hex_cells)
    nonhex_cells = [cell(grid, r, c)
                    for r, c in reading_order_cells()
                    if hex_value(cell(grid, r, c)) is None
                    and cell(grid, r, c) != HYPHEN]
    nonhex_alpha_sum = sum(alphabet_pos(ch) or 0 for ch in nonhex_cells)
    candidates.append(("nonhex_alpha_sum", nonhex_alpha_sum, "sum of a..z values of non-hex cells"))

    # 5. Sum of alphabet positions of ALL cells
    all_alpha = sum(alphabet_pos(ch) or 0 for ch in flat)
    candidates.append(("all_alpha_sum", all_alpha, "sum of a..z of every letter"))

    # Dedupe / filter rejected
    lines.append("\n## Candidate integers\n")
    lines.append("| method | value | note | rejected? |")
    lines.append("|--------|------:|------|-----------|")
    with (FINDINGS / "phase3_candidates.csv").open("w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["method", "value", "note", "rejected"])
        for method, value, note in candidates:
            rej = "yes" if value in REJECTED else ""
            lines.append(f"| {method} | {value} | {note} | {rej} |")
            wr.writerow([method, value, note, rej])

    (FINDINGS / "PHASE3_SELF_CONTAINED.md").write_text("\n".join(lines))
    print(f"Phase 3 complete → {len(candidates)} candidates")


if __name__ == "__main__":
    main()
