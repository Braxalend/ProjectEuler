#-*- coding: utf-8 -*-
"""
Сумма цифр степени
2**15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 2**1000?
"""

print(sum([int(i) for i in str(2**1000)]))

#or

print(sum(map(int, str(2 ** 1000))))

#or

s=0
for i in str(2**1000):
    s+=int(i)
print(s)