# Напишите программу, которая принимает на вход координаты точки
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


def quarters(x, y):
    if x == 0 and y == 0:
        print('x and y should not be equal zero.')
    elif x > 0 and y >0:
        print('I')
    elif x < 0 and y > 0:
        print('II')
    elif x < 0 and y < 0:
        print('III')
    else:
        print('IV')

print('Please, enter сoordinates x, y and we will tell you the number of the quarter in which they are located.')
x = int(input(' Write a number for x: '))
y = int(input(' Write a number for y: '))

quarters(x, y)