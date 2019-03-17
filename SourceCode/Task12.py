#Последовательность треугольных чисел образуется путем сложения натуральных чисел.
#К примеру, 7-ое треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
#Первые десять треугольных чисел:
#
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#Перечислим делители первых семи треугольных чисел:
#
# 1: 1
# 3: 1, 3
# 6: 1, 2, 3, 6
#10: 1, 2, 5, 10
#15: 1, 3, 5, 15
#21: 1, 3, 7, 21
#28: 1, 2, 4, 7, 14, 28
#Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.
#
#Каково первое треугольное число, у которого более пятисот делителей?

import math
import itertools
import functools

a = 0
m = 1
tn = [1]
while (a < 5):
    tn += [tn[m-1] + (m+1)]
    m +=1
    a +=1
print (tn)




def IsPrime(pc):
    if pc < 2:
        return False
    for number in itertools.islice(itertools.count(2), int(math.sqrt(pc) - 1)):
        if not pc % number:
            return False
    return True

def IsInt(n):
    return int(n) == float(n)

def CountD(en):
    lp = [2, 3]
    ls = [i for i in range(1,en+1)]
    lp.extend([i for i in range(5,en+1) if IsPrime(i)])
    n = {j:[math.log(i,j) for i in ls if IsInt(math.log(i,j))] for j in lp}
    print(n)
    return (functools.reduce(lambda x, y: x*y, [y+1 for y in n.values() if y > 0]))

print(CountD(28))

