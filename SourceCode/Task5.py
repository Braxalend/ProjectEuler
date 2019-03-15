#2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#Какое самое маленькое число делится нацело на все числа от 1 до 20?
import math
import time
import itertools
start_time = time.time()
def IsPrime(pc):
    if pc < 2:
        return False
    for number in itertools.islice(itertools.count(2), int(math.sqrt(pc) - 1)):
        if not pc % number:
            return False
    return True

l = [i for i in range(5,21) if IsPrime(i)]

print (l)
print("--- %s seconds ---" % (time.time() - start_time))