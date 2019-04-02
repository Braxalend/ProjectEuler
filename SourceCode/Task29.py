# -*- coding: utf-8 -*-
"""
Различные степени
Рассмотрим все целочисленные комбинации ab для 2 ≤ a ≤ 5 и 2 ≤ b ≤ 5:

22=4, 23=8, 24=16, 25=32
32=9, 33=27, 34=81, 35=243
42=16, 43=64, 44=256, 45=1024
52=25, 53=125, 54=625, 55=3125
Если их расположить в порядке возрастания, исключив повторения, мы получим следующую последовательность
из 15 различных членов:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

Сколько различных членов имеет последовательность ab для 2 ≤ a ≤ 100 и 2 ≤ b ≤ 100?
"""
arr = []
for i in range(2,101):
    arr += [i ** l for l in range(2,101)]
print(len(set(arr)))


print(len({a**b for a in range(2,101) for b in range(2,101)}))