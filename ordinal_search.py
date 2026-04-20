"""Test every ordinal as the qualifier in:
   'find the <ORDINAL> smallest number with digits totaling twenty-six'

Also test variants where <ORDINAL> qualifies 'number' directly
and where the sentence uses alternate verbs.
"""
from solve_d_pairs import PAIRS, parse_path, GRID

used = set()
for _, p1, _, p2 in PAIRS:
    used |= set(parse_path(p1)); used |= set(parse_path(p2))
letters = ''.join(GRID[r-1][c-1] for r in range(1,15) for c in range(1,15)
                  if (r,c) not in used and GRID[r-1][c-1] != '-')


def subseq_left(hyp, src=letters):
    i = j = 0
    while i < len(src) and j < len(hyp):
        if src[i] == hyp[j]: j += 1
        i += 1
    if j != len(hyp): return None
    # extras
    i = j = 0; mk = [False]*len(src)
    while i < len(src) and j < len(hyp):
        if src[i] == hyp[j]: mk[i] = True; j += 1
        i += 1
    return ''.join(src[k] for k in range(len(src)) if not mk[k])


def digit_sum(n): return sum(int(d) for d in str(n))


# Nth smallest number with digit sum 26
nums = [n for n in range(1, 1_000_000) if digit_sum(n) == 26]

# All ordinals 1 through 100
ORDINALS = [
    "first", "second", "third", "fourth", "fifth", "sixth", "seventh",
    "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth",
    "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth",
    "nineteenth", "twentieth", "twentyfirst", "twentysecond", "twentythird",
    "twentyfourth", "twentyfifth", "twentysixth", "twentyseventh",
    "twentyeighth", "twentyninth", "thirtieth",
]

print("=== Test each ORDINAL with variants ===")
fits = []
for k, ord_w in enumerate(ORDINALS, 1):
    for template in [
        f"findthe{ord_w}smallestnumberwithdigitstotalingtwentysix",
        f"ifindthe{ord_w}smallestnumberwithdigitstotalingtwentysix",
        f"findthe{ord_w}numberwithdigitstotalingtwentysix",
        f"findthe{ord_w}integerwithdigitstotalingtwentysix",
        f"findthe{ord_w}positiveinteger withdigitstotalingtwentysix".replace(" ", ""),
    ]:
        ex = subseq_left(template)
        if ex is not None:
            fits.append((k, ord_w, template, ex))

for rank, ord_w, template, ex in fits:
    val = nums[rank - 1] if rank - 1 < len(nums) else 'out-of-range'
    print(f"  ✓ ({rank:2d}={ord_w:12s}) LEFT={len(ex):2d} → answer={val}")
    print(f"     '{template}'")
    print(f"     extras: '{ex}'\n")

# Check some odd alternatives
print("\n=== Odd alternatives ===")
for template in [
    "findthenumberofnumberswithdigitstotalingtwentysix",
    "howmanythreedigitnumberswithdigitstotalingtwentysix",
    "findthenumberofintegerswithdigitstotalingtwentysix",
    "sumofthreesmallestnumberswithdigitstotalingtwentysix",
    "productofthreesmallestnumberswithdigitstotalingtwentysix",
    "thefourthsmallestnumberwhosedigitsaretwentysix",
]:
    ex = subseq_left(template)
    if ex is not None:
        print(f"  ✓ LEFT={len(ex):2d} {template}")
        print(f"     extras: '{ex}'")
