# 1061
# https://adventofcode.com/2015/day/18

import sys
import pprint
import numpy as np 

filename = sys.argv[1]

with open(filename, 'r') as inputFile:
    data = [0 if x == '.' else 1 for x in inputFile.read().replace('\n', '')]

npData = np.resize(data, (100,100))
padded = np.pad(npData, 1, 'constant')


def getNewValue(grid, row, col):

    sum = np.sum(grid[row-1:row+2, col-1:col+2]) - grid[row, col]

    # A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
    # A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
    if grid[row, col] == 1:
        if sum == 2 or sum == 3:
            return 1
        else:
            return 0
    else:
        if sum == 3:
            return 1
        else:
            return 0

for step in range(0, 100):
    newGrid = np.zeros((102, 102), dtype = int)
    for row in range(1, 101):
        for col in range(1, 101):
            newGrid[row, col] = getNewValue(padded, row, col)
    padded = newGrid

print(np.sum(padded))
