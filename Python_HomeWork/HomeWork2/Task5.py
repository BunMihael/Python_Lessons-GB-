# Реализуйте алгоритм перемешивания списка.
from random import randint


def generator(some_num):
    x = []
    for i in range(0, some_num):
        x.append(randint(1, 20))
    return x



def mix(set_of_num, length):
    for i in range(length-1):
        set_of_num[i], set_of_num[length - 1 - i] = set_of_num[length - 1 - i], set_of_num[i]
    return set_of_num


length = int(input('Please, write a length of numbers you want: '))
list = generator(length)
print(list)
some = mix(list, length)
print(some)
