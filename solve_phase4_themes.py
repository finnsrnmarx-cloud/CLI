"""Phase 4b — Filter for COMMON English (not archaic) + thematic clusters.

The web2 dictionary contains many obscure words. Score by:
  - Length (longer = better)
  - Commonality (filter against a frequent-words set)
  - Theme relevance (numbers, music, mining, computing, time)
"""
from __future__ import annotations
import sys
from english_words import get_english_words_set

ALL_ENG = get_english_words_set(["web2"], lower=True)

# Build a "common" subset by intersecting with a word-frequency-like list
# Use words that look "modern English" — avoid weird endings
def looks_common(w):
    if len(w) < 5: return False
    if not w.isalpha(): return False
    # Exclude weirdness
    bad_suffix = ["ite", "oid", "ial", "ist", "ous"]
    if w.endswith("aria") or w.endswith("oria"): return False
    return True

ENG = {w for w in ALL_ENG if 5 <= len(w) <= 15 and w.isalpha()}

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
TERMINAL = "$"

def build_trie(words):
    trie = {}
    for w in words:
        node = trie
        for ch in w:
            node = node.setdefault(ch, {})
        node[TERMINAL] = w
    return trie

TRIE = build_trie(ENG)

def search():
    found = set()
    def dfs(r, c, node, seen):
        ch = G[r][c]
        if ch == "-" or ch not in node: return
        nxt = node[ch]
        if TERMINAL in nxt:
            found.add(nxt[TERMINAL])
        for dr, dc in DIRS:
            nr, nc = r+dr, c+dc
            if 0<=nr<H and 0<=nc<W and (nr,nc) not in seen:
                dfs(nr, nc, nxt, seen | {(nr, nc)})
    for r in range(H):
        for c in range(W):
            if G[r][c] != "-":
                dfs(r, c, TRIE, frozenset({(r, c)}))
    return found

sys.setrecursionlimit(20000)
words = search()

# A small set of "common modern English" 5+ letter words known a priori
COMMON_5PLUS = set("""
about above abuse actual added admit adopt after again agent agree ahead alarm
album alert alike alive allow alone along altar alter anger anglo angry apart
apple apply arena argue arise armed array arrow asset audio audit avoid awake
award aware badly basic basis batch beach began begin begun being below bench
bible black blade blame blank blast blend blind block blood board bonus boost
bound brain brand brass brave bread break breed brick brief bring brisk broad
broke brown brush build built bunch burst butter buyer cable cache candy carry
catch cause cease chain chair chalk charm chart cheap cheat check chess chest
chief child china choke chord chose chunk civil claim clamp clang clash class
clean clear click cliff climb cling clock close cloth cloud clown clued coach
coast color count cover crack craft crash crazy cream creek crime crowd crown
crude crush cycle daily dance dated dealt death debit debug delay delta dense
depth derby deter dig digit digital dirty doing donor dozen drain drama dread
dream dress drift drill drink drive drove dying eager eagle early earth eaten
edges eight elder elect elite empty enact ended enemy enjoy enter entry equal
error event every exact exist extra faith false fancy fault favor feast fence
fewer field fifth fifty fight final finance findi finer first fixed flame flash
flask fleet flesh flight flood floor flora flour fluid focus force forge forget
forty found frame frank fraud fresh front fruit fully funny gauge giant given
glass glory grade grand grant grass great green grief grind gross group grown
guard guess guest guide guilt happy harsh haste hatch heart heavy henry hence
hides honor horse hotel house human ideal image imply index inner input issue
items japan joint judge juice known label labor lamps lance large later laugh
laundry leads leaks learn lease least leave legal level light limit linen liner
lined links liver loans local locks lodge logic loose loser lower loyal lucky
lunar lunch lying magic major maker mango maple match maybe meant medal media
metal might minor mixed model money month moral motel motor mount mouse mouth
movie music nails naked named nasty nepal never night noble noise north novel
nurse occur ocean offer often older opera order other ought outer owner panel
panic paper paris party pasta patch pause peace peach pearl phase phone photo
piano piece pilot pitch place plain plane plant plate point poker polar polish
porch pound power pride prime print prior prize proof proud proxy psalm pulse
punch pupil quake queen query quest quick quiet quote radar radio raise rally
random range rapid ratio reach react ready realm rebel refer relax repay reply
right rigid rival river robot rocky rover royal rugby rural saint salad salty
saved scale scope score sense serve seven shall shape shark sharp sheep sheet
shelf shell shift shine shock shoot shore short shown sight silly since singh
sixth sixty sized skill sleep slept slice slide slope small smart smell smile
smoke snake solid solve sound south space spare speak speed spell spend spent
spice spoke sport spray squad stack staff stage stake stand stars start state
stays steam steel steep steer stick still stock stone storm stove style sugar
sweet swift swing sword table taken talks taste teach teams tease teeth temple
tense terms tests texts theme there thick thing think third those three throw
thumb tight times tired title today total touch tough tower toxic trace track
trade trail train trait trash tread treat trend trial tribe trick tried tries
truck truly trunk trust truth twice twins ultra uncle under union unite unity
until upper upset urban usage usual valid value video virus vital vivid voice
vowel waste watch water weapon wedge whale wheat wheel whilst white whole whose
witty woman world worry worth would wound wrist write wrong yacht youth zebra
""".lower().split())

print(f"Total king-path English words: {len(words)}")
print(f"Common-set size: {len(COMMON_5PLUS)}\n")

print("=" * 70)
print("LONG WORDS (>= 7 chars) THAT ARE ALSO COMMON-ish")
print("=" * 70)
common_long = sorted([w for w in words if len(w) >= 7 and w in COMMON_5PLUS],
                     key=lambda w: (-len(w), w))
for w in common_long:
    print(f"  {len(w):2d}  {w}")

print(f"\nFound {len(common_long)} common 7+ letter words.")

print("\n" + "=" * 70)
print("LONG WORDS (>= 8 chars) regardless of commonality")
print("=" * 70)
all_long = sorted([w for w in words if len(w) >= 8], key=lambda w: (-len(w), w))
for w in all_long:
    is_common = "★" if w in COMMON_5PLUS else " "
    print(f"  {len(w):2d}  {is_common}  {w}")

print(f"\nFound {len(all_long)} 8+ letter words ({sum(1 for w in all_long if w in COMMON_5PLUS)} common-marked).")

print("\n" + "=" * 70)
print("THEMATIC FILTERS")
print("=" * 70)
themes = {
    "numbers/digits": ["digit", "number", "integer", "count", "total", "sum",
                       "addition", "decimal", "binary", "hex", "value"],
    "music/tunes": ["tune", "music", "song", "note", "chord", "melody", "rhythm",
                    "verse", "chorus"],
    "mining/digging": ["dig", "mine", "miner", "ore", "metal", "drill", "shaft"],
    "computing/hex": ["bit", "byte", "code", "data", "hex", "memory", "register"],
    "time/date": ["date", "year", "month", "day", "time", "calendar"],
    "wire/electric": ["wire", "cable", "current", "spark", "circuit"],
    "directional": ["north", "south", "east", "west", "left", "right", "up", "down"],
}

for theme, kw_list in themes.items():
    matches = [w for w in words if any(kw in w for kw in kw_list)]
    matches.sort(key=lambda w: (-len(w), w))
    if matches:
        print(f"\n  Theme: {theme}")
        for w in matches[:15]:
            print(f"    {len(w):2d}  {w}")
