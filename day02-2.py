# 3737498
# The ribbon required to wrap a present is the shortest distance around its sides, 
# or the smallest perimeter of any one face. 
# Each present also requires a bow made out of ribbon as well; 
# the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. 

import sys

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    packageSizes = inputFile.readlines()

total = 0
for package in packageSizes:
    edges = package.strip().split("x")
    edges = map((lambda x : int(x)), edges)
    [l, w, h] = edges
    bow = l * w * h
    smallest = 2 * (sum(edges) - max(edges))
    total += bow + smallest

print total