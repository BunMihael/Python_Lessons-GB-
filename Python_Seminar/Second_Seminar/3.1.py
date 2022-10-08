# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

str1 = str(input('Введите первую строку: '))
str2 = str(input('Введите вторую строку: '))

score = 0
for i in range(len(str2) + 1):
    l = len(str1) + i
    if str1 == str2[i: l]:
        score += 1
print(score)

# textFirst = input('Введите первую строку: ')
# textSecond = input('Введите первую строку: ')
#
# string = ''
# subString = ''
#
# if len(textFirst) > len(textSecond):
#     string = textFirst
#     subString = textSecond
# else:
#     string = textSecond
#     subString = textFirst
#
# print(string.count(subString))

# count = 0
# counter = 0
#
# for i in range(len(string) - len(subString)+1):
#     if string[i] == subString[0]:
#         counterIn = 0
#         for k in range(len(subString)):
#             if subString[0+k] == string[i+k]:
#                 counterIn += 1
#         if counterIn == len(subString):
#             counter += 1
#
# print(f'Counter = {counter}')
