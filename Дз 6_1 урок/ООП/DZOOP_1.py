# 1.Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.
# CODE:
class One:
    def __init__(self, b):
        self.b = b

    def int(self):
        z = 0
        a = 0
        if self.b.isdigit():
            c = int(self.b)
            while c > 0:
                v = c % 10
                if v % 2 == 0:
                    z += v
                a += 1
                c = c // 10
        if z * a > 0:
            return z * a

    def str(self):
        if self.b.isalpha():
            c = str(self.b)
            n = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
            a = 0
            s = 0
            q = ''
            w = ''
            for i in c:
                if i in n:
                    a += 1
                    q += i
                else:
                    s += 1
                    w += i
            if a * s <= len(c):
                return w
            else:
                return q


object = One(input('Введите число\строку: '))
print(object.int())
print(object.str())
