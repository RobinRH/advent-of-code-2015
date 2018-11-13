# 201
# get the max cost and you still lose
# boss:
# Hit Points: 103
# Damage: 9
# Armor: 2
# https://adventofcode.com/2015/day/21

import sys
import pprint

class Player:

    def __init__(self, n, d, a, h):
        self.name = n
        self.damage = d
        self.armor = a
        self.hitpoints = h

    def __repr__(self):
        return self.name

class Item:

    def __init__(self, n, c, d, a):
        self.name = n
        self.cost = c
        self.damage = d
        self.armor = a

    def __repr__(self):
        return self.name + ": " + str(self.cost) + "," + str(self.damage) + "," + str(self.armor)

# The player (you) and the enemy (the boss) take turns attacking.
# The player always goes first. Each attack reduces the opponent's hit points by at least 1.
# The first character at or below 0 hit points loses.
# Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score.
# An attacker always does at least 1 damage. 
# So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points. 
# If the defender had an armor score of 300, the defender would still lose 1 hit point.

def runGame(you, boss):

    while True:
        # you go

        damage = you.damage - boss.armor
        if damage <= 1:
            damage = 1

        boss.hitpoints -= damage

        if boss.hitpoints <= 0:
            return you

        # boss goes
        damage = boss.damage - you.armor
        if damage <= 1:
            damage = 1

        you.hitpoints -= damage

        if you.hitpoints <= 0:
            return boss

        #print you.hitpoints, boss.hitpoints

    return you


#Weapons:    Cost  Damage  Armor
weapons = [
    Item("Dagger",      8,     4,       0),
    Item("Shortsword", 10,     5,       0),
    Item("Warhammer",  25,     6,       0),
    Item("Longsword",  40,     7,       0),
    Item("Greataxe",   74,     8,       0)
]

pprint.pprint(weapons)

#Armor:      Cost  Damage  Armor
armor = [
    Item("Leather",     13,     0,       1),
    Item("Chainmail",   31,     0,       2),
    Item("Splintmail",  53,     0,       3),
    Item("Bandedmail",  75,     0,       4),
    Item("Platemail",   102,    0,       5),
    Item("None",        0,      0,       0)
]
pprint.pprint(armor)

#Rings:      Cost  Damage  Armor
rings = [
    Item("Damage +1",   25,     1,       0),
    Item("Damage +2",   50,     2,       0),
    Item("Damage +3",   100,    3,       0),
    Item("Defense +1",  20,     0,       1),
    Item("Defense +2",  40,     0,       2),
    Item("Defense +3",  80,     0,       3)
]
pprint.pprint(rings)

boss = Player('boss', 9, 2, 103)
print boss

maxCost = 0
myhitpoints = 100
# 1 weapon, 0 or 1 armor, 0 or 1 or 2 rings
# can't buy duplicates

for w in weapons:
    for a in armor:
        # choose no rings
        cost = w.cost + a.cost
        you = Player('you', w.damage + a.damage, w.armor + a.armor, myhitpoints)
        boss = Player('boss', 9, 2, 103)
        winner = runGame(you, boss)
        if (winner is boss) and (cost > maxCost):
            maxCost = cost
            print winner.name, cost

        # choose one ring
        for r in rings:
            cost = w.cost + a.cost + r.cost
            you = Player('you', w.damage + a.damage + r.damage, w.armor + a.armor + r.armor, myhitpoints)
            boss = Player('boss', 9, 2, 103)
            winner = runGame(you, boss)
            if (winner is boss) and (cost > maxCost):
                maxCost = cost
                print winner.name, cost


        # choose two rings
        for r1 in range(0, len(rings)):
            for r2 in range(r1 + 1, len(rings)):
                ring1 = rings[r1]
                ring2 = rings[r2]

                cost = w.cost + a.cost + ring1.cost + ring2.cost
                you = Player('you', w.damage + a.damage + ring1.damage + ring2.damage, w.armor + a.armor + ring1.armor + ring2.armor, myhitpoints)
                boss = Player('boss', 9, 2, 103)
                winner = runGame(you, boss)
                if (winner is boss) and (cost > maxCost):
                    maxCost = cost
                    print winner.name, cost

print maxCost

#you = Player('you', 5, 5, 8)
#boss = Player('boss', 7, 2, 12)
#winner = runGame(you, boss)
#print winner.name