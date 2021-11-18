x = 0
y = 0
x1 = 0
while True:
    print('Выберите каким ведром желаете воспользоваться(Для выбора введите 5 или 3)')
    n = int(input('Введите каким ведром будите пользоваться:'))
    if n == 0:
        print('До свидание!')
        break
    if n == 5:
        m = input('Введите команду(Наполнить,Вылить,Перелить):')
        if m == '0':
            x1 = +1
        if m == 'Наполнить' and x < 5:
            x = 5
            print([x, y])
        if m == 'Вылить' and x > 0:
            x = 0
            print([x, y])
        if m == 'Перелить':
            if y == 3:
                x = x
                y = y
                print([x, y])
            if y == 0 and 3 <= x:
                x = x - 3
                y = 3
                print([x, y])
            if y == 0 and x <= 2:
                y = x
                x = x - x
            if y == 1 and x <= 2:
                y = x + y
                x = 0
                print([x, y])
            if y == 1 and 3 <= x:
                x = x - (3 - y)
                y = 3
                print([x, y])
            if y == 2 and x <= 1:
                y = y + x
                x = x - x
                print([x, y])
            if y == 2 and x >= 2:
                y = 3
                x = x - 1
                print([x, y])
    if n == 3:
        m = input('Введите команду(Наполнить,Вылить,Перелить):')
        if m == 'Наполнить' and y < 3:
            y = 3
            print([x, y])
        if m == 'Вылить' and y > 0:
            y = 0
            print([x, y])
        if m == 'Перелить':
            if x == 1 or x == 2 or x == 0 or (x == 3 and y <= 2):
                x = y + x
                y = y - y
                print([x, y])
            if x == 3 and y == 3:
                x = 5
                y = 1
                print([x, y])
            if x == 5:
                x = 5
                y = y
                print([x, y])

    if x1 == 1:
        print('До свидание!')
        break
    if x == 4:
        print('Вы выиграли!')
        break
