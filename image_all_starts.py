"""Exhaustive thematic start-position search."""
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
    s_all = sum(bs[i] for i in range(start, n, 6))
    s_hex = sum(bs[i] for i in range(start, n, 6) if 10 <= bs[i] <= 15)
    return s_all, s_hex

STARTS = [
    (6,   "Track 6 / Unearthing 2006 / hyphen 14-8"),
    (15,  "15 tracks on album"),
    (14,  "'Can U dig it?' count 14 / Grid side"),
    (23,  "dig count=23 / Vanadium Z / V-from-axiom-Δcol"),
    (44,  "dig count=44 / Ruthenium Z"),
    (30,  "UK chart peak #30"),
    (89,  "Release year 1989 mod 100 / Actinium / Date-wire hex"),
    (79,  "Warriors 1979 / TUNES sum / Gold Z"),
    (53,  "Alan Moore born 1953 / Sum U-rows"),
    (86,  "Watchmen 1986 / Radon Z"),
    (10,  "Unearthing 2010 / Neon Z"),
    (88,  "V for Vendetta 1988 / Radium Z"),
    (20,  "Score = 20"),
    (16,  "Hex base / byte 0x10"),
    (75,  "Hex A-F sum: 10+11+12+13+14+15"),
    (39,  "Al+Fe = 39 thermite"),
    (36,  "Al+V = 36 aluminothermic / Krypton Z"),
    (63,  "Al+Sn = 63"),
    (102, "Al2O3 formula weight ≈ 102"),
    (5,   "5 axioms"),
    (13,  "Aluminum Z"),
    (18,  "Argon Z / Delta-row sum"),
    (26,  "Iron Z (rejected answer)"),
    (50,  "Tin Z"),
    (67,  "Holmium Z / DQT length"),
    (2,   "Helium Z"),
    (54,  "Xenon Z"),
    (33,  "Col 6 hex / Vanadium-hex / U-col-sum"),
    (83,  "Bismuth / concat snake"),
    (65,  "Q+V+Z alphabet"),
    (3,   "3 missing letters"),
    (17,  "Q alphabet pos"),
    (112, "Hyphen 14*8"),
    (22,  "Hyphen 14+8 / V alphabet / rejected"),
    (12,  "FIND THE START length"),
    (9,   "STEP BY SIX length / Nitrogen F"),
    (45,  "Rhodium / main diag"),
    (77,  "Iridium / anti-diag"),
    (82,  "Lead / corner sum"),
    (46,  "Palladium (79-33)"),
    (56,  "Barium (33+23)"),
    (43,  "Technetium / 4085 factor"),
    (100, "HUNDRED king-path"),
]

seen = set()
print(f"{'Start':>5} {'Byte':<10} {'Raw':<6} {'Hex':<6} {'+2026':<6} {'Label'}")
print("-" * 100)
for idx, label in STARTS:
    if idx in seen or idx >= n:
        if idx >= n:
            print(f"  {idx:<4d}  OUT-OF-RANGE                               {label}")
        continue
    seen.add(idx)
    s, h = step6(idx)
    print(f"  {idx:<4d}  0x{bs[idx]:02X} ({bs[idx]:>3d})  {s:<5d}  {h:<5d}  {s+2026:<5d}  {label}")

# Clustering
from collections import defaultdict
sum_clusters = defaultdict(list)
hex_clusters = defaultdict(list)
for idx, label in STARTS:
    if idx >= n: continue
    s, h = step6(idx)
    sum_clusters[s].append((idx, label))
    hex_clusters[h].append((idx, label))

print("\n\n=== Raw sums appearing from MULTIPLE thematic starts ===")
for s in sorted(sum_clusters.keys()):
    entries = sum_clusters[s]
    if len(entries) >= 2:
        print(f"\n  sum={s}: {len(entries)} anchors")
        for idx, label in entries:
            print(f"    byte {idx:>3d}: {label}")

print("\n=== STRICT-HEX sums with 3+ anchors ===")
for h in sorted(hex_clusters.keys()):
    entries = hex_clusters[h]
    if len(entries) >= 3:
        print(f"\n  hex_sum={h}: {len(entries)} anchors")
        for idx, label in entries[:6]:
            print(f"    byte {idx:>3d}: {label}")
