#-*- coding: utf-8 -*-
"""
Очки за имена
Используйте names.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'), текстовый файл размером
46 КБ, содержащий более пяти тысяч имен. Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные
значения каждого имени и умножьте это значение на порядковый номер имени в отсортированном списке для получения
количества очков имени.
Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53)
является 938-ым в списке. Поэтому, имя COLIN получает 938 × 53 = 49714 очков.
Какова сумма очков имен в файле?
"""

import re

def NamePoint(n, t):
    ts = 0
    for i in t:
        ts += ord(i) - 64
    p = n*ts
    return p

with open('T022_names.txt','r') as file:
    l = re.findall(r"([A-Z]+)", file.read())

l.sort()
ls = dict(zip(range(1,len(l)+1), l))
s = sum([NamePoint(i, j) for i, j in zip(ls.keys() , ls.values())])
print(s)
file.close()


#or

sl = sorted(open("T022_names.txt").read().replace('"', '').split(","))

res = 0
for i in range(len(sl)):
    res+=(i+1)*sum([ord(char)-64 for char in sl[i]])

print(res)