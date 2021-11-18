n=['Иванов','Петрова','Сидоров']
n.reverse()
print(n)
v=[]
for i in n:
    c=str(i[::-1])
    v.append(c)
print(v)