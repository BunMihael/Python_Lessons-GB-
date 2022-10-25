# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) 2) с помощью дополнительных библиотек Python

import math
from unittest import result

path_read = 'test4_2.txt'
with open(path_read) as f:
    string = f.readline()

str_final = string.split(' + ')

print(str_final)

a = int(str_final[0][0])
b = int(str_final[1][0])
c = int(str_final[2][0])

print(a, b, c, sep = " ")

discr = b ** 2 - 4 * a * c
res  = ''

print('%.2f' % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    res = f" Корни уравнения Х1 = {x1}, Х2 = {x2}"
elif discr == 0:
    x = -b / (2 * a)
    res = f" Корень уравнения Х1 = {x}"
else:
    res = "Корней нет."
print(res)

with open('newres.txt', 'w', encoding='UTF-8') as ff:
    ff.write(res)