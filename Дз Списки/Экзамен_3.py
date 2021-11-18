import random

n = int(input())
m = int(input())
b = n + m
o = 0
p = 0
u = 0
r = 0
for i in range(7):
    v = random.randint(1, 20)
    c = random.randint(1, 20)
    z = c + v
    print(v,c)
    if i == 4:
        u = v
        r = c
    if b > z:
        o += 1
    if b < z:
        p += 1
print(o, p)
if p >= 4:
    print(u,r)
