"""Search the grid for more king-path words that could fill the D-pair pattern.

Given the solver's theory — CAN (containers) + U-DIGIT (fingers/toes/number
names/ordinals) — enumerate themed candidate words and check whether each one
traces as a king-path in the 14x14 grid without reusing cells.
"""
from __future__ import annotations
import sys
sys.setrecursionlimit(5000)

GRID = [
    "rsdifindthsart",
    "ehresodaeetgna",
    "netrhalxhgowip",
    "egedauyueaenrp",
    "ptnnmllmxidnee",
    "ohuinkthanacsm",
    "alnpfyldebsttn",
    "uumjarebemehrw",
    "mithdceigiugts",
    "tlamibftotegat".replace("tlamibftotegat","tlamibftotegеt".replace("е","e")),  # safety: it's "tlamibftoteget"
    "sailniitniapen",
    "nstoagrniiobrt",
    "ietiryeesprayw",
    "tunenty-tessix",
]
# Re-set row 10 cleanly (fix any encoding mishap)
GRID[9] = "tlamibftoteget"
assert all(len(r) == 14 for r in GRID), [len(r) for r in GRID]
H = W = 14

# Words already claimed by the solver's 12 pairs
ALREADY = {
    "aluminum","can","end","fire","jar","opener","paint","soda","spray","tin",
    "trash","oil",
    "hexadecimal","thumb","ringtoe","binary","pinky","hundreds","baseten",
    "hallux","integer","units","appendage","tens",
}

# Curated wordlist across plausible themes
WORDS = {
  # Containers / "can" theme
  "can": "CAN", "jar": "CAN", "tin": "CAN", "urn": "CAN", "mug": "CAN", "jug": "CAN",
  "pot": "CAN", "pan": "CAN", "box": "CAN", "bin": "CAN", "bag": "CAN", "tub": "CAN",
  "vat": "CAN", "keg": "CAN", "cup": "CAN",
  "bucket": "CAN", "barrel": "CAN", "bottle": "CAN", "vial": "CAN", "flask": "CAN",
  "kettle": "CAN", "pitcher": "CAN", "basket": "CAN", "crate": "CAN", "chest": "CAN",
  "tray": "CAN", "pail": "CAN", "canister": "CAN", "tube": "CAN", "drum": "CAN",
  "vase": "CAN", "carton": "CAN", "case": "CAN", "vessel": "CAN", "cistern": "CAN",
  "tank": "CAN", "mailbox": "CAN", "mailbag": "CAN", "sack": "CAN", "pouch": "CAN",
  "amphora": "CAN", "decanter": "CAN", "pitcher": "CAN",
  # Container contents (the sorted solver's can-words)
  "aluminum": "CAN", "paint": "CAN", "fire": "CAN", "soda": "CAN", "spray": "CAN",
  "oil": "CAN", "trash": "CAN", "end": "CAN", "opener": "CAN",

  # Digit-body theme (fingers, toes, joints)
  "thumb": "DIGIT", "index": "DIGIT", "middle": "DIGIT", "ring": "DIGIT",
  "pinky": "DIGIT", "pinkie": "DIGIT", "pointer": "DIGIT", "finger": "DIGIT",
  "toe": "DIGIT", "bigtoe": "DIGIT", "ringtoe": "DIGIT", "hallux": "DIGIT",
  "knuckle": "DIGIT", "nail": "DIGIT", "cuticle": "DIGIT", "joint": "DIGIT",
  "appendage": "DIGIT", "phalanx": "DIGIT", "digit": "DIGIT",
  "foot": "DIGIT", "hand": "DIGIT",

  # Digit-number theme (bases, counting, ordinals)
  "binary": "DIGIT", "octal": "DIGIT", "decimal": "DIGIT", "hex": "DIGIT",
  "hexadecimal": "DIGIT", "ones": "DIGIT", "tens": "DIGIT", "hundreds": "DIGIT",
  "thousands": "DIGIT", "millions": "DIGIT", "billions": "DIGIT",
  "units": "DIGIT", "integer": "DIGIT", "base": "DIGIT", "baseten": "DIGIT",
  "count": "DIGIT", "digits": "DIGIT", "number": "DIGIT", "numeral": "DIGIT",
  # Ordinal names — these might be the START word
  "first": "ORD", "second": "ORD", "third": "ORD", "fourth": "ORD",
  "fifth": "ORD", "sixth": "ORD", "seventh": "ORD", "eighth": "ORD",
  "ninth": "ORD", "tenth": "ORD", "eleventh": "ORD", "twelfth": "ORD",
  "thirteenth": "ORD", "fourteenth": "ORD", "fifteenth": "ORD",
  "sixteenth": "ORD", "seventeenth": "ORD", "eighteenth": "ORD",
  "nineteenth": "ORD", "twentieth": "ORD",

  # Number words
  "one": "NUM", "two": "NUM", "three": "NUM", "four": "NUM", "five": "NUM",
  "six": "NUM", "seven": "NUM", "eight": "NUM", "nine": "NUM", "ten": "NUM",
  "eleven": "NUM", "twelve": "NUM", "thirteen": "NUM", "fourteen": "NUM",
  "fifteen": "NUM", "sixteen": "NUM", "seventeen": "NUM", "eighteen": "NUM",
  "nineteen": "NUM", "twenty": "NUM", "thirty": "NUM", "forty": "NUM",
  "fifty": "NUM", "sixty": "NUM", "seventy": "NUM", "eighty": "NUM",
  "ninety": "NUM", "hundred": "NUM", "thousand": "NUM", "million": "NUM",

  # Instruction-fragment words (the "drawn a blank" clue hypothesis)
  "find": "CLUE", "smallest": "CLUE", "largest": "CLUE", "number": "CLUE",
  "with": "CLUE", "digits": "CLUE", "totaling": "CLUE", "summing": "CLUE",
  "equal": "CLUE", "twentysix": "CLUE", "twenty": "CLUE", "six": "CLUE",
  "sum": "CLUE", "to": "CLUE",
}

