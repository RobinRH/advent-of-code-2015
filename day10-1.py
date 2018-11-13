# 40: 492982
# 50: 6989950
# input: 1321131112, 40 repeats
# test input: 1, repeats: 5, result: 312211
# https://adventofcode.com/2015/day/10

def lookAndSay(input):

    # create an array of sequences that breaks on digits

    # create a new string with a dash evertime the digit changes
    dashed = ""
    for index in range(0, len(input)-1):
        dashed += input[index]
        if input[index] != input[index + 1]:
            dashed += '-'
    dashed += input[-1]
    #print dashed

    tokens = dashed.split('-')
    #print tokens

    output = ""
    for t in tokens:
        output += str(len(t)) + t[0]

    return output

testout = "1"
realout = "1321131112"
for count in range(0, 40):
    #testout = lookAndSay(testout)
    realout = lookAndSay(realout)

#print testout
print "40: ", len(str(realout))

realout = "1321131112"
for count in range(0, 50):
    realout = lookAndSay(realout)

print "50: ", len(str(realout))
