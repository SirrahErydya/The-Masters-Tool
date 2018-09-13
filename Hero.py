"""
Wrapper class for a DSA hero formatted a xml-file by Helden-Software
:author: Fenja Kollasch
:date: 2018/09/13
"""
import xml.etree.ElementTree as tree

attributes = { 'MU':'courage', 'KL':'smarts', 'IN':'intuition', 'CH':'charisma', 'FF':'dexterity', 'GE':'artifice', 'KO':'constitution', 'KK':'strength'}
class Hero:
    name = ''

    # Attributes
    courage = 0
    smarts = 0
    intuition = 0
    charisma = 0
    dexterity = 0
    artifice = 0
    constitution = 0
    strength = 0
    social_state = 0

    initiative = 0
    pary = 0

    skills = {}

    spells = {}

    # Fighting
    daggers = ()
    batons = ()
    fistfight = ()
    wrestling = ()
    swords = ()

    def __init__(self, xmllink):
        hero = tree.parse(xmllink).getroot().find('held')
        self.name = hero.get('name')
        for child in hero:
            if child.tag == 'eigenschaften':
                self.__get_attributes(child)
            elif child.tag == 'talentliste':
                self.skills = self.__get_skill_dict(child)
            elif child.tag == 'zauberliste':
                self.spells = self.__get_skill_dict(child)
            elif child.tag == 'kampf':
                self.__get_fightatts(child)
            else:
                pass

        self.initiative = (self.courage + self.artifice) / 2
        self.pary = self.artifice / 2



    @staticmethod
    def get_hero_by_name(heroes, name):
        for hero in heroes:
            if hero.name == name:
                return hero

    def roll_attribute(self, attribute, roll, mod):
        return self.__getattribute__(attribute) - roll + mod

    def roll_skill(self, skill, roll1, roll2, roll3, mod):
        attributes = self.__skill_attrs(skill)
        return attributes[0] - roll1 + attributes[1] - roll2 + attributes[2] - roll3 + self.__getattribute__(skill)[
            1] + mod

    def roll_ini(self, roll, mod):
        return self.initiative + roll + mod

    def __get_attributes(self, tree):
        for child in tree:
            if child.get('name') == 'Mut':
                self.courage = child.get('value')
            elif child.get('name') == 'Klugheit':
                self.smarts = child.get('value')
            elif child.get('name') == 'Intuition':
                self.intuition = child.get('value')
            elif child.get('name') == 'Charisma':
                self.charisma = child.get('value')
            elif child.get('name') == 'Fingerfertigkeit':
                self.dexterity = child.get('value')
            elif child.get('name') == 'Gewandtheit':
                self.artifice = child.get('value')
            elif child.get('name') == 'Konstitution':
                self.constitution = child.get('value')
            elif child.get('name') == 'Körperkraft':
                self.strength = child.get('value')
            elif child.get('name') == 'Sozialstatus':
                self.social_state = child.get('value')
            else:
                pass

    def __get_fightatts(self, tree):
        for child in tree:
            attack = child.find('attacke').get('value')
            pary = child.find('parade').get('value')
            if child.get('name') == 'Dolche':
                self.daggers = (attack, pary)
            elif child.get('name') == 'Hiebwaffen':
                self.batons = (attack, pary)
            elif child.get('name') == 'Raufen':
                self.fistfight = (attack, pary)
            elif child.get('name') == 'Ringen':
                self.wrestling = (attack, pary)
            elif child.get('name') == 'Säbel':
                self.swords = (attack, pary)
            else:
                pass

    def __skill_attrs(self, skill):
        attr = self.skills[skill][0]
        return [self.__getattribute__(attributes[attr[0]]), self.__getattribute__(attributes[attr[1]]), self.__getattribute__(attributes[attr[2]])]

    @staticmethod
    def __get_skill_dict(tree):
        skill_dict = {}
        for child in tree:
            probe = ''.join(child.get('probe').split())
            skill = [ probe[1:-1].split('/'), child.get('value')]
            skill_dict[child.get('name')] = skill
        return skill_dict
