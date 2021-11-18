a = [1, -1, 2, 3, 5, -8, 13, 21, -34, 56, 89]
n = len(a)

for i in range(n):
    if a[i] < 0 and a[i] % 2 == 0:
        print(a[i])
