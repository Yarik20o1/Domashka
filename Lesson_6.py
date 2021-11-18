n = 'Геннадий ttdababmt@gmail.com 169'
s = n.split()
v = 0
z=0
if s[0].isalpha():
    z+=1
else:
    with open('registrations_bad.log.txt', 'a') as f:  # mode (режим): запись символьная, кодировка по умолчанию utf8
        file_content = n
        f.write(file_content)

if '.' in s[1]:
    z+=0.5
else:
    with open('registrations_bad.log.txt', 'a') as f:  # mode (режим): запись символьная, кодировка по умолчанию utf8
        file_content = n
        f.write(file_content)
if '@' in s[1]:
    z+=0.5
else:
    with open('registrations_bad.log.txt', 'a') as f:  # mode (режим): запись символьная, кодировка по умолчанию utf8
        file_content = n
        f.write(file_content)
if s[2].isdigit():
    v = int(s[2])
    if 10 <= v <= 99:
        z+=1
    if v>=100:
        with open('registrations_bad.log.txt', 'a') as f:  # mode (режим): запись символьная, кодировка по умолчанию utf8
            file_content = n
            f.write(file_content)
if z==3:
    with open('registrations_good.log.txt.log.txt', 'a') as f:  # mode (режим): запись символьная, кодировка по умолчанию utf8
        file_content = n
        f.write(file_content)
print(s)
