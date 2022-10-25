# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# from msilib.schema import Error



nums = float(input('Please, write a number and we show the sum of the numbers: '))
print(f"The sum of {nums} ", end="")
nums = abs(nums)
result = 0

if nums < 1:
    while nums != int(nums):
        nums *= 10

if nums > 0:
    while nums != 0:
        result += nums % 10
        nums //= 10

print(f"is {result}.") 

# 2й Вариант.

# nums = input('Please, write a number and we show the sum of the numbers: ')
# result = 0

# for i in nums:
#     if i.isdigit():
#         result += int(i)

# print(result)

# 3й вариант

# users_num = input('Укажите вещественное число: ')

# nums_sum = 0

# for num in users_num:
#     if num.isdigit(): nums_sum += int(num)

# print(nums_sum)

# 4й вариант

# def float_completed_integer(real_number: float) -> int:
#     magnitude = int(1)
#     temp = float(real_number)
#     while not temp.is_integer():
#         magnitude *= 10
#         temp = real_number * magnitude
#     return int(temp)

# def get_digit_sum(any_number):
#     no_point_number = float_to_completed_integer(any_number)
#     no_point_number = abs(no_point_number)
#     sum = 0
#     while no_point_number > 0:
#         sum += no_point_number % 10
#         no_point_number //= 10
#     return sum

# num = float(input("Please, write a number and we show the sum of the numbers: "))
# print(get_digit_sum(num))