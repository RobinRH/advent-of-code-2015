# 117936
# only cookies with 500 calories are eligible
# https://adventofcode.com/2015/day/15

import sys
import pprint
import re
import itertools

# create a class to hold the ingredient data
class Ingredient:
    def __init__(self, nam, cap, dur, fla, tex, cal):
        self.name = nam
        self.capacity = cap
        self.durability = dur
        self.flavor = fla
        self.texture = tex
        self.calories = cal

    def __str__(self):
        return name


filename = sys.argv[1]

with open(filename, 'r') as inputFile:
    lines = inputFile.readlines()

#Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
#Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

#Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
#Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
#Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
#Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8
ruleExpr = re.compile('(?P<name>.+): .+ (?P<capacity>-?\d+), .+ (?P<durability>-?\d+), .+ (?P<flavor>-?\d+), .+ (?P<texture>-?\d+), .+ (?P<calories>\d+)')

# create the ingredients
ingredients = {}
for line in lines:
    match = ruleExpr.match(line)
    if match:
        name = match.group('name')
        capacity = int(match.group('capacity'))
        durability = int(match.group('durability'))
        flavor = int(match.group('flavor'))
        texture = int(match.group('texture'))
        calories = int(match.group('calories'))
        ingredients[name] = Ingredient(name, capacity, durability, flavor, texture, calories)

sugar = ingredients['Sugar']
sprinkles = ingredients['Sprinkles']
candy = ingredients['Candy']
chocolate = ingredients['Chocolate']

recipe = {}

def countCalories(tSugar, tSprinkles, tCandy, tChocolate):
    calories = tSugar * sugar.calories + tSprinkles * sprinkles.calories + tCandy * candy.calories + tChocolate * chocolate.calories
    return calories

def evaluateRecipe(tSugar, tSprinkles, tCandy, tChocolate):
    global recipe
    global sugar, sprinkles, candy, chocolate

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
maxScore = 0
for su in range(0, limit + 1):
    for sp in range(0, limit - su + 1):
        for ca in range(0, limit - (su + sp) + 1):
            ch = limit - su - sp - ca
            score = evaluateRecipe(su, sp, ca, ch)
            calories = countCalories(su, sp, ca, ch)
            # print su, sp, ca, ch, score
            if (calories == 500) and (score > maxScore):
                maxScore = score

print maxScore


'''
def evaluateRecipe(tButter, tCinn):
    global recipe

    butter = ingredients['Butterscotch']
    cinn = ingredients['Cinnamon']
    capacity = tButter * butter.capacity + tCinn * cinn.capacity
    durability = tButter * butter.durability + tCinn * cinn.durability
    flavor = tButter * butter.flavor + tCinn * cinn.flavor
    texture = tButter * butter.texture + tCinn * cinn.texture
    if capacity < 0: capacity = 0
    if durability < 0: durability = 0
    if flavor < 0: flavor = 0
    if texture < 0: texture = 0
    score = capacity * durability * flavor * texture
    return score

maxScore = 0
for butter in range(0, 100+1):
    cinn = 100 - butter
    score = evaluateRecipe(butter, cinn)
    print butter, cinn, score
    if score > maxScore:
        maxScore = score

print 
'''