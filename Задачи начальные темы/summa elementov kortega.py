# Дан кортеж чисел. Определите сумму элементов лежащих между максимальным и минимальным числами кортежа.
# (Что делать если повторы так и не определено) 
import random

dlina = int(input('введи максимальную длину кортежа, например, 10 :'))
diap = int(input('введи число больше или равно длине кортежа для определения диапазона значений элементов кортежа, рекомендуется не менее 25 :'))
ktg_1 = list(random.randint(1,diap) for i in range(dlina))
# второй вариант задания кортежа: 
# ktg_1 = (5,2,12,4,17,1,10,4) #внимание, желательно не вводить повторные элементы кортежа
print(tuple (ktg_1))

dlinak  = len (ktg_1)
sumktg1 = 0
maximal = max(ktg_1)
minimal = min(ktg_1)

print('максимальное и минимальное значение:', maximal,',', minimal)
print('их позиции в кортеже:', ktg_1.index(maximal),',', ktg_1.index(minimal))

# вариант с двумя for-ами:
# if ktg_1.index(maximal)> ktg_1.index(minimal):
#     for i in range (ktg_1.index(minimal)+1, ktg_1.index(maximal)):
#         sumktg1 += int(ktg_1[i])
# else:
#     for i in range (ktg_1.index(maximal)+1, ktg_1.index(minimal)):
#         sumktg1 += int(ktg_1[i])

if ktg_1.index(maximal)> ktg_1.index(minimal):
    maximal, minimal = minimal, maximal


for i in range (ktg_1.index(maximal)+1, ktg_1.index(minimal)):
        sumktg1 += int(ktg_1[i])

print('сумма без max и min :', sumktg1)
      