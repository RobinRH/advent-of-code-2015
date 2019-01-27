# 1586300
# 29x13x26
# calculate total area of sides of box
# find area of smallest side
# add up across all packages

import sys

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    packageSizes = inputFile.readlines()

total = 0
for package in packageSizes:
    [l, w, h] = package.strip().split("x")
    [l, w, h] = map((lambda x : int(x)), [l, w, h])
    total += 2 * (l*w + w*h + l*h)
    smallest = min([l*w, w*h, l*h])
    total += smallest

print total