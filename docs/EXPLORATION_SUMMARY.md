# Exploration Summary for Jane Street April 2026 "Can U Dig It?" Puzzle

## Overview of the Puzzle

The puzzle is a 14x14 grid of lowercase letters with a single hyphen located at cell `(14, 8)`. The title of the puzzle is "Can U Dig It?" (with a capitalized U), and the prompt indicates that "the answer is a positive integer". Several candidates and theories have been tested by the community, but the final, verified answer from Jane Street is still pending (as of this exploration).

## Key Themes and Theories Discovered in the Codebase

### 1. The "Digging for Metals" Theme (Strongest Candidates)
The phrase "Can U dig it?" features prominently. This led solvers to consider elements/metals as a possible answer, as these are substances one "digs" for.

- **Vanadium (V):**
    - The word "dig" appears 23 times in the Pop Will Eat Itself song "Can U Dig It?".
    - 23 is the atomic number of Vanadium (V).
    - V is one of the letters intentionally omitted from the grid (along with Q and Z).
    - The title asks "Can U dig it?" which might imply "Can you dig up the missing V?".

- **Gold (Au):**
    - The 14th (bottom) row of the grid visually spells out "twenty-six" with a few extra embedded letters: `t u n e n t y - t e s s i x`.
    - Extracting the extra letters gives `u, n, t, e, s` which anagrams to `TUNES`.
    - The alphabet position sum of `T+U+N+E+S` is exactly `79`.
    - 79 is the atomic number of Gold (Au), the iconic metal humans dig for.

### 2. The Instruction Axioms and "Step by Six" Mechanic
Five key instructional phrases form unique or near-unique "king-paths" (paths resembling a chess King's moves) through the grid:
1. `FIND THE START`
2. `STEP BY SIX`
3. `ADD THE HEXADECIMALS`
4. `THERE IS A DATE ON WIRE`
5. `LAST ENTRY ENTIRE INTEGER`

This has led solvers to try chains of operations:
- A prominent candidate is **33**, derived from summing the values of hexadecimal letters (`a-f`) in Column 6 (a literal interpretation of `STEP BY SIX`). Column 6 contains `a` (10), `c` (12), and `b` (11), which sum to 33. This has several convergent indicators:
    - 33 is the hex-letter sum of the word `VANADIUM`.
    - 33 is the sum of the column indices for all `u` characters in the grid.
    - 33 1/3 RPM relates to the `TUNES` theme.
- Another variation starts at the first valid hex letter (`d` at 1,3), steps 6 cells at a time, sums the hex values (167), and adds 2026 (interpreting `LAST ENTRY ENTIRE INTEGER` as the current year, found on the "wire"/hyphen row). Result: **2193**.

## Execution Outputs from the Solver Scripts

I ran several solver scripts included in the repository to observe their operation:

- `solve.py`: Showed grid statistics, including 7 `u`s, the absence of `q`, `v`, `z`. Confirmed that single-digit words (like `one`, `two`, `three`, `six`, `nine`) and `ten`, `nineteen`, `ninety`, `ninetynine`, `hundred` can be traced as king paths. Also confirmed the bottom row anomalies (anagram to `TUNES`).

- `solve_33.py`: Strongly confirmed the candidate 33. The script verifies that Column 6 is the only column where the hex sum matches 33. It also verified the `U` position columns sum to 33.

- `solve_instructions.py`: Verified that the five core instruction phrases (`FIND THE START`, `ADD THE HEXADECIMALS`, etc.) can definitively be traced via valid king-paths. It proved these paths exist and their traces are mathematically sound.

## Conclusions

The codebase serves as a comprehensive "lab notebook" for tackling the Jane Street April 2026 puzzle. It holds code for traversing the grid, extracting patterns, and validating multiple candidate theories. While many theories exist, candidates like **33**, **23**, and variants based on the hex-sum mechanics (e.g., **2193**) are highly ranked.
