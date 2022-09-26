# Напишите программу, которая принимает на вход цифру, обозначающую 
# день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = float(input(' Write a number indicating a day of the week and:'))

if day != int(day) or day > 7:
    print("There is no such day.")
elif day < 6:
    print("It's a weekday.")
else:
    print("It's a weekend.")