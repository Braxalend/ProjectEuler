#-*- coding: utf-8 -*-
#Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
#a2 + b2 = c2
#Например, 32 + 42 = 9 + 16 = 25 = 52.
#Существует только одна тройка Пифагора, для которой a + b + c = 1000.
#Найдите произведение abc.
###########
##a = 2mn, b = m2 − n2, c = m2 + n2 , m > n
import functools

def MultList(l):
    return functools.reduce(lambda x, y: x * y, l)

def SysFun(mr,st):
    i = st
    f = []
    while True:
        for n in range(i-(i-1),i):
            for m in range(i-(i-2),i+1):
                if m > n:
                    f = [2*n*m,(m**2)-(n**2),(m**2)+(n**2)]
                    if sum(f) == mr:
                        print (f)
                        return MultList(f)
        i += st
print(SysFun(1000,100))