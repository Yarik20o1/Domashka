# m = int(input("Введите число:"))
# for i in range(1, m):
#    if i!=(6,11) and i!=(15,25) and i!=(32,39):
#        print(i)
m = int(input("Введите числ:"))
if 5 <= m <= 11:
    for i in range(5):
        i = 1 + i
        print(i)
if 14 < m <= 25:
    for i in range(5):
        i = 1 + i
        print(i)
    for i in range(11, 14):
        i = 1 + i
        print(i)
if 11 < m <= 14:
    for i in range(5):
        i = 1 + i
        print(i)
    for i in range(11, m):
        i = 1 + i
        print(i)
if 25 < m <= 31:
    for i in range(5):
        i = 1 + i
        print(i)
    for i in range(11, 14):
        i = 1 + i
        print(i)
    for i in range(25, m):
        i = 1 + i
        print(i)
if 31 < m <= 39:
    for i in range(5):
        i = 1 + i
        print(i)
    for i in range(11, 14):
        i = 1 + i
        print(i)
    for i in range(25, 31):
        i = 1 + i
        print(i)
if m > 39:
    for i in range(5):
        i = 1 + i
        print(i)
    for i in range(11, 14):
        i = 1 + i
        print(i)
    for i in range(25, 31):
        i = 1 + i
        print(i)
    for i in range(40,m+1):
        print(i)

# for i in range(1, 6):
#   print(i)
# for i in range(12, 15):
#   print(i)
# if 26 < m <= 39:
#   for i in range(26, 32):
#      print(i)
# for i in range(40, m):
#   print(i)
