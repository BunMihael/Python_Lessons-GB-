# list comprehension

# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# from re import I


# n = int(input('Write a number n for to find the product of numbers from 1 to n: '))
# product_of_numbers = 1
# for i in range(1, n + 1):
#     product_of_numbers *= i
#     print(f'{product_of_numbers}', end=" ")


n = int(input('Введите число: '))
f = lambda x: ((x == 1) and 1) or x * f(x -1)
list_of_f = list( f(i) for i in range(1, n +1))
print(list_of_f)
