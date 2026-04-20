"""Extended investigation of Mozart/Köchel candidates after the
Symphony 26 → K.184 discovery, plus deeper hex-byte analysis."""
from __future__ import annotations

RAW = """
FF D8 FF E0 00 10 4A 46 49 46 00 01 01 01 00 90 00 90 00 00 FF DB 00 43 00 03 02 02 03 02 02 03 03 03
04 03 03 04 05 08 05 05 04 04 05 0A 07 07 06 08 0C 0A 0C 0C 0B 0A 0B 0B 0D 0E 12 10 0D 0E 11 0E 0B 0B 10
16 10 11 13 14 15 15 15 0C 0F 17 18 16 14 18 12 14 15 14 FF DB 00 43 01 03 04 04 05 04 05 09 05 09 14
0D 0B 0D 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14
""".strip()
bs = [int(t, 16) for t in RAW.split()]
n = len(bs)

print("=== MOZART / KÖCHEL ANGLE ===\n")
print("Row 14 phonetic: 'TUNE twenty-six' = Symphony No. 26 = K.184")
print("Also K.184/161a — note the alternative catalogue number 161a\n")

# Notable Mozart K-numbers
MOZART = {
    1:   "K.1 — Mozart's first composition (Menuett)",
    184: "K.184 — Symphony No. 26 (TUNE 26)",
    183: "K.183 — Symphony No. 25 ('little G minor')",
    201: "K.201 — Symphony No. 29",
    550: "K.550 — Symphony No. 40 ('great G minor')",
    551: "K.551 — Symphony No. 41 'Jupiter' (LAST symphony)",
    626: "K.626 — Requiem (LAST composition, unfinished)",
    161: "K.161a — alternative numbering of No. 26",
    41:  "41 numbered symphonies total",
}
for k, desc in MOZART.items():
    print(f"  K.{k:>3}  {desc}")

# STEP BY SIX from K.184 through Köchel catalogue?
print("\n=== STEP BY SIX from K.184 ===")
for stride_meaning in ["Köchel index", "Symphony number"]:
    print(f"  {stride_meaning}: 184, 190, 196, 202, ...")

# "LAST ENTRY" interpretations
print("\n=== LAST ENTRY ENTIRE INTEGER readings ===")
print("  (a) 184 itself is the final integer (stop at start)")
print("  (b) K.551 — last Mozart symphony")
print("  (c) K.626 — last Mozart composition (Requiem)")
print("  (d) 41 — last symphony number")

# Check image byte at the Köchel number
print("\n=== Image bytes at Köchel-indexed positions ===")
for k in [184, 161, 41, 26, 6]:
    if k < n:
        print(f"  bs[{k}] = 0x{bs[k]:02X} ({bs[k]})")
    else:
        print(f"  {k} out of range (n={n})")

# Sum of first K.184 bytes? (image only has 137 visible)
s137 = sum(bs)
print(f"\n=== Image statistics ===")
print(f"  Total bytes visible: {n}")
print(f"  Sum of all bytes: {s137}")
print(f"  Sum + 2026: {s137 + 2026}")
print(f"  Sum + 26: {s137 + 26}")
print(f"  Sum mod 626: {s137 % 626}")
print(f"  Sum mod 551: {s137 % 551}")

# Hex-strict sum (only 0x0A..0x0F) from various thematic starts
print("\n=== Step-6 STRICT-HEX sums (only bytes 0x0A..0x0F) ===")
for start in [0, 6, 13, 23, 26, 41, 89, 91, 184 % n, 161 % n]:
    if start < n:
        vals = [bs[i] for i in range(start, n, 6) if 10 <= bs[i] <= 15]
        total = sum(vals)
        print(f"  start={start:3d}: sum={total:3d}  (n={len(vals)} strict-hex bytes)")

# Multi-digit hex concatenation: what if we treat stride-6 bytes as
# a big hex number?
print("\n=== Step-6 bytes concatenated as hex string ===")
for start in [0, 6, 91]:
    stepped = [bs[i] for i in range(start, n, 6)]
    hx = "".join(f"{b:02X}" for b in stepped[:8])  # first 8 only
    print(f"  start={start}: {hx}...")

# The Gray 161 connection — K.184/161a means the alternative number 161
print("\n=== K.161a alternative (Symphony 26 has two numbers!) ===")
print(f"  184 + 161 = {184 + 161}")
print(f"  184 - 161 = {184 - 161}")
print(f"  184 * 161 / 1000 ≈ {184 * 161 / 1000:.2f}")

# If STEP BY SIX means stride 6 through Symphony numbers and the
# grid's row-14 "tune 26" is the START:
print("\n=== Stride-6 through Symphony numbers starting at 26 ===")
print("  Symphonies: 26, 32, 38, ... (but Mozart only wrote 41)")
for n_sym in [26, 32, 38, 41]:
    k_map = {26: 184, 32: 318, 38: 504, 41: 551}
    if n_sym in k_map:
        print(f"  Symphony {n_sym} → K.{k_map[n_sym]}")

# Sum of K-numbers for every 6th symphony
print("\n  Sum K-numbers of symphonies 26, 32, 38 = 184+318+504 =", 184+318+504)
print("  Plus 2026:", 184+318+504+2026)
print("  Plus 26:", 184+318+504+26)
