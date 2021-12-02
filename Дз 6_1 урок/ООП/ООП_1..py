class Example:
    stat1 = 1
    stat2 = 2
    def __init__(self):
        self.din1=3
        self.din2=4
    def one(self):
        num1=5
        print(num1)
    def two(self):
        num2=Example.stat1+Example.stat2
        print(num2)
    def three(self):
        num3=(self.din1)**self.din2
        print(num3)
num=Example()
num.one()
num.two()
num.three()
