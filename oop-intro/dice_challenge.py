#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Creating a simple dice program utilizing classes."""

# imports from cheadice.py (this is in the local directory)
from cheatdice_challenge import Player
from cheatdice_challenge import Cheat_Swapper_II
from cheatdice_challenge import Cheat_Swapper_III
from cheatdice_challenge import Cheat_Swapper_IV
from cheatdice_challenge import Cheat_Loaded_Dice

def main():
    """run-time code"""

    # create two cheater objects
    #cheater1 = Cheat_Swapper_II() # ability is to change randown dice roll to 6
    cheater1 = Cheat_Swapper_III() # ability is to change dices to 6
    #cheater2 = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6
    cheater2 = Cheat_Swapper_IV()  # increase all rolls by x2 with max value 6


    # both players take turns
    cheater1.roll()
    cheater2.roll()

    # both players use their cheat methods
    cheater1.cheat()
    cheater2.cheat()

    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")

    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
        print("Draw!")

    elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
        print("Cheater 1 wins!")

    else:
        print("Cheater 2 wins!")

if __name__ == "__main__":
    main()
