"""Try more specific hypotheses, since the 24 extras still contain
clear patterns ('three' lives in the unused string literally)."""
from solve_d_pairs import PAIRS, parse_path, GRID
from collections import Counter

used = set()
for _, p1, _, p2 in PAIRS:
    used |= set(parse_path(p1))
    used |= set(parse_path(p2))

letters = ''.join(GRID[r - 1][c - 1] for r in range(1, 15) for c in range(1, 15)
                  if (r, c) not in used and GRID[r - 1][c - 1] != '-')

print(f"Unused ({len(letters)}): {letters}\n")


def sub(hyp, src=letters):
    i = j = 0
    while i < len(src) and j < len(hyp):
        if src[i] == hyp[j]: j += 1
        i += 1
    if j != len(hyp): return None
    # find extras
    i = j = 0
    matched = [False] * len(src)
    while i < len(src) and j < len(hyp):
        if src[i] == hyp[j]:
            matched[i] = True
            j += 1
        i += 1
    extras = ''.join(src[k] for k in range(len(src)) if not matched[k])
    return extras


H = [
    # Structural variants
    "findthelargestthreedigitnumberwithdigitstotalingtwentysix",
    "findthethreedigitnumberwithdigitstotalingtwentysix",
    "findthefourthsmallestthreedigitnumberwithdigitstotalingtwentysix",
    # "Nth smallest"
    "findthefifthsmallestnumberwithdigitstotalingtwentysix",
    "findthetenthsmallestnumberwithdigitstotalingtwentysix",
    "findthesecondsmallestnumberwithdigitstotalingtwentysix",
    "findthethirdsmallestnumberwithdigitstotalingtwentysix",
    "findtheninthsmallestnumberwithdigitstotalingtwentysix",
    # With 'three' as position or constraint
    "findthesmallestnumberwiththreedigitstotalingtwentysix",
    "findthesmallestnumberwithatleastthreedigitstotalingtwentysix",
    # With "integer" (already used but text might repeat)
    "findthesmallestintegerwithdigitstotalingtwentysix",
    # Shorter / different operators
    "thesmallestnumberwithdigitstotalingtwentysix",
    "smallestnumberwhosedigitssumtotwentysix",
    "smallestnumberwhosedigitsumistwentysix",
    "findasmallestnumberofdigitstotalingtwentysix",
    # Clue style
    "findtheaveragesmallestnumberwithdigitstotalingtwentysix",
    "findtheaveragedigitsofthenumbertwentysix",
    # Stripped down
    "wheredigitstotaltwentysix",
    "thesumofdigitsistwentysix",
]

for h in H:
    extras = sub(h)
    if extras is None:
        print(f"  ✗ NO  {h}")
    else:
        ec = Counter(extras)
        print(f"  ✓ YES ({len(h):2d}) {h}")
        print(f"      extras ({len(extras)}): {extras}")

# Best single answer: if the hypothesis is "findthesmallestTHREEDIGITnumberwith..."
print("\n\nDetailed test: 'findthesmallestthreedigitnumberwithdigitstotalingtwentysix'")
h = "findthesmallestthreedigitnumberwithdigitstotalingtwentysix"
ex = sub(h)
print(f"  len(h)={len(h)}, len(ex)={len(ex) if ex else 'NO MATCH'}")
if ex:
    print(f"  extras: '{ex}'")
    c = Counter(ex)
    print(f"  counts: {dict(c)}")
