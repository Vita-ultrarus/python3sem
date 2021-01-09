# coding: utf-8
# license: GPLv3
from random import choice, randint
from enemies import *
from hero import *


class Artifact():

    def use_artifact(self, want, hero):
        if want in hero._artifacts:
            want().use_want


class apple(Artifact):

    def __init__(self):
        self.name = 'яблоко'

    def use_apple(self):
        hero.health += hero.finish_health


class marker(Artifact):

    def __init__(self):
        self.name = 'маркер'

    def use_marker(self):
        print('На какой цвет вы хотите поменять цвет дракона (зелёный/красный/чёрный)?')
        dragon._color = input()


class shield(Artifact):

    def __init__(self):
        self.name = 'щит'

    def use_shield(self):
        if dragon.check_answer(answer) == False:
            print('А я ничего не потеряю!!')
            hero.health += 10
        if troll.check_answer(answer) == False:
            print('А я ничего не потеряю!!')
            hero.health += 20

artifact_types = [apple, marker, shield]
