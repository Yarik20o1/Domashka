a = int(input('Введите число'))
b = int(input('Введите число'))
for i in range(a, b + 1):
    if i < 10 and i != 1:
        if b <= 10 and i == 1 or i == 4 or i == 6 or i == 8 or i == 9:
            continue
        print(i)
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i == 1:
        continue
    print(i)
#выполнил