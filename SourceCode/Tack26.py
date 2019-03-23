import math


def BackDiv(d):
    e = 1
    i = 0
    c = []
    while i < d-1:
        if e/d < 1:
            c += [e%d]
            e = (e*10)%d
            i += 1
    return c

for i in range(1,1001):
    if len(BackDiv(i)) == len(set(BackDiv(i))):
        r = i
print (r)
        




            
                

        
     