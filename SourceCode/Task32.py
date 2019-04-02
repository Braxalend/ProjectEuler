# -*- coding: utf-8 -*-
"""
Пан-цифровые произведения
Каждое n-значное число, которое содержит каждую цифру от 1 до n ровно один раз, будем считать пан-цифровым; к примеру,
5-значное число 15234 является пан-цифровым, т.к. содержит цифры от 1 до 5.

Произведение 7254 является необычным, поскольку равенство 39 × 186 = 7254, состоящее из множимого, множителя и
произведения является пан-цифровым, т.е. содержит цифры от 1 до 9.

Найдите сумму всех пан-цифровых произведений, для которых равенство "множимое × множитель = произведение" можно
записать цифрами от 1 до 9, используя каждую цифру только один раз.

ПОДСКАЗКА: Некоторые произведения можно получить несколькими способами, поэтому убедитесь, что включили
их в сумму лишь единожды.
"""
from itertools import permutations as prms

p = list(prms('123456789'))
res = []
for j in range(1,3):
    for i in p:
        m1 = (int(''.join(map(str, i[:j]))))
        m2 = (int(''.join(map(str, i[j:5]))))
        mul = (int(''.join(map(str, i[5:]))))
        if m1 * m2 == mul:
            res += [mul]

print(sum(set(res)))
