import random

n = int(input('Введите кол-во чисел:'))
m = input('Введите искомую цифру:')
b = 0
for i in range(1, n):
    x = random.randint(100, 1000)
    c = str(x)
    print(c)
    if c.count(m):
        b += 1
print(b)