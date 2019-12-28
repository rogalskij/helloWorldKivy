from DataModel.skill import Skill
import random


class Hero:

    name = ""
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

    def __init__(self, max=0, learning=0, name="Richard Grey"):
        self.name = name
        self.train(max)
        self.learning = learning
        return

    def train(self, max):
        i = 0
        train = [0, 0, 0, 0, 0, 0, 0, 0]
        while i < max:
            train[random.randint(0, 7)] += 1
            i += 1

        index = 0
        while index < 8:
            self.skills[index].train(train[index])
            index += 1

        return
