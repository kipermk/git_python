class Human:
    default_name = 'Name'
    default_age = 33

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"""        name: {self.name} 
        age: {self.age} 
        money: {self.__money} 
        house: {self.__house} """)

    @staticmethod
    def default_info():
        print(f'default name: {Human.default_name}')
        print(f'default age: {Human.default_age}')

    def earn_money(self, how_much):
        self.__money += how_much
        print(f'{self.name} has earned {self.__money} $')

    def __make_deal(self, price, house):
        self.__money -= price
        self.__house = house
        print(f'You has bought the {self.__house}, now your money = {self.__money} $')

    def buy_house(self, discount, house):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(price, house)
            print('House is bought')
        else:
            print(f'You\'ve got {self.__money} only, house is {price}')


class House:
    def __init__(self, area=5, price=500000):
        self._area = area
        self._price = price

    def final_price(self, discount):
        self._price -= discount
        print(f'Final price with special discount: {self._price}')
        return self._price


class SmallHouse(House):
    def __init__(self, price=100000):
        House.__init__(self, area=40, price=price)


Human.default_info()
alex = Human(name='alex', age=24)
alex.info()
alex.earn_money(100000)
alex.info()
sh = SmallHouse()
alex.buy_house(10, sh)
