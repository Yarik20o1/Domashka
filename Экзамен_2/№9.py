c = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1]
x = [1, 1, 1, 1, 1, 1, 5, 6, 56, 4, 565, 754, 46, 3, 5, 5, 5, ]
count = 0
for i in c:
    if i in x:
        count += 1
print(count)
