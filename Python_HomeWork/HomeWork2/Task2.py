# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from re import I


N = int(input('Write a number N for to find the product of numbers from 1 to N: '))
product_of_numbers = 1
for i in range(1, N + 1):
    product_of_numbers *= i
    print(f'{product_of_numbers}', end=" ")
