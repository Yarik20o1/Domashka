n = input('Введите строку:')
v = n.split()
print(v)
r=''
for i in v:
    if i.isdigit():
        c=str(i)
        r=c
        print(r,end=' ')

