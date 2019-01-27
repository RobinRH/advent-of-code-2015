# next: cqjxxyzz
# next: cqkaabcc
# input: cqjxjnds
# test input: abcdefgh output: abcdffaa
# test input: ghijklmn output: ghjaabcc
# https://adventofcode.com/2015/day/11


import sys
import string

input = sys.argv[1]

alphabet = string.ascii_lowercase

def increment(password):

    index = alphabet.find(password[7])
    if index + 1 <= 25:
        newPassword = password[0:-1] + alphabet[index + 1]
        return newPassword
    else:
        newPassword = password[0:-1] + "a"
        newPassword = incrementByPlace(newPassword, 6)
        return newPassword

def incrementByPlace(password, place):

    if place < 0:
        print("error")
        return

    if password[place] != 'z':
        # increment the place
        index = alphabet.find(password[place])
        newChar = alphabet[index + 1]
        newPassword = password[0:place] + newChar + password[place + 1:]
        return newPassword
    else:
        # set place equal to a and increment next place
        newPassword = password[0:place] + "a" + password[place + 1:]
        newPassword = incrementByPlace(newPassword, place - 1)
        return newPassword

# Passwords must include one increasing straight of at least three letters, 
# like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
def containsStraight(password):
    for index in range(len(password) - 3):
        i1 = alphabet.find(password[index])
        i2 = alphabet.find(password[index + 1])
        i3 = alphabet.find(password[index + 2])
        if (i2 == i1 + 1) and (i3 == i1 + 2):
            #print "straight: ", password
            return True

    return False

# Passwords may not contain the letters i, o, or l, 
# as these letters can be mistaken for other characters and are therefore confusing.
def noIOL(password):
    if 'i' in password:
        return False

    if 'o' in password:
        return False

    if 'l' in password:
        return False

    #print "no iol: ", password
    return True

# Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
# create all the pairs
pairs = []
for c in alphabet:
    pairs.append(c + c)
#print pairs

def hasPairs(password):

    count = 0
    for pair in pairs:
        if pair in password:
            count += 1
            if count >= 2:
                #print password
                return True

    return False

valid = False
while not valid:
    input = increment(input)

    if containsStraight(input) and noIOL(input) and hasPairs(input):
        valid = True

print input



