import random

n = int(input('Введите количество участников'))
m = [input('Введите имена') for i in range(n)]
print(sorted(m))
b = random.randint(1, 6)
x = ['', '', '', '', '', '']
x.insert(b, 'Пуля')
x.pop(b + 1)
v = len(m)
x = 0
while True:
    for j in range(n):
        q1 = int(input(f'{m[j]} Выбирай номер:'))
        if q1 == b + 1:
            print(f'{m[j]}-выбыл/а')
            x = 1
            break
    if x == 1:
        break
