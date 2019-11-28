# 3737498
# The ribbon required to wrap a present is the shortest distance around its sides, 
# or the smallest perimeter of any one face. 
# Each present also requires a bow made out of ribbon as well; 
# the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. 

import sys

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    packageSizes = inputFile.readlines()

packages = [package.strip().split('x') for package in packageSizes]
edges = [(int(x), int(y), int(z)) for (x, y, z) in packages]
areas = [2 * (l*w + w*h + l*h) for (l, w, h) in edges]
bows = [l*w*h for (l, w, h) in edges]
smalls = [2 * (sum(e) - max(e)) for e in edges]
print(sum(bows) + sum(smalls))
