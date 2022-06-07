# написать функцию которая принимает число, возвращает его значение умноженное на 2
multiplied = lambda n: n * 2
print(multiplied(6))

#  написать функцию которая определяет параметр на четность. Если четное чило, то принтим Yes
# если нет то принтим NO
even_odd = lambda n: "YES" if n % 2 == 0 else "NO"
print(even_odd(7))
print(even_odd(12))

# пишем функцию принимающую 2 аргумента.После чего проверим если первое число больше 10 принтим ДА, если меньше НЕТ
two_arguments = lambda a, b: "ДА" if a > 10 else "НЕТ"
print(two_arguments(11,4))
print(two_arguments(9,4))

# Написать лямбда функцию, которая делит нацело(//) два аргумента.
devision = lambda a, b : a // b
print(devision(15,4))


multiply_2 = lambda q: q * 2
even = lambda q: 'yes' if q % 2 == 0 else 'not'
over_10 = lambda a, b: 'да' if a > b else 'нет'
divides_modulo = lambda a, b: a % b

for i in range(9, 12):
    print('number =', i)
    print('even', even(i), end='; ')
    print('multiply * 2 =', multiply_2(i), end='; ')
    print('over_10 =', over_10(i, 10), end='; ')
    print('divides_modulo =', divides_modulo(i, 3))