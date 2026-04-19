"""'FIND THE START' in the image header + step-by-6 + sum.

Test every plausible starting byte position. For each one, stride 6
and sum the values.
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


def step6_from(start):
    return sum(bs[i] for i in range(start, n, 6))


# Plausible starting points
STARTS = [
    (0, "byte 0 — FF (SOI marker start)"),
    (1, "byte 1 — D8 (SOI end / real image start)"),
    (2, "byte 2 — FF (APP0 marker start)"),
    (3, "byte 3 — E0 (APP0 end)"),
    (4, "byte 4 — 00 (APP0 length high)"),
    (5, "byte 5 — 10 (APP0 length low)"),
    (6, "byte 6 — J (JFIF id start)"),
    (10, "byte 10 — 00 (JFIF terminator)"),
    (11, "byte 11 — 01 (version major)"),
    (20, "byte 20 — FF (first DQT marker)"),
    (21, "byte 21 — DB (DQT marker end)"),
    (22, "byte 22 — 00 (DQT length high)"),
    (23, "byte 23 — 43 (DQT length low, 67)"),
    (24, "byte 24 — 00 (DQT table id)"),
    (25, "byte 25 — first quantization value"),
    (89, "byte 89 — second FF DB"),
    (94, "byte 94 — start of table 2 values"),
]

print(f"Header bytes: {n}")
print(f"\n{'Start':<5s} {'Value':<5s} {'Bytes':<6s} {'Sum':<6s} {'Label'}")
print("-" * 70)
for s, label in STARTS:
    if s >= n: continue
    val = f"0x{bs[s]:02X}"
    count = len(list(range(s, n, 6)))
    total = step6_from(s)
    print(f"  {s:<3d}  {val:<5s} {count:>3d}    {total:>5d}   {label}")

# Special: start from the first hex 'a-f' byte (in ASCII sense those are 97-102)
# But our bytes are different. "First hex-valid byte" in a numeric sense
# might mean first byte >= 10 and <= 15 (0x0A..0x0F)
print("\n--- Start at first byte in range 0x0A..0x0F ---")
for i in range(n):
    if 0x0A <= bs[i] <= 0x0F:
        count = len(list(range(i, n, 6)))
        total = step6_from(i)
        print(f"  byte {i} = 0x{bs[i]:02X}  step6 sum from here = {total}")
        break

# First byte == 0x43 (Holmium / ASCII 'C')
print("\n--- Start at first 0x43 byte (the '67' = Holmium match) ---")
for i in range(n):
    if bs[i] == 0x43:
        count = len(list(range(i, n, 6)))
        total = step6_from(i)
        print(f"  byte {i}  step6 sum from here = {total}")
        break

# "FIND THE START" in JPEG terms = SOI = FF D8 which is bytes 0-1
# The 'start' position is 0 (byte after SOI = byte 2).
# Start positions to specifically test for axiom match:
print("\n--- Axiom-interpreted start points ---")
test_starts = {
    "Byte 0 (literal first byte)": 0,
    "Byte 2 (after SOI)": 2,
    "Byte 20 (first DQT marker = 'hexadecimal table start')": 20,
    "Byte 23 (DQT length = 67/Holmium)": 23,
    "Byte 25 (first quant table byte = 'hex data start')": 25,
}
for label, s in test_starts.items():
    tot = step6_from(s)
    print(f"  {label:<50s} sum = {tot}")

# Only sum values that are a-f (10-15) — the literal "hexadecimals"
print("\n--- Strict: only count bytes that are a-f (10..15) as the 'hexadecimals' ---")
for s, label in STARTS[:10]:
    if s >= n: continue
    stepped = [bs[i] for i in range(s, n, 6)]
    hex_only = [b for b in stepped if 10 <= b <= 15]
    total = sum(hex_only)
    count = len(hex_only)
    print(f"  start {s:>2d}: {count} hex-valid bytes, sum={total}")
