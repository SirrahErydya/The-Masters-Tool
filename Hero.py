"""
Wrapper class for a DSA hero formatted a xml-file by Helden-Software
:author: Fenja Kollasch
:date: 2018/09/13
"""
import xml.etree.ElementTree as tree


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


    @staticmethod
    def __get_skill_dict(tree):
        skill_dict = {}
        for child in tree:
            skill = [ child.get('probe'), child.get('value')]
            skill_dict[child.get('name')] = skill
        return skill_dict
