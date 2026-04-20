"""Phase 6 — Image metadata as the hexadecimal source.

The user revealed that the downloaded puzzle image has metadata
including a raw_header with explicit hexadecimal bytes. The axiom
'ADD THE HEXADECIMALS' may literally mean 'sum the hex bytes in
the image's header'.

This is a major pivot — the 'hexadecimals' were in the image all
along, not in the grid.
"""
from __future__ import annotations

# Raw header from the user's metadata viewer
RAW_HEADER = """
FF D8 FF E0 00 10 4A 46 49 46 00 01 01 01 00 90 00 90 00 00 FF DB 00 43 00 03 02 02 03 02 02 03 03 03
04 03 03 04 05 08 05 05 04 04 05 0A 07 07 06 08 0C 0A 0C 0C 0B 0A 0B 0B 0D 0E 12 10 0D 0E 11 0E 0B 0B 10
16 10 11 13 14 15 15 15 0C 0F 17 18 16 14 18 12 14 15 14 FF DB 00 43 01 03 04 04 05 04 05 09 05 09 14
0D 0B 0D 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14
""".strip()

# Parse all hex bytes
hex_tokens = RAW_HEADER.split()
bytes_list = [int(t, 16) for t in hex_tokens]
print(f"Total bytes in visible header: {len(bytes_list)}")

print("\n=== Basic sums ===")
print(f"Sum of ALL header bytes: {sum(bytes_list)}")
print(f"Sum of bytes excluding FF markers: {sum(b for b in bytes_list if b != 0xFF)}")
print(f"Sum of bytes excluding 00: {sum(b for b in bytes_list if b != 0x00)}")

# Identify JPEG structure
print("\n=== JPEG markers parsed ===")
print(f"  FF D8 = SOI (Start of Image)")
print(f"  FF E0 = APP0 (JFIF)")
print(f"  Length 0x{bytes_list[4]:02X} {bytes_list[5]:02X} = {bytes_list[4]*256+bytes_list[5]} bytes")
# Next 5 bytes should be 'JFIF\0'
jfif_bytes = bytes_list[6:11]
print(f"  JFIF id: {bytes(jfif_bytes).decode('latin-1')!r}")
print(f"  FF DB = DQT (Quantization Tables)")
# First DQT length
idx = 20  # after JFIF block
if bytes_list[idx] == 0xFF and bytes_list[idx+1] == 0xDB:
    dqt_len = bytes_list[idx+2]*256 + bytes_list[idx+3]
    print(f"  DQT #1 length: 0x{dqt_len:04X} = {dqt_len} (value 67!)")

# Specific interesting subsets
print("\n=== Specific byte counts ===")
from collections import Counter
cnt = Counter(bytes_list)
for val, count in sorted(cnt.items(), key=lambda x: -x[1])[:10]:
    print(f"  0x{val:02X} ({val}): {count} occurrences")

# 0x14 appears many times — notable
count_14 = cnt[0x14]
print(f"\n0x14 (decimal 20) appears {count_14} times")
print(f"Sum of 0x14 occurrences: {count_14 * 20}")

# Image dimensions from metadata
print("\n=== Image dimensions ===")
print(f"  Image size: 847 x 900 = {847*900}")
print(f"  847 + 900 = {847+900}")
print(f"  900 - 847 = {900-847}")
print(f"  GCD: {__import__('math').gcd(847, 900)}")
print(f"  Megapixels: 0.762 -> 762?")

# Y-density values: 0x90 = 144 each
print(f"\n  Y-density: 0x90 = {0x90} (x2 for both dimensions)")
print(f"  Sum: 144+144 = 288")

# The sum of specific sections
print("\n=== Sum of bytes AFTER FF DB (quantization tables) ===")
# Find first FF DB marker
first_ffdb = -1
for i in range(len(bytes_list)-1):
    if bytes_list[i] == 0xFF and bytes_list[i+1] == 0xDB:
        first_ffdb = i
        break
if first_ffdb >= 0:
    # Skip FF DB 00 43 00 (marker + length + table id)
    qtable_start = first_ffdb + 5
    # Quantization table is 64 bytes
    qtable1 = bytes_list[qtable_start:qtable_start+64]
    print(f"  First quantization table (64 bytes) sum: {sum(qtable1)}")

# All bytes > 0 and < 0xFF
non_marker = [b for b in bytes_list if 0 < b < 0xFF]
print(f"\n  Sum of non-zero non-marker bytes: {sum(non_marker)}")
print(f"  Count: {len(non_marker)}")
