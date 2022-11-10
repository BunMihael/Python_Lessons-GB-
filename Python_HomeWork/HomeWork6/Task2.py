# list comprehension

# 5. Реализуйте алгоритм перемешивания элементов списка. Без функции shuffle
#  из модуля random, другие методы использовать можно.

from random import  sample


# def generator(some_num):
#     x = []
#     for i in range(0, some_num):
#         x.append(randint(1, 20))
#     return x


import random

res = [random.randrange(1, 50, 1) for i in range(7)]
print(res)
result = sample(res, len(res))
print(result)
    

