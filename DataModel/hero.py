from DataModel.skill import Skill
import random


class Hero:
    '''mental'''
    strength = Skill()
    defence = Skill()
    perception = Skill()
    agility = Skill()

    power = Skill()
    reanimate = Skill()
    voodoo = Skill()
    love = Skill()

    skills = [strength, defence, perception, agility, power, reanimate, voodoo, love]

    learning = 0

    def __init__(self, max=0, learning=0):
        self.train(max)
        self.learning = learning
        return


    def train(self, max):

        i = 0
        while i < 8:
            gen = random.randint(0, max)
            self.skills[i].train(gen)
            max -= gen
            i += 1

        return
