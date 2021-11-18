n = int(input('Введите конечное значение диапазона:'))
c = 1
for i in range(1, n - 1):
    v = i + 1
    z = i + 1 + i
    m = i + 1 + i + i + 1
    l = (i + 1 + i) + (i + 1 + i) + (1 + i)
    b = (i + 1 + i) + (i + 1 + i) + (1 + i) + (i + 1 + i) + (1 + i)
    print(c, i, v, z, m, l)
