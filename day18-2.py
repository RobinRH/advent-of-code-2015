# 1006
# turn the four corners on before each animation
# https://adventofcode.com/2015/day/18

import sys
import pprint
import numpy as np 
import scipy

filename = sys.argv[1]

with open(filename, 'r') as inputFile:
    data = inputFile.read()

data = data.replace("\n","")

data = list(map(lambda x: 0 if x == "." else 1, data))
npData = np.array(data)
npData = np.resize(npData, (100,100))
padded = np.pad(npData, 1, 'constant')


kernel = np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]])

def getNewValue(grid, row, col):

    sum = grid[row-1, col-1] + grid[row-1, col] + grid[row-1, col + 1] + \
        grid[row, col-1] + grid[row, col + 1] + \
        grid[row+1, col-1] + grid[row+1, col] + grid[row+1, col + 1]
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

padded[1,1] = 1
padded[1, 100] = 1
padded[100, 1] = 1
padded[100, 100] = 1

for step in range(0, 100):
    newGrid = np.zeros((102, 102), dtype = int)
    for row in range(1, 101):
        for col in range(1, 101):
            newVal = getNewValue(padded, row, col)
            newGrid[row, col] = newVal
            newGrid[row, col] = getNewValue(padded, row, col)
    padded = newGrid
    padded[1,1] = 1
    padded[1, 100] = 1
    padded[100, 1] = 1
    padded[100, 100] = 1


print np.sum(padded)