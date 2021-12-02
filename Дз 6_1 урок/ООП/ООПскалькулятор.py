class Culc:
    def __init__(self, c, v):
        self.c = c
        self.v = v

    def raznica(self):
        return self.c - self.v

    def summa(self):
        return self.c + self.v

    def umnozh(self):
        return self.c * self.v

    def delenie(self):
        return self.c // self.v


object = Culc(int(input('Введите c:')), int(input('Введите v:')))
print(object.raznica())
print(object.summa())
print(object.umnozh())
print(object.delenie())
