# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов
# списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_odd_positions(lst):
    result = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            result += lst[i]
    print(f"Сумма равна: {result}")

your_list = [2, 3, 5, 9, 3]
sum_odd_positions(your_list)
your_list = list(map(int, input("Please, enter the numbers separated by the space:\n").split()))
sum_odd_positions(your_list)

# from random import randint

# my_list = [randint(10, 100) for i in range(randint(5, 10))]
# print(my_list)
# sum_digit = 0

# for el in range(1, len(my_list), 2):
#     sum_digit += my_list[el]

# users_nums = [
#     45, # 0
#     67, # 1
#     43, # 2
#     78, # 3
#     3,  # 4
#     5,  # 5
# ]

# print(f'Sum => {sum(users_nums[1::2])}')