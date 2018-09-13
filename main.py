"""
The main program loop
:author: Fenja Kollasch
:date: 2018/09/13
"""

import Hero as H
import os
import sys


def main():
    print("Welcome to The Master's Tool V1.0!")

    loc = input("Please tell me the location of your hero xml files:")
    heroes = []
    for file in os.listdir(loc):
        heroes.append(H.Hero(file))
    print("The following heros were loaded:")
    for hero in heroes:
        print(hero.name)

    ex = False

    while not ex:
        print("Enter the type of the roll you want to make: Attribute, skill or initiative?")
        print("Type exit if you want to leave.")
        rolltype = input()
        if rolltype.lower() == "exit":
            ex = True
        else:
            res = evaluate_roll(rolltype.lower(), heroes)
            print("{} rolled {} on their probe on {} with a modification of {}".format(res[1], res[2], res[0], res[3]))
            print("Based on your attribute values there are {} quality points left.").format(res[4])
            if res < 0:
                print("You haven't passed the probe.")
            elif res < 4:
                print("You barely passed the probe.")
            elif res < 7:
                print("You passed the probe.")
            elif res < 10:
                print("You passed the probe with bravour.")
            elif res < 16:
                print("You passed the probe with grace.")
            else:
                print("You passed the probe masterfully.")


def evaluate_roll(rolltype, heroes):
    if rolltype == "attribute":
        print("You want to roll for an attribute.")
        roll = input("Enter your roll like this: heroname attributename dicevalue modification")
        roll = roll.split(' ')
        if len(roll) != 4:
            print("I didn't got that. There should've been 4 arguments separated by spaces")
        else:
            hero = H.Hero.get_hero_by_name(heroes, roll[0])
            arg = roll[1]
            dice = int(roll[2])
            mod = int(roll[3])
            try:
                res = hero.roll_attribute(arg, dice, mod)
                return [arg, hero.name, [dice], mod, res]
            except:
                e = sys.exc_info()
                print("Sorry. There was an exception: {}".format_map(e))
                print("You entered: {}".format(roll))
                print("Perhaps there was a typo?")
    elif rolltype == "skill":
        print("You want to roll for a skill or a spell.")
        roll = input("Enter your roll like this: heroname skillname dice1 dice2 dice3 modification")
        roll = roll.split(' ')
        if len(roll) != 6:
            print("I didn't got that. There should've been 6 arguments separated by spaces")
        else:
            hero = H.Hero.get_hero_by_name(heroes, roll[0])
            arg = roll[1]
            dice1 = int(roll[2])
            dice2 = int(roll[3])
            dice3 = int(roll[4])
            mod = int(roll[5])
            try:
                res = hero.roll_skill(arg, dice1, dice2, dice3, mod)
                return [arg, hero.name, [dice1, dice2, dice3], mod, res]
            except:
                e = sys.exc_info()
                print("Sorry. There was an exception: {}".format_map(e))
                print("You entered: {}".format(roll))
                print("Perhaps there was a typo?")
    elif rolltype == "initiative":
        print("You want to roll for your initiative.")
        roll = input("Enter your roll like this: heroname dice modification")
        roll = roll.split(' ')
        if len(roll) != 3:
            print("I didn't got that. There should've been 3 arguments separated by spaces")
        else:
            hero = H.Hero.get_hero_by_name(heroes, roll[0])
            dice = roll[1]
            mod = int(roll[2])
            try:
                res = hero.roll_ini(dice, mod)
                return ["Initiative", hero.name, [dice], mod, res]
            except:
                e = sys.exc_info()
                print("Sorry. There was an exception: {}".format_map(e))
                print("You entered: {}".format(roll))
                print("Perhaps there was a typo?")
    else:
        print("I don't know what you mean. Is there a typo anywhere?")
        return "invalide"