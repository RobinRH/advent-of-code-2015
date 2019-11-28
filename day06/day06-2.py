# 17836115
# all lights start on
# follow instructions to turn lights on and off
# x through y -> x is top left of rectangle, y is bottom right of rectangle

import sys
import numpy as np 

# turn on 296,50 through 729,664
# toggle 756,965 through 812,992
# turn off 743,684 through 789,958

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    lines = [line.strip() for line in inputFile.readlines()]

lines = [line.replace('toggle', 'turn toggle').replace(' ', ',') for line in lines]
instructions = [line.split(',') for line in lines]
instructions = [[i[1], int(i[2]), int(i[3]), int(i[5]), int(i[6])] for i in instructions]

# set up the array
lights = np.zeros((1000, 1000), dtype = int)

['on', 674, 953, 820, 965]
['toggle', 398, 147, 504, 583]
['off', 778, 194, 898, 298]

for command, rowStart, colStart, rowEnd, colEnd in instructions:
    diff = 1 if command == 'on' else (-1 if command == 'off' else 2)
    lights[rowStart:(rowEnd + 1), colStart:(colEnd + 1)] += diff
    lights = np.maximum(lights, 0)

# onlights = sum(sum(row) for row in lights)
onlights = lights.sum()

print(onlights)
