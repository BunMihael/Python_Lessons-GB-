# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

from time import time
print(f'Random num from 0 to 99 = {int(time() % 1 * 100)}')

# x(n + 1) = (a * x (n) + b) % m
m = 100
b = 3
a = 2
x = 1
c = 50

list = []

for i in range (c):
    x = (a * x + b) % m
    list.append(x)

print(list)