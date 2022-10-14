# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*    
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# 1й вариант

# num = float(input(' Write number: '))

# number = int(num * 10 % 10)

# if num % 1 == 0:
#     print('No')
# else:
#     print(number)

# .....

# num = float(input('Write a number: '))

# if num == int(num):
#     print('Integer number.')
# else:
#     print('Fractional number.')

# 3й вариант

num = "6,78"
lst = num.split(",")
print(lst[1][0])


# 4й вариант

# num = float(input('Ввидите число '))
# number_dec = str(num-int(num))[2:3]
# num_dec = int(number_dec)
# if num_dec == 0:
# print('нет')
# else:
# print(num_dec)

# num[num.find(",") + 1]
# print(num)
