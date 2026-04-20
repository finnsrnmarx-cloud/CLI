"""Try to decode the hidden 'drawn a blank' sentence.

Hypothesis: the clue is
  'I FIND THE SMALLEST NUMBER WITH DIGITS TOTALING TWENTY-SIX'
(or some variant). Remaining letters should be consumed by yet-
undiscovered D-pairs.

Strategy:
  - Try every word the solver's clue might use as a subsequence
  - Report what extra letters remain after subtracting the sentence
  - Those extras are what MUST be in missing D-pairs
"""
from solve_d_pairs import PAIRS, parse_path, GRID
from collections import Counter

used = set()
for _, p1, _, p2 in PAIRS:
    used |= set(parse_path(p1))
    used |= set(parse_path(p2))

# Unused letters in reading order with position
unused = []
for r in range(1, 15):
    for c in range(1, 15):
        if (r, c) not in used and GRID[r - 1][c - 1] != '-':
            unused.append((r, c, GRID[r - 1][c - 1]))

letters = ''.join(u[2] for u in unused)
print(f"Unused ({len(unused)} letters):\n  {letters}\n")

# Try matching various hypothesis sentences as ORDERED subsequences
hypotheses = [
    "findthesmallestnumberwithdigitstotalingtwentysix",
    "ifindthesmallestnumberwithdigitstotalingtwentysix",
    "findthethirdsmallestnumberwithdigitstotalingtwentysix",
    "findtheninthsmallestnumberwithdigitstotalingtwentysix",
    "findthesmallestnumberwhosedigitstotaltwentysix",
    "findthelargestnumberwithdigitstotalingtwentysix",
    "findthesmallestprimewithdigitstotalingtwentysix",
    "findthesmallestpalindromewithdigitstotalingtwentysix",
    "findthesmallestsquarewithdigitstotalingtwentysix",
    "findthesmallestoddnumberwithdigitstotalingtwentysix",
    "findthesmallesteventwentysix",  # shorter
    "ifindthreetwentysix",
]


def match_subsequence(hyp, src):
    """Return (matched_positions, unmatched_char_counts) or None if hyp
    is not a subseq.
    """
    i = j = 0
    matched_idx = []
    while i < len(src) and j < len(hyp):
        if src[i] == hyp[j]:
            matched_idx.append(i)
            j += 1
        i += 1
    if j != len(hyp):
        return None
    # Remaining chars (ones NOT matched) are "extras"
    used_set = set(matched_idx)
    extras = [src[k] for k in range(len(src)) if k not in used_set]
    return matched_idx, extras


print("=== Testing hypotheses as ORDERED SUBSEQUENCE of unused letters ===\n")
for h in hypotheses:
    result = match_subsequence(h, letters)
    if result is None:
        print(f"  ✗ {h!r}: NOT a subsequence")
        continue
    matched_idx, extras = result
    extras_counter = Counter(extras)
    print(f"  ✓ {h!r} ({len(h)} chars)")
    print(f"     extras: {len(extras)} chars — {''.join(sorted(extras))}")
    print(f"     extra counts: {dict(extras_counter)}")
    # Show which unused positions match the hypothesis
    matched_positions = [(unused[k][0], unused[k][1], letters[k]) for k in matched_idx]
    print(f"     first 10 matched positions: {matched_positions[:10]}")
    print()

# Also compute: if sentence is "I FIND THE SMALLEST NUMBER WITH DIGITS TOTALING TWENTY SIX"
# how many letters left over? -> those letters must be in missing pairs
best = "ifindthesmallestnumberwithdigitstotalingtwentysix"
result = match_subsequence(best, letters)
if result:
    _, extras = result
    print(f"Best fit leaves {len(extras)} extra letters: {''.join(sorted(extras))}")
    print("These must appear in missing D-pair word(s).")
