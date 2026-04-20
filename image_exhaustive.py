"""Exhaustive start-position search — which step-6 sums produce known
meaningful integers?
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

# Exhaustive: step-6 from every start, collect all sums
all_sums = {}  # sum -> list of start indices
for start in range(n):
    s = sum(bs[i] for i in range(start, n, 6))
    all_sums.setdefault(s, []).append(start)

# Strict-hex variant: only count values in 0x0A..0x0F (10-15)
all_sums_strict = {}
for start in range(n):
    s = sum(bs[i] for i in range(start, n, 6) if 10 <= bs[i] <= 15)
    all_sums_strict.setdefault(s, []).append(start)

# Target values we've been tracking
TARGETS = [
    (33, "col 6 hex / U col / Vanadium hex"),
    (23, "Vanadium Z"),
    (79, "Gold Z / TUNES sum"),
    (44, "Ruthenium Z / song dig-count"),
    (67, "Holmium Z / DQT length"),
    (43, "Technetium Z / prime factor of 4085"),
    (89, "Actinium Z / DATEONWIRE hex"),
    (83, "Bismuth Z / snake every-6th"),
    (82, "Lead Z / corner alpha-sum"),
    (45, "Rhodium Z / main diag"),
    (77, "Iridium Z / anti-diag"),
    (46, "Palladium Z"),
    (56, "Barium Z"),
    (14, "grid side"),
    (18, "Argon Z"),
    (65, "Q+V+Z alphabet / step-6 off-0 axioms"),
    (166, "row-step hex"),
    (184, "all elements"),
    (100, "HUNDRED"),
    (2026, "year"),
]

print("=" * 60)
print("Step-6 sums on IMAGE header that match our tracked targets")
print("=" * 60)
print(f"{'Target':<8s} {'Starts':<30s} {'Strict-hex starts':<30s}")
print("-" * 70)

for val, desc in TARGETS:
    starts = all_sums.get(val, [])
    strict = all_sums_strict.get(val, [])
    if starts or strict:
        s1 = ",".join(str(s) for s in starts[:5])
        s2 = ",".join(str(s) for s in strict[:5])
        print(f"  {val:<5d}  {s1:<30s} {s2:<30s}  {desc}")

# Show small-integer sums (<200) that come out of step-6
print("\n\n=== All step-6 sums below 200 (full bytes) ===")
small_sums = sorted([s for s in all_sums.keys() if s < 200])
for s in small_sums:
    print(f"  sum={s:>5d}  at starts: {all_sums[s][:3]}")

# Shown step-6 sums for strict-hex (only 0x0A..0x0F bytes)
print("\n\n=== Strict-hex step-6 sums (ALL) ===")
for s in sorted(all_sums_strict.keys()):
    starts = all_sums_strict[s]
    if len(starts) <= 8:
        print(f"  sum={s:>4d}  at starts: {starts}")
    else:
        print(f"  sum={s:>4d}  at {len(starts)} starts")
