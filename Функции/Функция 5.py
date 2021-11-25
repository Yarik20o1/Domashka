def proverka(m):
    n='бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
    c='ауоыиэяюёеАУОЫИЭЯЮЁЕ'
    a=0
    s=0
    for i in m:
        if i in n:
            a+=1
    for i in m:
        if i in c:
            s+=1
    return f'Количество гласных букв равно {s},Количество согласных букв равно {a}'
print(proverka(input()))