#Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке, образуется следующая спираль 5 на 5:
#
#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13
#
#Можно убедиться, что сумма чисел в диагоналях равна 101.
#
#Какова сумма чисел в диагоналях спирали 1001 на 1001, образованной таким же способом?
import itertools

s = [1]
n = 0
r = [1]
while n < 1001 - 1:
    n += 2
    for i in range(4):
        s += [n]
        r += [sum(s)]

print (sum(r))

print (sum(list(itertools.accumulate(s))))

