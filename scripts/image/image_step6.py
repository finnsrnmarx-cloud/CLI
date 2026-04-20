"""Step-by-six analysis on the image raw header bytes.

Apply all 5 axioms to the image header:
  FIND THE START -> start at first byte / first non-marker
  STEP BY SIX -> stride 6 through bytes
  ADD THE HEXADECIMALS -> sum them
  THERE IS A DATE ON WIRE -> JPEG metadata timestamps / date fields?
  LAST ENTRY ENTIRE INTEGER -> final total
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
print(f"Header bytes: {n}\n")

print("=" * 50)
print("STEP-BY-SIX on header bytes")
print("=" * 50)
for offset in range(6):
    stepped = [bs[i] for i in range(offset, n, 6)]
    s = sum(stepped)
    print(f"  offset {offset}: {len(stepped)} bytes  sum={s}")
    print(f"    values: {' '.join(f'{b:02X}' for b in stepped[:15])}{'...' if len(stepped)>15 else ''}")

print("\n=== Sum of ALL bytes = 4085 ===")
print(f"4085 = 5 * 19 * 43")
print(f"4085 mod 256 = {4085 % 256}")
print(f"4085 mod 100 = {4085 % 100}")
print(f"4085 - 2026 = {4085 - 2026}")
print(f"4085 / 65 = {4085 / 65}")

# Starting from first actual DATA byte (after FF D8 FF E0 = start + marker)
# The APP0 block: FF E0 00 10 4A 46 49 46 00 ...
# The quantization table starts after APP0 block

# Find first FF DB and step from there
first_ffdb = next(i for i in range(len(bs)-1)
                  if bs[i] == 0xFF and bs[i+1] == 0xDB)
qt_start = first_ffdb + 5  # skip FF DB 00 43 00
print(f"\n--- Step-6 starting from quantization table (index {qt_start}) ---")
for offset in range(6):
    stepped = [bs[i] for i in range(qt_start + offset, n, 6)]
    s = sum(stepped)
    print(f"  offset {offset}: sum={s}")

# Specific interesting sums
print("\n=== Key individual values found ===")
print(f"  FF D8 bytes (start marker): {0xFF + 0xD8} = {0xFF+0xD8}")
print(f"  JFIF ASCII: J(74)+F(70)+I(73)+F(70) = {74+70+73+70}")
print(f"  JFIF version 01 01 01: {0x01+0x01+0x01} = 3")
print(f"  Density: 0x90 + 0x90 = 288")
print(f"  DQT length: 67 (= Holmium Z)")
print(f"  Table 1 sum (64 quantization values): 988")
print(f"  0x14 count (36) x 20 = 720")

# Sum quantization table values only (ignoring markers + lengths)
# Table 1 starts at qt_start, is 64 bytes
qt1 = bs[qt_start:qt_start+64]
print(f"\n  Quant table 1 (64 values): sum = {sum(qt1)}")
# find second FF DB
second_ffdb = next(i for i in range(qt_start + 64, len(bs)-1)
                   if bs[i] == 0xFF and bs[i+1] == 0xDB)
qt2_start = second_ffdb + 5  # FF DB 00 43 01
qt2 = bs[qt2_start:]
print(f"  Quant table 2 starts at {qt2_start}, {len(qt2)} bytes visible")
print(f"  Table 2 sum: {sum(qt2)}")
print(f"  Both tables combined: {sum(qt1) + sum(qt2)}")

# Step 6 JUST on quant table 1
print(f"\n--- Step 6 through quant table 1 (64 bytes) ---")
for off in range(6):
    s = sum(qt1[off::6])
    print(f"  off {off}: sum = {s}")

# Differences
print(f"\n=== Differences / alternatives ===")
print(f"  Table1 - Table2: {sum(qt1) - sum(qt2)}")
print(f"  Table2 - Table1: {sum(qt2) - sum(qt1)}")
print(f"  2026 - 988 (table 1): {2026 - 988}")
print(f"  Image dimension 847 * sum_table1: {847 * 988}")
