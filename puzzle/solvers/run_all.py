"""Convenience runner — executes phase1..phase3 once data/grid.txt is filled.

Usage:
  python solvers/run_all.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "data"))

from grid import load_grid, assert_filled  # noqa: E402

if __name__ == "__main__":
    g = load_grid()
    assert_filled(g)

    import phase1_catalog
    import phase2_axioms
    import phase3_mechanic

    phase1_catalog.main()
    phase2_axioms.main()
    phase3_mechanic.main()
    print("All phases complete. See findings/.")
