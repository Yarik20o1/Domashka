n = input('Введите строку:')
v=0
for i in range(len(n)-1):
    j = n[i] + n[i+1]
    if j.isupper() or j.islower():
        v+=1
print(v)


