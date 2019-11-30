# 222870
# https://adventofcode.com/2015/day/15

import sys
import pprint
import re
import itertools
import collections

Ingredient = collections.namedtuple('Ingredient', 'name capacity durability flavor texture calories')

filename = sys.argv[1]

with open(filename, 'r') as inputFile:
    lines = [line.strip().replace(':', '').replace(',', '').split(' ') for line in inputFile.readlines()]

#Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# name 0, capacity 2, durability 4, flavor 6, texture 8, calories 10

ingredients = {line[0]: Ingredient(line[0], int(line[2]), int(line[4]), int(line[6]), int(line[8]), int(line[10])) for line in lines}

sugar = ingredients['Sugar']
sprinkles = ingredients['Sprinkles']
candy = ingredients['Candy']
chocolate = ingredients['Chocolate']

def evaluateRecipe(tSugar, tSprinkles, tCandy, tChocolate):
    capacity = tSugar * sugar.capacity + tSprinkles * sprinkles.capacity + tCandy * candy.capacity + tChocolate * chocolate.capacity
    durability = tSugar * sugar.durability + tSprinkles * sprinkles.durability + tCandy * candy.durability + tChocolate * chocolate.durability
    flavor = tSugar * sugar.flavor + tSprinkles * sprinkles.flavor + tCandy * candy.flavor + tChocolate * chocolate.flavor
    texture = tSugar * sugar.texture + tSprinkles * sprinkles.texture + tCandy * candy.texture + tChocolate * chocolate.texture

    if capacity < 0: capacity = 0
    if durability < 0: durability = 0
    if flavor < 0: flavor = 0
    if texture < 0: texture = 0
    score = capacity * durability * flavor * texture
    return score

limit = 100
recipes = [(su, sp, ca, limit - (su + sp + ca)) for su in range(0, limit + 1) for sp in range(0, limit - su + 1) for ca in range(0, limit - (su+sp) + 1)]
scores = [evaluateRecipe(su, sp, ca, ch) for su, sp, ca, ch in recipes]
print(max(scores))
