#-*- coding: utf-8 -*-
#2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#Какое самое маленькое число делится нацело на все числа от 1 до 20?
import math
import itertools
import functools

en = 20
lp = [2, 3]
def IsPrime(pc):
    if pc < 2:
        return False
    for number in itertools.islice(itertools.count(2), int(math.sqrt(pc) - 1)):
        if not pc % number:
            return False
    return True

def IsInt(n):
    return int(n) == float(n)

ls = [i for i in range(1,en+1)]
lp.extend([i for i in range(5,en+1) if IsPrime(i)])
n = {j:max([math.log(i,j) for i in ls if IsInt(math.log(i,j))]) for j in lp}
print(functools.reduce(lambda x, y: x*y, [x**y for x, y in zip(n.keys(), n.values())]))

print(ls)
print(lp)
print(n)
