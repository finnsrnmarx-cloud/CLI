"""verify_t_positions.py — Which starting 't' yields 154? Yields 167?
Run every 't' in the grid as a step-by-6 start; report hex-sum at each.
"""

from __future__ import annotations

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

G = [row.split() for row in GRID_RAW.splitlines()]
H, W = len(G), len(G[0])

# Build flat string (excluding hyphen) with mapping flat_idx -> (row, col)
flat = []
flat_pos = []
for r in range(H):
    for c in range(W):
        ch = G[r][c]
        if ch != "-":
            flat.append(ch)
            flat_pos.append((r + 1, c + 1))
flat_str = "".join(flat)

HEX = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}


def step6_hex_sum(start: int, step: int = 6):
    letters = []
    hex_letters = []
    total = 0
    for i in range(start, len(flat_str), step):
        ch = flat_str[i]
        letters.append(ch)
        if ch in HEX:
            hex_letters.append(ch)
            total += HEX[ch]
    return total, "".join(letters), "".join(hex_letters)


def main():
    print(f"Flat grid length: {len(flat_str)}")
    print(f"First 30 chars: {flat_str[:30]!r}")

    # Report every t and its step-6 result
    print("\nEvery 't' position and its step-by-6 hex sum:\n")
    print(f"{'flat_idx':>8}  {'(row,col)':<10}  {'hex letters':<20}  {'sum':>4}  {'sum+2026':>8}  {'sum+26':>6}")
    print("-" * 80)
    for i, ch in enumerate(flat_str):
        if ch == "t":
            total, visited, hex_only = step6_hex_sum(i)
            rc = flat_pos[i]
            print(f"{i:>8}  {str(rc):<10}  {hex_only:<20}  {total:>4}  {total + 2026:>8}  {total + 26:>6}")

    # Also report every letter (any start) to find starts that yield 154 or 167
    print("\n\nAll starting positions whose step-6 hex sum ∈ {154, 167, 79, 63, 154, 2180-2026, etc}:\n")
    targets = [154, 167, 79, 63, 29, 142, 254]
    hits = {t: [] for t in targets}
    for i, ch in enumerate(flat_str):
        total, _, _ = step6_hex_sum(i)
        if total in hits:
            rc = flat_pos[i]
            hits[total].append((i, ch, rc))
    for t, entries in hits.items():
        print(f"  sum == {t}:")
        for e in entries[:10]:
            print(f"    flat[{e[0]:>3}] = {e[1]!r} at {e[2]}")
        if not entries:
            print(f"    (no start yields this)")

    # And try OTHER step sizes
    print("\n\n--- Step sizes other than 6 (from start=0), hex sums ---")
    for step in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
        total, _, _ = step6_hex_sum(0, step=step)
        print(f"  step={step:>2} from start=0: hex sum = {total}  +2026 = {total + 2026}")

    # Also: what's the total of ALL hex letters in the grid?
    total_all = sum(HEX[c] for c in flat_str if c in HEX)
    count_hex = sum(1 for c in flat_str if c in HEX)
    print(f"\n  Total hex letters in grid: {count_hex}")
    print(f"  Sum of ALL hex letters (a-f) in grid: {total_all}")
    print(f"    + 2026 = {total_all + 2026}")
    print(f"    + 26   = {total_all + 26}")


if __name__ == "__main__":
    main()
