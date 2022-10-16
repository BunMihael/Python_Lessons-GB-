# 5. Реализуйте алгоритм перемешивания элементов списка. Без функции shuffle
#  из модуля random, другие методы использовать можно.

from random import randint, sample


def generator(some_num):
    x = []
    for i in range(0, some_num):
        x.append(randint(1, 20))
    return x



def mix(set_of_num, length):
    result = sample(set_of_num, length)
    print(result)
    
    # for i in range(length-1):
    #     set_of_num[i], set_of_num[length - 1 - i] = set_of_num[length - 1 - i], set_of_num[i]
    # return set_of_num


length = int(input('Please, write a length of numbers you want: '))
list = generator(length)
print(list)
mix(list, length)

