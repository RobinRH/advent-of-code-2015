# 1586300
# 29x13x26
# calculate total area of sides of box
# find area of smallest side
# add up across all packages

import sys

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    packageSizes = inputFile.readlines()

packages = [package.strip().split('x') for package in packageSizes]
packages = [(int(x), int(y), int(z)) for (x, y, z) in packages]
areas = [2 * (l*w + w*h + l*h) for (l, w, h) in packages]
smallest = [min([l*w, w*h, l*h]) for (l, w, h) in packages]
total = sum(areas) + sum(smallest)
print(total)
