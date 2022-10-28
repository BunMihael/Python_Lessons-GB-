# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов многочлена 
# и записать в файл многочлен степени k.
# Коэффициенты должны быть случайными числами в диапазоне от 1 до 100
# Пример:
# - k=2 => 6*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

from random import randint


def coefficients_of_polynomial():
    coef = {}
    degree = int(input('Please enter the maximum degree: '))
    for i in range(degree, -1, -1):
        coef[i] = randint(1,100)
    print(coef)

coefficients_of_polynomial()