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