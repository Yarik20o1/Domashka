a = (2, 4, 5, 7, 6, 8, 7, 6, 5, 4, 6, 54, 67, 45, 6, 3)
b = (5, 7, 6, 4, 32, 2, 5, 6, 76, 8, 5, 865)
c = 1
x = 1
z = sum(a)
y = sum(b)
for i in a:
    c *= i
for i in b:
    x *= i
print(c * x)
print(a.index(min(a)))
