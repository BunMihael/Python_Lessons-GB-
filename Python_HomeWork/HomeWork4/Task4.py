# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов многочлена
# и записать в файл многочлен степени k.
# Коэффициенты должны быть случайными числами в диапазоне от -100 до 100
# 5. (Усложненное). Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример:
# - k=2 => 6*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

# from random import randint


# def coefficients_of_polynomial():
#     coef = {}
#     degree = int(input('Please enter the maximum degree: '))
#     for i in range(degree, -1, -1):
#         coef[i] = randint(-100, 100)
#     return coef


# def create_a_polynomial(coef: dict):
#     equation = ''
#     first = True
#     for i in coef.items():
#         if first:
#             first = False
#             if i[1] < 0:
#                 equation += ' -' + str(abs(i[1])) + 'x^' + str(i[0])
#             elif i[1] > 0:
#                 equation += str(abs(i[1])) + 'x^' + str(i[0])
#         else:
#             if i[1] < 0:
#                 equation += ' - ' + str(abs(i[1])) + 'x^' + str(i[0])
#             elif i[1] > 0:
#                 equation += ' + ' + str(abs(i[1])) + 'x^' + str(i[0])

#     return equation + ' = 0'


# def parse_equation(equation: str):
#     equation = equation.replace(' + ', ' +').replace(' - ', ' -')
#     equation = equation.split()
#     equation = equation[:-2]

#     dictEquation = {}
#     for i in range(len(equation)):
#         equation[i] = equation[i].replace('+', '').split('x^')
#         dictEquation[int(equation[i][1])] = int(equation[i][0])
#     return dictEquation


# equation1 = create_a_polynomial(coefficients_of_polynomial())
# equation2 = create_a_polynomial(coefficients_of_polynomial())

# with open("equation1.txt", "w") as file:
#     file.write(equation1)

# with open("equation2.txt", "w") as file:
#     file.write(equation2)


# file1 = []
# with open("equation1", 'r') as file:
#     file1 = file.readline()
# file2 = []
# with open("equation2", 'r') as file:
#     file2 = file.readline()


# parEq1 = parse_equation(file1)
# print(f' this {parEq1}')
# parEq2 = parse_equation(file2)
# print(f' this 2 {parEq2}')


# def result_equation():
#     result = {}
#     for i in range(max(len(parEq1), len(parEq2)), -1, -1):
#         first = parEq1.get(i)
#         second = parEq2.get(i)
#         if first != None or second != None:
#             result[i] = (first if first != None else 0) + \
#                 (second if second != None else 0)
#     return result


# def print_equation(equation: str):
#     print(equation.replace(" 1x", "x").replace("x^1", 'x').replace("x^0", ''))


# print_equation(create_a_polynomial(parEq1))
# print_equation(create_a_polynomial(parEq2))

# with open("Finish.txt", "w") as file:
#     file.write(create_a_polynomial(result_equation()))

# print_equation(create_a_polynomial(result_equation()))


# with open("Finish", "w") as file:
#     file.write(str(finish))


from random import randint


def create_coeffs(num: int) -> list:
    return [randint(1, 100) for _ in range(num)]


def create_str(list_coeff: list) -> str:
    length = len(list_coeff)
    lst_str = [f"{el}*x^{length - idx - 1}" for idx,
               el in enumerate(list_coeff)]
    return " + ".join(lst_str)


def write_to_file(polynom_string, filename):
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(polynom_string)
