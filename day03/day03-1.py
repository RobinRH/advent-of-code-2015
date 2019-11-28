# total houses: 2565
# total packages: 8193
# start at (0,0)
# north (^), south (v), east (>), or west (<)
# drop a gift at (0,0) and each location visited

import sys

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    directions = list(inputFile.read())

visited = set()

moves = {
    '^' : (0, 1),
    'v' : (0, -1),
    '>' : (1, 0),
    '<' : (-1, 0)
}

location = (0,0)
visited.add(location)

for move in directions:
    diff = moves[move]
    location = (location[0]+ diff[0], location[1] + diff[1])
    visited.add(location)

print("total packages: " + str(len(directions) + 1))
print("total houses: " + str(len(visited)))
