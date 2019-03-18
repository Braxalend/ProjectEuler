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

def IsSquare(k):
    x=math.ceil((math.sqrt(k)))
    if x*x==k:
        return True
    else:
        return False

def MaxTr(l):
    x=3
    k=2
    while (k<=l):
        k=2
        res=sum(list(range(1,x+1)))
        for i in range(2,math.ceil(math.sqrt(res))):
            if res%i==0:
                k+=2
        if IsSquare(res):
                k-=1
        x+=1
    return res

print(MaxTr(500))


def listDivisors(x):
    divisors = []
    for i in range(1,int(math.sqrt(x))+1):
        if x%i == 0:
            divisors.append(i)
    if math.sqrt(x) % 1 == 0:
        return (len(divisors)*2)-1
    return len(divisors)*2

counter = 2
ans = 1
while listDivisors(ans) <= 500:
    ans += counter
    counter += 1

print(ans)

