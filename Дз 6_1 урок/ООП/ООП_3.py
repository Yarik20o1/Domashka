class Human:
    default_name = 1
    default_age = 2

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__house = 3
        self.__money = 4

    def info(self):
        print(self.name, self.age, self.__house, self.__money)

    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_age)

    def earn_money(self):
        self.__money += 1


if __name__ == '__main__':
    Human.default_info()
    object = Human()
    object.info()
    object.earn_money()
    object.info()


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, sale):
        self._price = self._price * ((100 - sale) / 100)
        return self._price


object1 = House(100, 100)
print(object1.final_price(10))


class SmallHouse(House):
    def __init__(self, area, price):
        super().__init__(price, area=40)

