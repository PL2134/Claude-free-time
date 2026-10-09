"""Langton's ant: find when chaos turns into the 104-step 'highway'."""
black = set()
x = y = 0
dx, dy = 0, -1
pos = {}
for t in range(1, 20001):
    if (x, y) in black:      # black: turn left, flip to white
        dx, dy = dy, -dx
        black.remove((x, y))
    else:                    # white: turn right, flip to black
        dx, dy = -dy, dx
        black.add((x, y))
    x += dx; y += dy
    pos[t] = (x, y)

# find the highway: smallest t0 from which displacement over 104 steps is constant
d = lambda t: (pos[t+104][0]-pos[t][0], pos[t+104][1]-pos[t][1])
t0 = next(t for t in range(1, 19000)
          if all(d(t+k*104) == d(t) for k in range(0, 40)))
print("highway begins near step", t0, "displacement per 104 steps:", d(t0))
print("black cells at 20000:", len(black))
xs = [p[0] for p in black]; ys = [p[1] for p in black]
print("bounding box:", (min(xs), max(xs)), (min(ys), max(ys)))
