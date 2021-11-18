c = ' An apple a day keeps the doctor away'
s={}
x = c.split()
for i in c:
    v=c.count(i)
    s[i]=v
del s[' ']
print(s)
