# Наишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что ее нет.
# Пример:
# Список: ["qwe","asd","zxv","qwe","ertqwe"] ищем: "qwe" ответ: 3
# Список: ["123","234",123,"567"] ищем: "123" ответ: -1

from itertools import count
from turtle import position


lst = ["123","234",123,"567"]

x = "123"
index = 0

for i in range(len(lst)):
    if lst(i) == x:
        index += 1
    if index == 2:
        print(i)
        break
else:
    if index == 0:
        print('Нет вхождения.')
    else:
        print('Нет второго вхождения.')

# lst = ["123","234",123,"567"]

# def find_num(lst, some_num, find_position):
#     pos_count = 0
#     find_pos = 0
#     for i in lst:
#         find_pos += 1
#         while pos_count != find_position:
#             if some_num == i:
#                 pos_count += 1
#     if pos_count == find_position:
#         print(f'Ищем: {some_num}. Ответ: {find_pos - pos_count}.')
#     else:
#         print(f'ищем: {some_num} ответ: -1')

# some_num = str(input('Please, write a number you want to find in list: '))
# find_position = int(input('Please, write a number of position you want to find in list: '))
# print(find_num(lst,some_num,find_position))
