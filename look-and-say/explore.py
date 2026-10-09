"""Look-and-say exploration: growth ratio -> Conway's constant, and digit stats."""
from itertools import groupby
from collections import Counter

def step(s):
    return "".join(str(len(list(g))) + k for k, g in groupby(s))

s, prev = "1", 1
for n in range(1, 61):
    s = step(s)
    if n % 10 == 0:
        print(f"n={n:2d} len={len(s):>9,} ratio={len(s)/prev:.9f}")
    prev = len(s)

c = Counter(s)
print("digit freq at n=60:", {d: round(c[d]/len(s), 4) for d in sorted(c)})
print("max digit:", max(s))
