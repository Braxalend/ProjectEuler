#-*- coding: utf-8 -*-
"""
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
Какое число является 10001-ым простым числом?
"""
import time
import itertools
import math
start_time = time.time()
def IsPrime(pc):
    if pc < 2:
        return False
    for number in itertools.islice(itertools.count(2), int(math.sqrt(pc) - 1)):
        if not pc % number:
            return False
    return True

h = 2
co = 0
while co <+ 10001:
    if IsPrime(h):
        co += 1
        res = h
    h += 1
print(co, ' - ', res)
print("--- %s seconds ---" % (time.time() - start_time))
