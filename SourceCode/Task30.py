#Удивительно, но существует только три числа, которые могут быть записаны в виде суммы четвертых степеней их цифр:
#
#1634 = 14 + 64 + 34 + 44
#8208 = 84 + 24 + 04 + 84
#9474 = 94 + 44 + 74 + 44
#1 = 14 не считается, так как это - не сумма.
#
#Сумма этих чисел равна 1634 + 8208 + 9474 = 19316.
#
#Найдите сумму всех чисел, которые могут быть записаны в виде суммы пятых степеней их цифр.
import itertools

p = list(itertools.product('0123456789', '0123456789', repeat=3))
res = []
for i in p:
    r = [int(item) for item in i]
    if (int(''.join(map(str, r)))) == sum(list(map(lambda a: a ** 5, r))):
        res += [sum(list(map(lambda a: a ** 5, r)))]
print (sum(res)-1)




total_sum = 0
for n in range(2, 1000000):
    if sum([int(s)**5 for s in str(n)]) == n:
        total_sum += n
print('Total sum: %d' % total_sum)