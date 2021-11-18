# В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
# баллов и посчитать средний балл по классy
try:
    with open('input.txt', 'r', encoding='utf8') as f:
        line = True
        q=0
        l=0
        while line:
            line = f.readline()
            n = line
            s = n.split()
            z = int(s[2])
            l+=1
            q+=z
            if z <= 3:
                print(n)
    print(q/l)
except IndexError:
    print(f'Средний бал по классу = {q/l}')
