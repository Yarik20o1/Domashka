x = int(input("Введите сторону x конверта:"))
y = int(input("Введите сторону y конверта:"))
x_1 = int(input("Введите сторону x бумаги:"))
y_1 = int(input("Введите сторону y бумаги:"))
if (x >= x_1 and y >= y_1) or (y >= x_1 and x >= y_1):
    print('Да')
else:
    print('Нет')
