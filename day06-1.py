# 569999
# all lights start on
# follow instructions to turn lights on and off
# x through y -> x is top left of rectangle, y is bottom right of rectangle

import sys
import re

# turn on 296,50 through 729,664
# toggle 756,965 through 812,992
# turn off 743,684 through 789,958

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    lines = inputFile.readlines()

instructions = []
['turn', ' ', 'on', ' ', '489', ',', '959', ' ', 'through', ' ', '759', ',', '964\n']
for line in lines:
    tokens = re.split(r"( |,)", line)
    if len(tokens) == 13: # turn on/ turn off
        ins = [tokens[2], int(tokens[4]), int(tokens[6]), int(tokens[10]), int(tokens[12])]
    else:    # toggle
        ins = [tokens[0], int(tokens[2]), int(tokens[4]), int(tokens[8]), int(tokens[10])]
    instructions.append(ins)

# set up the array
lights = [[False for x in range(1000)] for y in range(1000)]

# ['on', 674, 953, 820, 965]
# ['toggle', 398, 147, 504, 583]
# ['off', 778, 194, 898, 298]
for ins in instructions:
    for row in range(ins[1], ins[3]+1):
        for col in range(ins[2], ins[4]+1):
            if ins[0] == "on":
                lights[row][col] = True
            elif ins[0] == "off":
                lights[row][col] = False
            else:
                lights[row][col] = not lights[row][col]

onlights = 0
for row in range(0, 1000):
    for col in range(0, 1000):
        if lights[row][col] == True:
            onlights += 1

print onlights