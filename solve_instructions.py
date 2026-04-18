"""solve_instructions.py — Full catalogue of instruction / sentence
phrases that trace as king-paths in the Jane Street 'Can U Dig It?' grid.

Verified findings (all 5 from the original user report trace cleanly):

  ✓  FIND THE START           (12 chars, 1 path)
  ✓  ADD THE HEXADECIMALS     (18 chars, 4 paths)
  ✓  STEP BY SIX              (9 chars, 3 paths)
  ✓  THERE IS A DATE ON WIRE  (18 chars, 2 paths)
  ✓  LAST ENTRY ENTIRE INTEGER(22 chars, 1 path)

This script re-verifies those, then tests many variants to see which
other instruction-style phrases are also embedded.
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

G = [row.split() for row in GRID_RAW.splitlines()]
H, W = len(G), len(G[0])
DIRS8 = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]


def count_king_paths(word: str, stop_at=None) -> int:
    count = 0

    def dfs(r, c, i, seen):
        nonlocal count
        if stop_at is not None and count >= stop_at:
            return
        if i == len(word):
            count += 1
            return
        for dr, dc in DIRS8:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in seen and G[nr][nc] == word[i]:
                dfs(nr, nc, i + 1, seen | {(nr, nc)})

    for r in range(H):
        for c in range(W):
            if G[r][c] == word[0]:
                dfs(r, c, 1, frozenset({(r, c)}))
                if stop_at is not None and count >= stop_at:
                    return count
    return count


def find_first_path(word: str):
    def dfs(r, c, i, seen, path):
        if i == len(word):
            return path
        for dr, dc in DIRS8:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in seen and G[nr][nc] == word[i]:
                res = dfs(nr, nc, i + 1, seen | {(nr, nc)}, path + [(nr, nc)])
                if res:
                    return res
        return None

    for r in range(H):
        for c in range(W):
            if G[r][c] == word[0]:
                res = dfs(r, c, 1, frozenset({(r, c)}), [(r, c)])
                if res:
                    return res
    return None


# ----------------------------------------------------------------------
# Phrase catalogue grouped by category
# ----------------------------------------------------------------------

# Category A: the 5 phrases claimed in the user's original report
REPORT_AXIOMS = [
    "findthestart",
    "addthehexadecimals",
    "stepbysix",
    "thereisadateonwire",
    "lastentryentireinteger",
]

# Category B: close variants of report axioms
VARIANTS = [
    "findthe", "findthenumber", "findthevalue", "findstart",
    "findthenumbers", "findall",
    "addthehex", "addthehexadecimal", "addthehexes",
    "addthenumbers", "addthevalues", "addall", "addupall",
    "stepbytwo", "stepbythree", "stepbyfour", "stepbyfive",
    "stepbyseven", "stepbyeight", "stepbynine", "stepbyten",
    "thereisadate", "thereisadateon", "dateonwire",
    "lastentry", "lastentryis", "lastentryisinteger",
    "entireinteger", "lastisinteger",
    "integer", "integers",
    "hex", "hexadecimal", "hexadecimals",
    "date", "wire", "start", "end", "last", "first",
]

# Category C: other imperative patterns
IMPERATIVES = [
    "sumthedigits", "sumthenumbers", "sumalldigits", "sumall",
    "countthedigits", "countthenumbers", "countallthe",
    "multiplythe", "multiplyall", "multiplyby",
    "dividethe", "divideby",
    "pickthe", "choosethe", "takethe", "taketheanswer",
    "readthe", "readevery", "readfromstart",
    "writethe", "writeout",
    "solvethe", "solveit",
    "lookforthe", "lookfora",
    "startat", "startatone", "startwithone",
    "beginat", "beginwith",
    "endatthe", "endwith",
    "takefirst", "takelast",
    "takeeveryother", "takeeverysix",
    "readdown", "readup", "readdownwards",
    "followthepath", "followthewire",
    "digforgold", "digforsilver", "digmetals",
    "digthroughthe", "dignumbers", "digthenumbers",
]

# Category D: answer / result phrasing
ANSWER_PHRASES = [
    "theansweris", "theanswer", "theanswerispositive",
    "theanswerisaninteger", "answerisinteger", "answerispositive",
    "itsaninteger", "itisapositive", "itisinteger",
    "positiveinteger", "positive",
]

# Category E: thematic / Jane Street
THEMATIC = [
    "canudigit", "canyoudigit", "canyoudig", "canudig",
    "yescandig", "yesucan", "yesyoucan",
    "digforaluminium", "digforaluminum", "digfortin",
    "aluminumandtin", "aluminumtin",
    "twentysix", "twentysixhundred",
    "tunes", "tune",
]


def test_all(phrases, group_name):
    print(f"\n{'='*80}")
    print(f"{group_name}")
    print("=" * 80)
    found = []
    missing = []
    for p in sorted(set(phrases), key=lambda x: (-len(x), x)):
        k = count_king_paths(p)
        if k > 0:
            found.append((p, k))
        else:
            missing.append(p)
    print(f"{'phrase':<30}  {'paths':>6}")
    print("-" * 40)
    for p, k in found:
        print(f"{p:<30}  {k:>6}")
    if missing:
        print(f"\nNot found ({len(missing)}): {', '.join(missing[:10])}{'...' if len(missing) > 10 else ''}")
    return found


def main():
    print("=" * 80)
    print("VERIFIED: User report's 5 'Core Axioms' all trace as king-paths")
    print("=" * 80)
    for p in REPORT_AXIOMS:
        k = count_king_paths(p)
        path = find_first_path(p)
        if path:
            cells = [(r + 1, c + 1) for r, c in path]
            first = cells[:4]
            last = cells[-2:]
            print(f"\n  ✓ {p}  (len {len(p)}, {k} path(s))")
            print(f"      first 4 cells: {first}")
            print(f"      last 2 cells:  {last}")

    test_all(VARIANTS, "VARIANTS of report axioms")
    test_all(IMPERATIVES, "Other imperative-style phrases")
    test_all(ANSWER_PHRASES, "Answer / result phrases")
    test_all(THEMATIC, "Thematic / title phrases")

    # Consolidated: all phrases that trace, ranked by length
    print("\n\n" + "=" * 80)
    print("ALL INSTRUCTION PHRASES FOUND (all categories combined)")
    print("=" * 80)
    all_phrases = set(REPORT_AXIOMS + VARIANTS + IMPERATIVES + ANSWER_PHRASES + THEMATIC)
    hits = []
    for p in all_phrases:
        k = count_king_paths(p)
        if k > 0:
            hits.append((len(p), k, p))
    hits.sort(reverse=True)
    print(f"{'len':>4}  {'paths':>6}  phrase")
    print("-" * 60)
    for L, k, p in hits:
        print(f"{L:>4}  {k:>6}  {p}")
    print(f"\nTotal phrases traceable: {len(hits)}")


if __name__ == "__main__":
    main()
