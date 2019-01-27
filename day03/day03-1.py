# total houses: 2565
# total packages: 8193
# start at (0,0)
# north (^), south (v), east (>), or west (<)
# drop a gift at (0,0) and each location visited

import sys

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    content = inputFile.read()

ns = 0
ew = 0
directions = list(content)

visited = set()
visited.add((ns, ew))

for move in directions:
    if move == '^':     # north
        ns += 1
    elif move == 'v':   # south
        ns -= 1
    elif move == '>':   # east
        ew += 1
    else:               # west
        ew -= 1

    visited.add((ns, ew))

print("total packages: " + str(len(content) + 1))
print("total houses: " + str(len(visited)))
