# 569999
# all lights start on
# follow instructions to turn lights on and off
# x through y -> x is top left of rectangle, y is bottom right of rectangle

import sys

# turn on 296,50 through 729,664
# toggle 756,965 through 812,992
# turn off 743,684 through 789,958

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    lines = inputFile.readlines()

lines = [line.strip().replace('toggle', 'turn toggle').replace(' ', ',') for line in lines]
instructions = [line.split(',') for line in lines]
instructions = [[i[1], int(i[2]), int(i[3]), int(i[5]), int(i[6])] for i in instructions]

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

onlights = sum(sum(row) for row in lights)

print (onlights)
