n = input("Введите количество рублей:")
k = input("Введите количество копеек:")
a = len(n)
s = len(k)
rub_1 = "рубль"
rub_2 = 'рублей'
rub_3 = 'рубля'
kop_1 = 'копейка'
kop_2 = 'копеек'
kop_3 = 'копейки'
if a == 1:
    if n == '1':
        r = rub_1
    if n == '2' or n == '3' or n == '4':
        r = rub_3
    if n == '5' or n == '6' or n == '7' or n == '8' or n == '9':
        r = rub_2
    if n == '0':
        r = n
else:
    if n[-1] == '0':
        r = rub_2
    if n[-2] + n[-1] == '11' or n[-2] + n[-1] == '12' or n[-2] + n[-1] == '13' or n[-2] + n[-1] == '14':
        r = rub_2
    if n[-2] + n[-1] != '11' and n[-1] == '1':
        r = rub_1
    if n[-2] + n[-1] != '12' and n[-2] + n[-1] != '13' and n[-2] + n[-1] != '14' and n[-1] == '2' or n[-1] == '3' or n[
        -1] == '4':
        r = rub_3
    if n[-1] == '5' or n[-1] == '6' or n[-1] == '7' or n[-1] == '8' or n[-1] == '9':
        r = rub_2
if s == 1:
    if k == '1':
        d = kop_1
    if k == '2' or k == '3' or k == '4':
        d = kop_3
    if k == '5' or k == '6' or k == '7' or k == '8' or k == '9':
        d = kop_2
    if k == '0':
        d = k
else:
    if k[-1] == '0':
        d = kop_2
    if k[-2] + k[-1] == '11' or k[-2] + k[-1] == '12' or k[-2] + k[-1] == '13' or k[-2] + k[-1] == '14':
        d = kop_2
    if k[-2] + k[-1] != '11' and k[-1] == '1':
        d = kop_1
    if k[-2] + k[-1] != '12' and k[-2] + k[-1] != '13' and k[-2] + k[-1] != '14' and k[-1] == '2' or k[-1] == '3' or k[
        -1] == '4':
        d = kop_3
    if k[-1] == '5' or k[-1] == '6' or k[-1] == '7' or k[-1] == '8' or k[-1] == '9':
        d = kop_2
if n == '0' and k != '0':
    print(f'{k} {d}')
if k == '0' and n != '0':
    print(f'{n} {r}')
if n != '0' and k != '0':
    print(f'{n} {r},{k} {d}')
if n == '0' and k == '0':
    print("Попробуйте еще раз")
