# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.


class Str_Int:
    def fun_check(self, a): # первый метод
        if a.isalpha():
            glas = soglas = ''
            for i in a:
                if i in 'aouyei':
                    glas += i
                else:
                    soglas += i
            if len(glas) * len(soglas) <= self.func_len(a):
                return glas
            return soglas
        elif a.isdigit():
            summa = sum(int(i) for i in a if i in '2468') # сумма чётных цифр
            return self.func_len(a) * summa # вызов второго метода и умножение на сумму

    def func_len(self, a): # второй метод
        return len(a)


str_ = input()
object_Str_Int = Str_Int() # создание объекта на основании класса
rezulitat = object_Str_Int.fun_check(str_) # вызов первого метода
print(rezulitat)