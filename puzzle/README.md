# Jane Street April 2026 — "Can U Dig It?" Investigation

## Status

**BLOCKED on input.** The 14×14 grid has not yet been supplied. The plan
references specific facts about it (DIGIT as a subsequence in row 9 at cols
5, 8, 9, 10, 13; ALUMINUM on the SW diagonal; hyphen at (14, 8); "tunenty"
and "tessix" in row 14; five axiom phrases at (1,5), (2,8), (9,14), (3,3),
(10,2)), but the 196 actual cell contents are not in this repo.

Jane Street's puzzle page returns 403 to programmatic fetches, and the
search-indexed snippet of the puzzle page says only: *"Apologies, but
we've drawn a blank with this puzzle's instructions. One thing we do know
is that the answer is a positive integer…"* — which is consistent with
the meta-gag you'd expect from a puzzle titled "Can U Dig It?" where the
solver must dig the instructions out of the grid itself.

## To unblock

Paste the 14 rows into `data/grid.txt`, one row per line, exactly 14
characters per line (use `-` for the hyphen cell at row 14 col 8, lowercase
letters everywhere else). Example skeleton:

```
##############
##############
##############
##############
##############
##############
##############
##############
##############
##############
##############
##############
##############
#######-######
```

Once that file is populated, the solvers in `solvers/` will run the whole
phased investigation. Each solver script is idempotent and writes to
`findings/`.

## Layout

- `data/` — raw puzzle inputs (`grid.txt`, `grid.py`)
- `solvers/` — reusable Python modules, one per phase
- `findings/` — human-readable reports and CSVs (generated output)
- `external/` — any external data pulled in (lyrics, discographies, etc.)

## Rejected candidates (do not re-propose)

600, 3241, 3242, 26, 22, 7
