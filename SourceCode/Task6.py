#-*- coding: utf-8 -*-
#Сумма квадратов первых десяти натуральных чисел равна
#1**2 + 2**2 + ... + 10**2 = 385
#Квадрат суммы первых десяти натуральных чисел равен
#(1 + 2 + ... + 10)**2 = 55**2 = 3025
#Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.
#Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
print (sum(range(1,101))**2 - sum([i**2 for i in range(1,101)]))
