"""
This functions calculate the values of dice rolls in DSA
:author: Fenja Kollasch
:date: 2018/09/13
"""

def roll_attribute(hero, attribute, roll):
    return hero.__getattribute__(attribute) - roll

def roll_skill(hero, skill, roll1, roll2, roll3):
    attributes = hero.get_attributes(skill)
    return attributes[0]-roll1 + attributes[1] - roll2 + attributes[2] - roll3 + hero.__getattribute__(skill)[1]