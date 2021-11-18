c = [1, 2, 3, 4, 5, 2, 3, 2]
cou = 0
for i,j in enumerate(c):
    if c.count(j) > 1:
        cou+=1
        del c[i]
        del c[c.index(j)]
print(c)