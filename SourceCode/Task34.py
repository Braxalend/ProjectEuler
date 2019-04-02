# -*- coding: utf-8 -*-
"""
145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.
Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.
Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.
"""

from math import factorial

s = [i for i in range(3,factorial(9)+1)]
res = []
for i in s:
    t = []
    for j in str(i):
        t += [factorial(int(j))]
        if i == sum(t):
            res += [i]
print(sum(res))

#or one line

print(sum(i for i in range(3, factorial(9)+1) if i == sum(factorial(int(j)) for j in str(i))))