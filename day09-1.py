# min: 141
# max: 736
# https://adventofcode.com/2015/day/9

import sys
import string
import re
import pprint
import itertools

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    lines = inputFile.readlines()

alphabet = list(string.ascii_lowercase)

# AlphaCentauri to Snowdin = 66
distanceExpr = re.compile('(.+) to (.+) = (\d+)')

distances = {}
cities = set()

# create a dictionary of distances
# the key for distances is (city1, city2)
# also include (city2, city1) for easier lookup
for line in lines:
    match = distanceExpr.match(line)
    if match:
        city1 = match.group(1)[0:2]
        city2 = match.group(2)[0:2]
        distances[(city1, city2)] = int(match.group(3))
        distances[(city2, city1)] = int(match.group(3))
        cities.add(match.group(1)[0:2])
        cities.add(match.group(2)[0:2])


# find all paths, using itertools to create all permutations
# a somewhat brute force approach, compared to a-star, but clear enough and we don't have
# performance constaints
allPaths = list(itertools.permutations(cities))

pathLengths = []

# find length of each path
for path in allPaths:
    pathLength = 0
    for leg in range(0, len(path) - 1):
        city1 = path[leg]
        city2 = path[leg + 1]
        miles = distances[(city1, city2)]
        pathLength += miles

    pathLengths.append(pathLength)

print "min: ", min(pathLengths)
print "max: ", max(pathLengths)