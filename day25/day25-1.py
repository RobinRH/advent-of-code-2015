# 8997277
# input: row 3010, column 3019
# https://adventofcode.com/2015/day/25

rowTarget = 3010
colTarget = 3019

# Multiply the old by 252533. 
# Divide that by 33554393. 
# That remainder is the next code.
def getNextCode(oldCode):
    product = oldCode * 252533
    newCode = product % 33554393
    return newCode

'''
   | 1   2   3   4   5   6  
---+---+---+---+---+---+---+
 1 |  1   3   6  10  15  21  28
 2 |  2   5   9  14  20  27
 3 |  4   8  13  19  26
 4 |  7  12  18  25
 5 | 11  17  24
 6 | 16  23
'''

def getIndexAtRowCol(row, col):
    # get start value of row
    rowStart = 1
    for i in range(1, row+1):
        rowStart += (i - 1)
    #return rowStart

    colValue = rowStart
    firstInc = row + 1
    for i in range(2, col + 1):
        colValue += firstInc
        firstInc += 1
        
    #return rowStart, colValue
    return colValue

index = getIndexAtRowCol(rowTarget, colTarget)
code = 20151125
for i in range(1, index):
    code = getNextCode(code)

print rowTarget, colTarget, code
