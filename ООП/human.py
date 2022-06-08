import random


class Head:
    eyes = 2
    ears = 2
    mouth = 1

    def eat(self):
        taste = 'вкусно' if random.randint(0, 1) else 'не вкусно'
        print(taste)
        # return taste


class Body:
    heart = 1

    def sweat(self):
        sweat_ml = random.randint(10, 1000)
        print(f'выделилось {sweat_ml} мл пота')
        # return sweat_ml


class Human(Head, Body):
    pass


# nick = Human()
# nick.sweat()
# nick.eat()
# print(nick.eyes)
# print(nick.heart)
