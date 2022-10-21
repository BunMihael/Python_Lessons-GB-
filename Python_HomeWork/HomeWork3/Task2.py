# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import random, randint, randrange

def generator(some_num):
    x = []
    for i in range(0, some_num):
        x.append(randint(1, 9))
    return x


def pairsOfNums(nums, amount):
    x = []
    for i in range(0,  int(amount/2)):
        x.append(nums[i] * nums[amount - 1 - i])
    return x


num_of_numbers = int(input('Please, write how many numbers do you want to generate:'))
result = generator(num_of_numbers)
print(result)
print(pairsOfNums(result, num_of_numbers))