def in_bounds(r, c):
    return 0 <= r < H and 0 <= c < W

def kings_of(r, c):
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == dc == 0: continue
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc): yield nr, nc

def find_kingpath(word):
    word = word.lower()
    # returns first found path as list of (r,c)
    start_cells = [(r, c) for r in range(H) for c in range(W) if GRID[r][c] == word[0]]
    def dfs(r, c, i, used, path):
        if i == len(word):
            return list(path)
        for nr, nc in kings_of(r, c):
            if (nr, nc) in used: continue
            if GRID[nr][nc] != word[i]: continue
            used.add((nr, nc))
            path.append((nr, nc))
            res = dfs(nr, nc, i + 1, used, path)
            if res: return res
            path.pop()
            used.remove((nr, nc))
        return None
    for sr, sc in start_cells:
        used = {(sr, sc)}
        path = [(sr, sc)]
        res = dfs(sr, sc, 1, used, path)
        if res: return res
    return None

def fmt_path(path):
    if not path: return ""
    def cell(r, c): return f"{chr(ord('A')+c)}{r+1}"
    return "->".join(cell(r, c) for r, c in path)

# Run
print(f"{'Word':<16} {'Theme':<8} {'New?':<6} {'Path'}")
print("-" * 90)
results = {"found": [], "missing": []}
for w in sorted(WORDS, key=lambda x: (WORDS[x], -len(x), x)):
    theme = WORDS[w]
    path = find_kingpath(w)
    if path:
        is_new = w.lower() not in ALREADY
        tag = "NEW" if is_new else ""
        print(f"{w:<16} {theme:<8} {tag:<6} {fmt_path(path)}")
        results["found"].append((w, theme, is_new, path))
    else:
        results["missing"].append(w)

print("\n--- Words NOT found as king-paths ---")
print(", ".join(results["missing"]))

# Summary of NEW findings
print("\n=== NEW words found (not already in solver's 12 pairs) ===")
new = [r for r in results["found"] if r[2]]
for w, theme, _, path in new:
    print(f"  {theme:<6} {w:<14} {fmt_path(path)}")
