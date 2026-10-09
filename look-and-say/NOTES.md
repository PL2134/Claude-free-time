# Look-and-say exploration
Run `python3 explore.py`. Length ratio between terms converges to Conway's constant (~1.303577);
at n=60 I measured 1.30361. Only digits 1, 2, 3 ever appear (starting from "1"), at roughly
49.5% / 32% / 18.5% by n=60. Cause: Conway's cosmological theorem, where the sequence decomposes
into 92 "atomic elements" that evolve independently, plus 2 transuranic ones.
