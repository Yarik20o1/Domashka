import math

n = input("Введите фигуру:")


def kruf(r):
    return (math.pi) * (r ** 2)


def prymo(c, v):
    return c * v


def treyg(c, v):
    return (1 // 2) * c * v


if n == 'круг':
    print(kruf(int(input('Введите радиус:'))))
if n == 'прямоугольник':
    print(prymo(int(input())), (int(input())))
if n == 'треуголник':
    print(treyg(int(input())), (int(input())))
