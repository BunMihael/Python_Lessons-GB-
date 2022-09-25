# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:* 
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

import numbers


N = int(input("Введите размер списка: "))
spam = list(range(-N, N+1))
print(spam)

# def list_of_numbers(x):
#     list = []
#     for i in range(-x, x + 1):
#         list.append(i)
#     return list

# number = int(input('Write a number: '))
# x = list_of_numbers(number)
# print(x)