import human


class dog:
    legs = 4
    had = 1
    voice = 'uff'

    def __init__(self, color, size, name, breed):
        self.color = color
        self.size = size
        self.name = name
        self.breed = breed

    def events(self):
        print(self.name, 'Jump')
        print(self.name, self.voice)


bobik = dog('Серый', "Большой", "Бобик", "Хаски-Икея")
print(bobik.voice)
bobik.events()

bobik2 = dog('Черный', "Большой", "Миша", "Хаски-Икея")
bobik2.events()

bobik3 = dog('Черный', "Большой", "Дина", "Хаски-Икея")
bobik3.voice = 'gaff'
bobik3.events()

man = human.Human()
man.eat()
s = man.sweat()
print(s.replace('пота', 'счастья'))
