# Напишите прграмму, которая на вход принимает 5 чисел и находит 
# максимальное из них.

# list = []

# for i in range(0,5):
#     list.append(int(input('Введите число: ')))
# print(f"Max number is: {max(list)}")

# list = []

# for i in range(0,5):
#     list.append(int(input('Введите число: ')))

# max = list[0]

# for i in list:
#     if i > max:
#         max = i

# print(max)

from re import A


def array(m):
    x = []
    for i in range(m):
        a = int(input(f'Write x{i + 1}: '))
        x.append(a)
    return x

def max_el(array):
    maxim = 0

    for i in range(len(array)):
        if array[i] > array[maxim]:
            maxim = i
    return array[maxim]

l = int(input(' Write number of elements: '))
new_array = array(l)
maxim = max_el(new_array)
print(f'Max element is: {maxim}')