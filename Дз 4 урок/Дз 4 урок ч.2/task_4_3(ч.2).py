num = int(input('Введите число:'))
for i in range(1, num + 1):
    c = 0
    for j in range(1, num + 1):
        if i % j == 0:
            c += 1
    z = c * '+'
    print(i,z)


# не выполнено
# m = int(input("Введите первое число:"))
# n = str(m)
# for i in range(m):
# i = 1 + i
# c = str(i)
# print(i * c)
