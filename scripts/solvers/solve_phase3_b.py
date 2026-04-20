"""Phase 3b — Test Gemini's alternative 'memory bytes' theory.

Gemini's alternative hypothesis (from the report dump):
  - Step by 6 through PWEI album tracks: 1, 7, 13, 19 (only 15 tracks)
  - Use 'memory used' bytes from album metadata (per Gemini):
    Track 1: 8927, Track 7: 15789, Track 13: 48990
  - ADD THE HEXADECIMALS = sum hex digits of those values
  - LAST ENTRY ENTIRE INTEGER = last one kept as decimal

Test this as a thoroughness check, not because I believe it's right.
"""

# Gemini's claimed values (from the dump)
# Track 1: PWEI Is A Four Letter Word — 8927 bytes
# Track 7: The Fuses Have Been Lit — 15789 bytes
# Track 13: Not Now James, We're Busy... — 48990 bytes
# Track 19: doesn't exist (album has 15 tracks)

memory_bytes = {1: 8927, 7: 15789, 13: 48990}


def hex_digit_sum(n):
    s = hex(n)[2:]  # strip '0x'
    total = 0
    for ch in s:
        if ch.isdigit():
            total += int(ch)
        else:
            total += ord(ch) - ord('a') + 10
    return total, s


for track, mem in memory_bytes.items():
    s, hex_s = hex_digit_sum(mem)
    print(f"Track {track:2d}: memory={mem:6d}  hex='0x{hex_s}'  hex-digit-sum={s}")

# Per Gemini's formula:
# Track 1 hex sum + Track 7 hex sum + Track 13 ENTIRE value
track1_sum, _ = hex_digit_sum(8927)
track7_sum, _ = hex_digit_sum(15789)
last_entire = 48990

print(f"\n  Track 1 hex-digit sum:   {track1_sum}")
print(f"  Track 7 hex-digit sum:   {track7_sum}")
print(f"  Track 13 entire integer: {last_entire}")
print(f"\n  Gemini's answer: {track1_sum} + {track7_sum} + {last_entire} = {track1_sum + track7_sum + last_entire}")

# Alternative: all three hex-summed
all_hex = track1_sum + track7_sum + hex_digit_sum(48990)[0]
print(f"\n  If ALL three hex-summed: {all_hex}")

# Alternative: 0x22DF + 0x3DAD + 0xBF5E as whole numbers
sum_all = 8927 + 15789 + 48990
print(f"\n  Sum of all three raw bytes: {sum_all}")

# VERY IMPORTANT CAVEAT:
# The "memory bytes" data from Gemini's dump is NOT verifiable — no source
# has been found independently that lists these specific values on the album.
# This is likely Gemini fabricating plausible-sounding data to fit its theory.
print("\n" + "=" * 60)
print("CAVEAT:")
print("=" * 60)
print("  Gemini's 'memory bytes' data is UNVERIFIED.")
print("  No independent source has been found for these values on PWEI's")
print("  'This Is the Day...' album. Gemini likely fabricated plausible")
print("  numbers to fit its theory. This path should be treated as")
print("  unreliable without independent confirmation.")
