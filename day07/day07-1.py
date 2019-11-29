# 956

import sys
import string
import pprint

# af AND ah -> ai
# 1 AND r -> s
# du OR dt -> dv 
# hz RSHIFT 1 -> is
# eo LSHIFT 15 -> es
# xxx NOT lk -> ll
# 0 -> c
# lx -> a


filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    lines = [line.strip().replace('NOT', 'xxx NOT').split(' ') for line in inputFile.readlines()]

alphabet = list(string.ascii_lowercase)

circuits = {}
count = 0
#(operator, output, left, right)
# operators - ANDN, ANDV, OR, RSHIFT, LSHIFT, NOT, ASSIGNN, ASSIGNV
for line in lines:
    operator = line[1]
    output = line[-1]
    right = ''
    if operator in ['RSHIFT', 'LSHIFT']:
        left = line[0]
        right = int(line[2])
    elif operator == 'OR':
        left = line[0]
        right = line[2]
    elif operator == 'NOT':
        left = line[2]
    elif operator == 'AND':
        if line[0][0] in '0123456789':
            operator = 'ANDN'
            left = int(line[0])
            right = line[2]
        else:
            operator = 'ANDV'
            left = line[0]
            right = line[2]
    else:
        if line[0][0] in '0123456789':
            operator = 'ASSIGNN'
            left = int(line[0])
        else:
            operator = 'ASSIGNV'
            left = line[0]
    circuits[output] = (operator, output, left, right)

def getNOT(word):
    leftString = format(word, "016b") # '00110011'
    leftString = leftString.replace("0", "a").replace("1", "0").replace("a", "1")
    return int(leftString, 2)


values = {} # an entry for each variable
while len(values.keys()) < len(circuits):
    # look at each rule and see if it can be resolved and added to values{}
    for operator, output, left, right in circuits.values():
        if output in values.keys():
            # don't need to recalculate this one
            continue

        if operator == "ASSIGNN":
            values[output] = left
        elif operator == "ASSIGNV" and left in values.keys():
            values[output] = values[left]
        elif operator == "NOT" and left in values.keys():
            values[output] = getNOT(values[left])
        elif operator == "RSHIFT"  and left in values.keys():
            values[output] = values[left] >> right
        elif operator == "LSHIFT"  and left in values.keys():
            values[output] = values[left] << right  
        elif operator == "ANDN" and right in values.keys():
            values[output] = left & values[right]
        elif operator == 'ANDV' and left in values.keys() and right in values.keys():
            values[output] = values[left] & values[right]        
        elif operator == 'OR' and left in values.keys() and right in values.keys():
            values[output] = values[left] | values[right]        
        else:
            pass


print (values['a'])
