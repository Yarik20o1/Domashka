import random


def mass(n, m):
    a = []
    for i in range(10):
        a.append(random.randint(n, m))
    print(a)


n = int(input())
m = int(input())
while n > m:
    if n > m:
        m = int(input())
    else:
        break
mass(n, m)
