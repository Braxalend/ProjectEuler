#1000-Значное число Фибоначчи
#Последовательность Фибоначчи определяется рекурсивным правилом:
#
#Fn = Fn−1 + Fn−2, где F1 = 1 и F2 = 1.
#Таким образом, первые 12 членов последовательности равны:
#
#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#Двенадцатый член F12 - первый член последовательности, который содержит три цифры.
#
#Каково значение первого члена последовательности Фибоначчи, содержащего 1000 цифр?
import time
start_time = time.time()


F = {1:1, 2:1, 3:2}
def fib(n):
    if n in F:
        return F[n]
    F[n] = fib(n - 1) + fib(n - 2)
    return F[n]

def FindNum(n):
    i = 0
    while True:
        i += 1
        if len(str(fib(i))) == n:
            return i
            break

print (FindNum(1000))

print("--- %s seconds ---" % (time.time() - start_time))

def Fibonachi(a,b,c):
    while True:
        a = a + b
        b = a - b
        if len(str(a)) == 1000:
            return c
            break
        c += 1
print(Fibonachi(0, 1, 1))

print("--- %s seconds ---" % (time.time() - start_time))