import random

# commet
class Body:
    heart = 1

    def __init__(self, height=180, weight=80, sex='f'):
        self.height = height
        self.weight = weight
        self.sex = sex
        self.children = 0

    def make_children(self, children_number):
        if self.sex == 'f':
            for i in range(children_number):
                self.gain_weight()
                self.children += 1
        else:
            print('You are not women')

    def sweat(self):
        sweat_ml = random.randint(10, 1000)
        print(f'выделилось {sweat_ml} мл пота')

    def gain_weight(self):
        self.weight += random.randint(1, 10)
        print('Вес, ', self.weight)


dude = Body(height=160, weight=60)
print(dude.height)
print(dude.weight)
dude.gain_weight()
dude.make_children(2)
print(dude.children)
