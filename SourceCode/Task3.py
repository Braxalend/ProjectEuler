#-*- coding: utf-8 -*-
"""
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""
import math
import time
import itertools

start_time = time.time()
num = 600851475143
FE = []


def IsPrime(pc):
    if pc < 2:
        return False
    for number in itertools.islice(itertools.count(2), int(math.sqrt(pc) - 1)):
        if not pc % number:
            return False
    #   return pc > 1 and all(pc%i for i in itertools.islice(itertools.count(2), int(math.sqrt(pc)-1)))
    return True

def IsMax(n):
    F = []
    a = 5
    count = 1
    while (count <= math.sqrt(n)):
        b = 0
        if (count <= math.sqrt(a)):
            if (a%count == 0):
                b = 1
        if  ((b != 1) & (n%a == 0)):
            F += [a]
        count += 1
        a += 2
    return F
for i in IsMax(num):
   if IsPrime(i):
       FE += [i]
print(max(FE))
print("--- %s seconds ---" % (time.time() - start_time))