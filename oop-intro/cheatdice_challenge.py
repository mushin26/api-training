#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Player - Class model
   Cheat_Swapper(Player) - Subclass model
   Cheat_Loaded_Dice(Player) - Subclass model"""

# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(5):  # make 5 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    def get_dice(self): # returns the dice rolls
        return self.dice

# allows user to turn their last roll into a 6
class Cheat_Swapper(Player):  # inheritance of Player
    def cheat(self):
        self.dice[-1] = 6

# allows user to turn randown position into a 6
class Cheat_Swapper_II(Player):  # inheritance of Player
    def cheat(self):
        self.dice[randint(0,4)] = 6

# allows user to turn all positions into a 6
class Cheat_Swapper_III(Player):  # inheritance of Player
    def cheat(self):
        for i in range(len(self.dice)):
            self.dice[i] = 6

# allows user to increase all rolls if they were less than a 6
class Cheat_Loaded_Dice(Player): # inheritance of Player
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1

# allows user to duplicate all rolls with max 6
class Cheat_Swapper_IV(Player): # inheritance of Player
    def cheat(self):
        for i in range(len(self.dice)):
            if self.dice[i] in [4,5,6]:
                self.dice[i] = 6
            elif self.dice[i] in [1,2,3]:
                self.dice[i]  *= 2
