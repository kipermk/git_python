# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.


class Str_Int:
    def __init__(self, str):
        self.str = str

    def fun_check(self): # первый метод
        if self.str.isalpha():
            glas = soglas = ''
            for i in self.str:
                if i in 'aouyei':
                    glas += i
                else:
                    soglas += i
            if len(glas) * len(soglas) <= self.func_len():
                return glas
            return soglas
        elif self.str.isdigit():
            summa = sum(int(i) for i in self.str if i in '2468') # сумма чётных цифр
            return self.func_len() * summa # вызов второго метода и умножение на сумму

    def func_len(self): # второй метод
        return len(self.str)


str_ = input()
object_Str_Int = Str_Int(str_) # создание объекта на основании класса
rezulitat = object_Str_Int.fun_check() # вызов первого метода
print(rezulitat)