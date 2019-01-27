# 1216
#[3, 1, 4, 3, 2, 4, 3, 0] 1216
#[3, 4, 1, 3, 2, 4, 3, 0] 1216
#[3, 4, 2, 3, 1, 4, 3, 0] 1216
#[3, 4, 2, 3, 4, 1, 3, 0] 1216
#True [3, 1, 4, 3, 2, 4, 3, 0] 1216
# You, hit points: 50, mana: 500
# Boss, hit Points: 51, Damage: 9
# https://adventofcode.com/2015/day/22

# Magic Missile costs 53 mana. 
# It instantly does 4 damage.

# Drain costs 73 mana. 
# It instantly does 2 damage and heals you for 2 hit points.

# Shield costs 113 mana. 
# Lasts for 6 turns. 
# Armor is increased by 7.

# Poison costs 173 mana. 
# Lasts for 6 turns. 
# It deals the boss 3 damage at the start of each turn.

# Recharge costs 229 mana. 
# Lasts for 5 turns. 
# It gives you 101 new mana at the start of each turn.

import pprint
import itertools

class Player:
    def __init__(self, n, h, m, d, a):
        self.name = n
        self.hitpoints = h
        self.mana = m
        self.damage = d
        self.armor = a

class Spell:
    def __init__(self, sType):
        self.spellType = sType
        self.counter = 0
        if self.spellType == sh:
            self.counter = 6
        elif self.spellType == po:
            self.counter = 6
        elif self.spellType == re:
            self.counter = 5
        else:
            pass


mm = 0
dr = 1
sh = 2
po = 3
re = 4

costs = {
    mm: 53,
    dr: 73,
    sh: 113,
    po: 173,
    re: 229
}

spells = [mm, dr, sh, po, re]

def playGame(you, boss, spells):
    #print "spells: ", spells

    spellsInPlay = []

    def upkeep(spellsInPlay):
        # upkeep
        #print spellsInPlay
        stillInPlay = []
        for s in spellsInPlay:
            if s[0] == sh: # lasts 6 turns, increase armor 7
                if s[1] == 0: # turn it off
                    you.armor -= 7
                else:
                    stillInPlay.append((sh, s[1]-1))
            elif s[0] == po: # last 6 turns, does 3 damage to boss
                if s[1] == 0: # turn if off
                    pass
                else:
                    boss.hitpoints -= 3
                    stillInPlay.append((po, s[1] - 1))
            elif s[0] == re: # lasts 5 turns, give you 101 mana
                if s[1] == 0:
                    pass
                else:
                    you.mana += 101
                    stillInPlay.append((re, s[1] - 1))
        return stillInPlay

    while True:

        # you go
        you.hitpoints -= 1
        spellsInPlay = upkeep(spellsInPlay)
        if you.hitpoints <= 0:
            return boss
        if len(spells) > 0:
            spellToCast = spells[0]
            # You cannot cast a spell that would start an effect which is already active. 
            for s in spellsInPlay:
                if s[0] == spellToCast and s[1] <> 0:
                    return boss # you can't cast this spell
            spells.remove(spellToCast)
            you.mana -= costs[spellToCast]
            if you.mana < 0:
                return boss # not enough mana to cast spell, you lose

            if spellToCast == mm:
                boss.hitpoints -= 4
            elif spellToCast == dr:
                boss.hitpoints -= 2
                you.hitpoints += 2
            elif spellToCast == sh:
                you.armor += 7
                spellsInPlay.append((sh, 6))
            elif spellToCast == po:
                spellsInPlay.append((po, 6))
            else: # re
                spellsInPlay.append((re, 5))
        else:
            #print "ran out of spells"
            return boss

        #print you.name, you.hitpoints, you.mana, you.armor
        #print boss.name, boss.hitpoints, boss.damage
        # and that all you need to do

        # boss goes
        spellsInPlay = upkeep(spellsInPlay)
        
        if you.hitpoints <= 0:
            #print "you lose"
            #print you.name, you.hitpoints, you.mana, you.armor
            #print boss.name, boss.hitpoints, boss.damage
            return boss

        if boss.hitpoints <= 0:
            return you

        damage = boss.damage - you.armor
        if damage <= 1:
            damage = 1

        you.hitpoints -= damage
        if you.hitpoints <= 0:
            "you lose"
            #print you.name, you.hitpoints, you.mana, you.armor
            #print boss.name, boss.hitpoints, boss.damage
            return boss

        #print you.name, you.hitpoints, you.mana, you.armor
        #print boss.name, boss.hitpoints, boss.damage
        #print you.mana, you.hitpoints, boss.hitpoints


def getCost(spellList):
    totalCost = 0
    for s in spellList:
        totalCost += costs[s]
    return totalCost


# test game
#you = Player('you', 10, 250, 0, 0)
#boss = Player('boss', 14, 0, 8, 0)
#winner = playGame(you, boss, [re, sh, dr, po, mm])
#print winner.name, you.mana, you.hitpoints

you = Player('you', 50, 500, 0, 0)
boss = Player('boss', 51, 0, 9, 0)

# try all the games with one spell
spellList = itertools.product(spells, spells, spells, spells, spells, spells, spells, spells)
# True [3, 4, 3, 0, 3, 0] 854
# True [3, 4, 3, 0, 3, 0, 0] 907 - too high
# True [0, 0, 4, 3, 3, 2, 0, 0] 900 - correct
# True [0, 0, 4, 3, 3, 2, 0, 0, 0] 953
won = False
minCost = 10000
minSpellList = []
for sl in spellList:
    you = Player('you', 50, 500, 0, 0)
    boss = Player('boss', 51, 0, 9, 0)
    winner = playGame(you, boss, list(sl))
    #print winner.name
    if winner == you:
        #print "you win", sl
        #print you.name, you.hitpoints, you.mana, you.armor
        #print boss.name, boss.hitpoints, boss.damage        
        won = True
        gameCost = getCost(list(sl))
        print list(sl), gameCost
        if gameCost < minCost:
            minCost = gameCost
            minSpellList = list(sl) 

print won, minSpellList, minCost
