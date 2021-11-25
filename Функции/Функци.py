def raznica(c):
    v=0
    while c>0:
        c=c//10
        v+=1

    return v
print(raznica(int(input())))