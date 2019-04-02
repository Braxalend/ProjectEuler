# -*- coding: utf-8 -*-
"""
Дробь 49/98 является любопытной, поскольку неопытный математик, пытаясь сократить ее, будет ошибочно полагать,
что 49/98 = 4/8, являющееся истиной, получено вычеркиванием девяток.
Дроби вида 30/50 = 3/5 будем считать тривиальными примерами.
Существует ровно 4 нетривиальных примера дробей подобного типа, которые меньше единицы и содержат
двухзначные числа как в числителе, так и в знаменателе.
Пусть произведение этих четырех дробей дано в виде несократимой дроби (числитель и знаменатель дроби не имеют
общих сомножителей). Найдите знаменатель этой дроби.
"""

from itertools import combinations

c = list(combinations([i for i in range(10,100) if i%10 != 0], 2))
res = 1
for i in c:
    a, b = list(str(i[0])), list(str(i[1]))
    if  a[1] == b [0]:
        if int(a[0])/int(b[1]) == i[0]/i[1]:
            res *= int(b[1])/int(a[0])
print (res)
