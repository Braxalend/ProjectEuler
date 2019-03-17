#Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
#Найдите сумму всех простых чисел меньше двух миллионов.

import itertools
import math
import time

start_time = time.time()

def IsPrime(pc):
    if pc < 2:
        return False
    for number in itertools.islice(itertools.count(2), int(math.sqrt(pc) - 1)):
        if not pc % number:
            return False
    return True

res = sum([i for i in range(1,2000001) if IsPrime(i)])
print (res)

print("--- %s seconds ---" % (time.time() - start_time))

#сито эратосфена - очень медленно для больших чисел
#def IsPrimeList(pc):
#    e = []
#    e = list(range(pc))
#    e[1] = 0
#    for i in e[2:]:
#        for j in range(i + i, len(e), i):
#            e[j] = 0
#    triger = True
#    while triger:
#        try:
#            e.remove(0)
#        except ValueError:
#            triger = False
#    return e
#print(sum(IsPrimeList(10)))
#print("--- %s seconds ---" % (time.time() - start_time))

def prime_sum(n):
    if n < 2: return 0
    if n == 2: return 2
    if n % 2 == 0: n += 1
    primes = [True] * n
    primes[0], primes[1] = [None] * 2
    sum = 0
    for ind, val in enumerate(primes):
        if val is True and ind > n ** 0.5 + 1:
            sum += ind
        elif val is True:
            primes[ind * 2::ind] = [False] * (((n - 1) // ind) - 1)
            sum += ind
    return sum


start = time.time()
sum = prime_sum(2000000)
delta = (time.time() - start)

print ("found %s in %s seconds" % (sum, delta))