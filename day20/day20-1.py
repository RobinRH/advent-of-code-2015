# 786240
# 34000000: find first house to get at least this many presents
# https://adventofcode.com/2015/day/20

import math
import functools

def primeFactors(n): 
    # https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
    factors = []

    # Print the number of two's that divide n 
    while n % 2 == 0: 
        factors.append(2)
        n = n / 2

    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            factors.append(i)
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        factors.append(n)

    return factors

def sumOfFactors(factors):
    # https://www.math.upenn.edu/~deturck/m170/wk3/lecture/sumdiv.html

    unique = set(factors)
    #twos = list(filter(lambda x: x == 2, factors))

    product = 1
    for p in unique:
        k = len(list(filter(lambda x: x == p, factors)))
        sumpk = ((p ** (k + 1)) -1)/ (p - 1)
        #print sumpk
        product *= sumpk

    return product

howMany = 34000000
n = 0
while True:
    n += 1
    factors = primeFactors(n)
    gifts = sumOfFactors(factors) * 10
    if n % 10000 == 0: print n, gifts
    #print n, factors, uniques
    #print n, gifts
    if gifts > howMany: break

print n


'''
howMany = 3400000
found = False
houseNumber = 960000
while not found:
    gifts = 0
    for elf in range(1, (houseNumber / 2) + 1):
        if houseNumber % elf == 0: # then elf visits the house
            gifts += elf
            if gifts >= howMany:
                print houseNumber
                exit()
    gifts += houseNumber
    print houseNumber, gifts, howMany - gifts
    #if houseNumber % 1000 == 0: print houseNumber, gifts
    houseNumber += 96

'''

