#-*- coding: utf-8 -*-
#Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
import time
start_time = time.time()

F = {1:1, 2:2}
def fib(n):
    if n in F:
        return F[n]
    F[n] = fib(n - 1) + fib(n - 2)
    return F[n]
summa = 0
i = 0
while True:
    i += 1
    if fib(i) > 4000000:
        break
    if fib(i)%2 == 0:
        summa += fib(i)
print (summa)
print("--- %s seconds ---" % (time.time() - start_time))

def fibonachi(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fibonachi(n-1)+fibonachi(n-2)
summa = 0
i = 0
while True:
    i += 1
    if fibonachi(i) > 4000000:
        break
    if fibonachi(i)%2 == 0:
        summa += fibonachi(i)
print (summa)
print("--- %s seconds ---" % (time.time() - start_time))


