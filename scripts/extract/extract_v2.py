"""Extended variant testing — explore the alternates that DID trace.

Key discoveries from first pass:
  - FIND THE HEX (5 paths)
  - LAST TEN (5 paths)
  - NO DATE (2 paths)
  - STEP BY TEN (2 paths)

Test: do longer variants built on these traces too? Maybe the real
axioms are slightly different than we've been using.
"""
from __future__ import annotations

GRID_RAW = """
r s d i f i n d t h s a r t
e h r e s o d a e e t g n a
n e t r h a l x h g o w i p
e g e d a u y u e a e n r p
p t n n m l l m x i d n e e
o h u i n k t h a n a c s m
a l n p f y l d e b s t t n
u u m j a r e b e m e h r w
m i t h d c e i g i u g t s
t l a m i b f t o t e g e t
s a i l n i i t n i a p e n
n s t o a g r n i i o b r t
i e t i r y e e s p r a y w
t u n e n t y - t e s s i x
""".strip()

G = [r.split() for r in GRID_RAW.splitlines()]
H, W = 14, 14
DIRS = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]

def kp(word, stop=5):
    cnt = 0
    def dfs(r, c, i, seen):
        nonlocal cnt
        if stop and cnt >= stop: return
        if i == len(word): cnt += 1; return
        for dr, dc in DIRS:
            nr, nc = r+dr, c+dc
            if 0<=nr<H and 0<=nc<W and (nr,nc) not in seen and G[nr][nc]==word[i]:
                dfs(nr, nc, i+1, seen | {(nr, nc)})
    for r in range(H):
        for c in range(W):
            if G[r][c] == word[0]:
                dfs(r, c, 1, frozenset({(r, c)}))
                if stop and cnt >= stop: return cnt
    return cnt

def report(phrases, title):
    print(f"\n=== {title} ===")
    for phrase, display in phrases:
        c = kp(phrase, stop=5)
        mark = "✓" if c > 0 else "✗"
        print(f"  {display:<36s}  {c:>3}  {mark}")

# Extended FIND THE HEX variants
find_hex = [
    ("findthehex", "FIND THE HEX"),
    ("findthehexadecimal", "FIND THE HEXADECIMAL"),
    ("findthehexadecimals", "FIND THE HEXADECIMALS"),
    ("findthehexday", "FIND THE HEX DAY"),
    ("findthehexsix", "FIND THE HEX SIX"),
    ("findthehexten", "FIND THE HEX TEN"),
    ("findthehexnine", "FIND THE HEX NINE"),
    ("findthehexandsix", "FIND THE HEX AND SIX"),
]
report(find_hex, "FIND THE HEX... variants")

# Extended NO DATE variants
no_date = [
    ("nodate", "NO DATE"),
    ("nodateonwire", "NO DATE ON WIRE"),
    ("nodatehere", "NO DATE HERE"),
    ("nodatenone", "NO DATE NONE"),
    ("nodateexists", "NO DATE EXISTS"),
    ("nonedate", "NONE DATE"),
    ("thereisnodate", "THERE IS NO DATE"),
    ("thereisnodateonwire", "THERE IS NO DATE ON WIRE"),
]
report(no_date, "NO DATE variants")

# LAST TEN variants
last_ten = [
    ("lastten", "LAST TEN"),
    ("lasttensix", "LAST TEN SIX"),
    ("lasttenentry", "LAST TEN ENTRY"),
    ("lasttenentireinteger", "LAST TEN ENTIRE INTEGER"),
    ("lasttenisinteger", "LAST TEN IS INTEGER"),
    ("lasttenhex", "LAST TEN HEX"),
    ("finalten", "FINAL TEN"),
    ("finaltenentry", "FINAL TEN ENTRY"),
    ("finaltensix", "FINAL TEN SIX"),
]
report(last_ten, "LAST TEN variants")

# STEP BY TEN variants
step_ten = [
    ("stepbyten", "STEP BY TEN"),
    ("stepbytensix", "STEP BY TEN SIX"),
    ("stepbyteneach", "STEP BY TEN EACH"),
    ("stepbytensteps", "STEP BY TEN STEPS"),
    ("stepbyoneten", "STEP BY ONE TEN"),
    ("tenstep", "TEN STEP"),
    ("stepten", "STEP TEN"),
]
report(step_ten, "STEP BY TEN variants")

# Numeric variations — is the instruction actually "STEP BY [X]" for various X?
print("\n=== STEP BY ALL NUMBERS ===")
for n in range(1, 30):
    nums = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",
            8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",
            13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",
            17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty"}
    if n not in nums: continue
    phrase = "stepby" + nums[n]
    c = kp(phrase, stop=3)
    if c:
        print(f"  STEP BY {nums[n].upper():<10s}  ({n:>2})  {c} paths")

# ADD THE [X] variants
print("\n=== ADD THE ALL NUMBERS ===")
for n in range(1, 30):
    nums = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",
            8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",
            13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen"}
    if n not in nums: continue
    phrase = "addthe" + nums[n]
    c = kp(phrase, stop=3)
    if c:
        print(f"  ADD THE {nums[n].upper():<10s}  ({n:>2})  {c} paths")

# FIND THE [X] variants where X is theme-related
print("\n=== FIND THE [...] ===")
for target in ["hex", "date", "wire", "start", "end", "last", "first", "answer",
               "integer", "digit", "tune", "tunes", "six", "ten", "metal", "nine",
               "key", "code", "solve", "wireend", "hexday", "digday", "hexsix",
               "hexten", "hextoten", "tunehex", "sixhex", "tenhex"]:
    c = kp("findthe" + target, stop=3)
    if c:
        print(f"  FIND THE {target.upper():<10s}  {c} paths")
