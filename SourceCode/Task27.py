from math import sqrt

def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n%2==0 or n%3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f*f < n:
        if n%f == 0 or n%(f+2) == 0: return False
        f+= 6
    return True

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

l = 1000
nmax = 0
for b in prime_sieve(l+1):
    for a in range(-b+2, 0, 2):
        n = 1
        while is_prime(n*n + a*n + b): n+= 1
        if n>nmax: nmax, p = n, (a,b)

print ('a * b = {0} * {1} = {2}').format(p[0], p[1], p[0]*p[1])


