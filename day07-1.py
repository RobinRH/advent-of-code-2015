# 956

import sys
import re
import string

# af AND ah -> ai
# 1 AND r -> s
# du OR dt -> dv 
# hz RSHIFT 1 -> is
# eo LSHIFT 15 -> es
# NOT lk -> ll
# 0 -> c
# lx -> a


filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    lines = inputFile.readlines()

alphabet = list(string.ascii_lowercase)

andOrExpr = re.compile('(?P<left>..?) (?P<op>AND|OR) (?P<right>..?) -> (?P<output>..?)')
shiftExpr = re.compile('(?P<left>..?) (?P<op>LSHIFT|RSHIFT) (?P<right>\d\d?) -> (?P<output>..?)')
notExpr = re.compile('NOT (?P<input>..?) -> (?P<output>..?)')
valueExpr = re.compile('(?P<value>\d+) -> (?P<output>..?)')
assignExpr = re.compile('(?P<input>..?) -> (?P<output>..?)')

circuits = {}
count = 0

for line in lines:
    line = line.strip()

    andOrMatch = andOrExpr.match(line)
    shiftMatch = shiftExpr.match(line)
    notMatch = notExpr.match(line)
    valueMatch = valueExpr.match(line)
    assignMatch = assignExpr.match(line)

    if andOrMatch:
        output = andOrMatch.group('output')
        left = andOrMatch.group('left')
        right = andOrMatch.group('right')
        op = andOrMatch.group('op')
        circuits[output] = (op, left, right, output)
    elif shiftMatch:
        output = shiftMatch.group('output')
        left = shiftMatch.group('left')
        right = shiftMatch.group('right')
        op = shiftMatch.group('op')
        circuits[output] = (op, left, right, output)
    elif notMatch:
        input = notMatch.group('input')
        output = notMatch.group('output')
        circuits[output] = ('NOT', input, output)
    elif valueMatch:
        value = valueMatch.group('value')
        output = valueMatch.group('output')
        circuits[output] = ('VALUE', value, output) 
    elif assignMatch:
        input = assignMatch.group('input')
        output = assignMatch.group('output')
        circuits[output] = ('ASSIGN', input, output)            
    else:
        print("matching error: " + line)


# this did not work, ran forever
def evaluateCircuit(circuit):
    global count
    count += 1
    if count > 100: return 0

    print circuit
    # circuit is a tuple like ('OR', left, right, output)
    operator = circuit[0]
    if operator == "AND":
        if (list(circuit[1])[0] in alphabet):
            leftVal = evaluateCircuit(circuits[circuit[1]])
        else:
            leftVal = int(circuit[1])
        rightVal = evaluateCircuit(circuits[circuit[2]])
        return leftVal & rightVal
    elif operator == "OR":
        leftVal = evaluateCircuit(circuits[circuit[1]])
        rightVal = evaluateCircuit(circuits[circuit[2]])
        return leftVal | rightVal
    elif operator == "LSHIFT":
        leftVal = evaluateCircuit(circuits[circuit[1]])
        rightVal = int(circuit[2])
        return leftVal << rightVal
    elif operator == "RSHIFT":
        leftVal = evaluateCircuit(circuits[circuit[1]])
        rightVal = int(circuit[2])
        return leftVal >> rightVal
    elif operator == "NOT":
        leftVal = evaluateCircuit(circuits[circuit[1]])
        leftString = format(leftVal, "016b") # '00110011'
        leftString = leftString.replace("0", "a").replace("1", "0").replace("a", "1")
        return int(leftString, 2)
    elif operator == "VALUE":
        print circuit[2], ": ", int(circuit[1])
        return int(circuit[1])
    elif operator == "ASSIGN":
        inputVal = evaluateCircuit(circuits[circuit[1]])
        return inputVal


def getNOT(word):
        leftString = format(word, "016b") # '00110011'
        leftString = leftString.replace("0", "a").replace("1", "0").replace("a", "1")
        return int(leftString, 2)



# doing this another way
nVars = len(circuits)
values = {} # an entry for each variable

while len(values.keys()) < nVars:
    # look at each rule and see if it can be resolved and added to values{}

    for c in circuits.values():
        if c[0] in values.keys():
            continue

        if c[0] == "VALUE":
            values[c[2]] = int(c[1])
        elif c[0] == "ASSIGN":
            if (c[1] in values.keys()):
                values[c[2]] = values[c[1]]
        elif c[0] == "NOT":
            if (c[1] in values.keys()):
                values[c[2]] = getNOT(values[c[1]])
        elif c[0] == "RSHIFT":
            if c[1] in values.keys():
                values[c[3]] = values[c[1]] >> int(c[2])
        elif c[0] == "LSHIFT":
            if c[1] in values.keys():
                values[c[3]] = values[c[1]] << int(c[2])  
        elif c[0] == "AND":
            if c[2] in values.keys():
                rightVal = values[c[2]]
                if (c[1][0] in alphabet) and (c[1] in values.keys()):
                    leftVal = values[c[1]]
                    values[c[3]] = leftVal & rightVal
                elif not (c[1][0] in alphabet):
                    leftVal = int(c[1])
                    values[c[3]] = leftVal & rightVal
        elif c[0] == "OR":
            if c[2] in values.keys():
                rightVal = values[c[2]]
                if (c[1][0] in alphabet) and (c[1] in values.keys()):
                    leftVal = values[c[1]]
                    values[c[3]] = leftVal | rightVal
                elif not (c[1][0] in alphabet):
                    leftVal = int(c[1])
                    values[c[3]] = leftVal | rightVal
        else:
            pass


print values["a"]
