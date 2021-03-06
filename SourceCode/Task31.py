# -*- coding: utf-8 -*-
"""
В Англии валютой являются фунты стерлингов £ и пенсы p, и в обращении есть восемь монет:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) и £2 (200p).
"£2 возможно составить следующим образом:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
Сколькими разными способами можно составить £2, используя любое количество монет?

https://blog.dreamshire.com/project/dyn_prog.pdf
"""

f2 = 200
c = [1, 2, 5, 10, 20, 50, 100, 200]
w = [1] + [0]*f2
for p in c:
    for i in range(p, f2+1):
        w[i] += w[i-p]
print (w[f2])


