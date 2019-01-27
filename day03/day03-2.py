# total houses: 2639
# total packages: 8193
# santa and robot start at (0,0)
# santa follows even directions, robot follows odd directions
# north (^), south (v), east (>), or west (<)
# drop a gift at (0,0) and each location visited

import sys

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    content = inputFile.read()

directions = list(content)

visited = set()

def visitLocations(directions) :
    ns = 0
    ew = 0
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

santaDirections = []
robotDirections = []

for index in range(0, len(directions)):
    if index % 2 == 0:
        santaDirections.append(directions[index])
    else:
        robotDirections.append(directions[index])


visitLocations(santaDirections)
visitLocations(robotDirections)

print("total packages: " + str(len(content) + 1))
print("total houses: " + str(len(visited)))

