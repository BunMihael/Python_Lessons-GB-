# Задайте список из N элементов, заполненных числами из промежутка
# [-N, N]. Найдите произведение элементов на указанных позициях.
# Найдите произведение элементов списка в указанном диапазоне индексов.
# Примечание: Границы диапазона вводятся пользователем, надо корректно учесть, 
# что они могут быть некорректными: больше длины списка, 
# меньше нуля, первый больше второго и т.п.

import functools
from operator import pos
from random import randint

length = int(input('Please, write a length of numbers you want: '))

list = []
for i in range(length):
    list.append(randint(-length,length))
print(list)

first_pos = int(input('Enter a first position: ')) - 1
second_pos = int(input('Enter a second position: ')) - 1

if first_pos > length and second_pos > length:
    print(f"Error. Wrong positions.")
elif first_pos <= length and second_pos > length:
    print(f"Error. Second position is more than length.")
    multiply = list[first_pos - 1]
    print(multiply)
elif first_pos > length and second_pos <= length:
    print(f"Error. first position is more than length.")
    multiply = list[second_pos - 1]
    print(multiply)
elif first_pos <= length and second_pos <= length:
    after_slice = slice(first_pos, second_pos + 1)
    result = functools.reduce(lambda a, b: a*b, list[after_slice]) 
    print(f'The product of numbers from the list is: {result}')
    
    # multiply = list[firstPos] * list[secondPos]
    # print(multiply)



# length = int(input('Please, write a length of numbers you want: '))
# with open('file.txt','r', encoding='utf-8') as f:
#     read = f.readlines()

# def generate(length):
#     list = []
#     for i in range(length):
#         list.append(randint(-length,length+1))

# def open_file(file):
#     position = []
#     for line in file:
#         position.append(line)

# def product_of_elements(length, read):
#     firstPos = int(read[0])
#     secondPos = int(read[1])
#     if firstPos > length and secondPos > length:
#         print(f"Значение позиций из файла больше длинны списка")
#     elif firstPos <= length and secondPos > length:
#         print(f"Значение второго числа больше длинны списка")
#         multy = list[firstPos - 1]
#         print(multy)
#     elif firstPos > length and secondPos <= length:
#         print(f"Значение первого числа больше длинны списка")
#         multy = list[secondPos - 1]
#         print(multy)
#     elif firstPos <= length and secondPos <= length: 
#         multy = list[firstPos - 1] * list[secondPos - 1]
#         print(multy)


# length = int(input('Please, write a length of numbers you want: '))
# with open('file.txt','r', encoding='utf-8') as f:
#     read = f.readlines()
# list = generate(length)
# print(list)
# file = open_file(read)
# print(file)
# rest = product_of_elements(list,file)
# print(rest)

