# a = 0 -> 170
# a = 1 -> 247
# there is only one code file, simply change the initial value of a
# https://adventofcode.com/2015/day/23

# hlf r sets register r to half its current value, then continues with the next instruction.
# tpl r sets register r to triple its current value, then continues with the next instruction.
# inc r increments register r, adding 1 to it, then continues with the next instruction.
# jmp offset is a jump; it continues with the instruction offset away relative to itself.
# jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
# jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

import sys
import pprint

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    lines = inputFile.readlines()

instructions = []
for line in lines:
    tokens = line.replace(",", "").replace("\n", "").split(" ")
    instructions.append(tokens)

#pprint.pprint(instructions)

aReg = 1    # non-negative integers
bReg = 0    # non-negative integers

counter = 0
while counter < len(instructions):
    inst = instructions[counter]
    if inst[0] == 'hlf':
        if inst[1] == 'a': 
            aReg = aReg / 2
        else:
            bReg = bReg / 2
        counter += 1
    elif inst[0] == 'tpl':
        if inst[1] == 'a': 
            aReg = aReg * 3
        else:
            bReg = bReg * 3
        counter += 1
    elif inst[0] == 'inc':
        if inst[1] == 'a': 
            aReg += 1
        else:
            bReg += 1
        counter += 1
    elif inst[0] == 'jmp':
        counter += int(inst[1])
    elif inst[0] == "jie":
        if inst[1] == 'a': 
            if aReg % 2 == 0:
                counter += int(inst[2])
            else:
                counter += 1
        else:
            if bReg % 2 == 0:
                counter += int(inst[2])
            else:
                counter += 1
    elif inst[0] == "jio": # jump if 1
        if inst[1] == 'a': 
            if aReg == 1:
                counter += int(inst[2])
            else:
                counter += 1
        else:
            if bReg == 1:
                counter += int(inst[2])
            else:
                counter += 1
    else:
        print "error"

print "a: ", aReg
print "b: ", bReg