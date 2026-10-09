# Langton's ant
Rule: on white turn right, on black turn left, flip the cell, step forward.
Result from `python3 ant.py`: ~9,900 steps of chaotic-looking behavior, then a repeating
104-step "highway" moving (-2, +2) per cycle (diagonal), forever. Open question: does every
finite starting pattern eventually produce a highway? Unproven.
