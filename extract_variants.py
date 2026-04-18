"""Test alternative axiom phrasings.

For each of the 5 axioms, test many operational variants to see if
the grid contains a different instruction than the 'canonical' one.
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
        print(f"  {display:<34s}  {c:>3} paths  {mark}")


# STEP variants
step = [
    ("stepbyone", "STEP BY ONE"),
    ("stepbytwo", "STEP BY TWO"),
    ("stepbythree", "STEP BY THREE"),
    ("stepbyfour", "STEP BY FOUR"),
    ("stepbyfive", "STEP BY FIVE"),
    ("stepbysix", "STEP BY SIX"),
    ("stepbyseven", "STEP BY SEVEN"),
    ("stepbyeight", "STEP BY EIGHT"),
    ("stepbynine", "STEP BY NINE"),
    ("stepbyten", "STEP BY TEN"),
    ("stepbythirteen", "STEP BY THIRTEEN"),
    ("stepbytwenty", "STEP BY TWENTY"),
    ("stepbyhundred", "STEP BY HUNDRED"),
    ("stepback", "STEP BACK"),
    ("stepforward", "STEP FORWARD"),
    ("stepreverse", "STEP REVERSE"),
    ("inreverse", "IN REVERSE"),
    ("reversestep", "REVERSE STEP"),
    ("stepinreverse", "STEP IN REVERSE"),
    ("steppath", "STEP PATH"),
]
report(step, "STEP variants")

# FIND variants
find = [
    ("findthestart", "FIND THE START"),
    ("findtheend", "FIND THE END"),
    ("findthelast", "FIND THE LAST"),
    ("findthefirst", "FIND THE FIRST"),
    ("findthenumber", "FIND THE NUMBER"),
    ("findthevalue", "FIND THE VALUE"),
    ("findthedate", "FIND THE DATE"),
    ("findthehex", "FIND THE HEX"),
    ("findtheanswer", "FIND THE ANSWER"),
    ("findthedigit", "FIND THE DIGIT"),
    ("findthetune", "FIND THE TUNE"),
    ("findthemetals", "FIND THE METALS"),
    ("findtheinteger", "FIND THE INTEGER"),
    ("findwire", "FIND WIRE"),
    ("findthewire", "FIND THE WIRE"),
]
report(find, "FIND variants")

# ADD variants
add = [
    ("addthehexadecimals", "ADD THE HEXADECIMALS"),
    ("addthehexadecimal", "ADD THE HEXADECIMAL"),
    ("addthedigits", "ADD THE DIGITS"),
    ("addthedigit", "ADD THE DIGIT"),
    ("addthenumbers", "ADD THE NUMBERS"),
    ("addthevalues", "ADD THE VALUES"),
    ("addalldigits", "ADD ALL DIGITS"),
    ("addallup", "ADD ALL UP"),
    ("addsix", "ADD SIX"),
    ("addten", "ADD TEN"),
    ("addonly", "ADD ONLY"),
    ("subtract", "SUBTRACT"),
    ("subtractthe", "SUBTRACT THE"),
    ("multiply", "MULTIPLY"),
    ("multiplythe", "MULTIPLY THE"),
    ("sumhex", "SUM HEX"),
    ("sumthehex", "SUM THE HEX"),
    ("sumthedigits", "SUM THE DIGITS"),
    ("sumthe", "SUM THE"),
    ("countthehex", "COUNT THE HEX"),
    ("countthedigits", "COUNT THE DIGITS"),
    ("countthenumbers", "COUNT THE NUMBERS"),
]
report(add, "ADD / ARITHMETIC variants")

# DATE variants
date = [
    ("thereisadateonwire", "THERE IS A DATE ON WIRE"),
    ("thedateonwire", "THE DATE ON WIRE"),
    ("dateonwire", "DATE ON WIRE"),
    ("dateinwire", "DATE IN WIRE"),
    ("dateofwire", "DATE OF WIRE"),
    ("dateatwire", "DATE AT WIRE"),
    ("noisedate", "NO DATE"),
    ("nodate", "NO DATE"),
    ("notadate", "NOT A DATE"),
    ("datehere", "DATE HERE"),
    ("datethere", "DATE THERE"),
    ("datebeneath", "DATE BENEATH"),
    ("datebelow", "DATE BELOW"),
    ("dateabove", "DATE ABOVE"),
    ("datebefore", "DATE BEFORE"),
    ("dateafter", "DATE AFTER"),
    ("dateistoday", "DATE IS TODAY"),
    ("thedate", "THE DATE"),
    ("datesix", "DATE SIX"),
    ("sixdate", "SIX DATE"),
    ("adateexists", "A DATE EXISTS"),
    ("theyear", "THE YEAR"),
    ("timeishere", "TIME IS HERE"),
    ("yearishere", "YEAR IS HERE"),
    ("whatisdate", "WHAT IS DATE"),
    ("dateishere", "DATE IS HERE"),
    ("onthewire", "ON THE WIRE"),
    ("offthewire", "OFF THE WIRE"),
    ("thewire", "THE WIRE"),
    ("follothewire", "FOLLOW THE WIRE"),
    ("followthewire", "FOLLOW THE WIRE"),
    ("tracethewire", "TRACE THE WIRE"),
    ("walkthewire", "WALK THE WIRE"),
    ("readthewire", "READ THE WIRE"),
]
report(date, "DATE/WIRE variants")

# LAST/ENTRY/INTEGER variants
last = [
    ("lastentryentireinteger", "LAST ENTRY ENTIRE INTEGER"),
    ("lastentryis", "LAST ENTRY IS"),
    ("lastentrysix", "LAST ENTRY SIX"),
    ("lastentryhex", "LAST ENTRY HEX"),
    ("lastisten", "LAST IS TEN"),
    ("lastissix", "LAST IS SIX"),
    ("firstlast", "FIRST LAST"),
    ("finalinteger", "FINAL INTEGER"),
    ("wholeinteger", "WHOLE INTEGER"),
    ("wholenumber", "WHOLE NUMBER"),
    ("thewholeinteger", "THE WHOLE INTEGER"),
    ("completeinteger", "COMPLETE INTEGER"),
    ("finalnumber", "FINAL NUMBER"),
    ("theanswer", "THE ANSWER"),
    ("answeris", "ANSWER IS"),
    ("theansweris", "THE ANSWER IS"),
    ("itisinteger", "IT IS INTEGER"),
    ("lastsix", "LAST SIX"),
    ("lastten", "LAST TEN"),
    ("outputinteger", "OUTPUT INTEGER"),
]
report(last, "LAST / FINAL variants")

# Other imperative phrases
other = [
    ("readthis", "READ THIS"),
    ("readeverything", "READ EVERYTHING"),
    ("readeach", "READ EACH"),
    ("takeevery", "TAKE EVERY"),
    ("takethesix", "TAKE THE SIX"),
    ("digfor", "DIG FOR"),
    ("digthis", "DIG THIS"),
    ("digitout", "DIG IT OUT"),
    ("extractit", "EXTRACT IT"),
    ("unearth", "UNEARTH"),
    ("nothing", "NOTHING"),
    ("theansweris", "THE ANSWER IS"),
    ("solveit", "SOLVE IT"),
    ("computeit", "COMPUTE IT"),
    ("seeabove", "SEE ABOVE"),
    ("seebelow", "SEE BELOW"),
]
report(other, "Other imperatives")
