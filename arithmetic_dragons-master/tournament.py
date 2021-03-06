# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *
from artifacts import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    health_start=hero._health
    for dragon in dragon_list:
        print('Вышел', dragon._color, 'дракон!')
        if hero._artifacts != []:
            print('Хотите использовать артефакт (да/нет)?')
            ans=input()
        else:
            ans='нет'
        if ans == 'да':
            print('Какой артефакт хотите использовать? ', *hero._artifacts)
            want = input()

        while dragon.is_alive() and hero.is_alive():

            if ans == 'да':
                Artifact().use_artifact(want, hero)

            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** дракон кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive():
            break
        hero.finish_health = hero._health - health_start
        print('Дракон', dragon._color, 'повержен!\n')
        artifact = Enemy().monster_gives_artifact(hero)
        if artifact:
            print('Поздравляем, вы получили артефакт: ', artifact, '!')
        hero._experience+=10

    if hero.is_alive():

        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)

    else:
        print('К сожалению, Вы проиграли...')

def game_trollnament(hero, troll_list):

    health_start = hero._health

    for troll in troll_list:
        print('Вышел', troll._color, 'тролль!')
        if hero._artifacts != []:
            print('Хотите использовать артефакт (да/нет)?')
            ans=input()
        else:
            ans='нет'
        if ans == 'да':
            print('Какой артефакт хотите использовать? ', *hero._artifacts)
            want = input()

        while troll.is_alive() and hero.is_alive():
            if ans == 'да':
                Artifact().use_artifact(want, hero)

            print('Вопрос:', troll.question())
            answer = input('Ответ:')

            if troll.check_answer(answer):
                hero.attack(troll)
                print('Верно! \n** троллю неприятно **')
            else:
                troll.attack(hero)
                print('Ошибка! \n** от вас откусили кусочек... **')
        if troll.is_alive():
            break
        hero.finish_health = hero._health - health_start
        print('Тролль', troll._color, 'затроллен!\n')
        artifact = Enemy().monster_gives_artifact(hero)
        if artifact:
            print('Поздравляем, вы получили артефакт: ', artifact, '!' )
        hero._experience+=20

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вас сожрали...')

def rod_dragon(number):
    if number%100 in [11,12,13,14]:return 'драконов'
    if number%10 in [2,3,4]:return 'дракона'
    if number%10==1:return 'дракон'
    else:return 'драконов'

def rod_troll(number):
    if number%100 in [11,12,13,14]:return 'троллей'
    if number%10 in [2,3,4]:return 'тролля'
    if number%10==1:return 'тролль'
    else:return 'троллей'

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())
        if randint(1,2)==1:
            dragon_number = randint(2,15)
            dragon_list = generate_dragon_list(dragon_number)
            print('У Вас на пути', dragon_number, rod_dragon(dragon_number)+'!')
            game_tournament(hero, dragon_list)
        else:
            troll_number = randint(2,15)
            troll_list = generate_troll_list(troll_number)
            print('Вам не дают пройти', troll_number, rod_troll(troll_number)+'!')
            game_trollnament(hero, troll_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')

start_game()