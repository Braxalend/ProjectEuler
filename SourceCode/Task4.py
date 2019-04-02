#-*- coding: utf-8 -*-
"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""
import functools
import time
start_time = time.time()
mn = 999 * 999
def ListNum(n):
    l = []
    while (n > 0):
        l.append(n%10)
        n //= 10
        l.reverse()
    return l
def Palindrom(m):
    while (m > 1):
        res = (ListNum(m))
        if res == res[::-1]:
            x = 999
            nres = functools.reduce(lambda t, y: 10*t + y, res, 0)
            while (x > 1):
                if (nres%x == 0 and nres/x < 1000):
                    return nres, x, nres/x
                x -= 1
        m -= 1
    return None
print (Palindrom(mn))
print("--- %s seconds ---" % (time.time() - start_time))

ent=[]
for i in range(100,1000):
    for j in range(100,1000):
        prod=i*j
        text=str(prod)
        temp=text[::-1]
        if text==temp:
            ent.append(prod)
print(max(ent))

print("--- %s seconds ---" % (time.time() - start_time))

def c():
    max = maxI = maxJ = 0
    i = 999
    j = 990
    while (i > 100):
        j = 990
        while (j > 100):
            product = i * j
            if (product > max):
                productString = str(product)
                if (productString == productString[::-1]):
                    max = product
                    maxI = i
                    maxJ = j
            j -= 11
        i -= 1
    return max, maxI, maxJ
print (c())
print("--- %s seconds ---" % (time.time() - start_time))