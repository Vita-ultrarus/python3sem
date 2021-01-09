# coding: utf-8
# license: GPLv3
from random import choice, randint
from enemies import *
from hero import *


# from tournament import *

# artifact_types=[roller_skates, apple, marker, shield, rebirth, wings]
def monster_gives_artifact(hero):
    artifact = None
    a = randint(1,10)
    if (3 <= a and a <= 6):
        artifact = choice(artifact_types)
        hero._artifacts.append(artifact)
    return artifact


def use_artifact(want, hero):
    if want in hero._artifacts:
        want().want


class Artifact(Hero):

    def _init_(self, name):
        self.cost = None
        self.name = name


class apple(Artifact):

    def __init__(self):
        self.name='яблоко'

    def apple(self):
        hero.health += hero.finish_health


class marker(Artifact):

    def __init__(self):
        self.name='маркер'

    def marker(self):
        print('На какой цвет вы хотите поменять цвет дракона (зелёный/красный/чёрный)?')
        dragon._color = input()


class shield(Artifact):

    def __init__(self):
        self.name='щит'

    def shield(self):
        if dragon.check_answer(answer) == False:
            print('А я ничего не потеряю!!')
            hero.health += 10
        if troll.check_answer(answer) == False:
            print('А я ничего не потеряю!!')
            hero.health += 20

artifact_types = [apple, marker, shield]
