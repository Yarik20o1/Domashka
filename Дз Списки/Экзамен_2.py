glas = ['а', 'е', 'у', 'я', 'и', 'э', 'о', 'ё', 'ю', 'ы']
soglas = ['й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'ч', 'с', 'м', 'т', 'б', 'ъ',
          'ь']
p = 0
o = 0
n = input('Введите строку:')
for i in n:
    if i in glas:
        p += 1
for i in n:
    if i in soglas:
        o += 1

print(p)
print(o)
if p==o:
    print(soglas)