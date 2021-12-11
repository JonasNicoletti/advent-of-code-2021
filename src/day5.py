import re
from collections import defaultdict

regex = r"(\d+),(\d+) -> (\d+),(\d+)"

board = defaultdict(int)
with open("src/inputs/day5.txt") as f:
    lines = [(int(i) for i in re.match(regex, line).groups())
             for line in f.readlines()]
    for x1, y1, x2, y2 in lines:
        dx = x2 - x1
        dy = y2 - y1

        for i in range(1 + max(abs(dx), abs(dy))):
            x = x1+(1 if dx > 0 else (-1 if dx < 0 else 0))*i
            y = y1+(1 if dy > 0 else (-1 if dy < 0 else 0))*i
            board[(x, y)] += 1

print(len([k for k in board if board[k] > 1]))
