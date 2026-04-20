"""Thematic starting-point search for step-6 on image header.

Test start positions that correspond to:
  - Song facts (track 6, dig count 44, chart peak 30)
  - Element atomic numbers (13, 50, 26, 10, 18, 23, 67)
  - Grid-derived numbers (14, 33, 79, 89, 83)
  - Image-derived markers (DQT length 67, density 144)
"""
from __future__ import annotations

RAW = """
FF D8 FF E0 00 10 4A 46 49 46 00 01 01 01 00 90 00 90 00 00 FF DB 00 43 00 03 02 02 03 02 02 03 03 03
04 03 03 04 05 08 05 05 04 04 05 0A 07 07 06 08 0C 0A 0C 0C 0B 0A 0B 0B 0D 0E 12 10 0D 0E 11 0E 0B 0B 10
16 10 11 13 14 15 15 15 0C 0F 17 18 16 14 18 12 14 15 14 FF DB 00 43 01 03 04 04 05 04 05 09 05 09 14
0D 0B 0D 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14
""".strip()

bs = [int(t, 16) for t in RAW.split()]
n = len(bs)


def step6(start):
    s = sum(bs[i] for i in range(start, n, 6))
    strict = sum(bs[i] for i in range(start, n, 6) if 10 <= bs[i] <= 15)
    count = len(list(range(start, n, 6)))
    return s, strict, count


# Thematic starts
STARTS = [
    # Song-based
    (6, "Track 6 (PWEI song position)"),
    (44, "Dig count in song = 44"),
    (30, "UK chart peak of PWEI single"),
    (23, "dig count variant = 23 OR Vanadium Z"),
    # Element atomic numbers
    (10, "Neon Z"),
    (13, "Aluminum Z"),
    (18, "Argon Z"),
    (26, "Iron Z"),
    (50, "Tin Z (out of header range: 50<137)"),
    (67, "Holmium Z"),
    # Grid-derived numbers
    (14, "Grid side"),
    (33, "Col 6 hex sum"),
    (79, "TUNES sum / Gold"),
    (83, "Bismuth / snake sum"),
    (89, "Actinium / DATEONWIRE"),
    # Other markers
    (22, "second DQT start attempt"),
    (55, "Total hex letters in grid"),
    (65, "Q+V+Z alphabet sum"),
    (91, "Second 0x43 = Holmium byte (our prior match → 184)"),
    (100, "HUNDRED king-path count"),
]


def describe_byte(i):
    if i >= n: return "OUT OF RANGE"
    return f"0x{bs[i]:02X} ({bs[i]})"


print(f"{'Start':>5s} {'Byte':<10s} {'Sum':<6s} {'StrictHex':<10s} {'+2026':<7s} {'Label'}")
print("-" * 80)
for idx, label in STARTS:
    if idx >= n:
        print(f"  {idx:<5d}  OUT-OF-RANGE ({idx} >= {n})                                     {label}")
        continue
    s, strict, cnt = step6(idx)
    print(f"  {idx:<5d}  {describe_byte(idx):<10s} {s:<6d} {strict:<10d} {s+2026:<7d} {label}")

# Also: whole-file stride-6 sum across all starts (grid histogram of "what sums emerge")
print("\n\n=== Step-6 sums ≤ 300 from each start-point ===")
sums_to_starts = {}
for start in range(n):
    s, strict, cnt = step6(start)
    if s <= 300:
        sums_to_starts.setdefault(s, []).append(start)

for s in sorted(sums_to_starts.keys()):
    starts = sums_to_starts[s]
    if len(starts) > 6:
        print(f"  sum={s:<4d}  at {len(starts)} starts")
    else:
        print(f"  sum={s:<4d}  at starts: {starts}")

# And key specific targets from our list
print("\n\n=== Specific candidate-matching starts (from full byte sum) ===")
CANDIDATES = [33, 23, 79, 89, 14, 67, 44, 56, 82, 45, 77, 46, 43, 83, 184, 2193, 2192]
for target in CANDIDATES:
    # Find any start that gives this step-6 sum
    matching_starts = [start for start in range(n) if step6(start)[0] == target]
    if matching_starts:
        print(f"  target {target:>4d}: matches starts {matching_starts[:5]}")
