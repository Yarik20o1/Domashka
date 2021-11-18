m = int(input("Введите первое число:"))
n = int(input("Введите второе число:"))
if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n+1, -1):
        print(i)
