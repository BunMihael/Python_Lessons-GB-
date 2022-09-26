# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = int(input('Please write x1:'))
y1 = int(input('Please write y1:'))
x2 = int(input('Please write x2:'))
y2 = int(input('Please write y2:'))

print(f'Distance between two points A({x1,y1}) and B({x2,y2}) in 2D space = {round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (0.5), 3)}')

