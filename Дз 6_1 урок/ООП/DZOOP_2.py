# 2.1.Необходимо реализовать модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
# 2.2.Создать двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.
# Условие:
# Поход на работу сытость [-5,-3]
#                 деньги [+5,+10]
# Поход в магазин сытость [-3,-1]
#                   еда [+5,+10]
# Играть деньги[-10,+15]
#        сытость [-4,-2]
# Есть сытость[+2,+7]
#     еда[-4,-1]
# Любое действие +1 день
import random


class House:
    seif = 100
    holodos = 100
    dni = 0
    sitost = 100

    def __init__(self):
        pass

    def est(self):
        House.sitost += random.randint(2, 7)
        House.holodos += random.randint(-4, -1)
        House.dni += 1
        return f'Сытость={House.sitost},Количество еды={House.holodos},Деньги={House.seif},Прожито дней={House.dni}'

    def rabota(self):
        House.sitost += random.randint(-5, -3)
        House.seif += random.randint(5, 10)
        House.dni += 1
        return f'Сытость={House.sitost},Количество еды={House.holodos},Деньги={House.seif},Прожито дней={House.dni}'

    def game(self):
        House.sitost += random.randint(-4, -2)
        House.seif += random.randint(-10, 15)
        House.dni += 1
        return f'Сытость={House.sitost},Количество еды={House.holodos},Деньги={House.seif},Прожито дней={House.dni}'

    def shop(self):
        House.sitost += random.randint(-3, -1)
        House.holodos += random.randint(5, 10)
        House.dni += 1
        return f'Сытость={House.sitost},Количество еды={House.holodos},Деньги={House.seif},Прожито дней={House.dni}'


object = House()
while True:
    print('Введите номер команды: \n'
          ' есть(1), работать(2), играть(3), ходить в магазин(4)')
    x = input()
    if x == '1':
        if House.holodos <= 0:
            print("У вас закончились продукты!")
        else:
            print('ВЫ ПОКУШАЛИ!')
            print(object.est())
    if x == '2':
        print('ВЫ СХОДИЛИ НА РАБОТУ!')
        print(object.rabota())
    if x == '3':
        if House.seif <= 0:
            print("У вас закончились деньги!")
        else:
            print('ВЫ ПОИГРАЛИ В КАЗИНО!')
            print(object.game())
    if x == '4':
        print('ВЫ СХОДИЛИ В МАШАЗИН!')
        print(object.shop())
    if House.sitost < 0:
        print('Вы проиграли!Ваша сытость упала ниже нуля')
        break
    elif House.dni==365:
        print('Вы выиграли!')
        break
